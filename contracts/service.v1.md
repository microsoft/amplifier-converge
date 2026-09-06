# Service Contract — v1 (DRAFT)

**Who builds against this:** the app (every screen reads and writes through it); the
`amplifier-converge` command and the skill handed to agents; every manager and worker session,
whatever agent type runs them; the agents part (it launches the runs the service
records); the queue part (the service fronts it); the method part's kits, which
judge the service by what it records.

## Purpose

One surface every actor speaks, whose records are the truth. Without it a lane is a
terminal session, a working copy, a marker file and a line in a manifest; a call is
a line in a plan record; a claim is a row only the manager's shell can reach — and
every incident of the practice that preceded this had the same shape: a
verification layer certifying the wrong thing. This contract names the first records
and the promises around them, so the app, the CLI and any agent see one operation
and the method's obligations are enforced by a machine where a machine can.

This is a first version, written before a run has flowed. It freezes two records and
leaves the rest open on purpose; it is rewritten from evidence after the first run.

## Core (the teeth)

1. **One API, spoken by all, from one instance.** The service runs as part of the one
   Amplifier Converge instance on a machine; the app, the CLI, the skill handed to
   agents and every manager and worker session use the same HTTP API. A write that reaches a record
   by any other path is a defect.

2. **The record is the truth; output is telemetry.** What an agent prints or leaves
   on disk is evidence; what it tells the service is fact. Where the two disagree,
   the record stands and the disagreement is filed.

3. **Two records are frozen: `run` and `check`.** A *run* is a lane or a manager's
   own wake: who launched it, for which project and item, its state, and its
   manager. A *check* is a manager's re-run of a verification: the command, its exit
   code, the commit it judged, and the run it names. Every field is a scalar or an
   identifier; no free text is stored that no clause reads.

4. **A run ends in exactly one of three ways, and merge is a request.** `done`,
   `stuck` with a cause, or `waiting` on a named call — then a *request* to mark it
   `merged`, which the service **refuses** unless a `check` record exists whose
   author is the run's manager and whose commit is on the run's branch. What this
   gate does not prove: that the check was meaningful. That remains the manager's
   obligation under the method; the service can only refuse a merge with no check.

5. **Identity is issued per run and scoped.** A run receives its identity in the
   environment — run id, project, role (`manager` | `worker`), API URL, a
   short-lived token scoped to that project and role — and nothing else grants write
   access. A token never comes from configuration. A manager's token may write
   `check`; a worker's may not.

6. **Liveness is an observation, not a state.** The agent type reports when it last
   saw a run alive; the service stores each report with its time and never
   maintains a "silent" flag. A reader derives *quiet* or *silent — may have died*
   from the age of the last observation and says so in those words.

## What v1 deliberately does NOT freeze

- **The other records** — *project*, *manager session*, *claim*, *call*, and the
  steward's writes (decision, feedback, priority, ask, steer) — promoted one at a
  time, each the first time it flows through a real run. Until then those facts
  live where they live today, and no path to them is called a defect.
- **The wire format** (REST vs RPC; poll vs push) — promoted when a client other
  than the app or the CLI needs it stable. Until then the app polls.
- **Budgets** — promoted the first time a steward asks for a cap; designed as a
  gate when it comes, never as a report.
- **Custody** — the queue part owns it; the service records what the queue says.

## Conformance kit asserts

- The route table and the skill's endpoints section name the same paths; a path in
  one and not the other fails.
- A `merged` request for a run with no `check` by its manager on its branch is
  refused, with the reason in plain words.
- A write with a configured or absent token is refused; a worker token writing
  `check` is refused.
- A `POST` creating a run without a liveness handle is refused.
- The store is one file in the instance's data directory holding every project,
  scoped by project id; nothing of the service is written into a repository's
  working copy.

## Reserved / open questions (NOT frozen)

- Whether a manager's own wake is a *run* (v1 says yes) or a distinct record.
- Whether a `check` may be *could not check* — a third answer that never collapses
  to false — and how the gate treats it.
