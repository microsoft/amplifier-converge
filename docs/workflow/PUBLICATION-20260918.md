# September 18 development checkpoint

This is a pullable development checkpoint, not a release or a claim that the
complete Converge conversation is working. No default-branch merge or deployment
is part of this publication. Next-step planning is deferred until the steward
returns.

## Product evidence

The verified desktop-reading slice increases Direction's document width by264px
across the three presets, preserves phone widths and draft text through preset/
viewport changes, and passes inspector keyboard and save/retry/reload checks.
The source document remains unchanged by those candidate-save checks.

The later shell-seams work has **not** completed a contextual conversation in App:
the standalone configured runtime returned a real reply, but its initial adapter
does not deliver quiet context or enforce the intended restricted tool boundary.
The SDK canonical-binding correction and Service turn/result association require
their own acceptance. Unit and producer results are not evidence of that complete
interaction. No unfinished conversation path was enabled in the verified candidate.

## Vision and contract disposition

- Family vision, family composition and Experience Interface updates already
  carry the recorded September 16 ratification. Their committed status is
  preserved; publication does not ratify anything else.
- [Service v2 candidate](../../contracts/service.v2-candidate.md) remains
  **DRAFT / PENDING**. Its evidence is now readable without private workspace
  links; its proposed promises and steward decision remain unchanged.
- No new method-contract changes are part of this checkpoint.
- The independent Direction, On-ramp and Possibly owners retain their branches,
  decisions and usable pins. This publication does not integrate their work by
  implication.

## How to use the checkpoints

Each product repository's checkpoint branch or draft PR states its exact commit,
checks and limitations. WIP branches preserve unfinished work separately and must
not be treated as compatible released packages. Existing consumer pins are not
automatically advanced to those WIP branches.

The product refs below were independently read back from GitHub on September 18
at10:19PDT. All branch names are deliberate: an ordinary pull of `main` does not
select these development checkpoints. The family documents are published with
this brief on `checkpoint/20260918-shell-seams`.

| Repository | Pullable branch | Commit | Readiness |
|---|---|---|---|
| [App](https://github.com/bkrabach/amplifier-converge-app/pull/4) | `night/20260918-document-first` | `08e7a5d` | Verified reading pilot plus person-message attribution preparation; not working agent conversation |
| [SDK](https://github.com/bkrabach/amplifier-converge-experience-sdk/pull/2) | `checkpoint/20260918-shell-seams` | `22016d5` | Accepted presentation checkpoint; does not include the unaccepted shell correction |
| [Agents](https://github.com/bkrabach/amplifier-converge-agents/pull/2) | `checkpoint/20260918-shell-seams` | `1cda345` | Development checkpoint with explicit context/tool-restriction limitations |
| [Service](https://github.com/bkrabach/amplifier-converge-service/tree/checkpoint/20260918-shell-seams) | `checkpoint/20260918-shell-seams` | `0e8aa92` | Checked existing Service base; unfinished turn association is separate |
| [Operation](https://github.com/bkrabach/amplifier-converge-operation/pull/2) | `night/20260918-document-first` | `b06d1c5` | Checked public-consumer/projection preparation |
| [Reader](https://github.com/bkrabach/amplifier-converge-reader/tree/hackathon/2026-09-17) | `hackathon/2026-09-17` | `44ba6f6` | Existing published observed-source boundary; unchanged in this pass |
| [Queue](https://github.com/bkrabach/amplifier-converge-queue/pull/2) | `checkpoint/20260918-shell-seams` | `9b630fe` | Checked scoped public-facade example and refusals |

**Unfinished work preserved separately — do not use as accepted dependencies:**

| Repository | WIP branch | Commit | Limitation |
|---|---|---|---|
| SDK | [`wip/20260918-canonical-shell`](https://github.com/bkrabach/amplifier-converge-experience-sdk/pull/3) | `6a12bca` | Canonical binding correction is not manager-accepted or packaged for consumers |
| Service | [`wip/20260918-slice-a-receipt-association`](https://github.com/bkrabach/amplifier-converge-service/tree/wip/20260918-slice-a-receipt-association) | `7ad6b40` | Earlier unaccepted association attempt; includes rejected SDK assumptions |
| Service | [`wip/20260918-slice-a-turn-snapshot`](https://github.com/bkrabach/amplifier-converge-service/tree/wip/20260918-slice-a-turn-snapshot) | `ce1728c` | Former uncommitted snapshot work is now preserved; changed-source tests and integration remain unrun |
| Service | [`wip/20260918-publication-qualification`](https://github.com/bkrabach/amplifier-converge-service/tree/wip/20260918-publication-qualification) | `b83416b` | Documentation of the checkpoint limits; no API change |

To inspect one checkpoint without merging it into current work:

```sh
git fetch origin <branch-from-table>
git show --stat FETCH_HEAD
# In a clean checkout, select the exact commit from the table:
git switch --detach <commit-from-table>
```

Existing PRs remain draft; no PR was merged. GitGuardian policy checks are not
test-CI or end-to-end runtime acceptance. The App consumer suite still has the
two documented failures that reproduce on its original baseline.

### Independent-owner and unchanged repositories

Direction, On-ramp and Possibly publication remains with their owners. In
particular, the pre-handoff Direction pilot source `d4771d4` is still local at
this checkpoint; its exact built package is included in the App's immutable vendor
pin, but that is not publication of the Direction source branch. The coordinator
did not overwrite those repositories or silently equate their existing published
pins with the newer local pilot.

The Method repository is already published at `d99c2a5` and has no unpublished
changes in this workspace. Reference and tooling repositories are outside this
product publication; their working trees and refs were not pushed.

Private coordination journals, runtime captures, credentials, test-instance data
and abandoned intermediate branches are not part of the product checkpoint.

## Review disposition

The independent session review reinforced early App-level acceptance, a single
integration owner, bounded context transfer and event-driven state updates. Those
are useful operating corrections, not a reason to restart feature work during
publication. Its activity/token counts are a limited snapshot, not a validated
bill or a precise avoidable-cost measurement.