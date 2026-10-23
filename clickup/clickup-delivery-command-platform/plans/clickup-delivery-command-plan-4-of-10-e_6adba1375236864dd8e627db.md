---
nebula: 3
specId: "e_6adba134925d282255bde0cd"
mode: "sonic"
title: "ClickUp Delivery Command · plan 4 of 10"
owner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"Delivery Command · Session slot","id":"OBJ_dcmd_session_slot"},{"kind":"object","name":"Delivery Command · Sign-off","id":"OBJ_dcmd_signoff"},{"kind":"object","name":"Delivery Command · Checklist item","id":"OBJ_dcmd_checklist_item"},{"kind":"object","name":"Delivery Command · Notification","id":"OBJ_dcmd_notification"},{"kind":"object","name":"Delivery Command · Integration","id":"OBJ_dcmd_integration"},{"kind":"object","name":"Delivery Command · Saved view","id":"OBJ_dcmd_saved_view"},{"kind":"object","name":"Delivery Command · Weekly snapshot","id":"OBJ_dcmd_weekly_snapshot"},{"kind":"object","name":"Delivery Command · Weekly metric","id":"OBJ_dcmd_weekly_metric"},{"kind":"object","name":"Delivery Command · AI output","id":"OBJ_dcmd_ai_output"},{"kind":"object","name":"Delivery Command · Role permission","id":"OBJ_dcmd_role_permission"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "fbe7310a-c767-48a3-bb73-7723e83dc957"
pageDesign: 2
createdAt: "2026-10-23T18:02:30.820Z"
runningAt: "2026-10-23T18:02:36.218Z"
runner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"382b1b0f-8b04-5591-805d-15b67bc592e7"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · plan 4 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | record | Delivery Command · Session slot |  | done | 1 |
| t2 | record | Delivery Command · Sign-off |  | done | 1 |
| t3 | record | Delivery Command · Checklist item |  | done | 1 |
| t4 | record | Delivery Command · Notification |  | done | 1 |
| t5 | record | Delivery Command · Integration |  | done | 1 |
| t6 | record | Delivery Command · Saved view |  | done | 1 |
| t7 | record | Delivery Command · Weekly snapshot |  | done | 1 |
| t8 | record | Delivery Command · Weekly metric |  | done | 1 |
| t9 | record | Delivery Command · AI output |  | done | 1 |
| t10 | record | Delivery Command · Role permission |  | done | 1 |

### t1 · Seed Delivery Command · Session slot

Body:
Read: get_objects for \`OBJ_dcmd_session_slot\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/session_slot.csv\`; get_records on \`OBJ_dcmd_session_slot\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/session_slot.csv\` is stored in \`OBJ_dcmd_session_slot\`, one record per row, nothing made up: the 12 rows of studio/data/seed/session_slot.csv (4 taken).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_session_slot\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_session_slot\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/session_slot.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_session_slot","records":["SLT-01","SLT-02","SLT-03","SLT-04","SLT-05","SLT-06","SLT-07","SLT-08","SLT-09","SLT-10","SLT-11","SLT-12"]}
Read back: OBJ_dcmd_session_slot: get_records total 12 (CSV has 12 rows); was 0 before the write
Read back: OBJ_dcmd_session_slot SLT-01 as stored: slot_id SLT-01, project_id IMP-2611, date 1793577600000 (2026-11-02 00:00 UTC), start 10:00, end 11:30, topic Admin training, taken true, booked_by Hana Mori
Note: Rows written with apply_record_edits (the object-storage-manager writer for storage rows), not save_entity_records as the body says; save_entity_records writes platform stored types, not object rows.
Note: Empty booked_by cells left unset; 4 rows taken true (SLT-01, 02, 06, 07).
Note: feedback:
Bug: Plan record-seed task bodies tell the builder to "Apply the writes with save_entity_records", a tool for the platform's own stored types, not Storage object rows.
Context: Plan e_6adba1375236864dd8e627db, seed tasks t1-t10 on OBJ_dcmd_* objects; object-storage-manager says storage rows are written with apply_record_edits.
Where: nebula
Evidence: Every task body in batch e627db-fde-agent-1-1.md says "Apply the writes with save_entity_records"; rows were seeded with apply_record_edits and every get_records total matched the CSV.
Cause: Suspected: the plan's record-seed task template names the wrong writer.
Regression: Generate a plan with a record seed task for a Storage object; its body should name apply_record_edits.

### t2 · Seed Delivery Command · Sign-off

Body:
Read: get_objects for \`OBJ_dcmd_signoff\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/signoff.csv\`; get_records on \`OBJ_dcmd_signoff\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/signoff.csv\` is stored in \`OBJ_dcmd_signoff\`, one record per row, nothing made up: the 4 rows of studio/data/seed/signoff.csv (SGN-302 Migration plan v2 Awaiting sign-off).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_signoff\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_signoff\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/signoff.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_signoff","records":["SGN-300","SGN-301","SGN-302","SGN-310"]}
Read back: OBJ_dcmd_signoff: get_records total 4 (CSV has 4 rows); was 0 before the write
Read back: OBJ_dcmd_signoff SGN-300 as stored: project_id IMP-2611, stage discovery, deliverable Discovery sign-off pack, status signed_off, requested_at 1786579200000 (2026-08-13), decided_by Hana Mori, decided_at 1786932000000 (2026-08-17T11:00+09:00)
Note: Stage labels mapped to codes (Discovery-&gt;discovery, Configuration-&gt;configuration, Data migration-&gt;data_migration). SGN-302 stored stage data_migration, status awaiting, decided_by/decided_at/comment unset. Written with apply_record_edits.

### t3 · Seed Delivery Command · Checklist item

Body:
Read: get_objects for \`OBJ_dcmd_checklist_item\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/checklist_item.csv\`; get_records on \`OBJ_dcmd_checklist_item\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/checklist_item.csv\` is stored in \`OBJ_dcmd_checklist_item\`, one record per row, nothing made up: the 10 rows of studio/data/seed/checklist_item.csv (7 answered, 3 not set).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_checklist_item\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_checklist_item\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/checklist_item.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_checklist_item","records":["CHK-01","CHK-02","CHK-03","CHK-04","CHK-05","CHK-06","CHK-07","CHK-08","CHK-09","CHK-10"]}
Read back: OBJ_dcmd_checklist_item: get_records total 10 (CSV has 10 rows); was 0 before the write
Read back: OBJ_dcmd_checklist_item CHK-01 as stored: project_id IMP-2611, order 1, question_en Single sign-on provider, question_ja シングルサインオンのプロバイダー, question_de Single-Sign-on-Anbieter, answer Okta
Note: 7 answered (CHK-01..07); CHK-08..10 answer left unset. answer is a string field so CHK-05 stored "14" as text. Written with apply_record_edits.

### t4 · Seed Delivery Command · Notification

Body:
Read: get_objects for \`OBJ_dcmd_notification\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/notification.csv\`; get_records on \`OBJ_dcmd_notification\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/notification.csv\` is stored in \`OBJ_dcmd_notification\`, one record per row, nothing made up: the 6 rows of studio/data/seed/notification.csv.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_notification\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_notification\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/notification.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_notification","records":["NTF-01","NTF-02","NTF-03","NTF-04","NTF-05","NTF-06"]}
Read back: OBJ_dcmd_notification: get_records total 6 (CSV has 6 rows); was 0 before the write
Read back: OBJ_dcmd_notification NTF-01 as stored: recipient Mei Takahashi, kind signoff, text Hana Mori signed off Configuration design, link /projects/IMP-2611, read true, at 1792459860000 (2026-10-20T10:31+09:00)
Note: Written with apply_record_edits.

### t5 · Seed Delivery Command · Integration

Body:
Read: get_objects for \`OBJ_dcmd_integration\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/integration.csv\`; get_records on \`OBJ_dcmd_integration\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/integration.csv\` is stored in \`OBJ_dcmd_integration\`, one record per row, nothing made up: the 4 rows of studio/data/seed/integration.csv (Jira Sync failed since 06:40 UTC, 3 escalations affected).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_integration\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_integration\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/integration.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_integration","records":["Salesforce","Slack","Google Drive","Jira"]}
Read back: OBJ_dcmd_integration: get_records total 4 (CSV has 4 rows); was 0 before the write
Read back: OBJ_dcmd_integration Salesforce as stored: system Salesforce, status live, last_sync 1792744800000 (2026-10-23T08:40Z)
Note: Jira row written status sync_failed, last_sync 1792737600000 (06:40 UTC), error and affected text verbatim. Written with apply_record_edits.
Note: handover: OBJ_dcmd_integration record ids are the system names (primary key): Salesforce, Slack, Google Drive, Jira.

### t6 · Seed Delivery Command · Saved view

Body:
Read: get_objects for \`OBJ_dcmd_saved_view\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/saved_view.csv\`; get_records on \`OBJ_dcmd_saved_view\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/saved_view.csv\` is stored in \`OBJ_dcmd_saved_view\`, one record per row, nothing made up: the 2 rows of studio/data/seed/saved_view.csv.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_saved_view\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_saved_view\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/saved_view.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_saved_view","records":["VW-01","VW-02"]}
Read back: OBJ_dcmd_saved_view: get_records total 2 (CSV has 2 rows); was 0 before the write
Read back: OBJ_dcmd_saved_view VW-01 as stored: name Japan · at risk, owner Elena Brooks, filters {"region":["Japan"],"health":["at_risk"]}, shared_with_team true
Note: filters JSON kept verbatim as text (field is a string textarea). Written with apply_record_edits.

### t7 · Seed Delivery Command · Weekly snapshot

Body:
Read: get_objects for \`OBJ_dcmd_weekly_snapshot\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/weekly_snapshot.csv\`; get_records on \`OBJ_dcmd_weekly_snapshot\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/weekly_snapshot.csv\` is stored in \`OBJ_dcmd_weekly_snapshot\`, one record per row, nothing made up: the 12 rows of studio/data/seed/weekly_snapshot.csv (on-track share 88.2% down to 66.7%).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_weekly_snapshot\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_weekly_snapshot\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/weekly_snapshot.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_weekly_snapshot","records":["1785715200000","1786320000000","1786924800000","1787529600000","1788134400000","1788739200000","1789344000000","1789948800000","1790553600000","1791158400000","1791763200000","1792368000000"]}
Read back: OBJ_dcmd_weekly_snapshot: get_records total 12 (CSV has 12 rows); was 0 before the write
Read back: OBJ_dcmd_weekly_snapshot 1785715200000 as stored: week_start 1785715200000 (2026-08-03), on_track 15, at_risk 1, off_track 1, active_projects 17, on_track_share 88.2
Note: Last row 2026-10-19 (id 1792368000000) on_track_share 66.7. Written with apply_record_edits.
Note: handover: OBJ_dcmd_weekly_snapshot and OBJ_dcmd_weekly_metric record ids are the week_start epoch ms as text (primary key), e.g. "1792368000000" for 2026-10-19.

### t8 · Seed Delivery Command · Weekly metric

Body:
Read: get_objects for \`OBJ_dcmd_weekly_metric\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/weekly_metric.csv\`; get_records on \`OBJ_dcmd_weekly_metric\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/weekly_metric.csv\` is stored in \`OBJ_dcmd_weekly_metric\`, one record per row, nothing made up: the 1 row of studio/data/seed/weekly_metric.csv.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_weekly_metric\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_weekly_metric\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/weekly_metric.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_weekly_metric","records":["1792368000000"]}
Read back: OBJ_dcmd_weekly_metric: get_records total 1 (CSV has 1 row); was 0 before the write
Read back: OBJ_dcmd_weekly_metric 1792368000000 as stored: week_start 1792368000000 (2026-10-19), active_projects 18, active_projects_prev 17, golives_this_month 1, golives_this_month_prev 1, projects_at_risk 6, projects_at_risk_prev 5, avg_days_to_golive 59.8, avg_days_to_golive_prev 57.1, utilisation_pct 72, utilisation_pct_prev 70, value_awaiting_q4_usd 4468380, value_awaiting_q4_usd_prev_week 4878380, value_awaiting_q4_usd_last_month 5502380, bridge_new_usd 184800, bridge_completed_usd 658800, bridge_slipped_usd 410000, bridge_cancelled_usd 150000
Note: Written with apply_record_edits.

### t9 · Seed Delivery Command · AI output

Body:
Read: get_objects for \`OBJ_dcmd_ai_output\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/ai_output.csv\`; get_records on \`OBJ_dcmd_ai_output\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/ai_output.csv\` is stored in \`OBJ_dcmd_ai_output\`, one record per row, nothing made up: the 7 rows of studio/data/seed/ai_output.csv, every row ai_written true.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_ai_output\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_ai_output\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/ai_output.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_ai_output","records":["AIO-01","AIO-02","AIO-03","AIO-04","AIO-05","AIO-06","AIO-07"]}
Read back: OBJ_dcmd_ai_output: get_records total 7 (CSV has 7 rows); was 0 before the write
Read back: OBJ_dcmd_ai_output AIO-01 as stored: kind risk_flag, project_id IMP-2611, title Likely to miss go-live on 19 Nov 2026, confidence high, status open, ai_written true, created_at 1792624500000 (2026-10-22T08:15+09:00), evidence text verbatim
Unverified: OBJ_dcmd_ai_output: ai_written true was sent explicitly on all 7 rows but only AIO-01 was read back; get_records with filter ai_written EQUAL true would show 7
Note: Empty confidence/evidence/transcript_ref cells left unset. Written with apply_record_edits.

### t10 · Seed Delivery Command · Role permission

Body:
Read: get_objects for \`OBJ_dcmd_role_permission\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/role_permission.csv\`; get_records on \`OBJ_dcmd_role_permission\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/role_permission.csv\` is stored in \`OBJ_dcmd_role_permission\`, one record per row, nothing made up: the 6 rows of studio/data/seed/role_permission.csv.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_role_permission\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_role_permission\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/role_permission.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_role_permission","records":["Delivery director","Implementation lead","Consultant","Resource manager","Finance partner","Customer sponsor"]}
Read back: OBJ_dcmd_role_permission: get_records total 6 (CSV has 6 rows); was 0 before the write
Read back: OBJ_dcmd_role_permission Delivery director as stored: view_portfolio true, edit_project true, move_tasks true, book_consultants true, approve_timesheets true, raise_change true, approve_change true, view_internal_health true, sign_off_deliverables false, admin true
Note: role is a plain string primary key (no picklist), so role names stored verbatim and are the record ids. Written with apply_record_edits.

