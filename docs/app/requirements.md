---
title: Requirements
description: System requirements for FGA Preview - Android version requirements, app permissions, accessibility service, overlay permission, and media projection setup.
tags:
  - requirements
  - setup
  - permissions
  - Android
---

# Requirements

## Overview

Before using FGA Preview, your device needs to meet a few basic requirements and you'll need to grant certain permissions. This page explains what's needed and why, so you can get the app running smoothly.

## Key Features

### Android version

FGA Preview requires **Android 8.0 (Oreo) or newer**. This is because the app uses special gestures like long-press that are only available on Android 8.0 and above.

!!! tip "How to check your Android version"
    Go to **Settings → About phone → Android version** on your device to see which version you have.

### Accessibility Service

The Accessibility Service lets FGA Preview interact with your screen on your behalf. Without it, the app cannot tap buttons, swipe the screen, or read what's happening in Fate/Grand Order.

| What it does          | Why it's needed                                        |
| --------------------- | ------------------------------------------------------ |
| Tap and swipe         | Performs in-game actions like selecting cards          |
| Read screen content   | Detects game state to know when to act                 |

!!! note
    Android will show a warning when enabling this permission. This is normal for all automation apps.

### Overlay Permission

The Overlay Permission allows FGA Preview to show controls on top of other apps. This is how the floating **Play button** and pop-up dialogs appear while you're in the game.

| What it does           | Why it's needed                                       |
| ---------------------- | ----------------------------------------------------- |
| Show Play button       | Lets you start and stop automation without switching apps |
| Display dialogs        | Shows exit confirmations and status messages          |

### Media Projection

Media Projection gives FGA Preview the ability to see what's on your screen. The app uses this to take quick screenshots, then analyzes them to understand what's happening in the game.

| What it does           | Why it's needed                                       |
| ---------------------- | ----------------------------------------------------- |
| Capture screen images  | Identifies cards, buttons, and game states            |
| Enable image matching  | Matches screenshots against known patterns            |

!!! info
    A notification will appear while screen capture is active. This is required by Android and cannot be hidden.

### Disable Battery Optimization

Some Android devices aggressively stop apps running in the background to save battery. Disabling battery optimization for FGA Preview ensures it keeps running during long farming sessions.

| What it does               | Why it's needed                                   |
| -------------------------- | ------------------------------------------------- |
| Prevents app from sleeping | Keeps automation running during extended sessions |
| Avoids unexpected stops    | Reduces interruptions from the system             |

## Tips for Best Results

- **Grant all permissions upfront.** The app will guide you through each one, but enabling them all at once avoids repeated prompts.
- **Check your Android version first.** If you're on Android 7.1 or older, FGA Preview won't work—consider updating your device or using a different phone.
- **Keep battery optimization disabled.** Even if the app works initially, the system may kill it during long runs if optimization is enabled.
- **Restart your device after setup.** A fresh restart can help ensure all permissions are applied correctly.

## Troubleshooting

| Problem                                      | Solution                                                                                       |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| App says Accessibility Service is off        | Go to **Settings → Accessibility → FGA Preview** and toggle it on                              |
| Play button doesn't appear                   | Check that Overlay Permission is enabled in **Settings → Apps → FGA Preview → Display over other apps** |
| Screen capture not working                   | Re-grant Media Projection by restarting the app and tapping **Allow** when prompted            |
| Automation stops after a few minutes         | Disable battery optimization for FGA Preview in your device's battery settings                 |
| Can't find the permission settings           | Use your device's search function in Settings and look for "FGA" or the specific permission name |
