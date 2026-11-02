---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P11"
touches: [{"kind":"ai-agent","name":"PF · Message Grader"},{"kind":"ai-agent","name":"PF · Call Script Writer"},{"kind":"ai-agent","name":"PF · Follow-up Planner"},{"kind":"ai-agent","name":"PF · Inbox Health Checker"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Message Grader"},{"action":"publish","kind":"ai-agent","name":"PF · Call Script Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Follow-up Planner"},{"action":"publish","kind":"ai-agent","name":"PF · Inbox Health Checker"}]
acceptedAt: "2026-11-02T10:38:15.759Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae8681cf410ab7b2f1566e9"]
latestPlanId: "e_6ae8681cf410ab7b2f1566e9"
planId: "e_6ae8681cf410ab7b2f1566e9"
---
# Pipeline Factory · G3 round 2 · P11

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds agents, sub-workflow 5 (part 2) and 6: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- ai-agent · PF · Message Grader · new
- ai-agent · PF · Call Script Writer · new
- ai-agent · PF · Follow-up Planner · new
- ai-agent · PF · Inbox Health Checker · new

## Contract
### ai-agent · PF · Message Grader
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C32, one job, built live.
- ai-agent · create · PF · Message Grader: registry row C32 (checker, sub-workflow 5. Outreach drafting, asks A53); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: grade each draft 0 to 100 on the message rubric: teaches something, relevant to role and company, actionable, applies to their business, well written in the right voice, follows the copy rules; reads PF Draft rows and PF Source handbook rows through Read component inputs (component_id C32); writes PF Draft.grade (its registered field) with the rubric scores in its PF Component run row, and a hand-off to Send Rules Check, only through Save agent output (component_id C32); threshold and routing: under 75: one automatic rewrite is requested (the run says rewrite_requested); under 75 again: waiting_person, a person decides at Gate 2 (Save agent output applies the threshold 75 and routes below it to one rewrite, then a person at Gate 2); feeds (the register): Send Rules Check; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; grades only; never rewrites. Runs on the other model family from Message Writer; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Call Script Writer
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C36, one job, built live.
- ai-agent · create · PF · Call Script Writer: registry row C36 (agent, sub-workflow 6. Outreach, asks A60); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write the call script for a call task: a signal-tied opener, a permission question, 3 to 5 discovery questions, the top 3 objection answers, a 20-second voicemail and a follow-up email draft, and order the BDR's call list by interest; reads PF Person, PF Signal, PF Fact and PF Source call_transcript rows (Gong, mocked) through Read component inputs (component_id C36); writes a PF Component run row of output_type call_script into the BDR's call list, only through Save agent output (component_id C36); threshold and routing: under 70: waiting_person, the BDR approves the script (Save agent output applies the threshold 70 and routes below it to BDR approves the script); feeds (the register): BDR call list; schedule in the registry: per call task (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never dials; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Follow-up Planner
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C37, one job, built live.
- ai-agent · create · PF · Follow-up Planner: registry row C37 (agent, sub-workflow 6. Outreach, asks A61); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: keep the account one conversation once anyone responds: a referral becomes the lead thread, a Tier 1 objection pauses Tiers 2 and 3 with an answer note for the AE, 2 or more people engaging in 7 days switches to Committee Surge; reads PF Source reply rows and hand-offs from Reply Sorter through Read component inputs (component_id C37); writes a PF Component run row of output_type replan and hand-offs to Fact Checker and Message Grader for every rewrite, only through Save agent output (component_id C37); threshold and routing: under 70: waiting_person, the BDR decides (Save agent output applies the threshold 70 and routes below it to BDR decides); feeds (the register): Fact Checker; Message Grader; schedule in the registry: on any response (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never sends; every rewrite goes back through Fact Checker and Message Grader; outside systems are the PF records (mocked), no connection.

### ai-agent · PF · Inbox Health Checker
[R2-P11 · agents, sub-workflow 5 (part 2) and 6] C38, one job, built live.
- ai-agent · create · PF · Inbox Health Checker: registry row C38 (agent, sub-workflow 6. Outreach, asks A62); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: check inbox health: placement per active domain, blacklists and reputation, reply rate by recipient provider, and the email-security-scanner list; reads PF Inbox rows through Read component inputs (component_id C38); writes PF Inbox.placement_pct_last and blacklisted (its registered fields), an alert PF Component run row for the BDR and the GTM engineer, and a hand-off to Email Domain Swapper, only through Save agent output (component_id C38); threshold and routing: every alert goes to the BDR and the GTM engineer (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Email Domain Swapper; schedule in the registry: weekly placement; daily blacklist (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never rests or swaps a domain itself (Email Domain Swapper owns it); outside systems are the PF records (mocked), no connection.

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
- publish PF · Message Grader
- publish PF · Call Script Writer
- publish PF · Follow-up Planner
- publish PF · Inbox Health Checker

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
