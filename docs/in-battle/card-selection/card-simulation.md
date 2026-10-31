---
title: Card Simulation
description: Test FGA Preview card selection without running the game. Set up a hand, read the pick, the ranked results, and the decision trace.
tags:
    - battle
    - cards
    - simulation
    - automation
---

# Card Simulation

The simulation screen lets you build a hand of cards and read the pick that FGA would make. You do not need to run the game.

## Overview

Open **Simulation** on a wave and turn entry. The screen uses the settings of that wave and turn, and it uses the same selection pipeline that the battle automation uses.

A new simulation starts with a default hand of five face cards and three NP cards.

## Key Features

- **A hand that you build**: five face cards and three NP cards.
- **The real pick**: the pick comes from the live selection pipeline.
- **Ranked results**: every possible pick, from the best to the worst.
- **A decision trace**: each step of the pipeline for that hand.
- **Nothing to save**: the hand is temporary and does not change your config.

## Set the Hand

The screen has two card sections and one sequence section.

### NP Cards

The NP section shows three NP mini-cards. Each card shows its slot letter, its type, its affinity, its owner, and its stunned state.

- Tap an NP to turn it on or off. A card that is off is dim, and FGA does not use that NP.
- Tap **Edit card** on an NP to open the NP pane.

### Command Cards

The command section shows five mini-cards. Each card shows its face letter, its affinity and type code, its owner, its star percentage, and its stunned state.

- Tap a card to open the card pane.

### Attack Sequence

The attack sequence shows the three click positions of the turn.

- Drag an NP to move it to another position.
- The other positions are placeholders. FGA fills them from the face-card priority.

Tap **Reset simulation cards** in the top bar to restore the default hand.

## Edit a Card

The card pane and the NP pane write each change at once. There is no draft and no **Done** step inside the pane. A live preview at the top shows the card as it is now.

| Field | Pane | Values |
| ----- | ---- | ------ |
| Card Type | Both | Buster, Arts, Quick |
| Affinity | Both | Weak, Normal, Resist |
| Team Slot | Card only | Slots 1 to 6 |
| Critical | Card only | On or off |
| Critical Percentage | Card only | 0 to 100 in steps of 10 |
| Stunned | Both | On or off |
| Use this NP | NP only | On or off |

### Team Slots and Field Slots

The two kinds of slot are different, and the difference matters.

- **Team Slot** is the position of the servant in your party, from 1 to 6. FGA uses this slot only for servant priority. You can set it on each card.
- **Field Slot** is the position of the servant on the battle screen, from 1 to 3. FGA uses this slot for chains and for custom picks. The simulation works it out and never stores it.

The simulation maps the servants of the hand onto the field slots in team slot order. The cards of the servant with the lowest team slot become field slot 1.

A hand can hold at most three different team slots, because only three servants can be on the field.

### Two Notes

- A change to the type of an NP affects the results only when that NP is on. The legacy brave-chain path does not read the NP type.
- When the rule turns on **Skip Servant Face Card Checks**, FGA cannot use a custom pick. A pick that matches then does not show as the result.

## Read the Results

The screen shows the pick, the priority order, and the ranked list.

### The Pick

The **Cards FGA would pick** row shows the cards in the order that the automation clicks them.

### The Priority Order

The **Face-card priority order** row shows the five face cards in the order that the sort makes. This order is the input to the chain rules.

### The Ranked List

The list shows every possible pick of three cards, from the best to the worst. Each row shows the rank, the cards of the pick, and the rest of the hand under a **Not picked** caption.

The count of picks depends on the number of NPs that you turn on.

| NPs on | Picks |
| ------ | ----- |
| 0 | 60 |
| 1 | 20 |
| 2 | 5 |
| 3 | 1 |

Each pick carries badges instead of scores.

| Badge | Meaning |
| ----- | ------- |
| `Brave chain` | All three cards come from one field slot. |
| A chain name | The pick satisfies a chain type from your chain priority list. |
| `Custom selection` | The pick is the sequence of a custom pick that matched. |
| `FGA's pick` | The pick is what the automation clicks. |

## Read the Decision Trace

The **How FGA decided** section shows each step of the pipeline for the hand. FGA runs the same steps in battle.

| Step | Name | What it shows |
| ---- | ---- | ------------- |
| 0 | Custom card priority check | The pick that matched, or the reason that FGA did not test the picks |
| 1 | Face-card priority sort | The ranked cards, and whether servant priority ran |
| 2 | Chain reorder | The new order, the chain that won, and any rearrange change |
| 3 | Take what the sequence needs | The cards that fill the face-card positions |
| 4 | Final click sequence | The NPs and the face cards in click order |

A custom pick that matches decides the click sequence. FGA then marks steps 1 to 3 as bypassed.

Step 0 shows one of three results:

| Result | Meaning |
| ------ | ------- |
| A pick matched | The match skips all priority sorting |
| No pick matched | Each pick, with a check mark or a cross for each card |
| FGA did not test the picks | The switch is off, or face-card checking is off |

See [Custom Card Priority](custom-card-priority.md) for the match rules.

## What the Simulation Does Not Do

- The hand is not saved to the battle config.
- The hand stays the same while you move between the wave and turn entries of the open editor.
- FGA keeps the hand until you reset it or close the editor.

## Troubleshooting

### My custom pick does not show as the pick

Read step 0 of the trace. The trace gives the reason. See [Custom Card Priority](custom-card-priority.md#test-with-the-simulation).

### The chain that I put first does not win

Some hands cannot form that chain. Read step 2 of the trace, then read the picks that are available. See [Chain Priority](chain-priority.md).

### A change to an NP does nothing

Turn that NP on. FGA reads the type of an NP only in the chain rules, and the legacy brave-chain path does not read it.

### The best pick in the list is not the pick of FGA

The list uses a score that copies the pipeline rules. In a rare case a fallback in the pipeline does not match that score. The `FGA's pick` badge always shows the real answer.

## Related Documentation

- [Face Card Priority](face-card-priority.md) - The card sort
- [Chain Priority](chain-priority.md) - The ordered chain rules
- [Custom Card Priority](custom-card-priority.md) - Exact three-card picks
- [Brave Chains](brave-chains.md) - Same-servant chains
- [Command Card Priority](../../battle-setup/card-priority.md) - The rule editor
