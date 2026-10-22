# All demo folders

One folder per POC that POC Studio Live builds with Demo Studio, named by the POC's row id
(for example `POC-clickup-delivery-command-20261022/`). Every cloud run for that POC works
inside its folder.

Each POC lives on its own branch, `claude/poc-<row id>`: the cloud session checks it out at the
start of a run, and its Stop hook commits and pushes the folder's `studio/` when the run ends.
`main` holds only this README and the `.gitignore`.

| Path | What it is |
|---|---|
| `<row id>/studio/state/<use case>.md` | Demo Studio's state file (the POC row's `demo_state` holds the same copy) |
| `<row id>/studio/profiles/<client>.md` | the client profile |
| `<row id>/studio/plan/<client>/` | the requirements doc, the plan doc and their PDFs |
| `<row id>/studio/solution.json` | the Nebula solution the POC builds into: one per POC, `<Client> · <use case>` on orbit.uat.unifyapps.com |

Nothing here is a secret: the Stop hook refuses a commit that matches a key, token or cookie.
Set up by the routine `demo-studio-build`; see `studio/cloud/README.md` in
gouravUnifyapps/DemoStudio-UnifyApps.
