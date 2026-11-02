---
nebula: 3
specId: "e_6ae83fcdd96c5f6ba225b227"
mode: "sonic"
title: "Pipeline Factory Control Tower · automations, part 1"
owner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save hand-off"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Log signal"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Decide Gate 1"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Clear Gate 2"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Book meeting"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Save hand-off"},{"kind":"automation","name":"Pipeline Factory · Log signal"},{"kind":"automation","name":"Pipeline Factory · Decide Gate 1"},{"kind":"automation","name":"Pipeline Factory · Clear Gate 2"},{"kind":"automation","name":"Pipeline Factory · Book meeting"}]
reviewEvidence: []
revision: 2
revisionHistory: [{"revision":2,"at":"2026-11-02T07:57:02.036Z","impact":"absorbed","reason":"Unattended run: no person can confirm deletes, so test rows are left for Reset demo instead of deleted.","added":0,"removed":0,"changed":5,"previousRemaining":10}]
creationId: "346c74c9-722d-4f7e-a95b-63d878660411"
pageDesign: 2
createdAt: "2026-11-02T07:46:24.038Z"
runningAt: "2026-11-02T07:46:50.442Z"
runner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"8da1d8cb-cc02-5ac8-85df-da01be5fab51"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory Control Tower · automations, part 1

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Save hand-off |  | done | 1 |
| t2 | deploy | Pipeline Factory · Save hand-off | t1 | done | 1 |
| t3 | automation | Pipeline Factory · Log signal | t2 | done | 1 |
| t4 | deploy | Pipeline Factory · Log signal | t3 | done | 1 |
| t5 | automation | Pipeline Factory · Decide Gate 1 | t2 | done | 1 |
| t6 | deploy | Pipeline Factory · Decide Gate 1 | t5 | done | 1 |
| t7 | automation | Pipeline Factory · Clear Gate 2 |  | done | 1 |
| t8 | deploy | Pipeline Factory · Clear Gate 2 | t7 | done | 1 |
| t9 | automation | Pipeline Factory · Book meeting | t2 | done | 1 |
| t10 | deploy | Pipeline Factory · Book meeting | t9 | done | 1 |

### t1 · Build Pipeline Factory · Save hand-off

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Save hand-off"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`.
2. Done when: the callable automation "Pipeline Factory · Save hand-off" is saved, compiled clean, with exactly this contract: callable from other automations; inputs from_component (text), to_component (text), record_type (text), patch_id (text), account_id (text), person_id (text), play_id (text), confidence (number), payload (text, JSON), evidence (text), writes_field (text); result result (text: saved \| duplicate \| rejected \| waiting_person), handoff_id (text), reason (text). Deterministic, no model call: refuses a pair not in the register (PF Component feeds) with rejected "not registered"; refuses a writes_field whose writer is another component with rejected "one writer per field"; refuses a payload with no confidence, no evidence or no patch_id with rejected "schema check failed: \`field\` missing" and a PF Hand-off row assigned_to GTM engineer; looks up idempotency_key account_id + person_id + play_id and answers duplicate without a second row; under the to-component's threshold saves waiting_person assigned to its below_threshold_goes_to; else saves flowed. Every row carries model, cost_usd, latency_ms and saved_at. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: make your own rows with origin \`test\` and unique ids that start \`T-\` (a test account, person, draft or component as the case needs, copied in shape from a seed row), run each result path the line names at least once, read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave the T- rows in place (Pipeline Factory · Reset demo clears origin test rows) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is seed or user; never test against the story row A-1001 or any other seeded row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Save hand-off; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae840a5fbdd550a9a44c524"}
Read back: Pipeline Factory · Save hand-off 6ae840a5fbdd550a9a44c524: search_workflows now answers version 2, deployment null, 31 nodes — the same version tested and scored
Read back: Pipeline Factory · Save hand-off 6ae840a5fbdd550a9a44c524: search_workflows found no automation of that name before the build; compile_and_save_workflow created it (version 0), saved version 2 is the latest; open_workflow version 2, deployment null (not deployed, as the task says)
Read back: Pipeline Factory · Save hand-off: open_workflow trigger CALLABLE callables/callables_from_automation; setup from_component, to_component, record_type, patch_id, account_id, person_id, play_id (string), confidence (number), payload, evidence, writes_field (string); result result (string enum saved\|duplicate\|rejected\|waiting_person), handoff_id (string), reason (string), all three required
Read back: Pipeline Factory · Save hand-off: describe_callable_workflow returned 11 parameters, the same names and types as above (confidence number, all others string)
Read back: Pipeline Factory · Save hand-off run 6ae84176fbdd550a9a44edc9 (v2, blank payload {}): COMPLETED, response {result: rejected, handoff_id: '', reason: 'not registered'}
Read back: Pipeline Factory · Save hand-off run 6ae84155f13e536c52a46a44 (v1, T-Other Writer to T-Receiver Agent, pair not in feeds): COMPLETED, {result: rejected, handoff_id: '', reason: 'not registered'}
Read back: Pipeline Factory · Save hand-off run 6ae84158f6f76639f8cec8f8 (v1, writes_field t_field_b written by T-C3): COMPLETED, {result: rejected, handoff_id: '', reason: 'one writer per field'}
Read back: Pipeline Factory · Save hand-off run 6ae8415af38e327618fc7383 (v1, evidence blank): COMPLETED, {result: rejected, handoff_id: H-6ae8415af38e327618fc7383, reason: 'schema check failed: evidence missing'}; get_records row: schema_status rejected, status rejected, assigned_to 'GTM engineer'
Read back: Pipeline Factory · Save hand-off run 6ae8417c17ec564d96dfe36a (v2, confidence absent): COMPLETED, {result: rejected, reason: 'schema check failed: confidence missing'}; get_records row assigned_to 'GTM engineer'
Read back: Pipeline Factory · Save hand-off run 6ae8417af13e536c52a5ad85 (v2, T-C1 to T-C2 by id, confidence 80): COMPLETED, {result: saved, handoff_id: H-6ae8417af13e536c52a5ad85, reason: 'flowed on'}; get_records row status flowed, schema_status passed, idempotency_key 'T-A1\|T-P7\|T-PLAY', model 'none (deterministic)', cost_usd 0, latency_ms 462, saved_at 1793606010879
Read back: Pipeline Factory · Save hand-off run 6ae841789ec43c6ee2de5cf4 (v2, same key T-A1\|T-P1\|T-PLAY as run 6ae8415217ec564d96dfd581 that saved): COMPLETED, {result: duplicate, handoff_id: H-6ae8415217ec564d96dfd581}; get_records on account_id T-A1 shows exactly one row with that idempotency_key (total 7 rows, all keys distinct)
Read back: Pipeline Factory · Save hand-off run 6ae841859594aa458cb9c0e1 (v2, confidence 55 under T-Receiver Agent threshold 70): COMPLETED, {result: waiting_person, handoff_id: H-6ae841859594aa458cb9c0e1, reason: 'confidence 55 under 70.0'}; get_records row status waiting_person, assigned_to 'T-BDR Reviewer' (the receiver's below_threshold_goes_to)
Read back: Pipeline Factory · Save hand-off: best practice 84 (82 of 85 checks), under 90 after 1 fix round, first read 81, version 2
Read back: Pipeline Factory · Save hand-off security: no secret in any node; every created row carries origin 'user' (contract has no origin input); writes set only the PF Hand-off fields the line names
Unverified: Pipeline Factory · Save hand-off: the not-registered-pair and one-writer paths were run on version 1; version 2 only added a blank-pair guard in front of them (runs on v2 of the saved, duplicate, schema and waiting paths are green). Check: one run of each on version 2
Unverified: Pipeline Factory · Save hand-off against the real seeded register: PF Component holds no seed rows yet (get_records total 0), so name matching against seed feeds such as 'Play Picker (fast lane)' and 'Gate 1 (human: pod BDR)' is untested. Check: one run with from_component 'Buying Signal Spotter', to_component 'Play Picker' once the 57 seed rows land
Note: assumed: from_component and to_component accept a component_id or a name; the component row is found by component_id, exact name, or name starting with the input (so 'Gate 1' finds 'Gate 1 (human: pod BDR)'); a pair is registered when the sender's feeds text contains the to_component input or the receiver's name
Note: assumed: one-writer check = another PF Component (component_id not the sender's) whose writes text contains writes_field; a blank writes_field skips it. Substring match, so a short field name can match a longer one
Note: assumed: schema check order confidence, evidence, patch_id; the first missing one names the reason
Note: assumed: duplicate lookup matches idempotency_key AND from_component AND to_component AND schema_status passed, so two different hand-offs for the same account/person/play (Gate 1 to two components) are not merged and a schema-rejected try does not block a corrected retry
Note: assumed: model 'none (deterministic)', cost_usd 0, latency_ms = run time so far, saved_at = RUN.currentTime (the contract has no model or cost input)
Note: handover: Save hand-off workflowId 6ae840a5fbdd550a9a44c524; idempotency_key format is '&lt;account_id&gt;\|&lt;person_id&gt;\|&lt;play_id&gt;'; handoff_id is 'H-&lt;executionId&gt;' and equals the row's record id; callers read result/handoff_id/reason at the top level of the call output
Note: handover: Save hand-off threshold reasons render the stored number as e.g. 'confidence 55 under 70.0'
Note: Defect found and fixed during testing: a blank payload failed at the first fetch (run 6ae8415df38e327618fc73b1, 'No Value found in filter with field: properties.component_id'); version 2 checks for a blank pair before the fetches, and run 6ae84176fbdd550a9a44edc9 answered rejected 'not registered'
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create record (n_8vnws, n_53la3, n_mfimt) · fix would change behaviour: the check names no field, the DSL has no node I/O visibility option, and renaming the contract's fields is not allowed
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_utr12, n_6ntkv, n_4fkhh, n_o04rw) · needs object indexes on OBJ_pf_component (component_id, name, writes) and OBJ_pf_handoff (idempotency_key, from_component, to_component, schema_status) outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create record (n_8vnws, n_53la3, n_mfimt) · fix would change behaviour: the create nodes are the hand-off writes; the answer returns the generated handoff_id
Note: test rows left for Reset demo: PF Component (OBJ_pf_component) T-C1, T-C2, T-C3 (origin test)
Note: test rows left for Reset demo (origin user, account_id T-A1, made by the test runs because Save hand-off has no origin input): PF Hand-off (OBJ_pf_handoff) H-6ae84105f6f76639f8ceba61, H-6ae8415217ec564d96dfd581, H-6ae8415af38e327618fc7383, H-6ae8415c2099302ffb12d7db, H-6ae8417af13e536c52a5ad85, H-6ae8417c17ec564d96dfe36a, H-6ae841859594aa458cb9c0e1 — Reset demo clears origin test rows only, so these 7 need their own cleanup
Note: No delete call made, per the person's answer: 'This is an unattended run: no person can answer a delete, so make no delete call and do not report declined.' Not deployed: the deploy task does.

### t2 · Deploy Pipeline Factory · Save hand-off

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Save hand-off" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Save hand-off" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Save hand-off".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Save hand-off deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae840a5fbdd550a9a44c524"}
Read back: Pipeline Factory · Save hand-off 6ae840a5fbdd550a9a44c524: open_workflow before deploy answered version 2, deployment null — the version t1 tested and scored
Read back: Pipeline Factory · Save hand-off: deploy_workflow returned ok:true, 'Deployed version 2 of automation 6ae840a5fbdd550a9a44c524.', paused false, storedVersion 2
Read back: Pipeline Factory · Save hand-off: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 2, deployedAt: 1793606354885, savedAfterDeploy: false} — definitionVersion 2 equals the saved version
Read back: Pipeline Factory · Save hand-off: best practice 84 (82 of 85 checks), version 2, read once (deploy task makes no fix round)
Read back: Pipeline Factory · Save hand-off: callers Log signal, Decide Gate 1 and Book meeting called the deployed copy (version -1) in test runs and got result saved, e.g. child run 6ae84591fbdd550a9a45b2a0 answered {result: saved, handoff_id: H-6ae84591fbdd550a9a45b2a0, reason: 'flowed on'}
Note: deploymentNotes 'Demo Studio · Pipeline Factory v1 · Pipeline Factory · Save hand-off' (bridge adds the plan tag). Answer from the person: yes, deploy Pipeline Factory · Save hand-off. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create record (n_cjwsl, n_8vnws, n_53la3, n_mfimt) · task does not save; fix would change behaviour: the check flags nodes carrying the contract field account_id (Clear Gate 2, whose contract has no account_id, passes it); renaming contract fields is not allowed and the DSL has no node I/O visibility option
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_utr12, n_6ntkv, n_4fkhh, n_o04rw) · task does not save; needs object indexes on OBJ_pf_component and OBJ_pf_handoff outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create record (n_8vnws, n_53la3, n_mfimt) · task does not save
Note: Finding for the router: Save hand-off's schema-check branch has overlapping arms (confidence/evidence/patch_id missing); the platform runs every true branch arm in parallel (see feedback), so when two fields are missing the reason may name either. The result stays rejected. A fix is a change to Save hand-off, outside this task.

### t3 · Build Pipeline Factory · Log signal

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Log signal"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`. It calls "Pipeline Factory · Save hand-off" (deployed; its workflowId from \`search_workflows\`) for every hand-off it saves, never writing PF Hand-off itself.
2. Done when: the callable automation "Pipeline Factory · Log signal" is saved, compiled clean, with exactly this contract: callable from the app; inputs account_id (text), signal_type (text, a PF Signal code), source_link (text), seconds_on_page (number), scrolled (boolean), minutes_after_email (number), origin (text); result result (text: counted \| not_counted \| fast_lane), timing_score (number), reason (text). Deterministic: the checked-visit rule (10+ seconds and a scroll, or a repeat within 7 days; never within 2 minutes of an email's delivery, never from a scanner network, never with no interaction); weights from the starting signal weights; timing_score is the sum of counted weights, capped at 40; new_leader, event, vendor_renewal and a second checked visit are strong and go to the fast lane: one PF Hand-off Buying Signal Spotter to Play Picker through Save hand-off, due within the hour. Writes PF Signal and PF Account.timing_score. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: make your own rows with origin \`test\` and unique ids that start \`T-\` (a test account, person, draft or component as the case needs, copied in shape from a seed row), run each result path the line names at least once, read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave the T- rows in place (Pipeline Factory · Reset demo clears origin test rows) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is seed or user; never test against the story row A-1001 or any other seeded row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Log signal; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae843cc9594aa458cba14d7"}
Read back: Pipeline Factory · Log signal 6ae843cc9594aa458cba14d7: search_workflows found no automation of that name before the build; created at version 0, saved version 1 is the latest (not deployed, as the task says)
Read back: Pipeline Factory · Log signal: trigger CALLABLE callables/callables_from_automation; setup account_id, signal_type, source_link (string), seconds_on_page (number), scrolled (boolean), minutes_after_email (number), origin (string); result result (string enum counted\|not_counted\|fast_lane), timing_score (number), reason (string), all required
Read back: Pipeline Factory · Log signal: describe_callable_workflow returned 7 parameters with those names and types
Read back: Pipeline Factory · Log signal run 6ae8448c17ec564d96e093bd (v0, blank {}): COMPLETED {result: not_counted, timing_score: 0, reason: 'account_id is required'}; run 6ae8448ef38e327618fcda14 (v0, signal_type not_a_code): {result: not_counted, reason: 'signal_type is not a PF Signal code'}
Read back: Pipeline Factory · Log signal run 6ae845039ec43c6ee2e2245c (v1, visit 1 minute after an email): {result: not_counted, timing_score: 30, reason: "visit within 2 minutes of an email's delivery"}
Read back: Pipeline Factory · Log signal run 6ae84506f38e327618fce5f5 (v1, scanner link): {result: not_counted, reason: 'visit from a security-scanner network'}; run 6ae845c0f6f76639f8cf6bfa (v1, 0 s, no scroll): {result: not_counted, reason: 'visit with no page interaction'}; run 6ae8450af38e327618fce61d (v1, 4 s, no scroll, no prior visit): not_counted 'visit under 10 seconds or without a scroll, and no visit in the last 7 days'
Read back: Pipeline Factory · Log signal run 6ae8451a17ec564d96e0b295 (v1, repeat short visit on T-A13): {result: counted, timing_score: 25, reason: 'checked visit: repeat within 7 days'}; run 6ae84513f13e536c52c63773 (v1, 30 s + scroll on T-A12 at 30): {result: counted, timing_score: 40, reason: 'checked visit: 10+ seconds and a scroll'} (30+25 capped at 40)
Read back: Pipeline Factory · Log signal run 6ae84524f6f76639f8cf59a6 (v1, second checked visit T-A12): {result: fast_lane, timing_score: 40, reason: 'strong signal: second checked visit in 14 days; fast-lane hand-off saved H-6ae84527f6f76639f8cf59bf, due within the hour'}; run 6ae8452a17ec564d96e0b45f (v1, new_leader T-A13): fast_lane, hand-off H-6ae8452b17ec564d96e0b46b
Read back: Pipeline Factory · Log signal get_records OBJ_pf_handoff: H-6ae84527f6f76639f8cf59bf and H-6ae8452b17ec564d96e0b46b from 'Buying Signal Spotter' to 'Play Picker', status flowed, idempotency_key 'T-A12\|\|fast_lane:pricing_visit' / 'T-A13\|\|fast_lane:new_leader', payload due_at = signal time + 3600000 (e.g. 1793610555154)
Read back: Pipeline Factory · Log signal run 6ae845bef13e536c52c668f7 (v1, bombora on T-A14 at 35): {result: counted, timing_score: 40}; get_records PF Signal S-6ae845bef13e536c52c668f7 weight 15, counted true, origin test; S-6ae845c0f6f76639f8cf6bfa weight 0, counted false, not_counted_reason 'visit with no page interaction'; PF Account T-A14 timing_score 40
Read back: Pipeline Factory · Log signal: best practice 83 (80 of 85 checks), version 1, first read 85 on version 0; no fix round (version 1 was a defect fix, see notes)
Read back: Pipeline Factory · Log signal security: no secret in any node; writes only the PF Signal fields and PF Account.timing_score the line names; origin is the caller's only when it is user or test, else user
Unverified: Pipeline Factory · Log signal: the blank, unknown-type and weight-10/15 non-visit paths ran on version 0; version 1 changed only the visit rules and the not-counted weight. Check: one blank run and one funding run on version 1
Unverified: Pipeline Factory · Log signal: vendor_renewal and event fast-lane arms not run on their own (new_leader shares the event arm). Check: one vendor_renewal run on a test account
Note: assumed: 'from a scanner network' = source_link contains 'scanner' (the contract has no network input); 'no interaction' = seconds_on_page missing or 0 and scrolled not true
Note: assumed: the checked-visit rule applies only to pricing_visit; every other PF Signal code counts at its starting weight (25 visit, 20 new_leader/event, 15 ai_hiring/earnings/bombora/vendor_interest/vendor_renewal, 10 funding/exec_posts)
Note: assumed: 'repeat within 7 days' = any earlier pricing_visit signal for the account in 7 days; 'second checked visit' = a checked visit with an earlier counted pricing_visit in 14 days (the weight table's '2+ in 14 days')
Note: assumed: timing_score = MIN(40, the account's stored timing_score + the counted weight); recomputing from PF Signal rows would lower seeded scores (A-1001 stores 25 but its counted seed signals sum to 55)
Note: assumed: fast-lane hand-off fields: confidence 90, record_type 'signal', person_id '', play_id 'fast_lane:&lt;signal_type&gt;', due within the hour as payload due_at (Save hand-off has no due_at input); every signal is written, counted or not
Note: Defect found and fixed during testing: version 0 wrote the visit rules as one branch; the platform ran every matching arm (run 6ae8449df13e536c52c61343 counted a visit 1 minute after an email; run 6ae8449f17ec564d96e09b26 sent a scanner visit down the fast lane, hand-off H-6ae844a017ec564d96e09b3f on T-A10). Version 1 uses an if/else-if chain and runs 6ae845039ec43c6ee2e2245c, 6ae84506f38e327618fce5f5 answer not_counted
Note: handover: Log signal workflowId 6ae843cc9594aa458cba14d7; a DSL branch runs every arm whose condition is true, so callers and later builds must keep arms mutually exclusive or use if/else-if
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create record, Call automation (n_07qlq, n_v6pkc, n_tbym3) · fix would change behaviour: the check flags nodes carrying the contract field account_id (Clear Gate 2, whose contract has no account_id, passes it); renaming contract fields is not allowed and the DSL has no node I/O visibility option
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition (n_nlfs3, n_69ba7, n_9cj3m, n_md4rl, n_7z06y) · fix would change behaviour: a branch runs every true arm, so the ordered visit rules must stay nested if/else
Note: best practice exception: CHECK_59 Limit multiple variable definitions except for branches · Create variables (n_smuou, n_siv57) · the save refused merging (UNKNOWN_INPUT_KEY on the existing node, see feedback)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_is6k1, n_49ey1, n_bow33) · needs object indexes on OBJ_pf_account (account_id) and OBJ_pf_signal (account_id, signal_type, counted, signal_date) outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create record, Update an existing record's fields (n_v6pkc, n_6gw4i) · fix would change behaviour: these are the PF Signal and timing_score writes
Note: Test rows I made that a concurrent Reset demo already removed: PF Account T-A10, T-A11, T-A12, T-A13 and their PF Signal rows (see feedback)
Note: test rows left for Reset demo: PF Account (OBJ_pf_account) T-A14; PF Signal (OBJ_pf_signal) S-6ae845bef13e536c52c668f7, S-6ae845c0f6f76639f8cf6bfa
Note: test rows left (origin user, made through Save hand-off, which has no origin input; Reset demo will not clear them): PF Hand-off H-6ae844a017ec564d96e09b3f (T-A10), H-6ae84527f6f76639f8cf59bf (T-A12), H-6ae8452b17ec564d96e0b46b (T-A13)
Note: feedback:
Bug: A DSL branch([...]) runs every arm whose condition matches, in parallel, not only the first; the DSL guide describes it as a multi-way switch.
Context: Pipeline Factory · Log signal 6ae843cc9594aa458cba14d7 v0, orbit UAT; arms 'Within 2 minutes of an email' and '10+ seconds and a scroll' both matched one payload.
Where: platform
Evidence: run 6ae8449df13e536c52c61343 shows BRANCH_CONDITION n_nd917@1 and n_nd917@4 both COMPLETED; a visit 1 minute after an email answered counted instead of not_counted.
Cause: Confirmed: BRANCH runs each true arm; rewriting as if/else-if fixed it (v1 run 6ae845039ec43c6ee2e2245c answers not_counted).
Regression: a branch with two overlapping arms setting one variable runs exactly one arm, or the guide says all matching arms run.
Note: feedback:
Bug: A concurrent Pipeline Factory · Reset demo run deleted this builder's origin test rows mid-test.
Context: plan e_6ae83fd1afe7fc590a161a7f batch 161a7f-automation-agent-1-3; T- accounts, patch and signals vanished between ~1793606752656 and ~1793606970000 while every seed account went to version 1 at 1793606961186-969851.
Where: nebula
Evidence: Decide Gate 1 runs 6ae8453cfbdd550a9a45a1af and 6ae8453e17ec564d96e0b644 answered 'account not found' for T-A27/T-A28 created minutes earlier; get_records OBJ_pf_account account_id STARTS_WITH T-A returned total 0.
Cause: Suspected: a Reset demo test ran in parallel with builders relying on origin test rows; next check: which batch ran Reset demo at 1793606961000.
Regression: no Reset demo run deletes origin test rows while a builder batch that made them is still running.
Note: feedback:
Bug: compile_and_save_workflow refuses new keys on an existing create_variables node (UNKNOWN_INPUT_KEY, 'Known properties' = the saved node's keys), so variables cannot be merged as CHECK_59 asks.
Context: Pipeline Factory · Log signal 6ae843cc9594aa458cba14d7, adding timing_score and due_at to node n_smuou.
Where: mcp-tool
Evidence: "'timing_score' does not exist in type 'Inputs of variable_by_unifyapps::variable_by_unifyapps_create_variables'. Known properties: 'counted', 'known_type', 'nc_reason', 'origin', 'reason', 'strong', 'weight'."
Cause: Unknown — next check: whether the compiler types a saved create_variables node from its stored inputs.
Regression: adding a key to an existing create_variables node compiles clean.

### t4 · Deploy Pipeline Factory · Log signal

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Log signal" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Log signal" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Log signal".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Log signal deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae843cc9594aa458cba14d7"}
Read back: Pipeline Factory · Log signal 6ae843cc9594aa458cba14d7: search_workflows before deploy showed version 1 (the version t3 saved), deployment null
Read back: Pipeline Factory · Log signal 6ae843cc9594aa458cba14d7: deploy_workflow answered ok:true, workflowVersion 1, deployedVersion 1, paused false, storedVersion 1, 'Deployed version 1 of automation 6ae843cc9594aa458cba14d7.'
Read back: Pipeline Factory · Log signal 6ae843cc9594aa458cba14d7: search_workflows after deploy: deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 1, deployedAt: 1793607301275, savedAfterDeploy: false}; definitionVersion 1 equals the saved version 1
Read back: Pipeline Factory · Log signal: best practice 83 (80 of 85 checks), version 1, read once; no fix round (deploy-only task)
Unverified: Pipeline Factory · Log signal: the plan tag the bridge appends to deploymentNotes was not shown by any read; check the tenant's deployment history for the notes 'Demo Studio · Pipeline Factory v1 · Pipeline Factory · Log signal [nebula plan e_6ae83fd1afe7fc590a161a7f]'
Note: Deployed on the plan's approval: the spec the person accepted names Pipeline Factory · Log signal under Ready when.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create record, Call automation · task does not save
Note: best practice exception: CHECK_59 Limit multiple variable definitions except for branches · Create variables (n_smuou), Create variables (n_siv57) · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_is6k1), Fetch records (n_49ey1), Fetch records (n_bow33) · task does not save
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition (n_nlfs3, n_69ba7, n_9cj3m, n_md4rl, n_7z06y) · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create record, Update an existing record's fields · task does not save

