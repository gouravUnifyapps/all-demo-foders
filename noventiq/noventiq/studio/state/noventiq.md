---
use_case: Noventiq
client: Noventiq
poc_row: POC-noventiq-noventiq-20261026
owner: Gourav Mahunta · U09EK0B6NKD
manager: Mrinal Dixit · U08LPV6J011
status: awaiting_g2
version: 1 · since 2026-10-26T13:19:06Z
channel: C0CBYSL95UK
threads:
  g1: 1793021406.071119
  g2: 1793606130.909069
  g3:
  g4:
intent:
stage_flag:

gates:
  g1: {status: approved, round: 2, posted_ts: 1793021406.071119, decided_by: Mrinal Dixit, decided_at: 2026-11-02T06:58:00Z}
  g2: {status: waiting, round: 1, posted_ts: 1793606130.909069, decided_by: , decided_at: }
  g3: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
  g4: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }

posts:
  - when: 2026-10-26T13:30:14Z
    kind: g1
    ts: 1793021406.071119
    by: bot
    version: 1
    round: 1
    documents:
      - {name: Requirements · Noventiq · v1 round 1, type: requirements, file_url: https://orbit.uat.unifyapps.com/auth/file/asset/download/185f86c27c55f3f59eb32240, file_name: requirements-v1-r1.pdf, file_size: 242596}
  - when: 2026-10-26T13:30:25Z
    kind: status
    ts: 1793021406.071119
    by: bot
    version: 1
    round: 1

  - when: 2026-10-30T08:45:00Z
    kind: g1
    ts: 1793021406.071119
    by: bot
    version: 1
    round: 2
    documents:
      - {name: Requirements · Noventiq · v1 round 2, type: requirements, file_url: https://orbit.uat.unifyapps.com/auth/file/asset/download/aa81469344015d74225a162f, file_name: requirements-v1-r2.pdf, file_size: 230936}
  - when: 2026-10-30T08:46:30Z
    kind: status
    ts: 1793021406.071119
    by: bot
    version: 1
    round: 2
  - when: 2026-11-02T08:05:00Z
    kind: g2
    ts: 1793606130.909069
    by: bot
    version: 1
    round: 1
    documents:
      - {name: Plan · Noventiq · v1 round 1, type: scope, file_url: https://orbit.uat.unifyapps.com/auth/file/asset/download/0bbef3d8fb1f0ec39943ec25, file_name: plan-v1-r1.pdf, file_size: 374169}
  - when: 2026-11-02T08:06:00Z
    kind: status
    ts: 1793606130.909069
    by: bot
    version: 1
    round: 1
runs:
  - started: 2026-10-26T13:19:06Z
    ended: 2026-10-26T13:30:25Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 151
    outcome: posted G1
  - started: 2026-10-30T08:32:46Z
    ended: 2026-10-30T08:46:00Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 157
    outcome: posted G1
  - started: 2026-11-02T06:53:00Z
    ended: 2026-11-02T06:58:00Z
    gate: g1
    stages: []
    spawns: 0
    tokens: 0
    outcome: "waiting: G1 not approved on the row; Mrinal Dixit's 'Approved, proceed' arrived as feedback FB-1793602287223-1, not as an approval"
  - started: 2026-11-02T07:25:00Z
    ended: 2026-11-02T08:05:00Z
    gate: g2
    stages: [2-plan]
    spawns: 1
    tokens: 302
    outcome: posted G2

stopped:

asks:
  - id: A1
    text: "Account view across three CRMs"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A2
    text: "Pipeline by stage, service and country"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A3
    text: "Gross profit, last four quarters"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A4
    text: "Every number traceable to source"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A5
    text: "Demo Date: 10th November"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782562785989 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A6
    text: "POC scope: 3 countries, 3 business views (subset of 6 full solution areas)"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A7
    text: "Data approach: strawman (not data lake); pull only what each use case requires, not all source data"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A8
    text: "Source systems: CRM (Dynamics 365 / Cresio), ERP (NetSuite / SAP B1), payroll, project management (Jira / Azure DevOps), ITSM"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A9
    text: "GP by service line, country, customer (revenue watchtower): monthly gross profit across service lines, sourced from ERP + project + payroll data"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A10
    text: "Customer and accounts / sales pipeline (sales watchtower): pipeline visibility, deals closed, products sold, revenue per customer from CRM"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A11
    text: "Utilization and delivery profitability: project overrun tracking (e.g. 50-day project running to 55 days = loss); overlaps with use case 1 but adds payroll and project management data"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A12
    text: "Booking and profit forecast: overlaps with sales watchtower"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A13
    text: "Vendor funding and rebate tracking: key income source; Embee does ~$800M with Microsoft India alone; rebate tracked by vendor, entity, and customer segment (enterprise vs. SMB)"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A14
    text: "UI expectation: combination of a digital assistant (chat/query) and static dashboard views; [the client's presenter] shared an insurance claim AI accelerator as a reference example"
    source: "https://unifyapps.slack.com/archives/C0CB9U3N84F/p1792782531375759 · Amogh Gupta · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A15
    text: "An unmatched customer, a rebate booked a quarter late, a team with missing timesheets."
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A16
    text: "Easy demos always work. We need to see who fixes exceptions."
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A17
    text: "Reconciliation to the accounts"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A18
    text: "Data issues found and fixed"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A19
    text: "What AI mapping really saved"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A20
    text: "Deliverable 4 – a working prototype on real data, used by real people, with measured effort"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A21
    text: "Deliverable 2 – common business definitions, decided by Noventiq and written up by the partner"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM (1).jpeg (image text) · Noventiq deck p.15 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A22
    text: "Finance drafts the gross-profit rule before the POC starts. The POC tests it and proposes fixes where it breaks."
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM (1).jpeg (image text) · Noventiq deck p.15 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A23
    text: "One customer key and hierarchy"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A24
    text: "One group set of stages"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A25
    text: "Local codes mapped to catalogue"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A26
    text: "One Finance-approved rule"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A27
    text: "Standard rates, utilisation feeds"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A28
    text: "A named owner per rule"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A29
    text: "“Qualified” means a first call in one CRM and a confirmed budget in another. Adding them up looks precise – but is not."
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (2).jpeg (image text) · Noventiq deck p.5 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A30
    text: "The idea: keep today’s systems, add a common data layer, answer one business question at a time"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text) · Noventiq deck p.7 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A31
    text: "Account, pipeline and gross-profit views + later AI agents"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text) · Noventiq deck p.7 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A32
    text: "Customer key, pipeline stages, service mapping, profit rules"
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text) · Noventiq deck p.7 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A33
    text: "Whatever platform we pick, the customer key, mappings and rules are documented and ours."
    source: "WhatsApp Image 2026-10-23 at 5.48.08 AM (1).jpeg (image text) · Noventiq deck p.7 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A34
    text: "Gross profit ties to the accounts"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text) · Noventiq deck p.10 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A35
    text: "Customers, stages and services mapped reliably"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text) · Noventiq deck p.10 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A36
    text: "Our people fix exceptions without the partner"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text) · Noventiq deck p.10 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A37
    text: "Month-end gross profit needs stable, reconciled numbers – a copy is safer. A deal’s current status can be read live from the CRM."
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text) · Noventiq deck p.10 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A38
    text: "Payroll visible to entitled only"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text) · Noventiq deck p.16 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A39
    text: "Two POC entities are in India and the profit view uses people cost. Privacy rules must be cleared before data moves."
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text) · Noventiq deck p.16 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A40
    text: "Open choice of models"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text) · Noventiq deck p.16 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A41
    text: "Three countries were chosen for learning: an easy, a typical and a hard system landscape"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM (3).jpeg (image text) · Noventiq deck p.9 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A42
    text: "Effort per step and country"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM (1).jpeg (image text) · Noventiq deck p.17 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Deliverable 5 · costed implementation plan and business case"
    status: out_of_scope
  - id: A43
    text: "Effort per system and country"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text) · Noventiq deck p.10 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Deliverable 5 · costed implementation plan and business case"
    status: out_of_scope
  - id: A44
    text: "What each country took, extrapolated to 20+"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM.jpeg (image text) · Noventiq deck p.10 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Deliverable 5 · costed implementation plan and business case"
    status: out_of_scope
  - id: A45
    text: "Deliverable 5 – a costed implementation plan and business case we can take to ExCom"
    source: "WhatsApp Image 2026-10-23 at 5.48.05 AM.jpeg (image text) · Noventiq deck p.18 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Deliverable 5 · costed implementation plan and business case"
    status: out_of_scope
  - id: A46
    text: "Deliverable 1 – a rollout plan that compares the sequencing options and recommends one"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM (1).jpeg (image text) · Noventiq deck p.14 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Deliverable 1 · rollout plan"
    status: out_of_scope
  - id: A47
    text: "Deliverable 3 – a target solution that settles the technical choices in business terms"
    source: "WhatsApp Image 2026-10-23 at 5.48.06 AM.jpeg (image text) · Noventiq deck p.16 · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Deliverable 3 · target solution"
    status: out_of_scope
  - id: A48
    text: "The POC runs for about four months, from set-up to an approved implementation plan"
    source: "WhatsApp Image 2026-10-23 at 5.48.07 AM (2).jpeg (image text) · Noventiq deck p.02 (timeline) · shared by Amogh Gupta in #p_noventiq · 2026-10-24, forwarded to #noventiq_internal 2026-10-26"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: the four-month POC programme"
    status: out_of_scope
  - id: A49
    text: "Research and ideation on the actual business model of Noventiq should be added to the overall context to understand the central user-persona, their pain points a bit more to have a better idea on what AI features need to be created finally."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A50
    text: "What multiple countries would be incuded in the anlaysis"
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A51
    text: "Creation of the synthetic systems that we are supposed to connect with for the data on which the business intelligence is supposed to be generated."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A52
    text: "Answer to the six practical questions that drive cost and feasibility needs to be explicitly answered."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A53
    text: "In addition to current revenue health the solution should also offer cross-sell/up-sell opportunities at an account level with evidence collected from data across all of these accounts"
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A54
    text: "These suggestions should translate to traceable action plans that can be acclelerated/rolled back or edited at any point of time."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A55
    text: "Central logic of linking disjointed data across different sources into a singular source of truth at an account level across multiple connector sources."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A56
    text: "How that logic and context will flow inside the agent."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A57
    text: "Logic for returning evidence on each and everty financial calculation made…finance people do not trust AI without citations."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A58
    text: "Data Sync strategies, how exactly is data updated across any of these systems refelcted in the final response."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A59
    text: "Logic for tracing back the errors detected in any connector/any data at any point of time to it’s source."
    source: "psl_feedback FB-1793291553836-1 · Mrinal Dixit · reply in the G1 thread https://unifyapps.slack.com/archives/C0CBYSL95UK/p1793021406071119 · 2026-10-29"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open

