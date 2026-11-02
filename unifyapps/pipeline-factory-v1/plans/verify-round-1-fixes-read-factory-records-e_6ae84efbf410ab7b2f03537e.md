---
nebula: 3
specId: "e_6ae84ef9f410ab7b2f035341"
mode: "sonic"
title: "Verify round 1 fixes: Read factory records returns people and finds an account by name; the analyst uses the account id"
owner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read factory records","id":"6ae843e69ec43c6ee2dec988"},{"action":"publish","kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Read factory records","id":"6ae843e69ec43c6ee2dec988"},{"kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "1bc30faa-1736-4ca0-b2c2-506d95ff212e"
pageDesign: 2
createdAt: "2026-11-02T08:51:07.602Z"
runningAt: "2026-11-02T08:51:11.430Z"
runner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"8da1d8cb-cc02-5ac8-85df-da01be5fab51"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Verify round 1 fixes: Read factory records returns people and finds an account by name; the analyst uses the account id

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Read factory records |  | done | 1 |
| t2 | deploy | Pipeline Factory · Read factory records | t1 | done | 1 |
| t3 | ai-agent | Pipeline Factory Analyst | t2 | done | 1 |
| t4 | publish | Pipeline Factory Analyst | t3 | done | 1 |

### t1 · Fix Pipeline Factory · Read factory records

