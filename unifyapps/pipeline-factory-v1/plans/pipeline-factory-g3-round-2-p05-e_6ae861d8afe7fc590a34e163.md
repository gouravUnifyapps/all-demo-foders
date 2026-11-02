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
| t3 | automation | Pipeline Factory · Content Handoff |  | done | 1 |
| t4 | deploy | Pipeline Factory · Content Handoff | t3 | running | 1 |
| t5 | automation | Pipeline Factory · Privacy and Consent |  | done | 1 |
| t6 | deploy | Pipeline Factory · Privacy and Consent | t5 | running | 1 |
| t7 | automation | Pipeline Factory · Run component |  | done | 1 |
| t8 | deploy | Pipeline Factory · Run component | t7 | running | 1 |

### t1 · Build Pipeline Factory · Alarm and Escalation

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Alarm and Escalation"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Pause component \`6ae843d1f6f76639f8cf2d55\`.
2. Done when: automation · create · Pipeline Factory · Alarm and Escalation: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs origin (text); result actions (text, JSON: component or patch, red line, action, before and after), escalations (text, JSON), reason (text). Reads PF Component success_rate and PF Patch; a component under 95% is paused automatically through Pipeline Factory · Pause component (a safety action; resuming needs a person); a component from 95% to under 97% gets a to-do item for the GTM engineer (a PF Hand-off waiting_person through Save hand-off) and is never paused by it, so beat 7's person still pauses Current Vendor Finder (96.1%); a patch under its intro pace gets a throttle or move-slots proposal as a to-do item; unfixed alarms escalate patch to pod after 2 business days, to Geo after 5, then to CRO (by the age of the open to-do item); logs before and after numbers in one PF Component run (C55). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Alarm and Escalation; test runs with origin test answer each result path.
Error: Asked the person: Question for the person: the GTM-engineer to-do for a component at 95% to under 97% (C08 Current Vendor Finder) is refused by Save hand-off as 'not registered', because C55's register row feeds only 'patch, pod, Geo, CRO', and no C55 hand-off can be waiting_person (no receiving register row with a threshold). Options: (a) add 'GTM engineer' to C55 feeds in PF Component and a register entry for the GTM engineer with a threshold above 0 (fde/data task, also in the seed snapshot), then re-test; (b) send the component to-do to 'pod' (registered) and accept status flowed; (c) change Save hand-off to accept a person target. The automation is built and saved at version 2; only this step waits. Made so far: ids {"entity":"6ae863282099302ffb2cf702"}.

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
Result IDs: {"entity":"6ae863d0fbdd550a9a4ffc58"}
Read back: Pipeline Factory · Content Handoff 6ae863d0fbdd550a9a4ffc58: open_workflow version 0, trigger CALLABLE callables/callables_from_automation, 15 nodes; setup {patch_id string required, origin enum user\|seed\|test}; result {audiences, to_content_factory, to_nurture, marketing_influenced_set: number; reason: string}, all required; describe_callable_workflow lists patch_id (required) and origin
Read back: Pipeline Factory · Content Handoff: run 6ae863d82099302ffb2d213a (PATCH-NAE-03, origin test) COMPLETED: audiences 6, to_content_factory 10, to_nurture 2, marketing_influenced_set 5, reason '6 accounts in play to the NA East LinkedIn audience, 10 people to the Content Factory, 2 to nurture, 5 accounts set marketing-influenced; logged in PF Component run CR-6ae863d82099302ffb2d213a'
Read back: Pipeline Factory · Content Handoff: get_records PF Account PATCH-NAE-03: A-1001, A-1002, A-1003, A-1004, A-1009 marketing_influenced true (boolean); A-1007 (locked_at set) stays false; A-1005 (held out) and A-1008 (queued) untouched
Read back: Pipeline Factory · Content Handoff: PF Component run CR-6ae863d82099302ffb2d213a component_id C56, status saved, origin test; payload holds audience (NA East, 8 weeks), content_factory, nurture (P-1007 not_now until 1794441600000 = 12 Nov 2026; P-1002 engaged), locked_skipped [A-1007], weekly_results assets/messages/patterns
Read back: Pipeline Factory · Content Handoff: run 6ae863dc46920244f3d5388d (patch_id '') COMPLETED -&gt; all counts 0, reason 'patch_id is required'; run 6ae863dd46920244f3d5389e (PATCH-NOPE-99) -&gt; reason 'patch PATCH-NOPE-99 not found'
Read back: Pipeline Factory · Content Handoff: best practice 97 (82 of 85 checks), no fix round needed, version 0
Note: assumed: accounts in play = gate1_status pending or accepted and not factory_holdout; booked/locked = locked_at set; people reached = a PF Source reply or an enrolled PF Draft; replies sorted by text (opt-out, not now, engaged); not-now nurture runs to the date in the reply, else 90 days; engaged nurture runs 30 days from the reply; audiences counts accounts added to the patch-geography audience
Note: Security (rule 4): writes only PF Account.marketing_influenced via update_record_fields_by_id; never on a locked account; in a test run, user-origin accounts are skipped (payload user_rows_skipped_in_test)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_b473t PF Patch patch_id, n_pvlri PF Account patch_id, n_qg21b PF Source source_kind) · score already 90 or more
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_pbnpo) · score already 90 or more
Note: best practice exception: CHECK_37 Capture Iterations enabled · For each loop (n_w7qt4) · score already 90 or more
Note: test rows left for Reset demo: PF Component run CR-6ae863d82099302ffb2d213a; seed rows PF Account A-1001, A-1002, A-1003, A-1004, A-1009 changed marketing_influenced to true (Reset demo puts seed rows back)

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
Result IDs: {"entity":"6ae86493f38e32761818a2c1"}
Read back: Pipeline Factory · Privacy and Consent 6ae86493f38e32761818a2c1: open_workflow version 1, trigger CALLABLE callables/callables_from_automation, 19 nodes; setup {account_id string (empty for all), origin enum user\|seed\|test}; result {checklist string, erasures_due number, cleanup_flagged number, reason string}, all required; describe_callable_workflow lists account_id and origin, both optional
Read back: Pipeline Factory · Privacy and Consent: run 6ae864e046920244f3d582ef (A-1001, origin test, version 1) COMPLETED_WITH_FAILURE: erasures_due 1 (SUP-TEST-ERASE), cleanup_flagged 7, checklist JSON per person (recording_consent, dnc, send_window, consent, footer, cleanup); reason '13 people checked, 0 clear to contact, 13 not screened, 1 erasures due (0 completed), 7 flagged for clean-up'; same outcome as run 6ae864a3f38e32761818a423 on version 0
Read back: Pipeline Factory · Privacy and Consent: the Do-Not-Contact List calls failed with 'DEPLOYED_WORKFLOW_DEFINITION_MAPPING with id 6ae864672099302ffb2d3157 not found' (DNC not deployed yet); onError CONTINUE kept the run going and the checklist says 'not screened'
Read back: Pipeline Factory · Privacy and Consent: run 6ae864d49594aa458cc4db7c (account_id 'A 1001;') -&gt; reason 'account_id must be an account id such as A-1001'; run 6ae864a99ec43c6ee22fd869 (A-9999) -&gt; reason 'account A-9999 not found'
Read back: Pipeline Factory · Privacy and Consent: get_records PF Component run CR-6ae864e046920244f3d582ef component_id C57, account_id A-1001, status saved, origin test
Read back: Pipeline Factory · Privacy and Consent: best practice 90 (81 of 85 checks) after 1 fix round, first read 88, version 1
Unverified: DNC screen and erase through Pipeline Factory · Do-Not-Contact List (6ae864672099302ffb2d3157): not deployed when tested, so 'clear/listed' per person and the erase of SUP-TEST-ERASE are unproven; check: after DNC is deployed, run Privacy and Consent with {account_id: A-1001, origin: test} and read checklist dnc values, erasures completed, and PF Person P-TEST-ERASE name
Unverified: All-blank payload (account_id empty = all accounts) not run separately; check: trigger with {origin: test} and read the checklist count
Note: handover: Privacy and Consent calls Do-Not-Contact List 6ae864672099302ffb2d3157 (action screen per person, action erase per erasure past erase_due); deploy DNC before Privacy and Consent's deploy test, then re-run with A-1001
Note: assumed: state from PF Account hq_city's last two letters; two-party recording-consent states CA, CT, DE, FL, IL, MD, MA, MI, MT, NV, NH, OR, PA, WA; send window calls 08:00-21:00 local, email 09:00-11:00 local; footer unsubscribe link + postal address (CCPA notice for CA); engaged in 12 months = a reply in 365 days or an enrolled draft
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation (n_1u6l2), Create record (n_avytp) · fix would change behaviour (the flagged field is the account_id contract input and the run row's account_id)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_ngttl PF Source source_kind, n_6lwjx PF Draft status) · score already 90 or more
Note: best practice exception: CHECK_27 Manual list aggregation detected · Add item to list (n_at3de, n_9bnxh) · score already 90 or more
Note: best practice exception: CHECK_37 Capture Iterations enabled · For each loop (n_whh4o, n_jcaef) · score already 90 or more
Note: test rows left for Reset demo: PF Person P-TEST-ERASE (fixture); PF Suppression SUP-TEST-ERASE (fixture); PF Component run CR-6ae864a3f38e32761818a423, CR-6ae864e046920244f3d582ef

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
Result IDs: {"entity":"6ae865229ec43c6ee2300d8d"}
Read back: Pipeline Factory · Run component 6ae865229ec43c6ee2300d8d: open_workflow version 2, trigger CALLABLE callables/callables_from_automation, 68 nodes, 12 callables_call_automation (C12 6ae8632c9ec43c6ee22f380d, C13 6ae863a5f38e327618183dca, C14 6ae864059ec43c6ee22f8008, C24 6ae862f3f13e536c52e76ecd, C25 6ae864672099302ffb2d3157, C33 6ae863842099302ffb2d0262, C35 6ae864929594aa458cc23de9, C39 6ae864342099302ffb2d2a71, C43 6ae8654d2099302ffb2d9514, C55 6ae863282099302ffb2cf702, C56 6ae863d0fbdd550a9a4ffc58, C57 6ae86493f38e32761818a2c1) and 1 invoke_agent
Read back: Pipeline Factory · Run component: setup {component_id required, account_id, person_id, draft_id, origin}; result {result enum ran\|paused\|not_runnable\|failed, run_id, handoff_ids, confidence number, summary, reason}, all required; describe_callable_workflow confirms the five inputs
Read back: Pipeline Factory · Run component: run 6ae865349ec43c6ee2301263 (all blank) -&gt; failed 'component_id is required'; 6ae8659246920244f3d5b105 (account 'A 1001') -&gt; failed 'account_id must be an id ...'; 6ae865a546920244f3d5b2bd (C404) -&gt; failed 'component C404 is not in the register'
Read back: Pipeline Factory · Run component: run 6ae8653546920244f3d5a034 (C99-TEST, paused) -&gt; paused '... is paused; a person must resume it before it runs'; 6ae86536f13e536c52e9c14f (C15) -&gt; not_runnable 'run from To-do or Gate 2'; 6ae865382099302ffb2d9349 (C26) -&gt; not_runnable 'a person or a rule step, not a built entity'
Read back: Pipeline Factory · Run component: run 6ae8659a2099302ffb2d9dba (C98-TEST, built_kind ai_agent -&gt; Pipeline Factory Analyst e_6ae846ffd96c5f6ba22b98da) invoked the agent with 'Run your job for component C98-TEST on account A-1001 (draft D-04); origin test', agent answered, no PF Component run saved -&gt; failed 'the agent answered but saved no PF Component run for this account'
Read back: Pipeline Factory · Run component: run 6ae865e62099302ffb2db08a (version 2, C97-TEST built_kind automation, no branch) -&gt; not_runnable 'Run component workflow fixture (test row) has no workflow automation to run'
Read back: Pipeline Factory · Run component: best practice 83 (82 of 85 checks) at version 2 after 1 fix round, first read 75
Unverified: result 'ran' through a workflow branch: the 12 callees were undeployed or the PF Component rows have no built_kind yet, so no branch ran; check: once the registry sets C55 built_kind automation and Alarm and Escalation is deployed, run {component_id: C55, origin: test} and read run_id and reason
Unverified: result 'ran' with latency_ms write on an agent's run: no built agent saves a PF Component run yet; check: run a component whose built_entity_id is a deployed round-2 agent and read latency_ms on its newest PF Component run
Unverified: Version 2 (C43 arm added after the fix round) was retested only on the C97-TEST automation path; the agent path was last run on version 1
Note: PF Component seed rows have no built_kind or built_entity_id today (fields added after seeding); until the registry is filled, every component except the test fixtures answers not_runnable 'a person or a rule step, not a built entity'
Note: handover: Run component dispatches workflow components by component_id branch with these callee ids: C12 6ae8632c9ec43c6ee22f380d, C13 6ae863a5f38e327618183dca, C14 6ae864059ec43c6ee22f8008, C24 6ae862f3f13e536c52e76ecd, C25 6ae864672099302ffb2d3157, C33 6ae863842099302ffb2d0262, C35 6ae864929594aa458cc23de9, C39 6ae864342099302ffb2d2a71, C43 6ae8654d2099302ffb2d9514, C55 6ae863282099302ffb2cf702, C56 6ae863d0fbdd550a9a4ffc58, C57 6ae86493f38e32761818a2c1; all must be deployed before Run component reaches 'ran'
Note: The invoke operation takes the agent id as a parameter, so Run component invokes built_entity_id dynamically (no per-agent branch)
Note: assumed: C25 is run with action screen on person_id; C12 with mode rank on the account's patch; C13, C14, C56 with the account's patch_id; C39 with sender empty (all)
Note: Security (rule 2): component, account, person and draft ids are format-checked and only select which record runs; the agent call carries USER.contactDetails.email from the platform
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation (n_cglr3), Call automation (n_xtvtn, n_wl78k, n_tepgt, n_d6i2g) · fix would change behaviour (flagged field is the account_id contract input passed to callees whose input is named account_id)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (n_cr23d, n_lsmyd, n_khd03, n_anshr) · needs object index outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Update an existing record's fields (n_87wnj, latency_ms write) · fix would change behaviour
Note: test rows left for Reset demo: PF Component C97-TEST and C98-TEST (fixtures); no other rows written by Run component tests

### t8 · Deploy Pipeline Factory · Run component

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Run component" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Run component" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Run component".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Run component deployed with definitionVersion equal to the saved version.

