```mermaid
flowchart TD
    START([🌿 START\nGood evening...]) --> A1_OPEN

    A1_OPEN[/❓ A1_OPEN\nIf today were a weather report.../]
    A1_OPEN -->|Sunny / Overcast / Stormy / Foggy| A1_D1

    A1_D1{Decision\nRoute by mood}
    A1_D1 -->|Sunny| A1_Q_HIGH
    A1_D1 -->|Overcast| A1_Q_MID
    A1_D1 -->|Stormy / Foggy| A1_Q_LOW

    A1_Q_HIGH[/❓ A1_Q_HIGH\nWhat made things go well?/]
    A1_Q_HIGH --> A1_D2

    A1_Q_MID[/❓ A1_Q_MID\nWhere did the heaviness come from?/]
    A1_Q_MID --> A1_D3

    A1_Q_LOW[/❓ A1_Q_LOW\nWhen things went sideways, what was your first instinct?/]
    A1_Q_LOW --> A1_D4

    A1_D2{Decision\nInternal or External?}
    A1_D2 -->|Prepared / Adapted / Pushed through| A1_R_INTERNAL
    A1_D2 -->|Circumstances lined up| A1_R_EXTERNAL

    A1_D3{Decision}
    A1_D3 -->|Own handling / Own decision| A1_R_INTERNAL
    A1_D3 -->|Others / Unclear expectations| A1_R_EXTERNAL

    A1_D4{Decision}
    A1_D4 -->|Controlled / Pushed through| A1_R_INTERNAL
    A1_D4 -->|Blame / Wait| A1_R_EXTERNAL

    A1_R_INTERNAL[💡 Reflection\n'You stayed in the driver's seat...']
    A1_R_EXTERNAL[💡 Reflection\n'Somewhere in today you made a call...']

    A1_R_INTERNAL --> BRIDGE_1_2
    A1_R_EXTERNAL --> BRIDGE_1_2

    BRIDGE_1_2[🔗 BRIDGE\nNow let's look at what you gave.]

    BRIDGE_1_2 --> A2_OPEN

    subgraph AXIS2 [AXIS 2 — Orientation]
        A2_OPEN[/❓ A2_OPEN\nWhere did most of your energy flow?/]
        A2_OPEN -->|Helping / Team need| A2_Q_CONTRIB
        A2_OPEN -->|Own work| A2_Q_SELF
        A2_OPEN -->|Recognition / Defending| A2_Q_ENTITLE

        A2_Q_CONTRIB[/❓ A2_Q_CONTRIB\nDid you choose to help, or was it expected?/]
        A2_Q_SELF[/❓ A2_Q_SELF\nHow did you feel about what you received?/]
        A2_Q_ENTITLE[/❓ A2_Q_ENTITLE\nWhat specifically felt unacknowledged?/]

        A2_Q_CONTRIB --> A2_D2
        A2_Q_SELF --> A2_D3
        A2_Q_ENTITLE --> A2_D4

        A2_D2{Decision} -->|Any choice| A2_R_CONTRIBUTION
        A2_D3{Decision} -->|Fair / Neutral / Could give more| A2_R_CONTRIBUTION
        A2_D3 -->|Underappreciated| A2_R_ENTITLEMENT
        A2_D4{Decision} -->|Credit / Standing / Support| A2_R_ENTITLEMENT
        A2_D4 -->|Actually not about that| A2_R_CONTRIBUTION

        A2_R_CONTRIBUTION[💡 Reflection\n'That discretionary effort is what teams are built on.']
        A2_R_ENTITLEMENT[💡 Reflection\n'Wanting acknowledgment is human. But was there a moment to give...?']
    end

    A2_R_CONTRIBUTION --> BRIDGE_2_3
    A2_R_ENTITLEMENT --> BRIDGE_2_3

    BRIDGE_2_3[🔗 BRIDGE\nHow wide was your view today?]

    BRIDGE_2_3 --> A3_OPEN

    subgraph AXIS3 [AXIS 3 — Radius of Concern]
        A3_OPEN[/❓ A3_OPEN\nWho came to mind for today's biggest challenge?/]
        A3_OPEN -->|Just me| A3_Q_SELF
        A3_OPEN -->|Team / Colleague / Customer| A3_Q_WIDE

        A3_Q_SELF[/❓ A3_Q_SELF\nWas there someone struggling you noticed but didn't act on?/]
        A3_Q_WIDE[/❓ A3_Q_WIDE\nDid the wider view change how you acted?/]

        A3_Q_SELF --> A3_D2
        A3_Q_WIDE --> A3_D3

        A3_D2{Decision} -->|Saw but didn't act / Unaware| A3_R_SELF
        A3_D2 -->|Checked and no one needed anything| A3_R_ALTROCENTRIC

        A3_D3{Decision} -->|Any outward orientation| A3_R_ALTROCENTRIC

        A3_R_SELF[💡 Reflection\n'Tomorrow: one deliberate look outward.']
        A3_R_ALTROCENTRIC[💡 Reflection\n'People who orient toward others report higher meaning...']
    end

    A3_R_SELF --> SUMMARY
    A3_R_ALTROCENTRIC --> SUMMARY

    SUMMARY[◈ SUMMARY\nAxis 1: {axis1}\nAxis 2: {axis2}\nAxis 3: {axis3}\n{combo_reflection}]
    SUMMARY --> END([🌙 END\nRest well. See you tomorrow.])

    style START fill:#2d4a3e,color:#fff
    style END fill:#2d4a3e,color:#fff
    style BRIDGE_1_2 fill:#4a3d2d,color:#fff
    style BRIDGE_2_3 fill:#4a3d2d,color:#fff
    style A1_R_INTERNAL fill:#1e3a5f,color:#fff
    style A1_R_EXTERNAL fill:#1e3a5f,color:#fff
    style A2_R_CONTRIBUTION fill:#1e3a5f,color:#fff
    style A2_R_ENTITLEMENT fill:#1e3a5f,color:#fff
    style A3_R_SELF fill:#1e3a5f,color:#fff
    style A3_R_ALTROCENTRIC fill:#1e3a5f,color:#fff
    style SUMMARY fill:#3d1e5f,color:#fff
```
