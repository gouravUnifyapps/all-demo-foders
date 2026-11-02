---
nebula: 3
mode: "sonic"
format: "spec"
title: "Pipeline Factory Control Tower · seed records"
touches: [{"kind":"object","name":"PF Patch","id":"OBJ_pf_patch"},{"kind":"object","name":"PF Account","id":"OBJ_pf_account"},{"kind":"object","name":"PF Person","id":"OBJ_pf_person"},{"kind":"object","name":"PF Signal","id":"OBJ_pf_signal"},{"kind":"object","name":"PF Fact","id":"OBJ_pf_fact"},{"kind":"object","name":"PF Draft","id":"OBJ_pf_draft"},{"kind":"object","name":"PF Hand-off","id":"OBJ_pf_handoff"},{"kind":"object","name":"PF Component","id":"OBJ_pf_component"},{"kind":"object","name":"PF Seed snapshot","id":"OBJ_pf_seed_snapshot"}]
askBeforeDeploy: true
releaseYes: []
acceptedAt: "2026-11-02T07:45:23.016Z"
acceptedBy: {"clientId":"e3c4458d-7875-4592-a302-6ed8821e5525"}
planIds: ["e_6ae83f98afe7fc590a136f65"]
latestPlanId: "e_6ae83f98afe7fc590a136f65"
planId: "e_6ae83f98afe7fc590a136f65"
---
# Pipeline Factory Control Tower · seed records

## Requested outcome
The pod BDR and the patch AE watch one account, Carrow & Vale Logistics, move through the Pipeline Factory: a strong signal takes the fast lane, Gate 1 accepts it, research and the buying team arrive as confidence-scored hand-off records, Gate 2 approves drafts while the Send Rules Check refuses one, and the booked meeting locks its fields. Every hand-off is a saved record in the control tower that a person can see, check and stop; an assistant answers what is waiting on a person and a person pauses a red component from its answer.
This plan writes the seed rows every beat depends on, story row A-1001 Carrow & Vale Logistics included, and the snapshot the demo reset restores.

## Touches
- object · PF Patch · OBJ_pf_patch
- object · PF Account · OBJ_pf_account
- object · PF Person · OBJ_pf_person
- object · PF Signal · OBJ_pf_signal
- object · PF Fact · OBJ_pf_fact
- object · PF Draft · OBJ_pf_draft
- object · PF Hand-off · OBJ_pf_handoff
- object · PF Component · OBJ_pf_component
- object · PF Seed snapshot · OBJ_pf_seed_snapshot

## Contract
### object · PF Patch
The patches: slots, pace and success rate per patch.
- record · seed · PF Patch: origin seed on every row. PATCH-NAE-03 "NA East · Logistics and Utilities", pod POD-NAE-1, owner_ae Dana Okafor, bdr Marcus Ellery, geo NA East, eligible_accounts 312, slots_base 25, slots_allocated 24, slots_used 19, pace_boost_pct 0, intros_booked_7d 4, success_rate 98.6; PATCH-NAE-04 "NA East · Manufacturing and Health", pod POD-NAE-2, owner_ae Rhea Castillo, bdr Tomas Ilves, geo NA East, eligible_accounts 260, slots_base 25, slots_allocated 20, slots_used 20, pace_boost_pct 25, intros_booked_7d 2, success_rate 99.2

