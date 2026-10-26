---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 7 of 9: Copilot outputs, status report and weekly email automations"
touches: [{"kind":"automation","name":"ClickUp Command · Accept proposed tasks"},{"kind":"automation","name":"ClickUp Command · Publish status report"},{"kind":"automation","name":"ClickUp Command · Send executive summary"},{"kind":"connection","name":"Gmail","id":"6980e13788c7735877a8311c"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Accept proposed tasks"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Publish status report"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Send executive summary"}]
acceptedAt: "2026-10-26T12:51:04.718Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf4cbbdc07493166ce9964"]
latestPlanId: "e_6adf4cbbdc07493166ce9964"
planId: "e_6adf4cbbdc07493166ce9964"
---
# ClickUp Delivery Command · build 7 of 9: Copilot outputs, status report and weekly email automations

## Requested outcome
Build 7 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds Copilot outputs, status report and weekly email automations. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- automation · ClickUp Command · Accept proposed tasks · new
- automation · ClickUp Command · Publish status report · new
- automation · ClickUp Command · Send executive summary · new
- connection · Gmail · 6980e13788c7735877a8311c

## Contract

### automation · ClickUp Command · Accept proposed tasks
Turns accepted Copilot proposals into tasks.

- automation · create · ClickUp Command · Accept proposed tasks: callable; inputs output_codes (text, comma-separated), decision (text: accept | reject), decided_by (text); outputs created_task_codes (text), result (text); accept creates one Task per output with source copilot and sets the output's decision; reject creates nothing.

### automation · ClickUp Command · Publish status report
Publishes the lead-edited, AI-written weekly status report.

- automation · create · ClickUp Command · Publish status report: callable; inputs project_code, body, edited_by (text); outputs doc_code (text), published_at (number), result (text); writes Document kind status_report with ai_written true and edited_by, and one Activity row.

### automation · ClickUp Command · Send executive summary
Sends the weekly summary email through Gmail, labelled DEMO-TEST.

- automation · create · ClickUp Command · Send executive summary: callable; inputs to_email (text), week_start (number); outputs result (text: sent | failed), message_id (text); reads Weekly metric for the week, composes the six headline numbers, the value bridge and the five top movers as HTML with the ClickUp logo, and sends one email through the Gmail connection `6980e13788c7735877a8311c` with operation `gmail_send_email`, subject starting "DEMO-TEST · ClickUp Delivery Command · weekly summary".

### connection · Gmail
Existing Gmail connection the weekly summary email is sent through; probed read-only at plan time.


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
- deploy ClickUp Command · Accept proposed tasks
- deploy ClickUp Command · Publish status report
- deploy ClickUp Command · Send executive summary

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
