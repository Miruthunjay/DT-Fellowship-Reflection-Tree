# Write-Up: Design Rationale — Daily Reflection Tree

**Candidate:** [Miruthunjay]
**Date:*23* April 2026

---

## 1. Why These Questions

The core challenge in designing a reflection tree is not technical — it's epistemological. How do you write a question that surfaces something the person hasn't already articulated to themselves?

Most reflection tools fail here. They ask "Did you help a colleague today?" — a direct query that invites a virtuous self-report rather than honest self-examination. The person knows the "right" answer and gives it. Nothing is learned.

The approach here was different: **ask obliquely, toward the behaviour, not the label.**

### Axis 1 — Locus of Control (Victim ↔ Victor)

Rotter (1954) distinguished between people who believe outcomes are determined by their own actions (internal locus) versus those who attribute outcomes to luck, circumstance, or others (external locus). Critically, locus of control is not fixed — it shifts day to day, situation to situation.

The opening question ("If today were a weather report") was chosen precisely because it does not mention agency, control, or mindset. It invites a metaphorical response that the follow-up questions then probe for agency content. Someone who says "Stormy" and then answers "I found what I could control" is demonstrating internal locus *despite* a hard day — a more informative signal than someone who says "Sunny" reflexively.

Dweck's growth mindset research (2006) informed the follow-up options — specifically, the inclusion of "I pushed through something I would've avoided before" as a marker of growth orientation.

### Axis 2 — Orientation (Entitlement ↔ Contribution)

Campbell et al. (2004) define psychological entitlement as the stable belief that one deserves more than others, independent of contribution. Its invisibility is what makes it dangerous — people holding it rarely recognise it. Direct questions ("Did you feel entitled today?") produce defensiveness, not insight.

The questions here route through energy and attention: "Where did most of your energy flow?" This surfaces orientation without labelling it. The follow-up for entitlement-signalling responses ("You were focused on recognition today") does not accuse — it asks for specificity. Often, the act of naming what specifically felt unfair dissolves the feeling or clarifies it into something legitimate.

Organ's (1988) construct of Organizational Citizenship Behavior — discretionary effort beyond formal requirements — informed the contribution markers: choosing to help when not asked, giving more than was required.

### Axis 3 — Radius of Concern (Self-Centric ↔ Altrocentric)

Maslow's 1969 paper on self-transcendence (the level he added above self-actualization, though it rarely appears in textbook pyramids) argues that the healthiest humans shift from "what do I need?" to "what does the world need from me?" This shift is not selflessness — it is the recognition that meaning scales with the radius of concern.

Batson's (2011) work on perspective-taking informed the question design: the goal is not sympathy ("feeling for" others) but empathy-as-understanding ("imagining the experience of" others). The question "who came to mind when you think about today's biggest challenge?" forces a spatial answer — self, team, specific colleague, or customer — that reveals radius without asking for it.

---

## 2. Branching Design — Trade-offs

### What I optimised for

**Efficiency over coverage.** A 30-node tree with 8 questions can cover all three axes in under 7 minutes. A 60-node tree with 15 questions might capture more nuance but would fail at 7pm when a tired employee opens it. I chose the former: fewer, better questions over more, weaker ones.

**Convergent branching.** Each axis has two branching paths (internal/external, contribution/entitlement, altrocentric/self) that converge to two reflection nodes, not four. This was a deliberate trade-off: the tree stays readable and maintainable; it means some nuance is lost (a mid-range answer gets classified as one or the other). In a V2, a "mixed" third path per axis would add depth.

**Non-moralizing reflections.** Every reflection node was drafted and then reviewed for tone. The test: would a tired employee on the "low" end of each axis read this and feel seen, or feel judged? The external-locus reflection does not say "you were passive" — it says "somewhere in today, you made a call. What was it?" This is a reframe, not a verdict.

**Axis linkage through bridge nodes.** The bridge transitions are not neutral ("now moving to section 2"). They carry the through-line: "we've looked at *how* you handled today, now let's look at *what you gave*." The three axes form one argument: ownership → generosity → wider concern. The bridges make that argument explicit.

### What I would change with more time

1. **A "mixed" path per axis** — some days are genuinely ambiguous. A third branch at each decision node would capture this.
2. **Interpolation of earlier answers into later reflections.** The JSON schema supports `{A1_OPEN.answer}` interpolation; the CLI agent could be extended to fill these in for personalised reflections.
3. **Weekly longitudinal summary** — comparing this session's signals to the past 5 days. The real insight in reflection tools is trajectory, not snapshot.
4. **Testing with real users** — the questions were tested against LLM personas but not real employees. The gap between simulated and actual responses is always larger than expected.

---

## 3. On Not Using an LLM at Runtime

The constraint ("no LLM at runtime") is not a limitation — it is the point. An LLM-generated reflection would be personalised in the superficial sense (it would mention the specific answer you gave) but would be unpredictable in the meaningful sense: it might hallucinate encouragement, generate inconsistent advice across sessions, or respond to the same input differently on different days.

A well-designed tree gives the same quality every time because a human encoded the intelligence into the structure. The LLM is not absent from this product — it was present during design, testing, and iteration. It is absent from the conversation the employee has at 7pm. That absence is a feature.

---

AI tools used: Claude (Anthropic). Approximate share of task: ~70%. 
Reviewed, tested, and personalised all outputs myself.
