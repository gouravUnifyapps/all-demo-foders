---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 1 of 10"
touches: [{"kind":"object","name":"Delivery Command · Project"},{"kind":"object","name":"Delivery Command · Task"},{"kind":"object","name":"Delivery Command · RAID item"},{"kind":"object","name":"Delivery Command · Person"},{"kind":"object","name":"Delivery Command · Booking"},{"kind":"object","name":"Delivery Command · Time entry"},{"kind":"object","name":"Delivery Command · Change request"},{"kind":"object","name":"Delivery Command · Activity"},{"kind":"object","name":"Delivery Command · Document"},{"kind":"object","name":"Delivery Command · Session slot"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-23T17:15:02.163Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adb96180881d2257a9f97c3"]
latestPlanId: "e_6adb96180881d2257a9f97c3"
planId: "e_6adb96180881d2257a9f97c3"
---
# ClickUp Delivery Command · plan 1 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 1 of 10) builds the data layer: Project, Task, RAID item, Person, Booking, Time entry, Change request, Activity, Document, Session slot.

## Touches
- object · Delivery Command · Project · new
- object · Delivery Command · Task · new
- object · Delivery Command · RAID item · new
- object · Delivery Command · Person · new
- object · Delivery Command · Booking · new
- object · Delivery Command · Time entry · new
- object · Delivery Command · Change request · new
- object · Delivery Command · Activity · new
- object · Delivery Command · Document · new
- object · Delivery Command · Session slot · new

## Contract

### object · Delivery Command · Project
One customer implementation, from signed contract to Hypercare.
- object · create · Delivery Command · Project (`OBJ_dcmd_project`): project_id text unique (IMP-nnnn), customer text, customer_initials text, region picklist (north_america "North America", europe "Europe", japan "Japan"), stage picklist (kickoff "Kickoff", discovery "Discovery", configuration "Configuration", data_migration "Data migration", integrations "Integrations", training "Training", hypercare "Hypercare"), stage_index number 1 to 7, go_live date epoch ms, baseline_go_live date epoch ms, slipped boolean, health picklist (on_track "On track", at_risk "At risk", off_track "Off track"), lead text, seats number, contract_value number, currency picklist (USD, EUR, JPY), budget_hours number, used_hours number, lifecycle picklist (active "Active", live "Live", cancelled "Cancelled"), sponsor text, portal_language picklist (en, de, ja), last_synced_at datetime epoch ms; index on region, health, lead

### object · Delivery Command · Task
One task in a project plan, with dates, dependencies and the critical path.
- object · create · Delivery Command · Task (`OBJ_dcmd_task`): task_id text unique (TSK-nnnn), project_id text, title text, description long text, stage picklist (the seven stage codes of Project), status picklist (not_started "Not started", in_progress "In progress", blocked "Blocked", done "Done"), assignee text, start date epoch ms, end date epoch ms, depends_on text (a task_id), critical boolean, hours_planned number, hours_logged number, ai_proposed boolean; index on project_id, assignee

### object · Delivery Command · RAID item
One risk, assumption, issue or decision on a project.
- object · create · Delivery Command · RAID item (`OBJ_dcmd_raid`): raid_id text unique (RSK-, ASM-, ISS-, DEC-nnnn), project_id text, type picklist (risk "Risk", assumption "Assumption", issue "Issue", decision "Decision"), title text, owner text, due date epoch ms, status picklist (open "Open", mitigating "Mitigating", closed "Closed"), likelihood number 1 to 5, impact number 1 to 5, jira_key text, history long text

### object · Delivery Command · Person
One internal user or customer sponsor, with capacity and skill levels.
- object · create · Delivery Command · Person (`OBJ_dcmd_person`): person_id text unique (PER-nnn), name text, role picklist (consultant "Consultant", lead "Implementation lead", director "Delivery director", resource_manager "Resource manager", finance_partner "Finance partner", sponsor "Customer sponsor"), region picklist (as Project), capacity_hours number, skill_data_migration number 0 to 4, skill_integrations number 0 to 4, skill_admin_training number 0 to 4, skill_api number 0 to 4, skill_japanese number 0 to 4, customer text, email text, time_zone text, week_start picklist (monday "Monday", sunday "Sunday")

### object · Delivery Command · Booking
Hours one person is booked on one project in one week.
- object · create · Delivery Command · Booking (`OBJ_dcmd_booking`): booking_id text unique (BKG-nnnn), person text, project_id text, week_start date epoch ms, hours number; index on person, week_start

### object · Delivery Command · Time entry
Hours one person logged on one task on one day, inside a weekly timesheet.
- object · create · Delivery Command · Time entry (`OBJ_dcmd_time_entry`): entry_id text unique (TME-nnnn), person text, task_id text, project_id text, date date epoch ms, hours number, timesheet_week date epoch ms, timesheet_status picklist (draft "Draft", submitted "Pending approval", approved "Approved", returned "Returned"), return_reason text

### object · Delivery Command · Change request
One proposed change to a project, with its two-step approval route.
- object · create · Delivery Command · Change request (`OBJ_dcmd_change_request`): cr_id text unique (CR-nnnn), project_id text, raised_by text, reason long text, work_added long text, work_removed long text, hours_delta number, cost_delta number, currency picklist (USD, EUR, JPY), golive_before date epoch ms, golive_after date epoch ms, plan_before long text (JSON task list), plan_after long text (JSON task list), route picklist (director "Delivery director", director_finance "Delivery director, then finance partner"), step1_status picklist (pending, approved, rejected), step1_by text, step1_at datetime epoch ms, step2_status picklist (not_needed, waiting, pending, approved, rejected), step2_by text, step2_at datetime epoch ms, next_approver text, status picklist (draft "Draft", pending_approval "Pending approval", approved "Approved", rejected "Rejected"), reject_reason long text

### object · Delivery Command · Activity
One change on a project: who did what and when; never edited.
- object · create · Delivery Command · Activity (`OBJ_dcmd_activity`): activity_id text unique (ACT-nnnn), at datetime epoch ms, actor text, project_id text, action text, target text, detail text, source picklist (app "Delivery Command", automation "Automation", ai "Delivery Copilot", salesforce "Salesforce"); rows are only ever created, never updated or deleted; index on project_id, actor, action

### object · Delivery Command · Document
One file in a project library: statement of work, migration plan or sign-off record.
- object · create · Delivery Command · Document (`OBJ_dcmd_document`): document_id text unique (DOC-nn), project_id text, title text, body long text (the document's text, shown in the in-app viewer), kind picklist (sow "Statement of work", migration_plan "Migration plan", signoff_record "Sign-off record", other "Other"), file_url text, shared_with_customer boolean, source text, uploaded_by text, at date epoch ms

### object · Delivery Command · Session slot
One bookable customer training slot.
- object · create · Delivery Command · Session slot (`OBJ_dcmd_session_slot`): slot_id text unique (SLT-nn), project_id text, date date epoch ms, start text, end text, topic text, taken boolean, booked_by text

## Business rules
- Changes under 40 hours need the delivery director's approval; changes of 40 hours or more also need the finance partner, in that order.
- Rejecting a change request needs a written reason; returning a timesheet needs a reason; requesting changes on a sign-off needs a comment.
- An approved change updates the plan (tasks, go-live, budget hours) and is recorded in the activity feed.
- A board column shows a warning when it holds more than 15 tasks.
- A booking above a person's weekly capacity shows who, which weeks and by how much before it is saved.
- The activity record is never edited or deleted.
- Customers see only their own project and never internal health.
- Anything Delivery Copilot writes carries an AI-written label; nothing it proposes is created without acceptance.
- Every status shows an icon and a word, never colour alone; status words follow BRD §8 (good: On track, Signed off, Approved, Live; attention: At risk, Awaiting sign-off, Over capacity, Pending approval; problem: Off track, Blocked, Rejected, Sync failed; neutral: Not started, Draft, Scheduled, Hypercare).
- Errors say what happened and what to do next; no jokes or exclamation marks.
- Money shows in the contract currency; portfolio totals in USD at planning rates EUR 1.08 and JPY 0.0066.
- Dates show in the user's format (17 Oct 2026, 17.10.2026, 2026年10月17日); weeks start on Monday in Europe and Japan and Sunday in North America.
- No screen suggests billing, invoicing, revenue recognition, editing customer workspaces, hiring, payroll, a marketing site, video calls or offline phone use.
- Look: the app's one stylesheet is /home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/design-system/clickup/client.css (hue 244, brand #5F55EE); the rail logo is /home/user/all-demo-foders/clickup/clickup-delivery-command-platform/studio/design-system/clickup/logo.svg and the collapsed rail and tab icon use logo-mark.svg beside it, both as published; theme light by default with the dark tokens live and the switch in the profile menu.
- Test records written during the demo carry the DEMO-TEST label and the demo's date.

## Ready when
- Delivery Command · Project exists with every field the contract lists
- Delivery Command · Task exists with every field the contract lists
- Delivery Command · RAID item exists with every field the contract lists
- Delivery Command · Person exists with every field the contract lists
- Delivery Command · Booking exists with every field the contract lists
- Delivery Command · Time entry exists with every field the contract lists
- Delivery Command · Change request exists with every field the contract lists
- Delivery Command · Activity exists with every field the contract lists
- Delivery Command · Document exists with every field the contract lists
- Delivery Command · Session slot exists with every field the contract lists

## Assumptions
- Check this: proposed intent `both` (the outcome first, then 2 hood beats); the owner sets it at G2.
- Check this: G1 open questions 1 to 12 are unanswered; the plan follows each recommended option (portal shows no internal health; phone stays at today, status, time and alerts; portfolio opens on one screen with the paged list below; region as a labelled chip; A114 out of scope; integrations seeded; the official logo; a phone-width route; full portal language switch; 18 seeded projects and 13 consultants with a generated 50,000-row upload; a seeded finance partner; a scheduled email with one test run).
- Check this: the brand colour #5F55EE (hue 244) is brand-sample's recommendation among 14 candidates (profile standing answer for an ambiguous colour).
- Check this: the logo is ClickUp's own nav wordmark from clickup.com, saved as published; the script's first pick was the ClickUp Brain mark and was replaced.
- Check this: the seven stage names (Kickoff, Discovery, Configuration, Data migration, Integrations, Training, Hypercare) and the persona names are assumed; the BRD's own stage names are not in the state file.
- Check this: earlier "ClickUp DC ·" and "DC" objects, automations and agents exist on the tenant outside this solution; this build uses new "Delivery Command ·" names and touches none of them.
- Check this: the executive email sends only on a mail connection the owner names; until then Send executive summary stores a preview row.
- Check this: sign-in, forgot and reset password screens and the persona switch stand in for real accounts, which need governance tools not granted yet.
- Check this: Word export of the status report is an HTML document saved as .doc from the app; PDF is the browser's print to PDF.
- Check this: the code app name ClickUp Delivery Command is free; if taken, the name gets the suffix "· Demo".
- All seed rows are fictional; customer names follow the BRD's six invented customers plus twelve more invented names.
