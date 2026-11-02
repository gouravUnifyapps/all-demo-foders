---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fix: the fast-lane hand-off carries due_at, written by Save hand-off (new optional due_at input) and pass"
touches: [{"kind":"automation","name":"Pipeline Factory · Save hand-off","id":"6ae840a5fbdd550a9a44c524"},{"kind":"automation","name":"Pipeline Factory · Log signal","id":"6ae843cc9594aa458cba14d7"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save hand-off","id":"6ae840a5fbdd550a9a44c524"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Log signal","id":"6ae843cc9594aa458cba14d7"}]
acceptedAt: "2026-11-02T09:03:01.605Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae851cbf410ab7b2f03bef9"]
latestPlanId: "e_6ae851cbf410ab7b2f03bef9"
planId: "e_6ae851cbf410ab7b2f03bef9"
---
# Verify round 1 fix: the fast-lane hand-off carries due_at, written by Save hand-off (new optional due_at input) and pass

## Requested outcome
Verify round 1 fix: the fast-lane hand-off carries due_at, written by Save hand-off (new optional due_at input) and passed by Log signal along with its origin

## Touches
- automation · Pipeline Factory · Save hand-off · 6ae840a5fbdd550a9a44c524
- automation · Pipeline Factory · Log signal · 6ae843cc9594aa458cba14d7

## Ready when
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Save hand-off with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Save hand-off deployed at the fixed version.
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Log signal with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Log signal deployed at the fixed version.
- deploy Pipeline Factory · Save hand-off
- deploy Pipeline Factory · Log signal
