---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory Control Tower · automations, part 1"
touches: [{"kind":"automation","name":"Pipeline Factory · Save hand-off"},{"kind":"automation","name":"Pipeline Factory · Log signal"},{"kind":"automation","name":"Pipeline Factory · Decide Gate 1"},{"kind":"automation","name":"Pipeline Factory · Clear Gate 2"},{"kind":"automation","name":"Pipeline Factory · Book meeting"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save hand-off"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Log signal"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Decide Gate 1"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Clear Gate 2"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Book meeting"}]
acceptedAt: "2026-11-02T07:46:20.153Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae83fd1afe7fc590a161a7f"]
latestPlanId: "e_6ae83fd1afe7fc590a161a7f"
planId: "e_6ae83fd1afe7fc590a161a7f"
---
# Pipeline Factory Control Tower · automations, part 1

## Requested outcome
The pod BDR and the patch AE watch one account, Carrow & Vale Logistics, move through the Pipeline Factory: a strong signal takes the fast lane, Gate 1 accepts it, research and the buying team arrive as confidence-scored hand-off records, Gate 2 approves drafts while the Send Rules Check refuses one, and the booked meeting locks its fields. Every hand-off is a saved record in the control tower that a person can see, check and stop; an assistant answers what is waiting on a person and a person pauses a red component from its answer.

## Touches
- automation · Pipeline Factory · Save hand-off · new
- automation · Pipeline Factory · Log signal · new
- automation · Pipeline Factory · Decide Gate 1 · new
- automation · Pipeline Factory · Clear Gate 2 · new
- automation · Pipeline Factory · Book meeting · new

## Contract
### automation · Pipeline Factory · Save hand-off
The hand-off contract enforced in code for every connection.
- automation · create · Pipeline Factory · Save hand-off: callable from other automations; inputs from_component (text), to_component (text), record_type (text), patch_id (text), account_id (text), person_id (text), play_id (text), confidence (number), payload (text, JSON), evidence (text), writes_field (text); result result (text: saved | duplicate | rejected | waiting_person), handoff_id (text), reason (text). Deterministic, no model call: refuses a pair not in the register (PF Component feeds) with rejected "not registered"; refuses a writes_field whose writer is another component with rejected "one writer per field"; refuses a payload with no confidence, no evidence or no patch_id with rejected "schema check failed: `field` missing" and a PF Hand-off row assigned_to GTM engineer; looks up idempotency_key account_id + person_id + play_id and answers duplicate without a second row; under the to-component's threshold saves waiting_person assigned to its below_threshold_goes_to; else saves flowed. Every row carries model, cost_usd, latency_ms and saved_at.

### automation · Pipeline Factory · Log signal
Scores a signal and sends a strong one down the fast lane.
- automation · create · Pipeline Factory · Log signal: callable from the app; inputs account_id (text), signal_type (text, a PF Signal code), source_link (text), seconds_on_page (number), scrolled (boolean), minutes_after_email (number), origin (text); result result (text: counted | not_counted | fast_lane), timing_score (number), reason (text). Deterministic: the checked-visit rule (10+ seconds and a scroll, or a repeat within 7 days; never within 2 minutes of an email's delivery, never from a scanner network, never with no interaction); weights from the starting signal weights; timing_score is the sum of counted weights, capped at 40; new_leader, event, vendor_renewal and a second checked visit are strong and go to the fast lane: one PF Hand-off Buying Signal Spotter to Play Picker through Save hand-off, due within the hour. Writes PF Signal and PF Account.timing_score.

### automation · Pipeline Factory · Decide Gate 1
The BDR's accept or reject, with hard blocks and same-patch refill.
- automation · create · Pipeline Factory · Decide Gate 1: callable from the app; inputs account_id (text), decision (text: accept | reject), reason (text: bad_fit | active_deal | wrong_timing | in_conversation), origin (text); result result (text: accepted | rejected | blocked), refill_account_id (text), reason (text). Hard blocks answer blocked with the cause: no Patch ID, no AE or pod, an AE hold, or factory_holdout true ("held out until" and the date). A reject needs one reason and refills the slot with the next queued account of the same patch (lowest rank_in_patch), never another patch's. An accept saves a Gate 1 to Company Facts Collector and Buying Team Mapper hand-off through Save hand-off and adds 1 to PF Patch.slots_used.

### automation · Pipeline Factory · Clear Gate 2
The Send Rules Check and one enrolment per person and play.
- automation · create · Pipeline Factory · Clear Gate 2: callable from the app; inputs draft_id (text), decision (text: approve | hold), actor (text), origin (text); result result (text: approved | blocked | already_enrolled | held), rule (text), reason (text). Runs the Send Rules Check before an approve: the sender's pod must be the account's pod; the person not on DNC, not in another sequence, not held out; Patch ID, AE and pod present; a planted_error draft is always blocked and counted as caught. A blocked draft gets rules_check blocked and rules_reason; an approved draft is enrolled once (Outreach Launcher, mocked: status enrolled, enrolment_key account_id + person_id + play_id, "queued for Apollo sequence (mocked)"); an approve of an enrolled draft answers already_enrolled and writes nothing.

### automation · Pipeline Factory · Book meeting
Books the meeting and locks the attribution fields.
- automation · create · Pipeline Factory · Book meeting: callable from the app; inputs account_id (text), action (text: book | correct), field (text), new_value (text), reason (text), actor_role (text), origin (text); result result (text: booked | locked | corrected), locked_fields (text), reason (text). book sets deal_stage engage, meeting_type intro, meeting_source "factory: AE booking link", factory_sourced true, factory_influenced true, locked_at now, and saves a Meeting Handoff hand-off through Save hand-off. correct on a locked field (patch_id, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced) answers locked "Locked at booking: corrections go through RevOps with a reason" unless actor_role is revops and reason is given, then corrected and logged.

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
- Pipeline Factory · Save hand-off answers every result path its Contract line names.
- Pipeline Factory · Log signal answers every result path its Contract line names.
- Pipeline Factory · Decide Gate 1 answers every result path its Contract line names.
- Pipeline Factory · Clear Gate 2 answers every result path its Contract line names.
- Pipeline Factory · Book meeting answers every result path its Contract line names.
- deploy Pipeline Factory · Save hand-off
- deploy Pipeline Factory · Log signal
- deploy Pipeline Factory · Decide Gate 1
- deploy Pipeline Factory · Clear Gate 2
- deploy Pipeline Factory · Book meeting

## Assumptions
- Check this: every outside system (HubSpot, Apollo, Sprouts, Gong, Bombora, Sales Navigator, Google Calendar) is mocked by the PF objects; no external step, no connection.
- Check this: the PF objects exist (OBJ_pf_*) and hold their seed rows; tests make their own origin test rows and remove them.
