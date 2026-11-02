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
## Plan

Goal: Pipeline Factory · G3 round 2 · P09

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Buying Team Mapper |  | running | 1 |
| t2 | publish | PF · Buying Team Mapper | t1 | pending | 0 |
| t3 | ai-agent | PF · Person Notes Writer |  | running | 1 |
| t4 | publish | PF · Person Notes Writer | t3 | pending | 0 |
| t5 | ai-agent | PF · Intro Finder |  | running | 1 |
| t6 | publish | PF · Intro Finder | t5 | pending | 0 |

### t1 · Build AI agent PF · Buying Team Mapper

Body:
1. Read: \`list_agents\` for "PF · Buying Team Mapper"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Buying Team Mapper" exists with this contract: ai-agent · create · PF · Buying Team Mapper: registry row C21 (agent, sub-workflow 4. Buying committee, asks A41); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: map the buying team: load the industry's default titles, assign each person a role, check the champions library, pick 3 Tier 1, 3 Tier 2, 4 Tier 3 and 2 backups, and flag the economic buyer; reads PF Person rows of the account and PF Source rows through Read component inputs (component_id C21); writes PF Person.role and tier (its registered fields; gatekeepers tier mapped) and hand-offs to Person Notes Writer, Contact Finder and Intro Finder, only through Save agent output (component_id C21); threshold and routing: under 70 on a role: waiting_person, the BDR checks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR checks at Gate 2); feeds (the register): Person Notes Writer; Contact Finder; Intro Finder; schedule in the registry: Day 1 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; a gatekeeper is mapped, never contacted; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C21 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C21 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Team Mapper with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t2 · Publish PF · Buying Team Mapper

Body:
1. Read: \`get_agent\` for "PF · Buying Team Mapper" (its id in Built so far).
2. Done when: "PF · Buying Team Mapper" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Team Mapper published.

### t3 · Build AI agent PF · Person Notes Writer

Body:
1. Read: \`list_agents\` for "PF · Person Notes Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Person Notes Writer" exists with this contract: ai-agent · create · PF · Person Notes Writer: registry row C22 (agent, sub-workflow 4. Buying committee, asks A42); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write a four-line note per person: role and time in role, past companies and public talks, what they own ([HYPOTHESIS] unless public), the link to the matched use case and nearby event fit; reads PF Person, PF Fact (use cases) and PF Source rows through Read component inputs (component_id C22); writes PF Person.note (its registered field) and a hand-off to Message Writer, only through Save agent output (component_id C22); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR) (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Message Writer; schedule in the registry: Day 1; every 90 days; on job change (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; professional information only; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C22 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C22 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Person Notes Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t4 · Publish PF · Person Notes Writer

Body:
1. Read: \`get_agent\` for "PF · Person Notes Writer" (its id in Built so far).
2. Done when: "PF · Person Notes Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Person Notes Writer published.

### t5 · Build AI agent PF · Intro Finder

Body:
1. Read: \`list_agents\` for "PF · Intro Finder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Intro Finder" exists with this contract: ai-agent · create · PF · Intro Finder: registry row C23 (agent, sub-workflow 4. Buying committee, asks A43); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: find a warm intro for Tier 1 people at best fit accounts from shared work history (opt-in LinkedIn exports, partners, SIs, investors), ranked worked together over overlapped over friend of a friend; reads PF Person rows (Tier 1) and PF Source rows of kind linkedin_export through Read component inputs (component_id C23); writes a PF Component run row of output_type intro_request (draft request, path, rank) into the patch AE's to-do list, and a 7-day hold on cold touches to that person in the payload, only through Save agent output (component_id C23); threshold and routing: under 60: not suggested (result no_action) (Save agent output applies the threshold 60 and routes below it to not suggested); feeds (the register): AE to-do list; schedule in the registry: Day 1, Tier 1 at best fit (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never contacts anyone; the AE sends the intro request; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C23 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C23 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Intro Finder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

### t6 · Publish PF · Intro Finder

Body:
1. Read: \`get_agent\` for "PF · Intro Finder" (its id in Built so far).
2. Done when: "PF · Intro Finder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Intro Finder published.

