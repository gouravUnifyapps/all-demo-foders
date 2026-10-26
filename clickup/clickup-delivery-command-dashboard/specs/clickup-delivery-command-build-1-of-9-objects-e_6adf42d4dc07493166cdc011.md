---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 1 of 9: objects, part 1"
touches: [{"kind":"object","name":"ClickUp Command · Project"},{"kind":"object","name":"ClickUp Command · Task"},{"kind":"object","name":"ClickUp Command · RAID item"},{"kind":"object","name":"ClickUp Command · Change request"},{"kind":"object","name":"ClickUp Command · Person"},{"kind":"object","name":"ClickUp Command · Booking"},{"kind":"object","name":"ClickUp Command · Time entry"},{"kind":"object","name":"ClickUp Command · Deliverable"},{"kind":"object","name":"ClickUp Command · Session slot"},{"kind":"object","name":"ClickUp Command · Document"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-26T12:08:52.235Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf42d7dc07493166cdc058"]
latestPlanId: "e_6adf42d7dc07493166cdc058"
planId: "e_6adf42d7dc07493166cdc058"
---
# ClickUp Delivery Command · build 1 of 9: objects, part 1

## Requested outcome
Build 1 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds objects, part 1. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- object · ClickUp Command · Project · new
- object · ClickUp Command · Task · new
- object · ClickUp Command · RAID item · new
- object · ClickUp Command · Change request · new
- object · ClickUp Command · Person · new
- object · ClickUp Command · Booking · new
- object · ClickUp Command · Time entry · new
- object · ClickUp Command · Deliverable · new
- object · ClickUp Command · Session slot · new
- object · ClickUp Command · Document · new

## Contract

### object · ClickUp Command · Project
One customer implementation, from signed contract to Hypercare; the story row is IMP-2611.

- object · create · ClickUp Command · Project: id `OBJ_cucmd_project`; fields project_code (text, primaryKey, required, e.g. `IMP-2611`), customer (text, required), industry (text), region (picklist: europe "Europe", north_america "North America", japan "Japan"), stage (picklist: kickoff "Kickoff", discovery "Discovery", configuration "Configuration", migration "Migration", training "Training", go_live "Go-live", hypercare "Hypercare"), go_live_date (date, epoch ms), original_go_live_date (date, epoch ms; set only when the date slipped), health (picklist: on_track "On track", at_risk "At risk", off_track "Off track"), health_last_week (same codes as health), lead (text), sponsor (text), seats (number), contract_value (number), currency (picklist: usd "USD", eur "EUR", jpy "JPY"), budget_hours_planned (number), budget_hours_used (number), column_limit (number, default 15), next_signoff (text), next_signoff_due (date, epoch ms), timezone (text, IANA name)

### object · ClickUp Command · Task
One task in a project plan, with stage, dates, dependencies and the critical path.

- object · create · ClickUp Command · Task: id `OBJ_cucmd_task`; fields task_code (text, primaryKey, required), project_code (text, required), title (text, required), description (text), stage (the seven Project stage codes), status (picklist: not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee (text), start_date (date, epoch ms), end_date (date, epoch ms), depends_on (text, comma-separated task_codes, finish-to-start), critical (boolean), hours_logged (number), comments_json (text), attachments_json (text), source (picklist: manual "Manual", copilot "Copilot")

### object · ClickUp Command · RAID item
One risk, assumption, issue or decision on a project, with likelihood and impact.

- object · create · ClickUp Command · RAID item: id `OBJ_cucmd_raid`; fields raid_code (text, primaryKey, required, e.g. `RSK-1183`), project_code (text, required), kind (picklist: risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title (text, required), owner (text), due_date (date, epoch ms), status (picklist: open "Open", mitigating "Mitigating", closed "Closed"), likelihood (number 1 to 5), impact (number 1 to 5), history_json (text)

### object · ClickUp Command · Change request
One proposed change to a project, with its rule-routed approval steps.

- object · create · ClickUp Command · Change request: id `OBJ_cucmd_change_request`; fields cr_code (text, primaryKey, required, e.g. `CR-0457`), project_code (text, required), reason (text, required), work_added (text), work_removed (text), hours_delta (number), cost_delta (number), go_live_delta_days (number), before_json (text), after_json (text), route_json (text: the ordered approver steps with role, name, decision, at, reason), next_approver (picklist: delivery_director "Delivery director", finance_partner "Finance partner", none "None"), status (picklist: draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), raised_by (text), raised_at (date, epoch ms), rejection_reason (text)

### object · ClickUp Command · Person
One internal user or customer sponsor, with region, capacity and skill levels.

- object · create · ClickUp Command · Person: id `OBJ_cucmd_person`; fields person_code (text, primaryKey, required), name (text, required), role (picklist: implementation_lead "Implementation lead", consultant "Implementation consultant", delivery_director "Delivery director", finance_partner "Finance partner", resource_manager "Resource manager", customer_sponsor "Customer sponsor"), region (Project region codes), email (text, fictional `@example.com`), capacity_hours (number, default 40), skill_data_migration (number 0 to 4), skill_integrations (number 0 to 4), skill_admin_training (number 0 to 4), skill_api (number 0 to 4), skill_japanese (number 0 to 4), project_code (text; a sponsor's own project), language (picklist: en "English", de "German", ja "Japanese")

### object · ClickUp Command · Booking
Hours one person is booked on one project for a run of weeks.

- object · create · ClickUp Command · Booking: id `OBJ_cucmd_booking`; fields booking_code (text, primaryKey, required), person_code (text, required), project_code (text, required), first_week (date, epoch ms, the Monday), weeks (number), hours_per_week (number), over_capacity (boolean)

### object · ClickUp Command · Time entry
Hours one person logged on one task on one day, inside a weekly timesheet.

- object · create · ClickUp Command · Time entry: id `OBJ_cucmd_time_entry`; fields entry_code (text, primaryKey, required), person_code (text, required), task_code (text, required), project_code (text), work_date (date, epoch ms), hours (number), week_start (date, epoch ms), timesheet_status (picklist: draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason (text)

### object · ClickUp Command · Deliverable
One stage deliverable awaiting or carrying the sponsor sign-off.

- object · create · ClickUp Command · Deliverable: id `OBJ_cucmd_deliverable`; fields deliverable_code (text, primaryKey, required), project_code (text, required), stage (Project stage codes), title (text), title_ja (text), title_de (text), due_date (date, epoch ms), status (picklist: awaiting_signoff "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), decided_by (text), decided_at (date, epoch ms), comment (text)

### object · ClickUp Command · Session slot
One bookable customer training slot.

- object · create · ClickUp Command · Session slot: id `OBJ_cucmd_session_slot`; fields slot_code (text, primaryKey, required), project_code (text), topic (text), slot_start (date, epoch ms), duration_min (number), taken (boolean), booked_by (text)

### object · ClickUp Command · Document
One file in a project library, a published status report or a customer upload with its row errors.

- object · create · ClickUp Command · Document: id `OBJ_cucmd_document`; fields doc_code (text, primaryKey, required), project_code (text, required), kind (picklist: sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", status_report "Status report", upload "Customer upload"), title (text), body (text, the content the in-app viewer shows), shared_with_customer (boolean), row_count (number), error_count (number), errors_json (text: the first errors with row, column and message), upload_status (picklist: checking "Checking", needs_fixing "Needs fixing", confirmed "Confirmed"), ai_written (boolean), edited_by (text), published_at (date, epoch ms)

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
- `get_objects` shows ClickUp Command · Project (`OBJ_cucmd_project`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Task (`OBJ_cucmd_task`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · RAID item (`OBJ_cucmd_raid`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Change request (`OBJ_cucmd_change_request`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Person (`OBJ_cucmd_person`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Booking (`OBJ_cucmd_booking`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Time entry (`OBJ_cucmd_time_entry`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Deliverable (`OBJ_cucmd_deliverable`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Session slot (`OBJ_cucmd_session_slot`) with every field its Contract line names.
- `get_objects` shows ClickUp Command · Document (`OBJ_cucmd_document`) with every field its Contract line names.

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
