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
| t1 | automation | Pipeline Factory · Read component inputs |  | running | 1 |
| t2 | deploy | Pipeline Factory · Read component inputs | t1 | pending | 0 |

### t1 · Give each list of Pipeline Factory · Read component inputs its own share of the reply

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Read component inputs" (\`6ae8635446920244f3d5194b\`), its deployed version (narrowed earlier today to answer under 12,000 characters, filling lists in order of importance), code, \`setup\` and \`result\` schema. If its inputs or result field names changed from component_id, account_id, person_id, draft_id, patch_id and component, account, people, signals, facts, drafts, sources, handoffs_in, inboxes, suppression, recent_runs, reason, stop and report.
2. Done when: the reply stays under 12,000 characters in total, but no list can starve another: each list gets its own cap, and a list that needs less leaves its room to the next. Caps (characters): component 1,000; account 800; drafts 2,000 (the draft named by draft_id first, then at most 4 more, body cut to 400); handoffs_in 1,500 (newest 6, payload dropped, evidence cut to 120); facts 1,800 (all of the account's facts, compact: fact_id, kind, text cut to 200, source link, evidence tag); people 1,500 (person_id, name, title, role, tier); sources 1,800 (the account's or person's rows, plus for C29, C30, C42 and C44 the handbook and content assets, body cut to 250); signals 600; suppression 300; inboxes and recent_runs only for the components named before (C35, C38, C39; C48 to C54) within the room left. reason says what each cut list kept (for example 'facts 10 of 13'). For C30 and C18 on A-1001 the reply holds facts F-01 and F-03, the people and the handbook source SRC-19. Same inputs and result fields, deterministic, no model call, read-only.
3. Test it with bounded test runs on the saved draft for C30 with draft_id D-01 on A-1001, C18 on A-1001, C32 with draft_id D-04, C37 on A-1001 with person_id P-1002, and C53 with patch_id PATCH-NAE-03: read each output's length and that facts, people, sources, drafts and handoffs_in each hold rows where the account has them. It writes nothing, so nothing is deleted.
4. Read back: \`open_workflow\` for the saved version, \`describe_callable_workflow\` (inputs unchanged), each test run id with \`inspect_workflow_run\` status, output length and the reason line, and the best practice score. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: Test runs answer under 12,000 characters, and for C30 on A-1001 facts, people and sources are not empty while drafts and handoffs_in still hold rows.

### t2 · Deploy Pipeline Factory · Read component inputs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read component inputs" and the version the automation task saved (from Built so far).
2. Done when: it is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Read component inputs: a share of the reply per list".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read component inputs deployed with definitionVersion equal to the saved version.

