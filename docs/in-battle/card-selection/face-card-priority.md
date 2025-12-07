---
title: Face Card Priority System
description: Configure how FGA selects command cards during battle. Set card type priorities, servant order, and critical star preferences.
tags:
    - battle
    - cards
    - priority
    - automation
---

# Face Card Priority System

Control how FGA selects the best command cards during battle.

## Overview

The Face Card Priority system determines which command cards FGA clicks during the attack phase. You can configure priorities based on card type (Buster, Arts, Quick), servant order, class affinity, and critical star chance to optimize your farming or boss-killing strategy.

## Key Features

- **Card Type Priority**: Prioritize Buster, Arts, or Quick cards
- **Affinity Sorting**: Prefer cards with class advantage (weak affinity)
- **Servant Priority**: Group cards by servant before sorting
- **Critical Star Detection**: Prioritize cards with high critical chance
- **Per-Wave Configuration**: Different priorities for each quest wave

## How Card Selection Works

```text
┌─────────────────────────────────────────┐
│         Read 5 Command Cards            │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Parse Card Properties                │
│    • Card type (B/A/Q)                  │
│    • Affinity (W/Normal/R)              │
│    • Critical percentage                │
│    • Servant owner                      │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Apply Servant Priority (if enabled)  │
│    Group cards by servant order         │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Apply Card Priority                  │
│    Sort by type + affinity + critical   │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Select Top 3 Cards                   │
└─────────────────────────────────────────┘
```

## Card Type Priority

### Card Types

| Type       | Icon  | Best For                  |
| ---------- | ----- | ------------------------- |
| **Buster** | Red   | Damage output             |
| **Arts**   | Blue  | NP gauge charging         |
| **Quick**  | Green | Critical stars generation |

### Affinity Modifiers

| Prefix         | Meaning            | Damage        |
| -------------- | ------------------ | ------------- |
| **W** (Weak)   | Class advantage    | +50% to +100% |
| _(none)_       | Neutral            | Normal        |
| **R** (Resist) | Class disadvantage | -50%          |

### Critical Modifier

| Suffix   | Meaning                   |
| -------- | ------------------------- |
| **C**    | High critical star chance |
| _(none)_ | Low or no critical chance |

### Priority Code Examples

| Code    | Full Meaning              |
| ------- | ------------------------- |
| **WBC** | Weak Buster with Critical |
| **WB**  | Weak Buster               |
| **BC**  | Buster with Critical      |
| **B**   | Normal Buster             |
| **RA**  | Resist Arts               |

## Default Priority Order

The standard priority from highest to lowest:

```text
WBC → WAC → WQC → WB → WA → WQ → BC → AC → QC → B → A → Q → RB → RA → RQ
```

This order:

1. Maximizes damage with class advantage cards
2. Capitalizes on critical opportunities
3. Falls back to neutral cards
4. Avoids resist cards unless necessary

## Servant Priority

When enabled, cards are grouped by servant before applying card priority.

### Team Slot Positions

| Slot | Position                 |
| ---- | ------------------------ |
| 1    | First servant (leftmost) |
| 2    | Second servant           |
| 3    | Third servant            |
| 4    | First backup             |
| 5    | Second backup            |
| 6    | Third backup             |

### Selection Process with Servant Priority

```text
Example Setup:
- Servant Priority: [3, 1, 2]
- Card Priority: [B, A, Q]

Available Cards:
- Servant 1: Arts, Buster
- Servant 2: Quick, Quick
- Servant 3: Buster, Arts

Selection Order:
1. Servant 3's Buster (highest priority servant + card)
2. Servant 3's Arts
3. Servant 1's Buster
4. Servant 1's Arts
5. Servant 2's Quick
6. Servant 2's Quick
```

## Critical Star Priority

When enabled, FGA reads the critical star percentage on each card and factors it into sorting.

### Detection Method

- Scans the star icon area on each card
- Detects percentage numerically (7% threshold for "critical")
- Cards with high critical chance are promoted within their priority group

### When to Enable

| Situation                  | Recommendation   |
| -------------------------- | ---------------- |
| Consistent star generation | Enable           |
| Variable star counts       | Enable           |
| No star generators         | Disable (faster) |
| Challenge quests           | Enable           |

## Per-Wave Configuration

Different waves may need different strategies:

### Wave 1 (Farming)

- Focus: NP generation
- Priority: Arts cards
- Goal: Charge NP for later waves

### Wave 2 (Transition)

- Focus: Clear enemies efficiently
- Priority: Balanced or Quick
- Goal: Generate stars for wave 3

### Wave 3 (Boss)

- Focus: Maximum damage
- Priority: Buster cards + servant priority
- Goal: Defeat boss with critical hits

## Tips for Best Results

1. **Match your team composition**: If running Buster servants, prioritize Buster cards
2. **Use servant priority for single-target damage**: Focus all cards on your main damage dealer
3. **Enable critical stars for RNG-heavy teams**: Critical hits can dramatically increase damage
4. **Adjust per wave**: Different waves often need different card selections
5. **Consider card chains**: Three of the same type gives bonus effects

## Card Chain Bonuses

Selecting three cards of the same type grants bonuses:

| Chain Type   | Bonus                          |
| ------------ | ------------------------------ |
| Buster Chain | +20% attack for all cards      |
| Arts Chain   | +20% NP gauge for all servants |
| Quick Chain  | +10 critical stars             |

## Troubleshooting

### Cards not being selected in expected order

- Check if Servant Priority is overriding Card Priority
- Verify critical star detection isn't promoting unexpected cards
- Confirm the current wave is using the correct priority configuration

### Servant's cards not being picked

- Add the servant higher in Servant Priority list
- Check if the servant is stunned (stunned cards are deprioritized)
- Verify the servant tracker correctly identified the servant

### Wrong card types being selected

- Review your Card Priority order in settings
- Check if affinity detection is working correctly
- Ensure your priority list includes all card types you want

### Critical cards not being prioritized

- Enable "Read Critical Star Priority" in settings
- Check if the critical threshold is being met (7%+)
- Verify the card visually shows critical stars

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Command Card Priority Setup](../../battle-setup/card-priority.md) - Configure priorities
- [Brave Chains](brave-chains.md) - Card chain optimization
