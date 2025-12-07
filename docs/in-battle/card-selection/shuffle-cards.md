---
title: Card Shuffle Feature
description: Automatically shuffle command cards when optimal cards aren't available. Configure conditions for reshuffling in FGA.
tags:
    - battle
    - cards
    - shuffle
    - optimization
---

# Card Shuffle Feature

Reshuffle command cards to get better draws when current cards are suboptimal.

## Overview

FGA can use the card shuffle feature (available through Mystic Codes or game mechanics) to get a new set of command cards when the current draw doesn't meet your criteria. This helps ensure you have effective cards available when dealing with difficult enemies.

## Key Features

- **Condition-Based Shuffle**: Only shuffle when criteria aren't met
- **Multiple Modes**: Different conditions for different strategies
- **NP Integration**: Consider NP servant cards when deciding
- **Automatic Detection**: Scans current cards to evaluate quality

## Shuffle Modes

| Mode               | Shuffles When                      |
| ------------------ | ---------------------------------- |
| **None**           | Never shuffle                      |
| **No Effective**   | No class advantage cards available |
| **No NP Matching** | No cards matching NP servant       |

## How Shuffle Checker Works

```text
┌─────────────────────────────────────────┐
│        Command Cards Read               │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Check Shuffle Condition              │
│    Based on configured mode             │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Should Shuffle?         │ No
         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│  Use Shuffle    │    │  Select Best    │
│  Get New Cards  │    │  Available Cards│
└────────┬────────┘    └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Read New Cards                       │
│    Continue with selection              │
└─────────────────────────────────────────┘
```

## Mode Details

### None Mode

No automatic shuffling occurs:

- Use whatever cards are drawn
- Manual shuffle still possible
- Fastest processing

### No Effective Mode

Shuffles when no class advantage cards are present:

```text
Your Servants: [Saber] [Saber] [Caster]
Enemy: [Lancer]

Current Cards:
[Caster Buster] [Caster Arts] [Saber Quick] ...

None of these are "effective" against Lancer
(Sabers should have advantage)

Check: Are any cards marked as "Weak" affinity?
If none → Shuffle to try for better cards
```

**When to use**:

- Mixed class teams against single-type enemies
- Want to maximize class advantage damage

### No NP Matching Mode

Shuffles when using NP but no matching face cards exist:

```text
Using NP: Servant A (Slot 1)

Current Cards:
[Servant B] [Servant B] [Servant C] [Servant C] [Servant B]

No cards from Servant A available!

Shuffle to try for Servant A's cards
(for brave chain potential)
```

**When to use**:

- NP turns where brave chains matter
- Single target NP servants
- Maximizing main DPS damage

## Card Affinity Detection

For "No Effective" mode, FGA checks card affinity:

| Affinity | Display   | Meaning            |
| -------- | --------- | ------------------ |
| Weak     | W prefix  | Class advantage    |
| Normal   | No prefix | Neutral            |
| Resist   | R prefix  | Class disadvantage |

A card is "effective" if it has the Weak affinity.

## NP Usage Integration

For "No NP Matching" mode, FGA considers:

1. Which servant(s) are using NP this turn
2. What field slot each NP servant occupies
3. Whether any face cards belong to those servants

If NPs are queued but no matching face cards exist, shuffle is triggered.

## Shuffle Limitations

### Mystic Code Requirement

Shuffle typically requires a Mystic Code skill:

- Not all Mystic Codes have shuffle
- Skill may have cooldown
- Check your equipped Mystic Code

### One Shuffle Per Turn

FGO limits reshuffling:

- Can only shuffle once per turn
- After shuffle, must use new cards
- No infinite rerolling

### RNG Factor

Shuffling doesn't guarantee better cards:

- May get same or worse cards
- Class advantage cards not guaranteed
- Servant card distribution is random

## Tips for Best Results

1. **Match mode to strategy**: Use the mode that fits your farming approach
2. **Consider NP timing**: No NP Matching is most useful on NP turns
3. **Check Mystic Code**: Ensure you have shuffle available
4. **Don't over-rely on shuffle**: Bad RNG can persist after shuffle
5. **Test with your team**: See how often shuffle triggers

## Configuration Examples

### Boss Farming Setup

- Mode: No NP Matching
- Goal: Maximize NP servant brave chains
- When: Wave 3 boss turns

### Mixed Enemy Farming

- Mode: No Effective
- Goal: Always hit class weakness
- When: Variable enemy classes

### Speed Farming

- Mode: None
- Goal: Fastest clear time
- When: Don't need optimal cards

## Troubleshooting

### Shuffle not triggering when expected

- Verify mode is correctly set
- Check if condition is actually met
- Cards may have the required affinity/servant

### Shuffling too often

- Mode conditions are being met frequently
- Consider if shuffle is actually helping
- May want to switch to None mode

### No improvement after shuffle

- Shuffle is random, same cards possible
- Card distribution depends on deck
- Consider team composition changes

### Shuffle skill on cooldown

- Can only shuffle when skill available
- FGA checks for shuffle availability
- May need to wait for cooldown

## Shuffle vs Card Priority

| Feature    | Shuffle          | Card Priority          |
| ---------- | ---------------- | ---------------------- |
| Purpose    | Get new cards    | Pick best from current |
| When       | Before selection | During selection       |
| Random     | Yes              | No                     |
| Guaranteed | No               | Works with any cards   |

Both features work together:

1. Shuffle checks if current cards are acceptable
2. If not acceptable and shuffle available, reshuffle
3. Card priority then selects best from (possibly new) cards

## Related Documentation

- [Face Card Priority](face-card-priority.md) - Card selection logic
- [Brave Chains](brave-chains.md) - Chain formation with shuffled cards
- [Skill Maker](../../battle-setup/skill-maker.md) - Configure shuffle timing
