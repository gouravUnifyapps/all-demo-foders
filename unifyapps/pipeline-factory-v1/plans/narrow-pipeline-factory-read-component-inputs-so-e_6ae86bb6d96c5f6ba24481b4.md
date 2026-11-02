---
nebula: 3
specId: "e_6ae86bb5afe7fc590a500ad8"
mode: "sonic"
title: "Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the f"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "60960e92-7827-4348-a744-1c5d39da4ff0"
pageDesign: 2
createdAt: "2026-11-02T10:53:42.498Z"
runningAt: "2026-11-02T10:53:46.147Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the f

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Read component inputs |  | done | 1 |
| t2 | deploy | Pipeline Factory · Read component inputs | t1 | running | 1 |

### t1 · Narrow Pipeline Factory · Read component inputs to fit an agent's tool reply

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Read component inputs" (\`6ae8635446920244f3d5194b\`), its saved and deployed versions, code, \`setup\` and \`result\` schema; \`describe_callable_workflow\` for its inputs. If its inputs or result field names differ from component_id, account_id, person_id, draft_id, patch_id and component, account, people, signals, facts, drafts, sources, handoffs_in, inboxes, suppression, recent_runs, reason, stop and report.
2. Done when: the same inputs and result fields (names and types unchanged) answer under 12,000 characters in total for component C32 on account A-1001 and for every other component on A-1001, because the AI agent runtime keeps only the first 16,000 and last 2,000 characters of a tool reply (today A-1001 answers about 200,000). The rules: each JSON list holds only the fields an agent needs (ids, names, status, confidence, short text fields cut to 300 characters; no payload or row_values blobs; no system fields); the lists come in this order of importance and the rest of the reply budget goes to them in that order: component, account, drafts (the draft named by draft_id first, else the account's drafts, at most 10), handoffs_in (this component's, for the account when given, newest 10), sources (the account's or person's, plus rows with no account only when the component is C29, C30, C42 or C44 for content assets and the handbook, at most 10), signals (newest 10), facts (at most 10), people (the person named by person_id first, at most 13), suppression (only the person's or account's rows); inboxes only for C38, C39 and C35 (else an empty list); recent_runs only for C48 to C54 (the newest 30, compact: run_id, component_id, status, confidence, output_type, summary cut to 120 characters, run_at), else an empty list. A list that is cut says so in reason (for example 'sources cut to 10 of 19'). Deterministic, no model call, read-only.
3. Test it with bounded test runs on the saved draft for C32 with draft_id D-04 on A-1001, C37 on A-1001 with person_id P-1002, C08 on A-1001, C53 with patch_id PATCH-NAE-03, and an unknown component: read each run's output length and that the draft, sources and handoffs_in each component needs are present. It writes nothing, so no test rows are made and nothing is deleted.
4. Read back: \`open_workflow\` for the saved version and its \`result\` schema, \`describe_callable_workflow\` for its inputs (unchanged), each test run's id with \`inspect_workflow_run\` status and the character length of its output, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: Test runs of Pipeline Factory · Read component inputs answer under 12,000 characters for C32 on A-1001 with D-04 present, and the result fields are unchanged.
Result IDs: {"entity":"6ae8635446920244f3d5194b"}
Read back: Pipeline Factory · Read component inputs 6ae8635446920244f3d5194b: open_workflow shows saved version 4 (was 2), deployment DEPLOYED definitionVersion 2, savedAfterDeploy true. Not deployed here; the deploy task does that.
Read back: Pipeline Factory · Read component inputs: the result schema in the version 4 code matches version 2 exactly. It still has the 12 string fields component, account, people, signals, facts, drafts, sources, handoffs_in, inboxes, suppression, recent_runs and reason, all required.
Read back: Pipeline Factory · Read component inputs: describe_callable_workflow still shows component_id (string, required) and account_id, person_id, draft_id, patch_id (string, optional), unchanged.
Read back: Pipeline Factory · Read component inputs run 6ae86c6bfbdd550a9a52d621 (C32, A-1001, draft_id D-04): COMPLETED, output 11,315 characters. Drafts start with D-04, then D-01 to D-03, D-05, D-06, D-6ae86bea…, D-T01 to D-T03. handoffs_in has H-6ae86bea9594aa458cd64499 to Message Grader. Sources has 9 of 17. reason 'drafts cut to 10 of 11; sources cut to 9 of 17; signals cut to 0 of 6; facts cut to 0 of 13; people cut to 0 of 14; suppression cut to 0 of 4'.
Read back: Pipeline Factory · Read component inputs run 6ae86c6df6f76639f83ac72a (C37, A-1001, person_id P-1002): COMPLETED, output 11,460 characters. 10 drafts, 10 of 17 sources, 1 of 6 signals, no hand-offs to C37, people cut to 0 of 14.
Read back: Pipeline Factory · Read component inputs run 6ae86c6f9594aa458cd6c0d6 (C08, A-1001): COMPLETED, output 11,336 characters. 10 drafts, 10 of 17 sources, 1 of 6 signals, no hand-offs to C08.
Read back: Pipeline Factory · Read component inputs run 6ae86c702099302ffb2f4b09 (C53, patch_id PATCH-NAE-03): COMPLETED, output 9,912 characters. recent_runs has the newest 30 of 50 in compact form (run_id, component_id, status, confidence, output_type, summary cut to 120 characters, run_at). Other lists are empty, reason 'recent_runs cut to 30 of 50'.
Read back: Pipeline Factory · Read component inputs run 6ae86c72f13e536c52ed4a68 (unknown component C999 on A-1001): COMPLETED, reason 'unknown component', all lists empty.
Read back: Pipeline Factory · Read component inputs: best practice 93 (83 of 85 checks), no fix round needed, version 4 (version 3 also read 93).
Read back: Pipeline Factory · Read component inputs: security rule 4 (only the fields needed). The payload projections were removed from the hand-off and run fetches. Each list is narrowed to named fields, with text cut to 300 characters (run summaries to 120). Suppression with no account or person now answers [] instead of every row. Read-only: no write nodes (11 fetches and 1 Groovy node).
Unverified: Pipeline Factory · Read component inputs: under 12,000 characters for every other component on A-1001 follows from the code but was not run per component. Lists are filled against an 11,200-character budget, and reason is capped at 400 characters, so the worst case is about 11,750. The component and account objects are counted first and are not capped beyond 300 characters per field; on A-1001 they measure 439 to 743 and 965. Check: a test run per component on A-1001.
Unverified: Pipeline Factory · Read component inputs: the length was measured as JSON.stringify of the STOP response (pretty-printed 11,509 at most). How the AI agent runtime serialises the tool reply was not observed. Check: one agent run calling this tool and reading the tool reply length in its trace.
Unverified: Pipeline Factory · Read component inputs: callers still get version 2, which answers about 200,000 characters, until the deploy task deploys version 4.
Note: With the brief's order of importance, A-1001's 11 drafts (about 590 characters each after escaping) and its sources use most of the budget, so people (P-1002 for C37 included), facts and suppression come back empty on A-1001. Each cut is named in reason. If an agent needs the named person or facts, people would have to come before drafts, or draft bodies would need a shorter cut. That is a change to the brief, so it was not made.
Note: assumed: dropped from the lists as system or blob fields: origin, payload, evidence (hand-offs), model, cost_usd, latency_ms, idempotency_key, planted_error (drafts), ask_id, built_link and built_at (component). Empty values are omitted from each row.
Note: assumed: signals, facts and sources are ordered newest first by signal_date, fact_date and source_date. Hand-offs are ordered by saved_at and runs by run_at. Drafts and people are ordered by id, after the named draft or person.
Note: The first save (version 3) used a 10,200-character list budget. The runs on version 3 (6ae86c3ff6f76639f83ac2e0 at 10,500, 6ae86c40f38e3276181a8d90 at 10,438, 6ae86c41fbdd550a9a52d2b1 at 10,314, 6ae86c4346920244f3d74a3f at 9,905, 6ae86c44fbdd550a9a52d2d6 unknown component) gave signals and people nothing. Version 4 raised the budget to 11,200 and capped reason at 400 characters; nothing else changed ('changed 1 statement (line 550)').
Note: The version 3 save's changes line said '12 statements' changed. This task changed 3: the Groovy node, and the hand-off and run fetches (payload dropped from their fields). The version 4 read-back shows every other fetch with its fields as before.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Execute Groovy code · score already 90 or more
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (OBJ_pf_component component_id/name; OBJ_pf_component_run run_at) · score already 90 or more; needs object indexes outside the task
Note: feedback:
Bug: trigger_workflow_run answers about 118,000 characters for a workflow_test run whose response is about 11,000, so Claude Code refuses the reply and saves it to a file.
Context: trigger_workflow_run on 6ae8635446920244f3d5194b, runType workflow_test, fullValues ["response"]; the fetch nodes return up to 500 rows each.
Where: mcp-tool
Evidence: 'Error: result (118,570 characters across 2,888 lines) exceeds maximum allowed tokens' although \`shortened\` listed nodes and nodes.4.runDetails.output.objects.
Cause: Unknown — next check: measure which part of \`nodes\` makes up the 118k when fullValues names only \`response\`.
Regression: the same run with fullValues ["response"] answers under the client's tool-result limit while \`response\` stays whole.

### t2 · Deploy Pipeline Factory · Read component inputs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read component inputs" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Read component inputs" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Read component inputs narrowed for the agents' tool reply".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read component inputs deployed with definitionVersion equal to the saved version.

