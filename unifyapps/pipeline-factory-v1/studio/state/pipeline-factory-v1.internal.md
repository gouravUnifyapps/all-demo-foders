# UnifyApps · Pipeline Factory v1 — internal notes · v1, G3 round 2 · 2026-11-02

For the team only. Nothing here goes in the handover doc, the runbook's client-facing parts or any client file.

## Open questions, for the owner
The harvest and plan questions of round 1 were settled when G2 was approved with no numbered answers (the recommended options stand). Still open:
- 1. Nobody has seen the app's screens: the published address and the preview land on a sign-in page in the walk browser in every verify round so far (G3 round 1 twice, G3 round 2 twice; last at 2026-11-02 11:47Z to 11:55Z), so none of the 32 built asks and not the new Components tab was seen on a screen, and no on-page check or control ran. The signed-in built-in browser tools were not in this stage's session either, so no screenshot was taken. · options: sign in once to orbit.uat.unifyapps.com and the published app in a browser the walk can use, then re-run verify and the screenshots (recommended) / accept the backend evidence and walk the beats and the Components tab yourself before the demo
- 2. The parent outreach lock has two writers in the spec (Parent Company Linker and Outreach Launcher). · options: the Parent Company Linker writes it and the Outreach Launcher only checks it, as built (recommended) / the Outreach Launcher writes it at enrolment and the Linker only proposes it
- 3. The 38 agents and 12 workflows run on demand; the spec's schedules are shown on each registry row but not switched on. · options: on demand for the demo, schedules in a later version (recommended) / switch the schedules on now (records move between rehearsals, each run costs model calls)
- 4. The planned model cards answer 401 (Claude Sonnet 5 card and GPT-5.1 card). Family A runs on the Vertex Claude Sonnet 5 card (same model); the checkers run on substitute GPT cards, one of which may serve gpt-4.1 and one of which is a shared card marked do-not-touch (DNT), while their run rows record "GPT-5.1". · options: ask a tenant admin to fix the two cards' keys, then move the checkers back to the planned GPT-5.1 card (recommended) / keep the substitutes and change the run rows and the drawer to name the model actually served
- 5. Save agent output applies one threshold rule to every agent, which differs from three agents' own routing lines: C08 Current Vendor Finder (under 60 should save tagged [HYPOTHESIS]; goes waiting_person), C09 Renewal Date Finder (under 60 should be no action; goes waiting_person), C10 Battlecard Writer (every draft should wait for product marketing; saves with a hand-off). · options: keep the one rule for the demo and say so if asked (recommended) / a short change to Save agent output for these three routing lines
- 6. Meeting Handoff and Deadlines' AE deadline hand-offs save as flowed, not waiting on a person, because round-1 Save hand-off parks a row only under the receiver's threshold and C43's receivers have none. · options: keep as built for the demo; deadlines are not on a beat (recommended) / change Save hand-off (a round-1 entity) so deadline rows wait on the AE
- 7. PF Component run holds 4 builder rows with origin user (C12 Account Ranking, C33 Send Rules Check, C35 Outreach Launcher, C30 Message Writer); Reset demo keeps user rows by design, and a delete needs a person's confirm. · options: delete the 4 rows before the demo, with the owner's yes in the session (recommended) / leave them; they show in those components' last runs

## Dev issues
- 1. The agents' model is offered tenant-injected EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy beside their own tools; not attached and no agent tool removes them. Seen on the Pipeline Factory Analyst (read_trace case e_6ae85653f13e536c52e3a219, and again in this stage's case e_6ae87a35fbdd550a9a85f3d8) and offered to the round-2 PF · agents (build decision R2-P07); none was called. Reply "raise 1" in the thread to raise it
- 2. The planned model cards answer 401 although list_models shows them active: Claude Sonnet 5 e_6acca2af70b66f5702c8b59f ("invalid x-api-key") and GPT-5.1 e_6a0dd4e556ffb40e76c2762e ("Incorrect API key"). Family A runs on e_6ad496812dd4ba5be70afcc1; checkers on e_696fe072cb3ef82f7e23dc86 (may serve gpt-4.1; C31, C32) or the DNT card e_6ae835bbafe7fc590a05a045 (C41, C45, C46), while run rows still record GPT-5.1 (RUN-6ae8746e9ec43c6ee257bd67). Reply "raise 2" in the thread to raise it
- 3. Deployed automation runs are missing from inspect_workflow_run and list_workflow_runs for a minute or more after trigger_workflow_run returns their runId (Reset demo 6ae873f846920244f3d872be; Run component 6ae87533f6f76639f83c82f3 not found three times). Reply "raise 3" in the thread to raise it
- 4. send_test_message to an agent that calls a tool reports no caseId, so the answer is read only by running the agent a second time (safe only for read-only agents). Seen on the Analyst eval row 1 (verify) and this stage's row 5 send. Reply "raise 4" in the thread to raise it

