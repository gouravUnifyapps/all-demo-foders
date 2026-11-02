---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P14"
touches: [{"kind":"ai-agent","name":"PF · Agent Monitor"},{"kind":"ai-agent","name":"PF · Test Error Planter"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Agent Monitor"},{"action":"publish","kind":"ai-agent","name":"PF · Test Error Planter"}]
acceptedAt: "2026-11-02T10:55:25.017Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae86c21afe7fc590a50110a"]
latestPlanId: "e_6ae86c21afe7fc590a50110a"
planId: "e_6ae86c21afe7fc590a50110a"
---
# Pipeline Factory · G3 round 2 · P14

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflow 8 (part 2): each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Agent Monitor · new
- ai-agent · PF · Test Error Planter · new

## Contract
### ai-agent · PF · Agent Monitor
[R2-P14 · agents, sub-workflow 8 (part 2)] C53, one job, built live.
- ai-agent · create · PF · Agent Monitor: registry row C53 (monitor, sub-workflow 8. Learning and governance, asks A82); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: compare each agent to its baseline weekly on block and edit rate, factual errors, grades and confidence calibration, and alert the GTM engineer on any slip; reads PF Component, PF Component run and PF Hand-off rows through Read component inputs (component_id C53); writes a PF Component run row of output_type drift_alert per slipping agent for the GTM engineer, only through Save agent output (component_id C53); threshold and routing: any slip alerts (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): GTM engineer; schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Read factory records (Pipeline Factory · Read factory records, the round-1 read tool, unchanged); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never pauses a component (a person or Alarm and Escalation does); outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Test Error Planter
[R2-P14 · agents, sub-workflow 8 (part 2)] C54, one job, built live.
- ai-agent · create · PF · Test Error Planter: registry row C54 (agent, sub-workflow 8. Learning and governance, asks A83); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: plant test errors (for example a wrong patch AE or a sender from the wrong pod) in about 5% of Gate 2 items and score each reviewer's catch rate; reads PF Draft rows waiting at Gate 2 and PF Component run rows of Send Rules Check and Clear Gate 2 through Read component inputs (component_id C54); writes PF Draft.planted_error (its registered field) and a PF Component run row with the planted error and the catch rate per reviewer, and a hand-off to Gate 2, only through Save agent output (component_id C54); threshold and routing: about 5% of items (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Gate 2; schedule in the registry: Day 2, ~5% of Gate 2 items (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a planted draft never sends; outside systems are the PF records (mocked), no connection.

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
- publish PF · Agent Monitor
- publish PF · Test Error Planter

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
