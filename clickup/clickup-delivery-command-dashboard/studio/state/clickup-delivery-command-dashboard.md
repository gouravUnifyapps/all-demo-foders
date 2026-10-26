---
use_case: ClickUp Delivery command dashboard
client: Clickup
poc_row: POC-clickup-delivery-command-dashboard-20261026
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: verifying
version: 1 · since 2026-10-26T09:54:26Z
channel: C0CBXB542R1
threads:
  g1: 1793009027.033199
  g2: 1793013856.930499
  g3:
  g4:
intent: both (the outcome first, then one hood beat on the approval automation and the Copilot) · by Gourav Mahunta (G2 approval)
stage_flag:

gates:
  g1: {status: approved, round: 1, posted_ts: 1793009027.033199, decided_by: Gourav Mahunta, decided_at: 2026-10-26T11:01:49Z}
  g2: {status: approved, round: 1, posted_ts: 1793013856.930499, decided_by: Gourav Mahunta, decided_at: 2026-10-26T11:59:00Z}
  g3: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
  g4: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }

posts:
  - when: 2026-10-26T10:03:55Z
    kind: g1
    ts: 1793009027.033199
    by: bot
    version: 1
    round: 1
  - when: 2026-10-26T10:04:05Z
    kind: status
    ts: 1793009027.033199
    by: bot
    version: 1
    round: 1
  - when: 2026-10-26T11:24:30Z
    kind: g2
    ts: 1793013856.930499
    by: bot
    version: 1
    round: 1
  - when: 2026-10-26T11:25:00Z
    kind: status
    ts: 1793013856.930499
    by: bot
    version: 1
    round: 1

runs:
  - started: 2026-10-26T09:54:26Z
    ended: 2026-10-26T10:04:05Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 145
    outcome: posted G1
  - started: 2026-10-26T11:04:28Z
    ended: 2026-10-26T11:24:03Z
    gate: g2
    stages: [2-plan]
    spawns: 1
    tokens: 297
    outcome: posted G2
  - started: 2026-10-26T12:03:26Z
    gate: g3

stopped:

