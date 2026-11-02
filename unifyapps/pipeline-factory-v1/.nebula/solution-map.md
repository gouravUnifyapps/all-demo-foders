# Solution map

Solution: `UnifyApps · Pipeline Factory v1` (e_6ae5bfc3b4f0d14b27962a04) · tenant orbit.uat.unifyapps.com

## Entities

| Kind | Name | Id | Version | Stale |
|---|---|---|---|---|
| app | `UnifyApps Pipeline Factory Control Tower` | app-2fbe93e8c1f7 | 5 | no |
| page | `global-page-of-app-2fbe93e8c1f7` | e_global_app-2fbe93e8c1f7 | 0 | no |
| automation | `Pipeline Factory · Save hand-off` | 6ae840a5fbdd550a9a44c524 | 4 | no |
| automation | `Pipeline Factory · Clear Gate 2` | 6ae840d7f6f76639f8ceb67d | 2 | no |
| automation | `Pipeline Factory · Log signal` | 6ae843cc9594aa458cba14d7 | 2 | no |
| automation | `Pipeline Factory · Pause component` | 6ae843d1f6f76639f8cf2d55 | 0 | no |
| automation | `Pipeline Factory · Read factory records` | 6ae843e69ec43c6ee2dec988 | 2 | no |
| automation | `Pipeline Factory · Decide Gate 1` | 6ae8440df13e536c52c5d959 | 2 | no |
| automation | `Pipeline Factory · Reset demo` | 6ae8441df38e327618fcc13c | 4 | no |
| automation | `Pipeline Factory · Book meeting` | 6ae84449f38e327618fcc640 | 2 | no |
| automation | `Pipeline Factory · Ask the analyst` | 6ae84900fbdd550a9a465807 | 0 | no |
| object | `PF Patch` | OBJ_pf_patch | 0 | no |
| object | `PF Account` | OBJ_pf_account | 0 | no |
| object | `PF Person` | OBJ_pf_person | 0 | no |
| object | `PF Signal` | OBJ_pf_signal | 0 | no |
| object | `PF Fact` | OBJ_pf_fact | 0 | no |
| object | `PF Draft` | OBJ_pf_draft | 0 | no |
| object | `PF Hand-off` | OBJ_pf_handoff | 0 | no |
| object | `PF Component` | OBJ_pf_component | 1 | no |
| object | `PF Seed snapshot` | OBJ_pf_seed_snapshot | 0 | no |
| object | `PF Component run` | OBJ_pf_component_run | 0 | no |
| object | `PF Source` | OBJ_pf_source | 0 | no |
| object | `PF Inbox` | OBJ_pf_inbox | 0 | no |
| object | `PF Suppression` | OBJ_pf_suppression | 0 | no |
| ai-agent | `Pipeline Factory Analyst` | e_6ae846ffd96c5f6ba22b98da | 14 | no |

## Wiring

