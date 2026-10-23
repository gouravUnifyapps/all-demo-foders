---
nebula: 3
specId: "e_6adb9f245236864dd8e5ee6d"
mode: "sonic"
title: "ClickUp Delivery Command · plan 3 of 10"
owner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"Delivery Command · Executive email"},{"kind":"object","name":"Delivery Command · Project","id":"OBJ_dcmd_project"},{"kind":"object","name":"Delivery Command · Task","id":"OBJ_dcmd_task"},{"kind":"object","name":"Delivery Command · RAID item","id":"OBJ_dcmd_raid"},{"kind":"object","name":"Delivery Command · Person","id":"OBJ_dcmd_person"},{"kind":"object","name":"Delivery Command · Booking","id":"OBJ_dcmd_booking"},{"kind":"object","name":"Delivery Command · Time entry","id":"OBJ_dcmd_time_entry"},{"kind":"object","name":"Delivery Command · Change request","id":"OBJ_dcmd_change_request"},{"kind":"object","name":"Delivery Command · Activity","id":"OBJ_dcmd_activity"},{"kind":"object","name":"Delivery Command · Document","id":"OBJ_dcmd_document"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "8734f8ae-19ce-4703-acb9-5911f2f771f8"
pageDesign: 2
createdAt: "2026-10-23T17:53:42.628Z"
runningAt: "2026-10-23T17:53:46.131Z"
runner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"382b1b0f-8b04-5591-805d-15b67bc592e7"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · plan 3 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | Delivery Command · Executive email |  | done | 1 |
| t2 | record | Delivery Command · Project |  | done | 1 |
| t3 | record | Delivery Command · Task |  | done | 1 |
| t4 | record | Delivery Command · RAID item |  | done | 1 |
| t5 | record | Delivery Command · Person |  | done | 1 |
| t6 | record | Delivery Command · Booking |  | done | 1 |
| t7 | record | Delivery Command · Time entry |  | done | 1 |
| t8 | record | Delivery Command · Change request |  | done | 1 |
| t9 | record | Delivery Command · Activity |  | done | 1 |
| t10 | record | Delivery Command · Document |  | done | 1 |

### t1 · Create object Delivery Command · Executive email

Body:
Read: \`entity context object --name "Delivery Command · Executive email" --json\`, then get_objects for \`OBJ_dcmd_exec_email\`; if \`OBJ_dcmd_exec_email\` or the name Delivery Command · Executive email already exists, stop and report.
Done when: object Delivery Command · Executive email (\`OBJ_dcmd_exec_email\`), described "One composed weekly executive email, sent or kept as a preview.", holds every field the body lists, exactly: email_id text unique (EML-nnn), region picklist (as Project), send_at datetime epoch ms, recipient text, subject text, html long text, status picklist (sent "Sent", preview "Preview", failed "Failed"), error text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_exec_email\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_exec_email\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_exec_email"}
Read back: OBJ_dcmd_exec_email: get_objects name "Delivery Command · Executive email", fields email_id, region, send_at, recipient, subject, html, status, error; required ["email_id"]; unmirroredFields []
Read back: OBJ_dcmd_exec_email: email_id {type: string, primaryKey: true, uniqueKey: true, help: "EML-nnn"}
Read back: OBJ_dcmd_exec_email: region single-select codes [north_america, europe, japan] (same as OBJ_dcmd_project.region)
Read back: OBJ_dcmd_exec_email: send_at {type: integer, format: date-time, dateFormat: epoch}; recipient string; subject string (nameField); html {type: string, format: textarea}; error string
Read back: OBJ_dcmd_exec_email: status single-select codes [sent "Sent", preview "Preview", failed "Failed"]
Read back: OBJ_dcmd_exec_email: indexes [] (the spec line names no index)
Read back: Security: object created with the platform permission filter left on; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_exec_email description: the create step sent "One composed weekly executive email, sent or kept as a preview."; the read-back parts asked for do not show the description. Check: get_objects parts ['definition'].
Note: Pre-check: search 'Executive email' returned 0 rows and get_objects listed OBJ_dcmd_exec_email under missing before the create.
Note: Design: email_id is the natural key (primaryKey + uniqueKey, in required); subject is the display name; no index created because the spec names no access pattern for one; no lookup fields, so no foreignKey targets needed.

### t2 · Seed Delivery Command · Project

Body:
Read: get_objects for \`OBJ_dcmd_project\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/project.csv\`; get_records on \`OBJ_dcmd_project\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/project.csv\` is stored in \`OBJ_dcmd_project\`, one record per row, nothing made up: the 19 rows of studio/data/seed/project.csv (story row IMP-2611 Sakura Mobility, Japan, Data migration, go-live 19 Nov 2026, baseline 12 Nov 2026, At risk, lead Mei Takahashi, 1,200 seats, JPY 84,000,000, 860 h planned, 545 h used, sponsor Hana Mori; IMP-2590 Pellworth Labs is Cancelled).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_project\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_project\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/project.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_project","records":["IMP-2611","IMP-2633","IMP-2629","IMP-2640","IMP-2646","IMP-2598","IMP-2607","IMP-2622","IMP-2631","IMP-2637","IMP-2644","IMP-2604","IMP-2615","IMP-2620","IMP-2626","IMP-2635","IMP-2642","IMP-2590","IMP-2601"]}
Read back: OBJ_dcmd_project: get_records total 19, equal to the 19 data rows of studio/data/seed/project.csv
Read back: OBJ_dcmd_project: first file row stored as IMP-2611: customer "Sakura Mobility", region japan, stage data_migration, stage_index 4, go_live 1795046400000 (2026-11-19), baseline_go_live 1794441600000 (2026-11-12), slipped true, health at_risk, lead "Mei Takahashi", seats 1200, contract_value 84000000, currency JPY, budget_hours 860, used_hours 545, lifecycle active, sponsor "Hana Mori", portal_language ja, last_synced_at 1792744800000
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.
Note: IMP-2590 Pellworth Labs stored lifecycle cancelled; its empty health cell is left unset.
Note: feedback:
Bug: Seed-record task bodies say to write with save_entity_records, which writes platform stored types, not a storage object's rows.
Context: plan e_6adb9f27925d282255ba6215 record seed tasks t2-t10 on OBJ_dcmd_* objects.
Where: nebula
Evidence: Body says 'Apply the writes with save_entity_records'; object-storage-manager says storage rows go through apply_record_edits. Used apply_record_edits; totals matched.
Cause: Suspected: the plan's record-task template names the wrong writer tool.
Regression: Generate a record seed task for a MONGO object and check it names apply_record_edits.

### t3 · Seed Delivery Command · Task

Body:
Read: get_objects for \`OBJ_dcmd_task\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/task.csv\`; get_records on \`OBJ_dcmd_task\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/task.csv\` is stored in \`OBJ_dcmd_task\`, one record per row, nothing made up: the 96 rows of studio/data/seed/task.csv (45 on IMP-2611; 17 in its Data migration column; critical path TSK-5024 to TSK-5044; TSK-5024 and TSK-5025 past their end date).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_task\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_task\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/task.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_task","records":["TSK-5001..TSK-5096 (96 ids)"]}
Read back: OBJ_dcmd_task: get_records total 96, equal to the 96 data rows of studio/data/seed/task.csv
Read back: OBJ_dcmd_task: first file row stored as TSK-5001: project_id IMP-2611, title "Kickoff meeting with Sakura sponsors", stage kickoff, status done, assignee "Mei Takahashi", start 1783296000000, end 1783641600000, critical false, hours_planned 24, hours_logged 24, ai_proposed false
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

### t4 · Seed Delivery Command · RAID item

Body:
Read: get_objects for \`OBJ_dcmd_raid\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/raid.csv\`; get_records on \`OBJ_dcmd_raid\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/raid.csv\` is stored in \`OBJ_dcmd_raid\`, one record per row, nothing made up: the 17 rows of studio/data/seed/raid.csv (RSK-1183 likelihood 4, impact 5).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_raid\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_raid\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/raid.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_raid","records":["RSK-1183","RSK-1184","RSK-1185","RSK-1186","ASM-0311","ISS-0207","DEC-0098","RSK-1171","RSK-1172","RSK-1160","RSK-1161","RSK-1165","RSK-1168","RSK-1169","RSK-1173","RSK-1174","RSK-1175"]}
Read back: OBJ_dcmd_raid: get_records total 17, equal to the 17 data rows of studio/data/seed/raid.csv
Read back: OBJ_dcmd_raid: first file row stored as RSK-1183: project_id IMP-2611, type risk, owner "Aiko Tanaka", due 1793318400000, status open, likelihood 4, impact 5
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

### t5 · Seed Delivery Command · Person

Body:
Read: get_objects for \`OBJ_dcmd_person\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/person.csv\`; get_records on \`OBJ_dcmd_person\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/person.csv\` is stored in \`OBJ_dcmd_person\`, one record per row, nothing made up: the 18 rows of studio/data/seed/person.csv (13 consultants and leads, Elena Brooks delivery director, Tomás Herrera finance partner, Grace Liu resource manager, sponsors Hana Mori and Owen Price).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_person\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_person\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/person.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_person","records":["PER-101..PER-118 (18 ids)"]}
Read back: OBJ_dcmd_person: get_records total 18, equal to the 18 data rows of studio/data/seed/person.csv
Read back: OBJ_dcmd_person: first file row stored as PER-101: name "Mei Takahashi", role lead, region japan, capacity_hours 40, skill_data_migration 3, skill_japanese 4, time_zone Asia/Tokyo, week_start monday
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

### t6 · Seed Delivery Command · Booking

Body:
Read: get_objects for \`OBJ_dcmd_booking\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/booking.csv\`; get_records on \`OBJ_dcmd_booking\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/booking.csv\` is stored in \`OBJ_dcmd_booking\`, one record per row, nothing made up: the 168 rows of studio/data/seed/booking.csv (12 weeks from 26 Oct 2026; Haruto Sato 44 h in week of 2 Nov; Aiko Tanaka 30 h in week of 16 Nov and 20 h in week of 23 Nov; Marcus Bell none).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_booking\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_booking\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/booking.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_booking","records":["BKG-0001..BKG-0168 (168 ids)"]}
Read back: OBJ_dcmd_booking: get_records total 168, equal to the 168 data rows of studio/data/seed/booking.csv
Read back: OBJ_dcmd_booking: first file row stored as BKG-0001: person "Mei Takahashi", project_id IMP-2646, week_start 1792972800000 (2026-10-26), hours 36
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

### t7 · Seed Delivery Command · Time entry

Body:
Read: get_objects for \`OBJ_dcmd_time_entry\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/time_entry.csv\`; get_records on \`OBJ_dcmd_time_entry\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/time_entry.csv\` is stored in \`OBJ_dcmd_time_entry\`, one record per row, nothing made up: the 63 rows of studio/data/seed/time_entry.csv (week of 19 Oct Pending approval for 9 people; week of 12 Oct Approved).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_time_entry\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_time_entry\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/time_entry.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_time_entry","records":["TME-0001..TME-0063 (63 ids)"]}
Read back: OBJ_dcmd_time_entry: get_records total 63, equal to the 63 data rows of studio/data/seed/time_entry.csv
Read back: OBJ_dcmd_time_entry: first file row stored as TME-0001: person "Mei Takahashi", task_id TSK-5049, project_id IMP-2629, date 1791763200000, hours 7, timesheet_week 1791763200000, timesheet_status approved
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.
Note: Week of 19 Oct rows store timesheet_status submitted (label "Pending approval").

### t8 · Seed Delivery Command · Change request

Body:
Read: get_objects for \`OBJ_dcmd_change_request\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/change_request.csv\`; get_records on \`OBJ_dcmd_change_request\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/change_request.csv\` is stored in \`OBJ_dcmd_change_request\`, one record per row, nothing made up: the 2 rows of studio/data/seed/change_request.csv (CR-0452 approved by the director alone; CR-0449 rejected by the finance partner with a reason).
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_change_request\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_change_request\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/change_request.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_change_request","records":["CR-0452","CR-0449"]}
Read back: OBJ_dcmd_change_request: get_records total 2, equal to the 2 data rows of studio/data/seed/change_request.csv
Read back: OBJ_dcmd_change_request: first file row stored as CR-0452: project_id IMP-2633, raised_by "Kenji Arakawa", hours_delta 16, cost_delta 480000, currency JPY, route director, step1_status approved, step1_by "Elena Brooks", step1_at 1791990000000, step2_status not_needed, status approved
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

### t9 · Seed Delivery Command · Activity

Body:
Read: get_objects for \`OBJ_dcmd_activity\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/activity.csv\`; get_records on \`OBJ_dcmd_activity\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/activity.csv\` is stored in \`OBJ_dcmd_activity\`, one record per row, nothing made up: the 20 rows of studio/data/seed/activity.csv.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_activity\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_activity\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/activity.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_activity","records":["ACT-0001..ACT-0020 (20 ids)"]}
Read back: OBJ_dcmd_activity: get_records total 20, equal to the 20 data rows of studio/data/seed/activity.csv
Read back: OBJ_dcmd_activity: first file row stored as ACT-0001: at 1792368720000, actor "Aiko Tanaka", project_id IMP-2611, action task_moved, target TSK-5026, source app
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

### t10 · Seed Delivery Command · Document

Body:
Read: get_objects for \`OBJ_dcmd_document\` (its fields and picklist codes) and the file \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/document.csv\`; get_records on \`OBJ_dcmd_document\` must answer no rows yet, else stop and report what is there.
Done when: every row of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/document.csv\` is stored in \`OBJ_dcmd_document\`, one record per row, nothing made up: the 6 rows of studio/data/seed/document.csv, each with a short fictional body; file_url stays empty.
Values: a picklist stores its code; where the file holds the label (region "Japan", stage "Data migration", "Delivery director"), store the code whose label matches; a date-only value (2026-11-19) is epoch ms at 00:00 UTC that day; a datetime with an offset is its exact epoch ms; \`true\`/\`false\` are booleans; numbers are numbers; an empty cell is left unset; text and JSON text are kept verbatim.
Apply the writes with save_entity_records, in batches, then read back.
Read back: get_records on \`OBJ_dcmd_document\` with its total equal to the file's row count, and the first row of the file quoted as stored.
Report ids, readBack, unverified, notes.

Proof: get_records on \`OBJ_dcmd_document\` answers a total equal to the rows of \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/data/seed/document.csv\` and the first row as stored.
Result IDs: {"entity":"OBJ_dcmd_document","records":["DOC-10","DOC-12","DOC-13","DOC-14","DOC-15","DOC-20"]}
Read back: OBJ_dcmd_document: get_records total 6, equal to the 6 data rows of studio/data/seed/document.csv
Read back: OBJ_dcmd_document: first file row stored as DOC-10: project_id IMP-2611, title "Statement of work · Sakura Mobility", kind sow, shared_with_customer true, source "Google Drive", uploaded_by "Mei Takahashi", at 1783036800000, body kept verbatim, file_url unset
Note: Writer: apply_record_edits (the storage-object row writer) rather than save_entity_records, which is for platform stored types.
Note: Pre-check: get_records total 0 before the write.
Note: Values: picklist labels mapped to codes, date-only cells to epoch ms 00:00 UTC, offset datetimes to exact epoch ms, empty cells left unset.