### object · PF Account
The patch accounts with fit, timing, Gate 1 state and the fields that lock at booking.
- record · seed · PF Account: origin seed on every row; dates are epoch ms in the 90 days before the demo. A-1001 Carrow & Vale Logistics (the story row): logistics, PATCH-NAE-03, POD-NAE-1, owner_ae Dana Okafor, backup_ae Luis Brennan, bdr_of_record Marcus Ellery, hq_city Columbus OH, fit_score 49, fit_band best, icp_quadrant Q1, timing_score 25, rank_in_patch 1, top_signals "2 checked pricing visits in 14 days; AI platform hiring; renewal of current vendor in 8 months", gate1_status pending, gate1_reason none, factory_holdout false, ultimate_parent_lock Dana Okafor, deal_stage none, value_pattern "Order-to-cash orchestration", meeting_label none, qualified_status none. A-1002 Brightline Cold Chain: logistics, PATCH-NAE-03, fit 41 medium, timing 30, rank 2, pending. A-1003 Ostrander Marine Freight: logistics, PATCH-NAE-03, fit 44 medium, timing 15, rank 3, pending. A-1004 Pellham Ridge Distribution: logistics, PATCH-NAE-03, fit 38 low, timing 20, rank 4, pending. A-1005 Kestrel Ridge Utilities: utilities, PATCH-NAE-03, fit 40 medium, timing 22, rank 5, pending, factory_holdout true, factory_holdout_until 2027-01-27. A-1006 Tamsin Row Health Partners: healthcare, patch_id empty, pod empty, owner_ae empty, fit 43 medium, timing 18, gate1_status pending. A-1007 Quillfeather Insurance Group: insurance, PATCH-NAE-03, fit 46 best, timing 28, rank 6, accepted, deal_stage engage. A-1008 Marlow Basin Foods: food, PATCH-NAE-03, fit 37 low, timing 19, rank 7, queued. A-1009 Sablewood Retail Co: retail, PATCH-NAE-03, fit 42 medium, timing 12, rank 8, queued. A-1010 Fenwick Arc Manufacturing: manufacturing, PATCH-NAE-04, POD-NAE-2, Rhea Castillo, Tomas Ilves, fit 47 best, timing 26, rank 1, pending. A-1011 Larkspur Data Centers: technology, PATCH-NAE-04, fit 39 low, timing 24, rank 2, pending. A-1012 Harrowgate Mutual: insurance, PATCH-NAE-04, fit 45 best, accepted, deal_stage connect, meeting_label new_buyer. A-1013 Vexmoor Telecom: telecom, PATCH-NAE-04, fit 48 best, accepted, deal_stage commit, meeting_label new_buyer, qualified_status qualified. A-1014 Bellwether Grain Co-op: agriculture, PATCH-NAE-04, fit 35 low, not_eligible (below the floor of 36). A-1015 Corrin Bay Pharmacy Group: healthcare, PATCH-NAE-04, fit 41 medium, timing 17, rank 3, pending. Every PATCH-NAE-03 row carries pod POD-NAE-1, owner_ae Dana Okafor, backup_ae Luis Brennan, bdr_of_record Marcus Ellery; every PATCH-NAE-04 row pod POD-NAE-2, owner_ae Rhea Castillo, backup_ae Omar Haddad, bdr_of_record Tomas Ilves.

### object · PF Person
The story account's buying committee by tier and role.
- record · seed · PF Person: origin seed on every row; all for A-1001. P-1001 Helena Marsh, CFO, economic_buyer, t1, verified, confidence 88, public. P-1002 Arjun Mehta, VP Digital Operations, champion, t1, verified, 91, public. P-1003 Colette Baines, Head of AI (joined 6 weeks ago), business_owner, t1, verified, 84, public. P-1004 Wes Odum, Director Enterprise Architecture, technical_evaluator, t2, verified, 79, public. P-1005 Nadia Fournier, Director Order Management, business_owner, t2, verified, 66, hypothesis. P-1006 Gabe Lindahl, IT Integration Manager, technical_evaluator, t2, linkedin_only, 74, public. P-1007 Imani Clarke, Customer Operations Lead, business_owner, t3, verified, 72, public. P-1008 Sven Aldous, Finance Systems Manager, technical_evaluator, t3, verified, 70, public, in_other_sequence true. P-1009 Ruth Okonkwo, Procurement Lead, business_owner, t3, verified, 71, public. P-1010 Theo Marchetti, Automation Engineer, technical_evaluator, t3, verified, 75, public. P-1011 Lena Voss, Director Supply Chain Systems, champion, backup, verified, 77, public. P-1012 Calvin Reyes, Senior Integration Architect, technical_evaluator, backup, verified, 73, public. P-1013 Joan Pruitt, Executive Assistant to the CFO, gatekeeper, mapped, verified, 90, public. Each note is four lines: role and time in role, past companies, what they own, link to UC-ID UC-LOG-014.

