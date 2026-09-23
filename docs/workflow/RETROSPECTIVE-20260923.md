# Converge workflow retrospective — September 23, 2026

A sanitized record of one narrow live customer trial, observed through 15:29:30
Pacific. This is a checkpoint, not product acceptance or a broad reliability
claim. The [ownership map](UNIFIED-CHECKPOINT-20260923.md) identifies where lessons
belong; the [next acceptance plan](ACCEPTANCE-PLAN-20260923.md) makes them testable.

## Trial and result

The customer used ordinary language in a fresh Unified conversation and workspace:
make a small club greeting page with editable greeting and background color, then
save several greetings so they survive closing and returning later. They also
asked to hear back and have the working app opened. After trying the initial
concept, they approved its direction without naming workflow tools or supplying
product code. The evaluator did not start a server or repair the product directly.

Native implementation and manager verification happened. The automatic status
report was inaccurate, and customer delivery was not established by the cutoff.

| Acceptance boundary | Evidence at the cutoff |
| --- | --- |
| Initial customer interaction | Greeting/color controls worked in a foreground HTML concept. This was not native worker delivery. |
| Native action recovery | Manager read the action descriptions but initially filed malformed arguments. The runtime refused without effects, named the missing/misplaced fields, and the manager corrected its call ten seconds later without coaching. |
| Real tracked worker | A work item, wave and isolated implementation lane were admitted. The native worker made 34 tool calls and produced the app and persistence-check files. |
| Model policy | Foreground and native configuration confirmed Terra/xhigh. Configuration and materialization are not a capture of every provider request. |
| Recovery with history intact | Worker returned stuck because Git author identity prevented committing. The manager used supported checkpoint recovery; the original stuck return and attempt 1 of 3 remained intact. |
| Manager verification/integration | The original checks qualified before and after integration. The retained browser check saved two presets, reloaded, closed/reopened and checked restored content and colors. Temporary check servers were not delivery services. |
| Watch admission and execution | Required task bookkeeping preceded arming. Actual scheduled observations ran while the foreground was idle; the task revision remained valid. |
| Watch expiry | The final expiry occurrence completed and the watch paused. No later-period duplicate-notice claim was made. |
| Accurate handback | **Failed.** Two unsolicited notices claimed no work or persistence proof despite qualified manager evidence. |
| Manager completion and delivered app | **Unproven at cutoff.** The native manager was still running; there was no selected review/publication result or customer opening to test. Watch expiry was not manager termination. |

## Later progress, outside the scored window

A subsequent read-only review of retained native events found these later actions
on the same date. They do not revise the cutoff scores above.

| Time (UTC) | Retained observation |
| --- | --- |
| 22:43:31 | A delegated checker reported two-preset close/reopen/restore checks on the retained opening. This is a delegated check report, not a customer observation. |
| 22:44:23 | The manager successfully closed the work item. |
| 22:46:52 | Publication succeeded and selected the current review result. |
| 22:47:03 | The manager successfully finished the wave. |
| 22:47:21 | An HTTP check returned 200 and the system-browser open command succeeded. |

The manager reached publication after six refused publication attempts: the
action discovery helper did not supply that action's schema. This is a remaining
native discoverability gap despite the earlier work-item recovery. A follow-up
source repair was being prepared when this record was written; it is not counted
as merged, installed or live-proven here.

The expired watch did not deliver these later results. A successful system-browser
open command is not customer-visible browser acceptance or a demonstrated
automatic scheduled handback. Eventual item/wave completion is real progress, but
does not erase the false status or establish that the overall experience is ready.

## Why the handback was wrong

The supervisor read a retained run admission snapshot explicitly labeled
`continuation.capture: before_run_claim`. It treated that snapshot's zero lanes
as current work state. At 15:23 it reported no build or persistence checks; at
15:29 its expiry notice again claimed no recorded reopen proof. The missing final
publication was real, but the missing-work claim was false. The problem was
interpretation of historical evidence, not lost worker output.

Current owner observations, historical continuation context and terminal reports
need distinct contracts and consumers. A report must retain its observation time
and distinguish pending work, failed work, expired observation and unknown state.
The optional host integration owns truthful presentation; portable guidance and
native public contracts must make the same distinction useful without a canvas.

