# Amplifier Converge vNext — the plan (DRAFT, for discussion)

*Written 2026-09-06 after: the Paperclip reading (`ai_working/paperclip-study/`), the
council review (`docs/workflow/COUNCIL-2026-09-06.md`), and the eleven-day session
chronicle of v1 (`ai_working/paperclip-study/SESSION-CHRONICLE.md`). This is a plan
for talking, not a contract. Nothing here is law until it is in a ratified document.*

---

## 0. Stance

**v1 stays.** `amplifier-bundle-converge` is a product people can install and use
today: the method (contracts, ledger, kits, the manager mode), an app, an adopter
harness that is green on both first-wake paths. It is kept as it is. Its frozen
vision — *"Converge is the method, not the project"* — remains true of v1 and is not
amended by anything here.

**vNext is a new product with a different architecture,** built for exactly one job:
getting work done the Converge way, with a person's attention spent only where a
person is irreplaceable. It is bespoke and trim on purpose. It does not inherit the
obligations of the components v1 borrowed (the Amplifier CLI's highway skill, tmux,
the general-purpose work-tracker, a FastAPI app grown inside the method repository).
Where v1 wrapped, vNext owns — a harness, an app, a service, a queue, session
management — each small, because each serves this one thing.

**What carries over unchanged:** the method as the law (vNext's documents are written
under v1's `documents.v1`; the manager's obligations are v1's `operation.v1`), and
the lessons — seventeen incidents, fourteen hand-rolled mechanics, thirty-eight
direction-setting words — catalogued in the chronicle. The recurring shape of every
incident was the same: *the verification layer certified the wrong thing* (a deleted
worktree, a moving count, a stale export, build detritus). vNext's first design rule
follows from it: **a fact the system judges by is a record the system wrote, or an
observation it timestamped — never a thing it inferred from the disk.**

---

## 1. The council's advice, taken and not taken

Taken (all of it except one item):

- **Nothing empty.** No registry row for a repository that does not exist. A part
  earns its row by existing *as a Converge project* — a repository with a vision and a
  first contract, even before it has a body. New status word: `seeded` (direction
  exists, no body yet) · `wrapper` · `body` · `retired`. A row's status is read by the
  family kit, so the word is a control, not a comment.
- **`service.v1` is rewritten from the first run that flows**, at six teeth or fewer,
  under a hundred lines: freeze `run` and `check`; the other records wait for the first
  one to flow. No pushed-stream clause (the app polls, deliberately, with a measurement
  on record). No service tick that *maintains* a liveness state — liveness is an
  **observation with a timestamp**, made by the agent type.
- **The merged-gate names what it does not prove.** Run ↔ manager is an edge; a
  manager token tier exists; `merged` is a *request*, not a report; "could not check"
  is a third answer that never collapses to false; scalars, never a free-text blob.
- **The steward's five writes have homes before any path is called a defect.**
- **One owner of custody.** Whatever is behind the queue seam owns custody; the
  service records it read-only.
- **The steward is not the bottleneck on seams.** Seam changes are proposals, but the
  family manager batches them into one sheet; "at most five things ask for your word
  at once" is per family, not per part.
- **A success bullet has a person and a number in it.**

Not taken: **the repository split.** The steward's call, and the reason is not
disputed by the council's own arithmetic — collapsing repos removed two of twenty
breaks. We want the split because we will build fast and in parallel, and because
*nested Converge projects* is itself the pattern to validate: several manager
sessions, each knuckled down on one part, learning and iterating on the method as we
go. The cost the council priced (five visions, five contract sets, five ratification
queues) is met by the family manager drafting the seeds in one sitting and putting
**one sheet** to the steward.

Two collisions the split dissolves rather than creates: the picker is not "a third
place" against v1's `experience.v1`, because vNext's app has its own experience
contract; and v1's frozen vision needs no candidate, because vNext is a different
product, not an amendment of v1.

---

## 2. The family

Each is a repository, a Converge project in full (vision, contracts, ledger, queue,
its own manager session), registered in `family.toml`, bound to its neighbours only
by the seam contracts held here.

| Part | Repository | Owns | Starts as |
|---|---|---|---|
| **amplifier-converge** (this) | `microsoft/amplifier-converge` | family vision, seam contracts, registry, the ledger that reads the seams, the family's manager | body |
| **service** | `microsoft/amplifier-converge-service` | the control plane: records (`run`, `check` first; then `project`, `session`, `claim`, `call`), one HTTP API, an event log, a single SQLite file under `<workspace>/.converge/<project>/service/`, endpoint docs **generated from the router**, refusals | seeded → body |
| **app** | `microsoft/amplifier-converge-app` | the experience: create a project · attach repositories · onboard them (the first wake, driven from the screen) · Home · Direction · Operation · Review · the four calls · the steward's writes · the family picker · BYO agent choice. Reads only the service | seeded → body |
| **agents** | `microsoft/amplifier-converge-agents` | agent types and **session management**: the adapter contract, the wake contract, the `amplifier` type built in (launch, resume, observe an Amplifier session without tmux), `process` and `http` always, then Claude Code · Codex · Cursor · Gemini as thin adapters | seeded → body |
| **queue** | `microsoft/amplifier-converge-queue` | the work queue with custody, trim and bespoke; one owner of custody | wrapper over `amplifier-work-tracker` → body |
| **method** | `microsoft/amplifier-bundle-converge` (v1) | the law: `documents.v1`, `operation.v1`, the ledger format, the kits, the manager mode, the templates | body (v1, unchanged) |

The council was right that **service and agents are one lifecycle**. Splitting them
before it is written is a risk we take knowingly; the mitigation is a seam contract
between them — `agent-types.v1`, drafted now, not later — and the rule that the
run's lifecycle transitions are the service's records while the run's *process* is
the agent type's business.

---

## 3. The seams (top-level contracts)

1. **`family.v1`** — how parts compose (drafted; to be corrected: `seeded` status;
   rows only for existing repositories; `<part-id>` everywhere; the method part named
   as v1; the tracker removed as a "part" and re-entered as what stands behind the
   queue seam).
2. **`service.v1`** — one API is the truth (drafted at eleven teeth; **to be rewritten
   at ≤6 after the first run record flows**, per the council).
3. **`agent-types.v1`** — the adapter contract (`type · execute(ctx) → onLog/onEvent/
   onEnd · testEnvironment()`), the wake contract (identity in env: run id, project,
   role, API URL, scoped token; one rendered prompt; the `converge` skill), liveness as
   an observation the type makes, and the rule that a type never writes a record the
   service did not ask for. **Not yet drafted — the seam the synthesis called for.**
4. **`experience.v1` (vNext)** — the app's own contract, in the app repository, not
   here; the family only names that it exists and what the picker must show.

---

## 4. The experience vNext must have that v1 never did

- **Create a project.** Name → workspace root (created) → vision drafted from the
  template on the screen → choose the manager's agent type → go. The first wake's
  *starting* path, from the UI.
- **Attach existing repositories.** Path or URL → the app reads them: already a
  Converge project (has `docs/VISION.md` + `contracts/`) → registered; not yet →
  **onboarding**.
- **Onboard a repository** (the *adopting* path, from the UI): pause the work in
  flight and say so; investigate — the four answers appear as sentences the steward
  can hold against what they know; drafts appear as documents to react to; the word
  is given in the app; the ledger is seeded and the alignment items filed; each step
  visible, none skipped, none silent.
- **The family, visible.** The picker lists the family's parts *and the steward's own
  projects*; each opens to its own Direction and Operation; a manager on any part
  appears within a minute of waking.
- **Bring your own agent, from the screen.** Choose the manager's type and the default
  worker type per project; "test this environment" before the first run.
- **Runs, live.** Lanes as records with their three endings; a `kill -9` yields
  "Silent — may have died" *and* an observation row with a time; merged only on a
  check the manager made.

Everything v1's experience taught — two places, plain words, the four calls, the
return brief, presence, offline read, restore — is carried into vNext's experience
contract by the app's own manager, not re-derived here.

---

## 5. Phases (each a wave; each with a measured bar)

**Phase 0 — seed the family (this week).**
Correct `family.v1` and `family.toml` to the council's lift conditions (no row without
a repository; `seeded`; one id form). Draft `agent-types.v1`. Create the four
repositories and seed each with its first wake: `docs/VISION.md` (DRAFT) · one first
contract (DRAFT) · the participant kit from v1's templates · `AGENTS.md` naming the
family and the seam it builds against. Register each in `family.toml`. Write the
family kit (the first reader of `family.toml`). **One sheet to the steward:** the
family vision, three seams, four part-visions, four first contracts. **Bar:** the
family kit green on five real rows; v1's documents kit green on every seeded repo.

