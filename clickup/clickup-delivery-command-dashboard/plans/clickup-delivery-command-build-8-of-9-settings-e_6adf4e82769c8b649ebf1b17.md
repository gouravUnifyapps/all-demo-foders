---
nebula: 3
specId: "e_6adf4e8008f965795442e816"
mode: "sonic"
title: "ClickUp Delivery Command · build 8 of 9: settings and notification automations, the Copilot agent, the app shell and summary screens"
owner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Update project settings"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Mark notification read"},{"action":"publish","kind":"ai-agent","name":"ClickUp Command Copilot"}]
touches: [{"kind":"automation","name":"ClickUp Command · Update project settings"},{"kind":"automation","name":"ClickUp Command · Mark notification read"},{"kind":"ai-agent","name":"ClickUp Command Copilot"},{"kind":"automation","name":"ClickUp Command · Read delivery data","id":"6adf45fef3cd5f19ed4a76ba"},{"kind":"code-app","name":"ClickUp Delivery Command"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "fb11b4d7-f77d-485f-9dc3-c415975f4277"
pageDesign: 2
createdAt: "2026-10-26T12:58:41.588Z"
runningAt: "2026-10-26T12:58:45.777Z"
runner: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"402e0464-c1ba-5334-8b57-9ece89217092"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: ClickUp Delivery Command · build 8 of 9: settings and notification automations, the Copilot agent, the app shell and summary screens

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation-shell | ClickUp Command · Update project settings |  | done | 1 |
| t2 | automation | ClickUp Command · Update project settings | t1 | done | 1 |
| t3 | deploy | ClickUp Command · Update project settings | t2 | done | 1 |
| t4 | automation-shell | ClickUp Command · Mark notification read |  | done | 1 |
| t5 | automation | ClickUp Command · Mark notification read | t4 | done | 1 |
| t6 | deploy | ClickUp Command · Mark notification read | t5 | done | 1 |
| t7 | ai-agent | ClickUp Command Copilot |  | done | 1 |
| t8 | publish | ClickUp Command Copilot | t7 | done | 1 |
| t9 | code-app | ClickUp Delivery Command |  | done | 1 |
| t10 | code-app | ClickUp Delivery Command | t9 | done | 1 |

### t1 · Shell for ClickUp Command · Update project settings

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update project settings\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs project_code, name (text), region (text), go_live_date (number), budget_hours_planned (number), and \`result\` = outputs result (text: saved \| failed), field_errors_json (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Update project settings\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Update project settings deployed.
Result IDs: {"entity":"6adf4eb5cac0655fe38aef9d"}
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: search_workflows for the name answered totalHits 0 before create; compile_and_save_workflow created:true version 0
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: deploy_workflow ok:true workflowVersion 0, deployedVersion 1, paused false
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: search_workflows deployment {status: DEPLOYED, deployedVersion 1, definitionVersion 0, savedAfterDeploy false}
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: describe_callable_workflow parameters project_code (string, required), name (string), region (string), go_live_date (number), budget_hours_planned (number)
Note: handover: ClickUp Command · Update project settings workflowId 6adf4eb5cac0655fe38aef9d; outputs result, field_errors_json (string)

### t2 · Logic for ClickUp Command · Update project settings

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Project (\`OBJ_cucmd_project\`), Activity (\`OBJ_cucmd_activity\`).
Done when: ClickUp Command · Update project settings does exactly this, with the shell's inputs and outputs unchanged: callable; inputs project_code, name (text), region (text), go_live_date (number), budget_hours_planned (number); outputs result (text: saved \| failed), field_errors_json (text); a go-live date in the past or budget hours below hours used fail with a field error.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: project_code \`IMP-2624\`, go_live_date 2026-01-05 (in the past): expect result \`failed\` with a go_live_date field error; budget_hours_planned 10 (below used 40): expect a budget_hours_planned field error; nothing written. Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Update project settings answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf4eb5cac0655fe38aef9d"}
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: compile_and_save_workflow ok:true version 1, 13 nodes (fetch project, Groovy validation, update_record_fields_by_id, create Activity record), warnings []; not deployed (definitionVersion stays 0)
Read back: ClickUp Command · Update project settings run 6adf4f2e6112da3e23ba86a5 (IMP-2624, go_live_date 1767571200000 = 2026-01-05): COMPLETED, response {"result":"failed","field_errors_json":"{\"go_live_date\":\"Go-live date cannot be in the past.\"}"}
Read back: ClickUp Command · Update project settings run 6adf4f3192718f6a64e5e669 (IMP-2624, budget_hours_planned 10): COMPLETED, response {"result":"failed","field_errors_json":"{\"budget_hours_planned\":\"Budget hours cannot be below the 40 hours already used.\"}"}
Read back: ClickUp Command · Update project settings run 6adf4f34ca4f9d20457f479c (all-blank payload): COMPLETED, response {"result":"failed","field_errors_json":"{\"project_code\":\"Project code is required.\"}"}
Read back: ClickUp Command · Update project settings run 6adf4f3592718f6a64e5e691 (unknown code IMP-9999-DEMO-TEST): COMPLETED, response {"result":"failed","field_errors_json":"{\"project_code\":\"No project has this code.\"}"}
Read back: ClickUp Command · Update project settings: nothing written on refusals: IMP-2624 read back after the runs with version 0, modifiedTime 1793016823705, budget_hours_planned 1900, go_live_date 1805068800000 (unchanged)
Read back: Security rule 3: hours used is read from the stored Project row (budget_hours_used 40 in the Fetch records node), not from the caller
Unverified: ClickUp Command · Update project settings saved path (result saved, fields written, Activity row created) was not run: the task names only refusal tests. Check: a test run on a DEMO-TEST project with a future go_live_date, then read the Project row for go_live_date/budget_hours_planned stored as numbers (setValue is string-typed on update_record_fields_by_id) and the ACT-&lt;executionId&gt; Activity row
Unverified: Security: who may change project settings is not checked (no role or ownership mapping from USER to a project lead exists in the objects) — needs the person to decide whether settings changes are limited to the project lead or a role
Note: assumed: input name is written to Project.customer, since OBJ_cucmd_project has no name column and project cards show the customer as the project name
Note: assumed: only filled fields are written (skipIfBlank true); a blank field keeps its stored value
Note: assumed: region must be a stored code (europe, north_america, japan), else a region field error; go-live counts as past when earlier than today 00:00 UTC
Note: Project update uses update_record_fields_by_id on the record id (= project_code) found by the fetch; that operation has no upsert key, so upsert: true does not apply; the record's existence is checked first
Note: On save it creates one Activity row: activity_code ACT-&lt;RUN.executionId&gt;, action updated, actor USER.name, at RUN.currentTime
Note: Test runs created no rows

### t3 · Deploy ClickUp Command · Update project settings

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update project settings\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Update project settings\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Update project settings deployed with definitionVersion equal to the logic task's saved version.
Result IDs: {"entity":"6adf4eb5cac0655fe38aef9d"}
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: before deploy search_workflows version 1 (the logic task's saved version), savedAfterDeploy true
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: deploy_workflow ok:true workflowVersion 1, storedVersion 1, deployedVersion 2, paused false
Read back: ClickUp Command · Update project settings 6adf4eb5cac0655fe38aef9d: search_workflows deployment {status: DEPLOYED, definitionVersion: 1, deployedAt: 1793019807711, savedAfterDeploy: false}
Note: Answer from the person: yes, deploy ClickUp Command · Update project settings (through plan confirm)

### t4 · Shell for ClickUp Command · Mark notification read

Body:
Read: \`search_workflows\` for \`ClickUp Command · Mark notification read\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs notification_code (text), and \`result\` = outputs result (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Mark notification read\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Mark notification read deployed.
Result IDs: {"entity":"6adf4eb8cac0655fe38aefc9"}
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: search_workflows for the name answered totalHits 0 before create; compile_and_save_workflow created:true version 0
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: deploy_workflow ok:true workflowVersion 0, deployedVersion 1, paused false
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: search_workflows deployment {status: DEPLOYED, deployedVersion 1, definitionVersion 0, savedAfterDeploy false}
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: describe_callable_workflow parameters notification_code (string, required)
Note: handover: ClickUp Command · Mark notification read workflowId 6adf4eb8cac0655fe38aefc9; output result (string)

### t5 · Logic for ClickUp Command · Mark notification read

Body:
Read: \`open_workflow\` on the shell's workflowId from Built so far, and \`describe_storage_object\` for each object it reads or writes: Notification (\`OBJ_cucmd_notification\`).
Done when: ClickUp Command · Mark notification read does exactly this, with the shell's inputs and outputs unchanged: callable; inputs notification_code (text); outputs result (text); sets read true.
Every write sets the record key (\`upsert: true\` on update by id); an Activity row it writes is created, never updated; a refusal writes nothing and returns its result word. Picklists store codes; dates are epoch ms.
\`compile_and_save_workflow\` on that workflowId, fixing every finding until it saves clean. Do not deploy.
Test-run the saved draft with \`trigger_workflow_run\`: notification_code \`N-08\`: expect result saved and read true on N-08 (it is already read, so the demo rows N-01 to N-03 stay unread). Never change the story rows IMP-2611, CR-0457, D-2611-5 or S-01 to S-12 beyond what the test names, and label any row a test makes \`DEMO-TEST 2026-10-26\`, listing its key in notes for cleanup.
Read back: the saved version from \`compile_and_save_workflow\`, and \`inspect_workflow_run\` output of each test run, quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: The test runs of ClickUp Command · Mark notification read answer the result words the body names, quoted from \`inspect_workflow_run\`.
Result IDs: {"entity":"6adf4eb8cac0655fe38aefc9"}
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: compile_and_save_workflow ok:true version 1, 9 nodes (fetch by notification_code, update_record_by_id upsert true with read true), warnings []; not deployed (definitionVersion stays 0)
Read back: ClickUp Command · Mark notification read run 6adf4f3ac79cad1140aa8be3 (N-08): COMPLETED, response {"result":"saved"}; update node output success true, object N-08 version 1, properties.read true
Read back: ClickUp Command · Mark notification read: N-08 read back with fetch_storage_records: read true, version 1, modifiedTime 1793019706449, other fields unchanged
Read back: ClickUp Command · Mark notification read run 6adf4f3b6112da3e23ba8718 (blank notification_code): COMPLETED, response {"result":"failed"}
Read back: ClickUp Command · Mark notification read run 6adf4f3ccac0655fe38af6a8 (unknown N-99-DEMO-TEST): COMPLETED, response {"result":"failed"}, no update node ran
Unverified: Security: the notification's owner (person_code) is not checked against the running user — no mapping from USER.id to person_code exists in the objects; needs the person to say how a signed-in user maps to a person_code
Note: assumed: a blank or unknown notification_code answers result failed
Note: Used update_record_by_id with upsert true and every stored field carried over (read set true), because update_record_fields_by_id refuses a boolean setValue (INVALID_INPUT_TYPE, string only) at compile
Note: Test runs created no rows; N-08 was already read, so only its version and modifiedTime moved

### t6 · Deploy ClickUp Command · Mark notification read

Body:
Read: \`search_workflows\` for \`ClickUp Command · Mark notification read\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Mark notification read\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Mark notification read deployed with definitionVersion equal to the logic task's saved version.
Result IDs: {"entity":"6adf4eb8cac0655fe38aefc9"}
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: before deploy search_workflows version 1 (the logic task's saved version), savedAfterDeploy true
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: deploy_workflow ok:true workflowVersion 1, storedVersion 1, deployedVersion 2, paused false
Read back: ClickUp Command · Mark notification read 6adf4eb8cac0655fe38aefc9: search_workflows deployment {status: DEPLOYED, definitionVersion: 1, deployedAt: 1793019810253, savedAfterDeploy: false}
Note: Answer from the person: yes, deploy ClickUp Command · Mark notification read (through plan confirm)

### t7 · Create AI agent ClickUp Command Copilot

Body:
Read: \`list_agents\` for \`ClickUp Command Copilot\`: it must not exist; if it does, stop and report. \`list_models\` for the models this tenant offers.
Done when: AI agent ClickUp Command Copilot exists, unpublished, with the model Nebula's \`agent-builder\` skill recommends for a read-only data assistant, and with exactly one tool: the deployed callable automation ClickUp Command · Read delivery data (workflowId \`6adf45fef3cd5f19ed4a76ba\`), inputs scope and filters_json, outputs rows_json, row_count and as_of.
Its instructions say, in these words' meaning: answer questions about ClickUp Delivery Command projects, risks, bookings, change requests and weekly metrics only from that tool's rows, name each record by its code (IMP-, CR-, RSK-), use dates as 16 Nov 2026 and money in the contract currency; when asked for a chart, return a JSON block with type, title, unit and series; when asked for a weekly status report, draft it from the project's tasks, risks and time entries with sections Summary, Progress, Risks, Next week; portfolio health counts come from the latest weekly metric; risk predictions come from AI output rows of kind risk_flag with their confidence and evidence; it never changes data, and says changes go through the app (a change request, a booking); billing, invoicing, revenue, payroll and anything not in the rows is declined with what to try instead; plain, calm, direct words, no exclamation marks.
The instructions list the scope codes the tool takes (projects, tasks, risks, bookings, people, change_requests, ai_outputs, weekly_metrics, documents) and how to pass filters_json as field equals value pairs, with date ranges as from and to epoch ms. No knowledge, no skills, no write tools.
Test it with \`send_test_messages\`: "Which Japan projects go live in November and are at risk?" (expect Sakura Mobility IMP-2611, 16 Nov 2026, At risk), "Show go-lives by month as a chart" (expect a JSON block with type, title, unit and series), and "What is the October invoice total?" (expect a calm decline naming what to try instead).
Read back: \`get_agent\` (model, tool, instructions) and the three test answers, quoted.
Report ids (the agent id as ids.entity), readBack, unverified, notes.

Proof: \`get_agent\` shows ClickUp Command Copilot with its one tool, and the test answer names Sakura Mobility, 16 Nov 2026, At risk.
Result IDs: {"entity":"e_6adf4f02dc07493166ced9fa"}
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: list_agents nameContains 'ClickUp Command' returned [] before create; create_agent made it as Advanced (ai-agent), version 5, published false, readiness canRun true, missing []
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: get_agent models runs/picksTask/answerGeneration = e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached), canCallTools true, connectionActive true)
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: get_agent counts tools 1, tasks 0, skills 0, knowledge 0, knowledgeSets 0. Tool e_6adf4f0b08f965795442fe85 'ReadDeliveryData', enabled true, topicId GLOBAL, automationId 6adf45fef3cd5f19ed4a76ba (ClickUp Command · Read delivery data, deployed, inputs scope + filters_json, outputs rows_json, row_count, as_of)
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: get_agent instructions say to answer only from ReadDeliveryData rows, name records by code (IMP-, CR-, RSK-), give dates as 16 Nov 2026 and money in the contract currency, return a chart as a fenced JSON block with type, title, unit and series, write weekly status reports with sections Summary, Progress, Risks, Next week, take portfolio health from the latest weekly metric and risk predictions from ai_outputs kind risk_flag with confidence and evidence, never change data (changes go through the app as a change request or booking), decline billing/invoicing/revenue/payroll with what to try instead, and use no exclamation marks. They list all 9 scope codes and the filters_json field=value and from/to epoch-ms forms
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: trace e_6adf50ba6112da3e23ba9cbc: model called ReadDeliveryData with arguments {"scope": "projects", "filters_json": "{\"region\":\"japan\",\"health\":\"at_risk\",\"go_live_date\":{\"from\":1793491200000,\"to\":1796083199000}}"}. The trace shows ReadDeliveryData offered with its scope and filters_json parameters
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: test 1 (case e_6adf50fc92718f6a64e60c9a) 'Which Japan projects go live in November and are at risk?' answered: "IMP-2611 — Sakura Mobility (Automotive), go-live 16 Nov 2026, stage Go live, health At risk (was On track last week), lead Kenji Arai, sponsor Haruto Mori, contract value JPY 62,400,000"
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: test 2 (case e_6adf50caca4f9d20457f7238) 'Show go-lives by month as a chart' answered with a fenced json block: {"type": "bar", "title": "Go-lives by Month", "unit": "projects", "series": [{"name": "Go-lives", "data": [{"label": "Oct 2026", "value": 2}, {"label": "Nov 2026", "value": 6}, ...]}]}
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: test 3 (case e_6adf5104cac0655fe38b19e7) 'What is the October invoice total?' answered: "I don't have invoicing or billing data in the delivery data I can access. For invoice totals, please check with the finance team or the billing system. I can help instead with delivery-related figures such as contract value, budget hours, bookings or change requests"
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: security (ai-agents, rule 4 least privilege): the only bound tool is the read-only automation, and no write tool, knowledge or skill is attached (get_agent counts above). No secret is in the instructions (rule 5)
Unverified: Security: the runtime also offers the model ClarifyFromUser, think and four environment tools (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy), seen in trace e_6adf50ba6112da3e23ba9cbc toolsOffered. No agent record holds them, so no tool here can remove them — needs a tenant admin to find what injects the Environment* tools and turn them off for this agent. The instructions forbid calling them
Unverified: Test 2 (the chart) ran on draft v4. v5 only added the line that forbids the environment tools. Check: one send_test_message 'Show go-lives by month as a chart' on the current draft
Unverified: The month counts in the chart (Oct 2, Nov 6, Dec 4, Jan 2, Feb 2, Mar 2) were not checked against the project rows. Check: count go_live_date by month in ReadDeliveryData scope projects
Note: Model: the agent-builder skill names no recommended model. The first pick, OpenAI GPT 4.1 (e_ai_agent_openai_gpt_4.1), failed every run with HTTP 500 'insufficient_quota/project_spend_limit_exceeded' on its OpenAI project. The agent now runs on Claude Sonnet 5 (UnifyApps, Vertex, cached) e_6ad496812dd4ba5be70afcc1, which answered every test
Note: generateChartTool and requestClarification are now written off (records created) so the agent returns a chart as a JSON block instead of calling GenerateChartWithBlocks. The GenerateChartWithBlocks tool is no longer offered
Note: Dates: the first runs said 15 Nov 2026 for go_live_date 1794787200000 (which is 16 Nov 2026 00:00 UTC), an off-by-one. The instructions now give UTC anchors and a worked example, and the answer reads 16 Nov 2026
Note: Stored values are lower-case codes (at_risk, japan, jpy). The instructions map them to words (At risk, Japan, JPY)
Note: send_test_messages timed out at the 60 s MCP limit, so the three questions ran one by one with send_test_message
Note: Not published: the publish waits for its own publish task
Note: handover: ClickUp Command Copilot agent id e_6adf4f02dc07493166ced9fa, tool id e_6adf4f0b08f965795442fe85 (ReadDeliveryData), model e_6ad496812dd4ba5be70afcc1
Note: feedback:
Bug: send_test_messages always fails with an MCP timeout after 60 s, though its own description says a call takes several minutes.
Context: agent-builder MCP send_test_messages with 3 questions on agent e_6adf4f02dc07493166ced9fa, runAgainToFindAnswer true.
Where: mcp-tool
Evidence: 'MCP server "plugin:nebula:agent-builder" tool "send_test_messages" timed out after 60s'; no rows came back. Running each question with send_test_message worked.
Cause: Suspected: the bridge or client caps a tool call at 60 s, below the tool's 2.5 min trace wait.
Regression: send_test_messages with 3 tool-using questions returns its rows instead of a 60 s timeout.
Note: feedback:
Bug: The runtime offers the model tools that neither get_agent nor list_capabilities shows, and a capability written off still reaches the model.
Context: new Advanced agent e_6adf4f02dc07493166ced9fa with exactly one bound tool. update_agent capabilities {generateChartTool:false, requestClarification:false} answered record created, on false.
Where: platform
Evidence: read_trace e_6adf50ba6112da3e23ba9cbc toolsOffered: think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy, ReadDeliveryData. get_agent shows capabilities [] and 1 tool. GenerateChartWithBlocks disappeared once written off; ClarifyFromUser stayed.
Cause: Unknown — next check: which runtime layer injects the Environment* tools, and why the requestClarification record does not suppress ClarifyFromUser.
Regression: a new agent with one bound tool and requestClarification off is offered only that tool plus think.
Note: feedback:
Bug: Plan tasks ask for 'the model Nebula's agent-builder skill recommends', but the skill recommends none.
Context: plan e_6adf4e82769c8b649ebf1b17 task t7. Read agent-builder SKILL.md, writing-good-agents.md and nebula-change defaults.md.
Where: nebula
Evidence: no file names a recommended card. The first card picked (OpenAI GPT 4.1, connectionActive true) failed every run with insufficient_quota/project_spend_limit_exceeded.
Cause: Confirmed: the planner refers to a recommendation the skill does not hold.
Regression: the planner's reference resolves to a named rule in agent-builder, or the plan stops using the phrase.

### t8 · Publish AI agent ClickUp Command Copilot

Body:
Read: \`get_agent\` for the agent id the ai-agent task reported in Built so far.
Done when: the agent is published, its published version holding the tool and the instructions the ai-agent task read back.
\`publish_agent\` once, with the note \`ClickUp Delivery Command demo v1\`.
Read back: \`get_agent\` showing the published state and version, quoted.
Report ids (the agent id as ids.entity), readBack, unverified, notes.

Proof: \`get_agent\` shows ClickUp Command Copilot published.
Result IDs: {"entity":"e_6adf4f02dc07493166ced9fa"}
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: publish_agent (confirmed true) returned publishedVersion 5, live true, automationSaid {response: success}
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: get_agent after publish: version 5, published true, needsPublish false, modifiedTime 1793020279577
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: get_agent: the published version 5 holds the one bound tool, ReadDeliveryData e_6adf4f0b08f965795442fe85 (enabled true, automationId 6adf45fef3cd5f19ed4a76ba), and the instructions t7 read back (they begin 'You are ClickUp Command Copilot, the read-only assistant for the ClickUp Delivery Command workspace'). Models runs/picksTask/answerGeneration = e_6ad496812dd4ba5be70afcc1
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: get_agent also lists 2 capability records, both switched off: generateChartTool e_6adf504b769c8b649ebf5c03 and requestClarification e_6adf504b769c8b649ebf5c06, enabled false. These are capability switches, not bound tools
Read back: ClickUp Command Copilot e_6adf4f02dc07493166ced9fa: publish yes, from Answer from the person: 'yes, publish ClickUp Command Copilot. The person said yes to 'Publish the AI agent ClickUp Command Copilot on orbit.uat.unifyapps.com?' through plan confirm'
Unverified: The live agent has no deployment (get_agent deployments []), so nobody can reach it yet. That is expected: no deploy was asked for. Check: list_deployments after a deploy task
Unverified: The published version was not run after the publish. The draft runs in t7 used the same version 5. Check: one copilot chat once the agent is deployed
Note: publish_agent takes no note or deploymentNotes, so the note 'ClickUp Delivery Command demo v1' could not be stored with the publish

### t9 · Create code app ClickUp Delivery Command: the shell

Body:
Read: \`entity context code-app --name "ClickUp Delivery Command" --json\` (a new app: it must not exist), Code Builder's skills (\`list_code_skills\`, \`read_code_skill\`: every \`alwaysInPrompt\` file for \`app-builder\`), and the files under \`/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/\` (client.css, tokens.css, logo.svg, logo-symbol.svg).
Done when: the code app ClickUp Delivery Command exists (\`create_code_app\`, no designSystemId, PRIVATE) and the file \`app/src/styles/design-system.css\` holds, byte for byte, the stylesheet at \`/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/client.css\`, with two \`@import url(...)\` lines at its top for Inter (with tabular figures) and Noto Sans JP and IBM Plex Mono from Google Fonts, and \`app/src/App.tsx\` imports it; the engine-owned files (\`vite.config.ts\`, \`main.tsx\`, \`index.css\`) are untouched.
The left rail is the ClickUp wordmark \`/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/logo.svg\` on a light plate (the collapsed rail and the browser tab icon use \`/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/logo-symbol.svg\`, used as published, never traced, redrawn or recoloured), with navigation Portfolio, Projects, Resourcing, Timesheets, Changes, Admin and the profile at the bottom, on the brand gradient (\`.rail\` from the kit). The top bar carries the current project or view, search, notifications and the profile menu with the persona switcher (Kenji Arai implementation lead, Elena Fischer delivery director, Marcus Bell finance partner, Tom Hale resource manager, Yui Sato consultant, Haruto Mori customer sponsor) and Appearance (light by default, the dark tokens left live), and nothing else; a right-hand Copilot panel slot opens from the top bar.
One route per screen, each an empty screen titled in the client's words for now: \`/summary\` Executive summary, \`/portfolio\` Portfolio, \`/projects/:code\` Project workspace, \`/projects/:code/change\` Change request, \`/changes\` and \`/changes/:code\` Changes, \`/resourcing\` Resourcing, \`/timesheets\` Timesheets, \`/admin\` Admin, \`/portal/home\`, \`/portal/signoffs\`, \`/portal/sessions\`, \`/portal/files\`, \`/portal/checklist\` (the portal with its own shorter top menu Home, Sign-offs, Sessions, Files, Checklist), and \`/m/today\`, \`/m/tasks\`, \`/m/time\`, \`/m/alerts\` (the phone layout with bottom tabs Today, Tasks, Time, Alerts). The default route opens \`/summary\`.
Components come from the class inventory (\`.g1 .g2 .g3 .pad .inner .solid\`, \`.btn .btn-p .btn-s .btn-t\`, \`.tag\`, \`.toolbar .field .chipsel .tblwrap .tbl .pg\`, \`.ai:not(.msg)\`, \`.tile .loop .empty\`, \`.tabs\`, \`.fld .ctl .hint .seg .tog .opt\`, \`.sth .stv .prog .stages\`, \`.canvas .convo .msg\`, \`.pc .faces .av\`, \`.feed\`, \`.chart .spark .delta .legend\`, \`.toast .menu .crumb .note\`), never a second implementation, never a new colour value, never a Tailwind colour, radius, shadow or type utility: Tailwind only for layout the kit has no class for.
Every status shows an icon and a word (On track, At risk, Off track, Signed off, Awaiting sign-off, Over capacity, Pending approval, Approved, Rejected, Blocked, Sync failed, Not started, Draft, Scheduled, Hypercare, Live), never colour alone. Copy is plain, calm and direct, no exclamation marks.
Build locally until \`tsc -b\` and \`vite build\` pass, then hold, push, release, as \`app-code-build\` says.
Read back: the push's \`commit\` and \`files\`; \`get_code_app\` answering that commit as \`head.sha\`; the \`previewUrl\` the green push answered, quoted.
Report ids (the app id as ids.entity), readBack, unverified, notes, and a \`handover:\` note with the app id, the branch, the routes and the preview address for the next task.

Proof: The push's \`commit\` is \`get_code_app\`'s \`head.sha\`, and \`app/src/styles/design-system.css\` equals client.css byte for byte below its font imports.
Result IDs: {"entity":"app-a2a9509a82c1","commit":"34c4f6defb4470355a5003bc499fba973fd22908"}
Read back: ClickUp Delivery Command app-a2a9509a82c1: create_code_app ok (no designSystemId), branch main, first head 7ed9eefe763bfb2242f15aced47d60309ecfe671
Read back: ClickUp Delivery Command app-a2a9509a82c1: push_code_patch committed:true builds:true commit 34c4f6defb4470355a5003bc499fba973fd22908, 29 files incl. app/src/styles/design-system.css (added), app/src/styles/shell.css, app/src/App.tsx, app/index.html, app/public/logo.svg, app/public/logo-symbol.svg, app/src/components/shell/*, app/src/routes/* (Home.tsx deleted); no vite.config.ts, main.tsx or index.css in the files list
Read back: ClickUp Delivery Command app-a2a9509a82c1: get_code_app head.sha 34c4f6defb4470355a5003bc499fba973fd22908 at the time, interfaceRecord mode code, security PRIVATE (update_code_app_settings security type PRIVATE read back stored PRIVATE)
Read back: ClickUp Delivery Command app-a2a9509a82c1: app/src/styles/design-system.css = 2 @import url() lines (Inter with opsz/400-700; Noto Sans JP + IBM Plex Mono) followed by client.css; \`tail -n +3 design-system.css \| cmp - client.css\` answered identical
Read back: ClickUp Delivery Command app-a2a9509a82c1: previewUrl "https://orbit.uat.unifyapps.com/agent-api/preview/b/app-a2a9509a82c1/main/"
Unverified: The shell was not opened in a browser (no [visual] proof): rail, top bar, profile menu, Appearance and Copilot slot rendering is unseen; check: open the previewUrl at /summary
Unverified: The vite bundle hoists both Google Fonts @import lines to the top of the CSS (seen in local dist); that Inter/Noto/Plex actually load under the app's CSP is unseen; check: the preview's network tab for fonts.googleapis.com
Note: handover: app id app-a2a9509a82c1, branch main (not git-linked), preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-a2a9509a82c1/main/, deployed URL https://app-a2a9509a82c1-orbit.tensor-uat.unifyapps.com (not published). Routes: / -&gt; /summary; /summary, /portfolio, /projects, /projects/:code, /projects/:code/change, /changes, /changes/:code, /resourcing, /timesheets, /admin (AppShell: rail + top bar + Copilot slot); /portal/home\|signoffs\|sessions\|files\|checklist (PortalShell, own top menu); /m/today\|tasks\|time\|alerts (PhoneShell, bottom tabs); /login, /forgot-password, /update-password kept.
Note: handover: shell pieces: app/src/components/shell/{AppShell,PortalShell,PhoneShell,ProfileMenu,Notifications,CopilotSlot,ScreenFrame}.tsx, nav.ts (deepest-match rail), app/src/components/status.tsx (StatusTag: icon + word for all 16 statuses), app/src/lib/store.ts (zustand: persona, appearance light default, rail collapse, Copilot open), app/src/lib/dates.ts (formatDay -&gt; '16 Nov 2026'). The Copilot slot (.canvas) says 'Not connected yet' until the Copilot task wires CopilotProvider into CopilotSlot.tsx.
Note: The kit has no \`.rail\` class (only \`.rail-demo\`), so the rail, top bar, portal bar and phone tabs are styled in app/src/styles/shell.css from kit tokens only (gradient var(--sp-deep) to var(--sp-blue), white plate for the logo, white tints at the kit's .22/.28/.72 alphas).
Note: The kit's body font is Archivo; per the spec's typeface line (Inter, Noto Sans JP, IBM Plex Mono), shell.css sets body font-family to Inter, Noto Sans JP with tnum, leaving design-system.css byte-identical.
Note: The persona switcher is a presentation 'View as' (it changes the shown persona and lands on their home screen); it does not change who is signed in, and gates no data. The rail's profile shows the signed-in user's name from useGetApiUserContext. The app's .agents/rules forbid a persona switcher unless asked; this task asks for one.
Note: The app's build script is \`tsc -b &amp;&amp; oxlint -A correctness src &amp;&amp; vite build\`, not the template's two steps; I ran tsc -b, oxlint -A correctness src and vite build locally, all clean, and the engine build passed.
Note: Tab icon: index.html links /logo-symbol.svg (app/public, copied byte for byte) and the title reads ClickUp Delivery Command; the engine's ua:csp and ua:theme-font blocks were left as they were.
Note: feedback:
Bug: A code-app task body tells the builder to read \`entity context code-app --name "&lt;app&gt;" --json\`, but the CLI refuses the kind \`code-app\`.
Context: plan e_6adf4e82769c8b649ebf1b17, task t9 Read line; nebula.mjs entity context with --session.
Where: nebula
Evidence: answered {"error":{"code":"USAGE","message":"Entity context takes solution, app, page, object, automation, ai-agent ..."}}; \`entity context app --name\` answered miss.
Cause: Suspected: the task writer emits \`code-app\` as an entity-context kind the CLI does not accept.
Regression: run a generated code-app task's Read command verbatim; it answers hit/miss, not USAGE.
Note: feedback:
Bug: The plan's code-app shell task names a kit class \`.rail\` that client.css does not define.
Context: plan e_6adf4e82769c8b649ebf1b17 task t9; studio/design-system/clickup/client.css.
Where: nebula
Evidence: client.css defines only \`.rail-demo\` and \`.rail-demo .nav\`; the builder wrote its own \`.rail\` in shell.css from kit tokens.
Cause: Unknown — next check: compare the planner's class inventory with the selectors client.css defines.
Regression: every class a task names exists as a selector in client.css.

### t10 · ClickUp Delivery Command: screen Executive summary and Portfolio

Body:
Read: \`get_code_app\` for the app id the shell task reported in Built so far, its checkout from \`get_branch_codebase\` (main), the app's \`.agents/rules/\`, Code Builder's skills (\`list_code_skills\`, \`read_code_skill\`: every \`alwaysInPrompt\` file for \`app-builder\`, plus \`automation-integration\` and the data skills), \`/home/user/all-demo-foders/clickup/clickup-delivery-command-dashboard/studio/design-system/clickup/client.css\` and the views and beats below.
Done when: screen Executive summary and Portfolio: six \`.tile\` headline numbers with \`.delta\` coloured by good or bad for the business, the value bridge \`.chart\`, the five top movers \`.tbl\`, the Email me this summary \`.btn-s\` and its preview; Portfolio health \`.tile\` counts with change since last week, the risk grid (likelihood against impact, a cell lists its risks), the 90-day go-live timeline grouped by region with slipped dates marked, the 12-week on-track \`.chart\`, the projects \`.tbl\` with \`.toolbar\` search "x of y", facets region, stage, health and lead, removable chips with Clear all, \`.pg\`, and Save view · reads Project, RAID item, Weekly metric, Saved view · calls ClickUp Command · Save view and ClickUp Command · Send executive summary
The regions follow these views, in the order the beats use them: Executive summary \`/summary\` · beat 1 · \`.tile\` ×6 with \`.delta\` · \`.chart\` (value bridge) · \`.tbl\` top movers · \`.btn-s\` Email me this summary + \`.toast\` · \`.note\` last updated \| Portfolio \`/portfolio\` · beats 1, 6 · \`.tile\` ×3 health with \`.delta\` · risk grid as a \`.tbl\` of likelihood × impact cells with \`.tag\` counts, a cell opening its risks · go-live timeline as \`.cal\` grouped by region with \`.tag.attention\` Slipped · \`.chart\` + \`.spark\` 12-week on-track · \`.toolbar\` \`.field\` \`.chipsel\` facets + chips, \`.tblwrap\` \`.tbl\`, \`.pg\`, \`.empty\` · \`.av\` customer initials circles · Copilot panel \`.canvas\`
The beat they serve: beat 1: **Monday: the summary, then the portfolio** · route \`/summary\` then \`/portfolio\` · mode \`live\` (reads), the headline counts \`seeded\` (Weekly metric) · The presenter, as Elena Fischer (Delivery director), opens the executive summary: six headline numbers with changes coloured good or bad (projects at risk 38, +5, red), the value bridge USD 17.8M to 18.4M, the five top movers led by Sakura Mobility. They press Email me this summary (external step: one real \`DEMO-TEST\` email through the tenant's Gmail connection; fallback: the in-app preview). They open Portfolio: health counts 161 / 38 / 15 with week-on-week change, the risk grid with RSK-1183 in the likelihood 4 × impact 5 cell, the 90-day go-live timeline by region with slipped dates marked, the 12-week on-track line 81% to 75%. Filter Region Japan and Health At risk: chips, "1 of 18", Sakura Mobility; Save view "Japan at risk" shared with the Japan team. · asks A6 A7 A8 A11 A13 A14 A15 A16 A17 A18 A48 A49 A50 A59 A62 A65 A70–A73 A90 A97
Data: the app reads Project (\`OBJ_cucmd_project\`), RAID item (\`OBJ_cucmd_raid\`), Weekly metric (\`OBJ_cucmd_weekly_metric\`), Saved view (\`OBJ_cucmd_saved_view\`) through the Storage dataSources (\`create_code_app_data_sources\` kind storage, \`ENTITY.&lt;name&gt;\` set to each object's entity type, made once for the app and extended here), and calls ClickUp Command · Save view (\`6adf460108750d257cf1e381\`), input fields name (text), filters_json (text), owner (text), shared_with (text), outputs view_code (text), result (text: saved \| refused_name_taken); ClickUp Command · Send executive summary (\`6adf4d1508750d257cf3df21\`), input fields to_email (text), week_start (number), outputs result (text: sent \| failed), message_id (text), each through its own automation dataSource (kind automation, automationId, inputFields, name).
The story values must show: On Portfolio, Sakura Mobility (IMP-2611) shows At risk with go-live 16 Nov 2026, Japan, lead Kenji Arai; filtering Region Japan and Health At risk answers "1 of 18"; health counts read 161 / 38 / 15 from the Weekly metric of week 2026-10-26; the risk grid holds RSK-1183 in the likelihood 4 × impact 5 cell. On Executive summary: projects at risk 38 (+5, coloured bad), value awaiting go-live USD 18.4M against 17.8M, the five top movers led by IMP-2611. Email me this summary calls Send executive summary with to_email the signed-in user's email and week_start 2026-10-26, then shows a \`.toast\` (sent) or the in-app preview when it fails.
Every list has loading, empty ("No items yet.") and filtered-empty ("No rows match your search and filters") states; every form has inline errors, a disabled submit while saving, a success \`.toast\` and a failure banner; a refusal shows the automation's result word in a \`.tag.negative\` with a \`.note\` saying what happened and what to do next.
Components come from the class inventory (\`.g1 .g2 .g3 .pad .inner .solid\`, \`.btn .btn-p .btn-s .btn-t\`, \`.tag\`, \`.toolbar .field .chipsel .tblwrap .tbl .pg\`, \`.ai:not(.msg)\`, \`.tile .loop .empty\`, \`.tabs\`, \`.fld .ctl .hint .seg .tog .opt\`, \`.sth .stv .prog .stages\`, \`.canvas .convo .msg\`, \`.pc .faces .av\`, \`.feed\`, \`.chart .spark .delta .legend\`, \`.toast .menu .crumb .note\`), never a second implementation, never a new colour value, never a Tailwind colour, radius, shadow or type utility: Tailwind only for layout the kit has no class for.
Build locally until \`tsc -b\` and \`vite build\` pass, then hold, push, release, as \`app-code-build\` says.
Read back: the push's \`commit\` and \`files\`; \`get_code_app\` answering that commit as \`head.sha\`; the committed \`app/src/data/bindings.ts\` naming a \`FETCH\` id and \`app/src/data/callables.ts\` holding each automation's block; the \`previewUrl\` the green push answered, quoted.
Report ids (the app id as ids.entity), readBack, unverified, notes, and a \`handover:\` note with the app id, the branch, the routes and the preview address.

Proof: The push's \`commit\` is \`get_code_app\`'s \`head.sha\`; \`bindings.ts\` holds a FETCH id and \`callables.ts\` the block of each automation the body names.
Result IDs: {"entity":"app-a2a9509a82c1","commit":"764c6e05bdb56105e341306a7f9a9b21d3a4aae9"}
Read back: ClickUp Delivery Command app-a2a9509a82c1: create_code_app_data_sources ok: storage fetch e_6adf5087dc07493166cf01c2, fetchOne e_6adf5087dc07493166cf01c5, create e_6adf5087769c8b649ebf5fec, update e_6adf5087dc07493166cf01c8, delete e_6adf5087769c8b649ebf5fef; SAVE_VIEW e_6adf5087769c8b649ebf5ff2 (automation 6adf460108750d257cf1e381, inputs name, filters_json, owner, shared_with); SEND_EXECUTIVE_SUMMARY e_6adf5087dc07493166cf01cb (automation 6adf4d1508750d257cf3df21, inputs to_email, week_start)
Read back: ClickUp Delivery Command app-a2a9509a82c1: push_code_patch committed:true builds:true commit 764c6e05bdb56105e341306a7f9a9b21d3a4aae9, files: app/src/components/portfolio/Overview.tsx, app/src/components/portfolio/ProjectsTable.tsx, app/src/components/ui-kit/kit.tsx, app/src/data/automations.ts, app/src/data/bindings.ts (modified), app/src/data/callables.ts (added), app/src/data/movers.ts, app/src/data/portfolio.ts, app/src/data/types.ts, app/src/routes/Portfolio.tsx, app/src/routes/Summary.tsx, app/src/styles/shell.css
Read back: ClickUp Delivery Command app-a2a9509a82c1: get_code_app head.sha 764c6e05bdb56105e341306a7f9a9b21d3a4aae9, message 'Build Executive summary and Portfolio screens', busy false, security PRIVATE
Read back: ClickUp Delivery Command app-a2a9509a82c1: committed app/src/data/bindings.ts line 19 \`id: "e_6adf5087dc07493166cf01c2",\` (FETCH) and ENTITY project OBJ_cucmd_project, raid OBJ_cucmd_raid, weeklyMetric OBJ_cucmd_weekly_metric, savedView OBJ_cucmd_saved_view; app/src/data/callables.ts holds \`// &gt;&gt;&gt; callable 6adf460108750d257cf1e381\` and \`// &gt;&gt;&gt; callable 6adf4d1508750d257cf3df21\`
Read back: ClickUp Delivery Command app-a2a9509a82c1: previewUrl "https://orbit.uat.unifyapps.com/agent-api/preview/b/app-a2a9509a82c1/main/"
Unverified: No screen was opened (no [visual] proof): that the story values render (38 at risk +5 worse, USD 18.4M from 17.8M, top movers led by IMP-2611, 161/38/15, RSK-1183 in the 4x5 cell, Region Japan + Health At risk answering '1 of 18') is unseen; check: open the previewUrl at /summary and /portfolio?region=japan&amp;health=at_risk
Unverified: top_movers_json's key names were never read (the seed read-back left it out); movers.ts reads project_code\|code\|project\|id and change\|reason\|summary\|note\|detail\|description plus optional from/to; check: read the 2026-10-26 Weekly metric row's top_movers_json and the Top movers table
Unverified: Send executive summary and Save view were not called from the app; check: press Email me this summary (expects a sent toast, or the preview with the result word) and Save view 'Japan at risk' shared with 'Japan team' (expects a saved toast with a view code; again answers refused_name_taken)
Unverified: Saved views apply only the keys q, region, stage, health, lead from filters_json; the seeded V-02 also carries a go_live_date range, which the table does not apply; check: open Saved views and choose 'Europe go-lives this quarter'
Note: handover: app id app-a2a9509a82c1, branch main, preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-a2a9509a82c1/main/. /summary: six .tile numbers with .delta (better/worse in words), value bridge .chart (recharts waterfall: start = value_awaiting_usd minus the four signed bridge fields), top movers .tbl, Email me this summary .btn-s + Preview + .note last updated. /portfolio: 3 health .tile with .spark and change since last week, risk grid .tbl (likelihood 5..1 by impact 1..5, a cell lists its risks inline), 90-day go-live timeline as .cal per region with Slipped tags, 12-week on-track .chart, projects .tbl with .toolbar search, Region/Stage/Health/Lead facets, removable chips, Clear all, 'x of y', .pg (10 per page), Saved views menu and Save view form. Filters live in the URL (?q=&amp;region=&amp;stage=&amp;health=&amp;lead=); the top bar search lands on /portfolio?q=.
Note: handover: storage dataSources exist for the app (bindings.ts FETCH e_6adf5087dc07493166cf01c2); add later objects to ENTITY in app/src/data/bindings.ts rather than provisioning again. Automation wrappers live in app/src/data/automations.ts (useSaveView, useSendSummary, failureMessage); add new automations through create_code_app_data_sources kind automation.
Note: Projects (limit 200) and RAID items (limit 200) are read whole and sliced in the browser for facets, 'x of y', timeline and risk grid, so all views derive from one set; the cache marks every facet field filterable:false, and 18 projects / 20 RAID rows fit one page. If a read ever reports hasMore, the count shows 'x of y+'.
Note: Email me this summary sends to_email = the signed-in user's email (useGetApiUserContext) and week_start = the latest Weekly metric's week_start as a number; result 'sent' shows a .toast with the message id, anything else opens the in-app preview with the result word in a .tag.negative and a .note.
Note: Charts are recharts (the app rules require it) inside the kit's .chart wrapper, coloured with kit tokens (--c2, --c3, --st-positive, --st-negative) and the kit .legend; the 90-day window and 'today' come from the clock at render.