coverage:
  - ask: A1
    by: beat 1
  - ask: A2
    by: beat 2
  - ask: A3
    by: beat 3
  - ask: A4
    by: beat 3
  - ask: A5
    by: open question 3
  - ask: A6
    by: beat 1
  - ask: A7
    by: beat H1
  - ask: A8
    by: beat 7
  - ask: A9
    by: beat 3
  - ask: A10
    by: beat 2
  - ask: A11
    by: control Delivery tab on Gross profit
  - ask: A12
    by: control weighted column and close-quarter facet on Pipeline
  - ask: A13
    by: control Rebates tab on Gross profit
  - ask: A14
    by: beat 7
  - ask: A15
    by: beat 4
  - ask: A16
    by: beat 5
  - ask: A17
    by: beat 4
  - ask: A18
    by: beat 5
  - ask: A19
    by: control minutes-saved tile on Accounts
  - ask: A20
    by: open question 4
  - ask: A21
    by: control Definitions tab on How it works
  - ask: A22
    by: beat 4
  - ask: A23
    by: beat 1
  - ask: A24
    by: beat 2
  - ask: A25
    by: control Definitions tab on How it works (service maps)
  - ask: A26
    by: beat 3
  - ask: A27
    by: control Delivery tab on Gross profit (standard rates, utilisation)
  - ask: A28
    by: beat 5
  - ask: A29
    by: beat 2
  - ask: A30
    by: beat H1
  - ask: A31
    by: beat 7
  - ask: A32
    by: control Definitions tab on How it works
  - ask: A33
    by: control Definitions tab on How it works
  - ask: A34
    by: beat 5
  - ask: A35
    by: beat 1
  - ask: A36
    by: beat 5
  - ask: A37
    by: control Layer copy / Live from CRM switch on Pipeline
  - ask: A38
    by: control Delivery tab on Gross profit (team-level cost only)
  - ask: A39
    by: open question 4
  - ask: A40
    by: beat H2
  - ask: A41
    by: beat 1
  - ask: A49
    by: beat 1
  - ask: A50
    by: beat 1
  - ask: A51
    by: beat 7
  - ask: A52
    by: beat H1
  - ask: A53
    by: beat 6
  - ask: A54
    by: beat 6
  - ask: A55
    by: beat 1
  - ask: A56
    by: beat H2
  - ask: A57
    by: beat 3
  - ask: A58
    by: beat 7
  - ask: A59
    by: beat 5

size:
  pages: 6
  objects: 12            # incl. Watchtower Seed snapshot (housekeeping)
  automations: 10        # incl. Noventiq Reset demo (housekeeping)
  agents: 1
  tasks: 63              # 12 object, 12 record, 9 shells + 10 logic + 10 deploys, 1 ai-agent, 1 agent publish, 7 code-app, 1 code-publish
  nebula_plans: 7        # one per 10 tasks, rounded up

data:
  source: "assumed, shaped like each synthetic source system (Creatio, Dynamics 365, Black and White CRMs; NetSuite, SAP B1, Tally ERPs; Payroll India; Zoho Projects and Azure DevOps time), generated by studio/data/seed/generate.py"
  masked: "none: fictional. Every company, person and id is invented; no emails or phones; payroll held at team level only; amounts in USD with INR at 84.00 per USD"
  rows:
    - "Source record: 178, record · seed from studio/data/seed/source-records.csv"
    - "Sync run: 10, record · seed from sync-runs.csv"
    - "Account: 13 named rows (story row NQ-ACC-0007 Meridian Retail Group), record · seed"
    - "Account link: 28, record · seed from account-links.csv"
    - "Opportunity: 20 named rows, record · seed"
    - "Definition: 17 named rows, record · seed"
    - "GP line: 77, record · seed from gp-lines.csv"
    - "Period close: 4 named rows, record · seed"
    - "Data exception: 6 named rows, record · seed"
    - "Account play: 6 named rows, record · seed"
    - "Play history: 2 named rows, record · seed"
    - "Watchtower Seed snapshot: one row per seeded row, written once by the seed tasks"
  expected_answers: eval.csv

verify:

collaterals:

review:

