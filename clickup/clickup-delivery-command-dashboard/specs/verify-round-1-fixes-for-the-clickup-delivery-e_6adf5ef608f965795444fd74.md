---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fixes for the ClickUp Delivery Command demo: the Copilot names the week it reads (26 Oct 2026) and compar"
touches: [{"kind":"ai-agent","name":"ClickUp Command Copilot","id":"e_6adf4f02dc07493166ced9fa"},{"kind":"code-app","name":"ClickUp Delivery Command","id":"app-a2a9509a82c1"}]
askBeforeDeploy: true
releaseYes: [{"action":"publish","kind":"ai-agent","name":"ClickUp Command Copilot","id":"e_6adf4f02dc07493166ced9fa"},{"action":"publish","kind":"code-app","name":"ClickUp Delivery Command","id":"app-a2a9509a82c1"}]
acceptedAt: "2026-10-26T14:08:53.982Z"
acceptedBy: {"clientId":"ef8e5eac-b1c9-485b-ae8e-f8151f796819"}
planIds: ["e_6adf5ef808f965795444ffac"]
latestPlanId: "e_6adf5ef808f965795444ffac"
planId: "e_6adf5ef808f965795444ffac"
---
# Verify round 1 fixes for the ClickUp Delivery Command demo: the Copilot names the week it reads (26 Oct 2026) and compar

## Requested outcome
Verify round 1 fixes for the ClickUp Delivery Command demo: the Copilot names the week it reads (26 Oct 2026) and compares health with last week, shows codes as words, and is published; the app's empty states name their items; publish both.

## Touches
- ai-agent · ClickUp Command Copilot · e_6adf4f02dc07493166ced9fa
- code-app · ClickUp Delivery Command · app-a2a9509a82c1

## Ready when
- Read-back: The test answer names the week of 26 Oct 2026 with 161 / 38 / 15 against 159 / 33 / 19, and the over-capacity answer shows no raw code.
- Read-back: `get_agent` shows ClickUp Command Copilot published with needsPublish false.
- Read-back: The push's commit is `get_code_app`'s head.sha and the committed source holds no literal "No items yet.".
- Read-back: `publish_code_app` answers deployed true with t3's commit.
- publish ClickUp Command Copilot
- publish ClickUp Delivery Command
