---
nebula: 3
specId: "e_6adb96de0881d2257aa193e7"
mode: "sonic"
title: "ClickUp Delivery Command · plan 2 of 10"
owner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"Delivery Command · Sign-off"},{"kind":"object","name":"Delivery Command · Checklist item"},{"kind":"object","name":"Delivery Command · Notification"},{"kind":"object","name":"Delivery Command · Integration"},{"kind":"object","name":"Delivery Command · Saved view"},{"kind":"object","name":"Delivery Command · Weekly snapshot"},{"kind":"object","name":"Delivery Command · Weekly metric"},{"kind":"object","name":"Delivery Command · AI output"},{"kind":"object","name":"Delivery Command · Role permission"},{"kind":"object","name":"Delivery Command · Upload"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "713bbf06-d6d3-4480-b969-313d905ae64c"
pageDesign: 2
createdAt: "2026-10-23T17:18:24.171Z"
runningAt: "2026-10-23T17:18:28.556Z"
runner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"382b1b0f-8b04-5591-805d-15b67bc592e7"}
---
## Plan

Goal: ClickUp Delivery Command · plan 2 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | Delivery Command · Sign-off |  | running | 1 |
| t2 | object | Delivery Command · Checklist item |  | running | 1 |
| t3 | object | Delivery Command · Notification |  | running | 1 |
| t4 | object | Delivery Command · Integration |  | running | 1 |
| t5 | object | Delivery Command · Saved view |  | running | 1 |
| t6 | object | Delivery Command · Weekly snapshot |  | running | 1 |
| t7 | object | Delivery Command · Weekly metric |  | running | 1 |
| t8 | object | Delivery Command · AI output |  | running | 1 |
| t9 | object | Delivery Command · Role permission |  | running | 1 |
| t10 | object | Delivery Command · Upload |  | running | 1 |

### t1 · Create object Delivery Command · Sign-off