### object · PF Signal
Buying signals with weight, confidence and whether they counted.
- record · seed · PF Signal: origin seed on every row. S-01 A-1001 pricing_visit weight 25, confidence 92, counted true (2 visits in 14 days, 40s and 65s with scroll). S-02 A-1001 pricing_visit weight 0, counted false, not_counted_reason "within 2 minutes of an email's delivery". S-03 A-1001 ai_hiring weight 15, confidence 81, counted true. S-04 A-1001 vendor_renewal weight 15, confidence 64, counted true. S-05 A-1002 bombora weight 15, confidence 77, counted true. S-06 A-1002 event weight 20, confidence 85, counted true. S-07 A-1003 earnings weight 15, confidence 73, counted true. S-08 A-1010 new_leader weight 20, confidence 88, counted true, fast_lane true. S-09 A-1011 funding weight 10, confidence 66, counted false, not_counted_reason "confidence under 70: logged, not scored".

### object · PF Fact
Sourced company facts, use case matches and Case for Change lines.
- record · seed · PF Fact: origin seed on every row; all for A-1001; links are invented addresses under carrowvale.example. F-01 fact "Order exceptions are handled by hand across three ERPs", quote from the latest annual report, page 14, public, confidence 90, writer Company Facts Collector. F-02 fact "Plans to automate order-to-cash by 2027", earnings call Q2, 00:18:40, public, 88. F-03 fact "Hiring three integration engineers for an AI platform team", job post, public, 82. F-04 fact "Cost-to-serve named a board priority", investor deck, slide 9, public, 86. F-05 use_case UC-LOG-014 "Order exception triage", confidence 84, writer Use Case Matcher. F-06 use_case UC-LOG-022 "Carrier invoice reconciliation", confidence 76. F-07 use_case UC-LOG-031 "Customer status agent", confidence 64, hypothesis (shown only as a question). F-08 case_for_change "Business problem: order exceptions handled by hand across three ERPs" (cites F-01), public. F-09 case_for_change "Why now: new Head of AI and an integration hiring push" (cites F-03), public. F-10 case_for_change "Risk: the current integration vendor contract may renew in 8 months" hypothesis, confidence 68, writer Case for Change Drafter.

### object · PF Draft
The drafts held at Gate 2 with grade, fact check and rules result.
- record · seed · PF Draft: origin seed on every row; all A-1001, play_id PLAY-SIG-NEWLEADER. D-01 P-1002 email, subject "Order exceptions across three ERPs", grade 86, fact_check passed, rules_check pending, sender Marcus Ellery, sender_pod POD-NAE-1, status waiting_gate2. D-02 P-1003 email, subject "Your first 90 days as Head of AI", grade 82, passed, pending, Marcus Ellery, POD-NAE-1, waiting_gate2. D-03 P-1001 linkedin, grade 79, passed, pending, sender Dana Okafor, POD-NAE-1, waiting_gate2. D-04 P-1004 email, subject "Integration hiring at Carrow & Vale", grade 81, passed, pending, sender Rhea Castillo, sender_pod POD-NAE-2, planted_error true, waiting_gate2. D-05 P-1005 email, grade 71 (under 75 after one rewrite: a person decides), passed, pending, Marcus Ellery, POD-NAE-1, waiting_gate2. D-06 P-1008 email, grade 80, passed, pending, Marcus Ellery, POD-NAE-1, waiting_gate2 (P-1008 is in another sequence). Each email body is 90 to 120 words, one sourced fact, one question, no em dashes.

