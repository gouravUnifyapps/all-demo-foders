---
nebula: 3
specId: "e_6adbab740881d2257aa4b599"
mode: "sonic"
title: "ClickUp Delivery Command · plan 8 of 10"
owner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Send executive summary"},{"action":"deploy","kind":"automation","name":"Delivery Command · Weekly executive email schedule"},{"action":"publish","kind":"ai-agent","name":"Delivery Command · Copilot"},{"action":"deploy","kind":"automation","name":"Delivery Command · Ask Copilot"}]
touches: [{"kind":"automation","name":"Delivery Command · Send executive summary"},{"kind":"automation","name":"Delivery Command · Weekly executive email schedule"},{"kind":"ai-agent","name":"Delivery Command · Copilot"},{"kind":"automation","name":"Delivery Command · Ask Copilot"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "35384676-afdc-4f49-8c30-f1e4d08f8e2a"
pageDesign: 2
createdAt: "2026-10-23T18:46:14.398Z"
runningAt: "2026-10-23T18:46:20.521Z"
runner: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"382b1b0f-8b04-5591-805d-15b67bc592e7"}
---
## Plan

Goal: ClickUp Delivery Command · plan 8 of 10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Delivery Command · Send executive summary |  | running | 1 |
| t2 | deploy | Delivery Command · Send executive summary | t1 | pending | 0 |
| t3 | automation | Delivery Command · Weekly executive email schedule | t2 | pending | 0 |
| t4 | deploy | Delivery Command · Weekly executive email schedule | t3 | pending | 0 |
| t5 | ai-agent | Delivery Command · Copilot |  | running | 1 |
| t6 | publish | Delivery Command · Copilot | t5 | pending | 0 |
| t7 | automation | Delivery Command · Ask Copilot | t6 | pending | 0 |
| t8 | deploy | Delivery Command · Ask Copilot | t7 | pending | 0 |

### t1 · Build automation Delivery Command · Send executive summary

Body:
Read: \`entity context automation --name "Delivery Command · Send executive summary" --json\` and search_workflows for "Delivery Command · Send executive summary"; if it exists, stop and report. describe_storage_object for each object it reads or writes: Delivery Command · Weekly metric (\`OBJ_dcmd_weekly_metric\`), Delivery Command · Weekly snapshot (\`OBJ_dcmd_weekly_snapshot\`), Delivery Command · Project (\`OBJ_dcmd_project\`), Delivery Command · Activity (\`OBJ_dcmd_activity\`), Delivery Command · Executive email (\`OBJ_dcmd_exec_email\`).
Done when: automation Delivery Command · Send executive summary ("Composes and sends the weekly executive email for a region.") is saved with exactly this contract and logic: callable; input region text, recipient text; composes the six headline numbers, the bridge and the five biggest movers from Weekly metric, Weekly snapshot, Project and Activity into an HTML email with the ClickUp logo, saves an Executive email row, and sends it on the mail connection named under Assumptions when there is one (status sent), else status preview; result email_id text, status text. No mail connection is named for this demo (the owner has not named one): the automation has no send step, saves the Executive email row with status \`preview\` and the composed html, and answers status preview.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id); never delete a row (no one can approve a delete in this run): leave the test rows in place and list every DEMO-TEST row id, per object, in notes; do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Send executive summary with the contract above, and a test run answers the result fields.

### t2 · Deploy Delivery Command · Send executive summary

Body:
Read: search_workflows for "Delivery Command · Send executive summary" and its saved version from the logic task's read-back.
Done when: Delivery Command · Send executive summary is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Send executive summary".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Send executive summary deployed with definitionVersion equal to the saved version.

### t3 · Build automation Delivery Command · Weekly executive email schedule

Body:
Read: \`entity context automation --name "Delivery Command · Weekly executive email schedule" --json\` and search_workflows for "Delivery Command · Weekly executive email schedule"; if it exists, stop and report. describe_storage_object for each object it reads or writes: none.
Done when: automation Delivery Command · Weekly executive email schedule ("Runs every Monday 08:00 in each region's time zone.") is saved with exactly this contract and logic: scheduled every hour on Sundays 22:00 UTC to Mondays 14:00 UTC; for each region whose local time (Asia/Tokyo, Europe/Berlin, America/New_York) is Monday 08:00 it calls Send executive summary for that region. It calls the deployed Delivery Command · Send executive summary (callable) for each region whose local time is Monday 08:00, with recipient "exec-team@delivery.example"; it writes nothing itself.
Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id); never delete a row (no one can approve a delete in this run): leave the test rows in place and list every DEMO-TEST row id, per object, in notes; do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Weekly executive email schedule with the contract above, and a test run answers the result fields.

### t4 · Deploy Delivery Command · Weekly executive email schedule

Body:
Read: search_workflows for "Delivery Command · Weekly executive email schedule" and its saved version from the logic task's read-back.
Done when: Delivery Command · Weekly executive email schedule is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Weekly executive email schedule".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Weekly executive email schedule deployed with definitionVersion equal to the saved version.

### t5 · Build AI agent Delivery Command · Copilot

Body:
Read: \`entity context ai-agent --name "Delivery Command · Copilot" --json\` and list_agents for "Delivery Command · Copilot"; if it exists, stop and report. The tool automation Delivery Command · Read delivery data is deployed as workflow \`6adbaa4fca4f9d20459bd303\` (callable, input entity text, filters text, limit number; result rows list, count number); read it with describe_entity before binding.
Done when: AI agent Delivery Command · Copilot ("Delivery Copilot", description "Delivery Copilot: a read-only assistant over the delivery data.") exists with instructions: answer delivery questions for ClickUp's implementation team from Read delivery data only, in plain, calm, direct English; name every project by id and customer and link it; when a chart helps, return a chart JSON {type: bar or line, unit, series} with units; draft weekly status reports from a project's tasks, risks and time entries, marked as an AI draft for the lead to edit; decline billing, invoicing, revenue, payroll, hiring and anything outside delivery data, and say plainly when a field the data does not hold is asked for, with what to try instead; never create or change anything; model: Nebula's recommendation; tool: Read delivery data.
Reply format, written into its instructions: every reply is one JSON object {"answer": text, "chart": a JSON text {type, unit, series} or empty, "links": list of {label, route} with route /projects/&lt;project_id&gt;, "refused": boolean}; a declined question (billing, invoicing, revenue, payroll, hiring, or a field the data does not hold) answers refused true with a plain sentence saying it is not in Delivery Command and what to ask instead. Projects are named by project_id and customer. The model is the one list_models recommends. The tool Read delivery data is its only tool, with each input described so the agent fills entity from its list and filters as JSON.
Apply create_agent and add_tools once each, then test with send_test_messages using every question in \`/home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/state/clickup-delivery-command-platform.eval.csv\`.
Read back: get_agent quoting the instructions' first line, the model and the one tool; each test question with the agent's reply quoted beside the file's expected_answer.
Report ids (the agent id as ids.entity), readBack, unverified, notes.

Proof: get_agent shows Delivery Command · Copilot with its model and the tool Read delivery data; send_test_messages answers the first question of the eval file with IMP-2611 and IMP-2633.

### t6 · Publish Delivery Command · Copilot

Body:
Read: get_agent for Delivery Command · Copilot (its id from Built so far).
Done when: Delivery Command · Copilot is published, so Invoke Agent reaches the version with its tool.
Apply publish_agent once.
Read back: get_agent showing the published version, quoted.
Report ids, readBack, unverified, notes.

Proof: get_agent shows Delivery Command · Copilot published.

### t7 · Build automation Delivery Command · Ask Copilot

Body:
Read: \`entity context automation --name "Delivery Command · Ask Copilot" --json\` and search_workflows for "Delivery Command · Ask Copilot"; if it exists, stop and report. describe_storage_object for each object it reads or writes: none.
Done when: automation Delivery Command · Ask Copilot ("Passes a question from the app to Delivery Copilot and returns its answer.") is saved with exactly this contract and logic: callable; input question text, persona text, screen text, project_id text; invokes the Delivery Command · Copilot agent with the question and its context (Invoke Agent, ai_agents_by_unifyapps); result answer text, chart text (JSON {type, unit, series} or empty), links list of {label, route}, refused boolean. It invokes the published AI agent Delivery Command · Copilot (Invoke Agent on ai_agents_by_unifyapps, no connection) with one message holding the question, persona, screen and project_id; the agent replies with one JSON object {answer, chart, links, refused}; the automation parses it and answers those fields, and when the reply is not JSON it answers the reply as answer, chart empty, links empty, refused false.
A callable's start trigger is callables_from_automation, with the input fields and result fields named above and their types; a refusal answers refused true with the exact message and writes nothing. Stored values: picklist codes as the objects define them, dates as epoch ms; an update by a known id sets upsert true only where a new row is meant; every Activity row gets a new activity_id (ACT- plus a unique suffix), at now, the actor and source automation.
Apply: compile_and_save_workflow until it saves clean; then test-run the draft as automation-testing says, with a payload that changes no seeded row (confirm false, a refused case, or rows the test makes itself with DEMO-TEST in their id); never delete a row (no one can approve a delete in this run): leave the test rows in place and list every DEMO-TEST row id, per object, in notes; do not deploy.
Read back: describe_callable_workflow answering the input fields above (for a callable), the result schema from open_workflow, and the test run's id with its output quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: open_workflow shows Delivery Command · Ask Copilot with the contract above, and a test run answers the result fields.

### t8 · Deploy Delivery Command · Ask Copilot

Body:
Read: search_workflows for "Delivery Command · Ask Copilot" and its saved version from the logic task's read-back.
Done when: Delivery Command · Ask Copilot is deployed and its live definition is the version the logic task saved.
Apply deploy_workflow once on its workflowId with deploymentNotes "ClickUp Delivery Command demo v1: Delivery Command · Ask Copilot".
Read back: search_workflows deployment status, deployedAt and definitionVersion, quoted.
Report ids, readBack, unverified, notes.

Proof: search_workflows shows Delivery Command · Ask Copilot deployed with definitionVersion equal to the saved version.

