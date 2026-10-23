---
use_case: ClickUp Delivery Command v2
client: Clickup
poc_row: POC-clickup-delivery-command-v2-20261022
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g4
version: 1 · since 2026-10-22T09:15:18Z
thread: C0CBAPEC4AD · 1792662475.792899
intent: both
stage_flag: 

gates:
  g1: {status: approved, round: 1, posted_ts: 1792661200.384079, decided_by: Gourav Mahunta (row), decided_at: 2026-10-22T09:31:00Z}
  g2: {status: approved, round: 1, posted_ts: 1792662475.772399, decided_by: Gourav Mahunta (row), decided_at: 2026-10-22T09:51:39Z}
  g3: {status: approved, round: 1, posted_ts: 1792662475.792899, decided_by: Gourav Mahunta (row), decided_at: 2026-10-23}
  g4: {status: waiting, round: 1, posted_ts: 1792662475.792899, decided_by: , decided_at: }

posts:
  - when: 2026-10-22T09:26:40Z
    kind: g1
    ts: 1792661200.384079
    by: bot
    version: 1
    round: 1
  - when: 2026-10-22T09:28:00Z
    kind: status
    ts: 1792661200.384079
    by: bot
    version: 1
    round: 1
  - when: 2026-10-22T09:47:08Z
    kind: g2
    ts: 1792662475.772399
    by: bot
    version: 1
    round: 1
  - when: 2026-10-22T09:48:30Z
    kind: status
    ts: 1792662475.772399
    by: bot
    version: 1
    round: 1
  - when: 2026-10-22T13:30:00Z
    kind: g3
    ts: 1792662475.792899
    by: bot
    version: 1
    round: 1
  - when: 2026-10-22T13:32:00Z
    kind: status
    ts: 1792662475.792899
    by: bot
    version: 1
    round: 1
  - when: 2026-10-23T07:52:00Z
    kind: status
    ts: 1792662475.792899
    by: bot
    version: 1
    round: 1

  - when: 2026-10-23T10:31:56Z
    kind: g4
    ts: 1792662475.792899
    by: bot
    version: 1
    round: 1
  - when: 2026-10-23T10:32:31Z
    kind: status
    ts: 1792662475.792899
    by: bot
    version: 1
    round: 1

runs:
  - started: 2026-10-22T09:15:18Z
    ended: 2026-10-22T09:26:28Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 130
    outcome: posted G1
  - started: 2026-10-22T09:31:00Z
    ended: 2026-10-22T09:47:08Z
    gate: g2
    stages: [2-plan]
    spawns: 1
    tokens: 276
    outcome: posted G2
  - started: 2026-10-22T09:53:30Z
    ended: 2026-10-22T13:30Z
    gate: g3
    stages: [3-build, 4-verify, 3-build, 4-verify, 5-handover]
    spawns: 19
    tokens: 4000
    outcome: posted G3
  - started: 2026-10-23T07:41:45Z
    ended: 2026-10-23T07:50Z
    gate: g4
    stages: []
    spawns: 0
    tokens: 0
    outcome: "stopped: poc-studio plugin (poc-collateral-studio) not installed in the cloud box"
  - started: 2026-10-23T09:55:00Z
    ended: 2026-10-23T10:31:56Z
    gate: g4
    stages: [6-collaterals, 7-review, 6-collaterals, 7-review]
    spawns: 4
    tokens: 690
    outcome: posted G4

stopped: 

asks:
  - id: A1
    text: "Delivery Command is one application where the team plans, staffs and reports on every implementation, where customers follow and sign off their own rollout, and where an AI assistant writes the routine status work."
    source: "ClickUp-Delivery-Command-BRD.pdf § 1 Summary, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A2
    text: "Earlier warning: a project at risk of missing its go-live date is flagged at least three weeks before the date, on average."
    source: "ClickUp-Delivery-Command-BRD.pdf § 1 Summary, outcomes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A3
    text: "Less reporting effort: weekly status reports take a consultant under 10 minutes instead of about an hour."
    source: "ClickUp-Delivery-Command-BRD.pdf § 1 Summary, outcomes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A4
    text: "Balanced staffing: no consultant is booked above 100% for more than one week in a quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf § 1 Summary, outcomes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A5
    text: "Faster customer sign-off: customers approve deliverables in the portal within two working days."
    source: "ClickUp-Delivery-Command-BRD.pdf § 1 Summary, outcomes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A6
    text: "Each project follows the same seven stages: Kickoff, Discovery, Configuration, Migration, Training, Go-live and Hypercare."
    source: "ClickUp-Delivery-Command-BRD.pdf § 2 Background, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A7
    text: "Most delays come from three causes: data migration taking longer than planned, the customer not signing off a stage on time, and consultants being booked on too many projects at once. Delivery Command should make all three visible and actionable."
    source: "ClickUp-Delivery-Command-BRD.pdf § 2 Background, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A8
    text: "Brand colour: none supplied. Take it from the live site clickup.com."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A9
    text: "Logo: no file supplied. Fetch the official logo. It appears on the sign-in page, the expanded and collapsed left menu, the browser tab icon, the customer portal header, generated status reports (PDF and Word), and the weekly executive email."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A10
    text: "Customer logos: shown as circles on project cards and in the portal."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A11
    text: "Typeface: take it from the live site. Numbers must line up in tables. The customer portal must also display Japanese and German text correctly."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A12
    text: "Tone: clear, calm and direct. Errors say what happened and what to do next. No jokes or exclamation marks in the product."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A13
    text: "Feel: the internal workspace is a daily working tool and should stay dense and quiet. The customer portal and the executive summary are also shown in sales demos and should look polished."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A14
    text: "Appearance: light and dark both needed. Light is the default."
    source: "ClickUp-Delivery-Command-BRD.pdf § 3 Brand and design inputs, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A15
    text: "Implementation lead | Owns 8 to 12 customer projects | Plan stages and tasks, manage risks, raise scope changes, publish weekly status | Desktop, all day, keyboard-heavy, dense screens"
    source: "ClickUp-Delivery-Command-BRD.pdf § 4 Personas, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A16
    text: "Delivery director | Runs the portfolio for one region | Spot projects at risk, rebalance staff, approve scope changes | Desktop and laptop, several times a day"
    source: "ClickUp-Delivery-Command-BRD.pdf § 4 Personas, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A17
    text: "Resource manager | Books consultants onto projects | See who is free, book people by skill, approve timesheets | Desktop, dense grids, long sessions"
    source: "ClickUp-Delivery-Command-BRD.pdf § 4 Personas, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A18
    text: "Implementation consultant | Works on 3 to 5 projects | Update tasks, log time, attend customer sessions | Laptop and phone, often between meetings"
    source: "ClickUp-Delivery-Command-BRD.pdf § 4 Personas, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A19
    text: "Customer project sponsor | External user at a customer | Follow progress, sign off deliverables, book training, upload files | Desktop, occasional, needs guidance and plain wording"
    source: "ClickUp-Delivery-Command-BRD.pdf § 4 Personas, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A20
    text: "VP of customer success | Executive owner | Read headline numbers and what changed, every Monday | Laptop and tablet, about 10 minutes a week"
    source: "ClickUp-Delivery-Command-BRD.pdf § 4 Personas, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A21
    text: "Delivery Copilot is an AI assistant available from every internal screen. It has the tools listed below. Anything it writes is labelled as AI-written."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 Delivery Copilot, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A22
    text: "List every project with customer, region, stage, go-live date, health, lead, seats and contract value. Users search and filter by region, stage, health and lead. The count of results shows as \"x of y\". Filters that apply show as removable chips with one \"clear all\"."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.1 P1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A23
    text: "Show portfolio health as counts of On track, At risk and Off track, with the change since last week."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.1 P2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A24
    text: "Place each open risk on a grid of likelihood against impact, so leaders see which risks matter most. Choosing a cell lists its risks."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.1 P3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A25
    text: "Show every go-live date in the next 90 days on a timeline, grouped by region, with slipped dates marked."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.1 P4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A26
    text: "Show how the share of projects on track has moved over the last 12 weeks."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.1 P5, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A27
    text: "Leaders can save a filtered view and share it with their team."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.1 P6, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A28
    text: "A project overview shows the stage the project is in, the seven stages as a progress path, days to go-live, budget hours used against planned, open risks and the next customer sign-off due."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A29
    text: "Tasks can be viewed as a list or as a board with one column per stage. A column shows a warning when it holds more than its limit (default 15). Tasks can be moved between columns by dragging or from a menu."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A30
    text: "A timeline shows tasks with start and end dates, dependencies between them and the critical path. Changing a date moves dependent tasks and shows the new go-live date before it is saved."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A31
    text: "A risks, assumptions, issues and decisions (RAID) log records each item with owner, due date, status and history."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A32
    text: "A document library holds the statement of work, migration plans and sign-off records. Files open in a viewer inside the application."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W5, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A33
    text: "An activity feed shows who changed what and when on the project."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W6, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A34
    text: "Task detail opens beside the list so the user keeps their place. It shows description, assignee, dates, time logged, comments and attachments."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.2 W7, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A35
    text: "Show every consultant against the next 12 weeks with the percentage they are booked each week. Over 100% is flagged."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.3 R1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A36
    text: "Book a consultant onto a project by choosing person, project, weeks and hours. Booking works without dragging."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.3 R2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A37
    text: "Show consultants against skills (data migration, integrations, admin training, API, Japanese language) with a level for each, so the right person can be found."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.3 R3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A38
    text: "Consultants log time against tasks each day. Managers approve or return weekly timesheets, giving a reason when they return one."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.3 R4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A39
    text: "Should: show booked hours against capacity for each region over the quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.3 R5, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A40
    text: "An implementation lead raises a change request with the reason, the work added or removed, and the effect on hours, cost and go-live date."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.4 S1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A41
    text: "Before submitting, the lead sees the plan before and after the change side by side, with the differences marked."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.4 S2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A42
    text: "Changes under 40 hours need the delivery director's approval. Changes of 40 hours or more also need the finance partner, in that order. The request shows who has approved and who is next."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.4 S3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A43
    text: "Rejecting a change request requires a written reason. Approved changes update the plan and are recorded in the activity feed."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.4 S4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A44
    text: "Users ask questions in plain language, for example \"Which Japan projects go live in November and are at risk?\" The assistant opens with three suggested questions based on the user's projects, and shows each stage while it works."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 A1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A45
    text: "Chart tool: the assistant can answer with a chart, such as hours by stage or go-lives by month. Charts use the application's colours and show units."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 A2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A46
    text: "Status report tool: the assistant drafts the weekly status report for a project from its tasks, risks and time entries. The lead edits and publishes it. The report can be exported as PDF or Word."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 A3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A47
    text: "Task tool: the assistant can propose tasks, for example after a meeting summary. Proposed tasks are listed for the user to accept or reject; nothing is created without acceptance."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 A4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A48
    text: "Meeting summary tool: the assistant summarises a customer meeting transcript into decisions, actions and risks. Each point links to the part of the transcript it came from."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 A5, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A49
    text: "Risk prediction: the assistant flags projects likely to miss go-live, with a confidence level and the evidence for each flag, such as migration tasks running late."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.5 A6, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A50
    text: "Customer sponsors sign in to see only their own project: stage, milestones, upcoming sessions, open actions for their team and the documents shared with them."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.6 C1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A51
    text: "Sponsors sign off a stage deliverable or request changes with a comment. A sign-off records who approved and when."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.6 C2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A52
    text: "Sponsors book training sessions by choosing a day and then a time slot. Taken slots stay visible but cannot be chosen."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.6 C3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A53
    text: "Sponsors upload files such as user lists (CSV up to 50,000 rows). Errors appear row by row and can be fixed before confirming."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.6 C4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A54
    text: "A readiness checklist guides the customer through 10 setup items. An item they have not answered shows as not set, never as a guessed value."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.6 C5, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A55
    text: "The portal is available in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.6 C6, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A56
    text: "A weekly summary shows six headline numbers with their change from last week: active projects, go-lives this month, projects at risk, average days to go-live, consultant utilisation and contract value awaiting go-live. A change is coloured by whether it is good or bad for the business, not by its sign."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.7 E1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A57
    text: "Show how contract value awaiting go-live moved from last month to this month, split into new projects, go-lives completed, slipped dates and cancellations."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.7 E2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A58
    text: "List the five projects that changed most this week, with the reason for each."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.7 E3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A59
    text: "The summary is also sent as an email every Monday at 08:00 in each region's time zone."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.7 E4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A60
    text: "Consultants see today's tasks and sessions, update a task's status, and log time in under 30 seconds on a phone."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.8 M1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A61
    text: "Notifications for new assignments, sign-offs and mentions. Each can be marked read or opened."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.8 M2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A62
    text: "Roles control what each user can see and change. Show roles against permissions as a grid."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.9 D1, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A63
    text: "Keep a record of who did what and when. It cannot be edited and can be filtered by person, project and action."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.9 D2, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A64
    text: "Show the status of each integration (Salesforce, Slack, Google Drive, Jira) with last sync time and any error."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.9 D3, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A65
    text: "Project settings (name, region, go-live date, budget hours) can be edited in place, with clear unsaved, saving, saved and failed states."
    source: "ClickUp-Delivery-Command-BRD.pdf § 5.9 D4, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A66
    text: "Sign-in, forgot password, reset password | Everyone | First | None"
    source: "ClickUp-Delivery-Command-BRD.pdf § 6 Screens and navigation, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A67
    text: "Internal users navigate with a left menu: Portfolio, Projects, Resourcing, Timesheets, Changes, Admin. The top bar shows the current project or view, search, notifications and the profile menu. Delivery Copilot opens as a panel on the right."
    source: "ClickUp-Delivery-Command-BRD.pdf § 6 Screens and navigation, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A68
    text: "Customers get a shorter top menu: Home, Sign-offs, Sessions, Files, Checklist."
    source: "ClickUp-Delivery-Command-BRD.pdf § 6 Screens and navigation, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A69
    text: "The phone has bottom tabs: Today, Tasks, Time, Alerts."
    source: "ClickUp-Delivery-Command-BRD.pdf § 6 Screens and navigation, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A70
    text: "Active projects | 180 to 300 | Portfolio list needs paging, search and filters"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A71
    text: "Tasks per project | 150 to 1,200 | Board and timeline must stay readable"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A72
    text: "Consultants and leads | about 72 | Resourcing grid is people against 12 weeks"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A73
    text: "Open risks across the portfolio | about 400 | Grid of likelihood against impact, with drill-down"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A74
    text: "Customer users | about 900 | Portal must be simple for occasional users"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A75
    text: "Time entries per week | about 3,000 | Timesheet approval in batches"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A76
    text: "Customer upload | up to 50,000 rows | Errors summarised, not listed in full"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A77
    text: "Languages | English, German, Japanese | Text can grow by 30% in German"
    source: "ClickUp-Delivery-Command-BRD.pdf § 7 Data volumes, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A78
    text: "Good or finished | On track, Signed off, Approved, Live"
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Status words, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A79
    text: "Needs attention | At risk, Awaiting sign-off, Over capacity, Pending approval"
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Status words, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A80
    text: "Problem | Off track, Blocked, Rejected, Sync failed"
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Status words, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A81
    text: "Neutral | Not started, Draft, Scheduled, Hypercare"
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Status words, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A82
    text: "Sample customers (all invented): Halden Freight | Logistics | Europe | 4,800 | Migration; Corvia Health | Healthcare | North America | 12,000 | Configuration; Brightmoor University | Education | Europe | 2,300 | Training; Kestrel Energy | Energy | North America | 7,500 | Discovery; Sakura Mobility | Automotive | Japan | 9,200 | Go-live; Ostrander Retail | Retail | North America | 650 | Hypercare"
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Sample content, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A83
    text: "Project IDs look like IMP-2611, change requests like CR-0457, risks like RSK-1183."
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Sample content, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A84
    text: "Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026 年 10 月 17 日)."
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Sample content, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A85
    text: "Money shows in the contract currency (USD, EUR or JPY)."
    source: "ClickUp-Delivery-Command-BRD.pdf § 8 Sample content, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A86
    text: "No projects assigned yet | Projects appear here once a lead assigns you"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A87
    text: "A search or filter matches nothing | Nothing matches the current filters, with a way to clear them"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A88
    text: "Copilot is still working | Which stage it is on"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A89
    text: "Copilot cannot answer | Why, and what to try instead"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A90
    text: "An integration has failed | Which one, since when, and what is affected"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A91
    text: "A booking takes someone over capacity | Who, which weeks and by how much, before saving"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A92
    text: "A customer upload has errors | For example 214 of 50,000 rows need fixing"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A93
    text: "A checklist item has no answer | The item shows as not set"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A94
    text: "The user has no access to a project | Who can grant access"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A95
    text: "The session is about to end | How to stay signed in"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A96
    text: "Data is out of date | When it was last updated"
    source: "ClickUp-Delivery-Command-BRD.pdf § 9 Situations the screens must handle, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A97
    text: "The internal workspace is in English. The customer portal is in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf § 10 Languages, regions and accessibility, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A98
    text: "Times show the user's time zone. Weeks start on Monday in Europe and Japan and on Sunday in North America."
    source: "ClickUp-Delivery-Command-BRD.pdf § 10 Languages, regions and accessibility, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A99
    text: "All drag actions also work from the keyboard. Controls are at least 24 px on desktop and larger on the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf § 10 Languages, regions and accessibility, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A100
    text: "Meaning never depends on colour alone: every status shows an icon and a word."
    source: "ClickUp-Delivery-Command-BRD.pdf § 10 Languages, regions and accessibility, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A101
    text: "Screens meet WCAG 2.2 AA in both light and dark appearance."
    source: "ClickUp-Delivery-Command-BRD.pdf § 10 Languages, regions and accessibility, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A102
    text: "Salesforce | Contract value, seats and close date when a deal is won, which creates the project"
    source: "ClickUp-Delivery-Command-BRD.pdf § 11 Integrations, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A103
    text: "Slack | Notifications and the weekly status post to each project channel"
    source: "ClickUp-Delivery-Command-BRD.pdf § 11 Integrations, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A104
    text: "Google Drive | Shared documents and customer uploads"
    source: "ClickUp-Delivery-Command-BRD.pdf § 11 Integrations, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A105
    text: "Jira | Engineering escalations linked to project issues"
    source: "ClickUp-Delivery-Command-BRD.pdf § 11 Integrations, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A106
    text: "The first release does not include the following, and the application must not suggest otherwise: Billing, invoicing or revenue recognition. Building or editing customer workspaces in the core ClickUp product. Hiring, performance reviews or payroll for consultants. A public marketing site. Video calls or call recording. Offline use of the phone view."
    source: "ClickUp-Delivery-Command-BRD.pdf § 12 Out of scope, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A107
    text: "Average warning before a missed go-live | 21 days or more"
    source: "ClickUp-Delivery-Command-BRD.pdf § 13 Success measures, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A108
    text: "Time to produce a weekly status report | Under 10 minutes"
    source: "ClickUp-Delivery-Command-BRD.pdf § 13 Success measures, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A109
    text: "Consultant weeks booked above 100% per quarter | No more than 1 per consultant"
    source: "ClickUp-Delivery-Command-BRD.pdf § 13 Success measures, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A110
    text: "Customer sign-off time | 2 working days or less"
    source: "ClickUp-Delivery-Command-BRD.pdf § 13 Success measures, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A111
    text: "Executive time to read the weekly summary | 10 minutes or less"
    source: "ClickUp-Delivery-Command-BRD.pdf § 13 Success measures, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A112
    text: "Customers completing the readiness checklist without help | 75%"
    source: "ClickUp-Delivery-Command-BRD.pdf § 13 Success measures, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A113
    text: "I want to see every project on one screen without scrolling."
    source: "ClickUp-Delivery-Command-BRD.pdf § 14 Stakeholder notes, delivery director, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A114
    text: "Let us edit the timeline straight from the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf § 14 Stakeholder notes, consultants, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A115
    text: "Show customers their health score."
    source: "ClickUp-Delivery-Command-BRD.pdf § 14 Stakeholder notes, VP of customer success, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A116
    text: "Customers should never see internal health."
    source: "ClickUp-Delivery-Command-BRD.pdf § 14 Stakeholder notes, implementation leads, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A117
    text: "Colour-code consultants by region everywhere."
    source: "ClickUp-Delivery-Command-BRD.pdf § 14 Stakeholder notes, resource manager, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A118
    text: "Add a pricing calculator for upsells."
    source: "ClickUp-Delivery-Command-BRD.pdf § 14 Stakeholder notes, sales, shared in #clickup-test-2 https://unifyapps.slack.com/archives/C0CBAPEC4AD/p1792660005169639 · 2026-10-22"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Sales upsell pricing"
    status: out_of_scope

