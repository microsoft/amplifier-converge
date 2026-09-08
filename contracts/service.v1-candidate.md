target: contracts/service.v1.md

# Service Contract — v1 candidate (proposal)

## The exact change

### 1. Promise 3 — a qualifying manager check reports success

Current text:

```
3. **Merge is a request the service may refuse.** A run ends `done`, `stuck` (with a
   cause) or `waiting` (on a call). Asking to mark it `merged` succeeds only when a
   `check` exists whose `by` is the run's manager and whose `commit` is on the run's
   branch. Otherwise the answer is a refusal, in a sentence. What this does not prove:
   that the check was meaningful — that stays the manager's obligation under the method.
```

Replacement:

```
3. **Merge is a request the service may refuse.** A run ends `done`, `stuck` (with a
   cause) or `waiting` (on a call). Asking to mark it `merged` succeeds only when a
   `check` exists whose `by` is the run's manager, whose `commit` is on the run's branch,
   and whose `exit_code` is `0`. Otherwise the answer is a refusal, in a sentence. An
   `exit_code` of `0` reports that manager's command succeeded; it does not independently
   prove the check was meaningful, which stays the manager's obligation under the method.
```

### 2. How the kit checks it — merge refusal

Current text:

```
- `merged` requested with no qualifying `check` → refused, with a sentence.
```

Replacement:

```
- `merged` requested without a `check` whose `by` is the run's manager, whose `commit` is
  on the run's branch, and whose `exit_code` is `0` → refused, with a sentence.
```

### 3. Changelog — proposed 2026-09-08 future row

Current text:

```
| 2026-09-06 | v1 drafted from the family vision and a study of a comparable harness; council review; ratified as content. Reshaped 2026-09-07 into the family format on the steward's word ("port it"); no promise changed. | Steward's word, 2026-09-06. `docs/FORMAT.md`. |
```

Replacement:

```
| 2026-09-06 | v1 drafted from the family vision and a study of a comparable harness; council review; ratified as content. Reshaped 2026-09-07 into the family format on the steward's word ("port it"); no promise changed. | Steward's word, 2026-09-06. `docs/FORMAT.md`. |
| 2026-09-08 | Promise 3 and its merge-refusal kit require a manager check to report `exit_code` `0`, in addition to the existing manager, run, and branch obligations. | Original baseline: `amplifier-converge-service@916cab87edf31b1780197f76b2f5eff16c44c5a2:src/amplifier_converge_service/gate.py:15-28`; `amplifier-converge-service@916cab87edf31b1780197f76b2f5eff16c44c5a2:tests/test_gate.py:156-160`. |
```

## The evidence

The original ratified-main baseline is
`amplifier-converge-service@916cab87edf31b1780197f76b2f5eff16c44c5a2`.
At that baseline, the service implementation explicitly says it never considers the number
a check finished with in
`src/amplifier_converge_service/gate.py:15-28`. Its reproduction test constructs a manager
check with `exit_code=1` and asserts that `refuse_merge(run(), [failed]) is None` in
`tests/test_gate.py:156-160`. A failed command could therefore meet the original merge gate.
These before-change facts remain pinned to that baseline, not to a subsequently changed
preparatory test.

The proposed `exit_code` requirement is narrow: `0` reports the manager's command
succeeded. It is not independent proof that the command was a meaningful test, and the
service still makes no test-quality judgment.

## What does NOT change

- The service does not execute a command, judge test quality, or access Git.
- The existing requirement that the check belongs to the run's manager, concerns that run,
  and has its commit on the run's branch remains an eligibility obligation; it is not
  reduced to a permissive comparison of reported strings.
- No authentication, record schema, or wire fields are added: `exit_code` is already part
  of the frozen `check` record.
- A contingent implementation and tests are prepared on the service review branch for
  reviewers. They are not adopted law and do not amend this target.
- The original ratified `contracts/service.v1.md` on main remains unchanged. Dependent
  publishing stays gated until the family approves this proposal and the target change merges.
- This proposal itself makes no source-contract edit, merge, or ratification.

## Residual

Reported branch strings and commits still do not establish an exact-current-commit linkage
or ancestry. This amendment alone must not be presented as a complete evidence-integrity
fix; a further artifact-binding design remains necessary.

## The steward's decision

**Pending:** ____________________
