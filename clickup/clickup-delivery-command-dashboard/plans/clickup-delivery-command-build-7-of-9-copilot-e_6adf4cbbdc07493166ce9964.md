---
nebula: 3
specId: "e_6adf4cb9dc07493166ce9940"
mode: "sonic"
title: "ClickUp Delivery Command · build 7 of 9: Copilot outputs, status report and weekly email automations"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Accept proposed tasks"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Publish status report"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Send executive summary"}]
touches: [{"kind":"automation","name":"ClickUp Command · Accept proposed tasks"},{"kind":"automation","name":"ClickUp Command · Publish status report"},{"kind":"automation","name":"ClickUp Command · Send executive summary"},{"kind":"connection","name":"Gmail","id":"6980e13788c7735877a8311c"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "cccea0a9-fda0-409a-9dc1-4f8008e09ba7"
pageDesign: 2
createdAt: "2026-10-26T12:51:07.580Z"
runningAt: "2026-10-26T12:51:10.576Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
## Plan

Goal: ClickUp Delivery Command · build 7 of 9: Copilot outputs, status report and weekly email automations

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation-shell | ClickUp Command · Accept proposed tasks |  | running | 1 |
| t2 | automation | ClickUp Command · Accept proposed tasks | t1 | running | 1 |
| t3 | deploy | ClickUp Command · Accept proposed tasks | t2 | pending | 0 |
| t4 | automation-shell | ClickUp Command · Publish status report |  | running | 1 |
| t5 | automation | ClickUp Command · Publish status report | t4 | running | 1 |
| t6 | deploy | ClickUp Command · Publish status report | t5 | pending | 0 |
| t7 | automation-shell | ClickUp Command · Send executive summary |  | running | 1 |
| t8 | automation | ClickUp Command · Send executive summary | t7 | running | 1 |
| t9 | deploy | ClickUp Command · Send executive summary | t8 | pending | 0 |

### t1 · Shell for ClickUp Command · Accept proposed tasks

Body:
Read: \`search_workflows\` for \`ClickUp Command · Accept proposed tasks\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs output_codes (text, comma-separated), decision (text: accept \| reject), decided_by (text), and \`result\` = outputs created_task_codes (text), result (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Accept proposed tasks\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Accept proposed tasks deployed.

### t2 · Logic for ClickUp Command · Accept proposed tasks

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: AI output (\`OBJ_cucmd_ai_output\`), Task (\`OBJ_cucmd_task\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Accept proposed tasks does exactly this, with the shell's inputs and outputs unchanged: callable; inputs output_codes (text, comma-separated), decision (text: accept \| reject), decided_by (text); outputs created_task_codes (text), result (text); accept creates one Task per output with source copilot and sets the output's decision; reject creates nothing.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: output_codes \`AI-05\`, decision \`reject\`, decided_by \`DEMO-TEST 2026-10-26\`: expect no task created and result naming the rejection; then set AI-05 back to decision \`proposed\` so the demo starts clean. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Accept proposed tasks answer the result words the body names, quoted from \`inspect_workflow_run\`.

### t3 · Deploy ClickUp Command · Accept proposed tasks

Body:
Read: \`search_workflows\` for \`ClickUp Command · Accept proposed tasks\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Accept proposed tasks\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Accept proposed tasks deployed with definitionVersion equal to the logic task's saved version.

### t4 · Shell for ClickUp Command · Publish status report

Body:
Read: \`search_workflows\` for \`ClickUp Command · Publish status report\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs project_code, body, edited_by (text), and \`result\` = outputs doc_code (text), published_at (number), result (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Publish status report\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Publish status report deployed.

### t5 · Logic for ClickUp Command · Publish status report

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Document (\`OBJ_cucmd_document\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Publish status report does exactly this, with the shell's inputs and outputs unchanged: callable; inputs project_code, body, edited_by (text); outputs doc_code (text), published_at (number), result (text); writes Document kind status_report with ai_written true and edited_by, and one Activity row.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: project_code \`IMP-2604\`, body \`DEMO-TEST 2026-10-26 status report test\`, edited_by \`Mira Lindqvist\`: expect a doc_code and published_at; record the doc_code and the Activity row it made for cleanup. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Publish status report answer the result words the body names, quoted from \`inspect_workflow_run\`.

### t6 · Deploy ClickUp Command · Publish status report

Body:
Read: \`search_workflows\` for \`ClickUp Command · Publish status report\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Publish status report\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Publish status report deployed with definitionVersion equal to the logic task's saved version.

### t7 · Shell for ClickUp Command · Send executive summary

Body:
Read: \`search_workflows\` for \`ClickUp Command · Send executive summary\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs to_email (text), week_start (number), and \`result\` = outputs result (text: sent \| failed), message_id (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Send executive summary\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Send executive summary deployed.

### t8 · Logic for ClickUp Command · Send executive summary

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Weekly metric (\`OBJ_cucmd_weekly_metric\`).
Done when: ClickUp Command · Send executive summary does exactly this, with the shell's inputs and outputs unchanged: callable; inputs to_email (text), week_start (number); outputs result (text: sent \| failed), message_id (text); reads Weekly metric for the week, composes the six headline numbers, the value bridge and the five top movers as HTML with the ClickUp logo, and sends one email through the Gmail connection \`6980e13788c7735877a8311c\` with operation \`gmail_send_email\`, subject starting "DEMO-TEST · ClickUp Delivery Command · weekly summary".
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: to_email \`gourav.mahunta@unifyapps.com\` (the presenter), week_start 2026-10-26 (epoch ms): expect result \`sent\` and a message_id; the subject starts \`DEMO-TEST · ClickUp Delivery Command · weekly summary\`. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Send executive summary answer the result words the body names, quoted from \`inspect_workflow_run\`.

### t9 · Deploy ClickUp Command · Send executive summary

Body:
Read: \`search_workflows\` for \`ClickUp Command · Send executive summary\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Send executive summary\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Send executive summary deployed with definitionVersion equal to the logic task's saved version.

