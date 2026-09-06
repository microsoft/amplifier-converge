# Family Contract — v1 (DRAFT)

**Who builds against this:** the intent steward choosing which project a manager
runs; every part's manager session, which must know what the top level promises and
what it does not; the app's project picker; the `converge` skill and CLI, which
resolve "which project" before anything else; anyone standing up a new part or
replacing the body behind an existing one.

## Purpose

Amplifier Converge is one experience made of several Converge projects. This
contract is the seam between them: how a part is named and registered, what the top
level holds and must not, and how a part is replaced without the whole moving. It
exists because one repository makes every part's detail everyone's problem and lets
no two managers work the same day without colliding.

## Core (the teeth)

1. **The top-level project holds seams, never internals.** `amplifier-converge`
   carries the family vision, the contracts between parts, the registry of parts and
   the ledger that reads those seams. No source code a part could own lives here.

2. **A part is a Converge project in full.** Each part has its own repository,
   `docs/VISION.md`, `contracts/`, ledger, work queue and manager session, and follows
   the method as the method part publishes it. The top level never files work into a
   part's queue; it files into its own and names the seam.

3. **A part is registered only when it exists.** `family.toml` at the top-level root
   lists every part: id, repository URL, default branch, the seam contracts it builds
   against, and a status — `seeded` (a repository with a vision and a first contract
   and no body yet) · `body` · `retired`. A row for a repository that does not exist,
   or for one without a vision and a contract, fails the family kit. The app's
   project picker shows exactly this file's parts, beside the steward's own projects.

4. **A part's contract is with the seam, not with a neighbour's insides.** A part may
   depend only on what another part's seam contract promises. A dependency on a
   file, table or route the seam does not name is a defect in whichever part reached
   across.

5. **Replacing a body changes no seam.** What is behind a seam may be rewritten or
   swapped without a change to any top-level contract or ledger row and without a
   word from the steward; the swap is the part's own work, judged by the part's own
   contracts.

6. **Two managers never share state.** Each part's operating state lives at
   `<workspace>/.converge/<part-id>/`; queues, plan records, lanes and calls are per
   part. A call about a seam goes to the top-level manager; a call about a part's
   insides goes to that part's manager.

7. **Seam changes are proposals, batched.** A part proposes a seam change as
   `<contract>.vN-candidate.md` beside the seam contract here; the top-level manager
   gathers open proposals into one sheet so the steward answers once, not per part.
   A part's own contracts change by its own process.

8. **The family is small and named.** v1 names six parts: `method` (the law —
   documents, operation, the ledger format, kits, templates, the manager mode),
   `service` (the control plane and its API), `app` (the experience), `agents`
   (agent types and session management), `queue` (the work queue with custody), and
   this top level. A seventh is a proposal here, not a directory.

## What v1 deliberately does NOT freeze

- **Where a part is hosted** — promoted when two parts disagree on how to reach a
  third. (Today: private repositories under one account; moved together later.)
- **Whether the top level pins each part's commit** or reads its default branch —
  promoted the first time "it worked yesterday" cannot be reproduced.
- **Whether the top-level ledger reads a part's ledger** — promoted when a seam
  promise can only be judged by a part's row.
- **A part's internal layout** — never frozen here; the part's contracts own it.

## Conformance kit asserts

- `family.toml` parses; every part has id, url, branch, seams and a status from the
  three words; every url answers and carries `docs/VISION.md` and `contracts/` at
  its branch.
- Every seam a part names exists as `contracts/<seam>.vN.md` at the top level.
- The top-level repository holds no directory that a listed part's description
  claims.
- The app's project picker, read live, lists exactly the parts in `family.toml`
  plus the steward's own projects — no more, no fewer.
- No two parts' `.converge/<part-id>/` directories share a path.

## Reserved / open questions (NOT frozen)

- How a part's manager learns the family exists — a line in its wake prompt, or a
  file the method part ships.
- Whether `seeded` should expire — a part with direction and no body after a
  named interval reads as a defect, or as patience.
