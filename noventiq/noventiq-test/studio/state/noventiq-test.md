---
use_case: Noventiq test
client: Noventiq
poc_row: POC-noventiq-test-20261026
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g2
version: 1 · since 2026-10-26T12:22:01Z
channel: C0CC5KT4JTB
threads:
  g1: 1793018143.802509
  g2: 1793021709.228989
  g3:
  g4:
intent:
stage_flag:

gates:
  g1: {status: approved, round: 1, posted_ts: 1793018143.802509, decided_by: Gourav Mahunta, decided_at: 2026-10-26T13:04:00Z}
  g2: {status: waiting, round: 1, posted_ts: 1793021709.228989, decided_by: , decided_at: }
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
  - when: 2026-10-26T13:40:00Z
    kind: g2
    ts: 1793021709.228989
    by: bot
    version: 1
    round: 1
    documents:
      - {name: "Plan · Noventiq test · v1 r1", type: scope, file_url: "https://orbit.uat.unifyapps.com/auth/file/asset/download/dc756099499faeaaaea1bd2f", file_name: plan-v1-r1.pdf, file_size: 543102}
  - when: 2026-10-26T13:42:00Z
    kind: status
    ts: 1793021709.228989
    by: bot
    version: 1
    round: 1

runs:
  - started: 2026-10-26T12:22:01Z
    ended: 2026-10-26T12:36:00Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 154
    outcome: posted G1
  - started: 2026-10-26T13:12:00Z
    ended: 2026-10-26T13:40:00Z
    gate: g2
    stages: [2-plan]
    spawns: 1
    tokens: 262
    outcome: posted G2

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

coverage:
  - ask: A1
    by: "beat 1"
  - ask: A2
    by: "beat 3"
  - ask: A3
    by: "beat 3"
  - ask: A4
    by: "beat 3"
  - ask: A5
    by: "beat 1"
  - ask: A6
    by: "beat 3"
  - ask: A7
    by: "control: weighted booking forecast and expected gross profit tiles on Pipeline (beat 2)"
  - ask: A8
    by: "beat 6"
  - ask: A9
    by: "beat 6"
  - ask: A10
    by: "open question: demo date and audience"
  - ask: A11
    by: "beat 1"
  - ask: A12
    by: "beat 2"
  - ask: A13
    by: "beat 3"
  - ask: A14
    by: "beat 3"
  - ask: A15
    by: "beat 4"
  - ask: A16
    by: "beat 4"
  - ask: A17
    by: "beat 5"
  - ask: A20
    by: "beat 1"
  - ask: A21
    by: "beat 2"
  - ask: A22
    by: "beat 2"
  - ask: A23
    by: "beat 3"
  - ask: A24
    by: "beat 3"
  - ask: A25
    by: "beat 5"
  - ask: A26
    by: "beat 6"
  - ask: A27
    by: "control: Mapping tab on Pipeline (beat 2)"
  - ask: A28
    by: "beat 3"
  - ask: A29
    by: "open question: a deal's status read live from the CRM"
  - ask: A30
    by: "beat 4"
  - ask: A31
    by: "control: persona switch Finance or Sales in the header, Gross profit screen (beat 3)"
  - ask: A32
    by: "control: India people-cost note on Gross profit (beat 3)"
  - ask: A33
    by: "beat 1"

size:
  pages: 5
  objects: 7
  automations: 4
  agents: 1
  tasks: 35
  nebula_plans: 4
  note: "over the reference (4 pages, 3 objects, 3 automations, 1 AI agent) on pages, objects and automations; a flag, not a cut; 3-build sequences 4 plans"

