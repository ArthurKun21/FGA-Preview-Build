---
title: Brave Chains
description: Learn how FGA Preview forms and avoids brave chains during battle, and how the brave-chain setting works with chain priority.
tags:
    - battle
    - cards
    - brave-chain
    - damage
---

# Brave Chains

A brave chain is a set of three cards that all belong to one servant. The brave-chain setting tells FGA how much it cares about brave chains on a turn.

## Overview

When the three clicked cards all come from one field slot, FGO adds an extra attack at the end of the chain. FGA can try to form a brave chain, or try to avoid one.

The setting belongs to each wave and turn. It works together with the chain priority list. See [Chain Priority](chain-priority.md).

## Key Features

- **Form or avoid**: four settings control the brave-chain behavior.
- **NP chains**: put an NP and the face cards of that servant together.
- **Avoid**: spread the cards across the servants.
- **Rearrange**: move the cards after FGA selects them.
- **A test in the app**: the simulation shows the brave chain and the rearrange step.

## Brave Chain Settings

| Setting | Behavior |
| ------- | -------- |
| **Don't care** | FGA has no brave-chain preference. The other priorities decide. |
| **With NP** | FGA tries to form a brave chain around a clicked NP. |
| **Always** | FGA tries to form a brave chain with or without an NP. |
| **Avoid** | FGA tries to avoid a brave chain. |

A new turn starts with **Don't care**.

### The Change from `pre-2614`

`pre-2614` had a **With NP Mighty** setting. The current **Always** setting replaces it, and **Always** can also look for a brave chain with no NP.

## Two Paths

FGA uses one of two paths for each turn.

| **Use Chain Priority** | Path | Behavior |
| ---------------------- | ---- | -------- |
| Off | The legacy path | The path reads only the brave-chain setting. |
| On | The chain priority path | The path reads the ordered chain list. |

Turn **Use Chain Priority** off, and **Always** does the same work as **With NP**. The full **Always** behavior needs the chain priority path.

FGA also repairs the stored value. When you turn **Use Chain Priority** off on a turn that holds **Always**, FGA saves the value as **With NP**.

## The Legacy Path

This path runs when **Use Chain Priority** is off. It takes the cards that the card sort already ranked, and it moves the preferred cards to the front. The other cards stay after them in the same order.

### Don't care

FGA applies only the rearrange rule.

### With NP and Always

FGA finds the field slot of the clicked NP, then moves the face cards of that slot to the front. The other cards follow.

```text
1. Read the first NP of the sequence.
2. Take the face cards that belong to the field slot of that NP.
3. Put those cards first, then the other cards.
4. Apply the rearrange rule.
```

### Avoid

FGA takes one card from each servant in turn, then fills the rest from the largest servant groups.

```text
1. Group the cards by servant.
2. Take one card from a servant that you did not use last.
3. Repeat until you have three cards.
4. Fill any open position from the largest group.
```

## The Chain Priority Path

This path runs when **Use Chain Priority** is on. The brave chain is one pass of that pipeline. See [Chain Priority](chain-priority.md).

| Setting | Field slot that the pass uses |
| ------- | ---------------------------- |
| **Don't care** | None |
| **Avoid** | None. The avoid handler runs instead |
| **With NP** | The slot of the NP, when that slot holds at least two face cards |
| **Always** | The first slot in priority order that can complete a brave chain |

When the pass finds a slot, the chain handlers accept only an order that also forms a brave chain. The result is a Brave Mighty chain or a Brave Color chain.

## When a Brave Chain Is Possible

A field slot needs three cards to make a brave chain. FGA counts a clicked NP as one card of its own slot.

```text
Sequence: NP of field slot B, then two face cards.
Hand: field slot B holds two face cards.
Count for slot B: two face cards plus the NP, so three cards.
Result: With NP can form a brave chain.
```

Two or more clicked NPs make a brave chain impossible. Each NP belongs to its own field slot.

## Rearrange Cards

The **Rearrange Cards** switch is also a setting of one wave and turn. FGA moves the cards after the chain rules run.

| Condition | Change |
| --------- | ------ |
| One NP and one card before that NP | FGA swaps the first two cards |
| No card before the NP, and at most one NP | FGA moves the second card to the last position |

The first card of a chain gives a bonus in FGO. FGA moves the card with the second highest rank to the last position to increase that bonus. FGA also puts a card of the NP servant directly after the NP.

### When Rearrangement Applies

| Condition | Rearrangement |
| --------- | ------------- |
| 1 NP, 1 card before NP | Yes |
| 2 or more NPs | No |
| No NPs | Based on the setting |
| 0 cards before NP | Based on the setting |

## Per-Wave Setup

You can use a different setting in each wave.

| Wave | Setting | Reason |
| ---- | ------- | ------ |
| 1 | Avoid | Clear multiple enemies |
| 2 | Don't care | A transition wave |
| 3 | With NP | Focus the damage on the boss |

## Test with the Simulation

Open **Simulation** on the wave and turn entry. The ranked list marks each pick with a `Brave chain` badge. The **How FGA decided** trace shows the path that ran, the chain that won, and the rearrange step.

See [Card Simulation](card-simulation.md).

## Troubleshooting

### No brave chain forms

- Check the setting on that wave and turn.
- **With NP** needs a clicked NP.
- **Always** needs **Use Chain Priority**.
- The servant needs three cards in one field slot.
- Two or more clicked NPs make a brave chain impossible.

### The wrong servant gets the brave chain

- Move your main damage servant higher in the servant list.
- Check the NP part of the skill command for that turn.

### No extra attack

- All three cards must come from one field slot.
- A clicked NP counts as a card of its own slot.
- The cards of a support servant also count.

### The order changes with **Rearrange Cards** on

- Read the condition table above.
- Open **Simulation** to see the change step by step.

## Related Documentation

- [Chain Priority](chain-priority.md) - The ordered chain rules
- [Face Card Priority](face-card-priority.md) - The card sort
- [Custom Card Priority](custom-card-priority.md) - Exact picks that bypass the chain rules
- [Card Simulation](card-simulation.md) - Test a hand without the game
- [Command Card Priority](../../battle-setup/card-priority.md) - The rule editor
