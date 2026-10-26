---
nebula: 3
slug: "clickup-delivery-command-app"
name: "ClickUp Delivery Command app"
summary: "The code app: executive summary, portfolio, project workspace, change approvals, resourcing, timesheets, Copilot panel, customer portal, phone view and admin."
entities: [{"kind":"code-app","name":"ClickUp Delivery Command"}]
planIds: ["e_6adf4e82769c8b649ebf1b17","e_6adf5240769c8b649ebf944c","e_6adf5ef808f965795444ffac"]
updatedAt: "2026-10-26T14:36:31.469Z"
---
## What it does
One PRIVATE code app (app-a2a9509a82c1) for ClickUp's implementation team and customer sponsors. Routes: /summary, /portfolio, /projects/:code (tabs list, board, timeline, raid, documents, activity, settings), /projects/:code/change, /changes, /changes/:code, /resourcing, /timesheets, /admin, /portal/home, /portal/signoffs, /portal/sessions, /portal/files, /portal/checklist, /m/today, /m/tasks, /m/time, /m/alerts. A persona switcher in the profile menu (view as) picks Kenji Arai, Elena Fischer, Marcus Bell, Tom Hale, Yui Sato, Haruto Mori or Grace Lin; it controls no access. Appearance switches light (default) and dark.

## How it works
The stylesheet app/src/styles/design-system.css is studio/design-system/clickup/client.css with Google Fonts imports; shell.css sets Inter and Noto Sans JP. Records are read through the app's Storage data sources (FETCH e_6adf5087dc07493166cf01c2) from the OBJ_cucmd_* objects, filtered in the browser. Every write goes through a deployed ClickUp Command automation called from app/src/data/callables.ts. Portal strings in EN, DE and JA come from a portal-only table (German and Japanese drafted for client review). Charts use recharts inside the kit's .chart.

## Known limits
Deep links on the published address answer 404 before sign-in; open the root. Update task answers result `save` and Raise change request `submit` (the contract says saved and submitted); the app accepts both. Published v2 at commit 9142bfc0.