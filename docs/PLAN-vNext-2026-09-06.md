# Amplifier Converge — the plan (DRAFT, for discussion)

*Written 2026-09-06 from the steward's sentences, a reading of Paperclip
(`ai_working/paperclip-study/`, outside this repo), and a six-lens council review of
the first drafts (`ai_working/council-converge-family/`, outside this repo). A plan
for talking. Nothing here is law until it is in a ratified document.*

---

## 0. Stance

Amplifier Converge is a new product, built for exactly one job: getting work done the
Converge way, with a person's attention spent only where a person is irreplaceable.
It is bespoke and trim on purpose. Every part serves this experience and owes nothing
to another product's users — so a queue is a queue with custody, a service is a few
records and one API, an adapter is three functions, and a session manager knows one
kind of session.

Two rules follow from the practice that preceded this and from the council:

- **A fact the system judges by is a record it wrote, or an observation it
  timestamped — never something inferred from the disk.** Every prior incident had
  the shape "the verification layer certified the wrong thing".
- **Nothing exists on paper before it exists in a repository, and nothing is
  frozen before it has flowed once.** A part is registered when its repository
  carries a vision and a first contract; `service.v1` is rewritten from the first
  run that flows.

Day-one installability decides the architecture: **Amplifier Converge installs on
its own and runs as one instance on a person's machine** — one local service with a
browser in front of it — depending on no other product. It creates workspaces,
clones repositories, launches and supervises manager sessions, and keeps every
record in a data directory it owns; a person never opens a terminal for any of it.
Amplifier is one agent type among several, shipped ready to configure and never
required. That is why the queue is ours, not borrowed, and why the instance — not
a person's shell — is where sessions live.

---

## 1. The council's advice — taken, except one

Taken:

- **Nothing empty.** A part earns its registry row by existing as a Converge project
  (vision + first contract). Status `seeded` names direction-without-body honestly;
  the family kit reads it, so it is a control, not a comment.
- **`service.v1` at six teeth, under a hundred lines, freezing `run` and `check`
  only**, rewritten from evidence after the first run. No pushed-stream clause; no
  service-maintained liveness — liveness is an observation with a time, made by the
  agent type.
- **The merged-gate names what it does not prove.** Run ↔ manager is an edge, a
  manager token tier exists, `merged` is a request the service may refuse, scalars
  only, and "could not check" is an open question the first run must answer.
- **The steward's writes have homes before any path is called a defect.**
- **One owner of custody** — the queue part. The service records what the queue
  says.
- **The steward is not the bottleneck on seams** — proposals batched into one sheet.
- **Success bullets carry a person and a number.**

Not taken: **the repository split.** The steward's call. We build fast and in
parallel, and *nested Converge projects* — several managers each knuckled down on one
part — is itself the pattern to validate. The council's own arithmetic does not
contest it (collapsing repos removed two of twenty breaks). The cost the council
priced — several visions, contract sets and ratification queues — is met by the
family manager launching each part's first wake and putting **one sheet** to the
steward.

---

## 2. The family — six repositories

Each is a Converge project in full, registered in `family.toml` once it carries a
vision and a first contract, bound to its neighbours only by the seam contracts held
here. Private under `bkrabach/` today; moved together once proven.

| Part | Repository | Owns |
|---|---|---|
| **top level** | `amplifier-converge` | family vision, seams, registry, the ledger that reads the seams, the family manager |
| **method** | `amplifier-converge-method` | the law, trim: how documents work (draft → ratified → locked; proposals beside locked files), how a manager operates (derived work, lanes, verification, the four calls, the first wake), the ledger format and the verdict words, the kits, the templates, the manager mode and the wake skill |
| **service** | `amplifier-converge-service` | the control plane inside the instance: `run` and `check` first; one HTTP API; one store in the instance's data directory scoped by project; endpoint docs generated from the router; refusals |
| **app** | `amplifier-converge-app` | the experience: create a project · attach repositories · onboard them from the screen · the picker · direction · operation · runs live · the four calls · the steward's writes · BYO agent choice · "test this environment". Reads only the service |
| **agents** | `amplifier-converge-agents` | agent types and session management: the adapter contract, the wake contract, attach-and-survive (a person attaches from the app or a terminal; a session outlives the instance's restart), `process` and `http` always, `amplifier` ready to configure and never required, Claude Code · Codex · GitHub Copilot as thin adapters; later Pi, OpenCode, others |
| **queue** | `amplifier-converge-queue` | the work queue with custody, bespoke: items naming a contract, atomic claim, one custody owner with renewal and reclaim, discovered-work links, plain-word states. Embedded in the instance, one store per project; learned from prior queue designs, owing them nothing |

The council was right that **service and agents are one lifecycle**. We split them
knowingly; the mitigation is `agent-types.v1` drafted *now* as the seam between them,
and the rule that a run's transitions are the service's records while a run's
process is the agent type's business.

---

## 3. The seams (top-level contracts)

1. **`family.v1`** — how parts compose (drafted).
2. **`service.v1`** — one API is the truth; two records frozen (drafted; rewritten
   from evidence after the first run).
3. **`agent-types.v1`** — the adapter contract (`type · execute(ctx) → onLog/onEvent/
   onEnd · testEnvironment()`), the wake contract (identity in env — run id, project,
   role, API URL, scoped token; one rendered prompt; the `amplifier-converge` skill), liveness
   as an observation the type makes, and the rule that a type never writes a record
   the service did not ask for. **To draft in Phase 0.**
4. **`queue.v1`** — the seam the service fronts: items, claim, custody, resolve,
   file. **To draft in Phase 0.**

Each part's own contracts (the app's experience, the method's documents and
operation) live in the part's repository; the family names only that they exist.

