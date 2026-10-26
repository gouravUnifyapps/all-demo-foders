# Clickup · ClickUp Delivery command dashboard — internal notes · v1 · 26 Oct 2026

For the team only. Nothing here goes in the handover doc, the runbook's client-facing parts or any client file.

## Open questions, for the owner
None of 1-18 has been answered by number; G1 and G2 were approved with each recommended option (a) as the build's assumption.
- 1. Scope: the BRD is the whole Delivery Command app, not only a dashboard · options: one app covering every ask, led by portfolio, executive summary and Copilot (recommended) / dashboard screens only / whole BRD with equal weight
- 2. Priority: keep all 50 must-worded asks as P0 · options: keep all 50 P0, the storyline picks the few (recommended) / lead names the P0 set
- 3. A99 "every project on one screen without scrolling" · options: compact overview above the paged list (recommended) / dense tile wall / paged list only, note declined
- 4. A100 "edit the timeline from the phone" · options: decline, timeline stays desktop (recommended) / allow date changes from the phone
- 5. A101 vs A102, customer health score · options: hide internal health from the portal (recommended) / separate customer-facing readiness score / show internal health
- 6. A103 region colour for consultants · options: labelled region tag, never colour alone (recommended) / resourcing grid only / decline
- 7. A104 Sales pricing calculator · options: leave out of this use case (recommended) / promote A104
- 8. Demo data volume · options: 15-20 projects with BRD-sized headline counts (recommended) / full BRD volumes
- 9. Phone view · options: responsive layout of the same code app in a phone frame (recommended) / separate native app
- 10. Integrations Salesforce, Slack, Google Drive, Jira · options: existing connections, the rest seeded with one Sync failed row (recommended) / seeded status only
- 11. Weekly executive email and Slack status post · options: in-app previews plus one real email to the presenter (recommended) / preview only / scheduled send to demo channel and inbox
- 12. External mailbox · options: the tenant's Gmail connection to the presenter, subject DEMO-TEST (recommended) / preview only / owner names another connection
- 13. Typeface (A9) · options: Inter with tabular figures, Noto Sans JP, IBM Plex Mono eyebrows (recommended) / keep Archivo
- 14. Sign-in, forgot and reset password (A58) · options: the tenant's own pages for a PRIVATE app (recommended) / branded mock sign-in screen
- 15. Roles and permissions (A54) · options: persona switcher plus seeded roles grid (recommended) / real tenant roles once governance tools are granted
- 16. Intent · options: both (recommended; G2 approval says both) / use-case / platform
- 17. Verify could not open the app: published address and preview both land on the tenant sign-in in the cloud runner's browser, so all 7 beats, every control, the coverage walk and six of seven checks are unverified: sign-in (handover hit the same, see Not captured) · options: run the verify walk on the presenter's Mac, signed in (recommended) / save a test user's sign-in for the Playwright browser and re-run here / make the app PUBLIC for the walk and PRIVATE after
- 18. The beat 1 email is sent through Gmail connection 6980e13788c7735877a8311c, a staff member's personal gmail.com mailbox (From: Rishabh Jain) · options: keep it and say so in presenter notes (recommended) / name a company mailbox connection / in-app preview only
- 19. Deep links on the published address answer 404 "This link isn't live yet" (handover, 26 Oct 14:24Z, /summary), while the root redirects to /login · options: presenter opens the root and navigates by the left menu (recommended) / fix the app's routing or hosting so deep links reach sign-in and then the page

## Dev issues
- 1. The Copilot's runtime offers the model tools no agent record holds: think, ClarifyFromUser (capability off), EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy, beside ReadDeliveryData, the agent's only enabled tool (get_agent: ReadDeliveryData enabled; requestClarification and generateChartTool disabled). Read in verify round 2 (case e_6adf612aca4f9d204580fff7, modelCalls[0..3].toolsOffered), every case in round 1, and again in handover (case e_6adf62f1f72100755f5f83a4). **Security point:** EnvironmentAccess's own description says it hands out a kubeconfig for a shared environment's cluster, and RequestEnvironmentDeploy deploys a pushed branch to a deployment environment. A read-only demo agent being offered cluster access and deploy tools is a security exposure, not only noise; the model has not called them in any trace read. Not raised yet; reply "raise 1" in the thread to raise it.

