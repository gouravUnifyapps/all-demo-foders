---
nebula: 3
specId: "e_6ae8608df410ab7b2f0604ea"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P01"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"PF Component","id":"OBJ_pf_component"},{"kind":"object","name":"PF Component run"},{"kind":"object","name":"PF Source","id":"OBJ_pf_source"},{"kind":"object","name":"PF Inbox","id":"OBJ_pf_inbox"},{"kind":"object","name":"PF Suppression","id":"OBJ_pf_suppression"},{"kind":"object","name":"PF Seed snapshot","id":"OBJ_pf_seed_snapshot"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "5ad17deb-9d28-4766-a551-7cdf4715e907"
pageDesign: 2
createdAt: "2026-11-02T10:06:08.192Z"
runningAt: "2026-11-02T10:06:11.463Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory · G3 round 2 · P01

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | PF Component |  | done | 1 |
| t2 | object | PF Component run |  | done | 1 |
| t3 | object | PF Source |  | done | 1 |
| t4 | object | PF Inbox |  | done | 1 |
| t5 | object | PF Suppression |  | done | 1 |
| t6 | record | PF Source | t3 | done | 1 |
| t7 | record | PF Inbox | t4 | done | 1 |
| t8 | record | PF Suppression | t5 | done | 1 |
| t9 | record | PF Seed snapshot | t6, t7, t8 | done | 1 |

### t1 · Change object PF Component

