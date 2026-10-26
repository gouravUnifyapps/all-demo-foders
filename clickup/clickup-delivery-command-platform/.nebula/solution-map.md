# Solution map

Solution: `Clickup · ClickUp Delivery command platform` (e_6adb4b845236864dd8b18935) · tenant orbit.uat.unifyapps.com

## Entities

| Kind | Name | Id | Version | Stale |
|---|---|---|---|---|
| app | `ClickUp Delivery Command` | app-f53fd0efccec | 3 | no |
| page | `global-page-of-app-f53fd0efccec` | e_global_app-f53fd0efccec | 0 | no |
| automation | `Delivery Command · Move task` | 6adba2ac92718f6a64f34bc5 | 1 | no |
| automation | `Delivery Command · Reschedule task` | 6adba3266112da3e23fcf133 | 1 | no |
| automation | `Delivery Command · Book consultant` | 6adba3b292718f6a64f39440 | 1 | no |
| automation | `Delivery Command · Review timesheets` | 6adba402f4431f44e30943f1 | 0 | no |
| automation | `Delivery Command · Log time` | 6adba405ca4f9d2045858cfc | 0 | no |
| automation | `Delivery Command · Book training slot` | 6adba59c92718f6a64f4015a | 0 | no |
| automation | `Delivery Command · Publish status report` | 6adba5cfeb71d135d657c23d | 0 | no |
| automation | `Delivery Command · Record sign-off` | 6adba5f8eb71d135d657e318 | 0 | no |
| automation | `Delivery Command · Accept proposed tasks` | 6adba625ca4f9d2045986507 | 0 | no |
| automation | `Delivery Command · Change request` | 6adba6a8cac0655fe3582da3 | 0 | no |
| automation | `Delivery Command · Mark notification read` | 6adba94deb71d135d658f2dc | 0 | no |
| automation | `Delivery Command · Confirm upload` | 6adba9abcac0655fe35aa2fc | 0 | no |
| automation | `Delivery Command · Save view` | 6adba9aef3cd5f19ed89eaec | 0 | no |
| automation | `Delivery Command · Update project settings` | 6adba9def3cd5f19ed89ef7d | 0 | no |
| automation | `Delivery Command · Read delivery data` | 6adbaa4fca4f9d20459bd303 | 0 | no |
| automation | `Delivery Command · Send executive summary` | 6adbac23eb71d135d65f4715 | 0 | no |
| automation | `Delivery Command · Weekly executive email schedule` | 6adbacd6f3cd5f19ed8a543a | 0 | no |
| automation | `Delivery Command · Ask Copilot` | 6adbaf90c79cad11403e9b72 | 0 | no |
| object | `Delivery Command · Task` | OBJ_dcmd_task | 0 | no |
| object | `Delivery Command · Project` | OBJ_dcmd_project | 0 | no |
| object | `Delivery Command · RAID item` | OBJ_dcmd_raid | 0 | no |
| object | `Delivery Command · Booking` | OBJ_dcmd_booking | 0 | no |
| object | `Delivery Command · Time entry` | OBJ_dcmd_time_entry | 0 | no |
| object | `Delivery Command · Person` | OBJ_dcmd_person | 0 | no |
| object | `Delivery Command · Change request` | OBJ_dcmd_change_request | 0 | no |
| object | `Delivery Command · Document` | OBJ_dcmd_document | 0 | no |
| object | `Delivery Command · Session slot` | OBJ_dcmd_session_slot | 0 | no |
| object | `Delivery Command · Activity` | OBJ_dcmd_activity | 0 | no |
| object | `Delivery Command · Sign-off` | OBJ_dcmd_signoff | 0 | no |
| object | `Delivery Command · Checklist item` | OBJ_dcmd_checklist_item | 0 | no |
| object | `Delivery Command · Notification` | OBJ_dcmd_notification | 0 | no |
| object | `Delivery Command · Integration` | OBJ_dcmd_integration | 0 | no |
| object | `Delivery Command · Saved view` | OBJ_dcmd_saved_view | 0 | no |
| object | `Delivery Command · AI output` | OBJ_dcmd_ai_output | 0 | no |
| object | `Delivery Command · Weekly snapshot` | OBJ_dcmd_weekly_snapshot | 0 | no |
| object | `Delivery Command · Weekly metric` | OBJ_dcmd_weekly_metric | 0 | no |
| object | `Delivery Command · Role permission` | OBJ_dcmd_role_permission | 0 | no |
| object | `Delivery Command · Upload` | OBJ_dcmd_upload | 0 | no |
| object | `Delivery Command · Executive email` | OBJ_dcmd_exec_email | 0 | no |
| ai-agent | `Delivery Command · Copilot` | e_6adbabd2925d282255cee62b | 10 | no |

## Wiring

| From | Part | To | Via | Fields |
|---|---|---|---|---|
| page `global-page-of-app-f53fd0efccec` | `data source Update project settings` | automation `Delivery Command · Update project settings` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Mark notification read` | automation `Delivery Command · Mark notification read` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Log time` | automation `Delivery Command · Log time` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Confirm upload` | automation `Delivery Command · Confirm upload` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Book training slot` | automation `Delivery Command · Book training slot` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Record sign-off` | automation `Delivery Command · Record sign-off` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Accept proposed tasks` | automation `Delivery Command · Accept proposed tasks` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Publish status report` | automation `Delivery Command · Publish status report` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Ask Copilot` | automation `Delivery Command · Ask Copilot` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Send executive summary` | automation `Delivery Command · Send executive summary` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Change request` | automation `Delivery Command · Change request` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Review timesheets` | automation `Delivery Command · Review timesheets` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Book consultant` | automation `Delivery Command · Book consultant` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Reschedule task` | automation `Delivery Command · Reschedule task` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Move task` | automation `Delivery Command · Move task` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source Save view` | automation `Delivery Command · Save view` | data source |  |
| page `global-page-of-app-f53fd0efccec` | `data source data_fetchOne_app-f53fd0efccec` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-f53fd0efccec` | `data source data_fetch_app-f53fd0efccec` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-f53fd0efccec` | `data source data_delete_app-f53fd0efccec` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-f53fd0efccec` | `data source data_update_app-f53fd0efccec` | object `{{object_type}}` | storage read |  |
| page `global-page-of-app-f53fd0efccec` | `data source data_create_app-f53fd0efccec` | object `{{object_type}}` | storage read |  |
| automation `Delivery Command · Move task` | `node Read the task by its id` | object `Delivery Command · Task` | storage read |  |
| automation `Delivery Command · Move task` | `node Set the task's stage and status` | object `Delivery Command · Task` | storage write |  |
| automation `Delivery Command · Move task` | `node Count the tasks now in the target column (same project, same stage)` | object `Delivery Command · Task` | storage read |  |
| automation `Delivery Command · Move task` | `node Record the move in the activity feed` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Reschedule task` | `node Read the task being rescheduled` | object `Delivery Command · Task` | storage read |  |
| automation `Delivery Command · Reschedule task` | `node Read every task of the same project` | object `Delivery Command · Task` | storage read |  |
| automation `Delivery Command · Reschedule task` | `node Read the project for its go-live` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Reschedule task` | `node Set the task's new dates` | object `Delivery Command · Task` | storage write |  |
| automation `Delivery Command · Reschedule task` | `node Save the project's go-live` | object `Delivery Command · Project` | storage write |  |
| automation `Delivery Command · Reschedule task` | `node Record the reschedule in the activity feed` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Book consultant` | `node Read the person for their weekly capacity` | object `Delivery Command · Person` | storage read |  |
| automation `Delivery Command · Book consultant` | `node Read the project being booked` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Book consultant` | `node Read the person's existing bookings in those weeks` | object `Delivery Command · Booking` | storage read |  |
| automation `Delivery Command · Book consultant` | `node Create the booking` | object `Delivery Command · Booking` | storage write |  |
| automation `Delivery Command · Book consultant` | `node Record the booking in the activity feed` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Review timesheets` | `node Approve or return every pending entry of those people in that week` | object `Delivery Command · Time entry` | storage write |  |
| automation `Delivery Command · Review timesheets` | `node Record the review in the activity feed` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Log time` | `node Read the task` | object `Delivery Command · Task` | storage read |  |
| automation `Delivery Command · Log time` | `node Read the person for their week start` | object `Delivery Command · Person` | storage read |  |
| automation `Delivery Command · Log time` | `node Write the time entry in Draft` | object `Delivery Command · Time entry` | storage write |  |
| automation `Delivery Command · Log time` | `node Add the hours to the task, and set its status when one was given` | object `Delivery Command · Task` | storage write |  |
| automation `Delivery Command · Log time` | `node Record the time in the activity feed` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Book training slot` | `node Read the slot as stored now` | object `Delivery Command · Session slot` | storage read |  |
| automation `Delivery Command · Book training slot` | `node Mark the slot taken by the actor` | object `Delivery Command · Session slot` | storage write |  |
| automation `Delivery Command · Publish status report` | `node Save the published status report` | object `Delivery Command · AI output` | storage write |  |
| automation `Delivery Command · Publish status report` | `node Write the activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Record sign-off` | `node Read the sign-off as stored now` | object `Delivery Command · Sign-off` | storage read |  |
| automation `Delivery Command · Record sign-off` | `node Read the project for its lead` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Record sign-off` | `node Save the decision on the sign-off` | object `Delivery Command · Sign-off` | storage write |  |
| automation `Delivery Command · Record sign-off` | `node Write the activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Record sign-off` | `node Notify the project lead` | object `Delivery Command · Notification` | storage write |  |
| automation `Delivery Command · Accept proposed tasks` | `node Read the proposal as stored now` | object `Delivery Command · AI output` | storage read |  |
| automation `Delivery Command · Accept proposed tasks` | `node Read the project for its current stage` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Accept proposed tasks` | `node Create the task from the proposal` | object `Delivery Command · Task` | storage write |  |
| automation `Delivery Command · Accept proposed tasks` | `node Mark the proposal accepted` | object `Delivery Command · AI output` | storage write |  |
| automation `Delivery Command · Accept proposed tasks` | `node Mark the proposal rejected` | object `Delivery Command · AI output` | storage write |  |
| automation `Delivery Command · Change request` | `node Read any stored copy of this change request` | object `Delivery Command · Change request` | storage read |  |
| automation `Delivery Command · Change request` | `node Read the project` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Change request` | `node Save the submitted change request` | object `Delivery Command · Change request` | storage write |  |
| automation `Delivery Command · Change request` | `node Write the activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Change request` | `node Read the change request as stored now` | object `Delivery Command · Change request` | storage read |  |
| automation `Delivery Command · Change request` | `node Record the finance rejection` | object `Delivery Command · Change request` | storage write |  |
| automation `Delivery Command · Change request` | `node Record the director rejection` | object `Delivery Command · Change request` | storage write |  |
| automation `Delivery Command · Change request` | `node Write the rejection activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Change request` | `node Approve step one and pass to finance` | object `Delivery Command · Change request` | storage write |  |
| automation `Delivery Command · Change request` | `node Write the step activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Change request` | `node Record the finance approval` | object `Delivery Command · Change request` | storage write |  |
| automation `Delivery Command · Change request` | `node Record the director approval` | object `Delivery Command · Change request` | storage write |  |
| automation `Delivery Command · Change request` | `node Read the project` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Change request` | `node Add the task to the project plan` | object `Delivery Command · Task` | storage write |  |
| automation `Delivery Command · Change request` | `node Move the project's go-live and budget` | object `Delivery Command · Project` | storage write |  |
| automation `Delivery Command · Change request` | `node Write the approval activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Change request` | `node Write the go-live and budget activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Mark notification read` | `node Find the notification` | object `Delivery Command · Notification` | storage read |  |
| automation `Delivery Command · Mark notification read` | `node Mark it read` | object `Delivery Command · Notification` | storage write |  |
| automation `Delivery Command · Confirm upload` | `node Find the project` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Confirm upload` | `node Save the confirmed upload` | object `Delivery Command · Upload` | storage write |  |
| automation `Delivery Command · Confirm upload` | `node Write the activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Save view` | `node Save the view` | object `Delivery Command · Saved view` | storage write |  |
| automation `Delivery Command · Update project settings` | `node Find the project` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Update project settings` | `node Save the number setting` | object `Delivery Command · Project` | storage write |  |
| automation `Delivery Command · Update project settings` | `node Save the text setting` | object `Delivery Command · Project` | storage write |  |
| automation `Delivery Command · Update project settings` | `node Write the activity row` | object `Delivery Command · Activity` | storage write |  |
| automation `Delivery Command · Read delivery data` | `node Read matching projects` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching tasks` | object `Delivery Command · Task` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching raid` | object `Delivery Command · RAID item` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching bookings` | object `Delivery Command · Booking` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching people` | object `Delivery Command · Person` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching time_entries` | object `Delivery Command · Time entry` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching signoffs` | object `Delivery Command · Sign-off` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching ai_outputs` | object `Delivery Command · AI output` | storage read |  |
| automation `Delivery Command · Read delivery data` | `node Read matching weekly_snapshots` | object `Delivery Command · Weekly snapshot` | storage read |  |
| automation `Delivery Command · Send executive summary` | `node Latest weekly metric` | object `Delivery Command · Weekly metric` | storage read |  |
| automation `Delivery Command · Send executive summary` | `node Latest weekly snapshot` | object `Delivery Command · Weekly snapshot` | storage read |  |
| automation `Delivery Command · Send executive summary` | `node Active projects in the region` | object `Delivery Command · Project` | storage read |  |
| automation `Delivery Command · Send executive summary` | `node Activity of the last 7 days` | object `Delivery Command · Activity` | storage read |  |
| automation `Delivery Command · Send executive summary` | `node Save the email as a preview (no mail connection is named)` | object `Delivery Command · Executive email` | storage write |  |
| automation `Delivery Command · Weekly executive email schedule` | `node Send that region's executive summary` | automation `Delivery Command · Send executive summary` | call node |  |

## Not checked

- ai-agent `Delivery Command · Copilot` (e_6adbabd2925d282255cee62b): its tools are not in the cache (get_agent)
