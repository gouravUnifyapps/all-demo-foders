---
use_case: ClickUp Delivery command dashboard
client: Clickup
poc_row: POC-clickup-delivery-command-dashboard-20261026
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g1
version: 1 · since 2026-10-26T09:54:26Z
channel: C0CBXB542R1
threads:
  g1: 1793009027.033199
  g2:
  g3:
  g4:
intent:
stage_flag:

gates:
  g1: {status: waiting, round: 1, posted_ts: 1793009027.033199, decided_by: , decided_at: }
  g2: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
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

runs:
  - started: 2026-10-26T09:54:26Z
    ended: 2026-10-26T10:04:05Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 145
    outcome: posted G1

stopped:

asks:
  - id: A1
    text: "Earlier warning: a project at risk of missing its go-live date is flagged at least three weeks before the date, on average."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A2
    text: "Less reporting effort: weekly status reports take a consultant under 10 minutes instead of about an hour."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A3
    text: "Balanced staffing: no consultant is booked above 100% for more than one week in a quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A4
    text: "Faster customer sign-off: customers approve deliverables in the portal within two working days."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 1 Summary · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A5
    text: "Delivery Command should make all three visible and actionable."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 2 Background · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A6
    text: "Brand colour: none supplied. Take it from the live site clickup.com."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A7
    text: "Logo: no file supplied. Fetch the official logo. It appears on the sign-in page, the expanded and collapsed left menu, the browser tab icon, the customer portal header, generated status reports (PDF and Word), and the weekly executive email."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A8
    text: "Customer logos: shown as circles on project cards and in the portal."
    source: "ClickUp-Delivery-Command-BRD.pdf p.1 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
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
    status: open
  - id: A11
    text: "Feel: the internal workspace is a daily working tool and should stay dense and quiet. The customer portal and the executive summary are also shown in sales demos and should look polished."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A12
    text: "Appearance: light and dark both needed. Light is the default."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 3 Brand · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A13
    text: "List every project with customer, region, stage, go-live date, health, lead, seats and contract value. Users search and filter by region, stage, health and lead. The count of results shows as \"x of y\". Filters that apply show as removable chips with one \"clear all\"."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A14
    text: "Show portfolio health as counts of On track, At risk and Off track, with the change since last week."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A15
    text: "Place each open risk on a grid of likelihood against impact, so leaders see which risks matter most. Choosing a cell lists its risks."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A16
    text: "Show every go-live date in the next 90 days on a timeline, grouped by region, with slipped dates marked."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A17
    text: "Show how the share of projects on track has moved over the last 12 weeks."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A18
    text: "Leaders can save a filtered view and share it with their team."
    source: "ClickUp-Delivery-Command-BRD.pdf p.2 § 5.1 Portfolio P6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A19
    text: "A project overview shows the stage the project is in, the seven stages as a progress path, days to go-live, budget hours used against planned, open risks and the next customer sign-off due."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A20
    text: "Tasks can be viewed as a list or as a board with one column per stage. A column shows a warning when it holds more than its limit (default 15). Tasks can be moved between columns by dragging or from a menu."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A21
    text: "A timeline shows tasks with start and end dates, dependencies between them and the critical path. Changing a date moves dependent tasks and shows the new go-live date before it is saved."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A22
    text: "A risks, assumptions, issues and decisions (RAID) log records each item with owner, due date, status and history."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A23
    text: "A document library holds the statement of work, migration plans and sign-off records. Files open in a viewer inside the application."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A24
    text: "An activity feed shows who changed what and when on the project."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A25
    text: "Task detail opens beside the list so the user keeps their place. It shows description, assignee, dates, time logged, comments and attachments."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.2 Project workspace W7 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A26
    text: "Show every consultant against the next 12 weeks with the percentage they are booked each week. Over 100% is flagged."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A27
    text: "Book a consultant onto a project by choosing person, project, weeks and hours. Booking works without dragging."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A28
    text: "Show consultants against skills (data migration, integrations, admin training, API, Japanese language) with a level for each, so the right person can be found."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A29
    text: "Consultants log time against tasks each day. Managers approve or return weekly timesheets, giving a reason when they return one."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A30
    text: "Should: show booked hours against capacity for each region over the quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf p.3 § 5.3 Resourcing and time R5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A31
    text: "An implementation lead raises a change request with the reason, the work added or removed, and the effect on hours, cost and go-live date."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A32
    text: "Before submitting, the lead sees the plan before and after the change side by side, with the differences marked."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A33
    text: "Changes under 40 hours need the delivery director's approval. Changes of 40 hours or more also need the finance partner, in that order. The request shows who has approved and who is next."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A34
    text: "Rejecting a change request requires a written reason. Approved changes update the plan and are recorded in the activity feed."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.4 Scope changes and approvals S4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A35
    text: "Delivery Copilot is an AI assistant available from every internal screen. It has the tools listed below. Anything it writes is labelled as AI-written."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot (intro) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A36
    text: "Users ask questions in plain language, for example \"Which Japan projects go live in November and are at risk?\" The assistant opens with three suggested questions based on the user's projects, and shows each stage while it works."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A37
    text: "Chart tool: the assistant can answer with a chart, such as hours by stage or go-lives by month. Charts use the application's colours and show units."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A38
    text: "Status report tool: the assistant drafts the weekly status report for a project from its tasks, risks and time entries. The lead edits and publishes it. The report can be exported as PDF or Word."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A39
    text: "Task tool: the assistant can propose tasks, for example after a meeting summary. Proposed tasks are listed for the user to accept or reject; nothing is created without acceptance."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A40
    text: "Meeting summary tool: the assistant summarises a customer meeting transcript into decisions, actions and risks. Each point links to the part of the transcript it came from."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A41
    text: "Risk prediction: the assistant flags projects likely to miss go-live, with a confidence level and the evidence for each flag, such as migration tasks running late."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4 § 5.5 Delivery Copilot A6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A42
    text: "Customer sponsors sign in to see only their own project: stage, milestones, upcoming sessions, open actions for their team and the documents shared with them."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A43
    text: "Sponsors sign off a stage deliverable or request changes with a comment. A sign-off records who approved and when."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A44
    text: "Sponsors book training sessions by choosing a day and then a time slot. Taken slots stay visible but cannot be chosen."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A45
    text: "Sponsors upload files such as user lists (CSV up to 50,000 rows). Errors appear row by row and can be fixed before confirming."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A46
    text: "A readiness checklist guides the customer through 10 setup items. An item they have not answered shows as not set, never as a guessed value."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C5 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A47
    text: "The portal is available in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf p.4–5 § 5.6 Customer portal C6 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A48
    text: "A weekly summary shows six headline numbers with their change from last week: active projects, go-lives this month, projects at risk, average days to go-live, consultant utilisation and contract value awaiting go-live. A change is coloured by whether it is good or bad for the business, not by its sign."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E1 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A49
    text: "Show how contract value awaiting go-live moved from last month to this month, split into new projects, go-lives completed, slipped dates and cancellations."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A50
    text: "List the five projects that changed most this week, with the reason for each."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.7 Executive summary E3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
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
    status: open
  - id: A53
    text: "Notifications for new assignments, sign-offs and mentions. Each can be marked read or opened."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.8 Consultant on the phone M2 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
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
    status: open
  - id: A56
    text: "Show the status of each integration (Salesforce, Slack, Google Drive, Jira) with last sync time and any error."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.9 Administration and audit D3 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A57
    text: "Project settings (name, region, go-live date, budget hours) can be edited in place, with clear unsaved, saving, saved and failed states."
    source: "ClickUp-Delivery-Command-BRD.pdf p.5 § 5.9 Administration and audit D4 · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
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
    status: open
  - id: A60
    text: "Customers get a shorter top menu: Home, Sign-offs, Sessions, Files, Checklist."
    source: "ClickUp-Delivery-Command-BRD.pdf p.6 § 6 Navigation · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A61
    text: "The phone has bottom tabs: Today, Tasks, Time, Alerts."
    source: "ClickUp-Delivery-Command-BRD.pdf p.6 § 6 Navigation · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A62
    text: "Active projects | 180 to 300 | Portfolio list needs paging, search and filters"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A63
    text: "Tasks per project | 150 to 1,200 | Board and timeline must stay readable"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A64
    text: "Consultants and leads | about 72 | Resourcing grid is people against 12 weeks"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A65
    text: "Open risks across the portfolio | about 400 | Grid of likelihood against impact, with drill-down"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A66
    text: "Customer users | about 900 | Portal must be simple for occasional users"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A67
    text: "Time entries per week | about 3,000 | Timesheet approval in batches"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A68
    text: "Customer upload | up to 50,000 rows | Errors summarised, not listed in full"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A69
    text: "Languages | English, German, Japanese | Text can grow by 30% in German"
    source: "ClickUp-Delivery-Command-BRD.pdf p.6–7 § 7 Data volumes (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A70
    text: "Good or finished | On track, Signed off, Approved, Live"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A71
    text: "Needs attention | At risk, Awaiting sign-off, Over capacity, Pending approval"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A72
    text: "Problem | Off track, Blocked, Rejected, Sync failed"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A73
    text: "Neutral | Not started, Draft, Scheduled, Hypercare"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Status words (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A74
    text: "Project IDs look like IMP-2611, change requests like CR-0457, risks like RSK-1183."
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Sample content · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A75
    text: "Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026 年 10 月 17 日). Money shows in the contract currency (USD, EUR or JPY)."
    source: "ClickUp-Delivery-Command-BRD.pdf p.7 § 8 Sample content · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A76
    text: "No projects assigned yet | Projects appear here once a lead assigns you"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A77
    text: "A search or filter matches nothing | Nothing matches the current filters, with a way to clear them"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A78
    text: "Copilot is still working | Which stage it is on"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A79
    text: "Copilot cannot answer | Why, and what to try instead"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A80
    text: "An integration has failed | Which one, since when, and what is affected"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A81
    text: "A booking takes someone over capacity | Who, which weeks and by how much, before saving"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A82
    text: "A customer upload has errors | For example 214 of 50,000 rows need fixing"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A83
    text: "A checklist item has no answer | The item shows as not set"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A84
    text: "The user has no access to a project | Who can grant access"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A85
    text: "The session is about to end | How to stay signed in"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A86
    text: "Data is out of date | When it was last updated"
    source: "ClickUp-Delivery-Command-BRD.pdf p.7–8 § 9 Situations the screens must handle (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A87
    text: "The internal workspace is in English. The customer portal is in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A88
    text: "Times show the user's time zone. Weeks start on Monday in Europe and Japan and on Sunday in North America."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A89
    text: "All drag actions also work from the keyboard. Controls are at least 24 px on desktop and larger on the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A90
    text: "Meaning never depends on colour alone: every status shows an icon and a word."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A91
    text: "Screens meet WCAG 2.2 AA in both light and dark appearance."
    source: "ClickUp-Delivery-Command-BRD.pdf p.8 § 10 Languages, regions and accessibility · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
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
    status: open
  - id: A97
    text: "Executive time to read the weekly summary | 10 minutes or less"
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 13 Success measures (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A98
    text: "Customers completing the readiness checklist without help | 75%"
    source: "ClickUp-Delivery-Command-BRD.pdf p.9 § 13 Success measures (table row) · posted in #clickup-test-4 by Gourav Mahunta (ts 1793001752.474139); same file as psl_document input row v1 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
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

coverage: []

size:

data:

verify:

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

dev_issues: []

frozen:

cost:
  runs: 1
  agent_spawns: 1
  tokens_m: 0.15
  wall_h: 0.2

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
---

## build_contract

## entities

## beats

## views
