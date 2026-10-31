---
use_case: Pipeline Factory
client: UnifyApps
poc_row: POC-unifyapps-pipeline-factory-20261030
owner: Gourav Mahunta · U09EK0B6NKD
manager: Gourav Mahunta · U09EK0B6NKD
status: awaiting_g2
version: 1 · since 2026-10-30T12:44:11Z
channel: C0CDGQKAFTQ
threads:
  g1: 1793364771.321039
  g2: 1793441228.777929
  g3:
  g4:
  connections:
intent:
stage_flag:

gates:
  g1: {status: approved, round: 1, posted_ts: 1793364771.321039, decided_by: Gourav Mahunta, decided_at: 2026-10-31}
  g2: {status: waiting, round: 1, posted_ts: 1793441228.777929}
  connections: {status: not_posted, round: 0, list: []}
  g3: {status: not_posted, round: 0}
  g4: {status: not_posted, round: 0}

posts:
  - when: 2026-10-30T12:52:38Z
    kind: g1
    ts: 1793364771.321039
    by: bot
    version: 1
    round: 1
    documents:
      - {name: "Requirements · Pipeline Factory · v1 r1", type: requirements, file_url: "https://orbit.uat.unifyapps.com/auth/file/asset/download/37c5ac145fc351a33665f584", file_name: requirements-v1-r1.pdf, file_size: 390632}

  - when: 2026-10-30T12:53:01Z
    kind: status
    ts: 1793364771.321039
    by: bot
    version: 1
    round: 1

  - when: 2026-10-31T10:12:00Z
    kind: g2
    ts: 1793441228.777929
    by: bot
    version: 1
    round: 1
    documents:
      - {name: "Plan · Pipeline Factory · v1 r1", type: scope, file_url: "https://sales.uat-us-east-1.unifyapps.com/auth/file/asset/download/0764759eae91a43ccaa7829a", file_name: plan-v1-r1.pdf, file_size: 481254}

  - when: 2026-10-31T10:12:30Z
    kind: status
    ts: 1793441228.777929
    by: bot
    version: 1
    round: 1

runs:
  - started: 2026-10-30T12:44:11Z
    gate: g1
    ended: 2026-10-30T12:52:38Z
    stages: [1-harvest]
    spawns: 1
    tokens: 212
    outcome: posted G1
  - started: 2026-10-31T09:52:00Z
    gate: g2
    ended: 2026-10-31T10:10:00Z
    stages: [2-plan]
    spawns: 1
    tokens: 300291
    outcome: posted G2

stopped:

