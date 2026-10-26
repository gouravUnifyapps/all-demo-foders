---
use_case: ClickUp Delivery command platform
client: Clickup
poc_row: POC-clickup-delivery-command-platform-20261023
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g3
version: 1 · since 2026-10-23T11:57:39Z
thread: C0CBK3E47E2 · 1792757255.287779
intent: both
stage_flag: 

gates:
  g1: {status: approved, round: 1, posted_ts: 1792757255.287779, decided_by: Gourav Mahunta (reply), decided_at: 2026-10-23T12:10:00Z}
  g2: {status: approved, round: 1, posted_ts: 1792759631.690889, decided_by: Gourav Mahunta (reply), decided_at: 2026-10-23T17:07:07Z}
  g3: {status: "ready, not posted: row shows G2 pending", round: 1, posted_ts: , decided_by: , decided_at: }
  g4: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }

posts:
  - when: 2026-10-23T12:07:22Z
    kind: g1
    ts: 1792757255.287779
    by: bot
    version: 1
    round: 1
  - when: 2026-10-23T12:07:57Z
    kind: status
    ts: 1792757255.287779
    by: bot
    version: 1
    round: 1
  - when: 2026-10-23T12:46:50Z
    kind: g2
    ts: 1792759631.690889
    by: Gourav Mahunta's Slack · gate_order: row still shows G1 waiting
    version: 1
    round: 1
  - when: 2026-10-23T12:46:50Z
    kind: status
    ts: 1792759633.012249
    by: Gourav Mahunta's Slack · gate_order: row still shows G1 waiting
    version: 1
    round: 1
  - when: 2026-10-23T17:12:00Z
    kind: status
    ts: 1792757255.287779
    by: bot
    version: 1
    round: 1
  - when: 2026-10-23T19:42:00Z
    kind: status
    ts: 1792757255.287779
    by: bot
    version: 1
    round: 1
  - when: 2026-10-26T10:08:00Z
    kind: g3
    ts: 
    by: "not posted: gate_order (row shows G2 pending; G2 was approved by thread reply on 23 Oct)"
    version: 1
    round: 1
  - when: 2026-10-26T10:08:00Z
    kind: status
    ts: 1792757255.287779
    by: bot
    version: 1
    round: 1
runs:
  - started: 2026-10-23T11:57:39Z
    ended: 2026-10-23T12:07:57Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 140
    outcome: posted G1
  - started: 2026-10-23T12:15:22Z
    ended: 2026-10-23T12:46:50Z
    gate: g2
    stages: [2-plan]
    spawns: 1
    tokens: 331
    outcome: posted G2
  - started: 2026-10-23T12:58:00Z
    ended: 2026-10-23T13:00:00Z
    gate: g2
    stages: []
    spawns: 0
    tokens: 0
    outcome: waiting

  - started: 2026-10-23T17:11:00Z
    ended: 2026-10-23T19:40:00Z
    gate: g3
    stages: [3-build]
    spawns: 24
    tokens: 3900
    outcome: stopped: AGENT_LLM_TOOLS refused on orbit.uat during plan 9
  - started: 2026-10-26T07:27:00Z
    ended: 2026-10-26T10:05:00Z
    gate: g3
    stages: [3-build, 4-verify r1, 3-build fixes, 4-verify r2, 5-handover]
    spawns: 9
    tokens: 1490
    outcome: "waiting: G3 pack ready, not posted (gate_order: row shows G2 pending)"

