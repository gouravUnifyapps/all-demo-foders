Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command dashboard" (e_6adf231a08f96579541331a5)

```mermaid
flowchart LR
  n1["automation ClickUp Command · Read delivery data · 6adf45fef3cd5f19ed4a76ba"]
  n2["automation ClickUp Command · Save view · 6adf460108750d257cf1e381"]
  n3["automation ClickUp Command · Update task · 6adf485af3cd5f19ed4ac683"]
  n4["automation ClickUp Command · Raise change request · 6adf485ec79cad1140a9e9a6"]
  n5["automation ClickUp Command · Decide change request · 6adf485ff3cd5f19ed4ac6fd"]
  n6["object ClickUp Command · Project · OBJ_cucmd_project"]
  n7["object ClickUp Command · RAID item · OBJ_cucmd_raid"]
  n8["object ClickUp Command · Task · OBJ_cucmd_task"]
  n9["object ClickUp Command · Time entry · OBJ_cucmd_time_entry"]
  n10["object ClickUp Command · Change request · OBJ_cucmd_change_request"]
  n11["object ClickUp Command · Person · OBJ_cucmd_person"]
  n12["object ClickUp Command · Booking · OBJ_cucmd_booking"]
  n13["object ClickUp Command · Deliverable · OBJ_cucmd_deliverable"]
  n14["object ClickUp Command · Session slot · OBJ_cucmd_session_slot"]
  n15["object ClickUp Command · Document · OBJ_cucmd_document"]
  n16["object ClickUp Command · Activity · OBJ_cucmd_activity"]
  n17["object ClickUp Command · AI output · OBJ_cucmd_ai_output"]
  n18["object ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric"]
  n19["object ClickUp Command · Saved view · OBJ_cucmd_saved_view"]
  n20["object ClickUp Command · Integration · OBJ_cucmd_integration"]
  n21["object ClickUp Command · Notification · OBJ_cucmd_notification"]
  n22["object ClickUp Command · Checklist item · OBJ_cucmd_checklist_item"]
  n1 -->|storage read| n6
  n1 -->|storage read| n8
  n1 -->|storage read| n7
  n1 -->|storage read| n12
  n1 -->|storage read| n11
  n1 -->|storage read| n10
  n1 -->|storage read| n17
  n1 -->|storage read| n18
  n1 -->|storage read| n15
  n2 -->|storage read| n19
  n2 -->|storage write| n19
  n3 -->|storage read| n8
  n3 -->|storage read| n6
  n3 -->|storage write| n8
  n3 -->|storage write| n16
  n4 -->|storage read| n6
  n4 -->|storage read| n10
  n4 -->|storage write| n10
  n4 -->|storage write| n16
  n5 -->|storage read| n10
  n5 -->|storage read| n6
  n5 -->|storage write| n10
  n5 -->|storage write| n6
  n5 -->|storage write| n16
```