**Phase 1 — one run record flows (the pipe).**
Service: `run` + `check` records, SQLite, the API for them, the merged-gate refusal.
Agents: the `amplifier` type launches one Amplifier session as a lane, reports start,
liveness observations and its ending. App: Home shows that run live. **Bar — the
council's three break-tests, pasted:** `POST /runs` without a liveness handle is
refused (400); `kill -9` yields *Silent — may have died* plus an observation row; an
empty branch + `command:"true"` + `merged` is **refused with the reason**. Then
`service.v1` is rewritten from what this taught, ≤6 teeth, kit green.

**Phase 2 — the manager through the service.**
The family's own manager (Amplifier, converge-manager mode) launches its lanes through
the service; the queue wrapper fronts the tracker with one custody owner; calls and
the steward's writes become records; the plan record, the call stamp and the check
record are records the app renders. **Bar:** this family's next wave runs with no
shell script, no `manifest.tsv`, no marker file — every fact v1 hand-rolled is a row.

**Phase 3 — the experience.**
Create · attach · onboard from the screen; the picker; BYO manager from the screen;
the usual-suspect adapters. **Bar:** v1's adopter harness, ported — a fresh container,
an AI user who has read only the README, both first-wake paths green — plus a third
scenario: *attach and onboard an existing repository from the app*.

