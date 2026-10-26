---
nebula: 3
mode: "sonic"
format: "spec"
title: "ClickUp Delivery Command · build 4 of 9: last seeds, the Copilot's read tool and Save view"
touches: [{"kind":"object","name":"ClickUp Command · Saved view","id":"OBJ_cucmd_saved_view"},{"kind":"object","name":"ClickUp Command · Checklist item","id":"OBJ_cucmd_checklist_item"},{"kind":"object","name":"ClickUp Command · Integration","id":"OBJ_cucmd_integration"},{"kind":"object","name":"ClickUp Command · Notification","id":"OBJ_cucmd_notification"},{"kind":"automation","name":"ClickUp Command · Read delivery data"},{"kind":"automation","name":"ClickUp Command · Save view"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"ClickUp Command · Read delivery data"},{"action":"deploy","kind":"automation","name":"ClickUp Command · Save view"}]
acceptedAt: "2026-10-26T12:21:28.408Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf45cbdc07493166ce0071"]
latestPlanId: "e_6adf45cbdc07493166ce0071"
planId: "e_6adf45cbdc07493166ce0071"
---
# ClickUp Delivery Command · build 4 of 9: last seeds, the Copilot's read tool and Save view

## Requested outcome
Build 4 of 9 of the ClickUp Delivery Command demo for Clickup (POC POC-clickup-delivery-command-dashboard-20261026, plan approved at G2 by Gourav Mahunta). This part builds last seeds, the Copilot's read tool and Save view. Implementation leads, delivery directors, finance partners, resource managers, consultants and customer sponsors work in one code app over these objects; the demo walks Sakura Mobility (IMP-2611) from At risk through a routed change request, staffing, the sponsor's sign-off and Delivery Copilot.

## Touches
- object · ClickUp Command · Saved view · OBJ_cucmd_saved_view
- object · ClickUp Command · Checklist item · OBJ_cucmd_checklist_item
- object · ClickUp Command · Integration · OBJ_cucmd_integration
- object · ClickUp Command · Notification · OBJ_cucmd_notification
- automation · ClickUp Command · Read delivery data · new
- automation · ClickUp Command · Save view · new

## Contract

### object · ClickUp Command · Saved view
One named, shareable set of portfolio filters.

- record · seed · ClickUp Command · Saved view: V-01 "My Japan projects" (region japan) owner Kenji Arai; V-02 "Europe go-lives this quarter" owner Elena Fischer, shared with "Europe delivery".

### object · ClickUp Command · Checklist item
One of the ten readiness questions with the customer answer, or none.

- record · seed · ClickUp Command · Checklist item: C-2611-01 to C-2611-10, questions in en, de and ja (SSO provider, admin users, departments, data residency, time zone, working week, support contacts, go-live freeze window, training rooms, success metrics); items 01 to 07 answered by Haruto Mori, 08, 09 and 10 with no answer.

### object · ClickUp Command · Integration
The sync status of one connected system.

- record · seed · ClickUp Command · Integration: salesforce synced 2026-10-26 07:55; slack synced 2026-10-26 07:58; google_drive synced 2026-10-26 07:40; jira sync_failed, failing since 2026-10-25 22:10, error "Authentication expired for the Jira project ESC", affects "Engineering escalations on 3 projects are not updating".

### object · ClickUp Command · Notification
One assignment, sign-off or mention for a user.

- record · seed · ClickUp Command · Notification: N-01 to N-08 for P-07 Yui Sato: 3 assignment, 2 signoff, 3 mention, N-01 to N-03 unread.

### automation · ClickUp Command · Read delivery data
The Copilot read-only tool over the delivery objects.

- automation · create · ClickUp Command · Read delivery data: callable, read-only, the Copilot's one tool; inputs scope (text: projects | tasks | risks | bookings | people | change_requests | ai_outputs | weekly_metrics | documents), filters_json (text: field equals value pairs, and date ranges as from and to epoch ms); outputs rows_json (text), row_count (number), as_of (number, epoch ms); writes nothing.

### automation · ClickUp Command · Save view
Saves a named portfolio filter set and shares it.

- automation · create · ClickUp Command · Save view: callable; inputs name (text), filters_json (text), owner (text), shared_with (text); outputs view_code (text), result (text: saved | refused_name_taken); writes Saved view.

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
- `get_records` on `OBJ_cucmd_saved_view` holds every row the Saved view seed line names.
- `get_records` on `OBJ_cucmd_checklist_item` holds every row the Checklist item seed line names.
- `get_records` on `OBJ_cucmd_integration` holds every row the Integration seed line names.
- `get_records` on `OBJ_cucmd_notification` holds every row the Notification seed line names.
- deploy ClickUp Command · Read delivery data
- deploy ClickUp Command · Save view

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
