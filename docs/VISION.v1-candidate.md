target: docs/VISION.md
original-sha256: 0e4e2212c05a2dff0468614d212a6d02f5084f7f58894e74afca698f29f60960

# Candidate amendment — dynamic family wording

## Exact change, sentence by sentence

### Change 1 — Principle 1, lines 21–25: registered parts rather than a fixed named list

Current text:

```
### 1. One experience, many projects
Amplifier Converge is a family of small Converge projects — method, service, app,
agents, queue — each with its own repository, vision, contracts, ledger, queue and
manager session, held together by contracts at their seams. The top level holds the
seams and names the parts; it holds no part's internals.
```

Replacement:

```
### 1. One experience, many projects
Amplifier Converge is a family of registered Converge parts, each with its own
repository, vision, contracts, ledger, queue and manager session, held together by
contracts at their public seams. The family registry names the parts and their seams;
it holds no part's internals.
```

### Change 2 — success metric, line 85: current registered parts rather than “six today”

Current text:

```
- A steward opening the picker sees every part (six today) and their own projects, and
  reaches any one's direction and runs in **one click**.
```

Replacement:

```
- A steward opening the picker sees every current registered part and their own
  projects, and reaches any one's direction and runs in **one click**.
```

### Change 3 — success metric, lines 87–88: independent concurrent parts rather than five

Current text:

```
- Five manager sessions run five parts at once with **zero** shared files, queue items
  or calls between them — read by the family kit, not asserted.
```

Replacement:

```
- Independently managed parts run concurrently with **zero** shared mutable files,
  queue items or calls between them — read by the family kit, not asserted.
```

## Evidence — cost paid / failure caught

The current `family.toml` has 8 rows, while the fixed “six today” and “Five manager
sessions run five parts” wording describes the wrong family identity and ownership.
The requested split requires every experience to have its own repository, manager,
work tracker, lanes, and related custody: “break each experience out to it's own repo
w/ its own manager and work-tracker and lanes and all.” Five prospective local,
unregistered parts — Onramp, Possibly, Direction, Operation, and ExperienceSDK —
would produce 10 active delivery managers; the eventual family is 13 including
Family, Method, and Sessions. This proposal does not claim that 13 parts are
registered now and does not edit `family.toml`.

## What does NOT change

- The independent-projects registry requirements and all four steward gates remain.
- Queue custody, service authority, and the rule against publication without the
  required record remain.
- The MVP project → direction → workers / service-first flow and the rest of the
  vision remain unchanged.
- Each part retains its specific UX in its own separate DRAFT documentation; App has
  prepared three candidates. New models, UI themes, and A2 UI are outside this
  surgical candidate.
- This does not ratify anything, weaken isolation, edit the target, or modify the
  registry.

## Steward's word

Pending human answer:

