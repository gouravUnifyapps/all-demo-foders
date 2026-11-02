"""Synthetic, fictional seed data for the Noventiq demo. Deterministic (seeded RNG)."""
import csv, json, random, sys, os
from collections import defaultdict

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
rnd = random.Random(1110)

Q = ["Q4 2025", "Q1 2026", "Q2 2026", "Q3 2026"]
QEND = {"Q4 2025": "2025-12-31", "Q1 2026": "2026-03-31", "Q2 2026": "2026-06-30", "Q3 2026": "2026-09-30"}
ENT = {
    "embee": {"label": "Embee", "country": "India", "landscape": "typical", "crm": "dynamics365", "erp": "sapb1", "time": "zoho_projects", "payroll": "payroll_in", "rate": 28, "cur": "INR"},
    "nqai": {"label": "NQ AI", "country": "India", "landscape": "hard", "crm": "blackandwhite", "erp": "tally", "time": "azure_devops", "payroll": "payroll_in", "rate": 32, "cur": "INR"},
    "entc": {"label": "Entity C", "country": "Country C (to be named)", "landscape": "easy", "crm": "creatio", "erp": "netsuite", "time": "netsuite", "payroll": "netsuite", "rate": 55, "cur": "USD"},
}
FX = {"INR": 84.0, "USD": 1.0}
SVC = {"cloud": "Cloud (Azure, AWS)", "licensing": "Software licensing", "security": "Cybersecurity", "managed": "Managed services", "ai_data": "AI and data"}
LOCAL = {  # erp -> service -> local code
    "sapb1": {"cloud": "AZ-CSP", "licensing": "M365-LIC", "security": "SEC-SOC", "managed": "MS-AMS", "ai_data": "AI-DAT"},
    "tally": {"cloud": "CLD01", "licensing": "LIC-MS", "security": "SEC01", "managed": "SRV-099", "ai_data": "AIP-01"},
    "netsuite": {"cloud": "4100-Cloud", "licensing": "4200-License", "security": "4300-Services", "managed": "4300-Services", "ai_data": "4400-Data"},
}
PEOPLE_SVC = {"security", "managed", "ai_data"}
REV = {"cloud": (60000, 140000), "licensing": (80000, 220000), "security": (25000, 60000), "managed": (30000, 70000), "ai_data": (20000, 50000)}
COST = {"cloud": 0.86, "licensing": 0.91, "security": 0.35, "managed": 0.30, "ai_data": 0.25}
HRS = {"security": (300, 520), "managed": (420, 700), "ai_data": (260, 460)}

ACC = [
    ("NQ-ACC-0001", "Aster Pharma", "embee", "Enterprise", ["licensing", "security"], ""),
    ("NQ-ACC-0002", "Kestrel Logistics", "entc", "Enterprise", ["cloud", "managed"], ""),
    ("NQ-ACC-0003", "Bluepeak Bank", "embee", "Enterprise", ["licensing", "cloud"], ""),
    ("NQ-ACC-0004", "Orchid Hotels", "nqai", "SMB", ["licensing"], ""),
    ("NQ-ACC-0005", "Vantara Motors", "embee", "Enterprise", ["cloud"], ""),
    ("NQ-ACC-0006", "Solace Health", "entc", "SMB", ["licensing"], ""),
    ("NQ-ACC-0007", "Meridian Retail Group", "embee", "Enterprise", ["licensing", "cloud"], ""),
    ("NQ-ACC-0008", "Tarang Telecom", "nqai", "Enterprise", ["ai_data", "licensing"], ""),
    ("NQ-ACC-0009", "Ironleaf Manufacturing", "entc", "SMB", ["cloud"], ""),
    ("NQ-ACC-0010", "Crescent Insurance", "embee", "SMB", ["licensing"], ""),
    ("NQ-ACC-0011", "Lumen Edtech", "nqai", "SMB", ["ai_data"], ""),
    ("NQ-ACC-0012", "Halcyon Energy", "entc", "Enterprise", ["licensing", "managed"], ""),
    ("NQ-ACC-0013", "Meridian Fashion", "embee", "SMB", ["licensing"], "NQ-ACC-0007"),
]
STORY = "NQ-ACC-0007"
SYS_LABEL = {"creatio": "Creatio", "dynamics365": "Dynamics 365", "blackandwhite": "Black and White", "netsuite": "NetSuite", "sapb1": "SAP B1",
             "tally": "Tally", "payroll_in": "Payroll India", "zoho_projects": "Zoho Projects", "azure_devops": "Azure DevOps"}
