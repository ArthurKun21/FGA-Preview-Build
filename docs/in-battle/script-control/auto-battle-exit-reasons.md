---
title: Exit Reasons and Session Statistics
description: Understand why the FGA Battle Script stops or pauses, and how to read the session statistics.
tags:
    - battle
    - exit
    - statistics
    - troubleshooting
---

# Exit Reasons and Session Statistics

This page explains why your farming session ended, and how to read the session statistics.

## Overview

When the Battle Script stops, FGA shows a notification with the exit reason and the session statistics. Read the reason to find the fix. Read the statistics to improve your farming setup.

Some conditions pause the script instead of ending it. See [Pauses and the Pause Screen](#pauses-and-the-pause-screen).

## Exit Reason Categories

### Normal Completion

These exit reasons mean the script completed your farming goal.

| Exit Reason             | What Happened                                        |
| ----------------------- | ---------------------------------------------------- |
| **Limit Runs**          | You completed the configured number of runs          |
| **Limit CEs**           | You collected the configured number of CE drops      |
| **Limit Materials**     | You collected the configured materials               |
| **CE Get**              | A Craft Essence dropped (you enabled stop on CE)     |
| **First Clear Rewards** | You received the first-time completion rewards       |
| **Bond Level Reached**  | A servant reached your target bond level             |
| **Stop After This Run** | You requested to stop after the current run finished |

### Resource Depletion

The script cannot continue because a resource ran out.

| Exit Reason               | What Happened                            | Solution                                        |
| ------------------------- | ---------------------------------------- | ----------------------------------------------- |
| **AP Ran Out**            | No AP remaining and no refill available  | Enable apple refill or wait for AP regeneration |
| **Inventory Full**        | Servant or CE inventory is full          | Sell or combine items to free space             |
| **Out of Command Spells** | Needed command spells but none available | Wait for command spell regeneration             |

### Configuration Issues

Your Battle Config settings caused the stop.

| Exit Reason                             | What Happened                                            | Solution                                                   |
| --------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| **Support Selection Preferred Not Set** | Preferred support enabled but no preferences configured  | Add servant/CE images in Preferred Support settings        |
| **Skill Command Parse Error**           | Your skill command syntax is invalid                     | Review skill command format in your config                 |
| **Card Priority Parse Error**           | Card priority configuration is invalid                   | Reset card priority to defaults and reconfigure            |
| **Missing Support Image**               | Image for a preferred servant, Craft Essence, or friend missing | Recreate the image or update the atlas data          |
| **Withdraw Disabled**                   | You disabled withdrawal, but the battle needed it        | Enable withdrawal in settings, or fix your battle strategy |
| **Preset Quest**                        | Quest has a preset party, preventing party selection     | Use quests without preset parties, or accept the preset    |

!!! note "Manual support mode"
    Manual support selection does not exit the script. The script pauses and waits until you select a support. See [Pauses and the Pause Screen](#pauses-and-the-pause-screen).

### Special Conditions

Game-specific situations caused the stop.

| Exit Reason                 | What Happened                                       | Server          |
| --------------------------- | --------------------------------------------------- | --------------- |
| **Duplicate CE**            | Your party has duplicate Craft Essences equipped    | JP only         |
| **Daily Reset**             | The game daily reset happened during farming        | All servers     |
| **Exit on Out of Commands** | No skill commands remain for the current wave       | When configured |
| **Exit on Off Script**      | You or another app turned off the script            | All servers     |

### User Actions

You or the system stopped the script.

| Exit Reason    | What Happened                                         |
| -------------- | ----------------------------------------------------- |
| **Abort**      | You manually stopped the script                       |
| **Paused**     | The script paused and waits for you to resume         |
| **Unexpected** | An unexpected error occurred (check logs for details) |

## Pauses and the Pause Screen

A pause is not an exit. The script suspends in place. It continues at the same point when you resume. FGA shows a notification with the pause reason.

The script pauses when:

- You request a pause
- Manual support mode waits for you to select a support

The pause screen shows the session statistics. It also shows the remaining skill commands for each wave and turn. The script removes each command from the list after it runs.

## Exit State Summary

After every session, FGA shows detailed statistics about your farming run.

### Statistics Box

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
│ Support Picks: Skadi x25, Waver x3      │
│ Teapots Used: 25                        │
│ Storm Pods Used: 5 (if used)            │
│ Withdraw Count: 0                       │
│ Total Time: 02:15:30                    │
│ Average Time Per Run: 05:25             │
│ Min Turns Per Run: 3                    │
│ Max Turns Per Run: 5                    │
│ Average Turns Per Run: 3.4              │
└─────────────────────────────────────────┘
```

While the script is paused, the pause screen shows the same statistics, plus the remaining skill commands.

### Understanding Each Statistic

| Statistic                 | Meaning                                                |
| ------------------------- | ------------------------------------------------------ |
| **Times Ran**             | Total quests completed this session                    |
| **Run Limit**             | Your configured maximum (if enabled)                   |
| **Times Refilled**        | Number of apple refills used                           |
| **Refill Limit**          | Maximum refills allowed                                |
| **CE Drop Count**         | Craft Essences that dropped                            |
| **Materials**             | Count of each tracked material collected               |
| **Support Picks**         | Preferred supports the script picked, with counts      |
| **Teapots Used**          | Stargazer's Teapots consumed                           |
| **Storm Pods Used**       | Ordeal Call storm pods consumed (shown only when used) |
| **Withdraw Count**        | Times you retreated from battle                        |
| **Total Time**            | Full session duration                                  |
| **Average Time Per Run**  | Mean time to complete one quest                        |
| **Min Turns Per Run**     | Fewest turns in any quest                              |
| **Max Turns Per Run**     | Most turns in any quest                                |
| **Average Turns Per Run** | Mean turns across all quests                           |

## Usage Records

The script writes usage records to the selected Battle Config. This happens after an exit with at least one completed run:

- Last usage date (UTC)
- Total run count
- Total usage time

Use these records to see which configs you use most.

## Tips for Best Results

### Avoid Unwanted Exits

- **Set appropriate apple limits** to avoid accidental resource depletion
- **Enable fallback support options** so the script can continue when the preferred support is not found
- **Leave inventory space** before you start long farming sessions
- **Test skill commands** on a few runs before long sessions

### Read the Statistics

- **Lower turn counts** mean a more efficient farming setup
- **Consistent turn counts** (min equals max) show reliable wave clearing
- **Lower average time** means faster animations or fewer support refreshes

### Auto-Decrement

FGA reduces your configured limits automatically after each session:

- **Run limits** decrease by the runs completed
- **Apple limits** decrease by the apples used
- **Material limits** decrease by the materials collected
- **CE limits** decrease by the CEs dropped

This helps you farm toward a total goal across multiple sessions.

## Troubleshooting Common Exit Reasons

### AP Ran Out

**Problem**: The script stopped because AP ran out and no refill was available.

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

### Support Selection Preferred Not Set

**Problem**: The script cannot find the configured support servant.

**Solutions**:

1. Check that you created the support images with Support Image Maker
2. Check that your friend actually has the servant/CE equipped
3. Enable "Also Check All" to search multiple tabs
4. Configure fallback options for when the preferred support is not found
5. Consider using "First" mode for faster but less specific selection

### Missing Support Image

**Problem**: The image file for a preferred servant, Craft Essence, or friend is missing.

**Solutions**:

1. Recreate the image with Support Image Maker
2. Update the atlas data, then re-select the servant or Craft Essence in your preferred support settings
3. Remove entries for supports that no longer exist

### Skill Command Parse Error

**Problem**: Your skill command syntax contains errors.

**Solutions**:

1. Review the skill command format requirements
2. Check for typos or invalid characters
3. Make sure the wave numbers match your quest
4. Check that target letters (A, B, C) are valid

### Unexpected Errors

**Problem**: Something went wrong that FGA did not expect.

**Solutions**:

1. Check the app logs for error details
2. Make sure FGA has all required permissions
3. Check the screen resolution and the game settings
4. Restart both FGA and FGO
5. Report persistent issues with logs attached
