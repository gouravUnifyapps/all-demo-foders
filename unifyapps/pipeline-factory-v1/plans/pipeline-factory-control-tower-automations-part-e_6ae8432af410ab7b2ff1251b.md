---
nebula: 3
specId: "e_6ae84329d96c5f6ba22b1290"
mode: "sonic"
title: "Pipeline Factory Control Tower · automations, part 2, and the analyst"
owner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"Pipeline Factory Analyst"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Pause component"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read factory records"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset demo"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Ask the analyst"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Pause component"},{"kind":"automation","name":"Pipeline Factory · Read factory records"},{"kind":"automation","name":"Pipeline Factory · Reset demo"},{"kind":"automation","name":"Pipeline Factory · Ask the analyst"},{"kind":"ai-agent","name":"Pipeline Factory Analyst"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "cccbf135-020f-4e1a-ae0b-58f3aed649b5"
pageDesign: 2
createdAt: "2026-11-02T08:00:42.574Z"
runningAt: "2026-11-02T08:00:47.710Z"
runner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"8da1d8cb-cc02-5ac8-85df-da01be5fab51"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory Control Tower · automations, part 2, and the analyst

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Pause component |  | done | 1 |
| t2 | deploy | Pipeline Factory · Pause component | t1 | done | 1 |
| t3 | automation | Pipeline Factory · Read factory records |  | done | 1 |
| t4 | deploy | Pipeline Factory · Read factory records | t3 | done | 1 |
| t5 | automation | Pipeline Factory · Reset demo |  | done | 1 |
| t6 | deploy | Pipeline Factory · Reset demo | t5 | done | 1 |
| t7 | ai-agent | Pipeline Factory Analyst | t4 | done | 1 |
| t8 | publish | Pipeline Factory Analyst | t7 | done | 1 |
| t9 | automation | Pipeline Factory · Ask the analyst | t8 | done | 1 |
| t10 | deploy | Pipeline Factory · Ask the analyst | t9 | done | 1 |

### t1 · Build Pipeline Factory · Pause component

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Pause component"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`.
2. Done when: the callable automation "Pipeline Factory · Pause component" is saved, compiled clean, with exactly this contract: callable from the app; inputs component_id (text), actor (text), origin (text); result result (text: paused \| already_paused), held_handoffs (number), reason (text). Sets PF Component.status paused and every flowed-pending or late PF Hand-off from that component to held; resuming is a person's job and is not offered. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: make your own rows with origin \`test\` and unique ids that start \`T-\` (a test account, person, draft or component as the case needs, copied in shape from a seed row), run each result path the line names at least once, read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave the T- rows in place (Pipeline Factory · Reset demo clears origin test rows) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is seed or user; never test against the story row A-1001 or any other seeded row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Pause component; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae843d1f6f76639f8cf2d55"}
Read back: Pipeline Factory · Pause component 6ae843d1f6f76639f8cf2d55: open_workflow version 0, deployment null, trigger CALLABLE callables/callables_from_automation, 12 nodes, 4 return terminals
Read back: Pipeline Factory · Pause component: setup {component_id string (required), actor string, origin string}; result {result string 'paused \| already_paused', held_handoffs number, reason string}; describe_callable_workflow lists component_id/actor/origin as string
Read back: Pipeline Factory · Pause component: run 6ae84442f6f76639f8cf39da COMPLETED on T-PAUSE-C1 -&gt; {result: paused, held_handoffs: 2, reason: 'T-Pause Sender paused by test-runner; its flowed and late hand-offs are held until a person resumes it'}
Read back: Pipeline Factory · Pause component: run 6ae844e5fbdd550a9a459c40 COMPLETED on T-PAUSE-C1 again -&gt; {result: already_paused, held_handoffs: 0, reason: 'T-Pause Sender was already paused; nothing changed'}
Read back: Pipeline Factory · Pause component: run 6ae8444917ec564d96e076fd COMPLETED all-blank payload -&gt; {result: '', held_handoffs: 0, reason: 'component_id is required'}; run 6ae8444cf38e327618fcc67e COMPLETED unknown id -&gt; {result: '', held_handoffs: 0, reason: 'No PF Component has component_id T-NO-SUCH-COMPONENT'}
Read back: Pipeline Factory · Pause component: get_records after run 1: T-PAUSE-C1 status paused (v1); T-PAUSE-H1 (was flowed) held, T-PAUSE-H2 (was late) held, T-PAUSE-H3 waiting_person unchanged (v0)
Read back: Pipeline Factory · Pause component: best practice 97 (81 of 85 checks), no fix round needed, version 0
Read back: Pipeline Factory · Pause component: security rules 2 and 4: writes only PF Component.status and PF Hand-off.status by its own read of the component; no secret, no caller-supplied field written
Unverified: Pipeline Factory · Pause component: the app's call through callables_call_automation is not exercised (not deployed; the deploy task does it) - check: a deployed run from the app after the deploy task
Note: assumed: an invalid call (blank or unknown component_id) answers result '' with held_handoffs 0 and a reason, since the contract names only paused \| already_paused
Note: assumed: 'flowed-pending or late' is read as PF Hand-off status flowed or late; a hand-off is 'from that component' when from_component equals the component's name or its component_id (seed hand-offs carry the name, e.g. 'Current Vendor Finder')
Note: assumed: already_paused makes no writes; the origin input is accepted but unused because this automation creates no rows; actor is quoted in reason only (no PF field holds it)
Note: test rows left for Reset demo: PF Component T-PAUSE-C1; PF Hand-off T-PAUSE-H1, T-PAUSE-H2, T-PAUSE-H3 (all origin test) - the t5 Reset demo test run 6ae8452df6f76639f8cf5a39 then deleted them
Note: Pre-existing hand-offs H-6ae84105…, H-6ae8415…, H-6ae8417…, H-6ae8418… carry patch T-PATCH-1 / from 'T-Sender Agent' but origin user, so Reset demo never clears them; I did not test against them
Note: best practice exception: CHECK_78 Restrict to Required Fields Only · Fetch records · score already 90 or more
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records · score already 90 or more
Note: best practice exception: CHECK_50 Array variable detected · Create variables · score already 90 or more
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields · score already 90 or more

