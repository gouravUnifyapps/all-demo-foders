---
nebula: 3
mode: "sonic"
format: "spec"
title: "Verify round 1 fixes (G3 round 2): Run component runs a component with no account; Save agent output passes the model an"
touches: [{"kind":"automation","name":"Pipeline Factory · Run component","id":"6ae865229ec43c6ee2300d8d"},{"kind":"automation","name":"Pipeline Factory · Save agent output","id":"6ae864829594aa458cc1ce69"},{"kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"},{"kind":"ai-agent","name":"PF · Reply Sorter","id":"e_6ae86bebf410ab7b2f20260c"}]
askBeforeDeploy: true
releaseYes: [{"action":"deploy","kind":"automation","name":"Pipeline Factory · Run component","id":"6ae865229ec43c6ee2300d8d"},{"action":"deploy","kind":"automation","name":"Pipeline Factory · Save agent output","id":"6ae864829594aa458cc1ce69"},{"action":"publish","kind":"ai-agent","name":"Pipeline Factory Analyst","id":"e_6ae846ffd96c5f6ba22b98da"},{"action":"publish","kind":"ai-agent","name":"PF · Reply Sorter","id":"e_6ae86bebf410ab7b2f20260c"}]
acceptedAt: "2026-11-02T11:37:15.164Z"
acceptedBy: {"clientId":"533e7426-6927-42a4-bbcf-657253136df4"}
planIds: ["e_6ae875efafe7fc590a571f16"]
latestPlanId: "e_6ae875efafe7fc590a571f16"
planId: "e_6ae875efafe7fc590a571f16"
---
# Verify round 1 fixes (G3 round 2): Run component runs a component with no account; Save agent output passes the model an

## Requested outcome
Verify round 1 fixes (G3 round 2): Run component runs a component with no account; Save agent output passes the model and each receiver's threshold to its hand-offs; the analyst gives stored dates as they are; publish PF · Reply Sorter's saved draft.

## Touches
- automation · Pipeline Factory · Run component · 6ae865229ec43c6ee2300d8d
- automation · Pipeline Factory · Save agent output · 6ae864829594aa458cc1ce69
- ai-agent · Pipeline Factory Analyst · e_6ae846ffd96c5f6ba22b98da
- ai-agent · PF · Reply Sorter · e_6ae86bebf410ab7b2f20260c

## Ready when
- Read-back: Test runs of Run component for C13, C33 and C39 with no account answer ran, and C18 on A-1001 still runs.
- Read-back: search_workflows shows Run component deployed at the saved version.
- Read-back: The PF Hand-off rows a test save makes carry the run's model and each receiver's threshold.
- Read-back: search_workflows shows Save agent output deployed at the saved version.
- Read-back: get_agent shows the date rule; the test answers 2027-01-27.
- Read-back: get_agent shows the analyst published with nothing left to publish.
- Read-back: get_agent shows PF · Reply Sorter published with nothing left to publish.
- deploy Pipeline Factory · Run component
- deploy Pipeline Factory · Save agent output
- publish Pipeline Factory Analyst
- publish PF · Reply Sorter
