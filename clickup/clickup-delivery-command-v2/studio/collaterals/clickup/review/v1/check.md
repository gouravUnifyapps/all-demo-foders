# Consistency check

**0 must fix · 3 to verify**

## Must fix

- none

## Verify

- e1: no screen text yet (run capture)
- e2: no screen text yet (run capture)
- e1: told, not shown? "Under the hood, the refusal came from one automation, Book consultant." (nothing on screen is cued in this sentence; show it, or check the screen has the button/state that makes it true)

## Read as the viewer (do this yourself, every version)

For each scene: does anything on this screen contradict the voice, an earlier screen, or another panel on the same screen (an AI summary vs the record it summarises; a status vs a date; a claim like "sends it" vs the buttons that exist)? Would someone who runs this business believe every sentence?

### a1 · Portfolio

**Voice:** Monday morning. Ines Moreau, the delivery director, opens Portfolio: 14 on track, 4 at risk, up one, and 2 off track, up one, since last week. A risk card, marked AI-written, flags Halden Freight with high confidence and shows its evidence. On the risk grid, the migration risk sits at likelihood 4 and impact 4, and the trend has fallen to 70 percent on track. She filters to Europe and At risk: 2 of 20 projects. A note says the Jira sync has failed since 06:40.

**Screen text:**

~~~
Portfolio
Projects
Resourcing
Timesheets
Changes
Admin
G
Gourav
gourav.mahunta@unifyapps.com
Portfolio
Search projects
6
G
DELIVERY PORTFOLIO
Portfolio

20 implementations · health as of Oct 23, 2026

Weekly summary
JIRA
Sync failed

Jira sync failed

Jira sync failed since 06:40 today: 3 escalation links on Halden Freight and Northgate Logistics not updated · Last updated Oct 22, 06:40 AM
On track
14
−2 since last week
At risk
4
+1 since last week
Off track
2
+1 since last week
On-track share
LAST 12 WEEKS · % OF PROJECTS
70%
−15 pts in 12 weeks
Aug 3
Aug 10
Aug 17
Aug 24
Aug 31
Sep 7
Sep 14
Sep 21
Sep 28
Oct 5
Oct 19
0%
25%
50%
75%
100%
AI INSIGHT · RISK PREDICTION
Halden Freight may miss its Nov 27, 2026 go-live
3 of 8 migration tasks are late (longest 6 days)
Migration plan v2 sign-off is due 28 Oct and not yet approved
Tomas Brandt is booked 100% in week 45

AI-written · IMP-2611 · lead Mira Castell

Confidence High
Open project 
Open risks
LIKELIHOOD BY IMPACT · COUNT
17 OPEN
L \ I	1	2	3	4	5
5	·	·	·	
1	
1
4	·	
1	·	
1	
1
3	·	
1	
1	
2	·
2	·	
1	
2	
1	
1
1	
1	
1	·	
1	·

Choose a cell to list its risks.

Go-lives in the next 90 days
PROJECTS BY REGION
On schedule
Slipped
0
2
4
5
Europe
North America
Japan
Slipped
Northgate Logistics Nov 19, was Nov 5
Slipped
Hokuto Rail Dec 18, was Dec 4
Projects
20 OF 20 PROJECTS
Search projects
Region
Stage
Health
Lead
Saved views
Save view
CUSTOMER	REGION	STAGE	GO-LIVE	HEALTH	LEAD

MS
Marlow Studios
IMP-2626
	Europe	Hypercare	
Oct 1, 2026
	
On track	Sofia Lind

OR
Ostrander Retail
IMP-2616
	North America	Hypercare	
Oct 6, 2026
	
On track	Dev Okafor

LM
Lindqvist Marine
IMP-2623
	Europe	Go-live	
Oct 30, 2026
	
On track	Mira Castell

GO
Granite Peak Outdoor
IMP-2629
	North America	Go-live	
Nov 3, 2026
	
On track	Dev Okafor

