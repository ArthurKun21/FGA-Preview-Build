---
title: Chain Priority
description: Learn how FGA Preview orders chain types and forms Mighty, Buster, Arts, Quick, and Avoid chains during battle.
tags:
    - battle
    - cards
    - chain
    - priority
---

# Chain Priority

Chain priority is an ordered list of chain types. FGA reads the list from top to bottom and uses the first chain that it can form.

## Overview

A chain is a bonus that three cards give when they share a property. In `pre-2614`, FGA had one brave-chain setting and no other chain rule. Now each wave and turn has its own ordered list of chain types, and FGA tries each type in your order.

Chain priority is a setting of each wave and turn. Turn on **Use Chain Priority** on the entry, then open **Chain Priority** to set the order.

## Key Features

- **An ordered list**: FGA tries the types in your order and stops at the first valid chain.
- **Per-turn settings**: each wave and turn keeps its own list.
- **Hidden types**: a hidden type is not in the list, so FGA never tries it.
- **Brave chain control**: the brave-chain setting limits which chains the handlers accept.
- **A test in the app**: the simulation shows the chain that won.

## Chain Types

| Type | Chain that FGA tries to form |
| ---- | ---------------------------- |
| **Mighty** | Three cards of three types. One Buster, one Arts, and one Quick |
| **Buster** | Three Buster cards |
| **Arts** | Three Arts cards |
| **Quick** | Three Quick cards |
| **Avoid** | No chain at all |

A chain of three cards of one type is a color chain. A chain of three cards of three types is a Mighty chain.

### The Default Order

A new turn starts with this order:

1. Mighty
2. Buster
3. Arts
4. Quick

FGA permits **Avoid**, but FGA hides it. FGA never tries a hidden type.

## Set the Order

1. Turn on **Use Chain Priority** on the wave and turn entry.
2. Open **Chain Priority**.
3. Drag the handle of a type to move it. A type at the top has the highest priority.
4. Tap the eye icon of a type to hide it. The type moves to the **Hidden** list.
5. Tap the eye icon in the **Hidden** list to show a type again.

FGA stores no position for a hidden type. When you show the type again, it goes to the end of the list.

## How the Pipeline Works

This is the order of the steps. FGA runs the same steps in battle.

```text
1. Drop the cards that have an unknown type.
   A stunned card and an undetected card have an unknown type.
   FGA puts those cards back at the end of the list.

2. Test if a chain is possible. The test needs two things:
   - no clicked NP has an unknown type
   - the count of known cards is at least 3 minus the count of clicked NPs
   The test fails, so FGA keeps the priority order.

3. Try the brave chain. The result is the brave fallback, and it can be empty.
   The Avoid type uses the avoid handler instead.

4. Try each chain type in your order. The first handler that returns a valid order wins.
   Mighty uses the Mighty handler.
   Buster, Arts, and Quick use the color handler.
   Avoid uses the avoid handler.

5. Take the result. The order is:
   the chain order, then the brave fallback, then the priority order.
   The rearrange rule runs last.
```

### Force a Brave Chain

When the brave fallback has a result, and **Brave Chains** is **With NP** or **Always**, FGA forces a brave chain in step 4. The chain handlers then accept only an order that also forms a brave chain.

The result of a forced chain is a Brave Mighty chain or a Brave Color chain.

## Brave Chains and Chain Priority

The **Brave Chains** setting stays on the same wave and turn entry.

| Setting | Behavior |
| ------- | -------- |
| **Don't care** | FGA has no brave-chain preference. |
| **With NP** | FGA tries to form a brave chain around a clicked NP. |
| **Always** | FGA tries to form a brave chain with or without an NP. |
| **Avoid** | FGA tries to avoid a brave chain. |

**Always** needs **Use Chain Priority**. When you turn **Use Chain Priority** off, FGA reads a stored **Always** as **With NP**. See [Brave Chains](brave-chains.md).

## What Each Handler Needs

### Mighty Chain

The handler needs all of these things:

- no clicked NP has an unknown type
- every clicked NP has a known type
- no face card has an unknown type
- at least three different types across the face cards and the NPs
- one clicked NP, or NPs that have different types

The handler walks your card order and takes the first card of each missing type.

### Color Chain

The handler needs both of these things:

- every clicked NP has the same type as the chain
- at least three cards of that type, with the NPs counted

A color chain with one NP uses that NP plus two face cards.

### Avoid

The handler gives no result when it cannot avoid a chain. These are the cases:

- the sequence clicks three NPs
- one field slot holds all the cards, so a brave chain is certain
- the hand has one card type, so a color chain is certain

The handler then takes one card at a time. It never takes a third card of the same field slot. It never takes a card that completes a color chain or a Mighty chain. It prefers a card from a different field slot than the previous card.

## Read the NP Types

FGA reads the type of each NP card from the battle screen. A support servant NP has an unknown type. An NP also has an unknown type when the rule turns on **Skip Servant Face Card Checks**.

An unknown NP type makes every chain impossible, so FGA keeps the priority order for that turn.


## Test with the Simulation

Open **Simulation** on the wave and turn entry. The **How FGA decided** trace shows step 2, the chain reorder. The trace names one of these results:

| Result | Meaning |
| ------ | ------- |
| The name of a chain type | That handler won |
| A brave chain | The brave fallback won |
| No chain matched | FGA kept the priority order |

The trace also marks the cards that moved, and it marks the pick when the rearrange rule ran.

The ranked list marks each pick with the chain that it forms. See [Card Simulation](card-simulation.md).

## Troubleshooting

### No chain forms

- Check that **Use Chain Priority** is on for that wave and turn.
- Check that the type is not in the **Hidden** list.
- A stunned card or an unknown NP makes every chain impossible.
- Some hands cannot form your chain. FGA then uses the next type in your list.

### FGA makes a chain that I put last

The chain rules come before the card rules. FGA moves the cards that make the chain to the front. Put the chain that you want first in the list, or hide the chains that you do not want.

### FGA forms a brave chain when I ask it to avoid one

Some hands force a brave chain. When one field slot holds all the cards, all three cards come from one servant. Read the ranked list in **Simulation** to see the picks that are available.

### The order changes but no chain formed

The rearrange rule runs after the chain rules. Check the **Rearrange Cards** switch on that entry. See [Brave Chains](brave-chains.md#rearrange-cards).

## Related Documentation

- [Face Card Priority](face-card-priority.md) - The card sort that runs before the chain rules
- [Brave Chains](brave-chains.md) - Same-servant chains
- [Custom Card Priority](custom-card-priority.md) - Exact picks that bypass the chain rules
- [Card Simulation](card-simulation.md) - Test a hand without the game
- [Command Card Priority](../../battle-setup/card-priority.md) - The rule editor
