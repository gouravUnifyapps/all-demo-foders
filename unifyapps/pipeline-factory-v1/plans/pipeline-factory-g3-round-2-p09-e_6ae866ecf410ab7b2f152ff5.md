---
nebula: 3
specId: "e_6ae866e9d96c5f6ba243de80"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P09"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Buying Team Mapper"},{"action":"publish","kind":"ai-agent","name":"PF · Person Notes Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Intro Finder"}]
touches: [{"kind":"ai-agent","name":"PF · Buying Team Mapper"},{"kind":"ai-agent","name":"PF · Person Notes Writer"},{"kind":"ai-agent","name":"PF · Intro Finder"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "dd15189d-d02f-4b32-8226-de9bf492d092"
pageDesign: 2
createdAt: "2026-11-02T10:33:15.453Z"
runningAt: "2026-11-02T10:33:21.127Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory · G3 round 2 · P09

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Buying Team Mapper |  | done | 1 |
| t2 | publish | PF · Buying Team Mapper | t1 | done | 1 |
| t3 | ai-agent | PF · Person Notes Writer |  | done | 1 |
| t4 | publish | PF · Person Notes Writer | t3 | done | 1 |
| t5 | ai-agent | PF · Intro Finder |  | done | 1 |
| t6 | publish | PF · Intro Finder | t5 | done | 1 |

### t1 · Build AI agent PF · Buying Team Mapper

Body:
1. Read: \`list_agents\` for "PF · Buying Team Mapper"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Buying Team Mapper" exists with this contract: ai-agent · create · PF · Buying Team Mapper: registry row C21 (agent, sub-workflow 4. Buying committee, asks A41); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: map the buying team: load the industry's default titles, assign each person a role, check the champions library, pick 3 Tier 1, 3 Tier 2, 4 Tier 3 and 2 backups, and flag the economic buyer; reads PF Person rows of the account and PF Source rows through Read component inputs (component_id C21); writes PF Person.role and tier (its registered fields; gatekeepers tier mapped) and hand-offs to Person Notes Writer, Contact Finder and Intro Finder, only through Save agent output (component_id C21); threshold and routing: under 70 on a role: waiting_person, the BDR checks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR checks at Gate 2); feeds (the register): Person Notes Writer; Contact Finder; Intro Finder; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a gatekeeper is mapped, never contacted; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C21 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C21 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Team Mapper with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae867cdafe7fc590a4f8e82"}
Read back: PF · Buying Team Mapper e_6ae867cdafe7fc590a4f8e82: get_agent version 3, agentType ai-agent, published false, readiness canRun true, models runs/picksTask/answerGeneration all e_6ad496812dd4ba5be70afcc1 ('Claude Sonnet 5 (UnifyApps, Vertex, cached)', list_models connectionActive true), memory false, capabilities [], deployments [] (not deployed).
Read back: PF · Buying Team Mapper tools: ReadComponentInputs e_6ae867dbafe7fc590a4f8f9e -&gt; 6ae8635446920244f3d5194b and SaveAgentOutput e_6ae867dbafe7fc590a4f8fa1 -&gt; 6ae864829594aa458cc1ce69, both enabled true, topicId GLOBAL, descriptions fix component_id "C21".
Read back: PF · Buying Team Mapper instructions state the one job (3 Tier 1 / 3 Tier 2 / 4 Tier 3 / 2 backups, economic buyer), read ReadComponentInputs first, save exactly once with SaveAgentOutput, output contract (output_type, summary, payload, confidence 0-100, evidence, evidence_tag), origin passed through, scope and refusals, gatekeeper mapped never contacted.
Read back: PF · Buying Team Mapper job test (trace caseId e_6ae86983fbdd550a9a51d224): ReadComponentInputs {component_id C21, account_id A-1001} then SaveAgentOutput {component_id C21, account_id A-1001, person_id P-1001, output_type buying_team_map, payload role economic_buyer, confidence 55, origin "test"}; Save agent output answered result "duplicate", reason "re-run of RUN-6ae8684f9594aa458cd579e6: already waiting_person, nothing written again". Agent answered: "SaveAgentOutput returned duplicate (run_id RUN-6ae8684f9594aa458cd579e6)". So the first save of this test is run RUN-6ae8684f9594aa458cd579e6 at waiting_person (confidence 55 under 70, BDR checks at Gate 2).
Read back: PF · Buying Team Mapper refusal test (caseId e_6ae867e69ec43c6ee230ca31, toolCalls []): "I'm not able to send emails — that falls outside my one job here, which is mapping an account's buying team ... Sending a message to Arjun Mehta would be handled by the Message Writer (drafts it) and a BDR (sends it) — not by me."
Unverified: PF · Buying Team Mapper: the first save's trace (run RUN-6ae8684f9594aa458cd579e6) is not readable because the tool-calling turn returned no caseId; its waiting_person result is known only from the duplicate reason of the re-run. Check: read PF Component run row RUN-6ae8684f9594aa458cd579e6 (status waiting_person, origin test).
Unverified: PF · Buying Team Mapper: the trace shows the model offered GenerateChartWithBlocks, think, ClarifyFromUser and four Environment* tools that get_agent and list_capabilities report as not attached or off. Check: list_capabilities/describe_entity on the tenant's default standard actions.
Unverified: Security: guardrails are absent on PF · Buying Team Mapper (get_agent guardrails []) — needs an admin to decide whether the agent needs content filter or PII masking in the agent's settings; the tools write only through Save agent output, which limits writes to C21's registered fields.
Note: Model card per Answer from the person: e_6ad496812dd4ba5be70afcc1 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' instead of e_6acca2af70b66f5702c8b59f; list_models shows it connectionActive true and the test runs answered on it.
Note: Round 1 job test was rejected by Save agent output: "schema check failed: person_id missing" (run RUN-6ae8683e9594aa458cd57867). Its decide code maps C21 to target person, fields role and tier, codes role in economic_buyer/champion/technical_evaluator/business_owner/gatekeeper and tier in t1/t2/t3/backup/mapped. Instructions and the SaveAgentOutput description were changed so each save names one person_id (the message's, else the economic buyer) with that person's role and tier at the payload's top level; the whole map stays in payload.people.
Note: plan_change: absorbed — Save agent output writes role and tier for ONE PF Person per save (the idempotency key includes person_id), so a C21 run writes the named person's (default the economic buyer's) role and tier, and the rest of the team map lives in the run's payload; mapping every person's fields needs one run per person_id.
Note: Test rows carry origin test (runs RUN-6ae8683e9594aa458cd57867 rejected, RUN-6ae8684f9594aa458cd579e6 waiting_person) and are left for Pipeline Factory · Reset demo; no delete made. Not published.
Note: feedback:
Bug: send_test_messages timed out at the MCP client's 60 s limit on a two-question list whose first question calls tools, so no rows came back while the runs (which write) still ran on the server.
Context: send_test_messages on PF · Person Notes Writer and PF · Intro Finder, two messages each, in parallel with a third call.
Where: mcp-tool
Evidence: \`MCP server "plugin:ua:agent-builder" tool "send_test_messages" timed out after 60s\`; the tool's description says to expect several minutes.
Cause: Suspected: the tool runs longer than the client-side MCP timeout.
Regression: send_test_messages with two questions, one tool-calling, returns rows without hitting the client timeout.
Note: feedback:
Bug: A tool-calling test turn returns no caseId, so the only way to read the trace or run id of an agent that writes is runAgainToFindAnswer, which runs the write a second time.
Context: Testing three PF agents that save through Pipeline Factory · Save agent output.
Where: mcp-tool
Evidence: rows came back with only "The agent called a tool, and the platform did not report which case it created"; send_test_message also said "Read the trace for the caseId above." with no caseId in the reply.
Cause: Suspected: the platform test invoke does not report the case for a paused tool turn; the warning references a caseId the reply does not carry.
Regression: send_test_message on a tool-calling agent returns its caseId on the first run.
Note: feedback:
Bug: The trace of a new Advanced agent shows the model offered seven tools nobody attached (GenerateChartWithBlocks, think, ClarifyFromUser, EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment, RequestEnvironmentDeploy), while get_agent reports capabilities [] and list_capabilities reports requestClarification and generateChartTool on:false.
Context: PF · Buying Team Mapper e_6ae867cdafe7fc590a4f8e82 created with create_agent and two add_tools.
Where: unknown
Evidence: read_trace caseId e_6ae86983fbdd550a9a51d224 toolsOffered lists them; list_capabilities agentId shows generateChartTool and requestClarification on false.
Cause: Unknown — next check: whether the runtime adds tenant default tools that no capability record reports.
Regression: get_agent or list_capabilities names every tool the trace shows offered to the model.

### t2 · Publish PF · Buying Team Mapper

Body:
1. Read: \`get_agent\` for "PF · Buying Team Mapper" (its id in Built so far).
2. Done when: "PF · Buying Team Mapper" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Team Mapper published.
Result IDs: {"entity":"e_6ae867cdafe7fc590a4f8e82"}
Read back: PF · Buying Team Mapper e_6ae867cdafe7fc590a4f8e82: publish_agent(confirmed true) answered ok true, publishedVersion 3, live true, automationSaid {response: "success"}.
Read back: PF · Buying Team Mapper e_6ae867cdafe7fc590a4f8e82: live re-read (list_agents ids) shows published true, needsPublish false, version 8.
Unverified: PF · Buying Team Mapper: no live invoke by Pipeline Factory · Run component was made after the publish. Check: run Run component for C21 and read its result.
Note: Publish per Answer from the person: "yes, publish PF · Buying Team Mapper. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval).
Note: The stored version rose from 3 to 8 during publish while needsPublish reads false; the published content is draft version 3. Not deployed to any app or channel.

### t3 · Build AI agent PF · Person Notes Writer

Body:
1. Read: \`list_agents\` for "PF · Person Notes Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Person Notes Writer" exists with this contract: ai-agent · create · PF · Person Notes Writer: registry row C22 (agent, sub-workflow 4. Buying committee, asks A42); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write a four-line note per person: role and time in role, past companies and public talks, what they own ([HYPOTHESIS] unless public), the link to the matched use case and nearby event fit; reads PF Person, PF Fact (use cases) and PF Source rows through Read component inputs (component_id C22); writes PF Person.note (its registered field) and a hand-off to Message Writer, only through Save agent output (component_id C22); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR) (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Message Writer; schedule in the registry: Day 1; every 90 days; on job change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; professional information only; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C22 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C22 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Person Notes Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae867d2f410ab7b2f155861"}
Read back: PF · Person Notes Writer e_6ae867d2f410ab7b2f155861: get_agent version 3, agentType ai-agent, published false, readiness canRun true, models runs/picksTask/answerGeneration all e_6ad496812dd4ba5be70afcc1 ('Claude Sonnet 5 (UnifyApps, Vertex, cached)'), memory false, capabilities [], deployments [] (not deployed).
Read back: PF · Person Notes Writer tools: ReadComponentInputs e_6ae867dff410ab7b2f1559cb -&gt; 6ae8635446920244f3d5194b and SaveAgentOutput e_6ae867dff410ab7b2f1559ce -&gt; 6ae864829594aa458cc1ce69, both enabled true, topicId GLOBAL, descriptions fix component_id "C22".
Read back: PF · Person Notes Writer instructions state the one job (four-line note: role and time in role; past companies and public talks; what they own, [HYPOTHESIS] unless public; matched use case link and nearby event fit), professional information only, read first, save exactly once, output contract, origin passed through, scope and refusals.
Read back: PF · Person Notes Writer job test (trace caseId e_6ae86ae32099302ffb2ed6f7): ReadComponentInputs {component_id C22, account_id A-1001} then SaveAgentOutput {component_id C22, account_id A-1001, person_id P-1001, output_type person_note, origin "test", confidence 88}; Save agent output answered result "duplicate", reason "re-run of RUN-6ae8690afbdd550a9a51b99e: already saved, nothing written again", handoff_ids H-6ae86940fbdd550a9a51bfcf. Agent answered: "Result: duplicate — run_id RUN-6ae8690afbdd550a9a51b99e ... A hand-off (H-6ae86940fbdd550a9a51bfcf) is associated with the original save for the Message Writer". So the first save is run RUN-6ae8690afbdd550a9a51b99e, saved.
Read back: PF · Person Notes Writer refusal test (caseId e_6ae868cdf13e536c52ec2cd3, no tool call): "This is outside my one job here. I'm PF · Person Notes Writer (C22) — I only write four-line professional notes ... I don't send emails or contact anyone directly."
Unverified: PF · Person Notes Writer: the first save's trace (run RUN-6ae8690afbdd550a9a51b99e) is not readable because the tool-calling turn returned no caseId; its saved result is known from the duplicate reason. Check: read PF Component run row RUN-6ae8690afbdd550a9a51b99e and PF Person P-1001.note.
Unverified: Security: guardrails are absent on PF · Person Notes Writer (get_agent guardrails []) — needs an admin to decide on PII masking in the agent's settings, since the agent writes notes about people; the instructions limit it to professional information.
Note: Model card per Answer from the person: e_6ad496812dd4ba5be70afcc1 instead of e_6acca2af70b66f5702c8b59f.
Note: Save agent output maps C22 to target person, field note, and refuses a save with no person_id; instructions and the SaveAgentOutput description name one person_id per save (the message's, else the first Tier 1 / economic buyer) with that person's note at the payload's top level, other notes in payload.notes.
Note: Round 1 answer misquoted the run id ("RUN-6ae8690afbdd550a9a51be9e (reported as RUN-6ae8690afbdd550a9a51b99e)"); instructions now say to copy run_id character for character, and round 2 quoted RUN-6ae8690afbdd550a9a51b99e exactly.
Note: plan_change: absorbed — Save agent output writes PF Person.note for ONE person per save, so a C22 run writes the named person's (default the economic buyer's) note and the others' notes ride in the payload; a note on every person needs one run per person_id.
Note: A send_test_messages call for this agent timed out client-side (60 s) and its job run likely wrote too; together with the runAgainToFindAnswer re-runs, every later save answered duplicate. Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made. Not published.

### t4 · Publish PF · Person Notes Writer

Body:
1. Read: \`get_agent\` for "PF · Person Notes Writer" (its id in Built so far).
2. Done when: "PF · Person Notes Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Person Notes Writer published.
Result IDs: {"entity":"e_6ae867d2f410ab7b2f155861"}
Read back: PF · Person Notes Writer e_6ae867d2f410ab7b2f155861: publish_agent(confirmed true) answered ok true, publishedVersion 3, live true, automationSaid {response: "success"}.
Read back: PF · Person Notes Writer e_6ae867d2f410ab7b2f155861: live re-read (list_agents ids) shows published true, needsPublish false, version 8.
Unverified: PF · Person Notes Writer: no live invoke by Pipeline Factory · Run component was made after the publish. Check: run Run component for C22 and read its result.
Note: Publish per Answer from the person: "yes, publish PF · Person Notes Writer. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval).
Note: The stored version rose from 3 to 8 during publish while needsPublish reads false. Not deployed to any app or channel.

### t5 · Build AI agent PF · Intro Finder

Body:
1. Read: \`list_agents\` for "PF · Intro Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Intro Finder" exists with this contract: ai-agent · create · PF · Intro Finder: registry row C23 (agent, sub-workflow 4. Buying committee, asks A43); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find a warm intro for Tier 1 people at best fit accounts from shared work history (opt-in LinkedIn exports, partners, SIs, investors), ranked worked together over overlapped over friend of a friend; reads PF Person rows (Tier 1) and PF Source rows of kind linkedin_export through Read component inputs (component_id C23); writes a PF Component run row of output_type intro_request (draft request, path, rank) into the patch AE's to-do list, and a 7-day hold on cold touches to that person in the payload, only through Save agent output (component_id C23); threshold and routing: under 60: not suggested (result no_action) (Save agent output applies the threshold 60 and routes below it to not suggested); feeds (the register): AE to-do list; schedule in the registry: Day 1, Tier 1 at best fit (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never contacts anyone; the AE sends the intro request; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C23 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C23 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Intro Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae867d4f410ab7b2f155959"}
Read back: PF · Intro Finder e_6ae867d4f410ab7b2f155959: get_agent version 2, agentType ai-agent, published false, readiness canRun true, models runs/picksTask/answerGeneration all e_6ad496812dd4ba5be70afcc1 ('Claude Sonnet 5 (UnifyApps, Vertex, cached)'), memory false, capabilities [], deployments [] (not deployed).
Read back: PF · Intro Finder tools: ReadComponentInputs e_6ae867e3d96c5f6ba2440ee4 -&gt; 6ae8635446920244f3d5194b and SaveAgentOutput e_6ae867e3f410ab7b2f155a3f -&gt; 6ae864829594aa458cc1ce69, both enabled true, topicId GLOBAL, descriptions fix component_id "C23".
Read back: PF · Intro Finder instructions state the one job (Tier 1 warm intro paths from linkedin_export, partners, SIs, investors; worked together over overlapped over friend of a friend; draft intro request for the patch AE; 7-day cold-touch hold in the payload), never contacts anyone, under 60 or no path saves once with suggested:false and a summary starting "No action:", read first, save exactly once, output contract, origin passed through.
Read back: PF · Intro Finder job test (trace caseId e_6ae86b189ec43c6ee24512e9): ReadComponentInputs {component_id C23, account_id A-1001} first, then SaveAgentOutput {component_id C23, account_id A-1001, output_type intro_request, summary "No action: no warm-intro path could be found for any Tier 1 person ...", payload suggested false, confidence 0, evidence_tag hypothesis, origin "test"}. Agent answered: "Result: duplicate — run_id RUN-6ae868f346920244f3d68adf. Reason given: this is a re-run of an existing run that is already waiting_person, so nothing new was written." So the first save is run RUN-6ae868f346920244f3d68adf at waiting_person (confidence 0 under 60).
Read back: PF · Intro Finder refusal test (caseId e_6ae868d3f6f76639f838ed23, no tool call): "I'm not able to send emails — that falls outside my one job here. I'm PF · Intro Finder (C23) ... Intro requests ... are drafted by me, but sent by the patch AE, not by me."
Unverified: PF · Intro Finder: the first save's trace (run RUN-6ae868f346920244f3d68adf) is not readable because the tool-calling turn returned no caseId; its waiting_person result is known from the duplicate reason. Check: read PF Component run row RUN-6ae868f346920244f3d68adf.
Unverified: PF · Intro Finder: the A-1001 records hold no linkedin_export source rows, so only the no-path branch (suggested:false) was exercised; a ranked path with a drafted request is untested. Check: run it on an account whose PF Source rows include kind linkedin_export.
Unverified: Security: guardrails are absent on PF · Intro Finder (get_agent guardrails []) — needs an admin to decide on content filter or PII masking in the agent's settings.
Note: Model card per Answer from the person: e_6ad496812dd4ba5be70afcc1 instead of e_6acca2af70b66f5702c8b59f.
Note: Save agent output has no MAP entry for C23, so it writes only the PF Component run row (no field) and needs no person_id; per Answer from the person there is no no_action result: under 60 it answers waiting_person, and the agent saves suggested:false with a 'No action:' summary.
Note: In the round 2 test the agent called ReadComponentInputs four times (with person_id, patch_id and draft_id "none") looking for linkedin_export rows before saving once; reads only, no extra write.
Note: A send_test_messages call for this agent timed out client-side (60 s) and its job run likely wrote the first row. Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made. Not published.

### t6 · Publish PF · Intro Finder

Body:
1. Read: \`get_agent\` for "PF · Intro Finder" (its id in Built so far).
2. Done when: "PF · Intro Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Intro Finder published.
Result IDs: {"entity":"e_6ae867d4f410ab7b2f155959"}
Read back: PF · Intro Finder e_6ae867d4f410ab7b2f155959: publish_agent(confirmed true) answered ok true, publishedVersion 2, live true, automationSaid {response: "success"}.
Read back: PF · Intro Finder e_6ae867d4f410ab7b2f155959: live re-read (list_agents ids) shows published true, needsPublish false, version 7.
Unverified: PF · Intro Finder: no live invoke by Pipeline Factory · Run component was made after the publish. Check: run Run component for C23 and read its result.
Note: Publish per Answer from the person: "yes, publish PF · Intro Finder. The spec the person accepted names it under Ready when, so it is already approved; do not ask again." (the plan's approval).
Note: The stored version rose from 2 to 7 during publish while needsPublish reads false. Not deployed to any app or channel.