SM
Sakura Mobility
IMP-2615
	Japan	Go-live	
Nov 5, 2026
	
At risk	Haruto Mori

BU
Brightmoor University
IMP-2613
	Europe	Training	
Nov 10, 2026
	
On track	Mira Castell

RC
Redfern Clinics
IMP-2624
	North America	Training	
Nov 13, 2026
	
On track	Priya Nair

NL
Northgate Logistics
IMP-2618
	North America	Migration	
Nov 19, 2026
Slipped
	
Off track	Dev Okafor

TE
Tamura Electronics
IMP-2619
	Japan	Training	
Nov 24, 2026
	
On track	Haruto Mori

HF
Halden Freight
IMP-2611
	Europe	Migration	
Nov 27, 2026
	
At risk	Mira Castell
1–10 OF 20
1
2
Delivery Copilot
Read-only
Chat
History
C

ClickUp Delivery Copilot

Read-only Delivery Copilot for ClickUp Delivery Command: answers delivery questions with linked re
~~~

### a2 · Project overview

**Voice:** She opens Halden Freight. The seven-stage path stands at Migration, with go-live on November 27, 512 of 640 budget hours used, 5 open RAID items, and Migration plan v2 due on October 28. The Migration column holds 16 tasks against a 15 task limit, and says so. Mira Castell, the lead, moves Validate pilot batch on to Training from the card's menu, the keyboard path. The move is recorded, and the task detail opens beside the board.

**Screen text:**

~~~
Portfolio
Projects
Resourcing
Timesheets
Changes
Admin
G
Gourav
gourav.mahunta@unifyapps.com
Project overview
Search projects
6
G
Portfolio
Europe
Halden Freight · IMP-2611
IMPLEMENTATION · MIRA CASTELL
Halden Freight
At risk
Go-live Nov 27, 2026
Draft status report
Kickoff
Discovery
Configuration
Migration
Training
Go-live
Hypercare
DAYS TO GO-LIVE
35
Nov 27, 2026
BUDGET HOURS
512 of 640 h
80% used
OPEN RAID ITEMS
5
2 risks
NEXT CUSTOMER SIGN-OFF
Migration plan v2
Due Oct 28
Board
List
Timeline
RAID
Documents
Activity
Settings

Drag a card to another stage, or use its menu to move it with the keyboard.

KICKOFF
1 of 15
T-2611-01
Kickoff workshop
Done
Mira Castell
DISCOVERY
1 of 15
T-2611-02
Discovery interviews
Done
Mira Castell
CONFIGURATION
2 of 15
T-2611-03
Workspace configuration
Done
Elif Demir
T-2611-04
Permission model
Done
Lena Vogt
MIGRATION
16 of 15
Over the 15-task limit by 1
T-2611-05
Extract legacy projects
Done
Tomas Brandt
T-2611-06
Map custom fields
Done
Lena Vogt
T-2611-07
Clean duplicate users
Done
Elif Demir
T-2611-08
Load pilot batch
Done
Tomas Brandt
T-2611-09
Validate pilot batch
Done
Lena Vogt
T-2611-13
Reconcile record counts
Not started
Lena Vogt
T-2611-14
Migrate attachments
Not started
Elif Demir
T-2611-15
Rebuild automations
In progress
Elif Demir
T-2611-16
Map integrations
In progress
Mira Castell
T-2611-17
Data quality sign-off pack
Not started
Lena Vogt
T-2611-18
Cutover runbook
Not started
Mira Castell
T-2611-10
Load batch 1 (Logistics ops)
In progress
Tomas Brandt · Oct 23
T-2611-11
Load batch 2 (Finance)
Not started
Tomas Brandt · Nov 6
T-2611-12
Load batch 3 (Warehouses)
Not started
Tomas Brandt · Nov 13
T-2611-19
Cutover rehearsal
Not started
Tomas Brandt · Nov 20
T-2611-20
Go-live readiness review
Blocked
Mira Castell · Nov 26
TRAINING
0 of 15
GO-LIVE
0 of 15
HYPERCARE
0 of 15
Delivery Copilot
Read-only
Chat
History
C

