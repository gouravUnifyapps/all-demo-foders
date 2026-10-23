---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 6 of 10"
touches: [{"kind":"automation","name":"Delivery Command · Change request"},{"kind":"automation","name":"Delivery Command · Accept proposed tasks"},{"kind":"automation","name":"Delivery Command · Publish status report"},{"kind":"automation","name":"Delivery Command · Record sign-off"},{"kind":"automation","name":"Delivery Command · Book training slot"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Change request"},{"action":"deploy","kind":"automation","name":"Delivery Command · Accept proposed tasks"},{"action":"deploy","kind":"automation","name":"Delivery Command · Publish status report"},{"action":"deploy","kind":"automation","name":"Delivery Command · Record sign-off"},{"action":"deploy","kind":"automation","name":"Delivery Command · Book training slot"}]
acceptedAt: "2026-10-23T18:18:24.882Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adba4f3925d282255c4195e"]
latestPlanId: "e_6adba4f3925d282255c4195e"
planId: "e_6adba4f3925d282255c4195e"
---
# ClickUp Delivery Command · plan 6 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 6 of 10) builds and deploys the automations Change request, Accept proposed tasks, Publish status report, Record sign-off, Book training slot; the objects they use already exist in this solution.

## Touches
- automation · Delivery Command · Change request · new
- automation · Delivery Command · Accept proposed tasks · new
- automation · Delivery Command · Publish status report · new
- automation · Delivery Command · Record sign-off · new
- automation · Delivery Command · Book training slot · new

## Contract

### automation · Delivery Command · Change request
Submits, routes, approves and rejects change requests by the 40-hour rule.
- automation · create · Delivery Command · Change request: callable; input action text (submit, approve, reject), cr_id text, project_id text, raised_by text, reason text, work_added text, work_removed text, hours_delta number, cost_delta number, golive_after date, plan_before text, plan_after text, actor text, reject_reason text; submit sets route director when hours_delta is under 40 and director_finance when 40 or more, next_approver Elena Brooks; approve by the director on director_finance sets next_approver Tomás Herrera; the last approval sets status approved, adds the change's tasks from plan_after, moves the project's go_live and budget_hours and writes Activity rows; reject with an empty reject_reason is refused with "A rejection needs a written reason. Add one and reject again."; result cr_id text, status text, route text, next_approver text, refused boolean, message text

### automation · Delivery Command · Accept proposed tasks
Turns accepted Copilot task proposals into tasks.
- automation · create · Delivery Command · Accept proposed tasks: callable; input output_ids list of text, decision text (accept or reject), actor text; accept creates one Task per output and sets the output accepted; reject sets it rejected and creates nothing; result created list of task_id

### automation · Delivery Command · Publish status report
Publishes the lead's edited status report.
- automation · create · Delivery Command · Publish status report: callable; input project_id text, title text, body text, actor text; saves an AI output of kind status_report with status published and ai_written true, writes one Activity row; result output_id text

### automation · Delivery Command · Record sign-off
Records a sponsor's sign-off or change request.
- automation · create · Delivery Command · Record sign-off: callable; input signoff_id text, decision text (sign_off or request_changes), comment text, actor text; request_changes with an empty comment is refused with "Add a comment so the team knows what to change."; saves decided_by and decided_at, writes one Activity row and one Notification for the project lead; result status text, decided_at datetime, refused boolean, message text

### automation · Delivery Command · Book training slot
Books a free training slot for the sponsor.
- automation · create · Delivery Command · Book training slot: callable; input slot_id text, actor text; a slot already taken is refused with "This slot was just taken. Choose another time."; result ok boolean, message text

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
- deploy Delivery Command · Change request
- deploy Delivery Command · Accept proposed tasks
- deploy Delivery Command · Publish status report
- deploy Delivery Command · Record sign-off
- deploy Delivery Command · Book training slot

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
