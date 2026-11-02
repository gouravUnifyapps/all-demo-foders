---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P05"
touches: [{"kind":"automation","name":"Pipeline Factory · Alarm and Escalation"},{"kind":"automation","name":"Pipeline Factory · Content Handoff"},{"kind":"automation","name":"Pipeline Factory · Privacy and Consent"},{"kind":"automation","name":"Pipeline Factory · Run component"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Alarm and Escalation"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Content Handoff"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Privacy and Consent"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Run component"}]
acceptedAt: "2026-11-02T10:11:31.855Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae861d8afe7fc590a34e163"]
latestPlanId: "e_6ae861d8afe7fc590a34e163"
planId: "e_6ae861d8afe7fc590a34e163"
---
# Pipeline Factory · G3 round 2 · P05

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds automations: the 12 workflows, part 3, and the registry's run action: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- automation · Pipeline Factory · Alarm and Escalation · new
- automation · Pipeline Factory · Content Handoff · new
- automation · Pipeline Factory · Privacy and Consent · new
- automation · Pipeline Factory · Run component · new

## Contract
### automation · Pipeline Factory · Alarm and Escalation
[R2-P05 · automations: the 12 workflows, part 3, and the registry's run action] C55. Reads the tower and acts on a red line.
- automation · create · Pipeline Factory · Alarm and Escalation: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs origin (text); result actions (text, JSON: component or patch, red line, action, before and after), escalations (text, JSON), reason (text). Reads PF Component success_rate and PF Patch; a component under 95% is paused automatically through Pipeline Factory · Pause component (a safety action; resuming needs a person); a component from 95% to under 97% gets a to-do item for the GTM engineer (a PF Hand-off waiting_person through Save hand-off) and is never paused by it, so beat 7's person still pauses Current Vendor Finder (96.1%); a patch under its intro pace gets a throttle or move-slots proposal as a to-do item; unfixed alarms escalate patch to pod after 2 business days, to Geo after 5, then to CRO (by the age of the open to-do item); logs before and after numbers in one PF Component run (C55).

### automation · Pipeline Factory · Content Handoff
[R2-P05] C56. Monday hand-off to marketing, mocked (LinkedIn ad audiences, Content Factory).
- automation · create · Pipeline Factory · Content Handoff: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, required), origin (text); result audiences (number), to_content_factory (number), to_nurture (number), marketing_influenced_set (number), reason (text). Accounts in play in the patch go to a LinkedIn ad audience by patch geography for 8 weeks; people never reached go to the Content Factory (ads and content only, never cold email); people whose reply was sorted "not now" or who engaged go to nurture until their date; sets PF Account.marketing_influenced true on accounts in play that are not yet booked (never on a locked account); the weekly asset, message and pattern results by patch are the run payload; one PF Component run (C56).

### automation · Pipeline Factory · Privacy and Consent
[R2-P05] C57. Consent, legal checklists, erasure and the 12-month clean-up.
- automation · create · Pipeline Factory · Privacy and Consent: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, empty for all), origin (text); result checklist (text, JSON per person: recording consent, DNC, send window, consent, footer), erasures_due (number), cleanup_flagged (number), reason (text). Per person: recording consent per state from PF Suppression consent rows, the DNC screen through Pipeline Factory · Do-Not-Contact List (action screen), the state legal checklist (send window, consent, footer); erasure rows past erase_due are completed through Do-Not-Contact List (action erase); people never engaged in 12 months are flagged for clean-up in the run (never deleted by the demo); one PF Component run (C57).

### automation · Pipeline Factory · Run component
[R2-P05] The registry's Run action: one call runs any built agent or workflow on an account.
- automation · create · Pipeline Factory · Run component: callable from the app; inputs component_id (text, required), account_id (text), person_id (text), draft_id (text), origin (text); result result (text: ran | paused | not_runnable | failed), run_id (text), handoff_ids (text), confidence (number), summary (text), reason (text). Reads the PF Component row: status paused answers paused and runs nothing; built_kind not_built (human gates C26, C40, C47 and the two rule steps) answers not_runnable "a person or a rule step, not a built entity"; built_kind ai_agent invokes the agent whose id is built_entity_id (the same invoke operation Pipeline Factory · Ask the analyst uses) with the message "Run your job for component `component_id` on account `account_id` (person, draft when given); origin `origin`", then reads the newest PF Component run of that component and account and writes latency_ms on it; built_kind automation calls the matching workflow automation above (one branch per component id, C12, C13, C14, C24, C25, C33, C35, C39, C43, C55, C56, C57, passing account_id or its patch_id and origin; C15 and C34 answer not_runnable "run from To-do or Gate 2"). If the invoke operation takes only a fixed agent, it branches per component id for the 38 agents instead. Deterministic itself; the model call is the invoked agent's.

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
- deploy Pipeline Factory · Alarm and Escalation
- deploy Pipeline Factory · Content Handoff
- deploy Pipeline Factory · Privacy and Consent
- deploy Pipeline Factory · Run component

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