decisions:
  - by: orchestrator
    when: 2026-10-26
    text: "Preflight: all checks ok after installing the collateral python packages on the runner; Google Calendar connector needs a re-sign-in, so harvest could not read Calendar."
  - by: orchestrator
    when: 2026-10-26
    text: "Profile drafted by Studio from the POC row (no profile existed for Noventiq); defaults used for every line the row did not give."

  - by: Mrinal Dixit
    when: 2026-10-29
    ticket_no: FB-1793291553836-1
    text: "G1 changes requested (psl_feedback FB-1793291553836-1), verbatim: Feedback on the requirements doc : General: Research and ideation on the actual business model of Noventiq should be added to the overall context to understand the central user-persona, their pain points a bit more to have a better idea on what AI features need to be created finally. Ideation perspective/Features: What multiple countries would be incuded in the anlaysis. Creation of the synthetic systems that we are supposed to connect with for the data on which the business intelligence is supposed to be generated. Answer to the six practical questions that drive cost and feasibility needs to be explicitly answered. In addition to current revenue health the solution should also offer cross-sell/up-sell opportunities at an account level with evidence collected from data across all of these accounts → These suggestions should translate to traceable action plans that can be acclelerated/rolled back or edited at any point of time. BE perspective: Central logic of linking disjointed data across different sources into a singular source of truth at an account level across multiple connector sources. How that logic and context will flow inside the agent. Logic for returning evidence on each and everty financial calculation made…finance people do not trust AI without citations. Data Sync strategies, how exactly is data updated across any of these systems refelcted in the final response. Logic for tracing back the errors detected in any connector/any data at any point of time to it’s source. Incorporate these and proceed to the next stage"
  - by: Gourav Mahunta
    when: 2026-10-30
    ticket_no: FB-1793345185239-1
    text: "G1 changes requested (psl_feedback FB-1793345185239-1), verbatim: rebuild this"
  - by: Gourav Mahunta
    when: 2026-10-30
    ticket_no: FB-1793349011236-1
    text: "G1 changes requested (psl_feedback FB-1793349011236-1), verbatim: build"
  - by: orchestrator
    when: 2026-10-30
    text: "Preflight on the cloud runner: Bun, Chrome (Playwright Chromium), tenant sign-in and Slack read tools ok; collateral python packages and faster-whisper were missing; installed in this session (doctor now all ok)."
  - by: orchestrator
    when: 2026-10-30
    text: "G1 round 2: round-1 open questions 2 (real vs fictional data) and 3 (which entities) are superseded by round 2's synthetic-systems and countries questions; the requirements doc §3 carries the 14 still open."
  - by: Mrinal Dixit
    when: 2026-11-02
    ticket_no: FB-1793602287223-1
    text: "G1 feedback (psl_feedback FB-1793602287223-1), verbatim: Approved, proceed. Read as an intent to approve, not as a change, so G1 was not reworked; the row still shows g1_status waiting, and Demo Studio never approves a gate itself. G2 starts once the manager approves G1 on the POC page or replies exactly `approve` in the G1 thread."
  - by: Mrinal Dixit
    when: 2026-11-02
    text: "G1 approved on the POC row (g1_status approved; Mrinal Dixit replied 'Approved' in the G1 thread). The 14 round-2 open questions got no numbered answers; 2-plan proceeds on their recommended options and carries what still needs a human into the G2 pack."
  - by: plan
    when: 2026-11-02
    text: "Round-2 open questions got no numbered answers; the plan used their recommended options: 1 audience and presenter (group finance seat, to the group CFO office and the three country leads, 20 minutes), 2 persona (finance controller primary, account lead secondary), 3 countries (India for Embee and NQ AI, the easy entity's country as a placeholder), 4 synthetic systems, 5 business views (account with cross-sell and plans, pipeline, gross profit), 6 plans in the app with full history, 7 six questions in the plan and a How it works screen, 8 Creatio, 10 proceed without the call, 11 exceptions worklist in the story, 12 deliverables out of scope, 13 dashboards plus assistant, 14 Gourav Mahunta owns all asks. Questions 3 (the third country) and 9 (the recording) still need a human and are carried into G2."
  - by: plan
    when: 2026-11-02
    text: "Option 4 (one synthetic store per source system) is built as one Source record object keyed by system and source id, holding the nine systems' records with their own ids, codes, last-updated times and sync runs, rather than nine objects: linking, sync and trace-back show the same, and the build stays smaller."
  - by: research
    when: 2026-11-02
    text: "Site: https://noventiq.com (the official site, Wikipedia infobox). Brand colours from the site's own header logo, https://noventiq.com/images/svg/noventiq/logo.svg (navy #0B408B, sky #25AADD, red #E31D22); the homepage refused plain fetches (403) and its stylesheets hold no :root colour, so the logo's navy was passed to brand-sample as the swatch (hue 215)."
  - by: profile
    when: 2026-11-02
    text: "Ambiguous brand colour (three logo colours): the standing answer takes the recommended one, #0B408B navy; #25AADD and #E31D22 listed in the G2 plan doc. The logo was found on the site, so no wordmark placeholder."
  - by: plan
    when: 2026-11-02
    text: "Modes follow the default: Noventiq Finance Assistant is the one live, read-only agent; every demo-path action is a live automation; the cross-sell suggestions, AI-suggested matches and the Q3 AI Insight card are seeded with the AI marker; matching, stage mapping, GP and the minutes-saved tile are deterministic and never presented as AI."
  - by: plan
    when: 2026-11-02
    text: "The code app reaches the assistant through Noventiq Ask assistant (an automation invoking the agent with ai_agents_by_unifyapps_invoke_agent), because create_code_app_data_sources takes only storage and automation sources."
  - by: plan
    when: 2026-11-02
    text: "External step: the existing Jira Connection (6ababb56207d2c4e18ad380c) answered a read-only project list (KAN, SAM1); Route to owner creates a DEMO-TEST task in SAM1, off the critical path. The other connection named jira (6a4c061b6fbae67b71ab307d) lists no projects; the Dynamics 365 and NetSuite connections hold other teams' data, so none is used."
dev_issues: []

frozen:

cost:
  runs: 4
  agent_spawns: 3
  tokens_m: 0.61
  wall_h: 1.11