## Not captured
Playwright browser tried once (14:24Z): the published root lands on /login?returnTo=%2F (page title ClickUp Delivery Command); a deep link (/summary) answered 404 "This link isn't live yet". No password typed; tab closed. Claude_Browser tools are not on this cloud runner.
- Beat 1 Monday: the summary, then the portfolio · not captured: sign-in
- Beat 2 Sakura Mobility's workspace and the change it needs · not captured: sign-in
- Beat 3 The rule routes the approval, and refuses a bare rejection · not captured: sign-in
- Beat 4 Staffing the change without burning anyone out · not captured: sign-in
- Beat 5 The sponsor's view, in Japanese · not captured: sign-in
- Beat 6 Delivery Copilot over live data · not captured: sign-in
(H1 under the hood shows no ask and takes no shot.)

## Cost so far
2 runs · 2 agent spawns · 0.45M tokens · 0.6h (state `cost`; the G3 run started 12:03Z is not yet counted)

## Known bugs and workarounds
- Verify could not walk the screens behind the sign-in (open question 17): round 2 scored 0 of 7 beats, 0 of 90 coverage, 1 of 7 checks, all unverified: sign-in. Workaround: walk all six beats on the presenter's signed-in Mac before the demo; the automations behind beats 2-4 were proved by direct test runs (CR-0457 preview, refused_reason_required, over_capacity 120%).
- Status report dropped the budget hours (verify round 2 open line, beat 6, query 4 failed): the Summary never said 1,236 of 1,480 h, though the project row holds both. Fix waiting: "ai-agent · update · ClickUp Command Copilot: in the weekly status report rules, the Summary always states the project's budget hours used against planned from the project row". In handover's run (case e_6adf62f1f72100755f5f83a4) the draft did say "Budget hours used stand at 1,236 of 1,480 planned", so it varies run to run. Workaround: if the line is missing, the presenter adds it while editing the draft before Publish (the edit is part of the beat).
- Over-capacity answer is thin (beat 6 / sample prompt 6): handover's first send of "Who is booked over 100% in the next 12 weeks?" finished with nothing said and no case id; the second (case e_6adf636a39bf2b61bdfa0ae4) named Jonas Weber, B-04 and B-05, but wrote "Over capacity" in the capacity column and gave no 110% / 44 of 40 h and no weeks of 16 and 23 Nov (verify round 2 had 44 h against 40 h). Workaround: do not ask this live; it is not a scripted beat.
- Copilot runtime offers environment tools (dev issue 1). Workaround on the day: none needed for the demo; do not open the trace view in front of the client.
- Deep links on the published address 404 (open question 19). Workaround: open the root address and use the left menu.
- Two deployed-lane trigger run ids from verify round 2 (Raise change request 6adf620a97a3bf334d700012, Book consultant 6adf620e92718f6a64e732b4) could not be found by inspect_workflow_run or list_workflow_runs; the test-lane runs answered correctly. Unverified whether the deployed lane writes as expected; beats 2 and 4 on screen are the first proof.
- Beat 5 portal: no safe tool run was made (sign-off D-2611-5 not touched); fully unverified.
- Copilot model: OpenAI GPT 4.1 (e_ai_agent_openai_gpt_4.1) failed every run with HTTP 500 insufficient_quota / project_spend_limit_exceeded on its OpenAI project; the agent now runs Claude Sonnet 5 (UnifyApps, Vertex) e_6ad496812dd4ba5be70afcc1 for topic selection, execution and answer generation (build plan 8 of 9 note; cache agent confirms the model id). Do not switch it back without checking the OpenAI quota.