ClickUp Delivery Copilot

Read-only Delivery Copilot for ClickUp Delivery Command: answers delivery questions with linked records or charts and drafts weekly status reports.

Which Europe projects go live in November and are at risk?

Draft this week's status report for Halden Freight

Show go-lives by month

When Delivery Copilot cannot answer, it says why. Try naming the project id (for example IMP-2611), a region or a month, and ask one thing at a time.
~~~

### b1 · The refusal: over capacity

**Voice:** As resource manager, she books Tomas Brandt onto Halden Freight for 8 hours a week in the weeks of November 2 and November 9, from a form, with no dragging. The app refuses before anything is saved. Over capacity: Tomas would be at 120 percent in the week of November 2, eight hours over, and 105 percent in the week of November 9, two hours over. She filters the skills matrix to data migration, finds Lena Vogt, and books her instead.

**Screen text:**

~~~
Portfolio
Projects
Resourcing
Timesheets
Changes
Admin
G
Gourav
gourav.mahunta@unifyapps.com
Resourcing
Search projects
6
G
RESOURCING
Consultants and capacity

Book consultants by week. A booking that takes anyone over 100% of their weekly capacity is refused before it saves.

Grid
Skills
Timesheets
Capacity
Booked share of weekly capacity
12 WEEKS FROM OCT 26 · 1 OVER CAPACITY
CONSULTANT	OCT 26	NOV 2	NOV 9	NOV 16	NOV 23	NOV 30	DEC 7	DEC 14	DEC 21	DEC 28	JAN 4	JAN 11
Aiko Tanaka
Japan · 40 h
	·	·	·	
110% Over	·	·	·	·	·	·	·	·
Dev Okafor
North America · 40 h
	·	65%	·	·	·	·	·	·	·	·	·	·
Elif Demir
Europe · 40 h
	·	90%	·	60%	·	·	·	·	·	·	·	·
Haruto Mori
Japan · 40 h
	·	·	75%	·	·	·	·	·	·	·	·	·
Kenji Ono
Japan · 40 h
	·	·	80%	·	·	·	·	·	·	·	·	·
Lena Vogt
Europe · 40 h
	·	100%	80%	·	·	·	·	·	·	·	·	·
Marcus Bell
North America · 40 h
	80%	75%	·	·	·	·	·	·	·	·	·	·
Mira Castell
Europe · 40 h
	60%	·	·	·	·	·	·	·	·	·	·	·
Nora Quist
Europe · 32 h
	88%	·	94%	·	·	·	·	·	·	·	·	·
Priya Nair
North America · 40 h
	·	·	·	70%	·	·	·	·	·	·	·	·
Sam Whitlow
North America · 40 h
	60%	·	·	·	·	·	·	·	·	·	·	·
Tomas Brandt
Europe · 40 h
	·	100%	85%	·	·	·	·	·	·	·	·	·
Book consultant
PERSON *
Choose a consultant
Aiko Tanaka · 40 h a week
Dev Okafor · 40 h a week
Elif Demir · 40 h a week
Haruto Mori · 40 h a week
Kenji Ono · 40 h a week
Lena Vogt · 40 h a week
Marcus Bell · 40 h a week
Mira Castell · 40 h a week
Nora Quist · 32 h a week
Priya Nair · 40 h a week
Sam Whitlow · 40 h a week
Tomas Brandt · 40 h a week
PROJECT *
Choose a project
Marlow Studios · IMP-2626
Ostrander Retail · IMP-2616
Lindqvist Marine · IMP-2623
Granite Peak Outdoor · IMP-2629
Sakura Mobility · IMP-2615
Brightmoor University · IMP-2613
Redfern Clinics · IMP-2624
Northgate Logistics · IMP-2618
Tamura Electronics · IMP-2619
Halden Freight · IMP-2611
Vellmar Insurance · IMP-2617
Pinecrest Media · IMP-2621
Eskel Foods · IMP-2628
Corvia Health · IMP-2612
Hokuto Rail · IMP-2625
Kawase Logistics · IMP-2630
Aoba Pharma · IMP-2622
Kestrel Energy · IMP-2614
Calder Bank · IMP-2620
Bayview Credit Union · IMP-2627
WEEKS *
Oct 26
Nov 2
Nov 9
Nov 16
Nov 23
Nov 30
Dec 7
Dec 14
Dec 21
Dec 28
Jan 4
Jan 11
Weeks start on Monday.
HOURS PER WEEK *
Book
Delivery Copilot
Read-only
Chat
History
C

