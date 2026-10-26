---
nebula: 3
specId: "e_6adf42d4dc07493166cdc011"
mode: "sonic"
title: "ClickUp Delivery Command · build 1 of 9: objects, part 1"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"ClickUp Command · Project"},{"kind":"object","name":"ClickUp Command · Task"},{"kind":"object","name":"ClickUp Command · RAID item"},{"kind":"object","name":"ClickUp Command · Change request"},{"kind":"object","name":"ClickUp Command · Person"},{"kind":"object","name":"ClickUp Command · Booking"},{"kind":"object","name":"ClickUp Command · Time entry"},{"kind":"object","name":"ClickUp Command · Deliverable"},{"kind":"object","name":"ClickUp Command · Session slot"},{"kind":"object","name":"ClickUp Command · Document"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "223eb4bd-1def-4b09-95b1-b194cd999926"
pageDesign: 2
createdAt: "2026-10-26T12:08:54.787Z"
runningAt: "2026-10-26T12:08:58.711Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · build 1 of 9: objects, part 1

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | ClickUp Command · Project |  | done | 1 |
| t2 | object | ClickUp Command · Task |  | done | 1 |
| t3 | object | ClickUp Command · RAID item |  | done | 1 |
| t4 | object | ClickUp Command · Change request |  | done | 1 |
| t5 | object | ClickUp Command · Person |  | done | 1 |
| t6 | object | ClickUp Command · Booking |  | done | 1 |
| t7 | object | ClickUp Command · Time entry |  | done | 1 |
| t8 | object | ClickUp Command · Deliverable |  | done | 1 |
| t9 | object | ClickUp Command · Session slot |  | done | 1 |
| t10 | object | ClickUp Command · Document |  | done | 1 |

### t1 · Create object ClickUp Command · Project

Body:
Read: \`entity context object --name "ClickUp Command · Project" --json\`, then \`get_objects\` on \`OBJ_cucmd_project\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Project exists with id \`OBJ_cucmd_project\` (One customer implementation, from signed contract to Hypercare; the story row is IMP-2611.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_project\`; fields project_code (text, primaryKey, required, e.g. \`IMP-2611\`), customer (text, required), industry (text), region (picklist: europe "Europe", north_america "North America", japan "Japan"), stage (picklist: kickoff "Kickoff", discovery "Discovery", configuration "Configuration", migration "Migration", training "Training", go_live "Go-live", hypercare "Hypercare"), go_live_date (date, epoch ms), original_go_live_date (date, epoch ms; set only when the date slipped), health (picklist: on_track "On track", at_risk "At risk", off_track "Off track"), health_last_week (same codes as health), lead (text), sponsor (text), seats (number), contract_value (number), currency (picklist: usd "USD", eur "EUR", jpy "JPY"), budget_hours_planned (number), budget_hours_used (number), column_limit (number, default 15), next_signoff (text), next_signoff_due (date, epoch ms), timezone (text, IANA name)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_project\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_project\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_project"}
Read back: OBJ_cucmd_project (ClickUp Command · Project): get_objects fields: project_code string primaryKey; customer string; industry string; region string/single-select {europe,north_america,japan}; stage string/single-select {kickoff,discovery,configuration,migration,training,go_live,hypercare}; go_live_date integer/date; original_go_live_date integer/date; health string/single-select {on_track,at_risk,off_track}; health_last_week string/single-select {on_track,at_risk,off_track}; lead string; sponsor string; seats number; contract_value number; currency string/single-select {usd,eur,jpy}; budget_hours_planned number; budget_hours_used number; column_limit number default 15; next_signoff string; next_signoff_due integer/date; timezone string
Read back: OBJ_cucmd_project: required ['project_code', 'customer']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_project: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t2 · Create object ClickUp Command · Task

Body:
Read: \`entity context object --name "ClickUp Command · Task" --json\`, then \`get_objects\` on \`OBJ_cucmd_task\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Task exists with id \`OBJ_cucmd_task\` (One task in a project plan, with stage, dates, dependencies and the critical path.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_task\`; fields task_code (text, primaryKey, required), project_code (text, required), title (text, required), description (text), stage (the seven Project stage codes), status (picklist: not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee (text), start_date (date, epoch ms), end_date (date, epoch ms), depends_on (text, comma-separated task_codes, finish-to-start), critical (boolean), hours_logged (number), comments_json (text), attachments_json (text), source (picklist: manual "Manual", copilot "Copilot")
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_task\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_task\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_task"}
Read back: OBJ_cucmd_task (ClickUp Command · Task): get_objects fields: task_code string primaryKey; project_code string; title string; description string; stage string/single-select {kickoff,discovery,configuration,migration,training,go_live,hypercare}; status string/single-select {not_started,in_progress,blocked,done}; assignee string; start_date integer/date; end_date integer/date; depends_on string; critical boolean; hours_logged number; comments_json string; attachments_json string; source string/single-select {manual,copilot}
Read back: OBJ_cucmd_task: required ['task_code', 'project_code', 'title']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_task: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t3 · Create object ClickUp Command · RAID item

Body:
Read: \`entity context object --name "ClickUp Command · RAID item" --json\`, then \`get_objects\` on \`OBJ_cucmd_raid\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · RAID item exists with id \`OBJ_cucmd_raid\` (One risk, assumption, issue or decision on a project, with likelihood and impact.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_raid\`; fields raid_code (text, primaryKey, required, e.g. \`RSK-1183\`), project_code (text, required), kind (picklist: risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title (text, required), owner (text), due_date (date, epoch ms), status (picklist: open "Open", mitigating "Mitigating", closed "Closed"), likelihood (number 1 to 5), impact (number 1 to 5), history_json (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_raid\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_raid\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_raid"}
Read back: OBJ_cucmd_raid (ClickUp Command · RAID item): get_objects fields: raid_code string primaryKey; project_code string; kind string/single-select {risk,assumption,issue,decision}; title string; owner string; due_date integer/date; status string/single-select {open,mitigating,closed}; likelihood number; impact number; history_json string
Read back: OBJ_cucmd_raid: required ['raid_code', 'project_code', 'title']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_raid: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t4 · Create object ClickUp Command · Change request

Body:
Read: \`entity context object --name "ClickUp Command · Change request" --json\`, then \`get_objects\` on \`OBJ_cucmd_change_request\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Change request exists with id \`OBJ_cucmd_change_request\` (One proposed change to a project, with its rule-routed approval steps.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_change_request\`; fields cr_code (text, primaryKey, required, e.g. \`CR-0457\`), project_code (text, required), reason (text, required), work_added (text), work_removed (text), hours_delta (number), cost_delta (number), go_live_delta_days (number), before_json (text), after_json (text), route_json (text: the ordered approver steps with role, name, decision, at, reason), next_approver (picklist: delivery_director "Delivery director", finance_partner "Finance partner", none "None"), status (picklist: draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), raised_by (text), raised_at (date, epoch ms), rejection_reason (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_change_request\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_change_request\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_change_request"}
Read back: OBJ_cucmd_change_request (ClickUp Command · Change request): get_objects fields: cr_code string primaryKey; project_code string; reason string; work_added string; work_removed string; hours_delta number; cost_delta number; go_live_delta_days number; before_json string; after_json string; route_json string; next_approver string/single-select {delivery_director,finance_partner,none}; status string/single-select {draft,pending_approval,approved,rejected}; raised_by string; raised_at integer/date; rejection_reason string
Read back: OBJ_cucmd_change_request: required ['cr_code', 'project_code', 'reason']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_change_request: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t5 · Create object ClickUp Command · Person

Body:
Read: \`entity context object --name "ClickUp Command · Person" --json\`, then \`get_objects\` on \`OBJ_cucmd_person\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Person exists with id \`OBJ_cucmd_person\` (One internal user or customer sponsor, with region, capacity and skill levels.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_person\`; fields person_code (text, primaryKey, required), name (text, required), role (picklist: implementation_lead "Implementation lead", consultant "Implementation consultant", delivery_director "Delivery director", finance_partner "Finance partner", resource_manager "Resource manager", customer_sponsor "Customer sponsor"), region (Project region codes), email (text, fictional \`@example.com\`), capacity_hours (number, default 40), skill_data_migration (number 0 to 4), skill_integrations (number 0 to 4), skill_admin_training (number 0 to 4), skill_api (number 0 to 4), skill_japanese (number 0 to 4), project_code (text; a sponsor's own project), language (picklist: en "English", de "German", ja "Japanese")
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_person\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_person\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_person"}
Read back: OBJ_cucmd_person (ClickUp Command · Person): get_objects fields: person_code string primaryKey; name string; role string/single-select {implementation_lead,consultant,delivery_director,finance_partner,resource_manager,customer_sponsor}; region string/single-select {europe,north_america,japan}; email string; capacity_hours number default 40; skill_data_migration number; skill_integrations number; skill_admin_training number; skill_api number; skill_japanese number; project_code string; language string/single-select {en,de,ja}
Read back: OBJ_cucmd_person: required ['person_code', 'name']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_person: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t6 · Create object ClickUp Command · Booking

Body:
Read: \`entity context object --name "ClickUp Command · Booking" --json\`, then \`get_objects\` on \`OBJ_cucmd_booking\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Booking exists with id \`OBJ_cucmd_booking\` (Hours one person is booked on one project for a run of weeks.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_booking\`; fields booking_code (text, primaryKey, required), person_code (text, required), project_code (text, required), first_week (date, epoch ms, the Monday), weeks (number), hours_per_week (number), over_capacity (boolean)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_booking\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_booking\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_booking"}
Read back: OBJ_cucmd_booking (ClickUp Command · Booking): get_objects fields: booking_code string primaryKey; person_code string; project_code string; first_week integer/date; weeks number; hours_per_week number; over_capacity boolean
Read back: OBJ_cucmd_booking: required ['booking_code', 'person_code', 'project_code']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_booking: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t7 · Create object ClickUp Command · Time entry

Body:
Read: \`entity context object --name "ClickUp Command · Time entry" --json\`, then \`get_objects\` on \`OBJ_cucmd_time_entry\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Time entry exists with id \`OBJ_cucmd_time_entry\` (Hours one person logged on one task on one day, inside a weekly timesheet.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_time_entry\`; fields entry_code (text, primaryKey, required), person_code (text, required), task_code (text, required), project_code (text), work_date (date, epoch ms), hours (number), week_start (date, epoch ms), timesheet_status (picklist: draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_time_entry\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_time_entry\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_time_entry"}
Read back: OBJ_cucmd_time_entry (ClickUp Command · Time entry): get_objects fields: entry_code string primaryKey; person_code string; task_code string; project_code string; work_date integer/date; hours number; week_start integer/date; timesheet_status string/single-select {draft,submitted,approved,returned}; return_reason string
Read back: OBJ_cucmd_time_entry: required ['entry_code', 'person_code', 'task_code']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_time_entry: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t8 · Create object ClickUp Command · Deliverable

Body:
Read: \`entity context object --name "ClickUp Command · Deliverable" --json\`, then \`get_objects\` on \`OBJ_cucmd_deliverable\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Deliverable exists with id \`OBJ_cucmd_deliverable\` (One stage deliverable awaiting or carrying the sponsor sign-off.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_deliverable\`; fields deliverable_code (text, primaryKey, required), project_code (text, required), stage (Project stage codes), title (text), title_ja (text), title_de (text), due_date (date, epoch ms), status (picklist: awaiting_signoff "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), decided_by (text), decided_at (date, epoch ms), comment (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_deliverable\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_deliverable\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_deliverable"}
Read back: OBJ_cucmd_deliverable (ClickUp Command · Deliverable): get_objects fields: deliverable_code string primaryKey; project_code string; stage string/single-select {kickoff,discovery,configuration,migration,training,go_live,hypercare}; title string; title_ja string; title_de string; due_date integer/date; status string/single-select {awaiting_signoff,signed_off,changes_requested}; decided_by string; decided_at integer/date; comment string
Read back: OBJ_cucmd_deliverable: required ['deliverable_code', 'project_code']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_deliverable: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t9 · Create object ClickUp Command · Session slot

Body:
Read: \`entity context object --name "ClickUp Command · Session slot" --json\`, then \`get_objects\` on \`OBJ_cucmd_session_slot\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Session slot exists with id \`OBJ_cucmd_session_slot\` (One bookable customer training slot.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_session_slot\`; fields slot_code (text, primaryKey, required), project_code (text), topic (text), slot_start (date, epoch ms), duration_min (number), taken (boolean), booked_by (text)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_session_slot\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_session_slot\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_session_slot"}
Read back: OBJ_cucmd_session_slot (ClickUp Command · Session slot): get_objects fields: slot_code string primaryKey; project_code string; topic string; slot_start integer/date; duration_min number; taken boolean; booked_by string
Read back: OBJ_cucmd_session_slot: required ['slot_code']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_session_slot: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

### t10 · Create object ClickUp Command · Document

Body:
Read: \`entity context object --name "ClickUp Command · Document" --json\`, then \`get_objects\` on \`OBJ_cucmd_document\`: it must answer not found. If the object already exists, stop and report what it holds.
Done when: object ClickUp Command · Document exists with id \`OBJ_cucmd_document\` (One file in a project library, a published status report or a customer upload with its row errors.) and holds every field this line names, with the types, picklist codes and labels exactly as written: id \`OBJ_cucmd_document\`; fields doc_code (text, primaryKey, required), project_code (text, required), kind (picklist: sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", status_report "Status report", upload "Customer upload"), title (text), body (text, the content the in-app viewer shows), shared_with_customer (boolean), row_count (number), error_count (number), errors_json (text: the first errors with row, column and message), upload_status (picklist: checking "Checking", needs_fixing "Needs fixing", confirmed "Confirmed"), ai_written (boolean), edited_by (text), published_at (date, epoch ms)
The primaryKey field is also in required; every picklist stores its code, never its label; every date field is epoch ms. Field properties follow \`object-storage-manager\` § Object schema format. Turn on \`logging.captureReporting\` before any row is written. No lookups: links between objects are plain code fields.
Apply the write once with \`apply_object_batch\`.
Read back: \`get_objects\` on \`OBJ_cucmd_document\`, quoting every field the body lists with its type, the primaryKey and the picklist codes.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: \`get_objects\` on \`OBJ_cucmd_document\` lists every field the body lists with its type and picklist codes.
Result IDs: {"entity":"OBJ_cucmd_document"}
Read back: OBJ_cucmd_document (ClickUp Command · Document): get_objects fields: doc_code string primaryKey; project_code string; kind string/single-select {sow,migration_plan,signoff_record,status_report,upload}; title string; body string; shared_with_customer boolean; row_count number; error_count number; errors_json string; upload_status string/single-select {checking,needs_fixing,confirmed}; ai_written boolean; edited_by string; published_at integer/date
Read back: OBJ_cucmd_document: required ['doc_code', 'project_code']; unmirroredFields []; settings.logging.captureReporting true; store MONGO
Read back: OBJ_cucmd_document: secure-by-default rule 1 kept: no skipPermissionsFilter or external written; no lookups (plain code fields)
Unverified: Picklist option labels (titles) were sent as specified but not listed by the picklists read; check get_objects parts fieldDefinitions for the oneOf titles
Note: Pre-read: entity context by name answered miss and get_objects listed the id under missing, so the object was new.
Note: Design: created in one apply_object_batch with the other nine objects plus captureReporting step; natural primaryKey code field in required; nameField on the label field; dates integer/date epoch; numeric ranges (1-5, 0-4) noted in help only, no min/max constraint; no indexes added since no access pattern in the task asks for one.

