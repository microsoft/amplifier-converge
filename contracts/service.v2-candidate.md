target: contracts/service.v1.md

# Service Contract — v2 candidate (DRAFT — PENDING)

## Exact change, sentence by sentence

### Change 1 — What it is, the existing frozen records

Current text:

```
Amplifier Converge runs as one instance on a machine. Inside it, the service holds the
records and serves one HTTP API. Two records are frozen in v1:
```

Replacement:

```
Amplifier Converge runs as one instance on a machine. Inside it, the service holds the
records and serves one HTTP API. The existing `run` and `check` shapes remain frozen;
the admission and first-authoring receipts below are durable Service records, while
their storage schema and wire remain unfrozen:
```

### Change 2 — add promises 7–8, Service-only initial authority

Current text:

```
6. **The store is one file the instance owns.** In the instance's data directory,
   scoped by project. Nothing of the service is written into a repository's working copy.

## Not in v1
```

Replacement:

```
6. **The store is one file the instance owns.** In the instance's data directory,
   scoped by project. Nothing of the service is written into a repository's working copy.

7. **Service admits creation before the first run.** For a declared project-creation
   request with unbound source, Service alone verifies a configured person-authentication
   source, a separately registered explicit creator authorization, and an allowlisted
   workspace root. It records the admitted durable creation in a versioned receipt that
   preserves the originating conversation and declared notes; an absent or invalid
   prerequisite is refused before effect. An unbound source record is not a project.
   The App/host only forwards: it neither stores nor inspects disk, nor mints identity,
   credential, admission, or receipt. Authentication, creator authority, and eventual
   project-steward assignment are separate; verified authentication does not by itself
   grant creator authority or assign a steward, nor do context, declaration, or `$USER`.
   Registered grants come from Service-controlled instance policy, never asserted request
   roles or self-registration by an ordinary caller. Service controls the local initializer, or
   gives it an explicit per-request authorization bound to that admitted creation and root;
   neither arbitrary commands nor remote clone or publish authority follows. Only after
   admission and an explicit launch request may Service issue the first project- and
   role-scoped run identity. Exact retry returns the settled receipt with 0 additional
   permanent empty projects; changed reuse and an unknown prior effect refuse, not replay.

8. **One grant admits the first draft.** Separately from creator authority, Service
   verifies an explicit initial-draft-create grant naming one recorded person, one selected
   registered project, and one admitted new unlocked text document per request. The grant
   works for a newly admitted project and for an already selected registered project.
   An absent grant, or an existing, locked, unsafe, foreign, occupied, or overwrite target,
   is refused before writing. Exact reuse returns its settled receipt without another
   document; changed reuse and an unknown prior effect refuse rather than replay. This
   grant is not apply or ratify authority, a worker capability, or manager-check authority.
   Service, run, and provider credentials never enter SDK context, browser-visible
   artifacts, logs, or argv. Protected person-authentication session material used only to
   establish the configured source is not a Service or run credential and is not forbidden.

## Not in v1
```

### Change 3 — Not in v1, implementation choices left open

Current text:

```
- **Wire details** (REST vs RPC, poll vs push) — until a third client needs them stable.
  A change reaches a reader within ten seconds either way.
```

Replacement:

```
- **Wire, person-authentication, and receipt details** (REST vs RPC, poll vs push;
  configured source and credential mechanism; grant, root, and receipt layout) — until
  interoperating clients need them stable. This amendment requires Service verification
  and explicit grants, but chooses no account model, authentication-provider platform,
  exact HTTP field spelling, database or registry, production migration, or storage layout.
  A change reaches a reader within ten seconds either way.
```

### Change 4 — How the kit checks it, post-ratification acceptance

Current text:

```
- The store is under the data directory; nothing service-owned appears in a working copy.
```

Replacement:

```
- The store is under the data directory; nothing service-owned appears in a working copy.
- After a steward word and implementation, a configured authenticated person with a
  separately registered creator authorization and an allowlisted root can receive one
  admitted creation receipt. An absent creator authorization is refused before effect;
  the preserved unbound conversation and declared notes remain attached to that receipt,
  and an exact retry adds 0 permanent empty projects.
- The initializer is confined to the admitted allowlisted root and refuses an occupied
  target, arbitrary command, remote clone, and publish attempts. The first run identity is
  issued only after that admission and an explicit launch request; Service/run/provider
  credentials are absent from SDK context, browser-visible artifacts, logs, and argv.
- A recorded person with a per-request initial-draft-create grant can create exactly one
  newly admitted unlocked text document in either a newly admitted or already selected
  registered project. Missing-grant, existing, locked, unsafe, foreign, and overwrite
  targets refuse before write; exact reuse has no second write; changed or unknown reuse
  is not replayed. The action neither applies nor ratifies a document and never authorizes
  a worker or a manager check.
```