open_questions:
  - by: harvest
    for: lead
    text: "Which three business views does the 10 November demo show (A6 says 3 business views, A9 to A13 list five)? Options: (recommended) The deck's \"What it must show\": account view across three CRMs, pipeline by stage, service and country, gross profit for the last four quarters (A1 to A3); Revenue watchtower, sales watchtower and vendor funding and rebate tracking (A9, A10, A13); All five business questions, the two extra ones at lower depth"
  - by: harvest
    for: lead
    text: "The deck asks for \"a working prototype on real data\" (A20); the profile says fictional seed data. Which data does the demo use? Options: (recommended) Fictional data shaped like the client's systems (Creatio, Dynamics, Black and White; NetSuite, SAP B1, Tally), labelled as sample data; Wait for sample extracts from the client before G2; Fictional data now, swapped for client extracts in a feedback round"
  - by: harvest
    for: lead
    text: "Which entities or countries appear in the demo (A6, A41)? Options: (recommended) The deck's three landscapes: the NetSuite + Creatio entity (easy), Embee (typical), NQ AI (hard); Three countries the lead names"
  - by: harvest
    for: lead
    text: "The CRM is written \"Cresio\" in the internal note (A8) and \"Creatio\" on the client's slide. Which name is used on screen? Options: (recommended) Creatio; Another name the lead gives"
  - by: harvest
    for: lead
    text: "The recording \"Noventiq Use Case.mov\" could not be read (Slack refused the file; the Drive link needs a signed-in account and Drive is not connected here). How to proceed? Options: (recommended) Re-upload it to #noventiq_internal or connect Google Drive, so the next round reads it; go on with G1 meanwhile; Proceed without it"
  - by: harvest
    for: lead
    text: "Ashish Jha offered a short call with Mrinal Dixit to give the use case, and the Cognizant business model as a reference (#p_noventiq, 2026-10-26). Wait for it? Options: (recommended) Proceed to G2 now; fold what the call gives into a feedback round; Hold G1 until the call has happened"
  - by: harvest
    for: lead
    text: "The deck's \"test the difficult cases\" (A15, A16, A36): make an exceptions worklist part of the demo story? Options: (recommended) Yes: unmatched customer, rebate booked a quarter late and team with missing timesheets, each with a named owner who fixes it, as the story row; Keep as P1, shown only if time allows"
  - by: harvest
    for: lead
    text: "Deliverables 1, 3 and 5 and the four-month programme (A42 to A48) are consulting deliverables, not the demo app, and were marked out of scope. Agree? Options: (recommended) Yes, keep them out of scope; Promote some (reply promote A<n>), e.g. a cost-to-scale view"
  - by: harvest
    for: lead
    text: "The UI reference \"insurance claim AI accelerator\" (A14) was not shared in any source read. Which shape does the demo follow? Options: (recommended) Dashboards plus a digital assistant over the same data, as A14 and A31 describe; The lead shares the accelerator so the plan can follow it"
  - by: harvest
    for: lead
    text: "Every ask's proposed owner is the POC lead; Amogh Gupta tagged Mrinal Dixit and Gourav Mahunta with \"need to pick this\". Who owns the asks? Options: (recommended) Gourav Mahunta owns all asks; Split between Gourav Mahunta and Mrinal Dixit (the lead names which)"
  - by: harvest
    for: lead
    text: "[Not said yet: audience] Who presents on 10 November, and to whom (roles, slot length)? No source names the audience. Options: (recommended) A UnifyApps presenter in the seat of Noventiq's group finance team, to Noventiq's group CFO office and the country leads of the three POC entities, 20 minutes; The profile default: a senior operations leader, 20 minutes, in person, projector"
  - by: harvest
    for: lead
    text: "[Not said yet: persona] Which persona are the screens for (A49 asks for the central user persona)? No source names one. Options: (recommended) Primary: the group or country finance controller who must trust gross profit, rebates and reconciliation (A3, A4, A13, A17, A57); secondary: the country sales or account lead who acts on pipeline and cross-sell/up-sell action plans (A2, A10, A53, A54); The profile default: the client's team lead"
  - by: harvest
    for: lead
    text: "Which countries are in the analysis (replaces round 1's entities question) (A50, A6, A41)? The deck names three landscapes; A39 says two POC entities are in India; no source names the third country. Options: (recommended) India for Embee (typical landscape) and NQ AI (hard landscape), plus the country of the NetSuite + Creatio entity (easy landscape), which the lead names; shown as a placeholder country until named; Three countries the lead names now"
  - by: harvest
    for: lead
    text: "How are the synthetic source systems built (settles round 1's real-versus-fictional data question) (A51; the demo data is synthetic, which settles round 1's real-versus-fictional question)? Options: (recommended) One synthetic store per source system, shaped like its real records and with its own ids, codes and last-updated times (Creatio, Dynamics 365, Black and White CRMs, NetSuite, SAP B1 and Tally ERPs, payroll, Zoho Projects and Azure DevOps time), so linking, sync and trace-back to source can be shown; Mock APIs behind custom connectors that the data layer calls; Trial instances of the real products"
  - by: harvest
    for: lead
    text: "Where do the cross-sell/up-sell action plans live (A54: accelerated, rolled back or edited at any time)? Options: (recommended) In the demo app, each plan a record with steps, owner, due dates, the evidence it rests on and a full change history, so accelerate, roll back and edit are each a logged version; Also written back to the synthetic CRM as tasks or opportunities"
  - by: harvest
    for: lead
    text: "Where are the six practical questions (deck p.10: get the data, make it consistent, can Finance trust it, keep it running, copy or read live, scaling cost) answered explicitly (A52)? Options: (recommended) In the G2 plan, one row per question with the demo screen or mechanism that proves it, and a \"How it works\" page in the demo app; In the G2 plan only"
  - by: plan
    for: owner
    text: "Which intent should the 10 November demo take? Options: (recommended) both: the outcome first, then two hood beats after the lean-forward beat (How it works and the matching rules on the canvas; the assistant in the builder), since half the manager's asks are about how it works (A55 to A59); use-case: the outcome only, no hood beats; platform: 2 to 4 hood beats and a one-line description on every node and field"
  - by: plan
    for: owner
    text: "Which country is the third POC entity (the NetSuite + Creatio entity, easy landscape) in (A50)? Options: (recommended) keep it on screen as \"Country C (to be named)\" and rename it in a feedback round once the lead names it; the lead names the country now"
  - by: plan
    for: owner
    text: "Confirm the slot (A5): 10 November, 20 minutes, a UnifyApps presenter in the seat of Noventiq's group finance controller, to the group CFO office and the three country leads, as the plan assumes? Options: (recommended) yes, as planned; another audience, presenter or length (the lead names it)"
  - by: plan
    for: owner
    text: "The deck asks for a prototype on real data used by real people (A20), and privacy must be cleared before data moves (A39). For 10 November? Options: (recommended) synthetic data now, labelled as sample data; client extracts in a feedback round once privacy is cleared; hold the build for client extracts"
  - by: plan
    for: owner
    text: "The recording \"Noventiq Use Case.mov\" is still not read (Google Drive link, Drive not connected). Options: (recommended) re-upload it to #noventiq_internal or connect Google Drive so a feedback round reads it; the plan goes on meanwhile; proceed without it"
  - by: plan
    for: owner
    text: "The external step writes a DEMO-TEST task into the shared UnifyApps test Jira (project SAM1 on the existing Jira Connection) when an exception is routed to its owner. Use it? Options: (recommended) yes, labelled DEMO-TEST and listed for clean-up in the handover; skip the Jira step and route in the app only"
---

build:

## build_contract
(Nebula short spec, headings one level down; the spec file Nebula reads is $STUDIO/noventiq.md)

### Requested outcome
Noventiq's group finance controller opens one account across three CRMs, sees pipeline by group stage, service and country, and gross profit for the last four quarters with every figure cited to its source rows. A quarter close is refused until the three difficult cases (an unmatched customer, a rebate booked a quarter late, a team with missing timesheets) are fixed by their named owners. Account leads turn cited cross-sell and up-sell suggestions into action plans they can accept, edit, accelerate and roll back, and a read-only assistant answers over the same data with citations, including a change just synced from a source system.

### Touches
- object · Source record · new
- object · Sync run · new
- object · Account · new
- object · Account link · new
- object · Opportunity · new
- object · Definition · new
- object · GP line · new
- object · Period close · new
- object · Data exception · new
- object · Account play · new
- object · Play history · new
- object · Watchtower Seed snapshot · new
- automation · Noventiq Link accounts · new
- automation · Noventiq Sync source · new
- automation · Noventiq Compute GP · new
- automation · Noventiq Fix exception · new
- automation · Noventiq Route exception to Jira · new
- automation · Noventiq Update play · new
- automation · Noventiq Account facts · new
- automation · Noventiq Figure evidence · new
- automation · Noventiq Ask assistant · new
- automation · Noventiq Reset demo · new
- connection · Jira Connection · 6ababb56207d2c4e18ad380c
- ai-agent · Noventiq Finance Assistant · new
- code-app · Noventiq Watchtower · new

### Contract
#### object · Source record
The nine synthetic source systems' records, as each system holds them.
- object · create · Source record (OBJ_nq_source_record): the synthetic source systems' records, one row per record as its system holds it. Fields: system picklist creatio "Creatio", dynamics365 "Dynamics 365", blackandwhite "Black and White", netsuite "NetSuite", sapb1 "SAP B1", tally "Tally", payroll_in "Payroll India", zoho_projects "Zoho Projects", azure_devops "Azure DevOps" (required); entity picklist embee "Embee", nqai "NQ AI", entc "Entity C" (required); record_type picklist account "Account", customer "Customer", invoice "Invoice", rebate "Rebate", timesheet "Timesheet", payroll_cost "Payroll cost", ledger_gp "Ledger GP", opportunity "Opportunity", accrual "Accrual" (required); source_id text (required, unique with system); customer_ref text; customer_name text; account_key text; quarter text; service_code text; service picklist cloud "Cloud (Azure, AWS)", licensing "Software licensing", security "Cybersecurity", managed "Managed services", ai_data "AI and data"; amount_usd number; amount_local number; currency text; cost_usd number; hours number; planned_hours number; vendor text; segment text; stage_local text; earned_quarter text; attributed_quarter text; note text; last_modified datetime (epoch ms); sync_run text; pending_change boolean default false; origin picklist user "User", seed "Seed", test "Test" (default user).

#### object · Sync run
One row per sync of a source system, the trace from a figure back to when it arrived.
- object · create · Sync run (OBJ_nq_sync_run): run_id text (required, unique); system picklist (the nine Source record codes); mode picklist copy_nightly "Copy, nightly", copy_monthly "Copy, monthly", live_read "Live read", on_demand "Sync now"; started datetime (epoch ms); status picklist ok "OK", failed "Failed", running "Running"; rows_read number; rows_changed number; errors number; note text; origin picklist user, seed, test (default user).

