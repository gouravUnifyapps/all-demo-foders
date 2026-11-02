---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fixes: Read factory records returns people and finds an account by name; the analyst uses the account id"
touches: [{"kind":"automation","name":"Pipeline Factory · Read factory records","id":"6ae843e69ec43c6ee2dec988"},{"kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read factory records","id":"6ae843e69ec43c6ee2dec988"},{"action":"publish","kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"}]
acceptedAt: "2026-11-02T08:51:03.615Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae84efbf410ab7b2f03537e"]
latestPlanId: "e_6ae84efbf410ab7b2f03537e"
planId: "e_6ae84efbf410ab7b2f03537e"
---
# Verify round 1 fixes: Read factory records returns people and finds an account by name; the analyst uses the account id

## Requested outcome
Verify round 1 fixes: Read factory records returns people and finds an account by name; the analyst uses the account id

## Touches
- automation · Pipeline Factory · Read factory records · 6ae843e69ec43c6ee2dec988
- ai-agent · Pipeline Factory Analyst · e_6ae846ffd96c5f6ba22b98da

## Ready when
- Read-back: open_workflow shows a higher saved version of Pipeline Factory · Read factory records with the fix; test runs read back.
- Read-back: search_workflows shows Pipeline Factory · Read factory records deployed at the fixed version.
- Read-back: get_agent shows the new instructions; the economic buyer answer names Helena Marsh.
- Read-back: get_agent shows the agent published.
- deploy Pipeline Factory · Read factory records
- publish Pipeline Factory Analyst
