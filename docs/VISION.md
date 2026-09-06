# Amplifier Converge — Vision (DRAFT)

*Drafted 2026-09-06 on the steward's sentences and a reading of Paperclip
(ai_working/paperclip-study/). A proposal until the steward answers.*

---

## Where this is going

Amplifier Converge is the app a person opens to run vision-first, contract-driven
work with a team of agents — and the harness that runs them. It is one experience
made of several small projects, each a Converge project in its own right, held
together by contracts at their seams rather than by one repository.

A person — the **intent steward** — picks a project in the app, picks what kind
of agent will manage it, and presses go. A **manager session** wakes, reads the
project's vision and contracts, and derives the work. It launches **worker
sessions** in **lanes**, each a bounded piece with its own working copy, and each
lane is a **run**: a record the app shows live — queued, running, ended with proof
or stuck with a cause, merged. The steward reads plain sentences, answers the four
calls that only a person can answer, and otherwise is never the bottleneck.

Every actor speaks one surface. The app, a command line, the manager session, and
every worker session — whatever agent runs them — talk to **the Converge service**
through the same API, and what the API records is the truth: a claim on a work
item, a run's state, a call put to the steward, a check the manager re-ran. What an
agent prints is telemetry; what it tells the service is fact.

Agents are brought, not built in. An **agent type** is a small adapter — start a
run with this identity and this wake prompt, stream what it says, report how it
ended — and Amplifier is the one that ships first, with a bare process and an HTTP
endpoint always available so anything else can be wired in, and the usual
command-line agents following as thin adapters. A manager can be any agent type;
so can any worker. The method does not depend on which agent runs it, because the
method is in the contracts and the service enforces what a contract can enforce.

The through-line: the vision and contracts of each project are the one text both
people and machines obey, and the top-level project's contracts are the seams
between the parts — so a part can begin as a wrapper around something that exists
and later become its own first-class experience without the whole moving.

---

## Principles

1. **One experience, many projects.** Amplifier Converge is the top-level project;
   the service, the app, the agent types, the queue and the method are
   sub-projects, each with its own vision, contracts, ledger, queue and manager.
   The top level holds the seams and names its parts; it holds no part's internals.

2. **The API is the truth.** Anything worth knowing about a run, a claim, a call or
   a check is a record the service holds; a file, a terminal or a log is evidence
   of it, never the source. If two disagree, the service's record wins and the
   disagreement is a defect.

3. **Bring your own agent; the method stays the law.** Any agent type can run a
   manager or a worker. What it must do — claim, resolve, file, call, heartbeat,
   and for a manager re-run the check — is in the wake contract and the service's
   gates, not in the agent.

4. **A run is a record, not a process.** A run has a beginning, a state, an
   ending in exactly one of three ways — done with proof, stuck with a cause,
   needs the steward — and a merge. Where its process lives, and whether it is one
   long session or many, is the agent type's business.

5. **Start as a wrapper, become a body.** A sub-project may begin by fronting
   something that exists — the shared work queue, today's lane launcher, today's
   app — behind the seam the top level names. Its contract is with the seam; what
   is behind it can be swapped without a word from the steward.

6. **The steward answers four things and reads sentences.** Ratify a change of
   direction, allow an irreversible act, perform a check only a person can, set a
   priority or stop. Everything else keeps moving, and what reaches them is
   written for a person who has never opened a code editor.

7. **Nothing is installed twice and nothing lands outside the project.** One
   command composes the whole experience onto the Amplifier a person already
   has; every project's operation state lives under that project's own
   workspace; a control plane sits lightly on the host it runs on.

8. **Endpoints are read from the router, never from prose.** What an agent is
   told it may call is generated from what the service actually serves, and a
   check fails the moment they drift.

---

## What this is not

- **Not a monorepo** — the parts are repositories with their own lives; the top
  level references them, it does not contain them.
- **Not an org chart, a company, or a budget-first system** — one steward per
  project; roles are modes, not hires; budgets arrive as a gate when a
  sub-project earns one.
- **Not a rewrite of what shipped** — `amplifier-bundle-converge` (the method:
  contracts, ledger, kits, mode) becomes the method sub-project as it is; the app
  and the lane launcher become the first bodies behind their seams.
- **Not a scheduler that re-spawns agents on a tick** — the service observes runs
  (heartbeat age, markers, commits); the agent type decides how a run lives.
- **Not cloud-first** — a run happens on the host or in a Digital Twin before any
  remote sandbox is an agent type.

---

## How you can tell it is working

- The app's project picker lists the top-level project and every sub-project
  registered to it, and each one opens to its own vision, contracts, ledger,
  queue and managers.
- A manager session launched from the app or from the CLI, on any built-in agent
  type, appears on Home within a minute with its lanes as live runs.
- Two managers run two sub-projects at once without sharing a file, a queue item
  or a call.
- A worker run ends in exactly one of three states every time, and the service
  refuses to mark a run merged until the manager's re-run check is on record.
- A sub-project's implementation is swapped behind its seam and every kit and
  ledger row of the top level reads the same before and after.

---

## Changelog

- **2026-09-06 — v1 (DRAFT).** From the steward's sentences ("not a monorepo;
  modular; sub-projects with their own managers; the main repo holds the top-level
  vision and contracts and is aware of the others; swappable parts; BYO agent with
  Amplifier built in"), the Paperclip reading, and the shipped
  `amplifier-bundle-converge` (2026-09-02 → 09-06).