coverage:
  - ask: A1
    by: beat 1
  - ask: A2
    by: beat 7
  - ask: A3
    by: beat 7
  - ask: A4
    by: beat 3
  - ask: A5
    by: beat 5
  - ask: A6
    by: beat 2
  - ask: A7
    by: beat 7
  - ask: A8
    by: beat 1
  - ask: A9
    by: beat 7
  - ask: A10
    by: beat 1
  - ask: A11
    by: open question 12 (typeface)
  - ask: A12
    by: beat 3
  - ask: A13
    by: beat 5
  - ask: A14
    by: control Appearance (Light, Dark) in the profile menu on Portfolio
  - ask: A15
    by: beat 2
  - ask: A16
    by: beat 1
  - ask: A17
    by: beat 3
  - ask: A18
    by: control Log time in the task detail panel on Project overview
  - ask: A19
    by: beat 5
  - ask: A20
    by: beat 6
  - ask: A21
    by: beat 7
  - ask: A22
    by: beat 1
  - ask: A23
    by: beat 1
  - ask: A24
    by: beat 1
  - ask: A25
    by: beat 1
  - ask: A26
    by: beat 1
  - ask: A27
    by: control Save view and the saved views menu on Portfolio
  - ask: A28
    by: beat 2
  - ask: A29
    by: beat 2
  - ask: A30
    by: control Timeline tab (date change previews the new go-live before Save) on Project overview
  - ask: A31
    by: control RAID tab on Project overview
  - ask: A32
    by: control Documents tab with the in-app viewer on Project overview
  - ask: A33
    by: beat 4
  - ask: A34
    by: beat 2
  - ask: A35
    by: beat 3
  - ask: A36
    by: beat 3
  - ask: A37
    by: control Skills tab on Resourcing
  - ask: A38
    by: control Timesheets tab (Approve, Return with reason) on Resourcing
  - ask: A39
    by: control Capacity tab on Resourcing
  - ask: A40
    by: beat 4
  - ask: A41
    by: beat 4
  - ask: A42
    by: beat 4
  - ask: A43
    by: beat 4
  - ask: A44
    by: beat 7
  - ask: A45
    by: beat 7
  - ask: A46
    by: beat 7
  - ask: A47
    by: control Proposed tasks (Accept, Reject) on the Copilot panel
  - ask: A48
    by: control Meeting summary with transcript links on the Copilot panel
  - ask: A49
    by: beat 1
  - ask: A50
    by: beat 5
  - ask: A51
    by: beat 5
  - ask: A52
    by: control Sessions (day, then slot) on Customer portal
  - ask: A53
    by: control Files upload with row errors on Customer portal
  - ask: A54
    by: control Checklist on Customer portal
  - ask: A55
    by: beat 5
  - ask: A56
    by: beat 6
  - ask: A57
    by: beat 6
  - ask: A58
    by: beat 6
  - ask: A59
    by: beat 6
  - ask: A60
    by: open question 7 (phone view)
  - ask: A61
    by: control notifications bell (mark read, open) on Portfolio
  - ask: A62
    by: open question 13 (Admin screen)
  - ask: A63
    by: open question 13 (Admin screen)
  - ask: A64
    by: open question 13 (Admin screen)
  - ask: A65
    by: control Settings tab (edit in place) on Project overview
  - ask: A66
    by: beat 1
  - ask: A67
    by: beat 1
  - ask: A68
    by: beat 5
  - ask: A69
    by: open question 7 (phone view)
  - ask: A70
    by: beat 1
  - ask: A71
    by: beat 2
  - ask: A72
    by: beat 3
  - ask: A73
    by: beat 1
  - ask: A74
    by: beat 5
  - ask: A75
    by: control Timesheets tab select-all Approve on Resourcing
  - ask: A76
    by: control Files upload error summary on Customer portal
  - ask: A77
    by: beat 5
  - ask: A78
    by: beat 1
  - ask: A79
    by: beat 1
  - ask: A80
    by: beat 1
  - ask: A81
    by: beat 1
  - ask: A82
    by: beat 1
  - ask: A83
    by: beat 1
  - ask: A84
    by: beat 5
  - ask: A85
    by: beat 1
  - ask: A86
    by: control My projects toggle (empty state for a user assigned to none) on Portfolio
  - ask: A87
    by: control Clear all on the filter chips (filtered-empty state) on Portfolio
  - ask: A88
    by: beat 7
  - ask: A89
    by: beat 7
  - ask: A90
    by: beat 1
  - ask: A91
    by: beat 3
  - ask: A92
    by: control Files upload error summary (214 of 50,000 rows) on Customer portal
  - ask: A93
    by: control Checklist (Not set items) on Customer portal
  - ask: A94
    by: control a link to another customer's project (who can grant access) on Customer portal
  - ask: A95
    by: control session-expiry dialog (Stay signed in) on Portfolio
  - ask: A96
    by: beat 1
  - ask: A97
    by: beat 5
  - ask: A98
    by: beat 3
  - ask: A99
    by: beat 2
  - ask: A100
    by: beat 1
  - ask: A101
    by: beat 1
  - ask: A102
    by: open question 6 (integrations)
  - ask: A103
    by: open question 6 (integrations)
  - ask: A104
    by: open question 6 (integrations)
  - ask: A105
    by: control Escalate to Jira on a RAID risk (external step) on Project overview
  - ask: A106
    by: beat 1
  - ask: A107
    by: beat 7
  - ask: A108
    by: beat 7
  - ask: A109
    by: beat 3
  - ask: A110
    by: beat 5
  - ask: A111
    by: beat 6
  - ask: A112
    by: control Checklist completion count on Customer portal
  - ask: A113
    by: open question 1
  - ask: A114
    by: open question 2
  - ask: A115
    by: open question 3
  - ask: A116
    by: open question 3
  - ask: A117
    by: open question 4

size:
  pages: 6
  objects: 15
  automations: 8
  agents: 1
  tasks_est: 56
  nebula_plans_est: 6
  reference: 4 pages / 3 objects / 3 automations / 1 agent

data:
  source: "assumed, shaped like ClickUp's implementation tracking as the BRD describes it (§ 5, § 7, § 8 sample customers and id shapes); no data file was given (studio/data/ holds none)"
  masked: "none: fictional. The six BRD sample customers are invented by the BRD itself; every other customer, person and identifier is invented here; no real names, emails or phones"
  rows:
    - "Project: 20, record · seed (story row IMP-2611 Halden Freight first; the six BRD sample customers included)"
    - "Task: 20, record · seed (all on IMP-2611; 16 in Migration to show the column-limit warning)"
    - "RAID item: 20, record · seed (RSK-1183 story risk)"
    - "Consultant: 12, record · seed"
    - "Booking: 20, record · seed (Tomas Brandt 100% in week of 2 Nov, Aiko Tanaka 110% in week of 16 Nov)"
    - "Time entry: 20, record · seed (timesheet week 19 Oct)"
    - "Change request: 2, record · seed (CR-0457 created live)"
    - "Deliverable: 8, record · seed (Migration plan v2 awaiting sign-off)"
    - "Session slot: 12, record · seed (4 taken)"
    - "Checklist item: 10, record · seed (3 not set)"
    - "Document: 8, record · seed"
    - "Activity: 20, record · seed (Jira sync failed row; 5 unread notifications)"
    - "AI output: 6, record · seed (AI-written marker on every row)"
    - "Weekly metric: 19, record · seed (12 trend, 6 headline, 1 bridge)"
    - "Saved view: 2, record · seed"
  lives_in: UnifyApps Storage (15 objects, OBJ_cudc_*)
  expected_answers: eval.csv

