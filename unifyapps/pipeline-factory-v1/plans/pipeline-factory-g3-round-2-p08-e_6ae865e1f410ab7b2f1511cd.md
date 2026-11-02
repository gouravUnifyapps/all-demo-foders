---
nebula: 3
specId: "e_6ae865dff410ab7b2f1511b3"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P08"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Buying Signal Spotter"},{"action":"publish","kind":"ai-agent","name":"PF · Company Facts Collector"},{"action":"publish","kind":"ai-agent","name":"PF · Use Case Matcher"},{"action":"publish","kind":"ai-agent","name":"PF · Case for Change Drafter"}]
touches: [{"kind":"ai-agent","name":"PF · Buying Signal Spotter"},{"kind":"ai-agent","name":"PF · Company Facts Collector"},{"kind":"ai-agent","name":"PF · Use Case Matcher"},{"kind":"ai-agent","name":"PF · Case for Change Drafter"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "97abaf8a-1c24-4d5f-bef8-774a299ee661"
pageDesign: 2
createdAt: "2026-11-02T10:28:49.219Z"
runningAt: "2026-11-02T10:28:53.562Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P08

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Buying Signal Spotter |  | done | 1 |
| t2 | publish | PF · Buying Signal Spotter | t1 | running | 1 |
| t3 | ai-agent | PF · Company Facts Collector |  | done | 1 |
| t4 | publish | PF · Company Facts Collector | t3 | running | 1 |
| t5 | ai-agent | PF · Use Case Matcher |  | done | 1 |
| t6 | publish | PF · Use Case Matcher | t5 | running | 1 |
| t7 | ai-agent | PF · Case for Change Drafter |  | done | 1 |
| t8 | publish | PF · Case for Change Drafter | t7 | running | 1 |

### t1 · Build AI agent PF · Buying Signal Spotter

Body:
1. Read: \`list_agents\` for "PF · Buying Signal Spotter"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Buying Signal Spotter" exists with this contract: ai-agent · create · PF · Buying Signal Spotter: registry row C11 (agent, sub-workflow 2. Account selection, asks A28); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: watch the signal sources, record each signal (company, type, date, source link, strength), verify company match and date, score confidence, and send strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) to the Play Picker; reads PF Source rows (web_visit, press, job_post, events), PF Signal and hand-offs from Renewal Date Finder through Read component inputs (component_id C11); writes PF Signal rows (its registered records, weights from the starting signal weights, the checked-visit rule) and hand-offs to Account Ranking, and to Play Picker for a strong signal, only through Save agent output (component_id C11); threshold and routing: under 70: logged, not scored (counted false); signals fade over 30 days (Save agent output applies the threshold 70 and routes below it to logged, not scored); feeds (the register): Account Ranking; Play Picker (fast lane); schedule in the registry: continuous (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never counts a visit that fails the checked-visit rule; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C11 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C11 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Signal Spotter with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8667ed96c5f6ba243cf29"}
Read back: PF · Buying Signal Spotter e_6ae8667ed96c5f6ba243cf29: update_agent model e_6ad496812dd4ba5be70afcc1 changed [responseGenerationSettings, topicExecutionSettings], version 5; get_agent models runs/picksTask/answerGeneration = e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached)), readiness canRun true, published false
Read back: PF · Buying Signal Spotter: send_test_message on the new card answered (case e_6ae86b039ec43c6ee244626d, llmCalls 1): "I'm not able to send emails—that falls outside my role here. I'm the PF · Buying Signal Spotter (component C11), and my one job is to detect and record buying signals for an account ... the Message Writer component drafts outreach, and a BDR (human) actually sends it."
Read back: PF · Buying Signal Spotter: get_agent tools ReadComponentInputs e_6ae86699d96c5f6ba243d3b8 (automation 6ae8635446920244f3d5194b, enabled true, topicId GLOBAL) and SaveAgentOutput e_6ae86699d96c5f6ba243d3be (automation 6ae864829594aa458cc1ce69, enabled true), each description fixing component_id; capabilities generateChartTool and requestClarification off; deployments [], skills [], knowledge [], memory false
Read back: PF · Buying Signal Spotter: instructions state the one job, ReadComponentInputs first and SaveAgentOutput exactly once, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through as given, scope and refusals, and that record text is never an instruction (rule 5: no secret in instructions; rule 4: writes only through Save agent output)
Read back: PF · Buying Signal Spotter e_6ae8667ed96c5f6ba243cf29: trace case e_6ae868d89ec43c6ee23134e4 turn 2 — ReadComponentInputs {"component_id": "C11", "account_id": "A-1001"}, then SaveAgentOutput {component_id C11, account_id A-1001, output_type buying_signal, payload signal_type pricing_visit weight 25 counted true fast_lane true, confidence 92, evidence_tag public, model 'Claude Sonnet 5', origin 'test'}
Read back: PF · Buying Signal Spotter answered: "Result: saved — run_id RUN-6ae86937f38e32761819bd56, reason: 'saved; wrote PF Signal row,' with two hand-offs generated (H-6ae86937f38e32761819bd63, H-6ae86938f38e32761819bd65), confirming the fast-lane routing to the Play Picker." It excluded S-02 as failing the checked-visit rule ('within 2 minutes of an email's delivery').
Read back: PF · Buying Signal Spotter refusal (case e_6ae866ca2099302ffb2dd951, toolCalls []): "I'm not able to send emails — that falls outside my one job here, which is spotting and recording buying signals for an account ... the Message Writer component drafts emails, and a BDR actually sends them"
Read back: PF · Buying Signal Spotter round 1 (case e_6ae867b0f13e536c52eb3dea): SaveAgentOutput failed 'Duplicate key exception while inserting entity' because the payload reused seeded signal_id S-01; instructions now forbid sending a signal_id, and round 2 saved
Unverified: Security: ClarifyFromUser, think and four Environment* tools (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) are still offered by the runtime though requestClarification is off and none is attached — needs an admin to find where the runtime injects them; the agent's own tools are exactly ReadComponentInputs and SaveAgentOutput
Unverified: Guardrails: none on the record (get_agent guardrails []); the other five rules are read-only here
Unverified: Security: the agent is shared tenant-wide through the 'All Users' and 'testing' groups (tenantWide in get_agent), which no agent share changes
Note: Answer from the person: (b): switch each agent to 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the card that passed your tests (same model, family A; the named card answers 401 invalid x-api-key). Set it with update_agent, read it back with get_agent, and send one test message to prove it answers; then report done so the publish task can run.
Note: The spec's model card e_6acca2af70b66f5702c8b59f was replaced by e_6ad496812dd4ba5be70afcc1 on the person's answer; the job-run proofs (Read then Save with origin test) were made on this same card in the first attempt.
Note: handover: Save agent output takes evidence_tag only as bare 'public' or 'hypothesis' (anything else is stored as none, and a fact with none becomes hypothesis); an agent must never send signal_id or fact_id in the payload, or the insert fails with a duplicate-key error.
Note: handover: a tool-calling first turn returns no caseId; send a greeting turn first, then the job message on that caseId, and read_trace turn 2.
Note: Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made.
Note: feedback:
Bug: Model card Claude Sonnet 5 (e_6acca2af70b66f5702c8b59f) is listed usable but every agent run on it fails.
Context: send_test_messages on new Advanced agents whose only model is that card.
Where: platform
Evidence: list_models shows connectionFound true, connectionActive true; each run returns HTTP 500 'Workflow execution failed' with root cause 401 authentication_error 'invalid x-api-key'.
Cause: Confirmed: the connection behind the card holds an API key Anthropic rejects.
Regression: send_test_message on an agent using e_6acca2af70b66f5702c8b59f answers instead of failing with 401 invalid x-api-key.
Note: feedback:
Bug: Switching requestClarification off does not stop the runtime offering ClarifyFromUser, and every agent is offered think plus four Environment* tools nobody attached.
Context: update_agent capabilities {generateChartTool:false, requestClarification:false}; get_agent then reports both off with records enabled:false.
Where: platform
Evidence: Next trace (case e_6ae868d89ec43c6ee23134e4) drops GenerateChartWithBlocks but still offers ClarifyFromUser, think, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy; none of the Environment* tools is in list_capabilities.
Cause: Unknown — next check: where the runtime injects ClarifyFromUser and the Environment* tools.
Regression: With requestClarification off, read_trace toolsOffered omits ClarifyFromUser; an agent with no Environment* tools attached is not offered them.
Note: feedback:
Bug: Pipeline Factory · Save agent output throws a raw 'Duplicate key exception while inserting entity' instead of answering rejected when the payload carries an existing signal_id or fact_id.
Context: The C11 agent passed payload signal_id 'S-01' (a seeded PF Signal id); the automation copies pay.signal_id / pay.fact_id into create_record.
Where: unknown
Evidence: Trace case e_6ae867b0f13e536c52eb3dea turn 2: SaveAgentOutput failed 'Duplicate key exception while inserting entity', no run_id. After the instructions forbade sending those ids, the same save answered saved RUN-6ae86937f38e32761819bd56.
Cause: Confirmed: create_record takes the caller's signal_id/fact_id, colliding with the unique key of existing rows.
Regression: Save agent output for C11 with payload signal_id of an existing PF Signal row returns result rejected naming the id, not a thrown error.
Note: feedback:
Bug: send_test_messages times out at the MCP client (60s) on tool-calling agents, and a tool-calling first turn returns no caseId.
Context: send_test_messages with two messages on PF · Use Case Matcher and PF · Case for Change Drafter, agents that write.
Where: mcp-tool
Evidence: 'tool send_test_messages timed out after 60s' while the server-side runs completed and saved (RUN-6ae867569594aa458cd53263, RUN-6ae867c4f13e536c52eb489a). Workaround: a greeting turn to get a caseId, then the job message on that caseId, then read_trace turn 2.
Cause: Suspected: the client MCP timeout (60s) is shorter than the tool's own wait.
Regression: send_test_messages with a tool-calling question taking over 60s returns its rows instead of a client timeout.
Note: feature:
Feature: A read-only way to find the caseId of a test run whose first turn called a tool.
Evidence: Tool-calling first turns return no caseId and runAgainToFindAnswer would write twice; each agent needed a greeting turn first to learn a caseId.
Benefit: Write-capable agents can be tested in one run and traced without a second write or workaround.
Scope: agent-builder MCP test tools; not how agents run.
Acceptance: A first-turn tool-calling test on a write agent yields a caseId that read_trace opens, with no second run.

### t2 · Publish PF · Buying Signal Spotter

Body:
1. Read: \`get_agent\` for "PF · Buying Signal Spotter" (its id in Built so far).
2. Done when: "PF · Buying Signal Spotter" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Signal Spotter published.

### t3 · Build AI agent PF · Company Facts Collector

Body:
1. Read: \`list_agents\` for "PF · Company Facts Collector"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Company Facts Collector" exists with this contract: ai-agent · create · PF · Company Facts Collector: registry row C16 (agent, sub-workflow 3. Account research, asks A36); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: extract sourced company facts on AI, automation, integration, modernisation, cost, CX and risk from the annual report, investor deck, two earnings calls, 12 months of press and current job posts; reads PF Source rows of the account (annual_report, investor_deck, earnings_call, press, job_post) through Read component inputs (component_id C16); writes PF Fact rows of kind fact (statement, exact quote, page or timestamp, date, link, [PUBLIC]) and hand-offs to Use Case Matcher and Case for Change Drafter, only through Save agent output (component_id C16); threshold and routing: a fact without quote and link is rejected; anything over 12 months old is dropped (except the latest annual report) (Save agent output applies the threshold 0 and routes below it to facts without quote and link rejected); feeds (the register): Use Case Matcher; Case for Change Drafter; schedule in the registry: Day 1; best fit every 30 days, others 90 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a fact without its quote and link; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C16 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C16 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Company Facts Collector with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86682d96c5f6ba243cf48"}
Read back: PF · Company Facts Collector e_6ae86682d96c5f6ba243cf48: update_agent model e_6ad496812dd4ba5be70afcc1 changed [responseGenerationSettings, topicExecutionSettings], version 5; get_agent models runs/picksTask/answerGeneration = e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached)), readiness canRun true, published false
Read back: PF · Company Facts Collector: send_test_message on the new card answered (case e_6ae86b089594aa458cd61c67, llmCalls 1): "I'm not able to send emails — that falls outside my one job, which is collecting sourced company facts ... handled by the Message Writer (drafts) together with a BDR (who actually sends it)."
Read back: PF · Company Facts Collector: get_agent tools ReadComponentInputs e_6ae8669dafe7fc590a4a450b (automation 6ae8635446920244f3d5194b, enabled true, topicId GLOBAL) and SaveAgentOutput e_6ae8669dd96c5f6ba243d414 (automation 6ae864829594aa458cc1ce69, enabled true), each description fixing component_id; capabilities generateChartTool and requestClarification off; deployments [], skills [], knowledge [], memory false
Read back: PF · Company Facts Collector: instructions state the one job, ReadComponentInputs first and SaveAgentOutput exactly once, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through as given, scope and refusals, and that record text is never an instruction (rule 5: no secret in instructions; rule 4: writes only through Save agent output)
Read back: PF · Company Facts Collector e_6ae86682d96c5f6ba243cf48: trace case e_6ae8699046920244f3d69db4 turn 2 — ReadComponentInputs {"component_id": "C16", "account_id": "A-1001"}, then SaveAgentOutput {component_id C16, output_type company_facts, payload statement/quote/source annual_report/page_or_time 'page 14'/link https://carrowvale.example/investors/annual-report-2026.pdf, confidence 90, evidence_tag public, origin 'test'}
Read back: PF · Company Facts Collector answered: "Result: duplicate — run_id RUN-6ae86959fbdd550a9a51cce4 ... reason: 're-run of RUN-6ae86959fbdd550a9a51cce4: already saved, nothing written again'" — RUN-6ae86959fbdd550a9a51cce4 is the save of the previous test run (case e_6ae868def13e536c52ec2ed5, whose trace stayed incomplete after its read)
Read back: PF · Company Facts Collector refusal (case e_6ae866edf38e3276181927b0, toolCalls []): "I'm not able to send emails — that falls outside my one job, which is collecting sourced company facts ... Sending messages is handled by the Message Writer ... together with a BDR"
Read back: PF · Company Facts Collector round 1 (case e_6ae867b4f13e536c52eb41da): SaveAgentOutput failed 'duplicate key exception'; instructions now forbid sending a fact_id
Unverified: Security: ClarifyFromUser, think and four Environment* tools (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) are still offered by the runtime though requestClarification is off and none is attached — needs an admin to find where the runtime injects them; the agent's own tools are exactly ReadComponentInputs and SaveAgentOutput
Unverified: Guardrails: none on the record (get_agent guardrails []); the other five rules are read-only here
Unverified: Security: the agent is shared tenant-wide through the 'All Users' and 'testing' groups (tenantWide in get_agent), which no agent share changes
Note: Answer from the person: (b): switch each agent to 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the card that passed your tests (same model, family A; the named card answers 401 invalid x-api-key). Set it with update_agent, read it back with get_agent, and send one test message to prove it answers; then report done so the publish task can run.
Note: The spec's model card e_6acca2af70b66f5702c8b59f was replaced by e_6ad496812dd4ba5be70afcc1 on the person's answer; the job-run proofs (Read then Save with origin test) were made on this same card in the first attempt.
Note: handover: Save agent output takes evidence_tag only as bare 'public' or 'hypothesis' (anything else is stored as none, and a fact with none becomes hypothesis); an agent must never send signal_id or fact_id in the payload, or the insert fails with a duplicate-key error.
Note: handover: a tool-calling first turn returns no caseId; send a greeting turn first, then the job message on that caseId, and read_trace turn 2.
Note: Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made.
Note: feedback:
Bug: Model card Claude Sonnet 5 (e_6acca2af70b66f5702c8b59f) is listed usable but every agent run on it fails.
Context: send_test_messages on new Advanced agents whose only model is that card.
Where: platform
Evidence: list_models shows connectionFound true, connectionActive true; each run returns HTTP 500 'Workflow execution failed' with root cause 401 authentication_error 'invalid x-api-key'.
Cause: Confirmed: the connection behind the card holds an API key Anthropic rejects.
Regression: send_test_message on an agent using e_6acca2af70b66f5702c8b59f answers instead of failing with 401 invalid x-api-key.
Note: feedback:
Bug: Switching requestClarification off does not stop the runtime offering ClarifyFromUser, and every agent is offered think plus four Environment* tools nobody attached.
Context: update_agent capabilities {generateChartTool:false, requestClarification:false}; get_agent then reports both off with records enabled:false.
Where: platform
Evidence: Next trace (case e_6ae868d89ec43c6ee23134e4) drops GenerateChartWithBlocks but still offers ClarifyFromUser, think, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy; none of the Environment* tools is in list_capabilities.
Cause: Unknown — next check: where the runtime injects ClarifyFromUser and the Environment* tools.
Regression: With requestClarification off, read_trace toolsOffered omits ClarifyFromUser; an agent with no Environment* tools attached is not offered them.

### t4 · Publish PF · Company Facts Collector

Body:
1. Read: \`get_agent\` for "PF · Company Facts Collector" (its id in Built so far).
2. Done when: "PF · Company Facts Collector" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Company Facts Collector published.

### t5 · Build AI agent PF · Use Case Matcher

Body:
1. Read: \`list_agents\` for "PF · Use Case Matcher"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Use Case Matcher" exists with this contract: ai-agent · create · PF · Use Case Matcher: registry row C17 (agent, sub-workflow 3. Account research, asks A37); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: match VEP-CFC use cases to the account's industry and core systems, score the evidence and keep the top 3 with two supporting facts (or one fact plus engagement), tagged with pattern and outcome; reads PF Fact rows of kind fact and PF Source rows through Read component inputs (component_id C17); writes PF Fact rows of kind use_case (UC-ID, pattern, outcome, supporting facts) and a hand-off to Case for Change Drafter, only through Save agent output (component_id C17); threshold and routing: under 70: saved as a question only, tagged [HYPOTHESIS], never a claim (Save agent output applies the threshold 70 and routes below it to shown only as a question); feeds (the register): Case for Change Drafter; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; uses only VEP-CFC use cases (a UC-ID); outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C17 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C17 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Use Case Matcher with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86685f410ab7b2f151b2f"}
Read back: PF · Use Case Matcher e_6ae86685f410ab7b2f151b2f: update_agent model e_6ad496812dd4ba5be70afcc1 changed [responseGenerationSettings, topicExecutionSettings], version 5; get_agent models runs/picksTask/answerGeneration = e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached)), readiness canRun true, published false
Read back: PF · Use Case Matcher: send_test_message on the new card answered (case e_6ae86b0cf6f76639f83a38eb, llmCalls 1): "I'm not able to send emails — that falls outside my one job, which is matching VEP-CFC use cases to an account's industry and core systems (component C17 of the Pipeline Factory)."
Read back: PF · Use Case Matcher: get_agent tools ReadComponentInputs e_6ae866a1f410ab7b2f1520e7 (automation 6ae8635446920244f3d5194b, enabled true, topicId GLOBAL) and SaveAgentOutput e_6ae866a1afe7fc590a4a4721 (automation 6ae864829594aa458cc1ce69, enabled true), each description fixing component_id; capabilities generateChartTool and requestClarification off; deployments [], skills [], knowledge [], memory false
Read back: PF · Use Case Matcher: instructions state the one job, ReadComponentInputs first and SaveAgentOutput exactly once, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through as given, scope and refusals, and that record text is never an instruction (rule 5: no secret in instructions; rule 4: writes only through Save agent output)
Read back: PF · Use Case Matcher e_6ae86685f410ab7b2f151b2f: trace case e_6ae867b89ec43c6ee230be92 turn 2 — ReadComponentInputs {"component_id": "C17", "account_id": "A-1001"}, then SaveAgentOutput {component_id C17, output_type use_case_match, payload uc_id UC-LOG-014, pattern, outcome, supporting_facts [F-01, F-02], top_use_cases UC-LOG-014/UC-LOG-022/UC-LOG-031, confidence 90, origin 'test'}
Read back: PF · Use Case Matcher answered: "Result: duplicate — Run ID: RUN-6ae867569594aa458cd53263 ... a prior C17 run already produced this same use-case match for A-1001, so nothing new was written ... (handoff H-6ae867569594aa458cd53284) already feeds the Case for Change Drafter" — RUN-6ae867569594aa458cd53263 is the save of this agent's first test run (send_test_messages timed out client-side, server run completed)
Read back: PF · Use Case Matcher refusal (case e_6ae868e546920244f3d688f7): "I'm not able to send emails — that falls outside my one job here, which is matching VEP-CFC use cases ... handled by the Message Writer ... and then a BDR"
Unverified: Security: ClarifyFromUser, think and four Environment* tools (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) are still offered by the runtime though requestClarification is off and none is attached — needs an admin to find where the runtime injects them; the agent's own tools are exactly ReadComponentInputs and SaveAgentOutput
Unverified: Guardrails: none on the record (get_agent guardrails []); the other five rules are read-only here
Unverified: Security: the agent is shared tenant-wide through the 'All Users' and 'testing' groups (tenantWide in get_agent), which no agent share changes
Note: Answer from the person: (b): switch each agent to 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the card that passed your tests (same model, family A; the named card answers 401 invalid x-api-key). Set it with update_agent, read it back with get_agent, and send one test message to prove it answers; then report done so the publish task can run.
Note: The spec's model card e_6acca2af70b66f5702c8b59f was replaced by e_6ad496812dd4ba5be70afcc1 on the person's answer; the job-run proofs (Read then Save with origin test) were made on this same card in the first attempt.
Note: handover: Save agent output takes evidence_tag only as bare 'public' or 'hypothesis' (anything else is stored as none, and a fact with none becomes hypothesis); an agent must never send signal_id or fact_id in the payload, or the insert fails with a duplicate-key error.
Note: handover: a tool-calling first turn returns no caseId; send a greeting turn first, then the job message on that caseId, and read_trace turn 2.
Note: Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made.
Note: feedback:
Bug: Model card Claude Sonnet 5 (e_6acca2af70b66f5702c8b59f) is listed usable but every agent run on it fails.
Context: send_test_messages on new Advanced agents whose only model is that card.
Where: platform
Evidence: list_models shows connectionFound true, connectionActive true; each run returns HTTP 500 'Workflow execution failed' with root cause 401 authentication_error 'invalid x-api-key'.
Cause: Confirmed: the connection behind the card holds an API key Anthropic rejects.
Regression: send_test_message on an agent using e_6acca2af70b66f5702c8b59f answers instead of failing with 401 invalid x-api-key.
Note: feedback:
Bug: Switching requestClarification off does not stop the runtime offering ClarifyFromUser, and every agent is offered think plus four Environment* tools nobody attached.
Context: update_agent capabilities {generateChartTool:false, requestClarification:false}; get_agent then reports both off with records enabled:false.
Where: platform
Evidence: Next trace (case e_6ae868d89ec43c6ee23134e4) drops GenerateChartWithBlocks but still offers ClarifyFromUser, think, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy; none of the Environment* tools is in list_capabilities.
Cause: Unknown — next check: where the runtime injects ClarifyFromUser and the Environment* tools.
Regression: With requestClarification off, read_trace toolsOffered omits ClarifyFromUser; an agent with no Environment* tools attached is not offered them.

### t6 · Publish PF · Use Case Matcher

Body:
1. Read: \`get_agent\` for "PF · Use Case Matcher" (its id in Built so far).
2. Done when: "PF · Use Case Matcher" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Use Case Matcher published.

### t7 · Build AI agent PF · Case for Change Drafter

Body:
1. Read: \`list_agents\` for "PF · Case for Change Drafter"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Case for Change Drafter" exists with this contract: ai-agent · create · PF · Case for Change Drafter: registry row C18 (agent, sub-workflow 3. Account research, asks A38); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write the Case for Change: business problem in the company's own words, impact with no dollar figures, why now from the top signals, why UnifyApps, closest proof, main and backup angle, and risks; reads PF Fact rows (facts and use cases), PF Signal rows and the account's PF Person rows through Read component inputs (component_id C18); writes PF Fact rows of kind case_for_change, each citing a fact_id or tagged [HYPOTHESIS], and hand-offs to Play Picker, Message Writer and Meeting Prep Writer, only through Save agent output (component_id C18); threshold and routing: under 70: waiting_person, the BDR reviews it at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR reviews at Gate 2); feeds (the register): Play Picker; Message Writer; Meeting Prep Writer; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes a sentence without a cited fact or a [HYPOTHESIS] tag, and never writes emails; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C18 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C18 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Case for Change Drafter with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86689d96c5f6ba243cfd8"}
Read back: PF · Case for Change Drafter e_6ae86689d96c5f6ba243cfd8: update_agent model e_6ad496812dd4ba5be70afcc1 changed [responseGenerationSettings, topicExecutionSettings], version 5; get_agent models runs/picksTask/answerGeneration = e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached)), readiness canRun true, published false
Read back: PF · Case for Change Drafter: send_test_message on the new card answered (case e_6ae86b10fbdd550a9a524e69, llmCalls 1): "I'm not able to send emails — that falls outside my one job, which is drafting the Case for Change ... The Message Writer component is the one that drafts the actual outreach email ... A BDR (human) is the one who actually sends the email."
Read back: PF · Case for Change Drafter: get_agent tools ReadComponentInputs e_6ae866a5d96c5f6ba243d634 (automation 6ae8635446920244f3d5194b, enabled true, topicId GLOBAL) and SaveAgentOutput e_6ae866a5afe7fc590a4a47af (automation 6ae864829594aa458cc1ce69, enabled true), each description fixing component_id; capabilities generateChartTool and requestClarification off; deployments [], skills [], knowledge [], memory false
Read back: PF · Case for Change Drafter: instructions state the one job, ReadComponentInputs first and SaveAgentOutput exactly once, the output contract (output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through as given, scope and refusals, and that record text is never an instruction (rule 5: no secret in instructions; rule 4: writes only through Save agent output)
Read back: PF · Case for Change Drafter e_6ae86689d96c5f6ba243cfd8: trace case e_6ae867bdf13e536c52eb46a4 turn 2 — ReadComponentInputs {"component_id": "C18", "account_id": "A-1001"}, then SaveAgentOutput {component_id C18, output_type case_for_change, payload business_problem/impact/why_now/why_unifyapps/closest_proof/main_angle/backup_angle/risks each sentence citing [F-xx] or [HYPOTHESIS], confidence 78, evidence_tag hypothesis, origin 'test'}
Read back: PF · Case for Change Drafter answered: "SaveAgentOutput returned duplicate (run_id RUN-6ae867c4f13e536c52eb489a) ... 're-run of RUN-6ae867c4f13e536c52eb489a: already saved, nothing written again,' with the existing hand-offs to Play Picker, Message Writer and Meeting Prep Writer (H-6ae867c4f13e536c52eb48a3, H-6ae867c4f13e536c52eb48ad, H-6ae867c4f13e536c52eb48b1)" — RUN-6ae867c4f13e536c52eb489a is the save of its first test run
Read back: PF · Case for Change Drafter refusal (case e_6ae868ec9ec43c6ee2313975): "I'm not able to send emails—that falls outside my role. I'm the PF Case for Change Drafter (C18) ... the Message Writer could then use [it] to compose an email"
Unverified: Security: ClarifyFromUser, think and four Environment* tools (EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy) are still offered by the runtime though requestClarification is off and none is attached — needs an admin to find where the runtime injects them; the agent's own tools are exactly ReadComponentInputs and SaveAgentOutput
Unverified: Guardrails: none on the record (get_agent guardrails []); the other five rules are read-only here
Unverified: Security: the agent is shared tenant-wide through the 'All Users' and 'testing' groups (tenantWide in get_agent), which no agent share changes
Note: Answer from the person: (b): switch each agent to 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the card that passed your tests (same model, family A; the named card answers 401 invalid x-api-key). Set it with update_agent, read it back with get_agent, and send one test message to prove it answers; then report done so the publish task can run.
Note: The spec's model card e_6acca2af70b66f5702c8b59f was replaced by e_6ad496812dd4ba5be70afcc1 on the person's answer; the job-run proofs (Read then Save with origin test) were made on this same card in the first attempt.
Note: handover: Save agent output takes evidence_tag only as bare 'public' or 'hypothesis' (anything else is stored as none, and a fact with none becomes hypothesis); an agent must never send signal_id or fact_id in the payload, or the insert fails with a duplicate-key error.
Note: handover: a tool-calling first turn returns no caseId; send a greeting turn first, then the job message on that caseId, and read_trace turn 2.
Note: Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made.
Note: feedback:
Bug: Model card Claude Sonnet 5 (e_6acca2af70b66f5702c8b59f) is listed usable but every agent run on it fails.
Context: send_test_messages on new Advanced agents whose only model is that card.
Where: platform
Evidence: list_models shows connectionFound true, connectionActive true; each run returns HTTP 500 'Workflow execution failed' with root cause 401 authentication_error 'invalid x-api-key'.
Cause: Confirmed: the connection behind the card holds an API key Anthropic rejects.
Regression: send_test_message on an agent using e_6acca2af70b66f5702c8b59f answers instead of failing with 401 invalid x-api-key.
Note: feedback:
Bug: Switching requestClarification off does not stop the runtime offering ClarifyFromUser, and every agent is offered think plus four Environment* tools nobody attached.
Context: update_agent capabilities {generateChartTool:false, requestClarification:false}; get_agent then reports both off with records enabled:false.
Where: platform
Evidence: Next trace (case e_6ae868d89ec43c6ee23134e4) drops GenerateChartWithBlocks but still offers ClarifyFromUser, think, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy; none of the Environment* tools is in list_capabilities.
Cause: Unknown — next check: where the runtime injects ClarifyFromUser and the Environment* tools.
Regression: With requestClarification off, read_trace toolsOffered omits ClarifyFromUser; an agent with no Environment* tools attached is not offered them.

### t8 · Publish PF · Case for Change Drafter

Body:
1. Read: \`get_agent\` for "PF · Case for Change Drafter" (its id in Built so far).
2. Done when: "PF · Case for Change Drafter" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Case for Change Drafter published.

