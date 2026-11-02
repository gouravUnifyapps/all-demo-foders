---
nebula: 3
specId: "e_6ae861aed96c5f6ba2341955"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P02"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read component inputs"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save agent output"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset agent runs"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset demo","id":"6ae8441df38e327618fcc13c"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Read component inputs"},{"kind":"automation","name":"Pipeline Factory · Save agent output"},{"kind":"automation","name":"Pipeline Factory · Reset agent runs"},{"kind":"automation","name":"Pipeline Factory · Reset demo","id":"6ae8441df38e327618fcc13c"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "ae211734-9205-4d9f-aef0-50963e53fd3e"
pageDesign: 2
createdAt: "2026-11-02T10:10:57.379Z"
runningAt: "2026-11-02T10:11:00.691Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P02

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Read component inputs |  | running | 1 |
| t2 | deploy | Pipeline Factory · Read component inputs | t1 | pending | 0 |
| t3 | automation | Pipeline Factory · Save agent output |  | running | 1 |
| t4 | deploy | Pipeline Factory · Save agent output | t3 | pending | 0 |
| t5 | automation | Pipeline Factory · Reset agent runs |  | running | 1 |
| t6 | deploy | Pipeline Factory · Reset agent runs | t5 | pending | 0 |
| t7 | automation | Pipeline Factory · Reset demo | t6 | pending | 0 |
| t8 | deploy | Pipeline Factory · Reset demo | t7 | pending | 0 |

### t1 · Build Pipeline Factory · Read component inputs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read component inputs"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Read component inputs: callable from the AI agents; inputs component_id (text, required), account_id (text), person_id (text), draft_id (text), patch_id (text); result component (text, JSON: the PF Component row with threshold, below_threshold_goes_to, feeds, writes, model_family, status), account (text, JSON), people (text, JSON), signals (text, JSON), facts (text, JSON), drafts (text, JSON), sources (text, JSON: PF Source rows of the account or person, plus rows with no account such as content assets and the handbook), handoffs_in (text, JSON: PF Hand-off rows whose to_component is this component's name, for the account when given), inboxes (text, JSON), suppression (text, JSON), recent_runs (text, JSON: the last 50 PF Component run rows, for the sw8 agents), reason (text). Read-only, deterministic, no model call; an account_id given as a name resolves to its account_id as Read factory records does; an unknown component_id answers reason "unknown component" and empty lists. Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Read component inputs; test runs with origin test answer each result path.

### t2 · Deploy Pipeline Factory · Read component inputs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read component inputs" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Read component inputs" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Read component inputs".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read component inputs deployed with definitionVersion equal to the saved version.

### t3 · Build Pipeline Factory · Save agent output

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Save agent output"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Save hand-off \`6ae840a5fbdd550a9a44c524\`.
2. Done when: automation · create · Pipeline Factory · Save agent output: callable from the AI agents; inputs component_id (text, required), account_id (text), person_id (text), play_id (text), draft_id (text), patch_id (text), output_type (text), summary (text), payload (text, JSON), confidence (number), evidence (text), evidence_tag (text: public \| hypothesis), model (text), origin (text); result result (text: saved \| waiting_person \| rejected \| duplicate \| paused), run_id (text), handoff_ids (text), reason (text). Deterministic, no model call. Reads the PF Component row: a paused component answers paused and writes nothing. Schema check: confidence 0 to 100, evidence and output_type present, patch_id taken from the account when not given; a failure saves a PF Component run with status rejected, assigned_to GTM engineer, reason "schema check failed: \`field\` missing", and nothing else. Idempotent on component_id + account_id + person_id + play_id + output_type: a re-run updates the same PF Component run row and answers duplicate, never a second row or a second hand-off. Under the component's threshold: the run is saved waiting_person, assigned_to its below_threshold_goes_to, and no field is written. At or over it: writes only the component's registered fields (one writer per field, from a fixed map: C02 PF Account.ultimate_parent_lock; C03 PF Account.hq_city; C06 PF Account.fit_score and fit_band; C11 PF Signal rows; C16, C17, C18 PF Fact rows of kind fact, use_case, case_for_change; C21 PF Person.role and tier; C22 PF Person.note; C30 PF Draft rows (status waiting_gate2, enrolment_key empty); C31 PF Draft.fact_check; C32 PF Draft.grade; C38 PF Inbox.placement_pct_last and blacklisted; C45 PF Account.meeting_label; C46 PF Account.qualified_status; C54 PF Draft.planted_error; every other component writes only its PF Component run row), never a locked field of a booked account (locked_at set), then calls Pipeline Factory · Save hand-off once per name in the component's feeds that is a component (from_component the component's name, to_component the feed, writes_field the field written, the same keys, confidence, payload and evidence), and saves the PF Component run with status saved (or proposal for the sw8 learning agents), model, run_at and the hand-off ids. Every write carries the origin given (default user). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Save agent output; test runs with origin test answer each result path.

### t4 · Deploy Pipeline Factory · Save agent output

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Save agent output" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Save agent output" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Save agent output".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Save agent output deployed with definitionVersion equal to the saved version.

### t5 · Build Pipeline Factory · Reset agent runs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Reset agent runs"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Reset demo \`6ae8441df38e327618fcc13c\`.
2. Done when: automation · create · Pipeline Factory · Reset agent runs: callable from Pipeline Factory · Reset demo, mode deterministic, no model call; no inputs; result deleted (number), restored (number). Deletes every row whose origin is test in PF Component run, PF Source, PF Inbox and PF Suppression, puts every seed row of those four objects back from PF Seed snapshot, never touches a user row. Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Reset agent runs; test runs with origin test answer each result path.

### t6 · Deploy Pipeline Factory · Reset agent runs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Reset agent runs" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Reset agent runs" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Reset agent runs".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Reset agent runs deployed with definitionVersion equal to the saved version.

### t7 · Change Pipeline Factory · Reset demo

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Reset demo" (\`6ae8441df38e327618fcc13c\`), its saved version, code, \`setup\` and \`result\` schema; \`describe_storage_object\` for each PF object it reads or writes (PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`). If its contract differs from the round-1 line, stop and report.
2. Done when: automation · update · Pipeline Factory · Reset demo: after its round-1 steps, unchanged, it calls Pipeline Factory · Reset agent runs and adds its deleted and restored counts to its own; the PF Component rows are restored from their snapshot rows, which the registry line below rewrites to hold the built-entity fields, so a reset keeps the links. Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call. Change only what the line says; every round-1 path keeps its behaviour and result.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Reset demo; test runs with origin test answer each result path.

### t8 · Deploy Pipeline Factory · Reset demo

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Reset demo" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Reset demo" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Reset demo".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Reset demo deployed with definitionVersion equal to the saved version.

