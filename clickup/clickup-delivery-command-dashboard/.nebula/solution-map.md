# Solution map

Solution: `Clickup · ClickUp Delivery command dashboard` (e_6adf231a08f96579541331a5) · tenant orbit.uat.unifyapps.com

## Entities

| Kind | Name | Id | Version | Stale |
|---|---|---|---|---|
| app | `ClickUp Delivery Command` | app-a2a9509a82c1 | 5 | no |
| page | `global-page-of-app-a2a9509a82c1` | e_global_app-a2a9509a82c1 | 0 | no |
| automation | `ClickUp Command · Read delivery data` | 6adf45fef3cd5f19ed4a76ba | 5 | no |
| automation | `ClickUp Command · Save view` | 6adf460108750d257cf1e381 | 1 | no |
| automation | `ClickUp Command · Update task` | 6adf485af3cd5f19ed4ac683 | 2 | no |
| automation | `ClickUp Command · Raise change request` | 6adf485ec79cad1140a9e9a6 | 1 | no |
| automation | `ClickUp Command · Decide change request` | 6adf485ff3cd5f19ed4ac6fd | 1 | no |
| automation | `ClickUp Command · Book consultant` | 6adf4aa308750d257cf32534 | 1 | no |
| automation | `ClickUp Command · Timesheet action` | 6adf4aa9f3cd5f19ed4afa85 | 2 | no |
| automation | `ClickUp Command · Portal action` | 6adf4aaef3cd5f19ed4afc58 | 1 | no |
| automation | `ClickUp Command · Accept proposed tasks` | 6adf4d11f3cd5f19ed4b436a | 1 | no |
| automation | `ClickUp Command · Publish status report` | 6adf4d1492718f6a64e5ca35 | 1 | no |
| automation | `ClickUp Command · Send executive summary` | 6adf4d1508750d257cf3df21 | 1 | no |
| automation | `ClickUp Command · Update project settings` | 6adf4eb5cac0655fe38aef9d | 1 | no |
| automation | `ClickUp Command · Mark notification read` | 6adf4eb8cac0655fe38aefc9 | 1 | no |
| automation | `ClickUp Command · Ask Copilot` | 6adf526ef3cd5f19ed626787 | 1 | no |
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
| ai-agent | `ClickUp Command Copilot` | e_6adf4f02dc07493166ced9fa | 10 | no |

## Wiring

