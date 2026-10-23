---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 9 of 10"
touches: [{"kind":"code-app","name":"ClickUp Delivery Command"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-23T19:06:42.004Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adbb044925d282255d09cab"]
latestPlanId: "e_6adbb044925d282255d09cab"
planId: "e_6adbb044925d282255d09cab"
---
# ClickUp Delivery Command · plan 9 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 9 of 10) builds the code app's shell and its internal screens; every object, automation and the Copilot agent it uses already exist in this solution.

## Touches
- code-app · ClickUp Delivery Command · new

## Contract

### code-app · ClickUp Delivery Command
The code app: internal workspace, customer portal and phone view.
- code-app · create · ClickUp Delivery Command: the shell: the design system stylesheet, the fonts, the rail (ClickUp logo; Portfolio, Projects, Resourcing, Timesheets, Changes, Admin), the top bar (current project or view, search, notifications, profile menu with persona switch, appearance Light or Dark, Phone view and Customer portal entries), the right-hand Copilot panel slot, the routes for Sign-in, Forgot password, Reset password, Portfolio, Projects, Project, Resourcing, Timesheets, Changes, Change request, Executive summary, Admin, Portal home, Portal sign-offs, Portal sessions, Portal files, Portal checklist and Phone; PRIVATE
- code-app · update · ClickUp Delivery Command: screen Sign-in, Forgot password, Reset password: the ClickUp logo, a persona picker standing in for sign-in, the two password screens with their inline errors; screen Portfolio: `.tile` health counts with `.delta` since last week, risk grid `.chart` (likelihood by impact, choosing a cell lists its risks in a `.tbl`), 90-day go-live timeline grouped by region with slipped dates marked, 12-week on-track share `.spark` in a `.chart`, project `.toolbar` (search, region, stage, health, lead `.chipsel`, removable chips with Clear all, "x of y") above a `.tblwrap .tbl` with `.pg`, Save view; reads Project, RAID item, Weekly snapshot, Saved view · calls Save view on Save
- code-app · update · ClickUp Delivery Command: screen Project (overview, board, list, task detail): `.crumb`, overview `.stages` of the seven stages, `.tile` days to go-live, budget hours used against planned `.prog`, open risks, next sign-off due; board `.kb` one column per stage with a `.tag.attention` warning above 15, drag and a Move to menu; list `.tbl`; task detail in a side pane beside the list (description, assignee, dates, time logged, comments, attachments); reads Project, Task, RAID item, Sign-off · calls Move task on a drop or Move to
- code-app · update · ClickUp Delivery Command: screen Project (timeline, RAID, documents, activity): timeline of tasks with dependencies and the critical path, a date change previewing the new go-live before Save; RAID `.tabs` with owner, due date, status and history; document library `.tbl` with an in-app viewer pane that pages the document's body; activity `.feed`; reads Task, RAID item, Document, Activity · calls Reschedule task on preview and Save
- code-app · update · ClickUp Delivery Command: screen Resourcing: people against the next 12 weeks with percent booked per week, over 100% as `.tag.negative`, region as a labelled chip; Book consultant form (person, project, weeks, hours) with the over-capacity `.note` before Save; skills matrix (data migration, integrations, admin training, API, Japanese language) with levels; booked against capacity by region for the quarter `.chart`; screen Timesheets: weekly timesheets `.tbl` with batch select, Approve and Return with a required reason; reads Person, Booking, Time entry · calls Book consultant on Check and Save, Review timesheets on Approve and Return
- code-app · update · ClickUp Delivery Command: screen Changes and Change request: list `.tbl`; New change request form (reason, work added or removed, hours, cost, go-live) with the plan before and after side by side and the differences marked; approval `.stv` showing who approved and who is next; Approve and Reject, Reject needing a written reason, the refusal as `.tag.negative` and `.note`; reads Change request, Task, Project · calls Change request on Submit, Approve and Reject
- code-app · update · ClickUp Delivery Command: screen Executive summary: six `.tile` headline numbers with `.delta` coloured by good or bad for the business, the contract value bridge `.chart` (last month, new projects, go-lives completed, slipped dates, cancellations, this month), the five projects that changed most `.tbl` with the reason, Send test email; reads Weekly metric, Weekly snapshot, Project, Activity · calls Send executive summary on Send test email

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
- ClickUp Delivery Command shows the Portfolio, Project, Resourcing, Timesheets, Changes and Executive summary screens on the preview with seeded rows

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
