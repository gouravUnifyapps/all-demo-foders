Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command platform" (e_6adb4b845236864dd8b18935)

```mermaid
flowchart LR
  n1["app ClickUp Delivery Command · app-f53fd0efccec"]
  n2["page global-page-of-app-f53fd0efccec · e_global_app-f53fd0efccec"]
  n3["data source Send executive summary · e_6adbb6845236864dd8edcd6b"]
  n4["data source Change request · e_6adbb56d925d282255d10fd5"]
  n5["data source Review timesheets · e_6adbb4b0925d282255d0fc9b"]
  n6["data source Book consultant · e_6adbb4b0925d282255d0fc96"]
  n7["data source Reschedule task · e_6adbb3ff0881d2257ad023b6"]
  n8["data source Move task · e_6adbb35b5236864dd8ed69d8"]
  n9["data source Save view · e_6adbb1ee0881d2257acff8f3"]
  n10["data source data_fetchOne_app-f53fd0efccec · e_6adbb1ed925d282255d0c00d"]
  n11["data source data_fetch_app-f53fd0efccec · e_6adbb1ed925d282255d0c00a"]
  n12["data source data_delete_app-f53fd0efccec · e_6adbb1ed0881d2257acff8ed"]
  n13["data source data_update_app-f53fd0efccec · e_6adbb1ed0881d2257acff8e9"]
  n14["data source data_create_app-f53fd0efccec · e_6adbb1ed0881d2257acff8e6"]
  n15["automation Delivery Command · Move task · 6adba2ac92718f6a64f34bc5"]
  n16["automation Delivery Command · Reschedule task · 6adba3266112da3e23fcf133"]
  n17["automation Delivery Command · Book consultant · 6adba3b292718f6a64f39440"]
  n18["automation Delivery Command · Review timesheets · 6adba402f4431f44e30943f1"]
  n19["automation Delivery Command · Log time · 6adba405ca4f9d2045858cfc"]
  n20["automation Delivery Command · Book training slot · 6adba59c92718f6a64f4015a"]
  n21["automation Delivery Command · Publish status report · 6adba5cfeb71d135d657c23d"]
  n22["automation Delivery Command · Record sign-off · 6adba5f8eb71d135d657e318"]
  n23["automation Delivery Command · Accept proposed tasks · 6adba625ca4f9d2045986507"]
  n24["automation Delivery Command · Change request · 6adba6a8cac0655fe3582da3"]
  n25["automation Delivery Command · Mark notification read · 6adba94deb71d135d658f2dc"]
  n26["automation Delivery Command · Confirm upload · 6adba9abcac0655fe35aa2fc"]
  n27["automation Delivery Command · Save view · 6adba9aef3cd5f19ed89eaec"]
  n28["automation Delivery Command · Update project settings · 6adba9def3cd5f19ed89ef7d"]
  n29["automation Delivery Command · Read delivery data · 6adbaa4fca4f9d20459bd303"]
  n30["automation Delivery Command · Send executive summary · 6adbac23eb71d135d65f4715"]
  n31["automation Delivery Command · Weekly executive email schedule · 6adbacd6f3cd5f19ed8a543a"]
  n32["automation Delivery Command · Ask Copilot · 6adbaf90c79cad11403e9b72"]
  n33["object Delivery Command · Task · OBJ_dcmd_task"]
  n34["object Delivery Command · Project · OBJ_dcmd_project"]
  n35["object Delivery Command · RAID item · OBJ_dcmd_raid"]
  n36["object Delivery Command · Booking · OBJ_dcmd_booking"]
  n37["object Delivery Command · Time entry · OBJ_dcmd_time_entry"]
  n38["object Delivery Command · Person · OBJ_dcmd_person"]
  n39["object Delivery Command · Change request · OBJ_dcmd_change_request"]
  n40["object Delivery Command · Document · OBJ_dcmd_document"]
  n41["object Delivery Command · Session slot · OBJ_dcmd_session_slot"]
  n42["object Delivery Command · Activity · OBJ_dcmd_activity"]
  n43["object Delivery Command · Sign-off · OBJ_dcmd_signoff"]
  n44["object Delivery Command · Checklist item · OBJ_dcmd_checklist_item"]
  n45["object Delivery Command · Notification · OBJ_dcmd_notification"]
  n46["object Delivery Command · Integration · OBJ_dcmd_integration"]
  n47["object Delivery Command · Saved view · OBJ_dcmd_saved_view"]
  n48["object Delivery Command · AI output · OBJ_dcmd_ai_output"]
  n49["object Delivery Command · Weekly snapshot · OBJ_dcmd_weekly_snapshot"]
  n50["object Delivery Command · Weekly metric · OBJ_dcmd_weekly_metric"]
  n51["object Delivery Command · Role permission · OBJ_dcmd_role_permission"]
  n52["object Delivery Command · Upload · OBJ_dcmd_upload"]
  n53["object Delivery Command · Executive email · OBJ_dcmd_exec_email"]
  n54["AI agent Delivery Command · Copilot · e_6adbabd2925d282255cee62b"]
  n55["object object_type · object_type"]
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
  n3 -->|data source| n30
  n4 -->|data source| n24
  n5 -->|data source| n18
  n6 -->|data source| n17
  n7 -->|data source| n16
  n8 -->|data source| n15
  n9 -->|data source| n27
  n10 -->|storage read| n55
  n11 -->|storage read| n55
  n12 -->|storage read| n55
  n13 -->|storage read| n55
  n14 -->|storage read| n55
  n15 -->|storage read| n33
  n15 -->|storage write| n33
  n15 -->|storage write| n42
  n16 -->|storage read| n33
  n16 -->|storage read| n34
  n16 -->|storage write| n33
  n16 -->|storage write| n34
  n16 -->|storage write| n42
  n17 -->|storage read| n38
  n17 -->|storage read| n34
  n17 -->|storage read| n36
  n17 -->|storage write| n36
  n17 -->|storage write| n42
  n18 -->|storage write| n37
  n18 -->|storage write| n42
  n19 -->|storage read| n33
  n19 -->|storage read| n38
  n19 -->|storage write| n37
  n19 -->|storage write| n33
  n19 -->|storage write| n42
  n20 -->|storage read| n41
  n20 -->|storage write| n41
  n21 -->|storage write| n48
  n21 -->|storage write| n42
  n22 -->|storage read| n43
  n22 -->|storage read| n34
  n22 -->|storage write| n43
  n22 -->|storage write| n42
  n22 -->|storage write| n45
  n23 -->|storage read| n48
  n23 -->|storage read| n34
  n23 -->|storage write| n33
  n23 -->|storage write| n48
  n24 -->|storage read| n39
  n24 -->|storage read| n34
  n24 -->|storage write| n39
  n24 -->|storage write| n42
  n24 -->|storage write| n33
  n24 -->|storage write| n34
  n25 -->|storage read| n45
  n25 -->|storage write| n45
  n26 -->|storage read| n34
  n26 -->|storage write| n52
  n26 -->|storage write| n42
  n27 -->|storage write| n47
  n28 -->|storage read| n34
  n28 -->|storage write| n34
  n28 -->|storage write| n42
  n29 -->|storage read| n34
  n29 -->|storage read| n33
  n29 -->|storage read| n35
  n29 -->|storage read| n36
  n29 -->|storage read| n38
  n29 -->|storage read| n37
  n29 -->|storage read| n43
  n29 -->|storage read| n48
  n29 -->|storage read| n49
  n30 -->|storage read| n50
  n30 -->|storage read| n49
  n30 -->|storage read| n34
  n30 -->|storage read| n42
  n30 -->|storage write| n53
  n31 -->|call node| n30
```
