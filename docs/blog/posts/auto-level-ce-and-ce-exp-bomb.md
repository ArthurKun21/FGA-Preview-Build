---
title: Auto Level CE and CE EXP Bomb Differences
description: The differences between the Auto Level CE and CE EXP Bomb scripts, and when to use each mode.
categories:
  - Scripts
tags:
  - scripts
  - CE
  - craft essence
  - CE EXP bomb
  - automation
  - enhancement
date:
  created: 2025-12-10
  updated: 2026-11-01
---

# Auto Level CE and CE EXP Bomb Differences

## Overview

FGA Preview has two scripts for Craft Essence (CE) enhancement: **Auto Level CE** and **CE EXP Bomb**. The two modes differ in target selection and stop behavior. This article compares them.

<!-- more -->

### Auto Level CE

The Auto Level CE script enhances one target CE that you selected. The script locks the target CE to protect it. The game selects the fodder CEs with its Auto Select feature. The Auto Select filter uses your **Fodder Rarity** and **Fodder Filter CE Type** settings.

The script stops with `Target CE have reached max level.` when the CE is at maximum level. It can also stop with `No fodder CE found` when no fodder CE matches the filter. Use this mode to level one CE.

### CE EXP Bomb

The CE EXP Bomb script creates CE Bombs. It levels one CE after another in a loop. The enhancement slot must be empty at the start. The script selects each target CE from your inventory.

The target selection uses your **Target Rarity** and **Target Filter CE Type** settings. The script stops when it finds no more fodder or target CEs, or when you stop it. Use this mode to make several leveled CEs.

## How to Use Each Mode

### Using Auto Level CE

1. Open **Enhancement → Craft Essence** in the game.
2. Select the CE that you want to level. The CE appears in the enhancement slot.
3. Open the CE setup screen in FGA Preview. Set the fodder settings.
4. Start the script.
5. The script stops by itself when the CE reaches its maximum level.

### Using CE EXP Bomb

1. Open **Enhancement → Craft Essence** in the game.
2. Leave the enhancement slot empty. Do not select a CE.
3. Open the CE setup screen in FGA Preview. Set the target and fodder settings.
4. Start the script.
5. The script levels one CE after another. You can stop it at any time.

## Summary

| Feature            | Auto Level CE                                     | CE EXP Bomb                                        |
| ------------------ | ------------------------------------------------- | -------------------------------------------------- |
| Target CE          | You select it before you start                    | The script selects it                              |
| Start state        | CE in the slot                                    | Empty slot                                         |
| Stop condition     | `Target CE have reached max level.` or `No fodder CE found` | `No fodder CE found` or `No suitable target CE found` |
| Use Case           | Level one specific CE                             | Make several leveled CEs                           |

## Conclusion

Your goal decides the mode. Use Auto Level CE to level one specific CE. Use CE EXP Bomb to make several leveled CEs. Later, feed the bombs to the CEs that you want to level.

## Related Articles

- [Auto Level CE](../../scripts/auto-level-ce.md)
- [Auto CE EXP Bomb](../../scripts/auto-ce-exp-bomb.md)
