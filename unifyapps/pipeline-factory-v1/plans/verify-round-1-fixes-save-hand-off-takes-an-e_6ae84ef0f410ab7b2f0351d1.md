---
nebula: 3
specId: "e_6ae84eedf410ab7b2f035198"
mode: "sonic"
title: "Verify round 1 fixes: Save hand-off takes an origin input and its callers pass theirs; Log signal sets due_at; Clear Gat"
owner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save hand-off","id":"6ae840a5fbdd550a9a44c524"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Log signal","id":"6ae843cc9594aa458cba14d7"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Decide Gate 1","id":"6ae8440df13e536c52c5d959"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Book meeting","id":"6ae84449f38e327618fcc640"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Clear Gate 2","id":"6ae840d7f6f76639f8ceb67d"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Save hand-off","id":"6ae840a5fbdd550a9a44c524"},{"kind":"automation","name":"Pipeline Factory · Log signal","id":"6ae843cc9594aa458cba14d7"},{"kind":"automation","name":"Pipeline Factory · Decide Gate 1","id":"6ae8440df13e536c52c5d959"},{"kind":"automation","name":"Pipeline Factory · Book meeting","id":"6ae84449f38e327618fcc640"},{"kind":"automation","name":"Pipeline Factory · Clear Gate 2","id":"6ae840d7f6f76639f8ceb67d"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "2c7ab9ab-9f03-4d53-9106-b0291cf84cd7"
pageDesign: 2
createdAt: "2026-11-02T08:50:55.714Z"
runningAt: "2026-11-02T08:50:59.421Z"
runner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"8da1d8cb-cc02-5ac8-85df-da01be5fab51"}
---
<!-- nebula:status -->
## Status
Finished. Remaining optional work was skipped.
<!-- /nebula:status -->

## Plan

Goal: Verify round 1 fixes: Save hand-off takes an origin input and its callers pass theirs; Log signal sets due_at; Clear Gat

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Save hand-off |  | done | 1 |
| t2 | deploy | Pipeline Factory · Save hand-off | t1 | done | 1 |
| t3 | automation | Pipeline Factory · Log signal | t2 | skipped | 0 |
| t4 | deploy | Pipeline Factory · Log signal | t3 | skipped | 0 |
| t5 | automation | Pipeline Factory · Decide Gate 1 | t2 | done | 1 |
| t6 | deploy | Pipeline Factory · Decide Gate 1 | t5 | done | 1 |
| t7 | automation | Pipeline Factory · Book meeting | t2 | done | 1 |
| t8 | deploy | Pipeline Factory · Book meeting | t7 | done | 1 |
| t9 | automation | Pipeline Factory · Clear Gate 2 |  | done | 1 |
| t10 | deploy | Pipeline Factory · Clear Gate 2 | t9 | done | 1 |

### t1 · Fix Pipeline Factory · Save hand-off

