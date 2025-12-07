---
title: Play Button Detection
description: FGA Preview play button detection and placement tracking. Ensure optimal play button position for reliable image matching during automation.
tags:
  - scripts
  - play button
  - detection
  - troubleshooting
  - fgo automation
  - setup
---

# Play Button Detection

## Overview

FGA Preview uses a floating play button to start and control automation scripts. The position of this play button on your screen matters because it can accidentally cover important areas of the game that FGA needs to see for accurate image matching.

The **Play Button Detection** feature automatically checks if your play button is in a safe location when you start any script. If the button is in a problematic position, FGA will warn you before proceeding.

## Why Play Button Position Matters

FGA works by taking screenshots of your game and matching specific images to determine what's happening on screen. If the play button covers any of these important regions, the script may:

- Fail to detect buttons or menus correctly
- Miss important game elements during automation
- Behave unexpectedly or stop working

**The recommended position is the bottom-left corner of the screen**, where it won't interfere with most game interfaces.

![Play Button Placement](../assets/other-scripts/play-button-placement.png)

## Key Features

### Automatic Position Check

FGA automatically verifies the play button position every time you start a script. The check happens before the script begins running, so you can correct any issues immediately.

### Warning System

When the play button is not in the optimal position, FGA displays a warning dialog:

![Play Button Error](../assets/other-scripts/play-button-error.png)

From this dialog, you can:

- **Move the play button** to the bottom-left corner and try again
- **Ignore the warning** if you understand the risks

### Ignore Future Warnings

If you prefer to keep the play button in a non-standard location, you can enable the **"Ignore further warning about play button's location"** option. This setting tells FGA to skip the position check for all future script runs.

You can also enable this setting permanently in **Settings > Advanced > Ignore warning about play button's location**.

## How to Move the Play Button

1. **Hold** the FGA play button (the floating circle on your screen)
2. **Drag** it to the bottom-left corner of your screen
3. **Release** to place it in the new position
4. Start your script again

## Tips for Best Results

1. **Place the button in the bottom-left corner** for maximum compatibility with all FGA features
2. **Keep the button near the screen edge** so it doesn't overlap with game menus
3. **Test after moving** to ensure FGA can still detect game elements correctly
4. **Avoid the center and right side** of the screen, as these areas contain important game information

## Troubleshooting

### FGA keeps warning me about the play button position

**Solution**: Move the play button to the bottom-left corner of your screen. This is the safest position that works with all features.

### I moved the button but FGA still shows the warning

**Possible causes**:

- The button may not be far enough into the bottom-left region
- Try moving it closer to the corner

**Check points**:

- The button should be in the **left half** of the screen (horizontally)
- The button should be in the **lower 3/8** of the screen (vertically)

### Scripts work fine even though the button isn't in the bottom-left

Some scripts may work regardless of button position, but others (especially those that interact with areas your button covers) may fail. For consistent results, keeping the button in the recommended position is best practice.

### I enabled "Ignore warning" but now want to see warnings again

1. Go to **Settings > Advanced**
2. Find **"Ignore warning about play button's location"**
3. Toggle it **off** to re-enable position warnings
