# Possibly PR set review — 2026-09-17

## Recommendation

**Do not merge the set yet.** The receiving App has no path to create or receive
the binding that Service requires before it can load a review surface. In
addition, every read holds Service's SQLite writer lock through library work.
Resolve those two implementation defects and obtain a steward decision on the
six newly advertised action modes before accepting the linked changes.

This is an exact-snapshot review, not a live-service or browser acceptance.
Review inputs were captured at 2026-09-17 13:41 PDT. PR prose and previously
reported checks were not treated as proof.

| PR | Reviewed base → head | Verdict | Reason |
|---|---|---|---|
| App #2 | `7f59c4de75c53c746ec137af7e9deeff21ad58ad` → `ff3d7c334b0f8132d010bcf52ec85b7b4c366343` | **FAIL** | F-001 leaves the receiving canvas unable to load; F-003 needs an authority decision. |
| Service #2 | `d44fb2d4e7fdecf729247489a3ef7993af6cf2cf` → `ccceea555fe4b8d819f9280a77b3440f8bb1a3ab` | **FAIL** | F-002 serializes routine reads behind library work; F-003 needs an authority decision. |
| Possibly #1 | `5af0dddfa6521dae3e14c225b51266721000f7fd` → `c1cf4aba64eb214c807cba6c243558f8adfb10ee` | **PASS, conditional** | Its adapter intentionally accepts a host-provided binding and does not own Service authority. It cannot make the receiving slice usable until F-001 is resolved. |

## Material findings

### F-001 — No component establishes the required review binding

**Severity:** high
**Owner:** App and the producer that owns the retained exploration, with Service
interface coordination
**Confidence:** high

Service rejects every non-`bind` operation unless an exact binding already
exists for the signed project/person/conversation/scope
(`service/src/amplifier_converge_service/api/experience.py:570-582`). The App's
`LibraryReviewHost` exposes only surface, artifact, thumbnail, and action calls
(`app/web/src/receiving-possibly-host.tsx:52-65`); its only outgoing operation
names are those calls. The app preview context supplies no exploration ID
(`app/src/amplifier_converge_app/server.py:118-128`). The Possibly package
deliberately does not resolve a project-to-exploration binding
(`possibly/docs/library-review.md:7-9`).

I exercised the exact Service head with a temporary TestClient instance and a
fake library. After recording the signed person but before a `bind` request,
`POST .../possibly/surface` returned **409** with
`possibly-stale-scope`; the library was not invoked. This matches the
unavailable path and means the receiving canvas cannot load merely from the
scope that App currently supplies. Existing Service coverage binds in the
fixture before every test (`service/tests/test_possibly_api.py:55-78`), so it
does not exercise the missing handoff.

**Recommended change:** define one explicit producer-to-Service handoff that
has both the signed scope and retained exploration ID. It must create the
binding before App mounts the review, then pass only the bound identity to App.
If App is meant to own this initiation, add a narrowly scoped host input and
App relay instead; do not infer an exploration or select a fallback. Add an
integration test that starts with an unbound receiving context, performs the
authorized bind through the selected owner, and confirms the first surface
loads.

### F-002 — Routine review reads hold the global SQLite writer lock during library work

**Severity:** high
**Owner:** Service
**Confidence:** high

The common review handler begins `BEGIN IMMEDIATE` before it distinguishes a
bind, read, or action (`service/src/amplifier_converge_service/api/experience.py:539-550`).
Consequently `surface`, `artifact`, and `thumbnail` retain the writer lock while
calling the optional library (`service/src/amplifier_converge_service/api/experience.py:584-598`).
The action path also reacquires the same lock before `client.review_action`
(`service/src/amplifier_converge_service/api/experience.py:669-692`). This
turns a slow library read and the renderer's recurring surface refresh into a
global write stall.

I reproduced serialization against the exact Service head in isolated
temporary state: a fake `review_surface` slept for 0.350 seconds after a real
binding was recorded; a second simultaneous authenticated `surface` request
completed only after **0.782 seconds**. Both returned 200. This is bounded
evidence of the lock scope, not a claim about the production library's
latency.

**Recommended change:** do not start an immediate transaction for read-only
operations. For actions, persist the intent and validate the activation under
short transactions around the state transitions, not across external library
work. Preserve the stale-activation fence with a binding revision or
compare-and-set check, and add a concurrent test proving a slow `surface`
cannot delay an unrelated bind or action.

### F-003 — Six Service-mutating modes are advertised before their authority is settled

**Severity:** merge blocker — product/contract decision, not an implementation
bug
**Owner:** intent steward and Experience Interface contract owners
**Confidence:** high

The receiving App enables `select`, `export`, `draft`, `feedback`,
`brief_correction`, and `reject`
(`app/web/src/receiving-possibly-host.tsx:13-20, 68-77`). Service maps each to
an admitted SDK action (`service/src/amplifier_converge_service/api/experience.py:635-646`);
the Service document describes all six as supported
(`service/docs/POSSIBLY-REVIEW.md:31-37`). That is more than neutral profile,
motion, theme, and consumer presentation.