## Evidence — a cost paid or a failure caught

This publication preserves the proposal's meaning and pending status. The evidence
below summarizes the observations that prompted the draft; it does not claim a
new end-to-end test or approval. Private coordination records are not required to
read this proposal and are not published with it. Supporting cross-repository
links require collaborator access to the private Converge repositories; the
relevant observations are summarized here so their meaning does not depend on
those links.

The previous family decision is real but does not decide this candidate. The
September 16 decision, `"ratified, let's go!"`, applied to the reviewed `r2`
packet with SHA-256
`8e2de16a8de4fe7f3b41893bc2d3e77d26bf24398fcff9b86a1580a96219c270`,
not this later proposal. The resulting shared promise is in
[Experience Interface v1](experience-interface.v1.md). No new initial authority
follows from that earlier ratification or from publishing this draft.

The ratified
[On-ramp experience contract](https://github.com/bkrabach/amplifier-converge-onramp/blob/f00663a3dca5dd7505d2116550f1553956ae1227/contracts/experience.v1.md)
assigns durable project-creation admission to Service. The producer investigation
that prompted this draft reported: “no inspected public call creates an app
project, workspace, or repository and binds the originating unbound conversation
today.” That is the observed missing producer, not a preference for a new platform.

At that investigation's Service checkpoint, working-copy registration associated
a directory with an already named project; starting a run also required an
existing project. Neither operation supplied the missing admitted transition from
an unbound conversation into a project, nor the separate authority to create its
first source document. The existing-source draft writer required a source path,
its exact digest, a same-directory candidate sibling and a candidate body; a
missing source was rejected before writing. Those observations explain why
reusing that writer as an implicit initial-creation grant would be incorrect.

Direction's existing promise separately distinguishes saving a draft, applying a
revision and recording ratification; see its
[experience contract](https://github.com/bkrabach/amplifier-converge-direction/blob/2cd4bb17084b9c8d94a6ada6add159470e8123f0/contracts/experience.v1.md).
The family [Service v1 contract](service.v1.md) remains authoritative and unchanged.
Its existing run/check authority cannot be broadened by a receipt or UI label.

Without an explicitly admitted initial transition, the full unbound journey would
have to invent a bootstrap credential, default project, ungranted write, or
App-owned disk effect. The review therefore parked that transition for a
Service-owned proposal and a steward decision. Existing-source candidate-save
proof does not close this different gap. Before any implementation of this draft,
its prospective checks must be rerun against the selected current Service API;
the historical observations above are not a current runtime acceptance claim.

### Suggested alternatives

1. **Recommended:** ratify the bounded Service-verified creator and first-authoring grants
   above. They give the ratified Service owner one explicit default-deny path without making
   a general permissions framework.
2. **Preprovisioning:** it can defer the unbound first-authoring journey, but it does not
   supply the missing per-request authority for a first document and is not a complete MVP
   path.
3. **App self-bootstrap:** not an approved alternative. It conflicts with the On-ramp rule
   that Service alone admits and records durable project creation, and with the App's
   no-record/no-disk/no-ambient-authority boundary.

## What does NOT change

- Promises 1–6 remain unchanged: one API and one instance remain the truth; the existing
  run identity rule remains; a worker still cannot write a `check`; and Service records stay
  in its one instance-owned store, never as Service bookkeeping in a working copy.
- App and every experience remain request forwarders without a Service bypass, fallback
  project, disk inspection, durable record, or credential-minting authority. A creator,
  login, and project steward remain distinct identities.
- The current existing-source candidate-save route and wire remain unchanged: `sourcePath`,
  `expectedSourceContentSha256`, `candidatePath`, `candidateBody`, and empty
  `expectedRevisions` stay its own behavior. This proposal does not authorize first-source
  creation through that route, or an implementation fixture before a steward word.
- No authentication provider, account platform, HTTP spelling, database, registry,
  production migration, storage layout, remote clone/publish feature, provider configuration
  policy, or source/body ceiling override is selected. The Service 30-source-file/8-table
  ceiling and second-domain split test remain unchanged.
- This is DRAFT/PENDING only. It does not apply or ratify any document, authorize a worker,
  manager check, or dependent implementation, change a locked file, or replace the prior
  ratification receipt.

## Steward's word

**Question:** Ratify the narrow Service-owned admission + first-authoring rule?

**Decision:** pending

**Permitted answers:** ratified · ratified with edits · declined · later

**Steward:**

**Date:**

**Edits or conditions (if any):**
