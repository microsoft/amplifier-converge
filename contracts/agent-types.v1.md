# Agent Types Contract — v1 (DRAFT)

**Who builds against this:** the agents part (it implements every type); the
service (it launches runs through a type and records what the type reports); the
app (it lists types, offers "test this environment", and attaches a person to a
running session); anyone adding a type for an agent this family has never met.

## Purpose

The method must not depend on which agent runs it. This seam is the whole of what
a type owes the family and the whole of what the family owes a type, so a manager
can be Amplifier, Claude Code, Codex or GitHub Copilot and the steward sees one
operation. It also carries the two promises the steward asked for by name: a person
can attach to a running session, and a session survives the service restarting and
the person disconnecting.

## Core (the teeth)

1. **A type is three functions.** `type` (its name), `execute(context) →
   callbacks` (start a run and report `log`, `event`, `end`), and
   `testEnvironment()` (say, in plain words, whether this host can run it and what
   is missing). Nothing else is required of a type; anything else a type offers is
   its own business.

2. **The wake is the whole context.** A run receives its identity in the
   environment — run id, project, role (`manager` | `worker`), API URL, a scoped
   token — plus one rendered prompt and the `amplifier-converge` skill. A type adds nothing
   the service did not hand it, and a run learns nothing from the disk it was not
   pointed at.

3. **The record is written by the service; the type only reports.** A type calls
   back with facts — started, alive at this time, printed this, ended this way with
   this cause — and never writes a record itself. `end` names exactly one of `done`,
   `stuck`, `waiting`, with the cause or the call.

4. **Liveness is an observation with a time.** A type reports when it last saw the
   run alive; it never reports a state word. What "quiet" or "silent — may have
   died" means is derived by the reader from the age of the last observation.

5. **A person can attach, and a session survives.** Every type that runs in a
   terminal names the mechanism by which a person attaches to the live session —
   from the app, and from a terminal if they choose — and by which the session
   outlives the instance's restart and the person's disconnect; `testEnvironment()`
   checks that mechanism and the instance installs what is missing when it can,
   naming what it could not. A type that cannot promise both says so in its listing, in plain words,
   and is still a valid type.

6. **`process` and `http` always exist; every other type is optional.** `process`
   runs any command and `http` calls any endpoint, and neither needs anything
   installed. `amplifier` ships ready to configure and is the type this family's own
   managers run on by choice, never by requirement: a person who configures no
   agent type but Claude Code loses nothing. Claude Code, Codex and GitHub Copilot follow as thin
   types over their command lines; later types arrive by the agents part's own
   process, never by a change here.

## What v1 deliberately does NOT freeze

- **The attach mechanism itself** (a terminal multiplexer, a pty server, a
  container's exec) — promoted when a second type needs the same one and they
  disagree.
- **Resume across a type's own session boundary** (a run continued after its
  process ended) — promoted the first time a manager run outlives its process.
- **Sandboxed and remote runs** — promoted when a type runs anywhere but the host
  or an isolated twin of it.

## Conformance kit asserts

- Every listed type answers `testEnvironment()` in plain words within ten seconds
  and names what is missing when something is.
- A run launched by any type receives exactly the wake variables and nothing from
  configuration.
- A type's `end` carries one of the three words and a cause or a call; a fourth word
  is refused by the service.
- For each terminal type: a person attaches to a live session by the mechanism the
  type names, the service is restarted, and the session is still running and still
  attachable afterwards — recorded with the date and the host.

## Reserved / open questions (NOT frozen)

- Whether the `amplifier` type drives sessions through the CLI's command line or
  the runtime it is built on; the agents part decides and its contract says which.