Body:
1. Read: \`open_workflow\` on \`6ae840a5fbdd550a9a44c524\` ("Pipeline Factory · Save hand-off", deployed) for its code, saved version and \`setup\`/\`result\` schema, and \`search_workflows\` for its deployment.
2. Done when: the saved automation does this verify fix and nothing else: takes an origin input and writes it on the hand-off (default user), so a walk with origin test leaves no origin-user hand-off; nothing else changes (its callers are changed by the tasks that follow). Every other input, result field and path keeps its current behaviour.
3. Save with \`compile_and_save_workflow\` on \`6ae840a5fbdd550a9a44c524\`, then test-run the changed path and one unchanged path on the saved draft with origin \`test\` rows and read the effects back with \`get_records\`. Make no delete call yourself (this run is unattended and no person can confirm one): tests use rows with origin \`test\` and ids starting \`T-\`, left for Reset demo.
4. Read back: \`open_workflow\` for the new saved version (higher than the one step 1 read) and its schema, the test runs' \`inspect_workflow_run\` output, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows a higher saved version of Pipeline Factory · Save hand-off with the fix; test runs read back.
Result IDs: {"entity":"6ae840a5fbdd550a9a44c524"}
Read back: Pipeline Factory · Save hand-off 6ae840a5fbdd550a9a44c524: open_workflow version 3 (step 1 read version 2); deployment definitionVersion 2, savedAfterDeploy true (not deployed, as the task says)
Read back: Pipeline Factory · Save hand-off: setup now declares origin {type string, title Origin, enum [user, seed, test]}; result schema unchanged (result, handoff_id, reason)
Read back: Pipeline Factory · Save hand-off: saved code line 232 \`origin: "user"\` (default), lines 236-244 take t.origin when it is test or seed, and all three create_record nodes write \`origin: &lt;that variable&gt;.origin\` (lines 371, 452, 493) in place of the hard-coded "user"
Read back: Pipeline Factory · Save hand-off test run 6ae84fde2099302ffb14d3b2 (changed path, origin test, C30 -&gt; Fact Checker): COMPLETED, response {result: saved, handoff_id: H-6ae84fde2099302ffb14d3b2, reason: flowed on}; get_records shows H-6ae84fde2099302ffb14d3b2 status flowed, origin test
Read back: Pipeline Factory · Save hand-off test run 6ae850102099302ffb14d9d8 (waiting path, origin test, confidence 50 -&gt; Message Grader 75): COMPLETED, {result: waiting_person, reason: confidence 50 under 75.0}; get_records shows H-6ae850102099302ffb14d9d8 status waiting_person, assigned_to 'one rewrite, then a person at Gate 2', origin test
Read back: Pipeline Factory · Save hand-off test run 6ae8500f9594aa458cbc22cd (unchanged duplicate path, same key again): COMPLETED, {result: duplicate, handoff_id: H-6ae84fde2099302ffb14d3b2, reason: already saved under T-A-01\|T-P-01\|T-PLAY-01}; get_records on account_id T-A-0* shows 2 rows, both origin test, no origin-user row
Read back: Pipeline Factory · Save hand-off test run 6ae84fe0fbdd550a9a475f52 (all-blank {}): COMPLETED, {result: rejected, handoff_id: '', reason: not registered}, no write
Read back: Pipeline Factory · Save hand-off: best practice 82 (81 of 85 checks), under 90, no fix round saved (the one attempted fix was refused by the compiler twice, nothing saved), version 3
Read back: Security: rule 4 (only needed fields) — the write sets origin only from the allowed values test/seed, anything else falls back to user
Unverified: Pipeline Factory · Save hand-off: the default (no origin, or an unknown value) writing origin user was not run, to avoid leaving an origin-user hand-off; config shows the variable starts as "user". Check: a run with origin omitted on a disposable pair, then get_records on its handoff_id
Note: assumed: an origin other than test or seed (including blank or a typo) is written as user rather than rejected, so callers that send nothing keep today's behaviour
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create record (n_8vnws, n_53la3, n_mfimt) · nodes not changed by this task beyond the origin value; no DSL node option turns node input/output visibility off, and renaming the flagged fields would change the contract
Note: best practice exception: CHECK_59 Limit multiple variable definitions except for branches · Create variables (n_t08z9, n_xfeac) · merging origin into the existing create_variables node was refused by compile_and_save_workflow (UNKNOWN_INPUT_KEY 'origin' ... Known properties: 'missing_field') on 2 tries; nothing saved
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_utr12, n_6ntkv, n_4fkhh, n_o04rw) · needs indexes on OBJ_pf_component and OBJ_pf_handoff outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create record (n_8vnws, n_53la3, n_mfimt) · fix would change behaviour (the writes are the automation's purpose)
Note: The 'Find the first missing schema field' BRANCH in Save hand-off runs every matching arm in parallel (same platform behaviour that broke Clear Gate 2), so with two schema fields missing the reported field is whichever arm writes last; not changed here since the task allows only the origin fix
Note: Test rows left for Reset demo (no delete made): OBJ_pf_handoff H-6ae84fde2099302ffb14d3b2, H-6ae850102099302ffb14d9d8, both origin test
Note: handover: Save hand-off v3 setup takes \`origin\` (string, enum user\|seed\|test); callers pass origin: t.origin; anything other than test or seed is saved as user
Note: feedback:
Bug: compile_and_save_workflow refuses a new variable key added to an existing variable_by_unifyapps_create_variables node, so two Create Variables nodes cannot be merged into one.
Context: Editing Pipeline Factory · Save hand-off (v3) to clear CHECK_59 by adding origin beside missing_field in existing node n_t08z9; the DSL prompt says create_variables takes a free name-to-value map.
Where: mcp-tool
Evidence: UNKNOWN_INPUT_KEY "'origin' does not exist in type 'Inputs of variable_by_unifyapps::variable_by_unifyapps_create_variables'. Known properties: 'missing_field'"; renaming the const matched the same node id and gave the same findings.
Cause: Suspected: the compiler takes the existing node's saved inputs as its input contract instead of treating create_variables as an open map.
Regression: add a second key to an existing create_variables statement and save; it should compile and the node should output both keys.

### t2 · Deploy Pipeline Factory · Save hand-off

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Save hand-off" and the version the automation task saved (Built so far).
2. Done when: "Pipeline Factory · Save hand-off" is deployed with \`definitionVersion\` equal to that saved version.
3. Apply \`deploy_workflow\` once on \`6ae840a5fbdd550a9a44c524\` with deploymentNotes "Demo Studio · verify round 1 fix · Pipeline Factory · Save hand-off".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Save hand-off deployed at the fixed version.
Result IDs: {"entity":"6ae840a5fbdd550a9a44c524"}
Read back: Pipeline Factory · Save hand-off 6ae840a5fbdd550a9a44c524: deploy_workflow returned ok:true, workflowVersion 3, deployedVersion 2, paused false, storedVersion 3
Read back: Pipeline Factory · Save hand-off: search_workflows deployment {status: DEPLOYED, deployedVersion: 2, definitionVersion: 3, deployedAt: 1793609875967, savedAfterDeploy: false}; definitionVersion 3 = the version t1 saved and tested
Read back: Pipeline Factory · Save hand-off: best practice 82 (81 of 85 checks), read by t1 on version 3, the version deployed
Note: Answer from the person: yes, deploy Pipeline Factory · Save hand-off. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create record · task does not save
Note: best practice exception: CHECK_59 Limit multiple variable definitions except for branches · Create variables · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create record · task does not save

### t3 · Fix Pipeline Factory · Log signal

Body:
1. Read: \`open_workflow\` on \`6ae843cc9594aa458cba14d7\` ("Pipeline Factory · Log signal", deployed) for its code, saved version and \`setup\`/\`result\` schema, and \`search_workflows\` for its deployment.
2. Done when: the saved automation does this verify fix and nothing else: it passes its own origin input to Save hand-off's new origin input, and the fast-lane hand-off sets the due_at field to saved_at plus one hour (today it sits only inside payload, so the Hand-offs drawer shows a dash for due); nothing else changes. Every other input, result field and path keeps its current behaviour.
3. Save with \`compile_and_save_workflow\` on \`6ae843cc9594aa458cba14d7\`, then test-run the changed path and one unchanged path on the saved draft with origin \`test\` rows and read the effects back with \`get_records\`. Make no delete call yourself (this run is unattended and no person can confirm one): tests use rows with origin \`test\` and ids starting \`T-\`, left for Reset demo.
4. Read back: \`open_workflow\` for the new saved version (higher than the one step 1 read) and its schema, the test runs' \`inspect_workflow_run\` output, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows a higher saved version of Pipeline Factory · Log signal with the fix; test runs read back.
Error: moved to its own change: Save hand-off needs a due_at input first (its only writer)

### t4 · Deploy Pipeline Factory · Log signal

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Log signal" and the version the automation task saved (Built so far).
2. Done when: "Pipeline Factory · Log signal" is deployed with \`definitionVersion\` equal to that saved version.
3. Apply \`deploy_workflow\` once on \`6ae843cc9594aa458cba14d7\` with deploymentNotes "Demo Studio · verify round 1 fix · Pipeline Factory · Log signal".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Log signal deployed at the fixed version.
Error: skipped: depends on t3

### t5 · Fix Pipeline Factory · Decide Gate 1

Body:
1. Read: \`open_workflow\` on \`6ae8440df13e536c52c5d959\` ("Pipeline Factory · Decide Gate 1", deployed) for its code, saved version and \`setup\`/\`result\` schema, and \`search_workflows\` for its deployment.
2. Done when: the saved automation does this verify fix and nothing else: it passes its own origin input to Save hand-off's new origin input on every hand-off it saves; nothing else changes. Every other input, result field and path keeps its current behaviour.
3. Save with \`compile_and_save_workflow\` on \`6ae8440df13e536c52c5d959\`, then test-run the changed path and one unchanged path on the saved draft with origin \`test\` rows and read the effects back with \`get_records\`. Make no delete call yourself (this run is unattended and no person can confirm one): tests use rows with origin \`test\` and ids starting \`T-\`, left for Reset demo.
4. Read back: \`open_workflow\` for the new saved version (higher than the one step 1 read) and its schema, the test runs' \`inspect_workflow_run\` output, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows a higher saved version of Pipeline Factory · Decide Gate 1 with the fix; test runs read back.
Result IDs: {"entity":"6ae8440df13e536c52c5d959"}
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: compile_and_save_workflow saved version 2 (step 1 read version 1); changes line 'changed 2 statements (lines 377, 398); nothing else moved'; search_workflows deployment definitionVersion 1, savedAfterDeploy true (not deployed, as the task says)
Read back: Pipeline Factory · Decide Gate 1: setup (account_id, decision accept\|reject, reason bad_fit\|active_deal\|wrong_timing\|in_conversation, origin) and result (result accepted\|rejected\|blocked, refill_account_id, reason) unchanged; both Save hand-off calls (Company Facts Collector, Buying Team Mapper) now pass \`origin: t.origin\`
Read back: Pipeline Factory · Decide Gate 1 test run 6ae850d8fbdd550a9a47a1ec (changed path, accept T-A-11, origin test): COMPLETED, {result: accepted, refill_account_id: '', reason: 'accepted; hand-offs: Company Facts Collector saved, Buying Team Mapper saved'}; get_records: H-6ae850d9fbdd550a9a47a218 (Gate 1 -&gt; Company Facts Collector) and H-6ae850dafbdd550a9a47a295 (Gate 1 -&gt; Buying Team Mapper) both origin test, status flowed; T-A-11 gate1_status accepted
Read back: Pipeline Factory · Decide Gate 1 test run 6ae850dd2099302ffb14facf (unchanged reject path, T-A-12 bad_fit): COMPLETED, {result: rejected, reason: 'rejected: bad_fit; no queued account left in patch T-PATCH-01'}; get_records T-A-12 gate1_status rejected, gate1_reason bad_fit; no hand-off row for T-A-12
Read back: Pipeline Factory · Decide Gate 1: best practice 67 (81 of 85 checks), under 90, no fix round (every failing check is outside this task or would change behaviour), version 2
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Respond to automation (n_me1f2, n_dk6h2, n_f4noe, n_57n94, n_2y213, n_22kfy, n_vi51h, n_qr8y9, n_qb3hq), Call automation (n_7ld0t, n_wzm03) · no DSL option turns node input/output visibility off; renaming the flagged fields would change the contract
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_uxpxc, n_vo43y, n_co0k2) · needs indexes on OBJ_pf_account and OBJ_pf_patch outside the task
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition (n_1ban7, n_odvh9) · nodes not changed by this task; a BRANCH also runs every matching arm in parallel on this platform (seen in Clear Gate 2), so the swap would change behaviour
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_jvl59, n_lyt8t, n_axd0o, n_5zxn6, n_rachq) · fix would change behaviour
Note: Test rows left for Reset demo (no delete made): OBJ_pf_account T-A-11, T-A-12 (patch T-PATCH-01, which has no patch row, so no seed patch slots changed); OBJ_pf_handoff H-6ae850d9fbdd550a9a47a218, H-6ae850dafbdd550a9a47a295, origin test

### t6 · Deploy Pipeline Factory · Decide Gate 1

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Decide Gate 1" and the version the automation task saved (Built so far).
2. Done when: "Pipeline Factory · Decide Gate 1" is deployed with \`definitionVersion\` equal to that saved version.
3. Apply \`deploy_workflow\` once on \`6ae8440df13e536c52c5d959\` with deploymentNotes "Demo Studio · verify round 1 fix · Pipeline Factory · Decide Gate 1".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Decide Gate 1 deployed at the fixed version.
Result IDs: {"entity":"6ae8440df13e536c52c5d959"}
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: before deploy search_workflows version 2, deployment {status DEPLOYED, deployedVersion 1, definitionVersion 1, savedAfterDeploy true}; saved version 2 matches t5's save
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: deploy_workflow returned ok:true, workflowVersion 2, storedVersion 2, paused false, 'Deployed version 2 of automation 6ae8440df13e536c52c5d959.'
Read back: Pipeline Factory · Decide Gate 1 6ae8440df13e536c52c5d959: after deploy search_workflows deployment {status: DEPLOYED, deployedVersion: 2, definitionVersion: 2, deployedAt: 1793610080855, savedAfterDeploy: false}
Read back: Pipeline Factory · Decide Gate 1: best practice 67 (81 of 85 checks), deploy-only task, no fix round, version 2
Note: Deploy approval: the accepted spec names Pipeline Factory · Decide Gate 1 under Ready when (plan approval, not a separate answer to this call).
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Respond to automation (x8), Call workflow n_7ld0t, n_wzm03 · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records n_uxpxc, n_vo43y, n_co0k2 · task does not save
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition n_1ban7, n_odvh9 · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields n_jvl59, n_lyt8t, n_axd0o, n_5zxn6, n_rachq · task does not save

### t7 · Fix Pipeline Factory · Book meeting

Body:
1. Read: \`open_workflow\` on \`6ae84449f38e327618fcc640\` ("Pipeline Factory · Book meeting", deployed) for its code, saved version and \`setup\`/\`result\` schema, and \`search_workflows\` for its deployment.
2. Done when: the saved automation does this verify fix and nothing else: it passes its own origin input to Save hand-off's new origin input on the Meeting Handoff hand-off; nothing else changes. Every other input, result field and path keeps its current behaviour.
3. Save with \`compile_and_save_workflow\` on \`6ae84449f38e327618fcc640\`, then test-run the changed path and one unchanged path on the saved draft with origin \`test\` rows and read the effects back with \`get_records\`. Make no delete call yourself (this run is unattended and no person can confirm one): tests use rows with origin \`test\` and ids starting \`T-\`, left for Reset demo.
4. Read back: \`open_workflow\` for the new saved version (higher than the one step 1 read) and its schema, the test runs' \`inspect_workflow_run\` output, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows a higher saved version of Pipeline Factory · Book meeting with the fix; test runs read back.
Result IDs: {"entity":"6ae84449f38e327618fcc640"}
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: compile_and_save_workflow saved version 2 (step 1 read version 1); changes line 'changed 1 statement (line 193); nothing else moved'; search_workflows deployment definitionVersion 1, savedAfterDeploy true (not deployed, as the task says)
Read back: Pipeline Factory · Book meeting: setup (account_id, action book\|correct, field, new_value, reason, actor_role, origin) and result (result booked\|locked\|corrected, locked_fields, reason) unchanged; the Meeting Handoff call node n_762el now passes origin '{{ n_2h9q2.outputs.origin }}'
Read back: Pipeline Factory · Book meeting test run 6ae850e29594aa458cbc46dc (changed path, book T-A-13, origin test): COMPLETED; call node input parameters.origin 'test', output {result: saved, handoff_id: H-6ae850e49594aa458cbc46e1}; response reason 'booked: deal stage engage, intro meeting; Meeting Handoff saved H-6ae850e49594aa458cbc46e1'; get_records H-6ae850e49594aa458cbc46e1 origin test, status flowed; T-A-13 deal_stage engage, meeting_type intro, locked_at 1793609956086
Read back: Pipeline Factory · Book meeting test run 6ae850edfbdd550a9a47a493 (unchanged already-booked path, T-A-13 again): COMPLETED, {result: booked, reason: 'already booked; booking fields locked'}, no second hand-off (get_records shows one row for T-A-13)
Read back: Pipeline Factory · Book meeting: best practice 88 (82 of 85 checks), under 90, no fix round (every failing check is outside this task or would change behaviour), version 2
Note: The correction hand-off ('Log the correction as a hand-off', action correct) still sends no origin, so it is saved as origin user; the task named only the Meeting Handoff hand-off. A test walk that corrects a field will still leave an origin-user hand-off
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Call automation (n_762el, n_kbscr) · no DSL option turns node input/output visibility off; renaming the flagged fields would change the contract
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_vakk5) · needs an index on OBJ_pf_account outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_12gpu, n_25fk6, n_8g3mt, n_hhkdo) · fix would change behaviour
Note: Test rows left for Reset demo (no delete made): OBJ_pf_account T-A-13, OBJ_pf_handoff H-6ae850e49594aa458cbc46e1, origin test

### t8 · Deploy Pipeline Factory · Book meeting

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Book meeting" and the version the automation task saved (Built so far).
2. Done when: "Pipeline Factory · Book meeting" is deployed with \`definitionVersion\` equal to that saved version.
3. Apply \`deploy_workflow\` once on \`6ae84449f38e327618fcc640\` with deploymentNotes "Demo Studio · verify round 1 fix · Pipeline Factory · Book meeting".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Book meeting deployed at the fixed version.
Result IDs: {"entity":"6ae84449f38e327618fcc640"}
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: before deploy search_workflows version 2, deployment {status DEPLOYED, deployedVersion 1, definitionVersion 1, savedAfterDeploy true}; saved version 2 matches t7's save
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: deploy_workflow returned ok:true, workflowVersion 2, storedVersion 2, paused false, 'Deployed version 2 of automation 6ae84449f38e327618fcc640.'
Read back: Pipeline Factory · Book meeting 6ae84449f38e327618fcc640: after deploy search_workflows deployment {status: DEPLOYED, deployedVersion: 2, definitionVersion: 2, deployedAt: 1793610083173, savedAfterDeploy: false}
Read back: Pipeline Factory · Book meeting: best practice 88 (82 of 85 checks), deploy-only task, no fix round, version 2
Note: Deploy approval: the accepted spec names Pipeline Factory · Book meeting under Ready when (plan approval, not a separate answer to this call).
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation n_2h9q2, Call workflow n_762el, n_kbscr · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records n_vakk5 · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields n_12gpu, n_25fk6, n_8g3mt, n_hhkdo · task does not save

### t9 · Fix Pipeline Factory · Clear Gate 2

Body:
1. Read: \`open_workflow\` on \`6ae840d7f6f76639f8ceb67d\` ("Pipeline Factory · Clear Gate 2", deployed) for its code, saved version and \`setup\`/\`result\` schema, and \`search_workflows\` for its deployment.
2. Done when: the saved automation does this verify fix and nothing else: approving D-04 answers result blocked, rule pod, reason "Blocked: sender Rhea Castillo is not in the account's pod (POD-NAE-1)" (today rule planted_error, reason "planted test error caught", both branch arms run); the planted-error count stays; nothing else changes. The Send Rules Check evaluates its rules in order (pod, DNC, other sequence, held out, Patch ID/AE/pod present, planted error) with if / else-if, so exactly one arm runs and the first failing rule is the one reported; a planted_error draft is still always blocked and counted as caught. Every other input, result field and path keeps its current behaviour.
3. Save with \`compile_and_save_workflow\` on \`6ae840d7f6f76639f8ceb67d\`, then test-run the changed path and one unchanged path on the saved draft with origin \`test\` rows and read the effects back with \`get_records\`. Make no delete call yourself (this run is unattended and no person can confirm one): tests use rows with origin \`test\` and ids starting \`T-\`, left for Reset demo.
4. Read back: \`open_workflow\` for the new saved version (higher than the one step 1 read) and its schema, the test runs' \`inspect_workflow_run\` output, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows a higher saved version of Pipeline Factory · Clear Gate 2 with the fix; test runs read back.
Result IDs: {"entity":"6ae840d7f6f76639f8ceb67d"}
Read back: Pipeline Factory · Clear Gate 2 6ae840d7f6f76639f8ceb67d: open_workflow version 2 (step 1 read version 1); deployment definitionVersion 1, savedAfterDeploy true (not deployed, as the task says); shape now IF_ELSE×12, no BRANCH
Read back: Pipeline Factory · Clear Gate 2: setup (draft_id, decision approve\|hold, actor, origin) and result (result approved\|blocked\|already_enrolled\|held, rule, reason) unchanged
Read back: Pipeline Factory · Clear Gate 2: saved code line 252 'Send Rules Check, rule 1: sender in the account's pod?' sets rule "pod" and reason \`Blocked: sender ${draft.sender} is not in the account's pod (${account.pod})\`; else-if chain DNC, other sequence, held out, Patch ID/AE/pod missing, then line 349 rule 6 planted test error
Read back: Pipeline Factory · Clear Gate 2 test run 6ae84fc39ec43c6ee20c8512 (approve T-D-04, copy of D-04: sender Rhea Castillo POD-NAE-2, planted_error true, account A-1001 POD-NAE-1): COMPLETED, response {result: blocked, rule: pod, reason: "Blocked: sender Rhea Castillo is not in the account's pod (POD-NAE-1)"}; exactly one Update variables node ran (n_duwi7); get_records T-D-04 status blocked, rules_check blocked, rules_reason "Blocked: sender Rhea Castillo is not in the account's pod (POD-NAE-1)", planted_error true
Read back: Pipeline Factory · Clear Gate 2 test run 6ae84fc6f38e327618fe5b88 (approve T-D-07, planted error only): COMPLETED, {result: blocked, rule: planted_error, reason: planted test error caught}; get_records T-D-07 status blocked, rules_check blocked, rules_reason 'planted test error caught'
Read back: Pipeline Factory · Clear Gate 2 test run 6ae84fc917ec564d96f82b3e (unchanged approve path, clean T-D-08): COMPLETED, {result: approved, rule: '', reason: queued for Apollo sequence (mocked)}; get_records T-D-08 status enrolled, rules_check passed, enrolment_key A-1001\|T-P-08\|PLAY-SIG-NEWLEADER
Read back: Pipeline Factory · Clear Gate 2 test run 6ae84fcbf38e327618fe5cb1 (all-blank {}): COMPLETED, {result: blocked, rule: input, reason: draft_id is required}
Read back: Pipeline Factory · Clear Gate 2: best practice 92 (82 of 85 checks), no fix round needed, version 2
Read back: Security: rule 3 (rule checked where its state is stored) — the Send Rules Check still reads the draft, account and person in the same run before blocking or enrolling
Unverified: Pipeline Factory · Clear Gate 2: 'the planted-error count stays' was not read on its consumer; planted drafts keep planted_error true and are always blocked (T-D-04, T-D-07 above), but D-04 now reports rule pod rather than planted_error. Check: read the planted-error/catch-rate count on the page or Read factory records after a Gate 2 walk and confirm it counts planted_error drafts that are blocked, not rule = planted_error
Unverified: Pipeline Factory · Clear Gate 2: hold path and the DNC/other-sequence/held-out/missing-pod arms were not re-run on v2. Check: approve a test draft on P-1008 (in another sequence) and expect rule other_sequence
Note: assumed: the pod rule only fires when the account has a pod; an account with no pod falls through to the Patch ID/AE/pod-missing rule, so that path keeps its current answer (rule patch_ae_pod)
Note: assumed: only the pod rule's name and reason changed (sender_pod -&gt; pod, new reason text); the other rule names and reasons are as before
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition (n_n4twh, n_2pb75, n_hmtn0, n_smfks) · fix would change behaviour: the task asks for if / else-if because the BRANCH ran every matching arm in parallel
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_pzz43, n_6q0j6, n_0bjyt, n_czgso) · needs indexes on OBJ_pf_draft, OBJ_pf_account, OBJ_pf_person outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_1fkhg, n_z4z40, n_xj8kv) · fix would change behaviour (the updates are the automation's writes)
Note: Test rows left for Reset demo (no delete made): OBJ_pf_draft T-D-04 (blocked), T-D-07 (blocked), T-D-08 (enrolled, enrolment_key A-1001\|T-P-08\|PLAY-SIG-NEWLEADER), all origin test; seed D-04 untouched (status waiting_gate2)
Note: Read factory records 6ae843e69ec43c6ee2dec988 shows version 2 saved after deploy (someone else's save during this run); not touched by this task

### t10 · Deploy Pipeline Factory · Clear Gate 2

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Clear Gate 2" and the version the automation task saved (Built so far).
2. Done when: "Pipeline Factory · Clear Gate 2" is deployed with \`definitionVersion\` equal to that saved version.
3. Apply \`deploy_workflow\` once on \`6ae840d7f6f76639f8ceb67d\` with deploymentNotes "Demo Studio · verify round 1 fix · Pipeline Factory · Clear Gate 2".
4. Read back: \`search_workflows\` for its \`deployment\`, quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Clear Gate 2 deployed at the fixed version.
Result IDs: {"entity":"6ae840d7f6f76639f8ceb67d"}
Read back: Pipeline Factory · Clear Gate 2 6ae840d7f6f76639f8ceb67d: deploy_workflow returned ok:true, workflowVersion 2, deployedVersion 2, paused false, storedVersion 2
Read back: Pipeline Factory · Clear Gate 2: search_workflows deployment {status: DEPLOYED, deployedVersion: 2, definitionVersion: 2, deployedAt: 1793609877552, savedAfterDeploy: false}; definitionVersion 2 = the version t9 saved and tested
Read back: Pipeline Factory · Clear Gate 2: best practice 92 (82 of 85 checks), read by t9 on version 2, the version deployed
Note: Answer from the person: yes, deploy Pipeline Factory · Clear Gate 2. The spec the person accepted names it under Ready when, so it is already approved; do not ask again.
Note: best practice exception: CHECK_22 Instead of using nested Conditions, prefer using a single branch node · Condition · task does not save
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records · task does not save
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields · task does not save

