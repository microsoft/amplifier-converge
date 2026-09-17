target: contracts/family.v1.md
original-sha256: 577682cbdf41cce14d63cc5b98488118caa0f1fac6a85fc77a1baac5963db01b

# Family Contract — v1 candidate

## Exact change, sentence by sentence

### Change 1 — What it is

Current text:

```
Six repositories, one registry. A part is in the family when it has a row:
```

Replacement:

```
One registry. A part is in the family when it has a row:
```

### Change 2 — Promise 1, the top level

Current text:

```
1. **The top level holds seams, never internals.** This repository carries the family
   vision, the seam contracts, `family.toml` (eight parts: method, service, app, agents,
   queue, reader, sessions, this), the seam ledger, and the one installable — a package that composes the
   parts and adds no code of its own. A seventh part arrives by a split-out or a proposal.
```

Replacement:

```
1. **The top level holds seams, never internals.** This repository carries the family
   vision, the seam contracts, `family.toml`, the seam ledger, and the one installable —
   a package that composes registered parts and adds no code of its own. The registry
   defines the parts; additions arrive through promise 8 or a proposal.
```

## Evidence — a cost paid or a failure caught

The registry currently has eight actual rows while this contract says both “Six repositories” and “eight
parts,” then calls a future arrival “a seventh part.” The conflicting enumeration makes the family boundary
unreliable at the moment it must guide composition: there are ten active delivery managers (five existing
and five new), while the intended family is thirteen eventual repositories (eight existing plus five new,
including Family, Method and Sessions), not thirteen registered parts now.

The human has now directed that each experience be split into its own repository with its own manager,
work-tracker, and lanes. The eight-row registry and the contract's incompatible
counts are directly inspectable in `family.toml` and the current text above.
Replacing the counts with that registry's authority prevents the next split from
silently reviving stale membership claims. It does not itself register new parts.

## What does NOT change

- Promise 2 still requires every part to be an independent project with its own repository, queue, and
  manager.
- Promise 3 still requires a reachable URL with `docs/VISION.md` and `contracts/`; local-only new
  repositories remain unregistered.
- Promise 6 still isolates manager-session state by session id.
- Promise 8 still supplies the numeric ceiling and second-domain split rule.
- Source ownership, queue custody, service admission, and existing gates remain unchanged.

## Steward's word

Answer: 

