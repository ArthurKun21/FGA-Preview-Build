---
title: Auto Target Enemy Selection
description: Automatically target dangerous enemies and servants during FGO battles. FGA detects priority targets and focuses your attacks.
tags:
    - battle
    - targeting
    - automation
---

# Auto Target Enemy Selection

Automatically prioritize dangerous enemies and servant bosses during battle.

## Overview

Auto Target helps you focus on the most threatening enemies first. When enabled, FGA scans the enemy formation at the start of each turn and automatically selects high-priority targets like bosses or dangerous enemies marked with special indicators.

## Key Features

- **Danger Detection**: Identifies enemies marked with the danger indicator (!)
- **Servant Detection**: Recognizes enemy servants by their crown icon
- **Formation Support**: Works with both 3-enemy and 6-enemy battle formations
- **Smart Targeting**: Prioritizes the rightmost dangerous enemy (typically the boss)

## How Auto Target Works

```text
┌─────────────────────────────────────────┐
│          Turn Starts                    │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Scan All Enemy Positions             │
│    (Left to Right)                      │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Check for Priority Indicators        │
│    • Danger icon (!)                    │
│    • Servant crown                      │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Select Rightmost Priority Target     │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Click to Focus Target                │
└─────────────────────────────────────────┘
```

## Enemy Formation Types

### Standard 3-Enemy Formation

The most common formation with enemies in three positions:

| Position | Priority |
| -------- | -------- |
| Left     | Lower    |
| Center   | Medium   |
| Right    | Higher   |

### Extended 6-Enemy Formation

Some quests feature six enemies across two rows:

| Row   | Positions                          |
| ----- | ---------------------------------- |
| Front | 3 enemies (clickable)              |
| Back  | 3 enemies (cannot target directly) |

FGA uses different detection images for 6-enemy formations to ensure accurate targeting.

## Priority Target Indicators

### Danger Indicator (!)

Enemies with the exclamation mark are about to use a powerful attack or have a special ability. Targeting them first can prevent team wipes.

### Servant Crown

Enemy servants (appearing in story quests or challenge content) are marked with a crown icon. These typically have:

- Higher HP pools
- Powerful Noble Phantasms
- Special skills and abilities

## Tips for Best Results

1. **Enable for boss fights**: Auto Target is most useful for quests with priority targets
2. **Combine with skill commands**: Use targeting commands in your skill setup to ensure focus on the right enemy
3. **Check quest formations**: Know whether you're facing a 3-enemy or 6-enemy formation for better planning
4. **Manual override available**: You can still manually select targets even with Auto Target enabled

## How Targeting Order Works

In FGO boss stages, enemies are typically arranged with the strongest on the right:

```text
┌─────────┬─────────┬─────────┐
│ Enemy 1 │ Enemy 2 │ Enemy 3 │
│ (Weak)  │ (Medium)│ (Boss)  │
└─────────┴─────────┴─────────┘
```

Auto Target scans from left to right but selects the **rightmost** priority target found. This means:

- If Enemy 3 is a servant → Target Enemy 3
- If only Enemy 1 has danger indicator → Target Enemy 1
- If both Enemy 2 and 3 are servants → Target Enemy 3

## Troubleshooting

### Auto Target isn't selecting the boss

- Verify the enemy has a visible priority indicator (! or crown)
- Check if you're in a non-standard formation that might not be detected
- Ensure the battle screen is fully loaded before the turn starts

### Wrong enemy being targeted

- The target selection always picks the rightmost priority enemy
- If multiple enemies have indicators, the one furthest right is selected
- Manual target commands in your skill setup can override auto targeting

### Targeting not working in 6-enemy quests

- FGA uses different detection images for 6-enemy formations
- Ensure your app version supports the extended formation detection
- Some event quests may have unique layouts not yet supported

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Skill Maker](../../battle-setup/skill-maker.md) - Configure manual target commands