### t5 · Build Pipeline Factory · Decide Gate 1

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Decide Gate 1"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`. It calls "Pipeline Factory · Save hand-off" (deployed; its workflowId from \`search_workflows\`) for every hand-off it saves, never writing PF Hand-off itself.
2. Done when: the callable automation "Pipeline Factory · Decide Gate 1" is saved, compiled clean, with exactly this contract: callable from the app; inputs account_id (text), decision (text: accept \| reject), reason (text: bad_fit \| active_deal \| wrong_timing \| in_conversation), origin (text); result result (text: accepted \| rejected \| blocked), refill_account_id (text), reason (text). Hard blocks answer blocked with the cause: no Patch ID, no AE or pod, an AE hold, or factory_holdout true ("held out until" and the date). A reject needs one reason and refills the slot with the next queued account of the same patch (lowest rank_in_patch), never another patch's. An accept saves a Gate 1 to Company Facts Collector and Buying Team Mapper hand-off through Save hand-off and adds 1 to PF Patch.slots_used. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: make your own rows with origin \`test\` and unique ids that start \`T-\` (a test account, person, draft or component as the case needs, copied in shape from a seed row), run each result path the line names at least once, read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave the T- rows in place (Pipeline Factory · Reset demo clears origin test rows) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is seed or user; never test against the story row A-1001 or any other seeded row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Decide Gate 1; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae8440df13e536c52c5d959"}
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: search_workflows found no automation of that name before the build; created at version 0, saved version 1 is the latest (not deployed)
Read back: Pipeline Factory · Decide Gate 1: trigger CALLABLE callables/callables_from_automation; setup account_id (string), decision (string enum accept\|reject), reason (string enum bad_fit\|active_deal\|wrong_timing\|in_conversation), origin (string); result result (enum accepted\|rejected\|blocked), refill_account_id (string), reason (string), all required; describe_callable_workflow returned the same 4 parameters
Read back: Pipeline Factory · Decide Gate 1 run 6ae845349ec43c6ee2e43198 (v1, blank {}): {result: blocked, refill_account_id: '', reason: 'account_id is required'}
Read back: Pipeline Factory · Decide Gate 1 runs (v1, accept): 6ae84564f6f76639f8cf5ec0 T-A25 'no Patch ID'; 6ae845679594aa458cba4f02 T-A26 'no AE or pod'; 6ae8456917ec564d96e0bf55 T-A27 'AE hold: the parent account is held by T AE Two'; 6ae8456cf38e327618fcf465 T-A28 'held out until 2027-01-27' — each result blocked; get_records gate1_status blocked on T-A25..T-A28
Read back: Pipeline Factory · Decide Gate 1 run 6ae845739ec43c6ee2e6e0a6 (reject, reason ''): {result: blocked, reason: 'a reject needs one reason: bad_fit, active_deal, wrong_timing or in_conversation'}
Read back: Pipeline Factory · Decide Gate 1 run 6ae8457d9594aa458cba5063 (reject T-A21 bad_fit): {result: rejected, refill_account_id: 'T-A23', reason: 'rejected: bad_fit; slot refilled from patch T-PATCH-1'}; get_records T-A21 rejected/bad_fit, T-A23 (rank 4, same patch) pending, T-A22 (rank 5) and T-A24 (other patch, rank 1) still queued
Read back: Pipeline Factory · Decide Gate 1 run 6ae84575f38e327618fcf657 (accept T-A20): {result: accepted, reason: 'accepted; hand-offs: Company Facts Collector saved, Buying Team Mapper saved'}; get_records PF Hand-off H-6ae84575f38e327618fcf658 Gate 1 → Company Facts Collector and H-6ae84576f38e327618fcf668 Gate 1 → Buying Team Mapper, both flowed, key 'T-A20\|\|gate1'; PF Patch T-PATCH-1 slots_used 3 → 4
Read back: Pipeline Factory · Decide Gate 1 run 6ae8457e17ec564d96e0c300 (accept T-A20 again): {result: accepted, reason: 'already accepted at Gate 1'}, no update or call node ran; slots_used still 4
Read back: Pipeline Factory · Decide Gate 1: best practice 67 (81 of 85 checks) after 1 fix round, first read 56, version 1
Read back: Pipeline Factory · Decide Gate 1 security: re-reads the account from storage in the same run and branches on what it read; writes only gate1_status, gate1_reason and slots_used by record id; hand-offs only through Save hand-off
Unverified: Pipeline Factory · Decide Gate 1: an unknown decision value (not accept or reject) was not run. Check: one run with decision 'maybe' answers blocked 'decision must be accept or reject'
Note: assumed: 'AE hold' = ultimate_parent_lock set and different from owner_ae; PF Account has no AE-hold field (plan_change: requirement if a real AE-hold field is wanted)
Note: assumed: hard blocks apply to accept and reject alike and set gate1_status blocked; a reject with no valid reason answers blocked (the result enum has no error value)
Note: assumed: refill moves the next queued account of the same patch (lowest rank_in_patch) to gate1_status pending; an accept of an already accepted account answers accepted and writes nothing
Note: assumed: Gate 1 hand-offs use from_component 'Gate 1', record_type 'gate1_decision', play_id 'gate1', person_id '', confidence 100; origin input is accepted but unused (this automation creates no rows itself)
Note: Version 1 replaced the hard-block branch with if/else-if (a branch runs every true arm, so two causes would race on one variable) and moved the blank refill id into a variable (CHECK_39 cleared, 56 → 67)
Note: handover: Decide Gate 1 workflowId 6ae8440df13e536c52c5d959
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Respond to automation x9, Call automation x2 (n_yni3c, n_me1f2, n_dk6h2, n_f4noe, n_57n94, n_2y213, n_22kfy, n_vi51h, n_qr8y9, n_qb3hq, n_7ld0t, n_wzm03) · fix would change behaviour: the check flags nodes carrying the contract fields account_id / refill_account_id (Clear Gate 2, whose contract has no account_id, passes it); renaming contract fields is not allowed and the DSL has no node I/O visibility option
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition (n_1ban7, n_odvh9) · fix would change behaviour: a branch runs every true arm
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_uxpxc, n_vo43y, n_co0k2) · needs object indexes on OBJ_pf_account and OBJ_pf_patch outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_jvl59, n_lyt8t, n_axd0o, n_5zxn6, n_rachq) · fix would change behaviour: these are the Gate 1 writes
Note: test rows left for Reset demo: PF Account (OBJ_pf_account) T-A20, T-A21, T-A22, T-A23, T-A24, T-A25, T-A26, T-A27, T-A28; PF Patch (OBJ_pf_patch) T-PATCH-1
Note: test rows left (origin user, made through Save hand-off; Reset demo will not clear them): PF Hand-off H-6ae84575f38e327618fcf658, H-6ae84576f38e327618fcf668 (T-A20)

