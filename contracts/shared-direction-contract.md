# Shared direction

For everyone writing, agreeing to, or relying on project guidance. The promise: people and agents can identify the same current agreement and tell when it has changed.

**Example:** “Anyone asking for help can see who owns the request” is a vision. “Support remains responsible until Billing accepts” is a contract. A mock labelled “idea to explore” is neither an approved design nor permission to change production.

## Commitments

1. **Name the boundary.** Each contract identifies who relies on it, the behavior, responsibility, or design choice it covers, and important choices left open. Specify exact interfaces, settings, defaults, or experience details when they are part of the promise. For a shared client experience, distinguish what stays consistent across platforms from what may adapt. A reader can tell what it promises without assuming everything nearby is a requirement.

2. **Make each promise checkable.** Say what would show it being kept or broken. Name necessary human judgment or missing checks. Progress and test results are recorded separately from the intended outcome; implementation does not quietly redefine the promise.

3. **Keep one current agreement.** Record the accepted wording or artifact version, who agreed, and the scope of that agreement. Give each promise one home; related contributions reference it. A draft, saved edit, or discussion is not automatically acceptance.

4. **Change direction explicitly.** Show what changes, why, the supporting evidence or judgment, and who is affected. The authorized owners settle consequential changes before dependent implementation follows them. Confirm affected work receives the new agreement. Implementation choices that preserve the agreement use the standing authority in [Ownership and collaboration](ownership-and-collaboration-contract.md).

5. **Make review accessible.** Use everyday words and the clearest form: text, pictures, charts, or working mocks. Keep essential meaning inspectable by people and agents. Make the current wording, proposed changes, and relevant decision history easy to compare without requiring developer tools. An approved mock establishes only the design and behavior identified as agreed, not its temporary implementation.

6. **Make deliberate choices explicit.** A contract can commit to a technology, architecture, or experience design. State the choice, its scope, why it matters, and the important tradeoffs. For a bet with uncertain benefits, identify the assumptions, how they will be checked, and what would prompt reconsideration. Name who has authority to change the commitment. Distinguish agreed choices from experiments; routine decisions within delegated authority need not become contracts.

**Check:** Give a new participant the guidance. Can they find the accepted version, explain a promise, and describe a violation? Change a shared promise: affected work should receive that change, while a later draft must not silently replace the agreement. Can a contributor distinguish a required design choice from an example, explain its purpose, and identify what remains flexible?

**Left open:** File names, approval tools, storage, and visual format. The agreement and its history must remain findable.