verify:
  round: 2
  walked: 2026-10-22T12:30Z to 13:05Z
  beats_pass: 3 of 9
  beats:
    - "1 Portfolio: pass (14 / 4 +1 / 2 +1, AI risk card High with evidence, RSK-1183 in the 4x4 cell, two slipped go-lives, 70% trend now in a chart token, Region Europe + Health At risk give 2 of 20, Jira sync failed note; Health tags on one line)"
    - "2 Project overview: fix (Open RAID items now 5; the task detail now opens beside the board with no page side-scroll, but it covers the Activity and Settings tabs and its Log time fields are 40 px and 8 px wide; Validate pilot batch is already Done from round 1, so Mark done is disabled and the beat cannot be played as written; Move task proved live with a net-zero move to Training and back, exec 6ada03135668097e1a8b64b5 and 6ada03235668097e1a8b79b8)"
    - "3 Resourcing: fix (refusal live and exact, exec 6ada041b5668097e1a8bf787 over_capacity; skills filter Data migration gives 4 of 12 with Lena Vogt; Lena Vogt still reads 100%, 80% before any booking from test leftovers, so the beat's 80%, 60% cannot show; the Lena booking was withheld this round so as not to add another leftover)"
    - "4 Change request: fix (DEMO-TEST CR-0460 submitted live, exec 6ada04965668097e1a8c45ef, path Ines Moreau then Raj Patel; plan before and after labels now wrap inside their cells; director approval live, exec 6ada04bb5668097e1a8c4acc moved_to_finance; the activity feed on CR-0460 still shows only 'raised' after the director approved, also after a reload; finance approval withheld)"
    - "5 Customer portal: unverified: sign-off withheld (it would change the story row); Deutsch, 27.11.2026 and 28.10.2026, Halden Freight only, no internal health, one .btn-p on Freigaben, dates without time, Sessions opens on November 2026, Checklist shows each answer's text: all shown"
    - "6 Weekly summary: fix (six tiles, at risk 6 +2 as bad, '+1 project'; bridge now Start, New, Completed, Slipped, Cancelled, End with $4.05M to $4.21M, but its x labels run together ('CompletedSlippedCancelled'); the five-projects # column is still 40 px; email preview per region shown)"
    - "7 Copilot: fix (live in the panel: Halden Freight with in-app links that open in the same tab; the AI-written draft cites T-2611-10/11/12 late, RSK-1183, ISS-0523 and 512 of 640 h in 39 s; the editor now opens on this week's empty draft (week of Oct 19); but Use Copilot draft leaves the editor empty and toasts 'Delivery Copilot has no answer in this conversation to use yet.' with the draft on screen, twice; the draft also ends with 'Time entries look odd: … consultant ID CNS-01 … dated 23 Oct, which is tomorrow'; Publish and Export withheld or unreachable with an empty editor)"
    - "H1 Book consultant canvas: pass (readable step names Read the consultant, Read the project, Read every booking; description shown)"
    - "H2 Copilot in agent builder: pass (instructions, one read tool, read-only, chart tool); createDocxOrPdf is attached and on but never offered to the model (platform, dev_issues)"
  controls_pass: 46 of 49
  controls_fail:
    - "Project overview: the open task panel covers the Activity and Settings tabs (clicks land on the panel) and its Log time Who and Hours fields are 40 px and 8 px wide"
    - "Change request: Approve as the director does not add a row to the activity feed, and Viewing as Ines Moreau still offers Approve and Reject after she approved"
    - "Status report: Use Copilot draft does not fill the editor though the panel holds the AI-written draft"
  controls_note: "round 1's sweep set; this round re-pressed the four that failed in round 1 (Mention row now opens IMP-2611, Copilot link now in-app, task panel and Use Copilot draft still fail), every beat control, the overview, resourcing and portal tabs, filters, search and the copilot suggestions. Writes left unpressed as in round 1: Save view, Escalate to Jira, Log time, Settings Save, Timesheets Approve and Return, CR Reject, finance approval, Sign off, Request changes, slot booking, checklist Save, CSV Confirm, Publish, Proposed task Accept and Reject; deletes: none seen"
  queries_pass: 4 of 4
  queries:
    - "Which Europe projects go live in November and are at risk?: pass, Halden Freight (IMP-2611) with link, Eskel Foods noted as December; 31 s by tool (case e_6ada0840a965b115459d7fb0, run twice by the tool to find the case)"
    - "Draft this week's status report for Halden Freight: pass, AI-written draft citing the late batch loads, RSK-1183 and 512 of 640 h; 39 s in the panel (by tool case e_6ada0866a965b115459d862d still running at 50 s)"
    - "Show go-lives by month: pass, column chart Oct 2026 to Feb 2027 in the brand colours with axis labels; 47 s in the panel (case e_6ada089ca965b115459d90d0)"
    - "What is our revenue this quarter?: pass, declined and pointed to the finance partner; 11 s (case e_6ada08cc1a10ec0c913072fe)"
  coverage_pass: 95 of 103
  coverage_not_shown: [A30 date-change preview on the timeline (not pressed), A43 approved change moves the plan (withheld), A75 select-all Approve (write), A86 My projects toggle (not built), A94 no-access project page (not built), A95 session-expiry dialog (not built), A105 Escalate to Jira (external write outside the beats), A108 publish the status report (withheld; the draft also cannot reach the editor)]
  checks_pass: 4 of 7
  p95_latency_s: 47
  latency_target_s: 90
  open:
    - "code-app · update · ClickUp Delivery Command: screen Project overview: the task detail panel beside the board starts below the tab row so Board, List, Timeline, RAID, Documents, Activity and Settings stay clickable while it is open (now the panel at x 680 to 1040 from y 456 covers the Activity and Settings tabs and takes their clicks), and its Log time Who and Hours fields show their values (now 40 px, reading 'Ler', and 8 px); nothing else changes"
    - "record · update · ClickUp DC · Task: T-2611-09 Validate pilot batch returns to In progress in Migration so beat 2's Mark done can run (now Done from round 1's walk, so Mark done is disabled); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screen Change request: each approval adds its row to the activity feed ('Ines Moreau approved CR-0460'), and the Approve and Reject buttons hide for an approver who has already decided (now the feed on CR-0460 shows only 'raised' after the director approved, also after a reload, and Viewing as Ines Moreau still offers Approve); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screen Weekly summary: the contract value bridge's x labels Start, New, Completed, Slipped, Cancelled, End each stand apart (now 'Completed', 'Slipped' and 'Cancelled' run together in the 344 px chart), and the five-projects # column is 64 px or wider (still 40 px); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screen Status report: Use Copilot draft puts the open Copilot conversation's latest AI-written answer into the report editor (now, with the draft on screen in the panel after Ask Copilot for a draft, it toasts 'Delivery Copilot has no answer in this conversation to use yet.' and the editor stays empty, twice); nothing else changes"
    - "automation · update · ClickUp DC · Read delivery data: each time_entry row carries the consultant's name beside its id (now only CNS-01, so the Copilot's status draft tells the presenter 'the data doesn't give a name for that ID'); nothing else changes"
    - "record · update · ClickUp DC · Time entry: the IMP-2611 entries of the week of 19 Oct are dated on or before 22 Oct and none sits on T-2611-09 after it is Done (now entries dated 23 Oct and 18 h on Validate pilot batch, which the Copilot's draft flags as 'tomorrow' and 'marked done but still has 18 h logged'); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screen Project overview: on the Settings tab Save takes .btn-s while the header's Draft status report stays the one .btn-p (now two .btn-p on screen); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: the sticky header keeps an opaque ground in the light theme too (now rgba(255,255,255,.82) with backdrop-filter computing to none, so board cards and the task panel show through behind 'Project overview' when scrolled; the dark theme is fixed); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: Copilot panel: the agent avatar shows the Copilot icon (still a bare letter 'C' in the welcome and on each answer); nothing else changes"
  previous_open:
    - "task detail beside the board: fixed for the side-scroll (scrollWidth 1440); the panel now covers the tab row (new line)"
    - "RAID 5 open items: fixed (Open RAID items 5, ISS-0523 present)"
    - "change request diff labels: fixed (labels wrap inside their cells, scrollWidth equals clientWidth)"
    - "weekly bridge Slipped and two decimals: fixed ($4.05M to $4.21M with Slipped); its x labels now collide (in the bridge line)"
    - "weekly five-projects table: tags on one line and '+1 project' fixed; # column still 40 px"
    - "portfolio Health tags and trend colour: fixed (one line; trend stroke #3F34D0)"
    - "status report opens on this week's draft: fixed; the draft reaching the editor without the clipboard: still failing"
    - "AI output 27 November: MS-2611-1020 fixed (decision, t2 and t3 read 27 November on the status report screen); SR-2611-W42 was not opened this round (the editor no longer opens on it)"
    - "Copilot project link in the same tab: fixed (/projects/IMP-2628/overview in the same tab)"
    - "Copilot avatar and suggested questions: questions show once (fixed); avatar still 'C'"
    - "portal Sign-offs one .btn-p and dates without time: fixed"
    - "status report Publish the only .btn-p: fixed"
    - "portal Sessions opens on a month with slots: fixed (November 2026)"
    - "portal Checklist shows answers: fixed (answer text in each answered item)"
    - "sticky header dark theme: fixed (opaque rgb(32,31,48)); light theme still translucent (new line)"
    - "notifications name once and Mention row opens: fixed"
    - "Copilot PDF and DOCX tool: still failing, platform (dev_issues)"
    - "console errors on load: still failing, platform (dev_issues)"
  notes:
    - "eval.csv (studio/state/clickup-delivery-command-v2.eval.csv) is not in this container; queries ran on the three Copilot questions in build_contract plus 'What is our revenue this quarter?', as in round 1"
    - "walked in the preview (https://orbit.uat.unifyapps.com/agent-api/preview/b/app-0e25eb6667c3/main/) through Nebula's browser.mjs signed in with the person's saved sign-in (user Gourav), 1440 x 900; open-page reports 'not a page of the builder or preview' for a code app but the browser was signed in and every route loaded; the published host was not opened"
    - "latency: send_test_message reruns a tool-calling message to find its case, so panel timings (39 s draft, 47 s chart) stand for those rows; p95 is the slowest of the four"
    - "checks per screen (worst): brand-primary-only fail (Project overview Settings tab: Draft status report and Save both .btn-p; masthead eyebrows, .prog fill, .av, .amb left out as the stylesheet's own; Portfolio, Customer portal, Status report now pass); no-horizontal-scroll pass on every screen including the task panel open; empty-states pass (Portfolio 'No rows match your search and filters' with Clear all; round 1's other tables unchanged); table-readable fail (Weekly summary # column 40 px); no-console-errors fail, platform (dev_issues); stylesheet-verbatim pass the minified way, light and dark (only 150ms vs .15s and .050 vs .05); logo-contrast pass (logo mean L 0.70 on #3028A8 to #665DD9, lowest about 3.6:1; portal logo-on-light on white)"
    - "writes withheld as in round 1 because they change the story row other beats read: the finance partner's approval (CR-0460 now waits on it), the sponsor's Sign off of Migration plan v2, Publish of the status report; the Lena Vogt booking was also withheld so as not to add a fourth Lena leftover"
    - "rows this round added: Change request CR-0460 (DEMO-TEST reason, director approved, pending finance) with its Activity row; Activity ACT-34 and ACT-35 (Validate pilot batch to Training and back to Migration, status unchanged Done); no booking, no Jira issue"

collaterals:
  folder: studio/collaterals/clickup
  round: 1
  script: {path: studio/collaterals/clickup/out/ClickUp_Delivery_Command_Demo_Script.pdf, bytes: 321707, pages: 15, length: "about 4:41", made_from: v1, source: studio/collaterals/clickup/story.json, page_images: studio/collaterals/clickup/review/v1/pages, revised: "7-review round 1: cover reads about 4:41; beat 2 drops 'already done' (a2 re-voiced, 32.1 s); coverage Shown in lists script only"}
  video: {path: none, bytes: 0, length: none, made_from: none, status: "not made: no signed-in session the recorder can use (Nebula's signed-in browser refuses to export its sign-in, and no person was present for kit/auth.mjs), and recording the beats would make live writes this stage must not make; open question by collaterals"}
  srt: {path: none, bytes: 0, made_from: none, status: "not made: made with the video"}
  deck: {path: studio/collaterals/clickup/out/ClickUp_Delivery_Command_Deck.pptx, bytes: 3417317, slides: 8, slide_images: studio/collaterals/clickup/review/v1/deck, made_from: v1, revised: "7-review round 1: slide 2 stat 48 h change routed to director then finance; slide 3 drops cell list and saved views; slide 4 caption matches the editor (screenshot not replaced, open question); slide 5 German and sign-off only, cropped above Geteilte Dokumente; slide 8 board crop without the Days to go-live tile"}
  check: "kit/check.py (after 7-review round 1): 0 must fix, 3 to verify (hood scenes e1, e2 have no screen text; one told-not-shown line in e1)"
  narrated_modes: "a1 Portfolio live (Storage reads), risk card named as AI-written, not live · a2 Project overview live (Move task) · b1 Resourcing live (Book consultant) · b2 Change request live (Submit and Decide change request) · c1 Customer portal live (Sign off deliverable) · d1 Weekly summary seeded snapshot, not AI; the Monday email a sample, not sent · d2 Copilot live agent and Publish status report · e1, e2 hood, live builder screens"
  notes:
    - "facts.json from the state's beats, entities and data rows plus the seed rows read live and read-only (Project, Booking, Change request, Deliverable, Weekly metric); the eval.csv and the internal notes file were not in this checkout, so internal.md is POC Studio's 'Internal notes · v1' row plus the state"
    - "deck screenshots taken read-only from the preview through Nebula's signed-in browser, cropped to drop the rail's user name; no write pressed"
    - "the story steers around known faults: beat 2 moves the already-done Validate pilot batch on to Training (not Mark done), beat 3 names no Lena Vogt percentages, beat 4 names no CR number and does not point at the feed, beat 7 does not export"

review:
  round: 2
  open:
    - "handover · p.3, beat 2 row · 2 · \"use a card's menu to move 'Validate pilot batch' to Done\" → \"move 'Validate pilot batch' on to Training from the card's menu\""
    - "handover · p.3, beat 5 row · 4 · \"in English, German and Japanese\" → \"in German\""
    - "handover · p.6, Sample prompts, second answer · 5, 6 · the 23 Oct time-entry line, the CNS-01 consultant id and the Tomas Brandt staffing line → dropped"
    - "handover · p.9, Change requests that route by the 40-hour rule · 5 · CR-0456 screenshot and \"A 60-hour change on Northgate Logistics\" → the beat's own Halden Freight change (48 h, EUR 7,200, +7 days)"
    - "handover · p.11, Before the demo · 5, 6 · the story-row reset note and the test-record list → removed from the handover"
    - "script · p.1, cover · 8 · about 4:41 against no audience time slot → unclear: confirm the audience minutes"
    - "deck · slide 4 · 4 · empty status report editor with \"Export it as PDF or Word\" and \"Use the Copilot's draft, or write the report here\" → the Copilot's draft in the editor"

