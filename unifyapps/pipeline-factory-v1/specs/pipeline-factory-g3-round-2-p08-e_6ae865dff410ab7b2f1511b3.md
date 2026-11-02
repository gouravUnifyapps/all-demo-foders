---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P08"
touches: [{"kind":"ai-agent","name":"PF · Buying Signal Spotter"},{"kind":"ai-agent","name":"PF · Company Facts Collector"},{"kind":"ai-agent","name":"PF · Use Case Matcher"},{"kind":"ai-agent","name":"PF · Case for Change Drafter"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Buying Signal Spotter"},{"action":"publish","kind":"ai-agent","name":"PF · Company Facts Collector"},{"action":"publish","kind":"ai-agent","name":"PF · Use Case Matcher"},{"action":"publish","kind":"ai-agent","name":"PF · Case for Change Drafter"}]
acceptedAt: "2026-11-02T10:28:46.278Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae865e1f410ab7b2f1511cd"]
latestPlanId: "e_6ae865e1f410ab7b2f1511cd"
planId: "e_6ae865e1f410ab7b2f1511cd"
---
# Pipeline Factory · G3 round 2 · P08

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflows 2 and 3: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Buying Signal Spotter · new
- ai-agent · PF · Company Facts Collector · new
- ai-agent · PF · Use Case Matcher · new
- ai-agent · PF · Case for Change Drafter · new

## Contract
### ai-agent · PF · Buying Signal Spotter
[R2-P08 · agents, sub-workflows 2 and 3] C11, one job, built live.
- ai-agent · create · PF · Buying Signal Spotter: registry row C11 (agent, sub-workflow 2. Account selection, asks A28); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: watch the signal sources, record each signal (company, type, date, source link, strength), verify company match and date, score confidence, and send strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) to the Play Picker; reads PF Source rows (web_visit, press, job_post, events), PF Signal and hand-offs from Renewal Date Finder through Read component inputs (component_id C11); writes PF Signal rows (its registered records, weights from the starting signal weights, the checked-visit rule) and hand-offs to Account Ranking, and to Play Picker for a strong signal, only through Save agent output (component_id C11); threshold and routing: under 70: logged, not scored (counted false); signals fade over 30 days (Save agent output applies the threshold 70 and routes below it to logged, not scored); feeds (the register): Account Ranking; Play Picker (fast lane); schedule in the registry: continuous (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never counts a visit that fails the checked-visit rule; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Company Facts Collector
[R2-P08 · agents, sub-workflows 2 and 3] C16, one job, built live.
- ai-agent · create · PF · Company Facts Collector: registry row C16 (agent, sub-workflow 3. Account research, asks A36); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: extract sourced company facts on AI, automation, integration, modernisation, cost, CX and risk from the annual report, investor deck, two earnings calls, 12 months of press and current job posts; reads PF Source rows of the account (annual_report, investor_deck, earnings_call, press, job_post) through Read component inputs (component_id C16); writes PF Fact rows of kind fact (statement, exact quote, page or timestamp, date, link, [PUBLIC]) and hand-offs to Use Case Matcher and Case for Change Drafter, only through Save agent output (component_id C16); threshold and routing: a fact without quote and link is rejected; anything over 12 months old is dropped (except the latest annual report) (Save agent output applies the threshold 0 and routes below it to facts without quote and link rejected); feeds (the register): Use Case Matcher; Case for Change Drafter; schedule in the registry: Day 1; best fit every 30 days, others 90 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a fact without its quote and link; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Use Case Matcher
[R2-P08 · agents, sub-workflows 2 and 3] C17, one job, built live.
- ai-agent · create · PF · Use Case Matcher: registry row C17 (agent, sub-workflow 3. Account research, asks A37); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: match VEP-CFC use cases to the account's industry and core systems, score the evidence and keep the top 3 with two supporting facts (or one fact plus engagement), tagged with pattern and outcome; reads PF Fact rows of kind fact and PF Source rows through Read component inputs (component_id C17); writes PF Fact rows of kind use_case (UC-ID, pattern, outcome, supporting facts) and a hand-off to Case for Change Drafter, only through Save agent output (component_id C17); threshold and routing: under 70: saved as a question only, tagged [HYPOTHESIS], never a claim (Save agent output applies the threshold 70 and routes below it to shown only as a question); feeds (the register): Case for Change Drafter; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; uses only VEP-CFC use cases (a UC-ID); outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Case for Change Drafter
[R2-P08 · agents, sub-workflows 2 and 3] C18, one job, built live.
- ai-agent · create · PF · Case for Change Drafter: registry row C18 (agent, sub-workflow 3. Account research, asks A38); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write the Case for Change: business problem in the company's own words, impact with no dollar figures, why now from the top signals, why UnifyApps, closest proof, main and backup angle, and risks; reads PF Fact rows (facts and use cases), PF Signal rows and the account's PF Person rows through Read component inputs (component_id C18); writes PF Fact rows of kind case_for_change, each citing a fact_id or tagged [HYPOTHESIS], and hand-offs to Play Picker, Message Writer and Meeting Prep Writer, only through Save agent output (component_id C18); threshold and routing: under 70: waiting_person, the BDR reviews it at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR reviews at Gate 2); feeds (the register): Play Picker; Message Writer; Meeting Prep Writer; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a sentence without a cited fact or a [HYPOTHESIS] tag, and never writes emails; outside systems are the PF records (mocked), no connection.

## Business rules
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

## Ready when
- Every entity this plan names is built and read back as its line says.
- publish PF · Buying Signal Spotter
- publish PF · Company Facts Collector
- publish PF · Use Case Matcher
- publish PF · Case for Change Drafter

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