PFX = {"creatio": "CR", "dynamics365": "D", "blackandwhite": "BW", "netsuite": "NS", "sapb1": "SB1", "tally": "T", "payroll_in": "PAY", "zoho_projects": "ZP", "azure_devops": "ADO"}

src, links, gp, opps, runs, exc, defs, plays, hist, closes = [], [], [], [], [], [], [], [], [], []
cnt = defaultdict(int)

def sid(system, kind):
    cnt[(system, kind)] += 1
    return f"{PFX[system]}-{kind}-{1000 + cnt[(system, kind)] * 7}"

# sync runs: latest copy per system, plus live read for CRMs, plus one failed ADO run
run_id = {}
rn = 300
for s in SYS_LABEL:
    rn += 1
    mode = "live_read" if s in ("creatio", "dynamics365", "blackandwhite") else "copy_nightly"
    if s == "payroll_in":
        mode = "copy_monthly"
    run_id[s] = f"SR-{rn:04d}"
    runs.append(dict(run_id=run_id[s], system=s, mode=mode, started="2026-11-01T22:00:00Z", status="ok", rows_read=0, rows_changed=0, errors=0, note=""))
rn += 1
runs.append(dict(run_id=f"SR-{rn:04d}", system="azure_devops", mode="copy_nightly", started="2026-11-02T22:00:00Z", status="failed", rows_read=0, rows_changed=0, errors=1,
                 note="Timeout after 120 s reading work-item time logs (page 3 of 5)"))
FAILED_RUN = f"SR-{rn:04d}"

def add_src(**k):
    k.setdefault("currency", ENT[k["entity"]]["cur"] if k.get("entity") else "USD")
    k.setdefault("last_modified", "2026-11-01T21:40:00Z")
    k["sync_run"] = run_id[k["system"]]
    for f in ["customer_ref", "customer_name", "account_key", "quarter", "service_code", "service", "amount_usd", "amount_local", "cost_usd", "hours", "planned_hours", "vendor", "segment", "stage_local", "earned_quarter", "attributed_quarter", "note"]:
        k.setdefault(f, "")
    if k["amount_usd"] != "" and k["amount_local"] == "":
        k["amount_local"] = round(k["amount_usd"] * FX[k["currency"]])
    src.append(k)
    runs_by = next(r for r in runs if r["run_id"] == k["sync_run"])
    runs_by["rows_read"] += 1
    return k

# CRM + ERP customer records and links
def norm(n):
    return n
for key, name, e, seg, svcs, parent in ACC:
    E = ENT[e]
    crm_id = sid(E["crm"], "ACC")
    erp_id = sid(E["erp"], "C")
    crm_name = {"dynamics365": f"{name} Pvt Ltd", "blackandwhite": name.upper(), "creatio": f"{name} LLC"}[E["crm"]]
    erp_name = {"sapb1": f"{name.upper()} PVT. LTD.", "tally": f"{name} Ltd", "netsuite": f"{name}, LLC"}[E["erp"]]
    add_src(system=E["crm"], entity=e, record_type="account", source_id=crm_id, customer_ref=crm_id, customer_name=crm_name, account_key=key, segment=seg)
    add_src(system=E["erp"], entity=e, record_type="customer", source_id=erp_id, customer_ref=erp_id, customer_name=erp_name, account_key=key, segment=seg)
    m1 = "tax_id" if e != "nqai" else "normalized_name"
    m2 = "tax_id" if e != "nqai" else ("ai_suggested" if key == "NQ-ACC-0004" else "normalized_name")
    links.append(dict(link_id=f"LNK-{len(links)+1:03d}", account_key=key, system=E["crm"], source_id=crm_id, source_name=crm_name, method=m1, confidence=1.0 if m1 == "tax_id" else 0.93, status="matched", confirmed_by="rule" if m1 != "ai_suggested" else "Kavya Rao"))
    links.append(dict(link_id=f"LNK-{len(links)+1:03d}", account_key=key, system=E["erp"], source_id=erp_id, source_name=erp_name, method=m2, confidence=1.0 if m2 == "tax_id" else (0.88 if m2 == "ai_suggested" else 0.95), status="matched", confirmed_by="Kavya Rao" if m2 == "ai_suggested" else "rule"))
    ACC_ERP = None

