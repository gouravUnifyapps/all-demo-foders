---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 3 of 10"
touches: [{"kind":"object","name":"Delivery Command · Executive email"},{"kind":"object","name":"Delivery Command · Project"},{"kind":"object","name":"Delivery Command · Task"},{"kind":"object","name":"Delivery Command · RAID item"},{"kind":"object","name":"Delivery Command · Person"},{"kind":"object","name":"Delivery Command · Booking"},{"kind":"object","name":"Delivery Command · Time entry"},{"kind":"object","name":"Delivery Command · Change request"},{"kind":"object","name":"Delivery Command · Activity"},{"kind":"object","name":"Delivery Command · Document"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-23T17:53:40.468Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adb9f27925d282255ba6215"]
latestPlanId: "e_6adb9f27925d282255ba6215"
planId: "e_6adb9f27925d282255ba6215"
---
# ClickUp Delivery Command · plan 3 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 3 of 10) builds the data layer: Executive email, Project rows, Task rows, RAID item rows, Person rows, Booking rows, Time entry rows, Change request rows, Activity rows, Document rows.

## Touches
- object · Delivery Command · Executive email · new
- object · Delivery Command · Project · new
- object · Delivery Command · Task · new
- object · Delivery Command · RAID item · new
- object · Delivery Command · Person · new
- object · Delivery Command · Booking · new
- object · Delivery Command · Time entry · new
- object · Delivery Command · Change request · new
- object · Delivery Command · Activity · new
- object · Delivery Command · Document · new

## Contract

### object · Delivery Command · Executive email
One composed weekly executive email, sent or kept as a preview.
- object · create · Delivery Command · Executive email (`OBJ_dcmd_exec_email`): email_id text unique (EML-nnn), region picklist (as Project), send_at datetime epoch ms, recipient text, subject text, html long text, status picklist (sent "Sent", preview "Preview", failed "Failed"), error text

### object · Delivery Command · Project
One customer implementation, from signed contract to Hypercare.
- record · seed · Delivery Command · Project: the 19 rows of studio/data/seed/project.csv (story row IMP-2611 Sakura Mobility, Japan, Data migration, go-live 19 Nov 2026, baseline 12 Nov 2026, At risk, lead Mei Takahashi, 1,200 seats, JPY 84,000,000, 860 h planned, 545 h used, sponsor Hana Mori; IMP-2590 Pellworth Labs is Cancelled)

### object · Delivery Command · Task
One task in a project plan, with dates, dependencies and the critical path.
- record · seed · Delivery Command · Task: the 96 rows of studio/data/seed/task.csv (45 on IMP-2611; 17 in its Data migration column; critical path TSK-5024 to TSK-5044; TSK-5024 and TSK-5025 past their end date)

### object · Delivery Command · RAID item
One risk, assumption, issue or decision on a project.
- record · seed · Delivery Command · RAID item: the 17 rows of studio/data/seed/raid.csv (RSK-1183 likelihood 4, impact 5)

### object · Delivery Command · Person
One internal user or customer sponsor, with capacity and skill levels.
- record · seed · Delivery Command · Person: the 18 rows of studio/data/seed/person.csv (13 consultants and leads, Elena Brooks delivery director, Tomás Herrera finance partner, Grace Liu resource manager, sponsors Hana Mori and Owen Price)

### object · Delivery Command · Booking
Hours one person is booked on one project in one week.
- record · seed · Delivery Command · Booking: the 168 rows of studio/data/seed/booking.csv (12 weeks from 26 Oct 2026; Haruto Sato 44 h in week of 2 Nov; Aiko Tanaka 30 h in week of 16 Nov and 20 h in week of 23 Nov; Marcus Bell none)

### object · Delivery Command · Time entry
Hours one person logged on one task on one day, inside a weekly timesheet.
- record · seed · Delivery Command · Time entry: the 63 rows of studio/data/seed/time_entry.csv (week of 19 Oct Pending approval for 9 people; week of 12 Oct Approved)

### object · Delivery Command · Change request
One proposed change to a project, with its two-step approval route.
- record · seed · Delivery Command · Change request: the 2 rows of studio/data/seed/change_request.csv (CR-0452 approved by the director alone; CR-0449 rejected by the finance partner with a reason)

### object · Delivery Command · Activity
One change on a project: who did what and when; never edited.
- record · seed · Delivery Command · Activity: the 20 rows of studio/data/seed/activity.csv

### object · Delivery Command · Document
One file in a project library: statement of work, migration plan or sign-off record.
- record · seed · Delivery Command · Document: the 6 rows of studio/data/seed/document.csv, each with a short fictional body; file_url stays empty

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
- Delivery Command · Executive email exists with every field the contract lists
- Delivery Command · Project holds every seed row of its file
- Delivery Command · Task holds every seed row of its file
- Delivery Command · RAID item holds every seed row of its file
- Delivery Command · Person holds every seed row of its file
- Delivery Command · Booking holds every seed row of its file
- Delivery Command · Time entry holds every seed row of its file
- Delivery Command · Change request holds every seed row of its file
- Delivery Command · Activity holds every seed row of its file
- Delivery Command · Document holds every seed row of its file

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
