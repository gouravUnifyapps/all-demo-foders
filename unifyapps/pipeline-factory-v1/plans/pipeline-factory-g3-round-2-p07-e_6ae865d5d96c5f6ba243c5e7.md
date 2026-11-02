---
nebula: 3
specId: "e_6ae865d2d96c5f6ba243c574"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P07"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Fit Scorer"},{"action":"publish","kind":"ai-agent","name":"PF · Patch Suggester"},{"action":"publish","kind":"ai-agent","name":"PF · Current Vendor Finder"},{"action":"publish","kind":"ai-agent","name":"PF · Renewal Date Finder"},{"action":"publish","kind":"ai-agent","name":"PF · Battlecard Writer"}]
touches: [{"kind":"ai-agent","name":"PF · Fit Scorer"},{"kind":"ai-agent","name":"PF · Patch Suggester"},{"kind":"ai-agent","name":"PF · Current Vendor Finder"},{"kind":"ai-agent","name":"PF · Renewal Date Finder"},{"kind":"ai-agent","name":"PF · Battlecard Writer"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "b5fc83be-528f-430f-968b-2732d3e4d15a"
pageDesign: 2
createdAt: "2026-11-02T10:28:36.974Z"
runningAt: "2026-11-02T10:28:40.898Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory · G3 round 2 · P07

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Fit Scorer |  | done | 1 |
| t2 | publish | PF · Fit Scorer | t1 | done | 1 |
| t3 | ai-agent | PF · Patch Suggester |  | done | 1 |
| t4 | publish | PF · Patch Suggester | t3 | done | 1 |
| t5 | ai-agent | PF · Current Vendor Finder |  | done | 1 |
| t6 | publish | PF · Current Vendor Finder | t5 | done | 1 |
| t7 | ai-agent | PF · Renewal Date Finder |  | done | 1 |
| t8 | publish | PF · Renewal Date Finder | t7 | done | 1 |
| t9 | ai-agent | PF · Battlecard Writer |  | done | 1 |
| t10 | publish | PF · Battlecard Writer | t9 | done | 1 |

### t1 · Build AI agent PF · Fit Scorer

Body:
1. Read: \`list_agents\` for "PF · Fit Scorer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Fit Scorer" exists with this contract: ai-agent · create · PF · Fit Scorer: registry row C06 (agent, sub-workflow 1. Patch accounts, asks A21); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: score fit out of 60 (up to 15 each: industry, size and complexity, core systems, AI and integration maturity) and map score plus ICP V2 quadrant to best, medium or low fit; the floor of 36 never moves; reads PF Account and PF Source rows through Read component inputs (component_id C06); writes PF Account.fit_score and fit_band (its registered fields) with the four sub-scores in its PF Component run row, only through Save agent output (component_id C06); threshold and routing: under 70 confidence: waiting_person for RevOps, fields not written (Save agent output applies the threshold 70 and routes below it to RevOps); feeds (the register): Account Ranking; schedule in the registry: on change and monthly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never moves the floor of 36; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C06 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C06 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Fit Scorer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86666d96c5f6ba243ce26"}
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: update_agent model e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached); list_models: claude-sonnet-5, vertex_ai, canCallTools true, connectionActive true) changed [responseGenerationSettings, topicExecutionSettings], version 2, readiness canRun true, published false
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: get_agent tools exactly 2, enabled true, topicId GLOBAL: ReadComponentInputs -&gt; 6ae8635446920244f3d5194b (Pipeline Factory · Read component inputs), SaveAgentOutput -&gt; 6ae864829594aa458cc1ce69 (Pipeline Factory · Save agent output), descriptions fix component_id C06; deployments [] (not deployed); memory false; capabilities []
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: instructions state the one job, the steps 'Call ReadComponentInputs first ... component_id "C06"' and 'Call SaveAgentOutput exactly once per run', the output contract (output_type, summary, payload, confidence 0-100, evidence, evidence_tag), 'Pass origin through exactly as the message gives it', and the scope and refusals
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: Please send an email to Arjun Mehta -&gt; 'Sending email is outside my one job as PF · Fit Scorer.' (caseId e_6ae867a946920244f3d628c0 turn 1, toolCalls [])
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26 case e_6ae867a946920244f3d628c0: trace turn 2: ReadComponentInputs {component_id C06, account_id A-1001}, then SaveAgentOutput once {output_type fit_score, payload fit_score 50, fit_band best, icp_quadrant Q1, sub_scores industry 13/size_and_complexity 12/core_systems 12/ai_and_integration_maturity 13, confidence 85, evidence_tag [PUBLIC], model Claude Sonnet 5, origin test}
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: answer: 'Result: duplicate - run_id: RUN-6ae867c546920244f3d62b3b - reason: Re-run of RUN-6ae867c546920244f3d62b3b — already saved, nothing written again - handoff_ids: H-6ae867c546920244f3d62b40'. The first job run (from the send_test_messages call that timed out client-side) saved RUN-6ae867c546920244f3d62b3b
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: Offered by the platform beside the two tools (trace toolsOffered): GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy — not attached tools on the agent (get_agent tools: 2, capabilities: [])
Unverified: PF · Fit Scorer: the original run's row in PF Component run (origin test, output_type, result) is known only from SaveAgentOutput's duplicate reason. Reading that row would settle it, and that read is fde-agent's
Unverified: Security: PF · Fit Scorer is offered the tenant-wide EnvironmentAccess/RequestEnvironmentDeploy/ReleaseEnvironment tools (kubeconfig and deploy actions), which are not attached to it and which no agent-builder tool removes — needs an admin to check why every agent is offered them
Unverified: Security: PF · Fit Scorer has no guardrail (counts.guardrails 0) — needs an admin to decide on content filter and PII masking before publish
Note: Answer from the person: 'Same model, another card: ... use the active card "Claude Sonnet 5 (UnifyApps, Vertex, cached)" e_6ad496812dd4ba5be70afcc1 (still Claude Sonnet 5, family A, as the contract says).' Applied.
Note: handover: family-A agents must use model card e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex); e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key
Note: The job test was run twice: the send_test_messages call timed out client-side after 60 s but ran on the server and made the original run. The rerun, in the same conversation as the refusal so its case id was known, came back duplicate and wrote nothing new. Every test row carries origin test and is left for Pipeline Factory · Reset demo. No delete was made
Note: The model sometimes calls ReadComponentInputs more than once before saving. It still always reads first and saves once.
Note: feedback:
Bug: send_test_messages fails with an MCP client timeout after 60 s, though its description says a call takes several minutes; the agent runs still execute on the server and write rows, but no rows or case ids come back.
Context: send_test_messages on four tool-using Advanced agents (2 messages each, Claude Sonnet 5 Vertex), called in parallel; agents write through Save agent output.
Where: mcp-tool
Evidence: 'tool send_test_messages timed out after 60s' on 4 of 5 parallel calls; later traces showed SaveAgentOutput answering duplicate of runs those timed-out calls created (e.g. RUN-6ae868f8f38e32761819b5e3).
Cause: Unknown — next check: whether the MCP client per-call timeout (60 s) is below the tool's own ~2.5 min trace wait.
Regression: send_test_messages with 2 tool-using messages returns its rows, not a 60 s timeout, when each turn takes about 90 s.

### t2 · Publish PF · Fit Scorer

Body:
1. Read: \`get_agent\` for "PF · Fit Scorer" (its id in Built so far).
2. Done when: "PF · Fit Scorer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Fit Scorer published.
Result IDs: {"entity":"e_6ae86666d96c5f6ba243ce26"}
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: before: list_agents version 2, published false, needsPublish true
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: publish_agent {confirmed: true} -&gt; ok true, published true, publishedVersion 2, live true, automationSaid response 'success' (agent.version 2)
Read back: PF · Fit Scorer e_6ae86666d96c5f6ba243ce26: read back with list_agents ids (same agent record as get_agent): version 7, published true, needsPublish false
Unverified: PF · Fit Scorer: a run of the published version through Pipeline Factory · Run component has not been made here. One Run component call for this component would settle it
Unverified: Security: PF · Fit Scorer is published with no guardrail and is offered tenant-wide EnvironmentAccess/RequestEnvironmentDeploy tools it was not given — needs an admin to review
Note: Release approval: 'yes, publish PF · Fit Scorer. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Not deployed to any app or channel, as the contract says. Pipeline Factory · Run component invokes the agent by id
Note: Model is e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex), the card the person chose in t1-t9; the spec's card e_6acca2af70b66f5702c8b59f answers 401
Note: feedback:
Bug: publish_agent reports publishedVersion 2 (agent.version 2 or 3), but a read straight after shows the agents at version 7 with published true and needsPublish false.
Context: publish_agent {confirmed: true} on five Advanced agents, each at version 2 before publishing, run in parallel.
Where: mcp-tool
Evidence: publish_agent on e_6ae86673afe7fc590a4a3dda answered version 3, publishedVersion 2; list_agents seconds later showed version 7, needsPublish false; the other four went from 2 to 7 the same way.
Cause: Unknown — next check: whether the publish automation writes the agent several times after publish_agent has already read it back.
Regression: after publish_agent, its publishedVersion equals the version list_agents reports.

### t3 · Build AI agent PF · Patch Suggester

Body:
1. Read: \`list_agents\` for "PF · Patch Suggester"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Patch Suggester" exists with this contract: ai-agent · create · PF · Patch Suggester: registry row C07 (agent, sub-workflow 1. Patch accounts, asks A22); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: propose a patch for a new account or an HQ change: geography first, then industry, with confidence and reason; reads PF Account, PF Patch and hand-offs from Headquarters Finder and Headquarters Re-checker through Read component inputs (component_id C07); writes a PF Component run row of output_type patch_proposal (proposed patch, reason), only through Save agent output (component_id C07); threshold and routing: under 80: waiting_person, RevOps decides from evidence (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): RevOps (patch decision); schedule in the registry: on new account or HQ change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a Patch ID; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C07 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C07 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Patch Suggester with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8666ad96c5f6ba243ce39"}
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: update_agent model e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached); list_models: claude-sonnet-5, vertex_ai, canCallTools true, connectionActive true) changed [responseGenerationSettings, topicExecutionSettings], version 2, readiness canRun true, published false
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: get_agent tools exactly 2, enabled true, topicId GLOBAL: ReadComponentInputs -&gt; 6ae8635446920244f3d5194b (Pipeline Factory · Read component inputs), SaveAgentOutput -&gt; 6ae864829594aa458cc1ce69 (Pipeline Factory · Save agent output), descriptions fix component_id C07; deployments [] (not deployed); memory false; capabilities []
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: instructions state the one job, the steps 'Call ReadComponentInputs first ... component_id "C07"' and 'Call SaveAgentOutput exactly once per run', the output contract (output_type, summary, payload, confidence 0-100, evidence, evidence_tag), 'Pass origin through exactly as the message gives it', and the scope and refusals
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: Please send an email to Arjun Mehta -&gt; 'Sending email is outside my one job as PF · Patch Suggester.' (caseId e_6ae868fe2099302ffb2e7ea8 turn 1, pausedForTool false)
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39 case e_6ae868fe2099302ffb2e7ea8: trace turn 2: ReadComponentInputs {C07, A-1001}, ReadComponentInputs {C07, A-1001, patch_id PATCH-NAE-03}, then SaveAgentOutput once {output_type patch_proposal, proposed_patch PATCH-NAE-03, geography 'NA East (HQ city: Columbus, OH)', industry logistics, confidence 83, evidence_tag [HYPOTHESIS], origin test}; no patch_id passed to SaveAgentOutput
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: answer: 'Result: duplicate - run_id: RUN-6ae8685b9594aa458cd57b4a - reason: re-run of RUN-6ae8685b9594aa458cd57b4a: already saved, nothing written again - handoff_ids: (none)'
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: Offered by the platform beside the two tools (trace toolsOffered): GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy — not attached tools on the agent (get_agent tools: 2, capabilities: [])
Unverified: PF · Patch Suggester: the original run's row in PF Component run (origin test, output_type, result) is known only from SaveAgentOutput's duplicate reason. Reading that row would settle it, and that read is fde-agent's
Unverified: Security: PF · Patch Suggester is offered the tenant-wide EnvironmentAccess/RequestEnvironmentDeploy/ReleaseEnvironment tools (kubeconfig and deploy actions), which are not attached to it and which no agent-builder tool removes — needs an admin to check why every agent is offered them
Unverified: Security: PF · Patch Suggester has no guardrail (counts.guardrails 0) — needs an admin to decide on content filter and PII masking before publish
Note: Answer from the person: 'Same model, another card: ... use the active card "Claude Sonnet 5 (UnifyApps, Vertex, cached)" e_6ad496812dd4ba5be70afcc1 (still Claude Sonnet 5, family A, as the contract says).' Applied.
Note: handover: family-A agents must use model card e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex); e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key
Note: The job test was run twice: the send_test_messages call timed out client-side after 60 s but ran on the server and made the original run. The rerun, in the same conversation as the refusal so its case id was known, came back duplicate and wrote nothing new. Every test row carries origin test and is left for Pipeline Factory · Reset demo. No delete was made
Note: The model sometimes calls ReadComponentInputs more than once before saving. It still always reads first and saves once.
Note: Observation: the proposal names the patch by its record id (PATCH-NAE-03, the account's current patch) inside payload.proposed_patch; it passes no patch_id to SaveAgentOutput and writes no PF Account field. If 'never writes a Patch ID' should also forbid naming the id in the payload, the instructions need one more line.

### t4 · Publish PF · Patch Suggester

Body:
1. Read: \`get_agent\` for "PF · Patch Suggester" (its id in Built so far).
2. Done when: "PF · Patch Suggester" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Patch Suggester published.
Result IDs: {"entity":"e_6ae8666ad96c5f6ba243ce39"}
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: before: list_agents version 2, published false, needsPublish true
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: publish_agent {confirmed: true} -&gt; ok true, published true, publishedVersion 2, live true, automationSaid response 'success' (agent.version 2)
Read back: PF · Patch Suggester e_6ae8666ad96c5f6ba243ce39: read back with list_agents ids (same agent record as get_agent): version 7, published true, needsPublish false
Unverified: PF · Patch Suggester: a run of the published version through Pipeline Factory · Run component has not been made here. One Run component call for this component would settle it
Unverified: Security: PF · Patch Suggester is published with no guardrail and is offered tenant-wide EnvironmentAccess/RequestEnvironmentDeploy tools it was not given — needs an admin to review
Note: Release approval: 'yes, publish PF · Patch Suggester. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Not deployed to any app or channel, as the contract says. Pipeline Factory · Run component invokes the agent by id
Note: Model is e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex), the card the person chose in t1-t9; the spec's card e_6acca2af70b66f5702c8b59f answers 401

### t5 · Build AI agent PF · Current Vendor Finder

Body:
1. Read: \`list_agents\` for "PF · Current Vendor Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Current Vendor Finder" exists with this contract: ai-agent · create · PF · Current Vendor Finder: registry row C08 (agent, sub-workflow 1. Patch accounts, asks A23); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find the integration, automation and agent tools a best or medium fit account uses, from vendor case studies, job posts and procurement notices; reads PF Account and PF Source rows (vendor_case_study, job_post, procurement_notice) through Read component inputs (component_id C08); writes a PF Component run row of output_type current_vendors (vendor, product, evidence, first seen date) and hand-offs to Renewal Date Finder and Battlecard Writer, only through Save agent output (component_id C08); threshold and routing: under 60: saved tagged [HYPOTHESIS] (Save agent output applies the threshold 60 and routes below it to tag [HYPOTHESIS]); feeds (the register): Renewal Date Finder; Battlecard Writer; schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never states a vendor without a source link; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C08 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C08 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Current Vendor Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8666dafe7fc590a4a3d96"}
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: update_agent model e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached); list_models: claude-sonnet-5, vertex_ai, canCallTools true, connectionActive true) changed [responseGenerationSettings, topicExecutionSettings], version 2, readiness canRun true, published false
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: get_agent tools exactly 2, enabled true, topicId GLOBAL: ReadComponentInputs -&gt; 6ae8635446920244f3d5194b (Pipeline Factory · Read component inputs), SaveAgentOutput -&gt; 6ae864829594aa458cc1ce69 (Pipeline Factory · Save agent output), descriptions fix component_id C08; deployments [] (not deployed); memory false; capabilities []
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: instructions state the one job, the steps 'Call ReadComponentInputs first ... component_id "C08"' and 'Call SaveAgentOutput exactly once per run', the output contract (output_type, summary, payload, confidence 0-100, evidence, evidence_tag), 'Pass origin through exactly as the message gives it', and the scope and refusals
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: Please send an email to Arjun Mehta -&gt; 'Sending email is outside my one job as PF · Current Vendor Finder.' (caseId e_6ae8690146920244f3d68cb5 turn 1, pausedForTool false)
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96 case e_6ae8690146920244f3d68cb5: trace turn 2: ReadComponentInputs {C08, A-1001} first (4 reads in all, one with draft_id 'NONE', one with person_id P-1002), then SaveAgentOutput once {output_type current_vendors, payload vendors [] (no source names a vendor), confidence 25, evidence_tag [HYPOTHESIS], origin test}
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: answer: 'Result: duplicate - run_id: RUN-6ae8687e2099302ffb2e565c - reason: re-run of RUN-6ae8687e2099302ffb2e565c — already waiting_person, nothing written again - handoff_ids: none'
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: Offered by the platform beside the two tools (trace toolsOffered): GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy — not attached tools on the agent (get_agent tools: 2, capabilities: [])
Unverified: PF · Current Vendor Finder: the original run's row in PF Component run (origin test, output_type, result) is known only from SaveAgentOutput's duplicate reason. Reading that row would settle it, and that read is fde-agent's
Unverified: Security: PF · Current Vendor Finder is offered the tenant-wide EnvironmentAccess/RequestEnvironmentDeploy/ReleaseEnvironment tools (kubeconfig and deploy actions), which are not attached to it and which no agent-builder tool removes — needs an admin to check why every agent is offered them
Unverified: Security: PF · Current Vendor Finder has no guardrail (counts.guardrails 0) — needs an admin to decide on content filter and PII masking before publish
Note: Answer from the person: 'Same model, another card: ... use the active card "Claude Sonnet 5 (UnifyApps, Vertex, cached)" e_6ad496812dd4ba5be70afcc1 (still Claude Sonnet 5, family A, as the contract says).' Applied.
Note: handover: family-A agents must use model card e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex); e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key
Note: The job test was run twice: the send_test_messages call timed out client-side after 60 s but ran on the server and made the original run. The rerun, in the same conversation as the refusal so its case id was known, came back duplicate and wrote nothing new. Every test row carries origin test and is left for Pipeline Factory · Reset demo. No delete was made
Note: The model sometimes calls ReadComponentInputs more than once before saving. It still always reads first and saves once.
Note: Observation for Save agent output (not this agent): with confidence 25, under C08's threshold 60, the saved run is waiting_person, while the contract says 'under 60: saved tagged [HYPOTHESIS]'. The routing belongs to the automation.
Note: Observation: the agent saved an empty vendor list rather than naming a vendor without a source link (the contract's 'never states a vendor without a source link' held). It said handoffs_in and full source text were not readable in the read output; Read component inputs' output may be too large or lack C08's vendor source rows for A-1001.

### t6 · Publish PF · Current Vendor Finder

Body:
1. Read: \`get_agent\` for "PF · Current Vendor Finder" (its id in Built so far).
2. Done when: "PF · Current Vendor Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Current Vendor Finder published.
Result IDs: {"entity":"e_6ae8666dafe7fc590a4a3d96"}
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: before: list_agents version 2, published false, needsPublish true
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: publish_agent {confirmed: true} -&gt; ok true, published true, publishedVersion 2, live true, automationSaid response 'success' (agent.version 2)
Read back: PF · Current Vendor Finder e_6ae8666dafe7fc590a4a3d96: read back with list_agents ids (same agent record as get_agent): version 7, published true, needsPublish false
Unverified: PF · Current Vendor Finder: a run of the published version through Pipeline Factory · Run component has not been made here. One Run component call for this component would settle it
Unverified: Security: PF · Current Vendor Finder is published with no guardrail and is offered tenant-wide EnvironmentAccess/RequestEnvironmentDeploy tools it was not given — needs an admin to review
Note: Release approval: 'yes, publish PF · Current Vendor Finder. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Not deployed to any app or channel, as the contract says. Pipeline Factory · Run component invokes the agent by id
Note: Model is e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex), the card the person chose in t1-t9; the spec's card e_6acca2af70b66f5702c8b59f answers 401

### t7 · Build AI agent PF · Renewal Date Finder

Body:
1. Read: \`list_agents\` for "PF · Renewal Date Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Renewal Date Finder" exists with this contract: ai-agent · create · PF · Renewal Date Finder: registry row C09 (agent, sub-workflow 1. Patch accounts, asks A24); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: estimate each vendor's renewal as 3 years from the earliest evidence unless a later contract signal exists, and raise a renewal signal 9 months before; reads hand-offs from Current Vendor Finder and PF Source rows through Read component inputs (component_id C09); writes a PF Component run row of output_type renewal_estimate and, inside 9 months, a hand-off to Buying Signal Spotter, only through Save agent output (component_id C09); threshold and routing: under 60: no signal (result no_action) (Save agent output applies the threshold 60 and routes below it to no signal); feeds (the register): Buying Signal Spotter; schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a PF Signal itself (Buying Signal Spotter owns it); outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C09 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C09 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Renewal Date Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86671d96c5f6ba243ce77"}
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: update_agent model e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached); list_models: claude-sonnet-5, vertex_ai, canCallTools true, connectionActive true) changed [responseGenerationSettings, topicExecutionSettings], version 2, readiness canRun true, published false
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: get_agent tools exactly 2, enabled true, topicId GLOBAL: ReadComponentInputs -&gt; 6ae8635446920244f3d5194b (Pipeline Factory · Read component inputs), SaveAgentOutput -&gt; 6ae864829594aa458cc1ce69 (Pipeline Factory · Save agent output), descriptions fix component_id C09; deployments [] (not deployed); memory false; capabilities []
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: instructions state the one job, the steps 'Call ReadComponentInputs first ... component_id "C09"' and 'Call SaveAgentOutput exactly once per run', the output contract (output_type, summary, payload, confidence 0-100, evidence, evidence_tag), 'Pass origin through exactly as the message gives it', and the scope and refusals
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: Please send an email to Arjun Mehta -&gt; 'Sending email is outside my one job as PF · Renewal Date Finder.' (caseId e_6ae86904f38e32761819b6c8 turn 1, pausedForTool false)
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77 case e_6ae86904f38e32761819b6c8: trace turn 2: ReadComponentInputs {C09, A-1001} first (3 reads), then SaveAgentOutput once {output_type renewal_estimate, estimated_renewal 2027-07-02, within_9_months true, handoff_to [Buying Signal Spotter], confidence 55, evidence_tag [HYPOTHESIS], origin test}
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: answer: 'Result: duplicate - Run ID: RUN-6ae86946f38e32761819c15a - Reason: Re-run of an existing run that is already waiting_person — nothing was written'
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: Offered by the platform beside the two tools (trace toolsOffered): GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy — not attached tools on the agent (get_agent tools: 2, capabilities: [])
Unverified: PF · Renewal Date Finder: the original run's row in PF Component run (origin test, output_type, result) is known only from SaveAgentOutput's duplicate reason. Reading that row would settle it, and that read is fde-agent's
Unverified: Security: PF · Renewal Date Finder is offered the tenant-wide EnvironmentAccess/RequestEnvironmentDeploy/ReleaseEnvironment tools (kubeconfig and deploy actions), which are not attached to it and which no agent-builder tool removes — needs an admin to check why every agent is offered them
Unverified: Security: PF · Renewal Date Finder has no guardrail (counts.guardrails 0) — needs an admin to decide on content filter and PII masking before publish
Note: Answer from the person: 'Same model, another card: ... use the active card "Claude Sonnet 5 (UnifyApps, Vertex, cached)" e_6ad496812dd4ba5be70afcc1 (still Claude Sonnet 5, family A, as the contract says).' Applied.
Note: handover: family-A agents must use model card e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex); e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key
Note: The job test was run twice: the send_test_messages call timed out client-side after 60 s but ran on the server and made the original run. The rerun, in the same conversation as the refusal so its case id was known, came back duplicate and wrote nothing new. Every test row carries origin test and is left for Pipeline Factory · Reset demo. No delete was made
Note: The model sometimes calls ReadComponentInputs more than once before saving. It still always reads first and saves once.
Note: Observation for Save agent output (not this agent): with confidence 55, under C09's threshold 60, the run is waiting_person, while the contract says 'under 60: no signal (result no_action)'. The routing belongs to the automation.
Note: Observation: the agent reported earliest_evidence as absent (the Current Vendor Finder hand-off was not in what it read) and used the vendor_renewal signal S-04 as the contract signal instead.

### t8 · Publish PF · Renewal Date Finder

Body:
1. Read: \`get_agent\` for "PF · Renewal Date Finder" (its id in Built so far).
2. Done when: "PF · Renewal Date Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Renewal Date Finder published.
Result IDs: {"entity":"e_6ae86671d96c5f6ba243ce77"}
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: before: list_agents version 2, published false, needsPublish true
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: publish_agent {confirmed: true} -&gt; ok true, published true, publishedVersion 2, live true, automationSaid response 'success' (agent.version 2)
Read back: PF · Renewal Date Finder e_6ae86671d96c5f6ba243ce77: read back with list_agents ids (same agent record as get_agent): version 7, published true, needsPublish false
Unverified: PF · Renewal Date Finder: a run of the published version through Pipeline Factory · Run component has not been made here. One Run component call for this component would settle it
Unverified: Security: PF · Renewal Date Finder is published with no guardrail and is offered tenant-wide EnvironmentAccess/RequestEnvironmentDeploy tools it was not given — needs an admin to review
Note: Release approval: 'yes, publish PF · Renewal Date Finder. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Not deployed to any app or channel, as the contract says. Pipeline Factory · Run component invokes the agent by id
Note: Model is e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex), the card the person chose in t1-t9; the spec's card e_6acca2af70b66f5702c8b59f answers 401

### t9 · Build AI agent PF · Battlecard Writer

Body:
1. Read: \`list_agents\` for "PF · Battlecard Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Battlecard Writer" exists with this contract: ai-agent · create · PF · Battlecard Writer: registry row C10 (agent, sub-workflow 1. Patch accounts, asks A25); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: draft battlecard changes per vendor: shortfalls, switch path, proof and objection answers; reads hand-offs from Current Vendor Finder and PF Source rows through Read component inputs (component_id C10); writes a PF Component run row of output_type battlecard_draft, always waiting_person for product marketing, only through Save agent output (component_id C10); threshold and routing: every draft waits for product marketing's approval (threshold 0, routed to Product marketing) (Save agent output applies the threshold 0 and routes below it to Product marketing approves each); feeds (the register): Message Writer; schedule in the registry: on vendor change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never publishes a battlecard; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C10 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C10 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Battlecard Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86673afe7fc590a4a3dda"}
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: update_agent model e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached); list_models: claude-sonnet-5, vertex_ai, canCallTools true, connectionActive true) changed [responseGenerationSettings, topicExecutionSettings], version 2, readiness canRun true, published false
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: get_agent tools exactly 2, enabled true, topicId GLOBAL: ReadComponentInputs -&gt; 6ae8635446920244f3d5194b (Pipeline Factory · Read component inputs), SaveAgentOutput -&gt; 6ae864829594aa458cc1ce69 (Pipeline Factory · Save agent output), descriptions fix component_id C10; deployments [] (not deployed); memory false; capabilities []
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: instructions state the one job, the steps 'Call ReadComponentInputs first ... component_id "C10"' and 'Call SaveAgentOutput exactly once per run', the output contract (output_type, summary, payload, confidence 0-100, evidence, evidence_tag), 'Pass origin through exactly as the message gives it', and the scope and refusals
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: Please send an email to Arjun Mehta -&gt; 'Sending an email is outside my one job as PF · Battlecard Writer.' (caseId e_6ae8690746920244f3d68d11 turn 1, pausedForTool false)
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda case e_6ae8690746920244f3d68d11: trace turn 2: ReadComponentInputs {C10, A-1001} first (5 reads, one with account_id 'Carrow &amp; Vale Logistics'), then SaveAgentOutput once {output_type battlecard_draft, one battlecard for the unnamed incumbent tooling with shortfalls, switch_path, proof, 3 objection_answers, confidence 35, evidence_tag [HYPOTHESIS], origin test}
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: answer: 'Result: duplicate - run_id: RUN-6ae868f8f38e32761819b5e3 - reason: re-run of RUN-6ae868f8f38e32761819b5e3: already saved, nothing written again - handoff_ids: H-6ae868f9f38e32761819b5e6'
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: Offered by the platform beside the two tools (trace toolsOffered): GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy — not attached tools on the agent (get_agent tools: 2, capabilities: [])
Unverified: PF · Battlecard Writer: the original run's row in PF Component run (origin test, output_type, result) is known only from SaveAgentOutput's duplicate reason. Reading that row would settle it, and that read is fde-agent's
Unverified: Security: PF · Battlecard Writer is offered the tenant-wide EnvironmentAccess/RequestEnvironmentDeploy/ReleaseEnvironment tools (kubeconfig and deploy actions), which are not attached to it and which no agent-builder tool removes — needs an admin to check why every agent is offered them
Unverified: Security: PF · Battlecard Writer has no guardrail (counts.guardrails 0) — needs an admin to decide on content filter and PII masking before publish
Note: Answer from the person: 'Same model, another card: ... use the active card "Claude Sonnet 5 (UnifyApps, Vertex, cached)" e_6ad496812dd4ba5be70afcc1 (still Claude Sonnet 5, family A, as the contract says).' Applied.
Note: handover: family-A agents must use model card e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex); e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key
Note: The job test was run twice: the send_test_messages call timed out client-side after 60 s but ran on the server and made the original run. The rerun, in the same conversation as the refusal so its case id was known, came back duplicate and wrote nothing new. Every test row carries origin test and is left for Pipeline Factory · Reset demo. No delete was made
Note: The model sometimes calls ReadComponentInputs more than once before saving. It still always reads first and saves once.
Note: Observation for Save agent output (not this agent): C10's contract says every draft is waiting_person for product marketing (threshold 0), but the original run RUN-6ae868f8f38e32761819b5e3 is reported 'already saved' with a hand-off H-6ae868f9f38e32761819b5e6. The routing belongs to the automation; worth a check by its owner before the demo.

### t10 · Publish PF · Battlecard Writer

Body:
1. Read: \`get_agent\` for "PF · Battlecard Writer" (its id in Built so far).
2. Done when: "PF · Battlecard Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Battlecard Writer published.
Result IDs: {"entity":"e_6ae86673afe7fc590a4a3dda"}
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: before: list_agents version 2, published false, needsPublish true
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: publish_agent {confirmed: true} -&gt; ok true, published true, publishedVersion 2, live true, automationSaid response 'success' (agent.version 3)
Read back: PF · Battlecard Writer e_6ae86673afe7fc590a4a3dda: read back with list_agents ids (same agent record as get_agent): version 7, published true, needsPublish false
Unverified: PF · Battlecard Writer: a run of the published version through Pipeline Factory · Run component has not been made here. One Run component call for this component would settle it
Unverified: Security: PF · Battlecard Writer is published with no guardrail and is offered tenant-wide EnvironmentAccess/RequestEnvironmentDeploy tools it was not given — needs an admin to review
Note: Release approval: 'yes, publish PF · Battlecard Writer. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.' (the plan's approval)
Note: Not deployed to any app or channel, as the contract says. Pipeline Factory · Run component invokes the agent by id
Note: Model is e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, Vertex), the card the person chose in t1-t9; the spec's card e_6acca2af70b66f5702c8b59f answers 401

