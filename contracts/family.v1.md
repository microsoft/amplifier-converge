# Family Contract — v1 (DRAFT)

**Who builds against this:** the intent steward choosing which project a manager
runs; every sub-project's manager session, which must know what the top level
promises and what it does not; the app's project picker; the `converge` skill and
CLI, which resolve "which project" before anything else; anyone standing up a new
part or swapping the body behind an existing one.

## Purpose

Amplifier Converge is one experience made of several Converge projects. This
contract is the seam between them: how a sub-project is named and registered,
what the top level holds and what it must not, and how a part can be a wrapper
today and a body tomorrow without the whole moving. It exists because the
alternative — one repository — makes every part's detail everyone's problem and
lets no two managers work the same day without colliding.

## Core (the teeth)

1. **The top-level project holds seams, never internals.** `amplifier-converge`
   carries the family vision, the contracts between parts, the registry of parts,
   and the ledger that reads those seams. No source code that a sub-project could
   own lives here.

2. **A sub-project is a Converge project in full.** Each part has its own
   repository, `docs/VISION.md`, `contracts/`, ledger, work queue and manager
   session, and follows the method as published by the method sub-project. The top
   level never files work into a sub-project's queue; it files into its own and
   names the seam.

3. **Registration is a file the top level owns.** `family.toml` at the top-level
   root lists every sub-project: id, repository URL, default branch, the seam
   contracts it builds against, and its status — `wrapper` · `body` · `retired`.
   A part not in the file is not in the family; the app's project picker shows
   exactly the file's contents.

4. **A part's contract is with the seam, not with its neighbour's insides.** A
   sub-project may depend only on what another part's seam contract promises. A
   dependency on a file, table or route the seam does not name is a defect in
   whichever part reached across.

5. **Wrapper and body are the same to the seam.** A part marked `wrapper` fronts
   something that already exists (the shared work queue, today's lane launcher,
   today's app). Swapping what is behind it changes no top-level contract, no
   top-level ledger row and requires no word from the steward; the swap is the
   sub-project's own work.

6. **Two managers never share state.** Each part's operation state lives at
   `<workspace>/.converge/<part-id>/`; queues, plan records, lanes and calls are
   per part. A top-level call about a seam goes to the top-level manager.

7. **A change to a seam is a proposal at the top level.** Sub-projects propose
   through `<contract>.vN-candidate.md` beside the seam contract here; a
   sub-project's own contracts change by its own process. The steward ratifies
   seam changes; they lock like any other contract.

8. **The family is small and named.** v1 names five parts: `converge-method` (the
   contracts, ledger, kits and manager mode — `amplifier-bundle-converge` as it
   ships), `converge-service` (the control plane and its API), `converge-app` (the
   experience), `converge-agent-types` (adapters, Amplifier built in), and
   `converge-queue` (a wrapper around `amplifier-work-tracker`). Adding a sixth is a
   proposal here, not a directory.

## What v1 deliberately does NOT freeze

- **Where a sub-project's repository is hosted** (GitHub organisation, mirror,
  local path) — promoted when two parts disagree on how to reach a third.
- **A part's internal layout** — never frozen here; each part's contracts own it.
- **Whether the top-level ledger reads sub-project ledgers** — promoted when a
  seam promise can only be judged by a sub-project's row.
- **Cross-family reuse** (a part serving a second family) — promoted when one
  exists.

## Conformance kit asserts

- `family.toml` parses, names five parts, and every part has id, url, branch,
  seams and a status from the three words.
- Every seam a part names in `family.toml` exists as `contracts/<seam>.vN.md` at
  the top level.
- The top-level repository holds no directory a listed part's `family.toml` entry
  claims (no `app/`, `service/`, `adapters/` here).
- The app's project picker, read live, lists exactly the parts in `family.toml`.
- Each listed part's repository, read at its default branch, carries
  `docs/VISION.md` and a `contracts/` directory.
- No two parts' operation state directories share a path.

## Reserved / open questions (NOT frozen)

- Should the top level pin each part's commit (a lockfile) or read the default
  branch? Pinning makes the family reproducible; reading keeps it honest.
- How a part's manager learns the family exists — a line in its wake prompt, or a
  file the method sub-project ships?