| From | Part | To | Via | Fields |
|---|---|---|---|---|
| page `global-page-of-app-a2a9509a82c1` | `data source Mark notification read` | automation `ClickUp Command · Mark notification read` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Portal action` | automation `ClickUp Command · Portal action` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Accept proposed tasks` | automation `ClickUp Command · Accept proposed tasks` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Publish status report` | automation `ClickUp Command · Publish status report` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Ask Copilot` | automation `ClickUp Command · Ask Copilot` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Timesheet action` | automation `ClickUp Command · Timesheet action` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Book consultant` | automation `ClickUp Command · Book consultant` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Decide change request` | automation `ClickUp Command · Decide change request` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Raise change request` | automation `ClickUp Command · Raise change request` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Update project settings` | automation `ClickUp Command · Update project settings` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Update task` | automation `ClickUp Command · Update task` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Send executive summary` | automation `ClickUp Command · Send executive summary` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source data_update_app-a2a9509a82c1` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-a2a9509a82c1` | `data source data_fetchOne_app-a2a9509a82c1` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-a2a9509a82c1` | `data source data_fetch_app-a2a9509a82c1` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-a2a9509a82c1` | `data source Save view` | automation `ClickUp Command · Save view` | data source |  |
| page `global-page-of-app-a2a9509a82c1` | `data source data_delete_app-a2a9509a82c1` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-a2a9509a82c1` | `data source data_create_app-a2a9509a82c1` | object `{{object_type}}` | storage read |  |
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
| automation `ClickUp Command · Book consultant` | `node Read the person` | object `ClickUp Command · Person` | storage read |  |
| automation `ClickUp Command · Book consultant` | `node Read the project` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Book consultant` | `node Read the person's existing bookings` | object `ClickUp Command · Booking` | storage read |  |
| automation `ClickUp Command · Book consultant` | `node Save the booking` | object `ClickUp Command · Booking` | storage write |  |
| automation `ClickUp Command · Book consultant` | `node Record the booking in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Read the task for its project` | object `ClickUp Command · Task` | storage read |  |
| automation `ClickUp Command · Timesheet action` | `node Create the time entry` | object `ClickUp Command · Time entry` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Record the log in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Read the open entries of that week` | object `ClickUp Command · Time entry` | storage read |  |
| automation `ClickUp Command · Timesheet action` | `node Mark the entry submitted` | object `ClickUp Command · Time entry` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Record the submit in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Read the pending entries named` | object `ClickUp Command · Time entry` | storage read |  |
| automation `ClickUp Command · Timesheet action` | `node Mark the entry approved` | object `ClickUp Command · Time entry` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Record the approval in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Mark the entry returned` | object `ClickUp Command · Time entry` | storage write |  |
| automation `ClickUp Command · Timesheet action` | `node Record the return in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Portal action` | `node Read the sponsor and their project` | object `ClickUp Command · Person` | storage read |  |
| automation `ClickUp Command · Portal action` | `node Read the deliverable` | object `ClickUp Command · Deliverable` | storage read |  |
| automation `ClickUp Command · Portal action` | `node Record the change request on the deliverable` | object `ClickUp Command · Deliverable` | storage write |  |
| automation `ClickUp Command · Portal action` | `node Sign the deliverable off` | object `ClickUp Command · Deliverable` | storage write |  |
| automation `ClickUp Command · Portal action` | `node Record the sign-off in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Portal action` | `node Read the slot` | object `ClickUp Command · Session slot` | storage read |  |
| automation `ClickUp Command · Portal action` | `node Book the slot` | object `ClickUp Command · Session slot` | storage write |  |
| automation `ClickUp Command · Portal action` | `node Read the checklist item` | object `ClickUp Command · Checklist item` | storage read |  |
| automation `ClickUp Command · Portal action` | `node Save the answer` | object `ClickUp Command · Checklist item` | storage write |  |
| automation `ClickUp Command · Portal action` | `node Confirm an upload: read the document` | object `ClickUp Command · Document` | storage read |  |
| automation `ClickUp Command · Portal action` | `node Confirm the upload` | object `ClickUp Command · Document` | storage write |  |
| automation `ClickUp Command · Accept proposed tasks` | `node Read the named AI outputs` | object `ClickUp Command · AI output` | storage read |  |
| automation `ClickUp Command · Accept proposed tasks` | `node Create the task from the proposal` | object `ClickUp Command · Task` | storage write |  |
| automation `ClickUp Command · Accept proposed tasks` | `node Set the output's decision` | object `ClickUp Command · AI output` | storage write |  |
| automation `ClickUp Command · Accept proposed tasks` | `node Record one Activity row` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Publish status report` | `node Read the project` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Publish status report` | `node Write the status report document` | object `ClickUp Command · Document` | storage write |  |
| automation `ClickUp Command · Publish status report` | `node Record one Activity row` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Send executive summary` | `node Read the Weekly metric for the week` | object `ClickUp Command · Weekly metric` | storage read |  |
| automation `ClickUp Command · Update project settings` | `node Read the project as stored` | object `ClickUp Command · Project` | storage read |  |
| automation `ClickUp Command · Update project settings` | `node Save the fields the caller filled in; blank ones keep their stored value` | object `ClickUp Command · Project` | storage write |  |
| automation `ClickUp Command · Update project settings` | `node Record the change in the activity feed` | object `ClickUp Command · Activity` | storage write |  |
| automation `ClickUp Command · Mark notification read` | `node Read the notification as stored` | object `ClickUp Command · Notification` | storage read |  |
| automation `ClickUp Command · Mark notification read` | `node Set read to true` | object `ClickUp Command · Notification` | storage write |  |

## Not checked

- ai-agent `ClickUp Command Copilot` (e_6adf4f02dc07493166ced9fa): its tools are not in the cache (get_agent)
