---
title: Card Shuffle
description: Learn how FGA Preview re-deals command cards when the hand does not meet your condition, and how to configure the shuffle wave.
tags:
    - battle
    - cards
    - shuffle
    - optimization
---

# Card Shuffle

Card shuffle re-deals the command cards when the hand does not meet your condition.

## Overview

A Mystic Code skill can give you a new set of command cards. FGA can use that skill for you when the current hand is not good enough.

Shuffle is a setting of the battle config, and not of a command-card rule. You set the condition and the wave in the **Additional Settings** group of the config.

## Key Features

- **A condition**: FGA shuffles only when the condition is met.
- **One wave**: you choose the wave that can cause a shuffle.
- **One shuffle per battle**: FGA shuffles one time in each battle.
- **Automatic detection**: FGA reads the hand and tests your condition.

## Shuffle Conditions

| Condition | FGA shuffles when |
| --------- | ----------------- |
| **None** | Never. This is the default. |
| **No effective cards** | The hand has no card with the Weak affinity. |
| **No cards matching NP** | The sequence clicks an NP, and the hand has no face card from the field slot of that NP. |

The **Wave** stepper sets the wave that can cause a shuffle, from 1 to 3. The stepper appears when you select a condition other than **None**. The default wave is 3.

## How the Shuffle Check Works

```mermaid
flowchart TD
    A[Open the attack screen and read the cards] --> B{Is this the configured wave?}
    B -->|No| C[Use the cards]
    B -->|Yes| D{Did this battle already shuffle?}
    D -->|Yes| C
    D -->|No| E[Test the condition]
    E -->|Condition met| F[Cast the shuffle skill and read the cards again]
    E -->|Condition not met| C

## Condition Details

### No Effective Cards

FGA counts the face cards that have the Weak affinity. A card is effective when the servant of that card has a class advantage against the enemy.

```text
Your servants: Saber, Saber, Caster
Enemy: Lancer

Hand: Caster Buster, Caster Arts, Saber Quick

Cards with the Weak affinity: none
Result: FGA shuffles
```

### No Cards Matching NP

FGA reads the field slot of each NP in the attack sequence. It then counts the face cards that belong to those slots.

```text
Sequence: NP of field slot 1, then two face cards

Hand: field slot 1 has no card. Field slot 2 has three cards.

Face cards in field slot 1: none
Result: FGA shuffles
```

The condition does nothing when the sequence clicks no NP.

## Card Affinity

FGA reads the affinity of each face card.

| Affinity | Meaning |
| -------- | ------- |
| Weak | The servant has a class advantage |
| Normal | The classes are neutral |
| Resist | The servant has a class disadvantage |

See [Face Card Priority](face-card-priority.md) for the full code of a card.

## Limitations

### The Mystic Code Skill

The shuffle needs the third skill of your Mystic Code.

- Not every Mystic Code has a shuffle skill.
- The skill has a cooldown.
- Check the Mystic Code that you equip.

### One Shuffle Per Battle

FGA shuffles one time in each battle, and only on the wave that you set. A shuffle does not guarantee a better hand.

### A Random Result

The new hand is random.

- You can get the same cards.
- A card with a class advantage is not guaranteed.
- The distribution of the cards of a servant is random.

    F --> C
```

## Shuffle and Card Selection

| Feature | Shuffle | Card priority |
| ------- | ------- | ------------- |
| Purpose | Get a new hand | Pick the best card from the hand |
| When | Before the selection | During the selection |
| Random | Yes | No |

Both features work together:

1. FGA reads the hand.
2. FGA tests your shuffle condition on the wave that you set.
3. FGA shuffles when the condition is met and the battle did not shuffle yet.
4. The card rules then rank the hand, which can be the new hand.

## Tips

1. Match the condition to your plan. Use **No effective cards** to always hit a class weakness.
2. Use **No cards matching NP** on the turns where a brave chain matters.
3. Check that your Mystic Code has a shuffle skill.
4. Keep **None** when you want the fastest clear.

## Troubleshooting

### FGA does not shuffle

- Check that the condition is not **None**.
- Check that the wave matches the wave of the turn.
- A battle shuffles one time only.
- The condition can already be met.

### FGA shuffles too often

The condition is met often in your quests. Check the condition, or set **None**.

### The new hand is not better

The new hand is random. You can get the same cards.

### The shuffle skill does nothing

- The skill can be on cooldown.
- Your Mystic Code can have no shuffle skill.

## Related Documentation

- [Face Card Priority](face-card-priority.md) - The card sort that runs after the shuffle
- [Card Simulation](card-simulation.md) - Test a hand without the game
- [Battle Config](../../battle-setup/config.md#additional-settings) - Set the shuffle condition