**Phase 4 — bodies replace wrappers.**
The bespoke queue replaces the tracker behind its seam; budgets arrive as a gate;
v1's app is retired when vNext passes v1's adopter bar and v1's experience contracts
read the same against vNext. **Bar:** every swap leaves every top-level ledger row
reading the same before and after.

Throughout: **v1 keeps running.** The steward opens v1's app on Monday; there is no
transit window in which nothing works.

---

## 6. How we know it is working (with a person and a number)

- A steward creates a project, attaches a repository that has never seen Converge,
  and reaches a ratified vision and a seeded ledger **in under an hour without opening
  a terminal**.
- Five manager sessions run five parts at once; **zero** shared files, queue items or
  calls between them (the family kit reads this).
- A run's three endings are the only endings observed across a wave; **zero** runs
  marked merged without a manager's check (the service refuses; the ledger counts).
- The steward's hours-to-notice for a stalled lane, measured in v1's report card,
  falls from *hours* to **under fifteen minutes**, because an observation row is
  written and shown, not inferred.
- One install command still composes the whole family onto the Amplifier a person
  already has (v1's `composition.v1` Core 5, kept).

---

## 7. Decisions for the steward (this sheet)

1. **Names.** vNext takes the product name *Amplifier Converge*; v1 is referred to as
   *Converge v1 — the method bundle* in vNext's documents (v1's own files unchanged).
   *Word: yes / other.*
2. **The status word `seeded`** for a part with direction and no body (the council's
   `planned` dispute, resolved by making the row real). *Word: yes / delete rows.*
3. **Service and agents as two repositories**, with `agent-types.v1` as the seam
   between them, taking the council's one-lifecycle risk knowingly. *Word: yes / one.*
4. **Seed all four repositories this week and receive one ratification sheet**
   (family vision + three seams + four part-visions + four first contracts).
   *Word: go / fewer.*
5. **First agent types after `amplifier`, `process`, `http`:** Claude Code, Codex,
   Cursor, Gemini — in that order? *Word: order / other.*
