---
nebula: 3
specId: "e_6ae83ebbf410ab7b2ff0bb80"
mode: "sonic"
title: "Pipeline Factory Control Tower · objects"
owner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","userId":66770}
askBeforeDeploy: true
releaseYes: []
touches: [{"kind":"object","name":"PF Patch"},{"kind":"object","name":"PF Account"},{"kind":"object","name":"PF Person"},{"kind":"object","name":"PF Signal"},{"kind":"object","name":"PF Fact"},{"kind":"object","name":"PF Draft"},{"kind":"object","name":"PF Hand-off"},{"kind":"object","name":"PF Component"},{"kind":"object","name":"PF Seed snapshot"}]
reviewEvidence: []
revision: 1
revisionHistory: []
creationId: "037b6ccf-b0e2-44f8-94df-6442b2f686a5"
pageDesign: 2
createdAt: "2026-11-02T07:41:49.244Z"
runningAt: "2026-11-02T07:41:53.111Z"
runner: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525","email":"gourav.mahunta@unifyapps.com","claudeSessionId":"8da1d8cb-cc02-5ac8-85df-da01be5fab51"}
---
<!-- nebula:status -->
## Status
Finished. All tasks completed.
<!-- /nebula:status -->

## Plan

Goal: Pipeline Factory Control Tower · objects

| id | kind | entity | dependsOn | status | attempts |
|---|---|---|---|---|---:|
| t1 | object | PF Patch |  | done | 1 |
| t2 | object | PF Account |  | done | 1 |
| t3 | object | PF Person |  | done | 1 |
| t4 | object | PF Signal |  | done | 1 |
| t5 | object | PF Fact |  | done | 1 |
| t6 | object | PF Draft |  | done | 1 |
| t7 | object | PF Hand-off |  | done | 1 |
| t8 | object | PF Component |  | done | 1 |
| t9 | object | PF Seed snapshot |  | done | 1 |

### t1 · Create object PF Patch