data:
  source: "assumed, shaped like Noventiq's systems per entity (Creatio, Dynamics 365 and Black and White CRM; NetSuite, SAP Business One and Tally; local payrolls; Zoho Projects and Azure DevOps): fictional rows written by 2-plan in studio/data/seed/ (7 CSV files); no file was given"
  masked: "none needed: fictional; invented company and person names, no real identifier; amounts in USD, chosen so each quarter's gross profit adds up line by line"
  rows: "Customer 12, CRM account 18, Opportunity 20, Rebate 12, Reconciliation 12, Data issue 4 (record · seed, named, story row NQ-C-0042 Kestrel Pharma in the first 20), GP line 57 (record · seed naming the file, under 200); all in UnifyApps Storage"
  expected_answers: eval.csv

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
  - by: Gourav Mahunta
    when: 2026-10-26
    text: "G1 approved (thread reply 'approved', recorded on the POC row). The 9 G1 open questions were not answered in the thread; they carry to G2."
  - by: plan
    when: 2026-10-26
    text: "Working assumptions from the 9 unanswered G1 questions: the recommended option of each (three views: accounts and pipeline, gross profit, vendor rebates, with A6 and A7 kept as controls since no ask is cut; entities Noventiq Germany, Embee, NQ AI; Creatio; fictional data; two personas Finance and Sales; one assistant beside dashboard views; A18, A19, A34 to A37 stay out). The undecided ones are carried as plan open questions for the owner."
  - by: plan
    when: 2026-10-26
    text: "Modes beyond the default: CRM status beside each deal is mocked (no CRM connection on the tenant, A29); expected gross profit on Pipeline and the reconciliation reasons are deterministic and never shown as AI; the persona switch is mocked; source systems are seeded rows shaped like each system."
  - by: plan
    when: 2026-10-26
    text: "External step: none. The tenant's only Jira connection (6a4c061b6fbae67b71ab307d) is active and answered the read-only probe jira_get_all_projects with 0 projects, so no issue can be created; no CRM, ERP or ITSM connection exists. Carried as an open question."
  - by: plan
    when: 2026-10-26
    text: "Names: Noventiq · objects (OBJ_nq_*), automations and agent, and the code app Noventiq Watchtower ('watchtower' is the client's own word, A4, A5); the solution links nothing yet and every object id read back as free."
  - by: profile
    when: 2026-10-26
    text: "Brand colour: brand-sample.py read noventiq.com and its two stylesheets but found no :root colour; the client's own header logo (www.noventiq.com/images/svg/noventiq/logo.svg, saved as published) carries #0B408B (wordmark navy), #25AADD and #E31D22. Standing answer for an ambiguous colour: the wordmark navy #0B408B, hue 215, recommended and listed in the G2 pack with the other two."
  - by: profile
    when: 2026-10-26
    text: "Logo: found, Noventiq's header logo saved as studio/design-system/noventiq/logo.svg, used as published."
  - by: profile
    when: 2026-10-26
    text: "Model for the Watchtower assistant: Nebula's recommendation. Publish and deploy on the tenant without asking; visibility PRIVATE."
  - by: state-check
    when: 2026-10-26
    text: "reverted stage_flag: written by plan, outside its fields (schema § Who writes what)"

dev_issues: []

frozen:

cost:
  runs: 2
  agent_spawns: 2
  tokens_m: 0.41
  wall_h: 0.9

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
  - by: plan
    for: owner
    text: "Intent: what should the audience leave with? Options: (a) both: the outcome first, then two hood beats (the Reconcile gross profit automation, the Watchtower assistant in the agent builder) [recommended]; (b) use-case: no hood beats; (c) platform: two to four hood beats and a description on every node and field"
  - by: plan
    for: owner
    text: "Entities and countries (A1): the plan uses Noventiq Germany (NetSuite and Creatio), Embee (India; Dynamics 365 and SAP Business One) and NQ AI (India; Black and White CRM and Tally). The name and country of the first are assumed, and two of the three are in India although A1 says three countries. Options: (a) keep these three, deals spread across Germany, Austria, Switzerland, India and Singapore [recommended]; (b) the lead names the first entity and its country; (c) the lead names three other entities"
  - by: plan
    for: owner
    text: "Data (the client's slide asks for 'a working prototype on real data'): Options: (a) fictional data shaped like their systems, with the three difficult cases seeded: an unmatched customer, a rebate booked a quarter late, a team with missing timesheets [recommended]; (b) Noventiq sends extracts per entity, which 2-plan profiles and masks before seeding (up to 200 rows per object)"
  - by: plan
    for: owner
    text: "Demo date and audience (A10): Options: (a) the build is ready by 2026-11-09 for the 10 November demo to Noventiq's group finance and sales leaders, in person [recommended]; (b) another date or audience the lead gives"
  - by: plan
    for: owner
    text: "A deal's current status read live from the CRM (A29): no Dynamics 365, Creatio or Black and White connection exists on the tenant. Options: (a) show the stored status labelled as read from the CRM and say in the room it would be read live [recommended]; (b) the lead provides a sandbox CRM connection, whose credential is asked for at build"
  - by: plan
    for: owner
    text: "External step: the tenant's only Jira connection lists no projects, and no CRM, ERP or ITSM connection exists. Options: (a) no external step; the demo stands on its own data [recommended]; (b) the lead names a Jira project on a connection that can see it, and the Data issues screen raises DI-101 as a DEMO-TEST issue; (c) email the reconciliation result from the tenant's Outlook connection"
  - by: plan
    for: owner
    text: "Two sources were not read: the recording 'Noventiq Use Case.mov' and the insurance claim AI accelerator the client shared as a UI reference (A9). Options: (a) go ahead without them: one digital assistant beside dashboard views [recommended]; (b) the lead shares a transcript or the reference, and the plan is checked against it before G3"
---

build:
  plans: []

## build_contract
Spec file in Nebula's exact shape: /home/user/all-demo-foders/noventiq/noventiq-test/.sessions/88455b10-96d8-5ec5-9a55-2f2ea40d7856/drafts/studio/noventiq-test.md (`spec check`: ready, no issues, no warnings). Headings are demoted two levels here so this section stays one block.

### Noventiq Watchtower demo

#### Requested outcome
Noventiq's group finance and sales leaders see accounts, pipeline and gross profit for three POC entities (Noventiq Germany, Embee, NQ AI) in one code app, Noventiq Watchtower, built on a common data layer: one customer key across three CRMs, one group set of stages, local service codes mapped to the catalogue and one Finance-approved gross profit rule with a named owner. Every number opens to its source lines, the quarter close refuses to reconcile while a customer is unmatched, and a digital assistant answers questions over the same data. The story follows Kestrel Pharma (NQ-C-0042), held under three names in Dynamics 365, Creatio and Black and White CRM.