### t2 · Deploy Pipeline Factory · Pause component

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Pause component" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Pause component" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Pause component".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Pause component deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae843d1f6f76639f8cf2d55"}
Read back: Pipeline Factory · Pause component 6ae843d1f6f76639f8cf2d55: before deploy search_workflows version 0, deployment null (matches the saved version 0 from t1)
Read back: Pipeline Factory · Pause component 6ae843d1f6f76639f8cf2d55: deploy_workflow ok:true, workflowVersion 0, deployedVersion 1, paused false, storedVersion 0
Read back: Pipeline Factory · Pause component 6ae843d1f6f76639f8cf2d55: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, deployedAt: 1793607301749, savedAfterDeploy: false}
Read back: Pipeline Factory · Pause component: best practice 97 (81 of 85 checks), no fix round needed, version 0
Note: Deployed per the plan's approval: yes, deploy Pipeline Factory · Pause component. The spec the person accepted names it under Ready when, so it is already approved.
Note: best practice exception: CHECK_78 Restrict to Required Fields Only · Fetch records · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records · task does not save
Note: best practice exception: CHECK_50 Array variable detected · Create variables · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields · task does not save

### t3 · Build Pipeline Factory · Read factory records

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read factory records"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`.
2. Done when: the callable automation "Pipeline Factory · Read factory records" is saved, compiled clean, with exactly this contract: callable from the AI agent; inputs patch_id (text), account_id (text); result patches (text, JSON), accounts (text, JSON), waiting_handoffs (text, JSON), red_components (text, JSON). Read-only: PF Patch, PF Account, PF Hand-off with status waiting_person, rejected or late, and PF Component with success_rate under 97. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`, and it is callable from an AI agent as a tool. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: it is read-only, so run it with patch_id PATCH-NAE-03 and with an empty input and check that waiting_handoffs holds H-07, H-10, H-12 and H-15 and red_components holds C08 Current Vendor Finder at 96.1, reading the seeded rows without changing any.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Read factory records; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae843e69ec43c6ee2dec988"}
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: open_workflow version 1, deployment null, trigger CALLABLE callables/callables_from_automation, 4 fetch_records + 1 groovy + return, no write node
Read back: Pipeline Factory · Read factory records: setup {patch_id string, account_id string} (both optional); result {patches, accounts, waiting_handoffs, red_components} all string (JSON text); describe_callable_workflow lists patch_id and account_id as string
Read back: Pipeline Factory · Read factory records: run 6ae844c7f38e327618fce003 COMPLETED patch_id PATCH-NAE-03 -&gt; patches [PATCH-NAE-03]; 8 accounts A-1001..A-1009; waiting_handoffs H-07 waiting_person (Patch Suggester-&gt;RevOps 74/80), H-10 rejected, H-12 waiting_person, H-14 late, H-15 waiting_person; red_components [C08 Current Vendor Finder 96.1]
Read back: Pipeline Factory · Read factory records: run 6ae844cafbdd550a9a459a0e COMPLETED blank payload -&gt; 3 patches, 28 accounts, 11 waiting hand-offs (incl. H-07, H-10, H-12, H-15), red_components [C08 Current Vendor Finder 96.1]
Read back: Pipeline Factory · Read factory records: best practice 93 (83 of 85 checks) after 1 fix round, first read 89, version 1
Read back: Pipeline Factory · Read factory records: security rule 4: each fetch projects named fields (payload, model, cost, latency left out of hand-offs); read-only, no write node in the graph
Unverified: Pipeline Factory · Read factory records: being bound as a tool of the Pipeline Factory Analyst agent is not checked here - check: the ai-agent task's tool read-back
Note: Fix round 1 (v0-&gt;v1): JavaScript code node replaced by Groovy because GraalJS JSON.stringify returned [{}] for platform objects (run 6ae8444e9ec43c6ee2ded35a); fields projections added; isIn variable replaced by or(eq). Outcome compared: same filtering counts, now with real values
Note: handover: Read factory records answers JSON text of each record's properties (no system fields); waiting_handoffs includes status late, so PATCH-NAE-03 also returns H-14 (Current Vendor Finder-&gt;Renewal Date Finder, late) beside H-07, H-10, H-12, H-15; with account_id only, patches is the account's own patch
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Execute Groovy code · score already 90 or more (no secret is passed; inputs are patch_id and account_id)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (hand-off status, component success_rate) · score already 90 or more
Note: feedback:
Bug: JSON.stringify inside a JavaScript code node turns every object passed in through parameters into {}.
Context: Read factory records v0 passed rows.objects.map((v) =&gt; v.properties) into code_by_unifyapps_javascript; filtering worked, serialisation did not; worked around with Groovy JsonOutput.toJson.
Where: platform
Evidence: run 6ae8444e9ec43c6ee2ded35a: code node input showed full property maps, response red_components "[{}]".
Cause: Suspected: GraalJS receives host (Java) maps that JSON.stringify does not enumerate.
Regression: a JS code node returning JSON.stringify(param) for an object parameter returns its keys.

### t4 · Deploy Pipeline Factory · Read factory records

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read factory records" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Read factory records" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Read factory records".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read factory records deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae843e69ec43c6ee2dec988"}
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: before deploy search_workflows version 1, deployment null (matches the saved version 1 from t3)
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: deploy_workflow ok:true, workflowVersion 1, deployedVersion 1, paused false, storedVersion 1
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 1, deployedAt: 1793607303375, savedAfterDeploy: false}
Read back: Pipeline Factory · Read factory records: best practice 93 (83 of 85 checks), no fix round in this task, version 1
Note: Deployed per the plan's approval: yes, deploy Pipeline Factory · Read factory records. The spec the person accepted names it under Ready when, so it is already approved.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Execute Groovy code · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_124yi, n_9ju5e) · task does not save

### t5 · Build Pipeline Factory · Reset demo

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Reset demo"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`.
2. Done when: the callable automation "Pipeline Factory · Reset demo" is saved, compiled clean, with exactly this contract: callable, mode deterministic, no model call; no inputs; result deleted (number), restored (number). Deletes every row whose origin is test in the nine PF objects, puts every seed row back to its values in PF Seed snapshot, never touches a user row. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it once on the saved draft: first run it; read back that the PF Signal row \`T-RESET-1\` (and every other origin test row the earlier tasks left) is gone, that every seed row equals its PF Seed snapshot row_values, and that no user row changed. It deletes only origin test rows and restores seed rows, so this run is safe; if your own tools refuse a delete it makes, report that, never confirm it.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Reset demo; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae8441df38e327618fcc13c"}
Read back: Pipeline Factory · Reset demo 6ae8441df38e327618fcc13c: open_workflow version 3 (saved after the read at v2; v3 compile summary: 49 nodes, 9 delete_records, 9 fetch_records, 8 update_record_by_id, 1 groovy), deployment null, trigger CALLABLE callables/callables_from_automation, no model node
Read back: Pipeline Factory · Reset demo: setup {} (no inputs, describe_callable_workflow parameters []); result {deleted number, restored number}
Read back: Pipeline Factory · Reset demo: run 6ae8452df6f76639f8cf5a39 (v2) CANCELLED at 61s by the tool timeout after all 9 deletes completed (patch 1, account 15, signal 13, hand-off 3, component 4, ...) and restore writes ran (e.g. F-01 update_record_by_id success true)
Read back: Pipeline Factory · Reset demo: run 6ae845aa17ec564d96e0e5ea (v3) COMPLETED -&gt; {deleted: 11, restored: 0}; its groovy node reported {skipped: 0, unchanged: 130}: all 130 PF Seed snapshot rows equal their live seed rows
Read back: Pipeline Factory · Reset demo: get_records: PF Signal T-RESET-1 missing; T-PAUSE-C1/H1-H3 gone; PF Person, Draft, Component and Hand-off have 0 origin test rows; H-07, H-12, H-15 equal their snapshot row_values (waiting_person, RevOps/Marcus Ellery, 74/66/68)
Read back: Pipeline Factory · Reset demo: the 8 origin user hand-offs from the baseline (H-6ae84105…, H-6ae8415217…, H-6ae8415af3…, H-6ae8415c20…, H-6ae8417af1…, H-6ae8417c17…, H-6ae8418595…, H-6ae844a017…) still exist at version 0
Read back: Pipeline Factory · Reset demo: best practice 88 (82 of 85 checks), under 90 after 2 fix rounds, first read 87, version 3
Read back: Pipeline Factory · Reset demo: security rule 2/3: restore re-reads each live row and skips one whose origin is no longer seed; deletes filter origin = test only
Unverified: Pipeline Factory · Reset demo: v3 restore of a row that differs from its snapshot was not seen in a v3 run (all 130 already matched); the same update_record_by_id arms wrote F-01 with success true in the v2 run - check: one v3 run after a seed row has been changed by the demo
Unverified: Pipeline Factory · Reset demo: origin test rows that exist now (PF Account T-A14, 2 PF Signal rows) were created after run 6ae845aa17ec564d96e0e5ea ended by builders running beside me - check: one more Reset demo run once they finish
Unverified: Test not run before the first fix round: the task allows one reset run, so the runs came after both rounds
Note: Changed after the test (v2-&gt;v3, not a best practice round): the restore now fetches the current seed rows of the 8 objects and rewrites only rows that differ from row_values, because run 6ae8452df6f76639f8cf5a39 at ~0.45 s per row could not finish 130 rows inside the 60 s tool timeout. restored now counts rows actually put back
Note: assumed: a seed row that no longer exists, or whose origin was changed away from seed, is skipped rather than re-created (upsert false, per 'upsert only where the line creates the row')
Note: Compiler refuses a pill as object_type (storage.unknownObjectType), so the restore routes through a branch with one update_record_by_id arm per PF object
Note: plan_change: absorbed
Note: handover: Reset demo deletes every origin test row in all nine PF objects, including fixtures other builders are using at that moment: run it only when no other test is in flight
Note: handover: trigger_workflow_run cancels a workflow_test run that passes 60 s (run 6ae8452df6f76639f8cf5a39 CANCELLED at 61051 ms); keep test runs under a minute
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (seed snapshot and the 8 current-row reads on origin) · needs object indexes outside the task
Note: best practice exception: CHECK_26 Use bulk storage operations instead of looping · Update an existing record (8 arms) · left after two fix rounds (each restore replaces a different whole row; no bulk replace-by-id op)
Note: best practice exception: CHECK_37 Capture Iterations enabled · For each loop · left after two fix rounds (each() captureIterations option compiles but has no effect)
Note: feedback:
Bug: trigger_workflow_run times out at 60s on the MCP side and the test run it started ends CANCELLED at the same moment, although the tool says it waits up to 90 seconds.
Context: workflow_test run of Pipeline Factory · Reset demo v2, a loop of ~130 storage updates; surface is the automation-code bridge timeout or the run lifecycle.
Where: mcp-tool
Evidence: 'tool trigger_workflow_run timed out after 60s'; list_workflow_runs showed 6ae8452df6f76639f8cf5a39 CANCELLED, EXECUTION_TIME 61051, loop node CANCELLED mid-iteration.
Cause: Suspected: the bridge's 60s call timeout aborts the request and the platform cancels the test run with it. Unknown — next check: a workflow with a 75s delay node.
Regression: a workflow_test run between 60s and 90s returns its final status and is not CANCELLED.
Note: feedback:
Bug: compile_and_save_workflow warns pill.unknownOutput for storage_by_unifyapps_delete_records .count, but the runtime returns count.
Context: Reset demo reads &lt;delete node&gt;.count for MULTIPLE deletes.
Where: mcp-tool
Evidence: warning 'delete_records emits objects, hasMore'; run 6ae845aa17ec564d96e0e5ea node n_v5lm3 output {"count": 1}.
Cause: Confirmed: the catalogue output schema lists objects/hasMore, not count.
Regression: reading delete_records .count gives no pill.unknownOutput warning.
Note: feedback:
Bug: each(xs, { captureIterations: false }) compiles clean but has no effect.
Context: Reset demo for-each loop; CHECK_37 stayed failing on n_e3ng2 after the save.
Where: mcp-tool
Evidence: v1 saved with the option, no finding; best practice report v1 still lists CHECK_37; get_dsl_reference documents captureIterations only for range().
Cause: Suspected: each() options pass through unvalidated and captureIterations is not mapped for loop_for_each.
Regression: the option turns Capture Iterations off, or the compiler refuses it.

### t6 · Deploy Pipeline Factory · Reset demo

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Reset demo" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Reset demo" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Reset demo".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Reset demo deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae8441df38e327618fcc13c"}
Read back: Pipeline Factory · Reset demo 6ae8441df38e327618fcc13c: before deploy search_workflows version 3, deployment null (matches the saved version 3 from t5)
Read back: Pipeline Factory · Reset demo 6ae8441df38e327618fcc13c: deploy_workflow ok:true, workflowVersion 3, deployedVersion 1, paused false, storedVersion 3
Read back: Pipeline Factory · Reset demo 6ae8441df38e327618fcc13c: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 3, deployedAt: 1793607304348, savedAfterDeploy: false}
Read back: Pipeline Factory · Reset demo: best practice 88 (82 of 85 checks), under 90, no fix round in this task (t5 made 2), version 3
Note: Deployed per the plan's approval: yes, deploy Pipeline Factory · Reset demo. The spec the person accepted names it under Ready when, so it is already approved.
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (9 nodes: seed snapshot, patch, account, person, signal, fact, draft, hand-off, component on origin) · task does not save
Note: best practice exception: CHECK_26 Use bulk storage operations instead of looping · Update an existing record (8 nodes) · task does not save
Note: best practice exception: CHECK_37 Capture Iterations enabled · For each loop · task does not save
Note: handover: Reset demo is now live; calling it deletes every origin test row in the nine PF objects, so run it only when no other test is in flight

### t7 · Build AI agent Pipeline Factory Analyst

Body:
1. Read: \`list_agents\` for "Pipeline Factory Analyst"; it must not exist (stop and report if it does). The tool automation "Pipeline Factory · Read factory records" is deployed (its workflowId in Built so far).
2. Done when: the AI agent "Pipeline Factory Analyst" exists with this contract: read-only; model Nebula's recommendation; instructions: answers the BDR, the AE and RevOps about one patch from the factory's records only; names each hand-off by its from and to components, its confidence against the threshold and who it waits on; names a component under 97% success as red; never sends, edits or approves anything; says a field is not held when no record holds it; tool Read factory records (Pipeline Factory · Read factory records). The model is the one \`list_models\` recommends; its one tool is the deployed automation "Pipeline Factory · Read factory records" with its inputs patch_id and account_id described; the instructions say it answers from that tool's records only, names hand-offs by id, from and to component, confidence against threshold and who it waits on, names any component under 97% success as red with its rate, offers at most one action (Pause and the component's name and component_id), and never sends, edits or approves anything.
3. Test with \`send_test_messages\`: "What is waiting on a person in patch PATCH-NAE-03 right now, and why?" must name H-07 (RevOps), H-12 and H-15 (Marcus Ellery) with confidence against threshold and H-10 rejected on its schema; "Which component is red, and what is its success rate?" must name Current Vendor Finder at 96.1%. Read the trace when an answer misses a fact, fix the instructions, and test again (two rounds at most). Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tool and settings, and both test answers quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows the model, the instructions and the Read factory records tool; both test answers name the facts the body lists.
Result IDs: {"entity":"e_6ae846ffd96c5f6ba22b98da","tool":"e_6ae84708afe7fc590a16efe7"}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: list_agents for the name returned [] before create, so it did not exist
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: get_agent models runs/picksTask/answerGeneration all e_6acca2af70b66f5702f183cc (Claude Sonnet 5, anthropic, canCallTools true, connectionActive true); readiness canRun true, missing []
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: get_agent tools [ReadFactoryRecords e_6ae84708afe7fc590a16efe7, enabled true, topicId GLOBAL, automationId 6ae843e69ec43c6ee2dec988]; counts.tools 1, capabilities [], memory false, deployments 0, published false
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: instructions say 'Answer only from what it returns', name each hand-off 'by its id (for example H-07), its from component and to component, its confidence against its threshold ... and who it waits on', 'any component whose success rate is under 97% is red', 'at most one action ... "Pause &lt;component name&gt; (&lt;component_id&gt;)"', 'You never send, edit, approve, reject, pause or resume anything', 'The factory records do not hold &lt;field&gt;'; v3 update_agent changed [instructions] adding rejected hand-offs to 'what is waiting' answers
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: trace case e_6ae8475817ec564d96e15082 shows ReadFactoryRecords called with {"patch_id": "PATCH-NAE-03"}, so the tool's patch_id input reached the model
Read back: Pipeline Factory Analyst test Q1 (v3, case e_6ae847d1fbdd550a9a462509): 'H-07 — Patch Suggester → RevOps ... Confidence 74 against threshold 80 ... parked with RevOps'; 'H-12 — Buying Team Mapper → Gate 2 ... Confidence 66 against threshold 70 ... Waiting on Marcus Ellery'; 'H-15 — Case for Change Drafter → Gate 2 ... Confidence 68 against threshold 70 ... Also waiting on Marcus Ellery'; 'H-10 — Case for Change Drafter → Play Picker ... Schema check failed: evidence missing ... rejected'
Read back: Pipeline Factory Analyst test Q2 (v3, case e_6ae84801f6f76639f8cfc56f): 'There is one red component across the factory: Current Vendor Finder (C08), at a success rate of 96.1% — below the 97% threshold.' with one suggested action 'pause Current Vendor Finder (C08)'; trace shows ReadFactoryRecords then answer
Read back: Pipeline Factory Analyst: round 1 (v2) Q1 missed H-10 — trace think 'H-10 is rejected (not waiting on a person)'; fixed by one instruction line, round 2 passed. Not published (publish task does it)
Unverified: Security: runtime offers tools not attached to Pipeline Factory Analyst (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy, GenerateChartWithBlocks, ClarifyFromUser) per read_trace toolsOffered, though list_capabilities shows every capability off — needs an admin to find and remove the tenant-level injection; RequestEnvironmentDeploy/ReleaseEnvironment can change things, so 'read-only' rests on the instructions until then
Unverified: Security: guardrails count 0 on Pipeline Factory Analyst (no denied topics, content filter or PII masking) — needs an admin to decide on guardrails before wide use
Unverified: Security: Pipeline Factory · Read factory records takes patch_id/account_id from the model; whether it limits records to what the asking user may see was not read here — check the automation's owner/permission filter
Unverified: Model 'Nebula's recommendation': list_models carries no recommendation field, so Claude Sonnet 5 (e_6acca2af70b66f5702f183cc) was picked as a tool-capable, active card and proved by both test runs — confirm the person accepts it
Unverified: Cross-user case access not tested (send_test_message userId is not proven to run as that user)
Note: send_test_messages timed out at the MCP client after 60s; both questions were run with send_test_message instead (2 rounds). Rows: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/.sessions/8da1d8cb-cc02-5ac8-85df-da01be5fab51/work/f1251b-agent-builder-1/test-rows.md
Note: Q2 has no patch: instructions tell the agent to call ReadFactoryRecords with an empty patch_id for factory-wide questions; it did and answered from it
Note: handover: Pipeline Factory Analyst agent id e_6ae846ffd96c5f6ba22b98da (draft v3, unpublished); the Ask the analyst automation should invoke this id
Note: feedback:
Bug: send_test_messages times out at the MCP client after 60 s, though the tool is documented to run for several minutes.
Context: Two questions to agent e_6ae846ffd96c5f6ba22b98da with runAgainToFindAnswer true; each calls one read tool.
Where: mcp-tool
Evidence: \`MCP server "plugin:ua:agent-builder" tool "send_test_messages" timed out after 60s\`; the same questions via send_test_message answered in under 50 s each.
Cause: Suspected: the MCP client's 60 s request timeout is shorter than the tool's documented multi-minute trace wait.
Regression: send_test_messages with two tool-calling questions returns rows instead of a client timeout.
Note: feedback:
Bug: An agent with every capability off and one attached tool is offered GenerateChartWithBlocks, ClarifyFromUser and four Environment* tools at run time; get_agent and list_capabilities show none of them.
Context: New Advanced agent e_6ae846ffd96c5f6ba22b98da, read-only by contract.
Where: platform
Evidence: read_trace toolsOffered on case e_6ae84801f6f76639f8cfc56f lists them beside ReadFactoryRecords; get_agent counts.tools 1, capabilities [].
Cause: Unknown — next check: where the runtime injects the Environment* tools and why disabled capabilities are still offered.
Regression: read_trace toolsOffered for that agent lists only think and ReadFactoryRecords.
Note: feedback:
Bug: Task says use the model list_models recommends, but list_models returns no recommendation among 284 cards.
Context: list_models forSlot TEXT_GENERATION; spec line 'model Nebula's recommendation'.
Where: mcp-tool
Evidence: top-level keys count, entityType, models, ok; no card carries recommended or default.
Cause: Confirmed: list_models has no recommendation output.
Regression: list_models answers a recommended card id, or plan guidance stops promising one.

### t8 · Publish Pipeline Factory Analyst

Body:
1. Read: \`get_agent\` for "Pipeline Factory Analyst" (its id in Built so far).
2. Done when: "Pipeline Factory Analyst" is published, so the automation "Pipeline Factory · Ask the analyst" can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows the agent published.
Result IDs: {"entity":"e_6ae846ffd96c5f6ba22b98da"}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: get_agent before publish version 3, published false, needsPublish true, readiness canRun true, tools [ReadFactoryRecords e_6ae84708afe7fc590a16efe7 enabled true]
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: publish_agent confirmed true returned publishedVersion 3, live true, published true, needsPublish false, automationSaid {response: success}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: list_agents by id after publish: published true, needsPublish false, version 8
Unverified: Pipeline Factory Analyst: no deployment (deployments 0) — the task asks only for publish; whether 'Pipeline Factory · Ask the analyst' invokes it successfully is proved by that automation's own run
Unverified: Security: runtime still offers unattached tools (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy, GenerateChartWithBlocks, ClarifyFromUser) per t7 traces, and guardrails count 0 — needs an admin to remove the injected tools and decide guardrails, now that the agent is live
Note: Publish approval: 'yes, publish Pipeline Factory Analyst. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Version read 3 at publish and 8 right after in list_agents, with needsPublish false; the platform's publish bumps the record version

### t9 · Build Pipeline Factory · Ask the analyst

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Ask the analyst"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`. It invokes the published AI agent "Pipeline Factory Analyst" (its id in Built so far) with the invoke-agent action of the AI agents connector; find it with \`search_operations\` and read its inputs with \`get_operation_schema\`.
2. Done when: the callable automation "Pipeline Factory · Ask the analyst" is saved, compiled clean, with exactly this contract: callable from the app; inputs question (text), patch_id (text); result answer (text), grounding (text), suggested_component_id (text). Invokes the Pipeline Factory Analyst agent with the question and the patch, and returns its answer, the records it cited, and the red component it names, if any. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: it is read-only, so run it with question "What is waiting on a person in patch PATCH-NAE-03 right now, and why?" and patch_id PATCH-NAE-03 and check that answer names H-07, H-12 and H-15, that grounding names the records it cites, and that suggested_component_id is C08 when the question is "Which component is red?". It changes no row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Ask the analyst; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae84900fbdd550a9a465807"}
Read back: Pipeline Factory · Ask the analyst 6ae84900fbdd550a9a465807: search_workflows before create returned 0 hits; compile_and_save_workflow created:true version 0, warnings []
Read back: Pipeline Factory · Ask the analyst 6ae84900fbdd550a9a465807: open_workflow version 0, deployment null, trigger CALLABLE callables/callables_from_automation, 8 nodes (3 groovy, 1 ai_agents_by_unifyapps_invoke_agent, 3 return terminals)
Read back: Pipeline Factory · Ask the analyst: setup {question string (required), patch_id string}; result {answer string, grounding string, suggested_component_id string}; describe_callable_workflow lists question (string, required) and patch_id (string, optional)
Read back: Pipeline Factory · Ask the analyst: Invoke Agent node calls aiAgentId e_6ae846ffd96c5f6ba22b98da (Pipeline Factory Analyst) with userQuery from the validated prompt and userEmailAddress from USER.contactDetails.email
Read back: Pipeline Factory · Ask the analyst: run 6ae849079ec43c6ee2f60072 COMPLETED (27.4 s) question 'What is waiting on a person in patch PATCH-NAE-03 right now, and why?' patch_id PATCH-NAE-03 -&gt; answer names H-07 (Patch Suggester-&gt;RevOps 74/80), H-12 and H-15 (Marcus Ellery, 66/70 and 68/70) as waiting on a person, plus H-10 rejected and H-14 late; grounding 'H-07, H-10, H-12, H-14, H-15, C08, PATCH-NAE-03, A-1001, A-1002, A-1003'; suggested_component_id 'C08'
Read back: Pipeline Factory · Ask the analyst: run 6ae84927f13e536c52dbe997 COMPLETED (14.4 s) question 'Which component is red?' patch_id PATCH-NAE-03 -&gt; answer 'Current Vendor Finder (C08) is the one red component in PATCH-NAE-03, with a success rate of 96.1%...'; grounding 'PATCH-NAE-03, C08, H-14'; suggested_component_id 'C08'
Read back: Pipeline Factory · Ask the analyst: run 6ae849232099302ffb13daf5 COMPLETED_WITH_FAILURE (validation node threw as designed, error path ran) all-blank payload -&gt; {answer: 'question is required', grounding: '', suggested_component_id: ''}
Read back: Pipeline Factory · Ask the analyst: best practice 100 (84 of 85 checks), no fix round needed, version 0
Read back: Pipeline Factory · Ask the analyst: security rules 4 and 5: no write node (read-only, no row changed), no secret in any node; the agent is read-only and the user's text goes only into the agent's query, never into a URL, SQL or HTML
Unverified: Pipeline Factory · Ask the analyst: the agent-failure path (Invoke Agent error -&gt; answer 'The analyst could not answer right now; try again.', grounding '', suggested_component_id '') was not run; settle it with a test run while the agent is unpublished or unreachable
Unverified: Pipeline Factory · Ask the analyst: the reply parser relies on the agent ending with GROUNDING:/RED_COMPONENT: lines as the prompt asks (it did in both runs); when the lines are missing it falls back to ids found in the text and an empty suggested_component_id; settle with a run where the agent omits them
Note: Read the PF objects from the cache (hit): PF Patch, PF Hand-off and PF Component schemas; this automation reads no object directly and writes none, the agent's tool Read factory records does the reading, so no origin field is written
Note: assumed: question is required and patch_id optional (blank patch asks across all patches); a rejected input answers the reason in answer with grounding and suggested_component_id empty, since the contract has no error field
Note: assumed: answer keeps the agent's Markdown with the two trailer lines stripped
Note: best practice exception: CHECK_38 Direct node pill mapping detected · Execute Groovy code (error-message normaliser on the validation catch path) · score already 90 or more
Note: handover: Ask the analyst takes 15-30 s per call (agent invocation 14-27 s); a caller page should show a loading state. suggested_component_id is a PF Component component_id such as C08, or '' when none is red
Note: handover: Ask the analyst's validation path ends with run status COMPLETED_WITH_FAILURE (the groovy guard throws into its catch arm); the returned values are still set

### t10 · Deploy Pipeline Factory · Ask the analyst

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Ask the analyst" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Ask the analyst" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Ask the analyst".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Ask the analyst deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae84900fbdd550a9a465807"}
Read back: Pipeline Factory · Ask the analyst 6ae84900fbdd550a9a465807: before deploy search_workflows version 0, deployment null (matches the saved version 0 from t9)
Read back: Pipeline Factory · Ask the analyst 6ae84900fbdd550a9a465807: deploy_workflow ok:true, workflowVersion 0, deployedVersion 1, paused false, storedVersion 0
Read back: Pipeline Factory · Ask the analyst 6ae84900fbdd550a9a465807: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 0, deployedAt: 1793608059826, savedAfterDeploy: false}
Read back: Pipeline Factory · Ask the analyst: best practice 100 (84 of 85 checks), no fix round needed, version 0 (read in t9 on this same version)
Note: Deployed per the plan's approval: yes, deploy Pipeline Factory · Ask the analyst. The spec the person accepted names it under Ready when, so it is already approved.
Note: best practice exception: CHECK_38 Direct node pill mapping detected · Execute Groovy code · task does not save