ClickUp Delivery Copilot

Read-only Delivery Copilot for ClickUp Delivery Command: answers delivery questions with linked records or charts and drafts weekly status reports.

Which Europe projects go live in November and are at risk?

Draft this week's
~~~

### b2 · Change request

**Voice:** To protect the date, Mira raises a change request: a third migration batch, 48 extra hours, 7,200 euros of cost, and 7 days to the go-live. Before submitting, she sees the plan before and after, side by side, with the differences marked. At 40 hours or more, it routes to Ines Moreau, the delivery director, then Raj Patel, the finance partner. Both approve, and Halden Freight's go-live moves to December 4.

**Screen text:**

~~~
Portfolio
Projects
Resourcing
Timesheets
Changes
Admin
G
Gourav
gourav.mahunta@unifyapps.com
New change request
Search projects
6
G
Portfolio
Halden Freight
New change request
CHANGE REQUEST · IMP-2611
New change request

Go-live today: Nov 27, 2026 · budget 640 h planned

REASON *
WORK
Work added
Work removed
WHAT IS ADDED
HOURS *
COST (EUR)
GO-LIVE EFFECT (DAYS)
Positive moves go-live later.
Submit
Cancel
APPROVAL PATH

Enter the hours to see who approves. Under 40 hours the delivery director decides; at 40 hours or more, the director and then the finance partner.

Delivery Copilot
Read-only
Chat
History
C

ClickUp Delivery Copilot

Read-only Delivery Copilot for ClickUp Delivery Command: answers delivery questions with linked records or charts and drafts weekly status reports.

Which Europe projects go live in November and are at risk?

Draft this week's status report for Halden Freight

Show go-lives by month




When Delivery Copilot cannot answer, it says why. Try naming the project id (for example IMP-2611), a region or a month, and ask one thing at a time.
~~~

### c1 · Customer portal

**Voice:** Now the customer's side. Katrin Albers, Halden Freight's sponsor, opens the portal in German. She sees only her own project: stage, milestones, sessions, open actions and shared documents, with no internal health score, and dates written the German way, like 28.10.2026. Under Freigaben, she signs off Migration plan v2. The sign-off records who approved and when, and lands in the project's activity feed.

**Screen text:**

~~~
Start
Freigaben
Schulungen
Dateien
Prüfliste
English
Deutsch
日本語
HF
Katrin Albers
Halden Freight
HALDEN FREIGHT · IMP-2611
Willkommen, Katrin Albers

Ihr Go-live ist für den 27.11.2026 geplant.

Wo Ihr Projekt steht
Kickoff
Analyse
Konfiguration
Migration
Schulung
Go-live
Hypercare
Meilensteine
Discovery report
12.09.2026
Analyse · Freigegeben
Configuration workbook
02.10.2026
Konfiguration · Freigegeben
3
Migration plan v2
28.10.2026
Migration · Wartet auf Freigabe
4
Training plan
12.11.2026
Schulung · Wartet auf Freigabe
Offene Aufgaben
Migration plan v2 freigeben
Öffnen
Training plan freigeben
Öffnen
Onboarding-Prüfliste beantworten (3 nicht festgelegt)
Öffnen
Anstehende Schulungen
10:00
Admin training
Montag, 16. November
Gebucht
10:00
Admin training
Dienstag, 17. November
Gebucht
Geteilte Dokumente
DOKUMENT	GETEILT	VON
Sign-off record: Configuration workbook	16.10.2026	Mira Castell
Migration plan v2	30.09.2026	Mira Castell
Statement of work	28.08.2026	Mira Castell
~~~

