---
nebula: 3
specId: "e_6adb9616925d282255ab4167"
mode: "sonic"
title: "ClickUp Delivery Command · plan 1 of 10"
owner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"Delivery Command · Project"},{"kind":"object","name":"Delivery Command · Task"},{"kind":"object","name":"Delivery Command · RAID item"},{"kind":"object","name":"Delivery Command · Person"},{"kind":"object","name":"Delivery Command · Booking"},{"kind":"object","name":"Delivery Command · Time entry"},{"kind":"object","name":"Delivery Command · Change request"},{"kind":"object","name":"Delivery Command · Activity"},{"kind":"object","name":"Delivery Command · Document"},{"kind":"object","name":"Delivery Command · Session slot"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "04525b1e-227d-437b-98f4-607b65eea465"
pageDesign: 2
createdAt: "2026-10-23T17:15:04.359Z"
runningAt: "2026-10-23T17:15:08.454Z"
runner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"382b1b0f-8b04-5591-805d-15b67bc592e7"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · plan 1 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | Delivery Command · Project |  | done | 1 |
| t2 | object | Delivery Command · Task |  | done | 1 |
| t3 | object | Delivery Command · RAID item |  | done | 1 |
| t4 | object | Delivery Command · Person |  | done | 1 |
| t5 | object | Delivery Command · Booking |  | done | 1 |
| t6 | object | Delivery Command · Time entry |  | done | 1 |
| t7 | object | Delivery Command · Change request |  | done | 1 |
| t8 | object | Delivery Command · Activity |  | done | 1 |
| t9 | object | Delivery Command · Document |  | done | 1 |
| t10 | object | Delivery Command · Session slot |  | done | 1 |

### t1 · Create object Delivery Command · Project

Body:
Read: \`entity context object --name "Delivery Command · Project" --json\`, then get_objects for \`OBJ_dcmd_project\`; if \`OBJ_dcmd_project\` or the name Delivery Command · Project already exists, stop and report.
Done when: object Delivery Command · Project (\`OBJ_dcmd_project\`), described "One customer implementation, from signed contract to Hypercare.", holds every field the body lists, exactly: project_id text unique (IMP-nnnn), customer text, customer_initials text, region picklist (north_america "North America", europe "Europe", japan "Japan"), stage picklist (kickoff "Kickoff", discovery "Discovery", configuration "Configuration", data_migration "Data migration", integrations "Integrations", training "Training", hypercare "Hypercare"), stage_index number 1 to 7, go_live date epoch ms, baseline_go_live date epoch ms, slipped boolean, health picklist (on_track "On track", at_risk "At risk", off_track "Off track"), lead text, seats number, contract_value number, currency picklist (USD, EUR, JPY), budget_hours number, used_hours number, lifecycle picklist (active "Active", live "Live", cancelled "Cancelled"), sponsor text, portal_language picklist (en, de, ja), last_synced_at datetime epoch ms; index on region, health, lead.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_project\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_project\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_project"}
Read back: OBJ_dcmd_project (Delivery Command · Project): get_objects fields = project_id string (primaryKey, uniqueKey), customer string (nameField), customer_initials string, region single-select, stage single-select, stage_index number, go_live integer date epoch, baseline_go_live integer date epoch, slipped boolean, health single-select, lead string, seats number, contract_value number, currency single-select, budget_hours number, used_hours number, lifecycle single-select, sponsor string, portal_language single-select, last_synced_at integer date-time epoch
Read back: OBJ_dcmd_project: required ["project_id"]; fieldDefinitions project_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_project: picklists region [north_america, europe, japan]; stage [kickoff, discovery, configuration, data_migration, integrations, training, hypercare]; health [on_track, at_risk, off_track]; currency [USD, EUR, JPY]; lifecycle [active, live, cancelled]; portal_language [en, de, ja]
Read back: OBJ_dcmd_project: idx_region (region asc) SUCCESS; idx_health (health asc) SUCCESS; idx_lead (lead asc) SUCCESS
Read back: OBJ_dcmd_project: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_project: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_project: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.
Note: stage_index range 1 to 7 is a help hint only (no min/max enforced) — check: a record write with stage_index 9 is accepted.
Note: Picklists currency and portal_language were given codes only; their labels equal the codes.

### t2 · Create object Delivery Command · Task

Body:
Read: \`entity context object --name "Delivery Command · Task" --json\`, then get_objects for \`OBJ_dcmd_task\`; if \`OBJ_dcmd_task\` or the name Delivery Command · Task already exists, stop and report.
Done when: object Delivery Command · Task (\`OBJ_dcmd_task\`), described "One task in a project plan, with dates, dependencies and the critical path.", holds every field the body lists, exactly: task_id text unique (TSK-nnnn), project_id text, title text, description long text, stage picklist (the seven stage codes of Project), status picklist (not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee text, start date epoch ms, end date epoch ms, depends_on text (a task_id), critical boolean, hours_planned number, hours_logged number, ai_proposed boolean; index on project_id, assignee.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_task\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_task\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_task"}
Read back: OBJ_dcmd_task (Delivery Command · Task): get_objects fields = task_id string (primaryKey, uniqueKey), project_id string, title string (nameField), description string textarea, stage single-select, status single-select, assignee string, start integer date epoch, end integer date epoch, depends_on string, critical boolean, hours_planned number, hours_logged number, ai_proposed boolean
Read back: OBJ_dcmd_task: required ["task_id"]; fieldDefinitions task_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_task: picklists stage [kickoff, discovery, configuration, data_migration, integrations, training, hypercare]; status [not_started, in_progress, blocked, done]
Read back: OBJ_dcmd_task: idx_project_id (project_id asc) SUCCESS; idx_assignee (assignee asc) SUCCESS
Read back: OBJ_dcmd_task: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_task: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_task: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.

### t3 · Create object Delivery Command · RAID item

Body:
Read: \`entity context object --name "Delivery Command · RAID item" --json\`, then get_objects for \`OBJ_dcmd_raid\`; if \`OBJ_dcmd_raid\` or the name Delivery Command · RAID item already exists, stop and report.
Done when: object Delivery Command · RAID item (\`OBJ_dcmd_raid\`), described "One risk, assumption, issue or decision on a project.", holds every field the body lists, exactly: raid_id text unique (RSK-, ASM-, ISS-, DEC-nnnn), project_id text, type picklist (risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title text, owner text, due date epoch ms, status picklist (open "Open", mitigating "Mitigating", closed "Closed"), likelihood number 1 to 5, impact number 1 to 5, jira_key text, history long text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_raid\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_raid\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_raid"}
Read back: OBJ_dcmd_raid (Delivery Command · RAID item): get_objects fields = raid_id string (primaryKey, uniqueKey), project_id string, type single-select, title string (nameField), owner string, due integer date epoch, status single-select, likelihood number, impact number, jira_key string, history string textarea
Read back: OBJ_dcmd_raid: required ["raid_id"]; fieldDefinitions raid_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_raid: picklists type [risk, assumption, issue, decision]; status [open, mitigating, closed]
Read back: OBJ_dcmd_raid: indexes: [] (none named by the body)
Read back: OBJ_dcmd_raid: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_raid: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_raid: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.
Note: likelihood and impact range 1 to 5 is a help hint only, not enforced.

### t4 · Create object Delivery Command · Person

Body:
Read: \`entity context object --name "Delivery Command · Person" --json\`, then get_objects for \`OBJ_dcmd_person\`; if \`OBJ_dcmd_person\` or the name Delivery Command · Person already exists, stop and report.
Done when: object Delivery Command · Person (\`OBJ_dcmd_person\`), described "One internal user or customer sponsor, with capacity and skill levels.", holds every field the body lists, exactly: person_id text unique (PER-nnn), name text, role picklist (consultant "Consultant", lead "Implementation lead", director "Delivery director", resource_manager "Resource manager", finance_partner "Finance partner", sponsor "Customer sponsor"), region picklist (as Project), capacity_hours number, skill_data_migration number 0 to 4, skill_integrations number 0 to 4, skill_admin_training number 0 to 4, skill_api number 0 to 4, skill_japanese number 0 to 4, customer text, email text, time_zone text, week_start picklist (monday "Monday", sunday "Sunday").
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_person\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_person\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_person"}
Read back: OBJ_dcmd_person (Delivery Command · Person): get_objects fields = person_id string (primaryKey, uniqueKey), name string (nameField), role single-select, region single-select, capacity_hours number, skill_data_migration number, skill_integrations number, skill_admin_training number, skill_api number, skill_japanese number, customer string, email string, time_zone string, week_start single-select
Read back: OBJ_dcmd_person: required ["person_id"]; fieldDefinitions person_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_person: picklists role [consultant, lead, director, resource_manager, finance_partner, sponsor]; region [north_america, europe, japan]; week_start [monday, sunday]
Read back: OBJ_dcmd_person: indexes: [] (none named by the body)
Read back: OBJ_dcmd_person: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_person: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_person: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.
Note: skill_* range 0 to 4 is a help hint only, not enforced.

### t5 · Create object Delivery Command · Booking

Body:
Read: \`entity context object --name "Delivery Command · Booking" --json\`, then get_objects for \`OBJ_dcmd_booking\`; if \`OBJ_dcmd_booking\` or the name Delivery Command · Booking already exists, stop and report.
Done when: object Delivery Command · Booking (\`OBJ_dcmd_booking\`), described "Hours one person is booked on one project in one week.", holds every field the body lists, exactly: booking_id text unique (BKG-nnnn), person text, project_id text, week_start date epoch ms, hours number; index on person, week_start.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_booking\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_booking\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_booking"}
Read back: OBJ_dcmd_booking (Delivery Command · Booking): get_objects fields = booking_id string (primaryKey, uniqueKey, nameField), person string, project_id string, week_start integer date epoch, hours number
Read back: OBJ_dcmd_booking: required ["booking_id"]; fieldDefinitions booking_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_booking: picklists no picklists
Read back: OBJ_dcmd_booking: idx_person (person asc) SUCCESS; idx_week_start (week_start asc) SUCCESS
Read back: OBJ_dcmd_booking: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_booking: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_booking: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.

### t6 · Create object Delivery Command · Time entry

Body:
Read: \`entity context object --name "Delivery Command · Time entry" --json\`, then get_objects for \`OBJ_dcmd_time_entry\`; if \`OBJ_dcmd_time_entry\` or the name Delivery Command · Time entry already exists, stop and report.
Done when: object Delivery Command · Time entry (\`OBJ_dcmd_time_entry\`), described "Hours one person logged on one task on one day, inside a weekly timesheet.", holds every field the body lists, exactly: entry_id text unique (TME-nnnn), person text, task_id text, project_id text, date date epoch ms, hours number, timesheet_week date epoch ms, timesheet_status picklist (draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_time_entry\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_time_entry\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_time_entry"}
Read back: OBJ_dcmd_time_entry (Delivery Command · Time entry): get_objects fields = entry_id string (primaryKey, uniqueKey, nameField), person string, task_id string, project_id string, date integer date epoch, hours number, timesheet_week integer date epoch, timesheet_status single-select, return_reason string
Read back: OBJ_dcmd_time_entry: required ["entry_id"]; fieldDefinitions entry_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_time_entry: picklists timesheet_status [draft, submitted, approved, returned]
Read back: OBJ_dcmd_time_entry: indexes: [] (none named by the body)
Read back: OBJ_dcmd_time_entry: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_time_entry: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_time_entry: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.

### t7 · Create object Delivery Command · Change request

Body:
Read: \`entity context object --name "Delivery Command · Change request" --json\`, then get_objects for \`OBJ_dcmd_change_request\`; if \`OBJ_dcmd_change_request\` or the name Delivery Command · Change request already exists, stop and report.
Done when: object Delivery Command · Change request (\`OBJ_dcmd_change_request\`), described "One proposed change to a project, with its two-step approval route.", holds every field the body lists, exactly: cr_id text unique (CR-nnnn), project_id text, raised_by text, reason long text, work_added long text, work_removed long text, hours_delta number, cost_delta number, currency picklist (USD, EUR, JPY), golive_before date epoch ms, golive_after date epoch ms, plan_before long text (JSON task list), plan_after long text (JSON task list), route picklist (director "Delivery director", director_finance "Delivery director, then finance partner"), step1_status picklist (pending, approved, rejected), step1_by text, step1_at datetime epoch ms, step2_status picklist (not_needed, waiting, pending, approved, rejected), step2_by text, step2_at datetime epoch ms, next_approver text, status picklist (draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), reject_reason long text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_change_request\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_change_request\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_change_request"}
Read back: OBJ_dcmd_change_request (Delivery Command · Change request): get_objects fields = cr_id string (primaryKey, uniqueKey, nameField), project_id string, raised_by string, reason textarea, work_added textarea, work_removed textarea, hours_delta number, cost_delta number, currency single-select, golive_before integer date epoch, golive_after integer date epoch, plan_before textarea, plan_after textarea, route single-select, step1_status single-select, step1_by string, step1_at integer date-time epoch, step2_status single-select, step2_by string, step2_at integer date-time epoch, next_approver string, status single-select, reject_reason textarea
Read back: OBJ_dcmd_change_request: required ["cr_id"]; fieldDefinitions cr_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_change_request: picklists currency [USD, EUR, JPY]; route [director, director_finance]; step1_status [pending, approved, rejected]; step2_status [not_needed, waiting, pending, approved, rejected]; status [draft, pending_approval, approved, rejected]
Read back: OBJ_dcmd_change_request: indexes: [] (none named by the body)
Read back: OBJ_dcmd_change_request: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_change_request: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_change_request: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.
Note: step1_status, step2_status and currency were given codes only; labels were derived (Pending, Approved, Rejected, Not needed, Waiting; currency label = code).

### t8 · Create object Delivery Command · Activity

Body:
Read: \`entity context object --name "Delivery Command · Activity" --json\`, then get_objects for \`OBJ_dcmd_activity\`; if \`OBJ_dcmd_activity\` or the name Delivery Command · Activity already exists, stop and report.
Done when: object Delivery Command · Activity (\`OBJ_dcmd_activity\`), described "One change on a project: who did what and when; never edited.", holds every field the body lists, exactly: activity_id text unique (ACT-nnnn), at datetime epoch ms, actor text, project_id text, action text, target text, detail text, source picklist (app "Delivery Command", automation "Automation", ai "Delivery Copilot", salesforce "Salesforce"); rows are only ever created, never updated or deleted; index on project_id, actor, action.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_activity\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_activity\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_activity"}
Read back: OBJ_dcmd_activity (Delivery Command · Activity): get_objects fields = activity_id string (primaryKey, uniqueKey, nameField), at integer date-time epoch, actor string, project_id string, action string, target string, detail string, source single-select
Read back: OBJ_dcmd_activity: required ["activity_id"]; fieldDefinitions activity_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_activity: picklists source [app, automation, ai, salesforce]
Read back: OBJ_dcmd_activity: idx_project_id (project_id asc) SUCCESS; idx_actor (actor asc) SUCCESS; idx_action (action asc) SUCCESS
Read back: OBJ_dcmd_activity: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_activity: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_activity: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.
Note: Append-only (never updated or deleted) is not a store setting; it must be held by the automations and pages that write Activity rows.

### t9 · Create object Delivery Command · Document

Body:
Read: \`entity context object --name "Delivery Command · Document" --json\`, then get_objects for \`OBJ_dcmd_document\`; if \`OBJ_dcmd_document\` or the name Delivery Command · Document already exists, stop and report.
Done when: object Delivery Command · Document (\`OBJ_dcmd_document\`), described "One file in a project library: statement of work, migration plan or sign-off record.", holds every field the body lists, exactly: document_id text unique (DOC-nn), project_id text, title text, body long text (the document's text, shown in the in-app viewer), kind picklist (sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", other "Other"), file_url text, shared_with_customer boolean, source text, uploaded_by text, at date epoch ms.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_document\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_document\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_document"}
Read back: OBJ_dcmd_document (Delivery Command · Document): get_objects fields = document_id string (primaryKey, uniqueKey), project_id string, title string (nameField), body string textarea, kind single-select, file_url string, shared_with_customer boolean, source string, uploaded_by string, at integer date epoch
Read back: OBJ_dcmd_document: required ["document_id"]; fieldDefinitions document_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_document: picklists kind [sow, migration_plan, signoff_record, other]
Read back: OBJ_dcmd_document: indexes: [] (none named by the body)
Read back: OBJ_dcmd_document: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_document: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_document: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.

### t10 · Create object Delivery Command · Session slot

Body:
Read: \`entity context object --name "Delivery Command · Session slot" --json\`, then get_objects for \`OBJ_dcmd_session_slot\`; if \`OBJ_dcmd_session_slot\` or the name Delivery Command · Session slot already exists, stop and report.
Done when: object Delivery Command · Session slot (\`OBJ_dcmd_session_slot\`), described "One bookable customer training slot.", holds every field the body lists, exactly: slot_id text unique (SLT-nn), project_id text, date date epoch ms, start text, end text, topic text, taken boolean, booked_by text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_session_slot\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_session_slot\` with every field the body lists, its primaryKey and its indexes.
Result IDs: {"entity":"OBJ_dcmd_session_slot"}
Read back: OBJ_dcmd_session_slot (Delivery Command · Session slot): get_objects fields = slot_id string (primaryKey, uniqueKey, nameField), project_id string, date integer date epoch, start string, end string, topic string, taken boolean, booked_by string
Read back: OBJ_dcmd_session_slot: required ["slot_id"]; fieldDefinitions slot_id input and schema both carry "primaryKey": true, "uniqueKey": true
Read back: OBJ_dcmd_session_slot: picklists no picklists
Read back: OBJ_dcmd_session_slot: indexes: [] (none named by the body)
Read back: OBJ_dcmd_session_slot: unmirroredFields: [] (both schema halves hold every field)
Read back: OBJ_dcmd_session_slot: Security rule 1 — created with default access settings; no skipPermissionsFilter or external written
Unverified: OBJ_dcmd_session_slot: field types beyond the primaryKey are as sent and checked by the batch's own post-write compare, not re-read via fieldDefinitions — check: get_objects parts [fieldDefinitions].
Note: Design check (object-schema-designer): plan specifies cross-object references (project_id, task_id, person, etc.) as plain text, not foreignKey lookups; built exactly as planned, so no write-time FK enforcement and no delete protection.
Note: Created in one apply_object_batch call with the other nine objects of this batch; wrote: true; post-write check reported no notStored changes.

