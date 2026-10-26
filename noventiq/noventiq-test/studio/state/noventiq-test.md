---
use_case: Noventiq test
client: Noventiq
poc_row: POC-noventiq-test-20261026
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g1
version: 1 · since 2026-10-26T12:22:01Z
channel: C0CC5KT4JTB
threads:
  g1: 1793018143.802509
  g2:
  g3:
  g4:
intent:
stage_flag:

gates:
  g1: {status: waiting, round: 1, posted_ts: 1793018143.802509, decided_by: , decided_at: }
  g2: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
  g3: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
  g4: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }

posts:
  - when: 2026-10-26T12:36:00Z
    kind: status
    ts: 1793018143.802509
    by: bot
    version: 1
    round: 1
  - when: 2026-10-26T12:40:00Z
    kind: g1
    ts: 1793018143.802509
    by: bot
    version: 1
    round: 1
    documents:
      - {name: "Requirements · Noventiq test · v1 r1", type: requirements, file_url: "https://orbit.uat.unifyapps.com/auth/file/asset/download/b33075ae516c9548bdcd4134", file_name: requirements-v1-r1.pdf, file_size: 268015}

runs:
  - started: 2026-10-26T12:22:01Z
    ended: 2026-10-26T12:36:00Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 154
    outcome: posted G1

stopped:

asks:
  - id: A1
    text: "POC scope: 3 countries, 3 business views (subset of 6 full solution areas)"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A2
    text: "Data approach: strawman (not data lake); pull only what each use case requires, not all source data"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A3
    text: "Source systems: CRM (Dynamics 365 / Cresio), ERP (NetSuite / SAP B1), payroll, project management (Jira / Azure DevOps), ITSM"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A4
    text: "GP by service line, country, customer (revenue watchtower): monthly gross profit across service lines, sourced from ERP + project + payroll data"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A5
    text: "Customer and accounts / sales pipeline (sales watchtower): pipeline visibility, deals closed, products sold, revenue per customer from CRM"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A6
    text: "Utilization and delivery profitability: project overrun tracking (e.g. 50-day project running to 55 days = loss); overlaps with use case 1 but adds payroll and project management data"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A7
    text: "Booking and profit forecast: overlaps with sales watchtower"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A8
    text: "Vendor funding and rebate tracking: key income source; Embee does ~$800M with Microsoft India alone; rebate tracked by vendor, entity, and customer segment (enterprise vs. SMB)"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219, 2026-10-26 (the channel copy is cut off after 'key income sour...'; full words from the original)"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A9
    text: "UI expectation: combination of a digital assistant (chat/query) and static dashboard views; [the client's presenter] shared an insurance claim AI accelerator as a reference example"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta (original #p_noventiq 2026-10-24), https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001685778219 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A10
    text: "Demo Date: 10th November"
    source: "#noventiq-poc-build-studio-cloud, forwarded from Amogh Gupta, https://unifyapps.slack.com/archives/C0CC5KT4JTB/p1793001727482519 · 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A11
    text: "Account view across three CRMs"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'Deliverable 4 - What it must show' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A12
    text: "Pipeline by stage, service and country"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'Deliverable 4 - What it must show' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A13
    text: "Gross profit, last four quarters"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'Deliverable 4 - What it must show' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A14
    text: "Every number traceable to source"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'Deliverable 4 - What it must show' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P0
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A15
    text: "An unmatched customer, a rebate booked a quarter late, a team with missing timesheets."
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'Test the difficult cases' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A16
    text: "Reconciliation to the accounts"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'What the test report contains' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A17
    text: "Data issues found and fixed"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'What the test report contains' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A18
    text: "Effort per step and country"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'What the test report contains' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: POC programme measurement (test report)"
    status: out_of_scope
  - id: A19
    text: "What AI mapping really saved"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text), slide 17 'What the test report contains' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: POC programme measurement (test report)"
    status: out_of_scope
  - id: A20
    text: "One customer key and hierarchy"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text), slide 5 'POC must settle' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A21
    text: "One group set of stages"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text), slide 5 'POC must settle' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A22
    text: "Local codes mapped to catalogue"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text), slide 5 'POC must settle' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A23
    text: "One Finance-approved rule"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text), slide 5 'POC must settle' (gross profit) of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A24
    text: "Standard rates, utilisation feeds"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text), slide 5 'POC must settle' (people cost) of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A25
    text: "A named owner per rule"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text), slide 5 'POC must settle' (ownership) of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A26
    text: "Account, pipeline and gross-profit views + later AI agents"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text), slide 7 'Reports and AI assistants' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A27
    text: "Customer key, pipeline stages, service mapping, profit rules"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text), slide 7 'Common data layer - owned by Noventiq' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A28
    text: "CRM, ERP, HR, payroll and time tools in each country"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text), slide 7 'Today's systems - unchanged' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A29
    text: "Month-end gross profit needs stable, reconciled numbers – a copy is safer. A deal's current status can be read live from the CRM."
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text), slide 10 'Copy or read live?' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A30
    text: "Gross profit ties to the accounts"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text), slide 10 'Can Finance trust it?' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A31
    text: "Payroll visible to entitled only"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text), slide 16 'Security' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A32
    text: "Two POC entities are in India and the profit view uses people cost. Privacy rules must be cleared before data moves."
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text), slide 16 'Data residency' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A33
    text: "Accounts and pipeline first, by system type. Gross profit follows country by country, once payroll and utilisation data are ready."
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM (1).jpeg (image text), slide 14 'A likely combination' of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: this
    status: open
  - id: A34
    text: "Deliverable 1 – a rollout plan that compares the sequencing options and recommends one"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM (1).jpeg (image text), slide 14 of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: POC programme workstream B (rollout plan, definitions, architecture, business case)"
    status: out_of_scope
  - id: A35
    text: "Deliverable 2 – common business definitions, decided by Noventiq and written up by the partner"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM (1).jpeg (image text), slide 15 of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: POC programme workstream B (rollout plan, definitions, architecture, business case)"
    status: out_of_scope
  - id: A36
    text: "Deliverable 3 – a target solution that settles the technical choices in business terms"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text), slide 16 of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: POC programme workstream B (rollout plan, definitions, architecture, business case)"
    status: out_of_scope
  - id: A37
    text: "Deliverable 5 – a costed implementation plan and business case we can take to ExCom"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM.jpeg (image text), slide 18 of Noventiq's POC deck shown on a Teams call, shared in #noventiq-poc-build-studio-cloud · 2026-10-24"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: POC programme workstream B (rollout plan, definitions, architecture, business case)"
    status: out_of_scope

