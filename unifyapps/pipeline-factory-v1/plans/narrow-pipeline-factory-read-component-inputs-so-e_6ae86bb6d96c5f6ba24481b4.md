---
nebula: 3
specId: "e_6ae86bb5afe7fc590a500ad8"
mode: "sonic"
title: "Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the f"
owner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
touches: [{"kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "60960e92-7827-4348-a744-1c5d39da4ff0"
pageDesign: 2
createdAt: "2026-11-02T10:53:42.498Z"
runningAt: "2026-11-02T10:53:46.147Z"
runner: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"ac6dc8fd-1e9e-54b2-abbf-69b907d4f5c1"}
---
## Plan

Goal: Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the f

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Pipeline Factory · Read component inputs |  | running | 1 |
| t2 | deploy | Pipeline Factory · Read component inputs | t1 | pending | 0 |

### t1 · Narrow Pipeline Factory · Read component inputs to fit an agent's tool reply

Body:
1. Read: \`open_workflow\` for "Pipeline Factory · Read component inputs" (\`6ae8635446920244f3d5194b\`), its saved and deployed versions, code, \`setup\` and \`result\` schema; \`describe_callable_workflow\` for its inputs. If its inputs or result field names differ from component_id, account_id, person_id, draft_id, patch_id and component, account, people, signals, facts, drafts, sources, handoffs_in, inboxes, suppression, recent_runs, reason, stop and report.
2. Done when: the same inputs and result fields (names and types unchanged) answer under 12,000 characters in total for component C32 on account A-1001 and for every other component on A-1001, because the AI agent runtime keeps only the first 16,000 and last 2,000 characters of a tool reply (today A-1001 answers about 200,000). The rules: each JSON list holds only the fields an agent needs (ids, names, status, confidence, short text fields cut to 300 characters; no payload or row_values blobs; no system fields); the lists come in this order of importance and the rest of the reply budget goes to them in that order: component, account, drafts (the draft named by draft_id first, else the account's drafts, at most 10), handoffs_in (this component's, for the account when given, newest 10), sources (the account's or person's, plus rows with no account only when the component is C29, C30, C42 or C44 for content assets and the handbook, at most 10), signals (newest 10), facts (at most 10), people (the person named by person_id first, at most 13), suppression (only the person's or account's rows); inboxes only for C38, C39 and C35 (else an empty list); recent_runs only for C48 to C54 (the newest 30, compact: run_id, component_id, status, confidence, output_type, summary cut to 120 characters, run_at), else an empty list. A list that is cut says so in reason (for example 'sources cut to 10 of 19'). Deterministic, no model call, read-only.
3. Test it with bounded test runs on the saved draft for C32 with draft_id D-04 on A-1001, C37 on A-1001 with person_id P-1002, C08 on A-1001, C53 with patch_id PATCH-NAE-03, and an unknown component: read each run's output length and that the draft, sources and handoffs_in each component needs are present. It writes nothing, so no test rows are made and nothing is deleted.
4. Read back: \`open_workflow\` for the saved version and its \`result\` schema, \`describe_callable_workflow\` for its inputs (unchanged), each test run's id with \`inspect_workflow_run\` status and the character length of its output, and the best practice score from \`get_workflow_best_practice_report\`. Do not deploy: the deploy task does.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: Test runs of Pipeline Factory · Read component inputs answer under 12,000 characters for C32 on A-1001 with D-04 present, and the result fields are unchanged.

### t2 · Deploy Pipeline Factory · Read component inputs

Body:
1. Read: \`search_workflows\` for "Pipeline Factory · Read component inputs" and the version the automation task saved (from Built so far).
2. Done when: "Pipeline Factory · Read component inputs" is deployed, its \`deployment.status\` live and \`definitionVersion\` equal to the version the automation task saved.
3. Apply \`deploy_workflow\` once with deploymentNotes "Demo Studio · Pipeline Factory v1 · G3 round 2 · Read component inputs narrowed for the agents' tool reply".
4. Read back: \`search_workflows\` for its \`deployment\` (\`status\`, \`deployedVersion\`, \`definitionVersion\`, \`deployedAt\`), quoted.
5. Report ids (the workflowId as \`ids.entity\`), readBack, unverified, notes.

Proof: search_workflows shows Pipeline Factory · Read component inputs deployed with definitionVersion equal to the saved version.