### t6 · Deploy Pipeline Factory · Decide Gate 1

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Decide Gate 1" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Decide Gate 1" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Decide Gate 1".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Decide Gate 1 deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae8440df13e536c52c5d959"}
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: search_workflows before deploy showed version 1 (the version t5 saved), deployment null
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: deploy_workflow answered ok:true, workflowVersion 1, deployedVersion 1, paused false, storedVersion 1, 'Deployed version 1 of automation 6ae8440df13e536c52c5d959.'
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: search_workflows after deploy: deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 1, deployedAt: 1793607302976, savedAfterDeploy: false}; definitionVersion 1 equals the saved version 1
Read back: Pipeline Factory · Decide Gate 1: best practice 67 (81 of 85 checks), version 1, read once; no fix round (deploy-only task)
Unverified: Pipeline Factory · Decide Gate 1: the plan tag the bridge appends to deploymentNotes was not shown by any read; check the tenant's deployment history for the notes 'Demo Studio · Pipeline Factory v1 · Pipeline Factory · Decide Gate 1 [nebula plan e_6ae83fd1afe7fc590a161a7f]'
Note: Deployed on the plan's approval: the spec the person accepted names Pipeline Factory · Decide Gate 1 under Ready when.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Respond to automation (8 nodes), Call automation (n_7ld0t, n_wzm03) · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_uxpxc, n_vo43y, n_co0k2) · task does not save
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition (n_1ban7, n_odvh9) · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_jvl59, n_lyt8t, n_axd0o, n_5zxn6, n_rachq) · task does not save

