---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 5 of 9: task, change request and approval automations"
touches: [{"kind":"automation","name":"ClickUp Command · Update task"},{"kind":"automation","name":"ClickUp Command · Raise change request"},{"kind":"automation","name":"ClickUp Command · Decide change request"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Update task"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Raise change request"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Decide change request"}]
acceptedAt: "2026-10-26T12:30:11.401Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf47d508f96579542f5180"]
latestPlanId: "e_6adf47d508f96579542f5180"
planId: "e_6adf47d508f96579542f5180"
---
# ClickUp Delivery Command · build 5 of 9: task, change request and approval automations

## Requested outcome
Build 5 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds task, change request and approval automations. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- automation · ClickUp Command · Update task · new
- automation · ClickUp Command · Raise change request · new
- automation · ClickUp Command · Decide change request · new

## Contract

### automation · ClickUp Command · Update task
Moves a task between stage columns, reschedules it with dependents, or sets its status.

- automation · create · ClickUp Command · Update task: callable; inputs task_code (text), action (text: move | reschedule | status), to_stage (text), new_start (number, epoch ms), new_end (number, epoch ms), status (text), preview (boolean); outputs result (text: saved | preview | refused), column_count (number), column_limit (number), over_limit (boolean), moved_json (text: each dependent task with its new dates), new_go_live (number, epoch ms); a reschedule moves every finish-to-start dependent by the same working days and returns the project's new go-live date; preview true writes nothing; a save writes Task and one Activity row.

### automation · ClickUp Command · Raise change request
Previews and submits a change request with its before and after plan and its route.

- automation · create · ClickUp Command · Raise change request: callable; inputs project_code, reason, work_added, work_removed (text), hours_delta, cost_delta, go_live_delta_days (number), raised_by (text), preview (boolean); outputs cr_code (text), before_json, after_json, route_json (text), result (text: preview | submitted | refused_reason_required); route: an absolute hours_delta under 40 goes to the Delivery director only; 40 or more goes to the Delivery director, then the Finance partner, in that order; the next cr_code continues from the highest stored one (CR-0457 first); submit writes Change request with status pending_approval and one Activity row.

### automation · ClickUp Command · Decide change request
Records one approver decision and applies the 40-hour route and the reason rule.

- automation · create · ClickUp Command · Decide change request: callable; inputs cr_code, approver_role (text: delivery_director | finance_partner), approver_name, decision (text: approve | reject), reason (text); outputs result (text: step_approved | approved | rejected | refused_reason_required | refused_not_your_turn), next_approver (text), new_go_live (number, epoch ms); a reject with an empty reason writes nothing and answers refused_reason_required; an approver who is not next answers refused_not_your_turn; the last approval sets status approved, moves the Project go_live_date by go_live_delta_days, adds hours_delta to budget_hours_planned, and writes one Activity row; every decision appends to route_json.

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
- deploy ClickUp Command · Update task
- deploy ClickUp Command · Raise change request
- deploy ClickUp Command · Decide change request

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
