---
use_case: ClickUp Delivery command platform
client: Clickup
poc_row: POC-clickup-delivery-command-platform-20261023
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g1
version: 1 · since 2026-10-23T11:57:39Z
thread: C0CBK3E47E2 · 1792757255.287779
intent: 
stage_flag: 

gates:
  g1: {status: waiting, round: 1, posted_ts: 1792757255.287779, decided_by: , decided_at: }
  g2: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
  g3: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
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
runs:
  - started: 2026-10-23T11:57:39Z
    ended: 2026-10-23T12:07:57Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 140
    outcome: posted G1

stopped: 

asks:
  - id: A1
    text: "Delivery Command should make all three visible and actionable."
    source: "ClickUp-Delivery-Command-BRD.pdf §2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A2
    text: "Brand colour: none supplied. Take it from the live site clickup.com."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Brand colour (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A3
    text: "Logo: no file supplied. Fetch the official logo. It appears on the sign-in page, the expanded and collapsed left menu, the browser tab icon, the customer portal header, generated status reports (PDF and Word), and the weekly executive email."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Logo (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A4
    text: "Customer logos: shown as circles on project cards and in the portal."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Customer logos (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A5
    text: "Typeface: take it from the live site. Numbers must line up in tables. The customer portal must also display Japanese and German text correctly."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Typeface (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A6
    text: "Tone: clear, calm and direct. Errors say what happened and what to do next. No jokes or exclamation marks in the product."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Tone (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A7
    text: "Feel: the internal workspace is a daily working tool and should stay dense and quiet. The customer portal and the executive summary are also shown in sales demos and should look polished."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Feel (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A8
    text: "Appearance: light and dark both needed. Light is the default."
    source: "ClickUp-Delivery-Command-BRD.pdf §3 Appearance (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A9
    text: "List every project with customer, region, stage, go-live date, health, lead, seats and contract value. Users search and filter by region, stage, health and lead. The count of results shows as \"x of y\". Filters that apply show as removable chips with one \"clear all\"."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A10
    text: "Show portfolio health as counts of On track, At risk and Off track, with the change since last week."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A11
    text: "Place each open risk on a grid of likelihood against impact, so leaders see which risks matter most. Choosing a cell lists its risks."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A12
    text: "Show every go-live date in the next 90 days on a timeline, grouped by region, with slipped dates marked."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A13
    text: "Show how the share of projects on track has moved over the last 12 weeks."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A14
    text: "Leaders can save a filtered view and share it with their team."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 P6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A15
    text: "A project overview shows the stage the project is in, the seven stages as a progress path, days to go-live, budget hours used against planned, open risks and the next customer sign-off due."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A16
    text: "Tasks can be viewed as a list or as a board with one column per stage. A column shows a warning when it holds more than its limit (default 15). Tasks can be moved between columns by dragging or from a menu."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A17
    text: "A timeline shows tasks with start and end dates, dependencies between them and the critical path. Changing a date moves dependent tasks and shows the new go-live date before it is saved."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A18
    text: "A risks, assumptions, issues and decisions (RAID) log records each item with owner, due date, status and history."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A19
    text: "A document library holds the statement of work, migration plans and sign-off records. Files open in a viewer inside the application."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A20
    text: "An activity feed shows who changed what and when on the project."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A21
    text: "Task detail opens beside the list so the user keeps their place. It shows description, assignee, dates, time logged, comments and attachments."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 W7 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A22
    text: "Show every consultant against the next 12 weeks with the percentage they are booked each week. Over 100% is flagged."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A23
    text: "Book a consultant onto a project by choosing person, project, weeks and hours. Booking works without dragging."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A24
    text: "Show consultants against skills (data migration, integrations, admin training, API, Japanese language) with a level for each, so the right person can be found."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A25
    text: "Consultants log time against tasks each day. Managers approve or return weekly timesheets, giving a reason when they return one."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A26
    text: "Should: show booked hours against capacity for each region over the quarter."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 R5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A27
    text: "An implementation lead raises a change request with the reason, the work added or removed, and the effect on hours, cost and go-live date."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A28
    text: "Before submitting, the lead sees the plan before and after the change side by side, with the differences marked."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A29
    text: "Changes under 40 hours need the delivery director's approval. Changes of 40 hours or more also need the finance partner, in that order. The request shows who has approved and who is next."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A30
    text: "Rejecting a change request requires a written reason. Approved changes update the plan and are recorded in the activity feed."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 S4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A31
    text: "Delivery Copilot is an AI assistant available from every internal screen."
    source: "ClickUp-Delivery-Command-BRD.pdf §5.5 intro a (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A32
    text: "Anything it writes is labelled as AI-written."
    source: "ClickUp-Delivery-Command-BRD.pdf §5.5 intro b (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A33
    text: "Users ask questions in plain language, for example \"Which Japan projects go live in November and are at risk?\" The assistant opens with three suggested questions based on the user's projects, and shows each stage while it works."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A34
    text: "Chart tool: the assistant can answer with a chart, such as hours by stage or go-lives by month. Charts use the application's colours and show units."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A35
    text: "Status report tool: the assistant drafts the weekly status report for a project from its tasks, risks and time entries. The lead edits and publishes it. The report can be exported as PDF or Word."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A36
    text: "Task tool: the assistant can propose tasks, for example after a meeting summary. Proposed tasks are listed for the user to accept or reject; nothing is created without acceptance."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A37
    text: "Meeting summary tool: the assistant summarises a customer meeting transcript into decisions, actions and risks. Each point links to the part of the transcript it came from."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A38
    text: "Risk prediction: the assistant flags projects likely to miss go-live, with a confidence level and the evidence for each flag, such as migration tasks running late."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 A6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A39
    text: "Customer sponsors sign in to see only their own project: stage, milestones, upcoming sessions, open actions for their team and the documents shared with them."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A40
    text: "Sponsors sign off a stage deliverable or request changes with a comment. A sign-off records who approved and when."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A41
    text: "Sponsors book training sessions by choosing a day and then a time slot. Taken slots stay visible but cannot be chosen."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A42
    text: "Sponsors upload files such as user lists (CSV up to 50,000 rows). Errors appear row by row and can be fixed before confirming."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A43
    text: "A readiness checklist guides the customer through 10 setup items. An item they have not answered shows as not set, never as a guessed value."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C5 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A44
    text: "The portal is available in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 C6 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A45
    text: "A weekly summary shows six headline numbers with their change from last week: active projects, go-lives this month, projects at risk, average days to go-live, consultant utilisation and contract value awaiting go-live. A change is coloured by whether it is good or bad for the business, not by its sign."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A46
    text: "Show how contract value awaiting go-live moved from last month to this month, split into new projects, go-lives completed, slipped dates and cancellations."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A47
    text: "List the five projects that changed most this week, with the reason for each."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A48
    text: "The summary is also sent as an email every Monday at 08:00 in each region's time zone."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 E4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A49
    text: "Consultants see today's tasks and sessions, update a task's status, and log time in under 30 seconds on a phone."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 M1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A50
    text: "Notifications for new assignments, sign-offs and mentions. Each can be marked read or opened."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 M2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A51
    text: "Roles control what each user can see and change. Show roles against permissions as a grid."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D1 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A52
    text: "Keep a record of who did what and when. It cannot be edited and can be filtered by person, project and action."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D2 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A53
    text: "Show the status of each integration (Salesforce, Slack, Google Drive, Jira) with last sync time and any error."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D3 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A54
    text: "Project settings (name, region, go-live date, budget hours) can be edited in place, with clear unsaved, saving, saved and failed states."
    source: "ClickUp-Delivery-Command-BRD.pdf §5 D4 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A55
    text: "Sign-in, forgot password, reset password"
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Screens (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A56
    text: "Internal users navigate with a left menu: Portfolio, Projects, Resourcing, Timesheets, Changes, Admin."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A57
    text: "The top bar shows the current project or view, search, notifications and the profile menu."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A58
    text: "Delivery Copilot opens as a panel on the right."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A59
    text: "Customers get a shorter top menu: Home, Sign-offs, Sessions, Files, Checklist."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A60
    text: "The phone has bottom tabs: Today, Tasks, Time, Alerts."
    source: "ClickUp-Delivery-Command-BRD.pdf §6 Navigation (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A61
    text: "Portfolio list needs paging, search and filters"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Active projects 180 to 300 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A62
    text: "Board and timeline must stay readable"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Tasks per project 150 to 1,200 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A63
    text: "Resourcing grid is people against 12 weeks"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Consultants and leads about 72 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A64
    text: "Grid of likelihood against impact, with drill-down"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Open risks across the portfolio about 400 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A65
    text: "Portal must be simple for occasional users"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Customer users about 900 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A66
    text: "Timesheet approval in batches"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Time entries per week about 3,000 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A67
    text: "Errors summarised, not listed in full"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Customer upload up to 50,000 rows (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A68
    text: "Text can grow by 30% in German"
    source: "ClickUp-Delivery-Command-BRD.pdf §7 Data volumes, row: Languages English, German, Japanese (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A69
    text: "On track, Signed off, Approved, Live"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Good or finished (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A70
    text: "At risk, Awaiting sign-off, Over capacity, Pending approval"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Needs attention (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A71
    text: "Off track, Blocked, Rejected, Sync failed"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Problem (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A72
    text: "Not started, Draft, Scheduled, Hypercare"
    source: "ClickUp-Delivery-Command-BRD.pdf §8 Status words, meaning: Neutral (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A73
    text: "Project IDs look like IMP-2611, change requests like CR-0457, risks like RSK-1183."
    source: "ClickUp-Delivery-Command-BRD.pdf §8 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A74
    text: "Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026年 10月 17日)."
    source: "ClickUp-Delivery-Command-BRD.pdf §8 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A75
    text: "Money shows in the contract currency (USD, EUR or JPY)."
    source: "ClickUp-Delivery-Command-BRD.pdf §8 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A76
    text: "Projects appear here once a lead assigns you"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: No projects assigned yet (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A77
    text: "Nothing matches the current filters, with a way to clear them"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A search or filter matches nothing (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A78
    text: "Which stage it is on"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: Copilot is still working (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A79
    text: "Why, and what to try instead"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: Copilot cannot answer (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A80
    text: "Which one, since when, and what is affected"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: An integration has failed (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A81
    text: "Who, which weeks and by how much, before saving"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A booking takes someone over capacity (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A82
    text: "For example 214 of 50,000 rows need fixing"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A customer upload has errors (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A83
    text: "The item shows as not set"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: A checklist item has no answer (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A84
    text: "Who can grant access"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: The user has no access to a project (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A85
    text: "How to stay signed in"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: The session is about to end (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A86
    text: "When it was last updated"
    source: "ClickUp-Delivery-Command-BRD.pdf §9 Situations the screens must handle, situation: Data is out of date (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A87
    text: "The internal workspace is in English. The customer portal is in English, German and Japanese."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A88
    text: "Times show the user's time zone. Weeks start on Monday in Europe and Japan and on Sunday in North America."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A89
    text: "All drag actions also work from the keyboard. Controls are at least 24 px on desktop and larger on the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A90
    text: "Meaning never depends on colour alone: every status shows an icon and a word."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A91
    text: "Screens meet WCAG 2.2 AA in both light and dark appearance."
    source: "ClickUp-Delivery-Command-BRD.pdf §10 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A92
    text: "Contract value, seats and close date when a deal is won, which creates the project"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Salesforce (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A93
    text: "Notifications and the weekly status post to each project channel"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Slack (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A94
    text: "Shared documents and customer uploads"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Google Drive (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A95
    text: "Engineering escalations linked to project issues"
    source: "ClickUp-Delivery-Command-BRD.pdf §11 Integrations, system: Jira (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A96
    text: "The first release does not include the following, and the application must not suggest otherwise:"
    source: "ClickUp-Delivery-Command-BRD.pdf §12 (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A97
    text: "Billing, invoicing or revenue recognition."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A98
    text: "Building or editing customer workspaces in the core ClickUp product."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A99
    text: "Hiring, performance reviews or payroll for consultants."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A100
    text: "A public marketing site."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A101
    text: "Video calls or call recording."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A102
    text: "Offline use of the phone view."
    source: "ClickUp-Delivery-Command-BRD.pdf §12 Out of scope (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A103
    text: "21 days or more"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Average warning before a missed go-live (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A104
    text: "Under 10 minutes"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Time to produce a weekly status report (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A105
    text: "No more than 1 per consultant"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Consultant weeks booked above 100% per quarter (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A106
    text: "2 working days or less"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Customer sign-off time (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A107
    text: "10 minutes or less"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Executive time to read the weekly summary (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A108
    text: "75%"
    source: "ClickUp-Delivery-Command-BRD.pdf §13 Success measures, measure: Customers completing the readiness checklist without help (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A109
    text: "I want to see every project on one screen without scrolling."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Delivery director (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A110
    text: "Let us edit the timeline straight from the phone."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Consultants (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A111
    text: "Show customers their health score."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, VP of customer success (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A112
    text: "Customers should never see internal health."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Implementation leads (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A113
    text: "Colour-code consultants by region everywhere."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Resource manager (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A114
    text: "Add a pricing calculator for upsells."
    source: "ClickUp-Delivery-Command-BRD.pdf §14 Stakeholder notes, Sales (Slack file F0CA4HW01MX, https://unifyapps.slack.com/archives/C0CBK3E47E2/p1792754833152389) · 2026-10-23"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Sales upsell pricing calculator"
    status: out_of_scope

coverage: []

size:

data:

verify:
  round: 0

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
dev_issues: []

frozen:

cost:
  runs: 1
  agent_spawns: 1
  tokens_m: 0.14
  wall_h: 0.15

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
---

## build_contract

## entities

## beats

## views
