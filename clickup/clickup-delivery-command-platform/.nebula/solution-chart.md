Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command platform" (e_6adb4b845236864dd8b18935)

```mermaid
flowchart LR
  n1["app ClickUp Delivery Command · app-f53fd0efccec"]
  n2["page global-page-of-app-f53fd0efccec · e_global_app-f53fd0efccec"]
  n3["data source Update project settings · e_6adf07466e8cff53fad1c683"]
  n4["data source Mark notification read · e_6adf0696bc76624e532e8420"]
  n5["data source Log time · e_6adf0696bc76624e532e841b"]
  n6["data source Confirm upload · e_6adf05bcbae51e4d7ab2148e"]
  n7["data source Book training slot · e_6adf04a5bae51e4d7ab1fb2f"]
  n8["data source Record sign-off · e_6adf04a56e8cff53fad18032"]
  n9["data source Accept proposed tasks · e_6adf038ebae51e4d7ab1dc7c"]
  n10["data source Publish status report · e_6adf038dbae51e4d7ab1dc78"]
  n11["data source Ask Copilot · e_6adf038d6e8cff53fad16a63"]
  n12["data source Send executive summary · e_6adbb6845236864dd8edcd6b"]
  n13["data source Change request · e_6adbb56d925d282255d10fd5"]
  n14["data source Review timesheets · e_6adbb4b0925d282255d0fc9b"]
  n15["data source Book consultant · e_6adbb4b0925d282255d0fc96"]
  n16["data source Reschedule task · e_6adbb3ff0881d2257ad023b6"]
  n17["data source Move task · e_6adbb35b5236864dd8ed69d8"]
  n18["data source Save view · e_6adbb1ee0881d2257acff8f3"]
  n19["data source data_fetchOne_app-f53fd0efccec · e_6adbb1ed925d282255d0c00d"]
  n20["data source data_fetch_app-f53fd0efccec · e_6adbb1ed925d282255d0c00a"]
  n21["data source data_delete_app-f53fd0efccec · e_6adbb1ed0881d2257acff8ed"]
  n22["data source data_update_app-f53fd0efccec · e_6adbb1ed0881d2257acff8e9"]
  n23["data source data_create_app-f53fd0efccec · e_6adbb1ed0881d2257acff8e6"]
  n24["automation Delivery Command · Move task · 6adba2ac92718f6a64f34bc5"]
  n25["automation Delivery Command · Reschedule task · 6adba3266112da3e23fcf133"]
  n26["automation Delivery Command · Book consultant · 6adba3b292718f6a64f39440"]
  n27["automation Delivery Command · Review timesheets · 6adba402f4431f44e30943f1"]
  n28["automation Delivery Command · Log time · 6adba405ca4f9d2045858cfc"]
  n29["automation Delivery Command · Book training slot · 6adba59c92718f6a64f4015a"]
  n30["automation Delivery Command · Publish status report · 6adba5cfeb71d135d657c23d"]
  n31["automation Delivery Command · Record sign-off · 6adba5f8eb71d135d657e318"]
  n32["automation Delivery Command · Accept proposed tasks · 6adba625ca4f9d2045986507"]
  n33["automation Delivery Command · Change request · 6adba6a8cac0655fe3582da3"]
  n34["automation Delivery Command · Mark notification read · 6adba94deb71d135d658f2dc"]
  n35["automation Delivery Command · Confirm upload · 6adba9abcac0655fe35aa2fc"]
  n36["automation Delivery Command · Save view · 6adba9aef3cd5f19ed89eaec"]
  n37["automation Delivery Command · Update project settings · 6adba9def3cd5f19ed89ef7d"]
  n38["automation Delivery Command · Read delivery data · 6adbaa4fca4f9d20459bd303"]
  n39["automation Delivery Command · Send executive summary · 6adbac23eb71d135d65f4715"]
  n40["automation Delivery Command · Weekly executive email schedule · 6adbacd6f3cd5f19ed8a543a"]
  n41["automation Delivery Command · Ask Copilot · 6adbaf90c79cad11403e9b72"]
  n42["object Delivery Command · Task · OBJ_dcmd_task"]
  n43["object Delivery Command · Project · OBJ_dcmd_project"]
  n44["object Delivery Command · RAID item · OBJ_dcmd_raid"]
  n45["object Delivery Command · Booking · OBJ_dcmd_booking"]
  n46["object Delivery Command · Time entry · OBJ_dcmd_time_entry"]
  n47["object Delivery Command · Person · OBJ_dcmd_person"]
  n48["object Delivery Command · Change request · OBJ_dcmd_change_request"]
  n49["object Delivery Command · Document · OBJ_dcmd_document"]
  n50["object Delivery Command · Session slot · OBJ_dcmd_session_slot"]
  n51["object Delivery Command · Activity · OBJ_dcmd_activity"]
  n52["object Delivery Command · Sign-off · OBJ_dcmd_signoff"]
  n53["object Delivery Command · Checklist item · OBJ_dcmd_checklist_item"]
  n54["object Delivery Command · Notification · OBJ_dcmd_notification"]
  n55["object Delivery Command · Integration · OBJ_dcmd_integration"]
  n56["object Delivery Command · Saved view · OBJ_dcmd_saved_view"]
  n57["object Delivery Command · AI output · OBJ_dcmd_ai_output"]
  n58["object Delivery Command · Weekly snapshot · OBJ_dcmd_weekly_snapshot"]
  n59["object Delivery Command · Weekly metric · OBJ_dcmd_weekly_metric"]
  n60["object Delivery Command · Role permission · OBJ_dcmd_role_permission"]
  n61["object Delivery Command · Upload · OBJ_dcmd_upload"]
  n62["object Delivery Command · Executive email · OBJ_dcmd_exec_email"]
  n63["AI agent Delivery Command · Copilot · e_6adbabd2925d282255cee62b"]
  n64["object object_type · object_type"]
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
  n2 --- n15
  n2 --- n16
  n2 --- n17
  n2 --- n18
  n2 --- n19
  n2 --- n20
  n2 --- n21
  n2 --- n22
  n2 --- n23
  n3 -->|data source| n37
  n4 -->|data source| n34
  n5 -->|data source| n28
  n6 -->|data source| n35
  n7 -->|data source| n29
  n8 -->|data source| n31
  n9 -->|data source| n32
  n10 -->|data source| n30
  n11 -->|data source| n41
  n12 -->|data source| n39
  n13 -->|data source| n33
  n14 -->|data source| n27
  n15 -->|data source| n26
  n16 -->|data source| n25
  n17 -->|data source| n24
  n18 -->|data source| n36
  n19 -->|storage read| n64
  n20 -->|storage read| n64
  n21 -->|storage read| n64
  n22 -->|storage read| n64
  n23 -->|storage read| n64
  n24 -->|storage read| n42
  n24 -->|storage write| n42
  n24 -->|storage write| n51
  n25 -->|storage read| n42
  n25 -->|storage read| n43
  n25 -->|storage write| n42
  n25 -->|storage write| n43
  n25 -->|storage write| n51
  n26 -->|storage read| n47
  n26 -->|storage read| n43
  n26 -->|storage read| n45
  n26 -->|storage write| n45
  n26 -->|storage write| n51
  n27 -->|storage write| n46
  n27 -->|storage write| n51
  n28 -->|storage read| n42
  n28 -->|storage read| n47
  n28 -->|storage write| n46
  n28 -->|storage write| n42
  n28 -->|storage write| n51
  n29 -->|storage read| n50
  n29 -->|storage write| n50
  n30 -->|storage write| n57
  n30 -->|storage write| n51
  n31 -->|storage read| n52
  n31 -->|storage read| n43
  n31 -->|storage write| n52
  n31 -->|storage write| n51
  n31 -->|storage write| n54
  n32 -->|storage read| n57
  n32 -->|storage read| n43
  n32 -->|storage write| n42
  n32 -->|storage write| n57
  n33 -->|storage read| n48
  n33 -->|storage read| n43
  n33 -->|storage write| n48
  n33 -->|storage write| n51
  n33 -->|storage write| n42
  n33 -->|storage write| n43
  n34 -->|storage read| n54
  n34 -->|storage write| n54
  n35 -->|storage read| n43
  n35 -->|storage write| n61
  n35 -->|storage write| n51
  n36 -->|storage write| n56
  n37 -->|storage read| n43
  n37 -->|storage write| n43
  n37 -->|storage write| n51
  n38 -->|storage read| n43
  n38 -->|storage read| n42
  n38 -->|storage read| n44
  n38 -->|storage read| n45
  n38 -->|storage read| n47
  n38 -->|storage read| n46
  n38 -->|storage read| n52
  n38 -->|storage read| n57
  n38 -->|storage read| n58
  n39 -->|storage read| n59
  n39 -->|storage read| n58
  n39 -->|storage read| n43
  n39 -->|storage read| n51
  n39 -->|storage write| n62
  n40 -->|call node| n39
```