#### object · Account
The one customer key and hierarchy across the three CRMs and ERPs.
- object · create · Account (OBJ_nq_account): account_key text (required, unique, NQ-ACC-nnnn); name text (required); entity picklist embee, nqai, entc; country text; landscape picklist easy "Easy", typical "Typical", hard "Hard"; segment picklist enterprise "Enterprise", smb "SMB"; parent_key text (the hierarchy); sources number; is_story boolean; origin picklist user, seed, test (default user).

#### object · Account link
Each source customer matched to an account key, with method and confidence.
- object · create · Account link (OBJ_nq_account_link): link_id text (required, unique); account_key text; system picklist (the nine codes); source_id text (required); source_name text; method picklist tax_id "Tax id", normalized_name "Normalised name", ai_suggested "AI suggested", manual "Manual"; confidence number; status picklist matched "Matched", needs_review "Needs review", rejected "Rejected"; confirmed_by text; origin picklist user, seed, test (default user).

#### object · Opportunity
Pipeline in the one group set of stages, with each deal's local stage and source.
- object · create · Opportunity (OBJ_nq_opportunity): opp_id text (required, unique); source_system picklist creatio, dynamics365, blackandwhite; source_id text (required); account_key text; entity picklist embee, nqai, entc; country text; title text; service picklist (the five services); stage_local text; stage_group picklist discovery "Discovery", qualified "Qualified", proposal "Proposal", negotiation "Negotiation", won "Won"; amount_usd number; close_date date (epoch ms); close_quarter text; weighted_usd number; synced_run text; origin picklist user, seed, test (default user).

#### object · Definition
The common business definitions, mappings, sync policies and their named owners.
- object · create · Definition (OBJ_nq_definition): the common business definitions, owned by Noventiq. code text (required, unique); kind picklist gp_rule "GP rule", standard_rate "Standard rate", fx "FX", match_rule "Match rule", stage_map "Stage map", service_map "Service map", sync_policy "Sync policy", exception_rule "Exception rule"; system text; local_value text; group_value text; version text; owner text (required); status picklist approved "Approved", draft "Draft"; origin picklist user, seed, test (default user).

#### object · GP line
Gross profit by quarter, entity, customer and service, with its citations.
- object · create · GP line (OBJ_nq_gp_line): line_id text (required, unique); quarter text (required); entity picklist embee, nqai, entc; country text; account_key text (UNASSIGNED when the customer has no key); service picklist (the five services); revenue_usd number; cost_of_sale_usd number; people_cost_usd number; rebate_usd number; gp_usd number; gp_pct number; rule_version text; source_ids text (semicolon list of Source record source_id values, the citation); origin picklist user, seed, test (default user).

#### object · Period close
Each quarter's tie to the ledger and its close status.
- object · create · Period close (OBJ_nq_period_close): period text (required, unique); status picklist open "Open", closed "Closed", refused "Refused"; gp_usd number; ledger_gp_usd number; difference_usd number; blocking_open number; signed_by text; signed_at date (epoch ms); last_result text; origin picklist user, seed, test (default user).

#### object · Data exception
The exceptions worklist, each traced to its system, record, sync run and owner.
- object · create · Data exception (OBJ_nq_data_exception): exception_id text (required, unique); kind picklist unmatched_customer "Unmatched customer", late_rebate "Rebate booked late", missing_timesheet "Missing timesheets", stage_conflict "Stage conflict", unmapped_service_code "Unmapped service code", sync_failed "Sync failed"; severity picklist blocking "Blocking", warning "Warning", info "Info"; status picklist open "Open", routed "Routed", fixed "Fixed"; system picklist (the nine codes); source_id text; sync_run text; rule text; owner text (required); title text; impact text; fixed_by text; fixed_at datetime (epoch ms); fix_note text; detected_at datetime (epoch ms); jira_key text; origin picklist user, seed, test (default user).

#### object · Account play
Cross-sell and up-sell suggestions and the action plans made from them.
- object · create · Account play (OBJ_nq_account_play): play_id text (required, unique); account_key text (required); kind picklist upsell "Up-sell", cross_sell "Cross-sell"; offer text; score number; value_usd number; status picklist suggested "Suggested", accepted "Accepted", accelerated "Accelerated", rolled_back "Rolled back", dismissed "Dismissed", done "Done"; owner text; evidence text; evidence_ids text; steps text (JSON list of n, step, owner, due, done); version number; ai_generated boolean; origin picklist user, seed, test (default user).

#### object · Play history
Every version of every action plan, so a change can be rolled back.
- object · create · Play history (OBJ_nq_play_history): history_id text (required, unique); play_id text (required); version number; change picklist accepted "Accepted", edited "Edited", accelerated "Accelerated", rolled_back "Rolled back"; by text; at datetime (epoch ms); note text; snapshot text (the play's steps, status and dates before the change, JSON); origin picklist user, seed, test (default user).

#### object · Watchtower Seed snapshot
The seeded values Reset demo puts back.
- object · create · Watchtower Seed snapshot (OBJ_nq_seed_snapshot): object_id text (required); row_key text (required); values text (the seeded row as JSON); written_at datetime (epoch ms). Written once by the seed tasks, read only by Noventiq Reset demo.
- record · seed · Source record: the 178 rows of `studio/data/seed/source-records.csv` (14 CRM accounts, 14 ERP customers, 77 invoices, 12 rebates, 21 timesheets, 8 payroll costs, 12 ledger GP rows, 20 opportunities), origin seed, last_modified as epoch ms.
- record · seed · Sync run: the 10 rows of `studio/data/seed/sync-runs.csv` (SR-0301 to SR-0310, SR-0310 the failed Azure DevOps run), origin seed.
- record · seed · Account: the 13 rows of `studio/data/seed/accounts.csv`, NQ-ACC-0007 Meridian Retail Group the story row, NQ-ACC-0013 Meridian Fashion its child, origin seed.
- record · seed · Account link: the 28 rows of `studio/data/seed/account-links.csv` (20 tax id, 5 normalised name, 3 AI suggested; LNK-027 BW-ACC-7731 and LNK-028 T-C-0441 needs_review), origin seed.
- record · seed · Opportunity: the 20 rows of `studio/data/seed/opportunities.csv` (OPP-003 Copilot pilot with no account key until BW-ACC-7731 is linked), origin seed.
- record · seed · Definition: the 17 rows of `studio/data/seed/definitions.csv`, origin seed.
- record · seed · GP line: the 77 rows of `studio/data/seed/gp-lines.csv` (Q4 2025 to Q3 2026; GP-077 UNASSIGNED), origin seed.
- record · seed · Period close: the 4 rows of `studio/data/seed/period-close.csv` (Q3 2026 open), origin seed.
- record · seed · Data exception: the 6 rows of `studio/data/seed/exceptions.csv` (EX-01 to EX-06, all open), origin seed.
- record · seed · Account play: the 6 rows of `studio/data/seed/account-plays.csv` (PLAY-01 the story play, suggested), ai_generated true, origin seed.
- record · seed · Play history: the 2 rows of `studio/data/seed/play-history.csv` (PLAY-02 v1 and v2), origin seed.
- record · seed · Watchtower Seed snapshot: one row per seeded row of the eleven objects above, written once after their seeds.

#### connection · Jira Connection
The existing, active Jira connection (6ababb56207d2c4e18ad380c), probed read-only on 2026-11-02 (projects KAN and SAM1); used only by Noventiq Route exception to Jira; no new connection.

#### automation · Noventiq Link accounts
Matches source customers to one account key.
- automation · create · Noventiq Link accounts: callable, mode deterministic. Input: entity (text, optional). Reads Source record rows of record_type account and customer with no matched Account link; MATCH-01 links the same tax id automatically, MATCH-02 suggests an account at name and address similarity 0.85 or more (status needs_review), below that raises an unmatched_customer Data exception. Output: linked (number), suggested (number), unmatched (number), minutes_saved (number, 12 minutes per automatic or suggested link), result `saved · error`.

#### automation · Noventiq Sync source
Copies a source system's changes into the layer and logs the run.
- automation · create · Noventiq Sync source: callable, mode deterministic. Input: system (text, required). Copies every Source record row of that system with pending_change true into the layer (Opportunity amount, stage_local and stage_group by the stage_map Definitions; GP lines through Noventiq Compute GP preview for the quarters touched), clears pending_change, writes one Sync run (mode on_demand) with rows_read and rows_changed. Output: run_id (text), rows_read (number), rows_changed (number), result `saved · error`.

#### automation · Noventiq Compute GP
Computes a quarter's GP, ties it to the ledger, and closes or refuses.
- automation · create · Noventiq Compute GP: callable, mode deterministic. Input: quarter (text, required), mode (text: preview or close, required), by (text). Recomputes the quarter's GP lines from Source records with GP-RULE v1.2 (revenue minus cost of sale minus hours times the entity's standard rate plus Microsoft rebates allocated by revenue share in the attributed quarter), writes source_ids on every line, then ties each entity to its ledger_gp row. Close refuses when any difference is not zero or a blocking Data exception of that quarter is open, and writes Period close status refused with last_result; otherwise closed, signed_by and signed_at. Output: gp_usd (number), ledger_gp_usd (number), difference_usd (number), blocking (text list of exception ids), result `closed · refused · previewed · error`.

