---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 4 of 10"
touches: [{"kind":"object","name":"Delivery Command · Session slot"},{"kind":"object","name":"Delivery Command · Sign-off"},{"kind":"object","name":"Delivery Command · Checklist item"},{"kind":"object","name":"Delivery Command · Notification"},{"kind":"object","name":"Delivery Command · Integration"},{"kind":"object","name":"Delivery Command · Saved view"},{"kind":"object","name":"Delivery Command · Weekly snapshot"},{"kind":"object","name":"Delivery Command · Weekly metric"},{"kind":"object","name":"Delivery Command · AI output"},{"kind":"object","name":"Delivery Command · Role permission"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-23T18:02:28.168Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adba1375236864dd8e627db"]
latestPlanId: "e_6adba1375236864dd8e627db"
planId: "e_6adba1375236864dd8e627db"
---
# ClickUp Delivery Command · plan 4 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 4 of 10) builds the data layer: Session slot rows, Sign-off rows, Checklist item rows, Notification rows, Integration rows, Saved view rows, Weekly snapshot rows, Weekly metric rows, AI output rows, Role permission rows.

## Touches
- object · Delivery Command · Session slot · new
- object · Delivery Command · Sign-off · new
- object · Delivery Command · Checklist item · new
- object · Delivery Command · Notification · new
- object · Delivery Command · Integration · new
- object · Delivery Command · Saved view · new
- object · Delivery Command · Weekly snapshot · new
- object · Delivery Command · Weekly metric · new
- object · Delivery Command · AI output · new
- object · Delivery Command · Role permission · new

## Contract

### object · Delivery Command · Session slot
One bookable customer training slot.
- record · seed · Delivery Command · Session slot: the 12 rows of studio/data/seed/session_slot.csv (4 taken)

### object · Delivery Command · Sign-off
One stage deliverable awaiting or carrying the customer sponsor's sign-off.
- record · seed · Delivery Command · Sign-off: the 4 rows of studio/data/seed/signoff.csv (SGN-302 Migration plan v2 Awaiting sign-off)

### object · Delivery Command · Checklist item
One of the ten readiness questions with the customer's answer.
- record · seed · Delivery Command · Checklist item: the 10 rows of studio/data/seed/checklist_item.csv (7 answered, 3 not set)

### object · Delivery Command · Notification
One assignment, sign-off or mention for a user.
- record · seed · Delivery Command · Notification: the 6 rows of studio/data/seed/notification.csv

### object · Delivery Command · Integration
The sync status of one connected system.
- record · seed · Delivery Command · Integration: the 4 rows of studio/data/seed/integration.csv (Jira Sync failed since 06:40 UTC, 3 escalations affected)

### object · Delivery Command · Saved view
One named, shareable set of portfolio filters.
- record · seed · Delivery Command · Saved view: the 2 rows of studio/data/seed/saved_view.csv

### object · Delivery Command · Weekly snapshot
Portfolio health counts for one week, for the trend.
- record · seed · Delivery Command · Weekly snapshot: the 12 rows of studio/data/seed/weekly_snapshot.csv (on-track share 88.2% down to 66.7%)

### object · Delivery Command · Weekly metric
The executive summary's six headline numbers and the contract value bridge for one week.
- record · seed · Delivery Command · Weekly metric: the 1 row of studio/data/seed/weekly_metric.csv

### object · Delivery Command · AI output
One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report.
- record · seed · Delivery Command · AI output: the 7 rows of studio/data/seed/ai_output.csv, every row ai_written true

### object · Delivery Command · Role permission
One role's row in the roles-against-permissions grid.
- record · seed · Delivery Command · Role permission: the 6 rows of studio/data/seed/role_permission.csv

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
- Delivery Command · Session slot holds every seed row of its file
- Delivery Command · Sign-off holds every seed row of its file
- Delivery Command · Checklist item holds every seed row of its file
- Delivery Command · Notification holds every seed row of its file
- Delivery Command · Integration holds every seed row of its file
- Delivery Command · Saved view holds every seed row of its file
- Delivery Command · Weekly snapshot holds every seed row of its file
- Delivery Command · Weekly metric holds every seed row of its file
- Delivery Command · AI output holds every seed row of its file
- Delivery Command · Role permission holds every seed row of its file

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
