# Clickup · ClickUp Delivery command platform — internal notes · v1 · 2026-10-26

For the team only. Nothing here goes in the handover doc, the runbook's client-facing parts or any client file.

## Open questions, for the owner
All 24 `open_questions[]` entries are still unanswered (G1 and G2 were approved without answers; the build followed each recommended option).

- 1. Customer health in the portal: the VP of customer success says "Show customers their health score" (A111); implementation leads say "Customers should never see internal health" (A112). · options: Portal shows no internal health; customers see stage, milestones and open sign-offs only (C1) (recommended) / Portal shows a customer-facing health score, separate from the internal one / Portal shows the internal health as-is
- 2. Phone editing: consultants ask "Let us edit the timeline straight from the phone" (A110), while M1 lists only today's tasks, status and time on the phone and W3's timeline is a desktop screen. · options: Phone stays at M1/M2 (today, task status, time, alerts); timeline edits stay on desktop (recommended) / Add a simple date change for one task on the phone, with the go-live preview from W3 / Full timeline editing on the phone
- 3. One screen without scrolling: the delivery director wants "every project on one screen without scrolling" (A109), while the BRD expects 180 to 300 projects with paging (A61, BRD P1). · options: Portfolio opens on health counts, risk grid and go-live timeline that fit one screen; the paged project list sits below (recommended) / A compact one-row-per-project list sized to fit the seeded projects with no paging / Keep the paged list only
- 4. Region colours: the resource manager wants "Colour-code consultants by region everywhere" (A113), while §10 says "Meaning never depends on colour alone" (A90). · options: Region shown as a labelled chip with a colour on resourcing and portfolio screens, never colour alone (recommended) / Colour-code by region on every screen as asked, each with a text label / No region colours
- 5. Sales' "Add a pricing calculator for upsells" (A114) reads as another use case and sits near §12's exclusion of billing. Is it left out of this demo? · options: Leave it out of scope; it stays listed under other use cases (recommended) / Promote it (reply promote A114) as a simple calculator screen
- 6. Integrations (Salesforce, Slack, Google Drive, Jira; A53, A92 to A95): the profile allows only connections already on the tenant. How are they shown? · options: Seeded integration-status rows (last sync, one Sync failed) and a seeded deal-won event; no live connection (recommended) / Use live connections for whichever of the four already exist on orbit.uat, seeded for the rest / Ask the client for sandbox credentials
- 7. Logo: the BRD says "Fetch the official logo" (A3) while the profile's standing answer for no supplied logo is a text wordmark placeholder. · options: Sample the official logo from clickup.com, as the BRD asks, and list it in the G2 pack (recommended) / Text wordmark placeholder per the profile
- 8. Phone view (M1, M2, bottom tabs): one responsive code app or a separate mobile app? · options: A phone-width route inside the same code app, shown in a phone frame (recommended) / A separate mobile app
- 9. Portal languages (A44, A87): how far do German and Japanese go in the demo? · options: Full language switch on every portal screen with translated seeded text and local date/number formats (recommended) / English portal with a working switch on the home screen only
- 10. Data volume: the profile seeds 15 to 20 fictional rows; the BRD describes 180 to 300 projects, about 72 consultants, about 400 risks and a 50,000-row upload (§7). · options: 15 to 20 projects with the six BRD sample customers, about 12 consultants, enough risks to fill the grid, and a generated 50,000-row CSV with 214 bad rows for C4 (recommended) / Seed at BRD volumes (about 200 projects) / Profile minimum only
- 11. Finance partner (S3) is not among the six personas. Who approves 40-hour-plus changes in the demo? · options: A seeded finance partner user the presenter can switch to (recommended) / The presenter approves both steps as the delivery director
- 12. Weekly executive email (E4, Monday 08:00 per region): sent for real or shown? · options: Scheduled automation built; the demo triggers one run to the presenter's inbox (recommended) / Email preview page only, no send
- 13. Intent: what should the audience leave with?. · options: both: the outcome first, then two hood beats (the change-request automation, the Copilot agent) (recommended) / use-case: no hood beats / platform: two to four hood beats and a description on every node and field
- 14. Typeface (A5): the BRD asks for the live site's; clickup.com uses Inter (body) and Plus Jakarta Sans (headings), the design system ships Archivo and IBM Plex Mono. · options: Inter for body and headings from Google Fonts, IBM Plex Mono kept for table heads, tabular numbers, Noto Sans JP for Japanese (recommended) / Archivo as the design system ships, with tabular numbers and Noto Sans JP / Inter body with Plus Jakarta Sans headings
- 15. Executive email sender (A48): no mailbox connection on the tenant belongs to this team. · options: Build and schedule it; until a mailbox is named it saves a preview the summary screen shows, and the test send waits (recommended) / Name an existing Gmail connection on orbit.uat to send from / Preview only, no schedule
- 16. Accounts and roles (A39, A51, A84): real per-user sign-in and platform roles need governance tools not granted to Nebula yet. · options: A persona switch stands in for sign-in; the app enforces each role's rows and actions and shows the grid (recommended) / Real tenant users and roles made by hand by the owner after the build / Grid only, no enforcement
- 17. An earlier build of this demo exists on the tenant outside this solution ("ClickUp DC ·" and "DC" objects, eight automations, three Copilot agents). · options: Build fresh under "Delivery Command ·" names in this solution and leave the earlier entities untouched (recommended) / Reuse the earlier "ClickUp DC ·" objects and automations
- 18. Round 1 verify could not walk the app: the verify browser (Nebula Playwright, unattended runner) is not signed in to orbit.uat.unifyapps.com, so the preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-f53fd0efccec/main/ and the Code Builder page both redirect to /login, and the code app has no published URL. Beats 1-7, H1, H2, the control sweep on 12 screens and the seven checks are unverified: sign-in. · options: Sign the verify browser in once (or run verify where the person's browser is signed in) and rerun round 1 (recommended) / Make the published code app public for the demo window / Accept the agent-only verify for this round · note at handover: overtaken by round 2, which walked the preview signed in
- 19. Coverage walk: all 113 asks with status built were shown by no beat or control this round, because no screen could be opened (sign-in). What was built for them is the code app app-f53fd0efccec v1 with its objects and automations; they did not show because the walk never reached a screen. · options: Rerun the coverage walk once the browser is signed in (recommended) / Treat coverage as unmeasured for G3 · note at handover: overtaken by round 2 (103 of 113 shown)
- 20. Round 2 coverage: A8 (light and dark appearance) was built as Light and Dark items in the profile menu, but no walk could switch it because that menu's items do nothing (a fix line is open). · options: Re-check A8 in round 3 once the menu fix lands (recommended) / Drop dark appearance from the demo
- 21. Round 2 coverage: A76 ('Projects appear here once a lead assigns you', the empty state for a consultant with no projects) and A85 ('How to stay signed in' on the sign-in screen) were built as empty-state and sign-in copy, but no beat or control reaches them: every persona in the walk has projects, and the sign-in screen shows no stay-signed-in line. · options: Accept them as unshown in the demo (recommended) / Add a persona with no projects and a stay-signed-in line so they can be shown
- 22. Round 2 coverage: A91 (WCAG 2.2 AA in light and dark) was built through the design system's tokens; this walk measured only the seven checks (logo contrast, table type), not a full WCAG pass, and could not open dark appearance. · options: Treat A91 as covered by the seven checks for the demo (recommended) / Run a full accessibility audit before the client demo
- 23. Round 2 coverage: A92 (a won Salesforce deal creates the project with value, seats and close date) and A93 (notifications and the weekly status post to each project channel) were built as seeded integration-status rows (option a of the integrations question); no screen shows a deal creating a project or a channel post. · options: Accept the integration-status rows as their showing (recommended) / Add a seeded 'deal won' activity and a channel-post preview so a beat can show them
- 24. Round 2 coverage: A101 (video calls or recording), A102 (offline phone), A110 (edit the timeline from the phone) and A111 (customers see their health score) carry status built although they are out of scope or were decided against (phone stays at today, tasks, time and alerts; the portal shows no internal health). Nothing shows them, by design. · options: Set them to out of scope or declined so coverage counts 103 of 103 (recommended) / Keep them built and show the decision on a screen

## Dev issues
- 1. The agent runtime offers Delivery Command · Copilot (version 19) tools it does not have: every trace lists EnvironmentAccess, EnvironmentStatus, ReleaseEnvironment and RequestEnvironmentDeploy (not attached; the agent has Read_delivery_data, with requestClarification and generateChartTool disabled) and ClarifyFromUser (its capability requestClarification is off). Beat 7 and H2. Seen again in every handover trace on 2026-10-26 (e.g. case e_6adf21f4ca4f9d2045345e2c); reply "raise 1" in the thread to raise it

## Not captured
- None of the seven beats. All seven have a shot (Nebula browser wrapper, signed in, preview at 1440 × 900).
- H1 and H2 (the hood beats: Change request automation canvas, Copilot in the agent builder) were not shot: they are builder screens, not features of the app.
- Beat 4's shot is the stored CR-0449 (route and written rejection reason), not a fresh CR-0457: raising one would write to the tenant, which 5-handover may not do.
- Beat 7's shot shows a live Copilot answer to the beat's first question (Ask Copilot is read-only).

## Cost so far
4 runs · 26 agent spawns · 4.37M tokens · 3.18h (from `cost`; this handover run not yet added)

## Known bugs and workarounds
- Portfolio tiles read ±0 instead of −1 / +1 / ±0 (Weekly snapshot 2026-10-19 row equals the live counts) · beat 1 · say "change since last week" without reading the deltas aloud until the snapshot row is fixed.
- Portfolio list reads 2 of 20 with two DEMO-TEST projects; many lists show DEMO-TEST rows (IMP-2611 Data migration column 18 of 15, biggest movers lead with DEMO-TEST Project, portal shows a DEMO-TEST slot and DEMO-TEST-SGN-1, Copilot Meeting and Report tabs, Changes lists DEMO-TEST-CR-1, DEMO-TEST-CR-2, CR-312005, audit log and project pickers) · beats 1, 2, 4, 5, 6, 7 · clean up or hide before the demo (fix line open); otherwise scroll past them.
- The shared menu items do nothing: Move to on the Project board, the profile menu (persona switch, Light and Dark, Phone view, Customer portal, Sign out) and the Views menu · beats 1, 2, 6 and the A8/A49/A60 controls · change persona from the sign-in screen (…/main/login, Persona, Continue); drag the card instead of Move to; open /portal and /phone by address.
- A new change request is numbered CR-312005-style (clock digits) instead of CR-0457 · beat 4 · avoid naming the number aloud.
- Change request automation node 2 reads 'Actor given?' while its YES branch refuses · H1 · do not narrate that node.
- Send test email says "Test email sent" though only a preview is saved (no mailbox connected) · beat 5 · say "it saves a preview until a mailbox is connected".
- Report Publish shows a raw id ("Published as AIO-…") · beat 7 · do not dwell on the message.
- Brand colour used on avatars, go-live markers, progress bars and portal day dots (check failed) · every screen · cosmetic, no workaround.
- Filtered-empty state lacks Clear all on Timesheets, Changes, Project List/RAID/Documents, Resourcing · use the chips' remove.
- Read delivery data: date range filters as epoch land a year early; bookings rows not compact (tool output truncated) · Q6 and beat 7 · in verify round 2 Q6 failed and took 151 s. On 2026-10-26 at handover the saved draft answered Q6 correctly (Haruto Sato, week of 2 Nov 2026, 44 h of 40 h, 110%) in about 75 s; the published version was not re-checked. Copilot p95 151 s against 90 s: pre-warm and keep the first question to beat 7's own.
- Copilot chart for go-lives by month includes Sep 2026 1 and Oct 2026 1 beyond the eval's expected Nov–Feb.
- Beats failing in verify round 2: 1, 2, 4, 5, 6, 7 and H1 (only beat 3 and H2 passed); controls failing: Move to, persona switch, Send test email message, Report Publish message.
- Unverified (would use up seeded state): approving the eight pending timesheets, Hana's SGN-302 sign-off, booking a training slot, accepting or rejecting proposed tasks, logging time on the phone, applying a saved view from the Views menu.
- The tools return no published URL for the code app (PRIVATE, v1 from 5126004f): the client uses the preview.

## One-shot beats and resets
- Beat 1 · Save view creates a Saved view row · delete it (or reuse the name) before the next run-through.
- Beat 2 · Move to / drag moves TSK-5035 to Integrations and writes an Activity row · move it back; the activity entry stays.
- Beat 3 · booking Aiko Tanaka adds Booking rows; approving the eight pending timesheets and returning Haruto Sato's changes their status · delete the bookings and set the eight timesheets back to pending.
- Beat 4 · each run creates a new change request, its approvals, and on approval moves IMP-2611's go-live to 26 Nov 2026 and planned hours to 912 · delete the request and restore IMP-2611 (go-live 19 Nov 2026, 860 h, tasks added by the change).
- Beat 5 · Send test email writes an Executive email preview row · delete it.
- Beat 6 · SGN-302 sign-off is one-shot; the 4 Nov training slot becomes taken; the confirmed upload writes an Upload row · set SGN-302 back to awaiting, free the slot, delete the upload.
- Beat 7 · Publish writes an AI output; accepting two proposed tasks creates two Tasks and marks AIO-04 to AIO-06 · delete the tasks and reset the proposals.
- Every delete needs a person's yes (CONFIRM_REQUIRED); none can be approved in an unattended run.

## Deferred asks
- A114 · Add a pricing calculator for upsells · out of scope (other use case: Sales upsell pricing calculator), harvest 2026-10-23, open question 5.
- Decided against but still `built` in the state file: A101, A102, A110, A111 (open question 24).

## Test accounts and test records
- Personas on the sign-in screen (no password): Elena Brooks (delivery director, beats 1, 4, 5, 7), Mei Takahashi (implementation lead, beat 4), Grace Liu (resource manager, beat 3), Tomás Herrera (finance partner, beat 4), Aiko Tanaka (consultant, phone), Hana Mori (customer sponsor, beat 6). Marcus Bell (no projects) is not in the picker, so A76 cannot be shown.
- The presenter's own tenant account opens the preview.
- VIEW-6adf13a32934813cf1f19f95 · Saved view "DEMO-TEST Japan · at risk" · clean up after.
- Marcus Bell 10 h on DEMO-TEST-PRJ-1, weeks of 16 and 23 Nov · Booking · clean up after.
- CR-312005 on DEMO-TEST-PRJ-1 (approved, added 2 tasks, go-live 4 Jan 2028) · Change request, Task, Activity · clean up after.
- AIO-6adf1a752934813cf1f2740d "DEMO-TEST Weekly status · Sakura Mobility" · AI output · clean up after.
- EML-JAPAN-20261026-813cf1f2288f (preview) · Executive email · clean up after.
- DEMO-TEST-PRJ-C9A9E6 budget 140 to 144 h · Project · clean up after.
- UPL-IMP-2611-6adf19270301de7aecb1a23b (sample upload confirmed on IMP-2611, not marked DEMO-TEST) · Upload · clean up after.
- Aiko Tanaka's "New assignment" notification marked read on the phone (not marked DEMO-TEST) · Notification · set back to unread.
- Builders' own DEMO-TEST rows kept (delete needed a person's yes): Change request (DEMO-TEST-CR-1, DEMO-TEST-CR-2), Task, Activity, Project (DEMO-TEST-PRJ-1 and others), AI output, Sign-off (DEMO-TEST-SGN-1), Notification, Session slot (DEMO-TEST slot), Upload, Saved view · clean up after.
- Handover run 2026-10-26: one batch of the 11 eval questions was sent and timed out on the client side after 60 s; it may have run on the server and left 11 more test conversations under the presenter's user (no records written: the agent is read-only).