#### automation · Noventiq Fix exception
Applies the owner's fix to an exception and recomputes what it touched.
- automation · create · Noventiq Fix exception: callable, mode deterministic. Input: exception_id (text, required), action (text: link, reattribute, accrue, map, retry), note (text, required), by (text, required). link confirms the suggested Account links and moves the customer's GP lines and opportunities to that account key; reattribute sets the rebate's attributed_quarter to its earned_quarter; accrue adds one accrual Source record for the missing hours at the standard rate; map adds a service_map Definition; retry reruns the failed system through Noventiq Sync source. Then Noventiq Compute GP preview for each quarter touched; writes status fixed, fixed_by, fixed_at, fix_note. Refuses when the exception is already fixed or the note is empty. Output: changed (text), result `fixed · already_fixed · invalid · error`.

#### automation · Noventiq Route exception to Jira
Opens a DEMO-TEST Jira task for an exception's owner.
- automation · create · Noventiq Route exception to Jira: callable, mode live, external bonus. Input: exception_id (text, required). Creates one Jira Task in project SAM1 on connection 6ababb56207d2c4e18ad380c (operation jira_create_issue), summary `DEMO-TEST 2026-11-10 <exception title>`, description with the system, source id, sync run and owner, label DEMO-TEST; writes jira_key and status routed on the Data exception. Output: jira_key (text), result `routed · error`; on error the exception keeps status open and the screen says "Jira not reached; routed in the app only".

#### automation · Noventiq Update play
Accepts, edits, accelerates or rolls back an action plan, versioned.
- automation · create · Noventiq Update play: callable, mode deterministic. Input: play_id (text, required), action (text: accept, edit, accelerate, roll_back, required), steps (text JSON, for edit), days (number, for accelerate), to_version (number, for roll_back), by (text, required), note (text). accept turns a suggestion into a plan with three steps owned by the play's owner; edit replaces the steps; accelerate brings every open step's due date forward by days; roll_back restores the snapshot of to_version. Every action first writes a Play history row with the snapshot before the change, then bumps version. Refuses roll_back to a version that does not exist and accelerate on a dismissed play. Output: version (number), status (text), result `saved · invalid · error`.

#### automation · Noventiq Account facts
The assistant's read of one account across every source.
- automation · create · Noventiq Account facts: callable, read-only, the assistant's tool. Input: account (text: key or name, required). Output: the Account row, its Account links with system and source_id, its Opportunities with stage_local, stage_group, amount_usd, source_system, source_id and synced_run, its GP lines by quarter and service with source_ids, its Account plays with evidence and evidence_ids, its open Data exceptions; result `found · not_found`.

#### automation · Noventiq Figure evidence
A financial figure with its formula and source rows.
- automation · create · Noventiq Figure evidence: callable, read-only, used by the citation drawer and the assistant. Input: line_id (text) or quarter, entity, account_key and service (text). Output: the figure (gp_usd and its parts), the formula and rule_version, every Source record behind it (system, source_id, record_type, amount_usd, amount_local, currency, last_modified, sync_run), and the ledger tie for its entity and quarter; result `found · not_found`.

#### automation · Noventiq Ask assistant
Carries a question from the app's agent drawer to the assistant and back.
- automation · create · Noventiq Ask assistant: callable, mode live. Input: question (text, required), screen (text), account_key (text), conversation_id (text). Invokes Noventiq Finance Assistant (operation ai_agents_by_unifyapps_invoke_agent) with the question and the screen and account it was asked from; answers answer (text), citations (text list of source ids with system and sync run), conversation_id (text), result `answered · error`.

#### automation · Noventiq Reset demo
Puts the demo back to its seed rows.
- automation · create · Noventiq Reset demo: callable, mode deterministic, no model call. Deletes every row whose origin is test in the eleven demo objects, puts every seed row back to its values in Watchtower Seed snapshot, never touches a user row, and answers deleted (number) and restored (number).

#### ai-agent · Noventiq Finance Assistant
The read-only assistant that answers with citations.
- ai-agent · create · Noventiq Finance Assistant: read-only, model as Nebula recommends; tools Noventiq Account facts and Noventiq Figure evidence. Instructions: answer Noventiq group finance and account leads about accounts, pipeline, gross profit, rebates, exceptions and account plays; resolve the account first through Account facts, then fetch each financial figure through Figure evidence; every number in an answer carries its citation (system, source id, sync run, rule version); say when a figure comes from a live CRM read or a nightly copy; decline salaries or any person-level payroll (payroll is visible to entitled people only and the data holds team-level cost); say the data does not hold a figure it cannot find; never write.

