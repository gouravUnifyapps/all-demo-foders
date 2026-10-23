---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 5 of 10"
touches: [{"kind":"automation","name":"Delivery Command · Move task"},{"kind":"automation","name":"Delivery Command · Reschedule task"},{"kind":"automation","name":"Delivery Command · Book consultant"},{"kind":"automation","name":"Delivery Command · Review timesheets"},{"kind":"automation","name":"Delivery Command · Log time"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Move task"},{"action":"deploy","kind":"automation","name":"Delivery Command · Reschedule task"},{"action":"deploy","kind":"automation","name":"Delivery Command · Book consultant"},{"action":"deploy","kind":"automation","name":"Delivery Command · Review timesheets"},{"action":"deploy","kind":"automation","name":"Delivery Command · Log time"}]
acceptedAt: "2026-10-23T18:06:04.491Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adba20e5236864dd8e64c53"]
latestPlanId: "e_6adba20e5236864dd8e64c53"
planId: "e_6adba20e5236864dd8e64c53"
---
# ClickUp Delivery Command · plan 5 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 5 of 10) builds and deploys the automations Move task, Reschedule task, Book consultant, Review timesheets, Log time; the objects they use already exist in this solution.

## Touches
- automation · Delivery Command · Move task · new
- automation · Delivery Command · Reschedule task · new
- automation · Delivery Command · Book consultant · new
- automation · Delivery Command · Review timesheets · new
- automation · Delivery Command · Log time · new

## Contract

### automation · Delivery Command · Move task
Moves a task to another stage or status and records it.
- automation · create · Delivery Command · Move task: callable; input task_id text, to_stage text, to_status text, actor text; sets the task's stage and status, writes one Activity row; result ok boolean, column_count number, over_limit boolean (column_count above 15), message text

### automation · Delivery Command · Reschedule task
Moves a task's dates, shifts its dependents and previews the new go-live.
- automation · create · Delivery Command · Reschedule task: callable; input task_id text, new_start date, new_end date, actor text, confirm boolean; walks depends_on forward and shifts every dependent task by the same working days; result shifted list of {task_id, new_start, new_end}, golive_before date, golive_after date; with confirm false it writes nothing, with confirm true it saves the tasks, the project's go_live and one Activity row

### automation · Delivery Command · Book consultant
Checks a booking against capacity, then writes it.
- automation · create · Delivery Command · Book consultant: callable; input person text, project_id text, weeks list of dates, hours number, actor text, confirm boolean; sums Booking hours per week against the Person's capacity_hours; result over_capacity list of {week_start, booked_hours, capacity_hours, percent}, ok boolean, message text; with confirm false it writes nothing; with confirm true it writes one Booking per week and one Activity row

### automation · Delivery Command · Review timesheets
Approves or returns weekly timesheets in a batch.
- automation · create · Delivery Command · Review timesheets: callable; input persons list of text, timesheet_week date, decision text (approve or return), reason text, actor text; result updated number, refused boolean, message text; decision return with an empty reason is refused with "A returned timesheet needs a reason."

### automation · Delivery Command · Log time
Logs hours on a task from the phone.
- automation · create · Delivery Command · Log time: callable; input person text, task_id text, date date, hours number, status text; writes a Time entry in Draft, adds hours to the task's hours_logged, sets the task status when given, writes one Activity row; result entry_id text

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
- deploy Delivery Command · Move task
- deploy Delivery Command · Reschedule task
- deploy Delivery Command · Book consultant
- deploy Delivery Command · Review timesheets
- deploy Delivery Command · Log time

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