Body:
1. Read: \`entity context object --name "PF Patch" --json\`, then \`get_objects\` on \`OBJ_pf_patch\`; it must answer not found. If an object named "PF Patch" or with id \`OBJ_pf_patch\` already exists, stop and report.
2. Done when: the object "PF Patch" exists with id \`OBJ_pf_patch\`, description "The patches: slots, pace and success rate per patch.", and exactly this schema from the contract: id OBJ_pf_patch; primaryKey patch_id (text, required); fields name (text), pod (text), owner_ae (text), bdr (text), geo (text), eligible_accounts (number), slots_base (number), slots_allocated (number), slots_used (number), pace_boost_pct (number), intros_booked_7d (number), success_rate (number), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_patch\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_patch shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_patch"}
Read back: OBJ_pf_patch: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_patch: get_objects primaryKey patch_id (string, primaryKey:true in input and schema halves); required: ["patch_id"]
Read back: OBJ_pf_patch: get_objects fields with types: patch_id string, name string, pod string, owner_ae string, bdr string, geo string, eligible_accounts number, slots_base number, slots_allocated number, slots_used number, pace_boost_pct number, intros_booked_7d number, success_rate number, origin string/single-select
Read back: OBJ_pf_patch: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_patch: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey patch_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_patch is live with primaryKey patch_id; a record created with patch_id gets that value as its record id. Picklist values are the codes, not the labels.

### t2 · Create object PF Account

Body:
1. Read: \`entity context object --name "PF Account" --json\`, then \`get_objects\` on \`OBJ_pf_account\`; it must answer not found. If an object named "PF Account" or with id \`OBJ_pf_account\` already exists, stop and report.
2. Done when: the object "PF Account" exists with id \`OBJ_pf_account\`, description "The patch accounts with fit, timing, Gate 1 state and the fields that lock at booking.", and exactly this schema from the contract: id OBJ_pf_account; primaryKey account_id (text, required); fields name (text), industry (text), patch_id (text), pod (text), owner_ae (text), backup_ae (text), bdr_of_record (text), hq_city (text), fit_score (number, of 60), fit_band (picklist: best "Best fit", medium "Medium fit", low "Low fit"), icp_quadrant (text), timing_score (number, of 40), rank_in_patch (number), top_signals (text), last_touch (date, epoch ms), gate1_status (picklist: pending "Pending", accepted "Accepted", rejected "Rejected", blocked "Blocked", queued "Queued", not_eligible "Not eligible"), gate1_reason (picklist: none "None", bad_fit "Bad fit", active_deal "Active deal", wrong_timing "Wrong timing", in_conversation "Already in conversation"), factory_holdout (boolean), factory_holdout_until (date, epoch ms), ultimate_parent_lock (text), deal_stage (picklist: none "None", engage "Engage", connect "Connect", commit "Commit"), meeting_type (text), meeting_source (text), factory_sourced (boolean), factory_influenced (boolean), marketing_influenced (boolean), value_pattern (text), locked_at (date, epoch ms), meeting_label (picklist: none "None", intro "Intro", new_buyer "New Buyer Meeting", does_not_count "Doesn't count"), qualified_status (picklist: none "None", qualified "Qualified", not_qualified "Not qualified"), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_account\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_account shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_account"}
Read back: OBJ_pf_account: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_account: get_objects primaryKey account_id (string, primaryKey:true in input and schema halves); required: ["account_id"]
Read back: OBJ_pf_account: get_objects fields with types: account_id string, name string, industry string, patch_id string, pod string, owner_ae string, backup_ae string, bdr_of_record string, hq_city string, fit_score number, fit_band string/single-select, icp_quadrant string, timing_score number, rank_in_patch number, top_signals string, last_touch integer/date, gate1_status string/single-select, gate1_reason string/single-select, factory_holdout boolean, factory_holdout_until integer/date, ultimate_parent_lock string, deal_stage string/single-select, meeting_type string, meeting_source string, factory_sourced boolean, factory_influenced boolean, marketing_influenced boolean, value_pattern string, locked_at integer/date, meeting_label string/single-select, qualified_status string/single-select, origin string/single-select
Read back: OBJ_pf_account: picklist fit_band [best "Best fit", medium "Medium fit", low "Low fit"] default best
Read back: OBJ_pf_account: picklist gate1_status [pending "Pending", accepted "Accepted", rejected "Rejected", blocked "Blocked", queued "Queued", not_eligible "Not eligible"] default pending
Read back: OBJ_pf_account: picklist gate1_reason [none "None", bad_fit "Bad fit", active_deal "Active deal", wrong_timing "Wrong timing", in_conversation "Already in conversation"] default none
Read back: OBJ_pf_account: picklist deal_stage [none "None", engage "Engage", connect "Connect", commit "Commit"] default none
Read back: OBJ_pf_account: picklist meeting_label [none "None", intro "Intro", new_buyer "New Buyer Meeting", does_not_count "Doesn't count"] default none
Read back: OBJ_pf_account: picklist qualified_status [none "None", qualified "Qualified", not_qualified "Not qualified"] default none
Read back: OBJ_pf_account: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_account: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey account_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_account is live with primaryKey account_id; a record created with account_id gets that value as its record id. Picklist values are the codes, not the labels.

### t3 · Create object PF Person

Body:
1. Read: \`entity context object --name "PF Person" --json\`, then \`get_objects\` on \`OBJ_pf_person\`; it must answer not found. If an object named "PF Person" or with id \`OBJ_pf_person\` already exists, stop and report.
2. Done when: the object "PF Person" exists with id \`OBJ_pf_person\`, description "The story account's buying committee by tier and role.", and exactly this schema from the contract: id OBJ_pf_person; primaryKey person_id (text, required); fields account_id (text), name (text), title (text), role (picklist: economic_buyer "Economic buyer", champion "Champion", technical_evaluator "Technical evaluator", business_owner "Business owner", gatekeeper "Gatekeeper"), tier (picklist: t1 "Tier 1", t2 "Tier 2", t3 "Tier 3", backup "Backup", mapped "Mapped only"), note (text), email_status (picklist: verified "Verified", linkedin_only "LinkedIn only"), dnc (boolean), in_other_sequence (boolean), confidence (number), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]"), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_person\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_person shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_person"}
Read back: OBJ_pf_person: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_person: get_objects primaryKey person_id (string, primaryKey:true in input and schema halves); required: ["person_id"]
Read back: OBJ_pf_person: get_objects fields with types: person_id string, account_id string, name string, title string, role string/single-select, tier string/single-select, note string, email_status string/single-select, dnc boolean, in_other_sequence boolean, confidence number, evidence_tag string/single-select, origin string/single-select
Read back: OBJ_pf_person: picklist role [economic_buyer "Economic buyer", champion "Champion", technical_evaluator "Technical evaluator", business_owner "Business owner", gatekeeper "Gatekeeper"] default economic_buyer
Read back: OBJ_pf_person: picklist tier [t1 "Tier 1", t2 "Tier 2", t3 "Tier 3", backup "Backup", mapped "Mapped only"] default t1
Read back: OBJ_pf_person: picklist email_status [verified "Verified", linkedin_only "LinkedIn only"] default verified
Read back: OBJ_pf_person: picklist evidence_tag [public "[PUBLIC]", hypothesis "[HYPOTHESIS]"] default public
Read back: OBJ_pf_person: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_person: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey person_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_person is live with primaryKey person_id; a record created with person_id gets that value as its record id. Picklist values are the codes, not the labels.
Note: Field title (text) has display label "Job Title" so that it does not clash with the object Name label; the field name is title exactly as the contract gives.
Note: Field dnc has display label "Do Not Contact".

### t4 · Create object PF Signal

Body:
1. Read: \`entity context object --name "PF Signal" --json\`, then \`get_objects\` on \`OBJ_pf_signal\`; it must answer not found. If an object named "PF Signal" or with id \`OBJ_pf_signal\` already exists, stop and report.
2. Done when: the object "PF Signal" exists with id \`OBJ_pf_signal\`, description "Buying signals with weight, confidence and whether they counted.", and exactly this schema from the contract: id OBJ_pf_signal; primaryKey signal_id (text, required); fields account_id (text), signal_type (picklist: pricing_visit "Checked pricing/product visit", new_leader "New CIO/CTO/CDO/CAIO/Head of AI", event "Event or webinar", ai_hiring "AI platform hiring", earnings "Earnings naming AI", bombora "Bombora surge", vendor_interest "Interest in a current vendor's tool", vendor_renewal "Vendor renewal within 9 months", funding "Funding, merger or new market", exec_posts "Executive posts on AI"), weight (number), signal_date (date, epoch ms), source_link (text), confidence (number), counted (boolean), not_counted_reason (text), fast_lane (boolean), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_signal\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_signal shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_signal"}
Read back: OBJ_pf_signal: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_signal: get_objects primaryKey signal_id (string, primaryKey:true in input and schema halves); required: ["signal_id"]
Read back: OBJ_pf_signal: get_objects fields with types: signal_id string, account_id string, signal_type string/single-select, weight number, signal_date integer/date, source_link string, confidence number, counted boolean, not_counted_reason string, fast_lane boolean, origin string/single-select
Read back: OBJ_pf_signal: picklist signal_type [pricing_visit "Checked pricing/product visit", new_leader "New CIO/CTO/CDO/CAIO/Head of AI", event "Event or webinar", ai_hiring "AI platform hiring", earnings "Earnings naming AI", bombora "Bombora surge", vendor_interest "Interest in a current vendor's tool", vendor_renewal "Vendor renewal within 9 months", funding "Funding, merger or new market", exec_posts "Executive posts on AI"] default pricing_visit
Read back: OBJ_pf_signal: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_signal: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey signal_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_signal is live with primaryKey signal_id; a record created with signal_id gets that value as its record id. Picklist values are the codes, not the labels.

### t5 · Create object PF Fact

Body:
1. Read: \`entity context object --name "PF Fact" --json\`, then \`get_objects\` on \`OBJ_pf_fact\`; it must answer not found. If an object named "PF Fact" or with id \`OBJ_pf_fact\` already exists, stop and report.
2. Done when: the object "PF Fact" exists with id \`OBJ_pf_fact\`, description "Sourced company facts, use case matches and Case for Change lines.", and exactly this schema from the contract: id OBJ_pf_fact; primaryKey fact_id (text, required); fields account_id (text), kind (picklist: fact "Company fact", use_case "Use case match", case_for_change "Case for Change line"), statement (text), quote (text), source (text), page_or_time (text), fact_date (date, epoch ms), link (text), evidence_tag (picklist: public "[PUBLIC]", hypothesis "[HYPOTHESIS]"), uc_id (text), confidence (number), writer (text), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_fact\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_fact shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_fact"}
Read back: OBJ_pf_fact: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_fact: get_objects primaryKey fact_id (string, primaryKey:true in input and schema halves); required: ["fact_id"]
Read back: OBJ_pf_fact: get_objects fields with types: fact_id string, account_id string, kind string/single-select, statement string, quote string, source string, page_or_time string, fact_date integer/date, link string, evidence_tag string/single-select, uc_id string, confidence number, writer string, origin string/single-select
Read back: OBJ_pf_fact: picklist kind [fact "Company fact", use_case "Use case match", case_for_change "Case for Change line"] default fact
Read back: OBJ_pf_fact: picklist evidence_tag [public "[PUBLIC]", hypothesis "[HYPOTHESIS]"] default public
Read back: OBJ_pf_fact: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_fact: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey fact_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_fact is live with primaryKey fact_id; a record created with fact_id gets that value as its record id. Picklist values are the codes, not the labels.

### t6 · Create object PF Draft

Body:
1. Read: \`entity context object --name "PF Draft" --json\`, then \`get_objects\` on \`OBJ_pf_draft\`; it must answer not found. If an object named "PF Draft" or with id \`OBJ_pf_draft\` already exists, stop and report.
2. Done when: the object "PF Draft" exists with id \`OBJ_pf_draft\`, description "The drafts held at Gate 2 with grade, fact check and rules result.", and exactly this schema from the contract: id OBJ_pf_draft; primaryKey draft_id (text, required); fields account_id (text), person_id (text), play_id (text), channel (picklist: email "Email", linkedin "LinkedIn", call "Call"), subject (text), body (text), grade (number), fact_check (picklist: passed "Passed", blocked "Blocked"), rules_check (picklist: pending "Pending", passed "Passed", blocked "Blocked"), rules_reason (text), sender (text), sender_pod (text), planted_error (boolean), status (picklist: waiting_gate2 "Waiting at Gate 2", approved "Approved", blocked "Blocked", held "Held", enrolled "Enrolled"), enrolment_key (text), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_draft\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_draft shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_draft"}
Read back: OBJ_pf_draft: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_draft: get_objects primaryKey draft_id (string, primaryKey:true in input and schema halves); required: ["draft_id"]
Read back: OBJ_pf_draft: get_objects fields with types: draft_id string, account_id string, person_id string, play_id string, channel string/single-select, subject string, body string, grade number, fact_check string/single-select, rules_check string/single-select, rules_reason string, sender string, sender_pod string, planted_error boolean, status string/single-select, enrolment_key string, origin string/single-select
Read back: OBJ_pf_draft: picklist channel [email "Email", linkedin "LinkedIn", call "Call"] default email
Read back: OBJ_pf_draft: picklist fact_check [passed "Passed", blocked "Blocked"] default passed
Read back: OBJ_pf_draft: picklist rules_check [pending "Pending", passed "Passed", blocked "Blocked"] default pending
Read back: OBJ_pf_draft: picklist status [waiting_gate2 "Waiting at Gate 2", approved "Approved", blocked "Blocked", held "Held", enrolled "Enrolled"] default waiting_gate2
Read back: OBJ_pf_draft: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_draft: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey draft_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_draft is live with primaryKey draft_id; a record created with draft_id gets that value as its record id. Picklist values are the codes, not the labels.

### t7 · Create object PF Hand-off

Body:
1. Read: \`entity context object --name "PF Hand-off" --json\`, then \`get_objects\` on \`OBJ_pf_handoff\`; it must answer not found. If an object named "PF Hand-off" or with id \`OBJ_pf_handoff\` already exists, stop and report.
2. Done when: the object "PF Hand-off" exists with id \`OBJ_pf_handoff\`, description "Every hand-off as a saved record: schema-checked, confidence-scored, keyed by Patch ID.", and exactly this schema from the contract: id OBJ_pf_handoff; primaryKey handoff_id (text, required); fields idempotency_key (text, account_id + person_id + play_id), patch_id (text), account_id (text), person_id (text), play_id (text), from_component (text), to_component (text), record_type (text), payload (text, JSON), evidence (text), confidence (number), threshold (number), schema_status (picklist: passed "Passed", rejected "Rejected"), status (picklist: flowed "Flowed on", waiting_person "Waiting on a person", rejected "Rejected", late "Late, retried", held "Held: component paused"), assigned_to (text), reason (text), model (text), cost_usd (number), latency_ms (number), due_at (date, epoch ms), saved_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_handoff\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_handoff shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_handoff"}
Read back: OBJ_pf_handoff: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_handoff: get_objects primaryKey handoff_id (string, primaryKey:true in input and schema halves); required: ["handoff_id"]
Read back: OBJ_pf_handoff: get_objects fields with types: handoff_id string, idempotency_key string, patch_id string, account_id string, person_id string, play_id string, from_component string, to_component string, record_type string, payload string, evidence string, confidence number, threshold number, schema_status string/single-select, status string/single-select, assigned_to string, reason string, model string, cost_usd number, latency_ms number, due_at integer/date, saved_at integer/date, origin string/single-select
Read back: OBJ_pf_handoff: picklist schema_status [passed "Passed", rejected "Rejected"] default passed
Read back: OBJ_pf_handoff: picklist status [flowed "Flowed on", waiting_person "Waiting on a person", rejected "Rejected", late "Late, retried", held "Held: component paused"] default flowed
Read back: OBJ_pf_handoff: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_handoff: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey handoff_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_handoff is live with primaryKey handoff_id; a record created with handoff_id gets that value as its record id. Picklist values are the codes, not the labels.

### t8 · Create object PF Component

Body:
1. Read: \`entity context object --name "PF Component" --json\`, then \`get_objects\` on \`OBJ_pf_component\`; it must answer not found. If an object named "PF Component" or with id \`OBJ_pf_component\` already exists, stop and report.
2. Done when: the object "PF Component" exists with id \`OBJ_pf_component\`, description "The registry: 38 agents, 12 workflows, 5 human gates and 2 rule steps.", and exactly this schema from the contract: id OBJ_pf_component; primaryKey component_id (text, required); fields name (text), sub_workflow (picklist: sw1 "1. Patch accounts", sw2 "2. Account selection", sw3 "3. Account research", sw4 "4. Buying committee", sw5 "5. Outreach drafting", sw6 "6. Outreach", sw7 "7. Engage, Connect and Commit", sw8 "8. Learning and governance"), kind (picklist: agent "Agent", checker "Checker", monitor "Monitor", workflow "Workflow", human_gate "Human gate", rule_step "Rule step"), what_it_does (text), threshold (number), below_threshold_goes_to (text), schedule (text), feeds (text), writes (text), model_family (picklist: family_a "Family A (drafters)", family_b "Family B (checkers)", none "No model"), checks (text), success_rate (number), status (picklist: live "Live", shadow "Shadow", paused "Paused"), ask_id (text), origin (picklist: user "User", seed "Seed", test "Test"; default user). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_component\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_component shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_component"}
Read back: OBJ_pf_component: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_component: get_objects primaryKey component_id (string, primaryKey:true in input and schema halves); required: ["component_id"]
Read back: OBJ_pf_component: get_objects fields with types: component_id string, name string, sub_workflow string/single-select, kind string/single-select, what_it_does string, threshold number, below_threshold_goes_to string, schedule string, feeds string, writes string, model_family string/single-select, checks string, success_rate number, status string/single-select, ask_id string, origin string/single-select
Read back: OBJ_pf_component: picklist sub_workflow [sw1 "1. Patch accounts", sw2 "2. Account selection", sw3 "3. Account research", sw4 "4. Buying committee", sw5 "5. Outreach drafting", sw6 "6. Outreach", sw7 "7. Engage, Connect and Commit", sw8 "8. Learning and governance"] default sw1
Read back: OBJ_pf_component: picklist kind [agent "Agent", checker "Checker", monitor "Monitor", workflow "Workflow", human_gate "Human gate", rule_step "Rule step"] default agent
Read back: OBJ_pf_component: picklist model_family [family_a "Family A (drafters)", family_b "Family B (checkers)", none "No model"] default family_a
Read back: OBJ_pf_component: picklist status [live "Live", shadow "Shadow", paused "Paused"] default live
Read back: OBJ_pf_component: picklist origin [user "User", seed "Seed", test "Test"] default user
Read back: OBJ_pf_component: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey component_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_component is live with primaryKey component_id; a record created with component_id gets that value as its record id. Picklist values are the codes, not the labels.

### t9 · Create object PF Seed snapshot

Body:
1. Read: \`entity context object --name "PF Seed snapshot" --json\`, then \`get_objects\` on \`OBJ_pf_seed_snapshot\`; it must answer not found. If an object named "PF Seed snapshot" or with id \`OBJ_pf_seed_snapshot\` already exists, stop and report.
2. Done when: the object "PF Seed snapshot" exists with id \`OBJ_pf_seed_snapshot\`, description "The seeded values the reset restores.", and exactly this schema from the contract: id OBJ_pf_seed_snapshot; primaryKey snapshot_id (text, required); fields object_id (text), record_id (text), row_values (text, JSON of the seeded row), taken_at (date, epoch ms), origin (picklist: user "User", seed "Seed", test "Test"; default seed). The primaryKey field is in \`required\`. Every picklist stores the codes quoted with the labels quoted, the first value as the default where the line names no default; every date field stores epoch ms; every number field is a number; text fields named JSON are plain text holding JSON. Field types and keys follow \`object-storage-manager\` § Object schema format.
3. Apply the write once, with the plain field names the line gives (no \`properties_\` prefix). No lookup fields: objects link by the text keys the line names (account_id, patch_id, person_id).
4. Read back: \`get_objects\` on \`OBJ_pf_seed_snapshot\` quoting the primaryKey, the required list and every field the body lists with its type, and each picklist with its codes and labels.
5. Report ids (the object id as \`ids.entity\`), readBack, unverified, notes.

Proof: get_objects on OBJ_pf_seed_snapshot shows primaryKey, required and every field the body lists, with each picklist's codes and labels.
Result IDs: {"entity":"OBJ_pf_seed_snapshot"}
Read back: OBJ_pf_seed_snapshot: apply_object_batch wrote:true, step create_object ok, objects[].unmirroredFields: [] (no half-stored field)
Read back: OBJ_pf_seed_snapshot: get_objects primaryKey snapshot_id (string, primaryKey:true in input and schema halves); required: ["snapshot_id"]
Read back: OBJ_pf_seed_snapshot: get_objects fields with types: snapshot_id string, object_id string, record_id string, row_values string, taken_at integer/date, origin string/single-select
Read back: OBJ_pf_seed_snapshot: picklist origin [user "User", seed "Seed", test "Test"] default seed
Read back: OBJ_pf_seed_snapshot: settings store MONGO; access external:false, skipPermissionsFilter:false (secure-by-default rule 1: platform permission filter kept); tags ["Nebula"] added by the platform
Unverified: No custom indexes were created: the contract names none; access patterns on text keys (account_id, patch_id, person_id) rely on default indexing. Check get_objects parts:[indexes] if a later task adds them.
Note: Schema check (object-schema-designer): natural primaryKey snapshot_id is a stable text key the plan gives, listed in required; cross-object links are plain text keys per the task (no foreignKey), so nothing enforces them on write and a delete leaves child rows pointing at the old key; every picklist default is its first value unless the contract named one; date fields are integer/format date/dateFormat epoch; no secure or hashed fields, since filters read every key field.
Note: handover: OBJ_pf_seed_snapshot is live with primaryKey snapshot_id; a record created with snapshot_id gets that value as its record id. Picklist values are the codes, not the labels.

