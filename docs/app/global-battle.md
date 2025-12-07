---
title: Global Battle Settings
description: Configure FGA Preview global battle settings. Set up game server detection, story skip, boost items, screenshot options, and exception handling for all battle configurations.
tags:
    - app
    - settings
    - battle
    - game-server
    - screenshots
---

# Global Battle Settings

## Overview

Global Battle Settings apply to every battle configuration you create. They control how FGA detects your game server, handles story scenes, manages resources, captures screenshots, and responds to special in-game events. Adjusting these options once affects all scripts, saving you from repeating the same choices in each config.

## Key Features

### Game server detection

FGA supports multiple Fate/Grand Order servers. The default **Auto-detect** mode uses the accessibility service to identify which FGO app package is running and selects the correct server automatically. You can also lock in a specific server if auto-detection fails.

| Server      | Notes                           |
| ----------- | ------------------------------- |
| Auto-detect | Recommended for most users.     |
| EN          | North American / Global server. |
| EN BFGO     | BetterFGO variant for EN.       |
| JP          | Japanese server.                |
| JP BFGO     | BetterFGO variant for JP.       |
| CN          | Chinese server.                 |
| TW          | Taiwan server.                  |
| KR          | Korean server.                  |

### Skip story scenes

Enable **Story skip** to fast-forward dialogue and cutscenes during quests. This speeds up event farming where story plays between battles.

!!! warning "Story skip limitation"
    The script cannot bypass story segments that require the player to make a choice. If you reach a branching choice, FGA will pause until you select an option manually.

### Boost item selection

Some events include items that boost servant performance. Choose how FGA handles the boost-item popup:

| Option   | Behavior                                                     |
| -------- | ------------------------------------------------------------ |
| Disabled | Do not interact with the popup (leave it for you to handle). |
| Skip     | Dismiss the popup without selecting an item.                 |
| 1, 2, 3  | Automatically select the item in that slot.                  |

### Hide Saint Quartz in refill options

Turn on **Hide SQ in AP resources** to remove Saint Quartz from the list when FGA offers to refill AP. This prevents accidental spending of premium currency during automated farming.

### Treat support servants like your own

Super-buffed support servants can receive so many buffs that the "Support" tag becomes partially hidden. FGA may then mistake them for your own servants. Enable **Treat support like own servants** to work around this edge case and track them correctly.

### Stop on bond level up

Enable **Stop on bond level up** to exit the script when any servant reaches a bond milestone. Use the **Bond level target** selector to choose which level (10–15) triggers the stop. This helps you react to bond rewards or swap out max-bonded servants.

### Exit on manual support selection

If you prefer to pick your friend support yourself, enable **Exit manual support selection**. FGA will stop when it reaches the support list, letting you choose before continuing.

### Enable withdraw option

Turn on **Enable withdraw** if you want FGA to attempt retreating from a battle under certain failure conditions instead of continuing or retrying.

### Stop on Craft Essence drop (Experimental)

Enable **Stop on CE get** to exit the script when a Craft Essence drops after a quest. Useful for farming limited event CEs so you can review or lock them immediately.

### Stop on first-clear rewards

Enable **Stop on first clear rewards** to exit the script when a quest gives first-time completion rewards. You can then collect them manually before restarting the script.

### Screenshot material drops

Turn on **Screenshot material drops** to capture an image of the drop screen at the end of each quest. Screenshots are saved to your storage folder for later review.

### Screenshot drops unmodified

Enable **Screenshot drops unmodified** to save the raw, unprocessed screenshot alongside the annotated version. This is useful if you want the original image without overlays.

### Screenshot bond information

Enable **Screenshot bond** to capture the bond point screen that appears after battle. Combine this with the bond-stop options to keep a visual record of progress.

## Tips for Best Results

- Use **Auto-detect** for game server unless you encounter detection problems, then switch to a manual selection.
- Enable **Hide SQ in AP resources** to avoid accidentally spending premium currency.
- Set a **Bond level target** and enable **Stop on bond level up** if you are farming bond points and want to react at certain milestones.

## Troubleshooting

- **Wrong server detected:** Force-select the correct server manually until auto-detect is fixed.
- **Story skip does not work:** Check if the quest has mandatory dialogue choices; FGA cannot auto-select those.
- **Screenshots not saved:** Verify that the storage folder is set correctly in Storage Settings and that FGA has write permission.
- **Bond stop triggers too early or not at all:** Sometimes the optical character recognition may misread bond levels; review screenshots to confirm accuracy.
