Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command dashboard" (e_6adf231a08f96579541331a5)

```mermaid
flowchart LR
  n1["app ClickUp Delivery Command · app-a2a9509a82c1"]
  n2["page global-page-of-app-a2a9509a82c1 · e_global_app-a2a9509a82c1"]
  n3["data source Timesheet action · e_6adf55a8769c8b649ebfe4a2"]
  n4["data source Book consultant · e_6adf55a8769c8b649ebfe49d"]
  n5["data source Decide change request · e_6adf552d08f965795443b4d9"]
  n6["data source Raise change request · e_6adf5341769c8b649ebfa6d9"]
  n7["data source Update project settings · e_6adf534108f96579544384bc"]
  n8["data source Update task · e_6adf5340769c8b649ebfa6d3"]
  n9["data source Send executive summary · e_6adf5087dc07493166cf01cb"]
  n10["data source data_update_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c8"]
  n11["data source data_fetchOne_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c5"]
  n12["data source data_fetch_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c2"]
  n13["data source Save view · e_6adf5087769c8b649ebf5ff2"]
  n14["data source data_delete_app-a2a9509a82c1 · e_6adf5087769c8b649ebf5fef"]
  n15["data source data_create_app-a2a9509a82c1 · e_6adf5087769c8b649ebf5fec"]
  n16["automation ClickUp Command · Read delivery data · 6adf45fef3cd5f19ed4a76ba"]
  n17["automation ClickUp Command · Save view · 6adf460108750d257cf1e381"]
  n18["automation ClickUp Command · Update task · 6adf485af3cd5f19ed4ac683"]
  n19["automation ClickUp Command · Raise change request · 6adf485ec79cad1140a9e9a6"]
  n20["automation ClickUp Command · Decide change request · 6adf485ff3cd5f19ed4ac6fd"]
  n21["automation ClickUp Command · Book consultant · 6adf4aa308750d257cf32534"]
  n22["automation ClickUp Command · Timesheet action · 6adf4aa9f3cd5f19ed4afa85"]
  n23["automation ClickUp Command · Portal action · 6adf4aaef3cd5f19ed4afc58"]
  n24["automation ClickUp Command · Accept proposed tasks · 6adf4d11f3cd5f19ed4b436a"]
  n25["automation ClickUp Command · Publish status report · 6adf4d1492718f6a64e5ca35"]
  n26["automation ClickUp Command · Send executive summary · 6adf4d1508750d257cf3df21"]
  n27["automation ClickUp Command · Update project settings · 6adf4eb5cac0655fe38aef9d"]
  n28["automation ClickUp Command · Mark notification read · 6adf4eb8cac0655fe38aefc9"]
  n29["automation ClickUp Command · Ask Copilot · 6adf526ef3cd5f19ed626787"]
  n30["object ClickUp Command · Project · OBJ_cucmd_project"]
  n31["object ClickUp Command · RAID item · OBJ_cucmd_raid"]
  n32["object ClickUp Command · Task · OBJ_cucmd_task"]
  n33["object ClickUp Command · Time entry · OBJ_cucmd_time_entry"]
  n34["object ClickUp Command · Change request · OBJ_cucmd_change_request"]
  n35["object ClickUp Command · Person · OBJ_cucmd_person"]
  n36["object ClickUp Command · Booking · OBJ_cucmd_booking"]
  n37["object ClickUp Command · Deliverable · OBJ_cucmd_deliverable"]
  n38["object ClickUp Command · Session slot · OBJ_cucmd_session_slot"]
  n39["object ClickUp Command · Document · OBJ_cucmd_document"]
  n40["object ClickUp Command · Activity · OBJ_cucmd_activity"]
  n41["object ClickUp Command · AI output · OBJ_cucmd_ai_output"]
  n42["object ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric"]
  n43["object ClickUp Command · Saved view · OBJ_cucmd_saved_view"]
  n44["object ClickUp Command · Integration · OBJ_cucmd_integration"]
  n45["object ClickUp Command · Notification · OBJ_cucmd_notification"]
  n46["object ClickUp Command · Checklist item · OBJ_cucmd_checklist_item"]
  n47["AI agent ClickUp Command Copilot · e_6adf4f02dc07493166ced9fa"]
  n48["object object_type · object_type"]
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
  n3 -->|data source| n22
  n4 -->|data source| n21
  n5 -->|data source| n20
  n6 -->|data source| n19
  n7 -->|data source| n27
  n8 -->|data source| n18
  n9 -->|data source| n26
  n10 -->|storage read| n48
  n11 -->|storage read| n48
  n12 -->|storage read| n48
  n13 -->|data source| n17
  n14 -->|storage read| n48
  n15 -->|storage read| n48
  n16 -->|storage read| n30
  n16 -->|storage read| n32
  n16 -->|storage read| n31
  n16 -->|storage read| n36
  n16 -->|storage read| n35
  n16 -->|storage read| n34
  n16 -->|storage read| n41
  n16 -->|storage read| n42
  n16 -->|storage read| n39
  n17 -->|storage read| n43
  n17 -->|storage write| n43
  n18 -->|storage read| n32
  n18 -->|storage read| n30
  n18 -->|storage write| n32
  n18 -->|storage write| n40
  n19 -->|storage read| n30
  n19 -->|storage read| n34
  n19 -->|storage write| n34
  n19 -->|storage write| n40
  n20 -->|storage read| n34
  n20 -->|storage read| n30
  n20 -->|storage write| n34
  n20 -->|storage write| n30
  n20 -->|storage write| n40
  n21 -->|storage read| n35
  n21 -->|storage read| n30
  n21 -->|storage read| n36
  n21 -->|storage write| n36
  n21 -->|storage write| n40
  n22 -->|storage read| n32
  n22 -->|storage write| n33
  n22 -->|storage write| n40
  n22 -->|storage read| n33
  n23 -->|storage read| n35
  n23 -->|storage read| n37
  n23 -->|storage write| n37
  n23 -->|storage write| n40
  n23 -->|storage read| n38
  n23 -->|storage write| n38
  n23 -->|storage read| n46
  n23 -->|storage write| n46
  n23 -->|storage read| n39
  n23 -->|storage write| n39
  n24 -->|storage read| n41
  n24 -->|storage write| n32
  n24 -->|storage write| n41
  n24 -->|storage write| n40
  n25 -->|storage read| n30
  n25 -->|storage write| n39
  n25 -->|storage write| n40
  n26 -->|storage read| n42
  n27 -->|storage read| n30
  n27 -->|storage write| n30
  n27 -->|storage write| n40
  n28 -->|storage read| n45
  n28 -->|storage write| n45
```
