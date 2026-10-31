---
title: Fine-tune Settings
description: Adjust FGA Preview performance settings. Change click delays, swipe speeds, image matching thresholds, and timing parameters.
tags:
    - app
    - settings
    - fine-tune
    - performance
---

# Fine-tune Settings

## Overview

Fine-tune settings control the timing, the sensitivity, and the performance of the automation engine. You control how fast FGA taps and swipes, how strictly FGA matches an image, and how long FGA waits before it reads the screen.

The default values work for most devices. Change a value when a specific problem occurs, or when you want a faster run on a strong device.

## How to Access

1. Open FGA.
2. Tap **Settings** in the main navigation bar.
3. Tap the **Fine-tune** tab.
4. Tap the **Fine-tune** button.

The fine-tune screen opens beside the settings list. A tab row shows one tab for each group, and a tap on a tab scrolls the list to that group. Tap the back button in the fine-tune screen to return to the settings list.

## Key Features

Each setting shows its name, its current value, its range, and a hint. Use the stepper on the card to change the value. Tap **RESET** on a card to return that card to its default value. FGA disables the reset button while the value is the default value.

FGA groups the settings into seven groups: Support, Similarity, Optimizations, Clicks, Swipes, Long Press, and Wait.

## Support

The Support settings control how FGA scrolls the support list.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Swipes per Update** | 10 | 0-35 | The number of scrolls through the support list before FGA refreshes the list. Use a low value when your preferred support is usually near the top of the list |
| **Max Updates** | 25 | 0-50 | The maximum number of refreshes of the support list. After this number, FGA uses the fallback option of the config. Use a high value when you look for a rare support |

## Similarity

The Similarity settings control how strictly FGA matches an image. A high value gives a strict match. A low value gives a loose match.

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Grayscale Similarity** | 80% | 50-100% | The minimum match for grayscale image matching. Change this value only when a detection fails |
| **Colored Difference** | 95% | 80-100% | The minimum match for colored image matching. A higher value makes the match more strict |
| **MLB Similarity** | 70% | 50-100% | The match for the MLB star of a Craft Essence. Reduce the value a little when FGA does not detect the MLB stars |
| **Stage Counter Similarity** | 85% | 50-100% | The match for the wave counter. Change this value when your skill commands run in the wrong wave |

## Optimizations

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Parallel Command Card Check** | 3 | 1-5 | The number of command cards that FGA reads at the same time. A high value reads the cards faster and uses more of the processor. Reduce the value when the device lags |

## Clicks

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Wait after clicking** | 300ms | 0-2000ms | The wait after each tap, unless FGA taps many times in a series. The game needs time to finish an animation |
| **Click duration** | 50ms | 1-200ms | The time between the touch down and the touch up of a tap. Increase the value when a tap does not register |
| **Multi-Click Interval** | 10ms | 0-50ms | The interval between two taps in a series. FGA taps in a series at the end of a battle, in the friend point summon, and in the lottery script |
| **Lotto Clicks** | 20 | 10-20 | The number of taps for one lottery spin. Reduce the value when the device lags |

## Swipes

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Wait after swiping** | 700ms | 50-3000ms | The wait after all the swipes of a gesture. The game needs time to finish an animation |
| **Swipe duration** | 300ms | 50-1000ms | The time that one swipe takes. A fast swipe scrolls a long distance, and a slow swipe scrolls a short distance |
| **Swipe Multiplier** | 100% | 50-200% | A multiplier for the length of every swipe. Change this value together with the swipe duration |

## Long Press

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Long Press for CE script duration** | 750ms | 500-3000ms | The duration of the long press. FGA uses the long press to drag a Craft Essence on the enhancement screen |
| **Drag duration** | 50ms | 50-1000ms | The duration of the drag. FGA uses the drag to move a Craft Essence on the enhancement screen |
| **Long Press for Lottery script duration** | 10s | 10-30s | The duration of the long press. FGA uses the long press to roll the lottery |

## Wait

| Setting | Default | Range | Description |
| :--- | :--- | :--- | :--- |
| **Skill Delay** | 500ms | 0-2000ms | The wait between a tap on a skill and a tap on the target servant |
| **Wait before Turn** | 500ms | 0-2000ms | The wait after FGA reads the battle screen and before the skill sequence starts. A slow device needs a longer wait |
| **Wait before Cards** | 2000ms | 0-6000ms | The wait between a tap on the attack button and a tap on a face card or an NP. A slow device needs a longer wait |
| **Wait Multiplier** | 100% | 50-200% | A multiplier for every wait and delay. Increase the value to slow the whole script, and decrease the value to speed up the whole script |
| **Wait at Tips screen** | 10s | 5-15s | The wait while the tips screen shows. FGA reads nothing on that screen, so the wait is safe |

## Tips for Best Results

1. **Start from the default values.** The default values work for most devices. Change a value only when a specific problem occurs.
2. **Change one value at a time.** Change one value, run the script, and read the result. You then know which change caused the difference.
3. **Use the Wait Multiplier first.** When the script is too fast for your device, set **Wait Multiplier** to 110% or to 120%. Then change other values only if the problem stays.
4. **Reset a value that you cannot explain.** Tap **RESET** on the card of that value.
5. **Consider the network.** On a slow connection, increase **Wait after swiping** and **Wait after clicking**.

## Troubleshooting

| Problem | Solution |
| :--- | :--- |
| **The script is too fast, or FGA misses taps** | Increase **Wait after clicking**, or increase **Wait Multiplier** for every wait |
| **The support list scrolls in an erratic way** | Increase **Swipe duration** or **Wait after swiping**. The images need time to load |
| **FGA does not find a support** | Increase **Swipes per Update**, or reduce **Grayscale Similarity** a little |
| **FGA taps a wrong card or a wrong skill** | Increase **Skill Delay** or **Wait before Cards**. You can also reduce **Parallel Command Card Check** |
| **The device lags or becomes hot** | Reduce **Parallel Command Card Check** and **Lotto Clicks** |
| **FGA does not detect a button** | Reduce **Grayscale Similarity** a little. Check that no screen filter sits above the game |

## Related Documentation

- [Settings](settings.md)
- [Battle Launcher](../battle-setup/launcher.md)
- [Preferred Support](../battle-setup/support.md)
- [Auto Battle](../in-battle/auto-battle.md)