# Meridian's NQ AI side: unmatched
bw = add_src(system="blackandwhite", entity="nqai", record_type="account", source_id="BW-ACC-7731", customer_ref="BW-ACC-7731", customer_name="Meridian Rtl Grp", account_key="", segment="Enterprise")
tc = add_src(system="tally", entity="nqai", record_type="customer", source_id="T-C-0441", customer_ref="T-C-0441", customer_name="MERIDIAN RTL GRP (NQ AI)", account_key="", segment="Enterprise")
links.append(dict(link_id=f"LNK-{len(links)+1:03d}", account_key="NQ-ACC-0007", system="blackandwhite", source_id="BW-ACC-7731", source_name="Meridian Rtl Grp", method="ai_suggested", confidence=0.86, status="needs_review", confirmed_by=""))
links.append(dict(link_id=f"LNK-{len(links)+1:03d}", account_key="NQ-ACC-0007", system="tally", source_id="T-C-0441", source_name="MERIDIAN RTL GRP (NQ AI)", method="ai_suggested", confidence=0.84, status="needs_review", confirmed_by=""))

erp_cust = {r["account_key"]: r["source_id"] for r in src if r["record_type"] == "customer" and r["account_key"]}

# invoices -> GP lines (seed basis)
lines = {}
for key, name, e, seg, svcs, parent in ACC:
    E = ENT[e]
    for s in svcs:
        for q in Q:
            lo, hi = REV[s]
            rev = round(rnd.uniform(lo, hi), -2)
            if key == STORY and s == "licensing":
                rev = {"Q4 2025": 182400, "Q1 2026": 176800, "Q2 2026": 194200, "Q3 2026": 201600}[q]
            if key == STORY and s == "cloud":
                rev = {"Q4 2025": 96400, "Q1 2026": 104800, "Q2 2026": 112600, "Q3 2026": 118200}[q]
            cost = round(rev * COST[s], -2)
            inv = add_src(system=E["erp"], entity=e, record_type="invoice", source_id=sid(E["erp"], "INV"), customer_ref=erp_cust[key], customer_name="", account_key=key,
                          quarter=q, service_code=LOCAL[E["erp"]][s], service=s, amount_usd=rev, cost_usd=cost, last_modified=QEND[q] + "T18:00:00Z")
            lines[(q, key, s)] = dict(quarter=q, account_key=key, entity=e, service=s, revenue=rev, cost=cost, people=0, rebate=0, src=[inv["source_id"]])

# NQ AI invoice of the unmatched Meridian side, Q3 only
inv = add_src(system="tally", entity="nqai", record_type="invoice", source_id="T-INV-3391", customer_ref="T-C-0441", customer_name="MERIDIAN RTL GRP (NQ AI)", account_key="",
              quarter="Q3 2026", service_code="AIP-01", service="ai_data", amount_usd=12600, cost_usd=3200, last_modified="2026-09-28T11:20:00Z")
lines[("Q3 2026", "UNASSIGNED", "ai_data")] = dict(quarter="Q3 2026", account_key="UNASSIGNED", entity="nqai", service="ai_data", revenue=12600, cost=3200, people=0, rebate=0, src=["T-INV-3391"])

# timesheets (people cost) per people-based line
MISSING = None
for (q, key, s), L in sorted(lines.items()):
    if s not in PEOPLE_SVC:
        continue
    E = ENT[L["entity"]]
    lo, hi = HRS[s]
    planned = int(rnd.uniform(lo, hi) / 2) * 2
    if key == "UNASSIGNED":
        planned = 60
    hours = planned
    if key == "NQ-ACC-0011" and q == "Q3 2026":
        hours = planned - 46
        MISSING = (q, key, s)
    ts = add_src(system=E["time"], entity=L["entity"], record_type="timesheet", source_id=sid(E["time"], "TS"), customer_ref="", account_key=key if key != "UNASSIGNED" else "", quarter=q, service=s,
                 hours=hours, planned_hours=planned, amount_usd=hours * E["rate"], note=("NQ AI Delivery, Data Platform team: 46 h of September not logged" if (key, q) == ("NQ-ACC-0011", "Q3 2026") else ""),
                 currency=E["cur"], last_modified=QEND[q] + "T20:00:00Z")
    L["people"] = hours * E["rate"]
    L["src"].append(ts["source_id"])
    L["_planned"] = planned
    L["_rate"] = E["rate"]

