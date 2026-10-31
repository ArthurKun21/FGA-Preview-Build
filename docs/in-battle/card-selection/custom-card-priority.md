---
title: Custom Card Priority
description: Set exact three-card picks in FGA Preview. Learn how a match works, when it bypasses card and chain priority, and how to test it.
tags:
    - battle
    - cards
    - priority
    - automation
---

# Custom Card Priority

Custom card priority lets you name the exact three cards for a turn. When your pick matches the hand, FGA clicks those three cards in your order.

## Overview

In `pre-2614`, FGA always ranked the cards with the card and servant priority. Now each wave and turn can hold an ordered list of exact picks. FGA reads the list from top to bottom and uses the first pick that matches the hand.

A match has the highest priority of all the card rules. FGA does not run the card sort, the chain rules, or the rearrange rule.

## Key Features

- **Exact picks**: you choose the card type and the field slot of each card.
- **Per-turn lists**: each wave and turn keeps its own picks.
- **Match order**: the first pick that fully matches wins.
- **A full bypass**: a match replaces the card sort, the chain rules, and the rearrange rule.
- **A test in the app**: the simulation shows the match and the reason for a failure.

## Set a Custom Pick

1. Turn on **Use Custom Cards Priority** on the wave and turn entry.
2. Open **Custom Cards Priority**.
3. Tap **Add**.
4. Choose exactly three cards.
5. Tap **Done**.
6. Add more picks, then drag a pick to set the match order.

The **Custom Cards Priority** row stays dim until you turn on the switch.

## Choose the Cards

The **Select cards** screen shows three empty slots and the choices for each field slot.

Each field slot 1, 2, and 3 offers four buttons: `B`, `A`, `Q`, and `NP`. Tap a button to fill the next empty slot. Tap a filled slot to take the card out.

A card in a pick is a card type plus a field slot. The field slot is the position of the servant on the battle screen. It is not the position of the servant in your party.

!!! note "The NP button is off"

    FGA reads the type of an NP card only when it detects the servant of that card. Because this read is not yet reliable, the `NP` button is off. A pick can hold face cards only.

## How a Match Works

FGA reads the five face cards and the NP cards, then tests each pick in your order.

The test follows these rules:

1. A pick with fewer than three cards or more than three cards never matches.
2. FGA matches each card in the pick to a different card on the screen.
3. FGA walks the cards in the order of the pick. A card type that you use two times needs two matching cards on the screen.
4. A face card matches when the card type and the field slot are both equal.
5. An NP card matches when the field slot is equal.
6. A stunned card never matches.
7. When two cards on the screen match one card in the pick, FGA takes the critical card first.

The class affinity and the critical percentage are not part of the pick. FGA uses them only to choose between two cards that both match.

### Examples

```text
Pick: B1, B1, A1
Hand: field slot 1 has two Buster cards and one Arts card.
Result: the pick matches. FGA clicks the two Buster cards, then the Arts card.
```

```text
Pick: B1, A2, Q3
Hand: field slot 1 has two Buster cards. Field slot 2 has one Arts card. Field slot 3 has one Quick card.
Result: the pick matches.
```

```text
Pick: A1, A1, A1
Hand: field slot 1 has one Arts card and two Buster cards.
Result: no match. The pick needs three Arts cards in field slot 1, and only one is present.
```

## What a Match Does

A match sets the click order of the turn. FGA clicks the matched cards in the order of your pick.

These steps do not run for that turn:

- the face-card priority sort
- the chain priority rules and the brave-chain rules
- the rearrange rule

When no pick matches, FGA uses the normal card rules. See [Face Card Priority](face-card-priority.md).

## When FGA Does Not Test the Picks

FGA does not test the picks in two cases:

- **Use Custom Cards Priority** is off for that wave and turn.
- The rule turns on **Skip Servant Face Card Checks**. FGA then has no face-card data to compare.

The face-card setting belongs to the whole rule, so it applies to every wave and turn of that rule. See [Command Card Priority](../../battle-setup/card-priority.md).

## Test with the Simulation

Open **Simulation** on the wave and turn entry. The **How FGA decided** trace starts with step 0, the custom card priority check.

| Result | What the trace shows |
| ------ | -------------------- |
| A pick matched | The three cards, and a note that the match skips all priority sorting |
| No pick matched | Each pick, with a check mark or a cross for each card of the pick |
| FGA did not test the picks | The reason. The switch is off, or face-card checking is off |

A cross on one card of a pick means that the hand has no card for that position. FGA stops the test at the first failure, so the cards after that cross also show as unmatched.

The ranked list marks the matched pick with a `Custom selection` badge. See [Card Simulation](card-simulation.md).

## Troubleshooting

### My pick never matches

- Check that **Use Custom Cards Priority** is on for that wave and turn.
- Check that the pick holds exactly three cards.
- Check the field slot of each card. The slot is the position on the battle screen.
- Check that the hand holds enough cards of that type in that slot.
- Check that no servant of the pick has the stunned state.
- Check the **Skip Servant Face Card Checks** setting of the rule.

### FGA clicks a different set of cards

Only the first pick that fully matches wins. Move your pick to the top of the list.

### FGA clicks the critical version of my card

Your pick holds a card type and a field slot. Two cards on the screen can have the same type and slot. FGA takes the critical card first.

### FGA picks cards with no match at all

A pick that does not match leaves the turn to the normal card rules. Read step 0 of the trace to find the card that failed.

## Related Documentation

- [Face Card Priority](face-card-priority.md) - The card sort that a match replaces
- [Chain Priority](chain-priority.md) - The chain rules that a match replaces
- [Brave Chains](brave-chains.md) - Same-servant chains
- [Card Simulation](card-simulation.md) - Test a hand without the game
- [Command Card Priority](../../battle-setup/card-priority.md) - The rule editor
