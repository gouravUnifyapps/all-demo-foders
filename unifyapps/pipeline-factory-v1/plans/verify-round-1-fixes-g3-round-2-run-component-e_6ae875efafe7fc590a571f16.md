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
| t1 | automation | Pipeline Factory · Run component |  | running | 1 |
| t2 | deploy | Pipeline Factory · Run component | t1 | pending | 0 |
| t3 | automation | Pipeline Factory · Save agent output |  | running | 1 |
| t4 | deploy | Pipeline Factory · Save agent output | t3 | pending | 0 |
| t5 | ai-agent | Pipeline Factory Analyst |  | done | 1 |
| t6 | publish | Pipeline Factory Analyst | t5 | running | 1 |
| t7 | publish | PF · Reply Sorter |  | done | 1 |

### t1 · Run component: run a component with no account

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Run component" (\`6ae865229ec43c6ee2300d8d\`), its deployed version, code, \`setup\` and \`result\`; \`describe_callable_workflow\` for its inputs.
2. Done when: with account_id empty, Run component skips the PF Account lookup instead of failing at Fetch records ("No Value found in filter with field: properties.account_id"), and for C13 Weekly Slot Planner it passes the account's patch_id when an account is given, else an empty patch_id so every patch is planned; C33 and C39 run with no account; every other path and the inputs and result fields stay as they are.
3. Test it on the saved draft with origin \`test\`: C13 with no account, C13 with A-1015, C33 with draft_id D-06 and no account, C39 with no account, and C18 on A-1001 (unchanged path); read each result and its effects back with \`get_records\`. Make no delete call; leave test rows for Pipeline Factory · Reset demo and list them in notes.
4. Read back: \`open_workflow\` for the saved version, each test run's id with \`inspect_workflow_run\` status and output (read the records when a run lags), and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: Test runs of Run component for C13, C33 and C39 with no account answer ran, and C18 on A-1001 still runs.

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