### t7 · Build Pipeline Factory · Clear Gate 2

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Clear Gate 2"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`.
2. Done when: the callable automation "Pipeline Factory · Clear Gate 2" is saved, compiled clean, with exactly this contract: callable from the app; inputs draft_id (text), decision (text: approve \| hold), actor (text), origin (text); result result (text: approved \| blocked \| already_enrolled \| held), rule (text), reason (text). Runs the Send Rules Check before an approve: the sender's pod must be the account's pod; the person not on DNC, not in another sequence, not held out; Patch ID, AE and pod present; a planted_error draft is always blocked and counted as caught. A blocked draft gets rules_check blocked and rules_reason; an approved draft is enrolled once (Outreach Launcher, mocked: status enrolled, enrolment_key account_id + person_id + play_id, "queued for Apollo sequence (mocked)"); an approve of an enrolled draft answers already_enrolled and writes nothing. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: make your own rows with origin \`test\` and unique ids that start \`T-\` (a test account, person, draft or component as the case needs, copied in shape from a seed row), run each result path the line names at least once, read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave the T- rows in place (Pipeline Factory · Reset demo clears origin test rows) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is seed or user; never test against the story row A-1001 or any other seeded row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Clear Gate 2; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae840d7f6f76639f8ceb67d"}
Read back: Pipeline Factory · Clear Gate 2 6ae840d7f6f76639f8ceb67d: search_workflows now answers version 1, deployment null, 36 nodes — the same version tested and scored
Read back: Pipeline Factory · Clear Gate 2 6ae840d7f6f76639f8ceb67d: search_workflows found no automation of that name before the build; compile_and_save_workflow created it (version 0), saved version 1 is the latest; open_workflow version 1, deployment null (not deployed, as the task says)
Read back: Pipeline Factory · Clear Gate 2: open_workflow trigger CALLABLE callables/callables_from_automation; setup draft_id (string), decision (string enum approve\|hold), actor (string), origin (string); result result (string enum approved\|blocked\|already_enrolled\|held), rule (string), reason (string), all three required
Read back: Pipeline Factory · Clear Gate 2: describe_callable_workflow returned 4 parameters draft_id, decision, actor, origin, all string
Read back: Pipeline Factory · Clear Gate 2 run 6ae841879594aa458cb9c0f7 (T-D1 approve): COMPLETED, {result: approved, rule: '', reason: 'queued for Apollo sequence (mocked)'}; get_records T-D1 status enrolled, rules_check passed, enrolment_key 'T-A1\|T-P1\|T-PLAY'
Read back: Pipeline Factory · Clear Gate 2 run 6ae841929ec43c6ee2de5e72 (T-D1 approve again): COMPLETED, {result: already_enrolled, rule: 'one enrolment per person and play', reason: 'already enrolled under T-A1\|T-P1\|T-PLAY'}; the run reached the return with no update node, and get_records T-D1 still version 1
Read back: Pipeline Factory · Clear Gate 2 run 6ae84188f6f76639f8ced1b4 (T-D2 planted_error true): COMPLETED, {result: blocked, rule: planted_error, reason: 'planted test error caught'}; get_records T-D2 rules_check blocked, rules_reason 'planted test error caught', status blocked
Read back: Pipeline Factory · Clear Gate 2 run 6ae84189f38e327618fc7c3c (T-D3 sender_pod T-POD-2, account pod T-POD-1): COMPLETED, {result: blocked, rule: sender_pod}; get_records T-D3 rules_check blocked
Read back: Pipeline Factory · Clear Gate 2 run 6ae8418af38e327618fc7c65 (T-D4, person T-P3 dnc true): COMPLETED, {result: blocked, rule: dnc, reason: 'person is on the do-not-contact list'}; get_records T-D4 rules_check blocked
Read back: Pipeline Factory · Clear Gate 2 run 6ae841939ec43c6ee2de5e87 (T-D5 hold): COMPLETED, {result: held, rule: '', reason: 'held at Gate 2 by T BDR One'}; get_records T-D5 status held, rules_check pending
Read back: Pipeline Factory · Clear Gate 2 run 6ae8418b9ec43c6ee2de5dd6 (blank payload {}): COMPLETED, {result: blocked, rule: input, reason: 'draft_id is required'}
Read back: Pipeline Factory · Clear Gate 2: best practice 95 (83 of 85 checks) after 1 fix round, first read 89, version 1
Read back: Pipeline Factory · Clear Gate 2 security: the Send Rules Check re-reads the draft, account and person from storage in the same run and branches on what it read, never on a caller flag; writes set only status, rules_check, rules_reason and enrolment_key by the draft's record id
Unverified: Pipeline Factory · Clear Gate 2: the other-sequence, held-out and missing Patch ID/AE/pod rules were not run on their own rows (blocked was proved through planted_error, sender_pod and dnc). Check: one approve run each on a test draft whose person has in_other_sequence true, and whose account has factory_holdout true or no patch_id
Note: assumed: Send Rules Check order planted_error, Patch ID/AE/pod present, sender pod, DNC, other sequence, held out; the first rule broken is the answer's rule
Note: assumed: a hold, or an approve, of a draft already enrolled (or of any draft whose account\|person\|play key is enrolled) answers already_enrolled and writes nothing
Note: assumed: an unknown decision or a blank draft_id answers blocked with rule 'input'; an unknown draft_id answers blocked with rule 'draft'
Note: assumed: 'counted as caught' is the draft's rules_reason 'planted test error caught' with rules_check blocked; PF Draft has no counter field
Note: assumed: the approve path writes status enrolled straight away (Outreach Launcher mocked) and puts 'queued for Apollo sequence (mocked)' in rules_reason and in the answer's reason
Note: The origin input is accepted but unused: Clear Gate 2 creates no rows, it only updates the draft
Note: handover: Clear Gate 2 workflowId 6ae840d7f6f76639f8ceb67d; enrolment_key format is '&lt;account_id&gt;\|&lt;person_id&gt;\|&lt;play_id&gt;' (same as Save hand-off's idempotency_key)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_pzz43, n_6q0j6, n_0bjyt, n_czgso) · needs object indexes on OBJ_pf_draft (draft_id; enrolment_key+status), OBJ_pf_account (account_id), OBJ_pf_person (person_id) outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_1fkhg, n_z4z40, n_xj8kv) · fix would change behaviour: these are the draft writes; their success output is not part of the answer
Note: test rows left for Reset demo: PF Draft (OBJ_pf_draft) T-D1, T-D2, T-D3, T-D4, T-D5; PF Person (OBJ_pf_person) T-P1, T-P3, T-P4, T-P5, T-P6; PF Account (OBJ_pf_account) T-A1 (all origin test)
Note: No delete call made, per the person's answer: 'This is an unattended run: no person can answer a delete, so make no delete call and do not report declined.' Not deployed: the deploy task does.

### t8 · Deploy Pipeline Factory · Clear Gate 2

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Clear Gate 2" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Clear Gate 2" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Clear Gate 2".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Clear Gate 2 deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae840d7f6f76639f8ceb67d"}
Read back: Pipeline Factory · Clear Gate 2 6ae840d7f6f76639f8ceb67d: open_workflow before deploy answered version 1, deployment null — the version t7 tested and scored
Read back: Pipeline Factory · Clear Gate 2: deploy_workflow returned ok:true, 'Deployed version 1 of automation 6ae840d7f6f76639f8ceb67d.', paused false, storedVersion 1
Read back: Pipeline Factory · Clear Gate 2: search_workflows deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 1, deployedAt: 1793606356302, savedAfterDeploy: false} — definitionVersion 1 equals the saved version
Read back: Pipeline Factory · Clear Gate 2: best practice 95 (83 of 85 checks), version 1, read once
Note: deploymentNotes 'Demo Studio · Pipeline Factory v1 · Pipeline Factory · Clear Gate 2'. Answer from the person: yes, deploy Pipeline Factory · Clear Gate 2. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_pzz43, n_6q0j6, n_0bjyt, n_czgso) · score already 90 or more
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_1fkhg, n_z4z40, n_xj8kv) · score already 90 or more
Note: Finding for the router: Clear Gate 2's Send Rules Check is a branch with overlapping arms; the platform runs every true arm in parallel, so a draft breaking two rules is still blocked but the answer's rule/rules_reason may name either rule, not the first. A fix is a change to Clear Gate 2, outside this task.

### t9 · Build Pipeline Factory · Book meeting

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Book meeting"; it must not exist (stop and report if it does). Read each PF object this automation reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`. It calls "Pipeline Factory · Save hand-off" (deployed; its workflowId from \`search_workflows\`) for every hand-off it saves, never writing PF Hand-off itself.
2. Done when: the callable automation "Pipeline Factory · Book meeting" is saved, compiled clean, with exactly this contract: callable from the app; inputs account_id (text), action (text: book \| correct), field (text), new_value (text), reason (text), actor_role (text), origin (text); result result (text: booked \| locked \| corrected), locked_fields (text), reason (text). book sets deal_stage engage, meeting_type intro, meeting_source "factory: AE booking link", factory_sourced true, factory_influenced true, locked_at now, and saves a Meeting Handoff hand-off through Save hand-off. correct on a locked field (patch_id, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced) answers locked "Locked at booking: corrections go through RevOps with a reason" unless actor_role is revops and reason is given, then corrected and logged. Inputs and result fields keep the names and types the line gives; every result field is set on every path; the start trigger is \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms; an update of a row by its key writes with \`upsert\` only where the line creates the row. Every row it creates carries the \`origin\` input when the line has one (default \`user\`), else origin \`user\`.
3. Test it with bounded test runs on the saved draft: make your own rows with origin \`test\` and unique ids that start \`T-\` (a test account, person, draft or component as the case needs, copied in shape from a seed row), run each result path the line names at least once, read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave the T- rows in place (Pipeline Factory · Reset demo clears origin test rows) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is seed or user; never test against the story row A-1001 or any other seeded row.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Book meeting; test runs on origin test rows answer each result path.
Result IDs: {"entity":"6ae84449f38e327618fcc640"}
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: search_workflows found no automation of that name before the build; created at version 0, saved version 1 is the latest (not deployed)
Read back: Pipeline Factory · Book meeting: trigger CALLABLE callables/callables_from_automation; setup account_id, action (enum book\|correct), field, new_value, reason, actor_role, origin (all string); result result (enum booked\|locked\|corrected), locked_fields (string), reason (string), all required; describe_callable_workflow returned the same 7 parameters
Read back: Pipeline Factory · Book meeting run 6ae8458ff13e536c52c65bd7 (v1, blank {}): {result: locked, locked_fields: 'patch_id, bdr_of_record, meeting_type, meeting_source, factory_sourced, factory_influenced, marketing_influenced', reason: 'account_id and an action of book or correct are required; nothing changed'}
Read back: Pipeline Factory · Book meeting run 6ae84591fbdd550a9a45b28f (book T-A30): {result: booked, reason: 'booked: deal stage engage, intro meeting; Meeting Handoff saved H-6ae84591fbdd550a9a45b2a0'}; get_records T-A30 deal_stage engage, meeting_type intro, meeting_source 'factory: AE booking link', factory_influenced true, locked_at 1793607057971; PF Hand-off H-6ae84591fbdd550a9a45b2a0 'Meeting Handoff and Deadlines' → 'Meeting Prep Writer', record_type meeting, flowed
Read back: Pipeline Factory · Book meeting run 6ae8459b2099302ffb1371ac (book T-A30 again): {result: booked, reason: 'already booked; booking fields locked'}, no write node ran
Read back: Pipeline Factory · Book meeting run 6ae845982099302ffb13718d (correct patch_id by bdr, no reason): {result: locked, reason: 'Locked at booking: corrections go through RevOps with a reason'}; get_records T-A30 patch_id still T-PATCH-1
Read back: Pipeline Factory · Book meeting run 6ae8459af13e536c52c65fb4 (correct factory_sourced=false by revops with reason): {result: corrected, reason: 'factory_sourced corrected to false; logged as hand-off H-6ae8459af13e536c52c65fc7'}; get_records T-A30 factory_sourced false (boolean); PF Hand-off H-6ae8459af13e536c52c65fc7 record_type correction, evidence 'correction by revops: meeting came from a partner referral'
Read back: Pipeline Factory · Book meeting: best practice 88 (82 of 85 checks) after 1 fix round, first read 85, version 1
Read back: Pipeline Factory · Book meeting security: re-reads the account and its locked_at in the same run; corrects only the seven named booking fields; the correction log goes through Save hand-off
Unverified: Pipeline Factory · Book meeting: a text-field correction (e.g. meeting_source) by revops was not run; only the yes/no path was. Check: one correct run with field meeting_source, actor_role revops and a reason
Note: assumed: refusals (blank account, unknown action, unknown account, a field outside the seven booking fields) answer result locked with a reason saying nothing changed (the result enum has no error value)
Note: assumed: before booking (no locked_at) the booking fields are not locked yet and anyone may correct them; after booking only actor_role 'revops' with a non-blank reason may
Note: assumed: 'logged' = a PF Hand-off record_type 'correction' from 'Meeting Handoff and Deadlines' to 'Meeting Prep Writer' through Save hand-off, play_id 'correction:&lt;executionId&gt;' so each correction is its own row; a second book is idempotent (answers booked, writes nothing)
Note: assumed: booking also writes nothing to meeting_label or marketing_influenced; yes/no fields are written as the strings 'true'/'false', which the store saved as booleans (read back factory_sourced false)
Note: Version 1 replaced the yes/no-field branch (its two arms overlapped and both ran, best practice CHECK_72) with if/else
Note: handover: Book meeting workflowId 6ae84449f38e327618fcc640
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Call automation x2 (n_2h9q2, n_762el, n_kbscr) · fix would change behaviour: the check flags nodes carrying the contract field account_id (Clear Gate 2, whose contract has no account_id, passes it); renaming contract fields is not allowed and the DSL has no node I/O visibility option
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_vakk5) · needs an object index on OBJ_pf_account (account_id) outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_12gpu, n_25fk6, n_8g3mt, n_hhkdo) · fix would change behaviour: these are the booking and correction writes
Note: test rows left for Reset demo: PF Account (OBJ_pf_account) T-A30
Note: test rows left (origin user, made through Save hand-off; Reset demo will not clear them): PF Hand-off H-6ae84591fbdd550a9a45b2a0, H-6ae8459af13e536c52c65fc7 (T-A30)

### t10 · Deploy Pipeline Factory · Book meeting

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Book meeting" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Book meeting" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · Pipeline Factory · Book meeting".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Book meeting deployed with definitionVersion equal to the saved version.
Result IDs: {"entity":"6ae84449f38e327618fcc640"}
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: search_workflows before deploy showed version 1 (the version t9 saved), deployment null
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: deploy_workflow answered ok:true, workflowVersion 1, deployedVersion 1, paused false, storedVersion 1, 'Deployed version 1 of automation 6ae84449f38e327618fcc640.'
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: search_workflows after deploy: deployment {status: DEPLOYED, deployedVersion: 1, definitionVersion: 1, deployedAt: 1793607304149, savedAfterDeploy: false}; definitionVersion 1 equals the saved version 1
Read back: Pipeline Factory · Book meeting: best practice 88 (82 of 85 checks), version 1, read once; no fix round (deploy-only task)
Unverified: Pipeline Factory · Book meeting: the plan tag the bridge appends to deploymentNotes was not shown by any read; check the tenant's deployment history for the notes 'Demo Studio · Pipeline Factory v1 · Pipeline Factory · Book meeting [nebula plan e_6ae83fd1afe7fc590a161a7f]'
Note: Deployed on the plan's approval: the spec the person accepted names Pipeline Factory · Book meeting under Ready when.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Call automation (n_762el, n_kbscr) · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_vakk5) · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_12gpu, n_25fk6, n_8g3mt, n_hhkdo) · task does not save

