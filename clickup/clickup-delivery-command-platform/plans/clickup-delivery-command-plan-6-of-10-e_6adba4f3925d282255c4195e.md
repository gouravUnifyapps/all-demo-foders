---
nebula: 3
specId: "e_6adba4f10881d2257aa3c07b"
mode: "sonic"
title: "ClickUp Delivery Command · plan 6 of 10"
owner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Change request"},{"action":"deploy","kind":"automation","name":"Delivery Command · Accept proposed tasks"},{"action":"deploy","kind":"automation","name":"Delivery Command · Publish status report"},{"action":"deploy","kind":"automation","name":"Delivery Command · Record sign-off"},{"action":"deploy","kind":"automation","name":"Delivery Command · Book training slot"}]
touches: [{"kind":"automation","name":"Delivery Command · Change request"},{"kind":"automation","name":"Delivery Command · Accept proposed tasks"},{"kind":"automation","name":"Delivery Command · Publish status report"},{"kind":"automation","name":"Delivery Command · Record sign-off"},{"kind":"automation","name":"Delivery Command · Book training slot"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "d233a736-734b-4783-a31c-f5541a3c1be8"
pageDesign: 2
createdAt: "2026-10-23T18:18:27.107Z"
runningAt: "2026-10-23T18:18:30.152Z"
runner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"382b1b0f-8b04-5591-805d-15b67bc592e7"}
---
## Plan

Goal: ClickUp Delivery Command · plan 6 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Delivery Command · Change request |  | done | 1 |
| t2 | deploy | Delivery Command · Change request | t1 | running | 1 |
| t3 | automation | Delivery Command · Accept proposed tasks |  | done | 1 |
| t4 | deploy | Delivery Command · Accept proposed tasks | t3 | running | 1 |
| t5 | automation | Delivery Command · Publish status report |  | done | 1 |
| t6 | deploy | Delivery Command · Publish status report | t5 | done | 1 |
| t7 | automation | Delivery Command · Record sign-off |  | done | 1 |
| t8 | deploy | Delivery Command · Record sign-off | t7 | running | 1 |
| t9 | automation | Delivery Command · Book training slot |  | done | 1 |
| t10 | deploy | Delivery Command · Book training slot | t9 | running | 1 |

### t1 · Build automation Delivery Command · Change request

Body:
Read: \`entity context automation --name "Delivery Command · Change request" --json\` and search_workflows for "Delivery Command · Change request"; if it exists, stop and report. describe_storage_object for each object it reads or writes: Delivery Command · Change request (\`OBJ_dcmd_change_request\`), Delivery Command · Task (\`OBJ_dcmd_task\`), Delivery Command · Project (\`OBJ_dcmd_project\`), Delivery Command · Activity (\`OBJ_dcmd_activity\`), Delivery Command · Person (\`OBJ_dcmd_person\`).
Done when: automation Delivery Command · Change request ("Submits, routes, approves and rejects change requests by the 40-hour rule.") is saved with exactly this contract and logic: callable; input action text (submit, approve, reject), cr_id text, project_id text, raised_by text, reason text, work_added text, work_removed text, hours_delta number, cost_delta number, golive_after date, plan_before text, plan_after text, actor text, reject_reason text; submit sets route director when hours_delta is under 40 and director_finance when 40 or more, next_approver Elena Brooks; approve by the director on director_finance sets next_approver Tomás Herrera; the last approval sets status approved, adds the change's tasks from plan_after, moves the project's go_live and budget_hours and writes Activity rows; reject with an empty reject_reason is refused with "A rejection needs a written reason. Add one and reject again."; result cr_id text, status text, route text, next_approver text, refused boolean, message text.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id, removed by those ids afterwards); do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Change request with the contract above, and a test run answers the result fields.
Result IDs: {"entity":"6adba6a8cac0655fe3582da3"}
Read back: Delivery Command · Change request 6adba6a8cac0655fe3582da3: compile_and_save_workflow ok, created:true, version 0, 51 nodes; trigger CALLABLE callables/callables_from_automation; open_workflow version 0, deployment null (not deployed)
Read back: Delivery Command · Change request: describe_callable_workflow answers 14 inputs action string (enum submit, approve, reject; required), cr_id, project_id, raised_by, reason, work_added, work_removed string, hours_delta number, cost_delta number, golive_after integer (format date), plan_before, plan_after string, actor string (required), reject_reason string
Read back: Delivery Command · Change request: open_workflow result schema { cr_id: string, status: string, route: string, next_approver: string, refused: boolean, message: string }
Read back: Delivery Command · Change request run 6adba6bcca4f9d20459b6601 (submit DEMO-TEST-CR-1, 48 h): {cr_id:DEMO-TEST-CR-1, status:pending_approval, route:director_finance, next_approver:Elena Brooks, refused:false, message:'Sent to Elena Brooks for approval.'}
Read back: Delivery Command · Change request run 6adba6beca4f9d20459b66c3 (submit DEMO-TEST-CR-2, 8 h): {route:director, next_approver:Elena Brooks, status:pending_approval, refused:false}
Read back: Delivery Command · Change request run 6adba6c6ca4f9d20459b6adc (approve by Elena Brooks on director_finance): {status:pending_approval, next_approver:'Tomás Herrera', refused:false}
Read back: Delivery Command · Change request run 6adba6ccf4431f44e30a2a4c (approve by Tomás Herrera): {status:approved, route:director_finance, next_approver:'', refused:false, message:'Approved. The plan, go-live and budget are updated.'}; get_records: DEMO-TEST-PRJ-1 go_live 1797465600000 -&gt; 1798675200000, budget_hours 100 -&gt; 148; tasks TSK-DEMO-TEST-CR-1-1 'SSO for contractors' and TSK-DEMO-TEST-CR-1-2 'SSO regression test' (status not_started, stage configuration); Activity ACT-6adba6ccf4431f44e30a2a4c-1 cr_approved and -2 golive_changed, source automation, actor Tomás Herrera
Read back: Delivery Command · Change request run 6adba6c592718f6a64f4341d (reject, blank reason): {refused:true, message:'A rejection needs a written reason. Add one and reject again.'} and no read or write node ran
Read back: Delivery Command · Change request run 6adba6d0ca4f9d20459b7026 (reject DEMO-TEST-CR-2 with reason): {status:rejected, refused:false}; get_records DEMO-TEST-CR-2 status rejected, step1_status rejected, step1_by Elena Brooks, reject_reason 'DEMO-TEST out of scope'
Read back: Delivery Command · Change request run 6adba6c4f3cd5f19ed89557a (approve by Mei Takahashi, not the next approver): {refused:true, message:'Only Elena Brooks can decide this step.'}; run 6adba6b56112da3e23fd9718 (all blank): {refused:true, message:'Sign in before you act on a change request.'}
Read back: Security (rule 3): approve and reject re-read the change request in the same run and branch on its stored status pending_approval, route, step1_status and next_approver, never on caller flags
Read back: Delivery Command · Change request 6adba6a8cac0655fe3582da3 (retry, live): search_workflows version 0, nodeCount 51, deployment null (not deployed); describe_callable_workflow still answers the 14 inputs above
Read back: Delivery Command · Change request test rows still present (get_records, live): DEMO-TEST-CR-1 status approved, DEMO-TEST-CR-2 status rejected, DEMO-TEST-PRJ-1 budget_hours 148, TSK-DEMO-TEST-CR-1-1/-2 present, 6 own Activity rows present
Unverified: Security: who approves is checked against the caller-supplied actor name (stored next_approver), not against the platform user (USER.id) — needs the person to decide whether Person rows should be mapped to platform users so the automation can check the signed-in user; check: a call with actor 'Elena Brooks' from a different signed-in user is accepted today
Unverified: assumed: plan_after is read as one task per line; when any line starts with '+', only those lines become tasks (a JSON array of {title, hours} is also accepted); hours_planned is 0 unless given — check with the page author what plan_after text the Change request page sends
Unverified: assumed: a blank cr_id on submit gets a new id 'CR-' + last 6 digits of the epoch ms; collision-free is not guaranteed — check: two submits in the same millisecond window
Note: Refusals beyond the spec, with their own messages: blank actor, submit without project_id or hours_delta, unknown project, a second submit of a non-draft CR, unknown CR, CR not pending_approval, actor not the stored next_approver, unknown action. Each writes nothing.
Note: Submit writes the CR with storage update_record_by_id upsert:true (a new row is meant); it sets currency and golive_before from the project, step1_status pending, step2_status not_needed (under 40 h) or waiting (40 h or more), status pending_approval.
Note: The last approval moves go_live with SET (skipIfBlank true, so a blank golive_after leaves go_live alone) and budget_hours with INCREMENT by hours_delta.
Note: Activity detail renders hours from the stored number as '48.0 h' (the store returns whole numbers as floats); cosmetic.
Note: handover: Change request is callable 6adba6a8cac0655fe3582da3; approve/reject require actor to equal the stored next_approver person name (Elena Brooks, then Tomás Herrera on director_finance), so the page must send the Person name as actor.
Note: feature:
Feature: A compact reply mode for trigger_workflow_run (status, response, and only the failed or named nodes) instead of every node's definition, run input and output.
Evidence: Each test run of this 51-node callable returned 15-30k characters, repeating the trigger's setup and result schema twice per run, while the verdict needed only status and response; 25 test runs across five automations were needed for one batch.
Benefit: Testing every outcome of an automation costs a fraction of the context, so a builder can test more cases in one batch.
Scope: automation-code MCP trigger_workflow_run reply shape; non-goal: changing inspect_workflow_run, which stays the place for full node detail.
Acceptance: trigger_workflow_run with a compact flag returns runId, status, response and failed nodes only, under 2k characters for a completed run.
Note: Left behind for cleanup (DEMO-TEST rows, not deleted): OBJ_dcmd_change_request: DEMO-TEST-CR-1, DEMO-TEST-CR-2 \| OBJ_dcmd_project: DEMO-TEST-PRJ-1 \| OBJ_dcmd_task: TSK-DEMO-TEST-CR-1-1, TSK-DEMO-TEST-CR-1-2 \| OBJ_dcmd_activity: ACT-6adba6bcca4f9d20459b6601, ACT-6adba6beca4f9d20459b66c3, ACT-6adba6c6ca4f9d20459b6adc, ACT-6adba6ccf4431f44e30a2a4c-1, ACT-6adba6ccf4431f44e30a2a4c-2, ACT-6adba6d0ca4f9d20459b7026 (also t5's ACT-6adba5d7f4431f44e309cf75 and t7's ACT-6adba607eb71d135d657e445, listed under those tasks). The Activity and task rows have no DEMO-TEST in the ACT- id but belong to project DEMO-TEST-PRJ-1.
Note: Answer from the person: 'No one can approve deletes in this unattended run (CONFIRM_REQUIRED needs the person). Do not delete: keep the test rows as they are, each labelled DEMO-TEST, and finish the task without the cleanup.' No delete was sent.

### t2 · Deploy Delivery Command · Change request

Body:
Read: search_workflows for "Delivery Command · Change request" and its saved version from the logic task's read-back.
Done when: Delivery Command · Change request is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Change request".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Change request deployed with definitionVersion equal to the saved version.

### t3 · Build automation Delivery Command · Accept proposed tasks

Body:
Read: \`entity context automation --name "Delivery Command · Accept proposed tasks" --json\` and search_workflows for "Delivery Command · Accept proposed tasks"; if it exists, stop and report. describe_storage_object for each object it reads or writes: Delivery Command · AI output (\`OBJ_dcmd_ai_output\`), Delivery Command · Task (\`OBJ_dcmd_task\`).
Done when: automation Delivery Command · Accept proposed tasks ("Turns accepted Copilot task proposals into tasks.") is saved with exactly this contract and logic: callable; input output_ids list of text, decision text (accept or reject), actor text; accept creates one Task per output and sets the output accepted; reject sets it rejected and creates nothing; result created list of task_id.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id, removed by those ids afterwards); do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Accept proposed tasks with the contract above, and a test run answers the result fields.
Result IDs: {"entity":"6adba625ca4f9d2045986507"}
Read back: Delivery Command · Accept proposed tasks 6adba625ca4f9d2045986507: compile_and_save_workflow ok, created:true, version 0; trigger CALLABLE callables/callables_from_automation; open_workflow version 0, deployment null
Read back: Delivery Command · Accept proposed tasks: describe_callable_workflow answers output_ids array of string (required), decision string enum accept, reject (required), actor string (required)
Read back: Delivery Command · Accept proposed tasks: open_workflow result schema { created: array of string }
Read back: Delivery Command · Accept proposed tasks run 6adba63692718f6a64f426db (accept DEMO-TEST-AIO-1, AIO-03, DEMO-TEST-NOPE): {created:['TSK-DEMO-TEST-AIO-1']}; AIO-03 (a meeting_summary) and the unknown id were skipped; get_records TSK-DEMO-TEST-AIO-1 project IMP-2611, title 'DEMO-TEST proposed task one', stage data_migration, status not_started, ai_proposed true
Read back: Delivery Command · Accept proposed tasks run 6adba63bca4f9d2045991630 (reject DEMO-TEST-AIO-2): {created:[]}, the update node set DEMO-TEST-AIO-2 status rejected and no create node ran
Read back: Delivery Command · Accept proposed tasks run 6adba631eb71d135d657ea21 (all blank): {created:[]}, no read or write ran
Read back: Security (rule 3): each proposal is re-read by id in the run and acted on only when kind is proposed_task and status is proposed
Read back: Delivery Command · Accept proposed tasks 6adba625ca4f9d2045986507 (retry, live): search_workflows version 0, nodeCount 14, deployment null; describe_callable_workflow still answers output_ids array, decision enum accept/reject, actor
Read back: Delivery Command · Accept proposed tasks test rows still present (get_records, live): DEMO-TEST-AIO-1 accepted, DEMO-TEST-AIO-2 rejected, TSK-DEMO-TEST-AIO-1 'DEMO-TEST proposed task one'
Unverified: Security: actor is accepted but not checked against the platform user (USER.id) — needs the person to decide who may accept proposals; check: a call from any signed-in user is accepted
Note: Each created task gets task_id 'TSK-' + output_id, the project's current stage, status not_started, critical false, hours_logged 0, ai_proposed true; the proposal is then set accepted. No Activity row is written (the contract names none).
Note: A proposal that is not a proposed_task, not in status proposed, or not found is skipped silently, so a repeat call creates nothing twice.
Note: Left behind for cleanup (DEMO-TEST rows, not deleted): OBJ_dcmd_ai_output: DEMO-TEST-AIO-1, DEMO-TEST-AIO-2 (and t5's AIO-6adba5d7f4431f44e309cf75 on project DEMO-TEST-PRJ) \| OBJ_dcmd_task: TSK-DEMO-TEST-AIO-1 (on real project IMP-2611, so it shows on that project's board until deleted).
Note: Answer from the person: 'No one can approve deletes in this unattended run (CONFIRM_REQUIRED needs the person). Do not delete: keep the test rows as they are, each labelled DEMO-TEST, and finish the task without the cleanup.' No delete was sent.

### t4 · Deploy Delivery Command · Accept proposed tasks

Body:
Read: search_workflows for "Delivery Command · Accept proposed tasks" and its saved version from the logic task's read-back.
Done when: Delivery Command · Accept proposed tasks is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Accept proposed tasks".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Accept proposed tasks deployed with definitionVersion equal to the saved version.

### t5 · Build automation Delivery Command · Publish status report

Body:
Read: \`entity context automation --name "Delivery Command · Publish status report" --json\` and search_workflows for "Delivery Command · Publish status report"; if it exists, stop and report. describe_storage_object for each object it reads or writes: Delivery Command · AI output (\`OBJ_dcmd_ai_output\`), Delivery Command · Activity (\`OBJ_dcmd_activity\`).
Done when: automation Delivery Command · Publish status report ("Publishes the lead's edited status report.") is saved with exactly this contract and logic: callable; input project_id text, title text, body text, actor text; saves an AI output of kind status_report with status published and ai_written true, writes one Activity row; result output_id text.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id, removed by those ids afterwards); do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Publish status report with the contract above, and a test run answers the result fields.
Result IDs: {"entity":"6adba5cfeb71d135d657c23d"}
Read back: Delivery Command · Publish status report 6adba5cfeb71d135d657c23d: compile_and_save_workflow ok, created:true, version 0; trigger CALLABLE callables/callables_from_automation; open_workflow version 0, deployment null
Read back: Delivery Command · Publish status report: describe_callable_workflow answers project_id, title, body, actor, all string and required
Read back: Delivery Command · Publish status report: open_workflow result schema { output_id: string }
Read back: Delivery Command · Publish status report run 6adba5d7f4431f44e309cf75: {output_id:'AIO-6adba5d7f4431f44e309cf75'}; the create node stored kind status_report, status published, ai_written true, created_at 1792779735124; Activity ACT-6adba5d7f4431f44e309cf75 action status_report_published, source automation, actor Mei Takahashi (get_records)
Read back: Delivery Command · Publish status report run 6adba5d8f4431f44e309cf81 (all blank): {output_id:''} and no write node ran
Unverified: Security: actor is caller-supplied text, not checked against USER.id or the project's lead — needs the person to decide who may publish; check: any caller can publish for any project_id
Unverified: assumed: the automation does not check that project_id exists, so a report for an unknown project is saved; check: run with project_id 'NOPE' and see a row saved
Note: output_id and activity_id are 'AIO-' / 'ACT-' + the run's execution id, unique per run.
Note: Its test rows (OBJ_dcmd_ai_output AIO-6adba5d7f4431f44e309cf75 on project DEMO-TEST-PRJ, OBJ_dcmd_activity ACT-6adba5d7f4431f44e309cf75) are inside t3's CONFIRM_REQUIRED (d_a7960b) and t1's CONFIRM_REQUIRED (d_1daff6) deletes; until then they sit on the non-existent project DEMO-TEST-PRJ, so no project page shows them.

### t6 · Deploy Delivery Command · Publish status report

Body:
Read: search_workflows for "Delivery Command · Publish status report" and its saved version from the logic task's read-back.
Done when: Delivery Command · Publish status report is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Publish status report".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Publish status report deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6adba5cfeb71d135d657c23d"}
Read back: Delivery Command · Publish status report 6adba5cfeb71d135d657c23d: before deploy search_workflows version 0, deployment null (matches t5's saved and tested version 0)
Read back: Delivery Command · Publish status report 6adba5cfeb71d135d657c23d: deploy_workflow ok:true, workflowVersion 0, deployedVersion 1, paused false, message 'Deployed version 0 of automation 6adba5cfeb71d135d657c23d.'
Read back: Delivery Command · Publish status report 6adba5cfeb71d135d657c23d: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, deployedAt: 1792780185136, savedAfterDeploy: false}; definitionVersion 0 equals saved version 0
Note: Deploy released on the plan's approval: 'yes, deploy Delivery Command · Publish status report. The spec the person accepted names it under Ready when, so it is already approved'.

### t7 · Build automation Delivery Command · Record sign-off

Body:
Read: \`entity context automation --name "Delivery Command · Record sign-off" --json\` and search_workflows for "Delivery Command · Record sign-off"; if it exists, stop and report. describe_storage_object for each object it reads or writes: Delivery Command · Sign-off (\`OBJ_dcmd_signoff\`), Delivery Command · Activity (\`OBJ_dcmd_activity\`), Delivery Command · Notification (\`OBJ_dcmd_notification\`), Delivery Command · Project (\`OBJ_dcmd_project\`).
Done when: automation Delivery Command · Record sign-off ("Records a sponsor's sign-off or change request.") is saved with exactly this contract and logic: callable; input signoff_id text, decision text (sign_off or request_changes), comment text, actor text; request_changes with an empty comment is refused with "Add a comment so the team knows what to change."; saves decided_by and decided_at, writes one Activity row and one Notification for the project lead; result status text, decided_at datetime, refused boolean, message text.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id, removed by those ids afterwards); do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Record sign-off with the contract above, and a test run answers the result fields.
Result IDs: {"entity":"6adba5f8eb71d135d657e318"}
Read back: Delivery Command · Record sign-off 6adba5f8eb71d135d657e318: compile_and_save_workflow ok, created:true, version 0; trigger CALLABLE callables/callables_from_automation; open_workflow version 0, deployment null
Read back: Delivery Command · Record sign-off: describe_callable_workflow answers signoff_id string (required), decision string enum sign_off, request_changes (required), comment string, actor string (required)
Read back: Delivery Command · Record sign-off: open_workflow result schema { status: string, decided_at: integer (format date-time), refused: boolean, message: string }
Read back: Delivery Command · Record sign-off run 6adba601c79cad114028b6a3 (request_changes, empty comment): {status:'', decided_at:0, refused:true, message:'Add a comment so the team knows what to change.'}, no read or write ran
Read back: Delivery Command · Record sign-off run 6adba607eb71d135d657e445 (request_changes on DEMO-TEST-SGN-1): {status:changes_requested, decided_at:1792779783914, refused:false, message:'Decision recorded.'}; get_records DEMO-TEST-SGN-1 status changes_requested, decided_by Hana Mori, decided_at 1792779783914; Notification NTF-6adba607eb71d135d657e445 recipient Mei Takahashi (IMP-2611's lead), kind signoff, text 'Hana Mori requested changes on DEMO-TEST deliverable'; Activity ACT-6adba607eb71d135d657e445 written
Read back: Delivery Command · Record sign-off run 6adba603c79cad114028b6e6 (SGN-301, already signed off): {status:signed_off, decided_at:1792459800000, refused:true, message:'This deliverable has already been decided.'}; run 6adba602f3cd5f19ed892e2a (all blank): {refused:true}
Read back: Security (rule 3): the sign-off is re-read in the run and decided only while its stored status is awaiting
Read back: Delivery Command · Record sign-off 6adba5f8eb71d135d657e318 (retry, live): search_workflows version 0, nodeCount 18, deployment null; describe_callable_workflow still answers signoff_id, decision enum sign_off/request_changes, comment, actor
Read back: Delivery Command · Record sign-off test rows still present (get_records, live): DEMO-TEST-SGN-1 changes_requested, NTF-6adba607eb71d135d657e445 recipient Mei Takahashi, ACT-6adba607eb71d135d657e445 changes_requested
Unverified: Security: actor is caller-supplied text, not checked against USER.id or the project's sponsor — needs the person to decide whether the portal's signed-in sponsor must match the project's sponsor; check: any caller can sign off any deliverable
Unverified: The sign_off decision path was not run against a test row (only request_changes was); check: run decision sign_off on a fresh DEMO-TEST sign-off row and read status signed_off
Note: Refusals beyond the spec: blank signoff_id or actor or an unknown decision ('Choose Sign off or Request changes for a deliverable.'), an unknown sign-off, and a deliverable already decided. Each writes nothing.
Note: Left behind for cleanup (DEMO-TEST rows, not deleted): OBJ_dcmd_signoff: DEMO-TEST-SGN-1 \| OBJ_dcmd_notification: NTF-6adba607eb71d135d657e445 (shows in Mei Takahashi's inbox until deleted) \| OBJ_dcmd_activity: ACT-6adba607eb71d135d657e445.
Note: Answer from the person: 'No one can approve deletes in this unattended run (CONFIRM_REQUIRED needs the person). Do not delete: keep the test rows as they are, each labelled DEMO-TEST, and finish the task without the cleanup.' No delete was sent.

### t8 · Deploy Delivery Command · Record sign-off

Body:
Read: search_workflows for "Delivery Command · Record sign-off" and its saved version from the logic task's read-back.
Done when: Delivery Command · Record sign-off is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Record sign-off".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Record sign-off deployed with definitionVersion equal to the saved version.

### t9 · Build automation Delivery Command · Book training slot

Body:
Read: \`entity context automation --name "Delivery Command · Book training slot" --json\` and search_workflows for "Delivery Command · Book training slot"; if it exists, stop and report. describe_storage_object for each object it reads or writes: Delivery Command · Session slot (\`OBJ_dcmd_session_slot\`).
Done when: automation Delivery Command · Book training slot ("Books a free training slot for the sponsor.") is saved with exactly this contract and logic: callable; input slot_id text, actor text; a slot already taken is refused with "This slot was just taken. Choose another time."; result ok boolean, message text.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id, removed by those ids afterwards); do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Book training slot with the contract above, and a test run answers the result fields.
Result IDs: {"entity":"6adba59c92718f6a64f4015a"}
Read back: Delivery Command · Book training slot 6adba59c92718f6a64f4015a: compile_and_save_workflow ok, created:true, version 0; trigger CALLABLE callables/callables_from_automation; open_workflow version 0, deployment null
Read back: Delivery Command · Book training slot: describe_callable_workflow answers slot_id string (required), actor string (required)
Read back: Delivery Command · Book training slot: open_workflow result schema { ok: boolean, message: string }
Read back: Delivery Command · Book training slot run 6adba5a66112da3e23fd651b (SLT-07, taken): {ok:false, message:'This slot was just taken. Choose another time.'}, no write ran
Read back: Delivery Command · Book training slot run 6adba5accac0655fe357f36b (DEMO-TEST-SLT-1, free): {ok:true, message:'Your training slot is booked.'}; get_records DEMO-TEST-SLT-1 taken true (boolean), booked_by Hana Mori
Read back: Delivery Command · Book training slot run 6adba5a76112da3e23fd652a (all blank): {ok:false, message:'Choose a slot and sign in before booking.'}; run 6adba5adf3cd5f19ed88fda1 (unknown slot): {ok:false, message:'This slot no longer exists. Choose another time.'}
Read back: Security (rule 3): the slot is re-read in the run and booked only when its stored taken is not true
Read back: Delivery Command · Book training slot 6adba59c92718f6a64f4015a (retry, live): search_workflows version 0, nodeCount 10, deployment null; describe_callable_workflow still answers slot_id, actor
Read back: Delivery Command · Book training slot test row still present (get_records, live): DEMO-TEST-SLT-1 taken true
Unverified: Security: actor is caller-supplied text, not checked against USER.id or the slot project's sponsor — needs the person to decide whether only the project's sponsor may book; check: any caller can book any slot
Unverified: Two bookings racing between the read and the write could both succeed (read-then-write, no compare-and-set); check: two simultaneous calls on one free slot
Note: update_record_fields_by_id takes setValue as a string, so taken is sent as "true"; the store coerced it to boolean true (read back).
Note: Left behind for cleanup (DEMO-TEST rows, not deleted): OBJ_dcmd_session_slot: DEMO-TEST-SLT-1 (project IMP-2611, taken by Hana Mori; may show in IMP-2611's slot list until deleted).
Note: Answer from the person: 'No one can approve deletes in this unattended run (CONFIRM_REQUIRED needs the person). Do not delete: keep the test rows as they are, each labelled DEMO-TEST, and finish the task without the cleanup.' No delete was sent.

### t10 · Deploy Delivery Command · Book training slot

Body:
Read: search_workflows for "Delivery Command · Book training slot" and its saved version from the logic task's read-back.
Done when: Delivery Command · Book training slot is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Book training slot".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Book training slot deployed with definitionVersion equal to the saved version.

