---
nebula: 3
specId: "e_6adf0c02bc76624e532ff484"
mode: "sonic"
title: "Verify round 1 fixes: Read delivery data returns each date also as UTC day text; Delivery Command · Copilot states dates"
owner: {"clientId":"95fa9a26-0dcf-442c-b37d-8d723221a36e","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Read delivery data","id":"6adbaa4fca4f9d20459bd303"},{"action":"publish","kind":"ai-agent","name":"Delivery Command · Copilot","id":"e_6adbabd2925d282255cee62b"}]
touches: [{"kind":"automation","name":"Delivery Command · Read delivery data","id":"6adbaa4fca4f9d20459bd303"},{"kind":"ai-agent","name":"Delivery Command · Copilot","id":"e_6adbabd2925d282255cee62b"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "530c0d44-5674-4587-adb1-84772c51a8b8"
pageDesign: 2
createdAt: "2026-10-26T08:15:00.191Z"
runningAt: "2026-10-26T08:15:02.897Z"
runner: {"clientId":"95fa9a26-0dcf-442c-b37d-8d723221a36e","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"de444057-11c4-5d06-b16b-82637919ad51"}
---
## Plan

Goal: Verify round 1 fixes: Read delivery data returns each date also as UTC day text; Delivery Command · Copilot states dates

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | automation | Delivery Command · Read delivery data |  | running | 1 |
| t2 | deploy | Delivery Command · Read delivery data | t1 | pending | 0 |
| t3 | ai-agent | Delivery Command · Copilot | t2 | pending | 0 |
| t4 | ai-agent | Delivery Command · Copilot | t3 | pending | 0 |
| t5 | publish | Delivery Command · Copilot | t4 | pending | 0 |

### t1 · Read delivery data returns UTC day text beside every date

Body:
Read: open_workflow for Delivery Command · Read delivery data (6adbaa4fca4f9d20459bd303) and describe_callable_workflow for its contract (input entity, filters, limit; result rows, count).
Change: for every row it returns, each date field it holds (go_live, baseline_go_live, start, end, due, week_start, date, decided_at, requested_at) also comes back as a text field named &lt;field&gt;_text holding the UTC calendar day, such as "19 Nov 2026" for 1795046400000, beside the unchanged epoch value.
Keep everything else as it is: the inputs, the filters, the limit, rows and count, and it stays read only and never writes.
Save with compile_and_save_workflow and test-run it with entity projects and filters {"id":"IMP-2611"} without deploying.
Read back: the test run's row for IMP-2611 shows go_live_text "19 Nov 2026" and baseline_go_live_text "12 Nov 2026", quoted.

Proof: A test run's IMP-2611 row shows go_live_text "19 Nov 2026" and baseline_go_live_text "12 Nov 2026".

### t2 · Deploy Delivery Command · Read delivery data

Body:
Read: search_workflows or open_workflow for Delivery Command · Read delivery data (6adbaa4fca4f9d20459bd303) and its saved draft from t1.
Deploy it with deploy_workflow.
It is callable only: it runs when the Copilot agent calls it, never by itself.
Then trigger_workflow_run once with entity projects and filters {"id":"IMP-2611"} and inspect_workflow_run.
Read back: the deployed version and the run's go_live_text "19 Nov 2026", quoted.

Proof: The deployed run returns go_live_text "19 Nov 2026" for IMP-2611.

### t3 · Copilot states dates from the day text

Body:
Read: get_agent for Delivery Command · Copilot (e_6adbabd2925d282255cee62b): its instructions, model and its one tool Read delivery data.
Change the instructions only: state every date from the &lt;field&gt;_text day text Read delivery data returns, and never convert epoch milliseconds by hand (it now says IMP-2611 goes live 18 Nov 2026 with baseline 11 or 16 Nov; the data says 19 Nov and 12 Nov).
Keep the model, the tool, the read-only rules and every other instruction as they are.
Test with send_test_messages: "When does IMP-2611 go live, and what was its baseline?" and read_trace for it.
Read back: the answer states 19 Nov 2026 and 12 Nov 2026, quoted, and the trace shows a Read delivery data call.

Proof: The test answer states 19 Nov 2026 and 12 Nov 2026 for IMP-2611.

### t4 · Copilot answers within 90 seconds

Body:
Read: get_agent for Delivery Command · Copilot (e_6adbabd2925d282255cee62b) after t3, and read_trace of a slow question.
Change the instructions only: plan in one short think step, then read each entity it needs once with limit 200 (bookings and people once each, never per-person rereads), then answer.
Today "Who is booked over 100% in the next 12 weeks?" takes 118 s and "Draft the weekly status report for IMP-2611" 106 s; the target is under 90 s at p95.
Keep the model, the tool, the date rule from t3 and every other instruction as they are.
Read back: send_test_messages with both questions; each trace's duration under 90 s and the answers still naming Haruto Sato (over 100% in the week of 2 Nov) and a status draft for IMP-2611, quoted.

Proof: Both test questions answer in under 90 s, with their durations quoted from the traces.

### t5 · Publish Delivery Command · Copilot

Body:
Read: get_agent for Delivery Command · Copilot (e_6adbabd2925d282255cee62b); it shows needsPublish true.
Publish it with publish_agent so the app's Ask Copilot automation runs the verified instructions.
Change nothing else: the visibility to All Users and testing stays.
Then get_agent again.
Read back: needsPublish false and the published version number, quoted.

Proof: get_agent answers needsPublish false with the published version.

