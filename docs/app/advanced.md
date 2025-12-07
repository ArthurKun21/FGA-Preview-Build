---
title: Advanced Settings
description: Configure FGA Preview advanced settings. Service automation, game area customization, permissions, and debugging options for power users.
tags:
    - app
    - settings
    - advanced
    - debug
    - permissions
---

# Advanced Settings

## Overview

Advanced Settings give you control over automation behavior, screen detection boundaries, Android permissions, and debugging options. Most users can leave these at their defaults, but they become useful when troubleshooting detection issues or running on devices with unusual screen layouts.

## Key Features

### Stop accessibility service when the script finishes

Enable **Auto stop accessibility service** to shut down the accessibility service automatically after stopping service. This ensures there would be no memory leaks and accessibility service would run fresh the next time you start it.

### Launch the service automatically with the app

Turn on **Auto start service** to begin the overlay and accessibility service as soon as you open the app. This saves a tap and gets you into farming faster.

### Adjust the game area detection mode

FGA needs to know where the game is drawn on screen to tap correctly. Three modes are available:

| Mode    | When to use                                                                          |
| ------- | ------------------------------------------------------------------------------------ |
| Default | Works for most phones in single-app view.                                            |
| Duo     | Use if you run FGO in a split-screen or floating window alongside another app.       |
| Custom  | Manually set pixel offsets (left, right, top, bottom) when detection problems occur. |

Custom offsets can compensate for navigation bars, notches, or display cutouts that shift the game image.

### Use thresholded stage counter

Enable this option if FGA has trouble reading the stage counter on some quests. The thresholded mode applies extra image processing to improve accuracy on low-contrast or stylized screens.

### Ignore play button detection warning

Turn this on to suppress the warning that appears when FGA cannot confidently detect the play button. Only enable it if you understand the risk of mis-taps and have verified detection manually.

### Manage system permissions

FGA requires several Android permissions to function correctly:

- **Notifications** – Required to display progress and completion alerts.
- **Ignore battery optimization** – Keeps the service alive during long farming sessions. Without this, Android may pause FGA to save power.
- **Display over other apps (Overlay)** – Allows the floating control panel to appear on top of the game.

Tap each permission row to open the relevant Android settings screen.

### Dump crash logs for troubleshooting

If FGA crashes or behaves unexpectedly, tap **Dump crash logs** to save diagnostic information. Share the resulting file when reporting bugs so developers can investigate.

### Enable debug mode

**Debug mode** shows extra status messages and logs internal actions. Use it when diagnosing problems; disable it afterward because it can slow down the script and clutter the log.

## Tips for Best Results

- Grant **Ignore battery optimization** if FGA stops during very long runs (over one hour).
- After changing game area offsets, run a short test quest to confirm taps land correctly.
- Leave **Debug mode** off unless actively troubleshooting, since extra logging increases overhead.
- **Accessibility service** must always be turned off after every farming session to ensure it would run without issues the next time you start it.

## Troubleshooting

- **Taps land in the wrong place:** Switch to Custom game area mode and adjust offsets until taps align.
- **Service keeps stopping:** Ensure Ignore battery optimization is enabled and no task-killer app is blocking FGA.
- **Overlay does not appear:** Open **Display over other apps** permission and grant access to FGA Preview.
- **Stage counter reads incorrectly:** Enable thresholded stage counter and re-run the quest.
