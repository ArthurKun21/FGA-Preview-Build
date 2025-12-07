---
title: Fine Tune Settings
description: Fine tune FGA Preview performance settings. Adjust click delays, swipe speeds, image matching thresholds, and timing parameters.
tags:
  - app
  - settings
  - fine-tune
  - performance
---

# Fine Tune Settings

Adjust timing, sensitivity, and performance parameters to optimize FGA on your device.

## Overview

The Fine Tune screen provides advanced control over FGA's automation behavior. These settings allow you to customize how fast FGA interacts with the game, how strictly it matches images, and how it handles scrolling. While the default settings work for most users, fine-tuning can help resolve specific issues or improve efficiency on different devices.

## Key Features

- **Timing Control**: Adjust specific delays for clicks, swipes, and skills to match your device's speed.
- **Detection Sensitivity**: Customize similarity thresholds for image recognition.
- **Scroll Behavior**: Modify how FGA searches through lists.
- **Performance Optimization**: Balance CPU usage and detection speed.

## How to Access

1. Open the FGA app.
2. Tap **Fine Tune** (usually represented by a sliders icon or in the main menu).

---

## Support Settings

Control how FGA searches through the support list.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Swipes Per Update** | 10 | 0-35 | Number of times FGA swipes down the support list before refreshing. **Tip**: Use lower values if your preferred support is usually near the top. |
| **Max Updates** | 25 | 0-35 | Maximum number of times FGA will refresh the support list before giving up. **Tip**: Set higher if you are looking for a rare support setup. |

## Similarity Settings

Control how strictly FGA matches images.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Minimum Similarity** | 80% | 50-100% | How closely an image must match for FGA to consider it a match. **Tip**: Decrease if FGA fails to recognize buttons; increase if it clicks the wrong things. |
| **MLB Similarity** | 70% | 50-100% | Threshold for detecting Max Limit Broken (MLB) Craft Essences. **Tip**: Lower slightly if FGA misses MLB stars due to screen brightness or rendering. |
| **Stage Counter Similarity** | 85% | 50-100% | Threshold for detecting the wave/stage counter during battle. **Tip**: Adjust if FGA misidentifies the current wave. |

## Optimization Settings

Performance tuning options for the automation engine.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Parallel Card Check** | 3 | 1-5 | Number of command cards to analyze simultaneously. **Tip**: Higher values are faster but use more CPU. Lower this if your device overheats or lags. |

## Click Settings

Control tap and click behavior.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Wait After Clicking** | 300ms | 0-2000ms | Time to wait after each click before proceeding. **Tip**: Increase if the game has slow animations or network lag. |
| **Click Duration** | 50ms | 1-200ms | How long each tap is held down. **Tip**: Increase if clicks are not registering on your device. |
| **Click Delay** | 10ms | 0-50ms | Delay between the start of a click action and the actual touch event. |
| **Lotto Clicks** | 20 | 10-20 | Number of clicks per lottery spin action. |

## Swipe Settings

Control swipe and scroll behavior.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Wait After Swiping** | 700ms | 50-3000ms | Time to wait after each swipe before proceeding. **Tip**: Increase if scrolling happens before images fully load. |
| **Swipe Duration** | 300ms | 50-1000ms | How long each swipe gesture takes to complete. |
| **Swipe Multiplier** | 100% | 50-200% | Multiplies the distance of every swipe. **Tip**: Adjust if FGA scrolls past too many items or not enough. |

## Drag Settings

Control drag-and-drop behavior (used for card selection and adjustments).

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Long Press Duration** | 750ms | 500-3000ms | Time to hold before a press matches a "long press". |
| **Drag Duration** | 50ms | 50-1000ms | How long drag gestures take to complete. |

## Wait Settings

Control delays during battle and general script execution.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Skill Delay** | 500ms | 0-2000ms | Wait time after using a skill before the next action. **Tip**: Increase if skills are skipped or the script moves too fast during skill chains. |
| **Wait Before Turn** | 500ms | 0-2000ms | Wait time at the start of each turn (allows animations to finish). |
| **Wait Before Cards** | 2000ms | 0-6000ms | Wait time before reading command cards. **Tip**: Critical for card detection. Increase if cards are misread or the attack screen loads slowly. |
| **Wait Multiplier** | 100% | 50-200% | Multiplies all wait times globally. **Tip**: Use this (>100%) to quickly slow down the entire script without changing individual settings. |
| **Wait at Tips Screen** | 10s | 5-15s | How long to wait when the loading tips screen appears. |

---

## Tips for Best Results

1. **Start with defaults**: The default values are tuned for the majority of devices. Only change them if you encounter a specific problem.
2. **Change one thing at a time**: Modify one setting, test the script, and observe the result. This makes it easier to tell what worked.
3. **Use the Wait Multiplier**: If the script is generally too fast for your device, try setting **Wait Multiplier** to 110% or 120% first.
4. **Reset if stuck**: Use the **RESET** button next to any setting to return it to the default value if you mess up.
5. **Network affects timing**: If you are on a slow connection, you might need to increase **Wait After Swiping** and **Wait After Clicking**.

## Troubleshooting

| Problem | Solution |
| :--- | :--- |
| **Script running too fast / Clicks ignored** | Increase **Wait After Clicking** or increase **Wait Multiplier** globally. |
| **Support list scrolling is erratic** | Increase **Swipe Duration** or **Wait After Swiping** (if images take time to load). |
| **FGA doesn't see Supports** | Increase **Swipes Per Update** or slightly decrease **Minimum Similarity** (e.g., to 75%). |
| **FGA clicks wrong cards/skills** | Increase **Skill Delay**, **Wait Before Cards**, or adjust **Parallel Card Check**. |
| **Buttons are not detected** | Decrease **Minimum Similarity** and ensure no overlays (like blue light filters) are interfering. |

## Related Documentation

- [Battle Launcher](../battle-setup/launcher.md)
- [Preferred Support](../battle-setup/support.md)
- [Auto Battle](../in-battle/auto-battle.md)
