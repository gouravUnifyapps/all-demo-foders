Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command platform" (e_6adb4b845236864dd8b18935)

```mermaid
flowchart LR
  n1["automation Delivery Command · Move task · 6adba2ac92718f6a64f34bc5"]
  n2["automation Delivery Command · Reschedule task · 6adba3266112da3e23fcf133"]
  n3["automation Delivery Command · Book consultant · 6adba3b292718f6a64f39440"]
  n4["automation Delivery Command · Review timesheets · 6adba402f4431f44e30943f1"]
  n5["automation Delivery Command · Log time · 6adba405ca4f9d2045858cfc"]
  n6["object Delivery Command · Task · OBJ_dcmd_task"]
  n7["object Delivery Command · Project · OBJ_dcmd_project"]
  n8["object Delivery Command · RAID item · OBJ_dcmd_raid"]
  n9["object Delivery Command · Booking · OBJ_dcmd_booking"]
  n10["object Delivery Command · Time entry · OBJ_dcmd_time_entry"]
  n11["object Delivery Command · Person · OBJ_dcmd_person"]
  n12["object Delivery Command · Change request · OBJ_dcmd_change_request"]
  n13["object Delivery Command · Document · OBJ_dcmd_document"]
  n14["object Delivery Command · Session slot · OBJ_dcmd_session_slot"]
  n15["object Delivery Command · Activity · OBJ_dcmd_activity"]
  n16["object Delivery Command · Sign-off · OBJ_dcmd_signoff"]
  n17["object Delivery Command · Checklist item · OBJ_dcmd_checklist_item"]
  n18["object Delivery Command · Notification · OBJ_dcmd_notification"]
  n19["object Delivery Command · Integration · OBJ_dcmd_integration"]
  n20["object Delivery Command · Saved view · OBJ_dcmd_saved_view"]
  n21["object Delivery Command · AI output · OBJ_dcmd_ai_output"]
  n22["object Delivery Command · Weekly snapshot · OBJ_dcmd_weekly_snapshot"]
  n23["object Delivery Command · Weekly metric · OBJ_dcmd_weekly_metric"]
  n24["object Delivery Command · Role permission · OBJ_dcmd_role_permission"]
  n25["object Delivery Command · Upload · OBJ_dcmd_upload"]
  n26["object Delivery Command · Executive email · OBJ_dcmd_exec_email"]
  n1 -->|storage read| n6
  n1 -->|storage write| n6
  n1 -->|storage write| n15
  n2 -->|storage read| n6
  n2 -->|storage read| n7
  n2 -->|storage write| n6
  n2 -->|storage write| n7
  n2 -->|storage write| n15
  n3 -->|storage read| n11
  n3 -->|storage read| n7
  n3 -->|storage read| n9
  n3 -->|storage write| n9
  n3 -->|storage write| n15
  n4 -->|storage write| n10
  n4 -->|storage write| n15
  n5 -->|storage read| n6
  n5 -->|storage read| n11
  n5 -->|storage write| n10
  n5 -->|storage write| n6
  n5 -->|storage write| n15
```