Pending scheduled inputs also appeared as lengthy machine-oriented user messages
and invoked model turns. Model-side reports inserted changing transport receipt
identifiers into comparison values, making semantically unchanged state appear
changed. Functional scheduling did not prove quiet or inexpensive observation.

## Delivery evidence and limits

The installed shell capability already supported detached background processes.
The manager encountered an occupied port, then started a server on a different
allocated port. Its retained observations showed the expected app returning
HTTP 200 across separate calls about five minutes apart. This established observed
process survival, not indefinite availability or customer browser acceptance.
No missing generic hosting capability was established.

The broader Compositor goal remains a genuine Publisher replacement, including
editable native Publisher documents and save-back. This greeting-app trial is a
workflow diagnostic, not a narrowing of that goal or evidence that those product
capabilities work. It also does not prove the full On-ramp → Direction → Possibly
→ Operations negotiation loop, voice parity, or a four-capability journey.

## Merged changes associated with this trial

These source results and installed receiving checks are distinct from the live
behavior above. Links and merge revisions were checked when this record was
prepared. Later package releases must not be backdated into the trial.

| Change | Published revision and validation | Live boundary |
| --- | --- | --- |
| [Agents #30](https://github.com/microsoft/amplifier-converge-agents/pull/30): exact discoverable workflow inputs, stable request identities and side-effect-free rejection | Runtime 0.2.27; merge `66325abc957c044e3f5b6b458d9caa904e8d7668`; 126 source tests plus 5 subtests, 12 installed checks | Used by the native manager; one malformed call recovered successfully. |
| [Operation #30](https://github.com/microsoft/amplifier-converge-operation/pull/30): receive the repaired runtime | Operations 0.2.29; merge `2a5b2a16f7bcd5445fe6fc5f3afb68738b0b5fa2`; 22 receiving checks | Used in this trial; UI unchanged. |
| [Optional bundle #30](https://github.com/microsoft/amplifier-bundle-unified-converge/pull/30): complete bookkeeping before arming | Behavior 0.2.16/module 0.1.11; merge `cdce01626a8f1209276683f18df282cbac6c3507`; 152 source and 19 installed checks | Used; watch survived foreground idle and retained its task binding. |
| [Optional bundle #31](https://github.com/microsoft/amplifier-bundle-unified-converge/pull/31): keep occurrence reports hook-owned and comparison values semantic | Behavior 0.2.17/module 0.1.12; merge `e1295e08139c4bbf88638d5d1b1e08f3a0a50286`; 155 source and 22 installed-wheel checks | Merged during the trial, **not installed in it**. Live effectiveness remains unproven. Does not remove scheduled text or provider turns. |

Portable instructions remained 0.4.24 in this pass. No Unified core change was
made. The [generic background-observation proposal](UNIFIED-CHECKPOINT-20260923.md#unapproved-host-proposal)
is unapproved design work, not a shipped interface.

## Lessons to carry forward

1. Make public action inputs discoverable and validate them before effects.
   Good errors enabled real self-correction, but the first malformed call means
   discovery alone has not eliminated mistakes.
2. Preserve imperfect returns and qualify exact retained work through the owning
   recovery API. A checkpoint, fresh manager checks and unchanged attempt history
   are stronger than hiding a failure or silently starting a replacement item.
3. Treat current observation, historical context, selected result and delivery as
   different evidence. Never infer a current empty queue from a pre-run snapshot.
4. Finish the customer loop: checked code must become a selected result, a
   qualified opening and an accurate requested return. Tests, HTTP success and an
   accepted open command are separate proofs.
5. Keep architecture boundaries intact while fixing the experience. Portable
   discipline belongs in the portable bundle/runtime; host bindings belong in
   the optional extension. A proposed generic host enhancement needs its own
   approval and receiving acceptance.

This summary intentionally omits local paths, runtime dumps, session identifiers,
credentials and full transcripts. The table preserves the results and boundaries
needed to reproduce the narrow case without publishing private execution data.
