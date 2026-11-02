---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P13"
touches: [{"kind":"ai-agent","name":"PF · Winning Message Finder"},{"kind":"ai-agent","name":"PF · Scoring Tuner"},{"kind":"ai-agent","name":"PF · Objection Collector"},{"kind":"ai-agent","name":"PF · A/B Tester"},{"kind":"ai-agent","name":"PF · Quality Grader"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Winning Message Finder"},{"action":"publish","kind":"ai-agent","name":"PF · Scoring Tuner"},{"action":"publish","kind":"ai-agent","name":"PF · Objection Collector"},{"action":"publish","kind":"ai-agent","name":"PF · A/B Tester"},{"action":"publish","kind":"ai-agent","name":"PF · Quality Grader"}]
acceptedAt: "2026-11-02T10:52:06.028Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae86b5cafe7fc590a4ffb95"]
latestPlanId: "e_6ae86b5cafe7fc590a4ffb95"
planId: "e_6ae86b5cafe7fc590a4ffb95"
---
# Pipeline Factory · G3 round 2 · P13

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflow 8 (part 1): each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Winning Message Finder · new
- ai-agent · PF · Scoring Tuner · new
- ai-agent · PF · Objection Collector · new
- ai-agent · PF · A/B Tester · new
- ai-agent · PF · Quality Grader · new

## Contract
### ai-agent · PF · Winning Message Finder
[R2-P13 · agents, sub-workflow 8 (part 1)] C48, one job, built live.
- ai-agent · create · PF · Winning Message Finder: registry row C48 (agent, sub-workflow 8. Learning and governance, asks A77); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find winning messages: promote messages with 3 or more positive replies into the Message Writer's examples for that role and industry; reads PF Draft rows, PF Source reply rows and PF Component run rows of Reply Sorter through Read component inputs (component_id C48); writes a PF Component run row of output_type example_proposal (status proposal) and a hand-off to Message Writer after the Quality Grader and the Friday review, only through Save agent output (component_id C48); threshold and routing: under 3 positives: not promoted (no_action) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Message Writer (after Quality Grader and Friday review); schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; nothing applies without the Quality Grader and the Friday review; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Scoring Tuner
[R2-P13 · agents, sub-workflow 8 (part 1)] C49, one job, built live.
- ai-agent · create · PF · Scoring Tuner: registry row C49 (agent, sub-workflow 8. Learning and governance, asks A78); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: re-fit fit and signal weights to meetings and qualified opportunities, learning from Gate 1 rejections, AE-rejected meetings, disqualifications and win/loss reasons, across all patches, reported per patch; reads PF Account, PF Signal, PF Patch and PF Component run rows through Read component inputs (component_id C49); writes a PF Component run row of output_type weight_proposal (status proposal, old and new weight per signal, per patch) and hand-offs to Fit Scorer and Account Ranking after the Quality Grader and the Friday review, only through Save agent output (component_id C49); threshold and routing: proposals only; only a change within plus or minus 20% may later apply on its own after 8 weeks without a drop (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Fit Scorer; Account Ranking (after Quality Grader and Friday review); schedule in the registry: monthly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never changes a weight itself; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Objection Collector
[R2-P13 · agents, sub-workflow 8 (part 1)] C50, one job, built live.
- ai-agent · create · PF · Objection Collector: registry row C50 (agent, sub-workflow 8. Learning and governance, asks A79); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: update the objection list and buyer language from call transcripts; reads PF Source rows of kind call_transcript and meeting_transcript through Read component inputs (component_id C50); writes a PF Component run row of output_type objection_list (status proposal) and a hand-off to Follow-up Planner after the Quality Grader and the Friday review, only through Save agent output (component_id C50); threshold and routing: under 70: waiting_person, sales reviews (Save agent output applies the threshold 70 and routes below it to sales reviews); feeds (the register): Follow-up Planner (after Quality Grader and Friday review); schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · A/B Tester
[R2-P13 · agents, sub-workflow 8 (part 1)] C51, one job, built live.
- ai-agent · create · PF · A/B Tester: registry row C51 (agent, sub-workflow 8. Learning and governance, asks A80); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: design A/B tests: small changes (subject, opener, asset) as continuous tests on positive replies with at least 20% traffic per version and a 4-week limit; bold changes as fixed-size tests on people; reads PF Draft rows and PF Component run rows through Read component inputs (component_id C51); writes a PF Component run row of output_type test_variant (status proposal, the variants, traffic split, sample size) and a hand-off to Message Writer after the Quality Grader and the Friday review, only through Save agent output (component_id C51); threshold and routing: never tests a one-point lift (no_action) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Message Writer (after Quality Grader and Friday review); schedule in the registry: continuous; fixed-size tests (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Quality Grader
[R2-P13 · agents, sub-workflow 8 (part 1)] C52, one job, built live.
- ai-agent · create · PF · Quality Grader: registry row C52 (checker, sub-workflow 8. Learning and governance, asks A81); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: hold every agent's rubric and test set, grade every proposal and every prompt, model or weight change, and block a release on any drop; enforce checker-on-other-model; compute each gate's rung weekly per pod and AE; draft a policy when the same exception is resolved the same way 3 times; reads PF Component, PF Component run and PF Hand-off rows through Read component inputs (component_id C52); writes a PF Component run row of output_type release_check (pass or block with the drop), rung or policy_draft, and a hand-off to the Friday review, only through Save agent output (component_id C52); threshold and routing: blocks on any drop (no threshold) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Friday review; schedule in the registry: on every prompt, model or weight change; weekly rungs (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Read factory records (Pipeline Factory · Read factory records, the round-1 read tool, unchanged); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on family B, a different family from every drafter it grades; outside systems are the PF records (mocked), no connection.

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
- publish PF · Winning Message Finder
- publish PF · Scoring Tuner
- publish PF · Objection Collector
- publish PF · A/B Tester
- publish PF · Quality Grader

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
