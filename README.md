# All demo folders

One folder per client and use case, `<client-slug>/<use-case-slug>/` (for example
`clickup/clickup-delivery-command-v2/`): the Nebula working folder of that demo. Every cloud
session for that client and use case loads it from `main` at its start and pushes it back to
`main` at its end, so work carries from one gate to the next without relying on any cache.
Slugs are the client and use case names in lower case, every run of other characters
replaced by `-`.

| Path in a use-case folder | What it is |
|---|---|
| `studio/state/<use case>.md` | Demo Studio's state file (the POC row's `demo_state` holds the same copy) |
| `studio/profiles/<client>.md` | the client profile |
| `studio/plan/<client>/` | the requirements doc, the plan doc and their PDFs |
| `studio/collaterals/<client>/` | G4's demo script, deck and the collateral kit's working files |
| `studio/solution.json` | the Nebula solution the use case builds into: `<Client> · <use case>` on orbit.uat.unifyapps.com |
| `records/`, `specs/`, `plans/`, `docs/`, `.nebula/`, `memory.md`, `CLAUDE.md` | Nebula's working folder; `records/solution.json` binds the folder to its solution |

Left out by `.gitignore`: caches Nebula rebuilds (`entities/`, `entity-manifests/`), session
scratch (`.sessions/`), a code app checkout (its source lives in Code Builder), and videos and
audio (uploaded to the tenant and Slack).

If the cloud ever refuses a push to `main`, the session pushes branch
`claude/demo-<client-slug>-<use-case-slug>` instead and the next session loads from it.
Nothing here is a secret: the save script refuses a commit that matches a key, token or cookie.
Written by the routine `demo-studio-build`; see `studio/cloud/README.md` in
gouravUnifyapps/DemoStudio-UnifyApps.
