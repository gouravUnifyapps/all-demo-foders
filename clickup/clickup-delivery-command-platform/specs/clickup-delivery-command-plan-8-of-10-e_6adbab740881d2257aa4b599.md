---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 8 of 10"
touches: [{"kind":"automation","name":"Delivery Command · Send executive summary"},{"kind":"automation","name":"Delivery Command · Weekly executive email schedule"},{"kind":"ai-agent","name":"Delivery Command · Copilot"},{"kind":"automation","name":"Delivery Command · Ask Copilot"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Send executive summary"},{"action":"deploy","kind":"automation","name":"Delivery Command · Weekly executive email schedule"},{"action":"publish","kind":"ai-agent","name":"Delivery Command · Copilot"},{"action":"deploy","kind":"automation","name":"Delivery Command · Ask Copilot"}]
acceptedAt: "2026-10-23T18:46:12.051Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adbab775236864dd8e7a211"]
latestPlanId: "e_6adbab775236864dd8e7a211"
planId: "e_6adbab775236864dd8e7a211"
---
# ClickUp Delivery Command · plan 8 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 8 of 10) builds the weekly executive email, Delivery Copilot and the automation the app asks it through.

## Touches
- automation · Delivery Command · Send executive summary · new
- automation · Delivery Command · Weekly executive email schedule · new
- ai-agent · Delivery Command · Copilot · new
- automation · Delivery Command · Ask Copilot · new

## Contract

### automation · Delivery Command · Send executive summary
Composes and sends the weekly executive email for a region.
- automation · create · Delivery Command · Send executive summary: callable; input region text, recipient text; composes the six headline numbers, the bridge and the five biggest movers from Weekly metric, Weekly snapshot, Project and Activity into an HTML email with the ClickUp logo, saves an Executive email row, and sends it on the mail connection named under Assumptions when there is one (status sent), else status preview; result email_id text, status text

### automation · Delivery Command · Weekly executive email schedule
Runs every Monday 08:00 in each region's time zone.
- automation · create · Delivery Command · Weekly executive email schedule: scheduled every hour on Sundays 22:00 UTC to Mondays 14:00 UTC; for each region whose local time (Asia/Tokyo, Europe/Berlin, America/New_York) is Monday 08:00 it calls Send executive summary for that region

### ai-agent · Delivery Command · Copilot
Delivery Copilot: a read-only assistant over the delivery data.
- ai-agent · create · Delivery Command · Copilot: instructions: answer delivery questions for ClickUp's implementation team from Read delivery data only, in plain, calm, direct English; name every project by id and customer and link it; when a chart helps, return a chart JSON {type: bar or line, unit, series} with units; draft weekly status reports from a project's tasks, risks and time entries, marked as an AI draft for the lead to edit; decline billing, invoicing, revenue, payroll, hiring and anything outside delivery data, and say plainly when a field the data does not hold is asked for, with what to try instead; never create or change anything; model: Nebula's recommendation; tool: Read delivery data

### automation · Delivery Command · Ask Copilot
Passes a question from the app to Delivery Copilot and returns its answer.
- automation · create · Delivery Command · Ask Copilot: callable; input question text, persona text, screen text, project_id text; invokes the Delivery Command · Copilot agent with the question and its context (Invoke Agent, ai_agents_by_unifyapps); result answer text, chart text (JSON {type, unit, series} or empty), links list of {label, route}, refused boolean

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
- deploy Delivery Command · Send executive summary
- deploy Delivery Command · Weekly executive email schedule
- publish Delivery Command · Copilot
- deploy Delivery Command · Ask Copilot
- Delivery Copilot answers "Which Japan projects go live in November and are at risk?" with IMP-2611 and IMP-2633.

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
