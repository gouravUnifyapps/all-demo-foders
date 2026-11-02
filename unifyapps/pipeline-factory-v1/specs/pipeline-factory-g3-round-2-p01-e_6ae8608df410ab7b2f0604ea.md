---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P01"
touches: [{"kind":"object","name":"PF Component","id":"OBJ_pf_component"},{"kind":"object","name":"PF Component run"},{"kind":"object","name":"PF Source"},{"kind":"object","name":"PF Inbox"},{"kind":"object","name":"PF Suppression"},{"kind":"object","name":"PF Seed snapshot","id":"OBJ_pf_seed_snapshot"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-11-02T10:06:04.166Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae86090afe7fc590a34bad5"]
latestPlanId: "e_6ae86090afe7fc590a34bad5"
planId: "e_6ae86090afe7fc590a34bad5"
---
# Pipeline Factory · G3 round 2 · P01

## Requested outcome
The manager asked to build all 38 agents and 12 workflows of the Pipeline Factory (feedback FB-1793612784906-1). This plan builds objects and field changes: each agent is a live UnifyApps AI agent with one job that reads through Pipeline Factory · Read component inputs and writes through Pipeline Factory · Save agent output; each workflow is a deterministic automation. The round-1 control tower and its automations stay unchanged.

## Touches
- object · PF Component · OBJ_pf_component
- object · PF Component run · new
- object · PF Source · new
- object · PF Inbox · new
- object · PF Suppression · new
- object · PF Seed snapshot · OBJ_pf_seed_snapshot

## Contract
### object · PF Component
[R2-P01 · objects and field changes] The registry learns which built entity runs each component.
- object · update · PF Component: add fields built_kind (picklist: ai_agent "AI agent", automation "Automation", not_built "Not built"; default not_built), built_entity_id (text), built_entity_name (text), built_link (text), built_status (picklist: live "Live", not_built "Not built"; default not_built), built_at (date, epoch ms). Nothing else on the object changes; the round-1 fields, picklists and the 57 seeded rows stay as they are.

### object · PF Component run
[R2-P01] Every agent and workflow run, traced: input, output, model, confidence, cost and latency, keyed by patch.
- object · create · PF Component run: id OBJ_pf_component_run; primaryKey run_id (text, required); fields component_id (text), component_name (text), kind (picklist: agent "Agent", checker "Checker", monitor "Monitor", workflow "Workflow"), patch_id (text), account_id (text), person_id (text), play_id (text), draft_id (text), output_type (text), summary (text), payload (text, JSON), confidence (number), evidence (text), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]", none "None"), status (picklist: saved "Saved, flowed on", waiting_person "Waiting on a person", rejected "Rejected: schema", proposal "Proposal only", blocked "Blocked", no_action "No action", paused "Not run: component paused"), assigned_to (text), reason (text), model (text), cost_usd (number), latency_ms (number), idempotency_key (text, component_id + account_id + person_id + play_id + output_type), handoff_ids (text), run_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)

### object · PF Source
[R2-P01] The outside systems' content, mocked: filings, press, job posts, vendor case studies, LinkedIn exports, contact data, Content Factory assets, Gong calls, replies, calendar events, meeting transcripts, the handbook.
- object · create · PF Source: id OBJ_pf_source; primaryKey source_id (text, required); fields account_id (text), person_id (text), source_kind (picklist: annual_report "Annual report", investor_deck "Investor deck", earnings_call "Earnings call", press "Press", job_post "Job post", vendor_case_study "Vendor case study", procurement_notice "Procurement notice", linkedin_export "LinkedIn connection export", contact_record "Contact record", content_asset "Content Factory asset", call_transcript "Call transcript", meeting_transcript "Meeting transcript", calendar_event "Calendar event", reply "Reply", web_visit "Web visit", handbook "Handbook section"), title (text), body (text), url (text), source_date (date, epoch ms), mocked_system (text), status (text), origin (picklist: user "User", seed "Seed", test "Test"; default user)

### object · PF Inbox
[R2-P01] The sending inboxes and domains, mocked (Apollo).
- object · create · PF Inbox: id OBJ_pf_inbox; primaryKey inbox_id (text, required); fields sender (text), pod (text), domain (text), daily_limit (number), sent_today (number), ramp_week (number), placement_pct_last (number), placement_pct_prev (number), blacklisted (boolean), previously_blacklisted (boolean), status (picklist: active "Active", resting "Resting", warm_spare "Warm spare", retired "Retired", blocked_new "Blocked: new sender"), checked_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)

