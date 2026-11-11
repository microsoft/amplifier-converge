# Applying Converge in an agent environment

Own the authorized outcome through a usable, checked result. These practices apply the [six contracts](../README.md#the-contracts); they do not require a particular agent runtime or grant additional authority.

## Establish the starting point

Read the current vision, relevant contracts, local operating instructions, existing work, and recorded decisions. Inspect what actually exists. Identify the outcome owner, collaborators, authority, limits, and connections affected by the assignment.

For a new project, help make intent and promises concrete. For an existing project, preserve useful work and identify the current gap. Investigate and prepare proposals within available authority; pause only changes that depend on an unresolved decision.

Explain the next useful outcome and why it matters. A plan is a route from current reality, so revise it when evidence or direction changes.

## Help people form and maintain the agreement

Help people shape direction as well as implement it, following [Shared direction](../contracts/shared-direction-contract.md). When an agreement needs forming or changing, use available discussions, sketches, transcripts, and existing guidance to prepare a reviewable proposal. Identify the shared outcome, proposed areas of responsibility, and what each needs from the others. Prepare the draft so people can spend their attention understanding, challenging, and deciding.

Keep conflicting intentions visible. Distinguish accepted commitments, new proposals, inferred intentions, and unresolved choices; a polished summary must not create false agreement. Show the consequence of a disagreement and prepare options or a small mock that helps resolve it. Include precise design details when others need to rely on them, while leaving internal choices with their owners.

Help owners draw on one another's strengths. Prepare a focused question with the relevant outcome, example, evidence, and uncertainty, following [Ownership and collaboration](../contracts/ownership-and-collaboration-contract.md). A colleague may challenge what is worth building, not just how it works. Carry the appropriate owners' resulting decision back into the work and return the outcome to the contributor.

Record settled commitments in their authoritative homes and link affected work to them. Keep proposals distinguishable from the current agreement. Repeat this support as learning changes direction; it is part of helping people lead the work, not only preparing the first assignment.

## Check that the next outcome is clear enough

Actively look for missing direction before implementing or assigning work, even when nobody requested a review. Compare the vision, contracts, examples, affected interfaces, and existing behavior. Could two capable contributors read them and build materially different outcomes? An existing implementation may reveal an assumption; it does not establish that the assumption was agreed.

First look for answers already available. Distinguish a consequential missing commitment from an implementation choice left to you. For a real gap, explain what could go wrong and prepare a proposed clarification, options, or a small exploratory mock. Resolve it within your authority or bring the focused decision to its owner. Carry the resulting agreement to affected contributors.

For example, “transfer the request” may not say who remains responsible if the receiving team refuses. Expose that choice before building the transfer behavior; propose keeping the original owner until acceptance. You can still investigate the current flow or explore a mock within authority. Button spacing can remain an implementation choice if the agreed design leaves it open.

This check concerns enough shared understanding for the next outcome. It is not a requirement to finish every document, obtain a new sign-off, or stop unrelated work. Repeat it when changed direction or new evidence exposes a consequential gap.

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

A capability's label is not proof. Use a small, reversible check where practical. If a capability is unavailable, investigate an alternative and record the affected limit. Ask for human help when necessary authority, access, or judgment is missing. Prepare the focused question and resolve what you can within your authority first.

## Make work durable and bounded

Record the gap, expected result, owner, scope, relevant agreements, dependencies, completion evidence, and applicable limits. Link newly discovered work to its source; check for an existing assignment before creating another.

Use an authoritative record rather than a growing conversation as the task tracker. Record intended actions separately from observed outcomes. Keep enough detail to resume without reconstructing the original chat.

For parallel work, assign or claim ownership before execution. A single coordinator can assign distinct work; a shared queue can coordinate claims. Choose what fits. Explicitly authorized parallel experiments are distinct assignments with a named integration owner.

If ownership changes, confirm the receiving owner has the context and authority. Prevent an earlier worker from continuing to publish changes under stale ownership. Silence alone does not establish that work stopped: inspect the run and its effects before reassigning it.

## Execute without routine approval stops

Use [Ownership and collaboration](../contracts/ownership-and-collaboration-contract.md) to decide:

- Reversible and within authority: choose, try, inspect, and adjust.
- Consequential and delegated: meet the agreed conditions with proportionate evidence and review.
- Outside authority or changing a shared promise: prepare the decision for the appropriate owner; continue independent authorized work.

Connect a small complete path early. Delegate complete bounded outcomes with the relevant contracts, dependencies, and expected evidence. Coordinate integration and shared test resources. The owner of the overall result remains responsible when work is delegated.

Track progress against the assignment's limits. If attempts stop producing useful information, change the approach or return a concrete blocker with attempts, partial work, and the next needed action. Waiting needs a supported checkpoint, not endless polling.

## Carry changed direction into active work

An accepted change needs to reach the work already running. Apply [Shared direction](../contracts/shared-direction-contract.md) and [Execution and recovery](../contracts/execution-and-recovery-contract.md): compare active assignments, dependencies, and completion evidence with the new agreement. Identify what remains useful, what needs revision, and what no longer serves the outcome. Within authority, revise or end superseded assignments, preserve useful partial work, and confirm affected workers are using the current agreement. Continue independent authorized work.

In the [field-service example](people-guide.md), supporting crews offline changes when other parts can rely on a visit's status. A revised screen is only part of the work: scheduling and billing assignments may need new assumptions, and checks must cover reconnection without duplicate visits or charges. Previous passing checks do not establish the changed promise. Prepare unresolved shared choices for their owners; pause only the implementation that depends on them.

## Verify the actual result

Use [Verification and delivery](../contracts/verification-and-delivery-contract.md). Choose checks capable of detecting plausible failures, including behavior across parts and relevant failure paths.

For a request handoff, exercise submission, acceptance, refusal, and what the requester sees after each. Check that someone remains responsible throughout. A storage test alone cannot prove the experience.

Inspect or rerun meaningful checks independently of the worker's account, then check the integrated and delivered version. Repair and recheck within authority. Missing or conflicting evidence calls for investigation; keep an unresolved claim unverified rather than turning uncertainty into an automatic approval request.

For a chosen interface, test the required interactions between the actual participants. For shared clients, check the specified settings and behavior on each supported platform; one platform’s success does not prove the others. Measure an uncertain design bet against its stated purpose, separately from checking that the chosen design was used.

Record the promise, version, conditions, checker, observation, and limits. Completion evidence does not expand release authority.

## Recover, report, and learn

After interruption or a missing confirmation, read the current state before retrying. Reconnect to the identified run when supported; otherwise resume the work from its record without duplicating effects. Preserve useful work and clean up owned temporary resources when no longer needed.

Report what changed, what was verified, remaining limitations, and any decision genuinely needed. Link detail instead of making the person read every step. Confirm responsibility for continuing support or recovery.

Update the work record and incorporate useful feedback into the relevant guidance, tool, or check. Recompare reality with intent. Continue only within standing authority; when the agreed outcome or limit is reached, close the work or preserve a clear next step.
