---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · plan 2 of 10"
touches: [{"kind":"object","name":"Delivery Command · Sign-off"},{"kind":"object","name":"Delivery Command · Checklist item"},{"kind":"object","name":"Delivery Command · Notification"},{"kind":"object","name":"Delivery Command · Integration"},{"kind":"object","name":"Delivery Command · Saved view"},{"kind":"object","name":"Delivery Command · Weekly snapshot"},{"kind":"object","name":"Delivery Command · Weekly metric"},{"kind":"object","name":"Delivery Command · AI output"},{"kind":"object","name":"Delivery Command · Role permission"},{"kind":"object","name":"Delivery Command · Upload"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-10-23T17:18:22.541Z"
acceptedBy: {"clientId":"cb1e0a4a-7af6-40cf-ac78-5470bd07a4fa"}
planIds: ["e_6adb96e00881d2257aa1945b"]
latestPlanId: "e_6adb96e00881d2257aa1945b"
planId: "e_6adb96e00881d2257aa1945b"
---
# ClickUp Delivery Command · plan 2 of 10

## Requested outcome
ClickUp's delivery director, implementation leads, resource manager and consultants run every customer implementation from one code app: portfolio health at a glance, a project workspace, resourcing and timesheets, change requests that route by an hours rule, a weekly executive summary and Delivery Copilot, a read-only AI assistant over the live data. Customer sponsors follow and sign off their own rollout in a portal in English, German and Japanese; consultants log time from a phone view. The story follows IMP-2611 Sakura Mobility, at risk of missing its 19 Nov 2026 go-live. This plan (part 2 of 10) builds the data layer: Sign-off, Checklist item, Notification, Integration, Saved view, Weekly snapshot, Weekly metric, AI output, Role permission, Upload.

## Touches
- object · Delivery Command · Sign-off · new
- object · Delivery Command · Checklist item · new
- object · Delivery Command · Notification · new
- object · Delivery Command · Integration · new
- object · Delivery Command · Saved view · new
- object · Delivery Command · Weekly snapshot · new
- object · Delivery Command · Weekly metric · new
- object · Delivery Command · AI output · new
- object · Delivery Command · Role permission · new
- object · Delivery Command · Upload · new

## Contract

### object · Delivery Command · Sign-off
One stage deliverable awaiting or carrying the customer sponsor's sign-off.
- object · create · Delivery Command · Sign-off (`OBJ_dcmd_signoff`): signoff_id text unique (SGN-nnn), project_id text, stage picklist (the seven stage codes), deliverable text, status picklist (awaiting "Awaiting sign-off", signed_off "Signed off", changes_requested "Changes requested"), requested_at date epoch ms, decided_by text, decided_at datetime epoch ms, comment long text

### object · Delivery Command · Checklist item
One of the ten readiness questions with the customer's answer.
- object · create · Delivery Command · Checklist item (`OBJ_dcmd_checklist_item`): item_id text unique (CHK-nn), project_id text, order number, question_en text, question_de text, question_ja text, answer text (empty means not set)

### object · Delivery Command · Notification
One assignment, sign-off or mention for a user.
- object · create · Delivery Command · Notification (`OBJ_dcmd_notification`): notification_id text unique (NTF-nn), recipient text, kind picklist (assignment "New assignment", signoff "Sign-off", mention "Mention"), text text, link text, read boolean, at datetime epoch ms

### object · Delivery Command · Integration
The sync status of one connected system.
- object · create · Delivery Command · Integration (`OBJ_dcmd_integration`): system text unique (Salesforce, Slack, Google Drive, Jira), status picklist (live "Live", sync_failed "Sync failed"), last_sync datetime epoch ms, error text, affected text

### object · Delivery Command · Saved view
One named, shareable set of portfolio filters.
- object · create · Delivery Command · Saved view (`OBJ_dcmd_saved_view`): view_id text unique (VW-nn), name text, owner text, filters long text (JSON), shared_with_team boolean

### object · Delivery Command · Weekly snapshot
Portfolio health counts for one week, for the trend.
- object · create · Delivery Command · Weekly snapshot (`OBJ_dcmd_weekly_snapshot`): week_start date epoch ms unique, on_track number, at_risk number, off_track number, active_projects number, on_track_share number

### object · Delivery Command · Weekly metric
The executive summary's six headline numbers and the contract value bridge for one week.
- object · create · Delivery Command · Weekly metric (`OBJ_dcmd_weekly_metric`): week_start date epoch ms unique, active_projects, active_projects_prev, golives_this_month, golives_this_month_prev, projects_at_risk, projects_at_risk_prev, avg_days_to_golive, avg_days_to_golive_prev, utilisation_pct, utilisation_pct_prev, value_awaiting_q4_usd, value_awaiting_q4_usd_prev_week, value_awaiting_q4_usd_last_month, bridge_new_usd, bridge_completed_usd, bridge_slipped_usd, bridge_cancelled_usd (all number)

### object · Delivery Command · AI output
One thing Delivery Copilot wrote: a risk flag, meeting summary, proposed task or status report.
- object · create · Delivery Command · AI output (`OBJ_dcmd_ai_output`): output_id text unique (AIO-nn), kind picklist (risk_flag "Risk flag", meeting_summary "Meeting summary", proposed_task "Proposed task", status_report "Status report"), project_id text, title text, body long text, confidence picklist (high "High", medium "Medium", low "Low"), evidence long text, transcript_ref text, status picklist (open, draft, proposed, accepted, rejected, published), ai_written boolean default true, created_at datetime epoch ms

### object · Delivery Command · Role permission
One role's row in the roles-against-permissions grid.
- object · create · Delivery Command · Role permission (`OBJ_dcmd_role_permission`): role text unique, view_portfolio, edit_project, move_tasks, book_consultants, approve_timesheets, raise_change, approve_change, view_internal_health, sign_off_deliverables, admin (all boolean)

### object · Delivery Command · Upload
One customer file upload with its row error summary.
- object · create · Delivery Command · Upload (`OBJ_dcmd_upload`): upload_id text unique (UPL-nnn), project_id text, file_name text, rows_total number, rows_error number, error_summary long text (JSON: error type, count, first five row numbers), status picklist (validated "Validated", confirmed "Confirmed"), uploaded_by text, at datetime epoch ms

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
- Delivery Command · Sign-off exists with every field the contract lists
- Delivery Command · Checklist item exists with every field the contract lists
- Delivery Command · Notification exists with every field the contract lists
- Delivery Command · Integration exists with every field the contract lists
- Delivery Command · Saved view exists with every field the contract lists
- Delivery Command · Weekly snapshot exists with every field the contract lists
- Delivery Command · Weekly metric exists with every field the contract lists
- Delivery Command · AI output exists with every field the contract lists
- Delivery Command · Role permission exists with every field the contract lists
- Delivery Command · Upload exists with every field the contract lists

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