#### code-app · Noventiq Watchtower
The demo app: six screens on Noventiq's colour.
- code-app · create · Noventiq Watchtower: the shell: the design system stylesheet, the fonts, the rail, the header, the agent drawer, the routes for Accounts, Pipeline, Gross profit, Data health, Plays, How it works; PRIVATE
- code-app · update · Noventiq Watchtower: screen Accounts (/accounts): `.tile` row (accounts, linked records, AI-suggested matches, minutes saved), `.toolbar` with `.field` search and `.chipsel` facets entity, country, landscape, segment above a `.tbl` of Account (key, name, entity, country, sources as `.tag` per system); the account `.drawer` with `.tabs` Sources (Account links as `.tbl`, method and confidence as `.tag`, needs_review as `.tag.attention`), Pipeline, Gross profit, Plays; `.btn-s` "Run matching" · reads Account, Account link, Opportunity, GP line, Account play · calls Noventiq Link accounts on Run matching
- code-app · update · Noventiq Watchtower: screen Pipeline (/pipeline): `.stages` of the five group stages with totals; `.chart` pipeline by service and country with `.legend`; `.toolbar` facets entity, country, service, source CRM above a `.tbl` of Opportunity (title, account, stage_local beside stage_group as `.tag`, amount, weighted, close quarter, source); a `.seg` "Layer copy / Live from CRM" that reads the same deals straight from Source record; a `.note` explaining Creatio Qualified as Discovery · reads Opportunity, Source record, Definition
- code-app · update · Noventiq Watchtower: screen Gross profit (/gross-profit): `.chart` GP last four quarters with `.delta` and the ledger tie per quarter as `.tag` (positive tied, negative not tied); `.tabs` By service, By country, By customer, Rebates (Source record rebates by vendor, entity, segment, earned and booked quarter), Delivery (timesheet hours against planned, people cost at standard rate, never person-level); every figure a link to the citation `.drawer` (formula, rule version, source rows as `.tbl` with system, source id, sync run); `.ai:not(.msg)` AI Insight card (seeded) on Q3; `.btn-p` "Close Q3 2026" showing refused as `.tag.negative` and a `.note` naming the differences and blocking exceptions · reads GP line, Period close, Source record · calls Noventiq Figure evidence on a figure, Noventiq Compute GP on Close Q3 2026
- code-app · update · Noventiq Watchtower: screen Data health (/data-health): `.tabs` Exceptions, Sync runs, Source systems; Exceptions as `.toolbar` with facets kind, severity, status, system above a `.tbl` (title, system, source id, sync run, rule, owner as `.av`, severity and status as `.tag`), the exception `.drawer` with its trace (system to sync run to source record, as `.stv`), a `.fld` note and one `.btn-p` per fix action plus `.btn-s` "Route to owner in Jira"; Sync runs as `.feed`; Source systems as `.tbl` of Source record by system with an edit `.drawer` on opportunity rows (amount_usd, stage_local, sets pending_change) and `.btn-s` "Sync now" per system · reads Data exception, Sync run, Source record · calls Noventiq Fix exception on a fix action, Noventiq Route exception to Jira on Route to owner in Jira, Noventiq Sync source on Sync now
- code-app · update · Noventiq Watchtower: screen Plays (/plays): `.toolbar` facets status, kind, owner above a `.tbl` of Account play (offer, account, score, value, status as `.tag`, AI marker on suggested rows); the play `.drawer`: evidence in an `.ai:not(.msg)` card with each evidence id a citation link, steps as `.sth`, `.btn-p` "Accept as plan", `.btn-s` "Edit steps", "Accelerate 7 days", "Roll back to version", history as `.feed` of Play history · reads Account play, Play history · calls Noventiq Update play on each action, Noventiq Figure evidence on a citation
- code-app · update · Noventiq Watchtower: screen How it works (/how-it-works): `.tbl` of the six practical questions, each with its answer and the screen that proves it; `.tabs` Definitions (Definition as `.tbl` with owner and version), Data flow (sources to layer to screens and assistant, as `.stages`), Assistant context (the order the assistant reads: account, links, figures, citations); the assistant in the `.agent-drawer` on every screen with `.msg.ai` answers and citation chips · reads Definition · calls Noventiq Ask assistant on send in the agent drawer