### d1 · Weekly summary

**Voice:** Every Monday, the VP of customer success reads one page. Six headline numbers show their change from last week, coloured by whether it is good or bad for the business: 6 projects at risk, 2 more than last week, shown as bad. The contract value bridge runs from 4.05 million at the start to 4.21 million at the end, in US dollars. Below sit the 5 projects that changed most, each with its reason, and a sample of the 08:00 Monday email for each region, shown here, not sent. In this demo, the summary is a seeded weekly snapshot.

**Screen text:**

~~~
Portfolio
Projects
Resourcing
Timesheets
Changes
Admin
G
Gourav
gourav.mahunta@unifyapps.com
Weekly summary
Search projects
6
G
WEEKLY SUMMARY
Week of Oct 19, 2026

What moved across the portfolio since last week. Totals are in USD.

Open Portfolio
ACTIVE PROJECTS
18 projects
+1 project from last week
GO-LIVES THIS MONTH
3 go-lives
No change from last week
PROJECTS AT RISK
6 projects
+2 projects from last week
AVERAGE DAYS TO GO-LIVE
47 days
+3 days from last week
CONSULTANT UTILISATION
91%
+3% from last week
CONTRACT VALUE AWAITING GO-LIVE
$4.2M
+$160K from last week
Contract value bridge
USD · START TO END OF WEEK
Start
New
Completed
Slipped
Cancelled
End
$0.00
$1.50M
$3.00M
$4.50M
$6.00M
$4.05M
$4.46M
$4.46M
$4.28M
$4.21M
Contract value
Added
Taken away
Five projects that changed most
#	PROJECT	HEALTH	WHY IT CHANGED
1	Halden Freight
IMP-2611
	
At risk	Health moved to At risk: migration tasks late
2	Hokuto Rail
IMP-2625
	
Off track	Health moved to Off track: go-live slipped 14 days
3	Northgate Logistics
IMP-2618
	
Off track	Go-live slipped 14 days
4	Sakura Mobility
IMP-2615
	
At risk	Second cutover rehearsal booked
5	Calder Bank
IMP-2620
	
On track	New project from won deal
Monday 08:00 email
Preview
PREVIEW ONLY

This is what each region would receive at 08:00 local time on Monday. Nothing is sent from this screen.

EUROPE · EUROPE/BERLIN
Monday, October 26 at 08:00 AM
Your time: Oct 26, 07:00 AM
Delivery summary, week of Oct 19, 2026
Active projects: 18 projects
Go-lives this month: 3 go-lives
Projects at risk: 6 projects
Average days to go-live: 47 days
Consultant utilisation: 91%
Contract value awaiting go-live: $4.2M
Most changed: Halden Freight, Health moved to At risk: migration tasks late
NORTH AMERICA · AMERICA/NEW_YORK
Monday, October 26 at 08:00 AM
Your time: Oct 26, 12:00 PM
Delivery summary, week of Oct 19, 2026
Active projects: 18 projects
Go-lives this month: 3 go-lives
Projects at risk: 6 projects
Average days to go-live: 47 days
Consultant utilisation: 91%
Contract value awaiting go-live: $4.2M
Most changed: Halden Freight, Health moved to At risk: migration tasks late
JAPAN · ASIA/TOKYO
Monday, October 26 at 08:00 AM
Your time: Oct 25, 11:00 PM
Delivery summary, week of Oct 19, 2026
Active projects: 18 projects
Go-lives this month: 3 go-lives
Projects at risk: 6 projects
Average days to go-live: 47 days
Consultant utilisation: 91%
Contract value awaiting go-live: $4.2M
Most changed: Halden Freight, Health moved to At risk: migration tas
~~~

