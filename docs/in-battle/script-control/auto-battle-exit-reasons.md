---
title: Exit Reasons and Session Statistics
description: Understand why FGA's Battle Script stops and how to interpret the exit state summary with run statistics.
tags:
    - battle
    - exit
    - statistics
    - troubleshooting
---

# Exit Reasons and Session Statistics

Understand why your farming session ended and review detailed statistics.

## Overview

When the Battle Script stops, FGA displays a notification with the exit reason and detailed session statistics. Understanding these helps you optimize your farming sessions and troubleshoot issues.

## Exit Reason Categories

### Normal Completion

These exit reasons indicate your farming goals were achieved.

| Exit Reason             | What Happened                                        |
| ----------------------- | ---------------------------------------------------- |
| **Limit Runs**          | You completed the configured number of runs          |
| **Limit CEs**           | You collected enough CE drops to reach your limit    |
| **Limit Materials**     | You gathered enough materials to reach your target   |
| **CE Get**              | A Craft Essence dropped (stop on CE was enabled)     |
| **First Clear Rewards** | You received first-time completion rewards           |
| **Bond Level Reached**  | A servant reached your target bond level             |
| **Stop After This Run** | You requested to stop after the current run finished |

### Resource Depletion

These occur when the script cannot continue due to resource limitations.

| Exit Reason               | What Happened                            | Solution                                        |
| ------------------------- | ---------------------------------------- | ----------------------------------------------- |
| **AP Ran Out**            | No AP remaining and no refill available  | Enable apple refill or wait for AP regeneration |
| **Inventory Full**        | Servant or CE inventory is full          | Sell or combine items to free space             |
| **Out of Command Spells** | Needed command spells but none available | Wait for command spell regeneration             |

### Configuration Issues

These indicate problems with your Battle Config settings.

| Exit Reason                             | What Happened                                           | Solution                                                   |
| --------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------- |
| **Support Selection Manual**            | Manual support mode requires user interaction           | Set support mode to First, Preferred, or Friend            |
| **Support Selection Preferred Not Set** | Preferred support enabled but no preferences configured | Add servant/CE images in Preferred Support settings        |
| **Skill Command Parse Error**           | Your skill command syntax is invalid                    | Review skill command format in your config                 |
| **Card Priority Parse Error**           | Card priority configuration is invalid                  | Reset card priority to defaults and reconfigure            |
| **Withdraw Disabled**                   | Battle required withdrawal but the option is disabled   | Enable withdrawal in settings, or fix your battle strategy |
| **Preset Quest**                        | Quest has a preset party, preventing party selection    | Use quests without preset parties, or accept the preset    |

### Special Conditions

These exit reasons occur due to game-specific situations.

| Exit Reason                 | What Happened                                    | Server          |
| --------------------------- | ------------------------------------------------ | --------------- |
| **Duplicate CE**            | Your party has duplicate Craft Essences equipped | JP only         |
| **Daily Reset**             | The game's daily reset occurred during farming   | All servers     |
| **Exit on Out of Commands** | No skill commands remain for the current wave    | When configured |
| **Exit on Off Script**      | Script was externally disabled                   | All servers     |

### User Actions

These occur when you or the system interrupts the script.

| Exit Reason    | What Happened                                         |
| -------------- | ----------------------------------------------------- |
| **Abort**      | You manually stopped the script                       |
| **Paused**     | The script is paused (not fully stopped)              |
| **Unexpected** | An unexpected error occurred (check logs for details) |

## Exit State Summary

After every session, FGA provides detailed statistics about your farming run.

### Statistics Display

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ Times Ran: 25                           │
│ Run Limit: 30                           │
│ Times Refilled: 3                       │
│ Refill Limit: 10                        │
│ CE Drop Count: 2                        │
│ Materials: Hearts x5, Bones x47         │
│ Teapots Used: 25                        │
│ Withdraw Count: 0                       │
│ Total Time: 02:15:30                    │
│ Average Time Per Run: 05:25             │
│ Min Turns Per Run: 3                    │
│ Max Turns Per Run: 5                    │
│ Average Turns Per Run: 3.4              │
└─────────────────────────────────────────┘
```

### Understanding Each Statistic

| Statistic                 | Meaning                                  |
| ------------------------- | ---------------------------------------- |
| **Times Ran**             | Total quests completed this session      |
| **Run Limit**             | Your configured maximum (if enabled)     |
| **Times Refilled**        | Number of apple refills used             |
| **Refill Limit**          | Maximum refills allowed                  |
| **CE Drop Count**         | Craft Essences that dropped              |
| **Materials**             | Count of each tracked material collected |
| **Teapots Used**          | Dreamfire/teapots consumed               |
| **Withdraw Count**        | Times you retreated from battle          |
| **Total Time**            | Full session duration                    |
| **Average Time Per Run**  | Mean time to complete one quest          |
| **Min Turns Per Run**     | Fewest turns in any quest                |
| **Max Turns Per Run**     | Most turns in any quest                  |
| **Average Turns Per Run** | Mean turns across all quests             |

## Tips for Best Results

### Avoiding Unwanted Exits

- **Set appropriate apple limits** to avoid depleting your resources accidentally
- **Enable fallback support options** so the script can continue if preferred support isn't found
- **Leave inventory space** before starting long farming sessions
- **Test skill commands** on a few runs before committing to long sessions

### Optimizing Statistics

- **Lower turn counts** indicate more efficient farming setups
- **Consistent turn counts** (min equals max) show reliable wave clearing
- **Lower average time** suggests faster animations or fewer refreshes needed

### Using Auto-Decrement

FGA can automatically reduce your configured limits after each session:

- **Run limits** decrease by runs completed
- **Apple limits** decrease by apples used
- **Material limits** decrease by materials collected
- **CE limits** decrease by CEs dropped

This helps you farm toward a total goal across multiple sessions.

## Troubleshooting Common Exit Reasons

### AP Ran Out

**Problem**: Script stopped because AP depleted and no refill was available.

**Solutions**:

1. Enable apple refill in your server configuration
2. Select which apple types to allow
3. Set a refill limit higher than zero
4. Consider enabling "Wait for AP Regen" for the last run

### Inventory Full

**Problem**: Your servant or CE inventory is completely full.

**Solutions**:

1. Sell unnecessary CEs
2. Use lower-rarity servants for EXP
3. Combine duplicate CEs
4. Expand inventory capacity (if available)

### Support Selection Issues

**Problem**: Script cannot find the configured support servant.

**Solutions**:

1. Verify support images were created with Support Image Maker
2. Check that your friend actually has the servant/CE equipped
3. Enable "Also Check All" to search multiple tabs
4. Configure fallback options for when preferred isn't found
5. Consider using "First" mode for faster but less specific selection

### Skill Command Parse Error

**Problem**: Your skill command syntax contains errors.

**Solutions**:

1. Review the skill command format requirements
2. Check for typos or invalid characters
3. Ensure wave numbers match your quest
4. Verify target letters (A, B, C) are valid

### Unexpected Errors

**Problem**: Something went wrong that FGA didn't anticipate.

**Solutions**:

1. Check the app logs for error details
2. Ensure FGA has all required permissions
3. Verify screen resolution and game settings
4. Try restarting both FGA and FGO
5. Report persistent issues with logs attached
