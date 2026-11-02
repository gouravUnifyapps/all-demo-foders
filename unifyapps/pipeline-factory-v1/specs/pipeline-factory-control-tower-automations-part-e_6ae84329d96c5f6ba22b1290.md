---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory Control Tower · automations, part 2, and the analyst"
touches: [{"kind":"automation","name":"Pipeline Factory · Pause component"},{"kind":"automation","name":"Pipeline Factory · Read factory records"},{"kind":"automation","name":"Pipeline Factory · Reset demo"},{"kind":"automation","name":"Pipeline Factory · Ask the analyst"},{"kind":"ai-agent","name":"Pipeline Factory Analyst"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"Pipeline Factory Analyst"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Pause component"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read factory records"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset demo"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Ask the analyst"}]
acceptedAt: "2026-11-02T08:00:40.908Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae8432af410ab7b2ff1251b"]
latestPlanId: "e_6ae8432af410ab7b2ff1251b"
planId: "e_6ae8432af410ab7b2ff1251b"
---
# Pipeline Factory Control Tower · automations, part 2, and the analyst

## Requested outcome
The pod BDR and the patch AE watch one account, Carrow & Vale Logistics, move through the Pipeline Factory: a strong signal takes the fast lane, Gate 1 accepts it, research and the buying team arrive as confidence-scored hand-off records, Gate 2 approves drafts while the Send Rules Check refuses one, and the booked meeting locks its fields. Every hand-off is a saved record in the control tower that a person can see, check and stop; an assistant answers what is waiting on a person and a person pauses a red component from its answer.

## Touches
- automation · Pipeline Factory · Pause component · new
- automation · Pipeline Factory · Read factory records · new
- automation · Pipeline Factory · Reset demo · new
- automation · Pipeline Factory · Ask the analyst · new
- ai-agent · Pipeline Factory Analyst · new

## Contract
### automation · Pipeline Factory · Pause component
A person stops a component; its hand-offs hold.
- automation · create · Pipeline Factory · Pause component: callable from the app; inputs component_id (text), actor (text), origin (text); result result (text: paused | already_paused), held_handoffs (number), reason (text). Sets PF Component.status paused and every flowed-pending or late PF Hand-off from that component to held; resuming is a person's job and is not offered.

### automation · Pipeline Factory · Read factory records
The analyst's read-only tool.
- automation · create · Pipeline Factory · Read factory records: callable from the AI agent; inputs patch_id (text), account_id (text); result patches (text, JSON), accounts (text, JSON), waiting_handoffs (text, JSON), red_components (text, JSON). Read-only: PF Patch, PF Account, PF Hand-off with status waiting_person, rejected or late, and PF Component with success_rate under 97.

### automation · Pipeline Factory · Reset demo
Clears test rows and restores the seed rows.
- automation · create · Pipeline Factory · Reset demo: callable, mode deterministic, no model call; no inputs; result deleted (number), restored (number). Deletes every row whose origin is test in the nine PF objects, puts every seed row back to its values in PF Seed snapshot, never touches a user row.

### automation · Pipeline Factory · Ask the analyst
Calls the analyst for the app.
- automation · create · Pipeline Factory · Ask the analyst: callable from the app; inputs question (text), patch_id (text); result answer (text), grounding (text), suggested_component_id (text). Invokes the Pipeline Factory Analyst agent with the question and the patch, and returns its answer, the records it cited, and the red component it names, if any.
### ai-agent · Pipeline Factory Analyst
The read-only assistant over the factory records.
- ai-agent · create · Pipeline Factory Analyst: read-only; model Nebula's recommendation; instructions: answers the BDR, the AE and RevOps about one patch from the factory's records only; names each hand-off by its from and to components, its confidence against the threshold and who it waits on; names a component under 97% success as red; never sends, edits or approves anything; says a field is not held when no record holds it; tool Read factory records (Pipeline Factory · Read factory records).

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

## Ready when
- Pipeline Factory · Pause component answers every result path its Contract line names.
- Pipeline Factory · Read factory records answers every result path its Contract line names.
- Pipeline Factory · Reset demo answers every result path its Contract line names.
- Pipeline Factory · Ask the analyst answers every result path its Contract line names.
- The analyst names the three hand-offs waiting on a person and Current Vendor Finder as red.
- publish Pipeline Factory Analyst
- deploy Pipeline Factory · Pause component
- deploy Pipeline Factory · Read factory records
- deploy Pipeline Factory · Reset demo
- deploy Pipeline Factory · Ask the analyst

## Assumptions
- Check this: every outside system (HubSpot, Apollo, Sprouts, Gong, Bombora, Sales Navigator, Google Calendar) is mocked by the PF objects; no external step, no connection.
- Check this: the PF objects exist (OBJ_pf_*) and hold their seed rows; tests make their own origin test rows and remove them.
- Check this: the analyst runs on the model list_models recommends.
