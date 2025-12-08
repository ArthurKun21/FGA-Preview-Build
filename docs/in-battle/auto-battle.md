---
title: Auto Battle
description: Automate farming quests in FGA Preview. Handle support selection, battle execution, skill commands, card selection, and result screens for efficient FGO farming.
tags:
  - scripts
  - battle
  - automation
  - farming
---

# Auto Battle

Automatically farms quests by handling support selection, battle execution, and result screens.

## Overview

The Auto Battle script is the primary automation script for farming quests in Fate/Grand Order. It handles the complete quest loop: selecting supports, executing battles using configured skills and card selections, processing rewards, and repeating quests until a stop condition is met.

## How to Start

1. Navigate to a **Quest Selection** screen in the game (showing the quest you want to farm)
2. **Configure a Battle Config** with your skill commands and card priorities
3. The script will automatically detect the battle screen when:
    - The Menu icon is visible (quest selection screen)
    - You're already in a support selection screen
    - You're in the middle of a battle
4. Start the script

!!! tip "Important"
    You must configure a Battle Config with skill commands before starting. The script will exit if skill commands cannot be parsed.

## Workflow

```text
┌─────────────────────────────────────────┐
│           Start Auto Battle             │
└─────────────────────┬───────────────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │     Main Battle Loop    │◄───────────────────────┐
        └─────────────┬───────────┘                        │
                      │                                    │
                      ▼                                    │
        ┌─────────────────────────┐                        │
        │   Detect Current Screen │                        │
        └─────────────┬───────────┘                        │
                      │                                    │
    ┌─────────────────┼─────────────────┐                  │
    │                 │                 │                  │
    ▼                 ▼                 ▼                  │
┌────────┐     ┌───────────┐     ┌───────────┐            │
│ Menu   │     │  Support  │     │  Battle   │            │
│ Screen │     │  Screen   │     │  Screen   │            │
└───┬────┘     └─────┬─────┘     └─────┬─────┘            │
    │                │                 │                   │
    ▼                ▼                 ▼                   │
Select Quest    Select Support    Execute Battle          │
    │                │                 │                   │
    └────────────────┴────────┬────────┘                   │
                              │                            │
                              ▼                            │
                    ┌─────────────────────┐                │
                    │   Result Screens    │                │
                    │  (Bond, Drops, EXP) │                │
                    └─────────┬───────────┘                │
                              │                            │
                              ▼                            │
                    ┌─────────────────────┐                │
                    │  Continue/Repeat?   │                │
                    └─────────┬───────────┘                │
                              │                            │
                 ┌────────────┴────────────┐               │
                 │ Yes                     │ No            │
                 └─────────────────────────┴───────────────┘
                              │
                              ▼
                         Exit Script
```

## Key Features

### Support Selection

- Automatic support servant selection based on configured preferences
- Multiple selection modes: Manual, First, Friend, or Preferred
- Refresh support list when preferred support not found
- See [Selection Modes](../support-screen/selection-modes.md) for details

### Battle Execution

- Executes configured skill commands per wave
- Handles card selection based on priority settings
- Supports Noble Phantasm chains and brave chains
- Manages servant swapping and order changes
- See [Skill Execution](skill-system/skill-execution.md) for details

### AP Refill (Apples)

- Automatic AP refill using configured apples
- Supports all apple types (gold, silver, bronze, copper, saint quartz)
- Configurable refill limits
- Wait for AP regeneration option
- See [Energy Refill](resources/energy-refill.md) for details

### Card Selection

- Command card reading and selection
- Face card priority sorting
- Critical star percentage consideration
- See [Face Card Priority](card-selection/face-card-priority.md) for details

### Brave Chain Optimization

- Multiple brave chain modes: None, Avoid, Force, Mighty
- Card rearrangement for damage optimization
- NP + matching face card combinations
- See [Brave Chains](card-selection/brave-chains.md) for details

### Material Tracking

- Tracks dropped materials during farming
- Can stop when target material count is reached
- Screenshots drops for reference
- See [Materials Tracking](tracking/materials-tracking.md) for details

### CE Drop Tracking

- Detects Craft Essence drops
- Can stop when CE drops
- Tracks total CE drop count
- See [CE Drops](tracking/ce-drops.md) for details

### Auto Target Selection

- Detects danger indicators (!) on enemies
- Detects servant enemies (crown icon)
- Prioritizes dangerous/servant enemies
- See [Auto Target](skill-system/auto-target.md) for details

### Run Limiting

- Configurable run limit
- Auto-decrements remaining runs
- Stops when limit reached

### Teapot Management

- Uses teapots for bonus drops (events)
- Manages teapot usage at appropriate times
- See [Teapots](resources/teapots.md) for details

## Settings

| Setting | Description |
|---------|-------------|
| Skill Command | Commands for skill usage per wave |
| Card Priority | Priority order for card selection |
| Party Selection | Which party slot to use |
| Support Selection | How to select support servant |
| Limit Runs | Enable run limit |
| Run Count | Maximum number of runs |
| Refill with Apples | Enable AP refill |
| Apple Type | Which apple types to use |
| Stop on CE Get | Stop when CE drops |
| Stop on First Clear | Stop on first clear rewards |
| Stop on Bond Level Up | Stop when bond target reached |
| Bond Level Target | Target bond level to stop at |
| Boost Item Selection | Which boost item to use (events) |

## Exit Reasons

The script will stop and notify you when any of these conditions occur:

### Normal Completion