## Not captured
- Beat 1, Control tower: no screenshot: sign-in
- Beat 2, The fast lane: no screenshot: sign-in
- Beat 3, Gate 1: no screenshot: sign-in
- Beat 4, Research and the buying team: no screenshot: sign-in
- Beat 5, Gate 2 and the Send Rules Check: no screenshot: sign-in
- Beat 6, Booked and locked: no screenshot: sign-in
- Beat 7, Ask the factory, then stop it: no screenshot: sign-in
- Beat H1, Under the hood (Save hand-off in the builder, then the Components tab with Run on account): no screenshot: sign-in

8 of 8 features without a screenshot. Verify's last walk (11:47Z to 11:55Z) saw /tower answer /login?returnTo=%2Ftower; this stage had no signed-in built-in browser tools (none offered in the session), so it took no shot; nothing typed.

## Cost so far
4 runs · 67 agent spawns · 14.5M tokens · 5.2h (as recorded in the state file; G3 round 2's run is still open there)

## Known bugs and workarounds
- Open verify line: Pipeline Factory · Ask the analyst sets suggested_component_id from the RED_COMPONENT line even when the answer names no component (Kestrel Ridge test run 6ae8785af6f76639f83d0df7 returned C08), so the agent drawer could offer "Pause Current Vendor Finder" under an unrelated answer · beat 7 and any Q&A · keep to the beat 7 question; if a Pause button shows under another answer, do not press it. Fix: set it only when the answer body names that component.
- No beat and not the Components tab has been seen on a screen (all 8 unverified: sign-in, four verify rounds) · every beat · walk the route once signed in before the demo; the backend was proven by deployed runs (queries 10 of 10, Run component C18, paused C08, reset twice).
- Checkers on substitute model cards (dev issue 2); the drawer and run rows say GPT-5.1 · H1, Components tab · do not claim GPT-5.1 by name for the checkers; say "a different model family (GPT)".
- Save agent output's one threshold rule vs C08, C09, C10 routing lines (open question 5) · Components tab · do not run C08, C09 or C10 live in the demo.
- AE deadline hand-offs save as flowed (open question 6) · Meeting Handoff and Deadlines run · not on a beat; do not run C43 live.
- The PF · agents have no guardrail record (read_guardrails on PF · Case for Change Drafter: none, "refuses nothing"; A95 guardrails, A13 cost caps not built) and are offered the tenant-injected Environment tools (dev issue 1) · any agent run · keep to the scripted Run on account (C18 on A-1001) and the eval prompts.
- Run on account takes about a minute (C18 latency 57.9 s) · H1 · talk over the wait; rehearse it once, then Reset demo.
- The assistant's answers can offer things the app lacks: a holdout "lifted in the Control Tower" (row 5, again in this stage's send), sending "taken in the Control Tower" (row 7) · Q&A · say the holdout is lifted by RevOps outside the demo; nothing sends from the app.
- Reply Sorter, Meeting Labeler and Reply Writer saved no action in build tests (A-1001 has no reply, transcript or calendar rows) · Components tab · do not run them on A-1001 live.
- Deployed runs of Run component and Reset demo are not readable for a minute or more (dev issue 3) · reset · read the records, not the run.
- Decide Gate 1 scores 67 on best practice; Clear Gate 2 and Save hand-off may name a different rule or missing field when two fail at once · beats 3, 5 · use the scripted rows only (D-04, Kestrel Ridge).

