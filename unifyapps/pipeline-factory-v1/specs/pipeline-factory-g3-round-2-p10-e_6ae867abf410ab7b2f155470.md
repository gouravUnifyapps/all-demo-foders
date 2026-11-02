---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P10"
touches: [{"kind":"ai-agent","name":"PF · Play Picker"},{"kind":"ai-agent","name":"PF · Page Builder"},{"kind":"ai-agent","name":"PF · Content Picker"},{"kind":"ai-agent","name":"PF · Message Writer"},{"kind":"ai-agent","name":"PF · Fact Checker"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Play Picker"},{"action":"publish","kind":"ai-agent","name":"PF · Page Builder"},{"action":"publish","kind":"ai-agent","name":"PF · Content Picker"},{"action":"publish","kind":"ai-agent","name":"PF · Message Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Fact Checker"}]
acceptedAt: "2026-11-02T10:36:24.916Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae867b3f410ab7b2f1555d6"]
latestPlanId: "e_6ae867b3f410ab7b2f1555d6"
planId: "e_6ae867b3f410ab7b2f1555d6"
---
# Pipeline Factory · G3 round 2 · P10

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflow 5 (part 1): each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Play Picker · new
- ai-agent · PF · Page Builder · new
- ai-agent · PF · Content Picker · new
- ai-agent · PF · Message Writer · new
- ai-agent · PF · Fact Checker · new

## Contract
### ai-agent · PF · Play Picker
[R2-P10 · agents, sub-workflow 5 (part 1)] C27, one job, built live.
- ai-agent · create · PF · Play Picker: registry row C27 (agent, sub-workflow 5. Outreach drafting, asks A48); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: pick the play for the signal (or the 13-week cycle) and set people, channels, start days and senders, spacing tiers so no two people at one account get email the same day; reads PF Account, PF Person, PF Signal, PF Patch and hand-offs from Buying Signal Spotter (fast lane) and Case for Change Drafter through Read component inputs (component_id C27); writes a PF Component run row of output_type play (play_id, people, channels, start days, senders) and hand-offs to Page Builder, Content Picker and Message Writer, only through Save agent output (component_id C27); threshold and routing: under 70: waiting_person, the BDR picks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR picks at Gate 2); feeds (the register): Page Builder; Content Picker; Message Writer; schedule in the registry: Day 2; fast lane within the hour (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; picks senders only from the account's patch and pod; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Page Builder
[R2-P10 · agents, sub-workflow 5 (part 1)] C28, one job, built live.
- ai-agent · create · PF · Page Builder: registry row C28 (agent, sub-workflow 5. Outreach drafting, asks A49); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: build one Art of the Possible page per account from public facts only: 2 to 3 workflows reimagined before and after for the matched use cases, proof, how UnifyApps connects their core systems and a patch event; reads PF Fact rows and hand-offs from Play Picker through Read component inputs (component_id C28); writes a PF Component run row of output_type aotp_page (the page content in marketing's locked template sections, noindex, a tracked link per prospect, mocked) and hand-offs to Fact Checker and Gate 2, only through Save agent output (component_id C28); threshold and routing: under 75: waiting_person, marketing ops checks (Save agent output applies the threshold 75 and routes below it to marketing ops checks); feeds (the register): Fact Checker; Gate 2; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never publishes a page; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Content Picker
[R2-P10 · agents, sub-workflow 5 (part 1)] C29, one job, built live.
- ai-agent · create · PF · Content Picker: registry row C29 (agent, sub-workflow 5. Outreach drafting, asks A50); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: pick one Content Factory asset per asset touch, matched on role, industry, use case, pattern, outcome, VEP stage and Geo; reads PF Source rows of kind content_asset and hand-offs from Play Picker through Read component inputs (component_id C29); writes a PF Component run row of output_type asset_pick per touch and a hand-off to Message Writer, only through Save agent output (component_id C29); threshold and routing: under 70: no asset, a sourced insight instead; skips assets over 18 months old or retired; never the same asset to two people at one account in a week (Save agent output applies the threshold 70 and routes below it to no asset, a sourced insight); feeds (the register): Message Writer; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never invents an asset; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Message Writer
[R2-P10 · agents, sub-workflow 5 (part 1)] C30, one job, built live.
- ai-agent · create · PF · Message Writer: registry row C30 (agent, sub-workflow 5. Outreach drafting, asks A51); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write every email and LinkedIn message in the play, from the Content Factory's best message for category, sub-sector, company and persona, in the assigned handbook voice, with one sourced fact, the pain this person owns and the likeliest objection for their role; reads PF Fact, PF Person, PF Source (handbook, content_asset) and hand-offs from Play Picker, Content Picker, Person Notes Writer and Battlecard Writer through Read component inputs (component_id C30); writes PF Draft rows (status waiting_gate2, its registered records) keyed account_id + person_id + play_id, and hand-offs to Fact Checker and Message Grader, only through Save agent output (component_id C30); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR); copy rules: subject 3 to 6 words on the trigger, emails 90 to 120 words, connection notes under 250 characters, open on the business problem, one insight and one question, no em dashes, placeholders or invented statistics (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Fact Checker; Message Grader; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; names the patch AE as session host and never sends; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Fact Checker
[R2-P10 · agents, sub-workflow 5 (part 1)] C31, one job, built live.
- ai-agent · create · PF · Fact Checker: registry row C31 (checker, sub-workflow 5. Outreach drafting, asks A52); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: trace every claim in drafts and pages: facts to a public source no older than 12 months, numbers to a source or the proof library, use cases to a UC-ID with account evidence; reads PF Draft rows, PF Fact rows and hand-offs from Message Writer and Page Builder through Read component inputs (component_id C31); writes PF Draft.fact_check (its registered field: passed or blocked, with the untraceable claim in its PF Component run row) and a hand-off to Send Rules Check, only through Save agent output (component_id C31); threshold and routing: blocks anything untraceable (no threshold) (Save agent output applies the threshold 0 and routes below it to blocks anything untraceable); feeds (the register): Send Rules Check; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; never rewrites a draft. Runs on the other model family from Message Writer and Page Builder; outside systems are the PF records (mocked), no connection.

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
- publish PF · Play Picker
- publish PF · Page Builder
- publish PF · Content Picker
- publish PF · Message Writer
- publish PF · Fact Checker

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