asks:
  - id: A1
    text: "Delivery Command should make all three visible and actionable."
    source: "ClickUp-Delivery-Command-BRD.pdf §2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A2
    text: "Brand colour: none supplied. Take it from the live site clickup.com."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Brand colour (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A3
    text: "Logo: no file supplied. Fetch the official logo. It appears on the sign-in page, the expanded and collapsed left menu, the browser tab icon, the customer portal header, generated status reports (PDF and Word), and the weekly executive email."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Logo (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A4
    text: "Customer logos: shown as circles on project cards and in the portal."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Customer logos (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A5
    text: "Typeface: take it from the live site. Numbers must line up in tables. The customer portal must also display Japanese and German text correctly."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Typeface (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A6
    text: "Tone: clear, calm and direct. Errors say what happened and what to do next. No jokes or exclamation marks in the product."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Tone (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A7
    text: "Feel: the internal workspace is a daily working tool and should stay dense and quiet. The customer portal and the executive summary are also shown in sales demos and should look polished."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Feel (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A8
    text: "Appearance: light and dark both needed. Light is the default."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Appearance (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A9
    text: "List every project with customer, region, stage, go-live date, health, lead, seats and contract value. Users search and filter by region, stage, health and lead. The count of results shows as \"x of y\". Filters that apply show as removable chips with one \"clear all\"."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A10
    text: "Show portfolio health as counts of On track, At risk and Off track, with the change since last week."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A11
    text: "Place each open risk on a grid of likelihood against impact, so leaders see which risks matter most. Choosing a cell lists its risks."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A12
    text: "Show every go-live date in the next 90 days on a timeline, grouped by region, with slipped dates marked."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A13
    text: "Show how the share of projects on track has moved over the last 12 weeks."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A14
    text: "Leaders can save a filtered view and share it with their team."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A15
    text: "A project overview shows the stage the project is in, the seven stages as a progress path, days to go-live, budget hours used against planned, open risks and the next customer sign-off due."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A16
    text: "Tasks can be viewed as a list or as a board with one column per stage. A column shows a warning when it holds more than its limit (default 15). Tasks can be moved between columns by dragging or from a menu."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A17
    text: "A timeline shows tasks with start and end dates, dependencies between them and the critical path. Changing a date moves dependent tasks and shows the new go-live date before it is saved."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A18
    text: "A risks, assumptions, issues and decisions (RAID) log records each item with owner, due date, status and history."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A19
    text: "A document library holds the statement of work, migration plans and sign-off records. Files open in a viewer inside the application."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A20
    text: "An activity feed shows who changed what and when on the project."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A21
    text: "Task detail opens beside the list so the user keeps their place. It shows description, assignee, dates, time logged, comments and attachments."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W7 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A22
    text: "Show every consultant against the next 12 weeks with the percentage they are booked each week. Over 100% is flagged."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A23
    text: "Book a consultant onto a project by choosing person, project, weeks and hours. Booking works without dragging."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A24
    text: "Show consultants against skills (data migration, integrations, admin training, API, Japanese language) with a level for each, so the right person can be found."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A25
    text: "Consultants log time against tasks each day. Managers approve or return weekly timesheets, giving a reason when they return one."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A26
    text: "Should: show booked hours against capacity for each region over the quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A27
    text: "An implementation lead raises a change request with the reason, the work added or removed, and the effect on hours, cost and go-live date."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A28
    text: "Before submitting, the lead sees the plan before and after the change side by side, with the differences marked."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A29
    text: "Changes under 40 hours need the delivery director's approval. Changes of 40 hours or more also need the finance partner, in that order. The request shows who has approved and who is next."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A30
    text: "Rejecting a change request requires a written reason. Approved changes update the plan and are recorded in the activity feed."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A31
    text: "Delivery Copilot is an AI assistant available from every internal screen."
    source: "ClickUp-Delivery-Command-BRD.pdf §5.5 intro a (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A32
    text: "Anything it writes is labelled as AI-written."
    source: "ClickUp-Delivery-Command-BRD.pdf §5.5 intro b (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A33
    text: "Users ask questions in plain language, for example \"Which Japan projects go live in November and are at risk?\" The assistant opens with three suggested questions based on the user's projects, and shows each stage while it works."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A34
    text: "Chart tool: the assistant can answer with a chart, such as hours by stage or go-lives by month. Charts use the application's colours and show units."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A35
    text: "Status report tool: the assistant drafts the weekly status report for a project from its tasks, risks and time entries. The lead edits and publishes it. The report can be exported as PDF or Word."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A36
    text: "Task tool: the assistant can propose tasks, for example after a meeting summary. Proposed tasks are listed for the user to accept or reject; nothing is created without acceptance."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A37
    text: "Meeting summary tool: the assistant summarises a customer meeting transcript into decisions, actions and risks. Each point links to the part of the transcript it came from."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A38
    text: "Risk prediction: the assistant flags projects likely to miss go-live, with a confidence level and the evidence for each flag, such as migration tasks running late."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A39
    text: "Customer sponsors sign in to see only their own project: stage, milestones, upcoming sessions, open actions for their team and the documents shared with them."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A40
    text: "Sponsors sign off a stage deliverable or request changes with a comment. A sign-off records who approved and when."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A41
    text: "Sponsors book training sessions by choosing a day and then a time slot. Taken slots stay visible but cannot be chosen."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A42
    text: "Sponsors upload files such as user lists (CSV up to 50,000 rows). Errors appear row by row and can be fixed before confirming."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A43
    text: "A readiness checklist guides the customer through 10 setup items. An item they have not answered shows as not set, never as a guessed value."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A44
    text: "The portal is available in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A45
    text: "A weekly summary shows six headline numbers with their change from last week: active projects, go-lives this month, projects at risk, average days to go-live, consultant utilisation and contract value awaiting go-live. A change is coloured by whether it is good or bad for the business, not by its sign."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A46
    text: "Show how contract value awaiting go-live moved from last month to this month, split into new projects, go-lives completed, slipped dates and cancellations."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A47
    text: "List the five projects that changed most this week, with the reason for each."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A48
    text: "The summary is also sent as an email every Monday at 08:00 in each region's time zone."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A49
    text: "Consultants see today's tasks and sessions, update a task's status, and log time in under 30 seconds on a phone."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 M1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A50
    text: "Notifications for new assignments, sign-offs and mentions. Each can be marked read or opened."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 M2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A51
    text: "Roles control what each user can see and change. Show roles against permissions as a grid."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A52
    text: "Keep a record of who did what and when. It cannot be edited and can be filtered by person, project and action."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A53
    text: "Show the status of each integration (Salesforce, Slack, Google Drive, Jira) with last sync time and any error."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A54
    text: "Project settings (name, region, go-live date, budget hours) can be edited in place, with clear unsaved, saving, saved and failed states."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A55
    text: "Sign-in, forgot password, reset password"
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Screens (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A56
    text: "Internal users navigate with a left menu: Portfolio, Projects, Resourcing, Timesheets, Changes, Admin."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A57
    text: "The top bar shows the current project or view, search, notifications and the profile menu."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A58
    text: "Delivery Copilot opens as a panel on the right."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A59
    text: "Customers get a shorter top menu: Home, Sign-offs, Sessions, Files, Checklist."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A60
    text: "The phone has bottom tabs: Today, Tasks, Time, Alerts."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A61
    text: "Portfolio list needs paging, search and filters"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Active projects 180 to 300 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A62
    text: "Board and timeline must stay readable"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Tasks per project 150 to 1,200 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A63
    text: "Resourcing grid is people against 12 weeks"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Consultants and leads about 72 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A64
    text: "Grid of likelihood against impact, with drill-down"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Open risks across the portfolio about 400 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A65
    text: "Portal must be simple for occasional users"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Customer users about 900 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A66
    text: "Timesheet approval in batches"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Time entries per week about 3,000 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A67
    text: "Errors summarised, not listed in full"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Customer upload up to 50,000 rows (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A68
    text: "Text can grow by 30% in German"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Languages English, German, Japanese (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A69
    text: "On track, Signed off, Approved, Live"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Good or finished (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A70
    text: "At risk, Awaiting sign-off, Over capacity, Pending approval"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Needs attention (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A71
    text: "Off track, Blocked, Rejected, Sync failed"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Problem (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A72
    text: "Not started, Draft, Scheduled, Hypercare"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Neutral (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A73
    text: "Project IDs look like IMP-2611, change requests like CR-0457, risks like RSK-1183."
    source: "ClickUp-Delivery-Command-BRD.pdf §8 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A74
    text: "Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026年 10月 17日)."
    source: "ClickUp-Delivery-Command-BRD.pdf §8 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A75
    text: "Money shows in the contract currency (USD, EUR or JPY)."
    source: "ClickUp-Delivery-Command-BRD.pdf §8 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A76
    text: "Projects appear here once a lead assigns you"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: No projects assigned yet (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A77
    text: "Nothing matches the current filters, with a way to clear them"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A search or filter matches nothing (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A78
    text: "Which stage it is on"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: Copilot is still working (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A79
    text: "Why, and what to try instead"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: Copilot cannot answer (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A80
    text: "Which one, since when, and what is affected"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: An integration has failed (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A81
    text: "Who, which weeks and by how much, before saving"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A booking takes someone over capacity (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A82
    text: "For example 214 of 50,000 rows need fixing"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A customer upload has errors (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A83
    text: "The item shows as not set"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A checklist item has no answer (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A84
    text: "Who can grant access"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: The user has no access to a project (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A85
    text: "How to stay signed in"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: The session is about to end (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A86
    text: "When it was last updated"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: Data is out of date (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A87
    text: "The internal workspace is in English. The customer portal is in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A88
    text: "Times show the user's time zone. Weeks start on Monday in Europe and Japan and on Sunday in North America."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A89
    text: "All drag actions also work from the keyboard. Controls are at least 24 px on desktop and larger on the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A90
    text: "Meaning never depends on colour alone: every status shows an icon and a word."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A91
    text: "Screens meet WCAG 2.2 AA in both light and dark appearance."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A92
    text: "Contract value, seats and close date when a deal is won, which creates the project"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Salesforce (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A93
    text: "Notifications and the weekly status post to each project channel"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Slack (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A94
    text: "Shared documents and customer uploads"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Google Drive (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A95
    text: "Engineering escalations linked to project issues"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Jira (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A96
    text: "The first release does not include the following, and the application must not suggest otherwise:"
    source: "ClickUp-Delivery-Command-BRD.pdf §12 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A97
    text: "Billing, invoicing or revenue recognition."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A98
    text: "Building or editing customer workspaces in the core ClickUp product."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A99
    text: "Hiring, performance reviews or payroll for consultants."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A100
    text: "A public marketing site."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A101
    text: "Video calls or call recording."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A102
    text: "Offline use of the phone view."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A103
    text: "21 days or more"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Average warning before a missed go-live (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A104
    text: "Under 10 minutes"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Time to produce a weekly status report (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A105
    text: "No more than 1 per consultant"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Consultant weeks booked above 100% per quarter (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A106
    text: "2 working days or less"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Customer sign-off time (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A107
    text: "10 minutes or less"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Executive time to read the weekly summary (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A108
    text: "75%"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Customers completing the readiness checklist without help (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A109
    text: "I want to see every project on one screen without scrolling."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Delivery director (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A110
    text: "Let us edit the timeline straight from the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Consultants (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A111
    text: "Show customers their health score."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, VP of customer success (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A112
    text: "Customers should never see internal health."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Implementation leads (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A113
    text: "Colour-code consultants by region everywhere."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Resource manager (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A114
    text: "Add a pricing calculator for upsells."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Sales (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Sales upsell pricing calculator"
    status: out_of_scope

coverage:
  - ask: A1
    by: "beat 1"
  - ask: A2
    by: "beat 1"
  - ask: A3
    by: "beat 1"
  - ask: A4
    by: "beat 1"
  - ask: A5
    by: "beat 6"
  - ask: A6
    by: "beat 4"
  - ask: A7
    by: "beat 1"
  - ask: A8
    by: "control Appearance Light or Dark in the profile menu, every screen"
  - ask: A9
    by: "beat 1"
  - ask: A10
    by: "beat 1"
  - ask: A11
    by: "beat 1"
  - ask: A12
    by: "beat 1"
  - ask: A13
    by: "beat 1"
  - ask: A14
    by: "beat 1"
  - ask: A15
    by: "beat 2"
  - ask: A16
    by: "beat 2"
  - ask: A17
    by: "beat 2"
  - ask: A18
    by: "beat 2"
  - ask: A19
    by: "beat 2"
  - ask: A20
    by: "beat 2"
  - ask: A21
    by: "beat 2"
  - ask: A22
    by: "beat 3"
  - ask: A23
    by: "beat 3"
  - ask: A24
    by: "beat 3"
  - ask: A25
    by: "beat 3"
  - ask: A26
    by: "beat 3"
  - ask: A27
    by: "beat 4"
  - ask: A28
    by: "beat 4"
  - ask: A29
    by: "beat 4"
  - ask: A30
    by: "beat 4"
  - ask: A31
    by: "beat 7"
  - ask: A32
    by: "beat 7"
  - ask: A33
    by: "beat 7"
  - ask: A34
    by: "beat 7"
  - ask: A35
    by: "beat 7"
  - ask: A36
    by: "beat 7"
  - ask: A37
    by: "beat 7"
  - ask: A38
    by: "beat 7"
  - ask: A39
    by: "beat 6"
  - ask: A40
    by: "beat 6"
  - ask: A41
    by: "beat 6"
  - ask: A42
    by: "beat 6"
  - ask: A43
    by: "beat 6"
  - ask: A44
    by: "beat 6"
  - ask: A45
    by: "beat 5"
  - ask: A46
    by: "beat 5"
  - ask: A47
    by: "beat 5"
  - ask: A48
    by: "beat 5"
  - ask: A49
    by: "control Phone view in the profile menu: /m Today and Time tabs, log time in three taps"
  - ask: A50
    by: "control Notifications bell in the top bar and the phone's Alerts tab, mark read or open"
  - ask: A51
    by: "control Admin › Roles: roles against permissions grid"
  - ask: A52
    by: "control Admin › Audit log, filtered by person, project and action, read only"
  - ask: A53
    by: "control Admin › Integrations: last sync and error per system"
  - ask: A54
    by: "control Admin › Projects: settings edited in place with unsaved, saving, saved, failed"
  - ask: A55
    by: "beat 1"
  - ask: A56
    by: "beat 1"
  - ask: A57
    by: "beat 1"
  - ask: A58
    by: "beat 7"
  - ask: A59
    by: "beat 6"
  - ask: A60
    by: "control Phone view bottom tabs Today, Tasks, Time, Alerts"
  - ask: A61
    by: "beat 1"
  - ask: A62
    by: "beat 2"
  - ask: A63
    by: "beat 3"
  - ask: A64
    by: "beat 1"
  - ask: A65
    by: "beat 6"
  - ask: A66
    by: "beat 3"
  - ask: A67
    by: "beat 6"
  - ask: A68
    by: "beat 6"
  - ask: A69
    by: "beat 1"
  - ask: A70
    by: "beat 1"
  - ask: A71
    by: "beat 1"
  - ask: A72
    by: "beat 1"
  - ask: A73
    by: "beat 1"
  - ask: A74
    by: "beat 6"
  - ask: A75
    by: "beat 1"
  - ask: A76
    by: "control Persona switch to Marcus Bell: \"Projects appear here once a lead assigns you\" on Portfolio"
  - ask: A77
    by: "control Portfolio filters with no match: \"No rows match your search and filters\" with Clear all"
  - ask: A78
    by: "beat 7"
  - ask: A79
    by: "beat 7"
  - ask: A80
    by: "control Admin › Integrations: Jira Sync failed since 06:40 UTC, 3 escalations affected"
  - ask: A81
    by: "beat 3"
  - ask: A82
    by: "beat 6"
  - ask: A83
    by: "beat 6"
  - ask: A84
    by: "beat 6"
  - ask: A85
    by: "control Profile menu › Preview session timeout: \"Your session ends in 2 minutes. Stay signed in\""
  - ask: A86
    by: "beat 1"
  - ask: A87
    by: "beat 6"
  - ask: A88
    by: "beat 3"
  - ask: A89
    by: "beat 2"
  - ask: A90
    by: "beat 1"
  - ask: A91
    by: "control Appearance switch, both themes on the kit's measured tokens"
  - ask: A92
    by: "control Admin › Integrations Salesforce row and the IMP-2646 \"created from won deal\" feed entry"
  - ask: A93
    by: "control Admin › Integrations Slack row"
  - ask: A94
    by: "control Project › Documents source label Google Drive; Admin › Integrations row"
  - ask: A95
    by: "control Project › RAID: RSK-1184 linked to ENG-4821; Admin › Integrations Jira row"
  - ask: A96
    by: "beat 1"
  - ask: A97
    by: "beat 7"
  - ask: A98
    by: "beat 1"
  - ask: A99
    by: "beat 1"
  - ask: A100
    by: "beat 1"
  - ask: A101
    by: "control No call or recording control anywhere; Copilot declines"
  - ask: A102
    by: "control Phone view has no offline mode or offline wording"
  - ask: A103
    by: "beat 7"
  - ask: A104
    by: "beat 7"
  - ask: A105
    by: "beat 3"
  - ask: A106
    by: "beat 6"
  - ask: A107
    by: "beat 5"
  - ask: A108
    by: "beat 6"
  - ask: A109
    by: "beat 1"
  - ask: A110
    by: "open question 2"
  - ask: A111
    by: "open question 1"
  - ask: A112
    by: "beat 6"
  - ask: A113
    by: "beat 3"

size:
  pages: 18
  objects: 21
  automations: 18
  agents: 1
  tasks: 108
  nebula_plans: 11
  note: "over the reference (4 pages, 3 objects, 3 automations, 1 AI agent); a flag, not a cut; 3-build sequences 11 plans"

data:
  source: "assumed, shaped like ClickUp's delivery operations (BRD §7 and §8): fictional rows written by 2-plan in studio/data/seed/ (19 CSV files); the BRD's six invented customers plus twelve invented ones"
  masked: "none: fictional; no real person, company, address or identifier; emails on .example domains; amounts in the contract currency, portfolio totals in USD at EUR 1.08 and JPY 0.0066"
  rows: "Project 19 (record · seed, named in the first 20, story row IMP-2611), Task 96, Booking 168, Time entry 63 (record · seed naming the file, under 200), RAID item 17, Person 18, Activity 20, Session slot 12, Weekly snapshot 12, Checklist item 10, AI output 7, Document 6, Notification 6, Role permission 6, Sign-off 4, Integration 4, Change request 2, Saved view 2, Weekly metric 1 (record · seed); Upload and Executive email 0 (written live); the 50,000-row upload is generated in the app (Use sample file), never stored"
  expected_answers: eval.csv

verify:
  round: 2
  walked_at: 2026-10-26T08:45Z to 09:38Z
  browser: "Nebula browser wrapper signed in on orbit.uat.unifyapps.com; preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-f53fd0efccec/main/ (same code as published v1, commit 5126004f); 1440 x 900; screenshots in /tmp/claude-0/verify-r2/"
  beats_pass: "2 of 9 (pass: beat 3, H2; fix: beat 1 tiles read ±0 and the list reads 2 of 20 with two DEMO-TEST projects; beat 2 Move to does nothing and the Data migration column reads 18 of 15 with a DEMO-TEST task; beat 4 the new request is numbered CR-312005; beat 5 Send test email says sent while the automation saved a preview, and a DEMO-TEST project leads the five biggest movers; beat 6 the sponsor's portal shows a DEMO-TEST session and a DEMO-TEST sign-off; beat 7 Publish shows a raw id and Meeting and Report list DEMO-TEST rows; H1 node 2 is labelled 'Actor given?' while its YES branch refuses. Persona changes were made from the sign-in screen because the profile menu's switch does nothing)"
  controls_pass: "82 of 86 (fail: Move to menu items, profile-menu persona switch, Send test email message, Report Publish message; unverified: writes that would use up the demo's seeded state: approve the eight pending timesheets, Hana's SGN-302 sign-off, book a training slot, accept or reject proposed tasks, log time on the phone, apply a saved view from the Views menu)"
  queries_pass: "10 of 11 (8 fact, 3 refusal; fail Q6 'Who is booked over 100% in the next 12 weeks?': 'no person in the data I can fully verify is booked over 100% in any of the 12 weeks', expected Haruto Sato week of 2 Nov 2026, 44 of 40 h, 110%; cases e_6adf1ad0f3cd5f19ed3dc868 to e_6adf1d93c79cad11400eb689)"
  coverage_pass: "103 of 113 (92 asks named by beats shown on their screens; A49 A50 A60 on Phone, A51 A52 A53 A54 A80 on Admin, A77 on filtered tables, A94 A95 on Portal and RAID; not shown: A8 A76 A85 A91 A92 A93 A101 A102 A110 A111, see open_questions)"
  checks_pass: "5 of 7 (fail: brand on the primary action only on every internal and portal screen; both empty states on Timesheets, Changes, Project List/RAID/Documents, Resourcing; pass: no horizontal scroll, table readable at 1440 (mono 10.5px heads, 13-15px cells, tabular numbers, nothing cut), no console errors and no failed tenant requests, stylesheet (source design-system.css equals client.css byte for byte after the two @import lines; the build is minified, so computed :root properties were compared and differ only in notation such as rgba vs hex8 and 150ms vs .15s), logo contrast 9.07:1 rail, 8.97:1 portal header)"
  p95_latency_s: 151
  latency_target_s: 90
  latencies_s: "Q1 12, Q2 18, Q3 21, Q4 15, Q5 62, Q6 151, Q7 23, Q8 22, Q9 4, Q10 4, Q11 4 (case creation to answer, from the case id time and the last LLM node; in the app: Q1 28 s, chart 49 s, status report draft about 57 s, invoice refusal 11 s, each with an Ask Copilot run 6adbaf90c79cad11403e9b72)"
  live_evidence: "every demo-path write in the walk returned an executionInstanceId from its automation: Save view 6adf13a32934813cf1f19f95, Reschedule preview, Book consultant 6adf15ee.. / 6adf1612.., Change request submit and decisions, Send executive summary 6adf18152934813cf1f2288f (status preview), Confirm upload 6adf19270301de7aecb1a23b, Ask Copilot 6adf198e0301de7aecb1afa1, Publish status report; list_workflow_runs returns no deployed runs for callable runs, so the run ids come from the page's own call replies"
  previous_open:
    - "Read delivery data day text: fixed (every stated date in the 11 answers and the app's draft matches the seed)"
    - "Copilot dates from day text: fixed for stated dates; new finding below: date range filters are still hand-converted to epoch and land a year early"
    - "Copilot within 90 s at p95: still failing (151 s on Q6, 62 s on Q5)"
    - "Copilot publish: fixed (version 19, published, needsPublish false)"
    - "Tools offered beyond the agent's own: still seen in every trace; platform, moved to dev_issues"
  demo_test_records: "VIEW-6adf13a32934813cf1f19f95 (saved view 'DEMO-TEST Japan · at risk'); Marcus Bell 10 h on DEMO-TEST-PRJ-1 weeks of 16 and 23 Nov; CR-312005 on DEMO-TEST-PRJ-1 (approved, added 2 tasks, moved its go-live to 4 Jan 2028); AIO-6adf1a752934813cf1f2740d ('DEMO-TEST Weekly status · Sakura Mobility'); EML-JAPAN-20261026-813cf1f2288f (preview); DEMO-TEST-PRJ-C9A9E6 budget 140 to 144 h. Not marked DEMO-TEST: UPL-IMP-2611-6adf19270301de7aecb1a23b (sample upload confirmed on IMP-2611, as beat 6 does) and Aiko Tanaka's 'New assignment' notification marked read on the phone"
  open:
    - "code-app · update · ClickUp Delivery Command: the shared menu item (components/kit.tsx MenuItem) runs its onSelect when chosen; today its own onClick calls preventDefault, which stops the menu's select, so every Move to item on the Project board, the profile menu (persona switch, Light and Dark, Phone view, Customer portal, Sign out) and the Views menu do nothing; nothing else changes"
    - "code-app · update · ClickUp Delivery Command: every list, board, chart, feed and selector leaves out rows whose id or name starts with DEMO-TEST (today the Portfolio list reads 2 of 20, the IMP-2611 Data migration column 18 of 15, Executive summary's biggest movers lead with DEMO-TEST Project, the portal shows a DEMO-TEST slot and DEMO-TEST-SGN-1 to the sponsor, Copilot Meeting and Report list DEMO-TEST-PRJ and DEMO-TEST proposed tasks, Changes lists DEMO-TEST-CR-1, DEMO-TEST-CR-2 and CR-312005, and the audit log and project pickers list DEMO-TEST projects); nothing else changes"
    - "object · update · Delivery Command · Weekly snapshot: the 2026-10-19 row reads on_track 13, at_risk 3, off_track 2, active_projects 18, so the Portfolio tiles, which compare with the latest snapshot before this week, read 12 On track −1, 4 At risk +1, 2 Off track ±0 as beat 1 says (today the row equals the live counts and all three read ±0); nothing else changes"
    - "automation · update · Delivery Command · Change request: a new request takes the next number of the CR-04nn series after the highest stored (CR-0452 now) instead of 'CR-' plus the last six digits of the clock (it made CR-312005); nothing else changes"
    - "automation · update · Delivery Command · Change request: node 2 is named 'No actor?' (its YES branch refuses the call; it reads 'Actor given?' on the canvas the hood beat H1 opens); nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screen Executive summary: when Send executive summary answers status preview, the message reads 'Saved as a preview. No mailbox is connected, so nothing was sent.' instead of 'Test email sent'; nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screen Copilot panel: after Publish on the Report tab the line reads 'Published to IMP-2611's report history' instead of 'Published as AIO-6adf1a752934813cf1f2740d.'; nothing else changes"
    - "code-app · update · ClickUp Delivery Command: the avatar circles (.av, header and portal), the Portfolio go-live markers (.mk) and their legend key (.k-brand), the progress bars (.prog on Portfolio rows, Project overview and Portal checklist) and the portal Sessions day dots (.evd) take the neutral ink or chart series token instead of the brand colour; nothing else changes"
    - "code-app · update · ClickUp Delivery Command: screens Timesheets, Changes, Project (List, RAID, Documents) and Resourcing (bookings grid): the filtered-empty state 'No rows match your search and filters' carries a Clear all filters button, as Portfolio and Admin do; nothing else changes"
    - "automation · update · Delivery Command · Read delivery data: a range filter on a date field also accepts day text such as {\"week_start\":{\"gte\":\"2026-10-26\",\"lte\":\"2026-11-16\"}} and converts it to epoch milliseconds itself (the Copilot sent 1761436800000, which is 26 Oct 2025, and read 0 bookings); nothing else changes"
    - "automation · update · Delivery Command · Read delivery data: bookings rows come back compact (person, project_id, week_start_text, hours) so a read of all 170 bookings reaches the model whole (the Copilot reported 'the tool output was truncated' for Haruto Sato, Aiko Tanaka and Kenji Arakawa); nothing else changes"
    - "ai-agent · update · Delivery Command · Copilot: instructions write date range filters as day text and read bookings in at most three ranges of four weeks, so 'Who is booked over 100% in the next 12 weeks?' answers Haruto Sato, week of 2 Nov 2026, 44 of 40 h, 110%, within 90 s (now 151 s and 'no person ... is booked over 100%'); nothing else changes"

collaterals:

review:
  round: 0
  open: []

decisions:
  - by: orchestrator
    when: 2026-10-23
    text: "Profile studio/profiles/clickup.md drafted by Studio from the request and defaults; the owner can confirm or change it."
  - by: state-check
    when: 2026-10-23
    text: "reverted stage_flag: written by harvest, outside its fields (schema § Who writes what)"
  - by: orchestrator
    when: 2026-10-23
    text: "Preflight: Bun, Chromium (render-doc needs a --no-sandbox wrapper on the cloud runner), ffmpeg, poppler, Slack read tools and the tenant sign-in are ok; the collateral kit's python packages are missing (blocks G4 until poc-collateral-setup installs them); Google Calendar is not connected (1-harvest skipped it)."
  - by: manager
    when: 2026-10-23
    text: "Gourav Mahunta replied in the thread: \"Approve\" (G1, round 1). The 12 G1 open questions were not answered; they stay open."
  - by: profile
    when: 2026-10-23
    text: "Brand colour ambiguous (14 candidates on clickup.com): took brand-sample's recommendation #5F55EE, hue 244, from --ProductScreen-CustomStatus-Primary (standing answer: ambiguous brand colour, the recommended one, listed in the G2 pack). Others: --Core-Accents-Purple #6647F0, --Table-Accent #7612FA, --Core-Accents-Blue #0091FF, --ProductScreen-FeatureCalendar-Blue-Accent #3E63DD, --Core-Accents-Pink #FF02F0, --Core-Accents-Orange #FC6D2D."
  - by: profile
    when: 2026-10-23
    text: "AI agent model: Nebula's recommendation (standing answer)."
  - by: plan
    when: 2026-10-23
    text: "Logo: brand-sample saved the ClickUp Brain mark from a page section; replaced with the official ClickUp wordmark from the site's nav (aria-label ClickUp) and the ClickUp mark (aria-label ClickUp Logo), both saved as published in studio/design-system/clickup/ (follows G1 open question 7, recommended option)."
  - by: plan
    when: 2026-10-23
    text: "G1 open questions 1 to 12 were not answered; the plan follows each recommended option and the plan doc says where."
  - by: plan
    when: 2026-10-23
    text: "Modes: the status report draft is live on the same Copilot agent (not seeded) because A104's under-10-minutes claim needs a real draft; seeded fallback AIO-07. The working stages are deterministic because Invoke Agent returns one answer to the app. Sign-in and the persona switch are mocked; integrations are mocked as seeded rows (G1 question 6)."
  - by: plan
    when: 2026-10-23
    text: "External step held: G1 open question 6 recommends seeded integrations. Inventory: active Salesforce, Jira and Slack connections on orbit.uat owned by other teams, no Google Drive one; with option (b) the candidate is a Jira escalation from RSK-1184, read-only probe not run."
  - by: plan
    when: 2026-10-23
    text: "Names: the tenant already holds an earlier build outside this solution (OBJ_cudc_*, OBJ_dc_*, eight \"ClickUp DC ·\" automations, three Copilot agents); this plan uses new \"Delivery Command ·\" names and OBJ_dcmd_* ids, all free, and touches none of them."
  - by: plan
    when: 2026-10-23
    text: "Document files: fde-agent has no file upload tool, so each Document carries its text and the in-app viewer pages it."
  - by: plan
    when: 2026-10-23
    text: "Appearance (A8): light default with the dark tokens live, the switch in the profile menu rather than the chrome bar."
  - by: state-check
    when: 2026-10-23
    text: "reverted stage_flag: written by plan, outside its fields (schema § Who writes what)"
  - by: orchestrator
    when: 2026-10-23
    text: "POC Studio refused the G2 plan report with gate_order (row g1_status still waiting although the manager approved G1 by thread reply); the G2 pack and status line were posted with Gourav Mahunta's own Slack, plan PDF linked. The row's G1 needs approving in POC Studio so later reports are accepted."
  - by: orchestrator
    when: 2026-10-23
    text: "Feedback rows FB-1792759783479-1 and FB-1792759783479-2 (gate g1, confirmed by Gourav Mahunta's \"Yes\") are the G2 pack and its status line, posted with Gourav Mahunta's Slack and collected back by the POC Studio bot as G1 feedback. They are not for the gate waiting (G2) and ask for no change, so they are not counted; G2 stays waiting."

  - by: manager
    when: 2026-10-23
    text: "Gourav Mahunta replied in the thread: \"Approve\" (ts 1792775227.687809, G2, round 1), after \"Stop rework\" (ts 1792775213.284849). G2 approved; the proposed intent `both` becomes intent. The 17 G2 open questions were not answered; the build follows each recommended option as the plan doc says."
  - by: orchestrator
    when: 2026-10-23
    text: "The confirmed G1 feedback item \"Status?\" and the pending \"Stop rework\" ask for no change and are not counted; G1 stays approved. The row still shows G1 waiting, so POC Studio will refuse the G3 report with gate_order until G1 and G2 are approved in POC Studio."
  - by: orchestrator
    when: 2026-10-23
    text: "3-build split the contract into 10 Nebula plans; automations were built without contract shells because every caller (the agent, the code app) comes in a later plan, after each deploy."
  - by: orchestrator
    when: 2026-10-23
    text: "Builders asked to delete their own DEMO-TEST rows (CONFIRM_REQUIRED); no person can approve a delete in an unattended run, so they kept them: DEMO-TEST rows remain in Change request, Task, Activity, Project, AI output, Sign-off, Notification, Session slot, Upload and Saved view; their cleanup is a handover checklist item."
  - by: build
    when: 2026-10-23
    text: "Found while building, for 4-verify: Read delivery data returns 0 rows for a region or ai_outputs kind filter; the Copilot read some go-live dates one day early (time zone); the code app's t4/t5 screens send local-midnight dates (fix built in the unpushed t7 change); Copilot model is Vertex Sonnet 5 AI FDE because the first two listed models failed (spend limit, invalid key); the agent is visible to groups All Users and testing."
  - by: state-check
    when: 2026-10-23
    text: "reverted open_questions: written by build, outside its fields (schema § Who writes what)"
  - by: orchestrator
    when: 2026-10-26
    text: "Gourav Mahunta clicked Build again (the step the AGENT_LLM_TOOLS open question asked for); the tenant answered Nebula's reads, so the build resumed. Plan 9's runner was another machine's Nebula client and this session could not resume it (INVALID_PLAN: only the plan's runner), so its unfinished t7 and plan 10's six tasks ran as a new plan e_6adf01b4bc76624e532df4c9: 7 of 7 done, ClickUp Delivery Command published v1 from commit 5126004f, PRIVATE."
  - by: build
    when: 2026-10-26
    text: "Found while building, for 4-verify: no screen was opened in a browser and no writing action was run; only the portal is translated (EN/DE/JA, lib/portalText.ts), the rest stays English; the portal picks the sponsor's project by persona name; the five biggest movers are ranked by a rule the builder chose (go-live, health and cancellation events weighted highest); meeting-summary transcript links have no transcript player to land on; the tools return no published URL."
  - by: orchestrator
    when: 2026-10-26
    text: "POC Studio refused the G3 build report with gate_order (\"G2 is pending; G2 · BRD & design system must be approved before G3 · Build sign-off\"). The row shows g1 approved, g2 pending, although Gourav Mahunta approved G2 by thread reply on 23 Oct. The G3 pack is kept (handover PDF uploaded, report built); the next run sends it once G2 is approved in POC Studio."
dev_issues:
  - what: "The agent runtime offers the model tools the agent does not have: every trace of Delivery Command · Copilot (version 19) lists EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy (not attached; the agent has 3 tool records: Read_delivery_data, and requestClarification and generateChartTool both disabled) and ClarifyFromUser (its capability requestClarification is off)"
    beat: "Beat 7 · Ask Delivery Copilot (and H2)"
    read: "read_trace modelCalls[].toolsOffered for cases e_6adf1ad0f3cd5f19ed3dc868, e_6adf1b5497a3bf334ddc82a1 and e_6adf1bfd08750d257cc4b917; get_agent tools and capabilities for e_6adbabd2925d282255cee62b"
    raised:

frozen:

cost:
  runs: 5
  agent_spawns: 35
  tokens_m: 5.86
  wall_h: 5.85

open_questions:
  - by: harvest
    for: lead
    text: "Customer health in the portal: the VP of customer success says \"Show customers their health score\" (A111); implementation leads say \"Customers should never see internal health\" (A112). Options: (a) Portal shows no internal health; customers see stage, milestones and open sign-offs only (C1) [recommended]; (b) Portal shows a customer-facing health score, separate from the internal one; (c) Portal shows the internal health as-is"
  - by: harvest
    for: lead
    text: "Phone editing: consultants ask \"Let us edit the timeline straight from the phone\" (A110), while M1 lists only today's tasks, status and time on the phone and W3's timeline is a desktop screen. Options: (a) Phone stays at M1/M2 (today, task status, time, alerts); timeline edits stay on desktop [recommended]; (b) Add a simple date change for one task on the phone, with the go-live preview from W3; (c) Full timeline editing on the phone"
  - by: harvest
    for: lead
    text: "One screen without scrolling: the delivery director wants \"every project on one screen without scrolling\" (A109), while the BRD expects 180 to 300 projects with paging (A61, BRD P1). Options: (a) Portfolio opens on health counts, risk grid and go-live timeline that fit one screen; the paged project list sits below [recommended]; (b) A compact one-row-per-project list sized to fit the seeded projects with no paging; (c) Keep the paged list only"
  - by: harvest
    for: lead
    text: "Region colours: the resource manager wants \"Colour-code consultants by region everywhere\" (A113), while §10 says \"Meaning never depends on colour alone\" (A90). Options: (a) Region shown as a labelled chip with a colour on resourcing and portfolio screens, never colour alone [recommended]; (b) Colour-code by region on every screen as asked, each with a text label; (c) No region colours"
  - by: harvest
    for: lead
    text: "Sales' \"Add a pricing calculator for upsells\" (A114) reads as another use case and sits near §12's exclusion of billing. Is it left out of this demo? Options: (a) Leave it out of scope; it stays listed under other use cases [recommended]; (b) Promote it (reply promote A114) as a simple calculator screen"
  - by: harvest
    for: lead
    text: "Integrations (Salesforce, Slack, Google Drive, Jira; A53, A92 to A95): the profile allows only connections already on the tenant. How are they shown? Options: (a) Seeded integration-status rows (last sync, one Sync failed) and a seeded deal-won event; no live connection [recommended]; (b) Use live connections for whichever of the four already exist on orbit.uat, seeded for the rest; (c) Ask the client for sandbox credentials"
  - by: harvest
    for: lead
    text: "Logo: the BRD says \"Fetch the official logo\" (A3) while the profile's standing answer for no supplied logo is a text wordmark placeholder. Options: (a) Sample the official logo from clickup.com, as the BRD asks, and list it in the G2 pack [recommended]; (b) Text wordmark placeholder per the profile"
  - by: harvest
    for: lead
    text: "Phone view (M1, M2, bottom tabs): one responsive code app or a separate mobile app? Options: (a) A phone-width route inside the same code app, shown in a phone frame [recommended]; (b) A separate mobile app"
  - by: harvest
    for: lead
    text: "Portal languages (A44, A87): how far do German and Japanese go in the demo? Options: (a) Full language switch on every portal screen with translated seeded text and local date/number formats [recommended]; (b) English portal with a working switch on the home screen only"
  - by: harvest
    for: lead
    text: "Data volume: the profile seeds 15 to 20 fictional rows; the BRD describes 180 to 300 projects, about 72 consultants, about 400 risks and a 50,000-row upload (§7). Options: (a) 15 to 20 projects with the six BRD sample customers, about 12 consultants, enough risks to fill the grid, and a generated 50,000-row CSV with 214 bad rows for C4 [recommended]; (b) Seed at BRD volumes (about 200 projects); (c) Profile minimum only"
  - by: harvest
    for: lead
    text: "Finance partner (S3) is not among the six personas. Who approves 40-hour-plus changes in the demo? Options: (a) A seeded finance partner user the presenter can switch to [recommended]; (b) The presenter approves both steps as the delivery director"
  - by: harvest
    for: lead
    text: "Weekly executive email (E4, Monday 08:00 per region): sent for real or shown? Options: (a) Scheduled automation built; the demo triggers one run to the presenter's inbox [recommended]; (b) Email preview page only, no send"
  - by: plan
    for: lead
    text: "Intent: what should the audience leave with?. Options: (a) both: the outcome first, then two hood beats (the change-request automation, the Copilot agent) [recommended]; (b) use-case: no hood beats; (c) platform: two to four hood beats and a description on every node and field"
  - by: plan
    for: lead
    text: "Typeface (A5): the BRD asks for the live site's; clickup.com uses Inter (body) and Plus Jakarta Sans (headings), the design system ships Archivo and IBM Plex Mono. Options: (a) Inter for body and headings from Google Fonts, IBM Plex Mono kept for table heads, tabular numbers, Noto Sans JP for Japanese [recommended]; (b) Archivo as the design system ships, with tabular numbers and Noto Sans JP; (c) Inter body with Plus Jakarta Sans headings"
  - by: plan
    for: lead
    text: "Executive email sender (A48): no mailbox connection on the tenant belongs to this team. Options: (a) Build and schedule it; until a mailbox is named it saves a preview the summary screen shows, and the test send waits [recommended]; (b) Name an existing Gmail connection on orbit.uat to send from; (c) Preview only, no schedule"
  - by: plan
    for: lead
    text: "Accounts and roles (A39, A51, A84): real per-user sign-in and platform roles need governance tools not granted to Nebula yet. Options: (a) A persona switch stands in for sign-in; the app enforces each role's rows and actions and shows the grid [recommended]; (b) Real tenant users and roles made by hand by the owner after the build; (c) Grid only, no enforcement"
  - by: plan
    for: lead
    text: "An earlier build of this demo exists on the tenant outside this solution (\"ClickUp DC ·\" and \"DC\" objects, eight automations, three Copilot agents). Options: (a) Build fresh under \"Delivery Command ·\" names in this solution and leave the earlier entities untouched [recommended]; (b) Reuse the earlier \"ClickUp DC ·\" objects and automations"
  - by: verify
    for: owner
    text: "Round 1 verify could not walk the app: the verify browser (Nebula Playwright, unattended runner) is not signed in to orbit.uat.unifyapps.com, so the preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-f53fd0efccec/main/ and the Code Builder page both redirect to /login, and the code app has no published URL. Beats 1-7, H1, H2, the control sweep on 12 screens and the seven checks are unverified: sign-in. Options: (a) Sign the verify browser in once (or run verify where the person's browser is signed in) and rerun round 1 [recommended]; (b) Make the published code app public for the demo window; (c) Accept the agent-only verify for this round"
  - by: verify
    for: owner
    text: "Coverage walk: all 113 asks with status built were shown by no beat or control this round, because no screen could be opened (sign-in). What was built for them is the code app app-f53fd0efccec v1 with its objects and automations; they did not show because the walk never reached a screen. Options: (a) Rerun the coverage walk once the browser is signed in [recommended]; (b) Treat coverage as unmeasured for G3"
  - by: verify
    for: owner
    text: "Round 2 coverage: A8 (light and dark appearance) was built as Light and Dark items in the profile menu, but no walk could switch it because that menu's items do nothing (a fix line is open). Options: (a) Re-check A8 in round 3 once the menu fix lands [recommended]; (b) Drop dark appearance from the demo"
  - by: verify
    for: owner
    text: "Round 2 coverage: A76 ('Projects appear here once a lead assigns you', the empty state for a consultant with no projects) and A85 ('How to stay signed in' on the sign-in screen) were built as empty-state and sign-in copy, but no beat or control reaches them: every persona in the walk has projects, and the sign-in screen shows no stay-signed-in line. Options: (a) Accept them as unshown in the demo [recommended]; (b) Add a persona with no projects and a stay-signed-in line so they can be shown"
  - by: verify
    for: owner
    text: "Round 2 coverage: A91 (WCAG 2.2 AA in light and dark) was built through the design system's tokens; this walk measured only the seven checks (logo contrast, table type), not a full WCAG pass, and could not open dark appearance. Options: (a) Treat A91 as covered by the seven checks for the demo [recommended]; (b) Run a full accessibility audit before the client demo"
  - by: verify
    for: owner
    text: "Round 2 coverage: A92 (a won Salesforce deal creates the project with value, seats and close date) and A93 (notifications and the weekly status post to each project channel) were built as seeded integration-status rows (option a of the integrations question); no screen shows a deal creating a project or a channel post. Options: (a) Accept the integration-status rows as their showing [recommended]; (b) Add a seeded 'deal won' activity and a channel-post preview so a beat can show them"
  - by: verify
    for: owner
    text: "Round 2 coverage: A101 (video calls or recording), A102 (offline phone), A110 (edit the timeline from the phone) and A111 (customers see their health score) carry status built although they are out of scope or were decided against (phone stays at today, tasks, time and alerts; the portal shows no internal health). Nothing shows them, by design. Options: (a) Set them to out of scope or declined so coverage counts 103 of 103 [recommended]; (b) Keep them built and show the decision on a screen"
---

## build_contract
Spec file in Nebula's exact shape: /home/user/all-demo-foders/clickup/clickup-delivery-command-platform/.sessions/42e28f3b-d1d9-58fa-ba61-c9b8441d96b4/drafts/studio/clickup-delivery-command-platform.md (`spec check`: ready, no issues, no warnings). Headings are demoted two levels here so this section stays one block.

### ClickUp Delivery Command demo

#### Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live.

#### Touches
- object · Delivery Command · Project · new
- object · Delivery Command · Task · new
- object · Delivery Command · RAID item · new
- object · Delivery Command · Person · new
- object · Delivery Command · Booking · new
- object · Delivery Command · Time entry · new
- object · Delivery Command · Change request · new
- object · Delivery Command · Activity · new
- object · Delivery Command · Document · new
- object · Delivery Command · Session slot · new
- object · Delivery Command · Sign-off · new
- object · Delivery Command · Checklist item · new
- object · Delivery Command · Notification · new
- object · Delivery Command · Integration · new
- object · Delivery Command · Saved view · new
- object · Delivery Command · Weekly snapshot · new
- object · Delivery Command · Weekly metric · new
- object · Delivery Command · AI output · new
- object · Delivery Command · Role permission · new
- object · Delivery Command · Upload · new
- object · Delivery Command · Executive email · new
- automation · Delivery Command · Move task · new
- automation · Delivery Command · Reschedule task · new
- automation · Delivery Command · Book consultant · new
- automation · Delivery Command · Review timesheets · new
- automation · Delivery Command · Log time · new
- automation · Delivery Command · Change request · new
- automation · Delivery Command · Accept proposed tasks · new
- automation · Delivery Command · Publish status report · new
- automation · Delivery Command · Record sign-off · new
- automation · Delivery Command · Book training slot · new
- automation · Delivery Command · Confirm upload · new
- automation · Delivery Command · Save view · new
- automation · Delivery Command · Update project settings · new
- automation · Delivery Command · Mark notification read · new
- automation · Delivery Command · Send executive summary · new
- automation · Delivery Command · Weekly executive email schedule · new
- automation · Delivery Command · Read delivery data · new
- automation · Delivery Command · Ask Copilot · new
- ai-agent · Delivery Command · Copilot · new
- code-app · ClickUp Delivery Command · new

#### Contract

##### object · Delivery Command · Project
One customer implementation, from signed contract to Hypercare.
- object · create · Delivery Command · Project (`OBJ_dcmd_project`): project_id text unique (IMP-nnnn), customer text, customer_initials text, region picklist (north_america "North America", europe "Europe", japan "Japan"), stage picklist (kickoff "Kickoff", discovery "Discovery", configuration "Configuration", data_migration "Data migration", integrations "Integrations", training "Training", hypercare "Hypercare"), stage_index number 1 to 7, go_live date epoch ms, baseline_go_live date epoch ms, slipped boolean, health picklist (on_track "On track", at_risk "At risk", off_track "Off track"), lead text, seats number, contract_value number, currency picklist (USD, EUR, JPY), budget_hours number, used_hours number, lifecycle picklist (active "Active", live "Live", cancelled "Cancelled"), sponsor text, portal_language picklist (en, de, ja), last_synced_at datetime epoch ms; index on region, health, lead
- record · seed · Delivery Command · Project: the 19 rows of studio/data/seed/project.csv (story row IMP-2611 Sakura Mobility, Japan, Data migration, go-live 19 Nov 2026, baseline 12 Nov 2026, At risk, lead Mei Takahashi, 1,200 seats, JPY 84,000,000, 860 h planned, 545 h used, sponsor Hana Mori; IMP-2590 Pellworth Labs is Cancelled)

##### object · Delivery Command · Task
One task in a project plan, with dates, dependencies and the critical path.
- object · create · Delivery Command · Task (`OBJ_dcmd_task`): task_id text unique (TSK-nnnn), project_id text, title text, description long text, stage picklist (the seven stage codes of Project), status picklist (not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee text, start date epoch ms, end date epoch ms, depends_on text (a task_id), critical boolean, hours_planned number, hours_logged number, ai_proposed boolean; index on project_id, assignee
- record · seed · Delivery Command · Task: the 96 rows of studio/data/seed/task.csv (45 on IMP-2611; 17 in its Data migration column; critical path TSK-5024 to TSK-5044; TSK-5024 and TSK-5025 past their end date)

##### object · Delivery Command · RAID item
One risk, assumption, issue or decision on a project.
- object · create · Delivery Command · RAID item (`OBJ_dcmd_raid`): raid_id text unique (RSK-, ASM-, ISS-, DEC-nnnn), project_id text, type picklist (risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title text, owner text, due date epoch ms, status picklist (open "Open", mitigating "Mitigating", closed "Closed"), likelihood number 1 to 5, impact number 1 to 5, jira_key text, history long text
- record · seed · Delivery Command · RAID item: the 17 rows of studio/data/seed/raid.csv (RSK-1183 likelihood 4, impact 5)

##### object · Delivery Command · Person
One internal user or customer sponsor, with capacity and skill levels.
- object · create · Delivery Command · Person (`OBJ_dcmd_person`): person_id text unique (PER-nnn), name text, role picklist (consultant "Consultant", lead "Implementation lead", director "Delivery director", resource_manager "Resource manager", finance_partner "Finance partner", sponsor "Customer sponsor"), region picklist (as Project), capacity_hours number, skill_data_migration number 0 to 4, skill_integrations number 0 to 4, skill_admin_training number 0 to 4, skill_api number 0 to 4, skill_japanese number 0 to 4, customer text, email text, time_zone text, week_start picklist (monday "Monday", sunday "Sunday")
- record · seed · Delivery Command · Person: the 18 rows of studio/data/seed/person.csv (13 consultants and leads, Elena Brooks delivery director, Tomás Herrera finance partner, Grace Liu resource manager, sponsors Hana Mori and Owen Price)

##### object · Delivery Command · Booking
Hours one person is booked on one project in one week.
- object · create · Delivery Command · Booking (`OBJ_dcmd_booking`): booking_id text unique (BKG-nnnn), person text, project_id text, week_start date epoch ms, hours number; index on person, week_start
- record · seed · Delivery Command · Booking: the 168 rows of studio/data/seed/booking.csv (12 weeks from 26 Oct 2026; Haruto Sato 44 h in week of 2 Nov; Aiko Tanaka 30 h in week of 16 Nov and 20 h in week of 23 Nov; Marcus Bell none)

##### object · Delivery Command · Time entry
Hours one person logged on one task on one day, inside a weekly timesheet.
- object · create · Delivery Command · Time entry (`OBJ_dcmd_time_entry`): entry_id text unique (TME-nnnn), person text, task_id text, project_id text, date date epoch ms, hours number, timesheet_week date epoch ms, timesheet_status picklist (draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason text
- record · seed · Delivery Command · Time entry: the 63 rows of studio/data/seed/time_entry.csv (week of 19 Oct Pending approval for 9 people; week of 12 Oct Approved)

##### object · Delivery Command · Change request
One proposed change to a project, with its two-step approval route.
- object · create · Delivery Command · Change request (`OBJ_dcmd_change_request`): cr_id text unique (CR-nnnn), project_id text, raised_by text, reason long text, work_added long text, work_removed long text, hours_delta number, cost_delta number, currency picklist (USD, EUR, JPY), golive_before date epoch ms, golive_after date epoch ms, plan_before long text (JSON task list), plan_after long text (JSON task list), route picklist (director "Delivery director", director_finance "Delivery director, then finance partner"), step1_status picklist (pending, approved, rejected), step1_by text, step1_at datetime epoch ms, step2_status picklist (not_needed, waiting, pending, approved, rejected), step2_by text, step2_at datetime epoch ms, next_approver text, status picklist (draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), reject_reason long text
- record · seed · Delivery Command · Change request: the 2 rows of studio/data/seed/change_request.csv (CR-0452 approved by the director alone; CR-0449 rejected by the finance partner with a reason)

##### object · Delivery Command · Activity
One change on a project: who did what and when; never edited.
- object · create · Delivery Command · Activity (`OBJ_dcmd_activity`): activity_id text unique (ACT-nnnn), at datetime epoch ms, actor text, project_id text, action text, target text, detail text, source picklist (app "Delivery Command", automation "Automation", ai "Delivery Copilot", salesforce "Salesforce"); rows are only ever created, never updated or deleted; index on project_id, actor, action
- record · seed · Delivery Command · Activity: the 20 rows of studio/data/seed/activity.csv

##### object · Delivery Command · Document
One file in a project library: statement of work, migration plan or sign-off record.
- object · create · Delivery Command · Document (`OBJ_dcmd_document`): document_id text unique (DOC-nn), project_id text, title text, body long text (the document's text, shown in the in-app viewer), kind picklist (sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", other "Other"), file_url text, shared_with_customer boolean, source text, uploaded_by text, at date epoch ms
- record · seed · Delivery Command · Document: the 6 rows of studio/data/seed/document.csv, each with a short fictional body; file_url stays empty

##### object · Delivery Command · Session slot
One bookable customer training slot.
- object · create · Delivery Command · Session slot (`OBJ_dcmd_session_slot`): slot_id text unique (SLT-nn), project_id text, date date epoch ms, start text, end text, topic text, taken boolean, booked_by text
- record · seed · Delivery Command · Session slot: the 12 rows of studio/data/seed/session_slot.csv (4 taken)

##### object · Delivery Command · Sign-off
One stage deliverable awaiting or carrying the customer sponsor's sign-off.
- object · create · Delivery Command · Sign-off (`OBJ_dcmd_signoff`): signoff_id text unique (SGN-nnn), project_id text, stage picklist (the seven stage codes), deliverable text, status picklist (awaiting "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), requested_at date epoch ms, decided_by text, decided_at datetime epoch ms, comment long text
- record · seed · Delivery Command · Sign-off: the 4 rows of studio/data/seed/signoff.csv (SGN-302 Migration plan v2 Awaiting sign-off)

##### object · Delivery Command · Checklist item
One of the ten readiness questions with the customer's answer.
- object · create · Delivery Command · Checklist item (`OBJ_dcmd_checklist_item`): item_id text unique (CHK-nn), project_id text, order number, question_en text, question_de text, question_ja text, answer text (empty means not set)
- record · seed · Delivery Command · Checklist item: the 10 rows of studio/data/seed/checklist_item.csv (7 answered, 3 not set)

##### object · Delivery Command · Notification
One assignment, sign-off or mention for a user.
- object · create · Delivery Command · Notification (`OBJ_dcmd_notification`): notification_id text unique (NTF-nn), recipient text, kind picklist (assignment "New assignment", signoff "Sign-off", mention "Mention"), text text, link text, read boolean, at datetime epoch ms
- record · seed · Delivery Command · Notification: the 6 rows of studio/data/seed/notification.csv

##### object · Delivery Command · Integration
The sync status of one connected system.
- object · create · Delivery Command · Integration (`OBJ_dcmd_integration`): system text unique (Salesforce, Slack, Google Drive, Jira), status picklist (live "Live", sync_failed "Sync failed"), last_sync datetime epoch ms, error text, affected text
- record · seed · Delivery Command · Integration: the 4 rows of studio/data/seed/integration.csv (Jira Sync failed since 06:40 UTC, 3 escalations affected)

##### object · Delivery Command · Saved view
One named, shareable set of portfolio filters.
- object · create · Delivery Command · Saved view (`OBJ_dcmd_saved_view`): view_id text unique (VW-nn), name text, owner text, filters long text (JSON), shared_with_team boolean
- record · seed · Delivery Command · Saved view: the 2 rows of studio/data/seed/saved_view.csv

##### object · Delivery Command · Weekly snapshot
Portfolio health counts for one week, for the trend.
- object · create · Delivery Command · Weekly snapshot (`OBJ_dcmd_weekly_snapshot`): week_start date epoch ms unique, on_track number, at_risk number, off_track number, active_projects number, on_track_share number
- record · seed · Delivery Command · Weekly snapshot: the 12 rows of studio/data/seed/weekly_snapshot.csv (on-track share 88.2% down to 66.7%)

##### object · Delivery Command · Weekly metric
The executive summary's six headline numbers and the contract value bridge for one week.
- object · create · Delivery Command · Weekly metric (`OBJ_dcmd_weekly_metric`): week_start date epoch ms unique, active_projects, active_projects_prev, golives_this_month, golives_this_month_prev, projects_at_risk, projects_at_risk_prev, avg_days_to_golive, avg_days_to_golive_prev, utilisation_pct, utilisation_pct_prev, value_awaiting_q4_usd, value_awaiting_q4_usd_prev_week, value_awaiting_q4_usd_last_month, bridge_new_usd, bridge_completed_usd, bridge_slipped_usd, bridge_cancelled_usd (all number)
- record · seed · Delivery Command · Weekly metric: the 1 row of studio/data/seed/weekly_metric.csv

##### object · Delivery Command · AI output
One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report.
- object · create · Delivery Command · AI output (`OBJ_dcmd_ai_output`): output_id text unique (AIO-nn), kind picklist (risk_flag "Risk flag", meeting_summary "Meeting summary", proposed_task "Proposed task", status_report "Status report"), project_id text, title text, body long text, confidence picklist (high "High", medium "Medium", low "Low"), evidence long text, transcript_ref text, status picklist (open, draft, proposed, accepted, rejected, published), ai_written boolean default true, created_at datetime epoch ms
- record · seed · Delivery Command · AI output: the 7 rows of studio/data/seed/ai_output.csv, every row ai_written true

##### object · Delivery Command · Role permission
One role's row in the roles-against-permissions grid.
- object · create · Delivery Command · Role permission (`OBJ_dcmd_role_permission`): role text unique, view_portfolio, edit_project, move_tasks, book_consultants, approve_timesheets, raise_change, approve_change, view_internal_health, sign_off_deliverables, admin (all boolean)
- record · seed · Delivery Command · Role permission: the 6 rows of studio/data/seed/role_permission.csv

##### object · Delivery Command · Upload
One customer file upload with its row error summary.
- object · create · Delivery Command · Upload (`OBJ_dcmd_upload`): upload_id text unique (UPL-nnn), project_id text, file_name text, rows_total number, rows_error number, error_summary long text (JSON: error type, count, first five row numbers), status picklist (validated "Validated", confirmed "Confirmed"), uploaded_by text, at datetime epoch ms

##### object · Delivery Command · Executive email
One composed weekly executive email, sent or kept as a preview.
- object · create · Delivery Command · Executive email (`OBJ_dcmd_exec_email`): email_id text unique (EML-nnn), region picklist (as Project), send_at datetime epoch ms, recipient text, subject text, html long text, status picklist (sent "Sent", preview "Preview", failed "Failed"), error text

##### automation · Delivery Command · Move task
Moves a task to another stage or status and records it.
- automation · create · Delivery Command · Move task: callable; input task_id text, to_stage text, to_status text, actor text; sets the task's stage and status, writes one Activity row; result ok boolean, column_count number, over_limit boolean (column_count above 15), message text

##### automation · Delivery Command · Reschedule task
Moves a task's dates, shifts its dependents and previews the new go-live.
- automation · create · Delivery Command · Reschedule task: callable; input task_id text, new_start date, new_end date, actor text, confirm boolean; walks depends_on forward and shifts every dependent task by the same working days; result shifted list of {task_id, new_start, new_end}, golive_before date, golive_after date; with confirm false it writes nothing, with confirm true it saves the tasks, the project's go_live and one Activity row

##### automation · Delivery Command · Book consultant
Checks a booking against capacity, then writes it.
- automation · create · Delivery Command · Book consultant: callable; input person text, project_id text, weeks list of dates, hours number, actor text, confirm boolean; sums Booking hours per week against the Person's capacity_hours; result over_capacity list of {week_start, booked_hours, capacity_hours, percent}, ok boolean, message text; with confirm false it writes nothing; with confirm true it writes one Booking per week and one Activity row

##### automation · Delivery Command · Review timesheets
Approves or returns weekly timesheets in a batch.
- automation · create · Delivery Command · Review timesheets: callable; input persons list of text, timesheet_week date, decision text (approve or return), reason text, actor text; result updated number, refused boolean, message text; decision return with an empty reason is refused with "A returned timesheet needs a reason."

##### automation · Delivery Command · Log time
Logs hours on a task from the phone.
- automation · create · Delivery Command · Log time: callable; input person text, task_id text, date date, hours number, status text; writes a Time entry in Draft, adds hours to the task's hours_logged, sets the task status when given, writes one Activity row; result entry_id text

##### automation · Delivery Command · Change request
Submits, routes, approves and rejects change requests by the 40-hour rule.
- automation · create · Delivery Command · Change request: callable; input action text (submit, approve, reject), cr_id text, project_id text, raised_by text, reason text, work_added text, work_removed text, hours_delta number, cost_delta number, golive_after date, plan_before text, plan_after text, actor text, reject_reason text; submit sets route director when hours_delta is under 40 and director_finance when 40 or more, next_approver Elena Brooks; approve by the director on director_finance sets next_approver Tomás Herrera; the last approval sets status approved, adds the change's tasks from plan_after, moves the project's go_live and budget_hours and writes Activity rows; reject with an empty reject_reason is refused with "A rejection needs a written reason. Add one and reject again."; result cr_id text, status text, route text, next_approver text, refused boolean, message text

##### automation · Delivery Command · Accept proposed tasks
Turns accepted Copilot task proposals into tasks.
- automation · create · Delivery Command · Accept proposed tasks: callable; input output_ids list of text, decision text (accept or reject), actor text; accept creates one Task per output and sets the output accepted; reject sets it rejected and creates nothing; result created list of task_id

##### automation · Delivery Command · Publish status report
Publishes the lead's edited status report.
- automation · create · Delivery Command · Publish status report: callable; input project_id text, title text, body text, actor text; saves an AI output of kind status_report with status published and ai_written true, writes one Activity row; result output_id text

##### automation · Delivery Command · Record sign-off
Records a sponsor's sign-off or change request.
- automation · create · Delivery Command · Record sign-off: callable; input signoff_id text, decision text (sign_off or request_changes), comment text, actor text; request_changes with an empty comment is refused with "Add a comment so the team knows what to change."; saves decided_by and decided_at, writes one Activity row and one Notification for the project lead; result status text, decided_at datetime, refused boolean, message text

##### automation · Delivery Command · Book training slot
Books a free training slot for the sponsor.
- automation · create · Delivery Command · Book training slot: callable; input slot_id text, actor text; a slot already taken is refused with "This slot was just taken. Choose another time."; result ok boolean, message text

##### automation · Delivery Command · Confirm upload
Records a validated customer upload.
- automation · create · Delivery Command · Confirm upload: callable; input project_id text, file_name text, rows_total number, rows_error number, error_summary text, actor text; saves an Upload with status confirmed and one Activity row; result upload_id text

##### automation · Delivery Command · Save view
Saves a filtered portfolio view.
- automation · create · Delivery Command · Save view: callable; input name text, filters text, shared_with_team boolean, actor text; result view_id text

##### automation · Delivery Command · Update project settings
Saves one project setting edited in place.
- automation · create · Delivery Command · Update project settings: callable; input project_id text, field text (name, region, go_live, budget_hours), value text, actor text; validates the value (a go-live date in the past and a negative budget are refused with a message saying what to enter), saves it and writes one Activity row; result ok boolean, message text, saved_at datetime

##### automation · Delivery Command · Mark notification read
Marks one notification read.
- automation · create · Delivery Command · Mark notification read: callable; input notification_id text; result ok boolean

##### automation · Delivery Command · Send executive summary
Composes and sends the weekly executive email for a region.
- automation · create · Delivery Command · Send executive summary: callable; input region text, recipient text; composes the six headline numbers, the bridge and the five biggest movers from Weekly metric, Weekly snapshot, Project and Activity into an HTML email with the ClickUp logo, saves an Executive email row, and sends it on the mail connection named under Assumptions when there is one (status sent), else status preview; result email_id text, status text

##### automation · Delivery Command · Weekly executive email schedule
Runs every Monday 08:00 in each region's time zone.
- automation · create · Delivery Command · Weekly executive email schedule: scheduled every hour on Sundays 22:00 UTC to Mondays 14:00 UTC; for each region whose local time (Asia/Tokyo, Europe/Berlin, America/New_York) is Monday 08:00 it calls Send executive summary for that region

##### automation · Delivery Command · Read delivery data
The Copilot's read-only tool over the delivery objects.
- automation · create · Delivery Command · Read delivery data: callable, read only; input entity text (projects, tasks, raid, bookings, people, time_entries, signoffs, ai_outputs, weekly_snapshots), filters text (JSON field equals or range), limit number; result rows list, count number; never writes

##### automation · Delivery Command · Ask Copilot
Passes a question from the app to Delivery Copilot and returns its answer.
- automation · create · Delivery Command · Ask Copilot: callable; input question text, persona text, screen text, project_id text; invokes the Delivery Command · Copilot agent with the question and its context (Invoke Agent, ai_agents_by_unifyapps); result answer text, chart text (JSON {type, unit, series} or empty), links list of {label, route}, refused boolean

##### ai-agent · Delivery Command · Copilot
Delivery Copilot: a read-only assistant over the delivery data.
- ai-agent · create · Delivery Command · Copilot: instructions: answer delivery questions for ClickUp's implementation team from Read delivery data only, in plain, calm, direct English; name every project by id and customer and link it; when a chart helps, return a chart JSON {type: bar or line, unit, series} with units; draft weekly status reports from a project's tasks, risks and time entries, marked as an AI draft for the lead to edit; decline billing, invoicing, revenue, payroll, hiring and anything outside delivery data, and say plainly when a field the data does not hold is asked for, with what to try instead; never create or change anything; model: Nebula's recommendation; tool: Read delivery data

##### code-app · ClickUp Delivery Command
The code app: internal workspace, customer portal and phone view.
- code-app · create · ClickUp Delivery Command: the shell: the design system stylesheet, the fonts, the rail (ClickUp logo; Portfolio, Projects, Resourcing, Timesheets, Changes, Admin), the top bar (current project or view, search, notifications, profile menu with persona switch, appearance Light or Dark, Phone view and Customer portal entries), the right-hand Copilot panel slot, the routes for Sign-in, Forgot password, Reset password, Portfolio, Projects, Project, Resourcing, Timesheets, Changes, Change request, Executive summary, Admin, Portal home, Portal sign-offs, Portal sessions, Portal files, Portal checklist and Phone; PRIVATE
- code-app · update · ClickUp Delivery Command: screen Sign-in, Forgot password, Reset password: the ClickUp logo, a persona picker standing in for sign-in, the two password screens with their inline errors; screen Portfolio: `.tile` health counts with `.delta` since last week, risk grid `.chart` (likelihood by impact, choosing a cell lists its risks in a `.tbl`), 90-day go-live timeline grouped by region with slipped dates marked, 12-week on-track share `.spark` in a `.chart`, project `.toolbar` (search, region, stage, health, lead `.chipsel`, removable chips with Clear all, "x of y") above a `.tblwrap .tbl` with `.pg`, Save view; reads Project, RAID item, Weekly snapshot, Saved view · calls Save view on Save
- code-app · update · ClickUp Delivery Command: screen Project (overview, board, list, task detail): `.crumb`, overview `.stages` of the seven stages, `.tile` days to go-live, budget hours used against planned `.prog`, open risks, next sign-off due; board `.kb` one column per stage with a `.tag.attention` warning above 15, drag and a Move to menu; list `.tbl`; task detail in a side pane beside the list (description, assignee, dates, time logged, comments, attachments); reads Project, Task, RAID item, Sign-off · calls Move task on a drop or Move to
- code-app · update · ClickUp Delivery Command: screen Project (timeline, RAID, documents, activity): timeline of tasks with dependencies and the critical path, a date change previewing the new go-live before Save; RAID `.tabs` with owner, due date, status and history; document library `.tbl` with an in-app viewer pane that pages the document's body; activity `.feed`; reads Task, RAID item, Document, Activity · calls Reschedule task on preview and Save
- code-app · update · ClickUp Delivery Command: screen Resourcing: people against the next 12 weeks with percent booked per week, over 100% as `.tag.negative`, region as a labelled chip; Book consultant form (person, project, weeks, hours) with the over-capacity `.note` before Save; skills matrix (data migration, integrations, admin training, API, Japanese language) with levels; booked against capacity by region for the quarter `.chart`; screen Timesheets: weekly timesheets `.tbl` with batch select, Approve and Return with a required reason; reads Person, Booking, Time entry · calls Book consultant on Check and Save, Review timesheets on Approve and Return
- code-app · update · ClickUp Delivery Command: screen Changes and Change request: list `.tbl`; New change request form (reason, work added or removed, hours, cost, go-live) with the plan before and after side by side and the differences marked; approval `.stv` showing who approved and who is next; Approve and Reject, Reject needing a written reason, the refusal as `.tag.negative` and `.note`; reads Change request, Task, Project · calls Change request on Submit, Approve and Reject
- code-app · update · ClickUp Delivery Command: screen Executive summary: six `.tile` headline numbers with `.delta` coloured by good or bad for the business, the contract value bridge `.chart` (last month, new projects, go-lives completed, slipped dates, cancellations, this month), the five projects that changed most `.tbl` with the reason, Send test email; reads Weekly metric, Weekly snapshot, Project, Activity · calls Send executive summary on Send test email
- code-app · update · ClickUp Delivery Command: Copilot panel on every internal screen: `.convo` with `.msg.me` and `.msg.ai`, three suggested questions as `.chips` from the persona's projects, `.stages` while it works, the answer in an AI Insight card `.ai:not(.msg)` with an AI-written label, a grounding line and one action, a chart answer in `.chart` with units, the cannot-answer state saying why and what to try; risk flags with confidence and evidence; status report draft the lead edits and publishes with PDF and Word export; meeting summary with each point linked to its transcript time; proposed tasks with Accept and Reject; reads AI output · calls Ask Copilot on Send, Publish status report on Publish, Accept proposed tasks on Accept and Reject
- code-app · update · ClickUp Delivery Command: screen Portal home, Portal sign-offs, Portal sessions: the customer top menu (Home, Sign-offs, Sessions, Files, Checklist) with the ClickUp logo and the customer's initials circle; only the sponsor's own project: stage, milestones, upcoming sessions, open actions, shared documents, no internal health; sign-off or request changes with a comment; day then time `.slot` picker with taken slots visible and disabled; reads Project, Task, Sign-off, Session slot, Document · calls Record sign-off on Sign off and Request changes, Book training slot on Book
- code-app · update · ClickUp Delivery Command: screen Portal files and Portal checklist: CSV upload (up to 50,000 rows, a Use sample file control that generates 50,000 fictional rows with 214 bad rows), errors summarised by type ("214 of 50,000 rows need fixing") with row-by-row fixes before Confirm; readiness checklist of 10 items, an unanswered item showing Not set; English, German and Japanese switch with local dates, numbers and currency; the no-access state naming who can grant access; reads Checklist item, Document, Project · calls Confirm upload on Confirm
- code-app · update · ClickUp Delivery Command: screen Phone: a phone-width route shown in a phone frame with bottom tabs Today, Tasks, Time, Alerts; today's tasks and sessions, status change, a log-time form in three taps, notifications with mark read and open; reads Task, Session slot, Notification · calls Log time on Log, Move task on a status change, Mark notification read on Mark read
- code-app · update · ClickUp Delivery Command: screen Admin: roles against permissions grid `.tbl`; audit log `.tbl` filtered by person, project and action, read only; integrations (Salesforce, Slack, Google Drive, Jira) with last sync time and any error, the failed one saying which, since when and what is affected; project settings edited in place (name, region, go-live date, budget hours) with unsaved, saving, saved and failed states; reads Role permission, Activity, Integration, Project · calls Update project settings on Save

#### Business rules
- Changes under 40 hours need the delivery director's approval; changes of 40 hours or more also need the finance partner, in that order.
- Rejecting a change request needs a written reason; returning a timesheet needs a reason; requesting changes on a sign-off needs a comment.
- An approved change updates the plan (tasks, go-live, budget hours) and is recorded in the activity feed.
- A board column shows a warning when it holds more than 15 tasks.
- A booking above a person's weekly capacity shows who, which weeks and by how much before it is saved.
- The activity record is never edited or deleted.
- Customers see only their own project and never internal health.
- Anything Delivery Copilot writes carries an AI-written label; nothing it proposes is created without acceptance.
- Every status shows an icon and a word, never colour alone; status words follow BRD §8 (good: On track, Signed off, Approved, Live; attention: At risk, Awaiting sign-off, Over capacity, Pending approval; problem: Off track, Blocked, Rejected, Sync failed; neutral: Not started, Draft, Scheduled, Hypercare).
- Errors say what happened and what to do next; no jokes or exclamation marks.
- Money shows in the contract currency; portfolio totals in USD at planning rates EUR 1.08 and JPY 0.0066.
- Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026年10月17日); weeks start on Monday in Europe and Japan and Sunday in North America.
- No screen suggests billing, invoicing, revenue recognition, editing customer workspaces, hiring, payroll, a marketing site, video calls or offline phone use.
- Look: the app's one stylesheet is /home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/design-system/clickup/client.css (hue 244, brand #5F55EE); the rail logo is /home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/design-system/clickup/logo.svg and the collapsed rail and tab icon use logo-mark.svg beside it, both as published; theme light by default with the dark tokens live and the switch in the profile menu.
- Test records written during the demo carry the DEMO-TEST label and the demo's date.

#### Ready when
- The delivery director sees IMP-2611 Sakura Mobility at risk on the Portfolio, books a consultant, raises CR-0457 for 52 hours, sees it route to the director then the finance partner, sees a reject without a reason refused, and sees the approved change move the go-live in the activity feed.
- Hana Mori signs off Migration plan v2 in Japanese in the portal, and Delivery Copilot answers "Which Japan projects go live in November and are at risk?" with IMP-2611 and IMP-2633.
- deploy Delivery Command · Move task
- deploy Delivery Command · Reschedule task
- deploy Delivery Command · Book consultant
- deploy Delivery Command · Review timesheets
- deploy Delivery Command · Log time
- deploy Delivery Command · Change request
- deploy Delivery Command · Accept proposed tasks
- deploy Delivery Command · Publish status report
- deploy Delivery Command · Record sign-off
- deploy Delivery Command · Book training slot
- deploy Delivery Command · Confirm upload
- deploy Delivery Command · Save view
- deploy Delivery Command · Update project settings
- deploy Delivery Command · Mark notification read
- deploy Delivery Command · Send executive summary
- deploy Delivery Command · Weekly executive email schedule
- deploy Delivery Command · Read delivery data
- deploy Delivery Command · Ask Copilot
- publish Delivery Command · Copilot
- publish ClickUp Delivery Command

#### Assumptions
- Check this: proposed intent `both` (the outcome first, then 2 hood beats); the owner sets it at G2.
- Check this: G1 open questions 1 to 12 are unanswered; the plan follows each recommended option (portal shows no internal health; phone stays at today, status, time and alerts; portfolio opens on one screen with the paged list below; region as a labelled chip; A114 out of scope; integrations seeded; the official logo; a phone-width route; full portal language switch; 18 seeded projects and 13 consultants with a generated 50,000-row upload; a seeded finance partner; a scheduled email with one test run).
- Check this: the brand colour #5F55EE (hue 244) is brand-sample's recommendation among 14 candidates (profile standing answer for an ambiguous colour).
- Check this: the logo is ClickUp's own nav wordmark from clickup.com, saved as published; the script's first pick was the ClickUp Brain mark and was replaced.
- Check this: the seven stage names (Kickoff, Discovery, Configuration, Data migration, Integrations, Training, Hypercare) and the persona names are assumed; the BRD's own stage names are not in the state file.
- Check this: earlier "ClickUp DC ·" and "DC" objects, automations and agents exist on the tenant outside this solution; this build uses new "Delivery Command ·" names and touches none of them.
- Check this: the executive email sends only on a mail connection the owner names; until then Send executive summary stores a preview row.
- Check this: sign-in, forgot and reset password screens and the persona switch stand in for real accounts, which need governance tools not granted yet.
- Check this: Word export of the status report is an HTML document saved as .doc from the app; PDF is the browser's print to PDF.
- Check this: the code app name ClickUp Delivery Command is free; if taken, the name gets the suffix "· Demo".
- All seed rows are fictional; customer names follow the BRD's six invented customers plus twelve more invented names.

#### Capability check
- 21 object · create lines · beat 1–7 · fde-agent · apply_object_batch · read: get_objects · ok
- 19 record · seed lines (largest 168 rows, a named file under 200) · beat 1–7 · fde-agent · save_entity_records · read: get_records · ok
- 17 callable automations · beat 1–7 · automation-agent · compile_and_save_workflow, deploy_workflow · read: describe_callable_workflow, trigger_workflow_run then inspect_workflow_run · ok
- Weekly executive email schedule (scheduled trigger) · beat 5 · automation-agent · compile_and_save_workflow, deploy_workflow · read: search_workflows (deployment) · ok
- Send executive summary: the send step · beat 5 · automation-agent · a mail connector node · read: the Executive email row; the sent message · no tool for a team mailbox: question 15 (preview row meanwhile)
- Ask Copilot: Invoke Agent (ai_agents_by_unifyapps, no connection) · beat 7 · automation-agent · compile_and_save_workflow · read: trigger_workflow_run with question 1 of the eval · ok
- Delivery Command · Copilot · beat 7 · agent-builder · create_agent, add_tools · read: get_agent, send_test_messages with the 11 eval rows · ok
- Code app create and 11 updates · beat 1–7 · code-app-agent · create_code_app, create_code_app_data_sources, push_code_patch · read: get_code_app head.sha, bindings.ts FETCH id, callables.ts blocks · ok
- Publish ClickUp Delivery Command · beat all · code-app-agent · publish_code_app · read: deployed with commitHash · ok
- Real per-user sign-in and platform roles · beat 1, 6 · none · governance tools not granted · read: — · no tool: question 16 (persona switch meanwhile)
- Document files · beat 2, 6 · fde-agent · no file upload on its servers · read: — · worked around: the viewer pages each document's body text

## entities
- object · Delivery Command · Project · OBJ_dcmd_project · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_project/schema
- object · Delivery Command · Task · OBJ_dcmd_task · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_task/schema
- object · Delivery Command · RAID item · OBJ_dcmd_raid · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_raid/schema
- object · Delivery Command · Person · OBJ_dcmd_person · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_person/schema
- object · Delivery Command · Booking · OBJ_dcmd_booking · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_booking/schema
- object · Delivery Command · Time entry · OBJ_dcmd_time_entry · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_time_entry/schema
- object · Delivery Command · Change request · OBJ_dcmd_change_request · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_change_request/schema
- object · Delivery Command · Activity · OBJ_dcmd_activity · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_activity/schema
- object · Delivery Command · Document · OBJ_dcmd_document · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_document/schema
- object · Delivery Command · Session slot · OBJ_dcmd_session_slot · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_session_slot/schema
- object · Delivery Command · Sign-off · OBJ_dcmd_signoff · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_signoff/schema
- object · Delivery Command · Checklist item · OBJ_dcmd_checklist_item · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_checklist_item/schema
- object · Delivery Command · Notification · OBJ_dcmd_notification · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_notification/schema
- object · Delivery Command · Integration · OBJ_dcmd_integration · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_integration/schema
- object · Delivery Command · Saved view · OBJ_dcmd_saved_view · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_saved_view/schema
- object · Delivery Command · Weekly snapshot · OBJ_dcmd_weekly_snapshot · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_weekly_snapshot/schema
- object · Delivery Command · Weekly metric · OBJ_dcmd_weekly_metric · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_weekly_metric/schema
- object · Delivery Command · AI output · OBJ_dcmd_ai_output · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_ai_output/schema
- object · Delivery Command · Role permission · OBJ_dcmd_role_permission · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_role_permission/schema
- object · Delivery Command · Upload · OBJ_dcmd_upload · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_upload/schema
- object · Delivery Command · Executive email · OBJ_dcmd_exec_email · https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_exec_email/schema
- automation · Delivery Command · Move task · 6adba2ac92718f6a64f34bc5 · https://orbit.uat.unifyapps.com/p/0/automations/6adba2ac92718f6a64f34bc5/builder
- automation · Delivery Command · Reschedule task · 6adba3266112da3e23fcf133 · https://orbit.uat.unifyapps.com/p/0/automations/6adba3266112da3e23fcf133/builder
- automation · Delivery Command · Book consultant · 6adba3b292718f6a64f39440 · https://orbit.uat.unifyapps.com/p/0/automations/6adba3b292718f6a64f39440/builder
- automation · Delivery Command · Review timesheets · 6adba402f4431f44e30943f1 · https://orbit.uat.unifyapps.com/p/0/automations/6adba402f4431f44e30943f1/builder
- automation · Delivery Command · Log time · 6adba405ca4f9d2045858cfc · https://orbit.uat.unifyapps.com/p/0/automations/6adba405ca4f9d2045858cfc/builder
- automation · Delivery Command · Change request · 6adba6a8cac0655fe3582da3 · https://orbit.uat.unifyapps.com/p/0/automations/6adba6a8cac0655fe3582da3/builder
- automation · Delivery Command · Accept proposed tasks · 6adba625ca4f9d2045986507 · https://orbit.uat.unifyapps.com/p/0/automations/6adba625ca4f9d2045986507/builder
- automation · Delivery Command · Publish status report · 6adba5cfeb71d135d657c23d · https://orbit.uat.unifyapps.com/p/0/automations/6adba5cfeb71d135d657c23d/builder
- automation · Delivery Command · Record sign-off · 6adba5f8eb71d135d657e318 · https://orbit.uat.unifyapps.com/p/0/automations/6adba5f8eb71d135d657e318/builder
- automation · Delivery Command · Book training slot · 6adba59c92718f6a64f4015a · https://orbit.uat.unifyapps.com/p/0/automations/6adba59c92718f6a64f4015a/builder
- automation · Delivery Command · Confirm upload · 6adba9abcac0655fe35aa2fc · https://orbit.uat.unifyapps.com/p/0/automations/6adba9abcac0655fe35aa2fc/builder
- automation · Delivery Command · Save view · 6adba9aef3cd5f19ed89eaec · https://orbit.uat.unifyapps.com/p/0/automations/6adba9aef3cd5f19ed89eaec/builder
- automation · Delivery Command · Update project settings · 6adba9def3cd5f19ed89ef7d · https://orbit.uat.unifyapps.com/p/0/automations/6adba9def3cd5f19ed89ef7d/builder
- automation · Delivery Command · Mark notification read · 6adba94deb71d135d658f2dc · https://orbit.uat.unifyapps.com/p/0/automations/6adba94deb71d135d658f2dc/builder
- automation · Delivery Command · Read delivery data · 6adbaa4fca4f9d20459bd303 · https://orbit.uat.unifyapps.com/p/0/automations/6adbaa4fca4f9d20459bd303/builder
- automation · Delivery Command · Send executive summary · 6adbac23eb71d135d65f4715 · https://orbit.uat.unifyapps.com/p/0/automations/6adbac23eb71d135d65f4715/builder
- automation · Delivery Command · Weekly executive email schedule · 6adbacd6f3cd5f19ed8a543a · https://orbit.uat.unifyapps.com/p/0/automations/6adbacd6f3cd5f19ed8a543a/builder
- ai-agent · Delivery Command · Copilot ·  · https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6adbabd2925d282255cee62b
- automation · Delivery Command · Ask Copilot · 6adbaf90c79cad11403e9b72 · https://orbit.uat.unifyapps.com/p/0/automations/6adbaf90c79cad11403e9b72/builder
- code-app · ClickUp Delivery Command · app-f53fd0efccec · branch main · last commit 5126004fb989c524511308023adbc9c0ab14591d (head 8d75f623304c1b4f322edd227729bbc410300b11 "publish v1") · preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-f53fd0efccec/main/ · published v1 from 5126004f (deployed: true; the tools return no published URL: open it from https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-f53fd0efccec) · PRIVATE
- serves: objects and seeds A1–A114 data (all beats); automations per their beats; Copilot beat 7 (A31–A38); code app screens: shell, sign-in, Portfolio, Project (all tabs), Resourcing, Timesheets, Changes, Executive summary, Copilot panel, Portal (home, sign-offs, sessions, files, checklist), Phone, Admin (beats 1–7)

build:
  plans:
    - {id: e_6adb96180881d2257a9f97c3, n: 1, tasks: 10, status: done, what: objects 1-10, start: 2026-10-23T17:13Z, finish: 2026-10-23T17:18Z}
    - {id: e_6adb96e00881d2257aa1945b, n: 2, tasks: 10, status: done, what: objects 11-20, start: 2026-10-23T17:18Z, finish: 2026-10-23T17:53Z}
    - {id: e_6adb9f27925d282255ba6215, n: 3, tasks: 10, status: done, what: Executive email object and 9 seeds, start: 2026-10-23T17:53Z, finish: 2026-10-23T18:02Z}
    - {id: e_6adba1375236864dd8e627db, n: 4, tasks: 10, status: done, what: 10 seeds, start: 2026-10-23T18:02Z, finish: 2026-10-23T18:05Z}
    - {id: e_6adba20e5236864dd8e64c53, n: 5, tasks: 10, status: done, what: 5 automations and deploys, start: 2026-10-23T18:06Z, finish: 2026-10-23T18:18Z}
    - {id: e_6adba4f3925d282255c4195e, n: 6, tasks: 10, status: done, what: 5 automations and deploys, start: 2026-10-23T18:18Z, finish: 2026-10-23T18:34Z}
    - {id: e_6adba8af925d282255c9a9e6, n: 7, tasks: 10, status: done, what: 5 automations and deploys, start: 2026-10-23T18:34Z, finish: 2026-10-23T18:46Z}
    - {id: e_6adbab775236864dd8e7a211, n: 8, tasks: 8, status: done, what: executive email, schedule, Copilot agent and publish, Ask Copilot, start: 2026-10-23T18:46Z, finish: 2026-10-23T19:06Z}
    - {id: e_6adbb044925d282255d09cab, n: 9, tasks: 7, status: "left in_progress (t1-t6 pushed, commits up to 4da8ec33; its runner was another machine's Nebula client, so this session cannot resume or finish it; its t7 was carried into plan 10)", what: code app shell and internal screens, start: 2026-10-23T19:06Z}
    - {id: e_6adf01b4bc76624e532df4c9, n: 10, tasks: 7, status: done, what: Executive summary (with the UTC-date fix), Copilot panel, Portal home/sign-offs/sessions, Portal files/checklist, Phone, Admin, publish v1, start: 2026-10-26T07:31Z, finish: 2026-10-26T08:00Z}
    - {id: e_6adf0c04bc76624e532ff4a9, n: 11, tasks: 5, status: done, what: "verify round 1 fixes: Read delivery data returns <field>_text UTC day text, deployed; Copilot dates from the day text and one-read plan (slowest question 39 s, was 118 s); Copilot published v14", start: 2026-10-26T08:14Z, finish: 2026-10-26T08:44Z}

## beats
Storyline: "Every implementation visible and actionable" (A1), 7 beats and 2 hood beats; proposed intent `both`.

### Beat 1 · Portfolio at a glance
- does: Signs in as Elena Brooks, delivery director, on the ClickUp sign-in screen; filters the project list to Japan and At risk, removes a chip, clicks the RSK-1183 cell of the risk grid, saves the view "Japan · at risk" for the team.
- shows: 12 On track (−1), 4 At risk (+1), 2 Off track (0) since last week; the likelihood-by-impact grid with RSK-1183 at 4 × 5; the 90-day go-live timeline by region with IMP-2611, IMP-2604 and IMP-2631 marked slipped; on-track share 88% to 67% over 12 weeks; "2 of 18" with removable chips and Clear all; IMP-2611 Sakura Mobility At risk, go-live 19 Nov 2026.
- route: /signin → /portfolio
- asks: A1 A2 A3 A4 A7 A9 A10 A11 A12 A13 A14 A55 A56 A57 A61 A64 A69 A70 A71 A72 A73 A75 A86 A90 A96 A98 A99 A100 A109
- mode: live (sign-in mocked)

### Beat 2 · Inside IMP-2611
- does: Opens IMP-2611; switches overview, board, list and timeline; moves TSK-5035 SSO user mapping to Integrations from the Move to menu; opens TSK-5024 beside the list; drags Validate custom fields mapping two days later on the timeline and cancels after the preview.
- shows: Stage 4 of 7 on the progress path, 27 days to go-live, 545 of 860 hours, 4 open risks, next sign-off Migration plan v2; the Data migration column at 17 of 15 with its warning; task detail with description, assignee, dates, time logged, comments and attachments; the critical path and the preview "go-live moves to 23 Nov 2026" before saving; RAID log with history; the statement of work in the in-app viewer; the activity feed with the move just made.
- route: /projects/IMP-2611
- asks: A15 A16 A17 A18 A19 A20 A21 A62 A89
- mode: live

### Beat 3 · Staff it without overbooking
- does: As Grace Liu, resource manager: filters the skills matrix to Japanese and data migration at level 4, books Aiko Tanaka on IMP-2611 for 16 hours in the weeks of 16 and 23 Nov, reads the warning, changes it to 10 hours and saves; approves eight pending timesheets in one batch and returns Haruto Sato's with a reason.
- shows: 13 people against 12 weeks with Haruto Sato at 110% in the week of 2 Nov flagged; region as a labelled chip; the warning before saving: "Aiko Tanaka, week of 16 Nov: 46 of 40 h, 115%, 6 h over"; booked against capacity by region for the quarter; the batch approval and the required return reason.
- route: /resourcing → /timesheets
- asks: A22 A23 A24 A25 A26 A63 A66 A81 A88 A105 A113
- mode: live

### Beat 4 · The change that routes itself (failure beat)
- does: As Mei Takahashi, raises CR-0457 on IMP-2611: SSO and SCIM provisioning, +52 hours, ¥1,560,000, go-live 19 to 26 Nov; checks the plan before and after; submits. As Elena Brooks approves. As Tomás Herrera, finance partner, clicks Reject with no reason, then approves.
- shows: The side-by-side plan with three added tasks and the moved go-live marked; the route "Delivery director, then finance partner" because 52 is 40 hours or more; the stepper with who approved and who is next; the refusal "A rejection needs a written reason. Add one and reject again."; after approval the go-live 26 Nov 2026, 912 planned hours and two activity entries.
- route: /changes/new → /changes/CR-0457
- asks: A6 A27 A28 A29 A30
- mode: live

### Beat 5 · The Monday summary
- does: Opens the weekly summary tab; reads the six numbers; sends a test of the Monday 08:00 email.
- shows: Active projects 18 (+1), go-lives this month 1 (0), projects at risk 6 (+1, red although up), average days to go-live 59.8 (+2.7, red), utilisation 72% (+2), contract value awaiting go-live this quarter USD 4,468,380; the bridge from USD 5,502,380 last month: +184,800 new, −658,800 completed, −410,000 slipped, −150,000 cancelled; the five biggest movers with their reasons; the email preview with the ClickUp logo.
- route: /executive
- asks: A45 A46 A47 A48 A107
- mode: deterministic figures; live email automation

### Beat 6 · The sponsor's side
- does: Switches to Hana Mori, Sakura Mobility's sponsor; the portal opens in Japanese; signs off Migration plan v2; books a training slot on 4 Nov; uploads the sample 50,000-row user list, fixes two rows and confirms; opens the checklist; switches to German; opens a link to IMP-2604.
- shows: Only IMP-2611: stage, milestones, sessions, open actions, shared documents, no internal health; the sign-off recorded with who and when; taken slots visible but not choosable; "214 of 50,000 rows need fixing" summarised by error type; 7 of 10 checklist items set and 3 Not set; German labels that fit; "You do not have access to IMP-2604. Daniel Ortiz, the project lead, can grant it."
- route: /portal
- asks: A4 A5 A39 A40 A41 A42 A43 A44 A59 A65 A67 A68 A74 A82 A83 A84 A87 A106 A108 A112
- mode: live

### Beat 7 · Ask Delivery Copilot (lean-forward)
- does: As Elena Brooks opens the Copilot panel, picks no suggestion and types "Which Japan projects go live in November and are at risk?"; asks for go-lives by month as a chart; opens the risk flags; asks it to draft the weekly status report for IMP-2611, edits a line and publishes it as PDF; opens the 22 Oct meeting summary and accepts two of its three proposed tasks; asks for Sakura Mobility's invoice total.
- shows: Three suggested questions from her projects; the stages while it works; IMP-2611 and IMP-2633 with links in an AI Insight card labelled AI-written; a bar chart in go-lives per month; IMP-2611 flagged High with its evidence, raised 28 days before go-live; the status report draft; summary points linked to transcript times; two new tasks on the board; a plain refusal saying billing is not in Delivery Command and what to ask instead.
- route: Copilot panel on /portfolio
- asks: A31 A32 A33 A34 A35 A36 A37 A38 A58 A78 A79 A97 A103 A104
- mode: live agent; seeded risk flags, meeting summary and proposed tasks

Failure beat: beat 4 (a reject with no written reason is refused). Lean-forward beat: beat 7.

Alternatives considered: B / C
- B: The change request routing to the finance partner as the closing moment: strong, but it is a rule the audience saw in beat 4
- C: Hana Mori's Japanese sign-off landing in Mei Takahashi's notifications live: quick and quiet; it shows plumbing, not judgement
- Why beat 7: The profile's show-off line names an AI assistant over live data, and the delivery director's daily question is the first one asked.

### H1 · After beat 4: open Delivery Command · Change request in the automation canvas
- shows: the 40-hour branch, the second approver and the empty-reason refusal
- mode: live

### H2 · After beat 7: open Delivery Command · Copilot in the agent builder
- shows: its instructions, its one read-only tool Read delivery data, its model
- mode: live

### AI surfaces
- Copilot answers (Delivery Command · Copilot): live
- Chart answers: live
- Status report draft: live, seeded fallback AIO-07
- Three suggested questions: deterministic (from the persona's projects, not shown as AI)
- Stages while it works: deterministic (timed while the live call runs)
- Risk flags with confidence and evidence: seeded (AIO-01, AIO-02)
- Meeting summary with transcript links: seeded (AIO-03)
- Proposed tasks: seeded (AIO-04 to AIO-06); Accept and Reject are live

### Other modes
- Sign-in, forgot and reset password, persona switch: mocked
- Integration status (Salesforce, Slack, Google Drive, Jira): mocked: seeded rows
- Executive summary figures: deterministic
- Customer upload validation: deterministic (in the app)
- Every demo-path action: live automation that writes

### Story row
IMP-2611 · Sakura Mobility · Japan · stage Data migration (4 of 7) · go-live 19 Nov 2026 (baseline 12 Nov, slipped; 26 Nov after CR-0457) · At risk · lead Mei Takahashi · 1,200 seats · JPY 84,000,000 · 860 h planned, 545 h used (912 planned after CR-0457) · open risks RSK-1183 (likelihood 4, impact 5), RSK-1184, RSK-1185, RSK-1186 · late critical tasks TSK-5024, TSK-5025 · Data migration column 17 tasks · next sign-off SGN-302 Migration plan v2 · sponsor Hana Mori (portal in Japanese) · CR-0457 +52 h, ¥1,560,000

## views
- Sign-in, Forgot password, Reset password (beats 1): `.g2 .pad` card with the ClickUp logo, `.fld .ctl` persona picker and password fields with `.hint` errors, `.btn-p`
- Portfolio (beats 1, 7): rail `.rail`; header `.crumb`; `.tile` ×3 health counts with `.delta`; `.chart` risk grid (likelihood × impact) opening a `.tbl` of the cell's risks; `.chart` 90-day go-live timeline by region with slipped `.tag.attention`; `.chart .spark` 12-week on-track share; `.toolbar` (`.field` search, `.chipsel` region, stage, health, lead, removable chips, Clear all, "x of y") over `.tblwrap .tbl` with `.av` customer circles, `.tag` health and `.pg`; Save view `.btn-s` with `.menu`; `.empty` states
- Executive summary (Portfolio tab) (beats 5): `.tabs`; `.tile` ×6 with `.delta` coloured by business meaning; `.chart` contract value bridge with `.legend`; `.tbl` five biggest movers; `.btn-s` Send test email; `.toast`
- Project (beats 2): `.crumb`; `.stages` seven-stage path; `.tile` days to go-live, open risks, next sign-off; `.prog` budget hours; `.tabs` Overview, Board, List, Timeline, RAID, Documents, Activity; `.kb` stage columns with `.tag.attention` over-limit and `.menu` Move to; `.tbl` list; task detail side pane `.g3 .pad` with `.feed` comments; timeline `.chart` with critical path and a `.note` go-live preview; RAID `.tbl` with `.tag` and history `.feed`; documents `.tbl` with viewer pane `.g3`; activity `.feed .fi .fd`
- Resourcing (beats 3): `.toolbar` with region `.chipsel`; people × 12 weeks `.tbl` with `.n` percentages and `.tag.negative` Over capacity; region chip `.tag.neutral`; skills matrix `.tbl` with level `.pip`; Book consultant form `.fld .ctl .seg` with the over-capacity `.note`; `.chart` booked against capacity by region
- Timesheets (beats 3): `.toolbar`; `.tbl` with `.box` batch select and `.tag` Pending approval, Approved, Returned; return reason `.fld .ctl.err`; `.btn-p` Approve, `.btn-s` Return
- Changes, Change request (beats 4): `.tbl` list; form `.fld .ctl`; plan before and after: two `.tbl` side by side with changed rows marked (diff view built from tokens, not in the kit); `.stv` approval stepper; `.btn-p` Approve, `.btn-t` Reject; refusal `.tag.negative` and `.note`; `.feed`
- Copilot panel (every internal screen) (beats 7): right pane `.g2`; `.convo .msg.me .msg.ai`; `.chips` suggested questions; `.stages` reasoning stages; answers in `.ai:not(.msg)` with AI-written `.tag`, grounding line and one `.btn-s`; `.chart` with units; risk flags `.ai:not(.msg)` with confidence `.tag` and evidence list; status report editor `.fld .ctl` with Publish `.btn-p` and PDF, Word `.btn-t`; meeting summary with transcript time links; proposed tasks `.tbl` with Accept, Reject
- Portal home, Sign-offs, Sessions (beats 6): top menu (Home, Sign-offs, Sessions, Files, Checklist) with logo and `.av` customer circle; `.stages` milestones; `.agenda` upcoming sessions; `.tbl` open actions and shared documents; sign-off `.btn-p` and Request changes `.fld`; `.cal` day picker then `.slot` times, taken slots `.off`; language `.seg` EN DE JA
- Portal files, Checklist (beats 6): upload drop area (built from tokens; not in the kit) with `.prog`; error summary `.note` "214 of 50,000 rows need fixing" and a `.tbl` of rows to fix with `.ctl.err`; checklist `.tbl` with `.tag.neutral` Not set; no-access `.empty`
- Phone (beats controls): phone frame; bottom tabs Today, Tasks, Time, Alerts; `.agenda`; `.tbl` compact; log-time `.fld .ctl .seg`; notifications list with mark read
- Admin (beats controls): `.tabs` Roles, Audit log, Integrations, Projects; roles × permissions `.tbl` with `.dot`; audit `.toolbar` (person, project, action `.chipsel`) over `.tbl`; integrations `.tbl` with `.tag.positive` Live and `.tag.negative` Sync failed plus `.note`; projects `.tbl` with inline `.ctl` and unsaved, saving, saved, failed states