coverage: []

size:

data:

verify:
  round: 0

collaterals:

review:
  round: 0

decisions:
  - by: orchestrator
    when: 2026-10-26
    text: "Profile studio/profiles/noventiq.md drafted by Studio from the request and defaults."
  - by: orchestrator
    when: 2026-10-26
    text: "Preflight: python packages kokoro_onnx, soundfile, resvg_py, pptx, numpy were missing on the runner (they block G4 collaterals); installed with pip, doctor now ok. Bun, Chromium, ffmpeg, poppler, Slack read tools and the tenant sign-in ok."

dev_issues: []

frozen:

cost:
  runs: 1
  agent_spawns: 1
  tokens_m: 0.15
  wall_h: 0.4

open_questions:
  - by: harvest
    for: lead
    text: "Which three business views does the demo show? Recommended: (a) account and sales pipeline view (A5, A11, A12) + (b) gross profit by service line, country, customer over the last four quarters (A4, A13) + (c) vendor funding and rebate tracking (A8). Options: the recommended; or swap rebates for utilisation and delivery profitability (A6); or swap for booking and profit forecast (A7)."
  - by: harvest
    for: lead
    text: "Which three countries or entities does the demo use? Recommended: the three on the client's slide 9 - the NetSuite + Creatio entity (easy), Embee (typical, Dynamics + SAP B1) and NQ AI (hard, Black and White + Tally). Options: those three; or three named countries the lead gives."
  - by: harvest
    for: lead
    text: "The CRM is written 'Cresio' in the scope note (A3) and 'Creatio' on the client's slide 9. Which is right? Recommended: Creatio."
  - by: harvest
    for: lead
    text: "The recording 'Noventiq Use Case.mov' (Slack file, 78.8 KB, also a Drive link) could not be read: Slack returned file_content_unavailable on every attempt and no Drive tools are connected in this session. Can the lead share a transcript or re-upload the file? Recommended: share a transcript or notes in the channel; until then the demo rests on the scope note and the slides."
  - by: harvest
    for: lead
    text: "Is 'Demo Date: 10th November' (A10) the date this Studio build is shown to Noventiq (2026-11-10), and who is in the room? Recommended: yes, the build is ready by 2026-11-09 for a senior operations/finance audience."
  - by: harvest
    for: lead
    text: "The client's slide asks for 'a working prototype on real data'; the profile says the demo data is assumed and fictional. Which for this demo? Recommended: fictional data shaped like their systems (entities, CRMs, ERPs above), with the difficult cases seeded (an unmatched customer, a rebate booked a quarter late, a team with missing timesheets)."
  - by: harvest
    for: lead
    text: "Who may see payroll and people cost in the demo ('Payroll visible to entitled only', A31)? Recommended: two personas - a Finance user who sees people cost and gross profit, and a Sales user who sees accounts and pipeline only."
  - by: harvest
    for: lead
    text: "The scope note mentions an insurance claim AI accelerator shared by the client as the UI reference (A9). Can the lead share it? Recommended: go ahead without it - one digital assistant (chat over the data) beside static dashboard views."
  - by: harvest
    for: lead
    text: "The client's POC deliverables 1, 2, 3 and 5 (rollout plan, written definitions, target architecture, costed business case) and the test-report effort measures are recorded as other use cases (A18, A19, A34-A37). Keep them out of this demo? Recommended: yes - the demo shows deliverable 4 (the working prototype); reply 'promote A<n>' to bring any in."
---

build:
  plans: []

## build_contract

## entities

## beats

## views