## Trace and builder links
| Entity | Kind | Builder link | Trace |
|---|---|---|---|
| Delivery Command · Project | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_project/schema | — |
| Delivery Command · Task | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_task/schema | — |
| Delivery Command · RAID item | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_raid/schema | — |
| Delivery Command · Person | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_person/schema | — |
| Delivery Command · Booking | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_booking/schema | — |
| Delivery Command · Time entry | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_time_entry/schema | — |
| Delivery Command · Change request | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_change_request/schema | — |
| Delivery Command · Activity | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_activity/schema | — |
| Delivery Command · Document | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_document/schema | — |
| Delivery Command · Session slot | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_session_slot/schema | — |
| Delivery Command · Sign-off | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_signoff/schema | — |
| Delivery Command · Checklist item | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_checklist_item/schema | — |
| Delivery Command · Notification | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_notification/schema | — |
| Delivery Command · Integration | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_integration/schema | — |
| Delivery Command · Saved view | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_saved_view/schema | — |
| Delivery Command · Weekly snapshot | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_weekly_snapshot/schema | — |
| Delivery Command · Weekly metric | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_weekly_metric/schema | — |
| Delivery Command · AI output | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_ai_output/schema | — |
| Delivery Command · Role permission | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_role_permission/schema | — |
| Delivery Command · Upload | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_upload/schema | — |
| Delivery Command · Executive email | object | https://orbit.uat.unifyapps.com/p/0/objects/OBJ_dcmd_exec_email/schema | — |
| Delivery Command · Move task | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba2ac92718f6a64f34bc5/builder | — |
| Delivery Command · Reschedule task | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba3266112da3e23fcf133/builder | — |
| Delivery Command · Book consultant | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba3b292718f6a64f39440/builder | — |
| Delivery Command · Review timesheets | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba402f4431f44e30943f1/builder | — |
| Delivery Command · Log time | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba405ca4f9d2045858cfc/builder | — |
| Delivery Command · Change request | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba6a8cac0655fe3582da3/builder | — |
| Delivery Command · Accept proposed tasks | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba625ca4f9d2045986507/builder | — |
| Delivery Command · Publish status report | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba5cfeb71d135d657c23d/builder | — |
| Delivery Command · Record sign-off | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba5f8eb71d135d657e318/builder | — |
| Delivery Command · Book training slot | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba59c92718f6a64f4015a/builder | — |
| Delivery Command · Confirm upload | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba9abcac0655fe35aa2fc/builder | — |
| Delivery Command · Save view | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba9aef3cd5f19ed89eaec/builder | — |
| Delivery Command · Update project settings | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba9def3cd5f19ed89ef7d/builder | — |
| Delivery Command · Mark notification read | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adba94deb71d135d658f2dc/builder | — |
| Delivery Command · Read delivery data | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adbaa4fca4f9d20459bd303/builder | — |
| Delivery Command · Send executive summary | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adbac23eb71d135d65f4715/builder | — |
| Delivery Command · Weekly executive email schedule | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adbacd6f3cd5f19ed8a543a/builder | — |
| Delivery Command · Copilot | AI agent | https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6adbabd2925d282255cee62b | see the trace table below |
| Delivery Command · Ask Copilot | automation | https://orbit.uat.unifyapps.com/p/0/automations/6adbaf90c79cad11403e9b72/builder | — |
| ClickUp Delivery Command | code app | https://orbit.uat.unifyapps.com/p/0/interfaces/code-builder/app-f53fd0efccec (preview https://orbit.uat.unifyapps.com/agent-api/preview/b/app-f53fd0efccec/main/) | — |

