---
nebula: 3
specId: "e_6ae861bcd96c5f6ba2341a49"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P03"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Account Ranking"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Weekly Slot Planner"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Holdout Picker"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Do-Not-Contact List"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Account Ranking"},{"kind":"automation","name":"Pipeline Factory · Weekly Slot Planner"},{"kind":"automation","name":"Pipeline Factory · Holdout Picker"},{"kind":"automation","name":"Pipeline Factory · Do-Not-Contact List"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "b29e8605-53dd-460a-bdf4-e8e982be7ece"
pageDesign: 2
createdAt: "2026-11-02T10:11:11.238Z"
runningAt: "2026-11-02T10:11:14.874Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P03

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Account Ranking |  | running | 1 |
| t2 | deploy | Pipeline Factory · Account Ranking | t1 | pending | 0 |
| t3 | automation | Pipeline Factory · Weekly Slot Planner |  | running | 1 |
| t4 | deploy | Pipeline Factory · Weekly Slot Planner | t3 | pending | 0 |
| t5 | automation | Pipeline Factory · Holdout Picker |  | running | 1 |
| t6 | deploy | Pipeline Factory · Holdout Picker | t5 | pending | 0 |
| t7 | automation | Pipeline Factory · Do-Not-Contact List |  | running | 1 |
| t8 | deploy | Pipeline Factory · Do-Not-Contact List | t7 | pending | 0 |

### t1 · Build Pipeline Factory · Account Ranking

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Account Ranking"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Log signal \`6ae843cc9594aa458cba14d7\`.
2. Done when: automation · create · Pipeline Factory · Account Ranking: callable from Pipeline Factory · Run component and other automations; mode deterministic, no model call; inputs patch_id (text, required), mode (text: rank \| top_up), origin (text); result ranked (number), queued_to_gate1 (number), reason (text). rank (the Monday 06:00 job): recomputes each account's timing_score as the sum of its counted PF Signal weights in the last 30 days, capped at 40 (the same starting weights and checked-visit rule Pipeline Factory · Log signal applies; Log signal is unchanged and keeps scoring a single new signal), writes rank_in_patch by fit_score + timing_score and top_signals (the top 3) on PF Account; top_up (the daily 07:00 job): moves the highest-ranked queued accounts of the patch to gate1_status pending until the patch's slots left (slots_allocated minus slots_used) are filled, after fast-lane plays, skipping held-out and not_eligible accounts; saves an Account Ranking to Gate 1 hand-off per account queued through Save hand-off and one PF Component run (component_id C12, kind workflow, model none). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Account Ranking; test runs with origin test answer each result path.

### t2 · Deploy Pipeline Factory · Account Ranking

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Account Ranking" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Account Ranking" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Account Ranking".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Account Ranking deployed with definitionVersion equal to the saved version.

### t3 · Build Pipeline Factory · Weekly Slot Planner

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Weekly Slot Planner"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Weekly Slot Planner: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, empty for all), origin (text); result allocations (text, JSON per patch: base, cap, boost, allocated), reason (text). Base 25 slots per patch; a pace boost of up to 50% (25% by default) only to a patch whose AE has under 6 intros booked in 7 days and is behind on intro meetings (intros_booked_7d under 4, the assumed weekly target, since no diagnosis field exists); then never more than eligible_accounts ÷ 13 (rounded down), floor 15, cap 40. Writes PF Patch.slots_allocated and pace_boost_pct and one PF Component run per patch (C13) logging every allocation; PATCH-NAE-03 gets 24 (312 ÷ 13), PATCH-NAE-04 gets 20 (260 ÷ 13) with its 25% boost logged. Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Weekly Slot Planner; test runs with origin test answer each result path.

### t4 · Deploy Pipeline Factory · Weekly Slot Planner

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Weekly Slot Planner" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Weekly Slot Planner" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Weekly Slot Planner".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Weekly Slot Planner deployed with definitionVersion equal to the saved version.

### t5 · Build Pipeline Factory · Holdout Picker

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Holdout Picker"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Holdout Picker: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, required), week_seed (number; default the ISO week number of the run), origin (text); result held (text, JSON account ids), std_diff_fit (number), std_diff_timing (number), redraws (number), reason (text). From the patch's medium and low fit accounts that are pending or queued and not yet held, draws 10% (at least 1) with a seeded pseudo-random order from week_seed; checks the standardised difference of fit_score and timing_score between held and treated under 0.1, else redraws with week_seed + 1, at most 5 times, then answers the best draw with reason "balance not reached after 5 redraws"; sets factory_holdout true and factory_holdout_until 90 days after the run on each held account (HubSpot flag mocked as the PF Account fields) and logs the seed in one PF Component run (C14). Decide Gate 1, unchanged, refuses a held account. The 90- and 180-day reports are the PF Component run rows (assumption). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Holdout Picker; test runs with origin test answer each result path.

### t6 · Deploy Pipeline Factory · Holdout Picker

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Holdout Picker" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Holdout Picker" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Holdout Picker".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Holdout Picker deployed with definitionVersion equal to the saved version.

### t7 · Build Pipeline Factory · Do-Not-Contact List

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Do-Not-Contact List"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Do-Not-Contact List: callable from the AI agents (PF · Reply Sorter), Pipeline Factory · Run component and other automations; mode deterministic, no model call; inputs action (text: add \| erase \| sync \| screen), person_id (text), kind (text: opt_out \| bounce \| complaint \| legal_hold), reason (text), origin (text); result result (text: added \| already_listed \| erased \| synced \| clear \| listed), suppression_id (text), reason (text). add: one PF Suppression row per person and kind (no second row), PF Person.dnc true, copied_to "HubSpot, Apollo, Sprouts (mocked)" with copied_at now; erase: sets the PF Person's name to "Erased person" and its note empty, keeps only a hashed code (email_hash) on a PF Suppression erasure row with erase_due 30 days out, so the person is never re-added; sync: stamps copied_at on every row (the 15-minute copy, mocked); screen: answers listed or clear for a person (the phone DNC screen before any dialler, mocked as the list). One PF Component run per call (C25). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Do-Not-Contact List; test runs with origin test answer each result path.

### t8 · Deploy Pipeline Factory · Do-Not-Contact List

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Do-Not-Contact List" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Do-Not-Contact List" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Do-Not-Contact List".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Do-Not-Contact List deployed with definitionVersion equal to the saved version.

