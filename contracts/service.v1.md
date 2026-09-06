# Service Contract — v1 (DRAFT)

**Who builds against this:** the app (every screen reads and writes through it);
the `converge` CLI and skill; every manager session and worker session, whatever
agent type runs them (they claim, resolve, file, call and heartbeat through it);
the agent-types sub-project (it launches runs the service records); the queue
sub-project (the service fronts it); the method sub-project's kits, which judge
the service by what it records.

## Purpose

One surface that every actor speaks, whose records are the truth. Today a lane is
a tmux session, a worktree, a marker file and a line in a manifest; a call is a
line in a plan record; a claim is a row in a tracker only the manager's shell
reaches. That works for one manager on one host and for nothing else. This
contract names the records and the promises — what is recorded, who may write
it, and what the service refuses — so the app, the CLI and any agent see the same
operation and so the method's own obligations can be enforced by a machine where
a machine can.

## Core (the teeth)

1. **One API, spoken by all.** The app, the CLI, the skill handed to agents, and
   every manager and worker session use the same HTTP API. There is no second
   path: a write that reaches a record without the API is a defect.

2. **The record is the truth; output is telemetry.** What an agent prints, logs or
   leaves in a file is evidence; what it tells the service is fact. Where the two
   disagree, the record stands and the disagreement is filed.

3. **Six records, no more in v1.** *Project* (a family part or a steward's own),
   *manager session*, *run* (a lane or a manager's own wake), *claim* (a work item
   held, with custody), *call* (one of the four kinds, put to the steward, with its
   answer), and *check* (a manager's re-run of a verification, with its command
   and what it printed). Anything else is derived from these or lives in a
   sub-project.

4. **A run ends in exactly one of three ways.** `done` with the check it points
   at, `stuck` with the cause, or `needs-word` with the call it raised — then
   `merged` or `pruned`. The service refuses `merged` until a *check* record by the
   run's manager names the run. A marker file, a green log or a lane's own word
   is not a check.

5. **Identity is issued per run and scoped.** A run receives its identity in the
   environment — run id, project, role (`manager` | `worker`), API URL, a
   short-lived token scoped to that project and run — and nothing else grants
   write access. A token never comes from configuration.

6. **The four calls are records with answers.** `ratify` · `irreversible` ·
   `human-check` · `priority` are the only call kinds; each carries what is
   parked and what continued, and an answer is one word plus optional edits. A
   call of any other kind is refused with the reason.

7. **The queue is fronted, not replaced.** Claims resolve to the shared work
   queue the method already uses; the service adds custody heartbeats and the
   record. Reading an item never claims it; claiming is atomic; a reported write
   failure is unknown until re-read.

8. **Live state is pushed.** Every record change is published on one event
   stream the app and the CLI subscribe to; a reader never polls a record it can
   subscribe to. A subscriber that falls behind is told so, never silently trimmed.

9. **What an agent may call is generated from the router.** The endpoints section
   of the skill handed to agents is produced from the service's own route table at
   build; a check fails the moment a documented path is not served or a served
   write is undocumented.

10. **State lives under the project's workspace.** The service's store is one file
    (or one directory) at `<workspace>/.converge/<project-id>/service/`; nothing
    under the home directory, no daemon a person must install to read it.

11. **Operation is observed, never re-spawned by the service.** The service ticks
    to read heartbeat age, markers and commits and to mark a run *quiet* or
    *silent*; starting, resuming or killing a run is the agent type's act, on the
    service's request, and is recorded as such.

## What v1 deliberately does NOT freeze

- **Budgets** (per-project and per-run token/time caps as a gate) — promoted the
  first time a steward asks for a cap or a run's cost surprises one.
- **Multi-user** beyond one steward and any number of readers — promoted when a
  second person needs to answer a call.
- **The wire format** (REST vs RPC, WebSocket vs SSE) — promoted when a second
  client that is not the app or the CLI needs it stable.
- **A store beyond one file** — promoted when two hosts must share one project.

## Conformance kit asserts

- The route table, the skill's endpoints section and the CLI's command list name
  the same paths; a path in one and not the others fails.
- A run marked `merged` has a `check` record by its manager naming it (sampled
  from the live store); one without fails.
- A write attempted with a configured or absent token is refused.
- A call created with a fifth kind is refused with a reason in plain words.
- The service store sits under `<workspace>/.converge/<project-id>/service/` and
  nothing of the service is written under the home directory.
- The event stream delivers a record change to a subscribed client within five
  seconds, measured.

## Reserved / open questions (NOT frozen)

- Whether a manager's own wake is a *run* (v1 says yes) or a distinct record — a
  manager has no lane and no merge.
- Whether the service should hold the ledger's readings as records, or leave the
  ledger to the method sub-project entirely.