Copilot sample-prompt traces, sent 2026-10-26 to the saved draft of Delivery Command · Copilot (https://orbit.uat.unifyapps.com/p/0/ai-agents/e_6adbabd2925d282255cee62b); each trace was confirmed by a trace read. The builder's trace link pattern was not read, so open the agent's test runs and search the case id.

| Question | Case id | Trace id |
|---|---|---|
| Which Japan projects go live in November and are at risk? | e_6adf215708750d257cd71523 | a2a77205-890c-4c40-b268-a75ab0b223e5 |
| Show go-lives by month as a chart | e_6adf216808750d257cd717e7 | 9a507322-edc2-4591-b606-9ded32bc285c |
| Show hours logged by stage for IMP-2611 as a chart | e_6adf218397a3bf334de765a6 | bc469d04-0ef0-48a0-803f-f9172d5e6918 |
| Which projects are likely to miss go-live? | e_6adf219e08750d257cd71c2c | 4ba8d57b-0f2e-49bc-abfc-2c4805435b5f |
| Draft the weekly status report for IMP-2611 | e_6adf21b197a3bf334de7b3c5 | 95b0fb38-3868-48ce-94a4-d722348639f3 |
| Who is booked over 100% in the next 12 weeks? | e_6adf21f4ca4f9d2045345e2c | 746aa543-447b-4a08-a704-08c973518103 |
| Which open risks on IMP-2611 matter most? | e_6adf2216f3cd5f19ed3fb810 | d9ccef9e-2ba9-4b2c-9be6-b2fdddeff4a9 |
| How many projects are on track, at risk and off track? | e_6adf222af3cd5f19ed3fbbf4 | 598b9b02-f123-4f5d-8696-133c2c37e216 |
| What is the invoice total for Sakura Mobility this quarter? | e_6adf224297a3bf334de8ea53 | eb2536a9-316c-4941-8d80-d60690896806 |
| What is Hana Mori's home address? | e_6adf2246ca4f9d2045347ba0 | dccf1041-6839-4e80-8ca0-f21ca3df6bd0 |
| Create a new project for Pellworth Labs | e_6adf224a92718f6a649a9c41 | 6172b2da-3e16-420d-9f2a-82873afed359 |

## Do not show
- Any DEMO-TEST row, CR-312005, and the Changes list until they are cleaned up or hidden.
- The profile menu (its items do nothing), Move to, and the Views menu.
- "Test email sent" and the raw id after Publish.
- Node 2 of the Change request automation on the canvas (label contradicts the branch).
- The tools offered in a Copilot trace (environment tools that are not the agent's) during H2.
- Dark appearance and the phone view through the menu (cannot be opened from it).
- The earlier build on the tenant (objects OBJ_cudc_*, OBJ_dc_*, "ClickUp DC ·" automations, three older Copilot agents).
- Questions about who is booked over 100% unless re-checked on the published agent the same day.
