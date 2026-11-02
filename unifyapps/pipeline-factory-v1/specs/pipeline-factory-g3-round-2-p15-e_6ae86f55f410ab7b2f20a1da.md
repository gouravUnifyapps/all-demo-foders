---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory · G3 round 2 · P15"
touches: [{"kind":"object","name":"PF Component","id":"OBJ_pf_component"},{"kind":"object","name":"PF Seed snapshot","id":"OBJ_pf_seed_snapshot"},{"kind":"code-app","name":"UnifyApps Pipeline Factory Control Tower","id":"app-2fbe93e8c1f7"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"code-app","name":"UnifyApps Pipeline Factory Control Tower","id":"app-2fbe93e8c1f7"}]
acceptedAt: "2026-11-02T11:09:07.439Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae86f58d96c5f6ba244fc4d"]
latestPlanId: "e_6ae86f58d96c5f6ba244fc4d"
planId: "e_6ae86f58d96c5f6ba244fc4d"
---
# Pipeline Factory · G3 round 2 · P15

## Requested outcome
The manager asked to build all 38 agents and 12 workflows (feedback FB-1793612784906-1); they are built. This plan points each PF Component registry row at the entity that runs it, keeps those links through a reset, and shows them on the control tower's Components tab with a Run on account control, then publishes the app.

## Touches
- object · PF Component · OBJ_pf_component
- object · PF Seed snapshot · OBJ_pf_seed_snapshot
- code-app · UnifyApps Pipeline Factory Control Tower · app-2fbe93e8c1f7

## Contract
### object · PF Component
Each registry row points at the entity that runs it.
- record · update · PF Component: after every deploy and publish of R2-P02 to R2-P14 (it reads the ids they report), on the seeded rows, origin stays seed: the 38 agent rows (C01 to C11, C16 to C18, C21 to C23, C27 to C32, C36 to C38, C41, C42, C44 to C46, C48 to C54) get built_kind ai_agent, built_entity_id the agent's id, built_entity_name "PF · `name`", built_link https://orbit.uat.unifyapps.com/p/0/ai-agents/`id`, built_status live, status live, built_at the publish time; the 12 workflow rows (C12, C13, C14, C24, C25, C33, C35, C39, C43, C55, C56, C57) get built_kind automation, the automation's id, name "Pipeline Factory · `name`", built_link https://orbit.uat.unifyapps.com/p/0/automations/`id`/builder, built_status live, status live, built_at the deploy time; C15 Gate 1 gets built_kind automation, Pipeline Factory · Decide Gate 1 (6ae8440df13e536c52c5d959) and C34 Gate 2 gets Pipeline Factory · Clear Gate 2 (6ae840d7f6f76639f8ceb67d), the round-1 automations behind those gates; C26, C40, C47 (human gates) and C19, C20 (rule steps) stay not_built. C08 Current Vendor Finder keeps success_rate 96.1. Every other field stays as seeded.

### object · PF Seed snapshot
The snapshot keeps the links, so a reset restores them.
- record · update · PF Seed snapshot: the 57 PF Component snapshot rows' row_values are rewritten to the rows as the line above leaves them (with the built-entity fields), so Pipeline Factory · Reset demo restores the links, never blanks them.

### code-app · UnifyApps Pipeline Factory Control Tower
The Components tab shows each component's built entity and runs it on an account.
- code-app · update · UnifyApps Pipeline Factory Control Tower: screen Control tower, Components tab only (no new page, no other screen changes): the PF Component .tbl gains a Built column (.tag "AI agent" or "Automation" with the entity name as a link to built_link, opening in a new tab; a muted .tag "Not built" for human gates and rule steps) and a built kind facet in its .toolbar (AI agent, Automation, Not built); the component .drawer gains the built entity's name and link, its model (Claude Sonnet 5 for family A, GPT-5.1 for family B, none for a workflow), its last five PF Component run rows (output type, status .tag, confidence of threshold, model, latency) and a Run on account control: a .ctl select of PF Account (default A-1001 Carrow & Vale Logistics) and .btn-s Run, disabled with a .note when the component is paused or not built; the result as a .toast (result, confidence, summary) and the new hand-off at the top of the .feed · reads PF Component, PF Component run, PF Account · calls Pipeline Factory · Run component on Run with origin user

## Business rules
- A paused component runs nothing: Run component answers paused.
- Human gates C26, C40, C47 and rule steps C19, C20 are not built and cannot be run.
- Every call from the app sends origin user.

## Ready when
- The Components tab shows 38 rows Built · AI agent and 12 rows Built · Automation, each linking to its live entity; Gate 1 and Gate 2 link to Decide Gate 1 and Clear Gate 2; the other three human gates and the two rule steps show Not built.
- publish UnifyApps Pipeline Factory Control Tower

## Assumptions
- Check this: release line of the profile: publish and deploy without asking; visibility PRIVATE.
- Check this: built_at is the time this plan writes the row (the publish and deploy times are within the hour before).
