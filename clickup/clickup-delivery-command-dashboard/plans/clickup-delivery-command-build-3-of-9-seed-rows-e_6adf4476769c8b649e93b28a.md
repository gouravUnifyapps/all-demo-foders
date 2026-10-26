---
nebula: 3
specId: "e_6adf4474769c8b649e938398"
mode: "sonic"
title: "ClickUp Delivery Command · build 3 of 9: seed rows"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"ClickUp Command · Change request","id":"OBJ_cucmd_change_request"},{"kind":"object","name":"ClickUp Command · Person","id":"OBJ_cucmd_person"},{"kind":"object","name":"ClickUp Command · Booking","id":"OBJ_cucmd_booking"},{"kind":"object","name":"ClickUp Command · Time entry","id":"OBJ_cucmd_time_entry"},{"kind":"object","name":"ClickUp Command · Deliverable","id":"OBJ_cucmd_deliverable"},{"kind":"object","name":"ClickUp Command · Session slot","id":"OBJ_cucmd_session_slot"},{"kind":"object","name":"ClickUp Command · Document","id":"OBJ_cucmd_document"},{"kind":"object","name":"ClickUp Command · Activity","id":"OBJ_cucmd_activity"},{"kind":"object","name":"ClickUp Command · AI output","id":"OBJ_cucmd_ai_output"},{"kind":"object","name":"ClickUp Command · Weekly metric","id":"OBJ_cucmd_weekly_metric"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "07d0ee23-424e-463a-8a27-c4db54f6a706"
pageDesign: 2
createdAt: "2026-10-26T12:15:50.036Z"
runningAt: "2026-10-26T12:15:53.193Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · build 3 of 9: seed rows

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | record | ClickUp Command · Change request |  | done | 1 |
| t2 | record | ClickUp Command · Person |  | done | 1 |
| t3 | record | ClickUp Command · Booking |  | done | 1 |
| t4 | record | ClickUp Command · Time entry |  | done | 1 |
| t5 | record | ClickUp Command · Deliverable |  | done | 1 |
| t6 | record | ClickUp Command · Session slot |  | done | 1 |
| t7 | record | ClickUp Command · Document |  | done | 1 |
| t8 | record | ClickUp Command · Activity |  | done | 1 |
| t9 | record | ClickUp Command · AI output |  | done | 1 |
| t10 | record | ClickUp Command · Weekly metric |  | done | 1 |

### t1 · Seed ClickUp Command · Change request

Body:
Read: \`get_objects\` on \`OBJ_cucmd_change_request\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_change_request\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: CR-0455 IMP-2604 "Add Slack integration", +24 h, 4320 eur, 0 days, route delivery director approved, status approved; CR-0456 IMP-2598 "Extra sandbox migration", +64 h, 11520 usd, +7 days, route director approved then finance partner rejected with reason "Budget for this quarter is spent; raise again in January", status rejected. CR-0457 is not seeded: it is raised live in beat 2.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_change_request\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_change_request\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_change_request","records":["CR-0455","CR-0456"]}
Read back: OBJ_cucmd_change_request: get_records total 2
Read back: OBJ_cucmd_change_request CR-0455: project_code IMP-2604, reason "Add Slack integration", hours_delta 24, cost_delta 4320, go_live_delta_days 0, status approved, next_approver none
Read back: OBJ_cucmd_change_request CR-0456: project_code IMP-2598, reason "Extra sandbox migration", hours_delta 64, cost_delta 11520, go_live_delta_days 7, status rejected, rejection_reason "Budget for this quarter is spent; raise again in January"
Unverified: OBJ_cucmd_change_request route_json, before_json and after_json were not in the read-back projection: get_records on CR-0455/CR-0456 with fields route_json settles it
Note: The object has no currency field: currency lives on the Project (currency picklist). cost_delta holds 4320 / 11520 and the currency code (eur / usd) is also written inside before_json and after_json.
Note: route_json: CR-0455 one step delivery_director Elena Fischer approved 2026-10-15; CR-0456 delivery_director Elena Fischer approved 2026-10-19, then finance_partner Marcus Bell rejected 2026-10-20 with the reason.

### t2 · Seed ClickUp Command · Person

Body:
Read: \`get_objects\` on \`OBJ_cucmd_person\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_person\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: P-01 Kenji Arai implementation_lead japan; P-02 Mira Lindqvist implementation_lead europe; P-03 Dana Whitfield implementation_lead north_america; P-04 Sam Okafor implementation_lead north_america; P-05 Jonas Weber implementation_lead europe; P-06 Aiko Tanaka implementation_lead japan; P-07 Yui Sato consultant japan (data migration 3, integrations 2, admin training 2, API 1, Japanese 4); P-08 Daichi Ono consultant japan (3, 2, 3, 2, 4); P-09 Lena Brandt consultant europe (2, 3, 4, 1, 0); P-10 Priya Raman consultant north_america (2, 4, 1, 4, 0); P-11 Carla Mendes consultant north_america (4, 2, 2, 2, 0); P-12 Tom Hale resource_manager europe; P-13 Elena Fischer delivery_director europe; P-14 Marcus Bell finance_partner north_america; P-15 Haruto Mori customer_sponsor japan, project IMP-2611, language ja; P-16 Grace Lin customer_sponsor north_america, project IMP-2598, language en. Capacity 40 h each; emails \`&lt;first&gt;.&lt;last&gt;@example.com\`.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_person\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_person\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_person","records":["P-01","P-02","P-03","P-04","P-05","P-06","P-07","P-08","P-09","P-10","P-11","P-12","P-13","P-14","P-15","P-16"]}
Read back: OBJ_cucmd_person: get_records total 16, P-01 to P-16 each with capacity_hours 40 and email &lt;first&gt;.&lt;last&gt;@example.com
Read back: OBJ_cucmd_person P-01: Kenji Arai implementation_lead japan
Read back: OBJ_cucmd_person P-05: Jonas Weber implementation_lead europe
Read back: OBJ_cucmd_person P-07: Yui Sato consultant japan skill_japanese 4
Read back: OBJ_cucmd_person P-13: Elena Fischer delivery_director europe; P-14: Marcus Bell finance_partner north_america; P-12: Tom Hale resource_manager europe
Read back: OBJ_cucmd_person P-15: Haruto Mori customer_sponsor japan, project_code IMP-2611, language ja
Read back: OBJ_cucmd_person P-16: Grace Lin customer_sponsor north_america, project_code IMP-2598, language en
Unverified: OBJ_cucmd_person skill fields other than skill_japanese were not in the read-back projection: get_records with fields skill_data_migration, skill_integrations, skill_admin_training, skill_api settles it

### t3 · Seed ClickUp Command · Booking

Body:
Read: \`get_objects\` on \`OBJ_cucmd_booking\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_booking\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: B-01 P-07 IMP-2611 from 2026-10-26, 4 weeks, 24 h; B-02 P-07 IMP-2618 from 2026-10-26, 8 weeks, 8 h; B-03 P-08 IMP-2612 from 2026-10-26, 6 weeks, 20 h; B-04 P-05 IMP-2609 from 2026-10-26, 5 weeks, 24 h; B-05 P-05 IMP-2602 from 2026-11-16, 4 weeks, 20 h; B-06 P-09 IMP-2615 from 2026-10-26, 4 weeks, 30 h; B-07 P-09 IMP-2619 from 2026-11-23, 10 weeks, 10 h; B-08 P-10 IMP-2598 from 2026-10-26, 12 weeks, 24 h; B-09 P-10 IMP-2621 from 2026-11-02, 8 weeks, 12 h; B-10 P-11 IMP-2607 from 2026-10-26, 8 weeks, 32 h; B-11 P-11 IMP-2613 from 2026-10-26, 5 weeks, 8 h; B-12 P-01 IMP-2611 from 2026-10-26, 6 weeks, 20 h; B-13 P-01 IMP-2618 from 2026-10-26, 6 weeks, 10 h; B-14 P-02 IMP-2604 from 2026-10-26, 8 weeks, 20 h; B-15 P-03 IMP-2595 from 2026-10-26, 2 weeks, 16 h; B-16 P-04 IMP-2624 from 2026-11-09, 12 weeks, 16 h; B-17 P-06 IMP-2626 from 2026-11-02, 12 weeks, 12 h; B-18 P-06 IMP-2622 from 2026-10-26, 10 weeks, 16 h. Jonas Weber is at 110% in the weeks of 16 and 23 Nov 2026.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_booking\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_booking\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_booking","records":["B-01","B-02","B-03","B-04","B-05","B-06","B-07","B-08","B-09","B-10","B-11","B-12","B-13","B-14","B-15","B-16","B-17","B-18"]}
Read back: OBJ_cucmd_booking: get_records total 18, B-01 to B-18
Read back: OBJ_cucmd_booking B-01: P-07 IMP-2611 first_week 1792972800000 (2026-10-26), weeks 4, hours_per_week 24
Read back: OBJ_cucmd_booking B-12: P-01 IMP-2611 first_week 1792972800000, weeks 6, hours_per_week 20
Read back: OBJ_cucmd_booking B-04: P-05 IMP-2609 first_week 1792972800000, weeks 5, hours_per_week 24, over_capacity true
Read back: OBJ_cucmd_booking B-05: P-05 IMP-2602 first_week 1794787200000 (2026-11-16), weeks 4, hours_per_week 20, over_capacity true
Note: Jonas Weber (P-05) at 110%: B-04 (24 h, weeks 26 Oct to 23 Nov) plus B-05 (20 h from 16 Nov) give 44 h of 40 in the weeks of 16 and 23 Nov; over_capacity is true on both rows, false on all others.

### t4 · Seed ClickUp Command · Time entry

Body:
Read: \`get_objects\` on \`OBJ_cucmd_time_entry\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_time_entry\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: E-01 to E-15, week of 2026-10-19: P-07 on T-2611-07 Mon to Fri 6 h, 6 h, 7 h, 6 h, 5 h (submitted); P-07 on T-2611-08 Mon to Fri 2 h each (submitted); P-08 on T-2611-09 Mon to Fri 4 h each (submitted). E-16 to E-20, week of 2026-10-26, each a Monday draft: P-07 on T-2611-07 6 h, P-08 on T-2611-09 4 h, P-10 on T-2611-10 3 h, P-07 on T-2611-08 2 h, P-08 on T-2611-13 3 h.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_time_entry\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_time_entry\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_time_entry","records":["E-01","E-02","E-03","E-04","E-05","E-06","E-07","E-08","E-09","E-10","E-11","E-12","E-13","E-14","E-15","E-16","E-17","E-18","E-19","E-20"]}
Read back: OBJ_cucmd_time_entry: get_records total 20, E-01 to E-20
Read back: OBJ_cucmd_time_entry E-01..E-05: P-07 T-2611-07 work_date 1792368000000..1792713600000 (19-23 Oct) hours 6,6,7,6,5 submitted
Read back: OBJ_cucmd_time_entry E-06..E-10: P-07 T-2611-08 2 h each submitted; E-11..E-15: P-08 T-2611-09 4 h each submitted
Read back: OBJ_cucmd_time_entry E-16 P-07 T-2611-07 6 h, E-17 P-08 T-2611-09 4 h, E-18 P-10 T-2611-10 3 h, E-19 P-07 T-2611-08 2 h, E-20 P-08 T-2611-13 3 h, each work_date 1792972800000 (Mon 26 Oct) draft
Note: Every entry has project_code IMP-2611 and week_start the Monday of its week.

### t5 · Seed ClickUp Command · Deliverable

Body:
Read: \`get_objects\` on \`OBJ_cucmd_deliverable\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_deliverable\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: D-2611-1 Workspace design (discovery, signed_off by Haruto Mori 2026-08-21); D-2611-2 Configuration build (configuration, signed_off 2026-09-18); D-2611-3 Migration wave 1 report (migration, signed_off 2026-10-09); D-2611-4 Training completion (training, signed_off 2026-10-20); D-2611-5 Cutover plan (go_live, awaiting_signoff, due 2026-10-29); each with title, title_ja and title_de.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_deliverable\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_deliverable\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_deliverable","records":["D-2611-1","D-2611-2","D-2611-3","D-2611-4","D-2611-5"]}
Read back: OBJ_cucmd_deliverable: get_records total 5
Read back: OBJ_cucmd_deliverable D-2611-1: Workspace design / ワークスペース設計 / Workspace-Design, discovery, signed_off, decided_by Haruto Mori, decided_at 1787270400000 (2026-08-21)
Read back: OBJ_cucmd_deliverable D-2611-2: Configuration build, configuration, signed_off, decided_at 1789689600000 (2026-09-18)
Read back: OBJ_cucmd_deliverable D-2611-3: Migration wave 1 report, migration, signed_off, decided_at 1791504000000 (2026-10-09)
Read back: OBJ_cucmd_deliverable D-2611-4: Training completion, training, signed_off, decided_at 1792454400000 (2026-10-20)
Read back: OBJ_cucmd_deliverable D-2611-5: Cutover plan / カットオーバー計画 / Umstellungsplan, go_live, awaiting_signoff, due_date 1793232000000 (2026-10-29)
Note: All four signed-off rows carry decided_by Haruto Mori; due_date of each signed-off row is set to its sign-off date.

### t6 · Seed ClickUp Command · Session slot

Body:
Read: \`get_objects\` on \`OBJ_cucmd_session_slot\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_session_slot\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: S-01 to S-12 for IMP-2611, topic "Admin training: permissions", 3 days (2026-10-28, 2026-10-29, 2026-10-30) at 10:00, 13:00, 15:00 and 17:00 Asia/Tokyo, 60 min; S-02, S-05 and S-10 taken.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_session_slot\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_session_slot\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_session_slot","records":["S-01","S-02","S-03","S-04","S-05","S-06","S-07","S-08","S-09","S-10","S-11","S-12"]}
Read back: OBJ_cucmd_session_slot: get_records total 12, S-01 to S-12
Read back: OBJ_cucmd_session_slot S-01..S-04 slot_start 1793149200000, 1793160000000, 1793167200000, 1793174400000 (28 Oct 10:00, 13:00, 15:00, 17:00 Asia/Tokyo)
Read back: OBJ_cucmd_session_slot S-02 taken true, S-05 taken true, S-10 taken true; all others taken false
Note: slot_start holds the exact instant in epoch ms (Tokyo time minus 9 h, e.g. 10:00 JST = 01:00 UTC), not UTC midnight, because the line gives a time. Each row: project_code IMP-2611, topic "Admin training: permissions", duration_min 60. Taken rows carry a fictional booked_by name.

### t7 · Seed ClickUp Command · Document

Body:
Read: \`get_objects\` on \`OBJ_cucmd_document\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_document\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: DOC-01 IMP-2611 sow "Statement of work: Sakura Mobility", shared; DOC-02 IMP-2611 migration_plan "Migration plan v3", shared; DOC-03 IMP-2611 signoff_record "Sign-off: Configuration build"; DOC-04 IMP-2611 signoff_record "Sign-off: Migration wave 1"; DOC-05 IMP-2611 upload "sakura-users-wave2.csv", 50000 rows, 214 errors, needs_fixing, errors_json holding the first 20 errors (missing email, duplicate email, unknown department); DOC-06 IMP-2611 status_report "Weekly status 19 Oct", ai_written true, edited by Kenji Arai, published 2026-10-19; DOC-07 IMP-2604 sow; DOC-08 IMP-2598 migration_plan. Each body is the readable text the viewer shows.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_document\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_document\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_document","records":["DOC-01","DOC-02","DOC-03","DOC-04","DOC-05","DOC-06","DOC-07","DOC-08"]}
Read back: OBJ_cucmd_document: get_records total 8
Read back: OBJ_cucmd_document DOC-01: IMP-2611 sow "Statement of work: Sakura Mobility" shared_with_customer true; DOC-02: IMP-2611 migration_plan "Migration plan v3" shared true
Read back: OBJ_cucmd_document DOC-03: signoff_record "Sign-off: Configuration build"; DOC-04: signoff_record "Sign-off: Migration wave 1"
Read back: OBJ_cucmd_document DOC-05: upload "sakura-users-wave2.csv" row_count 50000, error_count 214, upload_status needs_fixing
Read back: OBJ_cucmd_document DOC-06: status_report "Weekly status 19 Oct" ai_written true, edited_by Kenji Arai, published_at 1792368000000 (2026-10-19)
Read back: OBJ_cucmd_document DOC-07: IMP-2604 sow; DOC-08: IMP-2598 migration_plan
Unverified: OBJ_cucmd_document body and errors_json were not in the read-back projection: get_records on DOC-05 with fields errors_json settles it
Note: errors_json on DOC-05 holds 20 entries with row, column and message (missing email, duplicate email, unknown department).
Note: shared_with_customer: true on DOC-01, DOC-02 (named shared), DOC-05 (the customer's own upload) and DOC-06 (published report); false on DOC-03, DOC-04, DOC-07, DOC-08, which the line does not call shared.

### t8 · Seed ClickUp Command · Activity

Body:
Read: \`get_objects\` on \`OBJ_cucmd_activity\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_activity\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: twenty rows across IMP-2611, IMP-2604, IMP-2598 and IMP-2609 from 2026-10-12 to 2026-10-26, among them A-20 IMP-2611 Kenji Arai updated "Health changed On track to At risk" 2026-10-26 and A-19 IMP-2611 Haruto Mori signed_off "Training completion" 2026-10-20.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_activity\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_activity\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_activity","records":["A-01","A-02","A-03","A-04","A-05","A-06","A-07","A-08","A-09","A-10","A-11","A-12","A-13","A-14","A-15","A-16","A-17","A-18","A-19","A-20"]}
Read back: OBJ_cucmd_activity: get_records total 20, A-01 to A-20
Read back: OBJ_cucmd_activity A-20: IMP-2611 Kenji Arai updated "Health changed On track to At risk" at 1792972800000 (2026-10-26)
Read back: OBJ_cucmd_activity A-19: IMP-2611 Haruto Mori signed_off "Training completion" at 1792454400000 (2026-10-20)
Note: Rows spread across IMP-2611, IMP-2604, IMP-2598 and IMP-2609 from 2026-10-12 to 2026-10-26, consistent with the change requests, bookings and AI outputs seeded in this batch.

### t9 · Seed ClickUp Command · AI output

Body:
Read: \`get_objects\` on \`OBJ_cucmd_ai_output\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_ai_output\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: AI-01 IMP-2611 risk_flag "Likely to miss 16 Nov go-live", confidence 78, evidence "4 of 6 migration tasks late by 5 days on average", "SSO cutover rehearsal failed twice (RSK-1183)", "214 of 50,000 user rows failing (DOC-05)"; AI-02 IMP-2609 risk_flag confidence 64, evidence "Go-live readiness review moved twice"; AI-03 IMP-2602 risk_flag confidence 52, evidence "Configuration 20% behind plan"; AI-04 IMP-2611 meeting_summary "Steering meeting 22 Oct" with decisions ("Cutover rehearsal re-run on 3 Nov"), actions ("Sakura IT to fix 214 user rows by 30 Oct") and risks ("Cutover weekend staffing"), each with transcript_refs_json pointing to lines of the transcript held in body; AI-05, AI-06, AI-07 IMP-2611 proposed_task from AI-04 ("Fix 214 failing user rows", "Book cutover weekend support", "Re-run SSO rehearsal"), decision proposed; AI-08 IMP-2611 status_report draft of 19 Oct. Every row ai_written true.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_ai_output\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_ai_output\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_ai_output","records":["AI-01","AI-02","AI-03","AI-04","AI-05","AI-06","AI-07","AI-08"]}
Read back: OBJ_cucmd_ai_output: get_records total 8, every row ai_written true
Read back: OBJ_cucmd_ai_output AI-01: IMP-2611 risk_flag "Likely to miss 16 Nov go-live" confidence 78
Read back: OBJ_cucmd_ai_output AI-02: IMP-2609 risk_flag confidence 64; AI-03: IMP-2602 risk_flag confidence 52
Read back: OBJ_cucmd_ai_output AI-04: IMP-2611 meeting_summary "Steering meeting 22 Oct"
Read back: OBJ_cucmd_ai_output AI-05 "Fix 214 failing user rows", AI-06 "Book cutover weekend support", AI-07 "Re-run SSO rehearsal": IMP-2611 proposed_task decision proposed
Read back: OBJ_cucmd_ai_output AI-08: IMP-2611 status_report "Weekly status 19 Oct (draft)"
Unverified: OBJ_cucmd_ai_output evidence_json and transcript_refs_json were not in the read-back projection: get_records on AI-01 and AI-04 with those fields settles it
Note: AI-04 body holds a 10-line numbered transcript; its decisions, actions and risks are in evidence_json as {decisions, actions, risks}, each item with transcript_refs line numbers, and transcript_refs_json lists the same items with their lines (decision 4-5, action 6-7, risk 8-10). AI-05..AI-07 transcript_refs_json point at AI-04 lines.

### t10 · Seed ClickUp Command · Weekly metric

Body:
Read: \`get_objects\` on \`OBJ_cucmd_weekly_metric\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_weekly_metric\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: twelve weeks from 2026-08-10 to 2026-10-26; on-track share 81, 80, 80, 79, 78, 78, 77, 77, 76, 76, 75, 75 percent; week 2026-10-19 on_track 159, at_risk 33, off_track 19, active 211; week 2026-10-26 on_track 161, at_risk 38, off_track 15, active 214, golives_this_month 9 (last week 10), avg_days_to_golive 61 (last week 63), utilisation_pct 87 (last week 83), value_awaiting_usd 18400000 (last month 17800000), bridge_new 2100000, bridge_golives -1300000, bridge_slipped 200000, bridge_cancelled -400000, top_movers_json naming IMP-2611 (On track to At risk: cutover rehearsal failed), IMP-2602 (go-live slipped 2 weeks), IMP-2613 (On track to At risk: training attendance 48%), IMP-2598 (At risk to Off track: sandbox change request rejected), IMP-2607 (go-live slipped 4 weeks), last_updated 2026-10-26 06:00 UTC.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_weekly_metric\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_weekly_metric\` returns every row the body names, quoted by primaryKey.
Result IDs: {"entity":"OBJ_cucmd_weekly_metric","records":["1786320000000","1786924800000","1787529600000","1788134400000","1788739200000","1789344000000","1789948800000","1790553600000","1791158400000","1791763200000","1792368000000","1792972800000"]}
Read back: OBJ_cucmd_weekly_metric: get_records total 12, week_start 1786320000000 (2026-08-10) to 1792972800000 (2026-10-26)
Read back: OBJ_cucmd_weekly_metric 1792368000000 (2026-10-19): on_track 159, at_risk 33, off_track 19, active_projects 211, golives_this_month 10, utilisation_pct 83
Read back: OBJ_cucmd_weekly_metric 1792972800000 (2026-10-26): on_track 161, at_risk 38, off_track 15, active_projects 214, golives_this_month 9, utilisation_pct 87, value_awaiting_usd 18400000, bridge_new 2100000, last_updated 1792994400000 (06:00 UTC)
Read back: OBJ_cucmd_weekly_metric 1790553600000 (2026-09-28, last month): value_awaiting_usd 17800000
Unverified: OBJ_cucmd_weekly_metric avg_days_to_golive, bridge_golives/slipped/cancelled and top_movers_json were not in the read-back projection: get_records on 1792972800000 with those fields settles it
Note: The object has no on-track share field: share is on_track / active_projects, and the rows round to 81, 80, 80, 79, 78, 78, 77, 77, 76, 76, 75, 75 percent.
Note: handover: OBJ_cucmd_weekly_metric's primaryKey is week_start (integer), so each record id is the epoch ms as a string, e.g. "1792972800000" for 2026-10-26.
Note: 'Last week' values live on the 2026-10-19 row (golives 10, avg_days 63, utilisation 83); 'last month' value_awaiting_usd 17800000 lives on the 2026-09-28 row.

