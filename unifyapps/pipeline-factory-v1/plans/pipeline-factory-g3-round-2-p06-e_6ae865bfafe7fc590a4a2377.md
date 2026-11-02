---
nebula: 3
specId: "e_6ae865bdd96c5f6ba243c034"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P06"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Duplicate Finder"},{"action":"publish","kind":"ai-agent","name":"PF · Parent Company Linker"},{"action":"publish","kind":"ai-agent","name":"PF · Headquarters Finder"},{"action":"publish","kind":"ai-agent","name":"PF · Headquarters Re-checker"},{"action":"publish","kind":"ai-agent","name":"PF · New Account Finder"}]
touches: [{"kind":"ai-agent","name":"PF · Duplicate Finder"},{"kind":"ai-agent","name":"PF · Parent Company Linker"},{"kind":"ai-agent","name":"PF · Headquarters Finder"},{"kind":"ai-agent","name":"PF · Headquarters Re-checker"},{"kind":"ai-agent","name":"PF · New Account Finder"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "90272984-2177-4b54-b4eb-2f55d3498efa"
pageDesign: 2
createdAt: "2026-11-02T10:28:14.645Z"
runningAt: "2026-11-02T10:28:21.795Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory · G3 round 2 · P06

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Duplicate Finder |  | done | 1 |
| t2 | publish | PF · Duplicate Finder | t1 | done | 1 |
| t3 | ai-agent | PF · Parent Company Linker |  | done | 1 |
| t4 | publish | PF · Parent Company Linker | t3 | done | 1 |
| t5 | ai-agent | PF · Headquarters Finder |  | done | 1 |
| t6 | publish | PF · Headquarters Finder | t5 | done | 1 |
| t7 | ai-agent | PF · Headquarters Re-checker |  | done | 1 |
| t8 | publish | PF · Headquarters Re-checker | t7 | done | 1 |
| t9 | ai-agent | PF · New Account Finder |  | done | 1 |
| t10 | publish | PF · New Account Finder | t9 | done | 1 |

### t1 · Build AI agent PF · Duplicate Finder

Body:
1. Read: \`list_agents\` for "PF · Duplicate Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Duplicate Finder" exists with this contract: ai-agent · create · PF · Duplicate Finder: registry row C01 (agent, sub-workflow 1. Patch accounts, asks A16); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find duplicate patch accounts: normalise keys (domain, legal name, LinkedIn ID, HubSpot ID, email), match exactly, score near-matches 0 to 100 and log the reasoning; reads PF Account rows of the patch through Read component inputs (component_id C01); writes a PF Component run of output_type merge_proposal per pair (pair, score, keys compared, reasoning); it never merges or deletes a row (a merge is a proposal in this demo), only through Save agent output (component_id C01); threshold and routing: 95 or more: proposal marked merge; 80 to 95: waiting_person for RevOps; under 80: kept separate, no hand-off (Save agent output applies the threshold 95 and routes below it to RevOps); feeds (the register): Parent Company Linker; schedule in the registry: every 15 min (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never deletes or merges an account itself; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C01 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C01 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Duplicate Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86680afe7fc590a4a3f53","tools":["e_6ae8669bf410ab7b2f151f8a","e_6ae8669bf410ab7b2f151f8d"]}
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: update_agent changed responseGenerationSettings, topicExecutionSettings (model) to card e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)" (list_models: claude-sonnet-5, vertex_ai, connectionActive true); version 2, published false, readiness canRun true
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: tools exactly 2 bound, enabled true, topicId GLOBAL: Read_component_inputs e_6ae8669bf410ab7b2f151f8a -&gt; 6ae8635446920244f3d5194b; Save_agent_output e_6ae8669bf410ab7b2f151f8d -&gt; 6ae864829594aa458cc1ce69; memory false, deployments [] (not deployed)
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: instructions state the one job, read with Read_component_inputs first, save once with Save_agent_output, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through, scope and refusals
Read back: PF · Duplicate Finder job test (case e_6ae868d9f6f76639f8391744, runAgainToFindAnswer after a send_test_messages row with no caseId): trace: Read_component_inputs {"component_id": "C01", "account_id": "A-1001"}, then {"component_id": "C01", "patch_id": "PATCH-NAE-03"}, then Save_agent_output {component_id C01, account_id A-1001, output_type merge_proposal, summary "No action: only one PF Account record (A-1001, Carrow &amp; Vale Logistics) was available...", payload {"pairs": []...}, confidence 0, evidence_tag public, origin test}
Read back: PF · Duplicate Finder job test e_6ae868d9f6f76639f8391744: Save agent output result duplicate of RUN-6ae86809fbdd550a9a518109, first run waiting_person (confidence under threshold); answer: "## Result: duplicate (run_id \`RUN-6ae86809fbdd550a9a518109\`) ... re-run of an existing run that is already \`waiting_person\` — nothing new was written ... No duplicate pairs found for A-1001"
Read back: PF · Duplicate Finder refusal test (case e_6ae867bc46920244f3d62a8f): "Sending an email is outside my job — I'm the PF · Duplicate Finder agent, and my one job is to find duplicate patch accounts, score near-matches, and save a merge proposal for RevOps." toolCalls []
Unverified: PF · Duplicate Finder: the model is also offered 7 platform tools not bound by this task (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) while get_agent shows capabilities []; settle with list_capabilities agentId and the agent's settings screen
Unverified: Security: the five guardrail rules other than denied topics are not set on PF · Duplicate Finder — needs an admin to turn them on in the agent's settings if the demo needs them
Unverified: PF · Duplicate Finder: the first job run's own answer (from send_test_messages, no caseId returned) is not read; its saved result is waiting_person per the later run's duplicate reason
Note: Instruction file: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/.sessions/ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1/work/4a2377-agent-builder-1/instr-duplicate-finder.md
Note: Model card per the person's answer: e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key, so the agent runs on e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, family A); confirmed by list_models and one test message (case e_6ae867a5fbdd550a9a513f49 on PF · Duplicate Finder, refusal answered)
Note: Each job test ran twice (send_test_messages, then send_test_message with runAgainToFindAnswer); Save agent output is idempotent per component+account+person+play+output_type, so the second run answered duplicate and wrote no new row. Rows carry origin test, left for Pipeline Factory · Reset demo
Note: handover: Save agent output stores evidence_tag only as lower-case public/hypothesis; rejects a save with no evidence, output_type or confidence; C02/C03 payload must hold ultimate_parent_lock / hq_city. Under the threshold it answers waiting_person, at or over saved; no no_action result
Note: Security rules touched: rule 4 the only write path is Save agent output, writing only the component's registered fields; rule 5 no secret in instructions or tools; tools take no user id (rule 2)
Note: feedback:
Bug: get_agent reports capabilities [] and exactly 2 bound tools, but the trace shows the model offered 7 more tools (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy).
Context: 5 new Advanced agents made by create_agent with no capabilities on orbit.uat.unifyapps.com, e.g. agent e_6ae86680afe7fc590a4a3f53.
Where: unknown
Evidence: get_agent "capabilities": [], counts.tools 2; read_trace case e_6ae868d9f6f76639f8391744 toolsOffered lists the 7 extra tools plus Read_component_inputs and Save_agent_output.
Cause: Unknown — next check: list_capabilities with agentId, and whether the Environment* tools are tenant-wide defaults.
Regression: on a new agent with no capabilities on, get_agent's capabilities and read_trace's toolsOffered name the same non-bound tools.
Note: feedback:
Bug: send_test_messages timed out at the MCP client ("tool send_test_messages timed out after 60s") for 3 of 5 parallel calls, though the tool says a call takes several minutes; the runs went on server-side and saved, with no caseId returned.
Context: 5 parallel send_test_messages calls of 2 messages each on orbit.uat.unifyapps.com.
Where: mcp-tool
Evidence: 'MCP server "plugin:ua:agent-builder" tool "send_test_messages" timed out after 60s' on agents e_6ae86687d96c5f6ba243cfb8, e_6ae8668bafe7fc590a4a3fec, e_6ae8668ef410ab7b2f151c47; a later run answered duplicate of RUN-6ae8686646920244f3d661b0, so the first run had saved.
Cause: Suspected: the MCP client's 60 s timeout is shorter than the tool's documented multi-minute run.
Regression: a send_test_messages call of 2 tool-calling questions returns its rows instead of a 60 s client timeout.

### t2 · Publish PF · Duplicate Finder

Body:
1. Read: \`get_agent\` for "PF · Duplicate Finder" (its id in Built so far).
2. Done when: "PF · Duplicate Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Duplicate Finder published.
Result IDs: {"entity":"e_6ae86680afe7fc590a4a3f53"}
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: before publish list_agents showed version 2, published false, needsPublish true (the draft tested in its ai-agent task)
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: publish_agent confirmed true answered ok true, publishedVersion 2, live true, automationSaid "success"
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: read back by list_agents after publish: published true, needsPublish false, version 7
Read back: PF · Duplicate Finder e_6ae86680afe7fc590a4a3f53: get_agent after publish: version 7, published true, needsPublish false, models runs/picksTask/answerGeneration e_6ad496812dd4ba5be70afcc1, tools Save_agent_output e_6ae8669bf410ab7b2f151f8d and Read_component_inputs e_6ae8669bf410ab7b2f151f8a enabled, deployments []
Unverified: PF · Duplicate Finder: not invoked through Pipeline Factory · Run component after publish; settle with one Run component call for its component
Note: Yes as given: "yes, publish PF · Duplicate Finder. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval)
Note: Not deployed to any app or channel, as the spec says; publish only
Note: The record version went from 2 to 7 during publish with no write from this task (publish automation's own saves); needsPublish false

### t3 · Build AI agent PF · Parent Company Linker

Body:
1. Read: \`list_agents\` for "PF · Parent Company Linker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Parent Company Linker" exists with this contract: ai-agent · create · PF · Parent Company Linker: registry row C02 (agent, sub-workflow 1. Patch accounts, asks A17); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: link each company to its parent, subsidiaries and divisions, propose divisions that buy separately, and set the outreach lock at the top parent; reads PF Account rows and PF Source rows (press, filings) through Read component inputs (component_id C02); writes PF Account.ultimate_parent_lock (its registered field) and a PF Component run row with parent_id, children and division proposals, only through Save agent output (component_id C02); threshold and routing: under 80: waiting_person for RevOps, the lock is not written (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Headquarters Finder; Patch Suggester; schedule in the registry: on new account, HQ change or M&amp;A news (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a division proposal is never applied without RevOps; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C02 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C02 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Parent Company Linker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86684d96c5f6ba243cf6a","tools":["e_6ae8669fafe7fc590a4a4656","e_6ae8669fd96c5f6ba243d509"]}
Read back: PF · Parent Company Linker e_6ae86684d96c5f6ba243cf6a: update_agent changed responseGenerationSettings, topicExecutionSettings (model) to card e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)" (list_models: claude-sonnet-5, vertex_ai, connectionActive true); version 2, published false, readiness canRun true
Read back: PF · Parent Company Linker e_6ae86684d96c5f6ba243cf6a: tools exactly 2 bound, enabled true, topicId GLOBAL: Read_component_inputs e_6ae8669fafe7fc590a4a4656 -&gt; 6ae8635446920244f3d5194b; Save_agent_output e_6ae8669fd96c5f6ba243d509 -&gt; 6ae864829594aa458cc1ce69; memory false, deployments [] (not deployed)
Read back: PF · Parent Company Linker e_6ae86684d96c5f6ba243cf6a: instructions state the one job, read with Read_component_inputs first, save once with Save_agent_output, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through, scope and refusals
Read back: PF · Parent Company Linker job test (case e_6ae868fa46920244f3d68c2a, runAgainToFindAnswer after a send_test_messages row with no caseId): trace: Read_component_inputs {"component_id": "C02", "account_id": "A-1001"}, then Save_agent_output {component_id C02, account_id A-1001, output_type parent_link, payload {"parent_id": "A-1001", "children": [], "division_proposals": [], "ultimate_parent_lock": "A-1001"}, confidence 85, evidence_tag hypothesis, origin test}
Read back: PF · Parent Company Linker job test e_6ae868fa46920244f3d68c2a: Save agent output result duplicate of RUN-6ae867faf13e536c52ebd003, first run waiting_person (confidence under threshold); answer: "**Result:** \`duplicate\` — run_id \`RUN-6ae867faf13e536c52ebd003\` (reason: \"re-run of RUN-6ae867faf13e536c52ebd003: already waiting_person, nothing written again\")"
Read back: PF · Parent Company Linker refusal test (case e_6ae867e49ec43c6ee230c4c1): "Sending an email is outside my job; I only link companies to their parent, subsidiaries, and divisions, and set the outreach lock at the top parent (PF · Parent Company Linker, component C02)." toolCalls []
Unverified: PF · Parent Company Linker: the model is also offered 7 platform tools not bound by this task (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) while get_agent shows capabilities []; settle with list_capabilities agentId and the agent's settings screen
Unverified: Security: the five guardrail rules other than denied topics are not set on PF · Parent Company Linker — needs an admin to turn them on in the agent's settings if the demo needs them
Unverified: PF · Parent Company Linker: the first job run's own answer (from send_test_messages, no caseId returned) is not read; its saved result is waiting_person per the later run's duplicate reason
Note: Instruction file: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/.sessions/ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1/work/4a2377-agent-builder-1/instr-parent-company-linker.md
Note: Model card per the person's answer: e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key, so the agent runs on e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, family A); confirmed by list_models and one test message (case e_6ae867a5fbdd550a9a513f49 on PF · Duplicate Finder, refusal answered)
Note: Each job test ran twice (send_test_messages, then send_test_message with runAgainToFindAnswer); Save agent output is idempotent per component+account+person+play+output_type, so the second run answered duplicate and wrote no new row. Rows carry origin test, left for Pipeline Factory · Reset demo
Note: handover: Save agent output stores evidence_tag only as lower-case public/hypothesis; rejects a save with no evidence, output_type or confidence; C02/C03 payload must hold ultimate_parent_lock / hq_city. Under the threshold it answers waiting_person, at or over saved; no no_action result
Note: Security rules touched: rule 4 the only write path is Save agent output, writing only the component's registered fields; rule 5 no secret in instructions or tools; tools take no user id (rule 2)

### t4 · Publish PF · Parent Company Linker

Body:
1. Read: \`get_agent\` for "PF · Parent Company Linker" (its id in Built so far).
2. Done when: "PF · Parent Company Linker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Parent Company Linker published.
Result IDs: {"entity":"e_6ae86684d96c5f6ba243cf6a"}
Read back: PF · Parent Company Linker e_6ae86684d96c5f6ba243cf6a: before publish list_agents showed version 2, published false, needsPublish true (the draft tested in its ai-agent task)
Read back: PF · Parent Company Linker e_6ae86684d96c5f6ba243cf6a: publish_agent confirmed true answered ok true, publishedVersion 2, live true, automationSaid "success"
Read back: PF · Parent Company Linker e_6ae86684d96c5f6ba243cf6a: read back by list_agents after publish: published true, needsPublish false, version 7
Unverified: PF · Parent Company Linker: not invoked through Pipeline Factory · Run component after publish; settle with one Run component call for its component
Note: Yes as given: "yes, publish PF · Parent Company Linker. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval)
Note: Not deployed to any app or channel, as the spec says; publish only
Note: The record version went from 2 to 7 during publish with no write from this task (publish automation's own saves); needsPublish false

### t5 · Build AI agent PF · Headquarters Finder

Body:
1. Read: \`list_agents\` for "PF · Headquarters Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Headquarters Finder" exists with this contract: ai-agent · create · PF · Headquarters Finder: registry row C03 (agent, sub-workflow 1. Patch accounts, asks A18); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find the parent's headquarters city, state and country by weighing sources; reads PF Account and PF Source rows (filings, press) through Read component inputs (component_id C03); writes PF Account.hq_city (its registered field) and a PF Component run row with state, country, other candidates and evidence, only through Save agent output (component_id C03); threshold and routing: under 80: waiting_person, RevOps picks from the candidates (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Patch Suggester; schedule in the registry: on new account (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never guesses a city without a source; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C03 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C03 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86687d96c5f6ba243cfb8","tools":["e_6ae866a4afe7fc590a4a4789","e_6ae866a4afe7fc590a4a478d"]}
Read back: PF · Headquarters Finder e_6ae86687d96c5f6ba243cfb8: update_agent changed responseGenerationSettings, topicExecutionSettings (model) to card e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)" (list_models: claude-sonnet-5, vertex_ai, connectionActive true); version 2, published false, readiness canRun true
Read back: PF · Headquarters Finder e_6ae86687d96c5f6ba243cfb8: tools exactly 2 bound, enabled true, topicId GLOBAL: Read_component_inputs e_6ae866a4afe7fc590a4a4789 -&gt; 6ae8635446920244f3d5194b; Save_agent_output e_6ae866a4afe7fc590a4a478d -&gt; 6ae864829594aa458cc1ce69; memory false, deployments [] (not deployed)
Read back: PF · Headquarters Finder e_6ae86687d96c5f6ba243cfb8: instructions state the one job, read with Read_component_inputs first, save once with Save_agent_output, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through, scope and refusals
Read back: PF · Headquarters Finder job test (case e_6ae86933f6f76639f839acc4, runAgainToFindAnswer after a send_test_messages row with no caseId): trace: Read_component_inputs {"component_id": "C03", "account_id": "A-1001"} (plus 2 more reads with draft_id D-01 and person_id P-1001), then Save_agent_output {component_id C03, account_id A-1001, output_type hq_location, payload {"hq_city": "", "hq_state": "", "hq_country": "", "other_candidates": [], sources F-01..F-04}, confidence 10, evidence_tag hypothesis, origin test}
Read back: PF · Headquarters Finder job test e_6ae86933f6f76639f839acc4: Save agent output result duplicate of RUN-6ae8686646920244f3d661b0, first run waiting_person (confidence under threshold); answer: "**Outcome:** \`duplicate\` — run_id \`RUN-6ae8686646920244f3d661b0\` (\"re-run of RUN-6ae8686646920244f3d661b0: already waiting_person, nothing written again\") ... none of them state a headquarters city ... I recorded \`hq_city\` as absent"
Read back: PF · Headquarters Finder refusal test (case e_6ae8692046920244f3d68f3a): "Sending an email is outside my one job as the PF · Headquarters Finder agent — I only find and save a parent company's headquarters city, state, and country..."
Unverified: PF · Headquarters Finder: the model is also offered 7 platform tools not bound by this task (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) while get_agent shows capabilities []; settle with list_capabilities agentId and the agent's settings screen
Unverified: Security: the five guardrail rules other than denied topics are not set on PF · Headquarters Finder — needs an admin to turn them on in the agent's settings if the demo needs them
Unverified: PF · Headquarters Finder: the first job run's own answer (from send_test_messages, no caseId returned) is not read; its saved result is waiting_person per the later run's duplicate reason
Note: Instruction file: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/.sessions/ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1/work/4a2377-agent-builder-1/instr-headquarters-finder.md
Note: Model card per the person's answer: e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key, so the agent runs on e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, family A); confirmed by list_models and one test message (case e_6ae867a5fbdd550a9a513f49 on PF · Duplicate Finder, refusal answered)
Note: Each job test ran twice (send_test_messages, then send_test_message with runAgainToFindAnswer); Save agent output is idempotent per component+account+person+play+output_type, so the second run answered duplicate and wrote no new row. Rows carry origin test, left for Pipeline Factory · Reset demo
Note: handover: Save agent output stores evidence_tag only as lower-case public/hypothesis; rejects a save with no evidence, output_type or confidence; C02/C03 payload must hold ultimate_parent_lock / hq_city. Under the threshold it answers waiting_person, at or over saved; no no_action result
Note: Security rules touched: rule 4 the only write path is Save agent output, writing only the component's registered fields; rule 5 no secret in instructions or tools; tools take no user id (rule 2)

### t6 · Publish PF · Headquarters Finder

Body:
1. Read: \`get_agent\` for "PF · Headquarters Finder" (its id in Built so far).
2. Done when: "PF · Headquarters Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Finder published.
Result IDs: {"entity":"e_6ae86687d96c5f6ba243cfb8"}
Read back: PF · Headquarters Finder e_6ae86687d96c5f6ba243cfb8: before publish list_agents showed version 2, published false, needsPublish true (the draft tested in its ai-agent task)
Read back: PF · Headquarters Finder e_6ae86687d96c5f6ba243cfb8: publish_agent confirmed true answered ok true, publishedVersion 2, live true, automationSaid "success"
Read back: PF · Headquarters Finder e_6ae86687d96c5f6ba243cfb8: read back by list_agents after publish: published true, needsPublish false, version 7
Unverified: PF · Headquarters Finder: not invoked through Pipeline Factory · Run component after publish; settle with one Run component call for its component
Note: Yes as given: "yes, publish PF · Headquarters Finder. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval)
Note: Not deployed to any app or channel, as the spec says; publish only
Note: The record version went from 2 to 7 during publish with no write from this task (publish automation's own saves); needsPublish false

### t7 · Build AI agent PF · Headquarters Re-checker

Body:
1. Read: \`list_agents\` for "PF · Headquarters Re-checker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Headquarters Re-checker" exists with this contract: ai-agent · create · PF · Headquarters Re-checker: registry row C04 (monitor, sub-workflow 1. Patch accounts, asks A19); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: re-check headquarters of companies with move or M&amp;A news and raise an alert on any change; reads PF Account.hq_city and PF Source press rows through Read component inputs (component_id C04); writes a PF Component run row of output_type hq_change_alert (old and new HQ, source) and a hand-off to Patch Suggester, only through Save agent output (component_id C04); threshold and routing: under 80: waiting_person for RevOps; no change: result no_action (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Patch Suggester; patch control tower; schedule in the registry: nightly on move or M&amp;A news; quarterly on all (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes hq_city itself (Headquarters Finder owns it); outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C04 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C04 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Re-checker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8668bafe7fc590a4a3fec","tools":["e_6ae866a9afe7fc590a4a4836","e_6ae866a9afe7fc590a4a483a"]}
Read back: PF · Headquarters Re-checker e_6ae8668bafe7fc590a4a3fec: update_agent changed responseGenerationSettings, topicExecutionSettings (model) to card e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)" (list_models: claude-sonnet-5, vertex_ai, connectionActive true); version 2, published false, readiness canRun true
Read back: PF · Headquarters Re-checker e_6ae8668bafe7fc590a4a3fec: tools exactly 2 bound, enabled true, topicId GLOBAL: Read_component_inputs e_6ae866a9afe7fc590a4a4836 -&gt; 6ae8635446920244f3d5194b; Save_agent_output e_6ae866a9afe7fc590a4a483a -&gt; 6ae864829594aa458cc1ce69; memory false, deployments [] (not deployed)
Read back: PF · Headquarters Re-checker e_6ae8668bafe7fc590a4a3fec: instructions state the one job, read with Read_component_inputs first, save once with Save_agent_output, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through, scope and refusals
Read back: PF · Headquarters Re-checker job test (case e_6ae8696546920244f3d69a7b, runAgainToFindAnswer after a send_test_messages row with no caseId): trace: Read_component_inputs {"component_id": "C04", "account_id": "A-1001"} (3 reads), then Save_agent_output {component_id C04, account_id A-1001, output_type hq_change_alert, summary "No headquarters change found for Carrow &amp; Vale Logistics (no action)...", payload {"old_hq": "Columbus OH", "new_hq": "Columbus OH", "source": "none found...", "changed": false}, confidence 35, evidence_tag hypothesis, origin test}
Read back: PF · Headquarters Re-checker job test e_6ae8696546920244f3d69a7b: Save agent output result duplicate of RUN-6ae868c09ec43c6ee2312dd8, first run waiting_person (confidence under threshold); answer: "**Result:** \`duplicate\` — run_id \`RUN-6ae868c09ec43c6ee2312dd8\` (this matches an already-saved run that is \`waiting_person\`; nothing new was written)"
Read back: PF · Headquarters Re-checker refusal test (case e_6ae86923fbdd550a9a51bbdc): "Sending an email is outside my one job as the PF · Headquarters Re-checker agent — I only re-check the headquarters of companies with move or M&amp;A news..."
Unverified: PF · Headquarters Re-checker: the model is also offered 7 platform tools not bound by this task (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) while get_agent shows capabilities []; settle with list_capabilities agentId and the agent's settings screen
Unverified: Security: the five guardrail rules other than denied topics are not set on PF · Headquarters Re-checker — needs an admin to turn them on in the agent's settings if the demo needs them
Unverified: PF · Headquarters Re-checker: the first job run's own answer (from send_test_messages, no caseId returned) is not read; its saved result is waiting_person per the later run's duplicate reason
Note: Instruction file: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/.sessions/ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1/work/4a2377-agent-builder-1/instr-headquarters-re-checker.md
Note: Model card per the person's answer: e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key, so the agent runs on e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, family A); confirmed by list_models and one test message (case e_6ae867a5fbdd550a9a513f49 on PF · Duplicate Finder, refusal answered)
Note: Each job test ran twice (send_test_messages, then send_test_message with runAgainToFindAnswer); Save agent output is idempotent per component+account+person+play+output_type, so the second run answered duplicate and wrote no new row. Rows carry origin test, left for Pipeline Factory · Reset demo
Note: handover: Save agent output stores evidence_tag only as lower-case public/hypothesis; rejects a save with no evidence, output_type or confidence; C02/C03 payload must hold ultimate_parent_lock / hq_city. Under the threshold it answers waiting_person, at or over saved; no no_action result
Note: Security rules touched: rule 4 the only write path is Save agent output, writing only the component's registered fields; rule 5 no secret in instructions or tools; tools take no user id (rule 2)
Note: No change saves once with "changed": false and "no action" in the summary, per the person's answer; seen in the trace summary "(no action)"

### t8 · Publish PF · Headquarters Re-checker

Body:
1. Read: \`get_agent\` for "PF · Headquarters Re-checker" (its id in Built so far).
2. Done when: "PF · Headquarters Re-checker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Re-checker published.
Result IDs: {"entity":"e_6ae8668bafe7fc590a4a3fec"}
Read back: PF · Headquarters Re-checker e_6ae8668bafe7fc590a4a3fec: before publish list_agents showed version 2, published false, needsPublish true (the draft tested in its ai-agent task)
Read back: PF · Headquarters Re-checker e_6ae8668bafe7fc590a4a3fec: publish_agent confirmed true answered ok true, publishedVersion 2, live true, automationSaid "success"
Read back: PF · Headquarters Re-checker e_6ae8668bafe7fc590a4a3fec: read back by list_agents after publish: published true, needsPublish false, version 2
Unverified: PF · Headquarters Re-checker: not invoked through Pipeline Factory · Run component after publish; settle with one Run component call for its component
Note: Yes as given: "yes, publish PF · Headquarters Re-checker. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval)
Note: Not deployed to any app or channel, as the spec says; publish only

### t9 · Build AI agent PF · New Account Finder

Body:
1. Read: \`list_agents\` for "PF · New Account Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · New Account Finder" exists with this contract: ai-agent · create · PF · New Account Finder: registry row C05 (agent, sub-workflow 1. Patch accounts, asks A20); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find new candidate accounts from closed-won lookalikes and the seven other sources, dropping fit under 36, customers, open deals, partners, competitors and DNC; reads PF Account, PF Source (web visits, events, job changes) and PF Suppression through Read component inputs (component_id C05); writes a PF Component run row of output_type account_suggestion per candidate (name, source, why, estimated fit), only through Save agent output (component_id C05); threshold and routing: under 70: not suggested (result no_action); 70 and over: waiting_person for RevOps (Save agent output applies the threshold 70 and routes below it to RevOps); feeds (the register): Fit Scorer; schedule in the registry: weekly lookalikes; daily 7 sources (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; suggests to RevOps, never adds an account; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C05 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C05 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · New Account Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8668ef410ab7b2f151c47","tools":["e_6ae866add96c5f6ba243d764","e_6ae866adafe7fc590a4a48d8"]}
Read back: PF · New Account Finder e_6ae8668ef410ab7b2f151c47: update_agent changed responseGenerationSettings, topicExecutionSettings (model) to card e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)" (list_models: claude-sonnet-5, vertex_ai, connectionActive true); version 2, published false, readiness canRun true
Read back: PF · New Account Finder e_6ae8668ef410ab7b2f151c47: tools exactly 2 bound, enabled true, topicId GLOBAL: Read_component_inputs e_6ae866add96c5f6ba243d764 -&gt; 6ae8635446920244f3d5194b; Save_agent_output e_6ae866adafe7fc590a4a48d8 -&gt; 6ae864829594aa458cc1ce69; memory false, deployments [] (not deployed)
Read back: PF · New Account Finder e_6ae8668ef410ab7b2f151c47: instructions state the one job, read with Read_component_inputs first, save once with Save_agent_output, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through, scope and refusals
Read back: PF · New Account Finder job test (case e_6ae869982099302ffb2e91b9, runAgainToFindAnswer after a send_test_messages row with no caseId): trace: Read_component_inputs {"component_id": "C05", "account_id": "A-1001"}, then Save_agent_output {component_id C05, account_id A-1001, output_type account_suggestion, summary "No new candidate to suggest: account A-1001 ... already has an open deal in progress...", payload candidates [{name Carrow &amp; Vale Logistics, estimated_fit 49, suggested false}], confidence 49, evidence_tag public, origin test}
Read back: PF · New Account Finder job test e_6ae869982099302ffb2e91b9: Save agent output result duplicate of RUN-6ae868dff13e536c52ec2ee3, first run waiting_person (confidence under threshold); answer: "**Result:** \`duplicate\` — this is a re-run of an earlier job already in \`waiting_person\` state ... **run_id:** \`RUN-6ae868dff13e536c52ec2ee3\`"
Read back: PF · New Account Finder refusal test (case e_6ae86928fbdd550a9a51bc55): "Sending an email is outside my one job as the PF · New Account Finder agent — I only find new candidate accounts from closed-won lookalikes and other signal sources..."
Unverified: PF · New Account Finder: the model is also offered 7 platform tools not bound by this task (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) while get_agent shows capabilities []; settle with list_capabilities agentId and the agent's settings screen
Unverified: Security: the five guardrail rules other than denied topics are not set on PF · New Account Finder — needs an admin to turn them on in the agent's settings if the demo needs them
Unverified: PF · New Account Finder: the first job run's own answer (from send_test_messages, no caseId returned) is not read; its saved result is waiting_person per the later run's duplicate reason
Note: Instruction file: /home/user/all-demo-foders/unifyapps/pipeline-factory-v1/.sessions/ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1/work/4a2377-agent-builder-1/instr-new-account-finder.md
Note: Model card per the person's answer: e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key, so the agent runs on e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, family A); confirmed by list_models and one test message (case e_6ae867a5fbdd550a9a513f49 on PF · Duplicate Finder, refusal answered)
Note: Each job test ran twice (send_test_messages, then send_test_message with runAgainToFindAnswer); Save agent output is idempotent per component+account+person+play+output_type, so the second run answered duplicate and wrote no new row. Rows carry origin test, left for Pipeline Factory · Reset demo
Note: handover: Save agent output stores evidence_tag only as lower-case public/hypothesis; rejects a save with no evidence, output_type or confidence; C02/C03 payload must hold ultimate_parent_lock / hq_city. Under the threshold it answers waiting_person, at or over saved; no no_action result
Note: Security rules touched: rule 4 the only write path is Save agent output, writing only the component's registered fields; rule 5 no secret in instructions or tools; tools take no user id (rule 2)
Note: Not-suggested candidates carry "suggested": false (seen in the trace); the summary said "No new candidate to suggest" rather than the words "no action"

### t10 · Publish PF · New Account Finder

Body:
1. Read: \`get_agent\` for "PF · New Account Finder" (its id in Built so far).
2. Done when: "PF · New Account Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · New Account Finder published.
Result IDs: {"entity":"e_6ae8668ef410ab7b2f151c47"}
Read back: PF · New Account Finder e_6ae8668ef410ab7b2f151c47: before publish list_agents showed version 2, published false, needsPublish true (the draft tested in its ai-agent task)
Read back: PF · New Account Finder e_6ae8668ef410ab7b2f151c47: publish_agent confirmed true answered ok true, publishedVersion 2, live true, automationSaid "success"
Read back: PF · New Account Finder e_6ae8668ef410ab7b2f151c47: read back by list_agents after publish: published true, needsPublish false, version 7
Unverified: PF · New Account Finder: not invoked through Pipeline Factory · Run component after publish; settle with one Run component call for its component
Note: Yes as given: "yes, publish PF · New Account Finder. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval)
Note: Not deployed to any app or channel, as the spec says; publish only
Note: The record version went from 2 to 7 during publish with no write from this task (publish automation's own saves); needsPublish false

