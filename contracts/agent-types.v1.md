# Agent Types Contract — v1 (RATIFIED 2026-09-06)

What an agent type owes the family and what the family owes it, so a manager or a
worker can be Amplifier, Claude Code, Codex or GitHub Copilot and the steward sees one
operation. Read by the agents part, the service, and the app.

## Who builds against this

**The agents part** implements every type. **The service** launches runs through a type
and records what it reports. **The app** lists types, offers "test this environment",
and attaches a person to a live session.

## What it is

A type is three functions, and a run is what one of them starts:

```
type()                      -> "amplifier" | "process" | "http" | "claude-code" | ...
testEnvironment()           -> { ok: bool, missing: ["tmux", ...], words: "Install tmux ..." }
execute(context, callbacks) -> callbacks.log(text) · callbacks.event(name, at, data)
                               callbacks.end(done | stuck | waiting, cause_or_call)

context = { run_id, project, role, api_url, token, prompt, skill }   # from the service
env     = CONVERGE_RUN_ID · CONVERGE_PROJECT · CONVERGE_ROLE · CONVERGE_API_URL · CONVERGE_TOKEN
```

## The promises

1. **Three functions, nothing else required.** `type`, `execute`, `testEnvironment`.
   Anything more a type offers is its own business.

2. **The wake is the whole context.** Identity in the environment, one rendered prompt,
   the `amplifier-converge` skill. A type adds nothing the service did not hand it; a run
   learns nothing from disk it was not pointed at.

3. **The type reports; the service records.** Callbacks carry facts — started, alive at
   T, printed this, ended this way. A type never writes a record itself. `end` names one
   of `done`, `stuck`, `waiting`, with the cause or the call.

4. **Liveness is a timestamp.** A type reports when it last saw the run alive, never a
   state word. *Quiet* and *silent* are the reader's derivation.

5. **A person can attach, converse with a manager, and the session survives.** A terminal
   type names how a person attaches (a read) and, for a manager run only, converses with
   it from the desk's console (a write, recorded as a *steer*) — from the app, or a
   terminal if they choose — and how the session outlives the instance restarting and the
   person disconnecting. `testEnvironment()` checks that mechanism; the instance installs
   what is missing when it can and says what it could not. A type that cannot promise all
   three says so in its listing and is still valid.

6. **`process` and `http` always exist; every other type is optional.** They need nothing
   installed. `amplifier` ships ready to configure and is what this family's own managers
   run on — by choice, never by requirement.

## Not in v1

- **The attach mechanism itself** (a multiplexer, a pty server, a container exec) — until a second type needs the same one and they disagree.
- **Resuming across a type's own session boundary** — the first time a manager run outlives its process.
- **Sandboxed and remote runs** — when a type runs anywhere but the host or an isolated twin of it.

## How the kit checks it

- Every listed type answers `testEnvironment()` within ten seconds, in plain words, naming what is missing.
- A run receives exactly the five `CONVERGE_*` variables and nothing from configuration.
- `end` with a fourth word → refused by the service.
- For each terminal type: attach, restart the instance, still attached — recorded with date and host.

## Open questions

- Whether `amplifier` drives sessions through the CLI's command line or the runtime beneath it; the agents part decides and says which.

## Changelog

| Date | Change | Evidence |
|---|---|---|
| 2026-09-06 | v1 drafted; attach-and-survive written as a promise on the steward's words; ratified as content. | Steward's words, 2026-09-06. |
| 2026-09-07 | Reshaped into the family format on the steward's word ("port it"); no promise changed. | `docs/FORMAT.md`. |
| 2026-09-07 | Promise 5 amended (a person may converse with a manager run from the desk's console — a write recorded as a steer) — proposal ratified. | `docs/workflow/agent-types.v1-candidate.ratified.md`; steward's word. |
