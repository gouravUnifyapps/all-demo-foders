---
nebula: 3
specId: "e_6ae867abf410ab7b2f155470"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P10"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Play Picker"},{"action":"publish","kind":"ai-agent","name":"PF · Page Builder"},{"action":"publish","kind":"ai-agent","name":"PF · Content Picker"},{"action":"publish","kind":"ai-agent","name":"PF · Message Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Fact Checker"}]
touches: [{"kind":"ai-agent","name":"PF · Play Picker"},{"kind":"ai-agent","name":"PF · Page Builder"},{"kind":"ai-agent","name":"PF · Content Picker"},{"kind":"ai-agent","name":"PF · Message Writer"},{"kind":"ai-agent","name":"PF · Fact Checker"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "0a1abc4d-b98f-49ab-94ef-5459a2da51b6"
pageDesign: 2
createdAt: "2026-11-02T10:36:33.701Z"
runningAt: "2026-11-02T10:36:41.447Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P10

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Play Picker |  | done | 1 |
| t2 | publish | PF · Play Picker | t1 | running | 1 |
| t3 | ai-agent | PF · Page Builder |  | done | 1 |
| t4 | publish | PF · Page Builder | t3 | running | 1 |
| t5 | ai-agent | PF · Content Picker |  | done | 1 |
| t6 | publish | PF · Content Picker | t5 | running | 1 |
| t7 | ai-agent | PF · Message Writer |  | running | 2 |
| t8 | publish | PF · Message Writer | t7 | pending | 0 |
| t9 | ai-agent | PF · Fact Checker |  | done | 1 |
| t10 | publish | PF · Fact Checker | t9 | running | 1 |

### t1 · Build AI agent PF · Play Picker

Body:
1. Read: \`list_agents\` for "PF · Play Picker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Play Picker" exists with this contract: ai-agent · create · PF · Play Picker: registry row C27 (agent, sub-workflow 5. Outreach drafting, asks A48); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: pick the play for the signal (or the 13-week cycle) and set people, channels, start days and senders, spacing tiers so no two people at one account get email the same day; reads PF Account, PF Person, PF Signal, PF Patch and hand-offs from Buying Signal Spotter (fast lane) and Case for Change Drafter through Read component inputs (component_id C27); writes a PF Component run row of output_type play (play_id, people, channels, start days, senders) and hand-offs to Page Builder, Content Picker and Message Writer, only through Save agent output (component_id C27); threshold and routing: under 70: waiting_person, the BDR picks at Gate 2 (Save agent output applies the threshold 70 and routes below it to BDR picks at Gate 2); feeds (the register): Page Builder; Content Picker; Message Writer; schedule in the registry: Day 2; fast lane within the hour (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; picks senders only from the account's patch and pod; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C27 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C27 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Play Picker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86821f410ab7b2f15695c"}
Read back: PF · Play Picker e_6ae86821f410ab7b2f15695c: get_agent shows models runs/picksTask/answerGeneration e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5, UnifyApps, Vertex, cached), readiness canRun true, not published, deployments [].
Read back: PF · Play Picker: tools exactly ReadComponentInputs e_6ae86836f410ab7b2f156b0d (automation 6ae8635446920244f3d5194b) and SaveAgentOutput e_6ae86836f410ab7b2f156b11 (automation 6ae864829594aa458cc1ce69), both enabled, topicId GLOBAL, descriptions fix component_id "C27".
Read back: PF · Play Picker: instructions state the one job, read with ReadComponentInputs first, save exactly once with SaveAgentOutput, the output contract (output_type play, summary, payload, confidence 0 to 100, evidence, evidence_tag), origin passed through, senders only from the account's patch and pod, refusals.
Read back: PF · Play Picker trace e_6ae86926f38e32761819bad2: ReadComponentInputs {component_id C27, account_id A-1001}, then SaveAgentOutput once with play_id PLAY-SIG-PRICING-VISIT, output_type play, confidence 82, origin "test"; answer: "SaveAgentOutput returned **duplicate** (run_id RUN-6ae868caf13e536c52ec2c87)" (the first test run had saved that row).
Read back: PF · Play Picker refusal case e_6ae8684a9ec43c6ee231033d, toolCalls []: "I can't send emails — that's outside my one job here. I'm the PF · Play Picker (C27)... The Message Writer drafts the actual email content, and a BDR is the one who sends it."
Unverified: PF · Play Picker: the first test run's own result (the save that made RUN-6ae868caf13e536c52ec2c87) was not seen: send_test_messages returned no case id for it. Check: read the PF Component run row RUN-6ae868caf13e536c52ec2c87 for its status.
Note: Model: card e_6acca2af70b66f5702c8b59f is not used (it answers 401, per the task); the agent runs on e_6ad496812dd4ba5be70afcc1, the same Claude Sonnet 5.
Note: Test rows carry origin test and are left for Pipeline Factory · Reset demo; no delete made. Not published, not deployed.

### t2 · Publish PF · Play Picker

Body:
1. Read: \`get_agent\` for "PF · Play Picker" (its id in Built so far).
2. Done when: "PF · Play Picker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Play Picker published.

### t3 · Build AI agent PF · Page Builder

Body:
1. Read: \`list_agents\` for "PF · Page Builder"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Page Builder" exists with this contract: ai-agent · create · PF · Page Builder: registry row C28 (agent, sub-workflow 5. Outreach drafting, asks A49); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: build one Art of the Possible page per account from public facts only: 2 to 3 workflows reimagined before and after for the matched use cases, proof, how UnifyApps connects their core systems and a patch event; reads PF Fact rows and hand-offs from Play Picker through Read component inputs (component_id C28); writes a PF Component run row of output_type aotp_page (the page content in marketing's locked template sections, noindex, a tracked link per prospect, mocked) and hand-offs to Fact Checker and Gate 2, only through Save agent output (component_id C28); threshold and routing: under 75: waiting_person, marketing ops checks (Save agent output applies the threshold 75 and routes below it to marketing ops checks); feeds (the register): Fact Checker; Gate 2; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never publishes a page; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C28 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C28 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Page Builder with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86825f410ab7b2f156a03"}
Read back: PF · Page Builder e_6ae86825f410ab7b2f156a03: get_agent shows models e_6ad496812dd4ba5be70afcc1 in all three slots, readiness canRun true, not published, deployments [].
Read back: PF · Page Builder: tools exactly ReadComponentInputs e_6ae86839d96c5f6ba2441c63 (6ae8635446920244f3d5194b) and SaveAgentOutput e_6ae86839d96c5f6ba2441c66 (6ae864829594aa458cc1ce69), enabled, component_id fixed to "C28".
Read back: PF · Page Builder: instructions state the one job (Art of the Possible page from public facts only, noindex, tracked link per prospect), never publishes a page, read first, save once, output_type aotp_page, origin passed through, refusals.
Read back: PF · Page Builder trace e_6ae86964fbdd550a9a51cf69: ReadComponentInputs C28/A-1001, then SaveAgentOutput once (output_type aotp_page); answer: "SaveAgentOutput returned **waiting_person** (run_id \`RUN-6ae869ccfbdd550a9a51d8ae\`), with reason \"confidence 68 under threshold 75\"".
Read back: PF · Page Builder refusal case e_6ae8685f46920244f3d6603c, toolCalls []: "I'm not able to send emails — that falls outside my one job here, which is building the Art of the Possible page content".
Unverified: PF · Page Builder: the agent said the Play Picker hand-off "was too large to read in full"; ReadComponentInputs results reach the model cut to 18,208 characters (see t7), so its tracked links came from people notes, not the hand-off. Check: rerun after Read component inputs returns a smaller, per-component result.
Note: PF · Page Builder made a second ReadComponentInputs call with person_id P-1002 before saving (save still once).

### t4 · Publish PF · Page Builder

Body:
1. Read: \`get_agent\` for "PF · Page Builder" (its id in Built so far).
2. Done when: "PF · Page Builder" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Page Builder published.

### t5 · Build AI agent PF · Content Picker

Body:
1. Read: \`list_agents\` for "PF · Content Picker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Content Picker" exists with this contract: ai-agent · create · PF · Content Picker: registry row C29 (agent, sub-workflow 5. Outreach drafting, asks A50); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: pick one Content Factory asset per asset touch, matched on role, industry, use case, pattern, outcome, VEP stage and Geo; reads PF Source rows of kind content_asset and hand-offs from Play Picker through Read component inputs (component_id C29); writes a PF Component run row of output_type asset_pick per touch and a hand-off to Message Writer, only through Save agent output (component_id C29); threshold and routing: under 70: no asset, a sourced insight instead; skips assets over 18 months old or retired; never the same asset to two people at one account in a week (Save agent output applies the threshold 70 and routes below it to no asset, a sourced insight); feeds (the register): Message Writer; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never invents an asset; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C29 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C29 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Content Picker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86828f410ab7b2f156a22"}
Read back: PF · Content Picker e_6ae86828f410ab7b2f156a22: get_agent shows models e_6ad496812dd4ba5be70afcc1 in all three slots, readiness canRun true, not published, deployments [].
Read back: PF · Content Picker: tools exactly ReadComponentInputs e_6ae8683ef410ab7b2f156c10 (6ae8635446920244f3d5194b) and SaveAgentOutput e_6ae8683ed96c5f6ba2441cdc (6ae864829594aa458cc1ce69), enabled, component_id fixed to "C29".
Read back: PF · Content Picker: instructions state the one job, never invents an asset, skips assets over 18 months or retired, no same asset to two people in a week, read first, save once, output_type asset_pick, suggested:false with no action, origin passed through.
Read back: PF · Content Picker trace e_6ae869972099302ffb2e9190: ReadComponentInputs C29/A-1001, then SaveAgentOutput once with output_type asset_pick, payload suggested:false, origin "test"; answer: "**Result: saved** — run_id \`RUN-6ae86a0d2099302ffb2e9edc\`, reason: \"saved; this component writes only its run row\" (handoff \`H-6ae86a0d2099302ffb2e9ee9\`)".
Read back: PF · Content Picker refusal case e_6ae86b9d9ec43c6ee2485e31: "I'm not able to send emails — that falls outside my one job here, which is picking a Content Factory asset per outreach touch".
Unverified: PF · Content Picker found no Play Picker hand-off and no content_asset sources, though PF · Play Picker issued hand-offs H-6ae868cbf13e536c52ec2c8f etc.; ReadComponentInputs results reach the model cut to 18,208 characters, which likely dropped them. Check: rerun after Read component inputs returns a per-component result.
Note: PF · Content Picker made two extra ReadComponentInputs calls (person_id, patch_id) before its one save.
Note: The first send_test_messages call for this agent timed out at 60s on the MCP client; its run may also have run on the server.

### t6 · Publish PF · Content Picker

Body:
1. Read: \`get_agent\` for "PF · Content Picker" (its id in Built so far).
2. Done when: "PF · Content Picker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Content Picker published.

### t7 · Build AI agent PF · Message Writer

Body:
1. Read: \`list_agents\` for "PF · Message Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Message Writer" exists with this contract: ai-agent · create · PF · Message Writer: registry row C30 (agent, sub-workflow 5. Outreach drafting, asks A51); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write every email and LinkedIn message in the play, from the Content Factory's best message for category, sub-sector, company and persona, in the assigned handbook voice, with one sourced fact, the pain this person owns and the likeliest objection for their role; reads PF Fact, PF Person, PF Source (handbook, content_asset) and hand-offs from Play Picker, Content Picker, Person Notes Writer and Battlecard Writer through Read component inputs (component_id C30); writes PF Draft rows (status waiting_gate2, its registered records) keyed account_id + person_id + play_id, and hand-offs to Fact Checker and Message Grader, only through Save agent output (component_id C30); threshold and routing: under 70: saved and flagged at Gate 2 (waiting_person for the BDR); copy rules: subject 3 to 6 words on the trigger, emails 90 to 120 words, connection notes under 250 characters, open on the business problem, one insight and one question, no em dashes, placeholders or invented statistics (Save agent output applies the threshold 70 and routes below it to flagged at Gate 2); feeds (the register): Fact Checker; Message Grader; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; names the patch AE as session host and never sends; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C30 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C30 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Message Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: PF · Message Writer did not save through Save agent output in either test round (round 1 case e_6ae869cb46920244f3d6a28e, round 2 case e_6ae86afe9594aa458cd61b23): ReadComponentInputs results arrive cut to 18,208 characters, so the model re-reads looking for hand-offs and drafts and the run ends without SaveAgentOutput. The refusal test called a tool instead of declining. Both rounds are used; it needs Read component inputs to return a smaller per-component result, then one more test.

### t8 · Publish PF · Message Writer

Body:
1. Read: \`get_agent\` for "PF · Message Writer" (its id in Built so far).
2. Done when: "PF · Message Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Message Writer published.

### t9 · Build AI agent PF · Fact Checker

Body:
1. Read: \`list_agents\` for "PF · Fact Checker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Fact Checker" exists with this contract: ai-agent · create · PF · Fact Checker: registry row C31 (checker, sub-workflow 5. Outreach drafting, asks A52); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: trace every claim in drafts and pages: facts to a public source no older than 12 months, numbers to a source or the proof library, use cases to a UC-ID with account evidence; reads PF Draft rows, PF Fact rows and hand-offs from Message Writer and Page Builder through Read component inputs (component_id C31); writes PF Draft.fact_check (its registered field: passed or blocked, with the untraceable claim in its PF Component run row) and a hand-off to Send Rules Check, only through Save agent output (component_id C31); threshold and routing: blocks anything untraceable (no threshold) (Save agent output applies the threshold 0 and routes below it to blocks anything untraceable); feeds (the register): Send Rules Check; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; checks only; never rewrites a draft. Runs on the other model family from Message Writer and Page Builder; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C31 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C31 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Fact Checker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8682ed96c5f6ba2441a5f"}
Read back: PF · Fact Checker e_6ae8682ed96c5f6ba2441a5f: get_agent shows models e_696fe072cb3ef82f7e23dc86 (GPT-5.1 (Azure Open AI), family B) in all three slots, version 5, readiness canRun true, not published, deployments [].
Read back: PF · Fact Checker: tools exactly ReadComponentInputs e_6ae86846d96c5f6ba2441e12 and SaveAgentOutput e_6ae86846d96c5f6ba2441e16 (requires draft_id and top-level fact_check passed or blocked), component_id fixed to "C31".
Read back: PF · Fact Checker: instructions state the one job (trace every claim; checks only, never rewrites a draft), read once first, save exactly once and report a rejection as it came, output_type fact_check, origin passed through, refusals.
Read back: PF · Fact Checker trace e_6ae86b3046920244f3d6f44e (round 2): ReadComponentInputs {C31, A-1001} once, then SaveAgentOutput once with payload fact_check "passed", origin "test", draft_id D-1001; tool answered {"result":"rejected","run_id":"RUN-6ae86a06f13e536c52ec5915","reason":"schema check failed: draft_id missing"}; agent answered "Result: rejected, run_id RUN-6ae86a06f13e536c52ec5915, reason: schema check failed: draft_id missing."
Read back: PF · Fact Checker refusal case e_6ae86b45fbdd550a9a525230: "I'm PF · Fact Checker, component C31. My role is strictly to trace the claims in drafts and pages, not to send emails or messages."
Unverified: PF · Fact Checker sent draft_id D-1001, which no record it saw holds: its ReadComponentInputs result (cut to 18,208 characters) carried no drafts, so the save was rejected and its fact claims were not checked against a real draft. Check: rerun after Read component inputs returns drafts and PF · Message Writer has saved a draft for A-1001.
Unverified: PF · Fact Checker model: card e_696fe072cb3ef82f7e23dc86 is named GPT-5.1, but the trace's raw response reads "model":"gpt-4.1-2025-04-14". Check: an admin confirms the Azure deployment behind the card.
Note: Model: e_6a0dd4e556ffb40e76c2762e answered 401 "Incorrect API key provided" on both test messages; e_694cd3948be44e32a01d7915 (GPT-5.1, openai) answered insufficient_quota/credit_balance_exhausted; the agent runs on the closest active GPT card e_696fe072cb3ef82f7e23dc86 "GPT-5.1 (Azure Open AI)", which answers. It is still a different family from the Message Writer and Page Builder (Claude Sonnet 5).
Note: Round 1 (case e_6ae86a00f38e32761819d7e8, gpt card e_696fe072) called SaveAgentOutput four times after rejections; round 2's instructions fixed it to once.
Note: handover: Save agent output for C31 requires draft_id naming an existing PF Draft row and payload top-level fact_check "passed" or "blocked".
Note: feedback:
Bug: The model card "GPT-5.1 (Azure Open AI)" e_696fe072cb3ef82f7e23dc86 serves gpt-4.1-2025-04-14, not gpt-5.1.
Context: PF · Fact Checker runs on that card after e_6a0dd4e556ffb40e76c2762e answered 401 and e_694cd3948be44e32a01d7915 answered credit_balance_exhausted.
Where: platform
Evidence: list_models shows model gpt-5.1, but the LLM Raw response in trace e_6ae86b3046920244f3d6f44e reads "model":"gpt-4.1-2025-04-14".
Cause: Suspected: the Azure deployment behind the card is a gpt-4.1 deployment.
Regression: One test message on an agent using the card shows a gpt-5.1 model name in the raw response.

### t10 · Publish PF · Fact Checker

Body:
1. Read: \`get_agent\` for "PF · Fact Checker" (its id in Built so far).
2. Done when: "PF · Fact Checker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Fact Checker published.

