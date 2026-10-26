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
## Plan

Goal: ClickUp Delivery Command · build 5 of 9: task, change request and approval automations

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation-shell | ClickUp Command · Update task |  | running | 1 |
| t2 | automation | ClickUp Command · Update task | t1 | running | 1 |
| t3 | deploy | ClickUp Command · Update task | t2 | pending | 0 |
| t4 | automation-shell | ClickUp Command · Raise change request |  | running | 1 |
| t5 | automation | ClickUp Command · Raise change request | t4 | running | 1 |
| t6 | deploy | ClickUp Command · Raise change request | t5 | pending | 0 |
| t7 | automation-shell | ClickUp Command · Decide change request |  | running | 1 |
| t8 | automation | ClickUp Command · Decide change request | t7 | running | 1 |
| t9 | deploy | ClickUp Command · Decide change request | t8 | pending | 0 |

### t1 · Shell for ClickUp Command · Update task

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update task\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs task_code (text), action (text: move \| reschedule \| status), to_stage (text), new_start (number, epoch ms), new_end (number, epoch ms), status (text), preview (boolean), and \`result\` = outputs result (text: saved \| preview \| refused), column_count (number), column_limit (number), over_limit (boolean), moved_json (text: each dependent task with its new dates), new_go_live (number, epoch ms), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Update task\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Update task deployed.

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

### t3 · Deploy ClickUp Command · Update task

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update task\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Update task\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Update task deployed with definitionVersion equal to the logic task's saved version.

### t4 · Shell for ClickUp Command · Raise change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Raise change request\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs project_code, reason, work_added, work_removed (text), hours_delta, cost_delta, go_live_delta_days (number), raised_by (text), preview (boolean), and \`result\` = outputs cr_code (text), before_json, after_json, route_json (text), result (text: preview \| submitted \| refused_reason_required), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Raise change request\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Raise change request deployed.

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

### t6 · Deploy ClickUp Command · Raise change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Raise change request\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Raise change request\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Raise change request deployed with definitionVersion equal to the logic task's saved version.

### t7 · Shell for ClickUp Command · Decide change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Decide change request\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs cr_code, approver_role (text: delivery_director \| finance_partner), approver_name, decision (text: approve \| reject), reason (text), and \`result\` = outputs result (text: step_approved \| approved \| rejected \| refused_reason_required \| refused_not_your_turn), next_approver (text), new_go_live (number, epoch ms), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Decide change request\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Decide change request deployed.

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

### t9 · Deploy ClickUp Command · Decide change request

Body:
Read: \`search_workflows\` for \`ClickUp Command · Decide change request\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Decide change request\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Decide change request deployed with definitionVersion equal to the logic task's saved version.

