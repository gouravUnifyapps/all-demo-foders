---
nebula: 3
specId: "e_6adf438308f96579542edf62"
mode: "sonic"
title: "ClickUp Delivery Command · build 2 of 9: objects, part 2, and the first seeds"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"ClickUp Command · Activity"},{"kind":"object","name":"ClickUp Command · AI output"},{"kind":"object","name":"ClickUp Command · Weekly metric"},{"kind":"object","name":"ClickUp Command · Saved view"},{"kind":"object","name":"ClickUp Command · Checklist item"},{"kind":"object","name":"ClickUp Command · Integration"},{"kind":"object","name":"ClickUp Command · Notification"},{"kind":"object","name":"ClickUp Command · Project","id":"OBJ_cucmd_project"},{"kind":"object","name":"ClickUp Command · Task","id":"OBJ_cucmd_task"},{"kind":"object","name":"ClickUp Command · RAID item","id":"OBJ_cucmd_raid"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "75c9a353-99c6-48af-83dc-ded8bd7b8e78"
pageDesign: 2
createdAt: "2026-10-26T12:11:48.524Z"
runningAt: "2026-10-26T12:11:53.331Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
## Plan

Goal: ClickUp Delivery Command · build 2 of 9: objects, part 2, and the first seeds

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | ClickUp Command · Activity |  | running | 1 |
| t2 | object | ClickUp Command · AI output |  | running | 1 |
| t3 | object | ClickUp Command · Weekly metric |  | running | 1 |
| t4 | object | ClickUp Command · Saved view |  | running | 1 |
| t5 | object | ClickUp Command · Checklist item |  | running | 1 |
| t6 | object | ClickUp Command · Integration |  | running | 1 |
| t7 | object | ClickUp Command · Notification |  | running | 1 |
| t8 | record | ClickUp Command · Project |  | running | 1 |
| t9 | record | ClickUp Command · Task |  | running | 1 |
| t10 | record | ClickUp Command · RAID item |  | running | 1 |

### t1 · Create object ClickUp Command · Activity

Body:
Read: \`entity context object --name "ClickUp Command · Activity" --json\`, then \`get_objects\` on \`OBJ_cucmd_activity\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Activity exists with id \`OBJ_cucmd_activity\` (One change on a project: who did what and when; never edited; also the audit log.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_activity\`; fields activity_code (text, primaryKey, required), project_code (text), actor (text), action (picklist: created "Created", updated "Updated", moved "Moved", approved "Approved", rejected "Rejected", signed_off "Signed off", booked "Booked", published "Published", logged "Logged time"), summary (text), at (date, epoch ms); never updated after it is written
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_activity\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_activity\` lists every field the body lists with its type and picklist codes.

### t2 · Create object ClickUp Command · AI output

Body:
Read: \`entity context object --name "ClickUp Command · AI output" --json\`, then \`get_objects\` on \`OBJ_cucmd_ai_output\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · AI output exists with id \`OBJ_cucmd_ai_output\` (One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report draft.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_ai_output\`; fields output_code (text, primaryKey, required), project_code (text), kind (picklist: risk_flag "Risk flag", meeting_summary "Meeting summary", proposed_task "Proposed task", status_report "Status report draft"), title (text), body (text), confidence (number 0 to 100), evidence_json (text), transcript_refs_json (text), decision (picklist: proposed "Proposed", accepted "Accepted", rejected "Rejected"), ai_written (boolean, default true), created_at (date, epoch ms)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_ai_output\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_ai_output\` lists every field the body lists with its type and picklist codes.

### t3 · Create object ClickUp Command · Weekly metric

Body:
Read: \`entity context object --name "ClickUp Command · Weekly metric" --json\`, then \`get_objects\` on \`OBJ_cucmd_weekly_metric\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Weekly metric exists with id \`OBJ_cucmd_weekly_metric\` (The portfolio health counts, the six headline numbers and the value bridge for one week.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_weekly_metric\`; fields week_start (date, epoch ms, primaryKey, required), on_track (number), at_risk (number), off_track (number), active_projects (number), golives_this_month (number), avg_days_to_golive (number), utilisation_pct (number), value_awaiting_usd (number), bridge_new (number), bridge_golives (number), bridge_slipped (number), bridge_cancelled (number), top_movers_json (text), last_updated (date, epoch ms)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_weekly_metric\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_weekly_metric\` lists every field the body lists with its type and picklist codes.

### t4 · Create object ClickUp Command · Saved view

Body:
Read: \`entity context object --name "ClickUp Command · Saved view" --json\`, then \`get_objects\` on \`OBJ_cucmd_saved_view\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Saved view exists with id \`OBJ_cucmd_saved_view\` (One named, shareable set of portfolio filters.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_saved_view\`; fields view_code (text, primaryKey, required), name (text, required), filters_json (text), owner (text), shared_with (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_saved_view\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_saved_view\` lists every field the body lists with its type and picklist codes.

### t5 · Create object ClickUp Command · Checklist item

Body:
Read: \`entity context object --name "ClickUp Command · Checklist item" --json\`, then \`get_objects\` on \`OBJ_cucmd_checklist_item\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Checklist item exists with id \`OBJ_cucmd_checklist_item\` (One of the ten readiness questions with the customer answer, or none.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_checklist_item\`; fields item_code (text, primaryKey, required), project_code (text, required), position (number), question_en (text), question_de (text), question_ja (text), answer (text; empty means not set), answered_by (text), answered_at (date, epoch ms)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_checklist_item\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_checklist_item\` lists every field the body lists with its type and picklist codes.

### t6 · Create object ClickUp Command · Integration

Body:
Read: \`entity context object --name "ClickUp Command · Integration" --json\`, then \`get_objects\` on \`OBJ_cucmd_integration\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Integration exists with id \`OBJ_cucmd_integration\` (The sync status of one connected system.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_integration\`; fields system (picklist: salesforce "Salesforce", slack "Slack", google_drive "Google Drive", jira "Jira"; primaryKey, required), status (picklist: synced "Synced", sync_failed "Sync failed"), last_sync (date, epoch ms), failing_since (date, epoch ms), error (text), affects (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_integration\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_integration\` lists every field the body lists with its type and picklist codes.

### t7 · Create object ClickUp Command · Notification

Body:
Read: \`entity context object --name "ClickUp Command · Notification" --json\`, then \`get_objects\` on \`OBJ_cucmd_notification\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Notification exists with id \`OBJ_cucmd_notification\` (One assignment, sign-off or mention for a user.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_notification\`; fields notification_code (text, primaryKey, required), person_code (text, required), kind (picklist: assignment "New assignment", signoff "Sign-off", mention "Mention"), text (text), link (text), read (boolean), created_at (date, epoch ms)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_notification\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_notification\` lists every field the body lists with its type and picklist codes.

### t8 · Seed ClickUp Command · Project

Body:
Read: \`get_objects\` on \`OBJ_cucmd_project\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_project\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: IMP-2611 Sakura Mobility, Automotive, japan, go_live, go-live 2026-11-16, health at_risk, last week on_track, lead Kenji Arai, sponsor Haruto Mori, 9200 seats, 62400000 jpy, 1480 planned, 1236 used, column_limit 15, next sign-off "Cutover plan" due 2026-10-29, Asia/Tokyo; IMP-2604 Halden Freight, Logistics, europe, migration, 2026-12-07, on_track/on_track, Mira Lindqvist, 4800, 386000 eur, 1100/640, Europe/Oslo; IMP-2598 Corvia Health, Healthcare, north_america, configuration, 2027-01-18 (original 2026-12-14), off_track/at_risk, Dana Whitfield, sponsor Grace Lin, 12000, 910000 usd, 2400/1310, America/Chicago; IMP-2615 Brightmoor University, Education, europe, training, 2026-11-23, on_track/on_track, Mira Lindqvist, 2300, 142000 eur, 620/510, Europe/London; IMP-2621 Kestrel Energy, Energy, north_america, discovery, 2027-02-22, on_track/on_track, Sam Okafor, 7500, 540000 usd, 1650/210, America/Denver; IMP-2587 Ostrander Retail, Retail, north_america, hypercare, 2026-10-12, on_track/on_track, Dana Whitfield, 650, 48000 usd, 260/248, America/New_York; IMP-2618 Tsubame Insurance, Insurance, japan, migration, 2026-11-27, on_track/on_track, Kenji Arai, 3100, 21600000 jpy, 900/610, Asia/Tokyo; IMP-2609 Nordwerk Maschinenbau, Manufacturing, europe, go_live, 2026-11-09, at_risk/at_risk, Jonas Weber, 5600, 412000 eur, 1300/1190, Europe/Berlin; IMP-2624 Lumen Bank, Financial services, north_america, kickoff, 2027-03-15, on_track/on_track, Sam Okafor, 8800, 720000 usd, 1900/40, America/New_York; IMP-2602 Fjordline Media, Media, europe, configuration, 2026-12-14 (original 2026-11-30), at_risk/on_track, Jonas Weber, 1400, 96000 eur, 520/300, Europe/Oslo; IMP-2612 Hikari Foods, Food and beverage, japan, training, 2026-12-01, on_track/on_track, Aiko Tanaka, 2600, 18200000 jpy, 700/520, Asia/Tokyo; IMP-2595 Redwater Logistics, Logistics, north_america, go_live, 2026-11-02, on_track/on_track, Dana Whitfield, 3900, 260000 usd, 980/900, America/Chicago; IMP-2619 Alpenrose Hotels, Hospitality, europe, discovery, 2027-02-08, on_track/on_track, Mira Lindqvist, 1800, 118000 eur, 560/60, Europe/Vienna; IMP-2607 Meridian Pharma, Pharmaceuticals, north_america, migration, 2026-12-21 (original 2026-11-23), off_track/off_track, Sam Okafor, 6400, 480000 usd, 1500/1010, America/New_York; IMP-2626 Kawase Electronics, Electronics, japan, kickoff, 2027-03-01, on_track/on_track, Aiko Tanaka, 5200, 34800000 jpy, 1200/20, Asia/Tokyo; IMP-2600 Solberg Telecom, Telecommunications, europe, hypercare, 2026-10-05, on_track/on_track, Jonas Weber, 4100, 290000 eur, 940/930, Europe/Oslo; IMP-2613 Prairie State Credit Union, Financial services, north_america, training, 2026-11-30, at_risk/on_track, Dana Whitfield, 1200, 84000 usd, 410/330, America/Chicago; IMP-2622 Minato Travel Group, Travel, japan, configuration, 2027-01-11, on_track/on_track, Kenji Arai, 2000, 14000000 jpy, 640/220, Asia/Tokyo. Every date is epoch ms at UTC midnight.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_project\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_project\` returns every row the body names, quoted by primaryKey.

### t9 · Seed ClickUp Command · Task

Body:
Read: \`get_objects\` on \`OBJ_cucmd_task\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_task\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: twenty tasks of IMP-2611, codes T-2611-01 to T-2611-20: 01 Kickoff workshop (kickoff, done); 02 Discovery interviews (discovery, done); 03 Workspace design sign-off (discovery, done); 04 Configure spaces and statuses (configuration, done); 05 SSO configuration (configuration, done); 06 User list migration wave 1 (migration, done, 6 days late); 07 User list migration wave 2 (migration, in_progress, Yui Sato, 2026-10-19 to 2026-10-30, late 5 days, critical); 08 Data migration: projects (migration, in_progress, Yui Sato, critical, late 4 days); 09 Data migration: docs (migration, blocked, Daichi Ono, late 5 days); 10 Integration test Salesforce (migration, in_progress, Priya Raman); 11 Admin training (training, done); 12 End-user training Tokyo (training, done); 13 End-user training Osaka (training, in_progress); 14 SSO cutover rehearsal 1 (go_live, done, failed); 15 SSO cutover rehearsal 2 (go_live, in_progress, critical, 2026-10-26 to 2026-11-03); 16 Cutover plan sign-off (go_live, not_started, critical, depends on 15); 17 Go-live readiness review (go_live, not_started, critical, depends on 16); 18 Production cutover (go_live, not_started, critical, 2026-11-14 to 2026-11-16, depends on 17); 19 Hypercare rota (hypercare, not_started, depends on 18); 20 Hypercare exit review (hypercare, not_started, depends on 19). Stage go_live holds 5 tasks; the Board shows the column limit from column_limit.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_task\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_task\` returns every row the body names, quoted by primaryKey.

### t10 · Seed ClickUp Command · RAID item

Body:
Read: \`get_objects\` on \`OBJ_cucmd_raid\` for its fields and picklist codes, and \`get_records\` on \`OBJ_cucmd_raid\` (limit 50). If a field a row needs is missing, stop and report. A row whose primaryKey already exists is updated to the values below, never written twice.
Done when: every row this line names is stored, with picklist codes (never labels) and dates as epoch ms at UTC midnight unless a time is given: RSK-1183 IMP-2611 risk "SSO cutover rehearsal failed twice", owner Kenji Arai, due 2026-11-03, open, likelihood 4, impact 5; RSK-1184 IMP-2611 risk "User list upload has 214 of 50,000 rows failing", 4, 4, open; RSK-1185 IMP-2611 issue "Docs migration blocked on export limits", 3, 4, open; ASM-0311 IMP-2611 assumption "Sponsor team available for cutover weekend"; DEC-0208 IMP-2611 decision "Cutover rehearsal re-run on 3 Nov"; RSK-1170 IMP-2609 risk 4, 4; RSK-1171 IMP-2602 risk 3, 4; RSK-1172 IMP-2598 risk 5, 5; RSK-1173 IMP-2598 risk 4, 5; RSK-1174 IMP-2607 risk 5, 4; RSK-1175 IMP-2613 risk 3, 3; RSK-1176 IMP-2604 risk 2, 3; RSK-1177 IMP-2618 risk 2, 4; RSK-1178 IMP-2615 risk 1, 2; RSK-1179 IMP-2621 risk 2, 2; RSK-1180 IMP-2624 risk 1, 3; RSK-1181 IMP-2612 risk 2, 2; RSK-1182 IMP-2595 risk 3, 2; RSK-1186 IMP-2619 risk 1, 1; RSK-1187 IMP-2622 risk 2, 3. Every risk is open, with an owner from its project's lead and history_json holding its creation.
Values the line leaves to you (a description, a document body, history_json, the remaining rows of a count) are fictional, consistent with the rows named, in plain business words, and never more than 20 rows. Emails are fictional \`@example.com\`.
Write the rows with \`apply_record_edits\`, the primaryKey value as each record's key.
Read back: \`get_records\` on \`OBJ_cucmd_raid\`, quoting each row's primaryKey and, for the story rows (IMP-2611 and its rows), the values the line names.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_records\` on \`OBJ_cucmd_raid\` returns every row the body names, quoted by primaryKey.