| From | Part | To | Via | Fields |
|---|---|---|---|---|
| page `global-page-of-app-2fbe93e8c1f7` | `data source Pause component` | automation `Pipeline Factory · Pause component` | data source |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source Book meeting` | automation `Pipeline Factory · Book meeting` | data source |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source Clear Gate 2` | automation `Pipeline Factory · Clear Gate 2` | data source |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source Ask the analyst` | automation `Pipeline Factory · Ask the analyst` | data source |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source Decide Gate 1` | automation `Pipeline Factory · Decide Gate 1` | data source |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source data_delete_app-2fbe93e8c1f7` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source data_update_app-2fbe93e8c1f7` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source data_create_app-2fbe93e8c1f7` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source data_fetchOne_app-2fbe93e8c1f7` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source data_fetch_app-2fbe93e8c1f7` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-2fbe93e8c1f7` | `data source Log signal` | automation `Pipeline Factory · Log signal` | data source |  |
| automation `Pipeline Factory · Save hand-off` | `node Find the sending component in the register` | object `PF Component` | storage read |  |
| automation `Pipeline Factory · Save hand-off` | `node Find the receiving component in the register` | object `PF Component` | storage read |  |
| automation `Pipeline Factory · Save hand-off` | `node Find another component registered as that field's writer` | object `PF Component` | storage read |  |
| automation `Pipeline Factory · Save hand-off` | `node Save the rejected hand-off for the GTM engineer` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Save hand-off` | `node Look for an earlier save under the same key and pair` | object `PF Hand-off` | storage read |  |
| automation `Pipeline Factory · Save hand-off` | `node Save the hand-off on the named person's to-do list` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Save hand-off` | `node Save the hand-off as flowed on` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Read the draft` | object `PF Draft` | storage read |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Look for an enrolment of the same person and play` | object `PF Draft` | storage read |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Park the draft` | object `PF Draft` | storage write |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Read the draft's account` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Read the draft's person` | object `PF Person` | storage read |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Mark the draft blocked` | object `PF Draft` | storage write |  |
| automation `Pipeline Factory · Clear Gate 2` | `node Enrol the draft once (Outreach Launcher, mocked)` | object `PF Draft` | storage write |  |
| automation `Pipeline Factory · Log signal` | `node Read the account` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Log signal` | `node Look for an earlier visit to the account in the last 7 days` | object `PF Signal` | storage read |  |
| automation `Pipeline Factory · Log signal` | `node Look for an earlier counted visit in the last 14 days` | object `PF Signal` | storage read |  |
| automation `Pipeline Factory · Log signal` | `node Save the signal` | object `PF Signal` | storage write |  |
| automation `Pipeline Factory · Log signal` | `node Write the account's timing score` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Log signal` | `node Send it down the fast lane to the Play Picker, due within the hour` | automation `Pipeline Factory · Save hand-off` | call node | `handoff_id`, `result` |
| automation `Pipeline Factory · Pause component` | `node Read the component from PF Component` | object `PF Component` | storage read |  |
| automation `Pipeline Factory · Pause component` | `node Set the component to paused` | object `PF Component` | storage write |  |
| automation `Pipeline Factory · Pause component` | `node Hold every flowed or late hand-off this component sent` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Read factory records` | `node Read the patches` | object `PF Patch` | storage read |  |
| automation `Pipeline Factory · Read factory records` | `node Read the accounts` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Read factory records` | `node Read the hand-offs waiting on a person, rejected or late` | object `PF Hand-off` | storage read |  |
| automation `Pipeline Factory · Read factory records` | `node Read the components under 97% success` | object `PF Component` | storage read |  |
| automation `Pipeline Factory · Read factory records` | `node Read the people of the accounts` | object `PF Person` | storage read |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Read the account` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Mark the account blocked at Gate 1` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Mark the account rejected with its reason` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Find the next queued account of the same patch` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Move the refill account to Gate 1` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Mark the account accepted` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Hand off to the Company Facts Collector` | automation `Pipeline Factory · Save hand-off` | call node | `result` |
| automation `Pipeline Factory · Decide Gate 1` | `node Hand off to the Buying Team Mapper` | automation `Pipeline Factory · Save hand-off` | call node | `result` |
| automation `Pipeline Factory · Decide Gate 1` | `node Read the patch` | object `PF Patch` | storage read |  |
| automation `Pipeline Factory · Decide Gate 1` | `node Add 1 to the patch's slots used` | object `PF Patch` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Patch` | object `PF Patch` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Account` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Person` | object `PF Person` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Signal` | object `PF Signal` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Fact` | object `PF Fact` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Draft` | object `PF Draft` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Hand-off` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Component` | object `PF Component` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Delete origin test rows in PF Seed snapshot` | object `PF Seed snapshot` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Read the seed snapshot` | object `PF Seed snapshot` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the PF Hand-off ids that have a seed snapshot` | object `PF Seed snapshot` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Delete every PF Hand-off with no seed snapshot` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Patch` | object `PF Patch` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Account` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Person` | object `PF Person` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Signal` | object `PF Signal` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Fact` | object `PF Fact` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Draft` | object `PF Draft` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Hand-off` | object `PF Hand-off` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Read the current seed rows of PF Component` | object `PF Component` | storage read |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Patch seed row back` | object `PF Patch` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Account seed row back` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Person seed row back` | object `PF Person` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Signal seed row back` | object `PF Signal` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Fact seed row back` | object `PF Fact` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Draft seed row back` | object `PF Draft` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Hand-off seed row back` | object `PF Hand-off` | storage write |  |
| automation `Pipeline Factory · Reset demo` | `node Put the PF Component seed row back` | object `PF Component` | storage write |  |
| automation `Pipeline Factory · Book meeting` | `node Read the account` | object `PF Account` | storage read |  |
| automation `Pipeline Factory · Book meeting` | `node Book the meeting and lock its fields` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Book meeting` | `node Save the Meeting Handoff hand-off` | automation `Pipeline Factory · Save hand-off` | call node | `handoff_id`, `result` |
| automation `Pipeline Factory · Book meeting` | `node Set the field to true` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Book meeting` | `node Set the field to false` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Book meeting` | `node Set the text field` | object `PF Account` | storage write |  |
| automation `Pipeline Factory · Book meeting` | `node Log the correction as a hand-off` | automation `Pipeline Factory · Save hand-off` | call node | `handoff_id` |

## Not checked

- ai-agent `Pipeline Factory Analyst` (e_6ae846ffd96c5f6ba22b98da): its tools are not in the cache (get_agent)