Body:
1. Read: \`get_objects\` for PF Component (\`OBJ_pf_component\`), every field, picklist and index as it stands; if any existing field differs from the earlier contract, stop and report.
2. Done when: object · update · PF Component: add fields built_kind (picklist: ai_agent "AI agent", automation "Automation", not_built "Not built"; default not_built), built_entity_id (text), built_entity_name (text), built_link (text), built_status (picklist: live "Live", not_built "Not built"; default not_built), built_at (date, epoch ms). Nothing else on the object changes; the existing fields, picklists and the 57 seeded rows stay as they are.
3. Apply the write once. Every field keeps the exact name, type and picklist codes and labels the line gives; dates are epoch ms; text marked JSON is a text field. Add only the new fields; change nothing else on the object and touch no row.
4. Read back: \`get_objects\` for \`OBJ_pf_component\`, quoting every field the line names with its type and picklist codes.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects shows PF Component with every field the line names.
Result IDs: {"entity":"OBJ_pf_component"}
Read back: OBJ_pf_component: get_objects fields now end ... origin, built_kind, built_entity_id, built_entity_name, built_link, built_status, built_at; required [component_id]; unmirroredFields: []
Read back: OBJ_pf_component: picklists built_kind [ai_agent, automation, not_built], built_status [live, not_built]; batch wrote both with default not_built
Read back: OBJ_pf_component: types built_entity_id/built_entity_name/built_link string, built_at integer format date dateFormat epoch (apply_object_batch changes)
Read back: OBJ_pf_component: existing picklists unchanged (sub_workflow sw1..sw8, kind agent..rule_step, model_family, status live/shadow/paused, origin); get_records total 57
Unverified: The earlier (round-1) contract was not in the message, so existing fields were not compared to it field by field; they were left untouched.
Note: Security: no access settings changed; object keeps the platform permission filter.

### t2 · Create object PF Component run

Body:
1. Read: \`get_objects\` for PF Component run; the id \`OBJ_pf_component_run\` must be free (stop and report if an object of that name or id exists). Load object-schema-designer before the write.
2. Done when: object · create · PF Component run: id OBJ_pf_component_run; primaryKey run_id (text, required); fields component_id (text), component_name (text), kind (picklist: agent "Agent", checker "Checker", monitor "Monitor", workflow "Workflow"), patch_id (text), account_id (text), person_id (text), play_id (text), draft_id (text), output_type (text), summary (text), payload (text, JSON), confidence (number), evidence (text), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]", none "None"), status (picklist: saved "Saved, flowed on", waiting_person "Waiting on a person", rejected "Rejected: schema", proposal "Proposal only", blocked "Blocked", no_action "No action", paused "Not run: component paused"), assigned_to (text), reason (text), model (text), cost_usd (number), latency_ms (number), idempotency_key (text, component_id + account_id + person_id + play_id + output_type), handoff_ids (text), run_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)
3. Apply the write once. Every field keeps the exact name, type and picklist codes and labels the line gives; dates are epoch ms; text marked JSON is a text field. The primary key is the one the line names; add an index on each field named \`*_id\`.
4. Read back: \`get_objects\` for \`OBJ_pf_component_run\`, quoting every field the line names with its type and picklist codes.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects shows PF Component run with every field the line names.
Result IDs: {"entity":"OBJ_pf_component_run"}
Read back: OBJ_pf_component_run: get_objects fields run_id, component_id, component_name, kind, patch_id, account_id, person_id, play_id, draft_id, output_type, summary, payload, confidence, evidence, evidence_tag, status, assigned_to, reason, model, cost_usd, latency_ms, idempotency_key, handoff_ids, run_at, origin; required [run_id]; unmirroredFields: []
Read back: OBJ_pf_component_run: picklists kind [agent, checker, monitor, workflow], evidence_tag [public, hypothesis, none], status [saved, waiting_person, rejected, proposal, blocked, no_action, paused], origin [user, seed, test] default user
Read back: OBJ_pf_component_run: run_id string primaryKey; payload string (JSON as text); confidence/cost_usd/latency_ms number; run_at integer date epoch
Read back: OBJ_pf_component_run: indexes idx_component_id, idx_patch_id, idx_account_person (account_id+person_id), idx_play_id, idx_draft_id, all status SUCCESS
Note: Design: six non-key *_id fields but the platform allows 5 custom indexes, so account_id and person_id share one composite index (account_id, person_id); a query on person_id alone is not served by an index.
Note: Design: idempotency_key is not marked unique because the contract does not say so; a writer must check it before insert.
Note: Security: no access settings changed.
Note: feedback:
Bug: The plan's object-create task body asks for an index on each \`*_id\` field, which cannot be met past five such fields (platform cap of 5 custom indexes).
Context: Task t2, OBJ_pf_component_run, six non-key \`*_id\` fields.
Where: nebula
Evidence: Task asked for six indexes; object-storage-manager says a 6th index is refused. Built five with a composite account_id+person_id.
Cause: Suspected: the planner's generic body does not count against the five-index cap.
Regression: Plan an object with six \`*_id\` fields; the task body names at most five indexes.

### t3 · Create object PF Source

Body:
1. Read: \`get_objects\` for PF Source; the id \`OBJ_pf_source\` must be free (stop and report if an object of that name or id exists). Load object-schema-designer before the write.
2. Done when: object · create · PF Source: id OBJ_pf_source; primaryKey source_id (text, required); fields account_id (text), person_id (text), source_kind (picklist: annual_report "Annual report", investor_deck "Investor deck", earnings_call "Earnings call", press "Press", job_post "Job post", vendor_case_study "Vendor case study", procurement_notice "Procurement notice", linkedin_export "LinkedIn connection export", contact_record "Contact record", content_asset "Content Factory asset", call_transcript "Call transcript", meeting_transcript "Meeting transcript", calendar_event "Calendar event", reply "Reply", web_visit "Web visit", handbook "Handbook section"), title (text), body (text), url (text), source_date (date, epoch ms), mocked_system (text), status (text), origin (picklist: user "User", seed "Seed", test "Test"; default user)
3. Apply the write once. Every field keeps the exact name, type and picklist codes and labels the line gives; dates are epoch ms; text marked JSON is a text field. The primary key is the one the line names; add an index on each field named \`*_id\`.
4. Read back: \`get_objects\` for \`OBJ_pf_source\`, quoting every field the line names with its type and picklist codes.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects shows PF Source with every field the line names.
Result IDs: {"entity":"OBJ_pf_source"}
Read back: OBJ_pf_source: get_objects fields source_id, account_id, person_id, source_kind, title, body, url, source_date, mocked_system, status, origin; required [source_id]; unmirroredFields: []
Read back: OBJ_pf_source: picklist source_kind [annual_report, investor_deck, earnings_call, press, job_post, vendor_case_study, procurement_notice, linkedin_export, contact_record, content_asset, call_transcript, meeting_transcript, calendar_event, reply, web_visit, handbook]; origin [user, seed, test] default user
Read back: OBJ_pf_source: source_id string primaryKey; source_date integer date epoch; indexes idx_account_id, idx_person_id status SUCCESS
Note: Security: no access settings changed.

### t4 · Create object PF Inbox

Body:
1. Read: \`get_objects\` for PF Inbox; the id \`OBJ_pf_inbox\` must be free (stop and report if an object of that name or id exists). Load object-schema-designer before the write.
2. Done when: object · create · PF Inbox: id OBJ_pf_inbox; primaryKey inbox_id (text, required); fields sender (text), pod (text), domain (text), daily_limit (number), sent_today (number), ramp_week (number), placement_pct_last (number), placement_pct_prev (number), blacklisted (boolean), previously_blacklisted (boolean), status (picklist: active "Active", resting "Resting", warm_spare "Warm spare", retired "Retired", blocked_new "Blocked: new sender"), checked_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)
3. Apply the write once. Every field keeps the exact name, type and picklist codes and labels the line gives; dates are epoch ms; text marked JSON is a text field. The primary key is the one the line names; add an index on each field named \`*_id\`.
4. Read back: \`get_objects\` for \`OBJ_pf_inbox\`, quoting every field the line names with its type and picklist codes.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects shows PF Inbox with every field the line names.
Result IDs: {"entity":"OBJ_pf_inbox"}
Read back: OBJ_pf_inbox: get_objects fields inbox_id, sender, pod, domain, daily_limit, sent_today, ramp_week, placement_pct_last, placement_pct_prev, blacklisted, previously_blacklisted, status, checked_at, origin; required [inbox_id]; unmirroredFields: []
Read back: OBJ_pf_inbox: picklists status [active, resting, warm_spare, retired, blocked_new], origin [user, seed, test] default user; numbers number, blacklisted/previously_blacklisted boolean, checked_at integer date epoch
Read back: OBJ_pf_inbox: no *_id field besides the primary key inbox_id, so no custom index
Note: Security: no access settings changed.

### t5 · Create object PF Suppression

Body:
1. Read: \`get_objects\` for PF Suppression; the id \`OBJ_pf_suppression\` must be free (stop and report if an object of that name or id exists). Load object-schema-designer before the write.
2. Done when: object · create · PF Suppression: id OBJ_pf_suppression; primaryKey suppression_id (text, required); fields person_id (text), account_id (text), email_hash (text), kind (picklist: opt_out "Opt-out", bounce "Bounce", complaint "Complaint", legal_hold "Legal hold", consent "Consent", erasure "Erasure"), reason (text), state (text), consent_given (boolean), copied_to (text), copied_at (date, epoch ms), erase_due (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user)
3. Apply the write once. Every field keeps the exact name, type and picklist codes and labels the line gives; dates are epoch ms; text marked JSON is a text field. The primary key is the one the line names; add an index on each field named \`*_id\`.
4. Read back: \`get_objects\` for \`OBJ_pf_suppression\`, quoting every field the line names with its type and picklist codes.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects shows PF Suppression with every field the line names.
Result IDs: {"entity":"OBJ_pf_suppression"}
Read back: OBJ_pf_suppression: get_objects fields suppression_id, person_id, account_id, email_hash, kind, reason, state, consent_given, copied_to, copied_at, erase_due, origin; required [suppression_id]; unmirroredFields: []
Read back: OBJ_pf_suppression: picklists kind [opt_out, bounce, complaint, legal_hold, consent, erasure], origin [user, seed, test] default user; consent_given boolean; copied_at, erase_due integer date epoch
Read back: OBJ_pf_suppression: indexes idx_person_id, idx_account_id status SUCCESS
Note: email_hash is a plain string, not format hash, so a send check can filter on it.
Note: Security: no access settings changed.

### t6 · Seed PF Source rows

Body:
1. Read: \`get_objects\` for \`OBJ_pf_source\` (fields and picklist codes) and \`get_records\` on \`OBJ_pf_source\` for the rows the line names, to see which already exist.
2. Done when: record · seed · PF Source: origin seed on every row; dates epoch ms in the 12 months before the demo unless said; links invented under carrowvale.example; all A-1001 unless named. SRC-01 annual_report "Annual report 2025", page 14: "Order exceptions are still handled by hand across our three ERPs". SRC-02 earnings_call "Q2 2026 call" 00:18:40: "We plan to automate order-to-cash end to end by 2027". SRC-03 job_post "Integration Engineer, AI Platform team (3 roles)". SRC-04 investor_deck slide 9: "Cost-to-serve is a board priority". SRC-05 press "Carrow &amp; Vale names Colette Baines Head of AI" (6 weeks before the demo). SRC-06 vendor_case_study "Carrow &amp; Vale on Corvane Integrate" dated 28 months before the demo (earliest evidence; renewal estimate 8 months out). SRC-07 linkedin_export, person P-1002: "Dana Okafor and Arjun Mehta worked together at Northgate Freight 2017 to 2020" (opt-in export, mocked_system "LinkedIn export (opt-in)"). SRC-08 contact_record P-1002 "arjun.mehta@carrowvale.example, verified" (mocked_system "Sprouts (mocked)"). SRC-09 contact_record P-1006 "no verified email" (Sprouts, mocked). SRC-10 content_asset "Order exception triage playbook for logistics" (UC-LOG-014, role operations, 5 months old). SRC-11 content_asset "Carrier invoice reconciliation case study" (UC-LOG-022, 22 months old: too old). SRC-12 call_transcript "Top call: logistics VP, objection: we already have an integration vendor" (Gong, mocked). SRC-13 reply P-1002 "Happy to talk next week, Tuesday works" (Apollo, mocked). SRC-14 reply P-1007 "Out of office until" a date 10 days after the demo (Apollo, mocked). SRC-15 reply P-1009 "Please remove me from your list" (Apollo, mocked). SRC-16 calendar_event "Intro: Carrow &amp; Vale and UnifyApps", 45 min, attendees Arjun Mehta, Colette Baines, Dana Okafor, booked in the AE's Google Calendar (mocked), 3 days after the demo. SRC-17 meeting_transcript, account A-1012 Harrowgate Mutual, "New Buyer Meeting, 48 min": quotes for fit, a VEP-CFC pain (claims intake), an engaged champion, timeline "this fiscal year", a mutual next step booked. SRC-18 web_visit A-1001 "/pricing, 65 s with scroll". SRC-19 handbook (no account) "Message handbook: voice and copy rules" (the copy rules of A56).
3. Write the rows once with the record tools, by primary key (upsert), so a second run makes no second row; picklist fields take their codes; dates are epoch ms computed from today (2026-11-02) as the line says; never change a row the line does not name.
4. Read back: \`get_records\` on \`OBJ_pf_source\` for every row the line names, quoting each id with its key fields and origin.
5. Report ids (the object id as \`ids.entity\`, the row ids as \`ids.rows\`), readBack, unverified, notes.

Proof: get_records on PF Source shows every row the line names with origin seed.
Result IDs: {"entity":"OBJ_pf_source","records":["SRC-01","SRC-02","SRC-03","SRC-04","SRC-05","SRC-06","SRC-07","SRC-08","SRC-09","SRC-10","SRC-11","SRC-12","SRC-13","SRC-14","SRC-15","SRC-16","SRC-17","SRC-18","SRC-19"],"rows":["SRC-01","SRC-02","SRC-03","SRC-04","SRC-05","SRC-06","SRC-07","SRC-08","SRC-09","SRC-10","SRC-11","SRC-12","SRC-13","SRC-14","SRC-15","SRC-16","SRC-17","SRC-18","SRC-19"]}
Read back: OBJ_pf_source: get_records origin EQUAL seed total 19, ids SRC-01..SRC-19
Read back: OBJ_pf_source: SRC-01 annual_report A-1001 ... SRC-17 meeting_transcript A-1012, SRC-18 web_visit A-1001, SRC-19 handbook (no account_id)
Read back: OBJ_pf_source: SRC-07 linkedin_export person P-1002 mocked_system LinkedIn export (opt-in); SRC-08/09 contact_record Sprouts (mocked); SRC-12 Gong (mocked); SRC-13/14/15 Apollo (mocked)
Note: Dates from 2026-11-02 (demo day = today): SRC-05 2026-09-21 (6 weeks before), SRC-06 2024-07-02 (28 months), SRC-10 2026-06-02 (5 months), SRC-11 2025-01-02 (22 months), SRC-14 body 'Out of office until 12 November 2026' (10 days after), SRC-16 source_date 2026-11-05 (3 days after); others picked inside the prior 12 months.
Note: status left empty on every row: the seed line gives no status value.
Note: Rows created by primary key source_id; the object was new, so none existed before.

### t7 · Seed PF Inbox rows

Body:
1. Read: \`get_objects\` for \`OBJ_pf_inbox\` (fields and picklist codes) and \`get_records\` on \`OBJ_pf_inbox\` for the rows the line names, to see which already exist.
2. Done when: record · seed · PF Inbox: origin seed on every row; invented UnifyApps-branded secondary domains under .example. IN-01 Marcus Ellery, POD-NAE-1, getunifyapps.example, daily_limit 40, sent_today 22, ramp_week 4, placement 92 then 90, active. IN-02 Marcus Ellery, POD-NAE-1, unifyapps-team.example, 40, 18, ramp 4, placement 64 then 68 (two tests under 70), active. IN-03 Marcus Ellery, POD-NAE-1, tryunifyapps.example, 40, 0, ramp 4, placement 88, warm_spare. IN-04 Tomas Ilves, POD-NAE-2, meetunifyapps.example, 20, 9, ramp 2, placement 85, active. IN-05 Tomas Ilves, POD-NAE-2, unifyappsmail.example, 40, 0, placement 81, previously_blacklisted true, resting. IN-06 Priya Anand (new BDR), POD-NAE-2, hellounifyapps.example, 10, 0, ramp 1, no placement test yet, blocked_new.
3. Write the rows once with the record tools, by primary key (upsert), so a second run makes no second row; picklist fields take their codes; dates are epoch ms computed from today (2026-11-02) as the line says; never change a row the line does not name.
4. Read back: \`get_records\` on \`OBJ_pf_inbox\` for every row the line names, quoting each id with its key fields and origin.
5. Report ids (the object id as \`ids.entity\`, the row ids as \`ids.rows\`), readBack, unverified, notes.

Proof: get_records on PF Inbox shows every row the line names with origin seed.
Result IDs: {"entity":"OBJ_pf_inbox","records":["IN-01","IN-02","IN-03","IN-04","IN-05","IN-06"],"rows":["IN-01","IN-02","IN-03","IN-04","IN-05","IN-06"]}
Read back: OBJ_pf_inbox: get_records origin EQUAL seed total 6: IN-01 active getunifyapps.example, IN-02 active unifyapps-team.example, IN-03 warm_spare tryunifyapps.example, IN-04 active meetunifyapps.example, IN-05 resting unifyappsmail.example, IN-06 blocked_new hellounifyapps.example
Read back: OBJ_pf_inbox: write result IN-02 placement_pct_prev 64, placement_pct_last 68; IN-05 previously_blacklisted true; IN-06 no placement fields
Note: 'placement X then Y' read as prev X, last Y. IN-05 ramp_week left empty (not given). blacklisted false on every row; checked_at 2026-11-02 00:00 UTC.

### t8 · Seed PF Suppression rows

Body:
1. Read: \`get_objects\` for \`OBJ_pf_suppression\` (fields and picklist codes) and \`get_records\` on \`OBJ_pf_suppression\` for the rows the line names, to see which already exist.
2. Done when: record · seed · PF Suppression: origin seed on every row. SUP-01 erasure, email_hash "sha256:9f2c…e41a" (an erased person, no person_id), reason "erasure completed", copied_to "HubSpot, Apollo, Sprouts (mocked)". SUP-02 legal_hold, account A-1004, reason "legal hold: procurement dispute". SUP-03 consent P-1001, state OH, consent_given true, reason "call recording consent". SUP-04 consent P-1002, state OH, consent_given true.
3. Write the rows once with the record tools, by primary key (upsert), so a second run makes no second row; picklist fields take their codes; dates are epoch ms computed from today (2026-11-02) as the line says; never change a row the line does not name.
4. Read back: \`get_records\` on \`OBJ_pf_suppression\` for every row the line names, quoting each id with its key fields and origin.
5. Report ids (the object id as \`ids.entity\`, the row ids as \`ids.rows\`), readBack, unverified, notes.

Proof: get_records on PF Suppression shows every row the line names with origin seed.
Result IDs: {"entity":"OBJ_pf_suppression","records":["SUP-01","SUP-02","SUP-03","SUP-04"],"rows":["SUP-01","SUP-02","SUP-03","SUP-04"]}
Read back: OBJ_pf_suppression: get_records origin EQUAL seed total 4: SUP-01 erasure, SUP-02 legal_hold, SUP-03 consent, SUP-04 consent
Read back: OBJ_pf_suppression: write result SUP-01 no person_id, copied_to 'HubSpot, Apollo, Sprouts (mocked)'; SUP-02 account_id A-1004; SUP-03 P-1001 OH consent_given true; SUP-04 P-1002 OH consent_given true

### t9 · Seed PF Seed snapshot rows

Body:
1. Read: \`get_objects\` for \`OBJ_pf_seed_snapshot\` (fields and picklist codes) and \`get_records\` on \`OBJ_pf_seed_snapshot\` for the rows the line names, to see which already exist.
2. Done when: record · seed · PF Seed snapshot: one more row per row the three seed lines above write (snapshot_id \`object_id:record_id\`, row_values the row as seeded, JSON), origin seed, written once after those seeds.
3. Write the rows once with the record tools, by primary key (upsert), so a second run makes no second row; picklist fields take their codes; dates are epoch ms computed from today (2026-11-02) as the line says; never change a row the line does not name.
4. Read back: \`get_records\` on \`OBJ_pf_seed_snapshot\` for every row the line names, quoting each id with its key fields and origin.
5. Report ids (the object id as \`ids.entity\`, the row ids as \`ids.rows\`), readBack, unverified, notes.

Proof: get_records on PF Seed snapshot shows every row the line names with origin seed.
Result IDs: {"entity":"OBJ_pf_seed_snapshot","records":["OBJ_pf_source:SRC-01..SRC-19","OBJ_pf_inbox:IN-01..IN-06","OBJ_pf_suppression:SUP-01..SUP-04"],"rows":["OBJ_pf_source:SRC-01..SRC-19","OBJ_pf_inbox:IN-01..IN-06","OBJ_pf_suppression:SUP-01..SUP-04"]}
Read back: OBJ_pf_seed_snapshot: get_records object_id IN [OBJ_pf_source, OBJ_pf_inbox, OBJ_pf_suppression] and origin EQUAL seed total 29 (19 + 6 + 4)
Read back: OBJ_pf_seed_snapshot: write results ok for ids OBJ_pf_source:SRC-01 .. OBJ_pf_suppression:SUP-04, each origin seed
Note: Before the write, no snapshot row existed for these three objects (filtered read total 0). row_values is each row exactly as sent in t6-t8, JSON text; taken_at 1793614080000.