### Rules
- theme: light · chrome: brand · surface: glass · density: comfortable · style-set: S1, set as data-theme, data-chrome, data-surface, data-density and data-style-set on `<html>`.
- stylesheet: /home/user/all-demo-foders/noventiq/noventiq/studio/design-system/noventiq/client.css, byte for byte, as app/src/styles/design-system.css.
- logo: /home/user/all-demo-foders/noventiq/noventiq/studio/design-system/noventiq/logo.svg (from noventiq.com's header), used as published in the rail's `.brand`.
- External test records are labelled DEMO-TEST with the demo date 2026-11-10.

### Business rules
- GP-RULE v1.2: GP = revenue - cost of sale - people cost (hours x the entity's standard rate) + vendor rebates allocated by revenue share; a rebate counts in the quarter it was earned.
- A quarter closes only when every entity ties to its ledger GP to the dollar and no blocking exception of that quarter is open.
- Every financial figure on screen and in an answer carries its citation: the Source record ids, their system and sync run, and the rule version.
- Month-end figures come from the nightly copy; a deal's current status and amount can be read live from the CRM (SYNC-01, SYNC-02).
- Payroll is held at team level only; no screen and no answer shows a person's pay.
- Every action-plan change writes a Play history version first, so any change can be rolled back.
- Every row carries origin: seed on seeded rows, test on rows a check or recording writes, user on rows a person makes.

### Ready when
- The story account Meridian Retail Group shows its Dynamics 365 and SAP B1 records linked and its Black and White record suggested at 0.86.
- Close Q3 2026 is refused with differences $38,400 (Embee) and $1,472 (NQ AI), and closes after EX-02 and EX-03 are fixed.
- deploy Noventiq Link accounts
- deploy Noventiq Sync source
- deploy Noventiq Compute GP
- deploy Noventiq Fix exception
- deploy Noventiq Route exception to Jira
- deploy Noventiq Update play
- deploy Noventiq Account facts
- deploy Noventiq Figure evidence
- deploy Noventiq Ask assistant
- deploy Noventiq Reset demo
- publish Noventiq Finance Assistant
- publish Noventiq Watchtower

### Assumptions
- Check this: intent proposed as both (the outcome, then how it works): two hood beats after the lean-forward beat; the owner sets it at G2.
- Check this: the demo's data is synthetic and fictional, shaped like each source system (studio/data/seed), one store for all nine synthetic systems (Source record, keyed by system and source id) rather than nine objects.
- Check this: countries are India (Embee, typical landscape; NQ AI, hard landscape) and a third country for the NetSuite and Creatio entity, shown as "Country C (to be named)" until the owner names it.
- Check this: Creatio is the name used on screen (not Cresio).
- Check this: amounts in USD; INR at 84.00 per USD, fixed for the POC; quarters are calendar quarters, Q3 2026 the one being closed.
- Check this: the brand colour is #0B408B, the navy of Noventiq's own logo; the logo's sky blue #25AADD and red #E31D22 are the other candidates.
- Check this: the external step uses the existing Jira Connection (6ababb56207d2c4e18ad380c), project SAM1, labelled DEMO-TEST; the demo stands without it.
- The cross-sell and up-sell suggestions, the AI-suggested matches and the Q3 AI Insight card are seeded with the AI marker; the assistant is the one live AI surface; every user action runs a live automation.
- The AI agent's model is Nebula's recommendation, as the profile's standing answer says.
- Noventiq Reset demo and Watchtower Seed snapshot are the demo's housekeeping: no beat shows them and no screen calls them.
- Visibility PRIVATE; publish and deploy without asking, as the profile's release line says.

## entities

## beats
Storyline: "One customer key, every number traceable to source" · 7 story beats + 2 hood beats · presenter: a UnifyApps presenter in the seat of Noventiq's group finance controller (round-2 question 1 and 2, recommended options); secondary persona the country account lead (beat 6).

Story row: Meridian Retail Group · NQ-ACC-0007 · Embee, India (typical landscape) and NQ AI, India (hard landscape) · Dynamics 365 D-ACC-1028 and SAP B1 SB1-C-1028 linked by tax id; Black and White BW-ACC-7731 "Meridian Rtl Grp" and Tally T-C-0441 suggested at 0.86 and 0.84 (EX-01) · child account Meridian Fashion NQ-ACC-0013 · open pipeline $180,000 (Azure landing zone, OPP-D-5531, Propose → Proposal) plus the unlinked $45,000 Copilot pilot (BW-OPP-118, Budget OK → Qualified) · GP Q1 2026 $37,823 (GP-029, GP-030), Q3 2026 $51,882 before the fix · Q3 2026 close: Embee +$38,400 (EX-02, REB-SB1-0912, Arjun Mehta), NQ AI +$1,472 (EX-03, ADO-TS-1042, 46 h, Neha Iyer), group GP $348,954 against ledger $309,082 · play PLAY-01 "Microsoft 365 E3 to E5 Security, 1,200 seats", score 0.82, $156,000, owner Rohan Kapoor.

1. Account view across three CRMs · route /accounts · mode live (reads; matching by Noventiq Link accounts is deterministic; the AI-suggested match rows are seeded). The presenter searches "Meridian", opens Meridian Retail Group: one key NQ-ACC-0007 with its hierarchy (Meridian Fashion), its Dynamics 365 and SAP B1 records linked by tax id, and the Black and White and Tally records waiting as AI-suggested matches at 0.86 / 0.84; the tiles show 28 links (20 by tax id, 5 by name, 3 AI-suggested) and the minutes matching saved; facets show the three entities, two countries and their easy / typical / hard landscapes; "Run matching" reruns the rules live. Asks A1, A6, A23, A35, A41, A49, A50, A55 (A19 by the tile).
2. Pipeline by stage, service and country · route /pipeline · mode live (deterministic stage mapping). The presenter shows the one group set of stages across Creatio, Dynamics 365 and Black and White; the note explains that Creatio's "Qualified" is a first call and is counted as Discovery while Dynamics 365's "Qualified" is a confirmed budget; the chart splits pipeline by service and country; the "Live from CRM" switch reads the same deals straight from the CRM records. Asks A2, A10, A24, A29 (A12 by the weighted column, A37 by the switch).
3. Gross profit, last four quarters, every number cited · route /gross-profit · mode live (reads and Noventiq Figure evidence; the AI Insight card on Q3 is seeded). The presenter shows GP Q4 2025 to Q3 2026 by service, country and customer, clicks Meridian's Q1 2026 GP of $37,823: the citation drawer shows the formula, GP-RULE v1.2 and the SAP B1 invoices and rebate behind it with their sync run. Asks A3, A4, A9, A26, A57 (A11, A13, A27, A38 by the Rebates and Delivery tabs).
4. The failure beat: Close Q3 2026 is refused · route /gross-profit · mode live (Noventiq Compute GP, close). The presenter clicks "Close Q3 2026"; the rule refuses: "Not tied to the ledger: Embee +$38,400, NQ AI +$1,472; 2 blocking exceptions open (EX-02, EX-03)", shown as a negative tag and a note. Finance's draft rule is tested and breaks where the data breaks. Asks A15, A17, A22.
5. Who fixes exceptions · route /data-health · mode live (Noventiq Fix exception; the Jira step live, external bonus). The presenter opens the exceptions worklist: each row traced to its system, source record, sync run, rule and named owner. As Arjun Mehta, re-attributes REB-SB1-0912 to Q2; as Neha Iyer, accrues the 46 missing hours at the standard rate and routes the team's follow-up to Jira (DEMO-TEST); confirms the Meridian match (EX-01), which moves $7,480 of Q3 GP and the $45,000 Copilot pilot onto Meridian. Back on Gross profit, Close Q3 2026 now closes: difference $0. Fallback for the Jira step: the exception shows "routed in the app only" and the beat goes on. Asks A16, A18, A28, A34, A36, A59.
6. Cross-sell and up-sell, as traceable action plans · route /plays · mode live (Noventiq Update play; the suggestions are seeded with the AI marker). In the account lead's seat, the presenter opens PLAY-01 on Meridian: the evidence card cites the E3 renewal (OPP-D-5408), the missing Cybersecurity line in four quarters of SAP B1 invoices and the Copilot pilot; accepts it as a three-step plan, accelerates it by 7 days, edits a step, then rolls back to version 1; the history shows every version, who and when. Asks A53, A54.
7. Lean-forward: a change in a source system reaches the cited answer · routes /data-health then the agent drawer · mode live (Noventiq Sync source, Noventiq Ask assistant, Noventiq Finance Assistant). The presenter edits the Azure landing zone in the synthetic Dynamics 365 to $210,000 at Close, clicks "Sync now": a new sync run appears with 1 row changed. In the assistant drawer types "What is Meridian Retail Group's open pipeline and Q3 GP, and where does each number come from?": the answer gives $255,000 open pipeline and Meridian's Q3 GP, each figure with its system, record id, sync run and rule version, and says the deal amount came from the sync just run. Then asks "What is each engineer on the NQ AI delivery team paid?" and the assistant declines. Asks A8, A14, A31, A51, A58 (A38 by the refusal).
   Alternatives considered: B / C. B: the action plan rolled back to version 1 with its full history (beat 6), strong for account leads but it answers only A54. C: the "minutes AI matching saved" tile after Run matching (beat 1), concrete but small on a projector. Chosen: the cited answer after a live sync, because it answers the manager's two sharpest points at once, "finance people do not trust AI without citations" and "how data updated in any system is reflected in the final response".
H1. How it works, then the matching rules on the canvas · route /how-it-works, then the automation canvas · mode live (read-only). The presenter shows the six practical questions, each answered with the screen that proved it, the Definitions tab (rules, mappings, sync policies and their named owners), then opens Noventiq Link accounts on the canvas: MATCH-01 tax id, MATCH-02 name and address 0.85, else an exception. Asks A7, A21, A25, A30, A32, A33, A52 (A55 again).
H2. The assistant in the builder · the agent builder · mode live (read-only). The presenter opens Noventiq Finance Assistant: its two tools, the order it reads (account, links, figures, citations), the instruction to cite every number and to decline person-level pay, and the model picker as an open choice of models. Asks A40, A56.

AI surfaces: Noventiq Finance Assistant · live (read-only, the one live agent) · Account play suggestions with evidence · seeded (AI marker) · AI-suggested matches in Account link · seeded (AI marker) · Q3 AI Insight card on Gross profit · seeded (AI marker) · "minutes saved" tile · deterministic (counts × 12 minutes, never presented as AI) · stage and service mapping · deterministic.

## views
- Accounts (/accounts) · beat 1 · `.app-top` with `.crumb`; `.tile` row (accounts, linked records, AI-suggested matches, minutes saved); `.toolbar` (`.field` search reporting "n of m", `.chipsel` entity, country, landscape, segment) above `.tblwrap .tbl` of Account with `.tag` per source system and `.pg`; account `.drawer.l` with `.tabs` Sources (`.tbl` of Account link, method and confidence as `.tag`, needs review `.tag.attention`), Pipeline, Gross profit, Plays; `.btn-s` Run matching with `.toast`; `.empty` states.
- Pipeline (/pipeline) · beat 2 · `.stages` of the five group stages with totals; `.chart` by service and country with `.legend`; `.seg` Layer copy / Live from CRM; `.note` on Creatio Qualified; `.toolbar` (`.field`, `.chipsel` entity, country, service, CRM) above `.tbl` of Opportunity (local stage beside group stage as `.tag`, amount, weighted, close quarter, source).
- Gross profit (/gross-profit) · beats 3, 4, 5 · `.chart` four quarters with `.delta` and a tie `.tag` per quarter; `.ai:not(.msg)` AI Insight card (seeded) on Q3; `.tabs` By service, By country, By customer, Rebates, Delivery, each a `.toolbar` + `.tbl`; citation `.drawer` (formula, rule version, `.tbl` of source rows with system, source id, sync run); `.btn-p` Close Q3 2026 with the refusal as `.tag.negative` and `.note`, the close as `.tag.positive`.
- Data health (/data-health) · beats 5, 7 · `.tabs` Exceptions, Sync runs, Source systems; Exceptions `.toolbar` (`.chipsel` kind, severity, status, system) above `.tbl` with owner `.av` and `.tag` severity and status; exception `.drawer` with the trace as `.stv` (system → sync run → source record → rule → owner), `.fld` note, one `.btn-p` per fix, `.btn-s` Route to owner in Jira; Sync runs as `.feed`; Source systems `.tbl` by system with edit `.drawer` (`.fld` amount, stage) and `.btn-s` Sync now.
- Plays (/plays) · beat 6 · `.toolbar` (`.chipsel` status, kind, owner) above `.tbl` of Account play with score and status `.tag`; play `.drawer` with the evidence in `.ai:not(.msg)` and citation links, steps as `.sth`, `.btn-p` Accept as plan, `.btn-s` Edit steps, Accelerate 7 days, Roll back to version (`.modal.s` to pick it), history as `.feed`.
- How it works (/how-it-works) · beat H1 · `.tbl` of the six practical questions (question, answer, the screen that proves it); `.tabs` Definitions (`.tbl` with owner `.av` and version), Data flow (`.stages` sources → layer → screens and assistant), Assistant context (`.stv` of what it reads, in order).
- Agent drawer (every screen) · beat 7, H2 · `.agent-launch` and `.agent-drawer` (`.ad-hd`, `.ad-ctx` naming the screen and account, `.ad-thread` of `.msg.me` / `.msg.ai` with citation `.chips`, `.ad-composer`).
