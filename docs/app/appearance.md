---
title: Appearance Settings
description: Customize FGA Preview appearance settings. Set the theme, the app language, and the date and time formats of the app interface.
tags:
    - app
    - settings
    - appearance
    - theme
    - language
    - date-time
---

# Appearance Settings

## Overview

Appearance Settings control how FGA looks and how FGA shows dates and times. The options are cosmetic, and they do not change the behavior of a script.

The Appearance section holds two settings and a Datetime group. The group holds three settings.

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
- Select a date format that matches how you read dates. The config timestamps in the Library are then easier to read.
- Enable **Use relative time** when you sort configs by "Recently Used". You then see how long ago each config ran.

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| The language change does not apply | FGA reloads the screen at once. If the old language stays, close FGA and open it again. |
| The theme flickers or looks wrong | Close FGA and open it again to reload the theme. |
| The date format example is wrong | Check the locale of the device. Then select the format again. |
| The date and time format does not apply everywhere | Some screens show a relative time. Enable or disable **Use relative time** to switch between the two styles. |

## Related Documentation

- [Settings](settings.md)
- [Global Battle Settings](global-battle.md)
- [GitHub Backup](github-backup.md)
