# Service Contract — v1 (RATIFIED 2026-09-06)

The one API every actor speaks, and the records behind it. Read by the app, the CLI,
every manager and worker session, and the service part that builds it.

## Who builds against this

**The service part** implements it. **Everyone else** speaks it: the app reads and
writes through it, the `amplifier-converge` command and the skill handed to agents call
it, and every manager or worker session — whatever agent runs it — claims, reports and
checks through it.

## What it is

Amplifier Converge runs as one instance on a machine. Inside it, the service holds the
records and serves one HTTP API. Two records are frozen in v1:

```
run    id · project · role (manager | worker) · item · manager_run · branch
       state (queued | running | done | stuck | waiting | merged | pruned)
       cause (when stuck) · call (when waiting) · started_at · ended_at

check  id · run · by (the manager run) · commit · command · exit_code · at
```

A run is a lane, or a manager's own wake. A check is a manager's own re-run of a
verification, pointing at the commit it judged.

## The promises

1. **One API, spoken by all.** Every write to a record goes through this API. A record
   changed any other way is a defect, and the disagreement is filed.

2. **The record is the truth.** What an agent prints or leaves on disk is evidence. What
   it tells the service is fact. When they disagree, the record stands.

3. **Merge is a request the service may refuse.** A run ends `done`, `stuck` (with a
   cause) or `waiting` (on a call). Asking to mark it `merged` succeeds only when a
   `check` exists whose `by` is the run's manager and whose `commit` is on the run's
   branch. Otherwise the answer is a refusal, in a sentence. What this does not prove:
   that the check was meaningful — that stays the manager's obligation under the method.

4. **Identity arrives with the run.** A run gets its id, project, role, the API URL and a
   short-lived token in its environment. Nothing else grants write access; a token never
   comes from configuration. A worker token cannot write a `check`.

5. **Liveness is an observation with a time.** Agent types report "seen alive at T". The
   service stores those and never a "silent" flag. *Quiet* and *silent — may have died*
   are derived from the age of the last observation, and said in those words.

6. **The store is one file the instance owns.** In the instance's data directory,
   scoped by project. Nothing of the service is written into a repository's working copy.

## Not in v1

- **The desk's records** — documents, proposals, artifacts, events, calls, the four writes,
  the manager session — named in `desk.v1`; each frozen the wave it first flows.
- **Wire details** (REST vs RPC, poll vs push) — until a third client needs them stable.
  A change reaches a reader within ten seconds either way.
- **Budgets** — the first time a steward asks for a cap; a gate when it comes, not a report.
- **Custody** — the queue owns it (`queue.v1`); the service records what the queue says.

## How the kit checks it

- The route table and the skill's endpoint list name the same paths.
- `merged` requested with no qualifying `check` → refused, with a sentence.
- A write with an absent or configured token → refused. A worker token writing `check` → refused.
- Creating a run with no liveness handle → refused.
- The store is under the data directory; nothing service-owned appears in a working copy.

## Open questions

- Is a manager's own wake a `run` (v1 says yes) or its own record?
- May a `check` say *could not check* — a third answer that never collapses to false?

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-06 | v1 drafted from the family vision and a study of a comparable harness; council review; ratified as content. | Steward's word, 2026-09-06. |
| 2026-09-07 | Reshaped into the family format on the steward's word ("port it"); no promise changed. | `docs/FORMAT.md`. |
