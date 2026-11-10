# System design and decomposition

For people and agents shaping the system, owning its parts, or relying on their connections. The promise: focused parts can be understood, reused, and developed independently while forming a working whole.

**Example:** One owner directs three repositories for request entry, status, and handoffs. Another owns billing. Both use a shared identity component. These owners coordinate on what crosses their boundaries—who may request access, who accepts responsibility, and what status is returned—without managing each other’s internal work.

## Commitments

1. **Favor focused parts and repositories.** Actively decompose broad systems into smaller, coherent responsibilities with clear interfaces: the connection points and behavior other parts rely on. Encourage focused repositories for those parts. This makes more of each part’s code, guidance, and relevant dependencies understandable together, supports reuse, and creates useful independent work.

2. **Carry direction at each useful level.** The overall vision explains the shared outcome. Each part states its contribution and promises, with links to the wider direction and dependencies it needs. Larger assemblies describe how their parts work together. Keep shared commitments in one authoritative place; do not copy the whole system’s guidance into every repository.

3. **Specify the connections.** Agree what each part provides, requires, and guarantees, including relevant failures and how compatibility is checked. Include selected protocols, relevant versions, and required capabilities where they define the connection. Others can build against those promises without depending on private implementation details. A proposed connection change identifies affected consumers and follows [Shared direction](shared-direction.md).

4. **Separate ownership from repository count.** One person or agent may own one part, many repositories, or a larger assembly with several levels beneath it. Record both responsibility and dependencies: some parts are shared across assemblies, so the relationships need not form a tree. Owners communicate with peers at the level where their responsibilities meet, going deeper when the decision requires it.

5. **Use decomposition to enable parallel work.** Assign independently actionable outcomes to capable agents, with the relevant direction and connection contracts. A coordinating agent may direct many contributors across many repositories. Apply [Execution and recovery](execution-and-recovery.md)’s work isolation and [Verification and delivery](verification-and-delivery.md)’s combined checks; repository separation alone does not prevent shared-resource conflicts or prove integration.

6. **Prune and reshape as the system learns.** Regularly remove obsolete explanation, duplicated guidance, and unnecessary implementation within existing authority. Split parts whose responsibilities have diverged; consolidate fragments when that restores a coherent purpose. Repeated context overload, conflicting owners, or changes that routinely spread across unrelated parts are signals to revisit the boundaries. Preserve still-needed promises and evidence; changing a commitment follows [Shared direction](shared-direction.md).

**Check:** Can a contributor understand one part, its purpose, and its connections without loading the entire system? Can two contributors change separate parts concurrently, then demonstrate that the combined outcome still works? Can a reusable part serve another consumer through its stated promises? Follow a shared dependency to every affected owner when its contract changes.

**Left open:** Repository count, number of ownership levels, module size, and programming techniques, except where a project deliberately commits to a choice under [Shared direction](shared-direction.md). Choose boundaries for comprehension, reuse, independent progress, and dependable composition.
