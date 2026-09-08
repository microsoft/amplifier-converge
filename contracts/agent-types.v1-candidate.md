target: contracts/agent-types.v1.md
proposal: family.v1p7

# Agent Types Contract — family.v1p7 candidate (proposal)

## The exact change

### 1. What it is — public names and shapes

Current text:

```
A type is three functions, and a run is what one of them starts:

```

Replacement:

```
A type is three capabilities, and a run is what one of them starts:

```

Current text:

```
type()                      -> "amplifier" | "process" | "http" | "claude-code" | ...
testEnvironment()           -> { ok: bool, missing: ["tmux", ...], words: "Install tmux ..." }
execute(context, callbacks) -> callbacks.log(text) · callbacks.event(name, at, data)
                               callbacks.end(done | stuck | waiting, cause_or_call)

context = { run_id, project, role, api_url, token, prompt, skill }   # from the service
env     = CONVERGE_RUN_ID · CONVERGE_PROJECT · CONVERGE_ROLE · CONVERGE_API_URL · CONVERGE_TOKEN
```

Replacement:

```
name (property)             -> "amplifier" | "process" | "http" | "claude-code" | ...
test_environment()          -> HostAnswer: can_run; missing things (what, why, remedy); sentence()
execute(wake, callbacks)    -> callbacks.log_line(text) · callbacks.event(name, detail='')
                               callbacks.seen_alive(at=None) · callbacks.ended(word, detail='')

wake = identity + prompt + skill   # conceptual payload; field mapping is unchanged
env  = CONVERGE_RUN_ID · CONVERGE_PROJECT · CONVERGE_ROLE · CONVERGE_API_URL · CONVERGE_TOKEN
```

### 2. Promise 1 — three capabilities

Current text:

```
1. **Three functions, nothing else required.** `type`, `execute`, `testEnvironment`.
   Anything more a type offers is its own business.
```

Replacement:

```
1. **Three capabilities, nothing else required.** `name` (a property),
   `execute(wake, callbacks)`, `test_environment()`. Anything more a type offers is its
   own business.
```

### 3. Promise 3 — reports and the ending callback

Current text:

```
3. **The type reports; the service records.** Callbacks carry facts — started, alive at
   T, printed this, ended this way. A type never writes a record itself. `end` names one
   of `done`, `stuck`, `waiting`, with the cause or the call.
```

Replacement:

```
3. **The type reports; the service records.** Callbacks carry facts — an event, seen alive
   at T, a printed line, and an ending. A type never writes a record itself.
   `ended(word, detail='')` accepts one of `done`, `stuck`, `waiting`; `stuck` carries the
   cause and `waiting` the call.
```

### 4. Promise 5 — environment check spelling

Current text:

```
5. **A person can attach, converse with a manager, and the session survives.** A terminal
   type names how a person attaches (a read) and, for a manager run only, converses with
   it from the desk's console (a write, recorded as a *steer*) — from the app, or a
   terminal if they choose — and how the session outlives the instance restarting and the
   person disconnecting. `testEnvironment()` checks that mechanism; the instance installs
   what is missing when it can and says what it could not. A type that cannot promise all
   three says so in its listing and is still valid.
```

Replacement:

```
5. **A person can attach, converse with a manager, and the session survives.** A terminal
   type names how a person attaches (a read) and, for a manager run only, converses with
   it from the desk's console (a write, recorded as a *steer*) — from the app, or a
   terminal if they choose — and how the session outlives the instance restarting and the
   person disconnecting. `test_environment()` checks that mechanism; the instance installs
   what is missing when it can and says what it could not. A type that cannot promise all
   three says so in its listing and is still valid.
```

### 5. How the kit checks it — public spellings

Current text:

```
- Every listed type answers `testEnvironment()` within ten seconds, in plain words, naming what is missing.
- A run receives exactly the five `CONVERGE_*` variables and nothing from configuration.
- `end` with a fourth word → refused by the service.
- For each terminal type: attach, restart the instance, still attached — recorded with date and host.
```

Replacement:

```
- Every listed type answers `test_environment()` within ten seconds, in plain words, naming what is missing.
- A run receives exactly the five `CONVERGE_*` variables and nothing from configuration.
- `callbacks.ended(word, detail='')` with a fourth word → refused.
- For each terminal type: attach, restart the instance, still attached — recorded with date and host.
```

### 6. Changelog — future row after the steward's word

Current text:

```
| 2026-09-07 | Promise 5 amended (a person may converse with a manager run from the desk's console — a write recorded as a *steer*) — proposal ratified. | `docs/workflow/agent-types.v1-candidate.ratified.md`; steward's word. |
```

Replacement:

```
| 2026-09-07 | Promise 5 amended (a person may converse with a manager run from the desk's console — a write recorded as a *steer*) — proposal ratified. | `docs/workflow/agent-types.v1-candidate.ratified.md`; steward's word. |
| YYYY-MM-DD | Corrected the public seam description to the existing Python `AgentType` and `Callbacks` names and shapes; no runtime API or implementation changed. | Review evidence: `amplifier-converge-agents/src/amplifier_converge_agents/agent_type.py:118-145`; `amplifier-converge-agents/src/amplifier_converge_agents/reporting.py:231-279`. |
```

## The evidence

The reviewed public Python source already defines `AgentType.name` as a property,
`AgentType.execute(wake, callbacks)`, and `AgentType.test_environment()` in
`amplifier-converge-agents/src/amplifier_converge_agents/agent_type.py:118-145`.
The existing `Callbacks` API is `log_line(text)`, `event(name, detail='')`,
`seen_alive(at=None)`, and `ended(word, detail='')` in
`amplifier-converge-agents/src/amplifier_converge_agents/reporting.py:231-279`.
`ended` rejects a word outside `done`, `stuck`, and `waiting`, and requires detail
for `stuck` and `waiting`, in that same file at `reporting.py:155-188`.

These source citations are evidence for this family-seam description correction, not new implementation
coupling or a dependency on a neighbour's internals. This family proposal and the
corresponding `amplifier-converge-agents/contracts/agent-types.v1-candidate.md` are
coordinated review proposals describing the same existing public API; neither proposes
a runtime dependent diff.

## What does NOT change

- The source contract, `contracts/agent-types.v1.md`, remains unchanged unless the
  steward ratifies this `family.v1p7` proposal.
- No adapter, compatibility alias, callback transport, runtime API, implementation,
  or test change is proposed.
- The optional manager-only steer remains a recorded manager interaction; this proposal
  does not name or add a new agent-type capability for it.
- The five existing `CONVERGE_*` environment-token promises remain exactly as written.
- Callback wire format remains deferred. This proposal does not specify an HTTP endpoint,
  event schema, polling, or push transport.
- The prior ratification recorded for Promise 5 is not evidence for this correction and
  is not extended or re-ratified by it.

## Residual

The environment literal names and identity-field mappings remain unaligned by this
proposal: the family contract still names `CONVERGE_*`, while the local description uses
`RUN_ID PROJECT ROLE API CREDENTIAL` and local `Wake` exposes `project_id` and
`credential`. This proposal makes no claim of full payload or environment alignment.

## The steward's decision

**Pending:** ____________________
