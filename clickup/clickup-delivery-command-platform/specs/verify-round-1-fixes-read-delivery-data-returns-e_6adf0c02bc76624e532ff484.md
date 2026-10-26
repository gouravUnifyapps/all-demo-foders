---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fixes: Read delivery data returns each date also as UTC day text; Delivery Command · Copilot states dates"
touches: [{"kind":"automation","name":"Delivery Command · Read delivery data","id":"6adbaa4fca4f9d20459bd303"},{"kind":"ai-agent","name":"Delivery Command · Copilot","id":"e_6adbabd2925d282255cee62b"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Delivery Command · Read delivery data","id":"6adbaa4fca4f9d20459bd303"},{"action":"publish","kind":"ai-agent","name":"Delivery Command · Copilot","id":"e_6adbabd2925d282255cee62b"}]
acceptedAt: "2026-10-26T08:14:57.765Z"
acceptedBy: {"clientId":"95fa9a26-0dcf-442c-b37d-8d723221a36e"}
planIds: ["e_6adf0c04bc76624e532ff4a9"]
latestPlanId: "e_6adf0c04bc76624e532ff4a9"
planId: "e_6adf0c04bc76624e532ff4a9"
---
# Verify round 1 fixes: Read delivery data returns each date also as UTC day text; Delivery Command · Copilot states dates

## Requested outcome
Verify round 1 fixes: Read delivery data returns each date also as UTC day text; Delivery Command · Copilot states dates from that text, answers within 90 seconds, and is published.

## Touches
- automation · Delivery Command · Read delivery data · 6adbaa4fca4f9d20459bd303
- ai-agent · Delivery Command · Copilot · e_6adbabd2925d282255cee62b

## Ready when
- Read-back: A test run's IMP-2611 row shows go_live_text "19 Nov 2026" and baseline_go_live_text "12 Nov 2026".
- Read-back: The deployed run returns go_live_text "19 Nov 2026" for IMP-2611.
- Read-back: The test answer states 19 Nov 2026 and 12 Nov 2026 for IMP-2611.
- Read-back: Both test questions answer in under 90 s, with their durations quoted from the traces.
- Read-back: get_agent answers needsPublish false with the published version.
- deploy Delivery Command · Read delivery data
- publish Delivery Command · Copilot
