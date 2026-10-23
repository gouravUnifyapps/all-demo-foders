# ClickUp Delivery Command v2: internal notes (team only)

Source: studio/state/clickup-delivery-command-v2.internal.md was not in this checkout, so this copy is
POC Studio's psl_document row "Internal notes · v1" (POC-clickup-delivery-command-v2-20261022__6_finalize__internal-notes-v1__v1),
read-only on 2026-10-23, plus the state file's verify, dev_issues and open_questions. Nothing here goes in a client file.

## Known bugs and workarounds

- Project overview (beat 2): the task detail panel covers the Activity and Settings tabs and takes their clicks; its Log time Who and Hours fields are 40 px and 8 px wide. Workaround: close the panel before opening Activity or Settings; do not demo Log time from the panel.
- Project overview (beat 2): T-2611-09 "Validate pilot batch" is Done since round 1, so Mark done is disabled and the beat cannot be played as written. Workaround: reset the task to In progress in Migration before the demo, or move another in-progress Migration card (net-zero move proven live).
- Resourcing (beat 3): Lena Vogt reads 100%, 80% in the weeks of 2 and 9 Nov because of test bookings, so the "80%, 60%" line cannot show. Workaround: delete the test bookings first (needs the person's yes), or say the numbers on screen.
- Resourcing: the 12-week grid runs under the Copilot panel (columns from about Dec 21 sit behind it). Workaround: collapse the Copilot panel on Resourcing.
- Change request (beat 4): approving as the director adds no row to the activity feed, and "Viewing as Ines Moreau" still offers Approve and Reject after she approved. Workaround: switch Viewing as to Raj Patel right after the director approves; do not point at the feed.
- Change request CR-0456: the approval path shows "Approved by Raj Patel" under the finance step while the tag reads "Pending approval: finance partner". Workaround: show the live request, not CR-0456.
- Weekly summary (beat 6): the bridge x labels Completed, Slipped and Cancelled run together; the five-projects # column is 40 px. Workaround: read the bridge aloud from the tile values.
- Status report (beat 7): "Use Copilot draft" leaves the editor empty and toasts "Delivery Copilot has no answer in this conversation to use yet." with the draft on screen. Workaround: copy the draft from the panel into the editor by hand; Publish and Export are unverified.
- Copilot status draft (beat 7): the time entries are dated 23 Oct ("tomorrow") and carry only consultant id CNS-01, and 18 h sit on a Done task, so the draft ends with "please check" notes naming them.
- Copilot (beat 7, H2): the Generate PDF and DOCX tool is attached and on but never offered to the model (platform, dev_issues), so "export as PDF" from the Copilot is not available.
- Copilot panel: the agent avatar is a bare letter "C".
- Project overview: Settings tab shows two primary buttons (Save and Draft status report); light-theme sticky header is translucent when scrolled.
- Every screen: console errors from the platform runtime (aborted fetches, mqtt WebSocket 426, "Dynamic property not found" while the Copilot answers). Keep DevTools closed.
- Notifications bell reads 6 unread (seed was 5): a test leftover notification.
- Not built: My projects toggle (A86), no-access project page (A94), session-expiry dialog (A95). Do not offer them.
- Customer portal (seen 2026-10-23 by collaterals): Shared documents lists "Migration plan v2" as shared 30 Sept 2026, while deliverable D-2611-2 was shared on 21 Oct 2026.

## One-shot beats and resets

- Beat 2: Move task changes a task's stage and writes an Activity row. Move the card back and reset T-2611-09 to In progress before each run-through.
- Beat 3: a successful Lena Vogt booking writes Booking rows and pushes her percentages up. Delete the new bookings after each run-through (needs the person's yes).
- Beat 4: Submit change request takes the next CR number and writes an Activity row; the two approvals move Halden Freight's go-live to 4 Dec and its budget hours up by 48. After each run-through delete the new CR and its Activity rows and reset IMP-2611 go_live_date to 2026-11-27 and budget_hours_planned to 640.
- Beat 5: Sign off deliverable sets Migration plan v2 to Signed off and writes Activity and notification rows. Reset D-2611-2 to Awaiting sign-off and delete the rows.
- Beat 7: Publish status report writes an AI output row and an Activity row. Delete them after each run-through.
- Every Copilot question opens a chat under the asking user. Start beat 7 from a fresh chat.

## Test accounts and test records

- Gourav (the person's own tenant user) signs in to the preview. No customer sponsor login exists; the portal is a route viewed as Katrin Albers.
- Personas in the beats are seeded names, not accounts: Ines Moreau, Raj Patel, Mira Castell, Katrin Albers.
- Change requests CR-0457, CR-0458, CR-0459, CR-0460 (DEMO-TEST) on OBJ_cudc_change_request: clean up before the demo; the live request will be numbered CR-0461 until then.
- Bookings BKG-021 to BKG-024 (Lena Vogt, CNS-02, IMP-2611, 8 h each in the weeks of 2 and 9 Nov) on OBJ_cudc_booking: clean up.
- Activity ACT-21 to ACT-30, ACT-34, ACT-35 and CR-0460's activity row: clean up.
- AI output SR-2626-1: clean up. Jira issue KAN-27 (DEMO-TEST): clean up.
- Pending delete confirmations from 3-build: d_d101f6, d_f7eac3, d_89dc27.

## Do not show

- Escalate to Jira on a RAID risk: it creates a real issue in KAN, a Jira project owned by another team.
- The Copilot's "Export as PDF or Word": not offered to the model.
- "Use Copilot draft" on the status report: leaves the editor empty.
- CR-0456's approval path, and the activity feed after the director's approval.
- The CR-0457 to CR-0460 test requests and the DEMO-TEST reason text.
- Admin on the rail: it opens Portfolio; the Admin screen is not built.
- The published host: it asks for a tenant user; use the preview.

## Collaterals round 1 (2026-10-23)

- The video was not made: no recordable signed-in session (Nebula's signed-in browser refuses state-save by design) and the beats' writes would change the tenant. Open question to the owner.
- The eval.csv was not in this checkout; facts come from beats, entities and the live seed rows.
