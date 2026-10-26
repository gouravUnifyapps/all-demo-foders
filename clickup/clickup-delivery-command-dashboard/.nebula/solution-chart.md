Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command dashboard" (e_6adf231a08f96579541331a5)

```mermaid
flowchart LR
  n1["app app-a2a9509a82c1 · app-a2a9509a82c1"]
  n2["automation ClickUp Command · Read delivery data · 6adf45fef3cd5f19ed4a76ba"]
  n3["automation ClickUp Command · Save view · 6adf460108750d257cf1e381"]
  n4["automation ClickUp Command · Update task · 6adf485af3cd5f19ed4ac683"]
  n5["automation ClickUp Command · Raise change request · 6adf485ec79cad1140a9e9a6"]
  n6["automation ClickUp Command · Decide change request · 6adf485ff3cd5f19ed4ac6fd"]
  n7["automation ClickUp Command · Book consultant · 6adf4aa308750d257cf32534"]
  n8["automation ClickUp Command · Timesheet action · 6adf4aa9f3cd5f19ed4afa85"]
  n9["automation ClickUp Command · Portal action · 6adf4aaef3cd5f19ed4afc58"]
  n10["automation ClickUp Command · Accept proposed tasks · 6adf4d11f3cd5f19ed4b436a"]
  n11["automation ClickUp Command · Publish status report · 6adf4d1492718f6a64e5ca35"]
  n12["automation ClickUp Command · Send executive summary · 6adf4d1508750d257cf3df21"]
  n13["automation ClickUp Command · Update project settings · 6adf4eb5cac0655fe38aef9d"]
  n14["automation ClickUp Command · Mark notification read · 6adf4eb8cac0655fe38aefc9"]
  n15["object ClickUp Command · Project · OBJ_cucmd_project"]
  n16["object ClickUp Command · RAID item · OBJ_cucmd_raid"]
  n17["object ClickUp Command · Task · OBJ_cucmd_task"]
  n18["object ClickUp Command · Time entry · OBJ_cucmd_time_entry"]
  n19["object ClickUp Command · Change request · OBJ_cucmd_change_request"]
  n20["object ClickUp Command · Person · OBJ_cucmd_person"]
  n21["object ClickUp Command · Booking · OBJ_cucmd_booking"]
  n22["object ClickUp Command · Deliverable · OBJ_cucmd_deliverable"]
  n23["object ClickUp Command · Session slot · OBJ_cucmd_session_slot"]
  n24["object ClickUp Command · Document · OBJ_cucmd_document"]
  n25["object ClickUp Command · Activity · OBJ_cucmd_activity"]
  n26["object ClickUp Command · AI output · OBJ_cucmd_ai_output"]
  n27["object ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric"]
  n28["object ClickUp Command · Saved view · OBJ_cucmd_saved_view"]
  n29["object ClickUp Command · Integration · OBJ_cucmd_integration"]
  n30["object ClickUp Command · Notification · OBJ_cucmd_notification"]
  n31["object ClickUp Command · Checklist item · OBJ_cucmd_checklist_item"]
  n32["AI agent e_6adf4f02dc07493166ced9fa · e_6adf4f02dc07493166ced9fa"]
  n2 -->|storage read| n15
  n2 -->|storage read| n17
  n2 -->|storage read| n16
  n2 -->|storage read| n21
  n2 -->|storage read| n20
  n2 -->|storage read| n19
  n2 -->|storage read| n26
  n2 -->|storage read| n27
  n2 -->|storage read| n24
  n3 -->|storage read| n28
  n3 -->|storage write| n28
  n4 -->|storage read| n17
  n4 -->|storage read| n15
  n4 -->|storage write| n17
  n4 -->|storage write| n25
  n5 -->|storage read| n15
  n5 -->|storage read| n19
  n5 -->|storage write| n19
  n5 -->|storage write| n25
  n6 -->|storage read| n19
  n6 -->|storage read| n15
  n6 -->|storage write| n19
  n6 -->|storage write| n15
  n6 -->|storage write| n25
  n7 -->|storage read| n20
  n7 -->|storage read| n15
  n7 -->|storage read| n21
  n7 -->|storage write| n21
  n7 -->|storage write| n25
  n8 -->|storage read| n17
  n8 -->|storage write| n18
  n8 -->|storage write| n25
  n8 -->|storage read| n18
  n9 -->|storage read| n20
  n9 -->|storage read| n22
  n9 -->|storage write| n22
  n9 -->|storage write| n25
  n9 -->|storage read| n23
  n9 -->|storage write| n23
  n9 -->|storage read| n31
  n9 -->|storage write| n31
  n9 -->|storage read| n24
  n9 -->|storage write| n24
  n10 -->|storage read| n26
  n10 -->|storage write| n17
  n10 -->|storage write| n26
  n10 -->|storage write| n25
  n11 -->|storage read| n15
  n11 -->|storage write| n24
  n11 -->|storage write| n25
  n12 -->|storage read| n27
  n13 -->|storage read| n15
  n13 -->|storage write| n15
  n13 -->|storage write| n25
  n14 -->|storage read| n30
  n14 -->|storage write| n30
```