# vendor rebates per entity-quarter; allocated to licensing+cloud lines by revenue share in earned quarter
REB = {}
for e in ENT:
    for q in Q:
        amt = round(rnd.uniform(0.018, 0.026) * sum(L["revenue"] for L in lines.values() if L["entity"] == e and L["quarter"] == q and L["service"] in ("licensing", "cloud")), -2)
        if e == "embee" and q == "Q2 2026":
            amt = 38400
        rid = "REB-SB1-0912" if (e == "embee" and q == "Q2 2026") else sid(ENT[e]["erp"], "REB")
        attributed = "Q3 2026" if rid == "REB-SB1-0912" else q
        booked = attributed
        r = add_src(system=ENT[e]["erp"], entity=e, record_type="rebate", source_id=rid, vendor="Microsoft", segment="Enterprise" if e != "entc" else "SMB", quarter=booked, earned_quarter=q, attributed_quarter=attributed,
                    amount_usd=amt, note=("Microsoft CSP rebate earned in Q2 2026, booked 2026-07-14" if rid == "REB-SB1-0912" else ""), last_modified=(QEND[q] + "T19:00:00Z") if rid != "REB-SB1-0912" else "2026-07-14T10:05:00Z")
        REB[(e, q)] = r

def allocate(basis):
    for L in lines.values():
        L["rebate"] = 0
        L["src"] = [x for x in L["src"] if not x.startswith("REB") and "-REB-" not in x]
    for (e, q), r in REB.items():
        qq = r["earned_quarter"] if basis == "earned" else r["attributed_quarter"]
        tgt = [L for L in lines.values() if L["entity"] == e and L["quarter"] == qq and L["service"] in ("licensing", "cloud") and L["account_key"] != "UNASSIGNED"]
        tot = sum(L["revenue"] for L in tgt)
        acc = 0
        for i, L in enumerate(sorted(tgt, key=lambda x: x["account_key"] + x["service"])):
            share = round(r["amount_usd"] * L["revenue"] / tot) if i < len(tgt) - 1 else r["amount_usd"] - acc
            acc += share
            L["rebate"] += share
            L["src"].append(r["source_id"])

def gp_of(L):
    return L["revenue"] - L["cost"] - L["people"] + L["rebate"]

# ledger = correct basis (earned rebates, full hours)
allocate("earned")
ml = lines[MISSING]
ml_people_full = ml["_planned"] * ml["_rate"]
ledger = defaultdict(int)
for L in lines.values():
    g = gp_of(L)
    if (L["quarter"], L["account_key"], L["service"]) == MISSING:
        g = L["revenue"] - L["cost"] - ml_people_full + L["rebate"]
    ledger[(L["entity"], L["quarter"])] += g
for (e, q), v in sorted(ledger.items()):
    add_src(system=ENT[e]["erp"], entity=e, record_type="ledger_gp", source_id=f"GL-{PFX[ENT[e]['erp']]}-{q.replace(' ', '')}", quarter=q, amount_usd=v,
            note="Gross profit per the general ledger after month-end journals", last_modified=QEND[q] + "T23:00:00Z")
# payroll aggregates (team level, never per person)
for e in ("embee", "nqai"):
    for q in Q:
        tot = sum(L.get("_planned", 0) * L.get("_rate", 0) for L in lines.values() if L["entity"] == e and L["quarter"] == q)
        add_src(system="payroll_in", entity=e, record_type="payroll_cost", source_id=sid("payroll_in", "RUN"), quarter=q, amount_usd=tot, note="Delivery team cost at standard rate, team level only", last_modified=QEND[q] + "T12:00:00Z")

# seed state = attributed basis (the late rebate sits in Q3)
allocate("attributed")
for (q, key, s), L in sorted(lines.items(), key=lambda kv: (Q.index(kv[0][0]), kv[0][1], kv[0][2])):
    g = gp_of(L)
    gp.append(dict(line_id=f"GP-{len(gp)+1:03d}", quarter=q, entity=L["entity"], country=ENT[L["entity"]]["country"], account_key=key, service=s,
                   revenue_usd=L["revenue"], cost_of_sale_usd=L["cost"], people_cost_usd=L["people"], rebate_usd=L["rebate"], gp_usd=g,
                   gp_pct=round(100 * g / L["revenue"], 1), rule_version="GP-RULE v1.2", source_ids=";".join(L["src"])))

tie = {}
for e in ENT:
    for q in Q:
        calc = sum(r["gp_usd"] for r in gp if r["entity"] == e and r["quarter"] == q)
        tie[(e, q)] = (calc, ledger[(e, q)], calc - ledger[(e, q)])
