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
| t1 | ai-agent | PF · Buying Signal Spotter |  | running | 1 |
| t2 | publish | PF · Buying Signal Spotter | t1 | pending | 0 |
| t3 | ai-agent | PF · Company Facts Collector |  | running | 1 |
| t4 | publish | PF · Company Facts Collector | t3 | pending | 0 |
| t5 | ai-agent | PF · Use Case Matcher |  | running | 1 |
| t6 | publish | PF · Use Case Matcher | t5 | pending | 0 |
| t7 | ai-agent | PF · Case for Change Drafter |  | running | 1 |
| t8 | publish | PF · Case for Change Drafter | t7 | pending | 0 |

### t1 · Build AI agent PF · Buying Signal Spotter

Body:
1. Read: \`list_agents\` for "PF · Buying Signal Spotter"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Buying Signal Spotter" exists with this contract: ai-agent · create · PF · Buying Signal Spotter: registry row C11 (agent, sub-workflow 2. Account selection, asks A28); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: watch the signal sources, record each signal (company, type, date, source link, strength), verify company match and date, score confidence, and send strong signals (champion job move, checked visit, new leader, renewal, event, several people engaging) to the Play Picker; reads PF Source rows (web_visit, press, job_post, events), PF Signal and hand-offs from Renewal Date Finder through Read component inputs (component_id C11); writes PF Signal rows (its registered records, weights from the starting signal weights, the checked-visit rule) and hand-offs to Account Ranking, and to Play Picker for a strong signal, only through Save agent output (component_id C11); threshold and routing: under 70: logged, not scored (counted false); signals fade over 30 days (Save agent output applies the threshold 70 and routes below it to logged, not scored); feeds (the register): Account Ranking; Play Picker (fast lane); schedule in the registry: continuous (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never counts a visit that fails the checked-visit rule; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C11 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C11 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Buying Signal Spotter with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.

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

### t8 · Publish PF · Case for Change Drafter

Body:
1. Read: \`get_agent\` for "PF · Case for Change Drafter" (its id in Built so far).
2. Done when: "PF · Case for Change Drafter" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Case for Change Drafter published.