### d2 · Delivery Copilot and the status report

**Voice:** Back on Halden Freight, Mira opens Delivery Copilot, a read-only AI agent, with 3 suggested questions. She asks which Europe projects go live in November and are at risk. The panel shows the step it is working on, then answers Halden Freight, with a link to the project. Then she asks for this week's status report. The AI-written draft cites the late migration tasks, the migration risk, and 512 of 640 budget hours. She brings it into the report, edits one line and publishes, well inside the 10 minute target.

**Screen text:**

~~~
Portfolio
Projects
Resourcing
Timesheets
Changes
Admin
G
Gourav
gourav.mahunta@unifyapps.com
Status report
Search projects
6
G
Portfolio
Halden Freight
Status report
STATUS REPORT · IMP-2611
Halden Freight

Check the AI-written draft, edit it, then publish. Export it as PDF or Word for the customer.

WRITTEN BY THE LEAD
TITLE
REPORT *
Draft for the week of Oct 19, 2026
Ask Copilot for a draft
Use Copilot draft
Export PDF
Word
Publish
Proposed tasks
From the meeting summary. Nothing is created until you accept it.
PROPOSAL	SOURCE	STATUS	
DECISION

Book second cutover rehearsal
PT-2611-1 · AI-written
	Transcript t3	
Proposed	
Accept
Reject

Send user list template to Katrin Albers
PT-2611-2 · AI-written
	Transcript t7	
Proposed	
Accept
Reject

Add Warehouses batch owner
PT-2611-3 · AI-written
	Transcript t12	
Proposed	
Accept
Reject

Reschedule steering call to 28 Oct
PT-2611-4 · AI-written
	Transcript t1	
Rejected	
Meeting summary
AI-written
MS-2611-1020 · STEERING CALL 20 OCT
Decision
Transcript t3

Go-live stays on 27 November if the second cutover rehearsal is booked this week.

Action
Transcript t7

Mira Castell sends the user list template to Katrin Albers by Wednesday.

Risk
Transcript t12

The Warehouses batch has no owner; RSK-1183 likelihood raised to High.

TRANSCRIPT

t1 Ines Moreau: Thanks all, let's start with the go-live date.

t2 Katrin Albers: We still want 27 November.

t3 Ines Moreau: Then we keep 27 November, provided we book the second cutover rehearsal this week.

t4 Mira Castell: I can hold the 3 November slot for it.

t5 Katrin Albers: Good. On users, the pilot list is in.

t6 Katrin Albers: For the full list I need the template from you.

t7 Mira Castell: I'll send you the user list template by Wednesday.

t8 Ines Moreau: Any blockers on migration?

t9 Mira Castell: Migration plan v2 is shared, no blockers there.

t10 Katrin Albers: The Warehouses team is the open question.

t11 Ines Moreau: Nobody owns that batch yet?

t12 Mira Castell: Correct, so I'm raising RSK-1183 to high likelihood until we have a Warehouses batch owner.

Delivery Copilot
Read-only
Chat
History
C

ClickUp Delivery Copilot

Read-only Delivery Copilot for ClickUp Delivery Command: answers delivery questions with linked records or charts and drafts weekly status reports.

Which Europe projects go live in November and are at risk?

Draft this week's status report for Halden Freight

Show go-lives by month

When Delivery Copilot cannot answer, it says why. Try nami
~~~

### e1 · Book consultant on the canvas

**Voice:** Under the hood, the refusal came from one automation, Book consultant. On its canvas, it reads the consultant, the project and every booking, adds the new hours week by week against weekly capacity, and refuses any week over 100 percent without writing anything.

**Screen text:**

~~~
(not captured)
~~~

### e2 · Delivery Copilot in the agent builder

**Voice:** The Copilot is set up in the agent builder: plain instructions, one tool that reads delivery data, and a chart tool. It has no tool that writes, so it drafts and explains, and people decide and publish.

**Screen text:**

~~~
(not captured)
~~~

