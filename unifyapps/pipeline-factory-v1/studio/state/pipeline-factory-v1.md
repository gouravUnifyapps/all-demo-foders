---
use_case: Pipeline Factory v1
client: UnifyApps
poc_row: POC-unifyapps-pipeline-factory-v1-20261031
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g2
version: 1 · since 2026-10-31T10:16:23Z
channel: C0CDB92FALX
threads:
  g1: 1793442419.752669
  g2: 1793522055.329009
  g3:
  g4:
  connections:
intent:
stage_flag:

gates:
  g1: {status: approved, round: 1, posted_ts: 1793442419.752669, decided_by: Gourav Mahunta (row), decided_at: 2026-11-01T08:11:55Z}
  g2: {status: waiting, round: 1, posted_ts: 1793522055.329009, decided_by: , decided_at: }
  connections: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: , list: []}
  g3: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
  g4: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }

posts:
  - when: 2026-10-31T10:26:47Z
    kind: g1
    ts: 1793442419.752669
    by: bot
    version: 1
    round: 1
    documents:
      - {name: Requirements · Pipeline Factory v1, type: requirements, file_url: https://orbit.uat.unifyapps.com/auth/file/asset/download/3e8e757cdbfeadc3279a5593, file_name: requirements-v1-r1.pdf, file_size: 533280}
  - when: 2026-11-01T08:34:02Z
    kind: g2
    ts: 1793522055.329009
    by: bot
    version: 1
    round: 1
    documents:
      - {name: Plan · Pipeline Factory v1, type: scope, file_url: https://orbit.uat.unifyapps.com/auth/file/asset/download/a788b16b901b736c5329b94c, file_name: plan-v1-r1.pdf, file_size: 416152}
  - when: 2026-11-01T08:34:32Z
    kind: status
    ts: 1793522055.329009
    by: bot
    version: 1
    round: 1
runs:
  - started: 2026-10-31T10:16:23Z
    ended: 2026-10-31T10:26:47Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 160
    outcome: posted G1
  - started: 2026-11-01T08:14:39Z
    ended: 2026-11-01T08:34:02Z
    gate: g2
    stages: [2-plan]
    spawns: 1
    tokens: 256364
    outcome: posted G2

stopped:

asks:
  - id: A1
    text: "The Pipeline Factory is 38 single-job agents and 12 deterministic workflows, built on the UnifyApps Solution Builder and connected only through the enterprise context graph. This spec covers how they connect, what each one does and what it plugs into, and how to build each one."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § Pipeline Factory: Engineering Build Spec · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A2
    text: "The dashed fast lane lets a strong signal skip the daily batch and start a play within the hour."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A3
    text: "The left line is the learning loop: outcomes from sub-workflow 8 return as proposed weights (to 1 and 2), best examples and test variants (to 5), and objections (to 6), applied only after the Quality Grader and the Friday review."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A4
    text: "Why: every hand-off can then be seen in the control towers, checked by the Quality Grader, and stopped by a person."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A5
    text: "Registered. A hand-off not in the Hand-off register below does not exist."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A6
    text: "One writer per field. Only the component named in the register writes a field; everyone else reads."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A7
    text: "Schema check on save. A record that fails its JSON schema is rejected, the GTM engineer is alerted, and the downstream step waits. Never substitute generic copy."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A8
    text: "Confidence gate. A record below the component's threshold does not flow on; it goes to the named person's to-do list (thresholds are in each sub-workflow table)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A9
    text: "Idempotent. Every save is keyed on account_id + person_id + play_id. Re-running a hand-off never creates a second copy or a second enrolment."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A10
    text: "On time. Each hand-off has a \"When\". A late one retries, then counts against the component's success rate (target 99%, red under 97%)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A11
    text: "Traced. Every run logs input, output, model, confidence, cost and latency, keyed by patch_id. Failures show in the control towers with their cause."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A12
    text: "Patch-keyed. Every record carries its patch_id and the sender's confidence score."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A13
    text: "Model split: two AI model families. Every checker (Fact Checker, Message Grader, Reply Sorter, Meeting Labeler, Deal Qualifier, Quality Grader) runs on a different family from the drafter it checks. Each run has a cost cap, plus a daily spend cap."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A14
    text: "Locked fields: Patch ID, BDR of record, meeting type, meeting source, factory-sourced, factory-influenced and marketing-influenced are written only by workflows and lock at booking. Corrections go through RevOps, logged with a reason."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A15
    text: "Keeps every patch's named accounts clean, scored, in the right patch and current."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 1. Patch accounts · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A16
    text: "Every 15 min pulls new and changed records, normalises keys (domain, legal name, LinkedIn ID, HubSpot ID, email), merges exact matches and scores near-matches 0–100. ≥95 merge; 80–95 to RevOps; <80 kept separate. Logs its reasoning"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Duplicate Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A17
    text: "Links each company to parent, subsidiaries, divisions; proposes divisions that buy separately (RevOps approves); sets the outreach lock at the top parent. Re-links on HQ change or M&A news. <80 → RevOps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Parent Company Linker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A18
    text: "Finds the parent's HQ city, state, country; weighs sources; returns location, confidence, other candidates and evidence. <80 → RevOps picks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Headquarters Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A19
    text: "Nightly on companies with move or M&A news, quarterly on all. Any change → alert in the patch control tower, then a new Patch Suggester proposal"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Headquarters Re-checker (monitor)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A20
    text: "Weekly closed-won lookalikes; daily checks 7 other sources (ecosystem lists, intent surges, web visitors, business units, champion job changes, event attendees, renewal windows). Drops fit <36, customers, open deals, partners, competitors, DNC. Suggests to RevOps, never adds. <70 not suggested"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “New Account Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A21
    text: "Scores fit out of 60 (up to 15 each: industry, size and complexity, core systems, AI and integration maturity); maps score + ICP V2 quadrant to best / medium / low fit. Floor 36 never moves. Re-scores on change and monthly. <70 → RevOps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Fit Scorer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A22
    text: "Proposes a patch for each new account or HQ change: geography first, then industry, with confidence and reason. Never writes a Patch ID. <80 → RevOps decides from evidence"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Patch Suggester”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A23
    text: "Finds integration, automation and agent tools each best/medium-fit account uses, from vendor case studies, job posts, procurement notices. Weekly. <60 tagged [HYPOTHESIS]"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Current Vendor Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A24
    text: "Estimates renewal as 3 years from earliest evidence unless a later contract signal exists; raises a renewal signal 9 months before. <60 no signal"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Renewal Date Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A25
    text: "Drafts battlecard changes per vendor: shortfalls, switch path, proof, objection answers. Product marketing approves each"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Battlecard Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A26
    text: "Reused, not built: Patch Mapper (Atomic Patch View) stamps patch_id on every account, person and dollar nightly, flags orphans, never moves an account. Gate 1 refuses any account without a Patch ID."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 1. Patch accounts · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Atomic Patch View"
    status: out_of_scope
  - id: A27
    text: "Decides which patch accounts start a play now. Strong signals start a play within the hour; the rest of each patch's slots fill every morning from its ranked list."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 2. Account selection · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A28
    text: "Watches continuously: web visits and intent, Bombora surges, Sales Navigator alerts, hiring and tech changes, job changes, leadership news, earnings calls, press, renewal signals, event sign-ups. Records company, type, date, source link, strength; verifies company match and date; scores confidence. Strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) go straight to the Play Picker. <70 logged, not scored. Signals fade over 30 days"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Buying Signal Spotter”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A29
    text: "Turns signals into a timing score (max 40) with the weights below. Monday 06:00 ranks each patch by fit + timing. Daily 07:00 tops up each patch's batch after fast-lane plays and sends it to Gate 1 with each account's top 3 signals. Applies the checked-visit rule"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Account Ranking (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A30
    text: "Monday after ranking: base 25 slots per patch; never more than eligible accounts ÷ 13; floor 15, cap 40; pace boost (up to +50%) only to patches behind on intro meetings whose diagnosis stops at Input or Engagement and whose AE has <6 intros booked in 7 days. Fast-lane plays use their own patch's slots; overflow takes spare capacity, then that patch's lowest-ranked accounts, never another patch's base. AE nominations (max 3/week) start inside their patch's slots. Logs every allocation"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Weekly Slot Planner (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A31
    text: "After allocation, randomly holds back 10% of each patch's new medium/low-fit plays with a logged weekly seed. Checks treated vs held-out balance on fit and timing (standardised difference <0.1) or redraws. Flags held accounts in graph and HubSpot with a 90-day end date. Reports at 90 and 180 days"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Holdout Picker (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A32
    text: "Batch lands in the BDR's to-do list at 07:00 with fit band, timing, top 3 signals, Patch ID, AE, last touch, slots left. Accept or reject by 10:00 with one reason (bad fit, active deal, wrong timing, already in conversation). A rejected slot refills from the same patch. Hard blocks: no Patch ID / AE / pod, on an AE hold, or held out"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Gate 1 (human: pod BDR)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A33
    text: "Starting signal weights (Scoring Tuner updates monthly): checked pricing/product visits (2+ in 14 days) 25 · new CIO/CTO/CDO/CAIO/Head of AI in 90 days 20 · event or webinar attendance 20 · hiring for AI platform, automation, integration roles 15 · earnings naming AI, automation, modernisation or cost-cutting 15 · Bombora surge 15 · interest in a current vendor's tool 15 · vendor renewal within 9 months 15 · funding, merger or new market 10 · executive posts on AI programs 10."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 2. Account selection · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A34
    text: "Checked visit: counts only with 10+ seconds and a scroll, or a repeat visit within 7 days. Never counts visits within 2 minutes of an email's delivery, from security-scanner networks, or with no page interaction."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 2. Account selection · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A35
    text: "Keeps a sourced view of every patch account current: best fit refreshed every 30 days, others every 90, and on new filings or press. Runs on Day 1 in parallel with the buying committee."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 3. Account research · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A36
    text: "Reads the latest annual report and investor deck, last two earnings call transcripts, 12 months of press, current AI/IT/automation job posts. Extracts statements on AI, automation, integration, modernisation, cost, CX, risk. Each fact keeps exact quote, page or timestamp, date, link. Drops anything >12 months old (except the latest annual report). Facts without quote + link are rejected"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 3. Account research › table row “Company Facts Collector”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A37
    text: "Finds candidate VEP-CFC use cases for the industry and core systems; scores evidence; keeps the top 3 with two supporting facts (or one fact + the company's engagement with us); tags each with pattern and outcome. <70 shown only as a question, never a claim"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 3. Account research › table row “Use Case Matcher”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A38
    text: "Writes: business problem in the company's own words, impact (no dollar figures), why now (top signals), why UnifyApps (use case + their core systems), closest proof, main and backup angle, risks (e.g. vendor contract). Every sentence cites a fact or is tagged [HYPOTHESIS]. <70 → BDR reviews at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 3. Account research › table row “Case for Change Drafter”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A39
    text: "Rules: VEP-CFC is the only source of use cases (UC-ID + Blueprint link + account evidence). Guesses are tagged [HYPOTHESIS] and reach prospects only as questions. Conflicting sources are shown side by side, never settled by the agent. Two rule steps also run here: a graph query pulling past contact (events, downloads, visits, calls, past deals, loss reasons), and an account tagger (vertical, Patch ID, size, systems, vendors, AI maturity, fit band, pattern, outcome)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 3. Account research · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A40
    text: "Maps 12 people per account, writes a note on each, gets verified contact details, screens them, and looks for a warm intro before anything goes cold."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 4. Buying committee · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A41
    text: "Loads the industry's default titles plus BDR edits; searches people at the company and division; assigns role (economic buyer, champion, technical evaluator, business owner, gatekeeper); checks the champions library; picks 3 Tier 1, 3 Tier 2, 4 Tier 3, 2 backups; flags the economic buyer. Gatekeepers mapped, never contacted. Job-change alerts promote a backup; a title the BDR removes 3× in an industry drops from its defaults. <70 on a role → BDR checks at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Buying Team Mapper”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A42
    text: "Four-line note per person: role, time in role, past companies, public talks and posts; what they own ([HYPOTHESIS] unless public); link to the matched use case; past touches; nearby event fit. Professional info only. Refresh every 90 days and on job change. <70 flagged at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Person Notes Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A43
    text: "For Tier 1 at best-fit accounts: finds shared work history with customer execs, partners, employees and AEs; uses opt-in LinkedIn connection exports (monthly) plus partners, SIs, investors. Ranks: worked together > overlapped > friend of a friend. Drafts the intro request into the patch AE's to-do list and holds cold touches to that person 7 days. <60 not suggested"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Intro Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A44
    text: "Sends each person to the Sprouts plugin → verified work email, plus phone for Tier 1 and engaged people. No verified email → LinkedIn only. Saves with source and verify date to graph and HubSpot; re-verifies emails older than 90 days before use"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Contact Finder (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A45
    text: "One suppression list (opt-outs, bounces, complaints, legal holds); copies it to HubSpot, Apollo and Sprouts every 15 min; screens every phone against federal and state DNC before any dialler; records consent per person; completes erasure across all tools within 30 days, keeping only a hashed code so the person is never re-added"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Do-Not-Contact List (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A46
    text: "Best-fit accounts reach the AE's to-do list on Day 1 with account view and buying team (~5/week/patch). Approve, adjust or disqualify by Day 2 12:00; else backup AE, then Geo leader, before Gate 2 closes"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “AE checkpoint (human: patch AE, best fit only)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A47
    text: "Picks the play, builds the account's Art of the Possible page, writes every touch, checks it, and holds it for the BDR at Gate 2. Runs on Day 2; nothing sends until Gate 2 clears."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 5. Outreach drafting · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A48
    text: "Matches the signal (or the 13-week cycle) to a play; sets people, channels, start days; spaces tiers so no two people at one account get email the same day; picks senders only from the account's patch and pod (AE for Tier 1 LinkedIn and AE notes, BDR for the rest, executive sponsor for C-level). Also receives fast-lane signals. <70 → BDR picks at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Play Picker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A49
    text: "Builds one Art of the Possible page per account: operations from public facts only, 2–3 workflows reimagined (before/after) for the matched use cases, proof, how UnifyApps connects their core systems, a patch event. Button books a 60-min session with the patch AE + solution consultant. Fills marketing's locked template; page is noindex, at a hard-to-guess URL, with a tracked link per prospect. <75 → marketing ops checks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Page Builder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A50
    text: "Picks one Content Factory asset per asset touch, matched on role, industry, use case, pattern, outcome, VEP stage, Geo; skips assets >18 months old or retired; ranks by fit and positive-reply history for that role; never the same asset to two people at one account in a week; adds an event only while seats remain. <70 → no asset, use a sourced insight"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Content Picker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A51
    text: "Writes every email and LinkedIn message in the play. Starts from the Content Factory's best message for category → sub-sector → company → persona and must agree with all four; uses the assigned handbook voice; one sourced fact, the pain this person owns, the likeliest objection for their role. Names the patch AE as session host. Pod-inbox emails in the BDR's name; AE notes from the AE's mailbox, warm plays only. <70 flagged at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Message Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A52
    text: "Traces every claim in drafts and pages: facts to a public source ≤12 months old, numbers to a source or the proof library, use cases to a UC-ID with account evidence. Blocks anything untraceable"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Fact Checker (checker, other model family)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A53
    text: "Scores each draft 0–100 on the message rubric: teaches something, relevant to role and company, actionable, applies to their business, well written in the right voice, follows copy rules. <75 → one automatic rewrite and regrade; <75 again → a person decides at Gate 2. Rubric weights checked monthly against replies"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Message Grader (checker, other model family)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A54
    text: "Blocks any draft that fails: clean text (no empty fields, wrong names incl. the AE's); person still in role (checked within 7 days of first send); not on DNC, held out, a customer or open deal; parent outreach lock owned by this owner; Patch ID, AE, pod present and no AE hold; sender from the account's pod and under their daily limit across all pods; person not in another sequence; state send window, consent, legal footer"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Send Rules Check (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A55
    text: "One screen per account: account view, buying team, page preview, every draft with grade, fact and rule results (~5% carry planted test errors that never send). BDR approves, edits, swaps a person or holds, by 17:00 Day 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Gate 2 (human: pod BDR)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A56
    text: "Copy rules the Message Writer enforces: subject 3–6 words built on the prospect's trigger; emails 90–120 words; connection notes <250 characters; open on the business problem, not AI; one insight + one question; guesses only as questions; no em dashes, placeholders or invented statistics; goodbye notes say we won't reach out for a while."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 5. Outreach drafting · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A57
    text: "Baseline sequence (Tier 2 starts 2 days after Tier 1, Tier 3 two days after that; Tier 1 gets email, LinkedIn, call; Tier 2 email, LinkedIn; Tier 3 email only):"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 5. Outreach drafting · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A58
    text: "Sends every approved touch on Day 3 in the prospect's local morning: email and calls through Apollo, LinkedIn through the Sprouts plugin. Re-plans the account as people respond and protects the inboxes."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 6. Outreach · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A59
    text: "Puts each approved person into channels: email steps into an Apollo sequence on the assigned inbox, LinkedIn steps into the sender's Sprouts queue, calls as Apollo call tasks. Schedules in the prospect's local morning and state window, keeping tier spacing. Holds every inbox and LinkedIn sender at 70% of daily limit. Writes owner, Patch ID, BDR of record, sequence status, tasks, notes to HubSpot; sets the parent outreach lock. Every write keyed on person + play (no double enrolment)"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Outreach Launcher (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A60
    text: "For each call task (Tier 1 day 6, Hot Visit, anyone engaged): adapts the BDR's best script or builds one from top Gong calls; writes signal-tied opener, permission question, 3–5 discovery questions, top 3 objection answers, 20-second voicemail, follow-up email draft. Orders each BDR's call list by interest inside each patch's time-zone block. <70 → BDR approves the script"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Call Script Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A61
    text: "Keeps the account one conversation once anyone responds: a referral becomes the lead thread; a Tier 1 objection pauses Tiers 2–3 and gives the AE an answer note; 2+ people engaging in 7 days switches to Committee Surge. Every rewrite goes back through Fact Checker and Message Grader. <70 → BDR decides"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Follow-up Planner”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A62
    text: "Weekly inbox-placement tests per active domain (Gmail, Outlook, Microsoft, Barracuda, Proofpoint); daily blacklist and Gmail reputation checks; reply rate by recipient provider; maintains the email-security-scanner list. Every alert to the BDR and GTM engineer"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Inbox Health Checker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A63
    text: "Rests a domain the same day if placement <70% in two tests or it hits a major blacklist, and swaps in a warmed spare. Blocks a new BDR's first send until their domains pass. Previously blacklisted domains are retired"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Email Domain Swapper (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A64
    text: "LinkedIn bans third-party automation, so people send. Each opens their Sprouts queue (messages pre-written and checked), reviews and sends from their own account. AE ~20 requests/day for own patch. A restriction warning → stop and report; tower pauses that sender. Unsent AE messages move to the BDR at day end"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “LinkedIn senders (human: AEs, BDR, exec sponsor)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A65
    text: "Sending limits: each BDR sends on 16 inboxes across 4 UnifyApps-branded secondary domains, ≤40 emails per inbox per day, with 2 warm spare domains (8 inboxes). SPF, DKIM, DMARC and one-click unsubscribe on every domain. New inboxes ramp 10/20/30/40 per day over 4 weeks. LinkedIn: ≤22 connection requests per person per day across all pods. One stop signal: a reply in Apollo or Sprouts stops every channel for that person in both tools within minutes."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 6. Outreach · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A66
    text: "Handles replies, books and hands off meetings, and labels and qualifies them. Engage = a reply becomes an intro meeting; Connect = an intro becomes a New Buyer Meeting; Commit = a qualified opportunity."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 7. Engage, Connect and Commit · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A67
    text: "Watches every pod inbox (Apollo) and LinkedIn reply (Sprouts); classifies into 9 types: positive, referral, not now (with date), objection, wrong person, out of office, unsubscribe, bounce, auto-reply. Stops all channels for that person in both tools and tells the Follow-up Planner. Handles mechanical types itself: OOO moves the next touch to the return date; unsubscribe to DNC within 15 min; bounce triggers re-check + backup person; \"not now\" to Content Handoff. <90 on unsubscribe → treated as unsubscribe; <80 on anything else → a person sorts it"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Reply Sorter (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A68
    text: "Drafts the answer from the thread, account view, objection list and the AE's booking link; puts it with confidence in the BDR's to-do list (and the AE's for positive replies at best-fit accounts). The person sends, edits, adds a booking link, hands to the AE, or snoozes, from one screen; it goes out from the original thread. Reminder at 90 min; Geo leader alerted at 2 business hours. <70 marked for full rewrite"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Reply Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A69
    text: "On booking via the AE's link: creates the deal at Engage owned by the patch AE; picks up meetings booked elsewhere from the AE's Google Calendar within 15 min. Locks Patch ID, BDR of record, meeting source, factory-sourced, factory-influenced (a rejected meeting rebooked within 30 days keeps its source). Books the SC, triggers the prep pack, sends agenda and 24h/1h reminders, runs a 2-touch reschedule on no-show. Runs AE deadlines (below) and escalations"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Meeting Handoff and Deadlines (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A70
    text: "Builds the pack for AE and SC: account view, buying team, thread, Case for Change draft, likely objections, AotP page, questions to confirm economic buyer and timeline. Delivered into the AE's AI Twin, which then tracks promises made on the call"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Meeting Prep Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A71
    text: "Reads transcript, attendees, economic-buyer flag; labels intro / New Buyer Meeting / doesn't count, quoting evidence. Doesn't count if <20 min, no Tier 1–2 attendee, a reschedule, or a second intro at the account within 90 days. Unrecorded meetings labelled from calendar attendees and AE notes and marked unrecorded. <80 → Geo leader checks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Meeting Labeler (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A72
    text: "After each New Buyer Meeting checks six requirements: fit 36+, a VEP-CFC pain, engaged champion, New Buyer Meeting held, timeline ≤12 months, scheduled mutual next step. Marks each met / partly / missing with transcript quotes; lists gaps with the question that closes each; drafts the recap; recommends Qualified only when all are met. Saves won/lost outcomes and reasons to the graph. <80 → recommended not qualified, with gaps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Deal Qualifier (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A73
    text: "AE confirms meeting label and stage within 2 business days; deal moves to Commit"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “AE confirm (human)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A74
    text: "Deadlines the workflow enforces (AE's business hours; reminder at half-window, escalation on miss): accept or reject a meeting within 1 business day (else Geo leader in 4h or backup AE takes it) · decide within 2 business days of every held meeting · stale after 5 idle business days at Engage · alert at 30 days in Connect, 45 days in Commit without a next step · one stage at a time, only with exit fields filled."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 7. Engage, Connect and Commit · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A75
    text: "Learns from every outcome, grades every agent, and turns red lines into actions. Learning agents only propose; the Quality Grader checks each proposal and the Friday review approves. Only weight changes within ±20% apply on their own, after 8 weeks without a drop."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 8. Learning and governance · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A76
    text: "Every touch is saved with its result: patch, signal, play, persona, tier, use case, pattern, outcome, subject, asset, sender, send time → reply type, meeting label, qualified, won/lost, deal size."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 8. Learning and governance · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A77
    text: "Weekly: promotes messages with 3+ positive replies into the Message Writer's examples for that role and industry; shares them with the Content Factory. <3 positives → not promoted"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Winning Message Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A78
    text: "Monthly: re-fits fit and signal weights to meetings and qualified opportunities, learning from Gate 1 rejections, AE-rejected meetings, disqualifications, win/loss reasons. Learns across all patches, reports per patch. Proposals only"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Scoring Tuner”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A79
    text: "Updates the objection list and buyer language from call transcripts. <70 → sales reviews"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Objection Collector”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A80
    text: "Small changes (subject, opener, asset): continuous tests on positive replies, ≥20% traffic per version, 4-week limit. Bold changes: fixed-size tests on people (5%→8% reply needs ~1,060 people per version). Never tests one-point lifts"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “A/B Tester”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A81
    text: "Holds every agent's rubric and test set; runs them on every prompt, model or weight change and blocks a release on any drop. Enforces checker-on-other-model. Computes each gate's rung weekly per pod and AE. Drafts a policy when the same exception is resolved the same way 3 times"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Quality Grader (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A82
    text: "Weekly: compares each agent to its baseline on block/edit rate, factual errors, grades, confidence calibration; alerts the GTM engineer on any slip"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Agent Monitor”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A83
    text: "Plants errors (e.g. wrong patch AE, sender from wrong pod) in ~5% of Gate 2 items, which never send; scores each reviewer's catch rate"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Test Error Planter”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A84
    text: "Every 15 min reads tower metrics; on a red line takes the listed action (pause, throttle, move slots, demote a gate, add a to-do item); escalates unfixed alarms patch → pod (2 business days) → Geo (5) → CRO. Logs before/after numbers. Safety actions are automatic; resuming or moving anyone's work needs a person"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Alarm and Escalation (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A85
    text: "Monday: pushes accounts in play to LinkedIn ad audiences by patch geography for 8 weeks; passes unreached people to the Content Factory (ads and content only, never cold email); moves \"not now\" and engaged prospects to nurture until their date; sets marketing_influenced; sends asset, message and pattern results by patch weekly"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Content Handoff (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A86
    text: "Recording consent per state; DNC checks; state legal checklists (send window, consent, footer); erasure across every tool within 30 days; 12-month clean-up of people who never engaged"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Privacy and Consent (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A87
    text: "Reused from the Atomic Patch View: Pipeline Analyst (pipeline signals), Patch Brief Agent (patch briefs, draft only), My 4P Coach (seller next steps, incl. factory replies, approvals and tasks)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 8. Learning and governance · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "other: Atomic Patch View"
    status: out_of_scope
  - id: A88
    text: "Every agent goes through these ten steps on the Solution Builder; deterministic workflows skip steps 5–8 and instead need a fixed test set that passes in full."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A89
    text: "Register first. Search the master registry; reuse if it exists, else register with plain name, owner and parent workflow to get its ID."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A90
    text: "One job. If the job description needs \"and\", it is two agents."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A91
    text: "Connect. Context graph plus only the connectors that one job needs."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A92
    text: "Contract. Output is a JSON schema that includes confidence (0–100) and the evidence behind it. Output failing the schema is rejected."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A93
    text: "Rubric. Publish the evaluation rubric in the registry: criteria, weights, good and bad examples."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A94
    text: "Knowledge. Attach only the handbook sections the job needs."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A95
    text: "Guardrails. Confidence threshold (below it → named person's to-do list); per-run cost cap; checker on a different model family."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A96
    text: "Monitor. Anything the agent produces that can go stale gets a monitor agent on a schedule that alerts the patch control tower on change."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A97
    text: "Evaluate. Score at least 50 real past items on the rubric. The Quality Grader sets the pass mark; no release below it."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A98
    text: "Shadow, then release. One week on live inputs with no side effects, then release at Rung 1. Traces, confidence, cost and errors stream to the control towers."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps › ten steps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A99
    text: "Every fact in the graph carries source, date, evidence tag ([PUBLIC] or [HYPOTHESIS]), the writing agent and its confidence. Views (account cards, committee maps, patch views) are live queries over the graph, not stored documents."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How to build each agent on UnifyApps · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A100
    text: "HubSpot is the system of record; Apollo is the only email sequencer and dialler; the Sprouts plugin is the only LinkedIn and contact-data tool. Give each connector only the access its agents need."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § Tools to connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A101
    text: "Create these HubSpot fields first (workflow-written only): patch_id, pod, owner_ae, backup_ae, ultimate_parent_lock, factory_holdout, factory_holdout_until, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced, value_pattern."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § Tools to connect · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A102
    text: "Do not connect: LinkedIn scrapers or any LinkedIn tool other than the Sprouts plugin (LinkedIn bans third-party automation); mirror profiles; a third outreach tool or second dialler (it would split reply detection and the DNC list)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § Tools to connect · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A103
    text: "Every agent hands off through the context graph, never directly"
    source: "image1.png inside Pipeline-Factory-Engineering-Build.docx (image text; Slack file F0CDQM8HAVC, posted by Gourav Mahunta in #pipeline-factory-v1) · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open
  - id: A104
    text: "Each hand-off is a saved record: schema-checked, confidence-scored, keyed by Patch ID"
    source: "image1.png inside Pipeline-Factory-Engineering-Build.docx (image text; Slack file F0CDQM8HAVC, posted by Gourav Mahunta in #pipeline-factory-v1) · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: open

coverage:
  - ask: A1
    by: beat 1
  - ask: A2
    by: beat 2
  - ask: A3
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A4
    by: beat 1
  - ask: A5
    by: beat H1
  - ask: A6
    by: beat H1
  - ask: A7
    by: beat H1
  - ask: A8
    by: beat 3
  - ask: A9
    by: beat 5
  - ask: A10
    by: beat 1
  - ask: A11
    by: beat 1
  - ask: A12
    by: beat 1
  - ask: A13
    by: control Components tab, model family and checks columns, on Control tower
  - ask: A14
    by: beat 6
  - ask: A15
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A16
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A17
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A18
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A19
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A20
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A21
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A22
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A23
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A24
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A25
    by: control Components tab, facet sub-workflow 1, on Control tower
  - ask: A27
    by: beat 1
  - ask: A28
    by: beat 2
  - ask: A29
    by: beat 2
  - ask: A30
    by: beat 3
  - ask: A31
    by: beat 3
  - ask: A32
    by: beat 3
  - ask: A33
    by: beat 2
  - ask: A34
    by: beat 2
  - ask: A35
    by: beat 4
  - ask: A36
    by: beat 4
  - ask: A37
    by: beat 4
  - ask: A38
    by: beat 4
  - ask: A39
    by: beat 4
  - ask: A40
    by: beat 4
  - ask: A41
    by: beat 4
  - ask: A42
    by: beat 4
  - ask: A43
    by: control Components tab, facet sub-workflow 4, on Control tower
  - ask: A44
    by: control Components tab, facet sub-workflow 4, on Control tower
  - ask: A45
    by: control Components tab, facet sub-workflow 4, on Control tower
  - ask: A46
    by: control Components tab, facet sub-workflow 4, on Control tower
  - ask: A47
    by: beat 5
  - ask: A48
    by: beat 2
  - ask: A49
    by: control Components tab, facet sub-workflow 5, on Control tower
  - ask: A50
    by: control Components tab, facet sub-workflow 5, on Control tower
  - ask: A51
    by: beat 5
  - ask: A52
    by: beat 5
  - ask: A53
    by: beat 5
  - ask: A54
    by: beat 5
  - ask: A55
    by: beat 5
  - ask: A56
    by: beat 5
  - ask: A57
    by: control Components tab, row Outreach Launcher (tier spacing), on Control tower
  - ask: A58
    by: control Components tab, row Outreach Launcher (tier spacing), on Control tower
  - ask: A59
    by: beat 5
  - ask: A60
    by: control Components tab, facet sub-workflow 6, on Control tower
  - ask: A61
    by: control Components tab, facet sub-workflow 6, on Control tower
  - ask: A62
    by: control Components tab, facet sub-workflow 6, on Control tower
  - ask: A63
    by: control Components tab, facet sub-workflow 6, on Control tower
  - ask: A64
    by: control Components tab, facet sub-workflow 6, on Control tower
  - ask: A65
    by: open question 4
  - ask: A66
    by: beat 6
  - ask: A67
    by: control Components tab, facet sub-workflow 7, on Control tower
  - ask: A68
    by: control Components tab, facet sub-workflow 7, on Control tower
  - ask: A69
    by: beat 6
  - ask: A70
    by: control Components tab, facet sub-workflow 7, on Control tower
  - ask: A71
    by: beat 6
  - ask: A72
    by: beat 6
  - ask: A73
    by: beat 6
  - ask: A74
    by: beat 6
  - ask: A75
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A76
    by: control Hand-offs tab, record drawer (payload and evidence), on Control tower
  - ask: A77
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A78
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A79
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A80
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A81
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A82
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A83
    by: beat 5
  - ask: A84
    by: beat 7
  - ask: A85
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A86
    by: control Components tab, facet sub-workflow 8 (feeds column), on Control tower
  - ask: A88
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A89
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A90
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A91
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A92
    by: beat H1
  - ask: A93
    by: open question 2
  - ask: A94
    by: open question 2
  - ask: A95
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A96
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A97
    by: open question 2
  - ask: A98
    by: control Components tab columns (registered, one job, feeds, threshold, monitor rows, status shadow or live), on Control tower
  - ask: A99
    by: beat 4
  - ask: A100
    by: open question 4
  - ask: A101
    by: beat 6
  - ask: A102
    by: open question 4
  - ask: A103
    by: beat 1
  - ask: A104
    by: beat 1

size:
  pages: 3
  objects: 9
  automations: 9
  agents: 1

data:
  source: "assumed, shaped like HubSpot (accounts, contacts, deals) and the factory's context graph; the component registry is given: the spec's sub-workflow tables (Pipeline-Factory-Engineering-Build.docx), written to studio/data/components.csv with seeded run statistics"
  masked: "none: fictional. Invented companies, people and links (carrowvale.example); the spec's own author and the earlier POC are not seeded; components.csv holds no personal field (57 rows, 16 columns, profiled)"
  rows:
    - "PF Patch: 2, record · seed"
    - "PF Account: 15, record · seed (story row A-1001 Carrow & Vale Logistics)"
    - "PF Person: 13, record · seed (A-1001's buying committee and its gatekeeper)"
    - "PF Signal: 9, record · seed"
    - "PF Fact: 10, record · seed"
    - "PF Draft: 6, record · seed"
    - "PF Hand-off: 18, record · seed"
    - "PF Component: 57, record · seed naming studio/data/components.csv"
    - "PF Seed snapshot: one per seeded row, written by the seed task"
  expected_answers: eval.csv

verify:
  round: 0
  open: []

collaterals:

review:
  round: 0
  open: []

decisions:
  - by: orchestrator
    when: 2026-10-31
    text: "Profile studio/profiles/unifyapps.md drafted by Studio from the request and the defaults; no profile existed."
  - by: orchestrator
    when: 2026-10-31
    text: "Preflight on the cloud runner: the collateral kit's python packages and faster-whisper are missing (blocks G4's collaterals and transcribing call recordings at G1). The runner's setup installs them; recorded here so a G4 run checks again."
  - by: orchestrator
    when: 2026-10-31
    text: "Version 1 is the first version: 1-harvest reads the channel's whole history, not only messages since the version time."
  - by: research
    when: 2026-11-01
    text: "Site: https://www.unifyapps.com (official, Strong). No brand page or press kit (/brand, /brand-kit, /press-kit, /media-kit answer 404); the colour source is the site itself: its stylesheets and the header logo Unify-logo.svg, whose 757 paths are filled #847347, the most-used colour in the stylesheets."
  - by: profile
    when: 2026-11-01
    text: "Brand colour: brand-sample.py picked #007AFF from --swiper-theme-color, a carousel library default, not a brand variable; the site names no brand variable, so the colour is ambiguous and the standing answer takes the recommended one: #847347 (hue 43), the logo fill. Other candidates: #0F2805 (dark green, text), #5C37EB (violet accent), #007AFF (library default). Listed in the G2 pack."
  - by: plan
    when: 2026-11-01
    text: "Logo: the site header logo Unify-logo.svg saved as published to studio/design-system/unifyapps/logo.svg (brand-sample.py fetched a chevron icon instead); no wordmark placeholder needed."
  - by: plan
    when: 2026-11-01
    text: "Modes: the outside systems (HubSpot, Apollo, Sprouts, Gong, Bombora, Sales Navigator, Google Calendar) are mocked by the PF objects: Sprouts and Gong have no connection on the tenant, and the HubSpot and Apollo connections there belong to other people (open question 4)."
  - by: plan
    when: 2026-11-01
    text: "Modes: the timing score, the Send Rules Check, Gate 1 hard blocks and the field locks are deterministic rules inside live automations, never presented as AI; the 38 agents' outputs (facts, Case for Change, person notes, drafts, grades, labels) are seeded with the AI marker; one live read-only AI agent, the Pipeline Factory Analyst."
  - by: plan
    when: 2026-11-01
    text: "The analyst reaches the code app through an automation (Pipeline Factory · Ask the analyst, on ai_agents_by_unifyapps_invoke_agent), because a code app calls only Storage and automations."
  - by: plan
    when: 2026-11-01
    text: "Harvest questions 2 (demo date), 5 (the earlier POC) and 6 (who owns the asks) are not carried into G2: the plan does not depend on them (20-minute slot, this POC only, Gourav Mahunta as owner)."

dev_issues: []

frozen:

cost:
  runs: 2
  agent_spawns: 2
  tokens_m: 0.42
  wall_h: 0.7

open_questions:
  - by: harvest
    for: lead
    text: "What will the client count as success for this demo? Options: (recommended) The spec's own shape: one account moves end to end through the factory (signal, Gate 1, research and buying team, Gate 2 drafts with grades and rule checks, a booked meeting) with every hand-off visible as a confidence-scored record a person can stop (A1, A4, A8); The profile's default: an approval that routes by a rule, an AI assistant over live data, clean tables"
  - by: harvest
    for: lead
    text: "When is the demo, or the next date this is shown? Nothing in the channel, the spec or the profile names one. Options: (recommended) Tell us the date and the slot; No date yet: plan for the profile's 20-minute in-person slot"
  - by: harvest
    for: lead
    text: "The spec covers 38 agents, 12 workflows and 5 human gates (A1); a 20-minute demo cannot run them all live. Which slice is built live? Options: (recommended) One account's path through sub-workflows 2 to 5 live (Buying Signal Spotter, Account Ranking, Gate 1, Company Facts Collector, Buying Team Mapper, Case for Change Drafter, Message Writer, Fact Checker, Message Grader, Send Rules Check, Gate 2), the rest shown as seeded records in a control tower; One sub-workflow in full depth; All 50 components as a registry and control tower with seeded runs and a handful live"
  - by: harvest
    for: lead
    text: "The spec names a source document, \"Pipeline Factory Final Blueprint — Patches and Pods (Oct 28, 2026)\", and a \"Hand-off register below\" (A5) that the shared file does not hold. Options: (recommended) Work from the spec's Feeds columns as the hand-off list, as its diagram note says; Share the blueprint and the register in the channel before G2"
  - by: harvest
    for: lead
    text: "Orbit holds an earlier POC for the same use case (POC-unifyapps-pipeline-factory-20261030) with a Requirements v1 r1 and a Plan v1 r1. Should its asks or decisions carry into this POC? Options: (recommended) No: this POC stands on the spec shared in #pipeline-factory-v1 (name anything to carry over); Yes: carry the earlier POC's asks forward as a feedback round"
  - by: harvest
    for: lead
    text: "The spec was written by Hardik (byline, Oct 28, 2026); the asks are proposed to the POC lead. Who owns them? Options: (recommended) Gourav Mahunta owns all asks, Hardik is the subject expert consulted on them; Hardik owns the asks in sub-workflows 1 to 8, Gourav the rest"
  - by: plan
    for: owner
    text: "1. Which intent should the demo take? The plan assumes both: the outcome first (one account through the factory), then one hood beat (the Save hand-off automation that enforces the hand-off contract). Options: (recommended) both; use-case: no hood beat, 15 to 20 rows; platform: 2 to 4 hood beats, a one-line description on every node and field."
  - by: plan
    for: owner
    text: "2. Which slice is built live, and is that what the client will count as success (harvest questions 1 and 3)? The plan assumes one account end to end (signal, fast lane, Gate 1, research and buying team, Gate 2 with the Send Rules Check, a booked meeting with locked fields) on six live automations and one live AI agent, with the 57 components as registry rows carrying seeded run statistics; the agents' rubrics (A93), handbook sections (A94) and 50-item evaluations (A97) are not built. Options: (recommended) that slice; one sub-workflow in full depth; build two or three more of the 38 agents live (name them)."
  - by: plan
    for: owner
    text: "3. The spec's Hand-off register (A5) and the blueprint it cites are not in the shared file (harvest question 4). The plan assumes the register is the spec's Feeds columns, written into each component's feeds, and Save hand-off refuses any pair not in it. Options: (recommended) the Feeds columns; share the register in the thread before the build starts."
  - by: plan
    for: owner
    text: "4. Outside systems: Sprouts and Gong have no connection on the tenant, and the HubSpot (9) and Apollo (2) connections there belong to other people. The plan assumes every outside system is mocked by the factory's own records and no external step is built (A65, A100, A102 shown as rules on the mocked records). Options: (recommended) mocked, labelled (mocked) on screen; name one HubSpot connection and the booking writes the locked fields to a DEMO-TEST company there as a bonus step; give a HubSpot sandbox (a credential asked in the session)."
---

## build_contract

Title: Pipeline Factory Control Tower

### Requested outcome
The pod BDR and the patch AE watch one account, Carrow & Vale Logistics, move through the Pipeline Factory: a strong signal takes the fast lane, Gate 1 accepts it, research and the buying team arrive as confidence-scored hand-off records, Gate 2 approves drafts while the Send Rules Check refuses one, and the booked meeting locks its fields. Every hand-off is a saved record in the control tower that a person can see, check and stop; an assistant answers what is waiting on a person and a person pauses a red component from its answer.

### Touches
- object · PF Patch · new
- object · PF Account · new
- object · PF Person · new
- object · PF Signal · new
- object · PF Fact · new
- object · PF Draft · new
- object · PF Hand-off · new
- object · PF Component · new
- object · PF Seed snapshot · new
- automation · Pipeline Factory · Save hand-off · new
- automation · Pipeline Factory · Log signal · new
- automation · Pipeline Factory · Decide Gate 1 · new
- automation · Pipeline Factory · Clear Gate 2 · new
- automation · Pipeline Factory · Book meeting · new
- automation · Pipeline Factory · Pause component · new
- automation · Pipeline Factory · Read factory records · new
- automation · Pipeline Factory · Ask the analyst · new
- automation · Pipeline Factory · Reset demo · new
- ai-agent · Pipeline Factory Analyst · new
- code-app · UnifyApps Pipeline Factory Control Tower · new

### Contract
#### object · PF Patch
The patches: slots, pace and success rate per patch.
- object · create · PF Patch: id OBJ_pf_patch; primaryKey patch_id (text, required); fields name (text), pod (text), owner_ae (text), bdr (text), geo (text), eligible_accounts (number), slots_base (number), slots_allocated (number), slots_used (number), pace_boost_pct (number), intros_booked_7d (number), success_rate (number), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Account
The patch accounts with fit, timing, Gate 1 state and the fields that lock at booking.
- object · create · PF Account: id OBJ_pf_account; primaryKey account_id (text, required); fields name (text), industry (text), patch_id (text), pod (text), owner_ae (text), backup_ae (text), bdr_of_record (text), hq_city (text), fit_score (number, of 60), fit_band (picklist: best "Best fit", medium "Medium fit", low "Low fit"), icp_quadrant (text), timing_score (number, of 40), rank_in_patch (number), top_signals (text), last_touch (date, epoch ms), gate1_status (picklist: pending "Pending", accepted "Accepted", rejected "Rejected", blocked "Blocked", queued "Queued", not_eligible "Not eligible"), gate1_reason (picklist: none "None", bad_fit "Bad fit", active_deal "Active deal", wrong_timing "Wrong timing", in_conversation "Already in conversation"), factory_holdout (boolean), factory_holdout_until (date, epoch ms), ultimate_parent_lock (text), deal_stage (picklist: none "None", engage "Engage", connect "Connect", commit "Commit"), meeting_type (text), meeting_source (text), factory_sourced (boolean), factory_influenced (boolean), marketing_influenced (boolean), value_pattern (text), locked_at (date, epoch ms), meeting_label (picklist: none "None", intro "Intro", new_buyer "New Buyer Meeting", does_not_count "Doesn't count"), qualified_status (picklist: none "None", qualified "Qualified", not_qualified "Not qualified"), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Person
The story account's buying committee by tier and role.
- object · create · PF Person: id OBJ_pf_person; primaryKey person_id (text, required); fields account_id (text), name (text), title (text), role (picklist: economic_buyer "Economic buyer", champion "Champion", technical_evaluator "Technical evaluator", business_owner "Business owner", gatekeeper "Gatekeeper"), tier (picklist: t1 "Tier 1", t2 "Tier 2", t3 "Tier 3", backup "Backup", mapped "Mapped only"), note (text), email_status (picklist: verified "Verified", linkedin_only "LinkedIn only"), dnc (boolean), in_other_sequence (boolean), confidence (number), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]"), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Signal
Buying signals with weight, confidence and whether they counted.
- object · create · PF Signal: id OBJ_pf_signal; primaryKey signal_id (text, required); fields account_id (text), signal_type (picklist: pricing_visit "Checked pricing/product visit", new_leader "New CIO/CTO/CDO/CAIO/Head of AI", event "Event or webinar", ai_hiring "AI platform hiring", earnings "Earnings naming AI", bombora "Bombora surge", vendor_interest "Interest in a current vendor's tool", vendor_renewal "Vendor renewal within 9 months", funding "Funding, merger or new market", exec_posts "Executive posts on AI"), weight (number), signal_date (date, epoch ms), source_link (text), confidence (number), counted (boolean), not_counted_reason (text), fast_lane (boolean), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Fact
Sourced company facts, use case matches and Case for Change lines.
- object · create · PF Fact: id OBJ_pf_fact; primaryKey fact_id (text, required); fields account_id (text), kind (picklist: fact "Company fact", use_case "Use case match", case_for_change "Case for Change line"), statement (text), quote (text), source (text), page_or_time (text), fact_date (date, epoch ms), link (text), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]"), uc_id (text), confidence (number), writer (text), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Draft
The drafts held at Gate 2 with grade, fact check and rules result.
- object · create · PF Draft: id OBJ_pf_draft; primaryKey draft_id (text, required); fields account_id (text), person_id (text), play_id (text), channel (picklist: email "Email", linkedin "LinkedIn", call "Call"), subject (text), body (text), grade (number), fact_check (picklist: passed "Passed", blocked "Blocked"), rules_check (picklist: pending "Pending", passed "Passed", blocked "Blocked"), rules_reason (text), sender (text), sender_pod (text), planted_error (boolean), status (picklist: waiting_gate2 "Waiting at Gate 2", approved "Approved", blocked "Blocked", held "Held", enrolled "Enrolled"), enrolment_key (text), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Hand-off
Every hand-off as a saved record: schema-checked, confidence-scored, keyed by Patch ID.
- object · create · PF Hand-off: id OBJ_pf_handoff; primaryKey handoff_id (text, required); fields idempotency_key (text, account_id + person_id + play_id), patch_id (text), account_id (text), person_id (text), play_id (text), from_component (text), to_component (text), record_type (text), payload (text, JSON), evidence (text), confidence (number), threshold (number), schema_status (picklist: passed "Passed", rejected "Rejected"), status (picklist: flowed "Flowed on", waiting_person "Waiting on a person", rejected "Rejected", late "Late, retried", held "Held: component paused"), assigned_to (text), reason (text), model (text), cost_usd (number), latency_ms (number), due_at (date, epoch ms), saved_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Component
The registry: 38 agents, 12 workflows, 5 human gates and 2 rule steps.
- object · create · PF Component: id OBJ_pf_component; primaryKey component_id (text, required); fields name (text), sub_workflow (picklist: sw1 "1. Patch accounts", sw2 "2. Account selection", sw3 "3. Account research", sw4 "4. Buying committee", sw5 "5. Outreach drafting", sw6 "6. Outreach", sw7 "7. Engage, Connect and Commit", sw8 "8. Learning and governance"), kind (picklist: agent "Agent", checker "Checker", monitor "Monitor", workflow "Workflow", human_gate "Human gate", rule_step "Rule step"), what_it_does (text), threshold (number), below_threshold_goes_to (text), schedule (text), feeds (text), writes (text), model_family (picklist: family_a "Family A (drafters)", family_b "Family B (checkers)", none "No model"), checks (text), success_rate (number), status (picklist: live "Live", shadow "Shadow", paused "Paused"), ask_id (text), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Seed snapshot
The seeded values the reset restores.
- object · create · PF Seed snapshot: id OBJ_pf_seed_snapshot; primaryKey snapshot_id (text, required); fields object_id (text), record_id (text), row_values (text, JSON of the seeded row), taken_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default seed)
- record · seed · PF Patch: origin seed on every row. PATCH-NAE-03 "NA East · Logistics and Utilities", pod POD-NAE-1, owner_ae Dana Okafor, bdr Marcus Ellery, geo NA East, eligible_accounts 312, slots_base 25, slots_allocated 24, slots_used 19, pace_boost_pct 0, intros_booked_7d 4, success_rate 98.6; PATCH-NAE-04 "NA East · Manufacturing and Health", pod POD-NAE-2, owner_ae Rhea Castillo, bdr Tomas Ilves, geo NA East, eligible_accounts 260, slots_base 25, slots_allocated 20, slots_used 20, pace_boost_pct 25, intros_booked_7d 2, success_rate 99.2
- record · seed · PF Account: origin seed on every row; dates are epoch ms in the 90 days before the demo. A-1001 Carrow & Vale Logistics (the story row): logistics, PATCH-NAE-03, POD-NAE-1, owner_ae Dana Okafor, backup_ae Luis Brennan, bdr_of_record Marcus Ellery, hq_city Columbus OH, fit_score 49, fit_band best, icp_quadrant Q1, timing_score 25, rank_in_patch 1, top_signals "2 checked pricing visits in 14 days; AI platform hiring; renewal of current vendor in 8 months", gate1_status pending, gate1_reason none, factory_holdout false, ultimate_parent_lock Dana Okafor, deal_stage none, value_pattern "Order-to-cash orchestration", meeting_label none, qualified_status none. A-1002 Brightline Cold Chain: logistics, PATCH-NAE-03, fit 41 medium, timing 30, rank 2, pending. A-1003 Ostrander Marine Freight: logistics, PATCH-NAE-03, fit 44 medium, timing 15, rank 3, pending. A-1004 Pellham Ridge Distribution: logistics, PATCH-NAE-03, fit 38 low, timing 20, rank 4, pending. A-1005 Kestrel Ridge Utilities: utilities, PATCH-NAE-03, fit 40 medium, timing 22, rank 5, pending, factory_holdout true, factory_holdout_until 2027-01-27. A-1006 Tamsin Row Health Partners: healthcare, patch_id empty, pod empty, owner_ae empty, fit 43 medium, timing 18, gate1_status pending. A-1007 Quillfeather Insurance Group: insurance, PATCH-NAE-03, fit 46 best, timing 28, rank 6, accepted, deal_stage engage. A-1008 Marlow Basin Foods: food, PATCH-NAE-03, fit 37 low, timing 19, rank 7, queued. A-1009 Sablewood Retail Co: retail, PATCH-NAE-03, fit 42 medium, timing 12, rank 8, queued. A-1010 Fenwick Arc Manufacturing: manufacturing, PATCH-NAE-04, POD-NAE-2, Rhea Castillo, Tomas Ilves, fit 47 best, timing 26, rank 1, pending. A-1011 Larkspur Data Centers: technology, PATCH-NAE-04, fit 39 low, timing 24, rank 2, pending. A-1012 Harrowgate Mutual: insurance, PATCH-NAE-04, fit 45 best, accepted, deal_stage connect, meeting_label new_buyer. A-1013 Vexmoor Telecom: telecom, PATCH-NAE-04, fit 48 best, accepted, deal_stage commit, meeting_label new_buyer, qualified_status qualified. A-1014 Bellwether Grain Co-op: agriculture, PATCH-NAE-04, fit 35 low, not_eligible (below the floor of 36). A-1015 Corrin Bay Pharmacy Group: healthcare, PATCH-NAE-04, fit 41 medium, timing 17, rank 3, pending. Every PATCH-NAE-03 row carries pod POD-NAE-1, owner_ae Dana Okafor, backup_ae Luis Brennan, bdr_of_record Marcus Ellery; every PATCH-NAE-04 row pod POD-NAE-2, owner_ae Rhea Castillo, backup_ae Omar Haddad, bdr_of_record Tomas Ilves.
- record · seed · PF Person: origin seed on every row; all for A-1001. P-1001 Helena Marsh, CFO, economic_buyer, t1, verified, confidence 88, public. P-1002 Arjun Mehta, VP Digital Operations, champion, t1, verified, 91, public. P-1003 Colette Baines, Head of AI (joined 6 weeks ago), business_owner, t1, verified, 84, public. P-1004 Wes Odum, Director Enterprise Architecture, technical_evaluator, t2, verified, 79, public. P-1005 Nadia Fournier, Director Order Management, business_owner, t2, verified, 66, hypothesis. P-1006 Gabe Lindahl, IT Integration Manager, technical_evaluator, t2, linkedin_only, 74, public. P-1007 Imani Clarke, Customer Operations Lead, business_owner, t3, verified, 72, public. P-1008 Sven Aldous, Finance Systems Manager, technical_evaluator, t3, verified, 70, public, in_other_sequence true. P-1009 Ruth Okonkwo, Procurement Lead, business_owner, t3, verified, 71, public. P-1010 Theo Marchetti, Automation Engineer, technical_evaluator, t3, verified, 75, public. P-1011 Lena Voss, Director Supply Chain Systems, champion, backup, verified, 77, public. P-1012 Calvin Reyes, Senior Integration Architect, technical_evaluator, backup, verified, 73, public. P-1013 Joan Pruitt, Executive Assistant to the CFO, gatekeeper, mapped, verified, 90, public. Each note is four lines: role and time in role, past companies, what they own, link to UC-ID UC-LOG-014.
- record · seed · PF Signal: origin seed on every row. S-01 A-1001 pricing_visit weight 25, confidence 92, counted true (2 visits in 14 days, 40s and 65s with scroll). S-02 A-1001 pricing_visit weight 0, counted false, not_counted_reason "within 2 minutes of an email's delivery". S-03 A-1001 ai_hiring weight 15, confidence 81, counted true. S-04 A-1001 vendor_renewal weight 15, confidence 64, counted true. S-05 A-1002 bombora weight 15, confidence 77, counted true. S-06 A-1002 event weight 20, confidence 85, counted true. S-07 A-1003 earnings weight 15, confidence 73, counted true. S-08 A-1010 new_leader weight 20, confidence 88, counted true, fast_lane true. S-09 A-1011 funding weight 10, confidence 66, counted false, not_counted_reason "confidence under 70: logged, not scored".
- record · seed · PF Fact: origin seed on every row; all for A-1001; links are invented addresses under carrowvale.example. F-01 fact "Order exceptions are handled by hand across three ERPs", quote from the latest annual report, page 14, public, confidence 90, writer Company Facts Collector. F-02 fact "Plans to automate order-to-cash by 2027", earnings call Q2, 00:18:40, public, 88. F-03 fact "Hiring three integration engineers for an AI platform team", job post, public, 82. F-04 fact "Cost-to-serve named a board priority", investor deck, slide 9, public, 86. F-05 use_case UC-LOG-014 "Order exception triage", confidence 84, writer Use Case Matcher. F-06 use_case UC-LOG-022 "Carrier invoice reconciliation", confidence 76. F-07 use_case UC-LOG-031 "Customer status agent", confidence 64, hypothesis (shown only as a question). F-08 case_for_change "Business problem: order exceptions handled by hand across three ERPs" (cites F-01), public. F-09 case_for_change "Why now: new Head of AI and an integration hiring push" (cites F-03), public. F-10 case_for_change "Risk: the current integration vendor contract may renew in 8 months" hypothesis, confidence 68, writer Case for Change Drafter.
- record · seed · PF Draft: origin seed on every row; all A-1001, play_id PLAY-SIG-NEWLEADER. D-01 P-1002 email, subject "Order exceptions across three ERPs", grade 86, fact_check passed, rules_check pending, sender Marcus Ellery, sender_pod POD-NAE-1, status waiting_gate2. D-02 P-1003 email, subject "Your first 90 days as Head of AI", grade 82, passed, pending, Marcus Ellery, POD-NAE-1, waiting_gate2. D-03 P-1001 linkedin, grade 79, passed, pending, sender Dana Okafor, POD-NAE-1, waiting_gate2. D-04 P-1004 email, subject "Integration hiring at Carrow & Vale", grade 81, passed, pending, sender Rhea Castillo, sender_pod POD-NAE-2, planted_error true, waiting_gate2. D-05 P-1005 email, grade 71 (under 75 after one rewrite: a person decides), passed, pending, Marcus Ellery, POD-NAE-1, waiting_gate2. D-06 P-1008 email, grade 80, passed, pending, Marcus Ellery, POD-NAE-1, waiting_gate2 (P-1008 is in another sequence). Each email body is 90 to 120 words, one sourced fact, one question, no em dashes.
- record · seed · PF Hand-off: origin seed on every row; idempotency_key is account_id + person_id + play_id; model, cost_usd and latency_ms on every agent row. H-01 PATCH-NAE-03 A-1001 Fit Scorer to Account Ranking, fit score, confidence 92, threshold 70, passed, flowed. H-02 A-1001 Buying Signal Spotter to Account Ranking, signal S-01, 92, 70, passed, flowed. H-03 A-1001 Account Ranking to Gate 1, batch row, 100, 0, passed, flowed. H-04 A-1007 Gate 1 to Company Facts Collector, 100, passed, flowed. H-05 A-1001 Company Facts Collector to Case for Change Drafter, facts F-01 to F-04, 88, 0, passed, flowed. H-06 A-1001 Use Case Matcher to Case for Change Drafter, F-05 to F-07, 84, 70, passed, flowed. H-07 A-1002 Patch Suggester to RevOps, patch proposal, 74, 80, passed, waiting_person, assigned_to RevOps, reason "confidence 74 under 80". H-08 A-1001 Buying Team Mapper to Person Notes Writer, P-1001 to P-1013, 81, 70, passed, flowed. H-09 A-1001 Person Notes Writer to Message Writer, 83, 70, passed, flowed. H-10 A-1003 Case for Change Drafter to Play Picker, 77, 70, rejected, rejected, assigned_to GTM engineer, reason "schema check failed: evidence missing". H-11 A-1010 Buying Signal Spotter to Play Picker, fast lane S-08, 88, 70, passed, flowed. H-12 A-1001 Buying Team Mapper to Gate 2, role of P-1005, 66, 70, passed, waiting_person, assigned_to Marcus Ellery, reason "role confidence 66 under 70". H-13 A-1001 Message Writer to Fact Checker, D-01 to D-06, 85, 70, passed, flowed. H-14 A-1002 Current Vendor Finder to Renewal Date Finder, 58, 60, passed, late, reason "late 2h 10m, retried once". H-15 A-1001 Case for Change Drafter to Gate 2, F-10, 68, 70, passed, waiting_person, assigned_to Marcus Ellery, reason "confidence 68 under 70". H-16 A-1012 Meeting Labeler to AE confirm, new_buyer, 86, 80, passed, flowed. H-17 A-1013 Deal Qualifier to AE confirm, qualified, 90, 80, passed, flowed. H-18 A-1011 Current Vendor Finder to Battlecard Writer, 61, 60, passed, late, reason "late 3h 40m, retried twice".
- record · seed · PF Component: origin seed on every row; every row of the file studio/data/components.csv (57 rows: 38 agents (30 agents, 6 checkers, 2 monitors), 12 workflows, 5 human gates, 2 rule steps), every column as the file gives it; C08 Current Vendor Finder carries success_rate 96.1 (red under 97).
- record · seed · PF Seed snapshot: one row per row the seed lines above write (snapshot_id `object_id:record_id`, row_values the row as seeded, JSON), written once after the seeds, origin seed.

#### automation · Pipeline Factory · Save hand-off
The hand-off contract enforced in code for every connection.
- automation · create · Pipeline Factory · Save hand-off: callable from other automations; inputs from_component (text), to_component (text), record_type (text), patch_id (text), account_id (text), person_id (text), play_id (text), confidence (number), payload (text, JSON), evidence (text), writes_field (text); result result (text: saved | duplicate | rejected | waiting_person), handoff_id (text), reason (text). Deterministic, no model call: refuses a pair not in the register (PF Component feeds) with rejected "not registered"; refuses a writes_field whose writer is another component with rejected "one writer per field"; refuses a payload with no confidence, no evidence or no patch_id with rejected "schema check failed: `field` missing" and a PF Hand-off row assigned_to GTM engineer; looks up idempotency_key account_id + person_id + play_id and answers duplicate without a second row; under the to-component's threshold saves waiting_person assigned to its below_threshold_goes_to; else saves flowed. Every row carries model, cost_usd, latency_ms and saved_at.

#### automation · Pipeline Factory · Log signal
Scores a signal and sends a strong one down the fast lane.
- automation · create · Pipeline Factory · Log signal: callable from the app; inputs account_id (text), signal_type (text, a PF Signal code), source_link (text), seconds_on_page (number), scrolled (boolean), minutes_after_email (number), origin (text); result result (text: counted | not_counted | fast_lane), timing_score (number), reason (text). Deterministic: the checked-visit rule (10+ seconds and a scroll, or a repeat within 7 days; never within 2 minutes of an email's delivery, never from a scanner network, never with no interaction); weights from the starting signal weights; timing_score is the sum of counted weights, capped at 40; new_leader, event, vendor_renewal and a second checked visit are strong and go to the fast lane: one PF Hand-off Buying Signal Spotter to Play Picker through Save hand-off, due within the hour. Writes PF Signal and PF Account.timing_score.

#### automation · Pipeline Factory · Decide Gate 1
The BDR's accept or reject, with hard blocks and same-patch refill.
- automation · create · Pipeline Factory · Decide Gate 1: callable from the app; inputs account_id (text), decision (text: accept | reject), reason (text: bad_fit | active_deal | wrong_timing | in_conversation), origin (text); result result (text: accepted | rejected | blocked), refill_account_id (text), reason (text). Hard blocks answer blocked with the cause: no Patch ID, no AE or pod, an AE hold, or factory_holdout true ("held out until" and the date). A reject needs one reason and refills the slot with the next queued account of the same patch (lowest rank_in_patch), never another patch's. An accept saves a Gate 1 to Company Facts Collector and Buying Team Mapper hand-off through Save hand-off and adds 1 to PF Patch.slots_used.

#### automation · Pipeline Factory · Clear Gate 2
The Send Rules Check and one enrolment per person and play.
- automation · create · Pipeline Factory · Clear Gate 2: callable from the app; inputs draft_id (text), decision (text: approve | hold), actor (text), origin (text); result result (text: approved | blocked | already_enrolled | held), rule (text), reason (text). Runs the Send Rules Check before an approve: the sender's pod must be the account's pod; the person not on DNC, not in another sequence, not held out; Patch ID, AE and pod present; a planted_error draft is always blocked and counted as caught. A blocked draft gets rules_check blocked and rules_reason; an approved draft is enrolled once (Outreach Launcher, mocked: status enrolled, enrolment_key account_id + person_id + play_id, "queued for Apollo sequence (mocked)"); an approve of an enrolled draft answers already_enrolled and writes nothing.

#### automation · Pipeline Factory · Book meeting
Books the meeting and locks the attribution fields.
- automation · create · Pipeline Factory · Book meeting: callable from the app; inputs account_id (text), action (text: book | correct), field (text), new_value (text), reason (text), actor_role (text), origin (text); result result (text: booked | locked | corrected), locked_fields (text), reason (text). book sets deal_stage engage, meeting_type intro, meeting_source "factory: AE booking link", factory_sourced true, factory_influenced true, locked_at now, and saves a Meeting Handoff hand-off through Save hand-off. correct on a locked field (patch_id, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced) answers locked "Locked at booking: corrections go through RevOps with a reason" unless actor_role is revops and reason is given, then corrected and logged.

#### automation · Pipeline Factory · Pause component
A person stops a component; its hand-offs hold.
- automation · create · Pipeline Factory · Pause component: callable from the app; inputs component_id (text), actor (text), origin (text); result result (text: paused | already_paused), held_handoffs (number), reason (text). Sets PF Component.status paused and every flowed-pending or late PF Hand-off from that component to held; resuming is a person's job and is not offered.

#### automation · Pipeline Factory · Read factory records
The analyst's read-only tool.
- automation · create · Pipeline Factory · Read factory records: callable from the AI agent; inputs patch_id (text), account_id (text); result patches (text, JSON), accounts (text, JSON), waiting_handoffs (text, JSON), red_components (text, JSON). Read-only: PF Patch, PF Account, PF Hand-off with status waiting_person, rejected or late, and PF Component with success_rate under 97.

#### automation · Pipeline Factory · Ask the analyst
Calls the analyst for the app.
- automation · create · Pipeline Factory · Ask the analyst: callable from the app; inputs question (text), patch_id (text); result answer (text), grounding (text), suggested_component_id (text). Invokes the Pipeline Factory Analyst agent with the question and the patch, and returns its answer, the records it cited, and the red component it names, if any.

#### automation · Pipeline Factory · Reset demo
Clears test rows and restores the seed rows.
- automation · create · Pipeline Factory · Reset demo: callable, mode deterministic, no model call; no inputs; result deleted (number), restored (number). Deletes every row whose origin is test in the nine PF objects, puts every seed row back to its values in PF Seed snapshot, never touches a user row.

#### ai-agent · Pipeline Factory Analyst
The read-only assistant over the factory records.
- ai-agent · create · Pipeline Factory Analyst: read-only; model Nebula's recommendation; instructions: answers the BDR, the AE and RevOps about one patch from the factory's records only; names each hand-off by its from and to components, its confidence against the threshold and who it waits on; names a component under 97% success as red; never sends, edits or approves anything; says a field is not held when no record holds it; tool Read factory records (Pipeline Factory · Read factory records).

#### code-app · UnifyApps Pipeline Factory Control Tower
The code app: Control tower, To-do and Account.
- code-app · create · UnifyApps Pipeline Factory Control Tower: the shell: the design system stylesheet, the fonts, the rail with the UnifyApps logo, the header, the routes for Control tower (/tower), To-do (/todo) and Account (/accounts/:accountId); PRIVATE
- code-app · update · UnifyApps Pipeline Factory Control Tower: screen Control tower: four .tile (slots left of allocated, intros booked in 7 days, success rate with .delta against 99% and red under 97%, waiting on a person); .tabs Hand-offs and Components; Hand-offs: .toolbar (search, facets status, from component, patch) above .tbl of PF Hand-off (from to, patch, confidence of threshold, status .tag, model, cost, latency) with a .drawer for one record's payload and evidence; Components: .toolbar (search, facets sub-workflow, kind, status) above .tbl of PF Component with .pg, and a .drawer for one component (what it does, threshold and where below goes, schedule, feeds, writes, model family, checks, success rate); a .feed of the newest hand-offs; a Log signal .modal (.fld, .ctl, .seg) · reads PF Patch, PF Hand-off, PF Component · calls Pipeline Factory · Log signal on Log signal
- code-app · update · UnifyApps Pipeline Factory Control Tower: screen To-do: the Gate 1 batch as .toolbar above .tbl of PF Account where gate1_status is pending or queued (fit band .tag, timing of 40, top 3 signals as .cell-chips, Patch ID, AE, last touch, slots left), Accept as the row's .btn-p and Reject with a .menu of four reasons; a hard block as .tag.negative with a .note; a Waiting on you .feed of PF Hand-off rows assigned to the BDR; .toast on each result · reads PF Account, PF Patch, PF Hand-off · calls Pipeline Factory · Decide Gate 1 on Accept and Reject
- code-app · update · UnifyApps Pipeline Factory Control Tower: screen Account: .crumb; the account head as .g1 with .dl (patch, AE, BDR, fit of 60, timing of 40, the locked fields with a lock mark); .tabs Research, Buying team, Gate 2, Meeting; Research: .tbl of PF Fact with [PUBLIC] or [HYPOTHESIS] .tag, and the Case for Change in an AI Insight card (.ai:not(.msg)) marked AI-drafted; Buying team: .pc cards by tier with .faces, the gatekeeper marked mapped only; Gate 2: .tbl of PF Draft with grade, fact check and rules .tag, Approve as .btn-p and Hold, the refusal as .tag.negative with a .note; Meeting: .stages Engage, Connect, Commit, Book meeting as .btn-p, the Deal Qualifier's six requirements as .tbl, the deadlines as .agenda, the locked-field correction as a .modal; the agent drawer (.agent-launch, .agent-drawer) on every screen with the answer in an AI Insight card (.ai:not(.msg)) with its grounding line and one action, Pause and the component name · reads PF Account, PF Person, PF Fact, PF Draft, PF Hand-off, PF Component · calls Pipeline Factory · Clear Gate 2 on Approve and Hold, Pipeline Factory · Book meeting on Book meeting and the correction, Pipeline Factory · Ask the analyst on Ask, Pipeline Factory · Pause component on Pause

### Business rules
- Every agent hands off through the context graph, never directly: a hand-off is a PF Hand-off row written only by Pipeline Factory · Save hand-off.
- A hand-off not in the register (PF Component feeds) is refused; only the component named as a field's writer writes it.
- A record that fails its schema is rejected, the GTM engineer is alerted, the downstream step waits; generic copy is never substituted.
- A record under the receiving component's threshold does not flow on; it goes to the named person's to-do list.
- Every save is keyed on account_id + person_id + play_id; a re-run never makes a second copy or a second enrolment.
- Gate 1 hard blocks: no Patch ID, AE or pod; an AE hold; held out. A rejected slot refills from the same patch.
- The Send Rules Check blocks a draft whose sender is not in the account's pod, whose person is on DNC or in another sequence, and every planted test error.
- Patch ID, BDR of record, meeting type, meeting source, factory-sourced, factory-influenced and marketing-influenced lock at booking; corrections go through RevOps with a reason.
- Timing score is the sum of counted signal weights, capped at 40; a visit counts only under the checked-visit rule.
- Safety actions are automatic; resuming a paused component needs a person.
- Every row carries origin: seed on seeded rows, test on rows a check or recording writes, user on rows a person makes in the demo.

### Ready when
- The BDR logs a new Head of AI signal on Carrow & Vale Logistics and a fast-lane hand-off to the Play Picker appears in the control tower.
- Gate 1 accepts Carrow & Vale Logistics, refuses Kestrel Ridge Utilities as held out, and refills a rejected slot from the same patch.
- Gate 2 approves D-01 once and answers already enrolled on a second approve, and refuses D-04 because its sender is not in the account's pod.
- Booking the meeting locks the seven fields and a correction without RevOps is refused.
- The assistant names the three hand-offs waiting on a person and Current Vendor Finder as red, and Pause holds its hand-offs.
- deploy Pipeline Factory · Save hand-off
- deploy Pipeline Factory · Log signal
- deploy Pipeline Factory · Decide Gate 1
- deploy Pipeline Factory · Clear Gate 2
- deploy Pipeline Factory · Book meeting
- deploy Pipeline Factory · Pause component
- deploy Pipeline Factory · Read factory records
- deploy Pipeline Factory · Ask the analyst
- deploy Pipeline Factory · Reset demo
- publish Pipeline Factory Analyst
- publish UnifyApps Pipeline Factory Control Tower

### Rules
- client.css: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/studio/design-system/unifyapps/client.css
- logo: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/studio/design-system/unifyapps/logo.svg
- theme: light · chrome: brand · surface: glass · density: comfortable · style-set: S1
- Outside systems (HubSpot, Apollo, Sprouts, Gong, Bombora, Sales Navigator, Google Calendar) are mocked by the PF objects; no external write; any test record on an outside system would be labelled DEMO-TEST with the demo's date.

### Assumptions
- Check this: proposed intent both (the outcome, then how), with one hood beat after the lean-forward beat.
- Check this: the live slice is one account's path (sub-workflows 2, 3, 4, 5 and 7 as six live automations and one live AI agent); the other components are PF Component registry rows with seeded run statistics.
- Check this: the hand-off register is the spec's Feeds columns, written into PF Component.feeds, until the blueprint's register is shared.
- Check this: HubSpot, Apollo, Sprouts, Gong, Bombora, Sales Navigator and Google Calendar are mocked; no external step is built.
- Check this: brand colour #847347 (the fill of the UnifyApps logo on www.unifyapps.com), hue 43; the sampler's own pick #007AFF was a carousel library default.
- Check this: the Pipeline Factory Analyst runs on Nebula's recommended model; the two model families of the spec are shown as a model_family column, not as two live models.
- Check this: seed rows are fictional (invented companies and people, links under carrowvale.example), dates in the 90 days before the demo.
- Check this: Pipeline Factory · Reset demo and PF Seed snapshot are the one automation and object no beat shows; 4-verify and 6-collaterals run the reset.
- Check this: app visibility PRIVATE; publish and deploy without asking (profile release line).

## entities

## beats

Storyline: "Every agent hands off through the context graph, never directly" (A103) · 7 beats and one hood beat · proposed intent: both.

Story row: PF Account A-1001 Carrow & Vale Logistics · PATCH-NAE-03 (NA East · Logistics and Utilities) · pod POD-NAE-1 · AE Dana Okafor (backup Luis Brennan) · BDR of record Marcus Ellery · fit 49 of 60, best fit, ICP Q1 · timing 25 of 40 before beat 2, 40 after · rank 1 in patch · play PLAY-SIG-NEWLEADER · economic buyer Helena Marsh (CFO), champion Arjun Mehta, new Head of AI Colette Baines · drafts D-01 to D-06, D-04 the planted wrong-pod sender · patch slots 19 used of 24.

1. **The control tower.** The presenter opens Control tower: the screen shows the patch tiles (5 slots left of 24, 4 intros in 7 days, success rate 98.6% against 99%, 3 waiting on a person) and the Hand-offs tab, every hand-off a saved record with its Patch ID, sender, confidence against threshold, model, cost and latency; Carrow & Vale Logistics tops the feed. Route /tower. Asks A1, A4, A10, A11, A12, A27, A103, A104. mode: live (reads seeded rows).
2. **The fast lane.** The presenter clicks Log signal on Carrow & Vale Logistics and logs "new Head of AI" (Colette Baines): the screen shows the result fast_lane, timing 25 to 40 of 40, and a new hand-off Buying Signal Spotter to Play Picker due within the hour at the top of the feed; a visit logged 90 seconds after an email is shown as not counted. Route /tower (Log signal modal). Asks A2, A28, A29, A33, A34, A48. mode: live (Pipeline Factory · Log signal, deterministic rules).
3. **Gate 1.** The presenter opens To-do as Marcus Ellery: the 07:00 batch shows fit band, timing, top 3 signals, Patch ID, AE, last touch and slots left; Accept on Carrow & Vale Logistics saves the hand-off to research; Reject on Ostrander Marine Freight with "active deal" refills the slot with Marlow Basin Foods from the same patch; Accept on Kestrel Ridge Utilities is refused "held out until 2027-01-27". Route /todo. Asks A8, A30, A31, A32. mode: live (Pipeline Factory · Decide Gate 1).
4. **Research and the buying team.** The presenter opens the account: Research shows four sourced facts with quote, page and link tagged [PUBLIC], three use case matches by UC-ID (the weakest shown only as a question), and the Case for Change in an AI Insight card with a [HYPOTHESIS] risk line; Buying team shows 12 people by tier, the economic buyer flagged and the gatekeeper mapped, never contacted. Route /accounts/A-1001 (Research, Buying team). Asks A35, A36, A37, A38, A39, A40, A41, A42, A99. mode: seeded (AI marker).
5. **Gate 2, and the failure beat.** On the Gate 2 tab the presenter approves D-01 (grade 86, fact check passed): Send Rules Check passes and it is enrolled once; Approve again answers already enrolled; Approve on D-04 is refused "Blocked: sender Rhea Castillo is not in the account's pod (POD-NAE-1)" and counted as a caught planted error. Route /accounts/A-1001 (Gate 2). Asks A9, A47, A51, A52, A53, A54, A55, A56, A59, A83. mode: live (Pipeline Factory · Clear Gate 2); drafts and grades seeded.
6. **Booked and locked.** On the Meeting tab the presenter clicks Book meeting: the deal opens at Engage owned by Dana Okafor and the seven fields lock (Patch ID, BDR of record, meeting type, meeting source, factory-sourced, factory-influenced, marketing-influenced); editing Patch ID is refused "Locked at booking: corrections go through RevOps with a reason"; the Deal Qualifier's six requirements and the AE deadlines sit below. Route /accounts/A-1001 (Meeting). Asks A14, A66, A69, A71, A72, A73, A74, A101. mode: live (Pipeline Factory · Book meeting); label and qualifier seeded.
7. **The lean-forward moment: ask the factory, then stop it.** The presenter opens the assistant and types "What is waiting on a person in patch PATCH-NAE-03 right now, and why?": the AI Insight card names H-07 (RevOps), H-12 and H-15 (Marcus Ellery) with their confidence against threshold, H-10 rejected on its schema, and Current Vendor Finder red at 96.1%; its one action, Pause Current Vendor Finder, holds that component's hand-offs and the tile turns paused; resuming is left to a person. Route /tower (agent drawer). Asks A4, A8, A10, A84. mode: live (Pipeline Factory Analyst through Pipeline Factory · Ask the analyst; Pipeline Factory · Pause component).
   Alternatives considered: B, the learning loop: a Scoring Tuner weight proposal passing the Quality Grader and the Friday review (A3, A75), weaker because it is seeded end to end. C, the stop alone: a person pauses a component from its drawer (A4), weaker without the question that finds it. This one wins because the audience asks the factory in their own words and a person stops it from the answer.
H1. **Under the hood.** After beat 7 the presenter opens Pipeline Factory · Save hand-off in the automation builder: the register check, one writer per field, the schema check that rejected H-10, the confidence gate, the idempotency key account_id + person_id + play_id, all in one deterministic automation every other automation calls. Asks A5, A6, A7, A9, A92. mode: live (the deployed automation).

AI surfaces: Pipeline Factory Analyst answer · live. Case for Change card · seeded. Company facts and use case matches · seeded. Person notes · seeded. Drafts, Message Grader grades, Fact Checker results · seeded. Meeting label and Deal Qualifier recap · seeded. Timing score · deterministic. Send Rules Check result · deterministic. Component success rates · seeded. Outside systems (HubSpot, Apollo, Sprouts, Gong, Bombora, Google Calendar) · mocked.

## views

- Control tower (/tower) · beats 1, 2, 7, H1 start · .app shell with .app-rail (logo, .nav-i), .app-top · four .tile (slots, intros, success rate with .delta, waiting) · .tabs Hand-offs / Components · Hand-offs: .toolbar (.field search "n of m", .chipsel status, from component, patch) above .tblwrap .tbl, status as .tag, a .drawer for one record · Components: .toolbar (.chipsel sub-workflow, kind, status) above .tbl with .pg, a .drawer (.dl) for one component · .feed newest hand-offs · Log signal .modal (.fld .ctl .seg) · .agent-launch and .agent-drawer, the answer in .ai:not(.msg) with grounding line and one .btn-p action · .toast
- To-do (/todo) · beat 3 · .toolbar above .tbl of the Gate 1 batch (.tag fit band, .cell-chips top 3 signals), row .btn-p Accept and Reject with a .menu of four reasons · .tag.negative and .note for a hard block · .feed Waiting on you · .toast · .empty states
- Account (/accounts/:accountId) · beats 4, 5, 6 · .crumb · .g1 head with .dl and lock marks · .tabs Research / Buying team / Gate 2 / Meeting · Research: .tbl facts with .tag [PUBLIC] / [HYPOTHESIS], Case for Change in .ai:not(.msg) · Buying team: .pc cards by tier, .faces, .av · Gate 2: .tbl drafts with grade, .tag fact check and rules, .btn-p Approve, .btn-s Hold, .tag.negative and .note for the refusal · Meeting: .stages Engage / Connect / Commit, .btn-p Book meeting, .tbl six requirements, .agenda deadlines, correction .modal
