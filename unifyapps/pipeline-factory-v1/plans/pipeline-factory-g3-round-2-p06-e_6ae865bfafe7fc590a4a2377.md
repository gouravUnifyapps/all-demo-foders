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
## Plan

Goal: Pipeline Factory · G3 round 2 · P06

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Duplicate Finder |  | running | 1 |
| t2 | publish | PF · Duplicate Finder | t1 | pending | 0 |
| t3 | ai-agent | PF · Parent Company Linker |  | running | 1 |
| t4 | publish | PF · Parent Company Linker | t3 | pending | 0 |
| t5 | ai-agent | PF · Headquarters Finder |  | running | 1 |
| t6 | publish | PF · Headquarters Finder | t5 | pending | 0 |
| t7 | ai-agent | PF · Headquarters Re-checker |  | running | 1 |
| t8 | publish | PF · Headquarters Re-checker | t7 | pending | 0 |
| t9 | ai-agent | PF · New Account Finder |  | running | 1 |
| t10 | publish | PF · New Account Finder | t9 | pending | 0 |

### t1 · Build AI agent PF · Duplicate Finder

Body:
1. Read: \`list_agents\` for "PF · Duplicate Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Duplicate Finder" exists with this contract: ai-agent · create · PF · Duplicate Finder: registry row C01 (agent, sub-workflow 1. Patch accounts, asks A16); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find duplicate patch accounts: normalise keys (domain, legal name, LinkedIn ID, HubSpot ID, email), match exactly, score near-matches 0 to 100 and log the reasoning; reads PF Account rows of the patch through Read component inputs (component_id C01); writes a PF Component run of output_type merge_proposal per pair (pair, score, keys compared, reasoning); it never merges or deletes a row (a merge is a proposal in this demo), only through Save agent output (component_id C01); threshold and routing: 95 or more: proposal marked merge; 80 to 95: waiting_person for RevOps; under 80: kept separate, no hand-off (Save agent output applies the threshold 95 and routes below it to RevOps); feeds (the register): Parent Company Linker; schedule in the registry: every 15 min (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never deletes or merges an account itself; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C01 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C01 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Duplicate Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: Asked the person: The agent is built and read back, but it cannot run: every test on model card e_6acca2af70b66f5702c8b59f "Claude Sonnet 5" (provider anthropic) fails with HTTP 500, root cause from the model provider "401 authentication_error: invalid x-api-key" (tried 2 rounds, plus one single send_test_message; same error). Question for the person: (a) have a tenant admin fix the API key on the Anthropic connection behind that card, then this task is re-sent to run the tests; or (b) move these agents to another active Sonnet 5 card, e.g. e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)", and run the tests on it? Made so far: ids {"entity":"e_6ae86680afe7fc590a4a3f53","tools":["e_6ae8669bf410ab7b2f151f8a","e_6ae8669bf410ab7b2f151f8d"]}.

### t2 · Publish PF · Duplicate Finder

Body:
1. Read: \`get_agent\` for "PF · Duplicate Finder" (its id in Built so far).
2. Done when: "PF · Duplicate Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Duplicate Finder published.

### t3 · Build AI agent PF · Parent Company Linker

Body:
1. Read: \`list_agents\` for "PF · Parent Company Linker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Parent Company Linker" exists with this contract: ai-agent · create · PF · Parent Company Linker: registry row C02 (agent, sub-workflow 1. Patch accounts, asks A17); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: link each company to its parent, subsidiaries and divisions, propose divisions that buy separately, and set the outreach lock at the top parent; reads PF Account rows and PF Source rows (press, filings) through Read component inputs (component_id C02); writes PF Account.ultimate_parent_lock (its registered field) and a PF Component run row with parent_id, children and division proposals, only through Save agent output (component_id C02); threshold and routing: under 80: waiting_person for RevOps, the lock is not written (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Headquarters Finder; Patch Suggester; schedule in the registry: on new account, HQ change or M&amp;A news (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a division proposal is never applied without RevOps; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C02 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C02 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Parent Company Linker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: Asked the person: The agent is built and read back, but it cannot run: every test on model card e_6acca2af70b66f5702c8b59f "Claude Sonnet 5" (provider anthropic) fails with HTTP 500, root cause from the model provider "401 authentication_error: invalid x-api-key" (tried 2 rounds, plus one single send_test_message; same error). Question for the person: (a) have a tenant admin fix the API key on the Anthropic connection behind that card, then this task is re-sent to run the tests; or (b) move these agents to another active Sonnet 5 card, e.g. e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)", and run the tests on it? Made so far: ids {"entity":"e_6ae86684d96c5f6ba243cf6a","tools":["e_6ae8669fafe7fc590a4a4656","e_6ae8669fd96c5f6ba243d509"]}.

### t4 · Publish PF · Parent Company Linker

Body:
1. Read: \`get_agent\` for "PF · Parent Company Linker" (its id in Built so far).
2. Done when: "PF · Parent Company Linker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Parent Company Linker published.

### t5 · Build AI agent PF · Headquarters Finder

Body:
1. Read: \`list_agents\` for "PF · Headquarters Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Headquarters Finder" exists with this contract: ai-agent · create · PF · Headquarters Finder: registry row C03 (agent, sub-workflow 1. Patch accounts, asks A18); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find the parent's headquarters city, state and country by weighing sources; reads PF Account and PF Source rows (filings, press) through Read component inputs (component_id C03); writes PF Account.hq_city (its registered field) and a PF Component run row with state, country, other candidates and evidence, only through Save agent output (component_id C03); threshold and routing: under 80: waiting_person, RevOps picks from the candidates (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Patch Suggester; schedule in the registry: on new account (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never guesses a city without a source; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C03 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C03 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: Asked the person: The agent is built and read back, but it cannot run: every test on model card e_6acca2af70b66f5702c8b59f "Claude Sonnet 5" (provider anthropic) fails with HTTP 500, root cause from the model provider "401 authentication_error: invalid x-api-key" (tried 2 rounds, plus one single send_test_message; same error). Question for the person: (a) have a tenant admin fix the API key on the Anthropic connection behind that card, then this task is re-sent to run the tests; or (b) move these agents to another active Sonnet 5 card, e.g. e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)", and run the tests on it? Made so far: ids {"entity":"e_6ae86687d96c5f6ba243cfb8","tools":["e_6ae866a4afe7fc590a4a4789","e_6ae866a4afe7fc590a4a478d"]}.

### t6 · Publish PF · Headquarters Finder

Body:
1. Read: \`get_agent\` for "PF · Headquarters Finder" (its id in Built so far).
2. Done when: "PF · Headquarters Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Finder published.

### t7 · Build AI agent PF · Headquarters Re-checker

Body:
1. Read: \`list_agents\` for "PF · Headquarters Re-checker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Headquarters Re-checker" exists with this contract: ai-agent · create · PF · Headquarters Re-checker: registry row C04 (monitor, sub-workflow 1. Patch accounts, asks A19); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: re-check headquarters of companies with move or M&amp;A news and raise an alert on any change; reads PF Account.hq_city and PF Source press rows through Read component inputs (component_id C04); writes a PF Component run row of output_type hq_change_alert (old and new HQ, source) and a hand-off to Patch Suggester, only through Save agent output (component_id C04); threshold and routing: under 80: waiting_person for RevOps; no change: result no_action (Save agent output applies the threshold 80 and routes below it to RevOps); feeds (the register): Patch Suggester; patch control tower; schedule in the registry: nightly on move or M&amp;A news; quarterly on all (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never writes hq_city itself (Headquarters Finder owns it); outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C04 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C04 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Re-checker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: Asked the person: The agent is built and read back, but it cannot run: every test on model card e_6acca2af70b66f5702c8b59f "Claude Sonnet 5" (provider anthropic) fails with HTTP 500, root cause from the model provider "401 authentication_error: invalid x-api-key" (tried 2 rounds, plus one single send_test_message; same error). Question for the person: (a) have a tenant admin fix the API key on the Anthropic connection behind that card, then this task is re-sent to run the tests; or (b) move these agents to another active Sonnet 5 card, e.g. e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)", and run the tests on it? Made so far: ids {"entity":"e_6ae8668bafe7fc590a4a3fec","tools":["e_6ae866a9afe7fc590a4a4836","e_6ae866a9afe7fc590a4a483a"]}.

### t8 · Publish PF · Headquarters Re-checker

Body:
1. Read: \`get_agent\` for "PF · Headquarters Re-checker" (its id in Built so far).
2. Done when: "PF · Headquarters Re-checker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Headquarters Re-checker published.

### t9 · Build AI agent PF · New Account Finder

Body:
1. Read: \`list_agents\` for "PF · New Account Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · New Account Finder" exists with this contract: ai-agent · create · PF · New Account Finder: registry row C05 (agent, sub-workflow 1. Patch accounts, asks A20); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find new candidate accounts from closed-won lookalikes and the seven other sources, dropping fit under 36, customers, open deals, partners, competitors and DNC; reads PF Account, PF Source (web visits, events, job changes) and PF Suppression through Read component inputs (component_id C05); writes a PF Component run row of output_type account_suggestion per candidate (name, source, why, estimated fit), only through Save agent output (component_id C05); threshold and routing: under 70: not suggested (result no_action); 70 and over: waiting_person for RevOps (Save agent output applies the threshold 70 and routes below it to RevOps); feeds (the register): Fit Scorer; schedule in the registry: weekly lookalikes; daily 7 sources (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; suggests to RevOps, never adds an account; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C05 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C05 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · New Account Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: Asked the person: The agent is built and read back, but it cannot run: every test on model card e_6acca2af70b66f5702c8b59f "Claude Sonnet 5" (provider anthropic) fails with HTTP 500, root cause from the model provider "401 authentication_error: invalid x-api-key" (tried 2 rounds, plus one single send_test_message; same error). Question for the person: (a) have a tenant admin fix the API key on the Anthropic connection behind that card, then this task is re-sent to run the tests; or (b) move these agents to another active Sonnet 5 card, e.g. e_6ad496812dd4ba5be70afcc1 "Claude Sonnet 5 (UnifyApps, Vertex, cached)", and run the tests on it? Made so far: ids {"entity":"e_6ae8668ef410ab7b2f151c47","tools":["e_6ae866add96c5f6ba243d764","e_6ae866adafe7fc590a4a48d8"]}.

### t10 · Publish PF · New Account Finder

Body:
1. Read: \`get_agent\` for "PF · New Account Finder" (its id in Built so far).
2. Done when: "PF · New Account Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · New Account Finder published.

