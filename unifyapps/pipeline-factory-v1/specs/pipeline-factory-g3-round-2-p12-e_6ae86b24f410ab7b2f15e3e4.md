---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P12"
touches: [{"kind":"ai-agent","name":"PF · Reply Sorter"},{"kind":"ai-agent","name":"PF · Reply Writer"},{"kind":"ai-agent","name":"PF · Meeting Prep Writer"},{"kind":"ai-agent","name":"PF · Meeting Labeler"},{"kind":"ai-agent","name":"PF · Deal Qualifier"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Reply Sorter"},{"action":"publish","kind":"ai-agent","name":"PF · Reply Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Meeting Prep Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Meeting Labeler"},{"action":"publish","kind":"ai-agent","name":"PF · Deal Qualifier"}]
acceptedAt: "2026-11-02T10:51:14.930Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae86b27afe7fc590a4ff784"]
latestPlanId: "e_6ae86b27afe7fc590a4ff784"
planId: "e_6ae86b27afe7fc590a4ff784"
---
# Pipeline Factory · G3 round 2 · P12

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflow 7: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Reply Sorter · new
- ai-agent · PF · Reply Writer · new
- ai-agent · PF · Meeting Prep Writer · new
- ai-agent · PF · Meeting Labeler · new
- ai-agent · PF · Deal Qualifier · new

## Contract
### ai-agent · PF · Reply Sorter
[R2-P12 · agents, sub-workflow 7] C41, one job, built live.
- ai-agent · create · PF · Reply Sorter: registry row C41 (checker, sub-workflow 7. Engage, Connect and Commit, asks A67); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: sort every reply into one of nine types (positive, referral, not now with date, objection, wrong person, out of office, unsubscribe, bounce, auto-reply), stop all channels for that person, and handle the mechanical types; reads PF Source rows of kind reply (Apollo and Sprouts, mocked) through Read component inputs (component_id C41); writes a PF Component run row of output_type reply_type (type, date if any, channels stopped) and hand-offs to Reply Writer, Follow-up Planner and Do-Not-Contact List; out of office moves the next touch to the return date in the payload; unsubscribe calls Do-Not-Contact List within the run, only through Save agent output (component_id C41); threshold and routing: under 90 on unsubscribe: treated as unsubscribe; under 80 on anything else: waiting_person, a person sorts it (Save agent output applies the threshold 80 and routes below it to a person sorts it (unsubscribe under 90 treated as unsubscribe)); feeds (the register): Reply Writer; Follow-up Planner; Do-Not-Contact List; schedule in the registry: on every reply (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Do-Not-Contact List (Pipeline Factory · Do-Not-Contact List); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on the other model family from Reply Writer; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Reply Writer
[R2-P12 · agents, sub-workflow 7] C42, one job, built live.
- ai-agent · create · PF · Reply Writer: registry row C42 (agent, sub-workflow 7. Engage, Connect and Commit, asks A68); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: draft the answer to a reply from the thread, the account view, the objection list and the AE's booking link; reads PF Source reply rows, PF Account, PF Fact and hand-offs from Reply Sorter through Read component inputs (component_id C42); writes a PF Component run row of output_type reply_draft into the BDR's to-do list (and the AE's for a positive reply at a best fit account), with the 90-minute reminder and 2-business-hour Geo alert as due times, only through Save agent output (component_id C42); threshold and routing: under 70: marked for full rewrite (waiting_person) (Save agent output applies the threshold 70 and routes below it to marked for full rewrite); feeds (the register): BDR to-do list; schedule in the registry: on every reply (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never sends; the person sends from the original thread; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Meeting Prep Writer
[R2-P12 · agents, sub-workflow 7] C44, one job, built live.
- ai-agent · create · PF · Meeting Prep Writer: registry row C44 (agent, sub-workflow 7. Engage, Connect and Commit, asks A70); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: build the meeting prep pack for the AE and SC: account view, buying team, thread, Case for Change, likely objections, Art of the Possible page, and questions to confirm the economic buyer and timeline; reads PF Account, PF Person, PF Fact, PF Source and hand-offs from Meeting Handoff and Deadlines and Case for Change Drafter through Read component inputs (component_id C44); writes a PF Component run row of output_type prep_pack and a hand-off to the AE AI Twin (mocked as the run), only through Save agent output (component_id C44); threshold and routing: no threshold (0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): AE AI Twin; schedule in the registry: on booking (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never invents a promise the AE made; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Meeting Labeler
[R2-P12 · agents, sub-workflow 7] C45, one job, built live.
- ai-agent · create · PF · Meeting Labeler: registry row C45 (checker, sub-workflow 7. Engage, Connect and Commit, asks A71); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: label each meeting intro, New Buyer Meeting or doesn't count, quoting evidence from the transcript, attendees and the economic-buyer flag; reads PF Source rows of kind meeting_transcript and calendar_event, PF Person through Read component inputs (component_id C45); writes PF Account.meeting_label (its registered field) with the quoted evidence in its PF Component run row, and hand-offs to Deal Qualifier and AE confirm, only through Save agent output (component_id C45); threshold and routing: doesn't count if under 20 minutes, no Tier 1 or 2 attendee, a reschedule, or a second intro within 90 days; unrecorded meetings labelled from attendees and AE notes and marked unrecorded; under 80: waiting_person, the Geo leader checks (Save agent output applies the threshold 80 and routes below it to Geo leader checks); feeds (the register): Deal Qualifier; AE confirm; schedule in the registry: after each meeting (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on the other model family from the drafters; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Deal Qualifier
[R2-P12 · agents, sub-workflow 7] C46, one job, built live.
- ai-agent · create · PF · Deal Qualifier: registry row C46 (checker, sub-workflow 7. Engage, Connect and Commit, asks A72); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: check the six qualification requirements after each New Buyer Meeting (fit 36+, a VEP-CFC pain, engaged champion, New Buyer Meeting held, timeline 12 months or less, a scheduled mutual next step), each met, partly or missing with transcript quotes; reads PF Account, PF Fact, PF Person and PF Source meeting_transcript rows through Read component inputs (component_id C46); writes PF Account.qualified_status (its registered field), the six results, the gaps with the question that closes each and the recap draft in its PF Component run row, and a hand-off to AE confirm, only through Save agent output (component_id C46); threshold and routing: recommends qualified only when all six are met; under 80: recommended not qualified, with gaps (Save agent output applies the threshold 80 and routes below it to recommended not qualified, with gaps); feeds (the register): AE confirm; graph; schedule in the registry: after each New Buyer Meeting (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; never moves a deal stage (the AE confirms). Runs on the other model family from the drafters; outside systems are the PF records (mocked), no connection.

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
- publish PF · Reply Sorter
- publish PF · Reply Writer
- publish PF · Meeting Prep Writer
- publish PF · Meeting Labeler
- publish PF · Deal Qualifier

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
