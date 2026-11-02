---
nebula: 3
specId: "e_6ae86819d96c5f6ba2441865"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P11"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"PF · Message Grader"},{"action":"publish","kind":"ai-agent","name":"PF · Call Script Writer"},{"action":"publish","kind":"ai-agent","name":"PF · Follow-up Planner"},{"action":"publish","kind":"ai-agent","name":"PF · Inbox Health Checker"}]
touches: [{"kind":"ai-agent","name":"PF · Message Grader"},{"kind":"ai-agent","name":"PF · Call Script Writer"},{"kind":"ai-agent","name":"PF · Follow-up Planner"},{"kind":"ai-agent","name":"PF · Inbox Health Checker"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "fc1ee4c8-93c7-4d7f-9ccf-09cd455d459a"
pageDesign: 2
createdAt: "2026-11-02T10:38:19.369Z"
runningAt: "2026-11-02T10:38:26.367Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P11

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | ai-agent | PF · Message Grader |  | pending | 1 |
| t2 | publish | PF · Message Grader | t1 | pending | 0 |
| t3 | ai-agent | PF · Call Script Writer |  | done | 1 |
| t4 | publish | PF · Call Script Writer | t3 | pending | 0 |
| t5 | ai-agent | PF · Follow-up Planner |  | done | 1 |
| t6 | publish | PF · Follow-up Planner | t5 | pending | 0 |
| t7 | ai-agent | PF · Inbox Health Checker |  | done | 1 |
| t8 | publish | PF · Inbox Health Checker | t7 | pending | 0 |

### t1 · Build AI agent PF · Message Grader

Body:
1. Read: \`list_agents\` for "PF · Message Grader"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Message Grader" exists with this contract: ai-agent · create · PF · Message Grader: registry row C32 (checker, sub-workflow 5. Outreach drafting, asks A53); model GPT-5.1 (model card e_6a0dd4e556ffb40e76c2762e, family B, the checkers' family); one job: grade each draft 0 to 100 on the message rubric: teaches something, relevant to role and company, actionable, applies to their business, well written in the right voice, follows the copy rules; reads PF Draft rows and PF Source handbook rows through Read component inputs (component_id C32); writes PF Draft.grade (its registered field) with the rubric scores in its PF Component run row, and a hand-off to Send Rules Check, only through Save agent output (component_id C32); threshold and routing: under 75: one automatic rewrite is requested (the run says rewrite_requested); under 75 again: waiting_person, a person decides at Gate 2 (Save agent output applies the threshold 75 and routes below it to one rewrite, then a person at Gate 2); feeds (the register): Send Rules Check; schedule in the registry: Day 2 (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; grades only; never rewrites. Runs on the other model family from Message Writer; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C32 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C32 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Message Grader with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Error: PF · Message Grader is built (model, instructions, both tools) and declines out-of-scope work, but its job run cannot save: send_test_message case e_6ae8699546920244f3d69de3 -&gt; SaveAgentOutput result rejected, run RUN-6ae869992099302ffb2e91c0, reason 'schema check failed: draft_id missing', because Read component inputs (~200k chars) is cut by the runtime to 16k+2k chars and no draft reaches the model. After the one instruction fix round the second run (case e_6ae86b07f6f76639f83a38a0) was rejected the same way. Needs Read component inputs narrowed (automation-agent) before this agent can grade.

### t2 · Publish PF · Message Grader

Body:
1. Read: \`get_agent\` for "PF · Message Grader" (its id in Built so far).
2. Done when: "PF · Message Grader" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Message Grader published.

### t3 · Build AI agent PF · Call Script Writer

Body:
1. Read: \`list_agents\` for "PF · Call Script Writer"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Call Script Writer" exists with this contract: ai-agent · create · PF · Call Script Writer: registry row C36 (agent, sub-workflow 6. Outreach, asks A60); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: write the call script for a call task: a signal-tied opener, a permission question, 3 to 5 discovery questions, the top 3 objection answers, a 20-second voicemail and a follow-up email draft, and order the BDR's call list by interest; reads PF Person, PF Signal, PF Fact and PF Source call_transcript rows (Gong, mocked) through Read component inputs (component_id C36); writes a PF Component run row of output_type call_script into the BDR's call list, only through Save agent output (component_id C36); threshold and routing: under 70: waiting_person, the BDR approves the script (Save agent output applies the threshold 70 and routes below it to BDR approves the script); feeds (the register): BDR call list; schedule in the registry: per call task (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never dials; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C36 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C36 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Call Script Writer with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae8687ef410ab7b2f1575c6"}
Read back: PF · Call Script Writer e_6ae8687ef410ab7b2f1575c6: get_agent version 1, readiness canRun true, models runs/picksTask/answerGeneration e_6ad496812dd4ba5be70afcc1 (Claude Sonnet 5 (UnifyApps, Vertex, cached)), role/goal set, instructions state the one job (C36 call script + call list order), read-first/save-once steps, output contract, origin pass-through, scope, never dials; tools ReadComponentInputs e_6ae86895d96c5f6ba24427da -&gt; 6ae8635446920244f3d5194b and SaveAgentOutput e_6ae86895d96c5f6ba24427e2 -&gt; 6ae864829594aa458cc1ce69, both enabled, topicId GLOBAL; deployments 0
Read back: PF · Call Script Writer e_6ae8687ef410ab7b2f1575c6: trace e_6ae8696046920244f3d69a2f calls ReadComponentInputs {component_id:C36, account_id:A-1001}, ReadComponentInputs {..., person_id:P-1002}, then one SaveAgentOutput {component_id:C36, account_id:A-1001, output_type:call_script, ...}; agent said: 'SaveAgentOutput returned **duplicate** (run_id RUN-6ae869289ec43c6ee231f771), with the reason that this is a re-run of an existing run already sitting at **waiting_person**' (the first batch run had saved it waiting_person for BDR approval)
Read back: PF · Call Script Writer e_6ae8687ef410ab7b2f1575c6: refusal case e_6ae868a6fbdd550a9a519ee3 answered 'I'm not able to send emails — that falls outside my one job here, which is writing call scripts and ordering the BDR's call list, not sending messages.' with toolCalls []
Unverified: PF · Call Script Writer: origin test on the first (waiting_person) save is not shown, because send_test_messages returned no case id for that run; the second run's SaveAgentOutput arguments are shortened in the trace. Settle with read_trace e_6ae8696046920244f3d69a2f fullValues modelCalls.2.toolCalls.0.arguments, or the PF Component run row RUN-6ae869289ec43c6ee231f771's origin.
Unverified: PF · Call Script Writer: call_transcript sources sit past the 16,000-char cut of Read component inputs, so objection answers cannot draw on Gong transcripts until that read is narrowed.
Note: Model: Claude Sonnet 5 card e_6acca2af70b66f5702c8b59f replaced by the active 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1 as the task says.
Note: The first send_test_messages call returned no case id for the tool run; a second send_test_message was used to get the trace, and Save agent output answered duplicate (no second write).

### t4 · Publish PF · Call Script Writer

Body:
1. Read: \`get_agent\` for "PF · Call Script Writer" (its id in Built so far).
2. Done when: "PF · Call Script Writer" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Call Script Writer published.

### t5 · Build AI agent PF · Follow-up Planner

Body:
1. Read: \`list_agents\` for "PF · Follow-up Planner"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Follow-up Planner" exists with this contract: ai-agent · create · PF · Follow-up Planner: registry row C37 (agent, sub-workflow 6. Outreach, asks A61); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: keep the account one conversation once anyone responds: a referral becomes the lead thread, a Tier 1 objection pauses Tiers 2 and 3 with an answer note for the AE, 2 or more people engaging in 7 days switches to Committee Surge; reads PF Source reply rows and hand-offs from Reply Sorter through Read component inputs (component_id C37); writes a PF Component run row of output_type replan and hand-offs to Fact Checker and Message Grader for every rewrite, only through Save agent output (component_id C37); threshold and routing: under 70: waiting_person, the BDR decides (Save agent output applies the threshold 70 and routes below it to BDR decides); feeds (the register): Fact Checker; Message Grader; schedule in the registry: on any response (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never sends; every rewrite goes back through Fact Checker and Message Grader; outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C37 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C37 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Follow-up Planner with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86881d96c5f6ba244257b"}
Read back: PF · Follow-up Planner e_6ae86881d96c5f6ba244257b: get_agent version 1, readiness canRun true, models e_6ad496812dd4ba5be70afcc1 in all three slots, role/goal set, instructions state the one job (C37 replan: referral lead thread, Tier 1 objection pause, Committee Surge), read-first/save-once, output contract, origin pass-through, scope, never sends, rewrites go to Fact Checker and Message Grader; tools ReadComponentInputs e_6ae86899d96c5f6ba244286d -&gt; 6ae8635446920244f3d5194b and SaveAgentOutput e_6ae86899f410ab7b2f15786e -&gt; 6ae864829594aa458cc1ce69, both enabled, topicId GLOBAL; deployments 0
Read back: PF · Follow-up Planner e_6ae86881d96c5f6ba244257b: trace e_6ae869a3f13e536c52ec4f4a calls ReadComponentInputs {component_id:C37, account_id:A-1001} (three reads), then one SaveAgentOutput {component_id:C37, account_id:A-1001, output_type:replan, ...}; agent said: '**Result: duplicate** — run_id \`RUN-6ae86984f38e32761819c92a\`. SaveAgentOutput reported this as a re-run of an existing run that's already "waiting_person," so nothing new was written.'
Read back: PF · Follow-up Planner e_6ae86881d96c5f6ba244257b: refusal case e_6ae86a522099302ffb2ec5ec answered 'I'm not able to send emails — that's outside my one job here. I'm the PF Follow-up Planner (component C37)...' with no tool call (llmCalls 1)
Unverified: PF · Follow-up Planner: the reply rows and Reply Sorter hand-offs never reached the model (the agent's own think step: 'Three ReadComponentInputs calls all truncated at the same point (end of "facts", just after F-09)'), so its replan rules are untested on real replies; settle after Read component inputs is narrowed with one run on an account that has replies.
Unverified: PF · Follow-up Planner: origin test on the first (waiting_person) save is not shown because that run returned no case id; settle by reading run RUN-6ae86984f38e32761819c92a's origin.
Note: Model: e_6ad496812dd4ba5be70afcc1 used in place of e_6acca2af70b66f5702c8b59f as the task says.
Note: plan_change: major — same cause as t1: Read component inputs' reply is cut to 16k+2k chars, so C37 never sees sources (reply rows) or handoffs_in and can only save a no-action replan.

### t6 · Publish PF · Follow-up Planner

Body:
1. Read: \`get_agent\` for "PF · Follow-up Planner" (its id in Built so far).
2. Done when: "PF · Follow-up Planner" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Follow-up Planner published.

### t7 · Build AI agent PF · Inbox Health Checker

Body:
1. Read: \`list_agents\` for "PF · Inbox Health Checker"; it must not exist (stop and report if it does). The tool automations are deployed: Pipeline Factory · Read component inputs \`6ae8635446920244f3d5194b\`; Pipeline Factory · Save agent output \`6ae864829594aa458cc1ce69\`; Pipeline Factory · Run component \`6ae865229ec43c6ee2300d8d\`. \`list_models\` shows the model card the line names as active.
2. Done when: the AI agent "PF · Inbox Health Checker" exists with this contract: ai-agent · create · PF · Inbox Health Checker: registry row C38 (agent, sub-workflow 6. Outreach, asks A62); model Claude Sonnet 5 (model card e_6acca2af70b66f5702c8b59f, family A, the drafters' family); one job: check inbox health: placement per active domain, blacklists and reputation, reply rate by recipient provider, and the email-security-scanner list; reads PF Inbox rows through Read component inputs (component_id C38); writes PF Inbox.placement_pct_last and blacklisted (its registered fields), an alert PF Component run row for the BDR and the GTM engineer, and a hand-off to Email Domain Swapper, only through Save agent output (component_id C38); threshold and routing: every alert goes to the BDR and the GTM engineer (threshold 0) (Save agent output applies the threshold 0 and routes below it to the named person); feeds (the register): Email Domain Swapper; schedule in the registry: weekly placement; daily blacklist (run on demand by Pipeline Factory · Run component in this demo); output contract: one JSON object with output_type, summary, payload, confidence 0 to 100, evidence and evidence_tag [PUBLIC] or [HYPOTHESIS], saved once per run, origin passed through as given; tools Read component inputs (Pipeline Factory · Read component inputs), Save agent output (Pipeline Factory · Save agent output); scope: this one job only, it declines anything else (another component's job, sending, booking, editing other fields) and says a field is absent when no record holds it; never rests or swaps a domain itself (Email Domain Swapper owns it); outside systems are the PF records (mocked), no connection. Its tools are exactly the deployed automations the line names, each bound with its inputs described (component_id fixed to C38 in the instructions); its instructions state the one job, the output contract (one JSON object: output_type, summary, payload, confidence 0 to 100, evidence, evidence_tag), that it always reads with Read component inputs first and saves once with Save agent output, the scope and refusals, and that it passes origin through as the message gives it. It is not deployed to any app or channel. Model card: the card e_6acca2af70b66f5702c8b59f answers 401 invalid x-api-key from its provider, so a family-A (Claude Sonnet 5) agent uses the active card 'Claude Sonnet 5 (UnifyApps, Vertex, cached)' e_6ad496812dd4ba5be70afcc1, the same model; a family-B (GPT-5.1) agent uses e_6a0dd4e556ffb40e76c2762e after one test message proves it answers, else the closest active GPT card, named in notes. Results: Save agent output's rule stands (under the component threshold: waiting_person for the named person; at or over: saved; it has no no_action result); where the line says no_action or not suggested, the agent still saves once with changed:false or suggested:false in the payload and says no action in its summary.
3. Test with \`send_test_messages\`, two messages: "Run your job for component C38 on account A-1001; origin test" must call Read component inputs, then Save agent output with origin test, and answer the result it got (saved, waiting_person, proposal, duplicate or rejected) with the run id; "Please send an email to Arjun Mehta" must decline as outside its one job. Read the trace when an answer misses, fix the instructions and test again (two rounds at most). Rows the test writes carry origin test and are left for Pipeline Factory · Reset demo; make no delete. Do not publish: the publish task does.
4. Read back: \`get_agent\` for its model, instructions, tools and settings, and both test answers quoted with the Save agent output result and run id from the trace.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Inbox Health Checker with its model, instructions and the tools the line names; the test run saved through Save agent output and the refusal declined.
Result IDs: {"entity":"e_6ae86884d96c5f6ba24425cc"}
Read back: PF · Inbox Health Checker e_6ae86884d96c5f6ba24425cc: get_agent version 2, readiness canRun true, models e_6ad496812dd4ba5be70afcc1 in all three slots, role/goal set, instructions state the one job (C38 inbox health), read-first (with a component-only re-read when inboxes are cut) and save-once, payload.inbox_id with placement_pct_last and blacklisted, output contract, origin pass-through, scope, never rests or swaps a domain; tools ReadComponentInputs e_6ae8689eafe7fc590a4fac26 -&gt; 6ae8635446920244f3d5194b and SaveAgentOutput e_6ae8689eafe7fc590a4fac2a -&gt; 6ae864829594aa458cc1ce69, both enabled, topicId GLOBAL; deployments 0
Read back: PF · Inbox Health Checker e_6ae86884d96c5f6ba24425cc: trace e_6ae86ad42099302ffb2ed624 calls ReadComponentInputs {component_id:C38, account_id:A-1001}, ReadComponentInputs {component_id:C38}, then one SaveAgentOutput {component_id:C38, account_id:A-1001, output_type:inbox_health, ...}; agent said: '**Result:** \`saved\` · **run_id:** \`RUN-6ae869e746920244f3d6a54f\` · **reason:** saved; wrote placement_pct_last, blacklisted (hand-off \`H-6ae86b052099302ffb2ee2d9\` sent to the Email Domain Swapper)' and 'getunifyapps.example (IN-01) triggered an alert as placement dropped from 92% to 90%'
Read back: PF · Inbox Health Checker e_6ae86884d96c5f6ba24425cc: refusal case e_6ae86a569594aa458cd5fa93 answered 'This falls outside my scope — I'm the Inbox Health Checker (C38)... I don't send emails or messages myself. That task belongs to a **BDR**' with no tool call (llmCalls 1)
Unverified: PF · Inbox Health Checker: origin test on the saved run is in the shortened SaveAgentOutput arguments (prior run trace e_6ae869d59ec43c6ee2366c25 showed origin "test" in full); settle with read_trace e_6ae86ad42099302ffb2ed624 fullValues modelCalls.2.toolCalls.0.arguments.
Unverified: PF · Inbox Health Checker: reply rate by provider and the email-security-scanner list were absent from the PF Inbox rows the agent saw; it reported them absent.
Note: Model: e_6ad496812dd4ba5be70afcc1 used in place of e_6acca2af70b66f5702c8b59f as the task says.
Note: Fix round 1: the first run (case e_6ae869d59ec43c6ee2366c25) saw no inbox rows because the read reply was cut at 16k chars and saved with no inbox_id; instructions now re-read with component_id only (shorter reply showing inboxes) and put inbox_id, placement_pct_last and blacklisted at the payload top level; the second run saved.

### t8 · Publish PF · Inbox Health Checker

Body:
1. Read: \`get_agent\` for "PF · Inbox Health Checker" (its id in Built so far).
2. Done when: "PF · Inbox Health Checker" is published, so Pipeline Factory · Run component can invoke it.
3. Apply \`publish_agent\` once.
4. Read back: \`get_agent\` showing the published version, quoted.
5. Report ids (the agent id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_agent shows PF · Inbox Health Checker published.

