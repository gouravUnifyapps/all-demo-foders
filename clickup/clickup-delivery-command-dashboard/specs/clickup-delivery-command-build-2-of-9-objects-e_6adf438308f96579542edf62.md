---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 2 of 9: objects, part 2, and the first seeds"
touches: [{"kind":"object","name":"ClickUp Command · Activity"},{"kind":"object","name":"ClickUp Command · AI output"},{"kind":"object","name":"ClickUp Command · Weekly metric"},{"kind":"object","name":"ClickUp Command · Saved view"},{"kind":"object","name":"ClickUp Command · Checklist item"},{"kind":"object","name":"ClickUp Command · Integration"},{"kind":"object","name":"ClickUp Command · Notification"},{"kind":"object","name":"ClickUp Command · Project","id":"OBJ_cucmd_project"},{"kind":"object","name":"ClickUp Command · Task","id":"OBJ_cucmd_task"},{"kind":"object","name":"ClickUp Command · RAID item","id":"OBJ_cucmd_raid"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-26T12:11:46.226Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf4385dc07493166cdd028"]
latestPlanId: "e_6adf4385dc07493166cdd028"
planId: "e_6adf4385dc07493166cdd028"
---
# ClickUp Delivery Command · build 2 of 9: objects, part 2, and the first seeds

## Requested outcome
Build 2 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds objects, part 2, and the first seeds. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- object · ClickUp Command · Activity · new
- object · ClickUp Command · AI output · new
- object · ClickUp Command · Weekly metric · new
- object · ClickUp Command · Saved view · new
- object · ClickUp Command · Checklist item · new
- object · ClickUp Command · Integration · new
- object · ClickUp Command · Notification · new
- object · ClickUp Command · Project · OBJ_cucmd_project
- object · ClickUp Command · Task · OBJ_cucmd_task
- object · ClickUp Command · RAID item · OBJ_cucmd_raid

## Contract

### object · ClickUp Command · Activity
One change on a project: who did what and when; never edited; also the audit log.

- object · create · ClickUp Command · Activity: id `OBJ_cucmd_activity`; fields activity_code (text, primaryKey, required), project_code (text), actor (text), action (picklist: created "Created", updated "Updated", moved "Moved", approved "Approved", rejected "Rejected", signed_off "Signed off", booked "Booked", published "Published", logged "Logged time"), summary (text), at (date, epoch ms); never updated after it is written

### object · ClickUp Command · AI output
One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report draft.

- object · create · ClickUp Command · AI output: id `OBJ_cucmd_ai_output`; fields output_code (text, primaryKey, required), project_code (text), kind (picklist: risk_flag "Risk flag", meeting_summary "Meeting summary", proposed_task "Proposed task", status_report "Status report draft"), title (text), body (text), confidence (number 0 to 100), evidence_json (text), transcript_refs_json (text), decision (picklist: proposed "Proposed", accepted "Accepted", rejected "Rejected"), ai_written (boolean, default true), created_at (date, epoch ms)

### object · ClickUp Command · Weekly metric
The portfolio health counts, the six headline numbers and the value bridge for one week.

- object · create · ClickUp Command · Weekly metric: id `OBJ_cucmd_weekly_metric`; fields week_start (date, epoch ms, primaryKey, required), on_track (number), at_risk (number), off_track (number), active_projects (number), golives_this_month (number), avg_days_to_golive (number), utilisation_pct (number), value_awaiting_usd (number), bridge_new (number), bridge_golives (number), bridge_slipped (number), bridge_cancelled (number), top_movers_json (text), last_updated (date, epoch ms)

### object · ClickUp Command · Saved view
One named, shareable set of portfolio filters.

- object · create · ClickUp Command · Saved view: id `OBJ_cucmd_saved_view`; fields view_code (text, primaryKey, required), name (text, required), filters_json (text), owner (text), shared_with (text)

### object · ClickUp Command · Checklist item
One of the ten readiness questions with the customer answer, or none.

- object · create · ClickUp Command · Checklist item: id `OBJ_cucmd_checklist_item`; fields item_code (text, primaryKey, required), project_code (text, required), position (number), question_en (text), question_de (text), question_ja (text), answer (text; empty means not set), answered_by (text), answered_at (date, epoch ms)

### object · ClickUp Command · Integration
The sync status of one connected system.

- object · create · ClickUp Command · Integration: id `OBJ_cucmd_integration`; fields system (picklist: salesforce "Salesforce", slack "Slack", google_drive "Google Drive", jira "Jira"; primaryKey, required), status (picklist: synced "Synced", sync_failed "Sync failed"), last_sync (date, epoch ms), failing_since (date, epoch ms), error (text), affects (text)

### object · ClickUp Command · Notification
One assignment, sign-off or mention for a user.

- object · create · ClickUp Command · Notification: id `OBJ_cucmd_notification`; fields notification_code (text, primaryKey, required), person_code (text, required), kind (picklist: assignment "New assignment", signoff "Sign-off", mention "Mention"), text (text), link (text), read (boolean), created_at (date, epoch ms)

### object · ClickUp Command · Project
One customer implementation, from signed contract to Hypercare; the story row is IMP-2611.

- record · seed · ClickUp Command · Project: IMP-2611 Sakura Mobility, Automotive, japan, go_live, go-live 2026-11-16, health at_risk, last week on_track, lead Kenji Arai, sponsor Haruto Mori, 9200 seats, 62400000 jpy, 1480 planned, 1236 used, column_limit 15, next sign-off "Cutover plan" due 2026-10-29, Asia/Tokyo; IMP-2604 Halden Freight, Logistics, europe, migration, 2026-12-07, on_track/on_track, Mira Lindqvist, 4800, 386000 eur, 1100/640, Europe/Oslo; IMP-2598 Corvia Health, Healthcare, north_america, configuration, 2027-01-18 (original 2026-12-14), off_track/at_risk, Dana Whitfield, sponsor Grace Lin, 12000, 910000 usd, 2400/1310, America/Chicago; IMP-2615 Brightmoor University, Education, europe, training, 2026-11-23, on_track/on_track, Mira Lindqvist, 2300, 142000 eur, 620/510, Europe/London; IMP-2621 Kestrel Energy, Energy, north_america, discovery, 2027-02-22, on_track/on_track, Sam Okafor, 7500, 540000 usd, 1650/210, America/Denver; IMP-2587 Ostrander Retail, Retail, north_america, hypercare, 2026-10-12, on_track/on_track, Dana Whitfield, 650, 48000 usd, 260/248, America/New_York; IMP-2618 Tsubame Insurance, Insurance, japan, migration, 2026-11-27, on_track/on_track, Kenji Arai, 3100, 21600000 jpy, 900/610, Asia/Tokyo; IMP-2609 Nordwerk Maschinenbau, Manufacturing, europe, go_live, 2026-11-09, at_risk/at_risk, Jonas Weber, 5600, 412000 eur, 1300/1190, Europe/Berlin; IMP-2624 Lumen Bank, Financial services, north_america, kickoff, 2027-03-15, on_track/on_track, Sam Okafor, 8800, 720000 usd, 1900/40, America/New_York; IMP-2602 Fjordline Media, Media, europe, configuration, 2026-12-14 (original 2026-11-30), at_risk/on_track, Jonas Weber, 1400, 96000 eur, 520/300, Europe/Oslo; IMP-2612 Hikari Foods, Food and beverage, japan, training, 2026-12-01, on_track/on_track, Aiko Tanaka, 2600, 18200000 jpy, 700/520, Asia/Tokyo; IMP-2595 Redwater Logistics, Logistics, north_america, go_live, 2026-11-02, on_track/on_track, Dana Whitfield, 3900, 260000 usd, 980/900, America/Chicago; IMP-2619 Alpenrose Hotels, Hospitality, europe, discovery, 2027-02-08, on_track/on_track, Mira Lindqvist, 1800, 118000 eur, 560/60, Europe/Vienna; IMP-2607 Meridian Pharma, Pharmaceuticals, north_america, migration, 2026-12-21 (original 2026-11-23), off_track/off_track, Sam Okafor, 6400, 480000 usd, 1500/1010, America/New_York; IMP-2626 Kawase Electronics, Electronics, japan, kickoff, 2027-03-01, on_track/on_track, Aiko Tanaka, 5200, 34800000 jpy, 1200/20, Asia/Tokyo; IMP-2600 Solberg Telecom, Telecommunications, europe, hypercare, 2026-10-05, on_track/on_track, Jonas Weber, 4100, 290000 eur, 940/930, Europe/Oslo; IMP-2613 Prairie State Credit Union, Financial services, north_america, training, 2026-11-30, at_risk/on_track, Dana Whitfield, 1200, 84000 usd, 410/330, America/Chicago; IMP-2622 Minato Travel Group, Travel, japan, configuration, 2027-01-11, on_track/on_track, Kenji Arai, 2000, 14000000 jpy, 640/220, Asia/Tokyo. Every date is epoch ms at UTC midnight.

### object · ClickUp Command · Task
One task in a project plan, with stage, dates, dependencies and the critical path.

- record · seed · ClickUp Command · Task: twenty tasks of IMP-2611, codes T-2611-01 to T-2611-20: 01 Kickoff workshop (kickoff, done); 02 Discovery interviews (discovery, done); 03 Workspace design sign-off (discovery, done); 04 Configure spaces and statuses (configuration, done); 05 SSO configuration (configuration, done); 06 User list migration wave 1 (migration, done, 6 days late); 07 User list migration wave 2 (migration, in_progress, Yui Sato, 2026-10-19 to 2026-10-30, late 5 days, critical); 08 Data migration: projects (migration, in_progress, Yui Sato, critical, late 4 days); 09 Data migration: docs (migration, blocked, Daichi Ono, late 5 days); 10 Integration test Salesforce (migration, in_progress, Priya Raman); 11 Admin training (training, done); 12 End-user training Tokyo (training, done); 13 End-user training Osaka (training, in_progress); 14 SSO cutover rehearsal 1 (go_live, done, failed); 15 SSO cutover rehearsal 2 (go_live, in_progress, critical, 2026-10-26 to 2026-11-03); 16 Cutover plan sign-off (go_live, not_started, critical, depends on 15); 17 Go-live readiness review (go_live, not_started, critical, depends on 16); 18 Production cutover (go_live, not_started, critical, 2026-11-14 to 2026-11-16, depends on 17); 19 Hypercare rota (hypercare, not_started, depends on 18); 20 Hypercare exit review (hypercare, not_started, depends on 19). Stage go_live holds 5 tasks; the Board shows the column limit from column_limit.

### object · ClickUp Command · RAID item
One risk, assumption, issue or decision on a project, with likelihood and impact.

- record · seed · ClickUp Command · RAID item: RSK-1183 IMP-2611 risk "SSO cutover rehearsal failed twice", owner Kenji Arai, due 2026-11-03, open, likelihood 4, impact 5; RSK-1184 IMP-2611 risk "User list upload has 214 of 50,000 rows failing", 4, 4, open; RSK-1185 IMP-2611 issue "Docs migration blocked on export limits", 3, 4, open; ASM-0311 IMP-2611 assumption "Sponsor team available for cutover weekend"; DEC-0208 IMP-2611 decision "Cutover rehearsal re-run on 3 Nov"; RSK-1170 IMP-2609 risk 4, 4; RSK-1171 IMP-2602 risk 3, 4; RSK-1172 IMP-2598 risk 5, 5; RSK-1173 IMP-2598 risk 4, 5; RSK-1174 IMP-2607 risk 5, 4; RSK-1175 IMP-2613 risk 3, 3; RSK-1176 IMP-2604 risk 2, 3; RSK-1177 IMP-2618 risk 2, 4; RSK-1178 IMP-2615 risk 1, 2; RSK-1179 IMP-2621 risk 2, 2; RSK-1180 IMP-2624 risk 1, 3; RSK-1181 IMP-2612 risk 2, 2; RSK-1182 IMP-2595 risk 3, 2; RSK-1186 IMP-2619 risk 1, 1; RSK-1187 IMP-2622 risk 2, 3. Every risk is open, with an owner from its project's lead and history_json holding its creation.

## Business rules
- A change request under 40 hours needs the Delivery director's approval; 40 hours or more needs the Delivery director, then the Finance partner, in that order.
- Rejecting a change request, returning a timesheet, or requesting changes on a deliverable needs a written reason.
- An approved change request moves the project's go-live date and planned hours and is recorded in the activity feed.
- A booking that takes a consultant above 100% of capacity in any week shows who, which weeks and by how much before it is saved.
- A customer sponsor sees only their own project and never internal health.
- An unanswered checklist item shows as Not set, never as a guessed value.
- Everything Delivery Copilot writes is labelled AI-written; nothing it proposes is created without acceptance.
- Activity rows are never edited.
- Every test record and every sent email is labelled DEMO-TEST with the demo date.


## Ready when
- `get_objects` shows ClickUp Command · Activity (`OBJ_cucmd_activity`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · AI output (`OBJ_cucmd_ai_output`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Weekly metric (`OBJ_cucmd_weekly_metric`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Saved view (`OBJ_cucmd_saved_view`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Checklist item (`OBJ_cucmd_checklist_item`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Integration (`OBJ_cucmd_integration`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Notification (`OBJ_cucmd_notification`) with every field its Contract line names.
- `get_records` on `OBJ_cucmd_project` holds every row the Project seed line names.
- `get_records` on `OBJ_cucmd_task` holds every row the Task seed line names.
- `get_records` on `OBJ_cucmd_raid` holds every row the RAID item seed line names.

## Assumptions
- Check this: intent proposed as `both` (the outcome, then how): one hood beat after the lean-forward beat; the owner sets it at G2.
- Check this: scope is one app covering every ask, led by the portfolio dashboard, the executive summary and Delivery Copilot (G1 question 1, recommended option).
- Check this: 18 fictional projects around the BRD's six sample customers; the headline counts read like the BRD's portfolio from the Weekly metric rows (G1 question 8).
- Check this: the phone view is a responsive layout of the same code app shown in a phone frame (G1 question 9).
- Check this: integrations show seeded status with one Sync failed row; the one live external step is the weekly summary email through the existing Gmail connection (G1 questions 10 and 11).
- Check this: customers never see internal health (G1 question 5); the timeline is not editable from the phone (G1 question 4); region shows as a labelled tag, never colour alone (G1 question 6).
- Check this: brand colour `#5F55EE` (hue 244) from clickup.com's `--ProductScreen-CustomStatus-Primary`; the sample was ambiguous and the profile takes the recommended one.
- Check this: typeface Inter, the body face of clickup.com, with tabular figures, Noto Sans JP for Japanese, IBM Plex Mono kept for eyebrows (open question 13).
- Check this: the app's sign-in, forgot and reset password are the tenant's own pages a PRIVATE code app opens with (open question 14).
- Check this: roles are a persona switcher in the profile menu with a seeded roles grid; no tenant roles are made (open question 15).
- Check this: documents open in an in-app viewer of the text the record holds; no file is uploaded.
- Check this: customer logos on project cards and in the portal are circles holding the customer's initials, since the customers are invented.
- Check this: German and Japanese portal text is drafted by Studio for the client to review.
- Check this: the Copilot's working stages are shown by the app while the call runs (Reading projects, Checking risks, Writing answer).
- Light is the default theme with the dark tokens live; Appearance in the profile menu switches it.
- The AI agent's model is Nebula's recommendation (profile standing answer).
- Release: publish and deploy on the tenant without asking; visibility PRIVATE (profile).