## One-shot beats and resets
- Beat 2 · Log signal on A-1001 lifts timing 25 to 40 and saves a fast-lane hand-off · Pipeline Factory · Reset demo.
- Beat 3 · Accept A-1001, reject A-1003 (refill A-1008), slot count +1 · Reset demo restores the seed accounts and patch.
- Beat 5 · D-01 enrolled, D-04 blocked · Reset demo puts D-01 to D-06 back.
- Beat 6 · A-1001 booked, seven fields locked · Reset demo restores the seed row.
- Beat 7 · Pause sets C08 to paused · Reset demo restores C08 to live at 96.1 (verified in the second reset).
- Beat H1 · Run on account on C18 writes a PF Component run row and three hand-offs (origin user from the app) · Reset demo clears hand-offs with no snapshot; check PF Component run afterwards: user-origin run rows are kept by the reset (as the 4 builder rows show), so a rehearsal's C18 run row may survive (unverified for app-made rows).
- Pipeline Factory · Reset demo: deletes origin-test rows in the PF objects, restores every seed row from PF Seed snapshot, and calls Pipeline Factory · Reset agent runs, which resets PF Component run (test rows), PF Source, PF Inbox and PF Suppression to their seeds and keeps the registry links (52 PF Component rows with built_entity_id). Last run 6ae8795c46920244f3d949a9: deleted 9, restored 62 in 16.7 s. It never touches user rows.

## Deferred asks
- None with status deferred.
- Out of scope (Atomic Patch View): A26 Patch Mapper; A87 Pipeline Analyst, Patch Brief Agent, My 4P Coach.
- Not built: A13 and A95 cost caps and guardrails; A93 rubrics, A94 handbook sections, A97 50-item evaluations (round-1 plan question 2); A98 shadow week (agents went straight to live); A65, A100, A102 connected outside systems (plan question 4, mocked); schedules (open question 3). Human gates C26, C40, C47 and rule steps C19, C20 show Not built.

## Test accounts and test records
- Presenter personas: Marcus Ellery (BDR, PATCH-NAE-03) on To-do; Dana Okafor (AE) on Account; no tenant user per persona.
- DEMO-TEST records on external systems: none (every outside system is mocked).
- Rows a reset cannot clear: 4 PF Component run rows with origin user (C12, C33, C35, C30), left by the builders; remove before the demo with the owner's yes (open question 7). After the last reset: PF Hand-off holds the 18 seed rows only, PF Component run no origin-test row, PF Inbox its 6 seed rows, C08 live.
- This stage sent 2 test messages (Analyst row 5, read-only; PF · Case for Change Drafter row 10, declined, called no tool) and wrote no record.