for q in Q:
    st = "open" if q == "Q3 2026" else "closed"
    closes.append(dict(period=q, status=st, gp_usd=sum(tie[(e, q)][0] for e in ENT), ledger_gp_usd=sum(tie[(e, q)][1] for e in ENT),
                       difference_usd=sum(tie[(e, q)][2] for e in ENT), blocking_open=2 if q == "Q3 2026" else 0,
                       signed_by="" if st == "open" else "Sara Thomas", signed_at="" if st == "open" else QEND[q][:8] + "15"))

# opportunities: CRM source rows + layer rows
STAGE = {  # (crm, local) -> group
    ("creatio", "Qualified"): "discovery", ("creatio", "Proposal sent"): "proposal", ("creatio", "Contracting"): "negotiation", ("creatio", "Closed won"): "won",
    ("dynamics365", "Qualify"): "discovery", ("dynamics365", "Qualified"): "qualified", ("dynamics365", "Propose"): "proposal", ("dynamics365", "Close"): "negotiation", ("dynamics365", "Won"): "won",
    ("blackandwhite", "First meeting"): "discovery", ("blackandwhite", "Budget OK"): "qualified", ("blackandwhite", "Quote"): "proposal", ("blackandwhite", "Won"): "won",
}
OPP = [
    ("NQ-ACC-0007", "Azure landing zone", "cloud", "Propose", 180000, "2026-12-15", "OPP-D-5531"),
    ("NQ-ACC-0007", "Microsoft 365 E3 renewal, 1,200 seats", "licensing", "Won", 240000, "2026-09-20", "OPP-D-5408"),
    ("NQ-ACC-0007", "Copilot pilot, store operations", "ai_data", "Budget OK", 45000, "2027-01-31", "BW-OPP-118"),
    ("NQ-ACC-0001", "Defender for Endpoint roll-out", "security", "Qualified", 62000, "2026-12-20", None),
    ("NQ-ACC-0001", "M365 E5 upgrade", "licensing", "Propose", 138000, "2027-02-15", None),
    ("NQ-ACC-0003", "Azure data centre exit", "cloud", "Close", 310000, "2026-11-30", None),
    ("NQ-ACC-0003", "SOC as a service", "security", "Qualify", 85000, "2027-03-31", None),
    ("NQ-ACC-0005", "AKS platform build", "cloud", "Qualified", 120000, "2027-01-15", None),
    ("NQ-ACC-0010", "Dynamics 365 licences", "licensing", "Won", 54000, "2026-10-12", None),
    ("NQ-ACC-0013", "M365 Business Premium", "licensing", "Propose", 36000, "2026-12-05", None),
    ("NQ-ACC-0002", "AWS migration wave 2", "cloud", "Proposal sent", 260000, "2026-12-31", None),
    ("NQ-ACC-0002", "Managed cloud operations", "managed", "Qualified", 96000, "2027-02-28", None),
    ("NQ-ACC-0006", "Microsoft 365 renewal", "licensing", "Contracting", 48000, "2026-11-25", None),
    ("NQ-ACC-0009", "Azure IoT pilot", "cloud", "Qualified", 70000, "2027-01-20", None),
    ("NQ-ACC-0012", "Managed SAP hosting", "managed", "Proposal sent", 150000, "2027-03-15", None),
    ("NQ-ACC-0012", "M365 Copilot licences", "licensing", "Closed won", 82000, "2026-10-02", None),
    ("NQ-ACC-0004", "Hotel PMS licences", "licensing", "Quote", 41000, "2026-12-10", None),
    ("NQ-ACC-0008", "Churn model on Fabric", "ai_data", "Budget OK", 98000, "2027-01-30", None),
    ("NQ-ACC-0008", "Microsoft 365 E3", "licensing", "First meeting", 120000, "2027-03-31", None),
    ("NQ-ACC-0011", "Learning analytics platform", "ai_data", "Won", 52000, "2026-09-10", None),
]
PROB = {"discovery": 0.1, "qualified": 0.3, "proposal": 0.5, "negotiation": 0.75, "won": 1.0}
accmap = {a[0]: a for a in ACC}
for key, title, s, local, amt, close, fixed in OPP:
    e = accmap[key][2]
    if title.startswith("Copilot pilot"):
        e = "nqai"
    crm = ENT[e]["crm"]
    sidv = fixed or sid(crm, "OPP")
    cref = "BW-ACC-7731" if title.startswith("Copilot pilot") else next(r["source_id"] for r in src if r["record_type"] == "account" and r["account_key"] == key)
    add_src(system=crm, entity=e, record_type="opportunity", source_id=sidv, customer_ref=cref, account_key=key if not title.startswith("Copilot") else "", service=s, stage_local=local, amount_usd=amt,
            note=title, quarter=close, currency="USD", last_modified="2026-11-01T16:30:00Z")
    g = STAGE[(crm, local)]
    q = "Q4 2026" if close <= "2026-12-31" and close >= "2026-10-01" else ("Q3 2026" if close < "2026-10-01" else "Q1 2027")
    opps.append(dict(opp_id=f"OPP-{len(opps)+1:03d}", source_system=crm, source_id=sidv, account_key=("" if title.startswith("Copilot") else key), entity=e, country=ENT[e]["country"], title=title, service=s,
                     stage_local=local, stage_group=g, amount_usd=amt, close_date=close, close_quarter=q, weighted_usd=round(amt * PROB[g]), synced_run=run_id[crm]))

