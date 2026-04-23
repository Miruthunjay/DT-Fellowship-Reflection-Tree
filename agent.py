#!/usr/bin/env python3
"""
Daily Reflection Tree — CLI Agent
Walks the reflection-tree.json deterministically.
No LLM calls at runtime. Same answers = same path, every time.
"""

import json
import sys
import textwrap
from pathlib import Path


# ── Helpers ────────────────────────────────────────────────────────────────

def wrap(text: str, width: int = 72) -> str:
    """Wrap text for clean terminal output."""
    lines = text.split("\n")
    wrapped = []
    for line in lines:
        if line.strip() == "":
            wrapped.append("")
        else:
            wrapped.extend(textwrap.wrap(line, width=width))
    return "\n".join(wrapped)


def hr(char: str = "─", width: int = 72) -> str:
    return char * width


def clear_line():
    print()


def print_header():
    print("\n" + hr("═"))
    print("  🌿  Daily Reflection Tree")
    print(hr("═"))
    print()


def prompt_continue():
    input("  [ Press Enter to continue ] ")
    print()


# ── State ──────────────────────────────────────────────────────────────────

class SessionState:
    def __init__(self):
        self.answers: dict[str, str] = {}          # node_id → answer text
        self.signals: dict[str, int] = {}          # "axis1:internal" → count
        self.path: list[str] = []                  # ordered node IDs visited

    def record_answer(self, node_id: str, answer: str):
        self.answers[node_id] = answer

    def record_signal(self, signal: str):
        if signal:
            self.signals[signal] = self.signals.get(signal, 0) + 1
            self.path.append(signal)

    def dominant(self, axis: str, poles: list[str]) -> str:
        """Return the dominant pole for an axis."""
        counts = {p: self.signals.get(f"{axis}:{p}", 0) for p in poles}
        return max(counts, key=lambda p: counts[p])

    def build_summary(self, templates: dict) -> str:
        axis1 = self.dominant("axis1", ["internal", "external"])
        axis2 = self.dominant("axis2", ["contribution", "entitlement"])
        axis3 = self.dominant("axis3", ["altrocentric", "self"])

        combo_key = f"{axis1}_{axis2}_{axis3}"
        combo_text = templates["combinations"].get(
            combo_key,
            "Every day is its own data point. Carry what's useful; leave the rest."
        )

        axis1_label = templates["axis1"][axis1]
        axis2_label = templates["axis2"][axis2]
        axis3_label = templates["axis3"][axis3]

        return axis1_label, axis2_label, axis3_label, combo_text


# ── Tree Loader ────────────────────────────────────────────────────────────

def load_tree(path: str) -> tuple[dict, dict, dict]:
    with open(path) as f:
        data = json.load(f)

    nodes_by_id = {n["id"]: n for n in data["nodes"]}
    templates = data.get("summary_templates", {})
    return nodes_by_id, templates


# ── Node Renderers ─────────────────────────────────────────────────────────

def render_start(node: dict, state: SessionState) -> str:
    print(hr())
    print()
    print(wrap(node["text"]))
    print()
    prompt_continue()
    return node["target"]


