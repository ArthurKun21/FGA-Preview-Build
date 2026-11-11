---
title: Appearance Settings
description: Customize FGA Preview appearance settings. Set the theme, the app language, the dim timeout of the script runner buttons, and the date and time formats of the app interface.
tags:
    - app
    - settings
    - appearance
    - theme
    - language
    - date-time
    - overlay
---

# Appearance Settings

## Overview

Appearance Settings control how FGA looks, when the script runner buttons dim, and how FGA shows dates and times. The options are cosmetic, and they do not change the behavior of a script.

The Appearance section holds three settings and a Datetime group. The group holds three settings.

## Key Features

### Select the app language

Tap **App Language** to open a list dialog. Tap a language to select it. FGA applies the language to all menus, labels, and messages.

| Language                       | Code  |
| ------------------------------ | ----- |
| English                        | en    |
| Japanese                       | ja    |
| Korean                         | ko    |
| Chinese (Simplified)           | zh-CN |
| Chinese (Traditional / Taiwan) | zh-TW |
| Vietnamese                     | vi    |

### Select the theme

Tap the **Theme** row to open a list of three options:

| Option | Description                                                    |
| ------ | -------------------------------------------------------------- |
| Light  | Light backgrounds with dark text                               |
| Dark   | Dark backgrounds with light text                               |
| Auto   | Follows the dark-mode setting of the device                     |

### Set the overlay dim timeout

The script runner shows floating buttons over the game. When you do not touch the buttons for some time, they dim to half opacity. **Overlay dim timeout** sets how long the buttons stay fully visible before they dim.

This setting shows only on Android. The floating buttons do not exist on the desktop app.

The default is 20 seconds. You can set a value from 15 to 180 seconds.

| Control                 | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| Slider and +/- buttons  | Set the timeout. The value applies when you release the control |
| RESET                   | Restores the default of 20 seconds                              |

The timeout applies while the runner is idle or paused. While a script runs, the buttons stay fully visible. If you change the timeout while the buttons are dim, they become fully visible again. The new timeout then applies at once.

### Use relative time

Enable **Use relative time** to show a time such as "5 minutes ago" instead of an exact date. Recent activity is then easier to read.

### Use the 24-hour format

Enable **Use 24-hour format** to show a time such as 14:30 instead of 2:30 PM.

### Select a date and time format

Tap **Date-Time Format** to open a list dialog. The row under the title shows a live example of each format. Tap a format to select it.

| Option        | Example            |
| ------------- | ------------------ |
| Default       | Uses the locale of the device |
| MM/dd/yy      | 12/06/25           |
| dd/MM/yy      | 06/12/25           |
| yyyy-MM-dd    | 2025-12-06         |
| dd MMM yyyy   | 06 Dec 2025        |
| MMM dd, yyyy  | Dec 06, 2025       |

The **Last sync** row in the GitHub Backup section also uses this format. See [GitHub Backup](github-backup.md).

## Tips for Best Results

- Use the **Auto** theme to follow the dark-mode schedule of the device.
- Set a longer **Overlay dim timeout** when the buttons dim too soon while the runner is idle.
- Select a date format that matches how you read dates. The config timestamps in the Library are then easier to read.
- Enable **Use relative time** when you sort configs by "Recently Used". You then see how long ago each config ran.

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| The language change does not apply | FGA reloads the screen at once. If the old language stays, close FGA and open it again. |
| The theme flickers or looks wrong | Close FGA and open it again to reload the theme. |
| The **Overlay dim timeout** card does not show | The card shows only on Android. The floating buttons do not exist on the desktop app. |
| The date format example is wrong | Check the locale of the device. Then select the format again. |
| The date and time format does not apply everywhere | Some screens show a relative time. Enable or disable **Use relative time** to switch between the two styles. |

## Related Documentation

- [Settings](settings.md)
- [Global Battle Settings](global-battle.md)
- [GitHub Backup](github-backup.md)
