Tenant orbit.uat.unifyapps.com · solution "Clickup · ClickUp Delivery command dashboard" (e_6adf231a08f96579541331a5)

```mermaid
flowchart LR
  n1["app ClickUp Delivery Command · app-a2a9509a82c1"]
  n2["page global-page-of-app-a2a9509a82c1 · e_global_app-a2a9509a82c1"]
  n3["data source Mark notification read · e_6adf5a2408f9657954446fc8"]
  n4["data source Portal action · e_6adf58c508f9657954442f32"]
  n5["data source Accept proposed tasks · e_6adf57ab08f965795444083e"]
  n6["data source Publish status report · e_6adf57ab08f9657954440835"]
  n7["data source Ask Copilot · e_6adf57aa769c8b649ec0291f"]
  n8["data source Timesheet action · e_6adf55a8769c8b649ebfe4a2"]
  n9["data source Book consultant · e_6adf55a8769c8b649ebfe49d"]
  n10["data source Decide change request · e_6adf552d08f965795443b4d9"]
  n11["data source Raise change request · e_6adf5341769c8b649ebfa6d9"]
  n12["data source Update project settings · e_6adf534108f96579544384bc"]
  n13["data source Update task · e_6adf5340769c8b649ebfa6d3"]
  n14["data source Send executive summary · e_6adf5087dc07493166cf01cb"]
  n15["data source data_update_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c8"]
  n16["data source data_fetchOne_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c5"]
  n17["data source data_fetch_app-a2a9509a82c1 · e_6adf5087dc07493166cf01c2"]
  n18["data source Save view · e_6adf5087769c8b649ebf5ff2"]
  n19["data source data_delete_app-a2a9509a82c1 · e_6adf5087769c8b649ebf5fef"]
  n20["data source data_create_app-a2a9509a82c1 · e_6adf5087769c8b649ebf5fec"]
  n21["automation ClickUp Command · Read delivery data · 6adf45fef3cd5f19ed4a76ba"]
  n22["automation ClickUp Command · Save view · 6adf460108750d257cf1e381"]
  n23["automation ClickUp Command · Update task · 6adf485af3cd5f19ed4ac683"]
  n24["automation ClickUp Command · Raise change request · 6adf485ec79cad1140a9e9a6"]
  n25["automation ClickUp Command · Decide change request · 6adf485ff3cd5f19ed4ac6fd"]
  n26["automation ClickUp Command · Book consultant · 6adf4aa308750d257cf32534"]
  n27["automation ClickUp Command · Timesheet action · 6adf4aa9f3cd5f19ed4afa85"]
  n28["automation ClickUp Command · Portal action · 6adf4aaef3cd5f19ed4afc58"]
  n29["automation ClickUp Command · Accept proposed tasks · 6adf4d11f3cd5f19ed4b436a"]
  n30["automation ClickUp Command · Publish status report · 6adf4d1492718f6a64e5ca35"]
  n31["automation ClickUp Command · Send executive summary · 6adf4d1508750d257cf3df21"]
  n32["automation ClickUp Command · Update project settings · 6adf4eb5cac0655fe38aef9d"]
  n33["automation ClickUp Command · Mark notification read · 6adf4eb8cac0655fe38aefc9"]
  n34["automation ClickUp Command · Ask Copilot · 6adf526ef3cd5f19ed626787"]
  n35["object ClickUp Command · Project · OBJ_cucmd_project"]
  n36["object ClickUp Command · RAID item · OBJ_cucmd_raid"]
  n37["object ClickUp Command · Task · OBJ_cucmd_task"]
  n38["object ClickUp Command · Time entry · OBJ_cucmd_time_entry"]
  n39["object ClickUp Command · Change request · OBJ_cucmd_change_request"]
  n40["object ClickUp Command · Person · OBJ_cucmd_person"]
  n41["object ClickUp Command · Booking · OBJ_cucmd_booking"]
  n42["object ClickUp Command · Deliverable · OBJ_cucmd_deliverable"]
  n43["object ClickUp Command · Session slot · OBJ_cucmd_session_slot"]
  n44["object ClickUp Command · Document · OBJ_cucmd_document"]
  n45["object ClickUp Command · Activity · OBJ_cucmd_activity"]
  n46["object ClickUp Command · AI output · OBJ_cucmd_ai_output"]
  n47["object ClickUp Command · Weekly metric · OBJ_cucmd_weekly_metric"]
  n48["object ClickUp Command · Saved view · OBJ_cucmd_saved_view"]
  n49["object ClickUp Command · Integration · OBJ_cucmd_integration"]
  n50["object ClickUp Command · Notification · OBJ_cucmd_notification"]
  n51["object ClickUp Command · Checklist item · OBJ_cucmd_checklist_item"]
  n52["AI agent ClickUp Command Copilot · e_6adf4f02dc07493166ced9fa"]
  n53["object object_type · object_type"]
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
  n3 -->|data source| n33
  n4 -->|data source| n28
  n5 -->|data source| n29
  n6 -->|data source| n30
  n7 -->|data source| n34
  n8 -->|data source| n27
  n9 -->|data source| n26
  n10 -->|data source| n25
  n11 -->|data source| n24
  n12 -->|data source| n32
  n13 -->|data source| n23
  n14 -->|data source| n31
  n15 -->|storage read| n53
  n16 -->|storage read| n53
  n17 -->|storage read| n53
  n18 -->|data source| n22
  n19 -->|storage read| n53
  n20 -->|storage read| n53
  n21 -->|storage read| n35
  n21 -->|storage read| n37
  n21 -->|storage read| n36
  n21 -->|storage read| n41
  n21 -->|storage read| n40
  n21 -->|storage read| n39
  n21 -->|storage read| n46
  n21 -->|storage read| n47
  n21 -->|storage read| n44
  n22 -->|storage read| n48
  n22 -->|storage write| n48
  n23 -->|storage read| n37
  n23 -->|storage read| n35
  n23 -->|storage write| n37
  n23 -->|storage write| n45
  n24 -->|storage read| n35
  n24 -->|storage read| n39
  n24 -->|storage write| n39
  n24 -->|storage write| n45
  n25 -->|storage read| n39
  n25 -->|storage read| n35
  n25 -->|storage write| n39
  n25 -->|storage write| n35
  n25 -->|storage write| n45
  n26 -->|storage read| n40
  n26 -->|storage read| n35
  n26 -->|storage read| n41
  n26 -->|storage write| n41
  n26 -->|storage write| n45
  n27 -->|storage read| n37
  n27 -->|storage write| n38
  n27 -->|storage write| n45
  n27 -->|storage read| n38
  n28 -->|storage read| n40
  n28 -->|storage read| n42
  n28 -->|storage write| n42
  n28 -->|storage write| n45
  n28 -->|storage read| n43
  n28 -->|storage write| n43
  n28 -->|storage read| n51
  n28 -->|storage write| n51
  n28 -->|storage read| n44
  n28 -->|storage write| n44
  n29 -->|storage read| n46
  n29 -->|storage write| n37
  n29 -->|storage write| n46
  n29 -->|storage write| n45
  n30 -->|storage read| n35
  n30 -->|storage write| n44
  n30 -->|storage write| n45
  n31 -->|storage read| n47
  n32 -->|storage read| n35
  n32 -->|storage write| n35
  n32 -->|storage write| n45
  n33 -->|storage read| n50
  n33 -->|storage write| n50
```