Body:
1. Read: \`open_workflow\` on \`6ae843e69ec43c6ee2dec988\` ("Pipeline Factory · Read factory records", deployed) for its code, saved version and \`setup\`/\`result\` schema, and \`search_workflows\` for its deployment.
2. Done when: the saved automation does this verify fix and nothing else: returns the account's people from PF Person (name, title, tier, buying role, gatekeeper and never-contact marks) and finds an account by its name as well as its id; nothing else changes. It stays read-only and callable from the AI agent; the new output is one more result field \`people\` (text, JSON), every existing field unchanged. Every other input, result field and path keeps its current behaviour.
3. Save with \`compile_and_save_workflow\`, then test-run it read-only with account_id A-1001, with account_id "Carrow &amp; Vale Logistics", and with patch_id PATCH-NAE-03: the first two must return the same account and its people (Helena Marsh, CFO, economic buyer, Tier 1 among them; Joan Pruitt marked gatekeeper, mapped only), the third the same waiting hand-offs and red components as before. It changes no row.
4. Read back: \`open_workflow\` for the new saved version (higher than the one step 1 read) and its schema, the test runs' \`inspect_workflow_run\` output, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows a higher saved version of Pipeline Factory · Read factory records with the fix; test runs read back.
Result IDs: {"entity":"6ae843e69ec43c6ee2dec988"}
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: open_workflow version 2 (step 1 read version 1); result schema now patches, accounts, waiting_handoffs, red_components, people (string, 'People (JSON)'); setup unchanged (patch_id, account_id, both optional strings; account_id description now says it takes the id or the name).
Read back: Pipeline Factory · Read factory records: compile_and_save_workflow ok, version 2, changes 'added 1 statement (line 223), changed 3 statements (lines 16, 253, 348), rewired 3 connections, changed the automation's own description' — the added statement is the PF Person fetch, the 3 changed ones are the trigger result schema, the Groovy node and the return; 8 nodes (5 storage fetches, 1 Groovy, 1 return), no write node.
Read back: Pipeline Factory · Read factory records: test run 6ae84f682099302ffb14c513 (account_id A-1001) COMPLETED: accounts = [A-1001 Carrow &amp; Vale Logistics, PATCH-NAE-03], patches = [PATCH-NAE-03], waiting_handoffs = H-12, H-15, red_components = C08 96.1, people = 13 rows of A-1001 (sha256 6d33d2e0…).
Read back: Pipeline Factory · Read factory records: test run 6ae84f6a9ec43c6ee20c63b3 (account_id 'Carrow &amp; Vale Logistics') COMPLETED, the same account A-1001, the same H-12/H-15 and the same people (same sha256 6d33d2e0…); inspect_workflow_run shows people include {"name":"Helena Marsh","title":"CFO","tier":"t1","buying_role":"economic_buyer","gatekeeper":false,"never_contact":false} and {"name":"Joan Pruitt","title":"Executive Assistant to the CFO","tier":"mapped","buying_role":"gatekeeper","gatekeeper":true,"never_contact":false}.
Read back: Pipeline Factory · Read factory records: test run 6ae84f6b2099302ffb14c55f (patch_id PATCH-NAE-03) COMPLETED: waiting_handoffs = H-07 waiting_person, H-10 rejected, H-12 waiting_person, H-14 late, H-15 waiting_person (every PATCH-NAE-03 row the fetch returned), red_components = C08 96.1, patches = [PATCH-NAE-03]; the hand-off and component code paths were not edited.
Read back: Pipeline Factory · Read factory records: best practice 92 (83 of 85 checks), no fix round needed, version 2.
Read back: Pipeline Factory · Read factory records: search/open shows deployment DEPLOYED definitionVersion 1, savedAfterDeploy true — not deployed, as the task says; the deploy task ships version 2.
Read back: Pipeline Factory · Read factory records: security — read-only (only fetch_records nodes), no secret, no caller identity used to widen access; the person read sends only person_id, account_id, name, title, tier, role, dnc.
Unverified: Pipeline Factory · Read factory records: the patch_id PATCH-NAE-03 output was not diffed against a version 1 run of the same input; the deployed-lane run 6ae84f71f13e536c52dd8b89 could not be inspected (tool answered 'No run with id'). Check: run the deployed version with patch_id PATCH-NAE-03 before the deploy and compare waiting_handoffs and red_components.
Note: Pipeline Factory · Read factory records: people are given for the accounts returned in \`accounts\` (one account when account_id is set, a patch's accounts with patch_id, every account with no input); fields person_id, account_id, name, title, tier, buying_role (PF Person role), gatekeeper (role == gatekeeper), never_contact (dnc).
Note: assumed: an account name match is a case-insensitive exact match on PF Account name, tried only when no account has that id; an unknown id or name still returns empty patches, accounts, hand-offs and people as before.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Execute Groovy code · score already 90 or more
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (OBJ_pf_handoff, OBJ_pf_component, OBJ_pf_person) · score already 90 or more
Note: handover: the result field is \`people\` (JSON text); each row has name, title, tier (t1/t2/t3/backup/mapped), buying_role (economic_buyer, champion, technical_evaluator, business_owner, gatekeeper), gatekeeper true/false and never_contact true/false. account_id accepts the account name too.
Note: feedback:
Bug: inspect_workflow_run cannot find a run that trigger_workflow_run started in the \`workflow\` (deployed) lane.
Context: trigger_workflow_run runType workflow on 6ae843e69ec43c6ee2dec988 with patch_id PATCH-NAE-03 returned runId 6ae84f71f13e536c52dd8b89; inspect_workflow_run runType workflow with that id called twice.
Where: mcp-tool
Evidence: Both answered 'No run with id 6ae84f71f13e536c52dd8b89 exists for automation 6ae843e69ec43c6ee2dec988 on this host.'; test-lane runs inspect fine.
Cause: Unknown — next check: list_workflow_runs runType workflow for this workflow.
Regression: Trigger a deployed callable run, then inspect_workflow_run with the returned runId answers its node details.

### t2 · Deploy Pipeline Factory · Read factory records

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read factory records" and the version the automation task saved (Built so far).
2. Done when: "Pipeline Factory · Read factory records" is deployed with \`definitionVersion\` equal to that saved version.
3. Apply \`deploy_workflow\` once on \`6ae843e69ec43c6ee2dec988\` with deploymentNotes "Demo Studio · verify round 1 fix · Pipeline Factory · Read factory records".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read factory records deployed at the fixed version.
Result IDs: {"entity":"6ae843e69ec43c6ee2dec988"}
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: before deploy, search_workflows version 2 (the version t1 saved, tested and scored), deployment definitionVersion 1, savedAfterDeploy true.
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: deploy_workflow returned ok:true, workflowVersion 2, deployedVersion 2, storedVersion 2, paused false, 'Deployed version 2 of automation 6ae843e69ec43c6ee2dec988.'
Read back: Pipeline Factory · Read factory records 6ae843e69ec43c6ee2dec988: search_workflows after deploy: deployment {"status":"DEPLOYED","deployedVersion":2,"definitionVersion":2,"deployedAt":1793609711065,"savedAfterDeploy":false}, version 2.
Read back: Pipeline Factory · Read factory records: best practice 92 (83 of 85 checks), version 2, read in t1; the version did not change, so it was not read again.
Unverified: Pipeline Factory · Read factory records: deploymentNotes on the tenant's deployment history were not read back (no tool reads them). Check: the automation's deployment history in the builder shows 'Demo Studio · verify round 1 fix · Pipeline Factory · Read factory records' with the plan tag.
Note: Deployed on the release approval as the message gives it: 'yes, deploy Pipeline Factory · Read factory records. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' This is the plan's approval of the accepted spec, not the person's answer to this call.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Execute Groovy code · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (OBJ_pf_handoff, OBJ_pf_component, OBJ_pf_person) · task does not save
Note: handover: the deployed copy is version 2. Callers such as the Pipeline Factory Analyst now get the \`people\` result field and can pass an account name as account_id.

### t3 · Fix Pipeline Factory Analyst

Body:
1. Read: \`get_agent\` on \`e_6ae846ffd96c5f6ba22b98da\` ("Pipeline Factory Analyst", published) for its instructions, tools and model, and the tool ReadFactoryRecords bound to the deployed "Pipeline Factory · Read factory records" (\`6ae843e69ec43c6ee2dec988\`), which now also returns \`people\`.
2. Done when: when a question names an account, read the patch first and use that account's id, never the name, as account_id, and answer buying-team questions from the people the tool returns (eval row 4, the economic buyer, fails); nothing else changes; the ReadFactoryRecords tool description names the new \`people\` result. Also, the model is offered only ReadFactoryRecords and think; EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy come off; nothing else changes where the agent tools can remove them; if they are not attached to the agent and no tool removes them, leave them and say so in notes.
3. Test with \`send_test_message\`, one question at a time: "Who is the economic buyer at Carrow &amp; Vale Logistics?" must answer Helena Marsh (CFO), and "What is waiting on a person in patch PATCH-NAE-03 right now, and why?" must still name H-07, H-10, H-12 and H-15. Read the trace when an answer misses, fix the instructions, test again (two rounds at most). Do not publish: the publish task does.
4. Read back: \`get_agent\` for the instructions and tools, and both answers quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows the new instructions; the economic buyer answer names Helena Marsh.
Result IDs: {"entity":"e_6ae846ffd96c5f6ba22b98da"}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: get_agent version 9, needsPublish true. The instructions now say 'When the question names an account, never pass the account's name as account_id. First call ReadFactoryRecords without an account_id ... find that account in the accounts it returns, and take its account id. Then call ReadFactoryRecords again with that account id' and 'answer questions about the buying team, the economic buyer ... from the people the tool returns'. Goal updated to add the buying team.
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: tool ReadFactoryRecords (e_6ae84708afe7fc590a16efe7) description now reads '... and people, the contacts on each account's buying team with their name, title and role such as economic buyer ... account_id, an account id taken from the accounts this tool returned, never an account name ... Returns: patches, accounts, waiting_handoffs, red_components and people as text.' enabled true, automation 6ae843e69ec43c6ee2dec988.
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: test 'Who is the economic buyer at Carrow &amp; Vale Logistics?' (case e_6ae85085f6f76639f8e6e121) answered 'The economic buyer at Carrow &amp; Vale Logistics is **Helena Marsh (CFO)**.' The trace shows a first ReadFactoryRecords call with no account_id, then ReadFactoryRecords {"patch_id": "PATCH-NAE-03", "account_id": "A-1001"}. Before the change (case e_6ae850399ec43c6ee20cb126) the call was {"account_id": "Carrow &amp; Vale Logistics"}.
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: test 'What is waiting on a person in patch PATCH-NAE-03 right now, and why?' (case e_6ae850a9f6f76639f8e7f65e) answered 'Three hand-offs are actively waiting on a person in PATCH-NAE-03, one is rejected ... and one is late', naming H-07 (RevOps, confidence 74 against threshold 80), H-12 and H-15 (Marcus Ellery), rejected H-10 (GTM engineer, 'Schema check failed — evidence field is missing') and late H-14.
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: trace toolsOffered after the change: think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy, ReadFactoryRecords. GenerateChartWithBlocks is gone, since get_agent shows the capability generateChartTool with on:false.
Unverified: Pipeline Factory Analyst: the changes are in the draft (version 9) only. They are live after the publish task; check with get_agent needsPublish false after publish_agent.
Note: Pipeline Factory Analyst: the tools offered are not yet only ReadFactoryRecords and think. EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy are not attached to the agent (get_agent lists no record for them, and list_capabilities has no key for them), so no agent-builder tool can remove them. They were left in place, with an instruction line telling the agent never to call environment, deploy or cluster tools.
Note: Pipeline Factory Analyst: GenerateChartWithBlocks and ClarifyFromUser were offered too, although every capability read off. I switched off generateChartTool and requestClarification, which created two disabled standard-action records (e_6ae8507bafe7fc590a22d7b6, e_6ae8507cd96c5f6ba2317b62). GenerateChartWithBlocks dropped from the trace; ClarifyFromUser is still offered.
Note: Pipeline Factory Analyst: role unchanged and resent; model unchanged (e_6acca2af70b66f5702f183cc in all three slots).
Note: feedback:
Bug: The requestClarification capability, switched off with update_agent, is still offered to the model as ClarifyFromUser.
Context: update_agent capabilities {generateChartTool:false, requestClarification:false} on agent e_6ae846ffd96c5f6ba22b98da. Both records were created with enabled:false, and get_agent reports on:false.
Where: platform
Evidence: The trace of case e_6ae85085f6f76639f8e6e121 dropped GenerateChartWithBlocks but still offered ClarifyFromUser.
Cause: Unknown — next check: see whether the runtime always injects ClarifyFromUser on useAgentCore agents.
Regression: Switch requestClarification off, run one test message: ClarifyFromUser is absent from toolsOffered.
Note: feedback:
Bug: The model is offered EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy, but no agent record shows them and no tool removes them.
Context: Agent e_6ae846ffd96c5f6ba22b98da. get_agent lists only ReadFactoryRecords and two capability records, and list_capabilities has no key for these tools.
Where: platform
Evidence: The read_trace toolsOffered for cases e_6ae850399ec43c6ee20cb126 and e_6ae85085f6f76639f8e6e121 includes all four Environment* tools.
Cause: Unknown — next check: find the tenant-level or runtime source that injects them.
Regression: get_agent lists these tools with a way to turn them off, or the trace stops offering them.

### t4 · Publish Pipeline Factory Analyst

Body:
1. Read: \`get_agent\` on \`e_6ae846ffd96c5f6ba22b98da\`.
2. Done when: the updated agent is published, so Ask the analyst invokes it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows the agent published.
Result IDs: {"entity":"e_6ae846ffd96c5f6ba22b98da"}
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: publish_agent (confirmed true) returned ok:true, publishedVersion 9, wasAtVersion 3, live true, automationSaid {"response":"success"}.
Read back: Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da: get_agent after publish shows published true, needsPublish false, version 14. The instructions include 'When the question names an account, never pass the account's name as account_id', and ReadFactoryRecords (e_6ae84708afe7fc590a16efe7) is enabled and names the people result.
Unverified: Pipeline Factory Analyst: get_agent lists no deployments for this agent. 'Ask the analyst' reaches it through its caller, which this task did not run. One live Ask-the-analyst call on the published app would settle that it gets version 9's behaviour.
Note: Pipeline Factory Analyst: the record version moved from 9 to 14 during the publish (the platform's own bumps). needsPublish false confirms the draft is the published one.
Note: Answer from the person: yes, publish Pipeline Factory Analyst. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.

