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
## Plan

Goal: ClickUp Delivery Command · build 8 of 9: settings and notification automations, the Copilot agent, the app shell and summary screens

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation-shell | ClickUp Command · Update project settings |  | running | 1 |
| t2 | automation | ClickUp Command · Update project settings | t1 | running | 1 |
| t3 | deploy | ClickUp Command · Update project settings | t2 | pending | 0 |
| t4 | automation-shell | ClickUp Command · Mark notification read |  | running | 1 |
| t5 | automation | ClickUp Command · Mark notification read | t4 | running | 1 |
| t6 | deploy | ClickUp Command · Mark notification read | t5 | pending | 0 |
| t7 | ai-agent | ClickUp Command Copilot |  | running | 1 |
| t8 | publish | ClickUp Command Copilot | t7 | pending | 0 |
| t9 | code-app | ClickUp Delivery Command |  | running | 1 |
| t10 | code-app | ClickUp Delivery Command | t9 | running | 1 |

### t1 · Shell for ClickUp Command · Update project settings

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update project settings\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs project_code, name (text), region (text), go_live_date (number), budget_hours_planned (number), and \`result\` = outputs result (text: saved \| failed), field_errors_json (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Update project settings\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Update project settings deployed.

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

### t3 · Deploy ClickUp Command · Update project settings

Body:
Read: \`search_workflows\` for \`ClickUp Command · Update project settings\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Update project settings\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Update project settings deployed with definitionVersion equal to the logic task's saved version.

### t4 · Shell for ClickUp Command · Mark notification read

Body:
Read: \`search_workflows\` for \`ClickUp Command · Mark notification read\`. If it exists, stop and report: a shell is only for a new automation.
Create the callable automation (trigger \`callables_from_automation\`) with \`setup\` = inputs notification_code (text), and \`result\` = outputs result (text), and a stub body that returns a typed value for every output.
\`compile_and_save_workflow\` with no \`workflowId\`, fixing every finding until it saves.
\`deploy_workflow\` with that \`workflowId\`, deploymentNotes \`Contract shell for ClickUp Command · Mark notification read\`. Step 3 must be the last save.
Read back \`search_workflows\` for its \`deployment\` and \`describe_callable_workflow\` for its inputs. Report the \`workflowId\` in \`ids.entity\`.

Proof: \`describe_callable_workflow\` lists every input the body names, and \`search_workflows\` shows the shell of ClickUp Command · Mark notification read deployed.

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

### t6 · Deploy ClickUp Command · Mark notification read

Body:
Read: \`search_workflows\` for \`ClickUp Command · Mark notification read\`, and the saved version the logic task reported in Built so far.
Done when: the automation is deployed and its \`definitionVersion\` equals the version the logic task saved.
\`deploy_workflow\` with its workflowId once, deploymentNotes \`ClickUp Delivery Command demo: Mark notification read\`.
Read back: \`search_workflows\` \`deployment\` (\`status\`, \`definitionVersion\`, \`deployedAt\`), quoted.
Report ids (the workflowId as ids.entity), readBack, unverified, notes.

Proof: \`search_workflows\` shows ClickUp Command · Mark notification read deployed with definitionVersion equal to the logic task's saved version.

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

### t8 · Publish AI agent ClickUp Command Copilot

Body:
Read: \`get_agent\` for the agent id the ai-agent task reported in Built so far.
Done when: the agent is published, its published version holding the tool and the instructions the ai-agent task read back.
\`publish_agent\` once, with the note \`ClickUp Delivery Command demo v1\`.
Read back: \`get_agent\` showing the published state and version, quoted.
Report ids (the agent id as ids.entity), readBack, unverified, notes.

Proof: \`get_agent\` shows ClickUp Command Copilot published.

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

