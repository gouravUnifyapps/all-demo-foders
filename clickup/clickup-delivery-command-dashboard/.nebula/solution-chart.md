Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command dashboard" (e_6adf231a08f96579541331a5)

```mermaid
flowchart LR
  n1["app ClickUp Delivery Command · app-a2a9509a82c1"]
  n2["page global-page-of-app-a2a9509a82c1 · e_global_app-a2a9509a82c1"]
  n3["data source Send executive summary · e_6adf5087dc07493166cf01cb"]
  n4["data source data_update_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c8"]
  n5["data source data_fetchOne_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c5"]
  n6["data source data_fetch_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c2"]
  n7["data source Save view · e_6adf5087769c8b649ebf5ff2"]
  n8["data source data_delete_app-a2a9509a82c1 · e_6adf5087769c8b649ebf5fef"]
  n9["data source data_create_app-a2a9509a82c1 · e_6adf5087769c8b649ebf5fec"]
  n10["automation ClickUp Command · Read delivery data · 6adf45fef3cd5f19ed4a76ba"]
  n11["automation ClickUp Command · Save view · 6adf460108750d257cf1e381"]
  n12["automation ClickUp Command · Update task · 6adf485af3cd5f19ed4ac683"]
  n13["automation ClickUp Command · Raise change request · 6adf485ec79cad1140a9e9a6"]
  n14["automation ClickUp Command · Decide change request · 6adf485ff3cd5f19ed4ac6fd"]
  n15["automation ClickUp Command · Book consultant · 6adf4aa308750d257cf32534"]
  n16["automation ClickUp Command · Timesheet action · 6adf4aa9f3cd5f19ed4afa85"]
  n17["automation ClickUp Command · Portal action · 6adf4aaef3cd5f19ed4afc58"]
  n18["automation ClickUp Command · Accept proposed tasks · 6adf4d11f3cd5f19ed4b436a"]
  n19["automation ClickUp Command · Publish status report · 6adf4d1492718f6a64e5ca35"]
  n20["automation ClickUp Command · Send executive summary · 6adf4d1508750d257cf3df21"]
  n21["automation ClickUp Command · Update project settings · 6adf4eb5cac0655fe38aef9d"]
  n22["automation ClickUp Command · Mark notification read · 6adf4eb8cac0655fe38aefc9"]
  n23["automation ClickUp Command · Ask Copilot · 6adf526ef3cd5f19ed626787"]
  n24["object ClickUp Command · Project · OBJ_cucmd_project"]
  n25["object ClickUp Command · RAID item · OBJ_cucmd_raid"]
  n26["object ClickUp Command · Task · OBJ_cucmd_task"]
  n27["object ClickUp Command · Time entry · OBJ_cucmd_time_entry"]
  n28["object ClickUp Command · Change request · OBJ_cucmd_change_request"]
  n29["object ClickUp Command · Person · OBJ_cucmd_person"]
  n30["object ClickUp Command · Booking · OBJ_cucmd_booking"]
  n31["object ClickUp Command · Deliverable · OBJ_cucmd_deliverable"]
  n32["object ClickUp Command · Session slot · OBJ_cucmd_session_slot"]
  n33["object ClickUp Command · Document · OBJ_cucmd_document"]
  n34["object ClickUp Command · Activity · OBJ_cucmd_activity"]
  n35["object ClickUp Command · AI output · OBJ_cucmd_ai_output"]
  n36["object ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric"]
  n37["object ClickUp Command · Saved view · OBJ_cucmd_saved_view"]
  n38["object ClickUp Command · Integration · OBJ_cucmd_integration"]
  n39["object ClickUp Command · Notification · OBJ_cucmd_notification"]
  n40["object ClickUp Command · Checklist item · OBJ_cucmd_checklist_item"]
  n41["AI agent ClickUp Command Copilot · e_6adf4f02dc07493166ced9fa"]
  n42["object object_type · object_type"]
  n1 --- n2
  n2 --- n3
  n2 --- n4
  n2 --- n5
  n2 --- n6
  n2 --- n7
  n2 --- n8
  n2 --- n9
  n3 -->|data source| n20
  n4 -->|storage read| n42
  n5 -->|storage read| n42
  n6 -->|storage read| n42
  n7 -->|data source| n11
  n8 -->|storage read| n42
  n9 -->|storage read| n42
  n10 -->|storage read| n24
  n10 -->|storage read| n26
  n10 -->|storage read| n25
  n10 -->|storage read| n30
  n10 -->|storage read| n29
  n10 -->|storage read| n28
  n10 -->|storage read| n35
  n10 -->|storage read| n36
  n10 -->|storage read| n33
  n11 -->|storage read| n37
  n11 -->|storage write| n37
  n12 -->|storage read| n26
  n12 -->|storage read| n24
  n12 -->|storage write| n26
  n12 -->|storage write| n34
  n13 -->|storage read| n24
  n13 -->|storage read| n28
  n13 -->|storage write| n28
  n13 -->|storage write| n34
  n14 -->|storage read| n28
  n14 -->|storage read| n24
  n14 -->|storage write| n28
  n14 -->|storage write| n24
  n14 -->|storage write| n34
  n15 -->|storage read| n29
  n15 -->|storage read| n24
  n15 -->|storage read| n30
  n15 -->|storage write| n30
  n15 -->|storage write| n34
  n16 -->|storage read| n26
  n16 -->|storage write| n27
  n16 -->|storage write| n34
  n16 -->|storage read| n27
  n17 -->|storage read| n29
  n17 -->|storage read| n31
  n17 -->|storage write| n31
  n17 -->|storage write| n34
  n17 -->|storage read| n32
  n17 -->|storage write| n32
  n17 -->|storage read| n40
  n17 -->|storage write| n40
  n17 -->|storage read| n33
  n17 -->|storage write| n33
  n18 -->|storage read| n35
  n18 -->|storage write| n26
  n18 -->|storage write| n35
  n18 -->|storage write| n34
  n19 -->|storage read| n24
  n19 -->|storage write| n33
  n19 -->|storage write| n34
  n20 -->|storage read| n36
  n21 -->|storage read| n24
  n21 -->|storage write| n24
  n21 -->|storage write| n34
  n22 -->|storage read| n39
  n22 -->|storage write| n39
```