---

## 4. The experience this must have

- **Install and first run.** On a machine with `uv` and `git` (the README says how
  to get `uv`): `uv tool install git+https://github.com/bkrabach/amplifier-converge`,
  then `amplifier-converge` — the instance starts, the browser opens, the person is
  asked only what the instance cannot know (where to keep its data, default
  `~/.amplifier-converge/`; which agent types to configure now, if any). The command
  carries the usual suspects for setup and check-in — `doctor`, `setup`,
  `start`/`stop`/`restart`/`status`, `logs`, `open`, `update`, `uninstall`,
  `agents list|test` — and nothing that belongs on the screen.
- **Create a project.** Name → the instance creates the workspace → vision drafted
  from the template on the screen → the manager's agent type chosen → go. The first
  wake's starting path, from the UI.
- **Attach existing repositories.** A URL or a path → the instance clones or
  registers it: already a Converge project → registered; not yet → **onboarding**.
- **Onboard a repository** (the adopting path, from the UI): pause the work in flight
  and say so; investigate — the four answers appear as sentences the steward can hold
  against what they know; drafts appear as documents to react to; the word is given
  in the app; the ledger is seeded and alignment items filed; each step visible,
  none skipped, none silent.
- **The family and your own projects, visible.** The picker lists both; each opens to
  its own direction and operation; a manager on any part appears within a minute of
  waking.
- **Bring your own agent, from the screen.** Choose the manager's type and the
  default worker type per project; "test this environment" before the first run.
- **Runs, live.** Lanes as records with their three endings; a killed lane yields
  *Silent — may have died* and an observation row with a time; merged only on a
  check the manager made.

---

## 5. Phases (each a wave; each with a measured bar)

**Phase 0 — seed the family (days).** Draft `agent-types.v1` and `queue.v1` here.
Create the five part repositories (private). The family manager launches **five part
manager sessions**, each performing its own first wake on a blank repository — the
nested pattern, exercised on day one — and each parking on the steward's word with a
DRAFT vision and one first contract. Register each in `family.toml` as `seeded`.
Write the family kit (the first reader of `family.toml`). **One sheet to the
steward.** *Bar:* the family kit green on six real rows; every part's documents pass
the method's kit.

**Phase 1 — one run record flows.** Service: `run` + `check`, SQLite, the API, the
merged-gate refusal. Agents: the `amplifier` type launches one session as a lane,
reports start, liveness observations and its ending. App: the run shows live.
*Bar — the council's three break-tests, pasted:* `POST /runs` without a liveness
handle refused; a killed lane yields *Silent — may have died* plus an observation
row; an empty branch + `command:"true"` + `merged` **refused with the reason**. Then
`service.v1` rewritten from what this taught.

**Phase 2 — the managers through the service.** The family's managers launch lanes
through the service; the queue is the bespoke one; calls and the steward's writes
become records; plan record, call stamp and check record are records the app
renders. *Bar:* a full wave on this family with no shell script, no manifest, no
marker file — every fact the practice hand-rolled is a row.

**Phase 3 — the experience.** Create · attach · onboard from the screen; the picker;
BYO manager from the screen; Claude Code, Codex, GitHub Copilot adapters. *Bar:* an
adopter harness — a fresh isolated host, an AI user who has read only the README —
green on: new project, attach and onboard an existing repository, both from the app.

**Phase 4 — day one for others.** Install proven on a machine that has nothing else on
it — no Amplifier, no other agent — through to a running instance with a project
created and a repository onboarded from the browser; budgets as a gate;
repositories moved to their public home.

---

## 6. How we know it is working (a person and a number)

- A steward creates a project, attaches a repository that has never seen Converge,
  and reaches a ratified vision and a seeded ledger **in under an hour without
  opening a terminal**.
- Five manager sessions run five parts at once with **zero** shared files, queue
  items or calls (the family kit reads this).
- **Zero** runs marked merged without a manager's check across a wave (the service
  refuses; the ledger counts).
- A stalled lane is visible to the steward within **fifteen minutes** — an
  observation row written and shown, not inferred.
- A person with `uv` installs and reaches a running instance with the browser open
  in **under five minutes**, one command, no other product required; `amplifier-converge
  doctor` reads green on the same machine.

---

## 7. Decisions for the steward (this sheet)

1. **Six parts including `method`** as its own repository (the law must have a home
   of its own; it is what every manager runs on). *Word: yes / fold into top level.*
2. **Service and agents as two repositories** with `agent-types.v1` between them —
   the one-lifecycle risk, taken knowingly. *Word: yes / one.*
3. **Phase 0 mechanism:** the family manager launches five part-manager sessions to
   perform their own first wakes in parallel, and you receive one sheet. *Word: go /
   fewer / I draft them myself.*
4. **Sessions live in the instance**, attachable from the app and from a terminal,
   surviving the instance's restart; the agents part names the mechanism and the
   instance installs it. *Answered 2026-09-06 in discussion.*
5. **Install and names** — `uv` assumed; `uv tool install git+https://…/amplifier-converge`;
   command, service and data directory all `amplifier-converge`; distribution shape and
   a fresh machine's baseline answered by the same words. *Answered 2026-09-06.*