#### Touches
- object · Noventiq · Customer · new
- object · Noventiq · CRM account · new
- object · Noventiq · Opportunity · new
- object · Noventiq · GP line · new
- object · Noventiq · Rebate · new
- object · Noventiq · Data issue · new
- object · Noventiq · Reconciliation · new
- automation · Noventiq · Match customer · new
- automation · Noventiq · Reconcile gross profit · new
- automation · Noventiq · Read watchtower data · new
- automation · Noventiq · Ask the assistant · new
- ai-agent · Noventiq · Watchtower assistant · new
- code-app · Noventiq Watchtower · new

#### Contract
##### object · Noventiq · Customer
One legal customer of the group, with its one customer key and hierarchy.
- object · create · Noventiq · Customer (`OBJ_nq_customer`): one legal customer of the group with its one key. customer_key text primaryKey (NQ-C-nnnn), group_name text, segment picklist (enterprise "Enterprise", smb "SMB"), parent_key text (the parent's customer_key, empty at the top of the hierarchy), industry text, home_country text, key_owner text; required customer_key, group_name, segment
- record · seed · Noventiq · Customer: the 12 rows of studio/data/seed/customer.csv (story row NQ-C-0042 Kestrel Pharma, enterprise, India, key owner Meera Iyer; NQ-C-0043 Kestrel Pharma Research has parent NQ-C-0042)

##### object · Noventiq · CRM account
An account as one country CRM holds it, matched to a group customer key.
- object · create · Noventiq · CRM account (`OBJ_nq_crm_account`): one account as a country CRM holds it. source_id text primaryKey, entity picklist (nq_de "Noventiq Germany", embee "Embee", nq_ai "NQ AI"), source_system picklist (creatio "Creatio", dynamics_365 "Dynamics 365", black_and_white "Black and White CRM"), local_name text, customer_key text, match_status picklist (matched "Matched", unmatched "Unmatched"), suggested_key text, match_score number, revenue_fy_usd number, deals_closed number, products_sold text; required source_id, entity, source_system, local_name, match_status; index on customer_key
- record · seed · Noventiq · CRM account: the 18 rows of studio/data/seed/crm_account.csv (DYN-ACC-3317 Kestrel Pharma Pvt Ltd at Embee and CRE-88412 Kestrel Pharma GmbH at Noventiq Germany matched to NQ-C-0042; BW-0719 KESTREL PHARMA LTD. at NQ AI unmatched, suggested NQ-C-0042 at 0.91)

##### object · Noventiq · Opportunity
One deal, with its local and group stage and its local and catalogue service.
- object · create · Noventiq · Opportunity (`OBJ_nq_opportunity`): one deal. opp_id text primaryKey, entity picklist (the three entity codes of CRM account), country text, customer_key text, crm_account_ref text, name text, source_system picklist (the three codes of CRM account), local_stage text, group_stage picklist (lead "Lead", qualified "Qualified", proposal "Proposal", negotiation "Negotiation", won "Won", lost "Lost"), local_service_code text, service_line picklist (software_licensing "Software licensing", cloud "Cloud", cybersecurity "Cybersecurity", professional_services "Professional services"), mapped_by picklist (rule "Mapping rule", ai_suggested "AI-suggested, approved"), amount_usd number, probability number, forecast_quarter text, close_date date epoch ms, crm_status_mocked text; required opp_id, entity, group_stage, service_line, amount_usd; index on customer_key, crm_account_ref
- record · seed · Noventiq · Opportunity: the 20 rows of studio/data/seed/opportunity.csv (close_date written as epoch ms of the CSV's date; Kestrel's OPP-EMB-5521 1-Qualify, OPP-DE-2207 Offer, OPP-AI-0391 Hot, the first and last both group stage Qualified)

##### object · Noventiq · GP line
One gross profit line for a quarter, with the source references behind each amount.
- object · create · Noventiq · GP line (`OBJ_nq_gp_line`): one gross profit line for a quarter. line_id text primaryKey, quarter text (2025-Q4 to 2026-Q3), entity picklist (the three entity codes), country text, service_line picklist (the four codes of Opportunity), customer_key text, crm_account_ref text, revenue_usd number, direct_cost_usd number, people_days number, standard_day_rate_usd number, people_cost_usd number, vendor_rebate_usd number, gp_usd number, erp_source text, erp_ref text, payroll_source text, timesheet_source text, project_ref text, planned_days number, actual_days number, timesheet_status picklist (complete "Complete", missing_september "Missing September"); required line_id, quarter, entity, service_line, gp_usd; index on quarter, crm_account_ref
- record · seed · Noventiq · GP line: the 57 rows of studio/data/seed/gp_line.csv (GPL-NQAI-2026Q3-5, BW-0719, no customer key, gp 60960; GPL-NQAI-2026Q3-1 PRJ-NQAI-014 planned 50 days, actual 55, gp -3800; Embee's Q2 line GPL-EMBEE-2026Q2-1 carries the 1490000 Microsoft rebate as earned)

##### object · Noventiq · Rebate
One vendor rebate or funding line, with the quarter earned and the quarter booked.
- object · create · Noventiq · Rebate (`OBJ_nq_rebate`): one vendor rebate or funding line. rebate_id text primaryKey, vendor text, entity picklist (the three entity codes), segment picklist (enterprise "Enterprise", smb "SMB"), programme text, amount_usd number, quarter_earned text, quarter_booked text, status picklist (booked "Booked", booked_late "Booked a quarter late", accrued "Accrued"); required rebate_id, vendor, entity, segment, amount_usd, quarter_earned, status
- record · seed · Noventiq · Rebate: the 12 rows of studio/data/seed/rebate.csv (RB-EMB-MS-26Q2 Microsoft, Embee, enterprise, 1200000, earned 2026-Q2, booked 2026-Q3, booked_late)

##### object · Noventiq · Data issue
One data issue a rule found, with its owner and whether it blocks the close.
- object · create · Noventiq · Data issue (`OBJ_nq_data_issue`): one data issue found by a rule. issue_id text primaryKey, kind picklist (unmatched_customer "Unmatched customer", late_rebate "Rebate booked late", missing_timesheets "Missing timesheets", unmapped_service_code "Unmapped service code"), entity picklist (the three entity codes), record_ref text, detail text, suggested_fix text, rule text, rule_owner text, severity picklist (blocking "Blocks the close", warning "Warning"), status picklist (open "Open", fixed "Fixed"), reconciling_amount_usd number, quarter text, fixed_by text, fixed_at text; required issue_id, kind, entity, severity, status
- record · seed · Noventiq · Data issue: the 4 rows of studio/data/seed/data_issue.csv (DI-101 unmatched customer BW-0719 blocking open, owner Daniel Weber; DI-102 late rebate -1200000 in 2026-Q3 warning open, owner Meera Iyer; DI-103 missing timesheets PRJ-NQAI-014 warning open, owner Ananya Rao; DI-104 unmapped service code AI-ML-BUILD fixed)

##### object · Noventiq · Reconciliation
Gross profit against the accounts for one entity and quarter.
- object · create · Noventiq · Reconciliation (`OBJ_nq_reconciliation`): gross profit against the accounts for one entity and quarter. run_id text primaryKey, quarter text, entity picklist (the three entity codes), gp_ledger_usd number, gp_computed_usd number, reconciling_items_usd number, difference_usd number, result picklist (not_run "Not run", reconciled "Reconciled", blocked "Blocked"), reason text, rule text, rule_owner text, run_at text; required run_id, quarter, entity, gp_ledger_usd, result
- record · seed · Noventiq · Reconciliation: the 12 rows of studio/data/seed/reconciliation.csv (nine reconciled rows for 2025-Q4 to 2026-Q2; REC-NQDE-2026Q3, REC-EMBEE-2026Q3 ledger 1711380 and REC-NQAI-2026Q3 ledger 117160 not_run)

##### automation · Noventiq · Match customer
Gives an unmatched CRM account its group customer key and fixes the data issue.
- automation · create · Noventiq · Match customer: callable; input source_id text, customer_key text, matched_by text; refuses with matched false and reason `No group customer <key>` when the key is not a Customer; else sets customer_key and match_status matched on the CRM account, sets customer_key on every GP line and Opportunity whose crm_account_ref is source_id, and sets the open unmatched_customer Data issue for that record_ref to fixed with fixed_by and today's date; result matched boolean, lines_updated number, reason text

##### automation · Noventiq · Reconcile gross profit
Reconciles a quarter's gross profit to the accounts per entity, or refuses with the reason.
- automation · create · Noventiq · Reconcile gross profit: callable; input quarter text, run_by text; for each entity: computed is the sum of gp_usd of that quarter's GP lines that carry a customer_key, reconciling is the sum of reconciling_amount_usd of open late_rebate Data issues for that entity and quarter, difference is computed minus gp_ledger_usd minus reconciling; result reconciled when the absolute difference is at most 0.5 percent of gp_ledger_usd and no open blocking Data issue exists for that entity, else blocked with a reason naming each blocking issue and the difference; writes the Reconciliation row run_id `REC-<ENTITY>-<quarter without dash>` by id with upsert true, with rule GP-01, rule owner Meera Iyer, Group Financial Controller, and run_at; result entities list of {entity, result, difference_usd, reason}, all_reconciled boolean

##### automation · Noventiq · Read watchtower data
The assistant's read-only tool over the watchtower objects.
- automation · create · Noventiq · Read watchtower data: callable, read only; input dataset text (customers, crm_accounts, opportunities, gp_lines, rebates, data_issues, reconciliations), filters text (JSON field equals or range), persona text (finance or sales), limit number; result rows list, count number; for persona sales it removes people_days, standard_day_rate_usd and people_cost_usd from every row; never writes

##### automation · Noventiq · Ask the assistant
Passes a question from the app to the Watchtower assistant and returns its answer.
- automation · create · Noventiq · Ask the assistant: callable; input question text, persona text, screen text; invokes the Noventiq · Watchtower assistant agent with the question, persona and screen (Invoke Agent, ai_agents_by_unifyapps); result answer text, sources list of {label, ref}, refused boolean

##### ai-agent · Noventiq · Watchtower assistant
The digital assistant: a read-only assistant over accounts, pipeline, gross profit and rebates.
- ai-agent · create · Noventiq · Watchtower assistant: instructions: answer questions from Noventiq's group finance and sales leaders about accounts, pipeline, gross profit, rebates and data issues for Noventiq Germany, Embee and NQ AI from Read watchtower data only, passing the persona it is given; amounts in USD; name the source of every number (line id, CRM account, rebate id or ERP reference) on a sources line; use the group stages, the catalogue service lines and rule GP-01 (vendor rebates count in the quarter earned); decline individual salary or payroll questions and anything for persona sales about people cost; say plainly when the data does not hold what is asked (forecasts of rebates, ITSM tickets) and what it can answer instead; never create or change anything; model: Nebula's recommendation; tool: Read watchtower data

##### code-app · Noventiq Watchtower
The code app: accounts, pipeline, gross profit, data issues, rebates and the assistant.
- code-app · create · Noventiq Watchtower: the shell: the design system stylesheet, the fonts, the rail (Noventiq logo; Accounts, Pipeline, Gross profit, Data issues, Rebates), the header (screen name, entity filter Noventiq Germany, Embee, NQ AI, the persona switch Finance or Sales, profile), the right-hand assistant panel slot, the routes for Accounts, Pipeline, Gross profit, Data issues and Rebates; PRIVATE
- code-app · update · Noventiq Watchtower: screen Accounts: `.toolbar` (search reporting "n of m", entity, segment and match status `.chipsel`) above a `.tblwrap .tbl` of group customers (customer key, group name, segment, CRMs holding it, revenue this year, deals closed, products sold) with `.pg`; selecting a customer opens a side pane `.g3 .pad` with its hierarchy, one row per CRM account (source system `.tag`, local name, entity, revenue, deals) and the sum with its sources; reads Customer, CRM account, Opportunity
- code-app · update · Noventiq Watchtower: screen Pipeline: `.tile` open pipeline, weighted booking forecast for 2026-Q4 and expected gross profit (weighted amount times the service line's last-four-quarter GP margin, a deterministic figure) with `.delta`; `.chart` pipeline by group stage stacked by service line with `.legend`; `.tabs` Deals and Mapping; Deals `.toolbar` (search, stage, service line, country, entity `.chipsel`) over a `.tbl` showing local stage beside group stage and local service code beside service line, mapped_by as a `.tag`, the CRM status shown as read from the CRM; Mapping `.tbl` of each local stage and local service code to its group value with the rule owner; reads Opportunity, GP line
- code-app · update · Noventiq Watchtower: screen Gross profit: `.tile` gross profit for each of the last four quarters with `.delta`; `.chart` GP by quarter by service line; `.toolbar` (quarter, entity, country, service line `.chipsel`, group by service line, country or customer `.seg`) over a `.tbl` of GP with revenue, direct cost, people cost, rebate and GP; every amount opens a trace side pane `.g3` listing its GP lines with ERP source and reference, payroll source, timesheet source, project, standard day rate and days; a project whose actual days pass its planned days shows `.tag.negative` Over plan with planned and actual; a `.note` with rule GP-01 and its owner, and a `.note` that India entities show people cost at standard rates only; persona Sales hides people cost, days and rates and shows "Visible to Finance only"; reads GP line, Customer, Rebate
- code-app · update · Noventiq Watchtower: screen Data issues: a quarter close strip `.stv` (lines loaded, customers matched, rebates checked, reconcile) with Reconcile Q3 as the one `.btn-p`; the result per entity as `.tag` Reconciled, Blocked or Not run with difference and reason, the refusal as `.tag.negative` and a `.note` naming DI-101; `.tbl` of data issues (kind, entity, record, detail, rule, rule owner, severity, status) with an open issue's side pane showing the suggested fix as an AI Insight card `.ai:not(.msg)` labelled AI-suggested and Match to NQ-C-0042 as its one action; the fixed issues listed as found and fixed with who and when; reads Data issue, Reconciliation, CRM account · calls Reconcile gross profit on Reconcile Q3 and Match customer on Match
- code-app · update · Noventiq Watchtower: screen Rebates and the assistant panel: Rebates `.tile` rebates earned in the last four quarters, booked late, accrued; `.toolbar` (vendor, entity, segment, quarter earned `.chipsel`) over a `.tbl` with quarter earned beside quarter booked and status `.tag` (Booked a quarter late as `.tag.attention`); assistant panel on every screen: right pane `.g2` with `.convo .msg.me .msg.ai`, three suggested questions as `.chips`, `.stages` while it works, the answer in an AI Insight card `.ai:not(.msg)` with an AI-written label, a sources line and one action, the cannot-answer state saying why and what to ask instead; reads Rebate · calls Ask the assistant on Send

#### Business rules
- GP-01, owned by Meera Iyer, Group Financial Controller: gross profit is revenue minus direct cost minus people cost at standard day rates plus vendor rebates in the quarter they are earned.
- One customer key per legal customer across every CRM (owner Daniel Weber, Sales Operations); an account with no key is an unmatched customer and blocks the quarter close for its entity.
- Local CRM stages map to one group set of stages (Lead, Qualified, Proposal, Negotiation, Won, Lost) and local service codes to one catalogue (Software licensing, Cloud, Cybersecurity, Professional services); each mapping has a named owner.
- A quarter reconciles for an entity when computed gross profit, after listed reconciling items, is within 0.5 percent of the accounts and no blocking data issue is open.
- People cost, days and day rates are visible to the Finance persona only.
- A project whose actual days pass its planned days is shown as over plan.
- Every amount opens to the source lines behind it.
- Anything the assistant writes carries an AI-written label and its sources; AI-suggested matches and mappings change nothing until a person accepts them.
- Amounts in USD at planning rates; quarters are calendar quarters.
- Look: the app's one stylesheet is /home/user/all-demo-foders/noventiq/noventiq-test/studio/design-system/noventiq/client.css (hue 215, brand #0B408B); the rail logo is /home/user/all-demo-foders/noventiq/noventiq-test/studio/design-system/noventiq/logo.svg, as published; theme light with the dark tokens left live and no toggle in the chrome.
- Status shows an icon and a word, never colour alone.

#### Ready when
- The finance lead sees Kestrel Pharma as one customer held in three CRMs, the pipeline by group stage, service and country, and gross profit for the last four quarters with every amount opening to its source lines.
- Reconcile Q3 is refused for NQ AI while BW-0719 is unmatched; after Match to NQ-C-0042 it reconciles all three entities, and the assistant explains Embee's Q2 gross profit by the late Microsoft rebate with its sources.
- deploy Noventiq · Match customer
- deploy Noventiq · Reconcile gross profit
- deploy Noventiq · Read watchtower data
- deploy Noventiq · Ask the assistant
- publish Noventiq · Watchtower assistant
- publish Noventiq Watchtower

#### Assumptions
- Check this: proposed intent `both` (the outcome first, then two hood beats); the owner sets it at G2.
- Check this: the G1 open questions were not answered; the plan follows each recommended option: the three views are accounts and pipeline, gross profit, and vendor rebates, with utilisation (A6) and the booking forecast (A7) shown as controls; the three entities are Noventiq Germany (NetSuite and Creatio), Embee (Dynamics 365 and SAP Business One) and NQ AI (Black and White CRM and Tally); the CRM is Creatio; fictional data shaped like their systems; two personas, Finance and Sales; one assistant beside dashboard views; deliverables 1, 2, 3 and 5 stay out.
- Check this: the brand colour #0B408B (hue 215) is the wordmark navy of Noventiq's own logo; the site declares no colour variables, the other logo colours are #25AADD and #E31D22.
- Check this: the name and country of the NetSuite and Creatio entity (Noventiq Germany) are assumed; Embee and NQ AI are both in India.
- Check this: the CRM status beside each deal is a stored value standing in for a live CRM read; no CRM connection exists on the tenant.
- Check this: no external step; the tenant's Jira connection lists no projects.
- Check this: the code app name Noventiq Watchtower is free; if taken, the name gets the suffix "· Demo".
- Check this: the persona switch stands in for real sign-ins and entitlements.
- All seed rows are fictional; no real person, company or identifier; amounts in USD.

#### Capability check
- 7 object · create lines · beats 1–6 · fde-agent · apply_object_batch · read: get_objects · ok
- 7 record · seed lines (largest 57 rows, a named file under 200; the rest 20 rows or fewer) · beats 1–6 · fde-agent · save_entity_records · read: get_records · ok
- Match customer, Reconcile gross profit, Read watchtower data (callable, storage reads and writes) · beats 4, 5, 6 · automation-agent · compile_and_save_workflow, deploy_workflow · read: describe_callable_workflow; trigger_workflow_run then inspect_workflow_run; search_workflows for the deploy · ok
- Reconcile gross profit writes the Reconciliation row by id · beat 4, 5 · automation-agent · update by id with upsert true (task-kinds § Update by id is not an upsert) · read: get_records on REC-NQAI-2026Q3 · ok
- Ask the assistant: Invoke Agent (ai_agents_by_unifyapps_invoke_agent, read in search_operations on this tenant; no connection) · beat 6 · automation-agent · compile_and_save_workflow · read: trigger_workflow_run with eval row 1 · ok
- Noventiq · Watchtower assistant · beat 6 · agent-builder · create_agent, add_tools, publish_agent · read: get_agent; send_test_messages with the 12 eval rows · ok
- Code app create and 5 updates · beats 1–6 · code-app-agent · create_code_app, create_code_app_data_sources, push_code_patch · read: get_code_app head.sha, bindings.ts FETCH id, callables.ts blocks · ok
- Publish Noventiq Watchtower · all beats · code-app-agent · publish_code_app · read: deployed with commitHash · ok
- Live CRM read of a deal's status (A29) · beat 2 · none · no CRM connection on the tenant (list_connections) · read: — · no tool: open question 5 (stored status meanwhile)
- External step on Jira (A3) · none · the Jira connection lists 0 projects (read-only probe) · read: — · no tool: open question 6
- Real sign-in per persona (A31) · beat 3 · none · governance tools not granted · read: — · worked around: persona switch, people cost hidden by the app and by Read watchtower data

## entities

## beats
Storyline: "Accounts, pipeline and gross profit, every number traceable to source" (A11, A12, A13, A14), 6 beats and 2 hood beats; proposed intent `both`.

### Beat 1 · One customer across three CRMs
- does: As Priya Raman (Group Finance) opens Accounts, searches "Kestrel", opens NQ-C-0042 Kestrel Pharma.
- shows: "1 of 12"; Kestrel Pharma, enterprise, key owner Meera Iyer, held in three CRMs: DYN-ACC-3317 Kestrel Pharma Pvt Ltd (Dynamics 365, Embee) $1,840,000, CRE-88412 Kestrel Pharma GmbH (Creatio, Noventiq Germany) $960,000, BW-0719 KESTREL PHARMA LTD. (Black and White CRM, NQ AI) $210,000 tagged Unmatched; $3,010,000 this year in all; child Kestrel Pharma Research (NQ-C-0043) $150,000; deals closed and products sold per CRM.
- route: /accounts
- asks: A1 A5 A11 A20 A33
- mode: live

### Beat 2 · Pipeline in one group set of stages
- does: Opens Pipeline; filters service line Cloud and country Germany; opens the Mapping tab.
- shows: open pipeline $3,795,000 across 16 deals by group stage stacked by service line; 2026-Q4 weighted booking forecast $1,598,500 and expected gross profit; OPP-DE-2207 Azure migration services $340,000 at Proposal (Creatio "Offer"); the mapping of Dynamics 365 "1-Qualify" and Black and White "Hot" both to Qualified, each local service code to its catalogue line, AI-suggested mappings tagged, with their owner Daniel Weber; each deal's CRM status.
- route: /pipeline
- asks: A3 A7 A12 A21 A22 A27
- mode: live; expected gross profit deterministic; CRM status mocked

### Beat 3 · Gross profit, last four quarters, traced to source
- does: Opens Gross profit; reads the four quarters; groups by customer; clicks Kestrel Pharma's Q3 amount; opens PRJ-NQAI-014; switches the persona to Sales.
- shows: Q4 2025 $784,880, Q1 2026 $800,260, Q2 2026 $2,026,660, Q3 2026 $852,880 under rule GP-01 (owner Meera Iyer); Kestrel Q3 $70,740 from GPL-NQDE-2026Q3-4 $32,140 (NetSuite NS-INV-2026Q3-103) and GPL-EMBEE-2026Q3-2 $38,600 (SAP Business One SAPB1-INV-2026Q3-101), with $60,960 under Unassigned customer (Tally TLY-INV-2026Q3-104); PRJ-NQAI-014 Over plan, 50 days planned, 55 running, GP -$3,800, timesheets missing for September; the India note; as Sales, people cost, days and rates hidden and "Visible to Finance only".
- route: /gross-profit
- asks: A2 A3 A4 A6 A13 A14 A23 A24 A28 A31 A32
- mode: live

### Beat 4 · The close refuses (failure beat)
- does: Opens Data issues; clicks Reconcile Q3.
- shows: Noventiq Germany Reconciled, difference $0; Embee Reconciled after the reconciling item -$1,200,000 for DI-102, the Microsoft rebate booked a quarter late; NQ AI Blocked: "DI-101 unmatched customer BW-0719; computed $56,200 against $117,160 in the accounts, difference -$60,960".
- route: /data-issues
- asks: A15 A16 A30
- mode: live

### Beat 5 · Fix the data, then close
- does: Opens DI-101; reads the suggested match; clicks Match to NQ-C-0042; clicks Reconcile Q3 again.
- shows: the AI-suggested match NQ-C-0042 Kestrel Pharma, name 0.91 and same tax registration, rule "one customer key per legal customer", owner Daniel Weber; the match writes BW-0719, one GP line and one deal; DI-101 Fixed by Priya Raman today beside DI-104 found and fixed earlier; all three entities Reconciled, NQ AI with the warning DI-103; Kestrel Pharma's Q3 gross profit now $131,700.
- route: /data-issues → /gross-profit
- asks: A16 A17 A20 A25 A30
- mode: live (the suggested match seeded)

### Beat 6 · Ask the watchtower (lean-forward)
- does: Opens Rebates; filters Microsoft and Embee; opens the assistant and types "Why is Embee's gross profit in Q2 2026 so much higher than in Q3?"; then asks "What is Ananya Rao's salary?".
- shows: rebates by vendor, entity and segment with quarter earned beside quarter booked: Embee Microsoft enterprise $2,120,000 and SMB $290,000, RB-EMB-MS-26Q2 $1,200,000 Booked a quarter late; the answer in an AI Insight card: the rebate earned in Q2 and booked in Q3, GP-01 counts it in Q2, Q2 $1,678,600 against Q3 $511,380, sources RB-EMB-MS-26Q2 and the Embee GP lines; a plain refusal of the salary question saying people cost is held only at standard rates for Finance.
- route: /rebates, assistant panel
- asks: A8 A9 A14 A15 A26
- mode: live agent

Failure beat: beat 4 (Reconcile Q3 refused for NQ AI while a customer is unmatched). Lean-forward beat: beat 6.

Alternatives considered: B / C
- B: An AI-suggested mapping of a new local service code accepted live (A22): shows AI mapping, but the slide puts mapping in the data layer, and it is quiet on screen
- C: The 2026-Q4 booking and profit forecast (A7): a number, not judgement, and it overlaps the sales watchtower
- Why beat 6: A9 (P0) asks for a digital assistant beside the dashboards, the profile's show-off line names an AI assistant over live data, and the answer ties three asks together: the rebate, the late booking and the Finance rule.

### H1 · After beat 5: open Noventiq · Reconcile gross profit in the automation canvas
- shows: rule GP-01, the 0.5 percent tolerance, the blocking-issue check and the named rule owner
- asks: A23 A25
- mode: live

### H2 · After beat 6: open Noventiq · Watchtower assistant in the agent builder
- shows: its instructions, its one read-only tool Read watchtower data, the persona filter that hides people cost from Sales
- asks: A14 A31
- mode: live

### AI surfaces
- Watchtower assistant answers: live
- Suggested customer match on DI-101: seeded
- AI-suggested stage and service mappings (mapped_by): seeded
- Expected gross profit on Pipeline: deterministic (weighted amount times the service line's margin; not shown as AI)
- Reconciliation result and reason: deterministic (the GP-01 rule in the automation; not shown as AI)

### Other modes
- CRM status beside each deal: mocked (a stored value; no CRM connection on the tenant)
- Source systems (Creatio, Dynamics 365, Black and White CRM, NetSuite, SAP Business One, Tally, payrolls, Zoho Projects, Azure DevOps): mocked as seeded rows shaped like each system
- Persona switch Finance or Sales: mocked (stands in for sign-in and entitlements)
- Every demo-path action (Match, Reconcile Q3, Send): live automation

### Story row
NQ-C-0042 · Kestrel Pharma · enterprise · India · key owner Meera Iyer · CRM accounts DYN-ACC-3317 (Dynamics 365, Embee, $1,840,000, 4 deals), CRE-88412 (Creatio, Noventiq Germany, $960,000, 3 deals), BW-0719 (Black and White CRM, NQ AI, $210,000, unmatched, suggested NQ-C-0042 at 0.91) · child NQ-C-0043 · deals OPP-EMB-5521 $620,000 Qualified (1-Qualify), OPP-DE-2207 $340,000 Proposal (Offer), OPP-AI-0391 $85,000 Qualified (Hot) · Q3 2026 GP $70,740 before the match, $131,700 after · issue DI-101 · NQ AI Q3 ledger $117,160

## views
- Shell (every screen) (beats 1–6): rail `.rail` on the brand gradient with the Noventiq logo and Accounts, Pipeline, Gross profit, Data issues, Rebates; header with `.crumb`, entity `.chipsel` (Noventiq Germany, Embee, NQ AI), persona `.seg` Finance or Sales, profile `.av`; `.amb.a .amb.b .amb.v`
- Accounts (beats 1): `.toolbar` (`.field` search with "n of m", entity, segment, match status `.chipsel`) above `.tblwrap .tbl` with source system `.tag` and `.pg`; customer side pane `.g3 .pad` with hierarchy, CRM accounts `.tbl` and Unmatched `.tag.attention`; `.empty` states
- Pipeline (beats 2): `.tile` ×3 (open pipeline, weighted Q4 booking forecast, expected GP) with `.delta`; `.chart` pipeline by group stage stacked by service line with `.legend`; `.tabs` Deals, Mapping; Deals `.toolbar` (search, stage, service line, country, entity `.chipsel`) over `.tbl` with local and group values and mapped_by `.tag`; Mapping `.tbl` with owner `.av`
- Gross profit (beats 3, 5): `.tile` ×4 quarters with `.delta`; `.chart` GP by quarter by service line with `.legend`; `.toolbar` (quarter, entity, country, service line `.chipsel`, group by `.seg`) over `.tbl`; trace side pane `.g3 .pad` with source lines `.tbl`, Over plan `.tag.negative`, people cost masked for Sales; `.note` GP-01 and owner, `.note` India people cost
- Data issues (beats 4, 5): close strip `.stv` with Reconcile Q3 `.btn-p`; per-entity result `.tag.positive` Reconciled / `.tag.negative` Blocked with a `.note` reason; `.toolbar` over issues `.tbl` with severity and status `.tag`; issue side pane `.g3` with the suggested match in `.ai:not(.msg)` labelled AI-suggested and Match to NQ-C-0042 `.btn-p`; found and fixed `.feed .fi .fd`; `.toast`
- Rebates (beats 6): `.tile` ×3 (earned, booked late, accrued); `.toolbar` (vendor, entity, segment, quarter earned `.chipsel`) over `.tbl` with Booked a quarter late `.tag.attention`
- Assistant panel (every screen) (beats 6): right pane `.g2`; `.convo .msg.me .msg.ai`; `.chips` suggested questions; `.stages` while it works; answer in `.ai:not(.msg)` with AI-written `.tag`, sources line and one `.btn-s`; cannot-answer `.note`
