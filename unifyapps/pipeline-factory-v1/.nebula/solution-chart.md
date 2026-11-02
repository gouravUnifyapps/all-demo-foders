Tenant orbit.uat.unifyapps.com · solution "UnifyApps · Pipeline Factory v1" (e_6ae5bfc3b4f0d14b27962a04)

```mermaid
flowchart LR
  n1["app UnifyApps Pipeline Factory Control Tower · app-2fbe93e8c1f7"]
  n2["page global-page-of-app-2fbe93e8c1f7 · e_global_app-2fbe93e8c1f7"]
  n3["data source Pause component · e_6ae849e0afe7fc590a1c44d8"]
  n4["data source Book meeting · e_6ae849dfd96c5f6ba22ff4e0"]
  n5["data source Clear Gate 2 · e_6ae849dfd96c5f6ba22ff4dc"]
  n6["data source Ask the analyst · e_6ae849dfafe7fc590a1c44d4"]
  n7["data source Decide Gate 1 · e_6ae84964d96c5f6ba22bd626"]
  n8["data source data_delete_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bb9"]
  n9["data source data_update_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bb5"]
  n10["data source data_create_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bb2"]
  n11["data source data_fetchOne_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1bad"]
  n12["data source data_fetch_app-2fbe93e8c1f7 · e_6ae84846f410ab7b2ffc1ba8"]
  n13["data source Log signal · e_6ae84846d96c5f6ba22bb5f0"]
  n14["automation Pipeline Factory · Save hand-off · 6ae840a5fbdd550a9a44c524"]
  n15["automation Pipeline Factory · Clear Gate 2 · 6ae840d7f6f76639f8ceb67d"]
  n16["automation Pipeline Factory · Log signal · 6ae843cc9594aa458cba14d7"]
  n17["automation Pipeline Factory · Pause component · 6ae843d1f6f76639f8cf2d55"]
  n18["automation Pipeline Factory · Read factory records · 6ae843e69ec43c6ee2dec988"]
  n19["automation Pipeline Factory · Decide Gate 1 · 6ae8440df13e536c52c5d959"]
  n20["automation Pipeline Factory · Reset demo · 6ae8441df38e327618fcc13c"]
  n21["automation Pipeline Factory · Book meeting · 6ae84449f38e327618fcc640"]
  n22["automation Pipeline Factory · Ask the analyst · 6ae84900fbdd550a9a465807"]
  n23["object PF Patch · OBJ_pf_patch"]
  n24["object PF Account · OBJ_pf_account"]
  n25["object PF Person · OBJ_pf_person"]
  n26["object PF Signal · OBJ_pf_signal"]
  n27["object PF Fact · OBJ_pf_fact"]
  n28["object PF Draft · OBJ_pf_draft"]
  n29["object PF Hand-off · OBJ_pf_handoff"]
  n30["object PF Component · OBJ_pf_component"]
  n31["object PF Seed snapshot · OBJ_pf_seed_snapshot"]
  n32["object PF Component run · OBJ_pf_component_run"]
  n33["object PF Source · OBJ_pf_source"]
  n34["object PF Inbox · OBJ_pf_inbox"]
  n35["object PF Suppression · OBJ_pf_suppression"]
  n36["AI agent Pipeline Factory Analyst · e_6ae846ffd96c5f6ba22b98da"]
  n37["object object_type · object_type"]
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
  n3 -->|data source| n17
  n4 -->|data source| n21
  n5 -->|data source| n15
  n6 -->|data source| n22
  n7 -->|data source| n19
  n8 -->|storage read| n37
  n9 -->|storage read| n37
  n10 -->|storage read| n37
  n11 -->|storage read| n37
  n12 -->|storage read| n37
  n13 -->|data source| n16
  n14 -->|storage read| n30
  n14 -->|storage write| n29
  n14 -->|storage read| n29
  n15 -->|storage read| n28
  n15 -->|storage write| n28
  n15 -->|storage read| n24
  n15 -->|storage read| n25
  n16 -->|storage read| n24
  n16 -->|storage read| n26
  n16 -->|storage write| n26
  n16 -->|storage write| n24
  n16 -->|call node| n14
  n17 -->|storage read| n30
  n17 -->|storage write| n30
  n17 -->|storage write| n29
  n18 -->|storage read| n23
  n18 -->|storage read| n24
  n18 -->|storage read| n29
  n18 -->|storage read| n30
  n18 -->|storage read| n25
  n19 -->|storage read| n24
  n19 -->|storage write| n24
  n19 -->|call node| n14
  n19 -->|storage read| n23
  n19 -->|storage write| n23
  n20 -->|storage write| n23
  n20 -->|storage write| n24
  n20 -->|storage write| n25
  n20 -->|storage write| n26
  n20 -->|storage write| n27
  n20 -->|storage write| n28
  n20 -->|storage write| n29
  n20 -->|storage write| n30
  n20 -->|storage write| n31
  n20 -->|storage read| n31
  n20 -->|storage read| n23
  n20 -->|storage read| n24
  n20 -->|storage read| n25
  n20 -->|storage read| n26
  n20 -->|storage read| n27
  n20 -->|storage read| n28
  n20 -->|storage read| n29
  n20 -->|storage read| n30
  n21 -->|storage read| n24
  n21 -->|storage write| n24
  n21 -->|call node| n14
```
