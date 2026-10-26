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
| t1 | automation-shell | ClickUp Command · Book consultant |  | running | 1 |
| t2 | automation | ClickUp Command · Book consultant | t1 | running | 1 |
| t3 | deploy | ClickUp Command · Book consultant | t2 | pending | 0 |
| t4 | automation-shell | ClickUp Command · Timesheet action |  | running | 1 |
| t5 | automation | ClickUp Command · Timesheet action | t4 | running | 1 |
| t6 | deploy | ClickUp Command · Timesheet action | t5 | pending | 0 |
| t7 | automation-shell | ClickUp Command · Portal action |  | running | 1 |
| t8 | automation | ClickUp Command · Portal action | t7 | running | 1 |
| t9 | deploy | ClickUp Command · Portal action | t8 | pending | 0 |

### t1 · Shell for ClickUp Command · Book consultant

Body:
Read: \`search_workflows\` for \`ClickUp Command · Book consultant\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs person_code, project_code (text), first_week (number, epoch ms), weeks, hours_per_week (number), confirm (boolean), and \`result\` = outputs result (text: saved \| over_capacity), overages_json (text: each week with booked hours, percent of capacity and hours over), booking_code (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Book consultant\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Book consultant deployed.

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

### t9 · Deploy ClickUp Command · Portal action

Body:
Read: \`search_workflows\` for \`ClickUp Command · Portal action\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Portal action\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Portal action deployed with definitionVersion equal to the logic task's saved version.

