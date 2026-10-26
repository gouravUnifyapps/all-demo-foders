---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 6 of 9: booking, timesheet and portal automations"
touches: [{"kind":"automation","name":"ClickUp Command · Book consultant"},{"kind":"automation","name":"ClickUp Command · Timesheet action"},{"kind":"automation","name":"ClickUp Command · Portal action"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Book consultant"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Timesheet action"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Portal action"}]
acceptedAt: "2026-10-26T12:40:45.130Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf4a4f08f96579542f8822"]
latestPlanId: "e_6adf4a4f08f96579542f8822"
planId: "e_6adf4a4f08f96579542f8822"
---
# ClickUp Delivery Command · build 6 of 9: booking, timesheet and portal automations

## Requested outcome
Build 6 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds booking, timesheet and portal automations. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- automation · ClickUp Command · Book consultant · new
- automation · ClickUp Command · Timesheet action · new
- automation · ClickUp Command · Portal action · new

## Contract

### automation · ClickUp Command · Book consultant
Books a person onto a project and refuses to save over capacity without confirmation.

- automation · create · ClickUp Command · Book consultant: callable; inputs person_code, project_code (text), first_week (number, epoch ms), weeks, hours_per_week (number), confirm (boolean); outputs result (text: saved | over_capacity), overages_json (text: each week with booked hours, percent of capacity and hours over), booking_code (text); a booking that takes the person above 100% of capacity_hours in any week answers over_capacity with the weeks and writes nothing unless confirm is true, when it saves with over_capacity true; a save writes Booking and one Activity row.

### automation · ClickUp Command · Timesheet action
Logs time, submits, approves or returns weekly timesheets.

- automation · create · ClickUp Command · Timesheet action: callable; inputs action (text: log | submit | approve | return), person_code, task_code (text), work_date (number), hours (number), week_start (number), entry_codes (text, comma-separated, for approve and return in a batch), reason (text); outputs result (text: saved | refused_reason_required), timesheet_status (text); a return with an empty reason is refused.

### automation · ClickUp Command · Portal action
The sponsor sign-off, change request, session booking, checklist answer and upload confirm.

- automation · create · ClickUp Command · Portal action: callable; inputs action (text: sign_off | request_changes | book_slot | answer_checklist | confirm_upload), sponsor_code, deliverable_code, slot_code, item_code, answer, doc_code, comment (text); outputs result (text: saved | refused_comment_required | refused_slot_taken | refused_not_your_project), decided_by (text), decided_at (number, epoch ms); a sponsor acts only on their own project_code; request_changes needs a comment; a taken slot is refused; sign_off records who and when and writes Activity.

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
- deploy ClickUp Command · Book consultant
- deploy ClickUp Command · Timesheet action
- deploy ClickUp Command · Portal action

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
