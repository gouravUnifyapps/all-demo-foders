Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command platform" (e_6adb4b845236864dd8b18935)

```mermaid
flowchart LR
  n1["app app-f53fd0efccec · app-f53fd0efccec"]
  n2["automation Delivery Command · Move task · 6adba2ac92718f6a64f34bc5"]
  n3["automation Delivery Command · Reschedule task · 6adba3266112da3e23fcf133"]
  n4["automation Delivery Command · Book consultant · 6adba3b292718f6a64f39440"]
  n5["automation Delivery Command · Review timesheets · 6adba402f4431f44e30943f1"]
  n6["automation Delivery Command · Log time · 6adba405ca4f9d2045858cfc"]
  n7["automation Delivery Command · Book training slot · 6adba59c92718f6a64f4015a"]
  n8["automation Delivery Command · Publish status report · 6adba5cfeb71d135d657c23d"]
  n9["automation Delivery Command · Record sign-off · 6adba5f8eb71d135d657e318"]
  n10["automation Delivery Command · Accept proposed tasks · 6adba625ca4f9d2045986507"]
  n11["automation Delivery Command · Change request · 6adba6a8cac0655fe3582da3"]
  n12["automation Delivery Command · Mark notification read · 6adba94deb71d135d658f2dc"]
  n13["automation Delivery Command · Confirm upload · 6adba9abcac0655fe35aa2fc"]
  n14["automation Delivery Command · Save view · 6adba9aef3cd5f19ed89eaec"]
  n15["automation Delivery Command · Update project settings · 6adba9def3cd5f19ed89ef7d"]
  n16["automation Delivery Command · Read delivery data · 6adbaa4fca4f9d20459bd303"]
  n17["automation Delivery Command · Send executive summary · 6adbac23eb71d135d65f4715"]
  n18["automation Delivery Command · Weekly executive email schedule · 6adbacd6f3cd5f19ed8a543a"]
  n19["automation Delivery Command · Ask Copilot · 6adbaf90c79cad11403e9b72"]
  n20["object Delivery Command · Task · OBJ_dcmd_task"]
  n21["object Delivery Command · Project · OBJ_dcmd_project"]
  n22["object Delivery Command · RAID item · OBJ_dcmd_raid"]
  n23["object Delivery Command · Booking · OBJ_dcmd_booking"]
  n24["object Delivery Command · Time entry · OBJ_dcmd_time_entry"]
  n25["object Delivery Command · Person · OBJ_dcmd_person"]
  n26["object Delivery Command · Change request · OBJ_dcmd_change_request"]
  n27["object Delivery Command · Document · OBJ_dcmd_document"]
  n28["object Delivery Command · Session slot · OBJ_dcmd_session_slot"]
  n29["object Delivery Command · Activity · OBJ_dcmd_activity"]
  n30["object Delivery Command · Sign-off · OBJ_dcmd_signoff"]
  n31["object Delivery Command · Checklist item · OBJ_dcmd_checklist_item"]
  n32["object Delivery Command · Notification · OBJ_dcmd_notification"]
  n33["object Delivery Command · Integration · OBJ_dcmd_integration"]
  n34["object Delivery Command · Saved view · OBJ_dcmd_saved_view"]
  n35["object Delivery Command · AI output · OBJ_dcmd_ai_output"]
  n36["object Delivery Command · Weekly snapshot · OBJ_dcmd_weekly_snapshot"]
  n37["object Delivery Command · Weekly metric · OBJ_dcmd_weekly_metric"]
  n38["object Delivery Command · Role permission · OBJ_dcmd_role_permission"]
  n39["object Delivery Command · Upload · OBJ_dcmd_upload"]
  n40["object Delivery Command · Executive email · OBJ_dcmd_exec_email"]
  n41["AI agent Delivery Command · Copilot · e_6adbabd2925d282255cee62b"]
  n2 -->|storage read| n20
  n2 -->|storage write| n20
  n2 -->|storage write| n29
  n3 -->|storage read| n20
  n3 -->|storage read| n21
  n3 -->|storage write| n20
  n3 -->|storage write| n21
  n3 -->|storage write| n29
  n4 -->|storage read| n25
  n4 -->|storage read| n21
  n4 -->|storage read| n23
  n4 -->|storage write| n23
  n4 -->|storage write| n29
  n5 -->|storage write| n24
  n5 -->|storage write| n29
  n6 -->|storage read| n20
  n6 -->|storage read| n25
  n6 -->|storage write| n24
  n6 -->|storage write| n20
  n6 -->|storage write| n29
  n7 -->|storage read| n28
  n7 -->|storage write| n28
  n8 -->|storage write| n35
  n8 -->|storage write| n29
  n9 -->|storage read| n30
  n9 -->|storage read| n21
  n9 -->|storage write| n30
  n9 -->|storage write| n29
  n9 -->|storage write| n32
  n10 -->|storage read| n35
  n10 -->|storage read| n21
  n10 -->|storage write| n20
  n10 -->|storage write| n35
  n11 -->|storage read| n26
  n11 -->|storage read| n21
  n11 -->|storage write| n26
  n11 -->|storage write| n29
  n11 -->|storage write| n20
  n11 -->|storage write| n21
  n12 -->|storage read| n32
  n12 -->|storage write| n32
  n13 -->|storage read| n21
  n13 -->|storage write| n39
  n13 -->|storage write| n29
  n14 -->|storage write| n34
  n15 -->|storage read| n21
  n15 -->|storage write| n21
  n15 -->|storage write| n29
  n16 -->|storage read| n21
  n16 -->|storage read| n20
  n16 -->|storage read| n22
  n16 -->|storage read| n23
  n16 -->|storage read| n25
  n16 -->|storage read| n24
  n16 -->|storage read| n30
  n16 -->|storage read| n35
  n16 -->|storage read| n36
  n17 -->|storage read| n37
  n17 -->|storage read| n36
  n17 -->|storage read| n21
  n17 -->|storage read| n29
  n17 -->|storage write| n40
  n18 -->|call node| n17
```