# exceptions
def ex(i, kind, sev, system, source_id, rule, owner, title, impact, run=None):
    exc.append(dict(exception_id=f"EX-{i:02d}", kind=kind, severity=sev, status="open", system=system, source_id=source_id, sync_run=run or run_id[system], rule=rule,
                    owner=owner, title=title, impact=impact, fixed_by="", fixed_at="", fix_note="", detected_at="2026-11-01T22:10:00Z"))
ex(1, "unmatched_customer", "warning", "blackandwhite", "BW-ACC-7731", "MATCH-02 name and address 0.85 or more: suggest, owner confirms", "Kavya Rao · NQ AI sales operations",
   "Customer Meridian Rtl Grp (Black and White, and Tally T-C-0441) has no account key; suggested NQ-ACC-0007 at 0.86", "Q3 2026 GP of $7,480 sits on Unassigned; Meridian's pipeline misses $45,000")
ex(2, "late_rebate", "blocking", "sapb1", "REB-SB1-0912", "GP-RULE v1.2 §3: a rebate counts in the quarter it was earned", "Arjun Mehta · Embee finance",
   "Microsoft CSP rebate of $38,400 earned in Q2 2026 was booked on 14 July (Q3)", "Q3 2026 Embee GP is $38,400 above the ledger; Q2 2026 is $38,400 below")
ex(3, "missing_timesheet", "blocking", "azure_devops", next(r["source_id"] for r in src if r["record_type"] == "timesheet" and r["account_key"] == "NQ-ACC-0011" and r["quarter"] == "Q3 2026"),
   "TIME-01 logged hours below 90% of planned hours for a closed month", "Neha Iyer · NQ AI delivery lead",
   "NQ AI Delivery, Data Platform team: 46 hours of September not logged (Lumen Edtech)", "Q3 2026 NQ AI people cost is $1,472 short; GP is $1,472 above the ledger")
ex(4, "stage_conflict", "info", "creatio", next(r["source_id"] for r in src if r["record_type"] == "opportunity" and r["system"] == "creatio" and r["stage_local"] == "Qualified"),
   "STAGE-MAP v1.0: Creatio Qualified means a first call, mapped to Discovery", "Sara Thomas · Group finance",
   "Creatio Qualified is counted as Discovery, not Qualified", "Explains $166,000 (2 Entity C deals) shown in Discovery, not Qualified")
ex(5, "unmapped_service_code", "warning", "tally", "SRV-099", "SERVICE-MAP v1.1: every local code maps to one catalogue service", "Kavya Rao · NQ AI sales operations",
   "Tally service code SRV-099 has no catalogue service yet", "No GP line uses it in the last four quarters; new invoices would land on Unmapped")
ex(6, "sync_failed", "warning", "azure_devops", FAILED_RUN, "SYNC-03 a failed run is retried once, then raised", "Neha Iyer · NQ AI delivery lead",
   "Azure DevOps sync SR run timed out reading time logs", "Time data is as of the previous night's run SR-0309", run=FAILED_RUN)