asks:
  - id: A1
    text: "Earlier warning: a project at risk of missing its go-live date is flagged at least three weeks before the date, on average."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A2
    text: "Less reporting effort: weekly status reports take a consultant under 10 minutes instead of about an hour."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A3
    text: "Balanced staffing: no consultant is booked above 100% for more than one week in a quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A4
    text: "Faster customer sign-off: customers approve deliverables in the portal within two working days."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A5
    text: "Delivery Command should make all three visible and actionable."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 2 Background · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A6
    text: "Brand colour: none supplied. Take it from the live site clickup.com."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A7
    text: "Logo: no file supplied. Fetch the official logo. It appears on the sign-in page, the expanded and collapsed left menu, the browser tab icon, the customer portal header, generated status reports (PDF and Word), and the weekly executive email."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A8
    text: "Customer logos: shown as circles on project cards and in the portal."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A9
    text: "Typeface: take it from the live site. Numbers must line up in tables. The customer portal must also display Japanese and German text correctly."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A10
    text: "Tone: clear, calm and direct. Errors say what happened and what to do next. No jokes or exclamation marks in the product."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A11
    text: "Feel: the internal workspace is a daily working tool and should stay dense and quiet. The customer portal and the executive summary are also shown in sales demos and should look polished."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A12
    text: "Appearance: light and dark both needed. Light is the default."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A13
    text: "List every project with customer, region, stage, go-live date, health, lead, seats and contract value. Users search and filter by region, stage, health and lead. The count of results shows as \"x of y\". Filters that apply show as removable chips with one \"clear all\"."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A14
    text: "Show portfolio health as counts of On track, At risk and Off track, with the change since last week."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A15
    text: "Place each open risk on a grid of likelihood against impact, so leaders see which risks matter most. Choosing a cell lists its risks."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A16
    text: "Show every go-live date in the next 90 days on a timeline, grouped by region, with slipped dates marked."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A17
    text: "Show how the share of projects on track has moved over the last 12 weeks."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A18
    text: "Leaders can save a filtered view and share it with their team."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A19
    text: "A project overview shows the stage the project is in, the seven stages as a progress path, days to go-live, budget hours used against planned, open risks and the next customer sign-off due."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A20
    text: "Tasks can be viewed as a list or as a board with one column per stage. A column shows a warning when it holds more than its limit (default 15). Tasks can be moved between columns by dragging or from a menu."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A21
    text: "A timeline shows tasks with start and end dates, dependencies between them and the critical path. Changing a date moves dependent tasks and shows the new go-live date before it is saved."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A22
    text: "A risks, assumptions, issues and decisions (RAID) log records each item with owner, due date, status and history."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A23
    text: "A document library holds the statement of work, migration plans and sign-off records. Files open in a viewer inside the application."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A24
    text: "An activity feed shows who changed what and when on the project."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A25
    text: "Task detail opens beside the list so the user keeps their place. It shows description, assignee, dates, time logged, comments and attachments."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W7 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A26
    text: "Show every consultant against the next 12 weeks with the percentage they are booked each week. Over 100% is flagged."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A27
    text: "Book a consultant onto a project by choosing person, project, weeks and hours. Booking works without dragging."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A28
    text: "Show consultants against skills (data migration, integrations, admin training, API, Japanese language) with a level for each, so the right person can be found."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A29
    text: "Consultants log time against tasks each day. Managers approve or return weekly timesheets, giving a reason when they return one."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A30
    text: "Should: show booked hours against capacity for each region over the quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A31
    text: "An implementation lead raises a change request with the reason, the work added or removed, and the effect on hours, cost and go-live date."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A32
    text: "Before submitting, the lead sees the plan before and after the change side by side, with the differences marked."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A33
    text: "Changes under 40 hours need the delivery director's approval. Changes of 40 hours or more also need the finance partner, in that order. The request shows who has approved and who is next."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A34
    text: "Rejecting a change request requires a written reason. Approved changes update the plan and are recorded in the activity feed."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A35
    text: "Delivery Copilot is an AI assistant available from every internal screen. It has the tools listed below. Anything it writes is labelled as AI-written."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot (intro) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A36
    text: "Users ask questions in plain language, for example \"Which Japan projects go live in November and are at risk?\" The assistant opens with three suggested questions based on the user's projects, and shows each stage while it works."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A37
    text: "Chart tool: the assistant can answer with a chart, such as hours by stage or go-lives by month. Charts use the application's colours and show units."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A38
    text: "Status report tool: the assistant drafts the weekly status report for a project from its tasks, risks and time entries. The lead edits and publishes it. The report can be exported as PDF or Word."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A39
    text: "Task tool: the assistant can propose tasks, for example after a meeting summary. Proposed tasks are listed for the user to accept or reject; nothing is created without acceptance."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A40
    text: "Meeting summary tool: the assistant summarises a customer meeting transcript into decisions, actions and risks. Each point links to the part of the transcript it came from."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A41
    text: "Risk prediction: the assistant flags projects likely to miss go-live, with a confidence level and the evidence for each flag, such as migration tasks running late."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A42
    text: "Customer sponsors sign in to see only their own project: stage, milestones, upcoming sessions, open actions for their team and the documents shared with them."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A43
    text: "Sponsors sign off a stage deliverable or request changes with a comment. A sign-off records who approved and when."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A44
    text: "Sponsors book training sessions by choosing a day and then a time slot. Taken slots stay visible but cannot be chosen."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A45
    text: "Sponsors upload files such as user lists (CSV up to 50,000 rows). Errors appear row by row and can be fixed before confirming."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A46
    text: "A readiness checklist guides the customer through 10 setup items. An item they have not answered shows as not set, never as a guessed value."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A47
    text: "The portal is available in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A48
    text: "A weekly summary shows six headline numbers with their change from last week: active projects, go-lives this month, projects at risk, average days to go-live, consultant utilisation and contract value awaiting go-live. A change is coloured by whether it is good or bad for the business, not by its sign."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A49
    text: "Show how contract value awaiting go-live moved from last month to this month, split into new projects, go-lives completed, slipped dates and cancellations."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A50
    text: "List the five projects that changed most this week, with the reason for each."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A51
    text: "The summary is also sent as an email every Monday at 08:00 in each region's time zone."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A52
    text: "Consultants see today's tasks and sessions, update a task's status, and log time in under 30 seconds on a phone."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.8 Consultant on the phone M1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A53
    text: "Notifications for new assignments, sign-offs and mentions. Each can be marked read or opened."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.8 Consultant on the phone M2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A54
    text: "Roles control what each user can see and change. Show roles against permissions as a grid."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.9 Administration and audit D1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A55
    text: "Keep a record of who did what and when. It cannot be edited and can be filtered by person, project and action."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.9 Administration and audit D2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A56
    text: "Show the status of each integration (Salesforce, Slack, Google Drive, Jira) with last sync time and any error."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.9 Administration and audit D3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A57
    text: "Project settings (name, region, go-live date, budget hours) can be edited in place, with clear unsaved, saving, saved and failed states."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.9 Administration and audit D4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A58
    text: "Sign-in, forgot password, reset password"
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 6 Screens (screen row: Everyone, First release) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A59
    text: "Internal users navigate with a left menu: Portfolio, Projects, Resourcing, Timesheets, Changes, Admin. The top bar shows the current project or view, search, notifications and the profile menu. Delivery Copilot opens as a panel on the right."
    source: "ClickUp-Delivery-Command-BRD.pdf p.6 § 6 Navigation · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A60
    text: "Customers get a shorter top menu: Home, Sign-offs, Sessions, Files, Checklist."
    source: "ClickUp-Delivery-Command-BRD.pdf p.6 § 6 Navigation · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A61
    text: "The phone has bottom tabs: Today, Tasks, Time, Alerts."
    source: "ClickUp-Delivery-Command-BRD.pdf p.6 § 6 Navigation · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A62
    text: "Active projects | 180 to 300 | Portfolio list needs paging, search and filters"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A63
    text: "Tasks per project | 150 to 1,200 | Board and timeline must stay readable"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A64
    text: "Consultants and leads | about 72 | Resourcing grid is people against 12 weeks"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A65
    text: "Open risks across the portfolio | about 400 | Grid of likelihood against impact, with drill-down"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A66
    text: "Customer users | about 900 | Portal must be simple for occasional users"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A67
    text: "Time entries per week | about 3,000 | Timesheet approval in batches"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A68
    text: "Customer upload | up to 50,000 rows | Errors summarised, not listed in full"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A69
    text: "Languages | English, German, Japanese | Text can grow by 30% in German"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A70
    text: "Good or finished | On track, Signed off, Approved, Live"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A71
    text: "Needs attention | At risk, Awaiting sign-off, Over capacity, Pending approval"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A72
    text: "Problem | Off track, Blocked, Rejected, Sync failed"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A73
    text: "Neutral | Not started, Draft, Scheduled, Hypercare"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A74
    text: "Project IDs look like IMP-2611, change requests like CR-0457, risks like RSK-1183."
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Sample content · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A75
    text: "Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026 年 10 月 17 日). Money shows in the contract currency (USD, EUR or JPY)."
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Sample content · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A76
    text: "No projects assigned yet | Projects appear here once a lead assigns you"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A77
    text: "A search or filter matches nothing | Nothing matches the current filters, with a way to clear them"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A78
    text: "Copilot is still working | Which stage it is on"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A79
    text: "Copilot cannot answer | Why, and what to try instead"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A80
    text: "An integration has failed | Which one, since when, and what is affected"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A81
    text: "A booking takes someone over capacity | Who, which weeks and by how much, before saving"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A82
    text: "A customer upload has errors | For example 214 of 50,000 rows need fixing"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A83
    text: "A checklist item has no answer | The item shows as not set"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A84
    text: "The user has no access to a project | Who can grant access"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A85
    text: "The session is about to end | How to stay signed in"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A86
    text: "Data is out of date | When it was last updated"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A87
    text: "The internal workspace is in English. The customer portal is in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A88
    text: "Times show the user's time zone. Weeks start on Monday in Europe and Japan and on Sunday in North America."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A89
    text: "All drag actions also work from the keyboard. Controls are at least 24 px on desktop and larger on the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A90
    text: "Meaning never depends on colour alone: every status shows an icon and a word."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A91
    text: "Screens meet WCAG 2.2 AA in both light and dark appearance."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A92
    text: "Salesforce | Contract value, seats and close date when a deal is won, which creates the project"
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 11 Integrations (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A93
    text: "Slack | Notifications and the weekly status post to each project channel"
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 11 Integrations (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A94
    text: "Google Drive | Shared documents and customer uploads"
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 11 Integrations (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A95
    text: "Jira | Engineering escalations linked to project issues"
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 11 Integrations (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A96
    text: "The first release does not include the following, and the application must not suggest otherwise: • Billing, invoicing or revenue recognition. • Building or editing customer workspaces in the core ClickUp product. • Hiring, performance reviews or payroll for consultants. • A public marketing site. • Video calls or call recording. • Offline use of the phone view."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 12 Out of scope · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A97
    text: "Executive time to read the weekly summary | 10 minutes or less"
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 13 Success measures (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A98
    text: "Customers completing the readiness checklist without help | 75%"
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 13 Success measures (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: built
  - id: A99
    text: "I want to see every project on one screen without scrolling."
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 14 Stakeholder notes, delivery director · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A100
    text: "Let us edit the timeline straight from the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 14 Stakeholder notes, consultants · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A101
    text: "Show customers their health score."
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 14 Stakeholder notes, VP of customer success · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A102
    text: "Customers should never see internal health."
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 14 Stakeholder notes, implementation leads · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A103
    text: "Colour-code consultants by region everywhere."
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 14 Stakeholder notes, resource manager · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A104
    text: "Add a pricing calculator for upsells."
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 14 Stakeholder notes, Sales · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Sales upsell pricing calculator"
    status: out_of_scope

coverage:
  - ask: A1
    by: beat 6
  - ask: A2
    by: beat 6
  - ask: A3
    by: beat 4
  - ask: A4
    by: beat 5
  - ask: A5
    by: beat 6
  - ask: A6
    by: beat 1
  - ask: A7
    by: beat 1
  - ask: A8
    by: beat 1
  - ask: A9
    by: open question 13
  - ask: A10
    by: beat 3
  - ask: A11
    by: beat 1
  - ask: A12
    by: control Appearance (Light, Dark) in the profile menu on every internal screen
  - ask: A13
    by: beat 1
  - ask: A14
    by: beat 1
  - ask: A15
    by: beat 1
  - ask: A16
    by: beat 1
  - ask: A17
    by: beat 1
  - ask: A18
    by: beat 1
  - ask: A19
    by: beat 2
  - ask: A20
    by: beat 2
  - ask: A21
    by: beat 2
  - ask: A22
    by: beat 2
  - ask: A23
    by: control Documents tab and viewer on Project workspace
  - ask: A24
    by: beat 2
  - ask: A25
    by: beat 2
  - ask: A26
    by: beat 4
  - ask: A27
    by: beat 4
  - ask: A28
    by: beat 4
  - ask: A29
    by: control Approve or Return with reason on Timesheets
  - ask: A30
    by: control Region capacity tab on Resourcing
  - ask: A31
    by: beat 2
  - ask: A32
    by: beat 2
  - ask: A33
    by: beat 3
  - ask: A34
    by: beat 3
  - ask: A35
    by: beat 6
  - ask: A36
    by: beat 6
  - ask: A37
    by: beat 6
  - ask: A38
    by: beat 6
  - ask: A39
    by: control Proposed tasks Accept or Reject on Copilot panel
  - ask: A40
    by: control Meeting summary tab with transcript links on Copilot panel
  - ask: A41
    by: beat 6
  - ask: A42
    by: beat 5
  - ask: A43
    by: beat 5
  - ask: A44
    by: beat 5
  - ask: A45
    by: beat 5
  - ask: A46
    by: beat 5
  - ask: A47
    by: beat 5
  - ask: A48
    by: beat 1
  - ask: A49
    by: beat 1
  - ask: A50
    by: beat 1
  - ask: A51
    by: open question 11
  - ask: A52
    by: control Today tab (status, log time) on Phone view
  - ask: A53
    by: control Alerts tab (mark read, open) on Phone view
  - ask: A54
    by: open question 15
  - ask: A55
    by: control Audit log filters (person, project, action) on Admin
  - ask: A56
    by: control Integrations tab on Admin
  - ask: A57
    by: control Settings tab inline edit on Project workspace
  - ask: A58
    by: open question 14
  - ask: A59
    by: beat 1
  - ask: A60
    by: beat 5
  - ask: A61
    by: control Bottom tabs Today, Tasks, Time, Alerts on Phone view
  - ask: A62
    by: beat 1
  - ask: A63
    by: control List view paging and Board column limits on Project workspace
  - ask: A64
    by: beat 4
  - ask: A65
    by: beat 1
  - ask: A66
    by: control Portal sign-in for the 900 customer users (Haruto Mori persona) on Portal
  - ask: A67
    by: control Approve selected (batch) on Timesheets
  - ask: A68
    by: beat 5
  - ask: A69
    by: control Language switch EN, DE, JA on Portal
  - ask: A70
    by: beat 1
  - ask: A71
    by: beat 1
  - ask: A72
    by: beat 1
  - ask: A73
    by: beat 1
  - ask: A74
    by: beat 2
  - ask: A75
    by: beat 2
  - ask: A76
    by: control No projects assigned yet empty state (persona with none) on Portfolio
  - ask: A77
    by: control Nothing matches the current filters, Clear all on Portfolio
  - ask: A78
    by: beat 6
  - ask: A79
    by: beat 6
  - ask: A80
    by: control Jira Sync failed row with since and affected on Admin
  - ask: A81
    by: beat 4
  - ask: A82
    by: beat 5
  - ask: A83
    by: beat 5
  - ask: A84
    by: control No access screen naming who can grant access on Portal
  - ask: A85
    by: control Session ending banner with Stay signed in on every internal screen
  - ask: A86
    by: control Last updated line on Executive summary
  - ask: A87
    by: beat 5
  - ask: A88
    by: beat 4
  - ask: A89
    by: control Move to menu and keyboard move on the Board on Project workspace
  - ask: A90
    by: beat 1
  - ask: A91
    by: control Appearance (Light, Dark) in the profile menu on every internal screen
  - ask: A92
    by: open question 10
  - ask: A93
    by: open question 11
  - ask: A94
    by: open question 10
  - ask: A95
    by: open question 10
  - ask: A96
    by: beat 6
  - ask: A97
    by: beat 1
  - ask: A98
    by: beat 5
  - ask: A99
    by: open question 3
  - ask: A100
    by: open question 4
  - ask: A101
    by: open question 5
  - ask: A102
    by: open question 5
  - ask: A103
    by: open question 6

size:
  pages: 10
  objects: 17
  automations: 14
  agents: 1
  tasks: 87
  nebula_plans: 9
  reference: 4 pages, 3 objects, 3 automations, 1 AI agent

data:
  source: "assumed, fictional, shaped like the BRD's sample content (six named customers, IMP-/CR-/RSK- ids, USD/EUR/JPY); no file given"
  masked: "none: fictional (invented names, @example.com emails, no phones, no real identifiers)"
  rows:
    - "Project: 18, record · seed (story row IMP-2611 Sakura Mobility first)"
    - "Task: 20, record · seed (all IMP-2611)"
    - "RAID item: 20, record · seed"
    - "Change request: 2, record · seed (CR-0457 raised live in beat 2)"
    - "Person: 16, record · seed"
    - "Booking: 18, record · seed"
    - "Time entry: 20, record · seed"
    - "Deliverable: 5, record · seed"
    - "Session slot: 12, record · seed"
    - "Document: 8, record · seed"
    - "Activity: 20, record · seed"
    - "AI output: 8, record · seed (AI-written)"
    - "Weekly metric: 12, record · seed"
    - "Saved view: 2, record · seed"
    - "Checklist item: 10, record · seed"
    - "Integration: 4, record · seed"
    - "Notification: 8, record · seed"
  where: UnifyApps Storage objects (OBJ_cucmd_*)
  expected_answers: eval.csv

verify:
  round: 1
  walked_at: 2026-10-26T13:56Z to 14:07Z (cloud container, Playwright browser; no Claude_Browser)
  beats_pass: "0 of 7 (7 unverified: sign-in; beats 1-6 and H1)"
  controls_pass: "0 of 0 measured (every control on the 10 beat screens unverified: sign-in)"
  queries_pass: "9 of 10"
  coverage_pass: "0 of 90 (unverified: sign-in; no screen could be opened)"
  checks_pass: "1 of 7 (stylesheet verbatim pass, from the checkout; the other six unverified: sign-in)"
  p95_latency_s: 64
  latency_target_s: 90
  browser: "published https://app-a2a9509a82c1-orbit.tensor-uat.unifyapps.com/ lands on /login?returnTo=%2F (Log in to your account); preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-a2a9509a82c1/main/ lands on the tenant /login. No password typed; tab closed."
  beats:
    - "1 Summary and portfolio: unverified: sign-in. Tool proof: external step read back on Gmail connection 6980e13788c7735877a8311c with gmail_get_message 1a17847cf729b474: label SENT, To gourav.mahunta@unifyapps.com, Subject 'DEMO-TEST · ClickUp Delivery Command · weekly summary · week of 26 Oct 2026', snippet 161 on track / 38 at risk / 15 off track (the build's test send at 12:55Z; not re-sent in this walk, so no run in the walk window). Sender header is a staff member's personal gmail.com mailbox (open question 12)."
    - "2 Workspace and CR-0457: unverified: sign-in. Tool proof: Raise change request test run 6adf5e4608750d257cf6455f, preview true, IMP-2611 +56 h JPY 1,120,000 +5 days: result preview, cr_code CR-0457, before 1,480 h / 16 Nov 2026, after 1,536 h / 21 Nov 2026, route Delivery director then Finance partner; wrote nothing."
    - "3 Approval rule and refusal: unverified: sign-in. Tool proof: Decide change request deployed run 6adf5e2608750d257cf64366 (cr_code DEMO-TEST-CR-0000, finance_partner, reject, empty reason): result refused_reason_required before any read or write. CR-0457 not decided."
    - "4 Resourcing: unverified: sign-in. Tool proof: Book consultant test run 6adf5e45c79cad1140c0a89e (P-07 Yui Sato, IMP-2611, weeks of 9 and 16 Nov, 16 h, confirm false): result over_capacity, 48 of 40 h = 120%, 8 h over in each week; wrote nothing."
    - "5 Portal in Japanese: unverified: sign-in (no safe tool run: sign-off D-2611-5 not touched)."
    - "6 Copilot: unverified: sign-in for the panel, stages, chart rendering and Publish/PDF. Agent live: traces for every eval row (cases below); status report draft (case e_6adf5cfc6112da3e23bb7f49) has Summary, Progress, Risks, Next week with Go live, 16 Nov 2026, At risk, RSK-1183, 1,236 of 1,480 h."
    - "H1 Under the hood: unverified: sign-in (builder canvas not opened). open_workflow shows Decide change request deployed v2, 15 nodes, first branch 'A reject needs a written reason'."
  queries:
    - "1 Japan November at risk: pass, 12 s (case e_6adf5c1dca4f9d20458076c6): IMP-2611 Sakura Mobility, 16 Nov 2026, At risk; Tsubame not listed."
    - "2 Go-lives by month chart: pass, 45 s (case e_6adf5c2c08750d257cf61657): Nov 6, Dec 4, Jan 2, Feb 2, Mar 2 (plus Oct 2026 2), unit projects."
    - "3 Likely to miss go-live: pass, 36 s (case e_6adf5c9608750d257cf61cb4): Sakura 78 with the three evidence lines, Nordwerk 64, Fjordline 52."
    - "4 Weekly status report: pass, 64 s (case e_6adf5cfc6112da3e23bb7f49, from trace); a first send (case e_6adf5cc0ca4f9d20458084c4) ended 'The agent hit an unexpected error ... (provider error: HTTP 400, invalid_request_error)' after three parallel ReadDeliveryData calls."
    - "5 On track / At risk / Off track: fail, 9 s (case e_6adf5d79f3cd5f19ed9378ac): counts 161/38/15 right, but 'For the week starting 20 Oct 2026' (the row is week_start 1792972800000 = 26 Oct 2026) and no comparison with last week's 159/33/19."
    - "6 Over 100% in 12 weeks: pass, 34 s (case e_6adf5d9397a3bf334d6f9aa9): Jonas Weber 44 of 40 h, about 110%, weeks of 16 and 23 Nov 2026 (shows the raw code 'over_capacity' twice)."
    - "7 Steering meeting 22 Oct: pass, 34 s (case e_6adf5dbdf3cd5f19ed938134)."
    - "8 Invoice total (refusal): pass, 3 s: declines, points to finance or billing."
    - "9 Change go-live date (refusal): pass, 4 s: declines, points to a change request in the app."
    - "10 Haruto Mori phone (refusal): pass, 7 s: says the data holds no phone numbers."
  latency_note: "seconds are wall time from send to answer with runAgainToFindAnswer (a first send returned no case id), so rows 1-3 and 5-10 may include a second run; row 4 is from its trace. Slowest = p95 with 10 rows."
  checks:
    - "brand on the primary action only: unverified: sign-in"
    - "no horizontal scroll: unverified: sign-in"
    - "both empty states reachable: unverified: sign-in (source has both 'No items yet.' and 'No rows match your search and filters' with Clear all in ProjectsTable, TaskList, Raid, Documents, Changes, CapacityGrid, Skills, Admin, Phone)"
    - "table readable at 1440: unverified: sign-in"
    - "no console errors: unverified: sign-in"
    - "stylesheet verbatim: pass, by byte hash on the checkout (not the page): app/src/styles/design-system.css minus its two @import lines = sha256 805b73e8f1f3a731ff5cd9a5cf7a7dfaa4577de79b6d7b3703ddbad51bd77c0e = studio/design-system/clickup/client.css; imported once in App.tsx"
    - "logo contrast: unverified: sign-in"
  agent_state: "ClickUp Command Copilot draft version 10, needsPublish true (the eval ran the saved draft; the state file records published version 5)"
  demo_test_records: "none created in this walk (preview, over_capacity and refusal runs write nothing); agent test conversations only"
  open:
    - "ai-agent · update · ClickUp Command Copilot: in the date rules add the anchor 1 Oct 2026 = 1790812800000, so week_start 1792972800000 reads 26 Oct 2026, and portfolio health answers name that week and compare it with the previous weekly_metrics row (161, 38, 15 against 159, 33, 19); nothing else changes"
    - "ai-agent · update · ClickUp Command Copilot: show stored flags and codes as words in answers (over_capacity is Over capacity), never a backticked field name; nothing else changes"
    - "ai-agent · update · ClickUp Command Copilot: publish the saved draft (version 10, needsPublish true) so the app's Copilot answers as the eval did; nothing else changes"
    - "ai-agent · update · ClickUp Command Copilot: the model is offered EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy and ClarifyFromUser (capability off) though only ReadDeliveryData is attached (read_trace toolsOffered, every case); remove them from what the runtime offers; nothing else changes · platform"
    - "ai-agent · update · ClickUp Command Copilot: a turn with three parallel ReadDeliveryData calls ended 'provider error: HTTP 400, invalid_request_error' (case e_6adf5cc0ca4f9d20458084c4); the same message answered on resend; nothing else changes · platform"
    - "code-app · update · ClickUp Delivery Command: every screen: the empty state names its items ('No change requests yet.', 'No projects yet.', 'No risks yet.' and so on) instead of the literal 'No items yet.'; nothing else changes"

collaterals:

review:

decisions:
  - by: orchestrator
    when: 2026-10-26
    text: "Profile studio/profiles/clickup.md drafted by Studio from the request and defaults."
  - by: orchestrator
    when: 2026-10-26
    text: "Preflight: collateral kit python packages MISSING (doctor.sh); blocks G4 (6-collaterals) until poc-studio:poc-collateral-setup installs them. Bun, Chromium (Playwright), ffmpeg, poppler, Slack read tools and the tenant sign-in are ok."
  - by: profile
    when: 2026-10-26
    text: "A7 (no logo file supplied): fetch the official logo from clickup.com; if none can be fetched, a text wordmark placeholder, listed in the G2 pack (standing answer: no logo)."
  - by: profile
    when: 2026-10-26
    text: "A6 (brand colour from clickup.com): if the sampled colour is ambiguous, the recommended one, listed in the G2 pack (standing answer: ambiguous brand colour)."
  - by: harvest
    when: 2026-10-26
    text: "Kickoff harvest read the whole #clickup-test-4 history, the BRD (Slack file and psl_document input row), psl_feedback (none) and Gmail (none). Not read: Google Calendar (connector needs sign-in again), call recordings (none shared), Google Drive (not connected)."
  - by: state-check
    when: 2026-10-26
    text: "reverted stage_flag: written by harvest, outside its fields (schema § Who writes what)"

  - by: orchestrator
    when: 2026-10-26
    text: "render-doc.mjs made no PDF on the cloud runner (root, Playwright Chromium without --no-sandbox); 1-harvest rendered the requirements PDF with Playwright's Chromium headless --no-sandbox directly."
  - by: Gourav Mahunta
    when: 2026-10-26
    text: "G1 approved in POC Studio (row g1_status approved; reply \"Approved\" in G1's thread). The 11 G1 open questions were not answered by number; they stay open for 2-plan."

  - by: profile
    when: 2026-10-26
    text: "A6 brand colour: clickup.com sampled ambiguous; took the recommended #5F55EE (hue 244, --ProductScreen-CustomStatus-Primary). Other candidates listed in the G2 pack: #6647F0 Core-Accents-Purple, #7612FA Table-Accent, #0091FF Core-Accents-Blue, #FC6D2D Core-Accents-Orange, #FF02F0 Core-Accents-Pink (standing answer: ambiguous brand colour)."
  - by: plan
    when: 2026-10-26
    text: "A7 logo: the official ClickUp wordmark (header svg, aria-label ClickUp) and symbol (/assets/brand/logo-v3-clickup-symbol-only.svg) fetched from clickup.com into studio/design-system/clickup/; brand-sample's first pick was the ClickUp Brain mark and was replaced. No placeholder needed."
  - by: profile
    when: 2026-10-26
    text: "AI agent model: Nebula's recommendation (standing answer: model)."
  - by: plan
    when: 2026-10-26
    text: "Modes beyond the default: the status report draft is live (the read-only agent drafts text; a live automation publishes it); the Copilot's working stages are deterministic (shown by the app while the call runs); integrations status and the roles grid are mocked; documents open as stored text in an in-app viewer (mocked files)."
  - by: plan
    when: 2026-10-26
    text: "External step: the weekly summary email through the existing Gmail connection 6980e13788c7735877a8311c (probed read-only with gmail_list_signatures: ok), sent once to the presenter, subject DEMO-TEST; fallback the in-app preview."
  - by: plan
    when: 2026-10-26
    text: "G1 questions 1, 3, 4, 5, 6, 8, 9, 10 and 11 are still open; the plan is built around each recommended option (a) and lists it under the build contract's Assumptions."
  - by: plan
    when: 2026-10-26
    text: "Names: the tenant already holds 'Delivery Command · …' and 'ClickUp DC · …' objects and automations and three Copilot agents outside this solution; this demo uses the free names 'ClickUp Command · …' (OBJ_cucmd_*), 'ClickUp Command Copilot' and the code app 'ClickUp Delivery Command', and touches none of the others."

  - by: Gourav Mahunta
    when: 2026-10-26
    text: "G2 approved (row g2_status approved; reply \"approve\" in G2's thread). Open questions 1-16 were not answered by number; the build follows each recommended option (a) as the build contract's Assumptions say. Intent: both."
  - by: state-check
    when: 2026-10-26
    text: "reverted stage_flag: written by verify, outside its fields (schema § Who writes what)"

dev_issues: []

frozen:

cost:
  runs: 2
  agent_spawns: 2
  tokens_m: 0.45
  wall_h: 0.6

build:
  plans:
    - id: e_6adf42d7dc07493166cdc058
      tasks: 10
      status: done
      started: 2026-10-26T12:05:00Z
      finished: 2026-10-26T12:11:00Z
    - id: e_6adf4385dc07493166cdd028
      tasks: 10
      status: done
      started: 2026-10-26T12:11:00Z
      finished: 2026-10-26T12:15:00Z
    - id: e_6adf4476769c8b649e93b28a
      tasks: 10
      status: done
      started: 2026-10-26T12:15:00Z
      finished: 2026-10-26T12:21:00Z
    - id: e_6adf45cbdc07493166ce0071
      tasks: 10
      status: done
      started: 2026-10-26T12:21:00Z
      finished: 2026-10-26T12:30:00Z
    - id: e_6adf47d508f96579542f5180
      tasks: 9
      status: done
      started: 2026-10-26T12:30:00Z
      finished: 2026-10-26T12:40:00Z
    - id: e_6adf4a4f08f96579542f8822
      tasks: 9
      status: done
      started: 2026-10-26T12:40:00Z
      finished: 2026-10-26T12:50:00Z
    - id: e_6adf4cbbdc07493166ce9964
      tasks: 9
      status: done
      started: 2026-10-26T12:50:00Z
      finished: 2026-10-26T12:58:00Z
    - id: e_6adf4e82769c8b649ebf1b17
      tasks: 10
      status: done
      started: 2026-10-26T12:58:00Z
      finished: 2026-10-26T13:14:00Z
    - id: e_6adf5240769c8b649ebf944c
      tasks: 10
      status: done
      started: 2026-10-26T13:14:00Z
      finished: 2026-10-26T13:53:00Z
    - id: e_6adf5ef808f965795444ffac
      tasks: 4
      status: done
      started: 2026-10-26T14:09:00Z
      finished: 2026-10-26T14:17:00Z

open_questions:
  - by: harvest
    for: lead
    text: "1. Scope of this use case. The POC is named \"Delivery command dashboard\", but the BRD (A1–A104) describes the whole Delivery Command application: 13 screen groups, an internal workspace, a customer portal, a phone view and an AI assistant. The BRD also calls itself an illustrative scenario. Options: (a) One app covering every ask, with the storyline led by the portfolio dashboard, the executive summary and Delivery Copilot (recommended) (b) The dashboard screens only (portfolio, executive summary, Copilot); the other areas logged as other use cases (c) The whole BRD with equal weight on every screen"
  - by: harvest
    for: lead
    text: "2. Priority. The BRD marks every § 5 requirement as Must unless marked Should, so 50 asks are P0 (all of § 5 except R5, plus the must-worded brand, navigation, sign-in and out-of-scope lines). Keep them all P0? Options: (a) Keep all 50 as P0; the plan shows each one somewhere, the storyline picks the lean-forward few (recommended) (b) The lead names the P0 set for the 20-minute demo and the rest become P1"
  - by: harvest
    for: lead
    text: "3. A99, delivery director: \"I want to see every project on one screen without scrolling.\" The BRD also says 180 to 300 projects and a paged list (A62, P1). Options: (a) A compact portfolio overview (health counts, risk grid, go-live timeline) above the paged list, so the whole portfolio reads on one screen (recommended) (b) Every project as a dense tile wall on one screen (c) Paged list only; the note is declined and recorded"
  - by: harvest
    for: lead
    text: "4. A100, consultants: \"Let us edit the timeline straight from the phone.\" Options: (a) Decline: the phone keeps M1 and M2 (status, time, notifications); the timeline stays a desktop screen (recommended) (b) Allow date changes from the phone with the W3 preview of the new go-live date"
  - by: harvest
    for: lead
    text: "5. A101 vs A102: the VP of customer success wants customers to see their health score; implementation leads say customers should never see internal health. Options: (a) Hide internal health from the portal; customers see stage, milestones and open actions (C1) only (recommended) (b) Show a customer-facing readiness score in the portal, separate from internal health (c) Show internal health in the portal"
  - by: harvest
    for: lead
    text: "6. A103, resource manager: \"Colour-code consultants by region everywhere.\" The BRD also says meaning never depends on colour alone (A90) and keeps status colours (A70–A73). Options: (a) A labelled region tag with its own colour on consultant rows and avatars, never colour alone (recommended) (b) Region colour in the resourcing grid only (c) Decline and record it"
  - by: harvest
    for: lead
    text: "7. A104, Sales: \"Add a pricing calculator for upsells.\" Logged under Other use cases; the BRD's out of scope (A96) excludes billing and revenue. Options: (a) Leave it out of this use case (recommended) (b) Reply promote A104 to bring it in"
  - by: harvest
    for: lead
    text: "8. Demo data volume. The profile says fictional data, 15 to 20 rows; the BRD speaks of 180 to 300 projects, about 72 consultants and about 400 risks, and names six sample customers. Options: (a) 15 to 20 projects built around the six named sample customers, with headline counts on the dashboards seeded to read like the BRD's portfolio (recommended) (b) Seed the full BRD volumes (about 250 projects, 72 consultants, 400 risks)"
  - by: harvest
    for: lead
    text: "9. Phone view (M1, M2, A61). The BRD asks for a phone with bottom tabs Today, Tasks, Time, Alerts. Options: (a) A responsive phone layout of the same code app, shown in a phone frame (recommended) (b) A separate native mobile app"
  - by: harvest
    for: lead
    text: "10. Integrations (A92–A95, D3): Salesforce, Slack, Google Drive and Jira. The profile allows only connections already on the tenant. Options: (a) Use a connection where one already exists on the tenant; show the rest on the integration status screen with seeded sync times and one seeded Sync failed row (recommended) (b) Seeded status only, no live connection at all"
  - by: harvest
    for: lead
    text: "11. Weekly executive email (E4) and the weekly Slack status post (A93). Options: (a) Generate the email and post as previews in the app, and send one real email to the presenter during the demo (recommended) (b) Preview only, nothing sent (c) Send to a demo Slack channel and inbox on a schedule"
  - by: plan
    for: owner
    text: "12. External mailbox. The only Gmail connections on the tenant are individual staff mailboxes; the one named Gmail passed a read-only probe. Options: (a) Send the one demo summary email from the tenant's Gmail connection to the presenter, subject DEMO-TEST (recommended) (b) Preview in the app only, nothing sent (c) The owner names another connection"
  - by: plan
    for: owner
    text: "13. Typeface (A9). clickup.com sets Inter for body text (Plus Jakarta Sans in places); the design system carries Archivo. Options: (a) Inter with tabular figures, Noto Sans JP for Japanese, IBM Plex Mono kept for eyebrows (recommended) (b) Keep the design system's Archivo"
  - by: plan
    for: owner
    text: "14. Sign-in, forgot and reset password (A58). No tool builds a custom sign-in page for a code app. Options: (a) The tenant's own sign-in, forgot and reset pages a PRIVATE app opens with (recommended) (b) A ClickUp-branded sign-in screen inside the app, as a mock with no real sign-in"
  - by: plan
    for: owner
    text: "15. Roles and permissions (A54). Nebula's governance tools are not granted on this tenant, so no real roles can be made. Options: (a) A persona switcher in the profile menu (Lead, Director, Finance partner, Resource manager, Consultant, Sponsor) and a roles-against-permissions grid from seeded rows (recommended) (b) Real tenant roles and permission groups, once governance tools are granted"
  - by: plan
    for: owner
    text: "16. Intent. Options: (a) both: the outcome first, then one hood beat on the approval automation and the Copilot (recommended) (b) use-case: no hood beat (c) platform: two to four hood beats, 8 to 12 seed rows"
  - by: verify
    for: owner
    text: "17. Round 1 verify could not open the app: the published address and the preview both land on the tenant sign-in in the cloud runner's browser, and no password is typed. All 7 beats, every control on the 10 beat screens, the coverage walk of the 90 built asks and six of the seven checks are unverified: sign-in. Options: (a) Run the verify walk on the presenter's Mac, where the built-in browser is signed in to the tenant (recommended) (b) Save a test user's sign-in for the Playwright browser and re-run verify here (c) Make the app PUBLIC for the walk and PRIVATE again after"
  - by: verify
    for: owner
    text: "18. The weekly summary email (beat 1) is sent through Gmail connection 6980e13788c7735877a8311c, whose mailbox is a staff member's personal gmail.com address (From: Rishabh Jain); the room will see that sender. Options: (a) Keep it for the demo and say so in the presenter notes (recommended) (b) Name a company mailbox connection to send from (c) Show the in-app preview only"
---

## build_contract

### Touches
- object · ClickUp Command · Project · new
- object · ClickUp Command · Task · new
- object · ClickUp Command · RAID item · new
- object · ClickUp Command · Change request · new
- object · ClickUp Command · Person · new
- object · ClickUp Command · Booking · new
- object · ClickUp Command · Time entry · new
- object · ClickUp Command · Deliverable · new
- object · ClickUp Command · Session slot · new
- object · ClickUp Command · Document · new
- object · ClickUp Command · Activity · new
- object · ClickUp Command · AI output · new
- object · ClickUp Command · Weekly metric · new
- object · ClickUp Command · Saved view · new
- object · ClickUp Command · Checklist item · new
- object · ClickUp Command · Integration · new
- object · ClickUp Command · Notification · new
- automation · ClickUp Command · Save view · new
- automation · ClickUp Command · Update task · new
- automation · ClickUp Command · Raise change request · new
- automation · ClickUp Command · Decide change request · new
- automation · ClickUp Command · Book consultant · new
- automation · ClickUp Command · Timesheet action · new
- automation · ClickUp Command · Portal action · new
- automation · ClickUp Command · Accept proposed tasks · new
- automation · ClickUp Command · Publish status report · new
- automation · ClickUp Command · Send executive summary · new
- automation · ClickUp Command · Update project settings · new
- automation · ClickUp Command · Mark notification read · new
- automation · ClickUp Command · Read delivery data · new
- automation · ClickUp Command · Ask Copilot · new
- connection · Gmail · 6980e13788c7735877a8311c
- ai-agent · ClickUp Command Copilot · new
- code-app · ClickUp Delivery Command · new

### Contract

#### object · ClickUp Command · Project
One customer implementation, from signed contract to Hypercare; the story row is IMP-2611.

- object · create · ClickUp Command · Project: id `OBJ_cucmd_project`; fields project_code (text, primaryKey, required, e.g. `IMP-2611`), customer (text, required), industry (text), region (picklist: europe "Europe", north_america "North America", japan "Japan"), stage (picklist: kickoff "Kickoff", discovery "Discovery", configuration "Configuration", migration "Migration", training "Training", go_live "Go-live", hypercare "Hypercare"), go_live_date (date, epoch ms), original_go_live_date (date, epoch ms; set only when the date slipped), health (picklist: on_track "On track", at_risk "At risk", off_track "Off track"), health_last_week (same codes as health), lead (text), sponsor (text), seats (number), contract_value (number), currency (picklist: usd "USD", eur "EUR", jpy "JPY"), budget_hours_planned (number), budget_hours_used (number), column_limit (number, default 15), next_signoff (text), next_signoff_due (date, epoch ms), timezone (text, IANA name)
- record · seed · ClickUp Command · Project: IMP-2611 Sakura Mobility, Automotive, japan, go_live, go-live 2026-11-16, health at_risk, last week on_track, lead Kenji Arai, sponsor Haruto Mori, 9200 seats, 62400000 jpy, 1480 planned, 1236 used, column_limit 15, next sign-off "Cutover plan" due 2026-10-29, Asia/Tokyo; IMP-2604 Halden Freight, Logistics, europe, migration, 2026-12-07, on_track/on_track, Mira Lindqvist, 4800, 386000 eur, 1100/640, Europe/Oslo; IMP-2598 Corvia Health, Healthcare, north_america, configuration, 2027-01-18 (original 2026-12-14), off_track/at_risk, Dana Whitfield, sponsor Grace Lin, 12000, 910000 usd, 2400/1310, America/Chicago; IMP-2615 Brightmoor University, Education, europe, training, 2026-11-23, on_track/on_track, Mira Lindqvist, 2300, 142000 eur, 620/510, Europe/London; IMP-2621 Kestrel Energy, Energy, north_america, discovery, 2027-02-22, on_track/on_track, Sam Okafor, 7500, 540000 usd, 1650/210, America/Denver; IMP-2587 Ostrander Retail, Retail, north_america, hypercare, 2026-10-12, on_track/on_track, Dana Whitfield, 650, 48000 usd, 260/248, America/New_York; IMP-2618 Tsubame Insurance, Insurance, japan, migration, 2026-11-27, on_track/on_track, Kenji Arai, 3100, 21600000 jpy, 900/610, Asia/Tokyo; IMP-2609 Nordwerk Maschinenbau, Manufacturing, europe, go_live, 2026-11-09, at_risk/at_risk, Jonas Weber, 5600, 412000 eur, 1300/1190, Europe/Berlin; IMP-2624 Lumen Bank, Financial services, north_america, kickoff, 2027-03-15, on_track/on_track, Sam Okafor, 8800, 720000 usd, 1900/40, America/New_York; IMP-2602 Fjordline Media, Media, europe, configuration, 2026-12-14 (original 2026-11-30), at_risk/on_track, Jonas Weber, 1400, 96000 eur, 520/300, Europe/Oslo; IMP-2612 Hikari Foods, Food and beverage, japan, training, 2026-12-01, on_track/on_track, Aiko Tanaka, 2600, 18200000 jpy, 700/520, Asia/Tokyo; IMP-2595 Redwater Logistics, Logistics, north_america, go_live, 2026-11-02, on_track/on_track, Dana Whitfield, 3900, 260000 usd, 980/900, America/Chicago; IMP-2619 Alpenrose Hotels, Hospitality, europe, discovery, 2027-02-08, on_track/on_track, Mira Lindqvist, 1800, 118000 eur, 560/60, Europe/Vienna; IMP-2607 Meridian Pharma, Pharmaceuticals, north_america, migration, 2026-12-21 (original 2026-11-23), off_track/off_track, Sam Okafor, 6400, 480000 usd, 1500/1010, America/New_York; IMP-2626 Kawase Electronics, Electronics, japan, kickoff, 2027-03-01, on_track/on_track, Aiko Tanaka, 5200, 34800000 jpy, 1200/20, Asia/Tokyo; IMP-2600 Solberg Telecom, Telecommunications, europe, hypercare, 2026-10-05, on_track/on_track, Jonas Weber, 4100, 290000 eur, 940/930, Europe/Oslo; IMP-2613 Prairie State Credit Union, Financial services, north_america, training, 2026-11-30, at_risk/on_track, Dana Whitfield, 1200, 84000 usd, 410/330, America/Chicago; IMP-2622 Minato Travel Group, Travel, japan, configuration, 2027-01-11, on_track/on_track, Kenji Arai, 2000, 14000000 jpy, 640/220, Asia/Tokyo. Every date is epoch ms at UTC midnight.

#### object · ClickUp Command · Task
One task in a project plan, with stage, dates, dependencies and the critical path.

- object · create · ClickUp Command · Task: id `OBJ_cucmd_task`; fields task_code (text, primaryKey, required), project_code (text, required), title (text, required), description (text), stage (the seven Project stage codes), status (picklist: not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee (text), start_date (date, epoch ms), end_date (date, epoch ms), depends_on (text, comma-separated task_codes, finish-to-start), critical (boolean), hours_logged (number), comments_json (text), attachments_json (text), source (picklist: manual "Manual", copilot "Copilot")
- record · seed · ClickUp Command · Task: twenty tasks of IMP-2611, codes T-2611-01 to T-2611-20: 01 Kickoff workshop (kickoff, done); 02 Discovery interviews (discovery, done); 03 Workspace design sign-off (discovery, done); 04 Configure spaces and statuses (configuration, done); 05 SSO configuration (configuration, done); 06 User list migration wave 1 (migration, done, 6 days late); 07 User list migration wave 2 (migration, in_progress, Yui Sato, 2026-10-19 to 2026-10-30, late 5 days, critical); 08 Data migration: projects (migration, in_progress, Yui Sato, critical, late 4 days); 09 Data migration: docs (migration, blocked, Daichi Ono, late 5 days); 10 Integration test Salesforce (migration, in_progress, Priya Raman); 11 Admin training (training, done); 12 End-user training Tokyo (training, done); 13 End-user training Osaka (training, in_progress); 14 SSO cutover rehearsal 1 (go_live, done, failed); 15 SSO cutover rehearsal 2 (go_live, in_progress, critical, 2026-10-26 to 2026-11-03); 16 Cutover plan sign-off (go_live, not_started, critical, depends on 15); 17 Go-live readiness review (go_live, not_started, critical, depends on 16); 18 Production cutover (go_live, not_started, critical, 2026-11-14 to 2026-11-16, depends on 17); 19 Hypercare rota (hypercare, not_started, depends on 18); 20 Hypercare exit review (hypercare, not_started, depends on 19). Stage go_live holds 5 tasks; the Board shows the column limit from column_limit.

#### object · ClickUp Command · RAID item
One risk, assumption, issue or decision on a project, with likelihood and impact.

- object · create · ClickUp Command · RAID item: id `OBJ_cucmd_raid`; fields raid_code (text, primaryKey, required, e.g. `RSK-1183`), project_code (text, required), kind (picklist: risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title (text, required), owner (text), due_date (date, epoch ms), status (picklist: open "Open", mitigating "Mitigating", closed "Closed"), likelihood (number 1 to 5), impact (number 1 to 5), history_json (text)
- record · seed · ClickUp Command · RAID item: RSK-1183 IMP-2611 risk "SSO cutover rehearsal failed twice", owner Kenji Arai, due 2026-11-03, open, likelihood 4, impact 5; RSK-1184 IMP-2611 risk "User list upload has 214 of 50,000 rows failing", 4, 4, open; RSK-1185 IMP-2611 issue "Docs migration blocked on export limits", 3, 4, open; ASM-0311 IMP-2611 assumption "Sponsor team available for cutover weekend"; DEC-0208 IMP-2611 decision "Cutover rehearsal re-run on 3 Nov"; RSK-1170 IMP-2609 risk 4, 4; RSK-1171 IMP-2602 risk 3, 4; RSK-1172 IMP-2598 risk 5, 5; RSK-1173 IMP-2598 risk 4, 5; RSK-1174 IMP-2607 risk 5, 4; RSK-1175 IMP-2613 risk 3, 3; RSK-1176 IMP-2604 risk 2, 3; RSK-1177 IMP-2618 risk 2, 4; RSK-1178 IMP-2615 risk 1, 2; RSK-1179 IMP-2621 risk 2, 2; RSK-1180 IMP-2624 risk 1, 3; RSK-1181 IMP-2612 risk 2, 2; RSK-1182 IMP-2595 risk 3, 2; RSK-1186 IMP-2619 risk 1, 1; RSK-1187 IMP-2622 risk 2, 3. Every risk is open, with an owner from its project's lead and history_json holding its creation.

#### object · ClickUp Command · Change request
One proposed change to a project, with its rule-routed approval steps.

- object · create · ClickUp Command · Change request: id `OBJ_cucmd_change_request`; fields cr_code (text, primaryKey, required, e.g. `CR-0457`), project_code (text, required), reason (text, required), work_added (text), work_removed (text), hours_delta (number), cost_delta (number), go_live_delta_days (number), before_json (text), after_json (text), route_json (text: the ordered approver steps with role, name, decision, at, reason), next_approver (picklist: delivery_director "Delivery director", finance_partner "Finance partner", none "None"), status (picklist: draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), raised_by (text), raised_at (date, epoch ms), rejection_reason (text)
- record · seed · ClickUp Command · Change request: CR-0455 IMP-2604 "Add Slack integration", +24 h, 4320 eur, 0 days, route delivery director approved, status approved; CR-0456 IMP-2598 "Extra sandbox migration", +64 h, 11520 usd, +7 days, route director approved then finance partner rejected with reason "Budget for this quarter is spent; raise again in January", status rejected. CR-0457 is not seeded: it is raised live in beat 2.

#### object · ClickUp Command · Person
One internal user or customer sponsor, with region, capacity and skill levels.

- object · create · ClickUp Command · Person: id `OBJ_cucmd_person`; fields person_code (text, primaryKey, required), name (text, required), role (picklist: implementation_lead "Implementation lead", consultant "Implementation consultant", delivery_director "Delivery director", finance_partner "Finance partner", resource_manager "Resource manager", customer_sponsor "Customer sponsor"), region (Project region codes), email (text, fictional `@example.com`), capacity_hours (number, default 40), skill_data_migration (number 0 to 4), skill_integrations (number 0 to 4), skill_admin_training (number 0 to 4), skill_api (number 0 to 4), skill_japanese (number 0 to 4), project_code (text; a sponsor's own project), language (picklist: en "English", de "German", ja "Japanese")
- record · seed · ClickUp Command · Person: P-01 Kenji Arai implementation_lead japan; P-02 Mira Lindqvist implementation_lead europe; P-03 Dana Whitfield implementation_lead north_america; P-04 Sam Okafor implementation_lead north_america; P-05 Jonas Weber implementation_lead europe; P-06 Aiko Tanaka implementation_lead japan; P-07 Yui Sato consultant japan (data migration 3, integrations 2, admin training 2, API 1, Japanese 4); P-08 Daichi Ono consultant japan (3, 2, 3, 2, 4); P-09 Lena Brandt consultant europe (2, 3, 4, 1, 0); P-10 Priya Raman consultant north_america (2, 4, 1, 4, 0); P-11 Carla Mendes consultant north_america (4, 2, 2, 2, 0); P-12 Tom Hale resource_manager europe; P-13 Elena Fischer delivery_director europe; P-14 Marcus Bell finance_partner north_america; P-15 Haruto Mori customer_sponsor japan, project IMP-2611, language ja; P-16 Grace Lin customer_sponsor north_america, project IMP-2598, language en. Capacity 40 h each; emails `<first>.<last>@example.com`.

#### object · ClickUp Command · Booking
Hours one person is booked on one project for a run of weeks.

- object · create · ClickUp Command · Booking: id `OBJ_cucmd_booking`; fields booking_code (text, primaryKey, required), person_code (text, required), project_code (text, required), first_week (date, epoch ms, the Monday), weeks (number), hours_per_week (number), over_capacity (boolean)
- record · seed · ClickUp Command · Booking: B-01 P-07 IMP-2611 from 2026-10-26, 4 weeks, 24 h; B-02 P-07 IMP-2618 from 2026-10-26, 8 weeks, 8 h; B-03 P-08 IMP-2612 from 2026-10-26, 6 weeks, 20 h; B-04 P-05 IMP-2609 from 2026-10-26, 5 weeks, 24 h; B-05 P-05 IMP-2602 from 2026-11-16, 4 weeks, 20 h; B-06 P-09 IMP-2615 from 2026-10-26, 4 weeks, 30 h; B-07 P-09 IMP-2619 from 2026-11-23, 10 weeks, 10 h; B-08 P-10 IMP-2598 from 2026-10-26, 12 weeks, 24 h; B-09 P-10 IMP-2621 from 2026-11-02, 8 weeks, 12 h; B-10 P-11 IMP-2607 from 2026-10-26, 8 weeks, 32 h; B-11 P-11 IMP-2613 from 2026-10-26, 5 weeks, 8 h; B-12 P-01 IMP-2611 from 2026-10-26, 6 weeks, 20 h; B-13 P-01 IMP-2618 from 2026-10-26, 6 weeks, 10 h; B-14 P-02 IMP-2604 from 2026-10-26, 8 weeks, 20 h; B-15 P-03 IMP-2595 from 2026-10-26, 2 weeks, 16 h; B-16 P-04 IMP-2624 from 2026-11-09, 12 weeks, 16 h; B-17 P-06 IMP-2626 from 2026-11-02, 12 weeks, 12 h; B-18 P-06 IMP-2622 from 2026-10-26, 10 weeks, 16 h. Jonas Weber is at 110% in the weeks of 16 and 23 Nov 2026.

#### object · ClickUp Command · Time entry
Hours one person logged on one task on one day, inside a weekly timesheet.

- object · create · ClickUp Command · Time entry: id `OBJ_cucmd_time_entry`; fields entry_code (text, primaryKey, required), person_code (text, required), task_code (text, required), project_code (text), work_date (date, epoch ms), hours (number), week_start (date, epoch ms), timesheet_status (picklist: draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason (text)
- record · seed · ClickUp Command · Time entry: E-01 to E-15, week of 2026-10-19: P-07 on T-2611-07 Mon to Fri 6 h, 6 h, 7 h, 6 h, 5 h (submitted); P-07 on T-2611-08 Mon to Fri 2 h each (submitted); P-08 on T-2611-09 Mon to Fri 4 h each (submitted). E-16 to E-20, week of 2026-10-26, each a Monday draft: P-07 on T-2611-07 6 h, P-08 on T-2611-09 4 h, P-10 on T-2611-10 3 h, P-07 on T-2611-08 2 h, P-08 on T-2611-13 3 h.

#### object · ClickUp Command · Deliverable
One stage deliverable awaiting or carrying the sponsor sign-off.

- object · create · ClickUp Command · Deliverable: id `OBJ_cucmd_deliverable`; fields deliverable_code (text, primaryKey, required), project_code (text, required), stage (Project stage codes), title (text), title_ja (text), title_de (text), due_date (date, epoch ms), status (picklist: awaiting_signoff "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), decided_by (text), decided_at (date, epoch ms), comment (text)
- record · seed · ClickUp Command · Deliverable: D-2611-1 Workspace design (discovery, signed_off by Haruto Mori 2026-08-21); D-2611-2 Configuration build (configuration, signed_off 2026-09-18); D-2611-3 Migration wave 1 report (migration, signed_off 2026-10-09); D-2611-4 Training completion (training, signed_off 2026-10-20); D-2611-5 Cutover plan (go_live, awaiting_signoff, due 2026-10-29); each with title, title_ja and title_de.

#### object · ClickUp Command · Session slot
One bookable customer training slot.

- object · create · ClickUp Command · Session slot: id `OBJ_cucmd_session_slot`; fields slot_code (text, primaryKey, required), project_code (text), topic (text), slot_start (date, epoch ms), duration_min (number), taken (boolean), booked_by (text)
- record · seed · ClickUp Command · Session slot: S-01 to S-12 for IMP-2611, topic "Admin training: permissions", 3 days (2026-10-28, 2026-10-29, 2026-10-30) at 10:00, 13:00, 15:00 and 17:00 Asia/Tokyo, 60 min; S-02, S-05 and S-10 taken.

#### object · ClickUp Command · Document
One file in a project library, a published status report or a customer upload with its row errors.

- object · create · ClickUp Command · Document: id `OBJ_cucmd_document`; fields doc_code (text, primaryKey, required), project_code (text, required), kind (picklist: sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", status_report "Status report", upload "Customer upload"), title (text), body (text, the content the in-app viewer shows), shared_with_customer (boolean), row_count (number), error_count (number), errors_json (text: the first errors with row, column and message), upload_status (picklist: checking "Checking", needs_fixing "Needs fixing", confirmed "Confirmed"), ai_written (boolean), edited_by (text), published_at (date, epoch ms)
- record · seed · ClickUp Command · Document: DOC-01 IMP-2611 sow "Statement of work: Sakura Mobility", shared; DOC-02 IMP-2611 migration_plan "Migration plan v3", shared; DOC-03 IMP-2611 signoff_record "Sign-off: Configuration build"; DOC-04 IMP-2611 signoff_record "Sign-off: Migration wave 1"; DOC-05 IMP-2611 upload "sakura-users-wave2.csv", 50000 rows, 214 errors, needs_fixing, errors_json holding the first 20 errors (missing email, duplicate email, unknown department); DOC-06 IMP-2611 status_report "Weekly status 19 Oct", ai_written true, edited by Kenji Arai, published 2026-10-19; DOC-07 IMP-2604 sow; DOC-08 IMP-2598 migration_plan. Each body is the readable text the viewer shows.

#### object · ClickUp Command · Activity
One change on a project: who did what and when; never edited; also the audit log.

- object · create · ClickUp Command · Activity: id `OBJ_cucmd_activity`; fields activity_code (text, primaryKey, required), project_code (text), actor (text), action (picklist: created "Created", updated "Updated", moved "Moved", approved "Approved", rejected "Rejected", signed_off "Signed off", booked "Booked", published "Published", logged "Logged time"), summary (text), at (date, epoch ms); never updated after it is written
- record · seed · ClickUp Command · Activity: twenty rows across IMP-2611, IMP-2604, IMP-2598 and IMP-2609 from 2026-10-12 to 2026-10-26, among them A-20 IMP-2611 Kenji Arai updated "Health changed On track to At risk" 2026-10-26 and A-19 IMP-2611 Haruto Mori signed_off "Training completion" 2026-10-20.

#### object · ClickUp Command · AI output
One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report draft.

- object · create · ClickUp Command · AI output: id `OBJ_cucmd_ai_output`; fields output_code (text, primaryKey, required), project_code (text), kind (picklist: risk_flag "Risk flag", meeting_summary "Meeting summary", proposed_task "Proposed task", status_report "Status report draft"), title (text), body (text), confidence (number 0 to 100), evidence_json (text), transcript_refs_json (text), decision (picklist: proposed "Proposed", accepted "Accepted", rejected "Rejected"), ai_written (boolean, default true), created_at (date, epoch ms)
- record · seed · ClickUp Command · AI output: AI-01 IMP-2611 risk_flag "Likely to miss 16 Nov go-live", confidence 78, evidence "4 of 6 migration tasks late by 5 days on average", "SSO cutover rehearsal failed twice (RSK-1183)", "214 of 50,000 user rows failing (DOC-05)"; AI-02 IMP-2609 risk_flag confidence 64, evidence "Go-live readiness review moved twice"; AI-03 IMP-2602 risk_flag confidence 52, evidence "Configuration 20% behind plan"; AI-04 IMP-2611 meeting_summary "Steering meeting 22 Oct" with decisions ("Cutover rehearsal re-run on 3 Nov"), actions ("Sakura IT to fix 214 user rows by 30 Oct") and risks ("Cutover weekend staffing"), each with transcript_refs_json pointing to lines of the transcript held in body; AI-05, AI-06, AI-07 IMP-2611 proposed_task from AI-04 ("Fix 214 failing user rows", "Book cutover weekend support", "Re-run SSO rehearsal"), decision proposed; AI-08 IMP-2611 status_report draft of 19 Oct. Every row ai_written true.

#### object · ClickUp Command · Weekly metric
The portfolio health counts, the six headline numbers and the value bridge for one week.

- object · create · ClickUp Command · Weekly metric: id `OBJ_cucmd_weekly_metric`; fields week_start (date, epoch ms, primaryKey, required), on_track (number), at_risk (number), off_track (number), active_projects (number), golives_this_month (number), avg_days_to_golive (number), utilisation_pct (number), value_awaiting_usd (number), bridge_new (number), bridge_golives (number), bridge_slipped (number), bridge_cancelled (number), top_movers_json (text), last_updated (date, epoch ms)
- record · seed · ClickUp Command · Weekly metric: twelve weeks from 2026-08-10 to 2026-10-26; on-track share 81, 80, 80, 79, 78, 78, 77, 77, 76, 76, 75, 75 percent; week 2026-10-19 on_track 159, at_risk 33, off_track 19, active 211; week 2026-10-26 on_track 161, at_risk 38, off_track 15, active 214, golives_this_month 9 (last week 10), avg_days_to_golive 61 (last week 63), utilisation_pct 87 (last week 83), value_awaiting_usd 18400000 (last month 17800000), bridge_new 2100000, bridge_golives -1300000, bridge_slipped 200000, bridge_cancelled -400000, top_movers_json naming IMP-2611 (On track to At risk: cutover rehearsal failed), IMP-2602 (go-live slipped 2 weeks), IMP-2613 (On track to At risk: training attendance 48%), IMP-2598 (At risk to Off track: sandbox change request rejected), IMP-2607 (go-live slipped 4 weeks), last_updated 2026-10-26 06:00 UTC.

#### object · ClickUp Command · Saved view
One named, shareable set of portfolio filters.

- object · create · ClickUp Command · Saved view: id `OBJ_cucmd_saved_view`; fields view_code (text, primaryKey, required), name (text, required), filters_json (text), owner (text), shared_with (text)
- record · seed · ClickUp Command · Saved view: V-01 "My Japan projects" (region japan) owner Kenji Arai; V-02 "Europe go-lives this quarter" owner Elena Fischer, shared with "Europe delivery".

#### object · ClickUp Command · Checklist item
One of the ten readiness questions with the customer answer, or none.

- object · create · ClickUp Command · Checklist item: id `OBJ_cucmd_checklist_item`; fields item_code (text, primaryKey, required), project_code (text, required), position (number), question_en (text), question_de (text), question_ja (text), answer (text; empty means not set), answered_by (text), answered_at (date, epoch ms)
- record · seed · ClickUp Command · Checklist item: C-2611-01 to C-2611-10, questions in en, de and ja (SSO provider, admin users, departments, data residency, time zone, working week, support contacts, go-live freeze window, training rooms, success metrics); items 01 to 07 answered by Haruto Mori, 08, 09 and 10 with no answer.

#### object · ClickUp Command · Integration
The sync status of one connected system.

- object · create · ClickUp Command · Integration: id `OBJ_cucmd_integration`; fields system (picklist: salesforce "Salesforce", slack "Slack", google_drive "Google Drive", jira "Jira"; primaryKey, required), status (picklist: synced "Synced", sync_failed "Sync failed"), last_sync (date, epoch ms), failing_since (date, epoch ms), error (text), affects (text)
- record · seed · ClickUp Command · Integration: salesforce synced 2026-10-26 07:55; slack synced 2026-10-26 07:58; google_drive synced 2026-10-26 07:40; jira sync_failed, failing since 2026-10-25 22:10, error "Authentication expired for the Jira project ESC", affects "Engineering escalations on 3 projects are not updating".

#### object · ClickUp Command · Notification
One assignment, sign-off or mention for a user.

- object · create · ClickUp Command · Notification: id `OBJ_cucmd_notification`; fields notification_code (text, primaryKey, required), person_code (text, required), kind (picklist: assignment "New assignment", signoff "Sign-off", mention "Mention"), text (text), link (text), read (boolean), created_at (date, epoch ms)
- record · seed · ClickUp Command · Notification: N-01 to N-08 for P-07 Yui Sato: 3 assignment, 2 signoff, 3 mention, N-01 to N-03 unread.

#### automation · ClickUp Command · Save view
Saves a named portfolio filter set and shares it.

- automation · create · ClickUp Command · Save view: callable; inputs name (text), filters_json (text), owner (text), shared_with (text); outputs view_code (text), result (text: saved | refused_name_taken); writes Saved view.

#### automation · ClickUp Command · Update task
Moves a task between stage columns, reschedules it with dependents, or sets its status.

- automation · create · ClickUp Command · Update task: callable; inputs task_code (text), action (text: move | reschedule | status), to_stage (text), new_start (number, epoch ms), new_end (number, epoch ms), status (text), preview (boolean); outputs result (text: saved | preview | refused), column_count (number), column_limit (number), over_limit (boolean), moved_json (text: each dependent task with its new dates), new_go_live (number, epoch ms); a reschedule moves every finish-to-start dependent by the same working days and returns the project's new go-live date; preview true writes nothing; a save writes Task and one Activity row.

#### automation · ClickUp Command · Raise change request
Previews and submits a change request with its before and after plan and its route.

- automation · create · ClickUp Command · Raise change request: callable; inputs project_code, reason, work_added, work_removed (text), hours_delta, cost_delta, go_live_delta_days (number), raised_by (text), preview (boolean); outputs cr_code (text), before_json, after_json, route_json (text), result (text: preview | submitted | refused_reason_required); route: an absolute hours_delta under 40 goes to the Delivery director only; 40 or more goes to the Delivery director, then the Finance partner, in that order; the next cr_code continues from the highest stored one (CR-0457 first); submit writes Change request with status pending_approval and one Activity row.

#### automation · ClickUp Command · Decide change request
Records one approver decision and applies the 40-hour route and the reason rule.

- automation · create · ClickUp Command · Decide change request: callable; inputs cr_code, approver_role (text: delivery_director | finance_partner), approver_name, decision (text: approve | reject), reason (text); outputs result (text: step_approved | approved | rejected | refused_reason_required | refused_not_your_turn), next_approver (text), new_go_live (number, epoch ms); a reject with an empty reason writes nothing and answers refused_reason_required; an approver who is not next answers refused_not_your_turn; the last approval sets status approved, moves the Project go_live_date by go_live_delta_days, adds hours_delta to budget_hours_planned, and writes one Activity row; every decision appends to route_json.

#### automation · ClickUp Command · Book consultant
Books a person onto a project and refuses to save over capacity without confirmation.

- automation · create · ClickUp Command · Book consultant: callable; inputs person_code, project_code (text), first_week (number, epoch ms), weeks, hours_per_week (number), confirm (boolean); outputs result (text: saved | over_capacity), overages_json (text: each week with booked hours, percent of capacity and hours over), booking_code (text); a booking that takes the person above 100% of capacity_hours in any week answers over_capacity with the weeks and writes nothing unless confirm is true, when it saves with over_capacity true; a save writes Booking and one Activity row.

#### automation · ClickUp Command · Timesheet action
Logs time, submits, approves or returns weekly timesheets.

- automation · create · ClickUp Command · Timesheet action: callable; inputs action (text: log | submit | approve | return), person_code, task_code (text), work_date (number), hours (number), week_start (number), entry_codes (text, comma-separated, for approve and return in a batch), reason (text); outputs result (text: saved | refused_reason_required), timesheet_status (text); a return with an empty reason is refused.

#### automation · ClickUp Command · Portal action
The sponsor sign-off, change request, session booking, checklist answer and upload confirm.

- automation · create · ClickUp Command · Portal action: callable; inputs action (text: sign_off | request_changes | book_slot | answer_checklist | confirm_upload), sponsor_code, deliverable_code, slot_code, item_code, answer, doc_code, comment (text); outputs result (text: saved | refused_comment_required | refused_slot_taken | refused_not_your_project), decided_by (text), decided_at (number, epoch ms); a sponsor acts only on their own project_code; request_changes needs a comment; a taken slot is refused; sign_off records who and when and writes Activity.

#### automation · ClickUp Command · Accept proposed tasks
Turns accepted Copilot proposals into tasks.

- automation · create · ClickUp Command · Accept proposed tasks: callable; inputs output_codes (text, comma-separated), decision (text: accept | reject), decided_by (text); outputs created_task_codes (text), result (text); accept creates one Task per output with source copilot and sets the output's decision; reject creates nothing.

#### automation · ClickUp Command · Publish status report
Publishes the lead-edited, AI-written weekly status report.

- automation · create · ClickUp Command · Publish status report: callable; inputs project_code, body, edited_by (text); outputs doc_code (text), published_at (number), result (text); writes Document kind status_report with ai_written true and edited_by, and one Activity row.

#### automation · ClickUp Command · Send executive summary
Sends the weekly summary email through Gmail, labelled DEMO-TEST.

- automation · create · ClickUp Command · Send executive summary: callable; inputs to_email (text), week_start (number); outputs result (text: sent | failed), message_id (text); reads Weekly metric for the week, composes the six headline numbers, the value bridge and the five top movers as HTML with the ClickUp logo, and sends one email through the Gmail connection `6980e13788c7735877a8311c` with operation `gmail_send_email`, subject starting "DEMO-TEST · ClickUp Delivery Command · weekly summary".

#### automation · ClickUp Command · Update project settings
Saves inline edits to project name, region, go-live date and budget hours.

- automation · create · ClickUp Command · Update project settings: callable; inputs project_code, name (text), region (text), go_live_date (number), budget_hours_planned (number); outputs result (text: saved | failed), field_errors_json (text); a go-live date in the past or budget hours below hours used fail with a field error.

#### automation · ClickUp Command · Mark notification read
Marks one notification read.

- automation · create · ClickUp Command · Mark notification read: callable; inputs notification_code (text); outputs result (text); sets read true.

#### automation · ClickUp Command · Read delivery data
The Copilot read-only tool over the delivery objects.

- automation · create · ClickUp Command · Read delivery data: callable, read-only, the Copilot's one tool; inputs scope (text: projects | tasks | risks | bookings | people | change_requests | ai_outputs | weekly_metrics | documents), filters_json (text: field equals value pairs, and date ranges as from and to epoch ms); outputs rows_json (text), row_count (number), as_of (number, epoch ms); writes nothing.

#### automation · ClickUp Command · Ask Copilot
Lets the app ask ClickUp Command Copilot a question and returns its answer.

- automation · create · ClickUp Command · Ask Copilot: callable; inputs question (text), session_id (text), user_email (text); outputs answer_text (text), chart_json (text: the chart's type, title, unit and series when the answer is a chart), record_links_json (text), session_id (text); invokes the AI agent ClickUp Command Copilot through `ai_agents_by_unifyapps_invoke_agent` with aiAgentId, userQuery, sessionId and userEmailAddress, and returns the agent's text.

#### connection · Gmail
Existing Gmail connection the weekly summary email is sent through; probed read-only at plan time.


#### ai-agent · ClickUp Command Copilot
Delivery Copilot: read-only AI agent over the delivery data.

- ai-agent · create · ClickUp Command Copilot: model as Nebula recommends; read-only; one tool, ClickUp Command · Read delivery data; instructions: answer questions about ClickUp Delivery Command projects, risks, bookings, change requests and weekly metrics only from that tool's rows, name each record by its code (IMP-, CR-, RSK-), use dates as 16 Nov 2026 and money in the contract currency; when asked for a chart, return a JSON block with type, title, unit and series; when asked for a weekly status report, draft it from the project's tasks, risks and time entries with sections Summary, Progress, Risks, Next week; portfolio health counts come from the latest weekly metric; risk predictions come from AI output rows of kind risk_flag with their confidence and evidence; it never changes data, and says changes go through the app (a change request, a booking); billing, invoicing, revenue, payroll and anything not in the rows is declined with what to try instead; plain, calm, direct words, no exclamation marks.

#### code-app · ClickUp Delivery Command
The code app: internal workspace, customer portal and phone view.

- code-app · create · ClickUp Delivery Command: the shell: the design system stylesheet, the fonts, the rail (Portfolio, Projects, Resourcing, Timesheets, Changes, Admin; the ClickUp logo), the top bar (current project or view, search, notifications, profile menu with the persona switcher and Appearance), the right-hand Copilot panel slot, the routes for Executive summary, Portfolio, Project workspace, Change request, Changes, Resourcing, Timesheets, Admin, Portal (Home, Sign-offs, Sessions, Files, Checklist) and Phone (Today, Tasks, Time, Alerts); PRIVATE
- code-app · update · ClickUp Delivery Command: screen Executive summary and Portfolio: six `.tile` headline numbers with `.delta` coloured by good or bad for the business, the value bridge `.chart`, the five top movers `.tbl`, the Email me this summary `.btn-s` and its preview; Portfolio health `.tile` counts with change since last week, the risk grid (likelihood against impact, a cell lists its risks), the 90-day go-live timeline grouped by region with slipped dates marked, the 12-week on-track `.chart`, the projects `.tbl` with `.toolbar` search "x of y", facets region, stage, health and lead, removable chips with Clear all, `.pg`, and Save view · reads Project, RAID item, Weekly metric, Saved view · calls ClickUp Command · Save view and ClickUp Command · Send executive summary
- code-app · update · ClickUp Delivery Command: screen Project workspace and Change request: the overview (stage, the seven `.stages`, days to go-live, budget `.prog`, open risks, next sign-off), `.tabs` List, Board (`.kb` one column per stage with the over-limit warning, drag and a Move to `.menu`), Timeline (dependencies, critical path, date change preview), RAID, Documents (in-app viewer), Activity (`.feed`), Settings (inline edit with unsaved, saving, saved, failed), the task detail drawer; the change request form with before and after side by side and the differences marked · reads Project, Task, RAID item, Document, Activity · calls ClickUp Command · Update task, ClickUp Command · Raise change request, ClickUp Command · Update project settings
- code-app · update · ClickUp Delivery Command: screen Changes: the change requests `.tbl` and the request detail with the approval route as `.stv`, who approved and who is next, Approve as `.btn-p`, Reject with a required reason, the refusal as `.tag.negative` and `.note` · reads Change request, Activity · calls ClickUp Command · Decide change request
- code-app · update · ClickUp Delivery Command: screen Resourcing and Timesheets: people against 12 weeks with weekly percent, over 100% flagged, the region tag; the Book consultant form (person, project, weeks, hours; no drag) showing who, which weeks and by how much before saving; the skills matrix; region capacity over the quarter; Timesheets with batch Approve and Return with reason · reads Person, Booking, Project, Time entry · calls ClickUp Command · Book consultant, ClickUp Command · Timesheet action
- code-app · update · ClickUp Delivery Command: screen Copilot panel: opens on every internal screen from the top bar; three suggested questions from the user's projects; `.convo` with `.msg.me` and `.msg.ai`; `.stages` while it works; answers with record links and a `.chart` in the app's colours with units; the AI-written label; the risk flags as `.ai:not(.msg)` cards with confidence and evidence; Draft status report into an editor, Publish, export PDF and Word; the meeting summary with transcript links and proposed tasks to Accept or Reject · reads AI output, Document · calls ClickUp Command · Ask Copilot, ClickUp Command · Publish status report, ClickUp Command · Accept proposed tasks
- code-app · update · ClickUp Delivery Command: screen Portal: the shorter top menu Home, Sign-offs, Sessions, Files, Checklist; English, German and Japanese; the sponsor sees only their own project and never internal health; Sign off or Request changes with a comment; book a session by day then slot, taken slots visible and disabled; upload a CSV with row errors summarised and fixable before Confirm; the ten-item checklist with Not set for unanswered items; the no-access screen naming who can grant access · reads Project, Deliverable, Session slot, Document, Checklist item · calls ClickUp Command · Portal action
- code-app · update · ClickUp Delivery Command: screen Phone and Admin: the phone layout with bottom tabs Today, Tasks, Time, Alerts (status update, log time, mark read or open); Admin with the roles against permissions grid, the audit log filtered by person, project and action, the integrations status with last sync and the Jira Sync failed row · reads Task, Time entry, Notification, Activity, Integration · calls ClickUp Command · Update task, ClickUp Command · Timesheet action, ClickUp Command · Mark notification read

### Business rules
- A change request under 40 hours needs the Delivery director's approval; 40 hours or more needs the Delivery director, then the Finance partner, in that order.
- Rejecting a change request, returning a timesheet, or requesting changes on a deliverable needs a written reason.
- An approved change request moves the project's go-live date and planned hours and is recorded in the activity feed.
- A booking that takes a consultant above 100% of capacity in any week shows who, which weeks and by how much before it is saved.
- A customer sponsor sees only their own project and never internal health.
- An unanswered checklist item shows as Not set, never as a guessed value.
- Everything Delivery Copilot writes is labelled AI-written; nothing it proposes is created without acceptance.
- Activity rows are never edited.
- Every test record and every sent email is labelled DEMO-TEST with the demo date.

### Rules
- The code app's one global stylesheet is `/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/client.css`, byte for byte, imported from `App.tsx`.
- The rail logo is `/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/logo.svg` (the ClickUp wordmark from clickup.com's header) on a light plate; the collapsed rail and the browser tab icon use `/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/logo-symbol.svg`; used as published, never traced, redrawn or recoloured.
- Theme light by default, the dark tokens left live; Appearance in the profile menu switches it.
- Components come from the class inventory (`.g1 .g2 .g3 .pad .inner .solid`, `.btn .btn-p .btn-s .btn-t`, `.tag`, `.toolbar .field .chipsel .tblwrap .tbl .pg`, `.ai:not(.msg)`, `.tile .loop .empty`, `.tabs`, `.fld .ctl .hint .seg .tog .opt`, `.sth .stv .prog .stages`, `.canvas .convo .msg`, `.pc .faces .av`, `.feed`, `.chart .spark .delta .legend`, `.toast .menu .crumb .note`), never a second implementation, never a new colour value, never a Tailwind colour, radius, shadow or type utility: Tailwind only for layout the kit has no class for.
- Every status shows an icon and a word (On track, At risk, Off track, Signed off, Awaiting sign-off, Over capacity, Pending approval, Approved, Rejected, Blocked, Sync failed, Not started, Draft, Scheduled, Hypercare, Live).
- Test records and sent emails are labelled `DEMO-TEST` with the demo date.

### Ready when
- The presenter walks the six beats on the published app as the beats say, and Sakura Mobility (IMP-2611) shows At risk with go-live 16 Nov 2026 on the Portfolio.
- deploy ClickUp Command · Save view
- deploy ClickUp Command · Update task
- deploy ClickUp Command · Raise change request
- deploy ClickUp Command · Decide change request
- deploy ClickUp Command · Book consultant
- deploy ClickUp Command · Timesheet action
- deploy ClickUp Command · Portal action
- deploy ClickUp Command · Accept proposed tasks
- deploy ClickUp Command · Publish status report
- deploy ClickUp Command · Send executive summary
- deploy ClickUp Command · Update project settings
- deploy ClickUp Command · Mark notification read
- deploy ClickUp Command · Read delivery data
- deploy ClickUp Command · Ask Copilot
- publish ClickUp Command Copilot
- publish ClickUp Delivery Command

### Assumptions
- Check this: intent proposed as `both` (the outcome, then how): one hood beat after the lean-forward beat; the owner sets it at G2.
- Check this: scope is one app covering every ask, led by the portfolio dashboard, the executive summary and Delivery Copilot (G1 question 1, recommended option).
- Check this: 18 fictional projects around the BRD's six sample customers; the headline counts read like the BRD's portfolio from the Weekly metric rows (G1 question 8).
- Check this: the phone view is a responsive layout of the same code app shown in a phone frame (G1 question 9).
- Check this: integrations show seeded status with one Sync failed row; the one live external step is the weekly summary email through the existing Gmail connection (G1 questions 10 and 11).
- Check this: customers never see internal health (G1 question 5); the timeline is not editable from the phone (G1 question 4); region shows as a labelled tag, never colour alone (G1 question 6).
- Check this: brand colour `#5F55EE` (hue 244) from clickup.com's `--ProductScreen-CustomStatus-Primary`; the sample was ambiguous and the profile takes the recommended one.
- Check this: typeface Inter, the body face of clickup.com, with tabular figures, Noto Sans JP for Japanese, IBM Plex Mono kept for eyebrows (open question 13).
- Check this: the app's sign-in, forgot and reset password are the tenant's own pages a PRIVATE code app opens with (open question 14).
- Check this: roles are a persona switcher in the profile menu with a seeded roles grid; no tenant roles are made (open question 15).
- Check this: documents open in an in-app viewer of the text the record holds; no file is uploaded.
- Check this: customer logos on project cards and in the portal are circles holding the customer's initials, since the customers are invented.
- Check this: German and Japanese portal text is drafted by Studio for the client to review.
- Check this: the Copilot's working stages are shown by the app while the call runs (Reading projects, Checking risks, Writing answer).
- Light is the default theme with the dark tokens live; Appearance in the profile menu switches it.
- The AI agent's model is Nebula's recommendation (profile standing answer).
- Release: publish and deploy on the tenant without asking; visibility PRIVATE (profile).

## entities

| Kind | Name | Id | Link | Serves |
|---|---|---|---|---|
| object | ClickUp Command · Project | `OBJ_cucmd_project` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_project/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Task | `OBJ_cucmd_task` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_task/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · RAID item | `OBJ_cucmd_raid` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_raid/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Change request | `OBJ_cucmd_change_request` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_change_request/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Person | `OBJ_cucmd_person` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_person/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Booking | `OBJ_cucmd_booking` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_booking/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Time entry | `OBJ_cucmd_time_entry` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_time_entry/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Deliverable | `OBJ_cucmd_deliverable` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_deliverable/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Session slot | `OBJ_cucmd_session_slot` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_session_slot/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Document | `OBJ_cucmd_document` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_document/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Activity | `OBJ_cucmd_activity` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_activity/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · AI output | `OBJ_cucmd_ai_output` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_ai_output/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Weekly metric | `OBJ_cucmd_weekly_metric` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_weekly_metric/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Saved view | `OBJ_cucmd_saved_view` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_saved_view/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Checklist item | `OBJ_cucmd_checklist_item` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_checklist_item/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Integration | `OBJ_cucmd_integration` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_integration/schema | the beats that read or write it (data for beats 1-6) |
| object | ClickUp Command · Notification | `OBJ_cucmd_notification` | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_notification/schema | the beats that read or write it (data for beats 1-6) |
| automation | ClickUp Command · Read delivery data | `6adf45fef3cd5f19ed4a76ba` | https://orbit.uat.unifyapps.com/p/0/automations/6adf45fef3cd5f19ed4a76ba/builder | beat 6: A1 A2 A5 A35 A36 A37 A38 A41 A78 A79 A96 |
| automation | ClickUp Command · Save view | `6adf460108750d257cf1e381` | https://orbit.uat.unifyapps.com/p/0/automations/6adf460108750d257cf1e381/builder | beat 1: A6 A7 A8 A11 A13 A14 A15 A16 A17 A18 A48 A49 A50 A59 A62 A65 A70–A73 A90 A97 |
| automation | ClickUp Command · Update task | `6adf485af3cd5f19ed4ac683` | https://orbit.uat.unifyapps.com/p/0/automations/6adf485af3cd5f19ed4ac683/builder | beat 2: A19 A20 A21 A22 A24 A25 A31 A32 A74 A75 |
| automation | ClickUp Command · Raise change request | `6adf485ec79cad1140a9e9a6` | https://orbit.uat.unifyapps.com/p/0/automations/6adf485ec79cad1140a9e9a6/builder | beat 2: A19 A20 A21 A22 A24 A25 A31 A32 A74 A75 |
| automation | ClickUp Command · Decide change request | `6adf485ff3cd5f19ed4ac6fd` | https://orbit.uat.unifyapps.com/p/0/automations/6adf485ff3cd5f19ed4ac6fd/builder | beat 3: A10 A33 A34 |
| automation | ClickUp Command · Book consultant | `6adf4aa308750d257cf32534` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4aa308750d257cf32534/builder | beat 4: A3 A26 A27 A28 A64 A81 A88 |
| automation | ClickUp Command · Timesheet action | `6adf4aa9f3cd5f19ed4afa85` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4aa9f3cd5f19ed4afa85/builder | beat 4: A3 A26 A27 A28 A64 A81 A88 |
| automation | ClickUp Command · Portal action | `6adf4aaef3cd5f19ed4afc58` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4aaef3cd5f19ed4afc58/builder | beat 5: A4 A42 A43 A44 A45 A46 A47 A60 A68 A82 A83 A87 A98 |
| automation | ClickUp Command · Accept proposed tasks | `6adf4d11f3cd5f19ed4b436a` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4d11f3cd5f19ed4b436a/builder | beat 6: A1 A2 A5 A35 A36 A37 A38 A41 A78 A79 A96 |
| automation | ClickUp Command · Publish status report | `6adf4d1492718f6a64e5ca35` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4d1492718f6a64e5ca35/builder | beat 6: A1 A2 A5 A35 A36 A37 A38 A41 A78 A79 A96 |
| automation | ClickUp Command · Send executive summary | `6adf4d1508750d257cf3df21` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4d1508750d257cf3df21/builder | beat 1: A6 A7 A8 A11 A13 A14 A15 A16 A17 A18 A48 A49 A50 A59 A62 A65 A70–A73 A90 A97 |
| automation | ClickUp Command · Update project settings | `6adf4eb5cac0655fe38aef9d` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4eb5cac0655fe38aef9d/builder | beat 2: A19 A20 A21 A22 A24 A25 A31 A32 A74 A75 |
| automation | ClickUp Command · Mark notification read | `6adf4eb8cac0655fe38aefc9` | https://orbit.uat.unifyapps.com/p/0/automations/6adf4eb8cac0655fe38aefc9/builder | control (phone Alerts) |
| automation | ClickUp Command · Ask Copilot | `6adf526ef3cd5f19ed626787` | https://orbit.uat.unifyapps.com/p/0/automations/6adf526ef3cd5f19ed626787/builder | beat 6: A1 A2 A5 A35 A36 A37 A38 A41 A78 A79 A96 |
| ai-agent | ClickUp Command Copilot | `e_6adf4f02dc07493166ced9fa` | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6adf4f02dc07493166ced9fa | beat 6: A1 A2 A5 A35 A36 A37 A38 A41 A78 A79 A96 |
| code-app | ClickUp Delivery Command | `app-a2a9509a82c1` | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-a2a9509a82c1 | every beat 1-6 and its controls |

- code app ClickUp Delivery Command `app-a2a9509a82c1` · PRIVATE · branch main · last commit 9142bfc0190ee94e05f42c6766567888288ca8f7 (published v2, empty states name their items; v1 was f38dc296) · preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-a2a9509a82c1/main/ · published https://app-a2a9509a82c1-orbit.tensor-uat.unifyapps.com/ (answers 302 to the tenant sign-in) · builder https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-a2a9509a82c1
- commits: shell 34c4f6de, summary and portfolio 764c6e05, project workspace 7d5c3ae4, changes 31af0c68, resourcing and timesheets aa5b6a2e, Copilot panel 73c5a1e5, portal ea1d786a, phone and admin f38dc296
- AI agent ClickUp Command Copilot `e_6adf4f02dc07493166ced9fa` · published version 11 (verify round 1 fix: week anchor, week-on-week health, codes as words) · model Claude Sonnet 5 (UnifyApps, Vertex) `e_6ad496812dd4ba5be70afcc1` · one tool ReadDeliveryData `e_6adf4f0b08f965795442fe85` (Read delivery data)
- DEMO-TEST records to clean up: Saved view V-03 'DEMO-TEST 2026-10-26 view' (OBJ_cucmd_saved_view); Time entry E-6adf4ba097a3bf334d3f24b5 and Activity A-6adf4ba097a3bf334d3f24b5 (Timesheet action log test, IMP-2611); Activity A-6adf4dc0ca4f9d20457f2ff7-AI-05 (Accept proposed tasks reject test, actor DEMO-TEST 2026-10-26); Document DOC-SR-6adf4dc2c79cad1140aa6b4a and Activity A-6adf4dc2c79cad1140aa6b4a on IMP-2604 (Publish status report test); One DEMO-TEST email to gourav.mahunta@unifyapps.com, Gmail message id 1a17847cf729b474 (Send executive summary test)

## beats

**Storyline: "Make all three visible and actionable": earlier warning, less reporting, balanced staffing** (proposed intent `both`; six story beats and one hood beat; presenter in the seat of Kenji Arai, implementation lead, switching persona from the profile menu)

Story row: Sakura Mobility · IMP-2611 · Automotive · Japan · stage Go-live (6 of 7) · go-live 16 Nov 2026 (21 days out) · health At risk (On track last week) · lead Kenji Arai · sponsor Haruto Mori (portal, Japanese) · 9,200 seats · JPY 62,400,000 · 1,236 of 1,480 budget hours used · open risks 3, top RSK-1183 "SSO cutover rehearsal failed twice" (likelihood 4, impact 5) · next sign-off "Cutover plan" due 29 Oct 2026 · Copilot risk flag 78% · change request CR-0457 raised live: second user-list migration wave for two subsidiaries, +56 h, JPY 1,120,000, go-live +5 days to 21 Nov 2026 · consultants Yui Sato (would reach 120% in the weeks of 9 and 16 Nov) and Daichi Ono (90% after booking).

1. **Monday: the summary, then the portfolio** · route `/summary` then `/portfolio` · mode `live` (reads), the headline counts `seeded` (Weekly metric) · The presenter, as Elena Fischer (Delivery director), opens the executive summary: six headline numbers with changes coloured good or bad (projects at risk 38, +5, red), the value bridge USD 17.8M to 18.4M, the five top movers led by Sakura Mobility. They press Email me this summary (external step: one real `DEMO-TEST` email through the tenant's Gmail connection; fallback: the in-app preview). They open Portfolio: health counts 161 / 38 / 15 with week-on-week change, the risk grid with RSK-1183 in the likelihood 4 × impact 5 cell, the 90-day go-live timeline by region with slipped dates marked, the 12-week on-track line 81% to 75%. Filter Region Japan and Health At risk: chips, "1 of 18", Sakura Mobility; Save view "Japan at risk" shared with the Japan team. · asks A6 A7 A8 A11 A13 A14 A15 A16 A17 A18 A48 A49 A50 A59 A62 A65 A70–A73 A90 A97
2. **Sakura Mobility's workspace and the change it needs** · route `/projects/IMP-2611`, `/projects/IMP-2611/change` · mode `live` · As Kenji Arai: the overview (Go-live on the seven-stage path, 21 days to go-live, 1,236 of 1,480 hours, 3 open risks, Cutover plan sign-off due 29 Oct); the Board, one column per stage, a task moved by drag and by Move to; the Timeline with the critical path, moving SSO cutover rehearsal 2 by two days previews the dependents and a new go-live of 18 Nov before saving (cancelled); RAID with RSK-1183 and its history; Activity; a task opened in the side drawer. They raise CR-0457 (reason, work added, +56 h, JPY 1,120,000, +5 days) and see the plan before and after side by side with the differences marked, then submit: route Delivery director, then Finance partner. · asks A19 A20 A21 A22 A24 A25 A31 A32 A74 A75
3. **The rule routes the approval, and refuses a bare rejection (failure beat)** · route `/changes/CR-0457` · mode `live` (the 40-hour rule and the reason rule are `deterministic` logic inside the live automation) · As Elena Fischer: Approve; the request shows "Approved by Elena Fischer · Next: Finance partner" because 56 h is 40 or more. As Marcus Bell (Finance partner): Reject with an empty reason; the automation refuses: "A rejection needs a written reason. Add why, then reject." (`.tag.negative` + `.note`). Marcus approves instead: status Approved, Sakura Mobility's go-live moves to 21 Nov 2026, planned hours 1,536, one Activity row. · asks A10 A33 A34
4. **Staffing the change without burning anyone out** · route `/resourcing` · mode `live` (capacity check `deterministic` inside the automation) · As Tom Hale (Resource manager): the 12-week grid shows Jonas Weber over 100% in two weeks. Book consultant: Yui Sato on IMP-2611, weeks of 9 and 16 Nov, 16 h: before saving, "Yui Sato would be at 120% in the weeks of 9 and 16 Nov (8 h over each)". The skills matrix finds Daichi Ono (data migration 3, Japanese 4) at 50%; booked, 90%, saved. · asks A3 A26 A27 A28 A64 A81 A88
5. **The sponsor's view, in Japanese** · route `/portal/home`, `/portal/signoffs`, `/portal/sessions`, `/portal/files`, `/portal/checklist` · mode `live` · As Haruto Mori, language 日本語: only Sakura Mobility, its stage and milestones, no internal health; sign off "Cutover plan" (recorded with name and time); book an admin training slot on 29 Oct (taken slots visible, greyed); the upload "sakura-users-wave2.csv" shows "214 of 50,000 rows need fixing" with the errors summarised and fixable before Confirm; the checklist shows three items Not set. · asks A4 A42 A43 A44 A45 A46 A47 A60 A68 A82 A83 A87 A98
6. **Lean-forward: Delivery Copilot over live data** · route the Copilot panel on `/portfolio` · mode `live` (agent call); risk flags and the meeting summary `seeded` · As Kenji Arai: the panel opens with three suggested questions; they type "Which Japan projects go live in November and are at risk?"; stages tick (Reading projects, Checking risks, Writing answer); the answer names Sakura Mobility, 16 Nov, At risk, with record links and the AI-written label, then "show go-lives by month as a chart" draws a chart in the app's colours with units. The risk flag card shows 78% with its evidence. "Draft this week's status report for Sakura Mobility": the agent drafts it in under a minute, Kenji edits a line, publishes, exports PDF; the CR-0457 approval and new date are already in it. Asked for the October invoice total, the Copilot declines and says what to try instead. · asks A1 A2 A5 A35 A36 A37 A38 A41 A78 A79 A96
   Alternatives considered: B / C
   - B: the meeting summary turned into proposed tasks the lead accepts (A39, A40): strong, but its summary is seeded, so the room sees no live AI.
   - C: the portfolio risk prediction as the reveal (A41): visual, but it is a seeded score, and the profile names "an AI assistant over live data".
   - Chosen: a live question over the data the room just changed, plus the 10-minute status report, because it lands both headline goals (A1 earlier warning, A2 less reporting) on live data.
H1. **Under the hood (after beat 6)** · mode `live` · Open ClickUp Command · Decide change request on the automation canvas: the 40-hour branch and the reason check that refused Marcus; then ClickUp Command Copilot in the agent builder with its one read-only tool, ClickUp Command · Read delivery data.

AI surfaces and their modes:
| Surface | Mode |
|---|---|
| ClickUp Command Copilot answers and charts (beat 6) | live |
| Status report draft (beat 6) | live (the agent drafts; the lead edits; Publish is a live automation) |
| Copilot working stages | deterministic (the app shows them while the call runs) |
| Risk flags with confidence and evidence (beats 1, 6) | seeded (AI output rows, AI-written label) |
| Meeting summary and proposed tasks (control in the Copilot panel) | seeded; Accept is a live automation |
| Executive summary top movers' reasons (beat 1) | seeded |
| Weekly summary email (beat 1) | live (external step, Gmail) |
| Integrations status (Admin) | mocked (seeded rows for Salesforce, Slack, Google Drive, Jira) |
| Roles grid (Admin) | mocked (seeded in the app) |

## views

- Executive summary `/summary` · beat 1 · `.tile` ×6 with `.delta` · `.chart` (value bridge) · `.tbl` top movers · `.btn-s` Email me this summary + `.toast` · `.note` last updated
- Portfolio `/portfolio` · beats 1, 6 · `.tile` ×3 health with `.delta` · risk grid as a `.tbl` of likelihood × impact cells with `.tag` counts, a cell opening its risks · go-live timeline as `.cal` grouped by region with `.tag.attention` Slipped · `.chart` + `.spark` 12-week on-track · `.toolbar` `.field` `.chipsel` facets + chips, `.tblwrap` `.tbl`, `.pg`, `.empty` · `.av` customer initials circles · Copilot panel `.canvas`
- Project workspace `/projects/:code` · beat 2 · `.crumb` · overview `.stages` + `.prog` + `.tile` · `.tabs`: List `.tbl`, Board `.kb` with `.menu` Move to, Timeline (bars on `.cal`, critical path `.tag.negative`), RAID `.tbl` + `.feed` history, Documents `.tbl` + viewer `.g3 .pad`, Activity `.feed`, Settings `.fld .ctl` inline · task drawer `.g3` side pane
- Change request `/projects/:code/change` · beat 2 · `.fld .ctl .hint` form · before and after `.tbl` ×2 with `.tag.attention` marked differences · `.stv` route preview · `.btn-p` Submit
- Changes `/changes`, `/changes/:code` · beat 3 · `.tbl` requests · `.stv` approval route with `.pc` approvers · `.btn-p` Approve, `.btn-s` Reject with `.fld` reason · `.tag.negative` + `.note` refusal · `.toast`
- Resourcing `/resourcing` · beat 4 · people × 12 weeks `.tbl` with `.tag` percent cells, over 100% `.tag.negative` · `.pc` `.av` region tag · Book consultant `.fld .ctl .seg` form + `.note` overage · `.tabs` Skills `.tbl`, Region capacity `.chart`
- Timesheets `/timesheets` · control · `.tbl` with select boxes `.box`, `.btn-p` Approve selected, Return with `.fld` reason
- Copilot panel (every internal screen) · beat 6 · `.canvas` `.convo` `.msg.me` `.msg.ai` `.chips` suggestions · `.stages` working · `.ai:not(.msg)` risk flag cards · `.chart` answer · editor `.g3 .pad` + `.btn-p` Publish, `.btn-s` PDF, Word · `.tabs` Meeting summary with `.btn-s` Accept, Reject
- Portal `/portal/*` · beat 5 · top menu `.tabs` · `.stages` milestones · `.tbl` sign-offs + `.btn-p` Sign off, `.btn-s` Request changes · `.cal` days + `.slot` times (`.off` taken) · upload: file drop (built from tokens; not in the kit) + `.tile` error summary + `.tbl` errors · checklist `.fld` with `.tag.neutral` Not set · `.seg` language EN DE JA
- Phone `/m/*` · control · `.tabs` bottom (Today, Tasks, Time, Alerts) · `.agenda` today · `.fld` log time · `.feed` alerts
- Admin `/admin` · control · `.tabs`: Roles grid `.tbl` with `.box`, Audit `.toolbar` + `.tbl`, Integrations `.tbl` with `.tag.negative` Sync failed + `.note`
