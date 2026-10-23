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
## Plan

Goal: ClickUp Delivery Command · plan 1 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | Delivery Command · Project |  | running | 1 |
| t2 | object | Delivery Command · Task |  | running | 1 |
| t3 | object | Delivery Command · RAID item |  | running | 1 |
| t4 | object | Delivery Command · Person |  | running | 1 |
| t5 | object | Delivery Command · Booking |  | running | 1 |
| t6 | object | Delivery Command · Time entry |  | running | 1 |
| t7 | object | Delivery Command · Change request |  | running | 1 |
| t8 | object | Delivery Command · Activity |  | running | 1 |
| t9 | object | Delivery Command · Document |  | running | 1 |
| t10 | object | Delivery Command · Session slot |  | running | 1 |

### t1 · Create object Delivery Command · Project

Body:
Read: \`entity context object --name "Delivery Command · Project" --json\`, then get_objects for \`OBJ_dcmd_project\`; if \`OBJ_dcmd_project\` or the name Delivery Command · Project already exists, stop and report.
Done when: object Delivery Command · Project (\`OBJ_dcmd_project\`), described "One customer implementation, from signed contract to Hypercare.", holds every field the body lists, exactly: project_id text unique (IMP-nnnn), customer text, customer_initials text, region picklist (north_america "North America", europe "Europe", japan "Japan"), stage picklist (kickoff "Kickoff", discovery "Discovery", configuration "Configuration", data_migration "Data migration", integrations "Integrations", training "Training", hypercare "Hypercare"), stage_index number 1 to 7, go_live date epoch ms, baseline_go_live date epoch ms, slipped boolean, health picklist (on_track "On track", at_risk "At risk", off_track "Off track"), lead text, seats number, contract_value number, currency picklist (USD, EUR, JPY), budget_hours number, used_hours number, lifecycle picklist (active "Active", live "Live", cancelled "Cancelled"), sponsor text, portal_language picklist (en, de, ja), last_synced_at datetime epoch ms; index on region, health, lead.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_project\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_project\` with every field the body lists, its primaryKey and its indexes.

### t2 · Create object Delivery Command · Task

Body:
Read: \`entity context object --name "Delivery Command · Task" --json\`, then get_objects for \`OBJ_dcmd_task\`; if \`OBJ_dcmd_task\` or the name Delivery Command · Task already exists, stop and report.
Done when: object Delivery Command · Task (\`OBJ_dcmd_task\`), described "One task in a project plan, with dates, dependencies and the critical path.", holds every field the body lists, exactly: task_id text unique (TSK-nnnn), project_id text, title text, description long text, stage picklist (the seven stage codes of Project), status picklist (not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee text, start date epoch ms, end date epoch ms, depends_on text (a task_id), critical boolean, hours_planned number, hours_logged number, ai_proposed boolean; index on project_id, assignee.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_task\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_task\` with every field the body lists, its primaryKey and its indexes.

### t3 · Create object Delivery Command · RAID item

Body:
Read: \`entity context object --name "Delivery Command · RAID item" --json\`, then get_objects for \`OBJ_dcmd_raid\`; if \`OBJ_dcmd_raid\` or the name Delivery Command · RAID item already exists, stop and report.
Done when: object Delivery Command · RAID item (\`OBJ_dcmd_raid\`), described "One risk, assumption, issue or decision on a project.", holds every field the body lists, exactly: raid_id text unique (RSK-, ASM-, ISS-, DEC-nnnn), project_id text, type picklist (risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title text, owner text, due date epoch ms, status picklist (open "Open", mitigating "Mitigating", closed "Closed"), likelihood number 1 to 5, impact number 1 to 5, jira_key text, history long text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_raid\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_raid\` with every field the body lists, its primaryKey and its indexes.

### t4 · Create object Delivery Command · Person

Body:
Read: \`entity context object --name "Delivery Command · Person" --json\`, then get_objects for \`OBJ_dcmd_person\`; if \`OBJ_dcmd_person\` or the name Delivery Command · Person already exists, stop and report.
Done when: object Delivery Command · Person (\`OBJ_dcmd_person\`), described "One internal user or customer sponsor, with capacity and skill levels.", holds every field the body lists, exactly: person_id text unique (PER-nnn), name text, role picklist (consultant "Consultant", lead "Implementation lead", director "Delivery director", resource_manager "Resource manager", finance_partner "Finance partner", sponsor "Customer sponsor"), region picklist (as Project), capacity_hours number, skill_data_migration number 0 to 4, skill_integrations number 0 to 4, skill_admin_training number 0 to 4, skill_api number 0 to 4, skill_japanese number 0 to 4, customer text, email text, time_zone text, week_start picklist (monday "Monday", sunday "Sunday").
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_person\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_person\` with every field the body lists, its primaryKey and its indexes.

### t5 · Create object Delivery Command · Booking

Body:
Read: \`entity context object --name "Delivery Command · Booking" --json\`, then get_objects for \`OBJ_dcmd_booking\`; if \`OBJ_dcmd_booking\` or the name Delivery Command · Booking already exists, stop and report.
Done when: object Delivery Command · Booking (\`OBJ_dcmd_booking\`), described "Hours one person is booked on one project in one week.", holds every field the body lists, exactly: booking_id text unique (BKG-nnnn), person text, project_id text, week_start date epoch ms, hours number; index on person, week_start.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_booking\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_booking\` with every field the body lists, its primaryKey and its indexes.

### t6 · Create object Delivery Command · Time entry

Body:
Read: \`entity context object --name "Delivery Command · Time entry" --json\`, then get_objects for \`OBJ_dcmd_time_entry\`; if \`OBJ_dcmd_time_entry\` or the name Delivery Command · Time entry already exists, stop and report.
Done when: object Delivery Command · Time entry (\`OBJ_dcmd_time_entry\`), described "Hours one person logged on one task on one day, inside a weekly timesheet.", holds every field the body lists, exactly: entry_id text unique (TME-nnnn), person text, task_id text, project_id text, date date epoch ms, hours number, timesheet_week date epoch ms, timesheet_status picklist (draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_time_entry\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_time_entry\` with every field the body lists, its primaryKey and its indexes.

### t7 · Create object Delivery Command · Change request

Body:
Read: \`entity context object --name "Delivery Command · Change request" --json\`, then get_objects for \`OBJ_dcmd_change_request\`; if \`OBJ_dcmd_change_request\` or the name Delivery Command · Change request already exists, stop and report.
Done when: object Delivery Command · Change request (\`OBJ_dcmd_change_request\`), described "One proposed change to a project, with its two-step approval route.", holds every field the body lists, exactly: cr_id text unique (CR-nnnn), project_id text, raised_by text, reason long text, work_added long text, work_removed long text, hours_delta number, cost_delta number, currency picklist (USD, EUR, JPY), golive_before date epoch ms, golive_after date epoch ms, plan_before long text (JSON task list), plan_after long text (JSON task list), route picklist (director "Delivery director", director_finance "Delivery director, then finance partner"), step1_status picklist (pending, approved, rejected), step1_by text, step1_at datetime epoch ms, step2_status picklist (not_needed, waiting, pending, approved, rejected), step2_by text, step2_at datetime epoch ms, next_approver text, status picklist (draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), reject_reason long text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_change_request\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_change_request\` with every field the body lists, its primaryKey and its indexes.

### t8 · Create object Delivery Command · Activity

Body:
Read: \`entity context object --name "Delivery Command · Activity" --json\`, then get_objects for \`OBJ_dcmd_activity\`; if \`OBJ_dcmd_activity\` or the name Delivery Command · Activity already exists, stop and report.
Done when: object Delivery Command · Activity (\`OBJ_dcmd_activity\`), described "One change on a project: who did what and when; never edited.", holds every field the body lists, exactly: activity_id text unique (ACT-nnnn), at datetime epoch ms, actor text, project_id text, action text, target text, detail text, source picklist (app "Delivery Command", automation "Automation", ai "Delivery Copilot", salesforce "Salesforce"); rows are only ever created, never updated or deleted; index on project_id, actor, action.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_activity\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_activity\` with every field the body lists, its primaryKey and its indexes.

### t9 · Create object Delivery Command · Document

Body:
Read: \`entity context object --name "Delivery Command · Document" --json\`, then get_objects for \`OBJ_dcmd_document\`; if \`OBJ_dcmd_document\` or the name Delivery Command · Document already exists, stop and report.
Done when: object Delivery Command · Document (\`OBJ_dcmd_document\`), described "One file in a project library: statement of work, migration plan or sign-off record.", holds every field the body lists, exactly: document_id text unique (DOC-nn), project_id text, title text, body long text (the document's text, shown in the in-app viewer), kind picklist (sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", other "Other"), file_url text, shared_with_customer boolean, source text, uploaded_by text, at date epoch ms.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_document\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_document\` with every field the body lists, its primaryKey and its indexes.

### t10 · Create object Delivery Command · Session slot

Body:
Read: \`entity context object --name "Delivery Command · Session slot" --json\`, then get_objects for \`OBJ_dcmd_session_slot\`; if \`OBJ_dcmd_session_slot\` or the name Delivery Command · Session slot already exists, stop and report.
Done when: object Delivery Command · Session slot (\`OBJ_dcmd_session_slot\`), described "One bookable customer training slot.", holds every field the body lists, exactly: slot_id text unique (SLT-nn), project_id text, date date epoch ms, start text, end text, topic text, taken boolean, booked_by text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_session_slot\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_session_slot\` with every field the body lists, its primaryKey and its indexes.