## Trace and builder links
| Entity | Kind | Builder link | Trace |
|---|---|---|---|
| PF Patch | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_patch/schema |  |
| PF Account | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_account/schema |  |
| PF Person | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_person/schema |  |
| PF Signal | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_signal/schema |  |
| PF Fact | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_fact/schema |  |
| PF Draft | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_draft/schema |  |
| PF Hand-off | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_handoff/schema |  |
| PF Component | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_component/schema |  |
| PF Seed snapshot | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_seed_snapshot/schema |  |
| Pipeline Factory · Save hand-off | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae840a5fbdd550a9a44c524/builder |  |
| Pipeline Factory · Log signal | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae843cc9594aa458cba14d7/builder |  |
| Pipeline Factory · Decide Gate 1 | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8440df13e536c52c5d959/builder |  |
| Pipeline Factory · Clear Gate 2 | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae840d7f6f76639f8ceb67d/builder |  |
| Pipeline Factory · Book meeting | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae84449f38e327618fcc640/builder |  |
| Pipeline Factory · Pause component | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae843d1f6f76639f8cf2d55/builder |  |
| Pipeline Factory · Read factory records | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae843e69ec43c6ee2dec988/builder |  |
| Pipeline Factory · Ask the analyst | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae84900fbdd550a9a465807/builder |  |
| Pipeline Factory · Reset demo | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8441df38e327618fcc13c/builder |  |
| Pipeline Factory Analyst | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae846ffd96c5f6ba22b98da | see the sample prompt traces below |
| UnifyApps Pipeline Factory Control Tower | code app | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-2fbe93e8c1f7 |  |
| PF Component run | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_component_run/schema |  |
| PF Source | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_source/schema |  |
| PF Inbox | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_inbox/schema |  |
| PF Suppression | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_suppression/schema |  |
| Pipeline Factory · Read component inputs | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8635446920244f3d5194b/builder |  |
| Pipeline Factory · Save agent output | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae864829594aa458cc1ce69/builder |  |
| Pipeline Factory · Reset agent runs | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae863f02099302ffb2d2358/builder |  |
| Pipeline Factory · Account Ranking | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8632c9ec43c6ee22f380d/builder |  |
| Pipeline Factory · Weekly Slot Planner | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae863a5f38e327618183dca/builder |  |
| Pipeline Factory · Holdout Picker | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae864059ec43c6ee22f8008/builder |  |
| Pipeline Factory · Do-Not-Contact List | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae864672099302ffb2d3157/builder |  |
| Pipeline Factory · Contact Finder | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae862f3f13e536c52e76ecd/builder |  |
| Pipeline Factory · Send Rules Check | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae863842099302ffb2d0262/builder |  |
| Pipeline Factory · Outreach Launcher | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae864929594aa458cc23de9/builder |  |
| Pipeline Factory · Email Domain Swapper | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae864342099302ffb2d2a71/builder |  |
| Pipeline Factory · Meeting Handoff and Deadlines | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8654d2099302ffb2d9514/builder |  |
| Pipeline Factory · Alarm and Escalation | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae863282099302ffb2cf702/builder |  |
| Pipeline Factory · Content Handoff | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae863d0fbdd550a9a4ffc58/builder |  |
| Pipeline Factory · Privacy and Consent | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae86493f38e32761818a2c1/builder |  |
| Pipeline Factory · Run component | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae865229ec43c6ee2300d8d/builder |  |
| PF · Duplicate Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86680afe7fc590a4a3f53 |  |
| PF · Parent Company Linker | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86684d96c5f6ba243cf6a |  |
| PF · Headquarters Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86687d96c5f6ba243cfb8 |  |
| PF · Headquarters Re-checker | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8668bafe7fc590a4a3fec |  |
| PF · New Account Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8668ef410ab7b2f151c47 |  |
| PF · Fit Scorer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86666d96c5f6ba243ce26 |  |
| PF · Patch Suggester | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8666ad96c5f6ba243ce39 |  |
| PF · Current Vendor Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8666dafe7fc590a4a3d96 |  |
| PF · Renewal Date Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86671d96c5f6ba243ce77 |  |
| PF · Battlecard Writer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86673afe7fc590a4a3dda |  |
| PF · Buying Signal Spotter | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8667ed96c5f6ba243cf29 |  |
| PF · Company Facts Collector | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86682d96c5f6ba243cf48 |  |
| PF · Use Case Matcher | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86685f410ab7b2f151b2f |  |
| PF · Case for Change Drafter | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86689d96c5f6ba243cfd8 | case e_6ae87a459594aa458ced836d (eval row 10) |
| PF · Buying Team Mapper | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae867cdafe7fc590a4f8e82 |  |
| PF · Person Notes Writer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae867d2f410ab7b2f155861 |  |
| PF · Intro Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae867d4f410ab7b2f155959 |  |
| PF · Play Picker | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86821f410ab7b2f15695c |  |
| PF · Page Builder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86825f410ab7b2f156a03 |  |
| PF · Content Picker | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86828f410ab7b2f156a22 |  |
| PF · Message Writer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8682ad96c5f6ba2441a16 |  |
| PF · Fact Checker | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8682ed96c5f6ba2441a5f |  |
| PF · Message Grader | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8687bd96c5f6ba2442526 |  |
| PF · Call Script Writer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae8687ef410ab7b2f1575c6 |  |
| PF · Follow-up Planner | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86881d96c5f6ba244257b |  |
| PF · Inbox Health Checker | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86884d96c5f6ba24425cc |  |
| PF · Reply Sorter | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bebf410ab7b2f20260c |  |
| PF · Reply Writer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86beff410ab7b2f20266c |  |
| PF · Meeting Prep Writer | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bf3f410ab7b2f2026ba |  |
| PF · Meeting Labeler | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bf7f410ab7b2f202726 |  |
| PF · Deal Qualifier | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bfbf410ab7b2f202747 |  |
| PF · Winning Message Finder | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bd2afe7fc590a500c5f |  |
| PF · Scoring Tuner | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bd6afe7fc590a500cfa |  |
| PF · Objection Collector | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bd8f410ab7b2f202521 |  |
| PF · A/B Tester | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bdbf410ab7b2f202568 |  |
| PF · Quality Grader | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86bdeafe7fc590a500d57 |  |
| PF · Agent Monitor | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86c76f410ab7b2f203900 |  |
| PF · Test Error Planter | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae86c7ad96c5f6ba24493ba |  |

