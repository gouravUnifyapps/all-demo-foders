---
nebula: 3
specId: "e_6ae875ecafe7fc590a571ed0"
mode: "sonic"
title: "Verify round 1 fixes (G3 round 2): Run component runs a component with no account; Save agent output passes the model an"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Run component","id":"6ae865229ec43c6ee2300d8d"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save agent output","id":"6ae864829594aa458cc1ce69"},{"action":"publish","kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"},{"action":"publish","kind":"ai-agent","name":"PF · Reply Sorter","id":"e_6ae86bebf410ab7b2f20260c"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Run component","id":"6ae865229ec43c6ee2300d8d"},{"kind":"automation","name":"Pipeline Factory · Save agent output","id":"6ae864829594aa458cc1ce69"},{"kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"},{"kind":"ai-agent","name":"PF · Reply Sorter","id":"e_6ae86bebf410ab7b2f20260c"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "7df20745-7faf-4bc6-9e9b-e97b9ac6ae1b"
pageDesign: 2
createdAt: "2026-11-02T11:37:18.142Z"
runningAt: "2026-11-02T11:37:21.994Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Verify round 1 fixes (G3 round 2): Run component runs a component with no account; Save agent output passes the model an

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Run component |  | done | 1 |
| t2 | deploy | Pipeline Factory · Run component | t1 | running | 1 |
| t3 | automation | Pipeline Factory · Save agent output |  | done | 1 |
| t4 | deploy | Pipeline Factory · Save agent output | t3 | running | 1 |
| t5 | ai-agent | Pipeline Factory Analyst |  | done | 1 |
| t6 | publish | Pipeline Factory Analyst | t5 | done | 1 |
| t7 | publish | PF · Reply Sorter |  | done | 1 |

### t1 · Run component: run a component with no account

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Run component" (\`6ae865229ec43c6ee2300d8d\`), its deployed version, code, \`setup\` and \`result\`; \`describe_callable_workflow\` for its inputs.
2. Done when: with account_id empty, Run component skips the PF Account lookup instead of failing at Fetch records ("No Value found in filter with field: properties.account_id"), and for C13 Weekly Slot Planner it passes the account's patch_id when an account is given, else an empty patch_id so every patch is planned; C33 and C39 run with no account; every other path and the inputs and result fields stay as they are.
3. Test it on the saved draft with origin \`test\`: C13 with no account, C13 with A-1015, C33 with draft_id D-06 and no account, C39 with no account, and C18 on A-1001 (unchanged path); read each result and its effects back with \`get_records\`. Make no delete call; leave test rows for Pipeline Factory · Reset demo and list them in notes.
4. Read back: \`open_workflow\` for the saved version, each test run's id with \`inspect_workflow_run\` status and output (read the records when a run lags), and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: Test runs of Run component for C13, C33 and C39 with no account answer ran, and C18 on A-1001 still runs.
Result IDs: {"entity":"6ae865229ec43c6ee2300d8d"}
Read back: Pipeline Factory · Run component 6ae865229ec43c6ee2300d8d: compile_and_save_workflow ok:true 'Workflow saved successfully at version 3.'; open_workflow returns version 3, deployment definitionVersion 2, savedAfterDeploy true (not deployed, as the task says); the saved code differs from the edit only in one auto-named variable (holdTheAccountSPatchEmptyWhenNoAccountIsGiven) and indentation
Read back: Pipeline Factory · Run component: the saved code wraps 'Read the account for its patch' (n_anshr) in 'Account given?' (n_b3a2k: account_id exists and is not empty); a new 'Hold the account's patch' variable (n_fb47z, patch_id "") takes the account's patch_id when one is given; C13 Weekly Slot Planner now passes that variable as patch_id; every other arm, input and result field is unchanged
Read back: Pipeline Factory · Run component test 6ae876ed46920244f3d8c6ec (C13, account_id ""): COMPLETED, n_b3a2k false so the account read was skipped, patch_id ""; response result 'ran', summary 'allocated 2 patch(es): PATCH-NAE-04 20 (boost 25%); PATCH-NAE-03 24'; get_records shows PF Component run rows CR-C13-6ae876ed46920244f3d8c6f1-PATCH-NAE-04 and -PATCH-NAE-03 (status saved, origin test)
Read back: Pipeline Factory · Run component test 6ae876f09ec43c6ee258587d (C13, A-1015): COMPLETED, n_anshr ran and the variable read patch_id 'PATCH-NAE-04'; response result 'ran', summary 'allocated 1 patch(es): PATCH-NAE-04 20 (boost 25%)'; row CR-C13-6ae876f09ec43c6ee25858da-PATCH-NAE-04 saved, origin test
Read back: Pipeline Factory · Run component test 6ae876f2f38e3276181c361d (C33, draft D-06, no account): COMPLETED, response result 'ran', summary 'Blocked: person is in another sequence', reason 'Send Rules Check answered blocked'; row CR-C33-6ae876f2f38e3276181c3626 status blocked, origin test
Read back: Pipeline Factory · Run component test 6ae876f39594aa458cecf85f (C39, no account): COMPLETED, response result 'ran', reason 'Email Domain Swapper answered done'; row CR-C39-6ae876f39594aa458cecf86d saved, origin test
Read back: Pipeline Factory · Run component test 6ae876f4f6f76639f83cc1fe (C18, A-1001, unchanged agent path): COMPLETED, response result 'ran', run_id RUN-6ae87720f6f76639f83cc5f0, confidence 72, reason 'run saved: saved; wrote PF Fact row (case_for_change)'
Read back: Pipeline Factory · Run component: best practice 83 (82 of 85 checks), version 3, no fix round (every failing check is an exception below)
Unverified: Run component with account_id given but not in PF Account (for example A-9999) was not tested: for C13 the patch_id would come through empty, so every patch would be planned. Check: one test run of C13 with A-9999.
Note: Test rows left for Pipeline Factory · Reset demo (origin test): PF Component run CR-C13-6ae876ed46920244f3d8c6f1-PATCH-NAE-04, CR-C13-6ae876ed46920244f3d8c6f1-PATCH-NAE-03, CR-C13-6ae876f09ec43c6ee25858da-PATCH-NAE-04, CR-C33-6ae876f2f38e3276181c3626, CR-C39-6ae876f39594aa458cecf86d, RUN-6ae87720f6f76639f83cc5f0; PF Hand-off H-6ae87720f6f76639f83cc5f1, H-6ae87720f6f76639f83cc5f3, H-6ae87720f6f76639f83cc5f5; the PF Fact row (case_for_change) the C18 agent saved for A-1001; plus whatever Weekly Slot Planner, Send Rules Check and Email Domain Swapper wrote (the C39 run rested IN-02, swapped IN-03 in and retired IN-05)
Note: The C18 test ran through the deployed Save agent output (version 0), so its hand-offs H-6ae87720…f1/f3/f5 still carry model 'none (deterministic)'; the t3 fix ships only when Save agent output is deployed
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Call workflow (n_xtvtn, n_wl78k, n_tepgt, n_d6i2g) · nodes not changed by this task; the DSL has no node option to hide inputs/outputs
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_cr23d, n_lsmyd, n_anshr, n_khd03) · needs object indexes on OBJ_pf_component, OBJ_pf_component_run and OBJ_pf_account outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_87wnj) · nodes not changed by this task
Note: Security: no change to access or identity; the account read is still filtered by account_id, and no secret was written

### t2 · Deploy Pipeline Factory · Run component

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Run component" and the version the automation task saved (from Built so far).
2. Done when: it is deployed, \`deployment.status\` live and \`definitionVersion\` equal to the saved version.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · verify fix: Run component with no account".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Run component deployed at the saved version.

### t3 · Save agent output: pass the model and the receiver's threshold to Save hand-off

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Save agent output" (\`6ae864829594aa458cc1ce69\`), its deployed version and code; \`describe_callable_workflow\` for it and for "Pipeline Factory · Save hand-off" (\`6ae840a5fbdd550a9a44c524\`, unchanged) to see which of model and threshold Save hand-off takes as inputs.
2. Done when: every hand-off Save agent output saves through Save hand-off carries the run's model input (for example Claude Sonnet 5), never "none (deterministic)", and the receiving component's registered threshold read from its PF Component row (Meeting Prep Writer's own threshold, not 0) where Save hand-off takes them; if Save hand-off takes no model or threshold input, Save agent output writes them onto the saved PF Hand-off rows by id right after (model and threshold fields only). Every other rule, input and result stays as it is; Save hand-off is not changed.
3. Test it on the saved draft with origin \`test\`: one save as C18 on A-1001 with model "Claude Sonnet 5" (it feeds Play Picker, Message Writer and Meeting Prep Writer) and one under threshold; read the PF Hand-off rows back for model and threshold. Make no delete call; leave test rows for Pipeline Factory · Reset demo.
4. Read back: \`open_workflow\` for the saved version, the test runs with \`inspect_workflow_run\`, the PF Hand-off rows with \`get_records\`, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: The PF Hand-off rows a test save makes carry the run's model and each receiver's threshold.
Result IDs: {"entity":"6ae864829594aa458cc1ce69"}
Read back: Pipeline Factory · Save agent output 6ae864829594aa458cc1ce69: saved as version 1 (51 nodes); open_workflow returns code identical to the edit, deployment definitionVersion 0, savedAfterDeploy true (not deployed, as the task says)
Read back: Pipeline Factory · Save agent output: describe_callable_workflow for Save hand-off 6ae840a5fbdd550a9a44c524 lists 13 inputs with no model or threshold, so after each Save hand-off call a new step writes properties.model = the run's model input and properties.threshold = the receiver's PF Component threshold onto the PF Hand-off row, by its id (handoff_id), and only when handoff_id is not empty and the result is not 'duplicate'; the register read now fetches threshold and each feed carries its receiver's threshold; Save hand-off is unchanged (version 4)
Read back: Pipeline Factory · Save agent output test 6ae877502099302ffb30f2aa (C18, A-1001, play PLAY-T3-TEST, model 'Claude Sonnet 5', confidence 80): COMPLETED, result 'saved', handoff_ids H-6ae877512099302ffb30f368,H-6ae877512099302ffb30f3a0,H-6ae877512099302ffb30f3ae
Read back: Pipeline Factory · Save agent output: get_records PF Hand-off H-6ae877512099302ffb30f368 to Play Picker: model 'Claude Sonnet 5', threshold 70; H-6ae877512099302ffb30f3a0 to Message Writer: model 'Claude Sonnet 5', threshold 70; H-6ae877512099302ffb30f3ae to Meeting Prep Writer: model 'Claude Sonnet 5', threshold 0 (its registered threshold in PF Component C44)
Read back: Pipeline Factory · Save agent output test 6ae8773af38e3276181c3a03 (under threshold, confidence 50): COMPLETED, result 'waiting_person', reason 'confidence 50 under threshold 70', handoff_ids '' (no hand-off is saved under threshold, as before)
Read back: Pipeline Factory · Save agent output test 6ae877379594aa458cecfc2a (same key as the agent's earlier save): result 'saved'; the three hand-offs answered 'duplicate already saved under A-1001\|\|', so no hand-off row was rewritten
Unverified: Best Practice score not read: get_workflow_best_practice_report answered HTTP 500 'Workflow execution failed' twice for version 1; no fix round was made. Check: read the score chip for Save agent output in the builder.
Unverified: A call with model left blank was not tested; the new step sets skipIfBlank true so that a blank model keeps Save hand-off's value. Check: one test save with model "" and a fresh play_id, then read the PF Hand-off model.
Note: The task expected Meeting Prep Writer's own threshold 'not 0', but its PF Component row C44 registers threshold 0. The row now carries that registered value, 0, read from the register. If 0 is wrong, the register row needs changing; that is outside this task.
Note: Save hand-off already wrote the receiver's threshold (70/70/0 on the agent's hand-offs H-6ae87720f6f76639f83cc5f1/3/5); the defect seen was model 'none (deterministic)' on all three
Note: Save hand-off keys hand-offs on account\|person\|play, so a second test save with the same account, person and play answers duplicate and writes no new row. The proof test used play_id PLAY-T3-TEST to get a fresh key.
Note: Test rows left for Pipeline Factory · Reset demo (origin test): PF Component run RUN-6ae877379594aa458cecfc2a, RUN-6ae8773af38e3276181c3a03, RUN-6ae877502099302ffb30f2aa; PF Hand-off H-6ae877512099302ffb30f368, H-6ae877512099302ffb30f3a0, H-6ae877512099302ffb30f3ae; the PF Fact rows (case_for_change, A-1001) the two saved runs wrote
Note: Security: the new write sets only the model and threshold fields of a PF Hand-off row that this same run saved (by its returned id); no access settings were changed and no secret was written
Note: feedback:
Bug: compile_and_save_workflow reported failure (a 60 s MCP timeout, then HTTP 502 on the one retry) while the retry's save had in fact landed.
Context: An update save of Pipeline Factory · Save agent output (6ae864829594aa458cc1ce69, about 47 KB by codeFile) on orbit UAT.
Where: mcp-tool
Evidence: Call 1 timed out after 60s and the version stayed 0. Call 2 returned 'Tenant MCP returned HTTP 502.', yet search_workflows then showed version 1 and open_workflow returned code identical to the file sent.
Cause: Unknown — next check: time the tenant save of a ~47 KB workflow against the bridge's 60 s timeout and the gateway's timeout.
Regression: Saving a workflow of about 47 KB by codeFile answers ok:true with the new version.
Note: feedback:
Bug: get_workflow_best_practice_report failed twice with HTTP 500 for Save agent output, while it scored Run component in the same session.
Context: workflowIds [6ae864829594aa458cc1ce69], version 1, 51 nodes, orbit UAT.
Where: platform
Evidence: 'POST /api/workflow/execute/node failed with HTTP 500 Internal Server Error: Workflow execution failed' on both tries.
Cause: Unknown — next check: open the builder's score chip for version 1 and read the platform log for that 500.
Regression: get_workflow_best_practice_report on 6ae864829594aa458cc1ce69 returns a score.

### t4 · Deploy Pipeline Factory · Save agent output

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Save agent output" and the version the automation task saved (from Built so far).
2. Done when: it is deployed, \`deployment.status\` live and \`definitionVersion\` equal to the saved version.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · verify fix: hand-off model and threshold".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Save agent output deployed at the saved version.

### t5 · Analyst: give stored dates as they are

Body:
1. Read: \`get_agent\` for "Pipeline Factory Analyst" (\`e_6ae846ffd96c5f6ba22b98da\`), its instructions whole, model and tools.
2. Done when: its instructions add one rule and change nothing else: a date field is given as the stored calendar date in the form the record holds it (for example Kestrel Ridge Utilities' holdout ends 2027-01-27), with no time-zone conversion and never "approximately" or "about".
3. Test with one message: "When does Kestrel Ridge Utilities' factory holdout end?" must answer 2027-01-27 (read the trace if it misses; two rounds at most). Do not publish: the publish task does.
4. Read back: \`get_agent\` for the instructions' new rule, quoted, and the test answer.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows the date rule; the test answers 2027-01-27.
Result IDs: {"entity":"e_6ae846ffd96c5f6ba22b98da"}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: before the change, send_test_message (case e_6ae876192099302ffb30dbdc) answered "Kestrel Ridge Utilities (A-1005, PATCH-NAE-03) is currently under a factory holdout that ends on **27 January 2028**". The trace's think call showed why: the record holds "factory_holdout_until: 1801008000000 (milliseconds epoch)", and the model used the wrong year anchor ("2027-01-01 = 1767225600", which is really 2026-01-01).
Read back: Pipeline Factory Analyst: update_agent changed ["instructions"], version 14 -&gt; 15, needsPublish true. No other field changed. role and goal were sent with the values already stored.
Read back: Pipeline Factory Analyst: get_agent shows the new rule under 'What every answer names': "A date field (such as factory_holdout_until): give the stored calendar date exactly, as YYYY-MM-DD, for example \"Kestrel Ridge Utilities' holdout ends 2027-01-27\". Never convert it to a time zone, never add a time of day, and never say \"approximately\", \"about\" or \"around\", because the record holds one exact date. When the record holds the date as a number, it is milliseconds since 1970-01-01 in UTC ... (1801008000000 is 2027-01-01 plus 26 days, so 2027-01-27)."
Read back: Pipeline Factory Analyst: after the change, send_test_message "When does Kestrel Ridge Utilities' factory holdout end?" (case e_6ae8765f9ec43c6ee25846bf) answered "Kestrel Ridge Utilities' factory holdout ends on **2027-01-27**. - Account: Kestrel Ridge Utilities (A-1005), PATCH-NAE-03 - \`factory_holdout\` is active, with \`factory_holdout_until\` = **2027-01-27**"
Read back: Pipeline Factory Analyst: date -u -d @1801008000 gives 'Wed Jan 27 00:00:00 UTC 2027', so 2027-01-27 is the stored date.
Unverified: Pipeline Factory Analyst: after 4 reads over about 2 minutes, the trace for the fixed run (case e_6ae8765f9ec43c6ee25846bf) still has no model call. The answer is quoted from send_test_message. Check: read_trace on e_6ae8765f9ec43c6ee25846bf to see the think step's day count.
Unverified: Pipeline Factory Analyst: the draft (version 15) is not published, as the task says. The publish task carries it.
Note: The record returns factory_holdout_until as epoch milliseconds (1801008000000), not as a calendar string. So the rule cannot only say 'as the record holds it': that would print the raw number. The rule also tells the model to convert from fixed UTC year anchors, because its own anchor was wrong by one year. A sturdier fix is for ReadFactoryRecords (automation 6ae843e69ec43c6ee2dec988) to format date fields as YYYY-MM-DD. That is not in this plan.
Note: plan_change: absorbed
Note: The baseline trace offers the model EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy, which are not among the agent's tools. The existing instructions already forbid them. Nothing was changed here.
Note: feedback:
Bug: read_trace never shows a model call for a caseId that send_test_message returned after runAgainToFindAnswer.
Context: send_test_message {agentId e_6ae846ffd96c5f6ba22b98da, runAgainToFindAnswer: true} returned case e_6ae8765f9ec43c6ee25846bf with a full answer; read_trace was called 4 times over about 2 minutes.
Where: mcp-tool
Evidence: Each read returned nodesInTrace 2 and incomplete: true, while the same flow earlier (case e_6ae876192099302ffb30dbdc) gave 11 nodes and 3 model calls on the first read.
Cause: Unknown — next check: read_trace on the rerun caseId after 10 minutes, and compare the case id the second invoke reports.
Regression: send_test_message with runAgainToFindAnswer, then read_trace on its caseId within 3 minutes returns at least one modelCalls entry.
Note: get_agent returned HTTP 502 once. The same read succeeded on the second try.

### t6 · Publish Pipeline Factory Analyst

Body:
1. Read: \`get_agent\` for "Pipeline Factory Analyst" (\`e_6ae846ffd96c5f6ba22b98da\`).
2. Done when: it is published with the date rule, so Pipeline Factory · Ask the analyst invokes it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing published true and needsPublish false, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows the analyst published with nothing left to publish.
Result IDs: {"entity":"e_6ae846ffd96c5f6ba22b98da"}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: before publishing, get_agent showed version 15, published true, needsPublish true. Its instructions hold the date rule: "A date field (such as factory_holdout_until): give the stored calendar date exactly, as YYYY-MM-DD ...".
Read back: Pipeline Factory Analyst: publish_agent {confirmed: true} answered publishedVersion 15, live true, automationSaid {"response":"success"}.
Read back: Pipeline Factory Analyst: get_agent afterwards shows "published": true, "needsPublish": false, version 20. The instructions still hold the date rule, and the tool ReadFactoryRecords is enabled.
Unverified: Pipeline Factory Analyst: that Pipeline Factory · Ask the analyst gets 2027-01-27 from the published version is not checked here. Check: ask it "When does Kestrel Ridge Utilities' factory holdout end?" and read the answer.
Note: Publish approval: 'yes, publish Pipeline Factory Analyst. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Same as t7: publish_agent reported publishedVersion 15, but get_agent right after showed version 20. This is already in feedbacks/records.md.

### t7 · Publish PF · Reply Sorter's saved draft

Body:
1. Read: \`get_agent\` for "PF · Reply Sorter" (\`e_6ae86bebf410ab7b2f20260c\`): needsPublish true, its instructions and tools as the draft holds them.
2. Done when: the saved draft is published, so Pipeline Factory · Run component runs the version that was tested; nothing else changes.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing published true and needsPublish false, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Reply Sorter published with nothing left to publish.
Result IDs: {"entity":"e_6ae86bebf410ab7b2f20260c"}
Read back: PF · Reply Sorter e_6ae86bebf410ab7b2f20260c: before publishing, get_agent showed version 7, published true, needsPublish true. Draft tools: ReadComponentInputs, DoNotContactList and SaveAgentOutput enabled; generateChartTool and requestClarification off.
Read back: PF · Reply Sorter: publish_agent {confirmed: true} answered publishedVersion 7, live true, automationSaid {"response":"success"}.
Read back: PF · Reply Sorter: get_agent afterwards shows "published": true, "needsPublish": false, version 12. Instructions and tools are the same as the draft held.
Unverified: PF · Reply Sorter: whether Pipeline Factory · Run component now runs the published version is not checked here. Check: run component C41 through Pipeline Factory · Run component and read the run.
Note: Publish approval: 'yes, publish PF · Reply Sorter. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: feedback:
Bug: publish_agent reports a version the next get_agent does not show.
Context: publish_agent {agentId e_6ae86bebf410ab7b2f20260c, confirmed: true} on PF · Reply Sorter at version 7.
Where: mcp-tool
Evidence: publish_agent answered publishedVersion 7 and wasAtVersion 2; get_agent seconds later showed version 12 with needsPublish false.
Cause: Unknown — next check: read the agent's version before and after one publish to see how many versions the publish automation writes.
Regression: publish_agent's publishedVersion equals the version get_agent reports right after it.