# definitions: rules, mappings, sync policy, owners
D = [
    ("GP-RULE", "gp_rule", "", "", "GP = revenue - cost of sale - people cost (hours x standard rate) + vendor rebates allocated by revenue share; a rebate counts in the quarter it was earned", "v1.2", "Sara Thomas · Group finance"),
    ("RATE-01", "standard_rate", "embee", "", "Delivery standard rate $28 per hour", "v1.0", "Arjun Mehta · Embee finance"),
    ("RATE-02", "standard_rate", "nqai", "", "Delivery standard rate $32 per hour", "v1.0", "Neha Iyer · NQ AI delivery lead"),
    ("RATE-03", "standard_rate", "entc", "", "Delivery standard rate $55 per hour", "v1.0", "Sara Thomas · Group finance"),
    ("FX-01", "fx", "", "", "Group reporting in USD; INR at 84.00 per USD, fixed for the POC", "v1.0", "Sara Thomas · Group finance"),
    ("MATCH-01", "match_rule", "", "", "Same tax id (GSTIN or VAT) in two systems: linked automatically", "v1.0", "Sara Thomas · Group finance"),
    ("MATCH-02", "match_rule", "", "", "Normalised name and address similarity 0.85 or more: suggested, owner confirms; below 0.85: exception", "v1.0", "Kavya Rao · NQ AI sales operations"),
    ("STAGE-CR-Q", "stage_map", "creatio", "Qualified", "discovery", "v1.0", "Sara Thomas · Group finance"),
    ("STAGE-D-Q", "stage_map", "dynamics365", "Qualified", "qualified", "v1.0", "Sara Thomas · Group finance"),
    ("STAGE-BW-B", "stage_map", "blackandwhite", "Budget OK", "qualified", "v1.0", "Sara Thomas · Group finance"),
    ("SVC-SB1", "service_map", "sapb1", "M365-LIC", "licensing", "v1.1", "Arjun Mehta · Embee finance"),
    ("SVC-T", "service_map", "tally", "AIP-01", "ai_data", "v1.1", "Kavya Rao · NQ AI sales operations"),
    ("SVC-NS", "service_map", "netsuite", "4300-Services", "managed", "v1.1", "Sara Thomas · Group finance"),
    ("SYNC-01", "sync_policy", "", "ERP, payroll, time", "Copied nightly (payroll monthly, team level only): month-end GP needs stable, reconciled numbers", "v1.0", "Sara Thomas · Group finance"),
    ("SYNC-02", "sync_policy", "", "CRM", "Deal status and amount read live from the CRM; copied into the layer on Sync now or nightly", "v1.0", "Sara Thomas · Group finance"),
    ("SYNC-03", "sync_policy", "", "all", "A failed run is retried once, then raised as an exception to the system's owner", "v1.0", "Neha Iyer · NQ AI delivery lead"),
    ("TIME-01", "exception_rule", "", "timesheets", "Logged hours below 90% of planned hours for a closed month raise an exception; the owner may accrue from planned hours", "v1.0", "Neha Iyer · NQ AI delivery lead"),
]
for code, kind, system, local, value, ver, owner in D:
    defs.append(dict(code=code, kind=kind, system=system, local_value=local, group_value=value, version=ver, owner=owner, status="approved"))

# account plays (seeded AI suggestions)
P = [
    ("PLAY-01", STORY, "upsell", "Microsoft 365 E3 to E5 Security, 1,200 seats", 0.82, 156000, "suggested", "Rohan Kapoor · Embee account lead",
     "E3 renewal won in Sept (Dynamics 365 OPP-D-5408, $240,000); no Cybersecurity line in four quarters of SAP B1 invoices; Azure landing zone in Propose (OPP-D-5531); Copilot pilot at NQ AI (BW-OPP-118) needs E5 data controls",
     "OPP-D-5408;OPP-D-5531;BW-OPP-118"),
    ("PLAY-02", "NQ-ACC-0003", "cross_sell", "Managed SOC after the data centre exit", 0.74, 85000, "accepted", "Rohan Kapoor · Embee account lead",
     "Azure data centre exit in Close (Dynamics 365, $310,000); SOC as a service still in Qualify; no Managed services line in SAP B1", ""),
    ("PLAY-03", "NQ-ACC-0002", "cross_sell", "Cybersecurity assessment with AWS wave 2", 0.68, 40000, "suggested", "Maya Fernandes · Entity C account lead",
     "AWS migration wave 2 in Proposal sent (Creatio, $260,000); no Cybersecurity line in NetSuite", ""),
    ("PLAY-04", "NQ-ACC-0008", "upsell", "Fabric capacity for the churn model", 0.71, 60000, "suggested", "Kavya Rao · NQ AI sales operations",
     "Churn model on Fabric at Budget OK (Black and White, $98,000); AI and data GP margin 42% in Tally invoices", ""),
    ("PLAY-05", "NQ-ACC-0012", "upsell", "Copilot adoption services after licences", 0.66, 35000, "suggested", "Maya Fernandes · Entity C account lead",
     "M365 Copilot licences won in Oct (Creatio, $82,000); Managed services line active in NetSuite", ""),
    ("PLAY-06", "NQ-ACC-0001", "cross_sell", "Azure cloud for Aster's lab systems", 0.58, 90000, "dismissed", "Rohan Kapoor · Embee account lead",
     "No Cloud line in SAP B1; Defender roll-out in Qualified", ""),
]
for pid, key, kind, offer, score, value, status, owner, evidence, ev_ids in P:
    steps = ""
    if pid == "PLAY-02":
        steps = json.dumps([{"n": 1, "step": "SOC scoping call with the CISO", "owner": "Rohan Kapoor", "due": "2026-11-12", "done": True},
                            {"n": 2, "step": "Proposal and pricing", "owner": "Rohan Kapoor", "due": "2026-11-26", "done": False},
                            {"n": 3, "step": "Order signed", "owner": "Rohan Kapoor", "due": "2026-12-18", "done": False}])
    plays.append(dict(play_id=pid, account_key=key, kind=kind, offer=offer, score=score, value_usd=value, status=status, owner=owner, evidence=evidence, evidence_ids=ev_ids,
                      steps=steps, version=2 if pid == "PLAY-02" else (1 if status != "suggested" else 0), ai_generated=True))
