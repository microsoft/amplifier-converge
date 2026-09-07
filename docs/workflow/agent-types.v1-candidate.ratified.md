> **RATIFIED 2026-09-07** — the steward's word: "consider ratified". Applied exactly the same day; the target carries the change.

# Agent Types Contract — v1 candidate (proposal)

**Target.** `contracts/agent-types.v1.md`, Promise 5. Rebased 2026-09-07 onto the reshaped text; the change is the same.

## The exact change
Before:
```
5. **A person can attach, and the session survives.** A terminal type names how a person
   attaches — from the app, or a terminal if they choose — and how the session outlives
   the instance restarting and the person disconnecting. `testEnvironment()` checks that
   mechanism; the instance installs what is missing when it can and says what it could
   not. A type that cannot promise both says so in its listing and is still valid.
```
After:
```
5. **A person can attach, converse with a manager, and the session survives.** A terminal
   type names how a person attaches (a read) and, for a manager run only, converses with
   it from the desk's console (a write, recorded as a *steer*) — from the app, or a
   terminal if they choose — and how the session outlives the instance restarting and the
   person disconnecting. `testEnvironment()` checks that mechanism; the instance installs
   what is missing when it can and says what it could not. A type that cannot promise all
   three says so in its listing and is still valid.
```

## The evidence
Transcript (403) "Conversation becomes a modality, not a place"; (783) "we'll call it manager console"; (843) "an actual pane that when active just remains in place." The agents part's ratified clause — attaching is a read, never a write — permits watching and forbids the console. A UI copilot as an agent type stays deferred on the steward's own word (853), recorded in `desk.v1`.

## What does NOT change
Promises 1–4, 6; the three-functions shape; liveness as a timestamp.

## The steward's word
_(ratified · ratified with edits · declined · later)_