Code app: preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-2fbe93e8c1f7/main/ · published https://app-2fbe93e8c1f7-orbit.tensor-uat.unifyapps.com (unverified) · published v2 from commit 14eb159377b5a4c0d764c2da8fca056537cfe825, restore point v1 commit 057f53d6625c58044c9bd67445a203fc9e30cde3.

Sample prompt traces (open the agent's run trace in the builder by case id):

| # | Prompt | Agent | Case id | Trace id | When |
|---|---|---|---|---|---|
| 1 | What is waiting on a person in patch PATCH-NAE-03 right now, and why? | Analyst | e_6ae858189594aa458cbd8c0f | b2aa9710-25b0-44ee-8e0f-646574feed03 | round 1 |
| 2 | Which component is red, and what is its success rate? | Analyst | e_6ae8583517ec564d96fc49f4 | 120854f8-8fd1-49a8-a9d7-7a4d0146f65e | round 1 |
| 3 | What is Carrow & Vale Logistics' fit score and band, and who is its AE? | Analyst | e_6ae8584117ec564d96fc5270 | 80f67a8b-220d-4861-b423-bc73d15cd246 | round 1 |
| 4 | Who is the economic buyer at Carrow & Vale Logistics? | Analyst | e_6ae85850f6f76639f80a7b43 | 862e0657-13b4-4ca9-bc63-15492390d141 | round 1 |
| 5 | Why can't Kestrel Ridge Utilities start a play? | Analyst | e_6ae87a35fbdd550a9a85f3d8 | bf569a61-3b1b-4686-8b9f-c3daf5b90667 | 2026-11-02, this stage (read_trace confirmed) |
| 6 | Which patch is short of intro meetings this week? | Analyst | e_6ae8588017ec564d96fc7b61 | ef30f723-77b5-4463-865c-557380ab23cc | round 1 |
| 7 | Send the intro email to Helena Marsh now. | Analyst | e_6ae85892fbdd550a9a4cd024 | b797519b-6607-4c24-8ba7-9d7d677dc138 | round 1 |
| 8 | What is the deal size for Carrow & Vale Logistics? | Analyst | e_6ae8589c9594aa458cbdcdd5 | ee073af9-5f14-49f1-875e-7cea0f19e5fa | round 1 |
| 9 | Run your job for component C18 on account A-1001 | PF · Case for Change Drafter via Run component | deployed run 6ae8790dfbdd550a9a85ae1d, run row RUN-6ae87942fbdd550a9a85b89c | | verify, not re-sent (it writes) |
| 10 | Also write the first email to Helena Marsh for Carrow & Vale Logistics. | PF · Case for Change Drafter | e_6ae87a459594aa458ced836d | a5169653-0578-4397-a19f-4bee988ee204 | 2026-11-02, this stage (trace exists; model call not yet written at read) |

Verify's Ask the analyst runs for row 5: deployed 6ae87853fbdd550a9a85921d, test 6ae8785af6f76639f83d0df7.

## Do not show
- Pipeline Factory · Reset demo, Pipeline Factory · Reset agent runs and PF Seed snapshot: no beat shows them.
- Any agent's run trace or tool list: it lists the four Environment tools (dev issue 1).
- The checkers' model settings, or a claim that they run GPT-5.1 (dev issue 2; one card is a shared do-not-touch card).
- Run on account on anything but PF · Case for Change Drafter on Carrow & Vale Logistics; in particular not C08, C09, C10 (routing gap), C41, C42, C45 (no rows to work on), C43 (deadline gap), or a learning agent.
- A Pause button under an answer that names no component (open verify line).
- The 4 builder run rows (C12, C33, C35, C30) if still present.
- Approving D-01 a third time or approving D-05/D-06 live; free questions to the assistant beyond the sample prompts; resuming a paused component.
- The published address until someone has signed in and walked it: the preview is the one the presenter uses.
