---
nebula: 3
specId: "e_6ae861d5d96c5f6ba2341ca3"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P05"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Alarm and Escalation"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Content Handoff"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Privacy and Consent"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Run component"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Alarm and Escalation"},{"kind":"automation","name":"Pipeline Factory · Content Handoff"},{"kind":"automation","name":"Pipeline Factory · Privacy and Consent"},{"kind":"automation","name":"Pipeline Factory · Run component"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "39a22fd8-46f4-44d5-90fc-6d91da7d506d"
pageDesign: 2
createdAt: "2026-11-02T10:11:35.483Z"
runningAt: "2026-11-02T10:11:40.071Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P05

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Alarm and Escalation |  | running | 1 |
| t2 | deploy | Pipeline Factory · Alarm and Escalation | t1 | pending | 0 |
| t3 | automation | Pipeline Factory · Content Handoff |  | running | 1 |
| t4 | deploy | Pipeline Factory · Content Handoff | t3 | pending | 0 |
| t5 | automation | Pipeline Factory · Privacy and Consent |  | running | 1 |
| t6 | deploy | Pipeline Factory · Privacy and Consent | t5 | pending | 0 |
| t7 | automation | Pipeline Factory · Run component |  | running | 1 |
| t8 | deploy | Pipeline Factory · Run component | t7 | pending | 0 |

### t1 · Build Pipeline Factory · Alarm and Escalation

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Alarm and Escalation"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Pause component \`6ae843d1f6f76639f8cf2d55\`.
2. Done when: automation · create · Pipeline Factory · Alarm and Escalation: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs origin (text); result actions (text, JSON: component or patch, red line, action, before and after), escalations (text, JSON), reason (text). Reads PF Component success_rate and PF Patch; a component under 95% is paused automatically through Pipeline Factory · Pause component (a safety action; resuming needs a person); a component from 95% to under 97% gets a to-do item for the GTM engineer (a PF Hand-off waiting_person through Save hand-off) and is never paused by it, so beat 7's person still pauses Current Vendor Finder (96.1%); a patch under its intro pace gets a throttle or move-slots proposal as a to-do item; unfixed alarms escalate patch to pod after 2 business days, to Geo after 5, then to CRO (by the age of the open to-do item); logs before and after numbers in one PF Component run (C55). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Alarm and Escalation; test runs with origin test answer each result path.

### t2 · Deploy Pipeline Factory · Alarm and Escalation

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Alarm and Escalation" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Alarm and Escalation" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Alarm and Escalation".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Alarm and Escalation deployed with definitionVersion equal to the saved version.

### t3 · Build Pipeline Factory · Content Handoff

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Content Handoff"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Content Handoff: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs patch_id (text, required), origin (text); result audiences (number), to_content_factory (number), to_nurture (number), marketing_influenced_set (number), reason (text). Accounts in play in the patch go to a LinkedIn ad audience by patch geography for 8 weeks; people never reached go to the Content Factory (ads and content only, never cold email); people whose reply was sorted "not now" or who engaged go to nurture until their date; sets PF Account.marketing_influenced true on accounts in play that are not yet booked (never on a locked account); the weekly asset, message and pattern results by patch are the run payload; one PF Component run (C56). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Content Handoff; test runs with origin test answer each result path.

### t4 · Deploy Pipeline Factory · Content Handoff

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Content Handoff" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Content Handoff" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Content Handoff".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Content Handoff deployed with definitionVersion equal to the saved version.

### t5 · Build Pipeline Factory · Privacy and Consent

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Privacy and Consent"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Privacy and Consent: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, empty for all), origin (text); result checklist (text, JSON per person: recording consent, DNC, send window, consent, footer), erasures_due (number), cleanup_flagged (number), reason (text). Per person: recording consent per state from PF Suppression consent rows, the DNC screen through Pipeline Factory · Do-Not-Contact List (action screen), the state legal checklist (send window, consent, footer); erasure rows past erase_due are completed through Do-Not-Contact List (action erase); people never engaged in 12 months are flagged for clean-up in the run (never deleted by the demo); one PF Component run (C57). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Privacy and Consent; test runs with origin test answer each result path.

### t6 · Deploy Pipeline Factory · Privacy and Consent

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Privacy and Consent" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Privacy and Consent" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Privacy and Consent".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Privacy and Consent deployed with definitionVersion equal to the saved version.

### t7 · Build Pipeline Factory · Run component

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Run component"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Ask the analyst \`6ae84900fbdd550a9a465807\`.
2. Done when: automation · create · Pipeline Factory · Run component: callable from the app; inputs component_id (text, required), account_id (text), person_id (text), draft_id (text), origin (text); result result (text: ran \| paused \| not_runnable \| failed), run_id (text), handoff_ids (text), confidence (number), summary (text), reason (text). Reads the PF Component row: status paused answers paused and runs nothing; built_kind not_built (human gates C26, C40, C47 and the two rule steps) answers not_runnable "a person or a rule step, not a built entity"; built_kind ai_agent invokes the agent whose id is built_entity_id (the same invoke operation Pipeline Factory · Ask the analyst uses) with the message "Run your job for component \`component_id\` on account \`account_id\` (person, draft when given); origin \`origin\`", then reads the newest PF Component run of that component and account and writes latency_ms on it; built_kind automation calls the matching workflow automation above (one branch per component id, C12, C13, C14, C24, C25, C33, C35, C39, C43, C55, C56, C57, passing account_id or its patch_id and origin; C15 and C34 answer not_runnable "run from To-do or Gate 2"). If the invoke operation takes only a fixed agent, it branches per component id for the 38 agents instead. Deterministic itself; the model call is the invoked agent's. Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Run component; test runs with origin test answer each result path.

### t8 · Deploy Pipeline Factory · Run component

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Run component" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Run component" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Run component".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Run component deployed with definitionVersion equal to the saved version.

