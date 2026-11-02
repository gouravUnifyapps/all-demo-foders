---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P02"
touches: [{"kind":"automation","name":"Pipeline Factory · Read component inputs"},{"kind":"automation","name":"Pipeline Factory · Save agent output"},{"kind":"automation","name":"Pipeline Factory · Reset agent runs"},{"kind":"automation","name":"Pipeline Factory · Reset demo","id":"6ae8441df38e327618fcc13c"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read component inputs"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save agent output"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset agent runs"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset demo","id":"6ae8441df38e327618fcc13c"}]
acceptedAt: "2026-11-02T10:10:54.219Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae861b1f410ab7b2f062f35"]
latestPlanId: "e_6ae861b1f410ab7b2f062f35"
planId: "e_6ae861b1f410ab7b2f062f35"
---
# Pipeline Factory · G3 round 2 · P02

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds automations: the agents' tools: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- automation · Pipeline Factory · Read component inputs · new
- automation · Pipeline Factory · Save agent output · new
- automation · Pipeline Factory · Reset agent runs · new
- automation · Pipeline Factory · Reset demo · 6ae8441df38e327618fcc13c

## Contract
### automation · Pipeline Factory · Read component inputs
[R2-P02 · automations: the agents' tools] The agents' one read tool.
- automation · create · Pipeline Factory · Read component inputs: callable from the AI agents; inputs component_id (text, required), account_id (text), person_id (text), draft_id (text), patch_id (text); result component (text, JSON: the PF Component row with threshold, below_threshold_goes_to, feeds, writes, model_family, status), account (text, JSON), people (text, JSON), signals (text, JSON), facts (text, JSON), drafts (text, JSON), sources (text, JSON: PF Source rows of the account or person, plus rows with no account such as content assets and the handbook), handoffs_in (text, JSON: PF Hand-off rows whose to_component is this component's name, for the account when given), inboxes (text, JSON), suppression (text, JSON), recent_runs (text, JSON: the last 50 PF Component run rows, for the sw8 agents), reason (text). Read-only, deterministic, no model call; an account_id given as a name resolves to its account_id as Read factory records does; an unknown component_id answers reason "unknown component" and empty lists.

### automation · Pipeline Factory · Save agent output
[R2-P02] The agents' one write tool: the hand-off contract applied to every agent output.
- automation · create · Pipeline Factory · Save agent output: callable from the AI agents; inputs component_id (text, required), account_id (text), person_id (text), play_id (text), draft_id (text), patch_id (text), output_type (text), summary (text), payload (text, JSON), confidence (number), evidence (text), evidence_tag (text: public | hypothesis), model (text), origin (text); result result (text: saved | waiting_person | rejected | duplicate | paused), run_id (text), handoff_ids (text), reason (text). Deterministic, no model call. Reads the PF Component row: a paused component answers paused and writes nothing. Schema check: confidence 0 to 100, evidence and output_type present, patch_id taken from the account when not given; a failure saves a PF Component run with status rejected, assigned_to GTM engineer, reason "schema check failed: `field` missing", and nothing else. Idempotent on component_id + account_id + person_id + play_id + output_type: a re-run updates the same PF Component run row and answers duplicate, never a second row or a second hand-off. Under the component's threshold: the run is saved waiting_person, assigned_to its below_threshold_goes_to, and no field is written. At or over it: writes only the component's registered fields (one writer per field, from a fixed map: C02 PF Account.ultimate_parent_lock; C03 PF Account.hq_city; C06 PF Account.fit_score and fit_band; C11 PF Signal rows; C16, C17, C18 PF Fact rows of kind fact, use_case, case_for_change; C21 PF Person.role and tier; C22 PF Person.note; C30 PF Draft rows (status waiting_gate2, enrolment_key empty); C31 PF Draft.fact_check; C32 PF Draft.grade; C38 PF Inbox.placement_pct_last and blacklisted; C45 PF Account.meeting_label; C46 PF Account.qualified_status; C54 PF Draft.planted_error; every other component writes only its PF Component run row), never a locked field of a booked account (locked_at set), then calls Pipeline Factory · Save hand-off once per name in the component's feeds that is a component (from_component the component's name, to_component the feed, writes_field the field written, the same keys, confidence, payload and evidence), and saves the PF Component run with status saved (or proposal for the sw8 learning agents), model, run_at and the hand-off ids. Every write carries the origin given (default user).

### automation · Pipeline Factory · Reset agent runs
[R2-P02] The reset for the round-2 objects.
- automation · create · Pipeline Factory · Reset agent runs: callable from Pipeline Factory · Reset demo, mode deterministic, no model call; no inputs; result deleted (number), restored (number). Deletes every row whose origin is test in PF Component run, PF Source, PF Inbox and PF Suppression, puts every seed row of those four objects back from PF Seed snapshot, never touches a user row.

### automation · Pipeline Factory · Reset demo
[P02] Pipeline Factory · Reset demo: changed as the line says.
- automation · update · Pipeline Factory · Reset demo: after its round-1 steps, unchanged, it calls Pipeline Factory · Reset agent runs and adds its deleted and restored counts to its own; the PF Component rows are restored from their snapshot rows, which the registry line below rewrites to hold the built-entity fields, so a reset keeps the links.

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
- deploy Pipeline Factory · Read component inputs
- deploy Pipeline Factory · Save agent output
- deploy Pipeline Factory · Reset agent runs
- deploy Pipeline Factory · Reset demo

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
