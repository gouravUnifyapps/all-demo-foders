# Solution map

Solution: `Clickup · ClickUp Delivery command platform` (e_6adb4b845236864dd8b18935) · tenant orbit.uat.unifyapps.com

## Entities

| Kind | Name | Id | Version | Stale |
|---|---|---|---|---|
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

## Wiring

| From | Part | To | Via | Fields |
|---|---|---|---|---|
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

## Not checked

- none
