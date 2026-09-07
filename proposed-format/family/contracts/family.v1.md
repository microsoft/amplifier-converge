# Family Contract — v1 (RATIFIED 2026-09-06)

How the parts of Amplifier Converge fit together and stay apart. Read by every part's
manager session, the app's picker, and anyone adding or replacing a part.

## Who builds against this

**The top-level project** keeps the registry, the seams and the ledger that reads them.
**Every part** — method, service, app, agents, queue — is a Converge project of its own
that builds only against the seams named here.

## What it is

Six repositories, one registry. A part is in the family when it has a row:

```toml
[[part]]
id     = "service"
url    = "https://github.com/bkrabach/amplifier-converge-service"
branch = "main"
seams  = ["family.v1", "service.v1", "agent-types.v1", "queue.v1"]
status = "seeded"          # seeded | body | retired
what   = "the control plane: run and check first, one door, one file"
```

`seeded` means the repository exists with a vision and a first contract and no body yet.

## The promises

1. **The top level holds seams, never internals.** This repository carries the family
   vision, the seam contracts, `family.toml`, the seam ledger, and the one installable —
   a package that composes the parts and adds no code of its own.

2. **A part is a full Converge project.** Its own repository, vision, contracts, ledger,
   queue and manager session. The top level files work into its own queue and names the
   seam; it never files into a part's.

3. **Registered only when it exists.** A row whose repository is unreachable, or lacks
   `docs/VISION.md` and `contracts/`, fails the family kit. The picker shows exactly
   these rows beside the steward's own projects.

4. **Contracts are with the seam.** A part depends only on what a neighbour's seam
   promises. Reaching for a neighbour's file, table or route is a defect in the part
   that reached.

5. **Replacing a body changes no seam.** Swap what is behind a seam and no top-level
   contract, ledger row or steward word changes.

6. **Two managers never share state.** The instance keeps each project's state under its
   data directory by project id. No two projects share a path; a working copy receives
   only the project's own documents.

7. **Seam changes are proposals, batched.** A part writes `<contract>.vN-candidate.md`
   beside the seam here; the top-level manager puts every open proposal on one sheet so
   the steward answers once.

8. **Split out before it becomes two.** Every part's contracts name a ceiling (a number)
   and a test for a second domain (own vocabulary, own kit, own steward questions).
   Crossing either means a split-out proposal here within one wave; over the ceiling with
   none open reads *Broken* in the ledger.

9. **Six parts, named.** Method, service, app, agents, queue, and this top level. A seventh
   arrives by a split-out or a proposal, never by a directory.

## Not in v1

- **Where parts are hosted** (today: private, one account) — until two parts disagree how to reach a third.
- **Pinning each part's commit** vs reading its branch — the first time "it worked yesterday" cannot be reproduced.
- **The top-level ledger reading a part's ledger** — when a seam promise can only be judged by a part's row.

## How the kit checks it

- `family.toml` parses; every row has the five fields and a status from the three words.
- Every `url` answers at its `branch` with `docs/VISION.md` and `contracts/`.
- Every seam a row names exists as `contracts/<seam>.md` here.
- No part's directory (`app/`, `service/`, `adapters/`, …) exists at the top level.
- Every part's contracts name a ceiling and a second-domain test.
- The picker, read live, lists exactly the rows plus the steward's own projects.

## Open questions

- How a part's manager learns the family exists — a wake-prompt line, or a file the method ships.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-06 | v1 drafted; corrected after the steward's reading (one instance, no dependency on any other product); ratified as content. | Steward's words, 2026-09-06. |
| 2026-09-07 | Proposed reshaped into this format (no promise changed). | `proposed-format/FORMAT.md`. |