decisions:
  - by: orchestrator
    when: 2026-10-22
    text: "Profile studio/profiles/clickup.md drafted by Studio from the POC row and the defaults."
  - by: orchestrator
    when: 2026-10-22
    text: "Preflight: the collateral kit (~/.local/poc-collateral/doctor.sh: ffmpeg, poppler, python packages) is not installed in this cloud box; it blocks G4 only. Chrome is Playwright's Chromium via CHROME_PATH; Bun 1.4.2, Slack read tools and the tenant sign-in are ok."

  - by: harvest
    when: 2026-10-22
    text: "harvest: the POC row's one input document (ClickUp-Delivery-Command-BRD.pdf) has an empty content field; the same file was read directly from its Slack post on the first attempt, so the \"Read input file\" automation was not run."
  - by: harvest
    when: 2026-10-22
    text: "harvest: BRD personas and stakeholder notes are quoted by role, not by the invented persona names; BRD table rows are quoted with their cells joined by \" | \"."
  - by: harvest
    when: 2026-10-22
    text: "harvest: BRD requirements marked Must (the default) are P0, as are the situations the screens \"must handle\" and the out-of-scope rule (\"must not suggest otherwise\"); R5 (Should) and the context sections are P1."

  - by: orchestrator
    when: 2026-10-22
    text: "Run 2 (cloud): the profile studio/profiles/clickup.md was not on this machine, so Studio drafted it again from the POC row and the defaults; tenant and solution are the folder's bound solution (POC Studio Live on orbit.uat.unifyapps.com). G1 approved on the POC row; the 11 G1 open questions have no reply in the thread, so they stay open for 2-plan."
  - by: plan
    when: 2026-10-22
    text: "plan: the AI surfaces follow the default except the controls off the demo path (timesheet approval, session booking, checklist answers, uploads, accepting proposed tasks, settings, saved views), which write through the code app's Storage dataSources instead of an automation each, so the automation count stays at the demo path's eight."
  - by: plan
    when: 2026-10-22
    text: "plan: A14 asks for light and dark; the design system's 'no toggle in the chrome' rule is kept by putting Appearance (Light, Dark) in the profile menu, light by default."
  - by: plan
    when: 2026-10-22
    text: "plan: brand-sample's logo pick was the ClickUp Brain 2 product mark (kept as studio/design-system/clickup/sampled-brain2-mark.svg, unused); ClickUp's own published logo files were fetched from clickup.com/assets/brand (logo-v3-clickup-dark.svg as logo.svg for the rail, logo-v3-clickup-light.svg as logo-on-light.svg, logo-v3-clickup-symbol-only.svg as logo-symbol.svg), used as published."
  - by: profile
    when: 2026-10-22
    text: "Brand colour sampled as ambiguous; the standing answer 'ambiguous brand colour: the recommended one, listed in the G2 pack' takes #5F55EE (hue 244, site variable --ProductScreen-CustomStatus-Primary). Other candidates: #6647F0 Core-Accents-Purple, #7612FA Table-Accent, #0091FF Core-Accents-Blue, #FF02F0 Core-Accents-Pink, #FC6D2D Core-Accents-Orange (all from clickup.com's site CSS)."
  - by: profile
    when: 2026-10-22
    text: "The AI agent's model is Nebula's recommendation (standing answer 'model: Nebula's recommendation')."
  - by: plan
    when: 2026-10-22
    text: "plan: external step probed read-only: Jira Connection (6ababb56207d2c4e18ad380c, active) answered jira_get_all_projects with KAN 'PS Chatbot' and SAM1 '(Example) Billing System Dev'; the step escalates a RAID risk to a DEMO-TEST Task in KAN, a bonus off the critical path, pending open question 15."

  - by: orchestrator
    when: 2026-10-22
    text: "state-check after 2-plan reverted 9 sections; all were false positives (the build_contract spec's own ## headings read as top-level sections, and gates/runs/stage_flag differed only by the orchestrator's own timestamp fix after the snapshot). The orchestrator restored 2-plan's output unchanged."
  - by: orchestrator
    when: 2026-10-22
    text: "POC Studio posted the G2 pack as a new top-level message (ts 1792662475.772399), not in the G1 thread; the state's thread now points at it, where G2 replies are read. POC Studio refused document type plan_sheet, so the plan sheet went as type scope, as a link (no Slack file attached)."
  - by: orchestrator
    when: 2026-10-22
    text: "Run 3 (cloud): G2 approved on the POC row (2026-10-22 15:21 IST); intent set to the proposed `both` (by the manager, through the G2 approval). No thread reply answered the G2 open questions, so they stay open and go into the G3 pack; the build follows build_contract as 2-plan wrote it."
  - by: orchestrator
    when: 2026-10-22
    text: "Run 3 (cloud): studio/design-system/clickup/ from run 2 was not in this container. client.css was regenerated with scripts/reskin.py transform --hue 244 (default secondary hue and saturation) from the design-system.md v3.4 stylesheet (count check ok); logo.svg, logo-on-light.svg and logo-symbol.svg were fetched again from clickup.com/assets/brand (logo-v3 files, as published). Profile studio/profiles/clickup.md was not here either; the POC row and defaults stand in for it."
  - by: orchestrator
    when: 2026-10-22
    text: "Run 3: build tasks' own test-row deletes (d_d101f6 Activity ACT-21 to ACT-24, d_f7eac3 Booking BKG-021 and BKG-022, d_89dc27 Change request CR-0457 and CR-0458) answered CONFIRM_REQUIRED; no person was in this scheduled session, so nothing was deleted and the rows are listed for the person. The Copilot's PDF and DOCX tool task failed on the platform (plan e_6ad9fa0ea965b115459b5300). The eval.csv from run 2 was not in this container; verify and handover used the three Copilot questions plus a refusal."
  - by: orchestrator
    when: 2026-10-23
    text: "Run 4 (cloud, scheduled): state restored from the POC row's demo_state (no local copy on branch claude/poc-POC-clickup-delivery-command-v2-20261022). G3 approved on the POC row. The folder is now bound to its own solution 'Clickup · ClickUp Delivery Command v2' (e_6adb0f9506a1ec756ed0ca89), not POC Studio Live. G4 not started: the poc-studio plugin (poc-collateral-studio, poc-collateral-setup) and ~/.local/poc-collateral are absent here; ffmpeg, poppler and Bun are present. The demo-studio version check could not run (raw URL 404)."
  - by: state-check
    when: 2026-10-23
    text: "reverted stage_flag: written by collaterals, outside its fields (schema § Who writes what)"
  - by: state-check
    when: 2026-10-23
    text: "reverted review: written by review, outside its fields (schema § Who writes what)"
  - by: orchestrator
    when: 2026-10-23
    text: "G4 round 1: poc-studio 1.17.2 installed in this cloud session (the container's setup predates 0.13.5); 7-review's 5 handover lines were not sent to 5-handover because the G3 handover source is not in this checkout; they go in the G4 pack as unverified"

dev_issues:
  - when: 2026-10-22
    text: "The agent ClickUp Delivery Copilot (e_6ad9e4db1a10ec0c912adab3, v8) has createDocxOrPdf attached, enabled and its capability on (get_agent), yet no model call is offered it: read_trace of cases e_6ada0866a965b115459d862d and e_6ada089ca965b115459d90d0 lists toolsOffered GenerateChartWithBlocks, think, ClarifyFromUser, read_delivery_data only. Beat 7 (export the status report as PDF) and H2 cannot show it; the build could not give it either (plan e_6ad9fa0ea965b115459b5300)."
    raised: 
  - when: 2026-10-22
    text: "In the code app preview every screen load logs errors from the platform runtime, not the app: '[fetch internal] error: signal is aborted without reason' for /api/entity-type, /api/workflow/execute/node, /api/lookup, /api/entity/e_ai_agent_settings (fetch-*.js), and 'WebSocket connection to wss://orbit.uat.unifyapps.com/mqtt failed: Unexpected response code: 426' every 5 s; while the Copilot panel answers it also logs 'Dynamic property not found at a path: undefined' and 'Dynamic path value is not a string at path: undefined' from the bundled SDK chunk index-cMPTQo7. Beats 1 to 7, read from the browser console logs of round 1 and round 2; the no-console-errors check fails on every screen for these alone."
    raised: 

frozen: {}

cost:
  runs: 5
  agent_spawns: 25
  tokens_m: 5.1
  wall_h: 4.9

open_questions:
  - by: harvest
    for: lead
    text: "The delivery director asks to \"see every project on one screen without scrolling\" (A113), while the BRD sizes the portfolio at 180 to 300 projects that need paging (A70). How should the portfolio screen answer A113? Options: (a) Recommended: headline counts, the risk grid and the first page of the project list fit one projector screen; paging below; (b) A compact wall of every seeded project with no scroll, which works only at demo size (15 to 20 projects); (c) Record A113 as declined, with the reason"
  - by: harvest
    for: lead
    text: "Consultants ask to \"edit the timeline straight from the phone\" (A114). The phone requirement (A60) covers today's tasks, status and time only. Should the phone edit timeline dates? Options: (a) Recommended: no; the phone keeps A60 and shows the timeline read-only; (b) Yes, with the same before-save go-live preview as the desktop timeline (A30)"
  - by: harvest
    for: lead
    text: "The VP of customer success says \"Show customers their health score\" (A115); implementation leads say \"Customers should never see internal health\" (A116). Which does the customer portal follow? Options: (a) Recommended: no internal health in the portal; it shows stage, milestones, sign-offs and open actions (A50); (b) A separate customer-facing health score, worded for the customer; (c) Show the internal health as it is"
  - by: harvest
    for: lead
    text: "The resource manager asks to \"Colour-code consultants by region everywhere\" (A117), but the BRD says meaning never depends on colour alone (A100). How is region shown? Options: (a) Recommended: a region word tag with a muted colour, in resourcing and portfolio screens only; (b) Region colour on every screen, always beside the region word; (c) No region colour; the region word only"
  - by: harvest
    for: lead
    text: "The BRD gives production volumes (A70 to A77: 180 to 300 projects, about 400 risks, about 3,000 time entries a week), while the profile sets 15 to 20 fictional rows. What volume is seeded? Options: (a) Recommended: 15 to 20 projects including the six sample customers (A82) and one story row, with tasks, risks and time scaled so every screen is full; paging and upload summaries still shown; (b) Seed at the BRD's volumes"
  - by: harvest
    for: lead
    text: "Salesforce, Slack, Google Drive and Jira (A102 to A105, A64), the weekly status post and the Monday email (A59): the profile allows only connections already on the tenant. How are these shown? Options: (a) Recommended: integration status, sync times and errors from seeded rows; a real send only where a matching connection already exists on the tenant, the rest shown as previews; (b) Create new connections for each system (needs credentials from the person, against the profile)"
  - by: harvest
    for: lead
    text: "The phone view (A60, A61, A69): the build is a Code Builder code app. How is the consultant's phone view delivered? Options: (a) Recommended: a phone layout of the same app at phone width, with the bottom tabs Today, Tasks, Time, Alerts; (b) A separate native mobile app"
  - by: harvest
    for: lead
    text: "The customer portal must be in English, German and Japanese (A55, A97). How much is translated for the demo? Options: (a) Recommended: every portal screen in all three languages, with a language switch and German text room for 30% growth (A77); (b) English throughout, with German and Japanese on the portal home only"
  - by: harvest
    for: lead
    text: "The BRD asks to \"Fetch the official logo\" (A9); the profile's standing answer for no logo is a text wordmark. Which applies? Options: (a) Recommended: fetch the official logo from clickup.com for every placement A9 lists; a text wordmark only if it cannot be fetched; (b) A text wordmark everywhere"
  - by: harvest
    for: lead
    text: "An earlier POC with this use case's first name exists (POC-clickup-delivery-command-20261022 on #click-up-test). Does v2 take asks from it? Options: (a) Recommended: no; v2 stands alone and the BRD shared in #clickup-test-2 is its input; (b) Also harvest the earlier channel's asks into v2"
  - by: harvest
    for: lead
    text: "Customer sponsors sign in to see only their own project (A50). How is the portal built? Options: (a) Recommended: a customer role in the same app with its own top menu (A68) and one demo sponsor user per sample customer; (b) A separate portal app"
  - by: plan
    for: owner
    text: "The BRD asks to take the typeface from the live site (A11); the Studio design system fixes Archivo and IBM Plex Mono. Which typeface? Options: (a) Recommended: the design system's Archivo and IBM Plex Mono with tabular figures so numbers line up, with Noto Sans JP for Japanese and room for 30% longer German; (b) ClickUp's site typeface, which moves the app off the design system's type scale"
  - by: plan
    for: owner
    text: "No beat shows the Admin area (A62 roles against permissions grid, A63 audit record filtered by person, project and action, A64 integration status with last sync and errors). How is it covered? Options: (a) Recommended: an Admin screen on the rail with the roles grid and integration status from seeded rows and the audit record from the Activity object, swept as controls, no beat (adds 1 page); (b) An Admin rail item that opens a plain 'Not in this demo' empty state, with A62 to A64 recorded as not shown"
  - by: plan
    for: owner
    text: "Five views the beats need are not in the design kit: the task timeline with dependencies and critical path (A30), the before and after plan diff (A41), the risk heatmap (A24), the CSV file drop (A53) and the notification tray (A61). How are they built? Options: (a) Recommended: built from the kit's tokens and doctrine, as the design system's 'Not in the kit' rule allows, never with new colour values; (b) The nearest kit part each: .tbl rows for the timeline and diff, a .tbl matrix for the heatmap, a plain .fld file input, a .menu for notifications"
  - by: plan
    for: owner
    text: "The one external step escalates RSK-1183 to Jira (A105). The only probed connection, 'Jira Connection' (active), points at a Jira site whose projects are 'PS Chatbot' (KAN) and '(Example) Billing System Dev', owned by another team. Use it? Options: (a) Recommended: yes, create one DEMO-TEST Task in KAN per demo run, listed for cleanup in the handover; (b) Drop the external step; Escalate to Jira shows a mocked key; (c) A ClickUp-team Jira sandbox, which needs a credential typed in the session at 3-build"
  - by: verify
    for: owner
    text: "Test rows on the tenant change what beats 3 and 4 show: Lena Vogt carries +8 h test bookings (BKG-021, BKG-022) plus this walk's booking in the weeks of 2 and 9 Nov, so beat 3 shows 100%, 80% instead of 80%, 60%; CR-0457, CR-0458 and CR-0459 exist, so the live request is CR-0460. Deleting them needs your own yes. Options: (a) Recommended: approve deleting the three Lena Vogt bookings and CR-0458/CR-0459 test rows before the demo; (b) keep them and change the beat words to the new numbers"
  - by: verify
    for: owner
    text: "Verify withheld three beat writes because they change the story row the earlier beats read: the finance partner's approval of the change request (moves Halden Freight's go-live to 4 Dec), the sponsor's sign-off of Migration plan v2, and Publish of the status report. Options: (a) Recommended: walk them in round 2 on a copy of the story row, or reset the row after the walk; (b) walk them on the story row and reset it by hand before the demo; (c) leave them unverified"
  - by: verify
    for: owner
    text: "A86 asks for a My projects toggle on Portfolio with its empty state for a user assigned to none; the screen has no such control. A95 (session-expiry dialog) and A94 (no-access project page with who can grant access) were not reachable in the walk. Options: (a) Recommended: add the My projects toggle and a route that shows the no-access page; record A95 as shown only by its code path; (b) record A86, A94 and A95 as not shown"
  - by: verify
    for: owner
    text: "Round 2 left more test rows on the tenant, on top of round 1's list: Change request CR-0460 (DEMO-TEST, director approved, waiting on the finance partner), so the live request in beat 4 will be numbered CR-0461; Activity ACT-34 and ACT-35 (Validate pilot batch moved to Training and back) and CR-0460's activity row. Lena Vogt still shows 100%, 80% in the weeks of 2 and 9 Nov, so beat 3 cannot show 80%, 60% until the round-1 bookings go. Deleting needs your own yes. Options: (a) Recommended: approve deleting the Lena Vogt test bookings and CR-0458 to CR-0460 with their activity rows before the demo; (b) keep them and change the beat words to the numbers on screen"
  - by: handover
    for: owner
    text: "The handover screenshots (1440 x 900, preview, 22 Oct 13:07Z to 13:11Z) show two faults not in verify's list: on Resourcing the 12-week grid runs under the open Copilot panel (columns from about Dec 21 sit behind it), and change request CR-0456 shows 'Approved by Raj Patel' under the finance step while its tag reads 'Pending approval: finance partner'. Options: (a) Recommended: add both to the next fix round with verify's open lines; (b) leave them; the presenter collapses the Copilot panel on Resourcing and does not open CR-0456"
  - by: collaterals
    for: owner
    text: "The demo video and its subtitles were not made in round 1: this cloud run had no signed-in session the recorder could use (no person to sign in, and Nebula's signed-in browser does not hand out its sign-in), and recording beats 2, 3, 4, 5 and 7 as written makes live writes (task move, booking, change request and both approvals, sign-off, publish) that the collaterals stage may not make. The script PDF and the deck are made. How should the video be recorded? Options: (a) Recommended: run 6-collaterals again in a session where you sign in once through the kit's browser window, after the test rows are cleaned up and the story row reset, and let it record the beats live (it writes the beat rows, which you reset after); (b) you screen-record the demo yourself from the script PDF and Studio adds the narration and subtitles; (c) record only the read-only parts (Portfolio, the refusal, Weekly summary, the hood beats) and leave the writes to the live demo"
  - by: collaterals
    for: owner
    text: "Screen against record, Customer portal (Halden Freight, Home, Shared documents): 'Migration plan v2' shows as shared on 30 Sept 2026, while Deliverable D-2611-2 (OBJ_cudc_deliverable) says shared_on 21 Oct 2026 and the plan is due 28 Oct. The script does not mention the shared date. Options: (a) Recommended: in the next fix round, make the Document row for Migration plan v2 on IMP-2611 carry 21 Oct 2026; (b) leave it; the presenter does not point at Shared documents"
  - by: collaterals
    for: owner
    text: "Deck slide 4 (7-review round 1) asks for a screenshot of the Copilot's AI-written status draft in the panel. No capture of it exists, the panel's History tab does not reopen past chats, and a fresh draft means sending the Copilot a prompt, which stores a conversation and an AI output row (like SR-2626-1): a live write this stage may not make. Slide 4 keeps the empty editor screenshot; only its caption was changed to match it. Options: (a) Recommended: in the next collaterals run, a session allowed to write asks 'Draft this week's status report for Halden Freight' once and the stage crops the panel's draft from that screen; (b) keep the editor screenshot as it is; (c) put the Copilot panel's suggested questions on slide 4 and change the caption to match"