Body:
Read: \`entity context object --name "Delivery Command · Sign-off" --json\`, then get_objects for \`OBJ_dcmd_signoff\`; if \`OBJ_dcmd_signoff\` or the name Delivery Command · Sign-off already exists, stop and report.
Done when: object Delivery Command · Sign-off (\`OBJ_dcmd_signoff\`), described "One stage deliverable awaiting or carrying the customer sponsor's sign-off.", holds every field the body lists, exactly: signoff_id text unique (SGN-nnn), project_id text, stage picklist (the seven stage codes), deliverable text, status picklist (awaiting "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), requested_at date epoch ms, decided_by text, decided_at datetime epoch ms, comment long text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_signoff\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_signoff\` with every field the body lists, its primaryKey and its indexes.

### t2 · Create object Delivery Command · Checklist item

Body:
Read: \`entity context object --name "Delivery Command · Checklist item" --json\`, then get_objects for \`OBJ_dcmd_checklist_item\`; if \`OBJ_dcmd_checklist_item\` or the name Delivery Command · Checklist item already exists, stop and report.
Done when: object Delivery Command · Checklist item (\`OBJ_dcmd_checklist_item\`), described "One of the ten readiness questions with the customer's answer.", holds every field the body lists, exactly: item_id text unique (CHK-nn), project_id text, order number, question_en text, question_de text, question_ja text, answer text (empty means not set).
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_checklist_item\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_checklist_item\` with every field the body lists, its primaryKey and its indexes.

### t3 · Create object Delivery Command · Notification

Body:
Read: \`entity context object --name "Delivery Command · Notification" --json\`, then get_objects for \`OBJ_dcmd_notification\`; if \`OBJ_dcmd_notification\` or the name Delivery Command · Notification already exists, stop and report.
Done when: object Delivery Command · Notification (\`OBJ_dcmd_notification\`), described "One assignment, sign-off or mention for a user.", holds every field the body lists, exactly: notification_id text unique (NTF-nn), recipient text, kind picklist (assignment "New assignment", signoff "Sign-off", mention "Mention"), text text, link text, read boolean, at datetime epoch ms.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_notification\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_notification\` with every field the body lists, its primaryKey and its indexes.

### t4 · Create object Delivery Command · Integration

Body:
Read: \`entity context object --name "Delivery Command · Integration" --json\`, then get_objects for \`OBJ_dcmd_integration\`; if \`OBJ_dcmd_integration\` or the name Delivery Command · Integration already exists, stop and report.
Done when: object Delivery Command · Integration (\`OBJ_dcmd_integration\`), described "The sync status of one connected system.", holds every field the body lists, exactly: system text unique (Salesforce, Slack, Google Drive, Jira), status picklist (live "Live", sync_failed "Sync failed"), last_sync datetime epoch ms, error text, affected text.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_integration\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_integration\` with every field the body lists, its primaryKey and its indexes.

### t5 · Create object Delivery Command · Saved view

Body:
Read: \`entity context object --name "Delivery Command · Saved view" --json\`, then get_objects for \`OBJ_dcmd_saved_view\`; if \`OBJ_dcmd_saved_view\` or the name Delivery Command · Saved view already exists, stop and report.
Done when: object Delivery Command · Saved view (\`OBJ_dcmd_saved_view\`), described "One named, shareable set of portfolio filters.", holds every field the body lists, exactly: view_id text unique (VW-nn), name text, owner text, filters long text (JSON), shared_with_team boolean.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_saved_view\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_saved_view\` with every field the body lists, its primaryKey and its indexes.

### t6 · Create object Delivery Command · Weekly snapshot

Body:
Read: \`entity context object --name "Delivery Command · Weekly snapshot" --json\`, then get_objects for \`OBJ_dcmd_weekly_snapshot\`; if \`OBJ_dcmd_weekly_snapshot\` or the name Delivery Command · Weekly snapshot already exists, stop and report.
Done when: object Delivery Command · Weekly snapshot (\`OBJ_dcmd_weekly_snapshot\`), described "Portfolio health counts for one week, for the trend.", holds every field the body lists, exactly: week_start date epoch ms unique, on_track number, at_risk number, off_track number, active_projects number, on_track_share number.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_weekly_snapshot\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_weekly_snapshot\` with every field the body lists, its primaryKey and its indexes.

### t7 · Create object Delivery Command · Weekly metric

Body:
Read: \`entity context object --name "Delivery Command · Weekly metric" --json\`, then get_objects for \`OBJ_dcmd_weekly_metric\`; if \`OBJ_dcmd_weekly_metric\` or the name Delivery Command · Weekly metric already exists, stop and report.
Done when: object Delivery Command · Weekly metric (\`OBJ_dcmd_weekly_metric\`), described "The executive summary's six headline numbers and the contract value bridge for one week.", holds every field the body lists, exactly: week_start date epoch ms unique, active_projects, active_projects_prev, golives_this_month, golives_this_month_prev, projects_at_risk, projects_at_risk_prev, avg_days_to_golive, avg_days_to_golive_prev, utilisation_pct, utilisation_pct_prev, value_awaiting_q4_usd, value_awaiting_q4_usd_prev_week, value_awaiting_q4_usd_last_month, bridge_new_usd, bridge_completed_usd, bridge_slipped_usd, bridge_cancelled_usd (all number).
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_weekly_metric\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_weekly_metric\` with every field the body lists, its primaryKey and its indexes.

### t8 · Create object Delivery Command · AI output

Body:
Read: \`entity context object --name "Delivery Command · AI output" --json\`, then get_objects for \`OBJ_dcmd_ai_output\`; if \`OBJ_dcmd_ai_output\` or the name Delivery Command · AI output already exists, stop and report.
Done when: object Delivery Command · AI output (\`OBJ_dcmd_ai_output\`), described "One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report.", holds every field the body lists, exactly: output_id text unique (AIO-nn), kind picklist (risk_flag "Risk flag", meeting_summary "Meeting summary", proposed_task "Proposed task", status_report "Status report"), project_id text, title text, body long text, confidence picklist (high "High", medium "Medium", low "Low"), evidence long text, transcript_ref text, status picklist (open, draft, proposed, accepted, rejected, published), ai_written boolean default true, created_at datetime epoch ms.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_ai_output\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_ai_output\` with every field the body lists, its primaryKey and its indexes.

### t9 · Create object Delivery Command · Role permission

Body:
Read: \`entity context object --name "Delivery Command · Role permission" --json\`, then get_objects for \`OBJ_dcmd_role_permission\`; if \`OBJ_dcmd_role_permission\` or the name Delivery Command · Role permission already exists, stop and report.
Done when: object Delivery Command · Role permission (\`OBJ_dcmd_role_permission\`), described "One role's row in the roles-against-permissions grid.", holds every field the body lists, exactly: role text unique, view_portfolio, edit_project, move_tasks, book_consultants, approve_timesheets, raise_change, approve_change, view_internal_health, sign_off_deliverables, admin (all boolean).
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_role_permission\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_role_permission\` with every field the body lists, its primaryKey and its indexes.

### t10 · Create object Delivery Command · Upload

Body:
Read: \`entity context object --name "Delivery Command · Upload" --json\`, then get_objects for \`OBJ_dcmd_upload\`; if \`OBJ_dcmd_upload\` or the name Delivery Command · Upload already exists, stop and report.
Done when: object Delivery Command · Upload (\`OBJ_dcmd_upload\`), described "One customer file upload with its row error summary.", holds every field the body lists, exactly: upload_id text unique (UPL-nnn), project_id text, file_name text, rows_total number, rows_error number, error_summary long text (JSON: error type, count, first five row numbers), status picklist (validated "Validated", confirmed "Confirmed"), uploaded_by text, at datetime epoch ms.
Rules: the unique text field named first is the primaryKey and is in \`required\`; each picklist stores its code with the label given; every date and datetime is epoch ms (number); booleans are booleans; long text is a long string; field properties follow object-storage-manager § Object schema format; plain field names, never \`properties_\` columns.
Apply the write once with apply_object_batch (create the object, its fields and the indexes the line names), then read it back.
Read back: get_objects for \`OBJ_dcmd_upload\` quoting every field the body lists with its type, the primaryKey, the picklist codes and each index.
Report ids (the object id as ids.entity), readBack, unverified, notes.

Proof: get_objects shows \`OBJ_dcmd_upload\` with every field the body lists, its primaryKey and its indexes.

