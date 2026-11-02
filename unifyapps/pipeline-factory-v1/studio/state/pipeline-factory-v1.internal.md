# UnifyApps · Pipeline Factory v1 — internal notes · v1 · 2026-11-02

For the team only. Nothing here goes in the handover doc, the runbook's client-facing parts or any client file.

## Open questions, for the owner
The harvest and plan questions were settled when G2 was approved with no numbered answers (the recommended options stand). One is still open:
- 1. Nobody has seen the app's screens: the published address and the preview both land on a sign-in page in the walk browser (verify rounds 1 and 2, and this stage's try at 09:29Z), so none of the 32 built asks was seen on a screen and no on-page check or control ran. · options: sign in once to orbit.uat.unifyapps.com and the published app in a browser the walk can use, then re-run verify and the screenshots (recommended) / accept the backend evidence and walk the eight beats yourself before the demo

## Dev issues
- 1. The Pipeline Factory Analyst's model is offered EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy beside think, ClarifyFromUser and ReadFactoryRecords; they are not attached to the agent and no agent tool removes them (tenant-injected). Seen in read_trace case e_6ae85653f13e536c52e3a219 (eval row 4, round 2); none was called. Not raised yet; reply "raise 1" in the thread to raise it

## Not captured
- Beat 1, Control tower: no screenshot: sign-in
- Beat 2, The fast lane: no screenshot: sign-in
- Beat 3, Gate 1: no screenshot: sign-in
- Beat 4, Research and the buying team: no screenshot: sign-in
- Beat 5, Gate 2 and the Send Rules Check: no screenshot: sign-in
- Beat 6, Booked and locked: no screenshot: sign-in
- Beat 7, Ask the factory, then stop it: no screenshot: sign-in
- Beat H1, Under the hood (automation builder): no screenshot: sign-in (the builder canvas needs the tenant sign-in)

The published address https://app-2fbe93e8c1f7-orbit.tensor-uat.unifyapps.com/tower redirected to /login?returnTo=%2Ftower at 2026-11-02 09:29Z; nothing typed.

