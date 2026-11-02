---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fix: Reset demo also deletes every PF Hand-off that has no seed snapshot"
touches: [{"kind":"automation","name":"Pipeline Factory · Reset demo","id":"6ae8441df38e327618fcc13c"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Reset demo","id":"6ae8441df38e327618fcc13c"}]
acceptedAt: "2026-11-02T09:11:58.734Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae853edd96c5f6ba232095f"]
latestPlanId: "e_6ae853edd96c5f6ba232095f"
planId: "e_6ae853edd96c5f6ba232095f"
---
# Verify round 1 fix: Reset demo also deletes every PF Hand-off that has no seed snapshot

## Requested outcome
Verify round 1 fix: Reset demo also deletes every PF Hand-off that has no seed snapshot

## Touches
- automation · Pipeline Factory · Reset demo · 6ae8441df38e327618fcc13c

## Ready when
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Reset demo with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Reset demo deployed at the fixed version.
- deploy Pipeline Factory · Reset demo
