---
title: Brave Chain Optimization
description: Maximize damage with brave chains in FGA. Configure card selection to form or avoid brave chains based on your farming strategy.
tags:
    - battle
    - cards
    - brave-chain
    - damage
---

# Brave Chain Optimization

Form or avoid brave chains to maximize your battle effectiveness.

## Overview

A Brave Chain occurs when you select three command cards from the same servant, granting an extra attack at the end of the chain. FGA can optimize card selection to form brave chains when you want maximum damage, or avoid them when you need to spread attacks across multiple servants.

## Key Features

- **Force Brave Chains**: Prioritize same-servant cards for extra attacks
- **Avoid Brave Chains**: Spread cards across servants for balanced damage
- **NP Brave Chains**: Combine Noble Phantasm with face cards
- **Mighty Chains**: Optimize for mixed card type bonuses
- **Card Rearrangement**: Position cards for maximum damage

## Brave Chain Modes

| Mode        | Behavior                     | Best For               |
| ----------- | ---------------------------- | ---------------------- |
| **None**    | No chain optimization        | Default card priority  |
| **Avoid**   | Spread cards across servants | Multiple enemy targets |
| **With NP** | Form chains with NP cards    | Single target damage   |
| **Mighty**  | Mixed card types + NP        | Balanced damage boost  |

## How Brave Chains Work

### Standard Brave Chain

```text
┌─────────┬─────────┬─────────┬─────────┐
│ Card 1  │ Card 2  │ Card 3  │  Extra  │
│ (Saber) │ (Saber) │ (Saber) │ Attack! │
└─────────┴─────────┴─────────┴─────────┘

All 3 cards from same servant = Extra Attack
```

### NP Brave Chain

```text
┌─────────┬─────────┬─────────┬─────────┐
│   NP    │ Buster  │ Quick   │  Extra  │
│ (Saber) │ (Saber) │ (Saber) │ Attack! │
└─────────┴─────────┴─────────┴─────────┘

NP + 2 face cards from same servant = NP Brave Chain
```

## Brave Chain Mode Details

### None Mode

No special handling for brave chains. Cards are selected purely based on card priority.

- Uses default priority order
- May accidentally form or avoid chains
- Fastest processing (no chain analysis)

### Avoid Mode

Actively prevents brave chains by selecting cards from different servants.

```text
Selection Process:
1. Group cards by servant
2. Take one card from each servant
3. Repeat until 3 cards selected
4. Only use same-servant if no alternatives
```

**Best for:**

- Multi-target waves
- Distributing damage evenly
- Generating stars/NP for multiple servants

### With NP Mode

Prioritizes forming brave chains when using Noble Phantasms.

```text
Selection Process:
1. Identify NP servant(s)
2. Find matching face cards from NP servant
3. Place NP and matching cards together
4. Fill remaining slots with priority cards
```

**Best for:**

- Single target boss damage
- Maximizing main DPS output
- Challenge quest final waves

### Mighty Chain Mode

Attempts to form chains with different card types for the Mighty Chain bonus.

```text
Mighty Chain Bonus:
Buster + Arts + Quick = +20% damage to all cards

Selection Process:
1. If using NP, check if different card types available
2. Select one of each type (B, A, Q) when possible
3. Prioritize cards from NP servant
4. Get bonus damage on entire chain
```

**Best for:**

- Servants with varied card decks
- Situations where chain bonus outweighs card priority
- NP turns with all three card types available

## Card Rearrangement

When enabled, FGA rearranges selected cards to optimize damage output.

### The Third Card Bonus

In FGO, the third card in a chain receives bonus damage. Rearrangement puts your second-best card in the third position:

```text
Without Rearrangement:
Position: [1st]     [2nd]     [3rd]
Cards:    Best   →  2nd Best → 3rd Best
Bonus:    First     Normal    +Bonus
          Card

With Rearrangement:
Position: [1st]     [2nd]     [3rd]
Cards:    Best   →  3rd Best → 2nd Best
Bonus:    First     Normal    +Bonus
          Card

Result: 2nd best card gets the position bonus
```

### When Rearrangement Applies

| Condition              | Rearrangement    |
| ---------------------- | ---------------- |
| 1 NP, 1 card before NP | Yes              |
| 2+ NPs selected        | No               |
| No NPs                 | Based on setting |
| 0 cards before NP      | Based on setting |

## Per-Wave Configuration

Configure different brave chain settings for each wave:

### Typical Setup

| Wave | Brave Chain | Rearrange | Reason                 |
| ---- | ----------- | --------- | ---------------------- |
| 1    | Avoid       | Off       | Clear multiple enemies |
| 2    | None        | On        | Transition wave        |
| 3    | With NP     | On        | Focus boss damage      |

## NP Usage Integration

Brave chains work with your NP configuration:

### Multiple NPs

When using multiple NPs in one turn:

- Chains consider all NP servants
- Matching face cards grouped after NPs
- Rearrangement may be disabled

### Cards Before NP

The "Cards Before NP" setting affects brave chains:

```text
Example: 1 card before NP, brave chain enabled

Turn Order:
1. Face card (from NP servant)
2. NP
3. Face card (from NP servant)
4. Extra attack!
```

## Tips for Best Results

1. **Match brave chain to content**: Avoid for farming, With NP for bosses
2. **Enable rearrangement with brave chains**: Maximize the third card bonus
3. **Use servant priority with brave chains**: Ensure your DPS has cards selected
4. **Check card availability**: Brave chains need 3 cards from one servant
5. **Consider NP card type**: NP counts toward card chain bonuses too

## Chain Type Synergies

Combining brave chains with card chains:

| Cards Selected      | Bonuses                     |
| ------------------- | --------------------------- |
| 3 Buster + Brave    | Buster chain + Extra attack |
| NP + 2 Arts + Brave | Arts chain + Extra attack   |
| B + A + Q + Brave   | Mighty chain + Extra attack |

## Troubleshooting

### Brave chains not forming

- Ensure brave chain mode is not set to "None" or "Avoid"
- Check if the servant has 3 cards on screen
- Verify servant tracking correctly identifies cards
- NP must be ready for NP brave chains

### Wrong servant getting brave chain

- Adjust Servant Priority to favor your main DPS
- Check NP usage settings
- Verify the servant you want has enough cards available

### Extra attack not triggering

- All 3 cards must be from the same servant
- NP counts as a card from that servant
- Support servant cards work for brave chains too

### Rearrangement not working

- Check if rearrangement is enabled for current wave
- Multiple NPs disable rearrangement
- Verify brave chain mode supports rearrangement

## Legacy Behavior

The "Avoid" mode uses a legacy algorithm that:

1. Sorts cards into servant groups
2. Takes one card per servant in rotation
3. Fills remaining slots from largest groups

This ensures maximum spread across available servants.

## Related Documentation

- [Face Card Priority](face-card-priority.md) - Base card selection
- [Command Card Priority Setup](../../battle-setup/card-priority.md) - Configure settings
- [Auto Battle](../auto-battle.md) - Overall battle automation
