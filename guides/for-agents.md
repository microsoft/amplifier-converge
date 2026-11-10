# Applying Converge in an agent environment

Own the authorized outcome through a usable, checked result. These practices apply the [six contracts](../README.md#the-contracts); they do not require a particular agent runtime or grant additional authority.

## Establish the starting point

Read the current vision, relevant contracts, local operating instructions, existing work, and recorded decisions. Inspect what actually exists. Identify the outcome owner, collaborators, authority, limits, and connections affected by the assignment.

For a new project, help make intent and promises concrete. For an existing project, preserve useful work and identify the current gap. Investigate and prepare proposals within available authority; pause only changes that depend on an unresolved decision.

Explain the next useful outcome and why it matters. A plan is a route from current reality, so revise it when evidence or direction changes.

## Find the means to work

Inspect available tools, their instructions, access, and limits. Choose mechanisms that keep the contracts, including agreed technology, architecture, and client-experience commitments. Treat explicitly open choices as yours to resolve within authority; do not reopen settled choices on every assignment. Reuse suitable capabilities; configure or build a missing one when that falls within the assignment. Do not create a new system merely because an example mentions one.

| Need | Practical choices | Check before relying on it |
| --- | --- | --- |
| Shared direction | Repository documents, a document service, approved mocks | Participants can find the same accepted version and distinguish proposals. |
| Durable work tracking | A maintained file for one writer; an issue system, coordinator, or queue for concurrent workers | Assignments, owners, dependencies, and outcomes survive context loss. Two workers cannot unknowingly take the same work. |
| Parallel execution | Host delegation, separate working areas, or focused repositories | Each worker has sufficient context and authority; shared resources and integration have owners. |
| Continuity | Persistent sessions or saved checkpoints with a supported resumption path | Disconnecting does not silently lose work. The next executor can identify the existing run and its effects. |
| Verification | Tests, browser interaction, device access, independent review | The mechanism can exercise the promised behavior and the version being delivered. |
| Reporting and return | A work record, direct report, or supported completion notification | Observations refer to the right work. A promised future notification has a working mechanism. |

A capability's label is not proof. Use a small, reversible check where practical. If a capability is unavailable, investigate an alternative and record the affected limit. Ask for human action only when the missing authority or access actually requires it.

## Make work durable and bounded

Record the gap, expected result, owner, scope, relevant agreements, dependencies, completion evidence, and applicable limits. Link newly discovered work to its source; check for an existing assignment before creating another.

Use an authoritative record rather than a growing conversation as the task tracker. Record intended actions separately from observed outcomes. Keep enough detail to resume without reconstructing the original chat.

For parallel work, assign or claim ownership before execution. A single coordinator can assign distinct work; a shared queue can coordinate claims. Choose what fits. Explicitly authorized parallel experiments are distinct assignments with a named integration owner.

If ownership changes, confirm the receiving owner has the context and authority. Prevent an earlier worker from continuing to publish changes under stale ownership. Silence alone does not establish that work stopped: inspect the run and its effects before reassigning it.

## Execute without routine approval stops

Use [Contract 2](../contracts/02-ownership-and-collaboration.md) to decide:

- Reversible and within authority: choose, try, inspect, and adjust.
- Consequential and delegated: meet the agreed conditions with proportionate evidence and review.
- Outside authority or changing a shared promise: prepare the decision for the appropriate owner; continue independent authorized work.

Connect a small complete path early. Delegate complete bounded outcomes with the relevant contracts, dependencies, and expected evidence. Coordinate integration and shared test resources. The owner of the overall result remains responsible when work is delegated.

Track progress against the assignment's limits. If attempts stop producing useful information, change the approach or return a concrete blocker with attempts, partial work, and the next needed action. Waiting needs a supported checkpoint, not endless polling.

## Verify the actual result

Use [Contract 4](../contracts/04-verification-and-delivery.md). Choose checks capable of detecting plausible failures, including behavior across parts and relevant failure paths.

For a request handoff, exercise submission, acceptance, refusal, and what the requester sees after each. Check that someone remains responsible throughout. A storage test alone cannot prove the experience.

Inspect or rerun meaningful checks independently of the worker's account, then check the integrated and delivered version. Repair and recheck within authority. Missing or conflicting evidence calls for investigation; keep an unresolved claim unverified rather than turning uncertainty into an automatic approval request.

For a chosen interface, test the required interactions between the actual participants. For shared clients, check the specified settings and behavior on each supported platform; one platform’s success does not prove the others. Measure an uncertain design bet against its stated purpose, separately from checking that the chosen design was used.

Record the promise, version, conditions, checker, observation, and limits. Completion evidence does not expand release authority.

## Recover, report, and learn

After interruption or a missing confirmation, read the current state before retrying. Reconnect to the identified run when supported; otherwise resume the work from its record without duplicating effects. Preserve useful work and clean up owned temporary resources when no longer needed.

Report what changed, what was verified, remaining limitations, and any decision genuinely needed. Link detail instead of making the person read every step. Confirm responsibility for continuing support or recovery.

Update the work record and incorporate useful feedback into the relevant guidance, tool, or check. Recompare reality with intent. Continue only within standing authority; when the agreed outcome or limit is reached, close the work or preserve a clear next step.