The separately authorized presentation wave says broader action advertising and
context sharing are not yet settled (`GOAL.md:45-49`). The ratified Experience
Interface requires declared versioned operations before use
(`contracts/experience-interface.v1.md:30-35`), but no reviewed ratification
establishes the ownership, effects, or admission of these six modes. The empty
captured PR-comment sets provide no contrary review decision.

**Recommended change:** before merge, either ratify the operation/authority
surface (including which effects remain local versus durable) or narrow the
App and Service to the explicitly approved subset. Do not use this code review
to choose that subset.

## Compatibility, dependency, and collision matrix

| Consumer | Depends on | Verified state | Required before the linked slice can work |
|---|---|---|---|
| App #2 | Possibly adapter #1 artifact at `c1cf4aba64eb214c807cba6c243558f8adfb10ee`; workspace renderer artifact; Service optional review routes | App's recorded adapter checksum matched its documentation; App build and tests passed. | A created, scope-matching Service binding (F-001), the optional Service library, and an action-authority decision (F-003). |
| Service #2 | Optional `possibly` Python package pinned at `28d82b9e00bf39cb9c3384b53cbaac0b1d441f2b` | Normal Service suite passed without the optional package. | Fix the writer-lock scope (F-002); install the optional package; bind an existing exploration; decide action authority. |
| Possibly #1 | Experience SDK artifact and a host that supplies scoped callbacks, renderer, and admitted actions | Adapter test suite passed: 22 passed, 6 pre-existing offline-evidence skips. | A correctly bound host. Its public contract explicitly leaves binding and Service authorization to that host. |

The exact App presentation reference `4d239275370b31f163e86e440dc701557157bae3`
adds `web/src/presentation-state.ts` and its test, not any file changed by App
#2. No same-file collision was established at that exact committed reference.
The PR nevertheless changes the integration hub (`web/src/main.tsx`,
`web/src/native-conversation-host.tsx`, `web/src/style.css`, `web/package.json`,
and `web/package-lock.json`), so it should not be merged concurrently with
uncommitted or newer presentation work without a three-way comparison.

Safe in parallel: the Possibly adapter's isolated fixes and Service's
transaction-scope fix can proceed independently after the authority decision.
Coupled: the binding handoff, the App receiver, and the Service bind endpoint
must be reviewed together.

## Suggested merge order

1. Obtain the steward's decision for the action/authority surface in F-003.
2. Fix and test Service transaction scope (F-002).
3. Implement and test the explicit binding handoff (F-001).
4. Merge/publish the Possibly adapter, rebuild App's immutable vendor artifact,
   verify its checksum, then merge App and Service together.

## Checks run

| Target | Command / method | Result |
|---|---|---|
| App relay | `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -p test_possibly_relay.py -v` | 4 passed |
| App web | isolated copy: `npm ci --ignore-scripts && npm run build && node --test tests/*.test.mjs` | build passed; 121 passed |
| Possibly #1 | isolated copy: `npm ci --ignore-scripts && npm test` | 22 passed; 6 skipped for missing offline browser-evidence fixtures |
| Service #2 | isolated copy: `PYTHONDONTWRITEBYTECODE=1 AMPLIFIER_CONVERGE_HOME=<temporary> PYTHONPATH=src python3 -m pytest -q -p no:cacheprovider` | 489 passed; 5 skipped |
| F-001 | isolated TestClient with signed recorded person and no bind | `surface` returned 409 / `possibly-stale-scope` |
| F-002 | isolated TestClient with two simultaneous bound `surface` reads and a 0.350-second fake library call | second request took 0.782 seconds; both returned 200 |

`npm ci` for the App reported 10 dependency-audit advisories and Vite reported
one 561.00 kB minified entry chunk. Neither was attributed to this PR because
the base lockfile's pre-existing local-package integrity mismatch prevented a
like-for-like base build. They are recorded as non-blocking residuals, not
findings.

## Not run

- `service/tests/test_possibly_api.py` against the actual optional Python
  library: the package was not installed locally. The normal Service suite
  correctly skipped optional-library cases.
- A live App + Service + browser check: prohibited for this review lane, and
  unit/static checks cannot establish it.
- A full accessibility/browser matrix: the Possibly suite records six missing
  offline evidence fixtures; no replacement evidence was manufactured.

## Proposed PR comment text for the coordinator to review

> I found two implementation blockers in this exact snapshot: the receiving
> App never creates or receives the `possibly/bind` handoff required before its
> first `surface` call, and Service holds `BEGIN IMMEDIATE` while executing
> every library read. I reproduced the first as a 409
> `possibly-stale-scope` and the second as serialization of two concurrent
> `surface` requests. The PRs also advertise six durable action modes that the
> presentation-wave brief says are not yet settled. Please establish the
> explicit binding owner, shorten Service transaction scope while retaining its
> activation fence, and obtain the operation-authority decision before review
> resumes.