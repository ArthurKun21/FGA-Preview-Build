---
title: Advanced Settings
description: Configure FGA Preview advanced settings. Control service automation, the game area, Android permissions, and debugging options.
tags:
    - app
    - settings
    - advanced
    - debug
    - permissions
---

# Advanced Settings

## Overview

Advanced Settings control the automation service, the game area, the Android permissions, and the debugging options.

Most users can keep the default values. Change a value when a detection problem occurs, or when the device has an unusual screen layout.

The Advanced section holds the service options, the game area options, a Permissions group, and a Debugging group. Three rows and the Permissions group show only on Android.

## Key Features

### Stop the accessibility service with the script service

Enable **Auto stop accessibility service on script service stop** to stop the accessibility service each time the script service stops. The next run then starts with a fresh service, and the service runs without problems.

!!! note "Android only"
    This row shows only on Android.

### Start the service with the app

Enable **Auto-start service** to start the overlay service and the accessibility service when you open FGA. You then start a run with one tap.

!!! note "Android only"
    This row shows only on Android.

### Select the game area mode

FGA must know where the game is drawn on the screen. It uses the game area to put each tap in the correct place.

| Mode     | When to use                                                              |
| -------- | ------------------------------------------------------------------------ |
| Default  | Works for most phones in single-app view                                  |
| Surface Duo | Use this mode when you run FGO in a split screen or a floating window |
| Custom   | Set the four offsets by hand when the detection fails                     |

Select **Custom** to show four steppers. Each stepper sets an offset in pixels, from 0 to 999:

| Stepper | Edge                          |
| ------- | ----------------------------- |
| Left    | The left edge of the game area  |
| Right   | The right edge of the game area |
| Top     | The top edge of the game area   |
| Bottom  | The bottom edge of the game area |

Use the offsets to compensate for a navigation bar, a notch, or a screen cutout. Those parts of the screen move the game image.

### Use the thresholded stage counter

Enable **Thresholded stage counter detection** when FGA reads the stage counter wrong. The option adds image processing, and it improves the read on screens with low contrast or an unusual style.

### Ignore the play button warning

FGA shows a warning when it cannot find the play button with confidence. Enable **Ignore warning about play button's location** to stop the warning.

!!! warning "Enable this option with care"
    With the warning off, FGA can tap a wrong place on the screen. Check the play button detection yourself before you use this option.

!!! note "Android only"
    This row shows only on Android.

## Permissions

The Permissions group holds three rows. Tap a row to open the related screen in the Android settings.

| Row | Why FGA needs it |
| --- | ---------------- |
| Notifications | To show the progress of a run and the alerts that report the end of a run |
| Battery Optimization | To keep the service alive during a long run. Android can otherwise stop FGA to save power. The permission gives FGA unrestricted battery use |
| Display over other apps | To show the floating control panel above the game |

!!! note "Android only"
    The Permissions group shows only on Android.

## Debugging

### Share crash logs

Tap **Share crash logs** to save the error logs to a file. Add the file to a bug report so that the developers can investigate the problem.

### Enable debug mode

Enable **Debug mode** to highlight the regions that FGA matches. Use this option when you diagnose a problem, because the extra work can slow the script.

## Tips for Best Results

- Grant the **Battery Optimization** permission when FGA stops during a run that lasts more than one hour. The permission gives FGA unrestricted battery use.
- Run a short test quest after you change a game area offset. The test shows whether each tap lands in the correct place.
- Keep **Debug mode** off when you do not diagnose a problem.
- Grant **Notifications** so that you see the progress of a backup, a restore, and a GitHub sync.

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| Taps land in the wrong place | Select the **Custom** game area mode. Change the offsets until the taps align with the game. |
| The service stops during a run | Grant **Battery Optimization**. Check that no task manager stops FGA. |
| The overlay does not show | Open **Display over other apps**. Grant the permission to FGA. |
| The stage counter reads wrong | Enable **Thresholded stage counter detection**. Then run the quest again. |
| FGA taps a wrong place after you disable the play button warning | Disable **Ignore warning about play button's location**. Then check the play button detection yourself. |
| The script is slow or taps in the wrong place | Disable **Debug mode**. The extra image processing slows the script. |

## Related Documentation

- [Settings](settings.md)
- [Requirements](requirements.md)
- [Storage Settings](storage.md)