hist.append(dict(history_id="PH-001", play_id="PLAY-02", version=1, change="accepted", by="Rohan Kapoor", at="2026-10-28T09:12:00Z", note="Accepted from the suggestion", snapshot=""))
hist.append(dict(history_id="PH-002", play_id="PLAY-02", version=2, change="edited", by="Rohan Kapoor", at="2026-10-30T15:40:00Z", note="Proposal due moved from 19 Nov to 26 Nov", snapshot=""))

def w(name, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=list(rows[0].keys()), extrasaction="ignore")
        wr.writeheader()
        for r in rows:
            wr.writerow({k: v for k, v in r.items() if not k.startswith("_")})

accounts = [dict(account_key=k, name=n, entity=e, country=ENT[e]["country"], landscape=ENT[e]["landscape"], segment=s, parent_key=p,
                 sources=len([l for l in links if l["account_key"] == k]), is_story=(k == STORY)) for k, n, e, s, sv, p in ACC]
w("accounts.csv", accounts); w("account-links.csv", links); w("source-records.csv", src); w("sync-runs.csv", runs); w("opportunities.csv", opps)
w("gp-lines.csv", gp); w("period-close.csv", closes); w("exceptions.csv", exc); w("definitions.csv", defs); w("account-plays.csv", plays); w("play-history.csv", hist)

# summary for the plan
def gpsum(q, key=None, e=None):
    return sum(r["gp_usd"] for r in gp if r["quarter"] == q and (key is None or r["account_key"] == key) and (e is None or r["entity"] == e))
summ = dict(
    counts={n: len(r) for n, r in [("accounts", accounts), ("links", links), ("source", src), ("runs", runs), ("opps", opps), ("gp", gp), ("closes", closes), ("exc", exc), ("defs", defs), ("plays", plays), ("hist", hist)]},
    src_by_type={t: sum(1 for r in src if r["record_type"] == t) for t in sorted(set(r["record_type"] for r in src))},
    tie={f"{e} {q}": tie[(e, q)] for e in ENT for q in Q},
    group_gp={q: gpsum(q) for q in Q},
    meridian_gp={q: gpsum(q, STORY) for q in Q},
    meridian_lines=[r for r in gp if r["account_key"] == STORY],
    meridian_open_pipeline=sum(o["amount_usd"] for o in opps if o["account_key"] == STORY and o["stage_group"] != "won"),
    unassigned_q3=[r for r in gp if r["account_key"] == "UNASSIGNED"],
    missing=MISSING, closes=closes, failed_run=FAILED_RUN,
    links_by_method={m: sum(1 for l in links if l["method"] == m) for m in set(l["method"] for l in links)},
    pipeline_by_group={g: sum(o["amount_usd"] for o in opps if o["stage_group"] == g) for g in PROB},
    ex3_src=exc[2]["source_id"], ex4_src=exc[3]["source_id"],
)
print(json.dumps(summ, indent=1, default=str))
