Tenant orbit.uat.unifyapps.com · solution "UnifyApps · Pipeline Factory v1" (e_6ae5bfc3b4f0d14b27962a04)

```mermaid
flowchart LR
  n1["app UnifyApps Pipeline Factory Control Tower · app-2fbe93e8c1f7"]
  n2["page global-page-of-app-2fbe93e8c1f7 · e_global_app-2fbe93e8c1f7"]
  n3["data source Run component · e_6ae8728cf410ab7b2f211dfe"]
  n4["data source Pause component · e_6ae849e0afe7fc590a1c44d8"]
  n5["data source Book meeting · e_6ae849dfd96c5f6ba22ff4e0"]
  n6["data source Clear Gate 2 · e_6ae849dfd96c5f6ba22ff4dc"]
  n7["data source Ask the analyst · e_6ae849dfafe7fc590a1c44d4"]
  n8["data source Decide Gate 1 · e_6ae84964d96c5f6ba22bd626"]
  n9["data source data_delete_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bb9"]
  n10["data source data_update_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bb5"]
  n11["data source data_create_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bb2"]
  n12["data source data_fetchOne_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bad"]
  n13["data source data_fetch_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1ba8"]
  n14["data source Log signal · e_6ae84846d96c5f6ba22bb5f0"]
  n15["automation Pipeline Factory · Save hand-off · 6ae840a5fbdd550a9a44c524"]
  n16["automation Pipeline Factory · Clear Gate 2 · 6ae840d7f6f76639f8ceb67d"]
  n17["automation Pipeline Factory · Log signal · 6ae843cc9594aa458cba14d7"]
  n18["automation Pipeline Factory · Pause component · 6ae843d1f6f76639f8cf2d55"]
  n19["automation Pipeline Factory · Read factory records · 6ae843e69ec43c6ee2dec988"]
  n20["automation Pipeline Factory · Decide Gate 1 · 6ae8440df13e536c52c5d959"]
  n21["automation Pipeline Factory · Reset demo · 6ae8441df38e327618fcc13c"]
  n22["automation Pipeline Factory · Book meeting · 6ae84449f38e327618fcc640"]
  n23["automation Pipeline Factory · Ask the analyst · 6ae84900fbdd550a9a465807"]
  n24["automation Pipeline Factory · Contact Finder · 6ae862f3f13e536c52e76ecd"]
  n25["automation Pipeline Factory · Alarm and Escalation · 6ae863282099302ffb2cf702"]
  n26["automation Pipeline Factory · Account Ranking · 6ae8632c9ec43c6ee22f380d"]
  n27["automation Pipeline Factory · Read component inputs · 6ae8635446920244f3d5194b"]
  n28["automation Pipeline Factory · Send Rules Check · 6ae863842099302ffb2d0262"]
  n29["automation Pipeline Factory · Weekly Slot Planner · 6ae863a5f38e327618183dca"]
  n30["automation Pipeline Factory · Content Handoff · 6ae863d0fbdd550a9a4ffc58"]
  n31["automation Pipeline Factory · Reset agent runs · 6ae863f02099302ffb2d2358"]
  n32["automation Pipeline Factory · Holdout Picker · 6ae864059ec43c6ee22f8008"]
  n33["automation Pipeline Factory · Email Domain Swapper · 6ae864342099302ffb2d2a71"]
  n34["automation Pipeline Factory · Do-Not-Contact List · 6ae864672099302ffb2d3157"]
  n35["automation Pipeline Factory · Save agent output · 6ae864829594aa458cc1ce69"]
  n36["automation Pipeline Factory · Outreach Launcher · 6ae864929594aa458cc23de9"]
  n37["automation Pipeline Factory · Privacy and Consent · 6ae86493f38e32761818a2c1"]
  n38["automation Pipeline Factory · Run component · 6ae865229ec43c6ee2300d8d"]
  n39["automation Pipeline Factory · Meeting Handoff and Deadlines · 6ae8654d2099302ffb2d9514"]
  n40["object PF Patch · OBJ_pf_patch"]
  n41["object PF Account · OBJ_pf_account"]
  n42["object PF Person · OBJ_pf_person"]
  n43["object PF Signal · OBJ_pf_signal"]
  n44["object PF Fact · OBJ_pf_fact"]
  n45["object PF Draft · OBJ_pf_draft"]
  n46["object PF Hand-off · OBJ_pf_handoff"]
  n47["object PF Component · OBJ_pf_component"]
  n48["object PF Seed snapshot · OBJ_pf_seed_snapshot"]
  n49["object PF Component run · OBJ_pf_component_run"]
  n50["object PF Source · OBJ_pf_source"]
  n51["object PF Inbox · OBJ_pf_inbox"]
  n52["object PF Suppression · OBJ_pf_suppression"]
  n53["AI agent Pipeline Factory Analyst · e_6ae846ffd96c5f6ba22b98da"]
  n54["AI agent PF · Fit Scorer · e_6ae86666d96c5f6ba243ce26"]
  n55["AI agent PF · Patch Suggester · e_6ae8666ad96c5f6ba243ce39"]
  n56["AI agent PF · Current Vendor Finder · e_6ae8666dafe7fc590a4a3d96"]
  n57["AI agent PF · Renewal Date Finder · e_6ae86671d96c5f6ba243ce77"]
  n58["AI agent PF · Battlecard Writer · e_6ae86673afe7fc590a4a3dda"]
  n59["AI agent PF · Buying Signal Spotter · e_6ae8667ed96c5f6ba243cf29"]
  n60["AI agent PF · Duplicate Finder · e_6ae86680afe7fc590a4a3f53"]
  n61["AI agent PF · Company Facts Collector · e_6ae86682d96c5f6ba243cf48"]
  n62["AI agent PF · Parent Company Linker · e_6ae86684d96c5f6ba243cf6a"]
  n63["AI agent PF · Use Case Matcher · e_6ae86685f410ab7b2f151b2f"]
  n64["AI agent PF · Headquarters Finder · e_6ae86687d96c5f6ba243cfb8"]
  n65["AI agent PF · Case for Change Drafter · e_6ae86689d96c5f6ba243cfd8"]
  n66["AI agent PF · Headquarters Re-checker · e_6ae8668bafe7fc590a4a3fec"]
  n67["AI agent PF · New Account Finder · e_6ae8668ef410ab7b2f151c47"]
  n68["AI agent PF · Buying Team Mapper · e_6ae867cdafe7fc590a4f8e82"]
  n69["AI agent PF · Person Notes Writer · e_6ae867d2f410ab7b2f155861"]
  n70["AI agent PF · Intro Finder · e_6ae867d4f410ab7b2f155959"]
  n71["AI agent PF · Play Picker · e_6ae86821f410ab7b2f15695c"]
  n72["AI agent PF · Page Builder · e_6ae86825f410ab7b2f156a03"]
  n73["AI agent PF · Content Picker · e_6ae86828f410ab7b2f156a22"]
  n74["AI agent PF · Message Writer · e_6ae8682ad96c5f6ba2441a16"]
  n75["AI agent PF · Fact Checker · e_6ae8682ed96c5f6ba2441a5f"]
  n76["AI agent PF · Message Grader · e_6ae8687bd96c5f6ba2442526"]
  n77["AI agent PF · Call Script Writer · e_6ae8687ef410ab7b2f1575c6"]
  n78["AI agent PF · Follow-up Planner · e_6ae86881d96c5f6ba244257b"]
  n79["AI agent PF · Inbox Health Checker · e_6ae86884d96c5f6ba24425cc"]
  n80["AI agent PF · Winning Message Finder · e_6ae86bd2afe7fc590a500c5f"]
  n81["AI agent PF · Scoring Tuner · e_6ae86bd6afe7fc590a500cfa"]
  n82["AI agent PF · Objection Collector · e_6ae86bd8f410ab7b2f202521"]
  n83["AI agent PF · A/B Tester · e_6ae86bdbf410ab7b2f202568"]
  n84["AI agent PF · Quality Grader · e_6ae86bdeafe7fc590a500d57"]
  n85["AI agent PF · Reply Sorter · e_6ae86bebf410ab7b2f20260c"]
  n86["AI agent PF · Reply Writer · e_6ae86beff410ab7b2f20266c"]
  n87["AI agent PF · Meeting Prep Writer · e_6ae86bf3f410ab7b2f2026ba"]
  n88["AI agent PF · Meeting Labeler · e_6ae86bf7f410ab7b2f202726"]
  n89["AI agent PF · Deal Qualifier · e_6ae86bfbf410ab7b2f202747"]
  n90["AI agent PF · Agent Monitor · e_6ae86c76f410ab7b2f203900"]
  n91["AI agent PF · Test Error Planter · e_6ae86c7ad96c5f6ba24493ba"]
  n92["object object_type · object_type"]
  n1 --- n2
  n2 --- n3
  n2 --- n4
  n2 --- n5
  n2 --- n6
  n2 --- n7
  n2 --- n8
  n2 --- n9
  n2 --- n10
  n2 --- n11
  n2 --- n12
  n2 --- n13
  n2 --- n14
  n3 -->|data source| n38
  n4 -->|data source| n18
  n5 -->|data source| n22
  n6 -->|data source| n16
  n7 -->|data source| n23
  n8 -->|data source| n20
  n9 -->|storage read| n92
  n10 -->|storage read| n92
  n11 -->|storage read| n92
  n12 -->|storage read| n92
  n13 -->|storage read| n92
  n14 -->|data source| n17
  n15 -->|storage read| n47
  n15 -->|storage write| n46
  n15 -->|storage read| n46
  n16 -->|storage read| n45
  n16 -->|storage write| n45
  n16 -->|storage read| n41
  n16 -->|storage read| n42
  n17 -->|storage read| n41
  n17 -->|storage read| n43
  n17 -->|storage write| n43
  n17 -->|storage write| n41
  n17 -->|call node| n15
  n18 -->|storage read| n47
  n18 -->|storage write| n47
  n18 -->|storage write| n46
  n19 -->|storage read| n40
  n19 -->|storage read| n41
  n19 -->|storage read| n46
  n19 -->|storage read| n47
  n19 -->|storage read| n42
  n20 -->|storage read| n41
  n20 -->|storage write| n41
  n20 -->|call node| n15
  n20 -->|storage read| n40
  n20 -->|storage write| n40
  n21 -->|storage write| n40
  n21 -->|storage write| n41
  n21 -->|storage write| n42
  n21 -->|storage write| n43
  n21 -->|storage write| n44
  n21 -->|storage write| n45
  n21 -->|storage write| n46
  n21 -->|storage write| n47
  n21 -->|storage write| n48
  n21 -->|storage read| n48
  n21 -->|storage read| n40
  n21 -->|storage read| n41
  n21 -->|storage read| n42
  n21 -->|storage read| n43
  n21 -->|storage read| n44
  n21 -->|storage read| n45
  n21 -->|storage read| n46
  n21 -->|storage read| n47
  n21 -->|call node| n31
  n22 -->|storage read| n41
  n22 -->|storage write| n41
  n22 -->|call node| n15
  n24 -->|storage read| n41
  n24 -->|storage read| n42
  n24 -->|storage read| n50
  n24 -->|storage read| n52
  n24 -->|storage write| n42
  n24 -->|storage write| n50
  n24 -->|storage write| n49
  n25 -->|storage read| n47
  n25 -->|storage read| n40
  n25 -->|storage read| n46
  n25 -->|storage read| n49
  n25 -->|call node| n18
  n25 -->|storage write| n49
  n25 -->|call node| n15
  n26 -->|storage read| n40
  n26 -->|storage read| n41
  n26 -->|storage read| n43
  n26 -->|storage write| n41
  n26 -->|call node| n15
  n26 -->|storage write| n49
  n27 -->|storage read| n47
  n27 -->|storage read| n41
  n27 -->|storage read| n42
  n27 -->|storage read| n43
  n27 -->|storage read| n44
  n27 -->|storage read| n45
  n27 -->|storage read| n50
  n27 -->|storage read| n46
  n27 -->|storage read| n51
  n27 -->|storage read| n52
  n27 -->|storage read| n49
  n28 -->|storage read| n45
  n28 -->|storage read| n41
  n28 -->|storage read| n42
  n28 -->|storage read| n52
  n28 -->|storage read| n51
  n28 -->|storage write| n49
  n29 -->|storage read| n40
  n29 -->|storage write| n40
  n29 -->|storage write| n49
  n30 -->|storage read| n40
  n30 -->|storage read| n41
  n30 -->|storage read| n42
  n30 -->|storage read| n45
  n30 -->|storage read| n50
  n30 -->|storage write| n41
  n30 -->|storage write| n49
  n31 -->|storage write| n49
  n31 -->|storage write| n50
  n31 -->|storage write| n51
  n31 -->|storage write| n52
  n31 -->|storage read| n48
  n31 -->|storage read| n49
  n31 -->|storage read| n50
  n31 -->|storage read| n51
  n31 -->|storage read| n52
  n32 -->|storage write| n49
  n32 -->|storage read| n41
  n32 -->|storage write| n41
  n33 -->|storage read| n51
  n33 -->|storage write| n51
  n33 -->|storage write| n49
  n34 -->|storage read| n42
  n34 -->|storage read| n52
  n34 -->|storage write| n52
  n34 -->|storage write| n42
  n34 -->|storage write| n49
  n35 -->|storage read| n47
  n35 -->|storage read| n41
  n35 -->|storage read| n42
  n35 -->|storage read| n45
  n35 -->|storage read| n51
  n35 -->|storage read| n49
  n35 -->|storage write| n41
  n35 -->|storage write| n42
  n35 -->|storage write| n45
  n35 -->|storage write| n51
  n35 -->|storage write| n43
  n35 -->|storage write| n44
  n35 -->|call node| n15
  n35 -->|storage write| n46
  n35 -->|storage write| n49
  n36 -->|storage read| n41
  n36 -->|storage read| n45
  n36 -->|storage read| n42
  n36 -->|storage read| n51
  n36 -->|storage read| n49
  n36 -->|storage write| n51
  n36 -->|storage write| n49
  n37 -->|storage read| n41
  n37 -->|storage read| n42
  n37 -->|storage read| n52
  n37 -->|storage read| n50
  n37 -->|storage read| n45
  n37 -->|call node| n34
  n37 -->|storage write| n49
  n38 -->|storage read| n47
  n38 -->|storage read| n49
  n38 -->|storage write| n49
  n38 -->|storage read| n41
  n38 -->|call node| n26
  n38 -->|call node| n29
  n38 -->|call node| n32
  n38 -->|call node| n24
  n38 -->|call node| n34
  n38 -->|call node| n28
  n38 -->|call node| n36
  n38 -->|call node| n33
  n38 -->|call node| n39
  n38 -->|call node| n25
  n38 -->|call node| n30
  n38 -->|call node| n37
  n39 -->|storage read| n41
  n39 -->|storage read| n50
  n39 -->|call node| n22
  n39 -->|call node| n15
  n39 -->|storage write| n49
```