### object · PF Suppression
[R2-P01] The one suppression list and consent records (copied to HubSpot, Apollo and Sprouts, mocked).
- object · create · PF Suppression: id OBJ_pf_suppression; primaryKey suppression_id (text, required); fields person_id (text), account_id (text), email_hash (text), kind (picklist: opt_out "Opt-out", bounce "Bounce", complaint "Complaint", legal_hold "Legal hold", consent "Consent", erasure "Erasure"), reason (text), state (text), consent_given (boolean), copied_to (text), copied_at (date, epoch ms), erase_due (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)
- record · seed · PF Source: origin seed on every row; dates epoch ms in the 12 months before the demo unless said; links invented under carrowvale.example; all A-1001 unless named. SRC-01 annual_report "Annual report 2025", page 14: "Order exceptions are still handled by hand across our three ERPs". SRC-02 earnings_call "Q2 2026 call" 00:18:40: "We plan to automate order-to-cash end to end by 2027". SRC-03 job_post "Integration Engineer, AI Platform team (3 roles)". SRC-04 investor_deck slide 9: "Cost-to-serve is a board priority". SRC-05 press "Carrow & Vale names Colette Baines Head of AI" (6 weeks before the demo). SRC-06 vendor_case_study "Carrow & Vale on Corvane Integrate" dated 28 months before the demo (earliest evidence; renewal estimate 8 months out). SRC-07 linkedin_export, person P-1002: "Dana Okafor and Arjun Mehta worked together at Northgate Freight 2017 to 2020" (opt-in export, mocked_system "LinkedIn export (opt-in)"). SRC-08 contact_record P-1002 "arjun.mehta@carrowvale.example, verified" (mocked_system "Sprouts (mocked)"). SRC-09 contact_record P-1006 "no verified email" (Sprouts, mocked). SRC-10 content_asset "Order exception triage playbook for logistics" (UC-LOG-014, role operations, 5 months old). SRC-11 content_asset "Carrier invoice reconciliation case study" (UC-LOG-022, 22 months old: too old). SRC-12 call_transcript "Top call: logistics VP, objection: we already have an integration vendor" (Gong, mocked). SRC-13 reply P-1002 "Happy to talk next week, Tuesday works" (Apollo, mocked). SRC-14 reply P-1007 "Out of office until" a date 10 days after the demo (Apollo, mocked). SRC-15 reply P-1009 "Please remove me from your list" (Apollo, mocked). SRC-16 calendar_event "Intro: Carrow & Vale and UnifyApps", 45 min, attendees Arjun Mehta, Colette Baines, Dana Okafor, booked in the AE's Google Calendar (mocked), 3 days after the demo. SRC-17 meeting_transcript, account A-1012 Harrowgate Mutual, "New Buyer Meeting, 48 min": quotes for fit, a VEP-CFC pain (claims intake), an engaged champion, timeline "this fiscal year", a mutual next step booked. SRC-18 web_visit A-1001 "/pricing, 65 s with scroll". SRC-19 handbook (no account) "Message handbook: voice and copy rules" (the copy rules of A56).
- record · seed · PF Inbox: origin seed on every row; invented UnifyApps-branded secondary domains under .example. IN-01 Marcus Ellery, POD-NAE-1, getunifyapps.example, daily_limit 40, sent_today 22, ramp_week 4, placement 92 then 90, active. IN-02 Marcus Ellery, POD-NAE-1, unifyapps-team.example, 40, 18, ramp 4, placement 64 then 68 (two tests under 70), active. IN-03 Marcus Ellery, POD-NAE-1, tryunifyapps.example, 40, 0, ramp 4, placement 88, warm_spare. IN-04 Tomas Ilves, POD-NAE-2, meetunifyapps.example, 20, 9, ramp 2, placement 85, active. IN-05 Tomas Ilves, POD-NAE-2, unifyappsmail.example, 40, 0, placement 81, previously_blacklisted true, resting. IN-06 Priya Anand (new BDR), POD-NAE-2, hellounifyapps.example, 10, 0, ramp 1, no placement test yet, blocked_new.
- record · seed · PF Suppression: origin seed on every row. SUP-01 erasure, email_hash "sha256:9f2c…e41a" (an erased person, no person_id), reason "erasure completed", copied_to "HubSpot, Apollo, Sprouts (mocked)". SUP-02 legal_hold, account A-1004, reason "legal hold: procurement dispute". SUP-03 consent P-1001, state OH, consent_given true, reason "call recording consent". SUP-04 consent P-1002, state OH, consent_given true.
- record · seed · PF Seed snapshot: one more row per row the three seed lines above write (snapshot_id `object_id:record_id`, row_values the row as seeded, JSON), origin seed, written once after those seeds.

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


## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: the run is unattended: test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete is made.
- Check this: outside systems are mocked by PF objects; no connection is used.