| Exit Reason | Description |
|-------------|-------------|
| **Limit Runs** | Configured run limit has been reached |
| **Limit CEs** | CE drop limit has been reached |
| **Limit Materials** | Material drop limit has been reached |
| **CE Get** | A Craft Essence dropped (if stop on CE enabled) |
| **First Clear Rewards** | First clear rewards obtained (if stop enabled) |
| **Bond Level Reached** | Target bond level achieved |
| **Stop After This Run** | User requested stop after current run |

### Resource Depletion

| Exit Reason | Description |
|-------------|-------------|
| **AP Ran Out** | No more AP and refill not possible/allowed |
| **Inventory Full** | Servant/CE inventory is full |
| **Out of Command Spells** | No command spells available when needed |

### Configuration Issues

| Exit Reason | Description |
|-------------|-------------|
| **Support Selection Manual** | Manual support selection required |
| **Support Selection Preferred Not Set** | Preferred support not configured |
| **Skill Command Parse Error** | Invalid skill command syntax |
| **Card Priority Parse Error** | Invalid card priority configuration |
| **Withdraw Disabled** | Tried to withdraw but option disabled |
| **Preset Quest** | Preset quest detected |

### Special Conditions

| Exit Reason | Description |
|-------------|-------------|
| **Duplicate CE** | Duplicate CE detected in party (JP) |
| **Daily Reset** | Game daily reset occurred |
| **Exit on Out of Commands** | Ran out of configured commands |
| **Exit on Off Script** | Script was turned off |

### User Actions

| Exit Reason | Description |
|-------------|-------------|
| **Abort** | Script manually stopped by user |
| **Paused** | Script is paused |
| **Unexpected** | An unexpected error occurred |

See [Exit Reasons](script-control/auto-battle-exit-reasons.md) for detailed explanations of each exit condition.

## Exit State Summary

After the script completes, you receive detailed statistics:

```text
┌─────────────────────────────────────────┐
│         Battle Exit State Summary       │
├─────────────────────────────────────────┤
│ Times Ran: X                            │
│ Run Limit: Y (if enabled)               │
│ Times Refilled: Z                       │
│ Refill Limit: W                         │
│ CE Drop Count: N                        │
│ Materials: {material: count, ...}       │
│ Teapots Used: T                         │
│ Withdraw Count: V                       │
│ Total Time: HH:MM:SS                    │
│ Average Time Per Run: MM:SS             │
│ Min Turns Per Run: A                    │
│ Max Turns Per Run: B                    │
│ Average Turns Per Run: C.D              │
└─────────────────────────────────────────┘
```

## Workflow with Battle Execution

```text
┌─────────────────────────────────────────┐
│            Battle Wave Start            │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Execute Configured Skill Commands    │
│    (Master skills, Servant skills)      │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Select Cards Based on Priority       │
│    (NP, Brave chains, card types)       │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│         Wait for Wave to End            │
└─────────────────────┬───────────────────┘
                      │
                      ▼
              Next Wave or Results
```

## Tips for Best Results

1. **Configure skill commands carefully** - Test your commands before long farming sessions
2. **Set appropriate card priorities** - Optimize for your farming strategy
3. **Use run limits** - Prevent accidental over-farming
4. **Enable screenshots** - Keep records of drops and bond levels
5. **Configure refill limits** - Control apple usage
6. **Check support settings** - Ensure preferred support is properly configured
7. **Monitor inventory space** - Leave room for drops

## Server Support

All FGO servers are supported with specific features:

- **JP/EN**: Full inventory full detection
- **KR**: Inventory full detection
- **JP**: Duplicate CE detection, Ordeal Call support
- **BetterFGO**: NP skip support

## Technical Notes

- Main loop checks ~20+ different screen states
- 0.5 second delay between screen checks
- Automatic connection retry on network issues
- Tracks run statistics including turns and time
- Auto-decrements configured limits after completion

## Related Documentation

### In-Battle Features

- [Skill Execution](skill-system/skill-execution.md) - How skills are cast during battle
- [Face Card Priority](card-selection/face-card-priority.md) - Card selection priorities
- [Brave Chains](card-selection/brave-chains.md) - Brave chain optimization
- [Auto Target](skill-system/auto-target.md) - Automatic enemy targeting
- [Shuffle Cards](card-selection/shuffle-cards.md) - Card shuffling options
- [Servant Tracking](tracking/servant-tracking.md) - Tracking servants on field
- [Stage Tracking](tracking/stage-tracking.md) - Wave/stage detection
- [Party Selection](script-control/party-selection.md) - Party slot selection
- [Energy Refill](resources/energy-refill.md) - AP refill management
- [Materials Tracking](tracking/materials-tracking.md) - Drop tracking
- [CE Drops](tracking/ce-drops.md) - CE drop detection
- [Teapots](resources/teapots.md) - Teapot usage
- [Withdraw](script-control/withdraw.md) - Battle withdrawal
- [Screen Detection](script-control/screen-detection.md) - Screen state detection
- [Exit Reasons](script-control/auto-battle-exit-reasons.md) - Exit conditions

### Support Screen Features

- [Selection Modes](../support-screen/selection-modes.md) - Support selection modes
- [Preferred Servant](../support-screen/preferred-servant.md) - Servant preference settings
- [Preferred CE](../support-screen/preferred-ce.md) - CE preference settings
- [Preferred Friend](../support-screen/preferred-friend.md) - Friend preference settings
- [Class Picker](../support-screen/class-picker.md) - Class filtering
- [Grand Servant](../support-screen/grand-servant.md) - Grand servant support
- [Refresh](../support-screen/refresh.md) - Support list refresh
