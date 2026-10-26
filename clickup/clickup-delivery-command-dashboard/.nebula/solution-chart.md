Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command dashboard" (e_6adf231a08f96579541331a5)

```mermaid
flowchart LR
  n1["automation ClickUp Command · Read delivery data · 6adf45fef3cd5f19ed4a76ba"]
  n2["automation ClickUp Command · Save view · 6adf460108750d257cf1e381"]
  n3["automation ClickUp Command · Update task · 6adf485af3cd5f19ed4ac683"]
  n4["automation ClickUp Command · Raise change request · 6adf485ec79cad1140a9e9a6"]
  n5["automation ClickUp Command · Decide change request · 6adf485ff3cd5f19ed4ac6fd"]
  n6["automation ClickUp Command · Book consultant · 6adf4aa308750d257cf32534"]
  n7["automation ClickUp Command · Timesheet action · 6adf4aa9f3cd5f19ed4afa85"]
  n8["automation ClickUp Command · Portal action · 6adf4aaef3cd5f19ed4afc58"]
  n9["automation ClickUp Command · Accept proposed tasks · 6adf4d11f3cd5f19ed4b436a"]
  n10["automation ClickUp Command · Publish status report · 6adf4d1492718f6a64e5ca35"]
  n11["automation ClickUp Command · Send executive summary · 6adf4d1508750d257cf3df21"]
  n12["object ClickUp Command · Project · OBJ_cucmd_project"]
  n13["object ClickUp Command · RAID item · OBJ_cucmd_raid"]
  n14["object ClickUp Command · Task · OBJ_cucmd_task"]
  n15["object ClickUp Command · Time entry · OBJ_cucmd_time_entry"]
  n16["object ClickUp Command · Change request · OBJ_cucmd_change_request"]
  n17["object ClickUp Command · Person · OBJ_cucmd_person"]
  n18["object ClickUp Command · Booking · OBJ_cucmd_booking"]
  n19["object ClickUp Command · Deliverable · OBJ_cucmd_deliverable"]
  n20["object ClickUp Command · Session slot · OBJ_cucmd_session_slot"]
  n21["object ClickUp Command · Document · OBJ_cucmd_document"]
  n22["object ClickUp Command · Activity · OBJ_cucmd_activity"]
  n23["object ClickUp Command · AI output · OBJ_cucmd_ai_output"]
  n24["object ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric"]
  n25["object ClickUp Command · Saved view · OBJ_cucmd_saved_view"]
  n26["object ClickUp Command · Integration · OBJ_cucmd_integration"]
  n27["object ClickUp Command · Notification · OBJ_cucmd_notification"]
  n28["object ClickUp Command · Checklist item · OBJ_cucmd_checklist_item"]
  n1 -->|storage read| n12
  n1 -->|storage read| n14
  n1 -->|storage read| n13
  n1 -->|storage read| n18
  n1 -->|storage read| n17
  n1 -->|storage read| n16
  n1 -->|storage read| n23
  n1 -->|storage read| n24
  n1 -->|storage read| n21
  n2 -->|storage read| n25
  n2 -->|storage write| n25
  n3 -->|storage read| n14
  n3 -->|storage read| n12
  n3 -->|storage write| n14
  n3 -->|storage write| n22
  n4 -->|storage read| n12
  n4 -->|storage read| n16
  n4 -->|storage write| n16
  n4 -->|storage write| n22
  n5 -->|storage read| n16
  n5 -->|storage read| n12
  n5 -->|storage write| n16
  n5 -->|storage write| n12
  n5 -->|storage write| n22
  n6 -->|storage read| n17
  n6 -->|storage read| n12
  n6 -->|storage read| n18
  n6 -->|storage write| n18
  n6 -->|storage write| n22
  n7 -->|storage read| n14
  n7 -->|storage write| n15
  n7 -->|storage write| n22
  n7 -->|storage read| n15
  n8 -->|storage read| n17
  n8 -->|storage read| n19
  n8 -->|storage write| n19
  n8 -->|storage write| n22
  n8 -->|storage read| n20
  n8 -->|storage write| n20
  n8 -->|storage read| n28
  n8 -->|storage write| n28
  n8 -->|storage read| n21
  n8 -->|storage write| n21
  n9 -->|storage read| n23
  n9 -->|storage write| n14
  n9 -->|storage write| n23
  n9 -->|storage write| n22
  n10 -->|storage read| n12
  n10 -->|storage write| n21
  n10 -->|storage write| n22
  n11 -->|storage read| n24
```