### object · PF Hand-off
Every hand-off as a saved record: schema-checked, confidence-scored, keyed by Patch ID.
- record · seed · PF Hand-off: origin seed on every row; idempotency_key is account_id + person_id + play_id; model, cost_usd and latency_ms on every agent row. H-01 PATCH-NAE-03 A-1001 Fit Scorer to Account Ranking, fit score, confidence 92, threshold 70, passed, flowed. H-02 A-1001 Buying Signal Spotter to Account Ranking, signal S-01, 92, 70, passed, flowed. H-03 A-1001 Account Ranking to Gate 1, batch row, 100, 0, passed, flowed. H-04 A-1007 Gate 1 to Company Facts Collector, 100, passed, flowed. H-05 A-1001 Company Facts Collector to Case for Change Drafter, facts F-01 to F-04, 88, 0, passed, flowed. H-06 A-1001 Use Case Matcher to Case for Change Drafter, F-05 to F-07, 84, 70, passed, flowed. H-07 A-1002 Patch Suggester to RevOps, patch proposal, 74, 80, passed, waiting_person, assigned_to RevOps, reason "confidence 74 under 80". H-08 A-1001 Buying Team Mapper to Person Notes Writer, P-1001 to P-1013, 81, 70, passed, flowed. H-09 A-1001 Person Notes Writer to Message Writer, 83, 70, passed, flowed. H-10 A-1003 Case for Change Drafter to Play Picker, 77, 70, rejected, rejected, assigned_to GTM engineer, reason "schema check failed: evidence missing". H-11 A-1010 Buying Signal Spotter to Play Picker, fast lane S-08, 88, 70, passed, flowed. H-12 A-1001 Buying Team Mapper to Gate 2, role of P-1005, 66, 70, passed, waiting_person, assigned_to Marcus Ellery, reason "role confidence 66 under 70". H-13 A-1001 Message Writer to Fact Checker, D-01 to D-06, 85, 70, passed, flowed. H-14 A-1002 Current Vendor Finder to Renewal Date Finder, 58, 60, passed, late, reason "late 2h 10m, retried once". H-15 A-1001 Case for Change Drafter to Gate 2, F-10, 68, 70, passed, waiting_person, assigned_to Marcus Ellery, reason "confidence 68 under 70". H-16 A-1012 Meeting Labeler to AE confirm, new_buyer, 86, 80, passed, flowed. H-17 A-1013 Deal Qualifier to AE confirm, qualified, 90, 80, passed, flowed. H-18 A-1011 Current Vendor Finder to Battlecard Writer, 61, 60, passed, late, reason "late 3h 40m, retried twice".

### object · PF Component
The registry: 38 agents, 12 workflows, 5 human gates and 2 rule steps.
- record · seed · PF Component: origin seed on every row; every row of the file studio/data/components.csv (57 rows: 38 agents (30 agents, 6 checkers, 2 monitors), 12 workflows, 5 human gates, 2 rule steps), every column as the file gives it; C08 Current Vendor Finder carries success_rate 96.1 (red under 97).

### object · PF Seed snapshot
The seeded values the reset restores.
- record · seed · PF Seed snapshot: one row per row the seed lines above write (snapshot_id `object_id:record_id`, row_values the row as seeded, JSON), written once after the seeds, origin seed.


## Business rules
- Every seeded row carries origin seed.
- Seeds are fictional: invented companies and people, links under carrowvale.example, dates in the 90 days before the demo.
- A picklist stores its code, a date stores epoch ms.

## Ready when
- PF Patch holds every seed row its line lists.
- PF Account holds every seed row its line lists.
- PF Person holds every seed row its line lists.
- PF Signal holds every seed row its line lists.
- PF Fact holds every seed row its line lists.
- PF Draft holds every seed row its line lists.
- PF Hand-off holds every seed row its line lists.
- PF Component holds every seed row its line lists.
- PF Seed snapshot holds every seed row its line lists.

## Assumptions
- Check this: seed rows are fictional (invented companies and people, links under carrowvale.example), dates in the 90 days before the demo.
- Check this: PF Component rows are the 57 rows of studio/data/components.csv as given.
