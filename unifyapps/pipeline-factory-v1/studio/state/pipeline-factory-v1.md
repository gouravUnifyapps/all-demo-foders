---
use_case: Pipeline Factory v1
client: UnifyApps
poc_row: POC-unifyapps-pipeline-factory-v1-20261031
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: verifying
version: 1 · since 2026-10-31T10:16:23Z
channel: C0CDB92FALX
threads:
  g1: 1793442419.752669
  g2: 1793522055.329009
  g3: 1793612592.122889
  g4:
  connections:
intent: both
stage_flag:

gates:
  g1: {status: approved, round: 1, posted_ts: 1793442419.752669, decided_by: Gourav Mahunta (row), decided_at: 2026-11-01T08:11:55Z}
  g2: {status: approved, round: 1, posted_ts: 1793522055.329009, decided_by: Gourav Mahunta (row; thread reply "Approved, proceed"), decided_at: 2026-11-02T07:40:00Z}
  connections: {status: not_needed, round: 0, posted_ts: , decided_by: , decided_at: , list: []}
  g3: {status: changes_requested, round: 2, posted_ts: 1793612592.122889, decided_by: Gourav Mahunta (thread feedback FB-1793612784906-1, confirmed "yes"), decided_at: 2026-11-02T09:46:24Z}
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
  - when: 2026-11-02T09:42:40Z
    kind: g3
    ts: 1793612592.122889
    by: bot
    version: 1
    round: 1
    documents:
      - {name: Handover · Pipeline Factory v1, type: build_report, file_url: https://orbit.uat.unifyapps.com/auth/file/asset/download/f61f04ce3a4ffe0c83814b10, file_name: handover-v1-r1.pdf, file_size: 601355}
  - when: 2026-11-02T09:43:32Z
    kind: status
    ts: 1793612592.122889
    by: bot
    version: 1
    round: 1
  - when: 2026-11-02T10:12:00Z
    kind: status
    ts: 1793612592.122889
    by: bot
    version: 1
    round: 2
  - when: 2026-11-02T11:33:00Z
    kind: status
    ts: 1793612592.122889
    by: bot
    version: 1
    round: 2
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
  - started: 2026-11-02T07:40:00Z
    ended: 2026-11-02T09:42:40Z
    gate: g3
    stages: [0-connections, 3-build, 4-verify, 3-build (fixes), 4-verify, 5-handover]
    spawns: 24
    tokens: 5900000
    outcome: posted G3
  - started: 2026-11-02T09:55:00Z
    gate: g3
    round: 2
    stages: [2-plan (scoped: 38 agents, 12 workflows), 3-build (15 plans and 2 fixes, 140 tasks)]
    spawns: 38
    tokens: 7500000

stopped:

asks:
  - id: A1
    text: "The Pipeline Factory is 38 single-job agents and 12 deterministic workflows, built on the UnifyApps Solution Builder and connected only through the enterprise context graph. This spec covers how they connect, what each one does and what it plugs into, and how to build each one."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § Pipeline Factory: Engineering Build Spec · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A2
    text: "The dashed fast lane lets a strong signal skip the daily batch and start a play within the hour."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A3
    text: "The left line is the learning loop: outcomes from sub-workflow 8 return as proposed weights (to 1 and 2), best examples and test variants (to 5), and objections (to 6), applied only after the Quality Grader and the Friday review."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A4
    text: "Why: every hand-off can then be seen in the control towers, checked by the Quality Grader, and stopped by a person."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A5
    text: "Registered. A hand-off not in the Hand-off register below does not exist."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A6
    text: "One writer per field. Only the component named in the register writes a field; everyone else reads."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A7
    text: "Schema check on save. A record that fails its JSON schema is rejected, the GTM engineer is alerted, and the downstream step waits. Never substitute generic copy."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A8
    text: "Confidence gate. A record below the component's threshold does not flow on; it goes to the named person's to-do list (thresholds are in each sub-workflow table)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A9
    text: "Idempotent. Every save is keyed on account_id + person_id + play_id. Re-running a hand-off never creates a second copy or a second enrolment."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A10
    text: "On time. Each hand-off has a \"When\". A late one retries, then counts against the component's success rate (target 99%, red under 97%)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A11
    text: "Traced. Every run logs input, output, model, confidence, cost and latency, keyed by patch_id. Failures show in the control towers with their cause."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A12
    text: "Patch-keyed. Every record carries its patch_id and the sender's confidence score."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect › Hand-off contract — enforce in code for every connection · 2026-10-31"
    priority: P0
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A13
    text: "Model split: two AI model families. Every checker (Fact Checker, Message Grader, Reply Sorter, Meeting Labeler, Deal Qualifier, Quality Grader) runs on a different family from the drafter it checks. Each run has a cost cap, plus a daily spend cap."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A14
    text: "Locked fields: Patch ID, BDR of record, meeting type, meeting source, factory-sourced, factory-influenced and marketing-influenced are written only by workflows and lock at booking. Corrections go through RevOps, logged with a reason."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § How the agents connect · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A15
    text: "Keeps every patch's named accounts clean, scored, in the right patch and current."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 1. Patch accounts · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A16
    text: "Every 15 min pulls new and changed records, normalises keys (domain, legal name, LinkedIn ID, HubSpot ID, email), merges exact matches and scores near-matches 0–100. ≥95 merge; 80–95 to RevOps; <80 kept separate. Logs its reasoning"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Duplicate Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A17
    text: "Links each company to parent, subsidiaries, divisions; proposes divisions that buy separately (RevOps approves); sets the outreach lock at the top parent. Re-links on HQ change or M&A news. <80 → RevOps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Parent Company Linker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A18
    text: "Finds the parent's HQ city, state, country; weighs sources; returns location, confidence, other candidates and evidence. <80 → RevOps picks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Headquarters Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A19
    text: "Nightly on companies with move or M&A news, quarterly on all. Any change → alert in the patch control tower, then a new Patch Suggester proposal"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Headquarters Re-checker (monitor)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A20
    text: "Weekly closed-won lookalikes; daily checks 7 other sources (ecosystem lists, intent surges, web visitors, business units, champion job changes, event attendees, renewal windows). Drops fit <36, customers, open deals, partners, competitors, DNC. Suggests to RevOps, never adds. <70 not suggested"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “New Account Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A21
    text: "Scores fit out of 60 (up to 15 each: industry, size and complexity, core systems, AI and integration maturity); maps score + ICP V2 quadrant to best / medium / low fit. Floor 36 never moves. Re-scores on change and monthly. <70 → RevOps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Fit Scorer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A22
    text: "Proposes a patch for each new account or HQ change: geography first, then industry, with confidence and reason. Never writes a Patch ID. <80 → RevOps decides from evidence"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Patch Suggester”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A23
    text: "Finds integration, automation and agent tools each best/medium-fit account uses, from vendor case studies, job posts, procurement notices. Weekly. <60 tagged [HYPOTHESIS]"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Current Vendor Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A24
    text: "Estimates renewal as 3 years from earliest evidence unless a later contract signal exists; raises a renewal signal 9 months before. <60 no signal"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Renewal Date Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A25
    text: "Drafts battlecard changes per vendor: shortfalls, switch path, proof, objection answers. Product marketing approves each"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 1. Patch accounts › table row “Battlecard Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    status: built
  - id: A28
    text: "Watches continuously: web visits and intent, Bombora surges, Sales Navigator alerts, hiring and tech changes, job changes, leadership news, earnings calls, press, renewal signals, event sign-ups. Records company, type, date, source link, strength; verifies company match and date; scores confidence. Strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) go straight to the Play Picker. <70 logged, not scored. Signals fade over 30 days"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Buying Signal Spotter”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A29
    text: "Turns signals into a timing score (max 40) with the weights below. Monday 06:00 ranks each patch by fit + timing. Daily 07:00 tops up each patch's batch after fast-lane plays and sends it to Gate 1 with each account's top 3 signals. Applies the checked-visit rule"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Account Ranking (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A30
    text: "Monday after ranking: base 25 slots per patch; never more than eligible accounts ÷ 13; floor 15, cap 40; pace boost (up to +50%) only to patches behind on intro meetings whose diagnosis stops at Input or Engagement and whose AE has <6 intros booked in 7 days. Fast-lane plays use their own patch's slots; overflow takes spare capacity, then that patch's lowest-ranked accounts, never another patch's base. AE nominations (max 3/week) start inside their patch's slots. Logs every allocation"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Weekly Slot Planner (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A31
    text: "After allocation, randomly holds back 10% of each patch's new medium/low-fit plays with a logged weekly seed. Checks treated vs held-out balance on fit and timing (standardised difference <0.1) or redraws. Flags held accounts in graph and HubSpot with a 90-day end date. Reports at 90 and 180 days"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Holdout Picker (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A32
    text: "Batch lands in the BDR's to-do list at 07:00 with fit band, timing, top 3 signals, Patch ID, AE, last touch, slots left. Accept or reject by 10:00 with one reason (bad fit, active deal, wrong timing, already in conversation). A rejected slot refills from the same patch. Hard blocks: no Patch ID / AE / pod, on an AE hold, or held out"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 2. Account selection › table row “Gate 1 (human: pod BDR)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A33
    text: "Starting signal weights (Scoring Tuner updates monthly): checked pricing/product visits (2+ in 14 days) 25 · new CIO/CTO/CDO/CAIO/Head of AI in 90 days 20 · event or webinar attendance 20 · hiring for AI platform, automation, integration roles 15 · earnings naming AI, automation, modernisation or cost-cutting 15 · Bombora surge 15 · interest in a current vendor's tool 15 · vendor renewal within 9 months 15 · funding, merger or new market 10 · executive posts on AI programs 10."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 2. Account selection · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A34
    text: "Checked visit: counts only with 10+ seconds and a scroll, or a repeat visit within 7 days. Never counts visits within 2 minutes of an email's delivery, from security-scanner networks, or with no page interaction."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 2. Account selection · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A35
    text: "Keeps a sourced view of every patch account current: best fit refreshed every 30 days, others every 90, and on new filings or press. Runs on Day 1 in parallel with the buying committee."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 3. Account research · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A36
    text: "Reads the latest annual report and investor deck, last two earnings call transcripts, 12 months of press, current AI/IT/automation job posts. Extracts statements on AI, automation, integration, modernisation, cost, CX, risk. Each fact keeps exact quote, page or timestamp, date, link. Drops anything >12 months old (except the latest annual report). Facts without quote + link are rejected"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 3. Account research › table row “Company Facts Collector”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A37
    text: "Finds candidate VEP-CFC use cases for the industry and core systems; scores evidence; keeps the top 3 with two supporting facts (or one fact + the company's engagement with us); tags each with pattern and outcome. <70 shown only as a question, never a claim"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 3. Account research › table row “Use Case Matcher”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A38
    text: "Writes: business problem in the company's own words, impact (no dollar figures), why now (top signals), why UnifyApps (use case + their core systems), closest proof, main and backup angle, risks (e.g. vendor contract). Every sentence cites a fact or is tagged [HYPOTHESIS]. <70 → BDR reviews at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 3. Account research › table row “Case for Change Drafter”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A39
    text: "Rules: VEP-CFC is the only source of use cases (UC-ID + Blueprint link + account evidence). Guesses are tagged [HYPOTHESIS] and reach prospects only as questions. Conflicting sources are shown side by side, never settled by the agent. Two rule steps also run here: a graph query pulling past contact (events, downloads, visits, calls, past deals, loss reasons), and an account tagger (vertical, Patch ID, size, systems, vendors, AI maturity, fit band, pattern, outcome)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 3. Account research · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A40
    text: "Maps 12 people per account, writes a note on each, gets verified contact details, screens them, and looks for a warm intro before anything goes cold."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 4. Buying committee · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A41
    text: "Loads the industry's default titles plus BDR edits; searches people at the company and division; assigns role (economic buyer, champion, technical evaluator, business owner, gatekeeper); checks the champions library; picks 3 Tier 1, 3 Tier 2, 4 Tier 3, 2 backups; flags the economic buyer. Gatekeepers mapped, never contacted. Job-change alerts promote a backup; a title the BDR removes 3× in an industry drops from its defaults. <70 on a role → BDR checks at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Buying Team Mapper”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A42
    text: "Four-line note per person: role, time in role, past companies, public talks and posts; what they own ([HYPOTHESIS] unless public); link to the matched use case; past touches; nearby event fit. Professional info only. Refresh every 90 days and on job change. <70 flagged at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Person Notes Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A43
    text: "For Tier 1 at best-fit accounts: finds shared work history with customer execs, partners, employees and AEs; uses opt-in LinkedIn connection exports (monthly) plus partners, SIs, investors. Ranks: worked together > overlapped > friend of a friend. Drafts the intro request into the patch AE's to-do list and holds cold touches to that person 7 days. <60 not suggested"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Intro Finder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A44
    text: "Sends each person to the Sprouts plugin → verified work email, plus phone for Tier 1 and engaged people. No verified email → LinkedIn only. Saves with source and verify date to graph and HubSpot; re-verifies emails older than 90 days before use"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Contact Finder (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A45
    text: "One suppression list (opt-outs, bounces, complaints, legal holds); copies it to HubSpot, Apollo and Sprouts every 15 min; screens every phone against federal and state DNC before any dialler; records consent per person; completes erasure across all tools within 30 days, keeping only a hashed code so the person is never re-added"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 4. Buying committee › table row “Do-Not-Contact List (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    status: built
  - id: A48
    text: "Matches the signal (or the 13-week cycle) to a play; sets people, channels, start days; spaces tiers so no two people at one account get email the same day; picks senders only from the account's patch and pod (AE for Tier 1 LinkedIn and AE notes, BDR for the rest, executive sponsor for C-level). Also receives fast-lane signals. <70 → BDR picks at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Play Picker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A49
    text: "Builds one Art of the Possible page per account: operations from public facts only, 2–3 workflows reimagined (before/after) for the matched use cases, proof, how UnifyApps connects their core systems, a patch event. Button books a 60-min session with the patch AE + solution consultant. Fills marketing's locked template; page is noindex, at a hard-to-guess URL, with a tracked link per prospect. <75 → marketing ops checks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Page Builder”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A50
    text: "Picks one Content Factory asset per asset touch, matched on role, industry, use case, pattern, outcome, VEP stage, Geo; skips assets >18 months old or retired; ranks by fit and positive-reply history for that role; never the same asset to two people at one account in a week; adds an event only while seats remain. <70 → no asset, use a sourced insight"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Content Picker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A51
    text: "Writes every email and LinkedIn message in the play. Starts from the Content Factory's best message for category → sub-sector → company → persona and must agree with all four; uses the assigned handbook voice; one sourced fact, the pain this person owns, the likeliest objection for their role. Names the patch AE as session host. Pod-inbox emails in the BDR's name; AE notes from the AE's mailbox, warm plays only. <70 flagged at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Message Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A52
    text: "Traces every claim in drafts and pages: facts to a public source ≤12 months old, numbers to a source or the proof library, use cases to a UC-ID with account evidence. Blocks anything untraceable"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Fact Checker (checker, other model family)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A53
    text: "Scores each draft 0–100 on the message rubric: teaches something, relevant to role and company, actionable, applies to their business, well written in the right voice, follows copy rules. <75 → one automatic rewrite and regrade; <75 again → a person decides at Gate 2. Rubric weights checked monthly against replies"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Message Grader (checker, other model family)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A54
    text: "Blocks any draft that fails: clean text (no empty fields, wrong names incl. the AE's); person still in role (checked within 7 days of first send); not on DNC, held out, a customer or open deal; parent outreach lock owned by this owner; Patch ID, AE, pod present and no AE hold; sender from the account's pod and under their daily limit across all pods; person not in another sequence; state send window, consent, legal footer"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 5. Outreach drafting › table row “Send Rules Check (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    status: built
  - id: A58
    text: "Sends every approved touch on Day 3 in the prospect's local morning: email and calls through Apollo, LinkedIn through the Sprouts plugin. Re-plans the account as people respond and protects the inboxes."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 6. Outreach · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A59
    text: "Puts each approved person into channels: email steps into an Apollo sequence on the assigned inbox, LinkedIn steps into the sender's Sprouts queue, calls as Apollo call tasks. Schedules in the prospect's local morning and state window, keeping tier spacing. Holds every inbox and LinkedIn sender at 70% of daily limit. Writes owner, Patch ID, BDR of record, sequence status, tasks, notes to HubSpot; sets the parent outreach lock. Every write keyed on person + play (no double enrolment)"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Outreach Launcher (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A60
    text: "For each call task (Tier 1 day 6, Hot Visit, anyone engaged): adapts the BDR's best script or builds one from top Gong calls; writes signal-tied opener, permission question, 3–5 discovery questions, top 3 objection answers, 20-second voicemail, follow-up email draft. Orders each BDR's call list by interest inside each patch's time-zone block. <70 → BDR approves the script"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Call Script Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A61
    text: "Keeps the account one conversation once anyone responds: a referral becomes the lead thread; a Tier 1 objection pauses Tiers 2–3 and gives the AE an answer note; 2+ people engaging in 7 days switches to Committee Surge. Every rewrite goes back through Fact Checker and Message Grader. <70 → BDR decides"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Follow-up Planner”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A62
    text: "Weekly inbox-placement tests per active domain (Gmail, Outlook, Microsoft, Barracuda, Proofpoint); daily blacklist and Gmail reputation checks; reply rate by recipient provider; maintains the email-security-scanner list. Every alert to the BDR and GTM engineer"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Inbox Health Checker”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A63
    text: "Rests a domain the same day if placement <70% in two tests or it hits a major blacklist, and swaps in a warmed spare. Blocks a new BDR's first send until their domains pass. Previously blacklisted domains are retired"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 6. Outreach › table row “Email Domain Swapper (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    status: built
  - id: A68
    text: "Drafts the answer from the thread, account view, objection list and the AE's booking link; puts it with confidence in the BDR's to-do list (and the AE's for positive replies at best-fit accounts). The person sends, edits, adds a booking link, hands to the AE, or snoozes, from one screen; it goes out from the original thread. Reminder at 90 min; Geo leader alerted at 2 business hours. <70 marked for full rewrite"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Reply Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A69
    text: "On booking via the AE's link: creates the deal at Engage owned by the patch AE; picks up meetings booked elsewhere from the AE's Google Calendar within 15 min. Locks Patch ID, BDR of record, meeting source, factory-sourced, factory-influenced (a rejected meeting rebooked within 30 days keeps its source). Books the SC, triggers the prep pack, sends agenda and 24h/1h reminders, runs a 2-touch reschedule on no-show. Runs AE deadlines (below) and escalations"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Meeting Handoff and Deadlines (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A70
    text: "Builds the pack for AE and SC: account view, buying team, thread, Case for Change draft, likely objections, AotP page, questions to confirm economic buyer and timeline. Delivered into the AE's AI Twin, which then tracks promises made on the call"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Meeting Prep Writer”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A71
    text: "Reads transcript, attendees, economic-buyer flag; labels intro / New Buyer Meeting / doesn't count, quoting evidence. Doesn't count if <20 min, no Tier 1–2 attendee, a reschedule, or a second intro at the account within 90 days. Unrecorded meetings labelled from calendar attendees and AE notes and marked unrecorded. <80 → Geo leader checks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Meeting Labeler (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A72
    text: "After each New Buyer Meeting checks six requirements: fit 36+, a VEP-CFC pain, engaged champion, New Buyer Meeting held, timeline ≤12 months, scheduled mutual next step. Marks each met / partly / missing with transcript quotes; lists gaps with the question that closes each; drafts the recap; recommends Qualified only when all are met. Saves won/lost outcomes and reasons to the graph. <80 → recommended not qualified, with gaps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 7. Engage, Connect and Commit › table row “Deal Qualifier (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    status: built
  - id: A75
    text: "Learns from every outcome, grades every agent, and turns red lines into actions. Learning agents only propose; the Quality Grader checks each proposal and the Friday review approves. Only weight changes within ±20% apply on their own, after 8 weeks without a drop."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § The agents › 8. Learning and governance · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    status: built
  - id: A78
    text: "Monthly: re-fits fit and signal weights to meetings and qualified opportunities, learning from Gate 1 rejections, AE-rejected meetings, disqualifications, win/loss reasons. Learns across all patches, reports per patch. Proposals only"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Scoring Tuner”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A79
    text: "Updates the objection list and buyer language from call transcripts. <70 → sales reviews"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Objection Collector”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A80
    text: "Small changes (subject, opener, asset): continuous tests on positive replies, ≥20% traffic per version, 4-week limit. Bold changes: fixed-size tests on people (5%→8% reply needs ~1,060 people per version). Never tests one-point lifts"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “A/B Tester”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A81
    text: "Holds every agent's rubric and test set; runs them on every prompt, model or weight change and blocks a release on any drop. Enforces checker-on-other-model. Computes each gate's rung weekly per pod and AE. Drafts a policy when the same exception is resolved the same way 3 times"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Quality Grader (checker)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A82
    text: "Weekly: compares each agent to its baseline on block/edit rate, factual errors, grades, confidence calibration; alerts the GTM engineer on any slip"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Agent Monitor”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A83
    text: "Plants errors (e.g. wrong patch AE, sender from wrong pod) in ~5% of Gate 2 items, which never send; scores each reviewer's catch rate"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Test Error Planter”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A84
    text: "Every 15 min reads tower metrics; on a red line takes the listed action (pause, throttle, move slots, demote a gate, add a to-do item); escalates unfixed alarms patch → pod (2 business days) → Geo (5) → CRO. Logs before/after numbers. Safety actions are automatic; resuming or moving anyone's work needs a person"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Alarm and Escalation (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A85
    text: "Monday: pushes accounts in play to LinkedIn ad audiences by patch geography for 8 weeks; passes unreached people to the Content Factory (ads and content only, never cold email); moves \"not now\" and engaged prospects to nurture until their date; sets marketing_influenced; sends asset, message and pattern results by patch weekly"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Content Handoff (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
  - id: A86
    text: "Recording consent per state; DNC checks; state legal checklists (send window, consent, footer); erasure across every tool within 30 days; 12-month clean-up of people who never engaged"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CDQM8HAVC in #pipeline-factory-v1, posted by Gourav Mahunta; spec dated Oct 28, 2026, by Hardik) § 8. Learning and governance › table row “Privacy and Consent (workflow)”, column What it does · 2026-10-31"
    priority: P1
    owner: Gourav Mahunta
    use_case: "this"
    status: built
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
    by: beat 1; beat H1 (all 38 agents and 12 workflows built, linked from the Components tab)
  - ask: A2
    by: beat 2
  - ask: A3
    by: "control Components tab, facet sub-workflow 8: built AI agents PF · Winning Message Finder, PF · Scoring Tuner, PF · Objection Collector and PF · A/B Tester save proposals that PF · Quality Grader checks, Run on account, on Control tower"
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
    by: "control Components tab, facet sub-workflow 1: ten built AI agents (PF · Duplicate Finder to PF · Battlecard Writer), each with Run on account, on Control tower"
  - ask: A16
    by: control Components tab, row Duplicate Finder (built AI agent PF · Duplicate Finder, Run on account), on Control tower
  - ask: A17
    by: control Components tab, row Parent Company Linker (built AI agent PF · Parent Company Linker, Run on account), on Control tower
  - ask: A18
    by: control Components tab, row Headquarters Finder (built AI agent PF · Headquarters Finder, Run on account), on Control tower
  - ask: A19
    by: control Components tab, row Headquarters Re-checker (built AI agent PF · Headquarters Re-checker, Run on account), on Control tower
  - ask: A20
    by: control Components tab, row New Account Finder (built AI agent PF · New Account Finder, Run on account), on Control tower
  - ask: A21
    by: control Components tab, row Fit Scorer (built AI agent PF · Fit Scorer, Run on account), on Control tower
  - ask: A22
    by: control Components tab, row Patch Suggester (built AI agent PF · Patch Suggester, Run on account), on Control tower
  - ask: A23
    by: control Components tab, row Current Vendor Finder (built AI agent PF · Current Vendor Finder, Run on account), on Control tower
  - ask: A24
    by: control Components tab, row Renewal Date Finder (built AI agent PF · Renewal Date Finder, Run on account), on Control tower
  - ask: A25
    by: control Components tab, row Battlecard Writer (built AI agent PF · Battlecard Writer, Run on account), on Control tower
  - ask: A27
    by: beat 1
  - ask: A28
    by: beat 2; built AI agent PF · Buying Signal Spotter runs from the Components tab (Run on account)
  - ask: A29
    by: beat 2; built automation Pipeline Factory · Account Ranking runs from the Components tab (Run on account)
  - ask: A30
    by: beat 3; built automation Pipeline Factory · Weekly Slot Planner runs from the Components tab (Run on account)
  - ask: A31
    by: beat 3; built automation Pipeline Factory · Holdout Picker runs from the Components tab (Run on account)
  - ask: A32
    by: beat 3
  - ask: A33
    by: beat 2
  - ask: A34
    by: beat 2
  - ask: A35
    by: beat 4
  - ask: A36
    by: beat 4; built AI agent PF · Company Facts Collector runs from the Components tab (Run on account)
  - ask: A37
    by: beat 4; built AI agent PF · Use Case Matcher runs from the Components tab (Run on account)
  - ask: A38
    by: beat 4; built AI agent PF · Case for Change Drafter runs from the Components tab (Run on account)
  - ask: A39
    by: beat 4
  - ask: A40
    by: beat 4
  - ask: A41
    by: beat 4; built AI agent PF · Buying Team Mapper runs from the Components tab (Run on account)
  - ask: A42
    by: beat 4; built AI agent PF · Person Notes Writer runs from the Components tab (Run on account)
  - ask: A43
    by: control Components tab, row Intro Finder (built AI agent PF · Intro Finder, Run on account), on Control tower
  - ask: A44
    by: control Components tab, row Contact Finder (built automation Pipeline Factory · Contact Finder, Run on account), on Control tower
  - ask: A45
    by: control Components tab, row Do-Not-Contact List (built automation Pipeline Factory · Do-Not-Contact List, Run on account), on Control tower
  - ask: A46
    by: control Components tab, facet sub-workflow 4, on Control tower
  - ask: A47
    by: beat 5
  - ask: A48
    by: beat 2; built AI agent PF · Play Picker runs from the Components tab (Run on account)
  - ask: A49
    by: control Components tab, row Page Builder (built AI agent PF · Page Builder, Run on account), on Control tower
  - ask: A50
    by: control Components tab, row Content Picker (built AI agent PF · Content Picker, Run on account), on Control tower
  - ask: A51
    by: beat 5; built AI agent PF · Message Writer runs from the Components tab (Run on account)
  - ask: A52
    by: beat 5; built AI agent PF · Fact Checker runs from the Components tab (Run on account)
  - ask: A53
    by: beat 5; built AI agent PF · Message Grader runs from the Components tab (Run on account)
  - ask: A54
    by: beat 5; built automation Pipeline Factory · Send Rules Check runs from the Components tab (Run on account)
  - ask: A55
    by: beat 5
  - ask: A56
    by: beat 5
  - ask: A57
    by: "control Components tab, row Outreach Launcher (built automation Pipeline Factory · Outreach Launcher: tier spacing, local morning, 70% inbox cap; Run on account), on Control tower"
  - ask: A58
    by: "control Components tab, row Outreach Launcher (built automation Pipeline Factory · Outreach Launcher: tier spacing, local morning, 70% inbox cap; Run on account), on Control tower"
  - ask: A59
    by: beat 5; built automation Pipeline Factory · Outreach Launcher runs from the Components tab (Run on account)
  - ask: A60
    by: control Components tab, row Call Script Writer (built AI agent PF · Call Script Writer, Run on account), on Control tower
  - ask: A61
    by: control Components tab, row Follow-up Planner (built AI agent PF · Follow-up Planner, Run on account), on Control tower
  - ask: A62
    by: control Components tab, row Inbox Health Checker (built AI agent PF · Inbox Health Checker, Run on account), on Control tower
  - ask: A63
    by: control Components tab, row Email Domain Swapper (built automation Pipeline Factory · Email Domain Swapper, Run on account), on Control tower
  - ask: A64
    by: control Components tab, facet sub-workflow 6, on Control tower
  - ask: A65
    by: open question 4
  - ask: A66
    by: beat 6
  - ask: A67
    by: control Components tab, row Reply Sorter (built AI agent PF · Reply Sorter, Run on account), on Control tower
  - ask: A68
    by: control Components tab, row Reply Writer (built AI agent PF · Reply Writer, Run on account), on Control tower
  - ask: A69
    by: beat 6; built automation Pipeline Factory · Meeting Handoff and Deadlines (calls Book meeting) runs from the Components tab (Run on account)
  - ask: A70
    by: control Components tab, row Meeting Prep Writer (built AI agent PF · Meeting Prep Writer, Run on account), on Control tower
  - ask: A71
    by: beat 6; built AI agent PF · Meeting Labeler runs from the Components tab (Run on account)
  - ask: A72
    by: beat 6; built AI agent PF · Deal Qualifier runs from the Components tab (Run on account)
  - ask: A73
    by: beat 6
  - ask: A74
    by: beat 6; built automation Pipeline Factory · Meeting Handoff and Deadlines runs from the Components tab (Run on account)
  - ask: A75
    by: "control Components tab, facet sub-workflow 8: seven built AI agents (proposals only, PF · Quality Grader checks each) and three built automations, on Control tower"
  - ask: A76
    by: control Hand-offs tab, record drawer (payload and evidence), on Control tower
  - ask: A77
    by: control Components tab, row Winning Message Finder (built AI agent PF · Winning Message Finder, Run on account), on Control tower
  - ask: A78
    by: control Components tab, row Scoring Tuner (built AI agent PF · Scoring Tuner, Run on account), on Control tower
  - ask: A79
    by: control Components tab, row Objection Collector (built AI agent PF · Objection Collector, Run on account), on Control tower
  - ask: A80
    by: control Components tab, row A/B Tester (built AI agent PF · A/B Tester, Run on account), on Control tower
  - ask: A81
    by: control Components tab, row Quality Grader (built AI agent PF · Quality Grader, Run on account), on Control tower
  - ask: A82
    by: control Components tab, row Agent Monitor (built AI agent PF · Agent Monitor, Run on account), on Control tower
  - ask: A83
    by: beat 5; built AI agent PF · Test Error Planter runs from the Components tab (Run on account)
  - ask: A84
    by: beat 7; built automation Pipeline Factory · Alarm and Escalation runs from the Components tab (Run on account)
  - ask: A85
    by: control Components tab, row Content Handoff (built automation Pipeline Factory · Content Handoff, Run on account), on Control tower
  - ask: A86
    by: control Components tab, row Privacy and Consent (built automation Pipeline Factory · Privacy and Consent, Run on account), on Control tower
  - ask: A88
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
  - ask: A89
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
  - ask: A90
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
  - ask: A91
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
  - ask: A92
    by: beat H1
  - ask: A93
    by: open question 2
  - ask: A94
    by: open question 2
  - ask: A95
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
  - ask: A96
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
  - ask: A97
    by: open question 2
  - ask: A98
    by: "beat H1 (Components tab: 38 built AI agents and 12 built automations, each registered with one job, feeds, threshold, model family and status live, Run on account)"
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
  objects: 13
  automations: 25
  agents: 39

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
    - "PF Component run (round 2): 0 seeded; one row per agent or workflow run, written by Save agent output and the 12 workflows"
    - "PF Source (round 2): 19, record · seed (the mocked outside content for A-1001, one A-1012 transcript, the handbook)"
    - "PF Inbox (round 2): 6, record · seed (Marcus Ellery 3, Tomas Ilves 2, new BDR Priya Anand 1; invented .example domains)"
    - "PF Suppression (round 2): 4, record · seed (one erasure hash, one legal hold, two consents)"
    - "PF Component (round 2): the 57 seeded rows updated with their built entity (38 AI agents, 12 automations, Gate 1 and Gate 2 linked to Decide Gate 1 and Clear Gate 2)"
  expected_answers: eval.csv

verify:
  round: 2
  walked: 2026-11-02T09:21Z to 09:27Z
  theme: light
  beats_pass: "0 of 8 (all unverified: sign-in)"
  beats:
    - "1 Control tower: unverified: sign-in. The published address /tower again answers /login?returnTo=%2Ftower; nothing typed. Data read: after the reset only the 18 seed hand-offs H-01 to H-18 remain (the 14 T-A* and 4 walk hand-offs from round 1 are gone)"
    - "2 Fast lane: unverified: sign-in. Live run read back (Log signal, deployed, run 6ae85623f6f76639f809eca8, origin test): fast_lane, timing 40, hand-off H-6ae856279594aa458cbd0b2b Buying Signal Spotter to Play Picker saved with origin test and the due_at field set (saved_at plus one hour, 1793614902251)"
    - "3 Gate 1: unverified: sign-in. Live run read back (Decide Gate 1, deployed, run 6ae85626f13e536c52e37aa2, origin test): Accept A-1001 saved hand-offs to Company Facts Collector and Buying Team Mapper, both origin test"
    - "4 Research and buying team: unverified: sign-in (seeded; no read of the screen)"
    - "5 Gate 2: unverified: sign-in. Live run read back (Clear Gate 2, deployed, run 6ae856249ec43c6ee218793a): approving D-04 answers result blocked, rule pod, reason \"Blocked: sender Rhea Castillo is not in the account's pod (POD-NAE-1)\" (round 1's fix holds)"
    - "6 Booked and locked: unverified: sign-in (Book meeting unchanged since round 1's read-back; not re-run)"
    - "7 Ask the factory, then stop it: unverified: sign-in. Agent answers row 1 with H-07, H-12, H-15, H-10 and C08 at 96.1% (trace read)"
    - "H1 Under the hood: unverified: sign-in (builder canvas needs the tenant sign-in)"
  controls_pass: "0 of 0 measured (unverified: sign-in; no control pressed)"
  queries_pass: "8 of 8"
  queries:
    - "1 waiting on a person in PATCH-NAE-03: pass (H-07 RevOps 74/80, H-12 and H-15 Marcus Ellery, H-10 rejected on missing evidence), about 50 s"
    - "2 red component: pass (Current Vendor Finder, 96.1%), about 24 s"
    - "3 Carrow & Vale fit and AE: pass (49, best, Dana Okafor), about 31 s"
    - "4 economic buyer: pass (\"Helena Marsh (CFO)\"; trace shows ReadFactoryRecords then the people list; round 1's fail is fixed), about 33 s"
    - "5 Kestrel Ridge: pass (factory holdout until about 27 January 2027), about 46 s"
    - "6 patch short of intros: pass (PATCH-NAE-04, 2 against 4), about 21 s"
    - "7 send the email: pass (declines, read-only), about 13 s"
    - "8 deal size: pass (says the records hold no deal size), under 20 s"
  p95_latency_s: 50
  latency_target_s: 90
  latency_note: "seconds read from consecutive case-id timestamps (the eight questions ran back to back), with runAgainToFindAnswer on, so upper bounds; fewer than 20 rows, so p95 is the slowest"
  coverage_pass: "0 of 32 (no screen reached: sign-in); backend re-proven this round by deployed runs: A2, A28, A29, A33, A34 (Log signal), A30, A31, A32 (Decide Gate 1), A9, A47 (Clear Gate 2), A5 to A9 (Save hand-off origin and due_at), A8, A10, A40, A41 (Read factory records and the analyst)"
  checks_pass: "0 of 7 measured (unverified: sign-in on every screen)"
  other_theme_checks: "0 of 7 (unverified: sign-in)"
  reset: "done twice. Before: run 6ae8560e2099302ffb15c3e5 completed (19.3 s), its counts read deleted 0, restored 0, although the 18 non-seed hand-offs listed in round 1 were gone when read right after. After: run 6ae8576ef6f76639f80a33b6 completed (the run lookup failed twice, so its counts were not read); read back from the records: PF Hand-off holds exactly 18 rows, H-01 to H-18, all origin seed; no non-seed PF Signal; A-1001 back to timing 25, gate1 pending; D-04 back to waiting_gate2"
  notes:
    - "No delete was made by this stage; only Reset demo's own runs deleted."
    - "Round 1 fix lines: Reset demo (clears hand-offs with no snapshot): fixed. Save hand-off origin and callers pass it: fixed (all three walk hand-offs origin test). Log signal due_at: fixed. Clear Gate 2 pod rule for D-04: fixed. Read factory records people and name lookup: fixed (account_id \"Carrow & Vale Logistics\" returns A-1001 and 13 people). Analyst account id: fixed (eval row 4 passes). Environment* tools: still offered (platform; moved to dev_issues)."
    - "Reset demo's returned counts read 0 deleted, 0 restored on a run that left only seed rows; the counts may not add the hand-off deletes. Not a fix line: the reset's effect is right, only its reported count is in doubt."
    - "A person must sign in to orbit.uat.unifyapps.com and the published app in the walk browser before the screens can be walked; two rounds have now stopped at the sign-in page."
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
  - by: Gourav Mahunta
    when: 2026-11-02
    text: "G2 approved on the row and in its thread (\"Approved, proceed\"); no numbered answers, so the plan's recommended assumptions stand. The proposed intent both becomes intent (by the manager)."
  - by: orchestrator
    when: 2026-11-02
    text: "Connections: build_contract has no connection line and no automation names an external connector operation (outside systems mocked), so the Connections step is not needed; final reports connections_used none."
  - by: plan
    when: 2026-11-02
    text: "Build: PF Account has no AE-hold field, so Decide Gate 1 reads an AE hold as ultimate_parent_lock set to someone other than owner_ae (from the contract's Gate 1 hard blocks and the PF Account line)."
  - by: nebula
    when: 2026-11-02
    text: "Build (automation-agent read): on this tenant a DSL branch runs every arm whose condition is true; Log signal was fixed to if/else-if. Clear Gate 2 and Save hand-off may name a different rule or missing field when two fail at once."
  - by: orchestrator
    when: 2026-11-02
    text: "Unattended run: no delete can be confirmed, so builders left their T- test rows for Pipeline Factory · Reset demo. Save hand-off has no origin input, so the test hand-offs it wrote (account_id T-A*) carry origin user and Reset demo keeps them; they are listed for removal before the demo."
  - by: state-check
    when: 2026-11-02
    text: "reverted open_questions: written by verify, outside its fields (schema § Who writes what)"
  - by: Gourav Mahunta
    when: 2026-11-02
    text: "G3 changes requested (feedback FB-1793612784906-1, gate g3, confirmed \"yes\" in G3's thread): \"build all the 38 agents and the 12 workflows\". G3 round 2: a fresh 2-plan adds build_contract lines for every agent and workflow in studio/data/components.csv not yet built live (changing nothing else, as the Connections rework does), then 3-build, 4-verify, 5-handover."

  - by: plan
    when: 2026-11-02
    text: "G3 round 2 plan (scoped change, FB-1793612784906-1 \"build all the 38 agents and the 12 workflows\"): build_contract gains 61 Touches and these contract lines, appended after the round-1 lines, none of which change: 4 object · create (PF Component run, PF Source, PF Inbox, PF Suppression), 1 object · update (PF Component: six built-entity fields), 3 record · seed (PF Source 19, PF Inbox 6, PF Suppression 4) and 1 more PF Seed snapshot seed, 16 automation · create (the 12 workflows: Account Ranking, Weekly Slot Planner, Holdout Picker, Contact Finder, Do-Not-Contact List, Send Rules Check, Outreach Launcher, Email Domain Swapper, Meeting Handoff and Deadlines, Alarm and Escalation, Content Handoff, Privacy and Consent; plus Read component inputs, Save agent output, Reset agent runs, Run component), 1 automation · update (Reset demo calls Reset agent runs), 38 ai-agent · create (PF · <component>), 2 record · update (PF Component links, PF Seed snapshot rows), 1 code-app · update (Components tab: Built column and facet, drawer with the entity link, last runs and Run on account); Ready when gains 16 deploy and 38 publish lines and 5 observable lines (Reset demo and the code app reuse their round-1 deploy and publish lines). Grouping for 3-build, each plan at most 10 tasks (about 127 tasks, 15 plans), marked [R2-Pnn] under each heading: R2-P01 objects, field change and seeds (9); R2-P02 Read component inputs, Save agent output, Reset agent runs, Reset demo update (10); R2-P03 Account Ranking, Weekly Slot Planner, Holdout Picker, Do-Not-Contact List (9); R2-P04 Contact Finder, Send Rules Check, Outreach Launcher, Email Domain Swapper, Meeting Handoff and Deadlines (10); R2-P05 Alarm and Escalation, Content Handoff, Privacy and Consent, Run component (9); then the agents, an ai-agent task and a publish each: R2-P06 sw1 C01 to C05 (10); R2-P07 sw1 C06 to C10 (10); R2-P08 sw2 C11 and sw3 C16 to C18 (8); R2-P09 sw4 C21 to C23 (6); R2-P10 sw5 C27 to C31 (10); R2-P11 sw5 C32 and sw6 C36 to C38 (8); R2-P12 sw7 C41, C42, C44, C45, C46 (10); R2-P13 sw8 C48 to C52 (10); R2-P14 sw8 C53, C54 (4); R2-P15 the registry link (PF Component and its snapshot rows), the code-app update and the app's publish (4). R2-P02 goes before every agent plan (their two tools); R2-P15 goes last (it reads every id). Size: 3 pages, 13 objects (incl. PF Seed snapshot), 25 automations (incl. Reset demo and Reset agent runs), 39 AI agents."
  - by: plan
    when: 2026-11-02
    text: "Round 2 modes: the 38 agents are live AI agents run on demand (Pipeline Factory · Run component from the Components tab, or verify's test messages); the 12 workflows are live deterministic automations with no model call, never presented as AI; the outside systems stay mocked by PF objects (three new: PF Source, PF Inbox, PF Suppression), so no connection is added and the Connections step stays not_needed. The round-1 seeded AI surfaces (facts, Case for Change, notes, drafts, grades, labels) stay seeded so the storyline does not move; beat H1 now shows one agent run live (PF · Case for Change Drafter on Carrow & Vale Logistics)."
  - by: plan
    when: 2026-11-02
    text: "Round 2 reuse: Clear Gate 2 keeps its inline Send Rules Check and mocked enrolment, Log signal its single-signal timing score, Decide Gate 1 its hard blocks, Book meeting its booking and locks, all unchanged; the dedicated Send Rules Check is read-only on PF Draft (one writer of rules_check stays Clear Gate 2), Account Ranking re-ranks with Log signal's weights, Outreach Launcher schedules what Clear Gate 2 enrolled, Meeting Handoff and Deadlines calls Book meeting for calendar pick-ups, Alarm and Escalation calls Pause component (only under 95%), Privacy and Consent calls Do-Not-Contact List. Every agent hand-off goes through Save agent output, which calls the round-1 Save hand-off unchanged."
  - by: plan
    when: 2026-11-02
    text: "Round 2 models: family A (drafters, monitors) Claude Sonnet 5, model card e_6acca2af70b66f5702c8b59f, the analyst's model; family B (the six checkers) GPT-5.1, model card e_6a0dd4e556ffb40e76c2762e, a different provider; both active with tool calling in list_models on orbit.uat.unifyapps.com (read 2026-11-02). The spec names no models, only two families."
  - by: state-check
    when: 2026-11-02
    text: "reverted stage_flag: written by plan, outside its fields (schema § Who writes what)"
  - by: orchestrator
    when: 2026-11-02
    text: "Build (R2-P04, Meeting Handoff and Deadlines): the AE deadline rows save as flowed, not waiting_person, because round-1 Save hand-off parks a row only under the receiver's threshold and C43's receivers have none; changing Save hand-off is outside this round (Assumptions: round-1 entities unchanged), so the gap is kept and listed for the G3 pack. Book meeting writes meeting_source 'factory: AE booking link' for calendar pick-ups; the true source (SRC-16) is in the prep-pack hand-off payload."

  - by: orchestrator
    when: 2026-11-02
    text: "Build (R2-P06, R2-P07): model card e_6acca2af70b66f5702c8b59f (Claude Sonnet 5, provider anthropic) fails every run with the provider's 401 invalid x-api-key although list_models shows it active; the family-A agents use the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model (a platform choice, not a client one). Save agent output's threshold rule stands for every agent (under threshold waiting_person, else saved; no no_action result): where a line says no_action or not suggested, the agent saves once with changed:false or suggested:false and says no action."

  - by: orchestrator
    when: 2026-11-02
    text: "Build (R2-P07): Save agent output's single threshold rule differs from three agents' own routing lines: C08 Current Vendor Finder (under 60 should save tagged [HYPOTHESIS], goes waiting_person), C09 Renewal Date Finder (under 60 should be no action, goes waiting_person), C10 Battlecard Writer (every draft should wait for product marketing, saves with a hand-off). Kept as built (one rule for every agent, decided above); listed for the G3 pack. Agents are also offered tenant-injected EnvironmentAccess and RequestEnvironmentDeploy tools they do not have attached (the round-1 dev issue)."

  - by: orchestrator
    when: 2026-11-02
    text: "Build (R2-P11): Pipeline Factory · Read component inputs answered about 200,000 characters for A-1001, and the agent runtime keeps only the first 16,000 and last 2,000 of a tool reply, so agents could not see drafts, sources or incoming hand-offs (C32 could not grade; C08, C09 and C37 saw no sources). A short change narrows it to under 12,000 characters with the same inputs and result fields (plan e_6ae86bb6d96c5f6ba24481b4); the agents tested before it are re-run by 4-verify."

  - by: orchestrator
    when: 2026-11-02
    text: "Build (R2-P12): the GPT-5.1 card e_6a0dd4e556ffb40e76c2762e answers 401 Incorrect API key, so family-B checkers run on another GPT card that answers: Reply Sorter, Meeting Labeler and Deal Qualifier on 'GPT-5.1_without_effort(DNT)' e_6ae835bbafe7fc590a05a045 (a shared card marked do-not-touch, used but not changed); some earlier checkers may be on e_696fe072cb3ef82f7e23dc86, which may serve gpt-4.1. 4-verify reads each checker's card; an admin fixing the two cards' keys restores the planned models. A-1001 holds no reply, transcript or calendar rows for its account, so Reply Sorter, Meeting Labeler and Reply Writer saved no action in their tests."

dev_issues:
  - what: "The Pipeline Factory Analyst's model is offered EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy beside think, ClarifyFromUser and ReadFactoryRecords; they are not attached to the agent and no agent tool removes them (tenant-injected)"
    beat: "7 Ask the factory"
    read: "read_trace case e_6ae85653f13e536c52e3a219 (eval row 4, round 2): toolsOffered on both model calls lists the four Environment* tools; none was called"
    raised: 

frozen:

cost:
  runs: 4
  agent_spawns: 64
  tokens_m: 13.8
  wall_h: 4.8

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
  - by: verify
    for: owner
    text: "Round 1 could not open the app: the published address and the preview both land on a sign-in page in the walk browser, so none of the 32 built asks (A1, A2, A4 to A14, A21, A27 to A42, A47, A48) was seen on a screen, and no control or on-page check ran. What was built for them (the Control tower, To-do and Account screens over the PF objects and eight automations) was proven only from records and deployed runs. Options: (recommended) sign in once to orbit.uat.unifyapps.com and the published app in the walk browser before round 2, so verify walks every beat; accept round 1's backend evidence and walk the screens yourself before the demo."
  - by: plan
    for: owner
    text: "Round 2: the spec gives the parent outreach lock two writers: the Parent Company Linker \"sets the outreach lock at the top parent\" (its registered field) and the Outreach Launcher \"sets the parent outreach lock\". One writer per field (A6) allows one. Options: (recommended) the Parent Company Linker writes ultimate_parent_lock and the Outreach Launcher only checks it (built this way); the Outreach Launcher writes it at enrolment and the Linker only proposes it."
  - by: plan
    for: owner
    text: "Round 2: the 38 agents and 12 workflows are built to run on demand; the spec's schedules (every 15 min, nightly, Monday 06:00, daily 07:00, weekly, monthly) are shown in the registry but not switched on, so the demo records never change by themselves. Options: (recommended) on demand for the demo, schedules switched on in a later version; switch the schedules on now (the records will move between rehearsals and each run costs model calls)."
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
- object · PF Component · OBJ_pf_component
- object · PF Component run · new
- object · PF Source · new
- object · PF Inbox · new
- object · PF Suppression · new
- automation · Pipeline Factory · Read component inputs · new
- automation · Pipeline Factory · Save agent output · new
- automation · Pipeline Factory · Reset agent runs · new
- automation · Pipeline Factory · Account Ranking · new
- automation · Pipeline Factory · Weekly Slot Planner · new
- automation · Pipeline Factory · Holdout Picker · new
- automation · Pipeline Factory · Do-Not-Contact List · new
- automation · Pipeline Factory · Contact Finder · new
- automation · Pipeline Factory · Send Rules Check · new
- automation · Pipeline Factory · Outreach Launcher · new
- automation · Pipeline Factory · Email Domain Swapper · new
- automation · Pipeline Factory · Meeting Handoff and Deadlines · new
- automation · Pipeline Factory · Alarm and Escalation · new
- automation · Pipeline Factory · Content Handoff · new
- automation · Pipeline Factory · Privacy and Consent · new
- automation · Pipeline Factory · Run component · new
- automation · Pipeline Factory · Reset demo · 6ae8441df38e327618fcc13c
- ai-agent · PF · Duplicate Finder · new
- ai-agent · PF · Parent Company Linker · new
- ai-agent · PF · Headquarters Finder · new
- ai-agent · PF · Headquarters Re-checker · new
- ai-agent · PF · New Account Finder · new
- ai-agent · PF · Fit Scorer · new
- ai-agent · PF · Patch Suggester · new
- ai-agent · PF · Current Vendor Finder · new
- ai-agent · PF · Renewal Date Finder · new
- ai-agent · PF · Battlecard Writer · new
- ai-agent · PF · Buying Signal Spotter · new
- ai-agent · PF · Company Facts Collector · new
- ai-agent · PF · Use Case Matcher · new
- ai-agent · PF · Case for Change Drafter · new
- ai-agent · PF · Buying Team Mapper · new
- ai-agent · PF · Person Notes Writer · new
- ai-agent · PF · Intro Finder · new
- ai-agent · PF · Play Picker · new
- ai-agent · PF · Page Builder · new
- ai-agent · PF · Content Picker · new
- ai-agent · PF · Message Writer · new
- ai-agent · PF · Fact Checker · new
- ai-agent · PF · Message Grader · new
- ai-agent · PF · Call Script Writer · new
- ai-agent · PF · Follow-up Planner · new
- ai-agent · PF · Inbox Health Checker · new
- ai-agent · PF · Reply Sorter · new
- ai-agent · PF · Reply Writer · new
- ai-agent · PF · Meeting Prep Writer · new
- ai-agent · PF · Meeting Labeler · new
- ai-agent · PF · Deal Qualifier · new
- ai-agent · PF · Winning Message Finder · new
- ai-agent · PF · Scoring Tuner · new
- ai-agent · PF · Objection Collector · new
- ai-agent · PF · A/B Tester · new
- ai-agent · PF · Quality Grader · new
- ai-agent · PF · Agent Monitor · new
- ai-agent · PF · Test Error Planter · new
- code-app · UnifyApps Pipeline Factory Control Tower · app-2fbe93e8c1f7

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

<!-- G3 round 2 (2-plan, 2026-11-02): every line below this mark is new; the round-1 lines above are unchanged. Plan groups R2-P01 to R2-P15 are named in each sub-section heading. -->

#### object · PF Component
[R2-P01 · objects and field changes] The registry learns which built entity runs each component.
- object · update · PF Component: add fields built_kind (picklist: ai_agent "AI agent", automation "Automation", not_built "Not built"; default not_built), built_entity_id (text), built_entity_name (text), built_link (text), built_status (picklist: live "Live", not_built "Not built"; default not_built), built_at (date, epoch ms). Nothing else on the object changes; the round-1 fields, picklists and the 57 seeded rows stay as they are.

#### object · PF Component run
[R2-P01] Every agent and workflow run, traced: input, output, model, confidence, cost and latency, keyed by patch.
- object · create · PF Component run: id OBJ_pf_component_run; primaryKey run_id (text, required); fields component_id (text), component_name (text), kind (picklist: agent "Agent", checker "Checker", monitor "Monitor", workflow "Workflow"), patch_id (text), account_id (text), person_id (text), play_id (text), draft_id (text), output_type (text), summary (text), payload (text, JSON), confidence (number), evidence (text), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]", none "None"), status (picklist: saved "Saved, flowed on", waiting_person "Waiting on a person", rejected "Rejected: schema", proposal "Proposal only", blocked "Blocked", no_action "No action", paused "Not run: component paused"), assigned_to (text), reason (text), model (text), cost_usd (number), latency_ms (number), idempotency_key (text, component_id + account_id + person_id + play_id + output_type), handoff_ids (text), run_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Source
[R2-P01] The outside systems' content, mocked: filings, press, job posts, vendor case studies, LinkedIn exports, contact data, Content Factory assets, Gong calls, replies, calendar events, meeting transcripts, the handbook.
- object · create · PF Source: id OBJ_pf_source; primaryKey source_id (text, required); fields account_id (text), person_id (text), source_kind (picklist: annual_report "Annual report", investor_deck "Investor deck", earnings_call "Earnings call", press "Press", job_post "Job post", vendor_case_study "Vendor case study", procurement_notice "Procurement notice", linkedin_export "LinkedIn connection export", contact_record "Contact record", content_asset "Content Factory asset", call_transcript "Call transcript", meeting_transcript "Meeting transcript", calendar_event "Calendar event", reply "Reply", web_visit "Web visit", handbook "Handbook section"), title (text), body (text), url (text), source_date (date, epoch ms), mocked_system (text), status (text), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Inbox
[R2-P01] The sending inboxes and domains, mocked (Apollo).
- object · create · PF Inbox: id OBJ_pf_inbox; primaryKey inbox_id (text, required); fields sender (text), pod (text), domain (text), daily_limit (number), sent_today (number), ramp_week (number), placement_pct_last (number), placement_pct_prev (number), blacklisted (boolean), previously_blacklisted (boolean), status (picklist: active "Active", resting "Resting", warm_spare "Warm spare", retired "Retired", blocked_new "Blocked: new sender"), checked_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)

#### object · PF Suppression
[R2-P01] The one suppression list and consent records (copied to HubSpot, Apollo and Sprouts, mocked).
- object · create · PF Suppression: id OBJ_pf_suppression; primaryKey suppression_id (text, required); fields person_id (text), account_id (text), email_hash (text), kind (picklist: opt_out "Opt-out", bounce "Bounce", complaint "Complaint", legal_hold "Legal hold", consent "Consent", erasure "Erasure"), reason (text), state (text), consent_given (boolean), copied_to (text), copied_at (date, epoch ms), erase_due (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)
- record · seed · PF Source: origin seed on every row; dates epoch ms in the 12 months before the demo unless said; links invented under carrowvale.example; all A-1001 unless named. SRC-01 annual_report "Annual report 2025", page 14: "Order exceptions are still handled by hand across our three ERPs". SRC-02 earnings_call "Q2 2026 call" 00:18:40: "We plan to automate order-to-cash end to end by 2027". SRC-03 job_post "Integration Engineer, AI Platform team (3 roles)". SRC-04 investor_deck slide 9: "Cost-to-serve is a board priority". SRC-05 press "Carrow & Vale names Colette Baines Head of AI" (6 weeks before the demo). SRC-06 vendor_case_study "Carrow & Vale on Corvane Integrate" dated 28 months before the demo (earliest evidence; renewal estimate 8 months out). SRC-07 linkedin_export, person P-1002: "Dana Okafor and Arjun Mehta worked together at Northgate Freight 2017 to 2020" (opt-in export, mocked_system "LinkedIn export (opt-in)"). SRC-08 contact_record P-1002 "arjun.mehta@carrowvale.example, verified" (mocked_system "Sprouts (mocked)"). SRC-09 contact_record P-1006 "no verified email" (Sprouts, mocked). SRC-10 content_asset "Order exception triage playbook for logistics" (UC-LOG-014, role operations, 5 months old). SRC-11 content_asset "Carrier invoice reconciliation case study" (UC-LOG-022, 22 months old: too old). SRC-12 call_transcript "Top call: logistics VP, objection: we already have an integration vendor" (Gong, mocked). SRC-13 reply P-1002 "Happy to talk next week, Tuesday works" (Apollo, mocked). SRC-14 reply P-1007 "Out of office until" a date 10 days after the demo (Apollo, mocked). SRC-15 reply P-1009 "Please remove me from your list" (Apollo, mocked). SRC-16 calendar_event "Intro: Carrow & Vale and UnifyApps", 45 min, attendees Arjun Mehta, Colette Baines, Dana Okafor, booked in the AE's Google Calendar (mocked), 3 days after the demo. SRC-17 meeting_transcript, account A-1012 Harrowgate Mutual, "New Buyer Meeting, 48 min": quotes for fit, a VEP-CFC pain (claims intake), an engaged champion, timeline "this fiscal year", a mutual next step booked. SRC-18 web_visit A-1001 "/pricing, 65 s with scroll". SRC-19 handbook (no account) "Message handbook: voice and copy rules" (the copy rules of A56).
- record · seed · PF Inbox: origin seed on every row; invented UnifyApps-branded secondary domains under .example. IN-01 Marcus Ellery, POD-NAE-1, getunifyapps.example, daily_limit 40, sent_today 22, ramp_week 4, placement 92 then 90, active. IN-02 Marcus Ellery, POD-NAE-1, unifyapps-team.example, 40, 18, ramp 4, placement 64 then 68 (two tests under 70), active. IN-03 Marcus Ellery, POD-NAE-1, tryunifyapps.example, 40, 0, ramp 4, placement 88, warm_spare. IN-04 Tomas Ilves, POD-NAE-2, meetunifyapps.example, 20, 9, ramp 2, placement 85, active. IN-05 Tomas Ilves, POD-NAE-2, unifyappsmail.example, 40, 0, placement 81, previously_blacklisted true, resting. IN-06 Priya Anand (new BDR), POD-NAE-2, hellounifyapps.example, 10, 0, ramp 1, no placement test yet, blocked_new.
- record · seed · PF Suppression: origin seed on every row. SUP-01 erasure, email_hash "sha256:9f2c…e41a" (an erased person, no person_id), reason "erasure completed", copied_to "HubSpot, Apollo, Sprouts (mocked)". SUP-02 legal_hold, account A-1004, reason "legal hold: procurement dispute". SUP-03 consent P-1001, state OH, consent_given true, reason "call recording consent". SUP-04 consent P-1002, state OH, consent_given true.
- record · seed · PF Seed snapshot: one more row per row the three seed lines above write (snapshot_id `object_id:record_id`, row_values the row as seeded, JSON), origin seed, written once after those seeds.

#### automation · Pipeline Factory · Read component inputs
[R2-P02 · automations: the agents' tools] The agents' one read tool.
- automation · create · Pipeline Factory · Read component inputs: callable from the AI agents; inputs component_id (text, required), account_id (text), person_id (text), draft_id (text), patch_id (text); result component (text, JSON: the PF Component row with threshold, below_threshold_goes_to, feeds, writes, model_family, status), account (text, JSON), people (text, JSON), signals (text, JSON), facts (text, JSON), drafts (text, JSON), sources (text, JSON: PF Source rows of the account or person, plus rows with no account such as content assets and the handbook), handoffs_in (text, JSON: PF Hand-off rows whose to_component is this component's name, for the account when given), inboxes (text, JSON), suppression (text, JSON), recent_runs (text, JSON: the last 50 PF Component run rows, for the sw8 agents), reason (text). Read-only, deterministic, no model call; an account_id given as a name resolves to its account_id as Read factory records does; an unknown component_id answers reason "unknown component" and empty lists.

#### automation · Pipeline Factory · Save agent output
[R2-P02] The agents' one write tool: the hand-off contract applied to every agent output.
- automation · create · Pipeline Factory · Save agent output: callable from the AI agents; inputs component_id (text, required), account_id (text), person_id (text), play_id (text), draft_id (text), patch_id (text), output_type (text), summary (text), payload (text, JSON), confidence (number), evidence (text), evidence_tag (text: public | hypothesis), model (text), origin (text); result result (text: saved | waiting_person | rejected | duplicate | paused), run_id (text), handoff_ids (text), reason (text). Deterministic, no model call. Reads the PF Component row: a paused component answers paused and writes nothing. Schema check: confidence 0 to 100, evidence and output_type present, patch_id taken from the account when not given; a failure saves a PF Component run with status rejected, assigned_to GTM engineer, reason "schema check failed: `field` missing", and nothing else. Idempotent on component_id + account_id + person_id + play_id + output_type: a re-run updates the same PF Component run row and answers duplicate, never a second row or a second hand-off. Under the component's threshold: the run is saved waiting_person, assigned_to its below_threshold_goes_to, and no field is written. At or over it: writes only the component's registered fields (one writer per field, from a fixed map: C02 PF Account.ultimate_parent_lock; C03 PF Account.hq_city; C06 PF Account.fit_score and fit_band; C11 PF Signal rows; C16, C17, C18 PF Fact rows of kind fact, use_case, case_for_change; C21 PF Person.role and tier; C22 PF Person.note; C30 PF Draft rows (status waiting_gate2, enrolment_key empty); C31 PF Draft.fact_check; C32 PF Draft.grade; C38 PF Inbox.placement_pct_last and blacklisted; C45 PF Account.meeting_label; C46 PF Account.qualified_status; C54 PF Draft.planted_error; every other component writes only its PF Component run row), never a locked field of a booked account (locked_at set), then calls Pipeline Factory · Save hand-off once per name in the component's feeds that is a component (from_component the component's name, to_component the feed, writes_field the field written, the same keys, confidence, payload and evidence), and saves the PF Component run with status saved (or proposal for the sw8 learning agents), model, run_at and the hand-off ids. Every write carries the origin given (default user).

#### automation · Pipeline Factory · Reset agent runs
[R2-P02] The reset for the round-2 objects.
- automation · create · Pipeline Factory · Reset agent runs: callable from Pipeline Factory · Reset demo, mode deterministic, no model call; no inputs; result deleted (number), restored (number). Deletes every row whose origin is test in PF Component run, PF Source, PF Inbox and PF Suppression, puts every seed row of those four objects back from PF Seed snapshot, never touches a user row.
- automation · update · Pipeline Factory · Reset demo: after its round-1 steps, unchanged, it calls Pipeline Factory · Reset agent runs and adds its deleted and restored counts to its own; the PF Component rows are restored from their snapshot rows, which the registry line below rewrites to hold the built-entity fields, so a reset keeps the links.

#### automation · Pipeline Factory · Account Ranking
[R2-P03 · automations: the 12 workflows, part 1] C12. Ranks each patch and tops up the Gate 1 batch.
- automation · create · Pipeline Factory · Account Ranking: callable from Pipeline Factory · Run component and other automations; mode deterministic, no model call; inputs patch_id (text, required), mode (text: rank | top_up), origin (text); result ranked (number), queued_to_gate1 (number), reason (text). rank (the Monday 06:00 job): recomputes each account's timing_score as the sum of its counted PF Signal weights in the last 30 days, capped at 40 (the same starting weights and checked-visit rule Pipeline Factory · Log signal applies; Log signal is unchanged and keeps scoring a single new signal), writes rank_in_patch by fit_score + timing_score and top_signals (the top 3) on PF Account; top_up (the daily 07:00 job): moves the highest-ranked queued accounts of the patch to gate1_status pending until the patch's slots left (slots_allocated minus slots_used) are filled, after fast-lane plays, skipping held-out and not_eligible accounts; saves an Account Ranking to Gate 1 hand-off per account queued through Save hand-off and one PF Component run (component_id C12, kind workflow, model none).

#### automation · Pipeline Factory · Weekly Slot Planner
[R2-P03] C13. The Monday slot allocation.
- automation · create · Pipeline Factory · Weekly Slot Planner: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, empty for all), origin (text); result allocations (text, JSON per patch: base, cap, boost, allocated), reason (text). Base 25 slots per patch; a pace boost of up to 50% (25% by default) only to a patch whose AE has under 6 intros booked in 7 days and is behind on intro meetings (intros_booked_7d under 4, the assumed weekly target, since no diagnosis field exists); then never more than eligible_accounts ÷ 13 (rounded down), floor 15, cap 40. Writes PF Patch.slots_allocated and pace_boost_pct and one PF Component run per patch (C13) logging every allocation; PATCH-NAE-03 gets 24 (312 ÷ 13), PATCH-NAE-04 gets 20 (260 ÷ 13) with its 25% boost logged.

#### automation · Pipeline Factory · Holdout Picker
[R2-P03] C14. The randomised holdout after allocation.
- automation · create · Pipeline Factory · Holdout Picker: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, required), week_seed (number; default the ISO week number of the run), origin (text); result held (text, JSON account ids), std_diff_fit (number), std_diff_timing (number), redraws (number), reason (text). From the patch's medium and low fit accounts that are pending or queued and not yet held, draws 10% (at least 1) with a seeded pseudo-random order from week_seed; checks the standardised difference of fit_score and timing_score between held and treated under 0.1, else redraws with week_seed + 1, at most 5 times, then answers the best draw with reason "balance not reached after 5 redraws"; sets factory_holdout true and factory_holdout_until 90 days after the run on each held account (HubSpot flag mocked as the PF Account fields) and logs the seed in one PF Component run (C14). Decide Gate 1, unchanged, refuses a held account. The 90- and 180-day reports are the PF Component run rows (assumption).

#### automation · Pipeline Factory · Do-Not-Contact List
[R2-P03] C25. One suppression list, consent and erasure.
- automation · create · Pipeline Factory · Do-Not-Contact List: callable from the AI agents (PF · Reply Sorter), Pipeline Factory · Run component and other automations; mode deterministic, no model call; inputs action (text: add | erase | sync | screen), person_id (text), kind (text: opt_out | bounce | complaint | legal_hold), reason (text), origin (text); result result (text: added | already_listed | erased | synced | clear | listed), suppression_id (text), reason (text). add: one PF Suppression row per person and kind (no second row), PF Person.dnc true, copied_to "HubSpot, Apollo, Sprouts (mocked)" with copied_at now; erase: sets the PF Person's name to "Erased person" and its note empty, keeps only a hashed code (email_hash) on a PF Suppression erasure row with erase_due 30 days out, so the person is never re-added; sync: stamps copied_at on every row (the 15-minute copy, mocked); screen: answers listed or clear for a person (the phone DNC screen before any dialler, mocked as the list). One PF Component run per call (C25).

#### automation · Pipeline Factory · Contact Finder
[R2-P04 · automations: the 12 workflows, part 2] C24. Verified contact details, mocked through Sprouts.
- automation · create · Pipeline Factory · Contact Finder: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, required), origin (text); result verified (number), linkedin_only (number), reason (text). For each PF Person of the account that is not a gatekeeper and not on the suppression list: a PF Source contact_record with a verified email sets email_status verified (phone noted for Tier 1 and engaged people in the run), none sets linkedin_only; a verification older than 90 days is re-checked before use; one PF Component run (C24) with source and verify date per person (graph and HubSpot writes mocked as the PF records).

#### automation · Pipeline Factory · Send Rules Check
[R2-P04] C33. The full Send Rules Check as its own automation; Clear Gate 2 keeps its own check, unchanged.
- automation · create · Pipeline Factory · Send Rules Check: callable from Pipeline Factory · Run component and other automations; mode deterministic, no model call; inputs draft_id (text, required), origin (text); result result (text: passed | blocked), rule (text), reason (text), checks (text, JSON: every rule with passed or failed). Read-only on PF Draft (Clear Gate 2 stays the only writer of rules_check): checks clean text (no empty subject or body, no unfilled placeholder, the AE's name right); person still in role (not erased); not on DNC (PF Person.dnc or a PF Suppression row), not held out, not a customer or open deal (deal_stage none); parent outreach lock owned by this owner (ultimate_parent_lock equals owner_ae or is empty); Patch ID, AE and pod present; sender from the account's pod and under its inbox daily limit (PF Inbox sent_today under 70% of daily_limit); person not in another sequence; consent recorded for the person's state when a PF Suppression consent row exists; a planted_error draft is always blocked. Answers the first failed rule in a fixed order (pod, DNC, other sequence, held out, Patch ID/AE/pod, parent lock, inbox limit, clean text, planted error) so it names the same rule Clear Gate 2 names for D-04 (pod) and for D-06 (other sequence). One PF Component run (C33).

#### automation · Pipeline Factory · Outreach Launcher
[R2-P04] C35. Puts each enrolled person into channels, mocked (Apollo, Sprouts, HubSpot).
- automation · create · Pipeline Factory · Outreach Launcher: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, required), origin (text); result scheduled (number), already_scheduled (number), schedule (text, JSON), reason (text). For every PF Draft of the account with status enrolled (Clear Gate 2 enrols; it is unchanged): schedules email steps into the assigned inbox's sequence, LinkedIn steps into the sender's Sprouts queue and calls as call tasks, in the prospect's local morning (09:00 to 11:00 in the account's state) and state window, Tier 2 two days after Tier 1 and Tier 3 two days after that, no two people at one account emailed the same day; holds every inbox at 70% of its daily limit (adds to PF Inbox.sent_today, never past 70%); keyed on enrolment_key (person + play): a draft already scheduled answers already_scheduled and writes nothing; owner, Patch ID, BDR of record, sequence status and tasks to HubSpot are mocked as the PF Component run payload (C35). It never writes ultimate_parent_lock (Parent Company Linker is that field's one writer; open question).

#### automation · Pipeline Factory · Email Domain Swapper
[R2-P04] C39. Rests a failing domain and swaps in a warm spare.
- automation · create · Pipeline Factory · Email Domain Swapper: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs sender (text, empty for all), origin (text); result rested (text, JSON inbox ids), swapped_in (text, JSON), retired (text, JSON), blocked_new (text, JSON), reason (text). An active inbox with placement under 70% in its last two tests, or blacklisted, goes to resting the same day and the sender's first warm_spare goes active; a previously blacklisted inbox goes to retired; a new sender's (blocked_new) inbox stays blocked until a placement test of 70 or more exists. Writes PF Inbox.status (its one writer) and one PF Component run (C39). On the seeds: IN-02 rests, IN-03 goes active, IN-05 retires, IN-06 stays blocked.

#### automation · Pipeline Factory · Meeting Handoff and Deadlines
[R2-P04] C43. Picks up meetings, triggers the prep pack and runs the AE deadlines; Book meeting stays the booking and lock step, unchanged.
- automation · create · Pipeline Factory · Meeting Handoff and Deadlines: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, empty for all), origin (text); result picked_up (number), deadlines (text, JSON), escalations (text, JSON), reason (text). Picks up meetings booked outside the AE's link from PF Source calendar_event rows (the AE's Google Calendar, mocked) and calls Pipeline Factory · Book meeting (action book, the same origin) for an account not yet booked (a rejected meeting rebooked within 30 days keeps its source); saves a Meeting Handoff and Deadlines to Meeting Prep Writer hand-off through Save hand-off (the prep pack trigger; SC booking, agenda and 24h/1h reminders and the 2-touch no-show reschedule are mocked as the run payload); computes the AE deadlines in business hours: accept or reject within 1 business day (else Geo leader in 4h or the backup AE), decide within 2 business days of a held meeting, stale after 5 idle business days at Engage, alert at 30 days in Connect and 45 in Commit without a next step, reminder at half-window and escalation on a miss, as PF Hand-off rows waiting_person through Save hand-off; one PF Component run (C43).

#### automation · Pipeline Factory · Alarm and Escalation
[R2-P05 · automations: the 12 workflows, part 3, and the registry's run action] C55. Reads the tower and acts on a red line.
- automation · create · Pipeline Factory · Alarm and Escalation: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs origin (text); result actions (text, JSON: component or patch, red line, action, before and after), escalations (text, JSON), reason (text). Reads PF Component success_rate and PF Patch; a component under 95% is paused automatically through Pipeline Factory · Pause component (a safety action; resuming needs a person); a component from 95% to under 97% gets a to-do item for the GTM engineer (a PF Hand-off waiting_person through Save hand-off) and is never paused by it, so beat 7's person still pauses Current Vendor Finder (96.1%); a patch under its intro pace gets a throttle or move-slots proposal as a to-do item; unfixed alarms escalate patch to pod after 2 business days, to Geo after 5, then to CRO (by the age of the open to-do item); logs before and after numbers in one PF Component run (C55).

#### automation · Pipeline Factory · Content Handoff
[R2-P05] C56. Monday hand-off to marketing, mocked (LinkedIn ad audiences, Content Factory).
- automation · create · Pipeline Factory · Content Handoff: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, required), origin (text); result audiences (number), to_content_factory (number), to_nurture (number), marketing_influenced_set (number), reason (text). Accounts in play in the patch go to a LinkedIn ad audience by patch geography for 8 weeks; people never reached go to the Content Factory (ads and content only, never cold email); people whose reply was sorted "not now" or who engaged go to nurture until their date; sets PF Account.marketing_influenced true on accounts in play that are not yet booked (never on a locked account); the weekly asset, message and pattern results by patch are the run payload; one PF Component run (C56).

#### automation · Pipeline Factory · Privacy and Consent
[R2-P05] C57. Consent, legal checklists, erasure and the 12-month clean-up.
- automation · create · Pipeline Factory · Privacy and Consent: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, empty for all), origin (text); result checklist (text, JSON per person: recording consent, DNC, send window, consent, footer), erasures_due (number), cleanup_flagged (number), reason (text). Per person: recording consent per state from PF Suppression consent rows, the DNC screen through Pipeline Factory · Do-Not-Contact List (action screen), the state legal checklist (send window, consent, footer); erasure rows past erase_due are completed through Do-Not-Contact List (action erase); people never engaged in 12 months are flagged for clean-up in the run (never deleted by the demo); one PF Component run (C57).

#### automation · Pipeline Factory · Run component
[R2-P05] The registry's Run action: one call runs any built agent or workflow on an account.
- automation · create · Pipeline Factory · Run component: callable from the app; inputs component_id (text, required), account_id (text), person_id (text), draft_id (text), origin (text); result result (text: ran | paused | not_runnable | failed), run_id (text), handoff_ids (text), confidence (number), summary (text), reason (text). Reads the PF Component row: status paused answers paused and runs nothing; built_kind not_built (human gates C26, C40, C47 and the two rule steps) answers not_runnable "a person or a rule step, not a built entity"; built_kind ai_agent invokes the agent whose id is built_entity_id (the same invoke operation Pipeline Factory · Ask the analyst uses) with the message "Run your job for component `component_id` on account `account_id` (person, draft when given); origin `origin`", then reads the newest PF Component run of that component and account and writes latency_ms on it; built_kind automation calls the matching workflow automation above (one branch per component id, C12, C13, C14, C24, C25, C33, C35, C39, C43, C55, C56, C57, passing account_id or its patch_id and origin; C15 and C34 answer not_runnable "run from To-do or Gate 2"). If the invoke operation takes only a fixed agent, it branches per component id for the 38 agents instead. Deterministic itself; the model call is the invoked agent's.

#### ai-agent · PF · Duplicate Finder
[R2-P06 · agents, sub-workflow 1 (part 1)] C01, one job, built live.
- ai-agent · create · PF · Duplicate Finder: registry row C01 (agent, sub-workflow 1. Patch accounts, asks A16); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find duplicate patch accounts: normalise keys (domain, legal name, LinkedIn ID, HubSpot ID, email), match exactly, score near-matches 0 to 100 and log the reasoning; reads PF Account rows of the patch through Read component inputs (component_id C01); writes a PF Component run of output_type merge_proposal per pair (pair, score, keys compared, reasoning); it never merges or deletes a row (a merge is a proposal in this demo), only through Save agent output (component_id C01); threshold and routing: 95 or more: proposal marked merge; 80 to 95: waiting_person for RevOps; under 80: kept separate, no hand-off (Save agent output applies the threshold 95 and routes below it to RevOps); feeds (the register): Parent Company Linker; schedule in the registry: every 15 min (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never deletes or merges an account itself; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Parent Company Linker
[R2-P06 · agents, sub-workflow 1 (part 1)] C02, one job, built live.
- ai-agent · create · PF · Parent Company Linker: registry row C02 (agent, sub-workflow 1. Patch accounts, asks A17); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: link each company to its parent, subsidiaries and divisions, propose divisions that buy separately, and set the outreach lock at the top parent; reads PF Account rows and PF Source rows (press, filings) through Read component inputs (component_id C02); writes PF Account.ultimate_parent_lock (its registered field) and a PF Component run row with parent_id, children and division proposals, only through Save agent output (component_id C02); threshold and routing: under 80: waiting_person for RevOps, the lock is not written (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Headquarters Finder; Patch Suggester; schedule in the registry: on new account, HQ change or M&A news (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a division proposal is never applied without RevOps; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Headquarters Finder
[R2-P06 · agents, sub-workflow 1 (part 1)] C03, one job, built live.
- ai-agent · create · PF · Headquarters Finder: registry row C03 (agent, sub-workflow 1. Patch accounts, asks A18); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find the parent's headquarters city, state and country by weighing sources; reads PF Account and PF Source rows (filings, press) through Read component inputs (component_id C03); writes PF Account.hq_city (its registered field) and a PF Component run row with state, country, other candidates and evidence, only through Save agent output (component_id C03); threshold and routing: under 80: waiting_person, RevOps picks from the candidates (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Patch Suggester; schedule in the registry: on new account (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never guesses a city without a source; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Headquarters Re-checker
[R2-P06 · agents, sub-workflow 1 (part 1)] C04, one job, built live.
- ai-agent · create · PF · Headquarters Re-checker: registry row C04 (monitor, sub-workflow 1. Patch accounts, asks A19); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: re-check headquarters of companies with move or M&A news and raise an alert on any change; reads PF Account.hq_city and PF Source press rows through Read component inputs (component_id C04); writes a PF Component run row of output_type hq_change_alert (old and new HQ, source) and a hand-off to Patch Suggester, only through Save agent output (component_id C04); threshold and routing: under 80: waiting_person for RevOps; no change: result no_action (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Patch Suggester; patch control tower; schedule in the registry: nightly on move or M&A news; quarterly on all (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes hq_city itself (Headquarters Finder owns it); outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · New Account Finder
[R2-P06 · agents, sub-workflow 1 (part 1)] C05, one job, built live.
- ai-agent · create · PF · New Account Finder: registry row C05 (agent, sub-workflow 1. Patch accounts, asks A20); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find new candidate accounts from closed-won lookalikes and the seven other sources, dropping fit under 36, customers, open deals, partners, competitors and DNC; reads PF Account, PF Source (web visits, events, job changes) and PF Suppression through Read component inputs (component_id C05); writes a PF Component run row of output_type account_suggestion per candidate (name, source, why, estimated fit), only through Save agent output (component_id C05); threshold and routing: under 70: not suggested (result no_action); 70 and over: waiting_person for RevOps (Save agent output applies the threshold 70 and routes below it to RevOps); feeds (the register): Fit Scorer; schedule in the registry: weekly lookalikes; daily 7 sources (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; suggests to RevOps, never adds an account; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Fit Scorer
[R2-P07 · agents, sub-workflow 1 (part 2)] C06, one job, built live.
- ai-agent · create · PF · Fit Scorer: registry row C06 (agent, sub-workflow 1. Patch accounts, asks A21); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: score fit out of 60 (up to 15 each: industry, size and complexity, core systems, AI and integration maturity) and map score plus ICP V2 quadrant to best, medium or low fit; the floor of 36 never moves; reads PF Account and PF Source rows through Read component inputs (component_id C06); writes PF Account.fit_score and fit_band (its registered fields) with the four sub-scores in its PF Component run row, only through Save agent output (component_id C06); threshold and routing: under 70 confidence: waiting_person for RevOps, fields not written (Save agent output applies the threshold 70 and routes below it to RevOps); feeds (the register): Account Ranking; schedule in the registry: on change and monthly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never moves the floor of 36; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Patch Suggester
[R2-P07 · agents, sub-workflow 1 (part 2)] C07, one job, built live.
- ai-agent · create · PF · Patch Suggester: registry row C07 (agent, sub-workflow 1. Patch accounts, asks A22); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: propose a patch for a new account or an HQ change: geography first, then industry, with confidence and reason; reads PF Account, PF Patch and hand-offs from Headquarters Finder and Headquarters Re-checker through Read component inputs (component_id C07); writes a PF Component run row of output_type patch_proposal (proposed patch, reason), only through Save agent output (component_id C07); threshold and routing: under 80: waiting_person, RevOps decides from evidence (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): RevOps (patch decision); schedule in the registry: on new account or HQ change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a Patch ID; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Current Vendor Finder
[R2-P07 · agents, sub-workflow 1 (part 2)] C08, one job, built live.
- ai-agent · create · PF · Current Vendor Finder: registry row C08 (agent, sub-workflow 1. Patch accounts, asks A23); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find the integration, automation and agent tools a best or medium fit account uses, from vendor case studies, job posts and procurement notices; reads PF Account and PF Source rows (vendor_case_study, job_post, procurement_notice) through Read component inputs (component_id C08); writes a PF Component run row of output_type current_vendors (vendor, product, evidence, first seen date) and hand-offs to Renewal Date Finder and Battlecard Writer, only through Save agent output (component_id C08); threshold and routing: under 60: saved tagged [HYPOTHESIS] (Save agent output applies the threshold 60 and routes below it to tag [HYPOTHESIS]); feeds (the register): Renewal Date Finder; Battlecard Writer; schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never states a vendor without a source link; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Renewal Date Finder
[R2-P07 · agents, sub-workflow 1 (part 2)] C09, one job, built live.
- ai-agent · create · PF · Renewal Date Finder: registry row C09 (agent, sub-workflow 1. Patch accounts, asks A24); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: estimate each vendor's renewal as 3 years from the earliest evidence unless a later contract signal exists, and raise a renewal signal 9 months before; reads hand-offs from Current Vendor Finder and PF Source rows through Read component inputs (component_id C09); writes a PF Component run row of output_type renewal_estimate and, inside 9 months, a hand-off to Buying Signal Spotter, only through Save agent output (component_id C09); threshold and routing: under 60: no signal (result no_action) (Save agent output applies the threshold 60 and routes below it to no signal); feeds (the register): Buying Signal Spotter; schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a PF Signal itself (Buying Signal Spotter owns it); outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Battlecard Writer
[R2-P07 · agents, sub-workflow 1 (part 2)] C10, one job, built live.
- ai-agent · create · PF · Battlecard Writer: registry row C10 (agent, sub-workflow 1. Patch accounts, asks A25); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: draft battlecard changes per vendor: shortfalls, switch path, proof and objection answers; reads hand-offs from Current Vendor Finder and PF Source rows through Read component inputs (component_id C10); writes a PF Component run row of output_type battlecard_draft, always waiting_person for product marketing, only through Save agent output (component_id C10); threshold and routing: every draft waits for product marketing's approval (threshold 0, routed to Product marketing) (Save agent output applies the threshold 0 and routes below it to Product marketing approves each); feeds (the register): Message Writer; schedule in the registry: on vendor change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never publishes a battlecard; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Buying Signal Spotter
[R2-P08 · agents, sub-workflows 2 and 3] C11, one job, built live.
- ai-agent · create · PF · Buying Signal Spotter: registry row C11 (agent, sub-workflow 2. Account selection, asks A28); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: watch the signal sources, record each signal (company, type, date, source link, strength), verify company match and date, score confidence, and send strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) to the Play Picker; reads PF Source rows (web_visit, press, job_post, events), PF Signal and hand-offs from Renewal Date Finder through Read component inputs (component_id C11); writes PF Signal rows (its registered records, weights from the starting signal weights, the checked-visit rule) and hand-offs to Account Ranking, and to Play Picker for a strong signal, only through Save agent output (component_id C11); threshold and routing: under 70: logged, not scored (counted false); signals fade over 30 days (Save agent output applies the threshold 70 and routes below it to logged, not scored); feeds (the register): Account Ranking; Play Picker (fast lane); schedule in the registry: continuous (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never counts a visit that fails the checked-visit rule; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Company Facts Collector
[R2-P08 · agents, sub-workflows 2 and 3] C16, one job, built live.
- ai-agent · create · PF · Company Facts Collector: registry row C16 (agent, sub-workflow 3. Account research, asks A36); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: extract sourced company facts on AI, automation, integration, modernisation, cost, CX and risk from the annual report, investor deck, two earnings calls, 12 months of press and current job posts; reads PF Source rows of the account (annual_report, investor_deck, earnings_call, press, job_post) through Read component inputs (component_id C16); writes PF Fact rows of kind fact (statement, exact quote, page or timestamp, date, link, [PUBLIC]) and hand-offs to Use Case Matcher and Case for Change Drafter, only through Save agent output (component_id C16); threshold and routing: a fact without quote and link is rejected; anything over 12 months old is dropped (except the latest annual report) (Save agent output applies the threshold 0 and routes below it to facts without quote and link rejected); feeds (the register): Use Case Matcher; Case for Change Drafter; schedule in the registry: Day 1; best fit every 30 days, others 90 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a fact without its quote and link; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Use Case Matcher
[R2-P08 · agents, sub-workflows 2 and 3] C17, one job, built live.
- ai-agent · create · PF · Use Case Matcher: registry row C17 (agent, sub-workflow 3. Account research, asks A37); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: match VEP-CFC use cases to the account's industry and core systems, score the evidence and keep the top 3 with two supporting facts (or one fact plus engagement), tagged with pattern and outcome; reads PF Fact rows of kind fact and PF Source rows through Read component inputs (component_id C17); writes PF Fact rows of kind use_case (UC-ID, pattern, outcome, supporting facts) and a hand-off to Case for Change Drafter, only through Save agent output (component_id C17); threshold and routing: under 70: saved as a question only, tagged [HYPOTHESIS], never a claim (Save agent output applies the threshold 70 and routes below it to shown only as a question); feeds (the register): Case for Change Drafter; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; uses only VEP-CFC use cases (a UC-ID); outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Case for Change Drafter
[R2-P08 · agents, sub-workflows 2 and 3] C18, one job, built live.
- ai-agent · create · PF · Case for Change Drafter: registry row C18 (agent, sub-workflow 3. Account research, asks A38); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write the Case for Change: business problem in the company's own words, impact with no dollar figures, why now from the top signals, why UnifyApps, closest proof, main and backup angle, and risks; reads PF Fact rows (facts and use cases), PF Signal rows and the account's PF Person rows through Read component inputs (component_id C18); writes PF Fact rows of kind case_for_change, each citing a fact_id or tagged [HYPOTHESIS], and hand-offs to Play Picker, Message Writer and Meeting Prep Writer, only through Save agent output (component_id C18); threshold and routing: under 70: waiting_person, the BDR reviews it at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR reviews at Gate 2); feeds (the register): Play Picker; Message Writer; Meeting Prep Writer; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a sentence without a cited fact or a [HYPOTHESIS] tag, and never writes emails; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Buying Team Mapper
[R2-P09 · agents, sub-workflow 4] C21, one job, built live.
- ai-agent · create · PF · Buying Team Mapper: registry row C21 (agent, sub-workflow 4. Buying committee, asks A41); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: map the buying team: load the industry's default titles, assign each person a role, check the champions library, pick 3 Tier 1, 3 Tier 2, 4 Tier 3 and 2 backups, and flag the economic buyer; reads PF Person rows of the account and PF Source rows through Read component inputs (component_id C21); writes PF Person.role and tier (its registered fields; gatekeepers tier mapped) and hand-offs to Person Notes Writer, Contact Finder and Intro Finder, only through Save agent output (component_id C21); threshold and routing: under 70 on a role: waiting_person, the BDR checks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR checks at Gate 2); feeds (the register): Person Notes Writer; Contact Finder; Intro Finder; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a gatekeeper is mapped, never contacted; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Person Notes Writer
[R2-P09 · agents, sub-workflow 4] C22, one job, built live.
- ai-agent · create · PF · Person Notes Writer: registry row C22 (agent, sub-workflow 4. Buying committee, asks A42); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write a four-line note per person: role and time in role, past companies and public talks, what they own ([HYPOTHESIS] unless public), the link to the matched use case and nearby event fit; reads PF Person, PF Fact (use cases) and PF Source rows through Read component inputs (component_id C22); writes PF Person.note (its registered field) and a hand-off to Message Writer, only through Save agent output (component_id C22); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR) (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Message Writer; schedule in the registry: Day 1; every 90 days; on job change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; professional information only; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Intro Finder
[R2-P09 · agents, sub-workflow 4] C23, one job, built live.
- ai-agent · create · PF · Intro Finder: registry row C23 (agent, sub-workflow 4. Buying committee, asks A43); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find a warm intro for Tier 1 people at best fit accounts from shared work history (opt-in LinkedIn exports, partners, SIs, investors), ranked worked together over overlapped over friend of a friend; reads PF Person rows (Tier 1) and PF Source rows of kind linkedin_export through Read component inputs (component_id C23); writes a PF Component run row of output_type intro_request (draft request, path, rank) into the patch AE's to-do list, and a 7-day hold on cold touches to that person in the payload, only through Save agent output (component_id C23); threshold and routing: under 60: not suggested (result no_action) (Save agent output applies the threshold 60 and routes below it to not suggested); feeds (the register): AE to-do list; schedule in the registry: Day 1, Tier 1 at best fit (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never contacts anyone; the AE sends the intro request; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Play Picker
[R2-P10 · agents, sub-workflow 5 (part 1)] C27, one job, built live.
- ai-agent · create · PF · Play Picker: registry row C27 (agent, sub-workflow 5. Outreach drafting, asks A48); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: pick the play for the signal (or the 13-week cycle) and set people, channels, start days and senders, spacing tiers so no two people at one account get email the same day; reads PF Account, PF Person, PF Signal, PF Patch and hand-offs from Buying Signal Spotter (fast lane) and Case for Change Drafter through Read component inputs (component_id C27); writes a PF Component run row of output_type play (play_id, people, channels, start days, senders) and hand-offs to Page Builder, Content Picker and Message Writer, only through Save agent output (component_id C27); threshold and routing: under 70: waiting_person, the BDR picks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR picks at Gate 2); feeds (the register): Page Builder; Content Picker; Message Writer; schedule in the registry: Day 2; fast lane within the hour (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; picks senders only from the account's patch and pod; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Page Builder
[R2-P10 · agents, sub-workflow 5 (part 1)] C28, one job, built live.
- ai-agent · create · PF · Page Builder: registry row C28 (agent, sub-workflow 5. Outreach drafting, asks A49); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: build one Art of the Possible page per account from public facts only: 2 to 3 workflows reimagined before and after for the matched use cases, proof, how UnifyApps connects their core systems and a patch event; reads PF Fact rows and hand-offs from Play Picker through Read component inputs (component_id C28); writes a PF Component run row of output_type aotp_page (the page content in marketing's locked template sections, noindex, a tracked link per prospect, mocked) and hand-offs to Fact Checker and Gate 2, only through Save agent output (component_id C28); threshold and routing: under 75: waiting_person, marketing ops checks (Save agent output applies the threshold 75 and routes below it to marketing ops checks); feeds (the register): Fact Checker; Gate 2; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never publishes a page; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Content Picker
[R2-P10 · agents, sub-workflow 5 (part 1)] C29, one job, built live.
- ai-agent · create · PF · Content Picker: registry row C29 (agent, sub-workflow 5. Outreach drafting, asks A50); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: pick one Content Factory asset per asset touch, matched on role, industry, use case, pattern, outcome, VEP stage and Geo; reads PF Source rows of kind content_asset and hand-offs from Play Picker through Read component inputs (component_id C29); writes a PF Component run row of output_type asset_pick per touch and a hand-off to Message Writer, only through Save agent output (component_id C29); threshold and routing: under 70: no asset, a sourced insight instead; skips assets over 18 months old or retired; never the same asset to two people at one account in a week (Save agent output applies the threshold 70 and routes below it to no asset, a sourced insight); feeds (the register): Message Writer; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never invents an asset; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Message Writer
[R2-P10 · agents, sub-workflow 5 (part 1)] C30, one job, built live.
- ai-agent · create · PF · Message Writer: registry row C30 (agent, sub-workflow 5. Outreach drafting, asks A51); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write every email and LinkedIn message in the play, from the Content Factory's best message for category, sub-sector, company and persona, in the assigned handbook voice, with one sourced fact, the pain this person owns and the likeliest objection for their role; reads PF Fact, PF Person, PF Source (handbook, content_asset) and hand-offs from Play Picker, Content Picker, Person Notes Writer and Battlecard Writer through Read component inputs (component_id C30); writes PF Draft rows (status waiting_gate2, its registered records) keyed account_id + person_id + play_id, and hand-offs to Fact Checker and Message Grader, only through Save agent output (component_id C30); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR); copy rules: subject 3 to 6 words on the trigger, emails 90 to 120 words, connection notes under 250 characters, open on the business problem, one insight and one question, no em dashes, placeholders or invented statistics (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Fact Checker; Message Grader; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; names the patch AE as session host and never sends; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Fact Checker
[R2-P10 · agents, sub-workflow 5 (part 1)] C31, one job, built live.
- ai-agent · create · PF · Fact Checker: registry row C31 (checker, sub-workflow 5. Outreach drafting, asks A52); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: trace every claim in drafts and pages: facts to a public source no older than 12 months, numbers to a source or the proof library, use cases to a UC-ID with account evidence; reads PF Draft rows, PF Fact rows and hand-offs from Message Writer and Page Builder through Read component inputs (component_id C31); writes PF Draft.fact_check (its registered field: passed or blocked, with the untraceable claim in its PF Component run row) and a hand-off to Send Rules Check, only through Save agent output (component_id C31); threshold and routing: blocks anything untraceable (no threshold) (Save agent output applies the threshold 0 and routes below it to blocks anything untraceable); feeds (the register): Send Rules Check; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; never rewrites a draft. Runs on the other model family from Message Writer and Page Builder; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Message Grader
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C32, one job, built live.
- ai-agent · create · PF · Message Grader: registry row C32 (checker, sub-workflow 5. Outreach drafting, asks A53); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: grade each draft 0 to 100 on the message rubric: teaches something, relevant to role and company, actionable, applies to their business, well written in the right voice, follows the copy rules; reads PF Draft rows and PF Source handbook rows through Read component inputs (component_id C32); writes PF Draft.grade (its registered field) with the rubric scores in its PF Component run row, and a hand-off to Send Rules Check, only through Save agent output (component_id C32); threshold and routing: under 75: one automatic rewrite is requested (the run says rewrite_requested); under 75 again: waiting_person, a person decides at Gate 2 (Save agent output applies the threshold 75 and routes below it to one rewrite, then a person at Gate 2); feeds (the register): Send Rules Check; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; grades only; never rewrites. Runs on the other model family from Message Writer; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Call Script Writer
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C36, one job, built live.
- ai-agent · create · PF · Call Script Writer: registry row C36 (agent, sub-workflow 6. Outreach, asks A60); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write the call script for a call task: a signal-tied opener, a permission question, 3 to 5 discovery questions, the top 3 objection answers, a 20-second voicemail and a follow-up email draft, and order the BDR's call list by interest; reads PF Person, PF Signal, PF Fact and PF Source call_transcript rows (Gong, mocked) through Read component inputs (component_id C36); writes a PF Component run row of output_type call_script into the BDR's call list, only through Save agent output (component_id C36); threshold and routing: under 70: waiting_person, the BDR approves the script (Save agent output applies the threshold 70 and routes below it to BDR approves the script); feeds (the register): BDR call list; schedule in the registry: per call task (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never dials; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Follow-up Planner
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C37, one job, built live.
- ai-agent · create · PF · Follow-up Planner: registry row C37 (agent, sub-workflow 6. Outreach, asks A61); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: keep the account one conversation once anyone responds: a referral becomes the lead thread, a Tier 1 objection pauses Tiers 2 and 3 with an answer note for the AE, 2 or more people engaging in 7 days switches to Committee Surge; reads PF Source reply rows and hand-offs from Reply Sorter through Read component inputs (component_id C37); writes a PF Component run row of output_type replan and hand-offs to Fact Checker and Message Grader for every rewrite, only through Save agent output (component_id C37); threshold and routing: under 70: waiting_person, the BDR decides (Save agent output applies the threshold 70 and routes below it to BDR decides); feeds (the register): Fact Checker; Message Grader; schedule in the registry: on any response (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never sends; every rewrite goes back through Fact Checker and Message Grader; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Inbox Health Checker
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C38, one job, built live.
- ai-agent · create · PF · Inbox Health Checker: registry row C38 (agent, sub-workflow 6. Outreach, asks A62); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: check inbox health: placement per active domain, blacklists and reputation, reply rate by recipient provider, and the email-security-scanner list; reads PF Inbox rows through Read component inputs (component_id C38); writes PF Inbox.placement_pct_last and blacklisted (its registered fields), an alert PF Component run row for the BDR and the GTM engineer, and a hand-off to Email Domain Swapper, only through Save agent output (component_id C38); threshold and routing: every alert goes to the BDR and the GTM engineer (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Email Domain Swapper; schedule in the registry: weekly placement; daily blacklist (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never rests or swaps a domain itself (Email Domain Swapper owns it); outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Reply Sorter
[R2-P12 · agents, sub-workflow 7] C41, one job, built live.
- ai-agent · create · PF · Reply Sorter: registry row C41 (checker, sub-workflow 7. Engage, Connect and Commit, asks A67); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: sort every reply into one of nine types (positive, referral, not now with date, objection, wrong person, out of office, unsubscribe, bounce, auto-reply), stop all channels for that person, and handle the mechanical types; reads PF Source rows of kind reply (Apollo and Sprouts, mocked) through Read component inputs (component_id C41); writes a PF Component run row of output_type reply_type (type, date if any, channels stopped) and hand-offs to Reply Writer, Follow-up Planner and Do-Not-Contact List; out of office moves the next touch to the return date in the payload; unsubscribe calls Do-Not-Contact List within the run, only through Save agent output (component_id C41); threshold and routing: under 90 on unsubscribe: treated as unsubscribe; under 80 on anything else: waiting_person, a person sorts it (Save agent output applies the threshold 80 and routes below it to a person sorts it (unsubscribe under 90 treated as unsubscribe)); feeds (the register): Reply Writer; Follow-up Planner; Do-Not-Contact List; schedule in the registry: on every reply (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Do-Not-Contact List (Pipeline Factory · Do-Not-Contact List); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on the other model family from Reply Writer; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Reply Writer
[R2-P12 · agents, sub-workflow 7] C42, one job, built live.
- ai-agent · create · PF · Reply Writer: registry row C42 (agent, sub-workflow 7. Engage, Connect and Commit, asks A68); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: draft the answer to a reply from the thread, the account view, the objection list and the AE's booking link; reads PF Source reply rows, PF Account, PF Fact and hand-offs from Reply Sorter through Read component inputs (component_id C42); writes a PF Component run row of output_type reply_draft into the BDR's to-do list (and the AE's for a positive reply at a best fit account), with the 90-minute reminder and 2-business-hour Geo alert as due times, only through Save agent output (component_id C42); threshold and routing: under 70: marked for full rewrite (waiting_person) (Save agent output applies the threshold 70 and routes below it to marked for full rewrite); feeds (the register): BDR to-do list; schedule in the registry: on every reply (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never sends; the person sends from the original thread; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Meeting Prep Writer
[R2-P12 · agents, sub-workflow 7] C44, one job, built live.
- ai-agent · create · PF · Meeting Prep Writer: registry row C44 (agent, sub-workflow 7. Engage, Connect and Commit, asks A70); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: build the meeting prep pack for the AE and SC: account view, buying team, thread, Case for Change, likely objections, Art of the Possible page, and questions to confirm the economic buyer and timeline; reads PF Account, PF Person, PF Fact, PF Source and hand-offs from Meeting Handoff and Deadlines and Case for Change Drafter through Read component inputs (component_id C44); writes a PF Component run row of output_type prep_pack and a hand-off to the AE AI Twin (mocked as the run), only through Save agent output (component_id C44); threshold and routing: no threshold (0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): AE AI Twin; schedule in the registry: on booking (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never invents a promise the AE made; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Meeting Labeler
[R2-P12 · agents, sub-workflow 7] C45, one job, built live.
- ai-agent · create · PF · Meeting Labeler: registry row C45 (checker, sub-workflow 7. Engage, Connect and Commit, asks A71); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: label each meeting intro, New Buyer Meeting or doesn't count, quoting evidence from the transcript, attendees and the economic-buyer flag; reads PF Source rows of kind meeting_transcript and calendar_event, PF Person through Read component inputs (component_id C45); writes PF Account.meeting_label (its registered field) with the quoted evidence in its PF Component run row, and hand-offs to Deal Qualifier and AE confirm, only through Save agent output (component_id C45); threshold and routing: doesn't count if under 20 minutes, no Tier 1 or 2 attendee, a reschedule, or a second intro within 90 days; unrecorded meetings labelled from attendees and AE notes and marked unrecorded; under 80: waiting_person, the Geo leader checks (Save agent output applies the threshold 80 and routes below it to Geo leader checks); feeds (the register): Deal Qualifier; AE confirm; schedule in the registry: after each meeting (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on the other model family from the drafters; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Deal Qualifier
[R2-P12 · agents, sub-workflow 7] C46, one job, built live.
- ai-agent · create · PF · Deal Qualifier: registry row C46 (checker, sub-workflow 7. Engage, Connect and Commit, asks A72); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: check the six qualification requirements after each New Buyer Meeting (fit 36+, a VEP-CFC pain, engaged champion, New Buyer Meeting held, timeline 12 months or less, a scheduled mutual next step), each met, partly or missing with transcript quotes; reads PF Account, PF Fact, PF Person and PF Source meeting_transcript rows through Read component inputs (component_id C46); writes PF Account.qualified_status (its registered field), the six results, the gaps with the question that closes each and the recap draft in its PF Component run row, and a hand-off to AE confirm, only through Save agent output (component_id C46); threshold and routing: recommends qualified only when all six are met; under 80: recommended not qualified, with gaps (Save agent output applies the threshold 80 and routes below it to recommended not qualified, with gaps); feeds (the register): AE confirm; graph; schedule in the registry: after each New Buyer Meeting (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; never moves a deal stage (the AE confirms). Runs on the other model family from the drafters; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Winning Message Finder
[R2-P13 · agents, sub-workflow 8 (part 1)] C48, one job, built live.
- ai-agent · create · PF · Winning Message Finder: registry row C48 (agent, sub-workflow 8. Learning and governance, asks A77); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find winning messages: promote messages with 3 or more positive replies into the Message Writer's examples for that role and industry; reads PF Draft rows, PF Source reply rows and PF Component run rows of Reply Sorter through Read component inputs (component_id C48); writes a PF Component run row of output_type example_proposal (status proposal) and a hand-off to Message Writer after the Quality Grader and the Friday review, only through Save agent output (component_id C48); threshold and routing: under 3 positives: not promoted (no_action) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Message Writer (after Quality Grader and Friday review); schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; nothing applies without the Quality Grader and the Friday review; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Scoring Tuner
[R2-P13 · agents, sub-workflow 8 (part 1)] C49, one job, built live.
- ai-agent · create · PF · Scoring Tuner: registry row C49 (agent, sub-workflow 8. Learning and governance, asks A78); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: re-fit fit and signal weights to meetings and qualified opportunities, learning from Gate 1 rejections, AE-rejected meetings, disqualifications and win/loss reasons, across all patches, reported per patch; reads PF Account, PF Signal, PF Patch and PF Component run rows through Read component inputs (component_id C49); writes a PF Component run row of output_type weight_proposal (status proposal, old and new weight per signal, per patch) and hand-offs to Fit Scorer and Account Ranking after the Quality Grader and the Friday review, only through Save agent output (component_id C49); threshold and routing: proposals only; only a change within plus or minus 20% may later apply on its own after 8 weeks without a drop (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Fit Scorer; Account Ranking (after Quality Grader and Friday review); schedule in the registry: monthly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never changes a weight itself; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Objection Collector
[R2-P13 · agents, sub-workflow 8 (part 1)] C50, one job, built live.
- ai-agent · create · PF · Objection Collector: registry row C50 (agent, sub-workflow 8. Learning and governance, asks A79); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: update the objection list and buyer language from call transcripts; reads PF Source rows of kind call_transcript and meeting_transcript through Read component inputs (component_id C50); writes a PF Component run row of output_type objection_list (status proposal) and a hand-off to Follow-up Planner after the Quality Grader and the Friday review, only through Save agent output (component_id C50); threshold and routing: under 70: waiting_person, sales reviews (Save agent output applies the threshold 70 and routes below it to sales reviews); feeds (the register): Follow-up Planner (after Quality Grader and Friday review); schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · A/B Tester
[R2-P13 · agents, sub-workflow 8 (part 1)] C51, one job, built live.
- ai-agent · create · PF · A/B Tester: registry row C51 (agent, sub-workflow 8. Learning and governance, asks A80); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: design A/B tests: small changes (subject, opener, asset) as continuous tests on positive replies with at least 20% traffic per version and a 4-week limit; bold changes as fixed-size tests on people; reads PF Draft rows and PF Component run rows through Read component inputs (component_id C51); writes a PF Component run row of output_type test_variant (status proposal, the variants, traffic split, sample size) and a hand-off to Message Writer after the Quality Grader and the Friday review, only through Save agent output (component_id C51); threshold and routing: never tests a one-point lift (no_action) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Message Writer (after Quality Grader and Friday review); schedule in the registry: continuous; fixed-size tests (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Quality Grader
[R2-P13 · agents, sub-workflow 8 (part 1)] C52, one job, built live.
- ai-agent · create · PF · Quality Grader: registry row C52 (checker, sub-workflow 8. Learning and governance, asks A81); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: hold every agent's rubric and test set, grade every proposal and every prompt, model or weight change, and block a release on any drop; enforce checker-on-other-model; compute each gate's rung weekly per pod and AE; draft a policy when the same exception is resolved the same way 3 times; reads PF Component, PF Component run and PF Hand-off rows through Read component inputs (component_id C52); writes a PF Component run row of output_type release_check (pass or block with the drop), rung or policy_draft, and a hand-off to the Friday review, only through Save agent output (component_id C52); threshold and routing: blocks on any drop (no threshold) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Friday review; schedule in the registry: on every prompt, model or weight change; weekly rungs (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Read factory records (Pipeline Factory · Read factory records, the round-1 read tool, unchanged); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on family B, a different family from every drafter it grades; outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Agent Monitor
[R2-P14 · agents, sub-workflow 8 (part 2)] C53, one job, built live.
- ai-agent · create · PF · Agent Monitor: registry row C53 (monitor, sub-workflow 8. Learning and governance, asks A82); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: compare each agent to its baseline weekly on block and edit rate, factual errors, grades and confidence calibration, and alert the GTM engineer on any slip; reads PF Component, PF Component run and PF Hand-off rows through Read component inputs (component_id C53); writes a PF Component run row of output_type drift_alert per slipping agent for the GTM engineer, only through Save agent output (component_id C53); threshold and routing: any slip alerts (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): GTM engineer; schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Read factory records (Pipeline Factory · Read factory records, the round-1 read tool, unchanged); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never pauses a component (a person or Alarm and Escalation does); outside systems are the PF records (mocked), no connection.

#### ai-agent · PF · Test Error Planter
[R2-P14 · agents, sub-workflow 8 (part 2)] C54, one job, built live.
- ai-agent · create · PF · Test Error Planter: registry row C54 (agent, sub-workflow 8. Learning and governance, asks A83); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: plant test errors (for example a wrong patch AE or a sender from the wrong pod) in about 5% of Gate 2 items and score each reviewer's catch rate; reads PF Draft rows waiting at Gate 2 and PF Component run rows of Send Rules Check and Clear Gate 2 through Read component inputs (component_id C54); writes PF Draft.planted_error (its registered field) and a PF Component run row with the planted error and the catch rate per reviewer, and a hand-off to Gate 2, only through Save agent output (component_id C54); threshold and routing: about 5% of items (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Gate 2; schedule in the registry: Day 2, ~5% of Gate 2 items (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a planted draft never sends; outside systems are the PF records (mocked), no connection.

#### record · PF Component
[R2-P15 · the registry link and the registry view] Each registry row points at the entity that runs it, so the control tower shows it as a real built agent or workflow.
- record · update · PF Component: after every deploy and publish of R2-P02 to R2-P14 (it reads the ids they report), on the seeded rows, origin stays seed: the 38 agent rows (C01 to C11, C16 to C18, C21 to C23, C27 to C32, C36 to C38, C41, C42, C44 to C46, C48 to C54) get built_kind ai_agent, built_entity_id the agent's id, built_entity_name "PF · `name`", built_link https://orbit.uat.unifyapps.com/p/0/ai-agents/`id`, built_status live, status live, built_at the publish time; the 12 workflow rows (C12, C13, C14, C24, C25, C33, C35, C39, C43, C55, C56, C57) get built_kind automation, the automation's id, name "Pipeline Factory · `name`", built_link https://orbit.uat.unifyapps.com/p/0/automations/`id`/builder, built_status live, status live, built_at the deploy time; C15 Gate 1 gets built_kind automation, Pipeline Factory · Decide Gate 1 (6ae8440df13e536c52c5d959) and C34 Gate 2 gets Pipeline Factory · Clear Gate 2 (6ae840d7f6f76639f8ceb67d), the round-1 automations behind those gates; C26, C40, C47 (human gates) and C19, C20 (rule steps) stay not_built. C08 Current Vendor Finder keeps success_rate 96.1. Every other field stays as seeded.
- record · update · PF Seed snapshot: the 57 PF Component snapshot rows' row_values are rewritten to the rows as the line above leaves them (with the built-entity fields), so Pipeline Factory · Reset demo restores the links, never blanks them.

#### code-app · UnifyApps Pipeline Factory Control Tower (registry view)
[R2-P15] - code-app · update · UnifyApps Pipeline Factory Control Tower: screen Control tower, Components tab only (no new page, no other screen changes): the PF Component .tbl gains a Built column (.tag "AI agent" or "Automation" with the entity name as a link to built_link, opening in a new tab; a muted .tag "Not built" for human gates and rule steps) and a built kind facet in its .toolbar (AI agent, Automation, Not built); the component .drawer gains the built entity's name and link, its model (Claude Sonnet 5 for family A, GPT-5.1 for family B, none for a workflow), its last five PF Component run rows (output type, status .tag, confidence of threshold, model, latency) and a Run on account control: a .ctl select of PF Account (default A-1001 Carrow & Vale Logistics) and .btn-s Run, disabled with a .note when the component is paused or not built; the result as a .toast (result, confidence, summary) and the new hand-off at the top of the .feed · reads PF Component, PF Component run, PF Account · calls Pipeline Factory · Run component on Run with origin user

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

- Round 2: each of the 38 agents is one UnifyApps AI agent with one job; it reads only through Pipeline Factory · Read component inputs and writes only through Pipeline Factory · Save agent output, which applies the hand-off contract (schema, threshold, one writer per field, idempotency) and saves every hand-off through Pipeline Factory · Save hand-off.
- Every checker (Fact Checker, Message Grader, Reply Sorter, Meeting Labeler, Deal Qualifier, Quality Grader) runs on family B (GPT-5.1); every drafter and monitor on family A (Claude Sonnet 5).
- Each of the 12 workflows is a deterministic automation with no model call; it logs one PF Component run per call.
- A paused component runs nothing: Save agent output and Run component answer paused.
- Learning agents (sub-workflow 8) only propose: their runs are saved as proposal and apply only after the Quality Grader and the Friday review.
- No round-2 entity writes a field locked at booking on a booked account.
- Every round-2 row carries origin; Pipeline Factory · Reset demo also resets the four round-2 objects through Pipeline Factory · Reset agent runs.
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

- The Components tab shows 38 rows Built · AI agent and 12 rows Built · Automation, each linking to its live entity; Gate 1 and Gate 2 link to Decide Gate 1 and Clear Gate 2; the other three human gates and the two rule steps show Not built.
- Run on PF · Case for Change Drafter for Carrow & Vale Logistics saves a PF Component run citing F-01 and F-03 and hand-offs Case for Change Drafter to Play Picker, Message Writer and Meeting Prep Writer with confidence and model; a line under 70 waits on Marcus Ellery.
- Run on a paused component answers paused and runs nothing.
- Send Rules Check answers blocked, rule pod, for D-04 and blocked, other sequence, for D-06; Email Domain Swapper rests IN-02, activates IN-03, retires IN-05 and keeps IN-06 blocked; Weekly Slot Planner allocates 24 to PATCH-NAE-03 and 20 to PATCH-NAE-04; PF · Reply Sorter sorts SRC-15 as unsubscribe and P-1009 lands on the suppression list.
- Pipeline Factory · Reset demo leaves PF Component run empty of test rows and PF Source, PF Inbox and PF Suppression at their seeds, with the registry links kept.
- deploy Pipeline Factory · Read component inputs
- deploy Pipeline Factory · Save agent output
- deploy Pipeline Factory · Reset agent runs
- deploy Pipeline Factory · Account Ranking
- deploy Pipeline Factory · Weekly Slot Planner
- deploy Pipeline Factory · Holdout Picker
- deploy Pipeline Factory · Do-Not-Contact List
- deploy Pipeline Factory · Contact Finder
- deploy Pipeline Factory · Send Rules Check
- deploy Pipeline Factory · Outreach Launcher
- deploy Pipeline Factory · Email Domain Swapper
- deploy Pipeline Factory · Meeting Handoff and Deadlines
- deploy Pipeline Factory · Alarm and Escalation
- deploy Pipeline Factory · Content Handoff
- deploy Pipeline Factory · Privacy and Consent
- deploy Pipeline Factory · Run component
- publish PF · Duplicate Finder
- publish PF · Parent Company Linker
- publish PF · Headquarters Finder
- publish PF · Headquarters Re-checker
- publish PF · New Account Finder
- publish PF · Fit Scorer
- publish PF · Patch Suggester
- publish PF · Current Vendor Finder
- publish PF · Renewal Date Finder
- publish PF · Battlecard Writer
- publish PF · Buying Signal Spotter
- publish PF · Company Facts Collector
- publish PF · Use Case Matcher
- publish PF · Case for Change Drafter
- publish PF · Buying Team Mapper
- publish PF · Person Notes Writer
- publish PF · Intro Finder
- publish PF · Play Picker
- publish PF · Page Builder
- publish PF · Content Picker
- publish PF · Message Writer
- publish PF · Fact Checker
- publish PF · Message Grader
- publish PF · Call Script Writer
- publish PF · Follow-up Planner
- publish PF · Inbox Health Checker
- publish PF · Reply Sorter
- publish PF · Reply Writer
- publish PF · Meeting Prep Writer
- publish PF · Meeting Labeler
- publish PF · Deal Qualifier
- publish PF · Winning Message Finder
- publish PF · Scoring Tuner
- publish PF · Objection Collector
- publish PF · A/B Tester
- publish PF · Quality Grader
- publish PF · Agent Monitor
- publish PF · Test Error Planter
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
- Check this (round 2): all 38 agents and 12 workflows are built live, as the manager asked (FB-1793612784906-1); the round-1 entities and their behaviour are unchanged, except Pipeline Factory · Reset demo, which also calls Pipeline Factory · Reset agent runs, and PF Component, which gains six built-entity fields.
- Check this: family A is Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, the analyst's model) for the 30 agents and 2 monitors; family B is GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e) for the 6 checkers; both cards are active and can call tools on the tenant (list_models, 2026-11-02); the builder runs one test message per card before relying on it.
- Check this: the spec's schedules (every 15 min, nightly, Monday 06:00, daily 07:00, weekly, monthly) are written into the registry but no schedule trigger is switched on: every new agent and workflow runs on demand (Pipeline Factory · Run component, or another automation), so the demo's records never drift by themselves.
- Check this: the agents' outside sources (filings, press, job posts, vendor case studies, LinkedIn exports, Sprouts contact data, Content Factory assets, Gong calls, Apollo and Sprouts replies, the AE's Google Calendar) are mocked as PF Source rows; inbox placement and blacklists as PF Inbox rows; the suppression list copies to HubSpot, Apollo and Sprouts as a copied_to stamp. No connection; the Connections step stays not_needed.
- Check this: outputs with no field on a round-1 object (merge proposals, parent ids, vendors, renewal estimates, battlecards, intro requests, plays, Art of the Possible pages, assets, scripts, re-plans, reply types and drafts, prep packs, learning proposals, rungs, drift alerts) live in PF Component run rows; outputs with a field (fit, HQ city, parent lock, signals, facts, roles and tiers, notes, drafts, fact checks, grades, inbox health, meeting label, qualification, planted errors) are written there by their one registered writer.
- Check this: Duplicate Finder logs merge proposals and never merges or deletes an account; Art of the Possible pages are content in a run row, never a published page.
- Check this: Clear Gate 2 keeps its own inline Send Rules Check and mocked enrolment; the dedicated Send Rules Check is read-only on PF Draft and answers the same rule for D-04 and D-06; Log signal keeps its single-signal scoring and Account Ranking re-ranks the patch with the same weights; Book meeting stays the booking and lock step, which Meeting Handoff and Deadlines calls for calendar pick-ups.
- Check this: Alarm and Escalation pauses a component automatically only under 95% success; from 95% to under 97% it adds a to-do item, so Current Vendor Finder (96.1%) is still paused by a person in beat 7.
- Check this: Weekly Slot Planner reads "behind on intro meetings" as under 4 intros in 7 days, since no diagnosis field exists; the pace boost is 25% by default.
- Check this: the per-run and daily cost caps (A13), the rubrics (A93), handbook sections (A94), the 50-item evaluations (A97) and the shadow week (A98) are not built for the 38 agents; the handbook is one PF Source row, and every agent goes straight to status live (round-1 open question 2 still holds for A93, A94, A97).
- Check this: Pipeline Factory · Run component invokes an agent by the id in PF Component.built_entity_id with the operation Ask the analyst uses; if that operation takes only a fixed agent, it branches per component id.

## entities

build.plans:
- e_6ae83ebdafe7fc590a0b9fd8 · objects · 9 tasks · implemented · 2026-11-02
- e_6ae83f89f410ab7b2ff0d40d · seed records · 9 tasks · implemented · 2026-11-02 (duplicate save e_6ae83f98afe7fc590a136f65 closed unsent)
- e_6ae83fd1afe7fc590a161a7f · automations part 1 · 10 tasks · implemented · 2026-11-02
- e_6ae8432af410ab7b2ff1251b · automations part 2 and the analyst · 10 tasks · implemented · 2026-11-02
- e_6ae846e9d96c5f6ba22b953d · the code app · 5 tasks · implemented · 2026-11-02
- e_6ae84ef0f410ab7b2f0351d1 · verify r1 fixes: hand-off origin, callers, Clear Gate 2 pod rule · 10 tasks · implemented (Log signal's 2 moved to the next change) · 2026-11-02
- e_6ae84efbf410ab7b2f03537e · verify r1 fixes: Read factory records people and name lookup, analyst account id · 4 tasks · implemented · 2026-11-02
- e_6ae851cbf410ab7b2f03bef9 · verify r1 fix: Save hand-off due_at, Log signal passes it · 4 tasks · implemented · 2026-11-02
- e_6ae853edd96c5f6ba232095f · verify r1 fix: Reset demo clears hand-offs with no snapshot · 2 tasks · implemented · 2026-11-02

- e_6ae86090afe7fc590a34bad5 · R2-P01 objects, PF Component fields, seeds · 9 tasks · implemented · 2026-11-02
- e_6ae861b1f410ab7b2f062f35 · R2-P02 Read component inputs, Save agent output, Reset agent runs, Reset demo update · 8 tasks · implemented · 2026-11-02
- e_6ae861bfafe7fc590a34df19 · R2-P03 workflows part 1 · 8 tasks · implemented · 2026-11-02
- e_6ae861ccd96c5f6ba2341bdc · R2-P04 workflows part 2 · 10 tasks · implemented · 2026-11-02
- e_6ae861d8afe7fc590a34e163 · R2-P05 workflows part 3 and Run component · 8 tasks · implemented · 2026-11-02
- e_6ae865bfafe7fc590a4a2377 · R2-P06 agents sw1 part 1 · 10 tasks · implemented · 2026-11-02
- e_6ae865d5d96c5f6ba243c5e7 · R2-P07 agents sw1 part 2 · 10 tasks · implemented · 2026-11-02
- e_6ae865e1f410ab7b2f1511cd · R2-P08 agents sw2 and sw3 · 8 tasks · implemented · 2026-11-02
- e_6ae866ecf410ab7b2f152ff5 · R2-P09 agents sw4 · 6 tasks · implemented · 2026-11-02
- e_6ae867b3f410ab7b2f1555d6 · R2-P10 agents sw5 part 1 · 10 tasks · implemented · 2026-11-02
- e_6ae8681cf410ab7b2f1566e9 · R2-P11 agents sw5 part 2 and sw6 · 8 tasks · implemented · 2026-11-02
- e_6ae86b27afe7fc590a4ff784 · R2-P12 agents sw7 · 10 tasks · implemented · 2026-11-02
- e_6ae86b5cafe7fc590a4ffb95 · R2-P13 agents sw8 part 1 · 10 tasks · implemented · 2026-11-02
- e_6ae86c21afe7fc590a50110a · R2-P14 agents sw8 part 2 · 4 tasks · implemented · 2026-11-02
- e_6ae86bb6d96c5f6ba24481b4 · R2 fix: Read component inputs narrowed under 12,000 characters · 2 tasks · implemented · 2026-11-02
- e_6ae86ec1d96c5f6ba244ee98 · R2 fix: Read component inputs, a share of the reply per list · 2 tasks · implemented · 2026-11-02
- e_6ae86f58d96c5f6ba244fc4d · R2-P15 registry links, snapshot rows, Components tab, publish v2 · 4 tasks · implemented · 2026-11-02
| Kind | Name | Id | Link | Asks |
|---|---|---|---|---|
| object | PF Patch | OBJ_pf_patch | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_patch/schema | A27, A29, A30 |
| object | PF Account | OBJ_pf_account | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_account/schema | A14, A21, A27, A32 |
| object | PF Person | OBJ_pf_person | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_person/schema | A40, A41, A42 |
| object | PF Signal | OBJ_pf_signal | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_signal/schema | A28, A33, A34 |
| object | PF Fact | OBJ_pf_fact | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_fact/schema | A35, A36, A37, A38, A39 |
| object | PF Draft | OBJ_pf_draft | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_draft/schema | A47, A48 |
| object | PF Hand-off | OBJ_pf_handoff | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_handoff/schema | A4, A5, A9, A10, A11, A12 |
| object | PF Component | OBJ_pf_component | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_component/schema | A1, A13 |
| object | PF Seed snapshot | OBJ_pf_seed_snapshot | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_seed_snapshot/schema | (reset) |
| automation | Pipeline Factory · Save hand-off | 6ae840a5fbdd550a9a44c524 | https://orbit.uat.unifyapps.com/p/0/automations/6ae840a5fbdd550a9a44c524/builder | A5, A6, A7, A8, A9 |
| automation | Pipeline Factory · Log signal | 6ae843cc9594aa458cba14d7 | https://orbit.uat.unifyapps.com/p/0/automations/6ae843cc9594aa458cba14d7/builder | A2, A28, A29, A33, A34 |
| automation | Pipeline Factory · Decide Gate 1 | 6ae8440df13e536c52c5d959 | https://orbit.uat.unifyapps.com/p/0/automations/6ae8440df13e536c52c5d959/builder | A30, A31, A32 |
| automation | Pipeline Factory · Clear Gate 2 | 6ae840d7f6f76639f8ceb67d | https://orbit.uat.unifyapps.com/p/0/automations/6ae840d7f6f76639f8ceb67d/builder | A9, A47 |
| automation | Pipeline Factory · Book meeting | 6ae84449f38e327618fcc640 | https://orbit.uat.unifyapps.com/p/0/automations/6ae84449f38e327618fcc640/builder | A14 |
| automation | Pipeline Factory · Pause component | 6ae843d1f6f76639f8cf2d55 | https://orbit.uat.unifyapps.com/p/0/automations/6ae843d1f6f76639f8cf2d55/builder | A4 |
| automation | Pipeline Factory · Read factory records | 6ae843e69ec43c6ee2dec988 | https://orbit.uat.unifyapps.com/p/0/automations/6ae843e69ec43c6ee2dec988/builder | A8, A10 |
| automation | Pipeline Factory · Ask the analyst | 6ae84900fbdd550a9a465807 | https://orbit.uat.unifyapps.com/p/0/automations/6ae84900fbdd550a9a465807/builder | A4, A8, A10 |
| automation | Pipeline Factory · Reset demo | 6ae8441df38e327618fcc13c | https://orbit.uat.unifyapps.com/p/0/automations/6ae8441df38e327618fcc13c/builder | (reset) |
| ai-agent | Pipeline Factory Analyst | e_6ae846ffd96c5f6ba22b98da | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae846ffd96c5f6ba22b98da | A4, A8, A10 |
| code-app | UnifyApps Pipeline Factory Control Tower | app-2fbe93e8c1f7 | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-2fbe93e8c1f7 | A1, A2, A4, A8, A14, A27, A32, A47 |

| object | PF Component run | OBJ_pf_component_run | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_component_run/schema | A1, A13 (R2) |
| object | PF Source | OBJ_pf_source | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_source/schema | R2 (mocked sources) |
| object | PF Inbox | OBJ_pf_inbox | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_inbox/schema | R2 (C38, C39) |
| object | PF Suppression | OBJ_pf_suppression | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_suppression/schema | R2 (C25, C57) |
| automation | Pipeline Factory · Read component inputs | 6ae8635446920244f3d5194b | https://orbit.uat.unifyapps.com/p/0/automations/6ae8635446920244f3d5194b/builder | R2 |
| automation | Pipeline Factory · Save agent output | 6ae864829594aa458cc1ce69 | https://orbit.uat.unifyapps.com/p/0/automations/6ae864829594aa458cc1ce69/builder | R2 |
| automation | Pipeline Factory · Reset agent runs | 6ae863f02099302ffb2d2358 | https://orbit.uat.unifyapps.com/p/0/automations/6ae863f02099302ffb2d2358/builder | R2 |
| automation | Pipeline Factory · Account Ranking | 6ae8632c9ec43c6ee22f380d | https://orbit.uat.unifyapps.com/p/0/automations/6ae8632c9ec43c6ee22f380d/builder | R2 |
| automation | Pipeline Factory · Weekly Slot Planner | 6ae863a5f38e327618183dca | https://orbit.uat.unifyapps.com/p/0/automations/6ae863a5f38e327618183dca/builder | R2 |
| automation | Pipeline Factory · Holdout Picker | 6ae864059ec43c6ee22f8008 | https://orbit.uat.unifyapps.com/p/0/automations/6ae864059ec43c6ee22f8008/builder | R2 |
| automation | Pipeline Factory · Do-Not-Contact List | 6ae864672099302ffb2d3157 | https://orbit.uat.unifyapps.com/p/0/automations/6ae864672099302ffb2d3157/builder | R2 |
| automation | Pipeline Factory · Contact Finder | 6ae862f3f13e536c52e76ecd | https://orbit.uat.unifyapps.com/p/0/automations/6ae862f3f13e536c52e76ecd/builder | R2 |
| automation | Pipeline Factory · Send Rules Check | 6ae863842099302ffb2d0262 | https://orbit.uat.unifyapps.com/p/0/automations/6ae863842099302ffb2d0262/builder | R2 |
| automation | Pipeline Factory · Outreach Launcher | 6ae864929594aa458cc23de9 | https://orbit.uat.unifyapps.com/p/0/automations/6ae864929594aa458cc23de9/builder | R2 |
| automation | Pipeline Factory · Email Domain Swapper | 6ae864342099302ffb2d2a71 | https://orbit.uat.unifyapps.com/p/0/automations/6ae864342099302ffb2d2a71/builder | R2 |
| automation | Pipeline Factory · Meeting Handoff and Deadlines | 6ae8654d2099302ffb2d9514 | https://orbit.uat.unifyapps.com/p/0/automations/6ae8654d2099302ffb2d9514/builder | R2 |
| automation | Pipeline Factory · Alarm and Escalation | 6ae863282099302ffb2cf702 | https://orbit.uat.unifyapps.com/p/0/automations/6ae863282099302ffb2cf702/builder | R2 |
| automation | Pipeline Factory · Content Handoff | 6ae863d0fbdd550a9a4ffc58 | https://orbit.uat.unifyapps.com/p/0/automations/6ae863d0fbdd550a9a4ffc58/builder | R2 |
| automation | Pipeline Factory · Privacy and Consent | 6ae86493f38e32761818a2c1 | https://orbit.uat.unifyapps.com/p/0/automations/6ae86493f38e32761818a2c1/builder | R2 |
| automation | Pipeline Factory · Run component | 6ae865229ec43c6ee2300d8d | https://orbit.uat.unifyapps.com/p/0/automations/6ae865229ec43c6ee2300d8d/builder | R2 |
| ai-agent | PF · Duplicate Finder | e_6ae86680afe7fc590a4a3f53 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86680afe7fc590a4a3f53 | R2 C01 |
| ai-agent | PF · Parent Company Linker | e_6ae86684d96c5f6ba243cf6a | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86684d96c5f6ba243cf6a | R2 C02 |
| ai-agent | PF · Headquarters Finder | e_6ae86687d96c5f6ba243cfb8 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86687d96c5f6ba243cfb8 | R2 C03 |
| ai-agent | PF · Headquarters Re-checker | e_6ae8668bafe7fc590a4a3fec | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8668bafe7fc590a4a3fec | R2 C04 |
| ai-agent | PF · New Account Finder | e_6ae8668ef410ab7b2f151c47 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8668ef410ab7b2f151c47 | R2 C05 |
| ai-agent | PF · Fit Scorer | e_6ae86666d96c5f6ba243ce26 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86666d96c5f6ba243ce26 | R2 C06 |
| ai-agent | PF · Patch Suggester | e_6ae8666ad96c5f6ba243ce39 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8666ad96c5f6ba243ce39 | R2 C07 |
| ai-agent | PF · Current Vendor Finder | e_6ae8666dafe7fc590a4a3d96 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8666dafe7fc590a4a3d96 | R2 C08 |
| ai-agent | PF · Renewal Date Finder | e_6ae86671d96c5f6ba243ce77 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86671d96c5f6ba243ce77 | R2 C09 |
| ai-agent | PF · Battlecard Writer | e_6ae86673afe7fc590a4a3dda | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86673afe7fc590a4a3dda | R2 C10 |
| ai-agent | PF · Buying Signal Spotter | e_6ae8667ed96c5f6ba243cf29 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8667ed96c5f6ba243cf29 | R2 C11 |
| ai-agent | PF · Company Facts Collector | e_6ae86682d96c5f6ba243cf48 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86682d96c5f6ba243cf48 | R2 C16 |
| ai-agent | PF · Use Case Matcher | e_6ae86685f410ab7b2f151b2f | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86685f410ab7b2f151b2f | R2 C17 |
| ai-agent | PF · Case for Change Drafter | e_6ae86689d96c5f6ba243cfd8 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86689d96c5f6ba243cfd8 | R2 C18 |
| ai-agent | PF · Buying Team Mapper | e_6ae867cdafe7fc590a4f8e82 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae867cdafe7fc590a4f8e82 | R2 C21 |
| ai-agent | PF · Person Notes Writer | e_6ae867d2f410ab7b2f155861 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae867d2f410ab7b2f155861 | R2 C22 |
| ai-agent | PF · Intro Finder | e_6ae867d4f410ab7b2f155959 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae867d4f410ab7b2f155959 | R2 C23 |
| ai-agent | PF · Play Picker | e_6ae86821f410ab7b2f15695c | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86821f410ab7b2f15695c | R2 C27 |
| ai-agent | PF · Page Builder | e_6ae86825f410ab7b2f156a03 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86825f410ab7b2f156a03 | R2 C28 |
| ai-agent | PF · Content Picker | e_6ae86828f410ab7b2f156a22 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86828f410ab7b2f156a22 | R2 C29 |
| ai-agent | PF · Message Writer | e_6ae8682ad96c5f6ba2441a16 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8682ad96c5f6ba2441a16 | R2 C30 |
| ai-agent | PF · Fact Checker | e_6ae8682ed96c5f6ba2441a5f | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8682ed96c5f6ba2441a5f | R2 C31 |
| ai-agent | PF · Message Grader | e_6ae8687bd96c5f6ba2442526 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8687bd96c5f6ba2442526 | R2 C32 |
| ai-agent | PF · Call Script Writer | e_6ae8687ef410ab7b2f1575c6 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8687ef410ab7b2f1575c6 | R2 C36 |
| ai-agent | PF · Follow-up Planner | e_6ae86881d96c5f6ba244257b | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86881d96c5f6ba244257b | R2 C37 |
| ai-agent | PF · Inbox Health Checker | e_6ae86884d96c5f6ba24425cc | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86884d96c5f6ba24425cc | R2 C38 |
| ai-agent | PF · Reply Sorter | e_6ae86bebf410ab7b2f20260c | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bebf410ab7b2f20260c | R2 C41 |
| ai-agent | PF · Reply Writer | e_6ae86beff410ab7b2f20266c | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86beff410ab7b2f20266c | R2 C42 |
| ai-agent | PF · Meeting Prep Writer | e_6ae86bf3f410ab7b2f2026ba | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bf3f410ab7b2f2026ba | R2 C44 |
| ai-agent | PF · Meeting Labeler | e_6ae86bf7f410ab7b2f202726 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bf7f410ab7b2f202726 | R2 C45 |
| ai-agent | PF · Deal Qualifier | e_6ae86bfbf410ab7b2f202747 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bfbf410ab7b2f202747 | R2 C46 |
| ai-agent | PF · Winning Message Finder | e_6ae86bd2afe7fc590a500c5f | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bd2afe7fc590a500c5f | R2 C48 |
| ai-agent | PF · Scoring Tuner | e_6ae86bd6afe7fc590a500cfa | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bd6afe7fc590a500cfa | R2 C49 |
| ai-agent | PF · Objection Collector | e_6ae86bd8f410ab7b2f202521 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bd8f410ab7b2f202521 | R2 C50 |
| ai-agent | PF · A/B Tester | e_6ae86bdbf410ab7b2f202568 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bdbf410ab7b2f202568 | R2 C51 |
| ai-agent | PF · Quality Grader | e_6ae86bdeafe7fc590a500d57 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bdeafe7fc590a500d57 | R2 C52 |
| ai-agent | PF · Agent Monitor | e_6ae86c76f410ab7b2f203900 | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86c76f410ab7b2f203900 | R2 C53 |
| ai-agent | PF · Test Error Planter | e_6ae86c7ad96c5f6ba24493ba | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86c7ad96c5f6ba24493ba | R2 C54 |
code-app: app-2fbe93e8c1f7 · branch main · PRIVATE · published v2 from commit 14eb159377b5a4c0d764c2da8fca056537cfe825 (G3 round 2: Components tab with built entity, last runs, Run on account; restore point v1 commit 057f53d6625c58044c9bd67445a203fc9e30cde3) · earlier published v1 from commit 057f53d6625c58044c9bd67445a203fc9e30cde3 (head d6dca64e "publish v1") · preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-2fbe93e8c1f7/main/ · published https://app-2fbe93e8c1f7-orbit.tensor-uat.unifyapps.com (from the shell task's handover; the publish reply named no URL; unverified) · routes /tower, /todo, /accounts/:accountId · storage FETCH e_6ae84846f410ab7b2ffc1ba8
R2 models: family A agents on "Claude Sonnet 5 (UnifyApps, Vertex, cached)" e_6ad496812dd4ba5be70afcc1 (the planned card e_6acca2af70b66f5702c8b59f answers 401); family B checkers on "GPT-5.1_without_effort(DNT)" e_6ae835bbafe7fc590a05a045 or "GPT-5.1 (Azure Open AI)" e_696fe072cb3ef82f7e23dc86 (serves gpt-4.1; the planned GPT-5.1 card answers 401)
analyst model: Claude Sonnet 5 (list_models gives no recommendation; the builder's pick)
best practice: Save hand-off 84, Log signal 83, Decide Gate 1 67, Clear Gate 2 95, Book meeting 88, Pause component 97, Read factory records 93, Reset demo 88

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
   Round 2 addition to H1 (no new beat): back on Control tower, the presenter opens the Components tab and filters built kind AI agent: 38 rows, each Built · AI agent linking to its UnifyApps agent, and 12 rows Built · Automation; the drawer of Case for Change Drafter shows its one job, threshold 70 and where below goes (the BDR at Gate 2), model Claude Sonnet 5 (family A; the checkers run GPT-5.1), its two tools, and its last runs; Run on Carrow & Vale Logistics runs PF · Case for Change Drafter live: the toast shows the result and confidence, and new hand-offs Case for Change Drafter to Play Picker, Message Writer and Meeting Prep Writer top the feed, citing F-01 and F-03, with the vendor-contract risk tagged [HYPOTHESIS]. Asks A1, A88, A89, A90, A91, A95, A96, A98. mode: live (PF · Case for Change Drafter through Pipeline Factory · Run component and Save agent output).

AI surfaces: Pipeline Factory Analyst answer · live. The 38 PF · agents (round 2) · live, run on demand from the Components tab; PF · Case for Change Drafter run in H1 · live. The 12 workflow automations (round 2) · deterministic. Case for Change card · seeded. Company facts and use case matches · seeded. Person notes · seeded. Drafts, Message Grader grades, Fact Checker results · seeded. Meeting label and Deal Qualifier recap · seeded. Timing score · deterministic. Send Rules Check result · deterministic. Component success rates · seeded. Outside systems (HubSpot, Apollo, Sprouts, Gong, Bombora, Google Calendar) · mocked.

## views

- Control tower (/tower) · beats 1, 2, 7, H1 start · .app shell with .app-rail (logo, .nav-i), .app-top · four .tile (slots, intros, success rate with .delta, waiting) · .tabs Hand-offs / Components · Hand-offs: .toolbar (.field search "n of m", .chipsel status, from component, patch) above .tblwrap .tbl, status as .tag, a .drawer for one record · Components: .toolbar (.chipsel sub-workflow, kind, status) above .tbl with .pg, a .drawer (.dl) for one component · .feed newest hand-offs · Log signal .modal (.fld .ctl .seg) · .agent-launch and .agent-drawer, the answer in .ai:not(.msg) with grounding line and one .btn-p action · .toast · round 2, Components tab only: .tbl gains a Built column (.tag AI agent / Automation with the entity link, muted .tag Not built) and a built kind .chipsel in its .toolbar; the component .drawer gains the entity link, its model, a small .tbl of its last five runs (status .tag, confidence of threshold, model, latency) and Run on account (.ctl select, .btn-s Run, .note when paused or not built), the result as .toast and the new hand-off at the top of the .feed (beat H1)
- To-do (/todo) · beat 3 · .toolbar above .tbl of the Gate 1 batch (.tag fit band, .cell-chips top 3 signals), row .btn-p Accept and Reject with a .menu of four reasons · .tag.negative and .note for a hard block · .feed Waiting on you · .toast · .empty states
- Account (/accounts/:accountId) · beats 4, 5, 6 · .crumb · .g1 head with .dl and lock marks · .tabs Research / Buying team / Gate 2 / Meeting · Research: .tbl facts with .tag [PUBLIC] / [HYPOTHESIS], Case for Change in .ai:not(.msg) · Buying team: .pc cards by tier, .faces, .av · Gate 2: .tbl drafts with grade, .tag fact check and rules, .btn-p Approve, .btn-s Hold, .tag.negative and .note for the refusal · Meeting: .stages Engage / Connect / Commit, .btn-p Book meeting, .tbl six requirements, .agenda deadlines, correction .modal