asks:
  - id: A1
    text: "Registered. A hand-off not in the Hand-off register below does not exist."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A2
    text: "One writer per field. Only the component named in the register writes a field; everyone else reads."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A3
    text: "Schema check on save. A record that fails its JSON schema is rejected, the GTM engineer is alerted, and the downstream step waits. Never substitute generic copy."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A4
    text: "Confidence gate. A record below the component's threshold does not flow on; it goes to the named person's to-do list (thresholds are in each sub-workflow table)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A5
    text: "Idempotent. Every save is keyed on account_id + person_id + play_id. Re-running a hand-off never creates a second copy or a second enrolment."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A6
    text: "On time. Each hand-off has a \"When\". A late one retries, then counts against the component's success rate (target 99%, red under 97%)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A7
    text: "Traced. Every run logs input, output, model, confidence, cost and latency, keyed by patch_id. Failures show in the control towers with their cause."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A8
    text: "Patch-keyed. Every record carries its patch_id and the sender's confidence score."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect, hand-off contract · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A9
    text: "Model split: two AI model families. Every checker (Fact Checker, Message Grader, Reply Sorter, Meeting Labeler, Deal Qualifier, Quality Grader) runs on a different family from the drafter it checks. Each run has a cost cap, plus a daily spend cap."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A10
    text: "Locked fields: Patch ID, BDR of record, meeting type, meeting source, factory-sourced, factory-influenced and marketing-influenced are written only by workflows and lock at booking. Corrections go through RevOps, logged with a reason."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How the agents connect · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A11
    text: "Every 15 min pulls new and changed records, normalises keys (domain, legal name, LinkedIn ID, HubSpot ID, email), merges exact matches and scores near-matches 0–100. ≥95 merge; 80–95 to RevOps; <80 kept separate. Logs its reasoning"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Duplicate Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A12
    text: "Links each company to parent, subsidiaries, divisions; proposes divisions that buy separately (RevOps approves); sets the outreach lock at the top parent. Re-links on HQ change or M&A news. <80 → RevOps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Parent Company Linker\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A13
    text: "Finds the parent's HQ city, state, country; weighs sources; returns location, confidence, other candidates and evidence. <80 → RevOps picks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Headquarters Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A14
    text: "Nightly on companies with move or M&A news, quarterly on all. Any change → alert in the patch control tower, then a new Patch Suggester proposal"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Headquarters Re-checker (monitor)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A15
    text: "Weekly closed-won lookalikes; daily checks 7 other sources (ecosystem lists, intent surges, web visitors, business units, champion job changes, event attendees, renewal windows). Drops fit <36, customers, open deals, partners, competitors, DNC. Suggests to RevOps, never adds. <70 not suggested"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"New Account Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A16
    text: "Scores fit out of 60 (up to 15 each: industry, size and complexity, core systems, AI and integration maturity); maps score + ICP V2 quadrant to best / medium / low fit. Floor 36 never moves. Re-scores on change and monthly. <70 → RevOps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Fit Scorer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A17
    text: "Proposes a patch for each new account or HQ change: geography first, then industry, with confidence and reason. Never writes a Patch ID. <80 → RevOps decides from evidence"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Patch Suggester\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A18
    text: "Finds integration, automation and agent tools each best/medium-fit account uses, from vendor case studies, job posts, procurement notices. Weekly. <60 tagged [HYPOTHESIS]"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Current Vendor Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A19
    text: "Estimates renewal as 3 years from earliest evidence unless a later contract signal exists; raises a renewal signal 9 months before. <60 no signal"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Renewal Date Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A20
    text: "Drafts battlecard changes per vendor: shortfalls, switch path, proof, objection answers. Product marketing approves each"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts, row \"Battlecard Writer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A21
    text: "Watches continuously: web visits and intent, Bombora surges, Sales Navigator alerts, hiring and tech changes, job changes, leadership news, earnings calls, press, renewal signals, event sign-ups. Records company, type, date, source link, strength; verifies company match and date; scores confidence. Strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) go straight to the Play Picker. <70 logged, not scored. Signals fade over 30 days"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 2. Account selection, row \"Buying Signal Spotter\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A22
    text: "Turns signals into a timing score (max 40) with the weights below. Monday 06:00 ranks each patch by fit + timing. Daily 07:00 tops up each patch's batch after fast-lane plays and sends it to Gate 1 with each account's top 3 signals. Applies the checked-visit rule"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 2. Account selection, row \"Account Ranking (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A23
    text: "Monday after ranking: base 25 slots per patch; never more than eligible accounts ÷ 13; floor 15, cap 40; pace boost (up to +50%) only to patches behind on intro meetings whose diagnosis stops at Input or Engagement and whose AE has <6 intros booked in 7 days. Fast-lane plays use their own patch's slots; overflow takes spare capacity, then that patch's lowest-ranked accounts, never another patch's base. AE nominations (max 3/week) start inside their patch's slots. Logs every allocation"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 2. Account selection, row \"Weekly Slot Planner (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A24
    text: "After allocation, randomly holds back 10% of each patch's new medium/low-fit plays with a logged weekly seed. Checks treated vs held-out balance on fit and timing (standardised difference <0.1) or redraws. Flags held accounts in graph and HubSpot with a 90-day end date. Reports at 90 and 180 days"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 2. Account selection, row \"Holdout Picker (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A25
    text: "Batch lands in the BDR's to-do list at 07:00 with fit band, timing, top 3 signals, Patch ID, AE, last touch, slots left. Accept or reject by 10:00 with one reason (bad fit, active deal, wrong timing, already in conversation). A rejected slot refills from the same patch. Hard blocks: no Patch ID / AE / pod, on an AE hold, or held out"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 2. Account selection, row \"Gate 1 (human: pod BDR)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A26
    text: "Checked visit: counts only with 10+ seconds and a scroll, or a repeat visit within 7 days. Never counts visits within 2 minutes of an email's delivery, from security-scanner networks, or with no page interaction."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 2. Account selection · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A27
    text: "Reads the latest annual report and investor deck, last two earnings call transcripts, 12 months of press, current AI/IT/automation job posts. Extracts statements on AI, automation, integration, modernisation, cost, CX, risk. Each fact keeps exact quote, page or timestamp, date, link. Drops anything >12 months old (except the latest annual report). Facts without quote + link are rejected"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 3. Account research, row \"Company Facts Collector\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A28
    text: "Finds candidate VEP-CFC use cases for the industry and core systems; scores evidence; keeps the top 3 with two supporting facts (or one fact + the company's engagement with us); tags each with pattern and outcome. <70 shown only as a question, never a claim"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 3. Account research, row \"Use Case Matcher\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A29
    text: "Writes: business problem in the company's own words, impact (no dollar figures), why now (top signals), why UnifyApps (use case + their core systems), closest proof, main and backup angle, risks (e.g. vendor contract). Every sentence cites a fact or is tagged [HYPOTHESIS]. <70 → BDR reviews at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 3. Account research, row \"Case for Change Drafter\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A30
    text: "Rules: VEP-CFC is the only source of use cases (UC-ID + Blueprint link + account evidence). Guesses are tagged [HYPOTHESIS] and reach prospects only as questions. Conflicting sources are shown side by side, never settled by the agent. Two rule steps also run here: a graph query pulling past contact (events, downloads, visits, calls, past deals, loss reasons), and an account tagger (vertical, Patch ID, size, systems, vendors, AI maturity, fit band, pattern, outcome)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 3. Account research · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A31
    text: "Loads the industry's default titles plus BDR edits; searches people at the company and division; assigns role (economic buyer, champion, technical evaluator, business owner, gatekeeper); checks the champions library; picks 3 Tier 1, 3 Tier 2, 4 Tier 3, 2 backups; flags the economic buyer. Gatekeepers mapped, never contacted. Job-change alerts promote a backup; a title the BDR removes 3× in an industry drops from its defaults. <70 on a role → BDR checks at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 4. Buying committee, row \"Buying Team Mapper\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A32
    text: "Four-line note per person: role, time in role, past companies, public talks and posts; what they own ([HYPOTHESIS] unless public); link to the matched use case; past touches; nearby event fit. Professional info only. Refresh every 90 days and on job change. <70 flagged at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 4. Buying committee, row \"Person Notes Writer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A33
    text: "For Tier 1 at best-fit accounts: finds shared work history with customer execs, partners, employees and AEs; uses opt-in LinkedIn connection exports (monthly) plus partners, SIs, investors. Ranks: worked together > overlapped > friend of a friend. Drafts the intro request into the patch AE's to-do list and holds cold touches to that person 7 days. <60 not suggested"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 4. Buying committee, row \"Intro Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A34
    text: "Sends each person to the Sprouts plugin → verified work email, plus phone for Tier 1 and engaged people. No verified email → LinkedIn only. Saves with source and verify date to graph and HubSpot; re-verifies emails older than 90 days before use"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 4. Buying committee, row \"Contact Finder (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A35
    text: "One suppression list (opt-outs, bounces, complaints, legal holds); copies it to HubSpot, Apollo and Sprouts every 15 min; screens every phone against federal and state DNC before any dialler; records consent per person; completes erasure across all tools within 30 days, keeping only a hashed code so the person is never re-added"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 4. Buying committee, row \"Do-Not-Contact List (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A36
    text: "Best-fit accounts reach the AE's to-do list on Day 1 with account view and buying team (~5/week/patch). Approve, adjust or disqualify by Day 2 12:00; else backup AE, then Geo leader, before Gate 2 closes"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 4. Buying committee, row \"AE checkpoint (human: patch AE, best fit only)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A37
    text: "Matches the signal (or the 13-week cycle) to a play; sets people, channels, start days; spaces tiers so no two people at one account get email the same day; picks senders only from the account's patch and pod (AE for Tier 1 LinkedIn and AE notes, BDR for the rest, executive sponsor for C-level). Also receives fast-lane signals. <70 → BDR picks at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Play Picker\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A38
    text: "Builds one Art of the Possible page per account: operations from public facts only, 2–3 workflows reimagined (before/after) for the matched use cases, proof, how UnifyApps connects their core systems, a patch event. Button books a 60-min session with the patch AE + solution consultant. Fills marketing's locked template; page is noindex, at a hard-to-guess URL, with a tracked link per prospect. <75 → marketing ops checks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Page Builder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A39
    text: "Picks one Content Factory asset per asset touch, matched on role, industry, use case, pattern, outcome, VEP stage, Geo; skips assets >18 months old or retired; ranks by fit and positive-reply history for that role; never the same asset to two people at one account in a week; adds an event only while seats remain. <70 → no asset, use a sourced insight"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Content Picker\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A40
    text: "Writes every email and LinkedIn message in the play. Starts from the Content Factory's best message for category → sub-sector → company → persona and must agree with all four; uses the assigned handbook voice; one sourced fact, the pain this person owns, the likeliest objection for their role. Names the patch AE as session host. Pod-inbox emails in the BDR's name; AE notes from the AE's mailbox, warm plays only. <70 flagged at Gate 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Message Writer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A41
    text: "Traces every claim in drafts and pages: facts to a public source ≤12 months old, numbers to a source or the proof library, use cases to a UC-ID with account evidence. Blocks anything untraceable"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Fact Checker (checker, other model family)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A42
    text: "Scores each draft 0–100 on the message rubric: teaches something, relevant to role and company, actionable, applies to their business, well written in the right voice, follows copy rules. <75 → one automatic rewrite and regrade; <75 again → a person decides at Gate 2. Rubric weights checked monthly against replies"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Message Grader (checker, other model family)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A43
    text: "Blocks any draft that fails: clean text (no empty fields, wrong names incl. the AE's); person still in role (checked within 7 days of first send); not on DNC, held out, a customer or open deal; parent outreach lock owned by this owner; Patch ID, AE, pod present and no AE hold; sender from the account's pod and under their daily limit across all pods; person not in another sequence; state send window, consent, legal footer"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Send Rules Check (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A44
    text: "One screen per account: account view, buying team, page preview, every draft with grade, fact and rule results (~5% carry planted test errors that never send). BDR approves, edits, swaps a person or holds, by 17:00 Day 2"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting, row \"Gate 2 (human: pod BDR)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A45
    text: "Copy rules the Message Writer enforces: subject 3–6 words built on the prospect's trigger; emails 90–120 words; connection notes <250 characters; open on the business problem, not AI; one insight + one question; guesses only as questions; no em dashes, placeholders or invented statistics; goodbye notes say we won't reach out for a while."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A46
    text: "Baseline sequence (Tier 2 starts 2 days after Tier 1, Tier 3 two days after that; Tier 1 gets email, LinkedIn, call; Tier 2 email, LinkedIn; Tier 3 email only):"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 5. Outreach drafting · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A47
    text: "Puts each approved person into channels: email steps into an Apollo sequence on the assigned inbox, LinkedIn steps into the sender's Sprouts queue, calls as Apollo call tasks. Schedules in the prospect's local morning and state window, keeping tier spacing. Holds every inbox and LinkedIn sender at 70% of daily limit. Writes owner, Patch ID, BDR of record, sequence status, tasks, notes to HubSpot; sets the parent outreach lock. Every write keyed on person + play (no double enrolment)"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach, row \"Outreach Launcher (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A48
    text: "For each call task (Tier 1 day 6, Hot Visit, anyone engaged): adapts the BDR's best script or builds one from top Gong calls; writes signal-tied opener, permission question, 3–5 discovery questions, top 3 objection answers, 20-second voicemail, follow-up email draft. Orders each BDR's call list by interest inside each patch's time-zone block. <70 → BDR approves the script"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach, row \"Call Script Writer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A49
    text: "Keeps the account one conversation once anyone responds: a referral becomes the lead thread; a Tier 1 objection pauses Tiers 2–3 and gives the AE an answer note; 2+ people engaging in 7 days switches to Committee Surge. Every rewrite goes back through Fact Checker and Message Grader. <70 → BDR decides"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach, row \"Follow-up Planner\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A50
    text: "Weekly inbox-placement tests per active domain (Gmail, Outlook, Microsoft, Barracuda, Proofpoint); daily blacklist and Gmail reputation checks; reply rate by recipient provider; maintains the email-security-scanner list. Every alert to the BDR and GTM engineer"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach, row \"Inbox Health Checker\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A51
    text: "Rests a domain the same day if placement <70% in two tests or it hits a major blacklist, and swaps in a warmed spare. Blocks a new BDR's first send until their domains pass. Previously blacklisted domains are retired"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach, row \"Email Domain Swapper (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A52
    text: "LinkedIn bans third-party automation, so people send. Each opens their Sprouts queue (messages pre-written and checked), reviews and sends from their own account. AE ~20 requests/day for own patch. A restriction warning → stop and report; tower pauses that sender. Unsent AE messages move to the BDR at day end"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach, row \"LinkedIn senders (human: AEs, BDR, exec sponsor)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A53
    text: "Sending limits: each BDR sends on 16 inboxes across 4 UnifyApps-branded secondary domains, ≤40 emails per inbox per day, with 2 warm spare domains (8 inboxes). SPF, DKIM, DMARC and one-click unsubscribe on every domain. New inboxes ramp 10/20/30/40 per day over 4 weeks. LinkedIn: ≤22 connection requests per person per day across all pods. One stop signal: a reply in Apollo or Sprouts stops every channel for that person in both tools within minutes."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 6. Outreach · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A54
    text: "Watches every pod inbox (Apollo) and LinkedIn reply (Sprouts); classifies into 9 types: positive, referral, not now (with date), objection, wrong person, out of office, unsubscribe, bounce, auto-reply. Stops all channels for that person in both tools and tells the Follow-up Planner. Handles mechanical types itself: OOO moves the next touch to the return date; unsubscribe to DNC within 15 min; bounce triggers re-check + backup person; \"not now\" to Content Handoff. <90 on unsubscribe → treated as unsubscribe; <80 on anything else → a person sorts it"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"Reply Sorter (checker)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A55
    text: "Drafts the answer from the thread, account view, objection list and the AE's booking link; puts it with confidence in the BDR's to-do list (and the AE's for positive replies at best-fit accounts). The person sends, edits, adds a booking link, hands to the AE, or snoozes, from one screen; it goes out from the original thread. Reminder at 90 min; Geo leader alerted at 2 business hours. <70 marked for full rewrite"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"Reply Writer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A56
    text: "On booking via the AE's link: creates the deal at Engage owned by the patch AE; picks up meetings booked elsewhere from the AE's Google Calendar within 15 min. Locks Patch ID, BDR of record, meeting source, factory-sourced, factory-influenced (a rejected meeting rebooked within 30 days keeps its source). Books the SC, triggers the prep pack, sends agenda and 24h/1h reminders, runs a 2-touch reschedule on no-show. Runs AE deadlines (below) and escalations"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"Meeting Handoff and Deadlines (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A57
    text: "Builds the pack for AE and SC: account view, buying team, thread, Case for Change draft, likely objections, AotP page, questions to confirm economic buyer and timeline. Delivered into the AE's AI Twin, which then tracks promises made on the call"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"Meeting Prep Writer\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A58
    text: "Reads transcript, attendees, economic-buyer flag; labels intro / New Buyer Meeting / doesn't count, quoting evidence. Doesn't count if <20 min, no Tier 1–2 attendee, a reschedule, or a second intro at the account within 90 days. Unrecorded meetings labelled from calendar attendees and AE notes and marked unrecorded. <80 → Geo leader checks"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"Meeting Labeler (checker)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A59
    text: "After each New Buyer Meeting checks six requirements: fit 36+, a VEP-CFC pain, engaged champion, New Buyer Meeting held, timeline ≤12 months, scheduled mutual next step. Marks each met / partly / missing with transcript quotes; lists gaps with the question that closes each; drafts the recap; recommends Qualified only when all are met. Saves won/lost outcomes and reasons to the graph. <80 → recommended not qualified, with gaps"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"Deal Qualifier (checker)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A60
    text: "AE confirms meeting label and stage within 2 business days; deal moves to Commit"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit, row \"AE confirm (human)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A61
    text: "Deadlines the workflow enforces (AE's business hours; reminder at half-window, escalation on miss): accept or reject a meeting within 1 business day (else Geo leader in 4h or backup AE takes it) · decide within 2 business days of every held meeting · stale after 5 idle business days at Engage · alert at 30 days in Connect, 45 days in Commit without a next step · one stage at a time, only with exit fields filled."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 7. Engage, Connect and Commit · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A62
    text: "Weekly: promotes messages with 3+ positive replies into the Message Writer's examples for that role and industry; shares them with the Content Factory. <3 positives → not promoted"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Winning Message Finder\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A63
    text: "Learns from every outcome, grades every agent, and turns red lines into actions. Learning agents only propose; the Quality Grader checks each proposal and the Friday review approves. Only weight changes within ±20% apply on their own, after 8 weeks without a drop."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A64
    text: "Every touch is saved with its result: patch, signal, play, persona, tier, use case, pattern, outcome, subject, asset, sender, send time → reply type, meeting label, qualified, won/lost, deal size."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A65
    text: "Monthly: re-fits fit and signal weights to meetings and qualified opportunities, learning from Gate 1 rejections, AE-rejected meetings, disqualifications, win/loss reasons. Learns across all patches, reports per patch. Proposals only"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Scoring Tuner\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A66
    text: "Updates the objection list and buyer language from call transcripts. <70 → sales reviews"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Objection Collector\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A67
    text: "Small changes (subject, opener, asset): continuous tests on positive replies, ≥20% traffic per version, 4-week limit. Bold changes: fixed-size tests on people (5%→8% reply needs ~1,060 people per version). Never tests one-point lifts"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"A/B Tester\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A68
    text: "Holds every agent's rubric and test set; runs them on every prompt, model or weight change and blocks a release on any drop. Enforces checker-on-other-model. Computes each gate's rung weekly per pod and AE. Drafts a policy when the same exception is resolved the same way 3 times"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Quality Grader (checker)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A69
    text: "Weekly: compares each agent to its baseline on block/edit rate, factual errors, grades, confidence calibration; alerts the GTM engineer on any slip"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Agent Monitor\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A70
    text: "Plants errors (e.g. wrong patch AE, sender from wrong pod) in ~5% of Gate 2 items, which never send; scores each reviewer's catch rate"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Test Error Planter\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A71
    text: "Every 15 min reads tower metrics; on a red line takes the listed action (pause, throttle, move slots, demote a gate, add a to-do item); escalates unfixed alarms patch → pod (2 business days) → Geo (5) → CRO. Logs before/after numbers. Safety actions are automatic; resuming or moving anyone's work needs a person"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Alarm and Escalation (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A72
    text: "Monday: pushes accounts in play to LinkedIn ad audiences by patch geography for 8 weeks; passes unreached people to the Content Factory (ads and content only, never cold email); moves \"not now\" and engaged prospects to nurture until their date; sets marketing_influenced; sends asset, message and pattern results by patch weekly"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Content Handoff (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A73
    text: "Recording consent per state; DNC checks; state legal checklists (send window, consent, footer); erasure across every tool within 30 days; 12-month clean-up of people who never engaged"
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance, row \"Privacy and Consent (workflow)\", column \"What it does\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A74
    text: "Every agent goes through these ten steps on the Solution Builder; deterministic workflows skip steps 5–8 and instead need a fixed test set that passes in full."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How to build each agent on UnifyApps · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A75
    text: "Every fact in the graph carries source, date, evidence tag ([PUBLIC] or [HYPOTHESIS]), the writing agent and its confidence. Views (account cards, committee maps, patch views) are live queries over the graph, not stored documents."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § How to build each agent on UnifyApps · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A76
    text: "Create these HubSpot fields first (workflow-written only): patch_id, pod, owner_ae, backup_ae, ultimate_parent_lock, factory_holdout, factory_holdout_until, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced, value_pattern."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § Tools to connect · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A77
    text: "Do not connect: LinkedIn scrapers or any LinkedIn tool other than the Sprouts plugin (LinkedIn bans third-party automation); mirror profiles; a third outreach tool or second dialler (it would split reply detection and the DNC list)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § Tools to connect · doc dated 2026-10-28, shared 2026-10-30"
    priority: P0
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A78
    text: "Everything they must act on lands in their to-do list in brain.unifyapps.com, prepared by their AI Twin."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Summary · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A79
    text: "Built fast. One pilot patch goes live end to end first, then the other patches, each visible in the brain portal as it lands."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Summary · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A80
    text: "Every control tower acts both ways: it rolls numbers up and pushes actions down into owners' to-do lists. An alarm not fixed at one level rises to the next."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A81
    text: "Every level uses one metric dictionary, so each level is the exact sum of the one below. Comparisons are normalised by named accounts, signal volume and deal size, and nothing is ranked on raw counts."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A82
    text: "The concentric view. Patch accounts, then those in a play in the last 90 days, then replied, Engage, Connect, Commit, Validate and Select, and Contract. The BDR works the outer rings, and the Content Factory reaches the people a play hasn't."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Control towers, two views every patch gets · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A83
    text: "The patch map. A graph from the AE to every named account, with aberrations highlighted, such as a New York AE holding California accounts."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Control towers, two views every patch gets · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A84
    text: "Seller, My 4P: their own output and scorecard. The factory's replies, approvals, LinkedIn tasks and deadlines appear in My 4P's My follow-up, and in the seller's to-do list in brain.unifyapps.com."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Control towers, role views · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A85
    text: "The CRO control tower shows every Geo on one screen. Every number drills down through Geo, pod and patch to the AE and account behind it."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A86
    text: "Pulse: bookings and Qualified Pipeline against target, coverage, holdout lift, cost per qualified opportunity, and data freshness, all shown as pace."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A87
    text: "Leak map: one row per Geo, one column per VEP stage. Each cell is green, amber or red against that Geo's own target, and a click opens its pods and patches."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A88
    text: "Top leaks: the five gaps with the most bookings at risk. Each shows where it is, the cause the diagnosis found, the action already taken, the owner, and when they report back."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A89
    text: "Decisions waiting: only the calls nobody below can make, each with a recommendation and evidence:"
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A90
    text: "Pace, not raw counts. Every panel shows its last read, and greys out after an hour."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers, rules that keep it true · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A91
    text: "When a patch turns red, Alarm and Escalation checks five stages in order and stops at the first one below its line. So one cause gets one action."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Control towers, diagnosis · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A92
    text: "People move from approving every item to governing exceptions, one gate at a time, and only when the numbers earn it. Two things decide what a person sees:"
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Governance: autonomy ladder and policy register · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A93
    text: "Every exception lands in its governor's to-do list with context, the agent's confidence score and a recommended resolution."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Governance, from exception to policy · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A94
    text: "When the same exception is resolved the same way three times, the Quality Grader drafts a policy."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Governance, from exception to policy · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A95
    text: "Slack carries alerts only for people who choose it; the to-do list is the source of truth."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Tool stack and connectors · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A96
    text: "Never played: customers, open deals, partners and competitors."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Coverage, re-entry rules · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "this"
    status: open
  - id: A97
    text: "Reused, not built: Patch Mapper (Atomic Patch View) stamps patch_id on every account, person and dollar nightly, flags orphans, never moves an account. Gate 1 refuses any account without a Patch ID."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 1. Patch accounts · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Atomic Patch View"
    status: out_of_scope
  - id: A98
    text: "Reused from the Atomic Patch View: Pipeline Analyst (pipeline signals), Patch Brief Agent (patch briefs, draft only), My 4P Coach (seller next steps, incl. factory replies, approvals and tasks)."
    source: "Pipeline-Factory-Engineering-Build.docx (Slack file F0CCGFK0UNB, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363781619109) § The agents, 8. Learning and governance · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Atomic Patch View"
    status: out_of_scope
  - id: A99
    text: "Message hierarchy: the best message for each category, sub-sector, company type and persona, each graded on its rubric"
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § The Content Factory, and the Halo, table \"What the Content Factory gives the Pipeline Factory\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Content Factory"
    status: out_of_scope
  - id: A100
    text: "Programs for people the factory hasn't reached, and nurture for \"not now\""
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § The Content Factory, and the Halo, table \"What the Content Factory gives the Pipeline Factory\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Content Factory"
    status: out_of_scope
  - id: A101
    text: "Company-level calls go to the CEO through Mission Control."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Geo and CRO control towers · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Mission Control"
    status: out_of_scope
  - id: A102
    text: "The Pipeline Factory (this blueprint) and the Content Factory at category and patch level. A Demo Factory comes later"
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Revenue Brain, row \"Factories\" · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Demo Factory"
    status: out_of_scope
  - id: A103
    text: "Customers are covered by the Value Expansion workflow instead."
    source: "UnifyApps Pipeline Factory Final Blueprint .docx (Slack file F0CDS8QGMUG, posted in #pipeline-factory by Gourav Mahunta, https://slack.com/archives/C0CDGQKAFTQ/p1793363792135149) § Coverage, re-entry rules · doc dated 2026-10-28, shared 2026-10-30"
    priority: P1
    owner: "Gourav Mahunta"
    use_case: "other: Value Expansion workflow"
    status: out_of_scope

coverage:
  - ask: A1
    by: beat 7
  - ask: A2
    by: beat 7
  - ask: A3
    by: beat 7
  - ask: A4
    by: beat 2
  - ask: A5
    by: beat 5
  - ask: A6
    by: beat 7
  - ask: A7
    by: beat 7
  - ask: A8
    by: beat 3
  - ask: A9
    by: open question 10
  - ask: A10
    by: beat 5
  - ask: A11
    by: control Register tab, stage 1 facet on Runs and register
  - ask: A12
    by: beat 3
  - ask: A13
    by: beat 3
  - ask: A14
    by: control Register tab, stage 1 facet on Runs and register
  - ask: A15
    by: control Register tab, stage 1 facet on Runs and register
  - ask: A16
    by: beat 3
  - ask: A17
    by: beat 3
  - ask: A18
    by: beat 3
  - ask: A19
    by: beat 3
  - ask: A20
    by: control Register tab, stage 1 facet on Runs and register
  - ask: A21
    by: beat 2
  - ask: A22
    by: beat 2
  - ask: A23
    by: beat 2
  - ask: A24
    by: beat 2
  - ask: A25
    by: beat 2
  - ask: A26
    by: beat 2
  - ask: A27
    by: beat 3
  - ask: A28
    by: beat 3
  - ask: A29
    by: beat 3
  - ask: A30
    by: beat 3
  - ask: A31
    by: beat 3
  - ask: A32
    by: beat 3
  - ask: A33
    by: control Intro paths tab on Account
  - ask: A34
    by: open question 8
  - ask: A35
    by: beat 4
  - ask: A36
    by: control AE checkpoint tab on Account
  - ask: A37
    by: beat 4
  - ask: A38
    by: control Page preview link on the Gate 2 review drawer (To-do)
  - ask: A39
    by: beat 4
  - ask: A40
    by: beat 4
  - ask: A41
    by: beat 4
  - ask: A42
    by: beat 4
  - ask: A43
    by: beat 4
  - ask: A44
    by: beat 4
  - ask: A45
    by: beat 4
  - ask: A46
    by: control Sequence tab on Account
  - ask: A47
    by: open question 8
  - ask: A48
    by: open question 8
  - ask: A49
    by: beat 5
  - ask: A50
    by: open question 8
  - ask: A51
    by: open question 8
  - ask: A52
    by: open question 8
  - ask: A53
    by: open question 8
  - ask: A54
    by: beat 5
  - ask: A55
    by: beat 5
  - ask: A56
    by: beat 5
  - ask: A57
    by: control Prep pack tab on Account
  - ask: A58
    by: control Register tab, stage 7 facet on Runs and register
  - ask: A59
    by: control Register tab, stage 7 facet on Runs and register
  - ask: A60
    by: control Register tab, stage 7 facet on Runs and register
  - ask: A61
    by: beat 5
  - ask: A62
    by: control Register tab, stage 8 facet on Runs and register
  - ask: A63
    by: beat 7
  - ask: A64
    by: beat 7
  - ask: A65
    by: control Register tab, stage 8 facet on Runs and register
  - ask: A66
    by: control Register tab, stage 8 facet on Runs and register
  - ask: A67
    by: control Register tab, stage 8 facet on Runs and register
  - ask: A68
    by: beat 7
  - ask: A69
    by: beat 7
  - ask: A70
    by: beat 4
  - ask: A71
    by: beat 6
  - ask: A72
    by: open question 8
  - ask: A73
    by: control Register tab, stage 8 facet on Runs and register
  - ask: A74
    by: beat 7
  - ask: A75
    by: beat 3
  - ask: A76
    by: open question 8
  - ask: A77
    by: control Register tab, demo mode facet (mocked) on Runs and register
  - ask: A78
    by: beat 2
  - ask: A79
    by: beat 1
  - ask: A80
    by: beat 1
  - ask: A81
    by: beat 6
  - ask: A82
    by: beat 1
  - ask: A83
    by: beat 1
  - ask: A84
    by: open question 9
  - ask: A85
    by: beat 6
  - ask: A86
    by: beat 1
  - ask: A87
    by: beat 6
  - ask: A88
    by: beat 6
  - ask: A89
    by: beat 6
  - ask: A90
    by: beat 1
  - ask: A91
    by: beat 1
  - ask: A92
    by: beat 7
  - ask: A93
    by: beat 6
  - ask: A94
    by: beat 7
  - ask: A95
    by: beat 6
  - ask: A96
    by: beat 2

size:
  pages: 5
  objects: 9
  automations: 7
  agents: 1

data:
  source: "assumed, shaped like the factory graph and HubSpot fields (the two shared documents); the hand-off register transcribed from the documents' agent tables (asks A11 to A73)"
  masked: "none: fictional (invented names, accounts and figures; no email, phone or real identifier in any row)"
  rows:
    - "Patch: 10, record · seed from studio/data/seed/pf_patch.csv"
    - "Account: 20, record · seed from studio/data/seed/pf_account.csv (story row ACC-001 Northwind Freight Systems)"
    - "Buying Team Member: 18, record · seed from studio/data/seed/pf_person.csv"
    - "Outreach Draft: 8, record · seed from studio/data/seed/pf_draft.csv"
    - "To-do Item: 20, record · seed from studio/data/seed/pf_todo.csv"
    - "Deal: 6, record · seed from studio/data/seed/pf_deal.csv"
    - "Factory Component: 57, record · seed from studio/data/seed/pf_component.csv (a file under 200 rows)"
    - "Agent Run: 20, record · seed from studio/data/seed/pf_run.csv"
    - "Pipeline Factory Seed snapshot: 159, one per seed row, written by its own record · seed task"
  expected_answers: eval.csv

verify:
  round: 0

collaterals: {}

review:
  round: 0
  open: []

decisions:
  - by: orchestrator
    when: 2026-10-30
    text: "Profile studio/profiles/unifyapps.md drafted by Studio from the request with the template defaults."
  - by: orchestrator
    when: 2026-10-30
    text: "Preflight: collateral python packages missing (blocks G4's collaterals until setup runs); faster-whisper missing (G1 recording transcripts are skipped). Everything else ok: Nebula 3.63.1, Bun 1.4.4, Playwright Chromium for PDFs, Slack read tools, tenant sign-in."

  - by: orchestrator
    when: 2026-10-31
    text: "G1 approved by Gourav Mahunta (the bot's 'G1 · Research approved' post in G1's thread). The POC row could not be read in this session: the platform plugin's object tools answer only for the folder's tenant (sales.uat-us-east-1.unifyapps.com), and the row is on orbit.uat. Gate status taken from the bot's approval post in G1's thread."
  - by: orchestrator
    when: 2026-10-31
    text: "Solution 'UnifyApps · Pipeline Factory' created on sales.uat-us-east-1.unifyapps.com (e_6ae5b8b80293635d6923e81e) and bound to the use-case folder; the use case moved off orbit.uat on 2026-10-30."
  - by: research
    when: 2026-10-31
    text: "Site https://www.unifyapps.com (the profile's site; confirmed by reading it). Brand colour source: the site's own stylesheets (_next/static/css, 8 files read 2026-10-31): #847347 is the header's current-link and hover colour and the fill of the published footer logo (Unify_Logo_Footer.svg); brand-sample's automatic pick #007AFF was the Swiper library's default --swiper-theme-color, not a brand colour. Other candidates on the site: #0F2805 (deep green, text), #5C37EB (form accents)."
  - by: profile
    when: 2026-10-31
    text: "Brand colour: #847347 (hue 43) taken as the recommended colour under the standing answer 'ambiguous brand colour: the recommended one, listed in the G2 pack'; candidates #0F2805 and #5C37EB listed in the plan doc. Logo: the site's published footer logo (Unify_Logo_Footer.svg) used as published."
  - by: profile
    when: 2026-10-31
    text: "The Factory Analyst's model is UnifyApps Headless's recommendation (standing answer 'model: Nebula's recommendation')."
  - by: plan
    when: 2026-10-31
    text: "Modes: the Send Rules Check, Gate 1 decisions, the booking and the escalation are live automations with rule logic and no model call; the agent outputs of the factory (fit scores, Case for Change, drafts, grades, reply sorting, diagnosis) are seeded with the AI marker; Apollo, Sprouts, Google Calendar, Gong, LinkedIn Ads and HubSpot writes are mocked as register and run rows, because the tenant has no connection for them (HubSpot only as 'UnifyApps Prod (Read Only)', a production system, so not used). External step: an optional Slack alert on Escalate on the existing 'Slack Connection' (DeliveryBrain bot), probed read-only on 2026-10-31."

dev_issues: []

frozen: {}

cost:
  runs: 2
  agent_spawns: 2
  tokens_m: 0.51
  wall_h: 0.7

open_questions:
  - by: harvest
    for: lead
    text: "Who presents this demo, and to whom (audience, roles, slot)? Options: Recommended: the CEO and CRO staff, at the next CEO / CRO staff review (the blueprint is written for the CEO's direction and the Atomic Patch View's CRO staff review; the architecture diagram is due 'the next CEO review') | Profile default: a senior operations leader, 20 minutes, in person, on a projector, presented by the person who asked"
  - by: harvest
    for: lead
    text: "When is the demo, or the next date with the audience? Options: Recommended: before the blueprint's Week 2 architecture review (task A3, 'the next CEO review'); please give the date | Profile default: none set; the plan assumes no fixed date"
  - by: harvest
    for: lead
    text: "The two documents were posted with no message saying what to build from them. Are all 38 agents, 12 workflows and the human gates asks for this demo, or is the demo a slice? Options: Recommended: keep every component as an ask; G2 picks the beats (for example one pilot patch walked from Gate 1 to Gate 2, the patch and CRO control towers, the to-do list) and lists what is shown as narrated | Alternative: name the sub-workflows the demo must show, and defer the rest"
  - by: harvest
    for: lead
    text: "The blueprint lists 'Decisions to confirm' (pilot patch, factory share, whether a factory-held meeting counts as a New Buyer Meeting, escalation windows, BDR pay, etc.). Should the demo run on the blueprint's stated defaults? Options: Recommended: yes, the blueprint's defaults (factory share 50%, five US patches, alarms rise after 2 and 5 business days, a factory meeting is an intro meeting unless the economic buyer attends) | Alternative: the lead gives the values to use"
  - by: harvest
    for: lead
    text: "The documents name real employees (RevOps, the registry owner, the blueprint and spec authors). Should demo screens and seed data use roles or fictional names? Options: Recommended: roles and fictional names only; no real employee names in seed data | Alternative: real first names for the internal audience"
  - by: harvest
    for: lead
    text: "The blueprint cites sources that were not shared: the October 27 strategic team sync transcript, the Atomic Patch View V2, the BDR Questionnaire, the AI Native Transformation Manifesto and the earlier Lead Engine blueprints. Will any be shared before G2? Options: Recommended: share the Atomic Patch View V2 and the October 27 sync transcript in the channel (they set the control tower and vocabulary the demo should match); the next harvest reads them | Alternative: go on from the two documents only"
  - by: plan
    for: owner
    text: "G2 asks the owner to set the intent. Options: Recommended: both (the outcome first, then one hood beat: the hand-off register, the Decide Gate 1 automation and the Factory Analyst in the builder, after the CRO tower) | use-case (drop beat 7; 15 to 20 seed rows stay) | platform (2 to 4 hood beats, a one-line description on every node and field)"
  - by: plan
    for: owner
    text: "Nine asks need a system the tenant has no connection for: Apollo (A47, A53), Sprouts (A34, A52), Gong (A48), inbox placement and blacklist tools (A50, A51), LinkedIn Ads (A72) and a writable HubSpot (A76; the tenant holds only 'UnifyApps Prod (Read Only)', a production system). Options: Recommended: show them as mocked rows in the hand-off register and the run trace (marked mocked), with the Do-Not-Contact and send rules live inside the demo | Alternative: name sandbox accounts for these tools and give their credentials at G3, and the plan adds one external step per tool"
  - by: plan
    for: owner
    text: "A84 (and A78) say the to-do list lives in brain.unifyapps.com and in My 4P's My follow-up (the Atomic Patch View). Options: Recommended: the demo's own To-do screen stands in for the brain to-do list, and the presenter says it lands in brain.unifyapps.com | Alternative: give access to the brain portal or My 4P so a beat can open it"
  - by: plan
    for: owner
    text: "A9 asks every checker to run on a different model family from the drafter it checks. Options: Recommended: show it in the register (model family per component, Family A drafters, Family B checkers) and in each run's model, with the one live agent on the recommended model | Alternative: add a live Message Grader agent on a second model family that grades a draft at Gate 2 (one more AI agent and one more automation)"
  - by: plan
    for: owner
    text: "The bonus external step posts a DEMO-TEST alert to Slack when the presenter escalates the Mountain patch, on the existing 'Slack Connection' (DeliveryBrain bot). Which channel? Options: Recommended: a private test channel the owner names, with the DeliveryBrain bot invited | Alternative: #pipeline-factory | Alternative: no Slack step (the escalation still writes its to-do)"
  - by: plan
    for: owner
    text: "Two views the design kit has no part for: the concentric view (A82) and the patch map graph from the AE to every account (A83). Options: Recommended: the concentric view as the kit's stage strip (.stages) with the ring counts, and the patch map as a table grouped by AE with aberrations tagged | Alternative: build both as custom charts from the kit's tokens (more build time, a new part outside the kit)"
---

## build_contract

### Requested outcome
A senior revenue leader watches one pilot patch (Mountain, PT-USW-03) run through the Pipeline Factory: the patch control tower, the BDR's Gate 1 batch, the account view and buying team, Gate 2 with the Send Rules Check refusing a draft, a positive reply booked into a locked deal, and the CRO control tower where the Factory Analyst explains a red cell. A last screen shows the hand-off register and every run's trace. Every action on the demo path runs a real automation that writes; the one AI agent answers live over the seeded rows.

### Touches
- object · Patch · new
- object · Account · new
- object · Buying Team Member · new
- object · Outreach Draft · new
- object · To-do Item · new
- object · Deal · new
- object · Factory Component · new
- object · Agent Run · new
- object · Pipeline Factory Seed snapshot · new
- automation · Pipeline Factory · Decide Gate 1 · new
- automation · Pipeline Factory · Approve Gate 2 draft · new
- automation · Pipeline Factory · Send reply and book meeting · new
- automation · Pipeline Factory · Escalate alarm · new
- automation · Pipeline Factory · Factory lookup · new
- automation · Pipeline Factory · Ask Factory Analyst · new
- automation · Pipeline Factory · Reset demo · new
- ai-agent · Factory Analyst · new
- code-app · UnifyApps Pipeline Factory · new
- connection · Slack Connection · 6abbc5c530617960ef072df6


### Contract
#### object · Patch
One sales patch with its pace, VEP-stage counts and targets, read by both control towers.

#### object · Account
A named account in a patch: fit, timing, signals, Gate 1 status, Case for Change and locked flags.

#### object · Buying Team Member
A person in an account's buying team, with tier, role, notes and the Do-Not-Contact flag.

#### object · Outreach Draft
One drafted email or LinkedIn message with its grade, fact check and send rules result.

#### object · To-do Item
Everything a person must act on: Gate 2 reviews, replies, leaks, decisions, exceptions, deadlines, alarms.

#### object · Deal
A booked meeting's deal at Engage with its locked fields, keyed on account, person and play.

#### object · Factory Component
The hand-off register: one row per agent, checker, workflow and human gate of the factory.

#### object · Agent Run
The trace of one component run: input, output, model, confidence, cost, latency, status and cause.

#### object · Pipeline Factory Seed snapshot
The seeded rows as written, read by Reset demo to put them back.

#### automation · Pipeline Factory · Decide Gate 1
Accepts or rejects a Gate 1 account, enforcing the hard blocks and refilling a rejected slot.

#### automation · Pipeline Factory · Approve Gate 2 draft
Runs the Send Rules Check on a draft and approves, blocks or holds it.

#### automation · Pipeline Factory · Send reply and book meeting
Books a positive reply into a Deal at Engage with locked fields, idempotently.

#### automation · Pipeline Factory · Escalate alarm
Raises an alarm or leak one level and optionally alerts Slack.

#### automation · Pipeline Factory · Factory lookup
Read-only tool the Factory Analyst uses to read factory rows.

#### automation · Pipeline Factory · Ask Factory Analyst
Lets the app ask the Factory Analyst a question and returns its answer.

#### automation · Pipeline Factory · Reset demo
Clears test rows and restores seed rows from the snapshot.

#### ai-agent · Factory Analyst
Read-only assistant that explains towers, leaks and decisions from the factory rows.

#### code-app · UnifyApps Pipeline Factory
The demo app: patch tower, to-do, account, CRO tower, runs and register.

#### connection · Slack Connection
Existing Slack connection (DeliveryBrain bot) for the optional alarm alert.

- object · create · Patch (`OBJ_pf_patch`): patch_id text primaryKey required; name text required; geo picklist us_west "US West", us_east "US East", us_central "US Central", emea "EMEA"; pod text; ae_name text; ae_location text; bdr_name text; is_pilot boolean; accounts_named number; in_play_90d number; replied number; engage, engage_target, connect, connect_target, commit, commit_target, validate_select, validate_select_target, contract, contract_target numbers; intro_target_to_date number; intro_booked_to_date number; pace_pct number; status picklist green "Green", amber "Amber", red "Red"; diagnosis_stage picklist none "None", input "Input", engagement "Engagement", conversion "Conversion", qualification "Qualification"; slots_base number; slots_left number; bookings_usd, bookings_target_usd, qualified_pipeline_usd, qualified_pipeline_target_usd, cost_per_qo_usd, holdout_lift_pct numbers; last_read date (epoch ms); origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Account (`OBJ_pf_account`): account_id text primaryKey required; name text required; parent_name text; patch_id text; pod text; ae_name text; ae_location text; bdr_name text; hq text; hq_confidence number; fit_score number (of 60); fit_band picklist best "Best fit", medium "Medium fit", low "Low fit"; icp_quadrant text; timing_score number (of 40); signal_1, signal_2, signal_3 text; last_touch date (epoch ms); gate1_status picklist queued "Queued", accepted "Accepted", rejected "Rejected", blocked "Blocked", held_out "Held out", not_in_batch "Not in batch"; gate1_reason picklist bad_fit "Bad fit", active_deal "Active deal", wrong_timing "Wrong timing", in_conversation "Already in conversation"; block_reason text; holdout_until date (epoch ms); rank_in_patch number; vep_stage picklist patch "Patch", in_play "In play", replied "Replied", engage "Engage", connect "Connect", commit "Commit", validate_select "Validate and Select", contract "Contract"; current_vendors text; renewal_estimate date (epoch ms); value_pattern text; outreach_lock_owner text; case_for_change long text; use_cases long text; patch_map_aberration text; factory_sourced, factory_influenced, marketing_influenced booleans; writer_component text; confidence number; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Buying Team Member (`OBJ_pf_person`): person_id text primaryKey required; account_id text required; name text required; title text; role picklist economic_buyer "Economic buyer", champion "Champion", technical_evaluator "Technical evaluator", business_owner "Business owner", gatekeeper "Gatekeeper"; tier picklist t1 "Tier 1", t2 "Tier 2", t3 "Tier 3", backup "Backup", mapped "Mapped only"; dnc boolean; dnc_reason text; notes long text; email_verified_at date (epoch ms); consent text; confidence number; writer_component text; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Outreach Draft (`OBJ_pf_draft`): draft_id text primaryKey required; account_id text required; person_id text required; tier picklist as Buying Team Member tier; channel picklist email "Email", linkedin "LinkedIn", call "Call"; subject text; body long text; word_count number; grade number; rewrite_count number; fact_check picklist pass "Traced", blocked "Blocked"; facts_traced text; rules_result picklist pending "Not run", pass "Pass", blocked "Blocked"; rules_reason text; status picklist pending_review "Waiting for Gate 2", approved "Approved", blocked "Blocked", held "Held", edited "Edited"; sender text; sender_pod text; asset text; play text; play_id text; send_day number; is_planted_error boolean; writer_family text; grader_family text; confidence number; patch_id text; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · To-do Item (`OBJ_pf_todo`): todo_id text primaryKey required; kind picklist gate2_review "Gate 2 review", reply "Reply", leak "Leak", decision "Decision waiting", exception "Exception", deadline "Deadline", alarm "Alarm"; title text required; owner_name text; owner_role text; account_id text; patch_id text; geo picklist as Patch geo; vep_stage picklist as Account vep_stage; confidence number; recommendation text; evidence text; cause text; action_taken text; bookings_at_risk_usd number; report_back date (epoch ms); due date (epoch ms); status picklist open "Open", done "Done", snoozed "Snoozed", escalated "Escalated"; reply_type picklist positive "Positive", referral "Referral", not_now "Not now", objection "Objection", wrong_person "Wrong person", ooo "Out of office", unsubscribe "Unsubscribe", bounce "Bounce", auto_reply "Auto-reply"; reply_from text; reply_text long text; drafted_answer long text; escalation_level picklist patch "Patch", pod "Pod", geo "Geo", cro "CRO"; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Deal (`OBJ_pf_deal`): deal_id text primaryKey required; account_id text required; person_id text; play_id text; booking_key text unique index (account_id, person_id and play_id joined by `|`); stage picklist as Account vep_stage; owner_ae text; patch_id text; bdr_of_record text; meeting_type picklist pending "Pending label", intro "Intro", new_buyer_meeting "New Buyer Meeting", does_not_count "Doesn't count"; meeting_source picklist factory_booked "Factory booked", calendar_pickup "Calendar pickup", ae_sourced "AE sourced"; factory_sourced, factory_influenced, marketing_influenced booleans; meeting_at date (epoch ms); locked_at date (epoch ms); ae_accept_due date (epoch ms); sc_booked boolean; next_step text; correction_reason text; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Factory Component (`OBJ_pf_component`): component_id text primaryKey required; stage number (1 to 8); name text required; kind picklist agent "Agent", checker "Checker", workflow "Workflow", monitor "Monitor", rule "Rule step", human_gate "Human gate"; ask_id text; when_runs text; threshold text; below_threshold_to text; writes_fields text; model_family picklist family_a "Family A", family_b "Family B", none "None"; checks text; rung picklist approve_every_item "Approve every item", sample "Sample", exceptions_only "Exceptions only"; demo_mode picklist live "Live", seeded "Seeded", mocked "Mocked"; success_rate_7d number; success_target number; status picklist as Patch status; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Agent Run (`OBJ_pf_run`): run_id text primaryKey required; patch_id text; component_name text required; account_id text; input_summary text; output_summary text; model text; model_family text; confidence number; cost_usd number; latency_ms number; status picklist ok "OK", late_retried "Late, retried", below_threshold "Below threshold", schema_rejected "Rejected on save", blocked "Blocked", failed "Failed"; cause text; ran_at date (epoch ms); idempotency_key text; origin picklist user "User" (default), seed "Seed", test "Test"
- object · create · Pipeline Factory Seed snapshot (`OBJ_pf_seed_snapshot`): snapshot_id text primaryKey required; object_id text required; record_key text required; values_json long text required; taken_at date (epoch ms); origin picklist user "User" (default), seed "Seed", test "Test"
- record · seed · Patch: every row of `studio/data/seed/pf_patch.csv` (PT-USW-01 to PT-EMA-02; the pilot PT-USW-03 Mountain at intro pace 62%, status red, diagnosis input, 3 slots left), origin seed
- record · seed · Account: every row of `studio/data/seed/pf_account.csv` (ACC-001 to ACC-020; the story row ACC-001 Northwind Freight Systems, fit 48 best, timing 31, rank 1, gate1 queued), origin seed
- record · seed · Buying Team Member: every row of `studio/data/seed/pf_person.csv` (PER-001 to PER-018; PER-006 Tom Brennan dnc true), origin seed
- record · seed · Outreach Draft: every row of `studio/data/seed/pf_draft.csv` (DR-001 to DR-008; DR-006 is_planted_error true), origin seed
- record · seed · To-do Item: every row of `studio/data/seed/pf_todo.csv` (TD-G2-01, TD-REP-01 to 03, TD-LEAK-01 to 05, TD-DEC-01 to 03, TD-EXC-01 to 04, TD-DL-01 to 02, TD-ALM-01 to 02), origin seed
- record · seed · Deal: every row of `studio/data/seed/pf_deal.csv` (DL-001 to DL-006), origin seed
- record · seed · Factory Component: every row of `studio/data/seed/pf_component.csv` (CMP-001 to CMP-057, the hand-off register), origin seed
- record · seed · Agent Run: every row of `studio/data/seed/pf_run.csv` (RUN-001 to RUN-020), origin seed
- record · seed · Pipeline Factory Seed snapshot: one row per seed row of the eight objects above (object_id, record_key = its primary key, values_json = the row as seeded)
- automation · create · Pipeline Factory · Decide Gate 1: callable; input account_id text, decision text (accept or reject), reason text (bad_fit, active_deal, wrong_timing, in_conversation; required on reject), bdr_name text; reads the Account; refuses with result `refused` and the block_reason when gate1_status is blocked or held_out, or when patch_id, ae_name or pod is empty; accept sets gate1_status accepted and vep_stage in_play; reject sets gate1_status rejected with gate1_reason, then refills the slot with the lowest rank_in_patch account of the same patch whose gate1_status is not_in_batch and has no block_reason (set to queued); writes one Agent Run row (component_name "Gate 1", idempotency_key account_id + "|-|gate1", origin user); output result text (accepted, rejected, refused), message text, refill_account_id text, refill_account_name text, slots_left number
- automation · create · Pipeline Factory · Approve Gate 2 draft: callable; input draft_id text, action text (approve or hold), reviewer_name text; on hold sets status held; on approve runs the Send Rules Check with no model call: the person is not dnc; the draft's sender_pod equals the account's pod; the account has patch_id, ae_name and pod and no AE hold; an email has 90 to 120 words and a subject of 3 to 6 words; no em dash and no `{{` in subject or body; fact_check pass; grade 75 or more; every failed rule is a reason; all pass sets status approved and rules_result pass; any fail sets status blocked, rules_result blocked and rules_reason; a planted error (is_planted_error true) that fails adds the reason "planted test error caught"; writes one Agent Run row (component_name "Send Rules Check", origin user); output result text (approved, blocked, held), reasons text, planted_caught boolean
- automation · create · Pipeline Factory · Send reply and book meeting: callable; input todo_id text, meeting_at date (epoch ms), bdr_name text; refuses with result `refused` unless the To-do Item's kind is reply and reply_type is positive or referral; booking_key = account_id + "|" + reply_from + "|" + the account's open play_id; when a Deal with that booking_key exists, answers `already_booked` with that deal_id and writes nothing else; otherwise creates a Deal (stage engage, owner_ae = the patch's ae_name, patch_id, bdr_of_record = bdr_name, meeting_type pending, meeting_source factory_booked, factory_sourced true, factory_influenced true, meeting_at, locked_at now, ae_accept_due = now + 1 business day, sc_booked true, origin user), sets the To-do Item status done and the Account vep_stage engage, writes one Agent Run row (component_name "Meeting Handoff and Deadlines", idempotency_key = booking_key, origin user); output result text (booked, already_booked, refused), deal_id text, ae_accept_due date
- automation · create · Pipeline Factory · Escalate alarm: callable; input todo_id text, notify_slack boolean; the To-do Item (kind leak or alarm) rises one level patch → pod → geo → cro: status escalated, escalation_level set, and a new To-do Item for the next owner with the evidence and the before numbers (origin user); when notify_slack is true, posts one message with `slack_post_message_in_channel` on connection 6abbc5c530617960ef072df6 to the channel the Business rules name, text starting "DEMO-TEST"; a Slack failure never fails the result; output result text (escalated, refused), escalated_to text, slack text (posted, skipped, failed)
- automation · create · Pipeline Factory · Factory lookup: callable, read-only; input scope text (patches, accounts, leaks, decisions, runs, components, people, drafts), patch_id text, geo text, account_id text; reads the matching rows (at most 60) of Patch, Account, To-do Item, Agent Run, Factory Component, Buying Team Member or Outreach Draft; output rows text (JSON array, each row with its primary key), count number
- automation · create · Pipeline Factory · Ask Factory Analyst: callable; input question text; invokes the Factory Analyst agent with `ai_agents_by_unifyapps_invoke_agent`; output answer text, grounding text (the row ids the answer used), latency_ms number
- automation · create · Pipeline Factory · Reset demo: callable, mode deterministic, no model call; deletes every row whose origin is test in the nine objects; puts every seed row back to the values_json kept in Pipeline Factory Seed snapshot; never touches a user row; output deleted number, restored number
- ai-agent · create · Factory Analyst: read-only analyst over the Pipeline Factory data; model: UnifyApps Headless's recommendation; tool Pipeline Factory · Factory lookup; instructions: answer only from rows the tool returns and name the row ids used; give pace, cause, action taken, owner and report-back date when asked about a red cell; professional information only, never personal contact details; never sends, approves or changes anything; when no row holds the answer, says the data does not hold it
- code-app · create · UnifyApps Pipeline Factory: the shell: the design system stylesheet, the fonts, the rail (logo, nav: Patch tower, To-do, CRO tower, Runs and register), the header, the routes /patch, /todo, /accounts/:accountId, /cro, /runs; PRIVATE
- code-app · update · UnifyApps Pipeline Factory: screen Patch tower (/patch): crumb and patch switcher (`.toolbar` `.chipsel`, pilot PT-USW-03 first); pace tiles (`.tile` with `.delta`: intro meetings booked of target, bookings and qualified pipeline against target, cost per qualified opportunity, holdout lift; each with its last read, greyed after an hour); the concentric view as `.stages` (patch accounts, in play 90 days, replied, Engage, Connect, Commit, Validate and Select, Contract); diagnosis in an AI Insight card (`.ai:not(.msg)`, seeded: the first of five stages below its line); patch map aberrations as `.tbl` grouped by AE with `.tag.attention`; alarms as `.feed` from To-do Item kind alarm with the Escalate button calling Pipeline Factory · Escalate alarm (todo_id, notify_slack); reads Patch, Account, To-do Item
- code-app · update · UnifyApps Pipeline Factory: screen To-do (/todo) as `.tabs` Gate 1, Gate 2, Replies, Exceptions: Gate 1 is the BDR's batch as `.toolbar` + `.tbl` (fit band, timing, top 3 signals, Patch ID, AE, last touch, slots left) with Accept as `.btn-p` and Reject with one reason (`.menu`) calling Pipeline Factory · Decide Gate 1 (account_id, decision, reason, bdr_name), blocked and held-out rows as `.tag.negative` / `.tag.attention` with Accept disabled, the refilled row shown with a `.toast`; Gate 2 opens the account review as `.drawer.l`: each draft with grade (`.prog`), fact check and rules (`.tag`), sender, asset and send day, Approve `.btn-p` and Hold `.btn-s` calling Pipeline Factory · Approve Gate 2 draft (draft_id, action, reviewer_name), a block shown as `.tag.negative` + `.note` with every reason; Replies as `.tbl` of To-do Item kind reply with the reply, its type and confidence and the drafted answer in an AI Insight card (seeded), Send and book as `.btn-p` calling Pipeline Factory · Send reply and book meeting (todo_id, meeting_at, bdr_name), the booked deal's locked fields shown as `.dl`; Exceptions as `.tbl` with confidence and recommendation; reads Account, Outreach Draft, Buying Team Member, To-do Item, Deal
- code-app · update · UnifyApps Pipeline Factory: screen Account (/accounts/:accountId): account card `.g2 .pad` (fit 48 of 60 and band, ICP quadrant, timing, HQ with confidence, parent and outreach lock, renewal estimate, current vendors); Case for Change as `.g1` with each sentence's `[PUBLIC]` or `[HYPOTHESIS]` tag; top 3 use cases with UC-IDs as `.cv`; buying team as `.pc` cards by tier with `.faces`, the gatekeeper "mapped, never contacted", Tom Brennan with a Do-Not-Contact `.tag.negative`; `.tabs` Sequence (tier schedule as `.sth`), Intro paths, AE checkpoint, Prep pack, Locked fields (`.dl`); past contact as `.feed`; reads Account, Buying Team Member, Outreach Draft, Deal, Agent Run
- code-app · update · UnifyApps Pipeline Factory: screen CRO tower (/cro): pulse tiles (`.tile` `.spark` `.delta`, shown as pace); leak map as `.tbl.freeze` one row per Geo, one column per VEP stage, each cell a `.tag` green, amber or red against that Geo's own target, every Geo the exact sum of its patches, a click opening its pods and patches in a `.drawer`; top leaks as `.tbl` (where, cause, action taken, owner, report back, bookings at risk); decisions waiting as `.g2` cards with recommendation and evidence; the assistant in the agent drawer (`.agent-launch` `.agent-drawer`) with its answer in an AI Insight card with a grounding line, calling Pipeline Factory · Ask Factory Analyst (question); reads Patch, To-do Item
- code-app · update · UnifyApps Pipeline Factory: screen Runs and register (/runs) as `.tabs`: Register as `.toolbar` (search, stage and kind facets as `.chipsel`) + `.tbl` of Factory Component (stage, name, kind, when, threshold, below-threshold owner, writes, model family, checks, rung, demo mode, success rate against 99% with `.tag` red under 97%); Runs as `.toolbar` + `.tbl` of Agent Run (component, patch, input, output, model and family, confidence, cost, latency, status `.tag`, cause), newest first with pagination; reads Factory Component, Agent Run

### Business rules
- Every object row carries origin: seed on seeded rows, test on rows a check or the recording writes, user on rows a person makes in the demo.
- Locked fields (patch_id, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced) are written only by automations and are shown read-only.
- A Deal is keyed on account_id, person_id and play_id; booking twice answers already_booked.
- The Send Rules Check makes no model call and every reason it gives is a rule.
- Slack alerts are a bonus: the Escalate alarm result never depends on them; the channel is the one the owner names at G2 (default: a private test channel the DeliveryBrain bot is in).
- Test records on Slack are labelled DEMO-TEST with the demo's date.
- Rules · look: stylesheet `studio/design-system/unifyapps/client.css` (absolute path /home/user/all-demo-foders/unifyapps/pipeline-factory/studio/design-system/unifyapps/client.css), logo `studio/design-system/unifyapps/logo.svg`, theme: light, chrome: brand, surface: glass, density: comfortable, style-set: S1.
- Components come from the class inventory, never a second implementation, never a new colour value, never a Tailwind colour, radius, shadow or type utility: Tailwind only for layout the kit has no class for.

### Ready when
- The presenter can walk the seven beats on the published app with the seeded rows.
- deploy Pipeline Factory · Decide Gate 1
- deploy Pipeline Factory · Approve Gate 2 draft
- deploy Pipeline Factory · Send reply and book meeting
- deploy Pipeline Factory · Escalate alarm
- deploy Pipeline Factory · Factory lookup
- deploy Pipeline Factory · Ask Factory Analyst
- deploy Pipeline Factory · Reset demo
- publish Factory Analyst
- publish UnifyApps Pipeline Factory

### Assumptions
- Check this: intent proposed as both (the outcome, then one hood beat after the lean-forward beat).
- Check this: data is assumed and fictional, shaped like the factory graph and HubSpot fields; no real people, companies or employees.
- Check this: the blueprint's defaults (five-stage diagnosis, alarms rising after 2 and 5 business days, a factory meeting counts as an intro unless the economic buyer attends) are used as seed values.
- Check this: leak map colours: green at 90% of target or more, amber 75 to 89%, red under 75%.
- Check this: brand colour #847347 (hue 43) from unifyapps.com's header and logo; logo is the site's published footer logo.
- Check this: the AI agent's model is UnifyApps Headless's recommendation (profile standing answer).
- Check this: external systems without a connection on the tenant (Apollo, Sprouts, Google Calendar, Gong, LinkedIn Ads, a writable HubSpot) are shown as mocked register and run rows.
- Pipeline Factory · Reset demo and Pipeline Factory Seed snapshot are the demo's housekeeping: no beat shows them and no screen calls Reset demo.

## entities

## beats

**Storyline: "One pilot patch, from signal to booked meeting"** · intent proposed: both · 7 beats (6 story beats and hood beat H1)

1. **Patch tower** · route `/patch` · mode: seeded (tower numbers and diagnosis), live reads. The presenter opens the pilot patch, Mountain (PT-USW-03). The screen shows pace tiles with their last read (intro meetings 8 of 13, 62%, red), the concentric view (412 patch accounts, 64 in play, 11 replied, 5 Engage, 3 Connect, 2 Commit, 1 Validate and Select, 0 Contract), the seeded diagnosis card "stops at Input: 3 of 25 slots unfilled", the patch map aberrations (a New York AE holding California accounts) and the alarm "Mountain red for 2 business days". Asks: A79 A80 A82 A83 A86 A90 A91.
2. **Gate 1** · route `/todo` (Gate 1 tab) · mode: live (Pipeline Factory · Decide Gate 1). The presenter, as Marco Ellison (pod BDR), opens the 07:00 batch: fit band, timing, top 3 signals (a checked visit counted as 14 s + scroll), Patch ID, AE, last touch, slots left. Alder Mutual shows "blocked · no Patch ID", Juniper Ridge "held out until 2027-01-29", Silverpine "on an AE hold". The presenter rejects Redstone Health Network as "active deal": the slot refills from the same patch (Basalt Energy Co-op appears), then accepts Northwind Freight Systems. Asks: A4 A21 A22 A23 A24 A25 A26 A78 A96.
3. **Account view** · route `/accounts/ACC-001` · mode: seeded (Fit Scorer, Case for Change, Buying Team Mapper, Person Notes marked AI). The presenter opens Northwind: fit 48 of 60 (best fit), HQ Denver CO (92), parent Northwind Holdings with the outreach lock, renewal est. 2027-05; the Case for Change with every sentence tagged [PUBLIC] with its quote and link or [HYPOTHESIS]; three UC-IDs; the buying team (3 Tier 1, 3 Tier 2, 4 Tier 3, 2 backups, the gatekeeper mapped and never contacted). Asks: A8 A12 A13 A16 A17 A18 A19 A27 A28 A29 A30 A31 A32 A75.
4. **Gate 2, the failure beat** · route `/todo` (Gate 2 tab, account review drawer) · mode: live (Pipeline Factory · Approve Gate 2 draft: the Send Rules Check, no model call). The presenter approves Helen Okafor's Tier 1 email (grade 86, 3 of 3 facts traced): approved. Then approves the Tier 2 email to Tom Brennan: **refused, "Blocked · on the Do-Not-Contact list (unsubscribed 2026-09-14)"**. Then approves Keisha Moreland's draft: blocked, "sender from the wrong pod · planted test error caught". Asks: A35 A37 A39 A40 A41 A42 A43 A44 A45 A70.
5. **Reply and booking** · route `/todo` (Replies tab) · mode: live (Pipeline Factory · Send reply and book meeting); reply type and drafted answer seeded. Helen Okafor replies (sorted positive, 94); the drafted answer names Dana Whitfield's booking link. The presenter clicks Send and book: a Deal at Engage owned by Dana Whitfield appears with Patch ID, BDR of record, meeting source and factory-sourced locked, and the AE's accept-by deadline. Clicking again answers "already booked · same deal". Asks: A5 A10 A49 A54 A55 A56 A61.
6. **CRO tower, the lean-forward beat** · route `/cro` · mode: live (Factory Analyst through Pipeline Factory · Ask Factory Analyst; Pipeline Factory · Escalate alarm), tower numbers seeded. The leak map shows every Geo by VEP stage; US West × Engage is red (14 of 20, 70%). The presenter clicks it to open its pods and patches, then asks the Factory Analyst "Why is US West red at Engage, and what has been done about it?"; the answer names the Mountain patch, the Input cause, the +20% pace boost on 2026-10-26, Alana Brooks and the 2026-11-04 report-back, with the rows it used. The presenter escalates the alarm; the CRO's decisions waiting show their recommendations. Optional: the DEMO-TEST alert lands in Slack (fallback: the escalation to-do alone). Asks: A71 A81 A85 A87 A88 A89 A93 A95.
   Alternatives considered: B / C. B: Gate 2 catching the planted test error, live (strong, but it is a rule, not the AI the audience came for; kept inside beat 4). C: the patch map drawing every AE-to-account line with the aberration lit (the kit has no graph part; open question 12). This one wins because the CRO tower is what the blueprint is written for: every number drills down and the assistant explains it from the same rows.
7. **H1 · under the hood** · route `/runs`, then the platform · mode: live reads. The presenter opens Runs and register: the hand-off register (57 components, stage, writer, threshold, model family, rung, success rate against 99%) and the run trace (input, output, model, confidence, cost, latency, patch, a "rejected on save" schema-check run and a "late, retried" run). Then opens Pipeline Factory · Decide Gate 1 on the automation canvas and the Factory Analyst in the agent builder. Asks: A1 A2 A3 A6 A7 A63 A64 A68 A69 A74 A92 A94.

**AI surfaces and their modes**
- Factory Analyst (agent, CRO tower): live, read-only.
- Diagnosis card (Patch tower): seeded.
- Fit score, HQ confidence, Case for Change, use-case match, buying team, person notes (Account): seeded.
- Draft text, Message Grader grade, Fact Checker result (Gate 2): seeded; the Send Rules Check: live, deterministic (rules, never presented as AI).
- Reply Sorter label and Reply Writer drafted answer (Replies): seeded.
- Apollo, Sprouts, Gong, inbox health, LinkedIn Ads, HubSpot writes: mocked as register and run rows.

**Story row**: Account ACC-001 Northwind Freight Systems · patch PT-USW-03 Mountain (pilot, pace 62%, red, diagnosis input, 3 slots left) · AE Dana Whitfield, BDR Marco Ellison, Pod West-2 · fit 48 of 60, best fit · timing 31 of 40 · rank 1 · gate1 queued · signals: champion job move (Priya Raman), checked visit 14 s + scroll, renewal window 2027-05 · Tier 1 Helen Okafor (CIO, economic buyer) · Tom Brennan on the Do-Not-Contact list · drafts DR-001 (grade 86) and DR-004 (blocked) · reply TD-REP-01 positive 94 · leak TD-LEAK-01.

## views

- **Patch tower** `/patch` · beat 1 · `.app-top` crumb + `.toolbar` `.chipsel` patch switcher · `.tile` ×5 with `.delta` (pace, last read) · `.stages` concentric view · `.ai:not(.msg)` diagnosis · `.tbl` patch map aberrations with `.tag.attention` · `.feed` alarms with Escalate `.btn-s`.
- **To-do** `/todo` · beats 2, 4, 5 · `.tabs` (Gate 1, Gate 2, Replies, Exceptions) · Gate 1: `.toolbar` `.field` `.chipsel` + `.tblwrap` `.tbl` with `.tag` states, `.btn-p` Accept, `.menu` reject reasons, `.toast` refill, `.pg` · Gate 2: `.tbl` of accounts + `.drawer.l` review (`.prog` grade, `.tag` fact and rules, `.note` block reasons, `.btn-p` Approve, `.btn-s` Hold) · Replies: `.tbl` + `.ai:not(.msg)` drafted answer + `.btn-p` Send and book + `.dl` locked fields · Exceptions: `.tbl`.
- **Account** `/accounts/:accountId` · beat 3 · `.g2 .pad` account card with `.tag` · `.g1` Case for Change with `.tag` evidence tags · `.cv` use cases · `.pc` + `.faces` + `.av` buying team · `.tabs` Sequence (`.sth`), Intro paths, AE checkpoint, Prep pack, Locked fields (`.dl`) · `.feed` past contact.
- **CRO tower** `/cro` · beat 6 · `.tile` `.spark` `.delta` pulse · `.tblwrap.freeze` `.tbl` leak map with `.tag` cells · `.drawer` drill-down · `.tbl` top leaks · `.g2` decision cards with `.btn-p` · `.agent-launch` `.agent-drawer` with `.ai:not(.msg)` answer and grounding line.
- **Runs and register** `/runs` · beat 7 · `.tabs` · `.toolbar` `.field` `.chipsel` (stage, kind, demo mode) · `.tblwrap` `.tbl` register with `.tag` status · `.tbl` runs with `.tag` status and `.pg`.
- Not in the kit: the concentric rings and the patch map graph (open question 12); nearest parts `.stages` and `.tbl` grouped by AE.