---

build:
  plans:
    - {id: e_6ad9de45a965b1154595bf1e, tasks: 10, status: done, started: 2026-10-22T09:59Z, finished: 2026-10-22T10:04Z}
    - {id: e_6ad9df5ca965b1154595ddae, tasks: 10, status: done, started: 2026-10-22T10:04Z, finished: 2026-10-22T10:08Z}
    - {id: e_6ad9e045a965b11545960455, tasks: 10, status: done, started: 2026-10-22T10:08Z, finished: 2026-10-22T10:11Z}
    - {id: e_6ad9e11fceac1b55f2d8fa8b, tasks: 8, status: done, started: 2026-10-22T10:11Z, finished: 2026-10-22T10:24Z}
    - {id: e_6ad9e44cceac1b55f2d964ac, tasks: 10, status: done, started: 2026-10-22T10:24Z, finished: 2026-10-22T10:39Z}
    - {id: e_6ad9e7501a10ec0c912b63eb, tasks: 9, status: done, started: 2026-10-22T10:39Z, finished: 2026-10-22T11:23Z}
    - {id: e_6ad9fa0ea965b115459b5300, tasks: 4, status: 'failed: 1 task (Copilot PDF and DOCX tool, platform; its publish skipped)', started: 2026-10-22T12:02Z, finished: 2026-10-22T12:09Z}
    - {id: e_6ad9fb9f1a10ec0c912e8dc9, tasks: 9, status: done, started: 2026-10-22T12:09Z, finished: 2026-10-22T12:40Z}

## build_contract

# ClickUp Delivery Command

## Requested outcome
ClickUp's delivery team plans, staffs and reports on every implementation in one code app: a delivery director sees portfolio health and the projects at risk, an implementation lead runs one project (board, timeline, RAID, documents, change requests), a resource manager books consultants without going over capacity, a customer sponsor signs off and books training in a portal, and the VP reads the Monday summary. Delivery Copilot, a live read-only AI agent in a right-hand panel on every internal screen, answers questions with linked records or charts and drafts the weekly status report the lead edits and publishes. The story row is Halden Freight (IMP-2611), at risk of missing its 27 Nov 2026 go-live because data migration is running late.

## Touches
- object · ClickUp DC · Project · new
- object · ClickUp DC · Task · new
- object · ClickUp DC · RAID item · new
- object · ClickUp DC · Consultant · new
- object · ClickUp DC · Booking · new
- object · ClickUp DC · Time entry · new
- object · ClickUp DC · Change request · new
- object · ClickUp DC · Deliverable · new
- object · ClickUp DC · Session slot · new
- object · ClickUp DC · Checklist item · new
- object · ClickUp DC · Document · new
- object · ClickUp DC · Activity · new
- object · ClickUp DC · AI output · new
- object · ClickUp DC · Weekly metric · new
- object · ClickUp DC · Saved view · new
- automation · ClickUp DC · Read delivery data · new
- automation · ClickUp DC · Move task · new
- automation · ClickUp DC · Book consultant · new
- automation · ClickUp DC · Submit change request · new
- automation · ClickUp DC · Decide change request · new
- automation · ClickUp DC · Sign off deliverable · new
- automation · ClickUp DC · Publish status report · new
- automation · ClickUp DC · Escalate to Jira · new
- connection · Jira Connection · 6ababb56207d2c4e18ad380c
- ai-agent · ClickUp Delivery Copilot · new
- code-app · ClickUp Delivery Command · new

