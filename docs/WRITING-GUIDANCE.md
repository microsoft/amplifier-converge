# Guidance for keeping it reviewable

Aim for a narrative one-page vision and focused contracts of one or two pages each. These are review aids, not quotas. Use as many contracts as meaningful responsibilities require.

Split when responsibilities, audiences, or decisions need separate attention. Focused repositories can give those parts a clearer home and allow more independent work; ownership may span many of them. Keep one promise understandable in one place and link supporting detail without hiding obligations. Prune and reshape as described in [Contract 6](../contracts/06-system-design-and-decomposition.md). Use familiar examples where they save explanation.

## Detail where it matters

The right altitude is the level at which people need to agree. A contract may name a protocol, an architecture, an exact setting, or a visual design when others rely on that choice. Keep the commitment and its reason easy to inspect; link deeper explanation. [Contract 1](../contracts/01-shared-direction.md) governs deliberate choices and bets.

These examples illustrate possible project commitments, not requirements of the methodology:

| Kind of commitment | Example and what to make explicit |
| --- | --- |
| Technology or architecture bet | Choose Agent Client Protocol (ACP) at the agent–experience boundary, aiming to let different agents connect through one agreed interface. Name the selected version, required interactions, and compatibility checks. Record assumptions and tradeoffs; reconsider if essential interactions require incompatible extensions. The choice alone does not prove interoperability. |
| Shared client experience | Appearance offers “Follow device,” “Light,” and “Dark” on each supported operating system; “Follow device” is the default, and the selection survives restart. State whether labels and placement must also match. Native controls and layout may differ where the contract leaves them open. |

An approved mock can specify appearance and interaction alongside written behavior. Identify which details are commitments and which are illustrative. Split a large experience contract by coherent areas, such as navigation or settings, while keeping shared behavior in one home.

Apply that test here: can you explain the method, challenge a promise, and recognize a broken one? If review invites rubber-stamping, revise it.
