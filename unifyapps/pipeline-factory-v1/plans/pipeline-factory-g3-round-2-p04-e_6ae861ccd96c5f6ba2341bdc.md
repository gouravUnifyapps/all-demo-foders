---
nebula: 3
specId: "e_6ae861c8d96c5f6ba2341b91"
mode: "sonic"
title: "Pipeline Factory · G3 round 2 · P04"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Contact Finder"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Send Rules Check"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Outreach Launcher"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Email Domain Swapper"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Meeting Handoff and Deadlines"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Contact Finder"},{"kind":"automation","name":"Pipeline Factory · Send Rules Check"},{"kind":"automation","name":"Pipeline Factory · Outreach Launcher"},{"kind":"automation","name":"Pipeline Factory · Email Domain Swapper"},{"kind":"automation","name":"Pipeline Factory · Meeting Handoff and Deadlines"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "9d5a3d24-5884-4502-8e2c-6226e47dfd13"
pageDesign: 2
createdAt: "2026-11-02T10:11:23.284Z"
runningAt: "2026-11-02T10:11:27.188Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Pipeline Factory · G3 round 2 · P04

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Contact Finder |  | running | 1 |
| t2 | deploy | Pipeline Factory · Contact Finder | t1 | pending | 0 |
| t3 | automation | Pipeline Factory · Send Rules Check |  | running | 1 |
| t4 | deploy | Pipeline Factory · Send Rules Check | t3 | pending | 0 |
| t5 | automation | Pipeline Factory · Outreach Launcher |  | running | 1 |
| t6 | deploy | Pipeline Factory · Outreach Launcher | t5 | pending | 0 |
| t7 | automation | Pipeline Factory · Email Domain Swapper |  | running | 1 |
| t8 | deploy | Pipeline Factory · Email Domain Swapper | t7 | pending | 0 |
| t9 | automation | Pipeline Factory · Meeting Handoff and Deadlines |  | running | 1 |
| t10 | deploy | Pipeline Factory · Meeting Handoff and Deadlines | t9 | pending | 0 |

### t1 · Build Pipeline Factory · Contact Finder

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Contact Finder"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Contact Finder: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, required), origin (text); result verified (number), linkedin_only (number), reason (text). For each PF Person of the account that is not a gatekeeper and not on the suppression list: a PF Source contact_record with a verified email sets email_status verified (phone noted for Tier 1 and engaged people in the run), none sets linkedin_only; a verification older than 90 days is re-checked before use; one PF Component run (C24) with source and verify date per person (graph and HubSpot writes mocked as the PF records). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Contact Finder; test runs with origin test answer each result path.

### t2 · Deploy Pipeline Factory · Contact Finder

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Contact Finder" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Contact Finder" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Contact Finder".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Contact Finder deployed with definitionVersion equal to the saved version.

### t3 · Build Pipeline Factory · Send Rules Check

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Send Rules Check"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Send Rules Check: callable from Pipeline Factory · Run component and other automations; mode deterministic, no model call; inputs draft_id (text, required), origin (text); result result (text: passed \| blocked), rule (text), reason (text), checks (text, JSON: every rule with passed or failed). Read-only on PF Draft (Clear Gate 2 stays the only writer of rules_check): checks clean text (no empty subject or body, no unfilled placeholder, the AE's name right); person still in role (not erased); not on DNC (PF Person.dnc or a PF Suppression row), not held out, not a customer or open deal (deal_stage none); parent outreach lock owned by this owner (ultimate_parent_lock equals owner_ae or is empty); Patch ID, AE and pod present; sender from the account's pod and under its inbox daily limit (PF Inbox sent_today under 70% of daily_limit); person not in another sequence; consent recorded for the person's state when a PF Suppression consent row exists; a planted_error draft is always blocked. Answers the first failed rule in a fixed order (pod, DNC, other sequence, held out, Patch ID/AE/pod, parent lock, inbox limit, clean text, planted error) so it names the same rule Clear Gate 2 names for D-04 (pod) and for D-06 (other sequence). One PF Component run (C33). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Send Rules Check; test runs with origin test answer each result path.

### t4 · Deploy Pipeline Factory · Send Rules Check

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Send Rules Check" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Send Rules Check" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Send Rules Check".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Send Rules Check deployed with definitionVersion equal to the saved version.

### t5 · Build Pipeline Factory · Outreach Launcher

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Outreach Launcher"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Outreach Launcher: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, required), origin (text); result scheduled (number), already_scheduled (number), schedule (text, JSON), reason (text). For every PF Draft of the account with status enrolled (Clear Gate 2 enrols; it is unchanged): schedules email steps into the assigned inbox's sequence, LinkedIn steps into the sender's Sprouts queue and calls as call tasks, in the prospect's local morning (09:00 to 11:00 in the account's state) and state window, Tier 2 two days after Tier 1 and Tier 3 two days after that, no two people at one account emailed the same day; holds every inbox at 70% of its daily limit (adds to PF Inbox.sent_today, never past 70%); keyed on enrolment_key (person + play): a draft already scheduled answers already_scheduled and writes nothing; owner, Patch ID, BDR of record, sequence status and tasks to HubSpot are mocked as the PF Component run payload (C35). It never writes ultimate_parent_lock (Parent Company Linker is that field's one writer; open question). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Outreach Launcher; test runs with origin test answer each result path.

### t6 · Deploy Pipeline Factory · Outreach Launcher

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Outreach Launcher" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Outreach Launcher" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Outreach Launcher".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Outreach Launcher deployed with definitionVersion equal to the saved version.

### t7 · Build Pipeline Factory · Email Domain Swapper

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Email Domain Swapper"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Email Domain Swapper: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs sender (text, empty for all), origin (text); result rested (text, JSON inbox ids), swapped_in (text, JSON), retired (text, JSON), blocked_new (text, JSON), reason (text). An active inbox with placement under 70% in its last two tests, or blacklisted, goes to resting the same day and the sender's first warm_spare goes active; a previously blacklisted inbox goes to retired; a new sender's (blocked_new) inbox stays blocked until a placement test of 70 or more exists. Writes PF Inbox.status (its one writer) and one PF Component run (C39). On the seeds: IN-02 rests, IN-03 goes active, IN-05 retires, IN-06 stays blocked. Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Email Domain Swapper; test runs with origin test answer each result path.

### t8 · Deploy Pipeline Factory · Email Domain Swapper

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Email Domain Swapper" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Email Domain Swapper" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Email Domain Swapper".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Email Domain Swapper deployed with definitionVersion equal to the saved version.

### t9 · Build Pipeline Factory · Meeting Handoff and Deadlines

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Meeting Handoff and Deadlines"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: Pipeline Factory · Book meeting \`6ae84449f38e327618fcc640\`.
2. Done when: automation · create · Pipeline Factory · Meeting Handoff and Deadlines: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, empty for all), origin (text); result picked_up (number), deadlines (text, JSON), escalations (text, JSON), reason (text). Picks up meetings booked outside the AE's link from PF Source calendar_event rows (the AE's Google Calendar, mocked) and calls Pipeline Factory · Book meeting (action book, the same origin) for an account not yet booked (a rejected meeting rebooked within 30 days keeps its source); saves a Meeting Handoff and Deadlines to Meeting Prep Writer hand-off through Save hand-off (the prep pack trigger; SC booking, agenda and 24h/1h reminders and the 2-touch no-show reschedule are mocked as the run payload); computes the AE deadlines in business hours: accept or reject within 1 business day (else Geo leader in 4h or the backup AE), decide within 2 business days of a held meeting, stale after 5 idle business days at Engage, alert at 30 days in Connect and 45 in Commit without a next step, reminder at half-window and escalation on a miss, as PF Hand-off rows waiting_person through Save hand-off; one PF Component run (C43). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Meeting Handoff and Deadlines; test runs with origin test answer each result path.

### t10 · Deploy Pipeline Factory · Meeting Handoff and Deadlines

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Meeting Handoff and Deadlines" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Meeting Handoff and Deadlines" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Meeting Handoff and Deadlines".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Meeting Handoff and Deadlines deployed with definitionVersion equal to the saved version.

