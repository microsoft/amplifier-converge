# Ownership and collaboration

For outcome owners, contributors, and the people whose expertise they need. The promise: independent work fits together without requiring everyone to supervise everything.

**Example:** One owner handles requesting help; another handles team handoffs. They agree what “accepted” means and name who checks the combined experience. A designer can improve that interaction without taking over either contribution.

## Commitments

1. **Give each outcome an owner.** Name the expected result, decision authority, limits, and dependencies. One owner may carry many parts or repositories; [System design and decomposition](system-design-and-decomposition-contract.md) describes how those responsibilities compose. Set standing authority for ongoing work, decisions reserved for people or other owners, and what happens when the outcome is met. This authority applies whether people are available or away. Name who coordinates the combined result and resolves disagreements. Delegating work does not make responsibility disappear.

2. **Respect shared promises.** Coordinate through the connection contracts described in [System design and decomposition](system-design-and-decomposition-contract.md). A change to a shared promise—including a chosen interface or agreed client behavior—or to commitments another owner relies on needs the appropriate owner’s agreement. Work within already agreed promises, limits, and authority does not require fresh agreement; coordinate affected integration and verification. Internal decisions stay with the responsible owner; do not silently bypass their responsibility or make consumers depend on an unagreed change.

3. **Complete the handoff.** The receiving owner accepts the scope and context before responsibility moves. Until then, the sender remains accountable for arranging the next step. A sent message or exported work packet alone does not establish acceptance.

4. **Make expertise usable.** Provide the outcome, relevant agreement or example, evidence, uncertainty, and reason for seeking this person’s judgment. Leave room to challenge the question. Return the resulting decision to the work and to the person who raised it.

5. **Manage attention deliberately.** Use existing authority without repeatedly asking for it. Agree what can wait and what warrants interruption. When a decision needs someone else, bring the unresolved choice, evidence, options, recommendation, and consequence of delay. Group related questions; continue unaffected work. Updates lead with what changed since the recipient last reviewed, progress toward the outcome, blockers, and decisions needed. Distinguish work activity from verified progress; keep supporting detail within reach. Adjust commitments when review demand exceeds capacity.

6. **Match care to consequence.** Consider how easily a choice can be undone, its cost, who it affects, and confidence in the evidence. For a bounded reversible choice, act, observe, and keep or revise the result. As consequences grow, use stronger investigation, review, staged trials, and recovery plans. Greater consequence calls for greater care; it does not automatically require a new human approval when the authority and conditions are already clear.

## Independent decisions by default

| Situation | What the responsible owner does |
| --- | --- |
| A reversible choice within agreed scope and limits | Make a reasonable choice, test it, and adjust without waiting. |
| A consequential choice already delegated | Check the agreed conditions, get proportionate evidence or review, and proceed when they are met. |
| A choice reserved for someone else or outside delegated authority | Prepare the decision and pause only the work that depends on it. Continue useful authorized work; silence does not expand permission. |

**Example:** Agents can try two request-screen layouts, test them, fix failures, and keep the better result within the agreed design scope without seeking fresh approval—even when a person is available. A change to who may access customer information needs the appropriate authority. Agents can investigate that choice and prepare options while other work continues.

**Check:** Give an owner a reversible design choice, a delegated consequential choice, and an out-of-scope decision. Try the same cases with a person available and unavailable: the authority to act should be the same. The first should proceed through a test; the second should follow its agreed conditions; only the third should wait for new authority. Track a dependency change and handoff: responsibility must remain clear throughout.

**Left open:** Meetings, messaging channels, team structure, and agent system. Agent-to-agent coordination follows the same boundaries within delegated authority.
