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
| t1 | automation | Pipeline Factory · Contact Finder |  | done | 1 |
| t2 | deploy | Pipeline Factory · Contact Finder | t1 | running | 1 |
| t3 | automation | Pipeline Factory · Send Rules Check |  | done | 1 |
| t4 | deploy | Pipeline Factory · Send Rules Check | t3 | running | 1 |
| t5 | automation | Pipeline Factory · Outreach Launcher |  | done | 1 |
| t6 | deploy | Pipeline Factory · Outreach Launcher | t5 | running | 1 |
| t7 | automation | Pipeline Factory · Email Domain Swapper |  | done | 1 |
| t8 | deploy | Pipeline Factory · Email Domain Swapper | t7 | running | 1 |
| t9 | automation | Pipeline Factory · Meeting Handoff and Deadlines |  | done | 1 |
| t10 | deploy | Pipeline Factory · Meeting Handoff and Deadlines | t9 | running | 1 |

### t1 · Build Pipeline Factory · Contact Finder

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Contact Finder"; it must not exist (stop and report if it does). Read each PF object it reads or writes with \`describe_storage_object\`: PF Patch \`OBJ_pf_patch\`; PF Account \`OBJ_pf_account\`; PF Person \`OBJ_pf_person\`; PF Signal \`OBJ_pf_signal\`; PF Fact \`OBJ_pf_fact\`; PF Draft \`OBJ_pf_draft\`; PF Hand-off \`OBJ_pf_handoff\`; PF Component \`OBJ_pf_component\`; PF Seed snapshot \`OBJ_pf_seed_snapshot\`; PF Component run \`OBJ_pf_component_run\`; PF Source \`OBJ_pf_source\`; PF Inbox \`OBJ_pf_inbox\`; PF Suppression \`OBJ_pf_suppression\`. Each automation it calls is deployed: .
2. Done when: automation · create · Pipeline Factory · Contact Finder: callable from Pipeline Factory · Run component; mode deterministic, no model call; inputs account_id (text, required), origin (text); result verified (number), linkedin_only (number), reason (text). For each PF Person of the account that is not a gatekeeper and not on the suppression list: a PF Source contact_record with a verified email sets email_status verified (phone noted for Tier 1 and engaged people in the run), none sets linkedin_only; a verification older than 90 days is re-checked before use; one PF Component run (C24) with source and verify date per person (graph and HubSpot writes mocked as the PF records). Inputs and result fields keep the names and types the line gives; every result field is set on every path; a callable from the AI agents or the app or other automations starts with \`callables_from_automation\`. Field writes use the PF objects' plain field names and picklist codes; dates are epoch ms. Every row it creates carries the \`origin\` input (default \`user\`). No model call.
3. Test it with bounded test runs on the saved draft, with origin \`test\`: run each result path the line names at least once (use seeded ids such as A-1001, P-1002, D-04, D-06, IN-02, C08 where the line names them, always passing origin \`test\`), and read the effects back with \`get_records\`. Make no delete call: this run is unattended and no person can confirm a delete, so leave test rows in place (Pipeline Factory · Reset demo clears origin \`test\` rows; PF Component run, PF Source, PF Inbox and PF Suppression through Pipeline Factory · Reset agent runs) and list them by object and id in notes as 'test rows left for Reset demo'. Never change a row whose origin is \`user\`.
4. Read back: \`open_workflow\` for the saved version and its \`setup\` and \`result\` schema, \`describe_callable_workflow\` for its inputs, the test runs' ids with \`inspect_workflow_run\` status and output for each path, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: open_workflow shows the contract of Pipeline Factory · Contact Finder; test runs with origin test answer each result path.
Result IDs: {"entity":"6ae862f3f13e536c52e76ecd"}
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: search_workflows shows version 1, deployment null (not deployed, as the task says); trigger CALLABLE callables/callables_from_automation.
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: describe_callable_workflow -&gt; account_id string required, origin string optional; result schema verified number, linkedin_only number, reason string (all required) as read in the run trigger definition.
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: run 6ae863ec46920244f3d53a40 (v1, A-1001, origin test) COMPLETED -&gt; {verified:1, linkedin_only:11, reason:'1 verified, 11 LinkedIn only, 1 skipped (gatekeeper or suppressed), 0 re-checked'}; 12 C24 runs CR-C24-6ae863ec46920244f3d53a40-1..12 inserted, P-1002 payload source SRC-08 verified_at 1792540800000 phone_noted true.
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: run 6ae863f8f13e536c52e85c06 (v1, no account_id key) COMPLETED -&gt; {verified:0, linkedin_only:0, reason:'account_id is required'}; run 6ae86324f13e536c52e78974 (v0, A-9999) -&gt; reason 'unknown account A-9999'; run 6ae862fa9ec43c6ee22f11c0 (v0, account_id '') -&gt; 'account_id is required'.
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: get_records PF Person A-1001 -&gt; P-1002 email_status verified, P-1001/1003/1004/1005/1007..1011 linkedin_only; gatekeeper P-1013 untouched (verified). get_records PF Component run C24 -&gt; 28 rows origin test.
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: best practice 86 (82 of 85 checks) after 1 fix round, first read 84, version 1.
Read back: Pipeline Factory · Contact Finder 6ae862f3f13e536c52e76ecd: Security rules — rule 5 no secret in any node; rule 4 writes only email_status on PF Person and the run fields; rule 2: account_id is caller-supplied and selects shared PF demo data (no per-user ownership on PF objects).
Unverified: Contact Finder: the 90-day re-check path (creates a PF Source contact_record re-check row) did not run — no seeded contact_record is older than 90 days (SRC-08 dated 1792540800000). Check: a test contact_record with source_date older than 90 days, then a run on its account.
Unverified: Contact Finder: the v1 re-run of A-1001 changed nothing (bulk update skipped, persons already set); the email_status write itself was shown on v0 run 6ae863152099302ffb2cf30c (updated:10).
Note: assumed: 'engaged' = the person has a PF Source reply, call_transcript, meeting_transcript or web_visit row; phone noted is recorded in the C24 run payload (PF Person has no phone field).
Note: assumed: suppression = any PF Suppression row of kind opt_out, bounce, complaint, legal_hold or erasure for the person, or an account-level row; PF Person.dnc also skips the person.
Note: assumed: a re-check of a verification older than 90 days is mocked as a new PF Source contact_record row (origin of the call, status re-verified) rather than editing the seeded source row.
Note: Test effect on seed rows: the A-1001 run set email_status linkedin_only on seed persons P-1001, P-1003, P-1004, P-1005, P-1007, P-1008, P-1009, P-1010, P-1011, P-1012 (were verified; none has a contact_record) — Reset demo must restore them.
Note: test rows left for Reset demo: PF Component run CR-C24-6ae862fa9ec43c6ee22f11c0-1, CR-C24-6ae863152099302ffb2cf30c-1..12, CR-C24-6ae86324f13e536c52e78974-1, CR-C24-6ae863ec46920244f3d53a40-1..12, CR-C24-6ae863f8f13e536c52e85c06-1 (all origin test).
Note: Fix round 1: rewrote the JavaScript node in Groovy (CHECK_35) and guarded the fetches behind 'account_id given' (a missing key would otherwise fail the fetch); outcome unchanged (1 verified, 11 LinkedIn only).
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create or update records in bulk (x2) · fix would change behaviour (flags the contract input and object field account_id; no DSL switch hides node I/O)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (x4) · needs object indexes on OBJ_pf_account, OBJ_pf_person, OBJ_pf_source, OBJ_pf_suppression outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Bulk update records via primary key, Create or update records in bulk (x2) · fix would change behaviour (the node is the write the automation exists to make; its output is not needed downstream)
Note: feedback:
Bug: CHECK_2 'Disable Input/Output Visibility for Sensitive Fields' (critical) fires on nodes whose only plausible secret is a field named account_id, and its row names no field.
Context: get_workflow_best_practice_report on Contact Finder 6ae862f3f13e536c52e76ecd, Outreach Launcher 6ae864929594aa458cc23de9, Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514.
Where: platform
Evidence: Send Rules Check (draft_id input) has no CHECK_2 row on its trigger; the automations with an account_id input do; Email Domain Swapper (no account_id) scores security 100. The DSL has no per-node input/output visibility switch.
Cause: Suspected: a name-pattern match on 'account' treats account_id as a credential.
Regression: the report on 6ae862f3f13e536c52e76ecd shows no CHECK_2 row for trigger n_eoc3a, or names the field it flags.
Note: feature:
Feature: A slim mode on trigger_workflow_run (response, status, node statuses and errors only).
Evidence: each test run of a ~10-node automation returned 40-100 KB, so many runs overflowed to files and the rest filled the context; 20+ runs were needed across five automations.
Benefit: testing every outcome path costs a fraction of the context.
Scope: automation-code trigger_workflow_run / inspect_workflow_run output shaping; non-goal: changing what the platform records.
Acceptance: a slim run of a 10-node automation answers runId, status, response and per-node status/error in under 3 KB.

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
Result IDs: {"entity":"6ae863842099302ffb2d0262"}
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: search_workflows shows version 1, deployment null; trigger CALLABLE callables/callables_from_automation.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: describe_callable_workflow -&gt; draft_id string required, origin string optional; result result (enum passed\|blocked), rule, reason, checks (JSON text), all required.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: run 6ae8659ef38e32761818d2ce (v1, D-04) COMPLETED -&gt; result blocked, rule pod, reason 'Blocked: sender Rhea Castillo is not in the account pod (POD-NAE-1)' — same rule Clear Gate 2 names.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: run 6ae865a02099302ffb2d9e89 (v1, D-06) COMPLETED -&gt; result blocked, rule other_sequence, reason 'Blocked: person is in another sequence'.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: run 6ae86389f38e32761818399a (v0, D-01) COMPLETED -&gt; result passed, rule '', every one of 12 checks passed; run 6ae863b8fbdd550a9a4ff748 (v1, draft_id '') -&gt; blocked/input 'draft_id is required'; run 6ae863b946920244f3d5343f (v1, D-99) -&gt; blocked/draft_not_found.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: read-only on PF Draft — no draft write node exists (operations: 5 fetch, 1 groovy, 1 bulk create on OBJ_pf_component_run); get_records PF Component run C33 shows one row per call.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: best practice 92 (82 of 85 checks), no fix round needed, version 1.
Read back: Pipeline Factory · Send Rules Check 6ae863842099302ffb2d0262: Security rule 3 — every rule reads its state live (PF Person, PF Suppression, PF Inbox, PF Account) in the same run; nothing trusts a caller flag.
Unverified: Send Rules Check: the passed path was shown on v0 (run 6ae86389f38e32761818399a); on v1 D-01 now answers blocked/open_deal (run 6ae865a1fbdd550a9a509e4e) because the Meeting Handoff and Deadlines test booked A-1001 (deal_stage engage). Check: after Reset demo, run v1 with D-01 and origin test, expect passed.
Note: assumed: rule order pod, dnc, person_in_role (erasure row / person missing), other_sequence, held_out, open_deal (deal_stage not none), patch_ae_pod, parent_lock, inbox_limit (email only: an active inbox of the sender in the account pod under 70% of daily_limit), consent (when consent rows exist: one with consent_given true for the state at the end of hq_city), clean_text (subject for email, body, no {{x}}/[X]/&lt;X&gt;/{x} placeholder, owner AE named in the body or is the sender), planted_error. The spec's nine are in its order; the three extra rules sit next to their kin.
Note: Fix (not a best practice round): v1 guards the dependent fetches; v0 run 6ae863909594aa458cbf7b85 FAILED on draft_id '' with 'No Value found in filter with field: properties.account_id'.
Note: Test rows with origin user (blank-origin payload defaults to user, as the contract says): CR-C33-6ae863b8fbdd550a9a4ff748 — Reset demo's origin-test sweep will not clear it.
Note: test rows left for Reset demo: PF Component run CR-C33-6ae86389f38e32761818399a, CR-C33-6ae8638e9594aa458cbf7b3c, CR-C33-6ae8638f46920244f3d51e47, CR-C33-6ae863b946920244f3d5343f, CR-C33-6ae8659ef38e32761818d2ce, CR-C33-6ae865a02099302ffb2d9e89, CR-C33-6ae865a1fbdd550a9a509e4e (origin test).
Note: Observed during tests: PF Suppression rows SUP-TEST-ERASE and SUP-6ae86495f13e536c52e934e5 (opt_out for P-1013) and PF Person P-TEST-ERASE appeared on A-1001 from another builder's tests; they did not change the D-01/D-04/D-06 answers.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Create or update records in bulk · fix would change behaviour (flags the PF Component run field account_id; no DSL switch hides node I/O)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (x5) · score already 90 or more
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create or update records in bulk · score already 90 or more
Note: feedback:
Bug: A storage filter whose value pill points at a field of an empty fetch result saves clean but fails at run time with 'No Value found in filter'.
Context: Send Rules Check v0, fetch OBJ_pf_account with eq(properties_account_id, draft.objects[0].properties.account_id) when the draft fetch matched nothing.
Where: platform
Evidence: run 6ae863909594aa458cbf7b85 FAILED at the account fetch: 'Validation failed with 1 violations ... No Value found in filter with field: properties.account_id, operator: EQUAL'; compile_and_save_workflow gave no warning. Worked around with if (exists(...)) guards.
Cause: Confirmed: an unresolved pill drops the filter's value key and the storage action rejects a filter without a value.
Regression: the compiler warns on an unguarded objects[0] filter value, or the run treats it as no match.

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
Result IDs: {"entity":"6ae864929594aa458cc23de9"}
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: search_workflows shows version 0, deployment null; trigger CALLABLE callables/callables_from_automation.
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: describe_callable_workflow -&gt; account_id string required, origin string optional; result scheduled number, already_scheduled number, schedule string (JSON), reason string, all required.
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: run 6ae864a62099302ffb2d6b15 (A-1001, origin test) COMPLETED -&gt; scheduled 4, already_scheduled 0: D-T01 email IN-03 2026-11-03T09:00 America/New_York, D-T02 linkedin sprouts_queue 09:20, D-T03 email IN-03 2026-11-04T09:00 (next day: one email per account per day), D-T04 Tier 2 call_task 2026-11-05T09:00 (two business days after Tier 1).
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: run 6ae864b5f13e536c52e94e0b (same input) COMPLETED -&gt; scheduled 0, already_scheduled 4, no inbox write (bulk update node not run).
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: run 6ae864bef13e536c52e95524 (account_id '') COMPLETED -&gt; scheduled 0, already_scheduled 0, schedule '[]', reason 'account_id is required'.
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: get_records PF Inbox IN-03 sent_today 2 (was 0; cap floor(0.7*40)=28); PF Account A-1001 ultimate_parent_lock unchanged 'Dana Okafor' (no write node on PF Account); PF Component run CR-C35-6ae864a62099302ffb2d6b15 status saved.
Read back: Pipeline Factory · Outreach Launcher 6ae864929594aa458cc23de9: best practice 89 (82 of 85 checks), under 90 with no fixable check (0 fix rounds), version 0.
Unverified: Outreach Launcher: the 'inbox at 70%' hold path (a draft held when every sender inbox is at 70%) did not run on seeds. Check: an enrolled email draft whose sender's active inboxes have sent_today &gt;= 0.7*daily_limit.
Note: No seeded PF Draft has status enrolled, so test fixtures were created with apply_record_edits (origin test): PF Draft D-T01, D-T02, D-T03, D-T04 for A-1001, status enrolled, enrolment keys P-100x+PLAY-TEST-LAUNCH.
Note: assumed: 'already scheduled' is read from the enrolment_keys in the payload of earlier saved C35 runs of the account (one C35 run per call); the state window is business days only; the account's state comes from the last two letters of hq_city mapped to a US time zone (default America/New_York); slots step 20 minutes from 09:00 inside 09:00-11:00.
Note: assumed: sent_today is raised by the number of email steps scheduled per inbox, as the spec says, even though the steps land on later days.
Note: Test effect on seed rows: PF Inbox IN-03 sent_today 0 -&gt; 2.
Note: Test rows with origin user (blank-origin payload): CR-C35-6ae864bef13e536c52e95524 — not cleared by an origin-test sweep.
Note: test rows left for Reset demo: PF Draft D-T01, D-T02, D-T03, D-T04; PF Component run CR-C35-6ae864a62099302ffb2d6b15, CR-C35-6ae864b5f13e536c52e94e0b (origin test).
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Create or update records in bulk · fix would change behaviour (flags the contract input and object field account_id; no DSL switch hides node I/O)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (x5) · needs object indexes on OBJ_pf_account, OBJ_pf_draft, OBJ_pf_person, OBJ_pf_inbox, OBJ_pf_component_run outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Bulk update records via primary key, Create or update records in bulk · fix would change behaviour (the node is the write the automation exists to make; its output is not needed downstream)

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
Result IDs: {"entity":"6ae864342099302ffb2d2a71"}
Read back: Pipeline Factory · Email Domain Swapper 6ae864342099302ffb2d2a71: search_workflows shows version 0, deployment null; trigger CALLABLE callables/callables_from_automation.
Read back: Pipeline Factory · Email Domain Swapper 6ae864342099302ffb2d2a71: describe_callable_workflow -&gt; sender string optional (empty for all), origin string optional; result rested, swapped_in, retired, blocked_new (JSON text), reason, all required.
Read back: Pipeline Factory · Email Domain Swapper 6ae864342099302ffb2d2a71: run 6ae8643a9594aa458cbfa603 (sender '', origin test) COMPLETED -&gt; rested ["IN-02"], swapped_in ["IN-03"], retired ["IN-05"], blocked_new ["IN-06"] — the four seed outcomes the spec names.
Read back: Pipeline Factory · Email Domain Swapper 6ae864342099302ffb2d2a71: run 6ae8643f9ec43c6ee22f8669 (sender 'Marcus Ellery') COMPLETED -&gt; all lists [], reason 'every inbox healthy; nothing to change' (no inbox write).
Read back: Pipeline Factory · Email Domain Swapper 6ae864342099302ffb2d2a71: get_records PF Inbox -&gt; IN-02 resting, IN-03 active, IN-05 retired, IN-06 blocked_new, IN-01/IN-04 active; PF Component run CR-C39-6ae8643a9594aa458cbfa603 status saved.
Read back: Pipeline Factory · Email Domain Swapper 6ae864342099302ffb2d2a71: best practice 98 (83 of 85 checks), no fix round needed, version 0.
Note: assumed: a blocked_new inbox whose placement_pct_last is 70 or more goes active; a previously blacklisted inbox that was active also swaps in the sender's first warm spare.
Note: Test effect on seed rows: PF Inbox IN-02 active -&gt; resting, IN-03 warm_spare -&gt; active, IN-05 resting -&gt; retired.
Note: test rows left for Reset demo: PF Component run CR-C39-6ae8643a9594aa458cbfa603, CR-C39-6ae8643f9ec43c6ee22f8669 (origin test).
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records · score already 90 or more
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Bulk update records via primary key, Create or update records in bulk · score already 90 or more

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
Result IDs: {"entity":"6ae8654d2099302ffb2d9514"}
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: search_workflows shows version 1, deployment null; trigger CALLABLE callables/callables_from_automation; calls Book meeting 6ae84449f38e327618fcc640 and Save hand-off 6ae840a5fbdd550a9a44c524 (both deployed).
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: describe_callable_workflow -&gt; account_id string optional (empty for all), origin string optional; result picked_up number, deadlines string (JSON), escalations string (JSON), reason string, all required.
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: run 6ae86556f38e32761818cb81 (v0, A-1001, origin test) COMPLETED -&gt; picked_up 1 (Book meeting answered booked from SRC-16), 2 deadlines (accept_reject, decide_after_meeting), prep-pack hand-off H-6ae86558f38e32761818cbc1 to Meeting Prep Writer saved.
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: run 6ae8656a46920244f3d5adf8 (v0, account_id '') COMPLETED -&gt; picked_up 0, 7 deadlines, 3 escalations (A-1001 stale_engage -&gt; Geo leader (POD-NAE-1); A-1007 accept_reject -&gt; backup AE Luis Brennan; A-1013 commit_45d -&gt; backup AE Omar Haddad), 8 hand-offs saved, 2 duplicate.
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: run 6ae86592f38e32761818d15a (v1, A-1001) COMPLETED -&gt; picked_up 0, 3 deadlines, 1 escalation, 4 already saved (Save hand-off answered duplicate); run 6ae8657dfbdd550a9a509b2d (v0, A-9999) -&gt; reason ends 'unknown account A-9999'.
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: get_records PF Hand-off from C43 -&gt; 11 rows origin test (prep_pack, deadline:* and escalation:* plays); PF Account A-1001 meeting_source 'factory: AE booking link', deal_stage engage, locked_at 1793615191550.
Read back: Pipeline Factory · Meeting Handoff and Deadlines 6ae8654d2099302ffb2d9514: best practice 86 (82 of 85 checks) after 1 fix round, first read 83, version 1.
Unverified: Meeting Handoff and Deadlines: the picked_up&gt;0 path ran on v0 only; v1 changed only distributeWorkflowLoad on the two batch calls (the Save hand-off batch with it was shown working in run 6ae86592f38e32761818d15a). Check: after Reset demo, run v1 with A-1001 and origin test, expect picked_up 1.
Unverified: Meeting Handoff and Deadlines: deadline and escalation hand-offs land with status flowed, not waiting_person (see plan_change note). Check: get_records PF Hand-off play_id deadline:* status.
Note: plan_change: requirement — the spec wants the AE deadlines saved 'as PF Hand-off rows waiting_person through Save hand-off', but Save hand-off (deployed v4) sets waiting_person only when confidence is under the receiving component's threshold; C43's registered receivers are Meeting Prep Writer (threshold 0) and HubSpot (not in the register, so no threshold), so every deadline row is saved as flowed. Making them waiting_person needs a Save hand-off change (e.g. a caller-set status or a registered AE to-do receiver with a threshold) — outside this task.
Note: plan_change: absorbed — Book meeting (action book) writes meeting_source 'factory: AE booking link' even for a meeting picked up from the AE Google Calendar; this automation records the true source (calendar event SRC-16) in the prep-pack hand-off payload and does not override the locked field.
Note: handover: Meeting Handoff and Deadlines books an account through Book meeting, which sets deal_stage engage; Send Rules Check then blocks that account's drafts as open_deal (seen on D-01 after the A-1001 test booking).
Note: assumed: business hours are 09:00-17:00 Monday-Friday in the account's state time zone; 1 business day = 8 business hours; accept_reject applies to booked accounts with meeting_label empty or none; decide_after_meeting runs from the latest calendar event of the account; stale_engage counts from last_touch; Connect 30 and Commit 45 days count from locked_at; reminder at half-window; on a miss escalate to the Geo leader of the pod within 4 business hours, after that to the backup AE.
Note: assumed: hand-offs go from_component C43 to Meeting Prep Writer (prep_pack) and to HubSpot (deadline:&lt;kind&gt;, escalation:&lt;kind&gt;), keyed account_id\|\|play_id so a re-run answers duplicate.
Note: Test effect on seed rows: PF Account A-1001 booked by Book meeting (deal_stage engage, meeting_type intro, meeting_source 'factory: AE booking link', factory_sourced and factory_influenced true, locked_at 1793615191550); Book meeting also saved hand-off H-6ae86557f38e32761818cbb1 (meeting_intro, origin test).
Note: test rows left for Reset demo: PF Component run CR-C43-6ae86556f38e32761818cb81, CR-C43-6ae8656a46920244f3d5adf8, CR-C43-6ae8657dfbdd550a9a509b2d, CR-C43-6ae86592f38e32761818d15a; PF Hand-off H-6ae86557f38e32761818cbb1, H-6ae86558f38e32761818cbc1, H-6ae86558f38e32761818cbc2, H-6ae86558f38e32761818cbc3, H-6ae8656a46920244f3d5ae3b, H-6ae8656a46920244f3d5ae3c, H-6ae8656a46920244f3d5ae3d, H-6ae8656a46920244f3d5ae3e, H-6ae8656a46920244f3d5ae4d, H-6ae8656a46920244f3d5ae50, H-6ae8656a46920244f3d5ae51, H-6ae8656a46920244f3d5ae52 (origin test).
Note: Fix round 1: set distributeWorkflowLoad true on both Call automation (batch) nodes (CHECK_23); score 83 -&gt; 86; re-run 6ae86592f38e32761818d15a COMPLETED with the same idempotent outcome.
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Call automation (batch) x2, Create or update records in bulk · fix would change behaviour (flags the contract input and parameter/field account_id; no DSL switch hides node I/O)
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (x3) · needs object indexes on OBJ_pf_account and OBJ_pf_source outside the task
Note: best practice exception: CHECK_1 Remove unused node outputs to prevent unnecessary delays · Create or update records in bulk · fix would change behaviour (the node is the write the automation exists to make; its output is not needed downstream)
Note: feedback:
Bug: get_workflow_best_practice_report answered HTTP 500 'Workflow execution failed' for a freshly saved automation, then ok on the next call.
Context: [6ae8654d2099302ffb2d9514] version 0, right after compile_and_save_workflow.
Where: platform
Evidence: first call 500 'POST /api/workflow/execute/node failed ... Workflow execution failed'; identical call ~40 s later ok, score 83.
Cause: Unknown — next check: whether the first report build for an unscored version times out.
Regression: the first call right after a save answers ok.

### t10 · Deploy Pipeline Factory · Meeting Handoff and Deadlines

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Meeting Handoff and Deadlines" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Meeting Handoff and Deadlines" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Pipeline Factory · Meeting Handoff and Deadlines".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Meeting Handoff and Deadlines deployed with definitionVersion equal to the saved version.

