# Using Converge as a person

Lead your area and help the whole succeed. The [vision](../docs/VISION.md) and [contracts](../README.md#the-contracts) describe the shared method. This illustrative example follows three peers building a field-service platform: customers request repairs, crews do the work, and the business schedules and bills it. Each person directs substantial work with agents, across several components and repositories.

## Find the outcome you can pursue together

The peers want customers to get dependable repairs and the business to run the service well. Their initial ideas differ: one assumes customers can book instantly; another expects dispatchers to confirm every visit. Both could build a convincing system that disappoints the other.

Discuss who should benefit, what should improve, important constraints, and which uncertainties matter next. Ask agents to use available conversations, sketches, and existing work to draft the vision and proposed commitments. Have them expose conflicting interpretations and missing choices. A discussion or an agent's summary does not itself establish agreement.

The peers choose a first working path within the larger platform: a customer requests a repair, a dispatcher confirms a visit, a crew completes it, and the customer receives an accurate invoice. They choose a connected pilot to learn quickly and record the assumption that crews will have reliable connectivity. They will check that assumption during pilot visits before expanding to more crews. This gives them something useful to test without settling the entire platform design.

## Divide responsibility and agree on the connections

The peers organize the work around coherent outcomes:

| Area | What the owner leads |
| --- | --- |
| Customer and crew experience | Requesting service, preparing for a visit, carrying out work, and understanding progress. |
| Scheduling and service operations | Capacity, dispatch, visit progress, and handling work that cannot be completed. |
| Business integrations and access | Connections to customer records and billing, permissions, and reliable exchange of information. |

For this initiative, one peer coordinates the combined outcome and unresolved disagreements within agreed authority. Each owner can lead many pieces; these connections need not form a tidy hierarchy. [System design and decomposition](../contracts/system-design-and-decomposition-contract.md) explains how to choose and adjust those boundaries.

Agree what others can rely on: for this pilot, a visit is confirmed only after capacity is reserved and a dispatcher commits it. Specify important failures too, such as unavailable capacity. A technology choice, a shared interface, or exact client behavior can belong when the team depends on it. [The writing guide](../docs/writing-guide.md#detail-where-it-matters) shows how to keep that detail accessible.

Use concise text, a mock, or another clear form. Each peer should be able to explain the promise, challenge it, and recognize a violation. Name who can change it and who checks the combined experience. Give each promise one authoritative home. Keep local implementation choices with their owners.

## Keep leading your area with your agents

You set priorities, constraints, and investment; judge tradeoffs and the experience; and adjust direction as you learn. Delegate work suited to the agents' demonstrated capabilities, tools, and access. The [agent guide](agent-guide.md) covers planning, durable tracking, implementation, integration, verification, and recovery.

An assignment can be brief:

> Make the confirmed visit visible to the customer and crew using the agreed scheduling interface. Include cancellation and unavailable-capacity cases. Choose and test implementation details within our design commitments and budget. Return a checked result with any limitations; prepare choices outside your authority while independent work continues.

Reversible choices within that scope proceed without another approval. Consequential delegated choices receive proportionate care. Your availability does not change that authority. Meanwhile, you may decide the next investment should improve failed visits before adding more booking options, based on what the pilot reveals.

## Bring in the judgment that changes the work

The experience owner asks a colleague with field-service experience to examine a mock: “When a crew cannot finish a repair, can they tell what to do next?” They provide the intended outcome, relevant promises, and what remains uncertain.

The colleague points out that a polished progress display still leaves the crew stranded when a part is missing. The owner shifts attention toward explaining the next action and works with the operations owner on what information that needs. The contribution changes what they build. The owner remains responsible, and the colleague receives the resulting decision without joining every project meeting.

Prepare requests for judgment with evidence, options, a recommendation where useful, and the consequence of delay. Leave room to challenge the question. Updates should make changed outcomes and decisions easy to see, with supporting detail available. Protect time for deeper discussion when its value warrants it.

## Adapt together while independent work continues

A clearer layout within the agreed experience is a local choice. Changing when a visit counts as confirmed affects other owners' promises and needs their agreement. [Ownership and collaboration](../contracts/ownership-and-collaboration-contract.md) governs that distinction.

Now the pilot reveals unreliable connectivity in the field. The peers reconsider the connected-only bet. If they agree to support offline work, they negotiate its effects: the crew must see which updates are pending, operations must reconcile them, and reconnecting must not create duplicate visits or charges.

The accepted change reaches the affected owners and their agent workflows. They compare active assignments with the new direction, preserve useful work, revise or end superseded assignments within authority, and identify which checks must be repeated. Work that does not depend on the unsettled choice continues. If every change keeps involving everyone, revisit the boundaries themselves.

## Judge the whole and choose again

Agents exercise the actual journey, including failures and the connections between contributions, then repair and recheck within authority. People judge whether the result serves the need and whether the evidence deserves confidence. You may explore the product yourself; routine testing belongs in the delegated work.

A technically correct system can still leave crews with too much administration. That may call for a different experience or priority, not just another implementation task. Feed observations back naturally; the workflow should investigate, connect them to existing work, and return what changed.

Compare current reality with today's intent. Starting fresh, completing unfinished work, and changing direction all use that same approach. Keep agreements current, prune obsolete explanation, and split responsibilities when that helps understanding. Judge the method by useful combined results and the total human effort required, including repeated explanations, corrections, and rescue.
