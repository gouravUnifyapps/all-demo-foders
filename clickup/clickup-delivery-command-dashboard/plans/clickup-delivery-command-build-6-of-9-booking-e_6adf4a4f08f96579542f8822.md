---
nebula: 3
specId: "e_6adf4a4d08f96579542f880b"
mode: "sonic"
title: "ClickUp Delivery Command · build 6 of 9: booking, timesheet and portal automations"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Book consultant"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Timesheet action"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Portal action"}]
touches: [{"kind":"automation","name":"ClickUp Command · Book consultant"},{"kind":"automation","name":"ClickUp Command · Timesheet action"},{"kind":"automation","name":"ClickUp Command · Portal action"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "0b7ec094-e62d-47e7-b203-7c1b94a83bc7"
pageDesign: 2
createdAt: "2026-10-26T12:40:47.213Z"
runningAt: "2026-10-26T12:40:50.132Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
## Plan

Goal: ClickUp Delivery Command · build 6 of 9: booking, timesheet and portal automations

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation-shell | ClickUp Command · Book consultant |  | done | 1 |
| t2 | automation | ClickUp Command · Book consultant | t1 | done | 1 |
| t3 | deploy | ClickUp Command · Book consultant | t2 | running | 1 |
| t4 | automation-shell | ClickUp Command · Timesheet action |  | done | 1 |
| t5 | automation | ClickUp Command · Timesheet action | t4 | done | 1 |
| t6 | deploy | ClickUp Command · Timesheet action | t5 | running | 1 |
| t7 | automation-shell | ClickUp Command · Portal action |  | done | 1 |
| t8 | automation | ClickUp Command · Portal action | t7 | done | 1 |
| t9 | deploy | ClickUp Command · Portal action | t8 | running | 1 |

### t1 · Shell for ClickUp Command · Book consultant

Body:
Read: \`search_workflows\` for \`ClickUp Command · Book consultant\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs person_code, project_code (text), first_week (number, epoch ms), weeks, hours_per_week (number), confirm (boolean), and \`result\` = outputs result (text: saved \| over_capacity), overages_json (text: each week with booked hours, percent of capacity and hours over), booking_code (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Book consultant\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Book consultant deployed.
Result IDs: {"entity":"6adf4aa308750d257cf32534"}
Read back: ClickUp Command · Book consultant 6adf4aa308750d257cf32534: compile_and_save_workflow created:true version 0 (trigger CALLABLE callables/callables_from_automation, STOP×1 stub)
Read back: ClickUp Command · Book consultant: deploy_workflow ok:true, "Deployed version 0 of automation 6adf4aa308750d257cf32534", paused:false
Read back: ClickUp Command · Book consultant: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, savedAfterDeploy: false} at shell time
Read back: ClickUp Command · Book consultant: describe_callable_workflow parameters person_code (string), project_code (string), first_week (number), weeks (number), hours_per_week (number), confirm (boolean); result schema result, overages_json, booking_code (string)
Note: search_workflows before create found no automation named ClickUp Command · Book consultant (5 other ClickUp Command automations only).

### t2 · Logic for ClickUp Command · Book consultant

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Booking (\`OBJ_cucmd_booking\`), Person (\`OBJ_cucmd_person\`), Project (\`OBJ_cucmd_project\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Book consultant does exactly this, with the shell's inputs and outputs unchanged: callable; inputs person_code, project_code (text), first_week (number, epoch ms), weeks, hours_per_week (number), confirm (boolean); outputs result (text: saved \| over_capacity), overages_json (text: each week with booked hours, percent of capacity and hours over), booking_code (text); a booking that takes the person above 100% of capacity_hours in any week answers over_capacity with the weeks and writes nothing unless confirm is true, when it saves with over_capacity true; a save writes Booking and one Activity row.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: person_code \`P-07\`, project_code \`IMP-2611\`, first_week 2026-11-09 (epoch ms, UTC midnight), weeks 2, hours_per_week 16, confirm \`false\`: expect result \`over_capacity\` and overages_json naming the weeks of 9 and 16 Nov at 120% (8 h over each), and nothing stored. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Book consultant answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf4aa308750d257cf32534"}
Read back: ClickUp Command · Book consultant 6adf4aa308750d257cf32534: compile_and_save_workflow ok:true, version 1, 14 nodes (3× fetch_records, 1 groovy, 2× create_record), changes line names only this task's statements; not deployed (live stays definitionVersion 0 shell)
Read back: ClickUp Command · Book consultant run 6adf4b4197a3bf334d3f1f57 (P-07, IMP-2611, first_week 1794182400000, weeks 2, 16 h, confirm false): COMPLETED, response {result: "over_capacity", overages_json: [{week:"2026-11-09", booked_hours:48.0, capacity_hours:40.0, percent:120, hours_over:8.0},{week:"2026-11-16", booked_hours:48.0, capacity_hours:40.0, percent:120, hours_over:8.0}], booking_code: ""}; no create_record node ran
Read back: ClickUp Command · Book consultant: get_records Booking person_code P-07 after the run total 2 (B-01, B-02) — nothing stored
Read back: ClickUp Command · Book consultant run 6adf4b49f3cd5f19ed4b0df8 (blank person_code/project_code, no numbers): COMPLETED, response {result: "refused_invalid_input", overages_json: "[]", booking_code: ""}
Read back: Security rules touched: rule 3 (capacity read from Person.capacity_hours and Booking rows in the same run, not from the caller); rule 4 (Booking create sets only the 7 contract fields)
Unverified: The saved path (confirm true or under capacity) was not run, to avoid a booking on story person P-07: Booking create with booking_code B-&lt;executionId&gt;, over_capacity flag and the one Activity row (action booked) are untested — check: trigger with confirm true on a DEMO-TEST person and read Booking and Activity by id
Unverified: Security: Person rows are not linked to platform users, so the caller-sent person_code/sponsor_code cannot be checked against USER.id — needs the person to decide whether Person should carry a platform user id
Note: assumed: added result word refused_invalid_input (missing/blank inputs, weeks &lt; 1, hours &lt;= 0, unknown person or project); contract fields unchanged, only the value set grew.
Note: assumed: overages_json lists only the weeks above 100% (each with week, week_start, booked_hours, capacity_hours, percent, hours_over); a save under capacity returns "[]". A person with no capacity_hours counts every week as over with percent null.
Note: assumed: booking_code and activity_code are B-/A-&lt;run executionId&gt;; the record id equals the code (create_record honoured the primary key in the Timesheet test).
Note: Existing bookings counted are all of the person's bookings whose first_week..first_week+weeks*7d covers the week.

### t3 · Deploy ClickUp Command · Book consultant

Body:
Read: \`search_workflows\` for \`ClickUp Command · Book consultant\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Book consultant\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Book consultant deployed with definitionVersion equal to the logic task's saved version.

### t4 · Shell for ClickUp Command · Timesheet action

Body:
Read: \`search_workflows\` for \`ClickUp Command · Timesheet action\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs action (text: log \| submit \| approve \| return), person_code, task_code (text), work_date (number), hours (number), week_start (number), entry_codes (text, comma-separated, for approve and return in a batch), reason (text), and \`result\` = outputs result (text: saved \| refused_reason_required), timesheet_status (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Timesheet action\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Timesheet action deployed.
Result IDs: {"entity":"6adf4aa9f3cd5f19ed4afa85"}
Read back: ClickUp Command · Timesheet action 6adf4aa9f3cd5f19ed4afa85: compile_and_save_workflow created:true version 0 (callables_from_automation stub)
Read back: ClickUp Command · Timesheet action: deploy_workflow ok:true, "Deployed version 0 of automation 6adf4aa9f3cd5f19ed4afa85", paused:false
Read back: ClickUp Command · Timesheet action: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, savedAfterDeploy: false} at shell time
Read back: ClickUp Command · Timesheet action: describe_callable_workflow parameters action, person_code, task_code (string), work_date, hours, week_start (number), entry_codes, reason (string)
Note: search_workflows before create found no automation named ClickUp Command · Timesheet action.

### t5 · Logic for ClickUp Command · Timesheet action

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Time entry (\`OBJ_cucmd_time_entry\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Timesheet action does exactly this, with the shell's inputs and outputs unchanged: callable; inputs action (text: log \| submit \| approve \| return), person_code, task_code (text), work_date (number), hours (number), week_start (number), entry_codes (text, comma-separated, for approve and return in a batch), reason (text); outputs result (text: saved \| refused_reason_required), timesheet_status (text); a return with an empty reason is refused.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: action \`return\`, entry_codes \`E-01\`, reason empty: expect \`refused_reason_required\` and nothing written; then action \`log\` for person_code \`P-07\`, task_code \`T-2611-07\`, work_date 2026-10-27, hours 1, week_start 2026-10-26: expect \`saved\`, and record the entry_code it made (label its row DEMO-TEST in the return_reason-free fields you can) for cleanup. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Timesheet action answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf4aa9f3cd5f19ed4afa85"}
Read back: ClickUp Command · Timesheet action 6adf4aa9f3cd5f19ed4afa85: compile_and_save_workflow ok:true, version 2 (39 nodes; v1 then v2 to treat a whitespace-only reason as empty); not deployed
Read back: ClickUp Command · Timesheet action run 6adf4b9f6112da3e23ba5481 (action return, entry_codes E-01, reason ""): COMPLETED, response {result: "refused_reason_required", timesheet_status: ""}; no storage node ran; get_records E-01 still timesheet_status submitted, no return_reason
Read back: ClickUp Command · Timesheet action run 6adf4ba097a3bf334d3f24b5 (log P-07, T-2611-07, work_date 1793059200000, 1 h, week_start 1792972800000): COMPLETED, response {result: "saved", timesheet_status: "draft"}
Read back: ClickUp Command · Timesheet action: get_records Time entry E-6adf4ba097a3bf334d3f24b5 {entry_code E-6adf4ba097a3bf334d3f24b5, timesheet_status draft, hours 1, work_date 1793059200000, week_start 1792972800000, project_code IMP-2611}; Activity A-6adf4ba097a3bf334d3f24b5 {action logged, actor Gourav, summary "P-07 logged 1 h on T-2611-07 (entry E-6adf4ba097a3bf334d3f24b5)"}
Read back: ClickUp Command · Timesheet action run 6adf4ba197a3bf334d3f24ba (all blank): COMPLETED, response {result: "refused_invalid_input", timesheet_status: ""}
Read back: Security rules touched: rule 3 (approve/return act only on entries the run reads as submitted; submit only on draft/returned rows it reads); rule 4 (each update sets entry_code, timesheet_status and, on return, return_reason only)
Unverified: submit, approve and return-with-reason paths were not run (they would change story time entries): check by running them on DEMO-TEST entries and reading timesheet_status/return_reason back
Unverified: Security: Person rows are not linked to platform users, so the caller-sent person_code/sponsor_code cannot be checked against USER.id — needs the person to decide whether Person should carry a platform user id
Note: Test rows for cleanup: Time entry E-6adf4ba097a3bf334d3f24b5 and Activity A-6adf4ba097a3bf334d3f24b5 (project IMP-2611, made 2026-10-26 by the log test). Time entry has no free-text field besides return_reason, so the row could not carry a DEMO-TEST label.
Note: assumed: added result word refused_invalid_input (unknown action, missing log fields, unknown task, nothing open to submit, no submitted entry among entry_codes).
Note: assumed: log reads Task (OBJ_cucmd_task) for the entry's project_code; every saved action writes one Activity row (logged / updated for submit / approved / rejected for return), created with A-&lt;executionId&gt;.
Note: assumed: approve and return touch only entries currently submitted; submit moves the person's draft and returned entries for week_start to submitted. Updates use storage_by_unifyapps_upsert_record by the fetched row id (update_record_fields_by_id has no upsert key).
Note: handover: actor for Activity rows comes from USER.name (read "Gourav" in the test run).
Note: feedback:
Bug: compile_and_save_workflow refuses a boolean literal as setValue on storage_by_unifyapps_upsert_record, so a boolean field cannot be SET to true without a workaround.
Context: Saving ClickUp Command · Portal action (6adf4aaef3cd5f19ed4afc58) with updateFields { fieldName: properties.taken, actionType: SET, setValue: true }; likely the DSL compiler type check against the upsert schema (setValue: string).
Where: mcp-tool
Evidence: INVALID_INPUT_TYPE "Type 'boolean' at 'updateFields[1].setValue' is not assignable to type 'string'"; passing a boolean pill from a code node output saved.
Cause: Suspected: literals are checked against the editor-form schema while boolean pills pass; runtime storage type of the pill is unverified.
Regression: Save setValue: true on upsert_record for a boolean field; it should save and store a boolean, or name the supported way.

### t6 · Deploy ClickUp Command · Timesheet action

Body:
Read: \`search_workflows\` for \`ClickUp Command · Timesheet action\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Timesheet action\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Timesheet action deployed with definitionVersion equal to the logic task's saved version.

### t7 · Shell for ClickUp Command · Portal action

Body:
Read: \`search_workflows\` for \`ClickUp Command · Portal action\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs action (text: sign_off \| request_changes \| book_slot \| answer_checklist \| confirm_upload), sponsor_code, deliverable_code, slot_code, item_code, answer, doc_code, comment (text), and \`result\` = outputs result (text: saved \| refused_comment_required \| refused_slot_taken \| refused_not_your_project), decided_by (text), decided_at (number, epoch ms), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Portal action\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Portal action deployed.
Result IDs: {"entity":"6adf4aaef3cd5f19ed4afc58"}
Read back: ClickUp Command · Portal action 6adf4aaef3cd5f19ed4afc58: compile_and_save_workflow created:true version 0 (callables_from_automation stub)
Read back: ClickUp Command · Portal action: deploy_workflow ok:true, "Deployed version 0 of automation 6adf4aaef3cd5f19ed4afc58", paused:false
Read back: ClickUp Command · Portal action: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, savedAfterDeploy: false} at shell time
Read back: ClickUp Command · Portal action: describe_callable_workflow parameters action, sponsor_code, deliverable_code, slot_code, item_code, answer, doc_code, comment (all string)
Note: search_workflows before create found no automation named ClickUp Command · Portal action.

### t8 · Logic for ClickUp Command · Portal action

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Deliverable (\`OBJ_cucmd_deliverable\`), Session slot (\`OBJ_cucmd_session_slot\`), Checklist item (\`OBJ_cucmd_checklist_item\`), Document (\`OBJ_cucmd_document\`), Person (\`OBJ_cucmd_person\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Portal action does exactly this, with the shell's inputs and outputs unchanged: callable; inputs action (text: sign_off \| request_changes \| book_slot \| answer_checklist \| confirm_upload), sponsor_code, deliverable_code, slot_code, item_code, answer, doc_code, comment (text); outputs result (text: saved \| refused_comment_required \| refused_slot_taken \| refused_not_your_project), decided_by (text), decided_at (number, epoch ms); a sponsor acts only on their own project_code; request_changes needs a comment; a taken slot is refused; sign_off records who and when and writes Activity.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: action \`request_changes\`, sponsor_code \`P-15\`, deliverable_code \`D-2611-5\`, comment empty: expect \`refused_comment_required\`; action \`book_slot\`, sponsor_code \`P-15\`, slot_code \`S-02\` (taken): expect \`refused_slot_taken\`; action \`sign_off\`, sponsor_code \`P-16\`, deliverable_code \`D-2611-5\`: expect \`refused_not_your_project\`. Nothing is written by these three. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Portal action answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf4aaef3cd5f19ed4afc58"}
Read back: ClickUp Command · Portal action 6adf4aaef3cd5f19ed4afc58: compile_and_save_workflow ok:true, version 1 (46 nodes: 5× fetch_records, 5× upsert_record, 1 create_record); not deployed
Read back: ClickUp Command · Portal action run 6adf4bf208750d257cf390a8 (request_changes, P-15, D-2611-5, comment ""): COMPLETED, response {result: "refused_comment_required", decided_by: "", decided_at: 0}
Read back: ClickUp Command · Portal action run 6adf4bf4f3cd5f19ed4b299f (book_slot, P-15, S-02): COMPLETED, response {result: "refused_slot_taken", decided_by: "", decided_at: 0}
Read back: ClickUp Command · Portal action run 6adf4bf46112da3e23ba5afe (sign_off, P-16, D-2611-5): COMPLETED, ownership condition read IMP-2611 NOT_EQUAL IMP-2598 = true, response {result: "refused_not_your_project", decided_by: "", decided_at: 0}
Read back: ClickUp Command · Portal action run 6adf4bf597a3bf334d3f29f2 (all blank): COMPLETED, response {result: "refused_invalid_input", decided_by: "", decided_at: 0}
Read back: ClickUp Command · Portal action: get_records after the runs — D-2611-5 status awaiting_signoff (no decided_by/comment), S-02 taken true booked_by Rina Kobayashi, no new Activity row: nothing written
Read back: Security rules touched: rule 3 (the sponsor's project_code and each target row's project_code, slot taken flag are read in the same run before any write); rule 4 (each update sets only the listed fields of its object)
Unverified: The saved paths (sign_off, request_changes with comment, book_slot on a free slot, answer_checklist, confirm_upload) were not run, to keep story rows unchanged: check by running each on DEMO-TEST rows and reading the row and the sign_off Activity back
Unverified: Whether upsert_record stores decided_at/answered_at as numbers and taken as a boolean (setValue is typed string) — check: after a sign_off and a book_slot test, read decided_at and taken types with get_records
Unverified: Security: Person rows are not linked to platform users, so the caller-sent person_code/sponsor_code cannot be checked against USER.id — needs the person to decide whether Person should carry a platform user id
Note: assumed: added result word refused_invalid_input (unknown action, blank sponsor_code, unknown deliverable/slot/item/document, blank checklist answer). A sponsor_code that is not a customer_sponsor Person with a project_code answers refused_not_your_project.
Note: assumed: only sign_off writes an Activity row (action signed_off, actor = sponsor name), as the contract names; request_changes stores status changes_requested, comment, decided_by, decided_at; book_slot sets taken and booked_by; answer_checklist sets answer, answered_by, answered_at; confirm_upload sets upload_status confirmed and edited_by. decided_by/decided_at are returned for every saved action.
Note: Check order: ownership before the comment check, so a sponsor of another project gets refused_not_your_project first.
Note: feedback:
Bug: compile_and_save_workflow refuses a boolean literal as setValue on storage_by_unifyapps_upsert_record, so a boolean field cannot be SET to true without a workaround.
Context: Saving ClickUp Command · Portal action (6adf4aaef3cd5f19ed4afc58) with updateFields { fieldName: properties.taken, actionType: SET, setValue: true }; likely the DSL compiler type check against the upsert schema (setValue: string).
Where: mcp-tool
Evidence: INVALID_INPUT_TYPE "Type 'boolean' at 'updateFields[1].setValue' is not assignable to type 'string'"; passing a boolean pill from a code node output saved.
Cause: Suspected: literals are checked against the editor-form schema while boolean pills pass; runtime storage type of the pill is unverified.
Regression: Save setValue: true on upsert_record for a boolean field; it should save and store a boolean, or name the supported way.

### t9 · Deploy ClickUp Command · Portal action

Body:
Read: \`search_workflows\` for \`ClickUp Command · Portal action\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Portal action\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Portal action deployed with definitionVersion equal to the logic task's saved version.

