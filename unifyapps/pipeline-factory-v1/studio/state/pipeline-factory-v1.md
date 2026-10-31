---
use_case: Pipeline Factory v1
client: UnifyApps
poc_row: POC-unifyapps-pipeline-factory-v1-20261031
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g1
version: 1 · since 2026-10-31T10:16:23Z
channel: C0CDB92FALX
threads:
  g1: 1793442419.752669
  g2:
  g3:
  g4:
  connections:
intent:
stage_flag:

gates:
  g1: {status: waiting, round: 1, posted_ts: 1793442419.752669, decided_by: , decided_at: }
  g2: {status: not_posted, round: 0, posted_ts: , decided_by: , decided_at: }
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

runs:
  - started: 2026-10-31T10:16:23Z
    ended: 2026-10-31T10:26:47Z
    gate: g1
    stages: [1-harvest]
    spawns: 1
    tokens: 160
    outcome: posted G1

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

coverage: []

size:
  pages:
  objects:
  automations:
  agents:

data:
  source:
  masked:
  rows:
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

dev_issues: []

frozen:

cost:
  runs: 1
  agent_spawns: 1
  tokens_m: 0.16
  wall_h: 0.2

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
---

## build_contract

## entities

## beats

## views