## Cost so far
2 runs · 2 agent spawns · 0.42M tokens · 0.7h (as recorded in the state file; this G3 run's own spawns are not yet added)

## Known bugs and workarounds
- No beat has been seen on a screen (all 8 unverified: sign-in) · every beat · walk the whole route once, signed in, before the demo; the backend for beats 2, 3, 5 and 7 was proven by deployed runs in verify round 2.
- Reset demo's reported counts read 0 deleted, 0 restored on a run that did clear rows · after a reset · trust the records, not the counts: check PF Hand-off holds exactly H-01 to H-18 and A-1001 reads timing 25, Gate 1 pending.
- The app passes origin "user" on every action (Log signal, Decide Gate 1, Clear Gate 2, Book meeting, Pause component), and Reset demo never touches user rows. Hand-offs with no snapshot are cleared (verify round 2 saw them go), but a PF Signal or other non-hand-off row created during a rehearsal may survive the reset (unverified) · beat 2 (a new PF Signal row per Log signal) · after each rehearsal, check PF Signal holds only S-01 to S-09; if not, remove the extras on the tenant by hand with the owner's yes.
- The assistant sometimes offers things the app does not have: in the Kestrel Ridge answer it says a holdout "can be lifted" in the Control Tower (no such control); in the send refusal it says sending "must be taken in the Control Tower" (the app only enrols into a mocked sequence) · beat 7 and the Q&A · keep to the beat 7 prompt; if asked, say the holdout is lifted by RevOps outside the demo.
- Shorter answers on rows 3 and 4 this run: row 3 named fit 49, best, Dana Okafor but not the backup AE or BDR; row 4 named Helena Marsh (CFO) but not the gatekeeper · Q&A · the expected facts are on the Account screen.
- The slowest answer was about 50 s (beat 7's question) · beat 7 · pre-send the question once before the demo, and talk over the wait.
- The Analyst is offered four Environment* tools it should not see (dev issue 1) · beat 7 · none was called; no workaround needed on the day.
- Decide Gate 1 scores 67 on best practice (lowest of the automations); Clear Gate 2 and Save hand-off may name a different rule or missing field when two fail at once (build note) · beats 3, 5 · use the scripted rows only (D-04 for the refusal, Kestrel Ridge for the hold-out).

## One-shot beats and resets
- Beat 2 · Log signal on A-1001 lifts timing 25 to 40 and saves a fast-lane hand-off · run Pipeline Factory · Reset demo (restores A-1001 to timing 25 and clears hand-offs with no snapshot; check PF Signal as above).
- Beat 3 · Accept A-1001, reject A-1003 (refill A-1008), slot count +1 · Reset demo restores the seed accounts and patch.
- Beat 5 · D-01 enrolled, D-04 blocked · Reset demo puts D-01 to D-06 back to waiting at Gate 2.
- Beat 6 · A-1001 booked, seven fields locked · Reset demo restores the seed row (locked_at cleared).
- Beat 7 · Pause sets Current Vendor Finder (C08) to paused and holds its hand-offs · Reset demo restores C08 to its seeded status and success rate 96.1.
- Pipeline Factory · Reset demo: deletes origin-test rows in the nine PF objects, puts every seed row back from PF Seed snapshot, never touches user rows; run it before every run-through. No delete is needed by a person for seed or test rows.

## Deferred asks
- None with status deferred.
- Out of scope (other use case, Atomic Patch View): A26 Patch Mapper; A87 Pipeline Analyst, Patch Brief Agent, My 4P Coach.
- Open, not built live (seeded registry rows or owner's question): A3, A15 to A20, A22 to A25, A43 to A46, A49 to A86, A88 to A102, A103 and A104 shown by beat 1 only. A93, A94, A97 wait on plan question 2; A65, A100, A102 on plan question 4 (outside systems mocked).

## Test accounts and test records
- Presenter persona: Marcus Ellery (BDR, PATCH-NAE-03) on To-do; Dana Okafor (AE) on Account. Personas only, no tenant user per persona; the presenter signs in as themself.
- DEMO-TEST records on external systems: none (every outside system is mocked).
- origin test rows a reset could not clear: none at verify round 2's last read (PF Hand-off exactly H-01 to H-18, all seed; no non-seed PF Signal).
- This stage sent 8 test questions to the Analyst (read-only; no records written).

## Trace and builder links
| Entity | Kind | Builder link | Trace |
|---|---|---|---|
| PF Patch | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_patch/schema | |
| PF Account | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_account/schema | |
| PF Person | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_person/schema | |
| PF Signal | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_signal/schema | |
| PF Fact | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_fact/schema | |
| PF Draft | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_draft/schema | |
| PF Hand-off | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_handoff/schema | |
| PF Component | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_component/schema | |
| PF Seed snapshot | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_pf_seed_snapshot/schema | |
| Pipeline Factory · Save hand-off | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae840a5fbdd550a9a44c524/builder | |
| Pipeline Factory · Log signal | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae843cc9594aa458cba14d7/builder | |
| Pipeline Factory · Decide Gate 1 | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8440df13e536c52c5d959/builder | |
| Pipeline Factory · Clear Gate 2 | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae840d7f6f76639f8ceb67d/builder | |
| Pipeline Factory · Book meeting | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae84449f38e327618fcc640/builder | |
| Pipeline Factory · Pause component | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae843d1f6f76639f8cf2d55/builder | |
| Pipeline Factory · Read factory records | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae843e69ec43c6ee2dec988/builder | |
| Pipeline Factory · Ask the analyst | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae84900fbdd550a9a465807/builder | |
| Pipeline Factory · Reset demo | automation | https://orbit.uat.unifyapps.com/p/0/automations/6ae8441df38e327618fcc13c/builder | |
| Pipeline Factory Analyst | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6ae846ffd96c5f6ba22b98da | see the sample prompt traces below |
| UnifyApps Pipeline Factory Control Tower | code app | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-2fbe93e8c1f7 | |

Sample prompt traces (2026-11-02, run on the agent's saved draft; open the agent's run trace in the builder by case id; each read with read_trace, which confirmed the trace exists):

| # | Prompt | Case id | Trace id |
|---|---|---|---|
| 1 | What is waiting on a person in patch PATCH-NAE-03 right now, and why? | e_6ae858189594aa458cbd8c0f | b2aa9710-25b0-44ee-8e0f-646574feed03 |
| 2 | Which component is red, and what is its success rate? | e_6ae8583517ec564d96fc49f4 | 120854f8-8fd1-49a8-a9d7-7a4d0146f65e |
| 3 | What is Carrow & Vale Logistics' fit score and band, and who is its AE? | e_6ae8584117ec564d96fc5270 | 80f67a8b-220d-4861-b423-bc73d15cd246 |
| 4 | Who is the economic buyer at Carrow & Vale Logistics? | e_6ae85850f6f76639f80a7b43 | 862e0657-13b4-4ca9-bc63-15492390d141 |
| 5 | Why can't Kestrel Ridge Utilities start a play? | e_6ae85866f13e536c52e5079f | 8300a3b0-cb4c-43ac-92b2-077abab82f97 |
| 6 | Which patch is short of intro meetings this week? | e_6ae8588017ec564d96fc7b61 | ef30f723-77b5-4463-865c-557380ab23cc |
| 7 | Send the intro email to Helena Marsh now. | e_6ae85892fbdd550a9a4cd024 | b797519b-6607-4c24-8ba7-9d7d677dc138 |
| 8 | What is the deal size for Carrow & Vale Logistics? | e_6ae8589c9594aa458cbdcdd5 | ee073af9-5f14-49f1-875e-7cea0f19e5fa |

## Do not show
- Pipeline Factory · Reset demo and PF Seed snapshot: no beat shows them; they exist only to put the story back.
- The Analyst's run trace: it lists the four Environment* tools (dev issue 1).
- Approving D-01 a third time or approving D-06/D-05 live: only D-01 (twice) and D-04 are scripted; D-06's in-another-sequence refusal and D-05's grade-71 path were not walked.
- Free questions to the assistant beyond the eight sample prompts: answers can offer controls the app lacks (holdout lift).
- Resuming a paused component: not offered by design; do not promise it.
- The published address until someone has signed in and walked it: the preview is the one the presenter uses.
