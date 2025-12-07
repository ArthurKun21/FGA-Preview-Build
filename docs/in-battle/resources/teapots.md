---
title: Teapot Management
description: Automatically manage teapots for bonus drops during FGO events. Configure teapot limits and usage timing in FGA.
tags:
    - battle
    - teapots
    - events
    - bonuses
---

# Teapot Management

Automatically activate and manage teapots for bond leveling.

## Overview

Teapots (officially "Stargazer's Teapot") provide double the Bond gained when completing a quest for the entire Party (including sub-members). FGA can automatically manage teapot activation before battles and track usage to ensure you don't exceed your limits.

## Key Features

- **Automatic Activation**: Turn on teapots before battles start
- **Usage Limits**: Set maximum teapots per farming session
- **State Management**: Track on/off state across runs
- **Ordeal Call Support**: Special handling for Ordeal Call quests
- **JP Server Format**: Supports new popup window interface

## How Teapots Work

```text
┌─────────────────────────────────────────┐
│        Party Selection Screen           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Check Teapot Settings                │
│    • Teapots enabled?                   │
│    • Limit remaining?                   │
│    • Current state on/off?              │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Should Use Teapot?      │ No
         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│  Toggle Teapot  │    │  Ensure Teapot  │
│  State to ON    │    │  State is OFF   │
└────────┬────────┘    └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Track Teapot Usage                   │
└─────────────────────────────────────────┘
```

## Teapot States

| State   | Icon          | Effect                 |
| ------- | ------------- | ---------------------- |
| **Off** | Gray/disabled | No bonus drops         |
| **On**  | Lit/glowing   | Bonus drop rate active |

## Configuration

### Enable Teapots

1. Open your Battle Config
2. Find the Teapot/Dreamfire settings
3. Enable teapot usage
4. Set your limit

### Teapot Limit

| Setting | Behavior                      |
| ------- | ----------------------------- |
| 0       | Teapots disabled              |
| 1+      | Maximum teapots to use        |
| Per run | One teapot consumed per quest |

## Teapot Management Points

FGA manages teapots at two key points:

### 1. Party Selection Screen

Before entering battle:

- Checks current teapot state
- Activates if limit allows
- Deactivates if limit reached
- Handles last-run scenarios

### 2. Quest Repeat Screen

After completing a quest:

- Verifies teapot state
- Updates for next run
- Manages state transitions

## JP Server New Format

The Japanese server introduced a popup window for teapot management:

```text
┌─────────────────────────────────────────┐
│         Teapot Popup Window             │
├─────────────────────────────────────────┤
│                                         │
│    [Teapot Icon]                        │
│                                         │
│    Remaining: X                         │
│                                         │
│    [ OFF ]  [ ON ]                      │
│                                         │
└─────────────────────────────────────────┘
```

FGA detects and handles both the old toggle format and new popup window.

## Ordeal Call Quests

Ordeal Call quests have special teapot handling:

- No repeat quest screen after completion
- Teapot counted at different timing
- Special logic to ensure accurate tracking
- Cannot be turned off when ran out of storm pods.

```text
Ordeal Call Flow:
Quest Complete → (No Repeat Screen) → Next Quest

FGA tracks teapot at quest completion instead
```

## Usage Tracking

### During Session

FGA tracks teapots in real-time:

```text
┌─────────────────────────────────────────┐
│         Teapot Status                   │
├─────────────────────────────────────────┤
│ Teapots Used: 3                         │
│ Teapot Limit: 10                        │
│ Remaining: 7                            │
└─────────────────────────────────────────┘
```

### Exit Summary

After script completion:

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ Teapots Used: 5                         │
│ ...                                     │
└─────────────────────────────────────────┘
```

## Last Run Handling

When on the final run of a limited session:

| Scenario          | Teapot Action         |
| ----------------- | --------------------- |
| More runs planned | Keep on for next run  |
| Last run          | Turn off after battle |
| Limit reached     | Turn off immediately  |

This ensures teapots aren't wasted on the repeat screen when you won't continue.

## Tips for Best Results

1. **Match teapots to runs**: Set teapot limit equal to or less than run limit
2. **Check event inventory**: Verify you have teapots before starting
3. **Monitor usage**: Watch the exit summary for accurate counts
4. **Test before farming**: Run one quest to verify teapot activation
5. **Consider Ordeal Call**: Special handling may affect timing

## Testing Teapot Configuration

Verify your setup with these test cases:

| Test                        | Expected Result            |
| --------------------------- | -------------------------- |
| 1 run, 1 teapot             | Turns off after battle     |
| 2 runs, 1 teapot            | Turns off after 1st battle |
| 1 run, 2 teapots            | Uses 1, leaves 1 for next  |
| 1 run, 0 teapots (state on) | Turns off before battle    |
| 3 OC runs, 3 teapots        | All 3 counted correctly    |

## Troubleshooting

### Teapot not activating

- Check if teapot limit is greater than 0
- Verify teapots are available in inventory
- Ensure the feature is enabled in settings
- Check if you're on the party selection screen

### Wrong teapot count

- Ordeal Call quests count differently
- Multiple quests may share state
- Check exit summary for accurate count

### Teapot stays on after limit reached

- May occur during screen transitions
- FGA corrects on next management point
- Verify state on party selection screen

### JP popup not being handled

- Update to latest FGA version
- New popup format requires updated detection
- Check if popup is fully visible on screen

### Teapot state stuck

- Close and reopen quest screen
- Manually toggle teapot state
- Restart FGA script

## Server Differences

| Server | Format    | Notes                      |
| ------ | --------- | -------------------------- |
| JP     | New popup | Supports latest interface  |
| NA/EN  | Toggle    | Classic on/off button      |
| Others | Varies    | Check server documentation |

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Run Limits](../../app/advanced.md) - Configure run limitations
- [Materials Tracking](../tracking/materials-tracking.md) - Track event drops
