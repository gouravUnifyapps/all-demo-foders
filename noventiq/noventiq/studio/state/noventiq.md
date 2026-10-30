---
use_case: Noventiq
client: Noventiq
poc_row: POC-noventiq-noventiq-20261026
owner: Gourav Mahunta · U09EK0B6NKD
manager: Mrinal Dixit · U08LPV6J011
status: awaiting_g1
version: 1 · since 2026-10-26T13:19:06Z
channel: C0CBYSL95UK
threads:
  g1: 1793021406.071119
  g2:
  g3:
  g4:
intent:
stage_flag:

gates:
  g1: {status: waiting, round: 2, posted_ts: 1793021406.071119, decided_by: , decided_at: }
  g2: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
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

coverage: []

size:

data:

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
dev_issues: []

frozen:

cost:
  runs: 2
  agent_spawns: 2
  tokens_m: 0.31
  wall_h: 0.53

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
---

build:

## build_contract

## entities

## beats

## views
