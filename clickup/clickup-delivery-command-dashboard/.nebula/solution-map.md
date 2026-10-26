# Solution map

Solution: `Clickup · ClickUp Delivery command dashboard` (e_6adf231a08f96579541331a5) · tenant orbit.uat.unifyapps.com

## Entities

| Kind | Name | Id | Version | Stale |
|---|---|---|---|---|
| automation | `ClickUp Command · Read delivery data` | 6adf45fef3cd5f19ed4a76ba | 5 | no |
| automation | `ClickUp Command · Save view` | 6adf460108750d257cf1e381 | 1 | no |
| automation | `ClickUp Command · Update task` | 6adf485af3cd5f19ed4ac683 | 2 | no |
| automation | `ClickUp Command · Raise change request` | 6adf485ec79cad1140a9e9a6 | 1 | no |
| automation | `ClickUp Command · Decide change request` | 6adf485ff3cd5f19ed4ac6fd | 1 | no |
| object | `ClickUp Command · Project` | OBJ_cucmd_project | 0 | no |
| object | `ClickUp Command · RAID item` | OBJ_cucmd_raid | 0 | no |
| object | `ClickUp Command · Task` | OBJ_cucmd_task | 0 | no |
| object | `ClickUp Command · Time entry` | OBJ_cucmd_time_entry | 0 | no |
| object | `ClickUp Command · Change request` | OBJ_cucmd_change_request | 0 | no |
| object | `ClickUp Command · Person` | OBJ_cucmd_person | 0 | no |
| object | `ClickUp Command · Booking` | OBJ_cucmd_booking | 0 | no |
| object | `ClickUp Command · Deliverable` | OBJ_cucmd_deliverable | 0 | no |
| object | `ClickUp Command · Session slot` | OBJ_cucmd_session_slot | 0 | no |
| object | `ClickUp Command · Document` | OBJ_cucmd_document | 0 | no |
| object | `ClickUp Command · Activity` | OBJ_cucmd_activity | 0 | no |
| object | `ClickUp Command · AI output` | OBJ_cucmd_ai_output | 0 | no |
| object | `ClickUp Command · Weekly metric` | OBJ_cucmd_weekly_metric | 0 | no |
| object | `ClickUp Command · Saved view` | OBJ_cucmd_saved_view | 0 | no |
| object | `ClickUp Command · Integration` | OBJ_cucmd_integration | 0 | no |
| object | `ClickUp Command · Notification` | OBJ_cucmd_notification | 0 | no |
| object | `ClickUp Command · Checklist item` | OBJ_cucmd_checklist_item | 0 | no |

## Wiring

| From | Part | To | Via | Fields |
|---|---|---|---|---|
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_project records (read only)` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_task records (read only)` | object `ClickUp Command · Task` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_raid records (read only)` | object `ClickUp Command · RAID item` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_booking records (read only)` | object `ClickUp Command · Booking` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_person records (read only)` | object `ClickUp Command · Person` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_change_request records (read only)` | object `ClickUp Command · Change request` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_ai_output records (read only)` | object `ClickUp Command · AI output` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_weekly_metric records (read only)` | object `ClickUp Command · Weekly metric` | storage read |  |
| automation `ClickUp Command · Read delivery data` | `node Fetch OBJ_cucmd_document records (read only)` | object `ClickUp Command · Document` | storage read |  |
| automation `ClickUp Command · Save view` | `node Read every saved view's code and name` | object `ClickUp Command · Saved view` | storage read |  |
| automation `ClickUp Command · Save view` | `node Create the saved view` | object `ClickUp Command · Saved view` | storage write |  |
| automation `ClickUp Command · Update task` | `node Read the task` | object `ClickUp Command · Task` | storage read |  |
| automation `ClickUp Command · Update task` | `node Read every task of its project` | object `ClickUp Command · Task` | storage read |  |
| automation `ClickUp Command · Update task` | `node Read the project` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Update task` | `node Upsert the task by its key` | object `ClickUp Command · Task` | storage write |  |
| automation `ClickUp Command · Update task` | `node Record one Activity row` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Raise change request` | `node Read the project` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Raise change request` | `node Read the highest stored change request code` | object `ClickUp Command · Change request` | storage read |  |
| automation `ClickUp Command · Raise change request` | `node Write the change request` | object `ClickUp Command · Change request` | storage write |  |
| automation `ClickUp Command · Raise change request` | `node Record one Activity row` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Decide change request` | `node Read the change request` | object `ClickUp Command · Change request` | storage read |  |
| automation `ClickUp Command · Decide change request` | `node Read its project` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Decide change request` | `node Save the decision on the change request` | object `ClickUp Command · Change request` | storage write |  |
| automation `ClickUp Command · Decide change request` | `node Move the project's go-live and planned hours` | object `ClickUp Command · Project` | storage write |  |
| automation `ClickUp Command · Decide change request` | `node Record one Activity row` | object `ClickUp Command · Activity` | storage write |  |

## Not checked

- none