## Contract
- object · create · ClickUp DC · Project (`OBJ_cudc_project`): project_id (primaryKey, text, e.g. IMP-2611), customer, industry, region picklist (europe "Europe", north_america "North America", japan "Japan"), stage picklist (kickoff "Kickoff", discovery "Discovery", configuration "Configuration", migration "Migration", training "Training", go_live "Go-live", hypercare "Hypercare"), go_live_date (date, epoch ms), original_go_live_date (date), health picklist (on_track "On track", at_risk "At risk", off_track "Off track"), health_last_week (same codes), lead, seats (number), contract_value (number), currency picklist (usd "USD", eur "EUR", jpy "JPY"), budget_hours_planned (number), budget_hours_used (number), next_signoff (text), next_signoff_due (date), sponsor_name, ai_risk_confidence picklist (high "High", medium "Medium", low "Low", none "None"), ai_risk_evidence (long text), ai_written (boolean), week_change_rank (number), week_change_reason (text), source (text). Required: project_id, customer, region, stage, go_live_date, health, lead. logging.captureReporting on.
- object · create · ClickUp DC · Task (`OBJ_cudc_task`): task_id (primaryKey), project_id, title, description (long text), stage (the Project stage codes), status picklist (not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee, start_date (date), end_date (date), depends_on (text, task ids comma separated), critical (boolean), hours_logged (number), late (boolean), source picklist (manual "Manual", ai_accepted "AI proposal accepted"). Required: task_id, project_id, title, stage, status.
- object · create · ClickUp DC · RAID item (`OBJ_cudc_raid`): raid_id (primaryKey, e.g. RSK-1183), project_id, type picklist (risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title, likelihood (number 1-5), impact (number 1-5), owner, due_date (date), status picklist (open "Open", mitigating "Mitigating", closed "Closed"), history (long text), jira_key (text). Required: raid_id, project_id, type, title, status.
- object · create · ClickUp DC · Consultant (`OBJ_cudc_consultant`): consultant_id (primaryKey), name, role picklist (lead "Implementation lead", consultant "Implementation consultant"), region (the Project region codes), weekly_capacity_hours (number), skill_data_migration, skill_integrations, skill_admin_training, skill_api, skill_japanese (numbers 0-5). Required: consultant_id, name, region, weekly_capacity_hours.
- object · create · ClickUp DC · Booking (`OBJ_cudc_booking`): booking_id (primaryKey), consultant_id, project_id, week_start (date, a Monday), hours (number). Required: booking_id, consultant_id, project_id, week_start, hours.
- object · create · ClickUp DC · Time entry (`OBJ_cudc_time_entry`): entry_id (primaryKey), consultant_id, project_id, task_id, entry_date (date), hours (number), timesheet_week (date), status picklist (submitted "Pending approval", approved "Approved", returned "Returned"), return_reason (text). Required: entry_id, consultant_id, task_id, entry_date, hours, status.
- object · create · ClickUp DC · Change request (`OBJ_cudc_change_request`): cr_id (primaryKey, e.g. CR-0457), project_id, reason (long text), work_change (long text), hours_delta (number), cost_delta (number), go_live_delta_days (number), plan_before (long text, JSON), plan_after (long text, JSON), status picklist (draft "Draft", pending_director "Pending approval: delivery director", pending_finance "Pending approval: finance partner", approved "Approved", rejected "Rejected"), director_decision_by, director_decision_at (date), finance_decision_by, finance_decision_at (date), reject_reason (text), raised_by, raised_at (date). Required: cr_id, project_id, reason, hours_delta, status.
- object · create · ClickUp DC · Deliverable (`OBJ_cudc_deliverable`): deliverable_id (primaryKey), project_id, stage (Project stage codes), title, due_date (date), status picklist (awaiting_signoff "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), decided_by, decided_at (date), comment (text), shared_on (date). Required: deliverable_id, project_id, title, status.
- object · create · ClickUp DC · Session slot (`OBJ_cudc_session_slot`): slot_id (primaryKey), project_id, session_title, slot_start (date-time, epoch ms), duration_minutes (number), taken (boolean), booked_by (text). Required: slot_id, project_id, slot_start, taken.
- object · create · ClickUp DC · Checklist item (`OBJ_cudc_checklist_item`): item_id (primaryKey), project_id, position (number), question, answer (text, empty when not answered), status picklist (not_set "Not set", answered "Answered"). Required: item_id, project_id, position, question, status.
- object · create · ClickUp DC · Document (`OBJ_cudc_document`): document_id (primaryKey), project_id, name, doc_type picklist (sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", user_list "User list", meeting_notes "Meeting notes"), body (long text, shown in the in-app viewer), shared_with_customer (boolean), uploaded_by, uploaded_at (date), row_count (number), error_rows (number). Required: document_id, project_id, name, doc_type.
- object · create · ClickUp DC · Activity (`OBJ_cudc_activity`): activity_id (primaryKey), project_id, kind picklist (change "Change", notification "Notification", integration "Integration status"), actor, action, detail (text), at (date-time, epoch ms), read (boolean), recipient (text), integration picklist (salesforce "Salesforce", slack "Slack", google_drive "Google Drive", jira "Jira"), integration_status picklist (live "Live", sync_failed "Sync failed"). Required: activity_id, kind, actor, action, at.
- object · create · ClickUp DC · AI output (`OBJ_cudc_ai_output`): output_id (primaryKey), project_id, kind picklist (status_report "Status report", meeting_summary "Meeting summary", proposed_task "Proposed task"), title, body (long text), transcript (long text with anchors t1..tn), source_anchor (text), status picklist (draft "Draft", published "Published", proposed "Proposed", accepted "Accepted", rejected "Rejected"), ai_written (boolean), week_of (date), published_by, published_at (date). Required: output_id, kind, title, status, ai_written.
- object · create · ClickUp DC · Weekly metric (`OBJ_cudc_weekly_metric`): metric_id (primaryKey), kind picklist (trend "On-track share", headline "Headline number", bridge "Value bridge"), week_of (date), label, value (number), last_week_value (number), unit (text), good_when picklist (up "Higher is better", down "Lower is better"), bridge_start, bridge_new, bridge_completed, bridge_slipped, bridge_cancelled, bridge_end (numbers, USD). Required: metric_id, kind, label.
- object · create · ClickUp DC · Saved view (`OBJ_cudc_saved_view`): view_id (primaryKey), name, owner, shared_with (text), filters (long text, JSON of region, stage, health, lead, search). Required: view_id, name, owner, filters.
- record · seed · ClickUp DC · Project: 20 rows, contract values in the contract currency. IMP-2611 Halden Freight, Logistics, europe, migration, go-live 2026-11-27 (original 2026-11-27), at_risk (last week on_track), lead Mira Castell, 4,800 seats, 312,000 eur, budget 640 h planned / 512 h used, next sign-off "Migration plan v2" due 2026-10-28, sponsor Katrin Albers, ai_risk_confidence high, ai_risk_evidence "3 of 8 migration tasks are late (longest 6 days); Migration plan v2 sign-off is due 28 Oct and not yet approved; Tomas Brandt is booked 100% in week 45", ai_written true, week_change_rank 1, week_change_reason "Health moved to At risk: migration tasks late"; IMP-2612 Corvia Health, Healthcare, north_america, configuration, 2026-12-15, on_track/on_track, Dev Okafor, 12,000, 540,000 usd, 1,400/610 h; IMP-2613 Brightmoor University, Education, europe, training, 2026-11-10, on_track/on_track, Mira Castell, 2,300, 118,000 eur, 380/341 h; IMP-2614 Kestrel Energy, Energy, north_america, discovery, 2027-01-29, on_track/on_track, Dev Okafor, 7,500, 365,000 usd, 900/96 h; IMP-2615 Sakura Mobility, Automotive, japan, go_live, 2026-11-05, at_risk/at_risk, Haruto Mori, 9,200, 61,000,000 jpy, 1,100/1,032 h, ai_risk_confidence medium, evidence "Cutover rehearsal failed once; 2 open issues", ai_written true, week_change_rank 4, reason "Second cutover rehearsal booked"; IMP-2616 Ostrander Retail, Retail, north_america, hypercare, 2026-10-06, on_track/on_track, Dev Okafor, 650, 42,000 usd, 160/158 h; IMP-2617 Vellmar Insurance, Insurance, europe, configuration, 2026-12-04, on_track/on_track, Sofia Lind, 3,100, 164,000 eur; IMP-2618 Northgate Logistics, Logistics, north_america, migration, 2026-11-19 (original 2026-11-05), off_track/off_track, Dev Okafor, 5,400, 288,000 usd, week_change_rank 3, reason "Go-live slipped 14 days"; IMP-2619 Tamura Electronics, Manufacturing, japan, training, 2026-11-24, on_track/on_track, Haruto Mori, 4,100, 27,500,000 jpy; IMP-2620 Calder Bank, Banking, europe, kickoff, 2027-02-12, on_track/on_track, Sofia Lind, 8,800, 410,000 eur, week_change_rank 5, reason "New project from won deal"; IMP-2621 Pinecrest Media, Media, north_america, configuration, 2026-12-09, at_risk/at_risk, Priya Nair, 1,900, 96,000 usd; IMP-2622 Aoba Pharma, Pharma, japan, discovery, 2027-01-20, on_track/on_track, Haruto Mori, 2,600, 18,000,000 jpy; IMP-2623 Lindqvist Marine, Marine, europe, go_live, 2026-10-30, on_track/on_track, Mira Castell, 1,200, 71,000 eur; IMP-2624 Redfern Clinics, Healthcare, north_america, training, 2026-11-13, on_track/on_track, Priya Nair, 3,300, 152,000 usd; IMP-2625 Hokuto Rail, Transport, japan, migration, 2026-12-18 (original 2026-12-04), off_track (last week at_risk), Haruto Mori, 6,700, 44,000,000 jpy, week_change_rank 2, reason "Health moved to Off track: go-live slipped 14 days"; IMP-2626 Marlow Studios, Media, europe, hypercare, 2026-10-01, on_track/on_track, Sofia Lind, 800, 39,000 eur; IMP-2627 Bayview Credit Union, Banking, north_america, kickoff, 2027-02-26, on_track/on_track, Priya Nair, 2,100, 88,000 usd; IMP-2628 Eskel Foods, Food, europe, configuration, 2026-12-11, at_risk (last week on_track), Sofia Lind, 3,900, 176,000 eur, ai_risk_confidence medium, evidence "Integration tasks 4 days late", ai_written true; IMP-2629 Granite Peak Outdoor, Retail, north_america, go_live, 2026-11-03, on_track/on_track, Dev Okafor, 1,500, 64,000 usd; IMP-2630 Kawase Logistics, Logistics, japan, configuration, 2026-12-22, on_track/on_track, Haruto Mori, 5,200, 33,000,000 jpy. Every other row: ai_risk_confidence none, ai_written false, source "Salesforce opportunity (won)".
- record · seed · ClickUp DC · Task: 20 rows, all on IMP-2611. T-2611-01 "Kickoff workshop" kickoff done; T-2611-02 "Discovery interviews" discovery done; T-2611-03 "Workspace configuration" configuration done; T-2611-04 "Permission model" configuration done; T-2611-05 to T-2611-20 in stage migration (16 tasks, one more than the column limit of 15): 05 "Extract legacy projects" done; 06 "Map custom fields" done; 07 "Clean duplicate users" done; 08 "Load pilot batch" done; 09 "Validate pilot batch" in_progress; 10 "Load batch 1 (Logistics ops)" in_progress, late, assignee Tomas Brandt, 2026-10-12 to 2026-10-23, critical; 11 "Load batch 2 (Finance)" not_started, late, depends_on T-2611-10, critical, 2026-10-26 to 2026-11-06; 12 "Load batch 3 (Warehouses)" not_started, late, depends_on T-2611-11, critical, 2026-11-09 to 2026-11-13; 13 "Reconcile record counts" not_started, depends_on T-2611-12, critical; 14 "Migrate attachments" not_started; 15 "Rebuild automations" in_progress; 16 "Map integrations" in_progress; 17 "Data quality sign-off pack" not_started; 18 "Cutover runbook" not_started; 19 "Cutover rehearsal" not_started, depends_on T-2611-13, critical, 2026-11-16 to 2026-11-20; 20 "Go-live readiness review" blocked, depends_on T-2611-19, critical, 2026-11-23 to 2026-11-26. Assignees from the Consultant seed; hours_logged on done and in_progress rows.
- record · seed · ClickUp DC · RAID item: 20 rows. RSK-1183 IMP-2611 risk "Legacy data migration running late" likelihood 4 impact 4 owner Mira Castell due 2026-10-30 open, history "15 Oct raised; 20 Oct likelihood 3 to 4"; RSK-1184 IMP-2611 risk "Customer sign-off of migration plan delayed" 3/4 open; ASM-0311 IMP-2611 assumption "Customer provides user list by 6 Nov"; ISS-0522 IMP-2611 issue "Duplicate user records in legacy export" open; DEC-0207 IMP-2611 decision "Migrate attachments after go-live" closed; and 15 risks across the other projects spread over the 5x5 grid, at least one in every row of likelihood, with RSK-1190 Sakura Mobility 4/5, RSK-1191 Northgate Logistics 5/4, RSK-1192 Hokuto Rail 5/5, RSK-1193 Pinecrest Media 3/3, RSK-1194 Eskel Foods 3/4.
- record · seed · ClickUp DC · Consultant: 12 rows. Tomas Brandt consultant europe 40 h, data migration 5, integrations 3, admin training 2, API 3, Japanese 0; Lena Vogt consultant europe 40 h, data migration 4, integrations 2, admin training 3, API 2, Japanese 3; Aiko Tanaka consultant japan 40 h, API 4, Japanese 5, data migration 3; Marcus Bell consultant north_america 40 h, integrations 4, API 4; Nora Quist consultant europe 32 h, admin training 5; Elif Demir consultant europe 40 h, API 3, integrations 3; Sam Whitlow consultant north_america 40 h, data migration 3; Kenji Ono consultant japan 40 h, admin training 4, Japanese 5; Mira Castell lead europe 40 h; Dev Okafor lead north_america 40 h; Haruto Mori lead japan 40 h, Japanese 5; Priya Nair lead north_america 40 h.
- record · seed · ClickUp DC · Booking: 20 rows over weeks starting 2026-10-26, 2026-11-02, 2026-11-09, 2026-11-16. Tomas Brandt: week 2026-11-02 24 h IMP-2611 and 16 h IMP-2618 (100%); week 2026-11-09 24 h IMP-2611 and 10 h IMP-2618 (85%); Lena Vogt: week 2026-11-02 24 h IMP-2613 (60%); week 2026-11-09 16 h IMP-2613 (40%); Aiko Tanaka: week 2026-11-16 28 h IMP-2615 and 16 h IMP-2619 (110%, the one seeded over-capacity week); the remaining 13 rows give each other consultant 24 to 36 h in two of the four weeks.
- record · seed · ClickUp DC · Time entry: 20 rows for timesheet week 2026-10-19: Tomas Brandt 10 entries on IMP-2611 tasks T-2611-09 and T-2611-10 (36 h, submitted); Lena Vogt 6 entries on IMP-2613 (24 h, submitted); Sam Whitlow 4 entries on IMP-2618 (12 h, returned, return_reason "Hours on 21 Oct are logged against a closed task. Move them to T-2618 data load and resubmit.").
- record · seed · ClickUp DC · Change request: 2 rows. CR-0455 IMP-2615 "Add a second cutover rehearsal" +24 h, +3,000,000 jpy, 0 days, approved by Haruto Mori's director Ines Moreau on 2026-10-14; CR-0456 IMP-2618 "Re-map warehouse codes" +60 h, +9,000 usd, +14 days, pending_finance, director approval by Ines Moreau 2026-10-20, finance partner Raj Patel next. CR-0457 is created live in the demo.
- record · seed · ClickUp DC · Deliverable: 8 rows. D-2611-1 IMP-2611 configuration "Configuration workbook" signed_off by Katrin Albers 2026-10-02 (shared 2026-09-30); D-2611-2 IMP-2611 migration "Migration plan v2" awaiting_signoff due 2026-10-28, shared 2026-10-21; D-2611-3 IMP-2611 training "Training plan" awaiting_signoff due 2026-11-12; D-2611-4 IMP-2611 discovery "Discovery report" signed_off 2026-09-12; four more on IMP-2613, IMP-2615, IMP-2618, IMP-2623 (one changes_requested with comment).
- record · seed · ClickUp DC · Session slot: 12 rows, IMP-2611 "Admin training", 90 minutes, three days (2026-11-16, 2026-11-17, 2026-11-18) at 09:00, 11:00, 14:00 and 16:00 Europe/Berlin; four taken (booked_by "Jonas Feld" or "Katrin Albers").
- record · seed · ClickUp DC · Checklist item: 10 rows on IMP-2611 at positions 1 to 10: Admin contacts, SSO provider, Workspace name, Data residency, User list owner, Default language, Time zone, Working week, Integrations to enable, Go-live communication date; positions 1, 2, 3, 4, 6, 7 and 8 answered (for example Time zone "Europe/Berlin"), positions 5, 9 and 10 not_set with an empty answer.
- record · seed · ClickUp DC · Document: 8 rows on IMP-2611: "Statement of work" sow (shared), "Migration plan v2" migration_plan (shared), "Sign-off record: Configuration workbook" signoff_record (shared), "Steering call notes 20 Oct" meeting_notes (internal), "Halden user list (pilot)" user_list uploaded by Katrin Albers, 1,250 rows, 0 errors; plus "Statement of work" for IMP-2613, IMP-2615, IMP-2618. Each body holds the readable text the viewer shows.
- record · seed · ClickUp DC · Activity: 20 rows in the last 14 days, newest 2026-10-22 06:40: one integration row "Jira sync failed since 06:40 today: 3 escalation links on Halden Freight and Northgate Logistics not updated" (jira, sync_failed); three integration rows live for Salesforce, Slack and Google Drive with last sync times; 8 change rows on IMP-2611 (task moved, date changed, RSK-1183 likelihood raised, sign-off shared); 8 notification rows for Mira Castell (new assignment, sign-off received, mention), 5 unread.
- record · seed · ClickUp DC · AI output: 6 rows on IMP-2611: SR-2611-W42 status_report published 2026-10-16 by Mira Castell, ai_written true; MS-2611-1020 meeting_summary "Steering call 20 Oct" with decisions, actions and risks each carrying an anchor (t3, t7, t12) into the transcript field, ai_written true; PT-2611-1 "Book second cutover rehearsal", PT-2611-2 "Send user list template to Katrin Albers", PT-2611-3 "Add Warehouses batch owner" as proposed_task proposed, ai_written true, source_anchor set; one rejected proposed task.
- record · seed · ClickUp DC · Weekly metric: 19 rows. 12 trend rows, weeks 2026-08-03 to 2026-10-19, on-track share 85, 85, 90, 90, 85, 85, 80, 80, 85, 80, 80, 70 percent; 6 headline rows for week 2026-10-19: Active projects 18 (last week 17, up), Go-lives this month 3 (3, up), Projects at risk 6 (4, down), Average days to go-live 47 (44, down), Consultant utilisation 91 % (88, up), Contract value awaiting go-live 4,210,000 USD (4,050,000, up); 1 bridge row for September to October, USD: start 4,050,000, new 410,000, completed 180,000, slipped 0, cancelled 70,000, end 4,210,000.
- record · seed · ClickUp DC · Saved view: 2 rows: "Europe at risk" (region europe, health at_risk and off_track) owner Ines Moreau shared with "Europe delivery leads"; "Japan go-lives" owner Ines Moreau, private.
- automation · create · ClickUp DC · Read delivery data: callable, read-only, the agent's one tool. Inputs entity (project, task, raid, consultant, booking, time_entry, change_request, deliverable, ai_output, weekly_metric), filters (JSON of field and value pairs), limit (default 50). Answers rows (the records with every field, and for projects their link path `/projects/{project_id}/overview`) and count. Writes nothing.
- automation · create · ClickUp DC · Move task: callable. Inputs task_id, to_stage, actor. Updates the Task stage, writes one Activity change row "moved {task} to {stage}". Result moved, or not_found.
- automation · create · ClickUp DC · Book consultant: callable. Inputs consultant_id, project_id, week_starts (list of Monday dates), hours_per_week, actor, confirm (boolean). For each week, sums existing Booking hours plus the new hours against weekly_capacity_hours. Any week over 100% answers result over_capacity with lines [{week_start, booked_hours, capacity, percent, over_by_hours}] and writes nothing. Otherwise writes one Booking per week and an Activity row and answers booked with the new percentages.
- automation · create · ClickUp DC · Submit change request: callable. Inputs project_id, reason, work_change, hours_delta, cost_delta, go_live_delta_days, plan_before, plan_after, actor. Refuses an empty reason (result missing_reason). Next number after the highest cr_id (CR-0457 in the demo). Under 40 h: status pending_director; 40 h or more: pending_director, then pending_finance. Writes the Change request and an Activity row; answers cr_id, status and approvers ["Ines Moreau (delivery director)", "Raj Patel (finance partner)" when 40 h or more].
- automation · create · ClickUp DC · Decide change request: callable. Inputs cr_id, decision (approve, reject), reason, actor. A reject with an empty reason answers reason_required and writes nothing. An approve at pending_director with hours_delta 40 or more moves to pending_finance; an approve at pending_finance, or at pending_director under 40 h, sets approved, adds hours_delta to the Project budget_hours_planned and go_live_delta_days to go_live_date, and writes an Activity row "CR-{n} approved: plan updated". A reject sets rejected with reject_reason and an Activity row.
- automation · create · ClickUp DC · Sign off deliverable: callable. Inputs deliverable_id, decision (sign_off, request_changes), comment, actor. request_changes with an empty comment answers comment_required. Sets status, decided_by, decided_at (now), writes an Activity change row and a notification row for the project lead.
- automation · create · ClickUp DC · Publish status report: callable. Inputs project_id, title, body, actor, ai_written (boolean). Writes an AI output row kind status_report, status published, published_by, published_at (now), and an Activity row "Weekly status published".
- automation · create · ClickUp DC · Escalate to Jira: callable, the external step. Inputs raid_id, actor. Creates one Jira issue of type Task in project KAN on connection Jira Connection (6ababb56207d2c4e18ad380c) with summary "DEMO-TEST 2026-10-22 {raid_id}: {title}" and label DEMO-TEST, stores the returned key in the RAID item jira_key and writes an Activity row. Answers jira_key, or jira_unavailable with the error text.
- ai-agent · create · ClickUp Delivery Copilot: model Nebula's recommendation; read-only; one tool ClickUp DC · Read delivery data, plus the platform's Generate Chart Tool and Generate PDF and DOCX Tool; instructions: answers delivery questions in plain, calm words from the tool's rows only, links every project it names to `/projects/{project_id}/overview`, answers with a chart (brand colours, units on both axes) when asked for hours by stage or go-lives by month, drafts the weekly status report for a project from its tasks, RAID items and time entries labelled "AI-written draft", summarises a meeting into decisions, actions and risks citing transcript anchors, proposes tasks only as a list for the user to accept, flags projects likely to miss go-live with a confidence and evidence, declines billing, invoicing, revenue, pay, hiring and performance questions as out of scope, and says plainly when the data does not hold an answer and what to ask instead. Three suggested questions: "Which Europe projects go live in November and are at risk?", "Draft this week's status report for Halden Freight", "Show go-lives by month".
- code-app · create · ClickUp Delivery Command: the shell: the design system stylesheet, the fonts, the rail (ClickUp logo, Portfolio, Projects, Resourcing, Timesheets, Changes, Admin, the profile at the bottom), the header (current view, search, notifications bell, profile menu), the Delivery Copilot right-hand panel, the routes /portfolio, /projects/:projectId/overview, /resourcing, /changes/:crId/detail, /summary/weekly, /portal/home; PRIVATE; light theme by default with the dark tokens live and an Appearance choice in the profile menu.
- code-app · update · ClickUp Delivery Command: screen Portfolio: health tiles On track, At risk, Off track with change since last week (`.tile` `.delta`); the AI Insight risk prediction card for Halden Freight with confidence and evidence and one action Open project (`.ai:not(.msg)`); the likelihood by impact risk grid with counts, a cell click listing its risks (`.tbl` as a 5x5 matrix, `.tag` cells); go-lives in the next 90 days by region with slipped dates marked (`.chart`); 12-week on-track share (`.chart` `.spark`); the project table with search "x of y", facets region, stage, health, lead as removable chips with Clear all, Save view and a saved views menu, customer monogram circles, paging at 10 rows (`.toolbar` `.field` `.chipsel` `.tblwrap` `.tbl` `.pg` `.av` `.menu`); the Jira sync failed note with last-updated time (`.note`); reads Project, RAID item, Weekly metric, Saved view, Activity.
- code-app · update · ClickUp Delivery Command: screen Project overview: crumb, the seven stages path, tiles days to go-live, budget hours used against planned, open risks, next customer sign-off (`.crumb` `.stages` `.tile` `.prog`); tabs Board, List, Timeline, RAID, Documents, Activity, Settings (`.tabs`); Board one column per stage with a column limit warning over 15 and Move to stage menu as the keyboard path (`.kb` `.menu`); task detail side panel with description, assignee, dates, time logged, comments, attachments and Log time (`.g3` `.fld` `.feed`); Timeline bars with dependencies and critical path, a date change shifting dependants and previewing the new go-live before Save (built from tokens); RAID log with Escalate to Jira on a risk (`.tbl` `.tag`); Documents with the in-app viewer (`.tbl` `.g3`); Activity feed (`.feed`); Settings edited in place with unsaved, saving, saved, failed states (`.fld` `.tag`); Draft status report opens the Copilot; calls ClickUp DC · Move task on a card move, ClickUp DC · Escalate to Jira on Escalate; reads Project, Task, RAID item, Document, Activity, Time entry; writes Task dates, Time entry and Project settings through Storage.
- code-app · update · ClickUp Delivery Command: screen Resourcing: tabs Grid, Skills, Timesheets, Capacity (`.tabs`); Grid consultants against 12 weeks with booked percent, over 100% flagged with icon and word (`.tbl` `.tag`); Book consultant form person, project, weeks, hours, no dragging (`.fld` `.ctl` `.seg` `.btn-p`); the refusal "Over capacity" naming who, which weeks and by how much before saving (`.tag.negative` `.note`); Skills matrix with levels (`.tbl`); Timesheets with select and Approve, Return with a required reason (`.tbl` `.fld` `.btn`); Capacity booked against capacity by region for the quarter (`.chart`); calls ClickUp DC · Book consultant; reads Consultant, Booking, Time entry; writes Time entry status through Storage.
- code-app · update · ClickUp Delivery Command: screen Change request: new request form reason, work added or removed, hours, cost, go-live effect (`.fld` `.ctl`); plan before and after side by side with differences marked (built from tokens); approval path with who approved and who is next (`.sth`); Approve, Reject with a required written reason (`.btn-p` `.btn-s` `.fld` `.err`); calls ClickUp DC · Submit change request and ClickUp DC · Decide change request; reads Change request, Project, Task.
- code-app · update · ClickUp Delivery Command: screen Customer portal: ClickUp logo and the customer's circle in the header; top menu Home, Sign-offs, Sessions, Files, Checklist (`.tabs`); English, Deutsch, 日本語 switch (`.seg`) with every portal string in three languages and dates in the language's format; Home stage, milestones, upcoming sessions, open actions, shared documents, no internal health (`.stages` `.stv` `.tbl`); Sign-offs with Sign off and Request changes with a comment (`.g2` `.btn-p` `.btn-s` `.fld`); Sessions day then time slot, taken slots visible and disabled (`.cal` `.slot`); Files upload of a CSV with row errors summarised and fixable before Confirm (file drop built from tokens, `.tbl` `.note`); Checklist of 10 items with unanswered ones shown as Not set (`.opt` `.tag.neutral`); a project the sponsor cannot open says who can grant access; calls ClickUp DC · Sign off deliverable; reads Project, Deliverable, Session slot, Document, Checklist item; writes Session slot, Checklist item and Document through Storage.
- code-app · update · ClickUp Delivery Command: screen Weekly summary: six headline tiles with change from last week coloured by good or bad for the business (`.tile` `.delta`); contract value bridge new, completed, slipped, cancelled (`.chart`); five projects that changed most with the reason (`.tbl`); preview of the Monday 08:00 email per region time zone (`.g2` `.note`); reads Weekly metric, Project.
- code-app · update · ClickUp Delivery Command: the Copilot panel and status report: the real ClickUp Delivery Copilot in the right-hand panel on every internal screen with its three suggested questions, the stage it is on while working, and why plus what to try when it cannot answer (`.canvas` `.convo` `.msg.me` `.msg.ai` `.chips` `.stages`); the status report editor with the AI-written draft, edit, Publish, Export PDF and Word (`.ai:not(.msg)` `.ctl` `.btn-p` `.btn-s`); Proposed tasks from the meeting summary with Accept and Reject, nothing created without Accept (`.tbl`); the meeting summary with each point linking to its transcript anchor (`.feed`); calls ClickUp DC · Publish status report; reads AI output; writes Task and AI output status through Storage on Accept or Reject.

## Business rules
- Every status shows an icon and a word, never colour alone: On track, Signed off, Approved, Live are positive; At risk, Awaiting sign-off, Over capacity, Pending approval are attention; Off track, Blocked, Rejected, Sync failed are negative; Not started, Draft, Scheduled, Hypercare are neutral.
- A booking that takes a consultant over 100% of weekly capacity in any week is refused before saving, naming who, which weeks and by how much.
- Change requests under 40 hours need the delivery director; 40 hours or more need the director, then the finance partner, in that order. Rejecting needs a written reason. An approved change updates the plan and is recorded in the activity feed.
- A sign-off records who approved and when; Request changes needs a comment.
- Nothing the Copilot proposes is created without the user's Accept. Anything AI wrote is labelled AI-written.
- The customer portal never shows internal health.
- An unanswered checklist item shows Not set, never a guessed value.
- Money shows in the contract currency; the weekly summary totals are in USD.
- Weeks start on Monday in Europe and Japan and on Sunday in North America; times show the user's time zone.
- Errors say what happened and what to do next; no jokes or exclamation marks.
- The app never offers billing, invoicing, revenue recognition, workspace building, hiring, performance reviews, payroll, a marketing site, video calls or offline use.
- Rules: the stylesheet is studio/design-system/clickup/client.css (absolute /root/poc/POC-clickup-delivery-command-v2-20261022/studio/design-system/clickup/client.css), hue 244 from #5F55EE; the rail logo is studio/design-system/clickup/logo.svg (ClickUp's own light-on-dark logo), logo-on-light.svg for light surfaces and documents, logo-symbol.svg for the browser tab icon; logos used as published, never redrawn or recoloured.
- Rules: Jira test records are labelled DEMO-TEST with the demo's date.

## Ready when
- The director sees portfolio health 14 On track, 4 At risk, 2 Off track and the Halden Freight risk flag on Portfolio.
- Booking Tomas Brandt for 8 h in the week of 2 Nov is refused as Over capacity (120%, 8 h over) and booking Lena Vogt succeeds.
- CR-0457 for 48 h routes to the director, then the finance partner, and its approval moves Halden Freight's plan.
- The sponsor signs off Migration plan v2 in German and the sign-off appears in the project's activity feed.
- Delivery Copilot answers "Which Europe projects go live in November and are at risk?" with Halden Freight and drafts its status report, which the lead publishes.
- deploy ClickUp DC · Read delivery data
- deploy ClickUp DC · Move task
- deploy ClickUp DC · Book consultant
- deploy ClickUp DC · Submit change request
- deploy ClickUp DC · Decide change request
- deploy ClickUp DC · Sign off deliverable
- deploy ClickUp DC · Publish status report
- deploy ClickUp DC · Escalate to Jira
- publish ClickUp Delivery Copilot
- publish ClickUp Delivery Command

## Assumptions
- Check this: intent proposed as `both` (the outcome first, then two hood beats: the Book consultant automation and the Copilot in the agent builder); the owner sets it at G2.
- Check this: 15 to 20 fictional rows per object (20 projects including the six BRD sample customers), not the BRD's production volumes; paging shows at 10 rows per page.
- Check this: brand colour #5F55EE (ClickUp site variable --ProductScreen-CustomStatus-Primary), sampled as ambiguous and taken as recommended under the profile's standing answer.
- Check this: logo is ClickUp's own published logo-v3 files from clickup.com/assets/brand; the sampler's first pick was the ClickUp Brain mark and was not used.
- Check this: the typeface is the design system's Archivo and IBM Plex Mono with tabular figures, with system Japanese fallbacks, not the site's typeface.
- Check this: the portal is a route of the same app viewed as the sponsor Katrin Albers; real customer logins and a customer role need governance tools the builders lack.
- Check this: the phone view, Admin screen, Salesforce, Slack, Google Drive and the Monday email are not built until the owner answers their open questions.
- Check this: controls off the demo path (timesheet approval, slot booking, checklist answers, uploads, task accept, settings, saved views) write through the app's Storage dataSources rather than automations.
- Check this: the risk prediction, the meeting summary, proposed tasks and last week's status report are seeded rows marked AI-written; the Copilot's answers and the new status draft are live.
- Check this: today is 2026-10-22; dates are in the last 90 days or the next 120.
- Check this: Jira project KAN on the existing Jira Connection is the escalation target.

### Capability check
| Contract line | Beat | Builder | Tool that makes it | Read that proves it | Result |
|---|---|---|---|---|---|
| 15 objects | all | fde-agent | apply_object_batch | get_objects | ok |
| 15 record seeds (2 to 20 rows each, none over 20) | all | fde-agent | apply_record_edits | get_records | ok |
| Read delivery data | 7 | automation-agent | compile_and_save_workflow, deploy_workflow | describe_callable_workflow, search_workflows, trigger_workflow_run | ok |
| Move task, Book consultant, Submit and Decide change request, Sign off deliverable, Publish status report | 2, 3, 4, 5, 7 | automation-agent | compile_and_save_workflow, deploy_workflow | search_workflows deployment, trigger_workflow_run then inspect_workflow_run | ok |
| Escalate to Jira (jira_create_issue on Jira Connection, active) | 2 control | automation-agent | compile_and_save_workflow | inspect_workflow_run; jira_get_issue read-back | ok (pending open question 15) |
| ClickUp Delivery Copilot with Read delivery data, Generate Chart Tool, Generate PDF and DOCX Tool | 7, H2 | agent-builder | create_agent, add_tools, publish_agent | get_agent, send_test_messages | ok |
| code-app create and 7 screen updates | 1 to 7 | code-app-agent | create_code_app, create_code_app_data_sources, push_code_patch | get_code_app head.sha, bindings.ts FETCH id, callables.ts blocks | ok |
| Copilot panel embedding the real agent | 7 | code-app-agent | Code Builder copilot skill (CopilotProvider agentId) | the push's files; preview | ok |
| Portal in English, German, Japanese | 5 | code-app-agent | Code Builder localization skill | the push's files; preview | ok |
| Customer sponsor login and customer role (A50 'sign in to see only their own project') | 5 | none | governance tools are not granted to builders; Code Builder's create_app_user is not on the code-builder server | none | no tool: open question 11 |
| publish ClickUp Delivery Command | all | code-app-agent | publish_code_app | deployed with commitHash | ok |
| Native phone app (A60, A69) | none | none | not in the contract | none | open question 7 |
| Monday 08:00 email, Slack post, Salesforce, Google Drive (A59, A102 to A104) | 6 | none | no connection chosen; Google Drive has no connection on the tenant | none | open question 6 |

Spec check: `nebula spec check` ready: true, one warning (Touches entities without their own ### heading, a full-spec convention the short spec does not use).


## entities

| kind | name | id | link | asks |
|---|---|---|---|---|
| object | ClickUp DC · Project | OBJ_cudc_project | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_project/schema | A1 A16 A22-A26 A70 A78-A83 |
| object | ClickUp DC · Task | OBJ_cudc_task | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_task/schema | A6 A15 A28-A30 A34 |
| object | ClickUp DC · RAID item (ISS-0523 added in the fix) | OBJ_cudc_raid | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_raid/schema | A24 A105 |
| object | ClickUp DC · Consultant | OBJ_cudc_consultant | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_consultant/schema | A4 A12 A17 A35 A36 |
| object | ClickUp DC · Booking | OBJ_cudc_booking | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_booking/schema | A4 A35 A36 A72 |
| object | ClickUp DC · Time entry | OBJ_cudc_time_entry | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_time_entry/schema | A37-A39 |
| object | ClickUp DC · Change request | OBJ_cudc_change_request | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_change_request/schema | A33 A40-A43 |
| object | ClickUp DC · Deliverable | OBJ_cudc_deliverable | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_deliverable/schema | A5 A51 |
| object | ClickUp DC · Session slot | OBJ_cudc_session_slot | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_session_slot/schema | A52 |
| object | ClickUp DC · Checklist item | OBJ_cudc_checklist_item | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_checklist_item/schema | A54 |
| object | ClickUp DC · Document | OBJ_cudc_document | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_document/schema | A53 |
| object | ClickUp DC · Activity | OBJ_cudc_activity | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_activity/schema | A49 A61 A63 A64 |
| object | ClickUp DC · AI output | OBJ_cudc_ai_output | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_ai_output/schema | A2 A3 A44-A46 |
| object | ClickUp DC · Weekly metric | OBJ_cudc_weekly_metric | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_weekly_metric/schema | A20 A56-A58 |
| object | ClickUp DC · Saved view | OBJ_cudc_saved_view | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cudc_saved_view/schema | A67 |
| automation (deployed) | ClickUp DC · Read delivery data | 6ad9e1ecf3b40669f5493989 | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e1ecf3b40669f5493989 | A2 A7 A21 |
| automation (deployed) | ClickUp DC · Move task | 6ad9e263ac81bd0349bbbd7e | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e263ac81bd0349bbbd7e | A28 A34 |
| automation (deployed) | ClickUp DC · Book consultant | 6ad9e2bdad671119e0cbffe0 | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e2bdad671119e0cbffe0 | A4 A12 A17 A35 A36 A98 |
| automation (deployed) | ClickUp DC · Submit change request | 6ad9e311ad671119e0cc3933 | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e311ad671119e0cc3933 | A33 A40 A41 |
| automation (deployed) | ClickUp DC · Decide change request | 6ad9e539f118275d3a1f6515 | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e539f118275d3a1f6515 | A42 A43 |
| automation (deployed) | ClickUp DC · Sign off deliverable | 6ad9e5d262fef87b0c74d89e | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e5d262fef87b0c74d89e | A5 A51 |
| automation (deployed) | ClickUp DC · Publish status report | 6ad9e61f690024749b2819e0 | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e61f690024749b2819e0 | A3 A44 A108 |
| automation (deployed) | ClickUp DC · Escalate to Jira | 6ad9e6720f07386bc11607e3 | https://orbit.uat.unifyapps.com/p/0/automations/6ad9e6720f07386bc11607e3 | A105 |
| ai-agent (published v3) | ClickUp Delivery Copilot | e_6ad9e4db1a10ec0c912adab3 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ad9e4db1a10ec0c912adab3 | A2 A3 A7 A21 A44-A46 A88 A89 A107 A108 |
| code-app (published v1) | ClickUp Delivery Command | app-0e25eb6667c3 | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-0e25eb6667c3 | every beat |

- code app: id app-0e25eb6667c3 · branch main (not git-linked) · published v2 from commit 481418b4f6fde5cd4334933a50902331787dfd02 (verify round 1 fixes; v1 was 39a12c53951ca948624f9cbad79fd5e094cd03ce)
- preview: https://orbit.uat.unifyapps.com/agent-api/preview/b/app-0e25eb6667c3/main/
- published: https://app-0e25eb6667c3-orbit.tensor-uat.unifyapps.com/portfolio (the host answers a sign-in redirect; not read back from a tool, which gives no live URL)
- routes: /portfolio, /projects/:projectId/overview, /projects/:projectId/status, /resourcing, /changes/new?project=<id>, /changes/:crId/detail, /summary/weekly, /portal/home (the deployed route list names the portal pages as /home, /signoffs …: unverified)
- connection: Jira Connection 6ababb56207d2c4e18ad380c (existing), project KAN
- test leftovers for cleanup (deletes need the person's own yes, CONFIRM_REQUIRED, not given in this scheduled run): Activity ACT-21 to ACT-30; Booking BKG-021, BKG-022 (Lena Vogt shows +8 h in the weeks of 2 and 9 Nov); Change request CR-0457, CR-0458 (the demo's live request will be numbered CR-0459, not CR-0457); AI output SR-2626-1; Jira issue KAN-27 (DEMO-TEST). Pending delete ids d_d101f6, d_f7eac3, d_89dc27.

## beats

Storyline: "Monday at ClickUp Delivery: catch Halden Freight before it slips"
Story row: Project IMP-2611 Halden Freight · Logistics · Europe · stage Migration · go-live 27 Nov 2026 (36 days out) · health At risk (On track last week) · lead Mira Castell · sponsor Katrin Albers · 4,800 seats · EUR 312,000 · budget 512 of 640 h · RSK-1183 "Legacy data migration running late" (likelihood 4, impact 4) · 3 of 8 migration tasks late · next sign-off "Migration plan v2" due 28 Oct · Tomas Brandt booked 100% in the week of 2 Nov · CR-0457 (+48 h, +EUR 7,200, +7 days) raised live.

1. Portfolio. The presenter, as delivery director Ines Moreau, signs in and opens Portfolio; the screen shows 14 On track, 4 At risk (+1), 2 Off track (+1) since last week, the AI risk card flagging Halden Freight (High, with evidence), the risk grid with RSK-1183 in the 4x4 cell, go-lives in the next 90 days by region with two slipped dates, the 12-week on-track trend falling to 70%, the project table filtered by chips to Europe and At risk ("2 of 20"), and the "Jira sync failed since 06:40" note. Route /portfolio. Asks A1, A8, A10, A16, A22 to A26, A49, A66, A67, A70, A73, A78 to A83, A85, A90, A96, A100, A101, A106. mode: live (Storage reads); the risk card is seeded.
2. Project overview. She opens Halden Freight; the screen shows the seven-stage path at Migration, 36 days to go-live, 512 of 640 h, 5 open RAID items, Migration plan v2 due 28 Oct; the board's Migration column carries the over-limit warning (16 of 15); the lead moves "Validate pilot batch" to Done from the card menu (the keyboard path) and the task detail opens beside the board. Route /projects/IMP-2611/overview. Asks A6, A15, A28, A29, A34, A71, A99. mode: live (ClickUp DC · Move task).
3. The failure beat. As resource manager she books Tomas Brandt onto Halden Freight, 8 h in the weeks of 2 and 9 Nov, without dragging; the app refuses before saving: "Over capacity: Tomas Brandt, week of 2 Nov 120% (8 h over), week of 9 Nov 105% (2 h over). Choose fewer hours or another consultant." She filters the skills matrix to data migration and books Lena Vogt instead (80%, 60%). Route /resourcing. Asks A4, A12, A17, A35, A36, A72, A91, A98, A109. mode: live (ClickUp DC · Book consultant).
4. Change request. The lead raises CR-0457: add 48 h for a third migration batch, EUR 7,200, go-live +7 days; the before and after plans sit side by side with the differences marked; submitted, it shows "Ines Moreau (delivery director), then Raj Patel (finance partner)"; the director approves, the finance partner approves, the plan moves to 4 Dec and the activity feed records it. Route /changes/CR-0457/detail. Asks A33, A40 to A43. mode: live (ClickUp DC · Submit change request, ClickUp DC · Decide change request).
5. Customer portal. The presenter switches to sponsor Katrin Albers in German; the portal shows only Halden Freight (stage, milestones, sessions, open actions, shared documents, no internal health), dates as 28.10.2026; she signs off "Migration plan v2" and the sign-off appears with who and when in the project's activity feed. Route /portal/home. Asks A5, A13, A19, A50, A51, A55, A68, A74, A77, A84, A97, A110. mode: live (ClickUp DC · Sign off deliverable).
6. Weekly summary. As the VP, the presenter opens the Monday summary; six headline tiles with changes coloured by good or bad for the business (Projects at risk 6, up 2, shown as bad), the contract value bridge from USD 4.05M to 4.21M, the five projects that changed most with reasons, and the 08:00 email preview per region. Route /summary/weekly. Asks A20, A56 to A59, A111. mode: seeded (snapshot rows, not presented as AI); the email is mocked as a preview.
7. Lean-forward: Delivery Copilot. Back as Mira Castell on Halden Freight, she opens the Copilot panel; it opens with three suggested questions; she asks "Which Europe projects go live in November and are at risk?", the panel shows its working stage and answers Halden Freight with a link; she asks "Draft this week's status report for Halden Freight"; the AI-written draft cites the late migration tasks, RSK-1183 and 512 of 640 h; she edits one line, publishes it and exports it as PDF; under 10 minutes on the clock. Route /projects/IMP-2611/overview with the Copilot panel and /projects/IMP-2611/status. Asks A2, A3, A7, A9, A21, A44 to A46, A88, A89, A107, A108. mode: live (the agent and ClickUp DC · Publish status report).
   Alternatives considered: B, the portal sign-off landing live in the lead's activity feed while both screens are side by side (strong, but it is a CRUD moment the audience has seen before) / C, the capacity refusal followed by the Copilot recommending Lena Vogt by skill (needs the agent to write a booking, which breaks the read-only rule). Chosen: the status report in under ten minutes, because it is the request's own "AI status reports" noun, the BRD's measured outcome (A3, A108) and it is the one moment only a live agent produces.
H1. Hood: the presenter opens ClickUp DC · Book consultant on the automation canvas and shows the capacity rule that refused Tomas Brandt in beat 3. mode: live.
H2. Hood: the presenter opens ClickUp Delivery Copilot in the agent builder: its instructions, its one read tool, the chart and document tools, and that it cannot write. mode: live.

AI surfaces:
- ClickUp Delivery Copilot (questions, charts, status report draft): live, read-only agent.
- Risk prediction card on Portfolio and the confidence and evidence fields: seeded, AI-written marker.
- Meeting summary with transcript anchors and the proposed tasks: seeded, AI-written marker; Accept writes for real.
- Last week's status report: seeded, AI-written marker.
- Weekly summary numbers and reasons: seeded, not presented as AI.

## views

- Portfolio (/portfolio) · beat 1 · header (search, notifications bell, profile menu with Appearance) and rail `.rail`; health tiles `.tile` + `.delta`; risk prediction `.ai:not(.msg)`; risk grid `.tbl` 5x5 matrix with `.tag` counts (heatmap built from tokens, open question 14); go-lives by region `.chart` lanes; on-track trend `.chart` + `.spark`; project table `.toolbar` `.field` `.chipsel` `.tblwrap` `.tbl` `.pg` with `.av` customer circles and `.tag` health; saved views `.menu`; Jira sync failed `.note`; empty and filtered-empty `.empty`.
- Project overview (/projects/:projectId/overview) · beats 2, 7 · `.crumb`; `.stages` seven stages; `.tile` + `.prog` for days, budget, risks, next sign-off; `.tabs` Board, List, Timeline, RAID, Documents, Activity, Settings; board `.kb` with column limit `.tag.attention` and Move to `.menu`; task detail `.g3` drawer with `.fld` and `.feed`; timeline built from tokens (open question 14); RAID `.tbl`; documents `.tbl` + viewer `.g3`; activity `.feed`; settings `.fld` `.ctl` with `.tag` save states.
- Resourcing (/resourcing) · beats 3, H1 · `.tabs` Grid, Skills, Timesheets, Capacity; grid `.tbl` with `.tag` percent cells; booking form `.fld` `.ctl` `.seg` `.btn-p`; refusal `.tag.negative` + `.note`; skills `.tbl`; timesheets `.tbl` + `.btn` + `.fld`; capacity `.chart`.
- Change request (/changes/:crId/detail) · beat 4 · form `.fld` `.ctl` `.hint`; before and after built from tokens (diff view, open question 14) in two `.g2` panes; approval path `.sth`; decision `.btn-p` `.btn-s` with reason `.fld` `.ctl.err`; activity `.feed`.
- Customer portal (/portal/home) · beat 5 · header with logo and `.av`; top menu `.tabs` Home, Sign-offs, Sessions, Files, Checklist; language `.seg`; `.stages`, milestones `.stv`; sign-off cards `.g2` with `.btn-p` `.btn-s` `.fld`; sessions `.cal` `.slot`; files `.tbl` + `.note` (file drop built from tokens); checklist `.opt` `.box` with `.tag.neutral` Not set; no-access `.empty`.
- Weekly summary (/summary/weekly) · beat 6 · six `.tile` + `.delta`; bridge `.chart`; top five `.tbl`; email preview `.g2` + `.note`.
- Copilot panel (right of every internal screen) and status report (/projects/:projectId/status) · beat 7, H2 · `.canvas` `.convo` `.msg.me` `.msg.ai` `.chips` (SDK copilot parts styled through appearance); working stage `.stages`; draft `.ai:not(.msg)` with AI-written `.tag`; editor `.ctl`; `.btn-p` Publish, `.btn-s` Export; proposed tasks `.tbl`; meeting summary `.feed`.
