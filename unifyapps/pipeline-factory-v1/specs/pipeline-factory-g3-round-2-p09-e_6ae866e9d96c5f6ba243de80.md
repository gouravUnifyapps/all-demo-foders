---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P09"
touches: [{"kind":"ai-agent","name":"PF · Buying Team Mapper"},{"kind":"ai-agent","name":"PF · Person Notes Writer"},{"kind":"ai-agent","name":"PF · Intro Finder"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Buying Team Mapper"},{"action":"publish","kind":"ai-agent","name":"PF · Person Notes Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Intro Finder"}]
acceptedAt: "2026-11-02T10:33:11.820Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae866ecf410ab7b2f152ff5"]
latestPlanId: "e_6ae866ecf410ab7b2f152ff5"
planId: "e_6ae866ecf410ab7b2f152ff5"
---
# Pipeline Factory · G3 round 2 · P09

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflow 4: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Buying Team Mapper · new
- ai-agent · PF · Person Notes Writer · new
- ai-agent · PF · Intro Finder · new

## Contract
### ai-agent · PF · Buying Team Mapper
[R2-P09 · agents, sub-workflow 4] C21, one job, built live.
- ai-agent · create · PF · Buying Team Mapper: registry row C21 (agent, sub-workflow 4. Buying committee, asks A41); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: map the buying team: load the industry's default titles, assign each person a role, check the champions library, pick 3 Tier 1, 3 Tier 2, 4 Tier 3 and 2 backups, and flag the economic buyer; reads PF Person rows of the account and PF Source rows through Read component inputs (component_id C21); writes PF Person.role and tier (its registered fields; gatekeepers tier mapped) and hand-offs to Person Notes Writer, Contact Finder and Intro Finder, only through Save agent output (component_id C21); threshold and routing: under 70 on a role: waiting_person, the BDR checks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR checks at Gate 2); feeds (the register): Person Notes Writer; Contact Finder; Intro Finder; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a gatekeeper is mapped, never contacted; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Person Notes Writer
[R2-P09 · agents, sub-workflow 4] C22, one job, built live.
- ai-agent · create · PF · Person Notes Writer: registry row C22 (agent, sub-workflow 4. Buying committee, asks A42); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write a four-line note per person: role and time in role, past companies and public talks, what they own ([HYPOTHESIS] unless public), the link to the matched use case and nearby event fit; reads PF Person, PF Fact (use cases) and PF Source rows through Read component inputs (component_id C22); writes PF Person.note (its registered field) and a hand-off to Message Writer, only through Save agent output (component_id C22); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR) (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Message Writer; schedule in the registry: Day 1; every 90 days; on job change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; professional information only; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Intro Finder
[R2-P09 · agents, sub-workflow 4] C23, one job, built live.
- ai-agent · create · PF · Intro Finder: registry row C23 (agent, sub-workflow 4. Buying committee, asks A43); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find a warm intro for Tier 1 people at best fit accounts from shared work history (opt-in LinkedIn exports, partners, SIs, investors), ranked worked together over overlapped over friend of a friend; reads PF Person rows (Tier 1) and PF Source rows of kind linkedin_export through Read component inputs (component_id C23); writes a PF Component run row of output_type intro_request (draft request, path, rank) into the patch AE's to-do list, and a 7-day hold on cold touches to that person in the payload, only through Save agent output (component_id C23); threshold and routing: under 60: not suggested (result no_action) (Save agent output applies the threshold 60 and routes below it to not suggested); feeds (the register): AE to-do list; schedule in the registry: Day 1, Tier 1 at best fit (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never contacts anyone; the AE sends the intro request; outside systems are the PF records (mocked), no connection.

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
- publish PF · Buying Team Mapper
- publish PF · Person Notes Writer
- publish PF · Intro Finder

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
