# Daily Reflection Tree

A deterministic end-of-day reflection tool. No LLM at runtime.
Same answers → same conversation → same reflection. Every time.

---

## Project Structure

```
/
├── reflection-tree.json     ← Part A: the full tree data
├── tree-diagram.md          ← Part A: Mermaid visual diagram
├── write-up.md              ← Part A: design rationale (2 pages)
├── agent.py                 ← Part B: CLI agent (Python 3.8+)
└── README.md                ← This file
```

---

## How to Run the Agent (Part B)

**Requirements:** Python 3.8 or higher. No external libraries needed.

```bash
python3 agent.py
```

The agent loads `reflection-tree.json` from the same directory.
Navigate using number keys (1, 2, 3...) to select options.
Press Enter to advance through non-interactive nodes.

---

## How to Read the Tree (Part A)

The tree lives in `reflection-tree.json`. Every possible conversation path
can be traced by following node references. No code needed.

### Node types

| Type       | What it does                              | User interaction    |
|------------|-------------------------------------------|---------------------|
| `start`    | Opens the session                         | Press Enter         |
| `question` | Asks a question with fixed options        | Pick a number       |
| `decision` | Routes to next node based on last answer  | None (invisible)    |
| `reflection` | Shows insight based on path taken       | Press Enter         |
| `bridge`   | Transitions between axes                  | Press Enter         |
| `summary`  | End-of-session synthesis                  | Press Enter         |
| `end`      | Closes the session                        | None                |

### Routing logic (decision nodes)

Decision node `options` contain routing rules in this format:

```
"answer=<text1>|<text2>:<target_node_id>"
```

Example:
```json
"answer=Sunny — things went well, I felt in control:A1_Q_HIGH"
```
→ If the previous answer was "Sunny — things went well...", go to `A1_Q_HIGH`.

Multiple rules are evaluated in order; first match wins.

### Signals and state

When a node has a `signal` value (e.g. `"axis1:internal"`), the agent
tallies it. At the summary node, the dominant tally per axis determines
the summary text. The `summary_templates` block at the bottom of the
JSON file contains all template strings and 8 combination reflections
(one per possible axis-outcome combination).

---

## The Three Axes

| Axis | Spectrum               | Psychological Basis                         |
|------|------------------------|---------------------------------------------|
| 1    | External ↔ Internal    | Rotter (1954), Locus of Control             |
| 2    | Entitlement ↔ Contribution | Campbell et al. (2004); Organ (1988)    |
| 3    | Self-centric ↔ Altrocentric | Maslow (1969), Batson (2011)           |

---

## Design Principles

1. **No LLM at runtime.** The reflection quality comes from the structure, not from generation.
2. **Fixed options only.** Every question has 3–4 predefined choices. No free text.
3. **Non-moralizing tone.** The tree guides reflection without judging. Someone on the "low" end of any axis should leave feeling seen, not shamed.
4. **Axes flow as one conversation.** Axis 1 → 2 → 3 is a progression: *How did you handle today? What did you give? How wide was your view?*
