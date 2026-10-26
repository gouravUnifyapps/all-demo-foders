---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 3 of 9: seed rows"
touches: [{"kind":"object","name":"ClickUp Command · Change request","id":"OBJ_cucmd_change_request"},{"kind":"object","name":"ClickUp Command · Person","id":"OBJ_cucmd_person"},{"kind":"object","name":"ClickUp Command · Booking","id":"OBJ_cucmd_booking"},{"kind":"object","name":"ClickUp Command · Time entry","id":"OBJ_cucmd_time_entry"},{"kind":"object","name":"ClickUp Command · Deliverable","id":"OBJ_cucmd_deliverable"},{"kind":"object","name":"ClickUp Command · Session slot","id":"OBJ_cucmd_session_slot"},{"kind":"object","name":"ClickUp Command · Document","id":"OBJ_cucmd_document"},{"kind":"object","name":"ClickUp Command · Activity","id":"OBJ_cucmd_activity"},{"kind":"object","name":"ClickUp Command · AI output","id":"OBJ_cucmd_ai_output"},{"kind":"object","name":"ClickUp Command · Weekly metric","id":"OBJ_cucmd_weekly_metric"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-26T12:15:47.279Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf4476769c8b649e93b28a"]
latestPlanId: "e_6adf4476769c8b649e93b28a"
planId: "e_6adf4476769c8b649e93b28a"
---
# ClickUp Delivery Command · build 3 of 9: seed rows

## Requested outcome
Build 3 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds seed rows. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- object · ClickUp Command · Change request · OBJ_cucmd_change_request
- object · ClickUp Command · Person · OBJ_cucmd_person
- object · ClickUp Command · Booking · OBJ_cucmd_booking
- object · ClickUp Command · Time entry · OBJ_cucmd_time_entry
- object · ClickUp Command · Deliverable · OBJ_cucmd_deliverable
- object · ClickUp Command · Session slot · OBJ_cucmd_session_slot
- object · ClickUp Command · Document · OBJ_cucmd_document
- object · ClickUp Command · Activity · OBJ_cucmd_activity
- object · ClickUp Command · AI output · OBJ_cucmd_ai_output
- object · ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric

## Contract

### object · ClickUp Command · Change request
One proposed change to a project, with its rule-routed approval steps.

- record · seed · ClickUp Command · Change request: CR-0455 IMP-2604 "Add Slack integration", +24 h, 4320 eur, 0 days, route delivery director approved, status approved; CR-0456 IMP-2598 "Extra sandbox migration", +64 h, 11520 usd, +7 days, route director approved then finance partner rejected with reason "Budget for this quarter is spent; raise again in January", status rejected. CR-0457 is not seeded: it is raised live in beat 2.

### object · ClickUp Command · Person
One internal user or customer sponsor, with region, capacity and skill levels.

- record · seed · ClickUp Command · Person: P-01 Kenji Arai implementation_lead japan; P-02 Mira Lindqvist implementation_lead europe; P-03 Dana Whitfield implementation_lead north_america; P-04 Sam Okafor implementation_lead north_america; P-05 Jonas Weber implementation_lead europe; P-06 Aiko Tanaka implementation_lead japan; P-07 Yui Sato consultant japan (data migration 3, integrations 2, admin training 2, API 1, Japanese 4); P-08 Daichi Ono consultant japan (3, 2, 3, 2, 4); P-09 Lena Brandt consultant europe (2, 3, 4, 1, 0); P-10 Priya Raman consultant north_america (2, 4, 1, 4, 0); P-11 Carla Mendes consultant north_america (4, 2, 2, 2, 0); P-12 Tom Hale resource_manager europe; P-13 Elena Fischer delivery_director europe; P-14 Marcus Bell finance_partner north_america; P-15 Haruto Mori customer_sponsor japan, project IMP-2611, language ja; P-16 Grace Lin customer_sponsor north_america, project IMP-2598, language en. Capacity 40 h each; emails `<first>.<last>@example.com`.

### object · ClickUp Command · Booking
Hours one person is booked on one project for a run of weeks.

- record · seed · ClickUp Command · Booking: B-01 P-07 IMP-2611 from 2026-10-26, 4 weeks, 24 h; B-02 P-07 IMP-2618 from 2026-10-26, 8 weeks, 8 h; B-03 P-08 IMP-2612 from 2026-10-26, 6 weeks, 20 h; B-04 P-05 IMP-2609 from 2026-10-26, 5 weeks, 24 h; B-05 P-05 IMP-2602 from 2026-11-16, 4 weeks, 20 h; B-06 P-09 IMP-2615 from 2026-10-26, 4 weeks, 30 h; B-07 P-09 IMP-2619 from 2026-11-23, 10 weeks, 10 h; B-08 P-10 IMP-2598 from 2026-10-26, 12 weeks, 24 h; B-09 P-10 IMP-2621 from 2026-11-02, 8 weeks, 12 h; B-10 P-11 IMP-2607 from 2026-10-26, 8 weeks, 32 h; B-11 P-11 IMP-2613 from 2026-10-26, 5 weeks, 8 h; B-12 P-01 IMP-2611 from 2026-10-26, 6 weeks, 20 h; B-13 P-01 IMP-2618 from 2026-10-26, 6 weeks, 10 h; B-14 P-02 IMP-2604 from 2026-10-26, 8 weeks, 20 h; B-15 P-03 IMP-2595 from 2026-10-26, 2 weeks, 16 h; B-16 P-04 IMP-2624 from 2026-11-09, 12 weeks, 16 h; B-17 P-06 IMP-2626 from 2026-11-02, 12 weeks, 12 h; B-18 P-06 IMP-2622 from 2026-10-26, 10 weeks, 16 h. Jonas Weber is at 110% in the weeks of 16 and 23 Nov 2026.

### object · ClickUp Command · Time entry
Hours one person logged on one task on one day, inside a weekly timesheet.

- record · seed · ClickUp Command · Time entry: E-01 to E-15, week of 2026-10-19: P-07 on T-2611-07 Mon to Fri 6 h, 6 h, 7 h, 6 h, 5 h (submitted); P-07 on T-2611-08 Mon to Fri 2 h each (submitted); P-08 on T-2611-09 Mon to Fri 4 h each (submitted). E-16 to E-20, week of 2026-10-26, each a Monday draft: P-07 on T-2611-07 6 h, P-08 on T-2611-09 4 h, P-10 on T-2611-10 3 h, P-07 on T-2611-08 2 h, P-08 on T-2611-13 3 h.

### object · ClickUp Command · Deliverable
One stage deliverable awaiting or carrying the sponsor sign-off.

- record · seed · ClickUp Command · Deliverable: D-2611-1 Workspace design (discovery, signed_off by Haruto Mori 2026-08-21); D-2611-2 Configuration build (configuration, signed_off 2026-09-18); D-2611-3 Migration wave 1 report (migration, signed_off 2026-10-09); D-2611-4 Training completion (training, signed_off 2026-10-20); D-2611-5 Cutover plan (go_live, awaiting_signoff, due 2026-10-29); each with title, title_ja and title_de.

### object · ClickUp Command · Session slot
One bookable customer training slot.

- record · seed · ClickUp Command · Session slot: S-01 to S-12 for IMP-2611, topic "Admin training: permissions", 3 days (2026-10-28, 2026-10-29, 2026-10-30) at 10:00, 13:00, 15:00 and 17:00 Asia/Tokyo, 60 min; S-02, S-05 and S-10 taken.

### object · ClickUp Command · Document
One file in a project library, a published status report or a customer upload with its row errors.

- record · seed · ClickUp Command · Document: DOC-01 IMP-2611 sow "Statement of work: Sakura Mobility", shared; DOC-02 IMP-2611 migration_plan "Migration plan v3", shared; DOC-03 IMP-2611 signoff_record "Sign-off: Configuration build"; DOC-04 IMP-2611 signoff_record "Sign-off: Migration wave 1"; DOC-05 IMP-2611 upload "sakura-users-wave2.csv", 50000 rows, 214 errors, needs_fixing, errors_json holding the first 20 errors (missing email, duplicate email, unknown department); DOC-06 IMP-2611 status_report "Weekly status 19 Oct", ai_written true, edited by Kenji Arai, published 2026-10-19; DOC-07 IMP-2604 sow; DOC-08 IMP-2598 migration_plan. Each body is the readable text the viewer shows.

### object · ClickUp Command · Activity
One change on a project: who did what and when; never edited; also the audit log.

- record · seed · ClickUp Command · Activity: twenty rows across IMP-2611, IMP-2604, IMP-2598 and IMP-2609 from 2026-10-12 to 2026-10-26, among them A-20 IMP-2611 Kenji Arai updated "Health changed On track to At risk" 2026-10-26 and A-19 IMP-2611 Haruto Mori signed_off "Training completion" 2026-10-20.

### object · ClickUp Command · AI output
One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report draft.

- record · seed · ClickUp Command · AI output: AI-01 IMP-2611 risk_flag "Likely to miss 16 Nov go-live", confidence 78, evidence "4 of 6 migration tasks late by 5 days on average", "SSO cutover rehearsal failed twice (RSK-1183)", "214 of 50,000 user rows failing (DOC-05)"; AI-02 IMP-2609 risk_flag confidence 64, evidence "Go-live readiness review moved twice"; AI-03 IMP-2602 risk_flag confidence 52, evidence "Configuration 20% behind plan"; AI-04 IMP-2611 meeting_summary "Steering meeting 22 Oct" with decisions ("Cutover rehearsal re-run on 3 Nov"), actions ("Sakura IT to fix 214 user rows by 30 Oct") and risks ("Cutover weekend staffing"), each with transcript_refs_json pointing to lines of the transcript held in body; AI-05, AI-06, AI-07 IMP-2611 proposed_task from AI-04 ("Fix 214 failing user rows", "Book cutover weekend support", "Re-run SSO rehearsal"), decision proposed; AI-08 IMP-2611 status_report draft of 19 Oct. Every row ai_written true.

### object · ClickUp Command · Weekly metric
The portfolio health counts, the six headline numbers and the value bridge for one week.

- record · seed · ClickUp Command · Weekly metric: twelve weeks from 2026-08-10 to 2026-10-26; on-track share 81, 80, 80, 79, 78, 78, 77, 77, 76, 76, 75, 75 percent; week 2026-10-19 on_track 159, at_risk 33, off_track 19, active 211; week 2026-10-26 on_track 161, at_risk 38, off_track 15, active 214, golives_this_month 9 (last week 10), avg_days_to_golive 61 (last week 63), utilisation_pct 87 (last week 83), value_awaiting_usd 18400000 (last month 17800000), bridge_new 2100000, bridge_golives -1300000, bridge_slipped 200000, bridge_cancelled -400000, top_movers_json naming IMP-2611 (On track to At risk: cutover rehearsal failed), IMP-2602 (go-live slipped 2 weeks), IMP-2613 (On track to At risk: training attendance 48%), IMP-2598 (At risk to Off track: sandbox change request rejected), IMP-2607 (go-live slipped 4 weeks), last_updated 2026-10-26 06:00 UTC.

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
- `get_records` on `OBJ_cucmd_change_request` holds every row the Change request seed line names.
- `get_records` on `OBJ_cucmd_person` holds every row the Person seed line names.
- `get_records` on `OBJ_cucmd_booking` holds every row the Booking seed line names.
- `get_records` on `OBJ_cucmd_time_entry` holds every row the Time entry seed line names.
- `get_records` on `OBJ_cucmd_deliverable` holds every row the Deliverable seed line names.
- `get_records` on `OBJ_cucmd_session_slot` holds every row the Session slot seed line names.
- `get_records` on `OBJ_cucmd_document` holds every row the Document seed line names.
- `get_records` on `OBJ_cucmd_activity` holds every row the Activity seed line names.
- `get_records` on `OBJ_cucmd_ai_output` holds every row the AI output seed line names.
- `get_records` on `OBJ_cucmd_weekly_metric` holds every row the Weekly metric seed line names.

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
