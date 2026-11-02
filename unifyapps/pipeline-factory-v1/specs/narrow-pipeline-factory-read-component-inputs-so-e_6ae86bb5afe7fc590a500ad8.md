---
nebula: 3
mode: "sonic"
format: "spec"
title: "Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the f"
touches: [{"kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Read component inputs","id":"6ae8635446920244f3d5194b"}]
acceptedAt: "2026-11-02T10:53:39.387Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae86bb6d96c5f6ba24481b4"]
latestPlanId: "e_6ae86bb6d96c5f6ba24481b4"
planId: "e_6ae86bb6d96c5f6ba24481b4"
---
# Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the f

## Requested outcome
Narrow Pipeline Factory · Read component inputs so its reply fits an AI agent's tool reply (the runtime keeps only the first 16,000 and last 2,000 characters; A-1001 answers about 200,000), with the same inputs and result fields, and deploy it.

## Touches
- automation · Pipeline Factory · Read component inputs · 6ae8635446920244f3d5194b

## Ready when
- Read-back: Test runs of Pipeline Factory · Read component inputs answer under 12,000 characters for C32 on A-1001 with D-04 present, and the result fields are unchanged.
- Read-back: search_workflows shows Pipeline Factory · Read component inputs deployed with definitionVersion equal to the saved version.
- deploy Pipeline Factory · Read component inputs
