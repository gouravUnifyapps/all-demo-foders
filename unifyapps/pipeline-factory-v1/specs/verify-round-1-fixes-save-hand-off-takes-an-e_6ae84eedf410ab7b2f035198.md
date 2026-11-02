---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fixes: Save hand-off takes an origin input and its callers pass theirs; Log signal sets due_at; Clear Gat"
touches: [{"kind":"automation","name":"Pipeline Factory · Save hand-off","id":"6ae840a5fbdd550a9a44c524"},{"kind":"automation","name":"Pipeline Factory · Log signal","id":"6ae843cc9594aa458cba14d7"},{"kind":"automation","name":"Pipeline Factory · Decide Gate 1","id":"6ae8440df13e536c52c5d959"},{"kind":"automation","name":"Pipeline Factory · Book meeting","id":"6ae84449f38e327618fcc640"},{"kind":"automation","name":"Pipeline Factory · Clear Gate 2","id":"6ae840d7f6f76639f8ceb67d"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save hand-off","id":"6ae840a5fbdd550a9a44c524"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Log signal","id":"6ae843cc9594aa458cba14d7"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Decide Gate 1","id":"6ae8440df13e536c52c5d959"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Book meeting","id":"6ae84449f38e327618fcc640"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Clear Gate 2","id":"6ae840d7f6f76639f8ceb67d"}]
acceptedAt: "2026-11-02T08:50:52.933Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae84ef0f410ab7b2f0351d1"]
latestPlanId: "e_6ae84ef0f410ab7b2f0351d1"
planId: "e_6ae84ef0f410ab7b2f0351d1"
---
# Verify round 1 fixes: Save hand-off takes an origin input and its callers pass theirs; Log signal sets due_at; Clear Gat

## Requested outcome
Verify round 1 fixes: Save hand-off takes an origin input and its callers pass theirs; Log signal sets due_at; Clear Gate 2 reports the pod rule for D-04

## Touches
- automation · Pipeline Factory · Save hand-off · 6ae840a5fbdd550a9a44c524
- automation · Pipeline Factory · Log signal · 6ae843cc9594aa458cba14d7
- automation · Pipeline Factory · Decide Gate 1 · 6ae8440df13e536c52c5d959
- automation · Pipeline Factory · Book meeting · 6ae84449f38e327618fcc640
- automation · Pipeline Factory · Clear Gate 2 · 6ae840d7f6f76639f8ceb67d

## Ready when
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Save hand-off with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Save hand-off deployed at the fixed version.
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Log signal with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Log signal deployed at the fixed version.
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Decide Gate 1 with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Decide Gate 1 deployed at the fixed version.
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Book meeting with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Book meeting deployed at the fixed version.
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Clear Gate 2 with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Clear Gate 2 deployed at the fixed version.
- deploy Pipeline Factory · Save hand-off
- deploy Pipeline Factory · Log signal
- deploy Pipeline Factory · Decide Gate 1
- deploy Pipeline Factory · Book meeting
- deploy Pipeline Factory · Clear Gate 2