def render_question(node: dict, state: SessionState) -> tuple[str, str]:
    """Render a question, return (next_node_id, chosen_answer)."""
    print(hr("·"))
    print()
    print(wrap(node["text"]))
    print()
    options = node["options"]
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    print()

    while True:
        raw = input("  Your choice (number): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            chosen = options[int(raw) - 1]
            print()
            return chosen
        print(f"  Please enter a number between 1 and {len(options)}.")


def render_decision(node: dict, state: SessionState, last_answer: str) -> str:
    """Evaluate routing rules and return next node id."""
    for rule in node["options"]:
        # Format: "answer=<text1>|<text2>:<target_id>"
        condition, target = rule.rsplit(":", 1)
        _, values_str = condition.split("=", 1)
        values = [v.strip() for v in values_str.split("|")]
        if last_answer in values:
            return target.strip()

    # Fallback: return first target (should not happen with well-formed tree)
    _, fallback = node["options"][0].rsplit(":", 1)
    return fallback.strip()


def render_reflection(node: dict, state: SessionState) -> str:
    print(hr("·"))
    print()
    print("  ✦  Reflection")
    print()
    print(wrap(node["text"]))
    print()
    prompt_continue()
    return node.get("target") or "__FOLLOW_CHILDREN__"


def render_bridge(node: dict, state: SessionState) -> str:
    print()
    print(f"  ── {wrap(node['text'])} ──")
    print()
    prompt_continue()
    return node["target"]


def render_summary(node: dict, state: SessionState, templates: dict) -> str:
    axis1_label, axis2_label, axis3_label, combo_text = state.build_summary(templates)

    raw_text = node["text"]
    filled = (
        raw_text
        .replace("{axis1_dominant}", axis1_label)
        .replace("{axis2_dominant}", axis2_label)
        .replace("{axis3_dominant}", axis3_label)
        .replace("{summary_reflection}", combo_text)
    )

    print(hr("═"))
    print()
    print("  ◈  Today's Reflection Summary")
    print()
    print(wrap(filled))
    print()
    prompt_continue()
    return node.get("target")


def render_end(node: dict, state: SessionState) -> None:
    print(hr("═"))
    print()
    print(wrap(node["text"]))
    print()
    print(hr("═"))
    print()


# ── Walker ─────────────────────────────────────────────────────────────────

def walk_tree(nodes: dict, templates: dict, state: SessionState):
    current_id = "START"
    last_answer = None

    while current_id:
        node = nodes.get(current_id)
        if node is None:
            print(f"[ERROR] Node '{current_id}' not found in tree.")
            break

        state.path.append(current_id)
        ntype = node["type"]

        # Record signal if present
        if node.get("signal"):
            state.record_signal(node["signal"])

        if ntype == "start":
            current_id = render_start(node, state)

        elif ntype == "question":
            answer = render_question(node, state)
            state.record_answer(current_id, answer)
            last_answer = answer

            # Record signal if present on question node
            if node.get("signal"):
                pass  # already recorded above

            # Move to children: look for a decision node that lists this as parent
            # Find children of this node
            children = [n for n in nodes.values() if n.get("parentId") == current_id]
            decision_children = [n for n in children if n["type"] == "decision"]
            if decision_children:
                current_id = decision_children[0]["id"]
            elif node.get("target"):
                current_id = node["target"]
            else:
                # Follow non-decision children
                non_decision = [n for n in children if n["type"] != "decision"]
                current_id = non_decision[0]["id"] if non_decision else None

        elif ntype == "decision":
            current_id = render_decision(node, state, last_answer)

        elif ntype == "reflection":
            next_id = render_reflection(node, state)
            if next_id == "__FOLLOW_CHILDREN__":
                children = [n for n in nodes.values() if n.get("parentId") == current_id]
                current_id = children[0]["id"] if children else None
            else:
                current_id = next_id

        elif ntype == "bridge":
            current_id = render_bridge(node, state)

        elif ntype == "summary":
            current_id = render_summary(node, state, templates)

        elif ntype == "end":
            render_end(node, state)
            break

        else:
            print(f"[WARN] Unknown node type '{ntype}'. Skipping.")
            children = [n for n in nodes.values() if n.get("parentId") == current_id]
            current_id = children[0]["id"] if children else None


# ── Entry Point ────────────────────────────────────────────────────────────

def main():
    tree_path = Path(__file__).parent / "reflection-tree.json"
    if not tree_path.exists():
        print(f"Error: Could not find reflection-tree.json at {tree_path}")
        sys.exit(1)

    nodes, templates = load_tree(str(tree_path))
    state = SessionState()

    print_header()

    try:
        walk_tree(nodes, templates, state)
    except KeyboardInterrupt:
        print("\n\n  Session ended early. See you tomorrow.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
