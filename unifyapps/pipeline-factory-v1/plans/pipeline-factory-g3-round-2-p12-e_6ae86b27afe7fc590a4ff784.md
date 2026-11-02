---
nebula: 3
specId: "e_6ae86b24f410ab7b2f15e3e4"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P12"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Reply Sorter"},{"action":"publish","kind":"ai-agent","name":"PF · Reply Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Meeting Prep Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Meeting Labeler"},{"action":"publish","kind":"ai-agent","name":"PF · Deal Qualifier"}]
touches: [{"kind":"ai-agent","name":"PF · Reply Sorter"},{"kind":"ai-agent","name":"PF · Reply Writer"},{"kind":"ai-agent","name":"PF · Meeting Prep Writer"},{"kind":"ai-agent","name":"PF · Meeting Labeler"},{"kind":"ai-agent","name":"PF · Deal Qualifier"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "ea2049da-a575-4578-a913-6addd610aeda"
pageDesign: 2
createdAt: "2026-11-02T10:51:18.191Z"
runningAt: "2026-11-02T10:51:22.880Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P12

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Reply Sorter |  | running | 1 |
| t2 | publish | PF · Reply Sorter | t1 | pending | 0 |
| t3 | ai-agent | PF · Reply Writer |  | running | 1 |
| t4 | publish | PF · Reply Writer | t3 | pending | 0 |
| t5 | ai-agent | PF · Meeting Prep Writer |  | running | 1 |
| t6 | publish | PF · Meeting Prep Writer | t5 | pending | 0 |
| t7 | ai-agent | PF · Meeting Labeler |  | running | 1 |
| t8 | publish | PF · Meeting Labeler | t7 | pending | 0 |
| t9 | ai-agent | PF · Deal Qualifier |  | running | 1 |
| t10 | publish | PF · Deal Qualifier | t9 | pending | 0 |

### t1 · Build AI agent PF · Reply Sorter

Body:
1. Read: \`list_agents\` for "PF · Reply Sorter"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Do-Not-Contact List \`6ae864672099302ffb2d3157\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Reply Sorter" exists with this contract: ai-agent · create · PF · Reply Sorter: registry row C41 (checker, sub-workflow 7. Engage, Connect and Commit, asks A67); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: sort every reply into one of nine types (positive, referral, not now with date, objection, wrong person, out of office, unsubscribe, bounce, auto-reply), stop all channels for that person, and handle the mechanical types; reads PF Source rows of kind reply (Apollo and Sprouts, mocked) through Read component inputs (component_id C41); writes a PF Component run row of output_type reply_type (type, date if any, channels stopped) and hand-offs to Reply Writer, Follow-up Planner and Do-Not-Contact List; out of office moves the next touch to the return date in the payload; unsubscribe calls Do-Not-Contact List within the run, only through Save agent output (component_id C41); threshold and routing: under 90 on unsubscribe: treated as unsubscribe; under 80 on anything else: waiting_person, a person sorts it (Save agent output applies the threshold 80 and routes below it to a person sorts it (unsubscribe under 90 treated as unsubscribe)); feeds (the register): Reply Writer; Follow-up Planner; Do-Not-Contact List; schedule in the registry: on every reply (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output), Do-Not-Contact List (Pipeline Factory · Do-Not-Contact List); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on the other model family from Reply Writer; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C41 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C41 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Reply Sorter with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t2 · Publish PF · Reply Sorter

Body:
1. Read: \`get_agent\` for "PF · Reply Sorter" (its id in Built so far).
2. Done when: "PF · Reply Sorter" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Reply Sorter published.

### t3 · Build AI agent PF · Reply Writer

Body:
1. Read: \`list_agents\` for "PF · Reply Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Reply Writer" exists with this contract: ai-agent · create · PF · Reply Writer: registry row C42 (agent, sub-workflow 7. Engage, Connect and Commit, asks A68); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: draft the answer to a reply from the thread, the account view, the objection list and the AE's booking link; reads PF Source reply rows, PF Account, PF Fact and hand-offs from Reply Sorter through Read component inputs (component_id C42); writes a PF Component run row of output_type reply_draft into the BDR's to-do list (and the AE's for a positive reply at a best fit account), with the 90-minute reminder and 2-business-hour Geo alert as due times, only through Save agent output (component_id C42); threshold and routing: under 70: marked for full rewrite (waiting_person) (Save agent output applies the threshold 70 and routes below it to marked for full rewrite); feeds (the register): BDR to-do list; schedule in the registry: on every reply (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never sends; the person sends from the original thread; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C42 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C42 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Reply Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t4 · Publish PF · Reply Writer

Body:
1. Read: \`get_agent\` for "PF · Reply Writer" (its id in Built so far).
2. Done when: "PF · Reply Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Reply Writer published.

### t5 · Build AI agent PF · Meeting Prep Writer

Body:
1. Read: \`list_agents\` for "PF · Meeting Prep Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Meeting Prep Writer" exists with this contract: ai-agent · create · PF · Meeting Prep Writer: registry row C44 (agent, sub-workflow 7. Engage, Connect and Commit, asks A70); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: build the meeting prep pack for the AE and SC: account view, buying team, thread, Case for Change, likely objections, Art of the Possible page, and questions to confirm the economic buyer and timeline; reads PF Account, PF Person, PF Fact, PF Source and hand-offs from Meeting Handoff and Deadlines and Case for Change Drafter through Read component inputs (component_id C44); writes a PF Component run row of output_type prep_pack and a hand-off to the AE AI Twin (mocked as the run), only through Save agent output (component_id C44); threshold and routing: no threshold (0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): AE AI Twin; schedule in the registry: on booking (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never invents a promise the AE made; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C44 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C44 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Meeting Prep Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t6 · Publish PF · Meeting Prep Writer

Body:
1. Read: \`get_agent\` for "PF · Meeting Prep Writer" (its id in Built so far).
2. Done when: "PF · Meeting Prep Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Meeting Prep Writer published.

### t7 · Build AI agent PF · Meeting Labeler

Body:
1. Read: \`list_agents\` for "PF · Meeting Labeler"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Meeting Labeler" exists with this contract: ai-agent · create · PF · Meeting Labeler: registry row C45 (checker, sub-workflow 7. Engage, Connect and Commit, asks A71); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: label each meeting intro, New Buyer Meeting or doesn't count, quoting evidence from the transcript, attendees and the economic-buyer flag; reads PF Source rows of kind meeting_transcript and calendar_event, PF Person through Read component inputs (component_id C45); writes PF Account.meeting_label (its registered field) with the quoted evidence in its PF Component run row, and hand-offs to Deal Qualifier and AE confirm, only through Save agent output (component_id C45); threshold and routing: doesn't count if under 20 minutes, no Tier 1 or 2 attendee, a reschedule, or a second intro within 90 days; unrecorded meetings labelled from attendees and AE notes and marked unrecorded; under 80: waiting_person, the Geo leader checks (Save agent output applies the threshold 80 and routes below it to Geo leader checks); feeds (the register): Deal Qualifier; AE confirm; schedule in the registry: after each meeting (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; runs on the other model family from the drafters; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C45 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C45 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Meeting Labeler with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t8 · Publish PF · Meeting Labeler

Body:
1. Read: \`get_agent\` for "PF · Meeting Labeler" (its id in Built so far).
2. Done when: "PF · Meeting Labeler" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Meeting Labeler published.

### t9 · Build AI agent PF · Deal Qualifier

Body:
1. Read: \`list_agents\` for "PF · Deal Qualifier"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Deal Qualifier" exists with this contract: ai-agent · create · PF · Deal Qualifier: registry row C46 (checker, sub-workflow 7. Engage, Connect and Commit, asks A72); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: check the six qualification requirements after each New Buyer Meeting (fit 36+, a VEP-CFC pain, engaged champion, New Buyer Meeting held, timeline 12 months or less, a scheduled mutual next step), each met, partly or missing with transcript quotes; reads PF Account, PF Fact, PF Person and PF Source meeting_transcript rows through Read component inputs (component_id C46); writes PF Account.qualified_status (its registered field), the six results, the gaps with the question that closes each and the recap draft in its PF Component run row, and a hand-off to AE confirm, only through Save agent output (component_id C46); threshold and routing: recommends qualified only when all six are met; under 80: recommended not qualified, with gaps (Save agent output applies the threshold 80 and routes below it to recommended not qualified, with gaps); feeds (the register): AE confirm; graph; schedule in the registry: after each New Buyer Meeting (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; never moves a deal stage (the AE confirms). Runs on the other model family from the drafters; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C46 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C46 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Deal Qualifier with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t10 · Publish PF · Deal Qualifier

Body:
1. Read: \`get_agent\` for "PF · Deal Qualifier" (its id in Built so far).
2. Done when: "PF · Deal Qualifier" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Deal Qualifier published.