## One-shot beats and resets
- Beat 1 · Email me this summary sends one real DEMO-TEST email from the staff Gmail mailbox; Save view "Japan at risk" writes a Saved view row (a second save of the same name answers refused_name_taken) · reset: delete the "Japan at risk" saved view; delete the email from the presenter's inbox.
- Beat 2 · Submit writes CR-0457 (pending_approval) and one Activity row; the next request would be CR-0458 · reset: delete CR-0457 and its Activity row. The timeline date move is previewed and cancelled, writes nothing; a Board drag or Move to writes the Task and an Activity row (move it back).
- Beat 3 · the final approval sets CR-0457 approved, moves IMP-2611 go-live 16 Nov to 21 Nov 2026, planned hours 1,480 to 1,536, one Activity row · reset: set IMP-2611 go_live_date back to 16 Nov 2026 (1794787200000) and budget_hours_planned 1480, delete CR-0457 and the Activity rows. The empty-reason rejection writes nothing.
- Beat 4 · booking Daichi Ono writes a Booking and an Activity row (Yui Sato's over-capacity preview writes nothing unless confirmed) · reset: delete the new booking and its Activity row.
- Beat 5 · sign-off of Cutover plan sets D-2611-5 signed_off with name and time; booking the 29 Oct slot marks it taken; confirming the upload sets DOC-05 confirmed · reset: D-2611-5 back to awaiting_signoff with decided_by and decided_at empty; the slot back to taken false, booked_by empty; DOC-05 back to needs_fixing; delete the sign-off Activity row.
- Beat 6 · Publish writes a status_report Document and an Activity row on IMP-2611 · reset: delete that Document and Activity row.
- Every reset is a delete or a row overwrite: it needs the person's yes (profile: avoid deletes) and is done in a builder session, never from this stage.

## Deferred asks
- None with status deferred. A104 (Sales pricing calculator) is out of scope as another use case. Open, waiting on the owner: A9 (q13), A51 (q11), A54 (q15), A58 (q14), A92-A95 (q10), A99 (q3), A100 (q4), A101-A102 (q5), A103 (q6).

## Test accounts and test records
- Presenter: own tenant account on orbit.uat.unifyapps.com; no test user exists. Personas are switched in the app's profile menu: Elena Fischer (Delivery director), Kenji Arai (Lead), Marcus Bell (Finance partner), Tom Hale (Resource manager), Haruto Mori (Sponsor, IMP-2611, Japanese), Grace Lin (Sponsor, IMP-2598). All fictional, @example.com.
- DEMO-TEST records to clean up (from `## entities`):
  - Saved view V-03 'DEMO-TEST 2026-10-26 view' · OBJ_cucmd_saved_view
  - Time entry E-6adf4ba097a3bf334d3f24b5 and Activity A-6adf4ba097a3bf334d3f24b5 · Timesheet action log test, IMP-2611 · OBJ_cucmd_time_entry, OBJ_cucmd_activity
  - Activity A-6adf4dc0ca4f9d20457f2ff7-AI-05 · Accept proposed tasks reject test, actor DEMO-TEST 2026-10-26 · OBJ_cucmd_activity
  - Document DOC-SR-6adf4dc2c79cad1140aa6b4a and Activity A-6adf4dc2c79cad1140aa6b4a · Publish status report test on IMP-2604 · OBJ_cucmd_document, OBJ_cucmd_activity
  - One DEMO-TEST email to gourav.mahunta@unifyapps.com, Gmail message id 1a17847cf729b474 · Send executive summary test
- Verify round 2 and this handover created no records: agent test conversations only (handover: 11 sends, read-only agent).

## Trace and builder links
Handover runs, 26 Oct 2026 14:24-14:28Z, agent published version 16. Case and trace ids confirmed by read_trace; the trace opens from the agent's builder page (direct trace URL format unverified).

| Entity | Kind | Builder link | Trace |
|---|---|---|---|
| ClickUp Command Copilot · Q1 Japan November at risk | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6adf4f02dc07493166ced9fa | case e_6adf62acdee2a3345023275c · trace d9145ef7-7ac8-44c5-a5f1-542bb642b5d5 |
| Copilot · Q2 go-lives by month chart | AI agent | same | case e_6adf62c1dee2a33450232843 · trace 805d5429-09f8-4508-8ac6-929a1bf1275b |
| Copilot · Q3 likely to miss go-live | AI agent | same | case e_6adf62ddca4f9d2045811aa8 · trace f657c9cd-451e-4d1a-8a29-92750e153ba2 |
| Copilot · Q4 weekly status report | AI agent | same | case e_6adf62f1f72100755f5f83a4 · trace 7d69b77d-bdf4-4bba-b3ad-ace9ed266331 |
| Copilot · Q5 health counts | AI agent | same | case e_6adf632451bd784a8d0307dd · trace 0c431f2a-1201-496f-9eb5-b8bf4f43b9c7 |
| Copilot · Q6 over 100% (second send; first returned no case) | AI agent | same | case e_6adf636a39bf2b61bdfa0ae4 · trace 7a3b51ef-8247-48e9-898c-eadd0f2cc16e |
| Copilot · Q7 steering meeting 22 Oct | AI agent | same | case e_6adf633df72100755f5f898c · trace d1d79aa2-ab74-4e94-b3da-b08fd66c80cb |
| Copilot · Q8 invoice total (refusal) | AI agent | same | case e_6adf63566112da3e23bc3e51 · trace a8be0ed8-7a0c-49a2-b672-1989633e5860 |
| Copilot · Q9 change go-live date (refusal) | AI agent | same | case e_6adf635939bf2b61bdfa0a0a · trace 02a2c791-661a-4a5b-ae4c-20f853a8d6eb |
| Copilot · Q10 Haruto Mori phone (refusal) | AI agent | same | case e_6adf6360f72100755f5f8bc8 · trace 929bc76e-0ef2-4ada-a576-725603e8f64f |
| ClickUp Delivery Command | code app | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-a2a9509a82c1 | last commit 9142bfc0 |
| ClickUp Command · Read delivery data | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf45fef3cd5f19ed4a76ba/builder | — |
| ClickUp Command · Save view | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf460108750d257cf1e381/builder | — |
| ClickUp Command · Update task | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf485af3cd5f19ed4ac683/builder | — |
| ClickUp Command · Raise change request | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf485ec79cad1140a9e9a6/builder | verify test run 6adf6228c79cad1140c0fe4b |
| ClickUp Command · Decide change request | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf485ff3cd5f19ed4ac6fd/builder | verify deployed run 6adf620c92718f6a64e73293 |
| ClickUp Command · Book consultant | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4aa308750d257cf32534/builder | verify test run 6adf622af3cd5f19edae3578 |
| ClickUp Command · Timesheet action | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4aa9f3cd5f19ed4afa85/builder | — |
| ClickUp Command · Portal action | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4aaef3cd5f19ed4afc58/builder | — |
| ClickUp Command · Accept proposed tasks | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4d11f3cd5f19ed4b436a/builder | — |
| ClickUp Command · Publish status report | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4d1492718f6a64e5ca35/builder | — |
| ClickUp Command · Send executive summary | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4d1508750d257cf3df21/builder | — |
| ClickUp Command · Update project settings | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4eb5cac0655fe38aef9d/builder | — |
| ClickUp Command · Mark notification read | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf4eb8cac0655fe38aefc9/builder | — |
| ClickUp Command · Ask Copilot | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adf526ef3cd5f19ed626787/builder | — |
| 17 objects ClickUp Command · * | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_cucmd_project/schema (and the other OBJ_cucmd_* ids in `## entities`) | — |

## Do not show
- The weekly summary email's sender: a staff member's personal gmail.com mailbox (Rishabh Jain), open question 18. Keep the inbox view on the subject and body, or show the in-app preview.
- The agent trace view and the agent builder's tool list beyond ReadDeliveryData: it exposes the environment tools of dev issue 1. In H1, show the agent's one attached tool only.
- "Who is booked over 100%?" asked live: the answer is thin (see Known bugs).
- Billing, invoicing, revenue, payroll or customer workspace building: out of the first release (A96); the Copilot refusal on the invoice is the only place they appear.
- Internal health presented as "what the customer sees" (open question 5): switch to the sponsor persona before opening the portal, and do not narrate an internal screen as the customer's view.
- The DEMO-TEST records above (saved view V-03, the IMP-2604 test status report): clean them before the demo or steer clear of the Saved views list and IMP-2604's documents.
- Deep links typed into the address bar (404 page).
