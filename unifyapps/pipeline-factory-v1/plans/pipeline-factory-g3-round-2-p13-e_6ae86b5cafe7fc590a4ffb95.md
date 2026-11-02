---
nebula: 3
specId: "e_6ae86b58afe7fc590a4ffb5d"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P13"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Winning Message Finder"},{"action":"publish","kind":"ai-agent","name":"PF · Scoring Tuner"},{"action":"publish","kind":"ai-agent","name":"PF · Objection Collector"},{"action":"publish","kind":"ai-agent","name":"PF · A/B Tester"},{"action":"publish","kind":"ai-agent","name":"PF · Quality Grader"}]
touches: [{"kind":"ai-agent","name":"PF · Winning Message Finder"},{"kind":"ai-agent","name":"PF · Scoring Tuner"},{"kind":"ai-agent","name":"PF · Objection Collector"},{"kind":"ai-agent","name":"PF · A/B Tester"},{"kind":"ai-agent","name":"PF · Quality Grader"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "076ad85e-ae67-45e9-a58e-42e8ad3531c8"
pageDesign: 2
createdAt: "2026-11-02T10:52:11.161Z"
runningAt: "2026-11-02T10:52:17.187Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P13

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Winning Message Finder |  | running | 1 |
| t2 | publish | PF · Winning Message Finder | t1 | pending | 0 |
| t3 | ai-agent | PF · Scoring Tuner |  | running | 1 |
| t4 | publish | PF · Scoring Tuner | t3 | pending | 0 |
| t5 | ai-agent | PF · Objection Collector |  | running | 1 |
| t6 | publish | PF · Objection Collector | t5 | pending | 0 |
| t7 | ai-agent | PF · A/B Tester |  | running | 1 |
| t8 | publish | PF · A/B Tester | t7 | pending | 0 |
| t9 | ai-agent | PF · Quality Grader |  | running | 1 |
| t10 | publish | PF · Quality Grader | t9 | pending | 0 |

### t1 · Build AI agent PF · Winning Message Finder

Body:
1. Read: \`list_agents\` for "PF · Winning Message Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Winning Message Finder" exists with this contract: ai-agent · create · PF · Winning Message Finder: registry row C48 (agent, sub-workflow 8. Learning and governance, asks A77); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find winning messages: promote messages with 3 or more positive replies into the Message Writer's examples for that role and industry; reads PF Draft rows, PF Source reply rows and PF Component run rows of Reply Sorter through Read component inputs (component_id C48); writes a PF Component run row of output_type example_proposal (status proposal) and a hand-off to Message Writer after the Quality Grader and the Friday review, only through Save agent output (component_id C48); threshold and routing: under 3 positives: not promoted (no_action) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Message Writer (after Quality Grader and Friday review); schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; nothing applies without the Quality Grader and the Friday review; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C48 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C48 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Winning Message Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t2 · Publish PF · Winning Message Finder

Body:
1. Read: \`get_agent\` for "PF · Winning Message Finder" (its id in Built so far).
2. Done when: "PF · Winning Message Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Winning Message Finder published.

### t3 · Build AI agent PF · Scoring Tuner

Body:
1. Read: \`list_agents\` for "PF · Scoring Tuner"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Scoring Tuner" exists with this contract: ai-agent · create · PF · Scoring Tuner: registry row C49 (agent, sub-workflow 8. Learning and governance, asks A78); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: re-fit fit and signal weights to meetings and qualified opportunities, learning from Gate 1 rejections, AE-rejected meetings, disqualifications and win/loss reasons, across all patches, reported per patch; reads PF Account, PF Signal, PF Patch and PF Component run rows through Read component inputs (component_id C49); writes a PF Component run row of output_type weight_proposal (status proposal, old and new weight per signal, per patch) and hand-offs to Fit Scorer and Account Ranking after the Quality Grader and the Friday review, only through Save agent output (component_id C49); threshold and routing: proposals only; only a change within plus or minus 20% may later apply on its own after 8 weeks without a drop (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Fit Scorer; Account Ranking (after Quality Grader and Friday review); schedule in the registry: monthly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never changes a weight itself; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C49 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C49 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Scoring Tuner with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t4 · Publish PF · Scoring Tuner

Body:
1. Read: \`get_agent\` for "PF · Scoring Tuner" (its id in Built so far).
2. Done when: "PF · Scoring Tuner" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Scoring Tuner published.

### t5 · Build AI agent PF · Objection Collector

Body:
1. Read: \`list_agents\` for "PF · Objection Collector"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Objection Collector" exists with this contract: ai-agent · create · PF · Objection Collector: registry row C50 (agent, sub-workflow 8. Learning and governance, asks A79); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: update the objection list and buyer language from call transcripts; reads PF Source rows of kind call_transcript and meeting_transcript through Read component inputs (component_id C50); writes a PF Component run row of output_type objection_list (status proposal) and a hand-off to Follow-up Planner after the Quality Grader and the Friday review, only through Save agent output (component_id C50); threshold and routing: under 70: waiting_person, sales reviews (Save agent output applies the threshold 70 and routes below it to sales reviews); feeds (the register): Follow-up Planner (after Quality Grader and Friday review); schedule in the registry: weekly (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C50 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C50 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Objection Collector with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t6 · Publish PF · Objection Collector

Body:
1. Read: \`get_agent\` for "PF · Objection Collector" (its id in Built so far).
2. Done when: "PF · Objection Collector" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Objection Collector published.

### t7 · Build AI agent PF · A/B Tester

Body:
1. Read: \`list_agents\` for "PF · A/B Tester"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · A/B Tester" exists with this contract: ai-agent · create · PF · A/B Tester: registry row C51 (agent, sub-workflow 8. Learning and governance, asks A80); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: design A/B tests: small changes (subject, opener, asset) as continuous tests on positive replies with at least 20% traffic per version and a 4-week limit; bold changes as fixed-size tests on people; reads PF Draft rows and PF Component run rows through Read component inputs (component_id C51); writes a PF Component run row of output_type test_variant (status proposal, the variants, traffic split, sample size) and a hand-off to Message Writer after the Quality Grader and the Friday review, only through Save agent output (component_id C51); threshold and routing: never tests a one-point lift (no_action) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Message Writer (after Quality Grader and Friday review); schedule in the registry: continuous; fixed-size tests (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; proposes only; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C51 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C51 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · A/B Tester with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t8 · Publish PF · A/B Tester

Body:
1. Read: \`get_agent\` for "PF · A/B Tester" (its id in Built so far).
2. Done when: "PF · A/B Tester" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · A/B Tester published.

### t9 · Build AI agent PF · Quality Grader

Body:
1. Read: \`list_agents\` for "PF · Quality Grader"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read factory records \`6ae843e69ec43c6ee2dec988\`; Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Quality Grader" exists with this contract: ai-agent · create · PF · Quality Grader: registry row C52 (checker, sub-workflow 8. Learning and governance, asks A81); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: hold every agent's rubric and test set, grade every proposal and every prompt, model or weight change, and block a release on any drop; enforce checker-on-other-model; compute each gate's rung weekly per pod and AE; draft a policy when the same exception is resolved the same way 3 times; reads PF Component, PF Component run and PF Hand-off rows through Read component inputs (component_id C52); writes a PF Component run row of output_type release_check (pass or block with the drop), rung or policy_draft, and a hand-off to the Friday review, only through Save agent output (component_id C52); threshold and routing: blocks on any drop (no threshold) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Friday review; schedule in the registry: on every prompt, model or weight change; weekly rungs (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Read factory records (Pipeline Factory · Read factory records, the round-1 read tool, unchanged); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on family B, a different family from every drafter it grades; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C52 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C52 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Quality Grader with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t10 · Publish PF · Quality Grader

Body:
1. Read: \`get_agent\` for "PF · Quality Grader" (its id in Built so far).
2. Done when: "PF · Quality Grader" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Quality Grader published.

