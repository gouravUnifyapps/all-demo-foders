---
nebula: 3
specId: "e_6ae86ebdd96c5f6ba244ee86"
mode: "sonic"
title: "Give each list Pipeline Factory · Read component inputs returns its own share of the 12,000-character reply, so drafts a"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "0ff3e3e1-86ff-4c79-b2ea-9b9f9b7fcd94"
pageDesign: 2
createdAt: "2026-11-02T11:06:40.401Z"
runningAt: "2026-11-02T11:06:44.473Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Give each list Pipeline Factory · Read component inputs returns its own share of the 12,000-character reply, so drafts a

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Read component inputs |  | done | 1 |
| t2 | deploy | Pipeline Factory · Read component inputs | t1 | running | 1 |

### t1 · Give each list of Pipeline Factory · Read component inputs its own share of the reply

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Read component inputs" (\`6ae8635446920244f3d5194b\`), its deployed version (narrowed earlier today to answer under 12,000 characters, filling lists in order of importance), code, \`setup\` and \`result\` schema. If its inputs or result field names changed from component_id, account_id, person_id, draft_id, patch_id and component, account, people, signals, facts, drafts, sources, handoffs_in, inboxes, suppression, recent_runs, reason, stop and report.
2. Done when: the reply stays under 12,000 characters in total, but no list can starve another: each list gets its own cap, and a list that needs less leaves its room to the next. Caps (characters): component 1,000; account 800; drafts 2,000 (the draft named by draft_id first, then at most 4 more, body cut to 400); handoffs_in 1,500 (newest 6, payload dropped, evidence cut to 120); facts 1,800 (all of the account's facts, compact: fact_id, kind, text cut to 200, source link, evidence tag); people 1,500 (person_id, name, title, role, tier); sources 1,800 (the account's or person's rows, plus for C29, C30, C42 and C44 the handbook and content assets, body cut to 250); signals 600; suppression 300; inboxes and recent_runs only for the components named before (C35, C38, C39; C48 to C54) within the room left. reason says what each cut list kept (for example 'facts 10 of 13'). For C30 and C18 on A-1001 the reply holds facts F-01 and F-03, the people and the handbook source SRC-19. Same inputs and result fields, deterministic, no model call, read-only.
3. Test it with bounded test runs on the saved draft for C30 with draft_id D-01 on A-1001, C18 on A-1001, C32 with draft_id D-04, C37 on A-1001 with person_id P-1002, and C53 with patch_id PATCH-NAE-03: read each output's length and that facts, people, sources, drafts and handoffs_in each hold rows where the account has them. It writes nothing, so nothing is deleted.
4. Read back: \`open_workflow\` for the saved version, \`describe_callable_workflow\` (inputs unchanged), each test run id with \`inspect_workflow_run\` status, output length and the reason line, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: Test runs answer under 12,000 characters, and for C30 on A-1001 facts, people and sources are not empty while drafts and handoffs_in still hold rows.
Result IDs: {"entity":"6ae8635446920244f3d5194b"}
Read back: Pipeline Factory · Read component inputs 6ae8635446920244f3d5194b: compile_and_save_workflow saved version 5; its change line says 'changed 1 statement (line 561), changed the automation's own description; nothing else moved' (only the Groovy node and the description changed)
Read back: Pipeline Factory · Read component inputs: search_workflows shows version 5, deployment DEPLOYED definitionVersion 4, savedAfterDeploy true. Not deployed here, because the deploy task does that
Read back: Pipeline Factory · Read component inputs: describe_callable_workflow shows the inputs are unchanged: component_id (required), account_id, person_id, draft_id, patch_id, all strings. The result fields are unchanged too (component, account, people, signals, facts, drafts, sources, handoffs_in, inboxes, suppression, recent_runs, reason)
Read back: Pipeline Factory · Read component inputs: per-list caps are measured as the JSON-escaped length (component 1000, account 800, drafts 2000 holding the named draft plus at most 4 more with body cut to 400, handoffs_in 1500 holding the newest 6 with evidence cut to 120, facts 1800 compact with text cut to 200, people 1500, sources 1800 with body cut to 250, signals 600, suppression 300). Room a list leaves unused passes to the next list. Inboxes and recent_runs get what is left of an 11,400 total, and reason is at most 300
Read back: Pipeline Factory · Read component inputs run 6ae86f6b46920244f3d7f7b8 (C30, A-1001, D-01): COMPLETED, reply JSON 11,480 characters. facts F-01..F-10 + 1 (both F-01 and F-03 present), people 11, sources SRC-19, SRC-13, SRC-08, SRC-07, SRC-16, SRC-18, drafts D-01, D-02, D-03, handoffs_in 2. reason 'drafts 3 of 11; handoffs_in 2 of 20; facts 11 of 13; people 11 of 14; sources 6 of 18; signals 2 of 6; suppression 2 of 4'
Read back: Pipeline Factory · Read component inputs run 6ae871c1f38e3276181b8a07 (C18, A-1001): COMPLETED, 11,460 characters. facts F-01..F-10 (F-01 and F-03 present), people 11, sources start with SRC-19 (6 rows), drafts 3, handoffs_in 3. reason 'drafts 3 of 11; handoffs_in 3 of 4; facts 10 of 13; people 11 of 14; sources 6 of 18; signals 3 of 6; suppression 1 of 4'
Read back: Pipeline Factory · Read component inputs run 6ae871c446920244f3d83952 (C32, D-04): COMPLETED, 11,421 characters. Account A-1001 resolved from the draft, drafts D-04 first then D-01, all 13 facts, 14 people, 7 sources, handoffs_in 1. reason 'drafts 2 of 11; sources 7 of 17; signals 2 of 6; suppression 2 of 4'
Read back: Pipeline Factory · Read component inputs run 6ae871c92099302ffb304ef5 (C37, A-1001, P-1002): COMPLETED, 11,466 characters. people starts with P-1002 (14 people), all 13 facts, sources start with P-1002's SRC-13 and SRC-08 (7 rows), drafts 3, handoffs_in empty (OBJ_pf_handoff has 0 rows whose to_component contains C37). reason 'drafts 3 of 11; sources 7 of 17; signals 2 of 6; suppression 2 of 4'
Read back: Pipeline Factory · Read component inputs run 6ae871cb2099302ffb304f5a (C53, PATCH-NAE-03): COMPLETED, 9,831 characters. No account was given, so the account lists are empty. recent_runs 30 of 50 (8,446 characters), reason 'recent_runs 30 of 50'
Read back: Pipeline Factory · Read component inputs: best practice 93 (83 of 85 checks), no fix round needed, version 5
Read back: Pipeline Factory · Read component inputs: security rule 4 (only the fields needed): each list now returns a compact field set (people: person_id, name, title, role, tier; facts: fact_id, kind, text, link, evidence_tag). The automation is still read-only, with 11 fetch_records nodes and no write node
Unverified: Pipeline Factory · Read component inputs: the blank component_id and unknown-component branches were not run again. They were not changed (the change line names only line 561 and the description). Check: run with component_id '' and expect reason 'unknown component'
Unverified: Pipeline Factory · Read component inputs: 'reply length' was measured as the JSON length of the run's response object. A caller that wraps the reply again adds its own characters. Check: read the agent tool call's raw reply length
Unverified: Pipeline Factory · Read component inputs: C53 handoffs_in is empty because 0 OBJ_pf_handoff rows have to_component containing C53 or C37. A row whose to_component holds only the component name, without the id, was not searched. Check: get_records OBJ_pf_handoff filtered on to_component equal to C53's name
Note: assumed: C18 added to the components that get the account-less handbook and content-asset sources (C18, C29, C30, C42, C44). The spec listed only C29, C30, C42 and C44, but its done-when requires SRC-19 for C18 on A-1001. SRC-19 has no account_id, so this was the only way to reach it
Note: assumed: these sources come first, ahead of the person's and the account's own sources (newest first), so SRC-19 is not cut by the 1,800 cap
Note: assumed: facts sorted by fact_id ascending (F-01 first) instead of newest-first, so F-01 and F-03 are kept when the facts cap cuts the list. Fact text is statement, or quote when statement is empty
Note: assumed: account_id dropped from rows in people, facts, sources and signals, because it repeats the requested account and the room is better spent on rows
Note: handover: version 5 is saved but not deployed. Deployment shows definitionVersion 4, savedAfterDeploy true, so the deploy task should deploy version 5
Note: best practice exception: CHECK_2 Disable Input/Output Visibility for Sensitive Fields · Trigger from automation, Execute Groovy code · score already 90 or more
Note: best practice exception: CHECK_86 Object queries in workflow running against unindexed fields · Fetch records (OBJ_pf_component component_id/name), Fetch records (OBJ_pf_component_run run_at) · score already 90 or more; needs object indexes outside the task
Note: trigger_workflow_run with fullValues ['response'] returned about 118,000 characters (every node's inputs and outputs), which went past the tool-result limit, so each run had to be parsed from a saved file

### t2 · Deploy Pipeline Factory · Read component inputs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read component inputs" and the version the automation task saved (from Built so far).
2. Done when: it is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Read component inputs: a share of the reply per list".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read component inputs deployed with definitionVersion equal to the saved version.

