# Execution and recovery

For whoever coordinates work and those carrying it out. The promise: authorized work has a reason, a manageable boundary, and an honest next step when it cannot finish.

**Example assignment:** “Make request handoffs preserve ownership until acceptance. The request and status screens are in scope. Verify acceptance and refusal. Choose and test reversible implementation details yourself. Stay within today’s agreed budget and stop when this outcome is verified. Prepare any decision outside your authority; continue independent work while it waits.”

## Commitments

1. **Start from reality.** Inspect the current agreement, product, participants, existing work, and unresolved decisions. For a new project, help establish the intended outcome and decision owners. For an existing one, preserve useful work and identify assumptions needing agreement. Apply [Shared direction](shared-direction-contract.md)’s clarity check to the next bounded outcome before implementing or delegating it; a request to build does not settle missing product decisions. Investigate and prepare drafts within existing authority; an unresolved choice blocks only work that depends on it.

2. **Derive and bound the work.** Each assignment names the gap or authorized request, intended result, scope, owner, context, completion evidence, and relevant time, cost, or retry limits. Choose the next useful work by expected value, risk, dependencies, and available resources. Make that reasoning visible. Stop at the agreed outcome or limit unless continuing to another outcome is already authorized.

3. **Own the whole workflow.** Agents carry planning, implementation, integration, and follow-through within their authority. Connect a simple complete path early. Arrange parallel work so contributors do not overwrite one another’s work or disrupt shared test resources. Establish assignment ownership before execution so concurrent workers do not unknowingly take the same work. Keep dependencies and newly discovered work linked to the assignments they affect.

4. **Stop unproductive repetition.** Track progress against the agreed limits. A blocked assignment returns the cause, attempted remedies, useful partial work, and decision or next owner needed. Continue independent work. A healthy wait has a next checkpoint; it is not an excuse for endless polling.

5. **Recover from known facts.** After an interruption or uncertain action, inspect what actually happened before retrying. Preserve enough context for another worker to continue. Do not duplicate an action merely because its acknowledgement was lost. Before reassigning work, establish the previous worker’s state and prevent it from making conflicting changes under outdated authority. Retain needed work and release owned temporary resources when their purpose ends.

6. **Find and check the means to work.** Identify the capabilities needed to build, collaborate, verify, and deliver. Discover the available tools and systems, read their instructions, and confirm access and suitability. Select and use them within existing authority and the project’s agreed technology and design choices. An alternative must preserve those commitments or follow their change process. If a capability is missing, find an authorized alternative or prepare what is needed; leave the affected result unverified rather than shifting routine testing to the person. Never claim unattended operation or a future notification without a working mechanism.

7. **Keep work resumable.** Maintain a findable working record linking current agreements, owners and authority, active assignments, decisions waiting, selected tools, evidence, and the next action or checkpoint. Update it when these change. Use a durable tracker or equivalent record rather than relying on an agent to remember a growing task list. Give each shared fact an authoritative home and distinguish requested actions from observed outcomes. A new participant should not need the original conversation to continue. Identify the work and its execution session separately. For unattended work, verify before starting that it can continue when its launcher or observer disconnects, or that a supported recovery path preserves progress. Observing work must not change it; reconnect to the identified run rather than accidentally starting another.

## Operating cycle

1. **Orient:** find current direction, authority, people, work, and available capabilities.

2. **Choose:** compare reality with intent and select a useful, bounded outcome.

3. **Act:** execute and coordinate within the decision boundaries in [Ownership and collaboration](ownership-and-collaboration-contract.md).

4. **Verify:** check the combined result against [Verification and delivery](verification-and-delivery-contract.md); repair failures within the work’s limits.

5. **Learn and continue:** apply [Feedback and learning](feedback-and-learning-contract.md), update the working record, and choose again only within continuing authority.

Repeat the comparison after completed work, failed checks, relevant feedback, changed agreements, or changed conditions. Human absence does not stop authorized progress. When no useful authorized work remains, preserve the state and report what is needed; do not invent activity or wait without a supported checkpoint.

**Check:** Start with either an empty project or unfinished work. The workflow should establish direction, inspect its capabilities, choose a bounded outcome, execute, verify, and reassess. Interrupt it: a fresh participant should resume from the working record. Remove a tool or lose an action’s confirmation: it should investigate an alternative or observed state without fabricating success or duplicating effects.

**Left open:** Task trackers, worker count, session layout, and isolation tools. Choose them to meet these promises and any explicit project commitments; the methodology itself prescribes no particular agent architecture.
