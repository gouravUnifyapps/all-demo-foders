---
nebula: 3
specId: "e_6adf47d4769c8b649e99d3bf"
mode: "sonic"
title: "ClickUp Delivery Command · build 5 of 9: task, change request and approval automations"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Update task"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Raise change request"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Decide change request"}]
touches: [{"kind":"automation","name":"ClickUp Command · Update task"},{"kind":"automation","name":"ClickUp Command · Raise change request"},{"kind":"automation","name":"ClickUp Command · Decide change request"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "7f167347-74b3-4641-8962-cf7b27b26e7e"
pageDesign: 2
createdAt: "2026-10-26T12:30:13.295Z"
runningAt: "2026-10-26T12:30:16.737Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · build 5 of 9: task, change request and approval automations

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation-shell | ClickUp Command · Update task |  | done | 1 |
| t2 | automation | ClickUp Command · Update task | t1 | done | 1 |
| t3 | deploy | ClickUp Command · Update task | t2 | done | 1 |
| t4 | automation-shell | ClickUp Command · Raise change request |  | done | 1 |
| t5 | automation | ClickUp Command · Raise change request | t4 | done | 1 |
| t6 | deploy | ClickUp Command · Raise change request | t5 | done | 1 |
| t7 | automation-shell | ClickUp Command · Decide change request |  | done | 1 |
| t8 | automation | ClickUp Command · Decide change request | t7 | done | 1 |
| t9 | deploy | ClickUp Command · Decide change request | t8 | done | 1 |

### t1 · Shell for ClickUp Command · Update task

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update task\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs task_code (text), action (text: move \| reschedule \| status), to_stage (text), new_start (number, epoch ms), new_end (number, epoch ms), status (text), preview (boolean), and \`result\` = outputs result (text: saved \| preview \| refused), column_count (number), column_limit (number), over_limit (boolean), moved_json (text: each dependent task with its new dates), new_go_live (number, epoch ms), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Update task\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Update task deployed.
Result IDs: {"entity":"6adf485af3cd5f19ed4ac683"}
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: search_workflows before create found no automation of that name; compile_and_save_workflow created it at version 0 (trigger callables/callables_from_automation, 2 nodes, STOP×1)
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: deploy_workflow ok:true, workflowVersion 0, deployedVersion 1, paused false, deploymentNotes 'Contract shell for ClickUp Command · Update task'
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, savedAfterDeploy: false} right after the shell deploy
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: describe_callable_workflow lists 7 inputs task_code (string), action (string), to_stage (string), new_start (number), new_end (number), status (string), preview (boolean)
Note: The result schema declares result, column_count, column_limit, over_limit, moved_json, new_go_live; the stub returned refused, 0, 0, false, "[]", 0.

### t2 · Logic for ClickUp Command · Update task

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Task (\`OBJ_cucmd_task\`), Project (\`OBJ_cucmd_project\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Update task does exactly this, with the shell's inputs and outputs unchanged: callable; inputs task_code (text), action (text: move \| reschedule \| status), to_stage (text), new_start (number, epoch ms), new_end (number, epoch ms), status (text), preview (boolean); outputs result (text: saved \| preview \| refused), column_count (number), column_limit (number), over_limit (boolean), moved_json (text: each dependent task with its new dates), new_go_live (number, epoch ms); a reschedule moves every finish-to-start dependent by the same working days and returns the project's new go-live date; preview true writes nothing; a save writes Task and one Activity row.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: task_code \`T-2611-15\`, action \`reschedule\`, new_start and new_end two working days later than stored, preview \`true\`; expect result \`preview\`, moved_json naming T-2611-16, T-2611-17 and T-2611-18 with new dates, new_go_live 2026-11-18 (epoch ms), and no stored row changed. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Update task answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf485af3cd5f19ed4ac683"}
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: compile_and_save_workflow ok, saved version 2 (13 nodes: 3 fetch_records, code_by_unifyapps_javascript, upsert_record in a loop, create_record on Activity, 3 returns); not deployed — search_workflows shows definitionVersion 0 live, savedAfterDeploy true
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: test run 6adf48e46112da3e23b9fd8f (T-2611-15, reschedule, new_start 1793145600000 = 2026-10-28, new_end 1793836800000 = 2026-11-05, preview true) COMPLETED with response result "preview", column_count 5, column_limit 15, over_limit false, new_go_live 1794960000000 (2026-11-18), moved_json naming T-2611-16 (2026-11-05 to 2026-11-09), T-2611-17 (2026-11-09 to 2026-11-12), T-2611-18 (2026-11-17 to 2026-11-18), T-2611-19 (2026-11-18 to 2026-12-02), T-2611-20 (2026-12-03 to 2026-12-08); it ended on the no-write return, and no upsert or create node ran
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: get_records after the tests: T-2611-15..18 still version 0 with their stored dates (T-2611-15 1792972800000/1793664000000, T-2611-18 1794614400000/1794787200000), so the preview changed no story row
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: all-blank test run 6adf490092718f6a64cea3da COMPLETED with response result "refused" (column_count 0, moved_json "[]"); it ended at the missing-task guard, and no write node ran
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: save test run 6adf490b08750d257cf27c0d on the fixture T-DEMOTEST-01 (reschedule +1 working day, preview false) COMPLETED with response result "saved" and moved_json naming T-DEMOTEST-02 (2026-10-30 to 2026-11-04); get_records shows T-DEMOTEST-01 end_date 1793318400000 and T-DEMOTEST-02 1793318400000/1793750400000, stored as numbers, version 1
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: that save created exactly one Activity row A-6adf490b08750d257cf27c0d (action updated, project_code DEMO-TEST-2026-10-26, actor from USER.name); get_records on Activity rows created since the build shows only that one
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: security rules 3 and 4: the task, its project tasks and the project are read again from storage in the same run; the writes set only stage, status, start_date and end_date, through upsert_record by the record id
Unverified: The move and status actions and the over_limit=true path were not test-run; only reschedule (preview, save) and the blank refusal were. Check: a preview run with action move on a T-2611 task to a stage at its column_limit.
Unverified: Run outputs are quoted from trigger_workflow_run's finished-run node details (the same data inspect_workflow_run returns); inspect_workflow_run was not called separately.
Note: assumed: the working-day shift counts Monday to Friday in UTC (no holidays), and the delta is taken from the task's end-date change. Dependents are found transitively through depends_on, so T-2611-19 and T-2611-20 move as well as 16 to 18.
Note: assumed: new_go_live is the new end of whichever moved task ended on the project's go_live_date (here T-2611-18). The Project row is not written, because the contract says a save writes Task and one Activity row.
Note: assumed: over_limit only flags the move and does not refuse it; result refused covers an unknown or blank task, a bad action, stage, status or dates.
Note: assumed: the Activity actor is USER.name, since the contract has no actor input. The activity_code is A-&lt;executionId&gt;, and the record id comes back equal to it.
Note: Test fixtures to clean up (label DEMO-TEST 2026-10-26): Task rows T-DEMOTEST-01 and T-DEMOTEST-02 (project_code DEMO-TEST-2026-10-26), and Activity row A-6adf490b08750d257cf27c0d.
Note: handover: Update task 6adf485af3cd5f19ed4ac683 saved version 2 is the logic version to deploy; the live deployment is still the shell, version 0.
Note: Every save's changes line named only this task's statements (added nodes, the changed return, the description).

### t3 · Deploy ClickUp Command · Update task

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update task\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Update task\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Update task deployed with definitionVersion equal to the logic task's saved version.
Result IDs: {"entity":"6adf485af3cd5f19ed4ac683"}
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: before deploying, search_workflows showed saved version 2, the version the logic task tested, so nothing was saved in between
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: deploy_workflow ok:true, workflowVersion 2, storedVersion 2, deployedVersion 2, paused false, deploymentNotes 'ClickUp Delivery Command demo: Update task'
Read back: ClickUp Command · Update task 6adf485af3cd5f19ed4ac683: search_workflows deployment {status: DEPLOYED, definitionVersion: 2, deployedAt: 1793018382698, savedAfterDeploy: false}, so definitionVersion 2 equals the logic task's saved version 2
Note: The deploy was made on the person's yes given through plan confirm.

### t4 · Shell for ClickUp Command · Raise change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Raise change request\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs project_code, reason, work_added, work_removed (text), hours_delta, cost_delta, go_live_delta_days (number), raised_by (text), preview (boolean), and \`result\` = outputs cr_code (text), before_json, after_json, route_json (text), result (text: preview \| submitted \| refused_reason_required), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Raise change request\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Raise change request deployed.
Result IDs: {"entity":"6adf485ec79cad1140a9e9a6"}
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: search_workflows before create found no automation of that name; compile_and_save_workflow created it at version 0 (callables_from_automation, 2 nodes)
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: deploy_workflow ok:true, workflowVersion 0, deployedVersion 1, paused false, deploymentNotes 'Contract shell for ClickUp Command · Raise change request'
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, savedAfterDeploy: false} right after the shell deploy
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: describe_callable_workflow lists 9 inputs project_code, reason, work_added, work_removed (string), hours_delta, cost_delta, go_live_delta_days (number), raised_by (string), preview (boolean)
Note: The result schema declares cr_code, before_json, after_json, route_json, result.

### t5 · Logic for ClickUp Command · Raise change request

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Change request (\`OBJ_cucmd_change_request\`), Project (\`OBJ_cucmd_project\`), Task (\`OBJ_cucmd_task\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Raise change request does exactly this, with the shell's inputs and outputs unchanged: callable; inputs project_code, reason, work_added, work_removed (text), hours_delta, cost_delta, go_live_delta_days (number), raised_by (text), preview (boolean); outputs cr_code (text), before_json, after_json, route_json (text), result (text: preview \| submitted \| refused_reason_required); route: an absolute hours_delta under 40 goes to the Delivery director only; 40 or more goes to the Delivery director, then the Finance partner, in that order; the next cr_code continues from the highest stored one (CR-0457 first); submit writes Change request with status pending_approval and one Activity row.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: project_code \`IMP-2611\`, reason \`DEMO-TEST 2026-10-26 second user-list wave\`, hours_delta 56, cost_delta 1120000, go_live_delta_days 5, raised_by \`Kenji Arai\`, preview \`true\`; expect result \`preview\`, cr_code \`CR-0457\`, route_json naming Delivery director then Finance partner, and nothing stored; then an empty reason answers \`refused_reason_required\`. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Raise change request answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf485ec79cad1140a9e9a6"}
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: compile_and_save_workflow ok, saved version 1 (13 nodes: 2 guards, project and latest-CR fetches, javascript, a create_record on Change request and one on Activity, 4 returns); not deployed — search_workflows shows definitionVersion 0 live, savedAfterDeploy true
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: test run 6adf494fc79cad1140aa03ab (IMP-2611, hours_delta 56, cost_delta 1120000, go_live_delta_days 5, raised_by Kenji Arai, preview true) COMPLETED with response result "preview", cr_code "CR-0457", route_json [step 1 delivery_director 'Delivery director' pending, step 2 finance_partner 'Finance partner' pending], before_json {budget_hours_planned:1480, currency:jpy, go_live_date:2026-11-16}, after_json {budget_hours_planned:1536, go_live_date:2026-11-21, cost_delta:1120000}
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: empty-reason run 6adf495008750d257cf2a1e2 COMPLETED with response result "refused_reason_required" at the first guard; whitespace-reason run 6adf4951c79cad1140aa045c also answered "refused_reason_required", caught in the script
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: get_records after the tests shows Change request still holds only CR-0455 and CR-0456 (version 0), and no Activity row came from these runs, so nothing was stored
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: security rule 3: the next cr_code and the before plan are read from storage in the same run (highest stored CR-0456, then CR-0457)
Unverified: The submit path (result submitted, Change request created with status pending_approval, and one Activity row) was not run, because its only possible code is CR-0457, which the demo raises live. Check: after the demo raises CR-0457, get_records on OBJ_cucmd_change_request CR-0457 should show status pending_approval, next_approver delivery_director and route_json with 2 pending steps.
Unverified: Run outputs are quoted from trigger_workflow_run's finished-run node details; inspect_workflow_run was not called separately.
Unverified: Security: approver_role, approver_name and raised_by are taken from the caller (the app's persona switcher, by the spec's design: no tenant roles are made), so the automations cannot tell who is really approving — needs the person to accept that for the demo, or an admin to make tenant roles the automation can check against USER
Note: assumed: a blank or unknown project answers result refused_project_not_found and writes nothing. That word is not in the contract's result list.
Note: assumed: go_live_delta_days is in calendar days, as the stored CR-0456 shows (2026-12-07 + 7 = 2026-12-14). before_json and after_json keep the stored rows' keys and add go_live_date_ms in epoch ms.
Note: assumed: route_json steps are {step, role, label, name, decision: pending, at, reason}. Decide change request fills the step in when an approver decides.
Note: The Task object (OBJ_cucmd_task) listed in the brief is not read: nothing in the contract needs it.
Note: handover: Raise change request 6adf485ec79cad1140a9e9a6 saved version 1 is the logic version to deploy; the live deployment is still the shell, version 0. Its route_json pending steps are what Decide change request expects.

### t6 · Deploy ClickUp Command · Raise change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Raise change request\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Raise change request\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Raise change request deployed with definitionVersion equal to the logic task's saved version.
Result IDs: {"entity":"6adf485ec79cad1140a9e9a6"}
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: before deploying, search_workflows showed saved version 1, the version the logic task tested, so nothing was saved in between
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: deploy_workflow ok:true, workflowVersion 1, storedVersion 1, deployedVersion 2, paused false, deploymentNotes 'ClickUp Delivery Command demo: Raise change request'
Read back: ClickUp Command · Raise change request 6adf485ec79cad1140a9e9a6: search_workflows deployment {status: DEPLOYED, definitionVersion: 1, deployedAt: 1793018384042, savedAfterDeploy: false}, so definitionVersion 1 equals the logic task's saved version 1
Note: The deploy was made on the person's yes given through plan confirm.

### t7 · Shell for ClickUp Command · Decide change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Decide change request\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs cr_code, approver_role (text: delivery_director \| finance_partner), approver_name, decision (text: approve \| reject), reason (text), and \`result\` = outputs result (text: step_approved \| approved \| rejected \| refused_reason_required \| refused_not_your_turn), next_approver (text), new_go_live (number, epoch ms), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Decide change request\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Decide change request deployed.
Result IDs: {"entity":"6adf485ff3cd5f19ed4ac6fd"}
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: search_workflows before create found no automation of that name; compile_and_save_workflow created it at version 0 (callables_from_automation, 2 nodes)
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: deploy_workflow ok:true, workflowVersion 0, deployedVersion 1, paused false, deploymentNotes 'Contract shell for ClickUp Command · Decide change request'
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, savedAfterDeploy: false} right after the shell deploy
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: describe_callable_workflow lists 5 inputs cr_code, approver_role, approver_name, decision, reason (all string)
Note: The result schema declares result, next_approver, new_go_live.

### t8 · Logic for ClickUp Command · Decide change request

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Change request (\`OBJ_cucmd_change_request\`), Project (\`OBJ_cucmd_project\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Decide change request does exactly this, with the shell's inputs and outputs unchanged: callable; inputs cr_code, approver_role (text: delivery_director \| finance_partner), approver_name, decision (text: approve \| reject), reason (text); outputs result (text: step_approved \| approved \| rejected \| refused_reason_required \| refused_not_your_turn), next_approver (text), new_go_live (number, epoch ms); a reject with an empty reason writes nothing and answers refused_reason_required; an approver who is not next answers refused_not_your_turn; the last approval sets status approved, moves the Project go_live_date by go_live_delta_days, adds hours_delta to budget_hours_planned, and writes one Activity row; every decision appends to route_json.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: cr_code \`CR-0456\` (already rejected) and approver_role \`finance_partner\`, decision \`reject\`, reason empty: expect \`refused_reason_required\` and nothing written; then approver_role \`delivery_director\` on \`CR-0455\` (already approved): expect \`refused_not_your_turn\` and nothing written. Never decide CR-0457: the demo raises it live. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Decide change request answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf485ff3cd5f19ed4ac6fd"}
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: compile_and_save_workflow ok, saved version 1 (15 nodes: reason guard, CR fetch, missing-CR guard, project fetch, javascript, CR upsert, project upsert on the last approval, Activity create, 4 returns); not deployed — search_workflows shows definitionVersion 0 live, savedAfterDeploy true
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: run 6adf498597a3bf334d3f0129 (CR-0456, finance_partner, reject, reason empty) COMPLETED with response result "refused_reason_required"; it stopped at the first guard before any read or write
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: run 6adf49866112da3e23ba1db8 (CR-0455, delivery_director, approve) COMPLETED with response result "refused_not_your_turn" (the CR's status is approved and next_approver none); it ended on the refusal return, and no upsert or create ran
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: all-blank run 6adf498708750d257cf2b993 COMPLETED with response result "refused_not_your_turn" (no such CR)
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: get_records after the tests shows CR-0455 (approved) and CR-0456 (rejected) still at version 0, with no new Activity row from these runs, so nothing was written; CR-0457 was not touched
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: security rule 3: the CR's status and next_approver are read from storage in the same run before any decision is accepted
Unverified: The step_approved, approved and rejected paths (CR upsert, Project go_live_date and budget_hours_planned upsert, Activity row) were not run on the tenant: the only pending change request will be CR-0457, which must not be decided. The script was checked locally with a pending 56-hour CR: DD approve gave step_approved, next finance_partner; a second DD approve gave refused_not_your_turn; FP approve gave approved, go-live 2026-11-16 to 2026-11-21, hours 1480 to 1536. Check: after the demo decides CR-0457, get_records on IMP-2611 should show go_live_date and budget_hours_planned moved, plus one Activity row per decision.
Unverified: Run outputs are quoted from trigger_workflow_run's finished-run node details; inspect_workflow_run was not called separately.
Unverified: Security: approver_role, approver_name and raised_by are taken from the caller (the app's persona switcher, by the spec's design: no tenant roles are made), so the automations cannot tell who is really approving — needs the person to accept that for the demo, or an admin to make tenant roles the automation can check against USER
Note: assumed: every decision (step approval, final approval, reject) writes one Activity row (action approved or rejected), since the Activity object is the audit log; the contract names the Activity row only for the last approval.
Note: assumed: a blank or unknown cr_code, an invalid role, or an invalid decision answers refused_not_your_turn. The go-live moves by go_live_delta_days calendar days, matching how Raise computes after_json.
Note: assumed: route_json is updated by filling in the matching pending step (name, decision, at = YYYY-MM-DD, reason), or by appending a step when none is pending for that role. rejection_reason is set on a reject.
Note: handover: Decide change request 6adf485ff3cd5f19ed4ac6fd saved version 1 is the logic version to deploy; the live deployment is still the shell, version 0.

### t9 · Deploy ClickUp Command · Decide change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Decide change request\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Decide change request\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Decide change request deployed with definitionVersion equal to the logic task's saved version.
Result IDs: {"entity":"6adf485ff3cd5f19ed4ac6fd"}
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: before deploying, search_workflows showed saved version 1, the version the logic task tested, so nothing was saved in between
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: deploy_workflow ok:true, workflowVersion 1, storedVersion 1, deployedVersion 2, paused false, deploymentNotes 'ClickUp Delivery Command demo: Decide change request'
Read back: ClickUp Command · Decide change request 6adf485ff3cd5f19ed4ac6fd: search_workflows deployment {status: DEPLOYED, definitionVersion: 1, deployedAt: 1793018386786, savedAfterDeploy: false}, so definitionVersion 1 equals the logic task's saved version 1
Note: The deploy was made on the person's yes given through plan confirm.

