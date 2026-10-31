---
title: Settings
description: Overview of the FGA Preview settings screen. Learn the section tabs, the settings search, dialog rows, and the rows that show only on Android.
tags:
    - app
    - settings
    - search
    - sections
---

# Settings

## Overview

Settings is one destination of the main navigation bar. The other destinations are Home, Library, and History. Tap **Settings** to open the settings screen.

The settings screen shows one scrollable list. The list holds every section in a fixed order. A tab row stays above the list. Tap a tab to scroll to that section. The selected tab follows the list when you scroll.

| Order | Section       | Contents                                                        |
| ----- | ------------- | --------------------------------------------------------------- |
| 1     | [Appearance](appearance.md)   | Theme, app language, and date and time formats                 |
| 2     | [Battle](global-battle.md)    | Game server, story skip, boost item, and battle exit exceptions |
| 3     | [Library](library.md)         | Server tabs and config sorting                                 |
| 4     | [Storage](storage.md)         | Storage location, support database reset, and backup            |
| 5     | [GitHub Backup](github-backup.md) | Battle config backup to a GitHub repository                |
| 6     | [Fine-tune](fine-tune.md)     | A button that opens the Fine-tune screen                        |
| 7     | [Advanced](advanced.md)       | Game area, permissions, and debugging                           |

On a wide window the list shows two columns. Section headers and grouped rows always span the full width.

!!! note "Tap and click"
    This guide uses "tap" for a touch action. On the desktop app, use a mouse click.

## Key Features

### Search settings

The search field stays at the top of the screen. Type any part of a setting name to filter the list. The results show the row name and the section name. Tap a result to jump to that row.

The search follows the app language. The search matches the names that you see on the screen.

Tap **Clear** to remove the text and return to the full list. If no row matches, the screen shows "No settings found".

### Open a dialog

Some rows open a list dialog. These rows are:

- **App Language** in the Appearance section
- **Date-Time Format** in the Appearance section
- **Game Server** in the Battle section. This row shows only on Android

Tap the row to open the dialog. Tap an item in the dialog to select it. FGA saves the selection and closes the dialog. Tap **Dismiss** or the back button to close the dialog without a change.

### Open another pane

Three rows open a pane in addition to the settings list:

- **Fine-tune** in the Fine-tune section. The Fine-tune screen opens beside the settings list.
- **Library Tabs** in the Library section. The pane opens above the settings content.
- **Configure GitHub** in the GitHub Backup section. The pane opens above the settings content.

Tap the back button in the pane to return to the settings list.

### Save each value at once

Every switch, selector, and row writes its value at once. The settings screen has no Save button. Leave the screen when you finish.

### Read the version and copy debug information

The last row of the settings list is **Version**. The row shows the build type, the commit count, and the commit hash. The build type is Dev, Preview, or Alpha.

Tap the row to copy the debug information to the clipboard. The information holds the device details and the build details. Paste the information into a bug report.

### Rows that show only on Android

FGA Preview also runs on the desktop. A few rows apply only to Android, and FGA hides them on the desktop:

| Row                          | Section   |
| ---------------------------- | --------- |
| Game Server                  | Battle    |
| Auto stop accessibility service on script service stop | Advanced |
| Auto-start service           | Advanced  |
| Ignore warning about play button's location | Advanced |
| Permissions group            | Advanced  |

## Tips for Best Results

- Use the search field when you cannot remember the section of a setting.
- Use the tabs to jump between sections. A scroll also changes the selected tab.
- Read the **Version** row before you report a bug. The value identifies your build.

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| A setting does not apply | Reload the script that uses the setting. Some values apply when a script starts. |
| The search finds nothing | Type fewer letters. The search matches the row names in the current app language. |
| A row is missing | The row can show only on Android. Run FGA on an Android device to see it. |
| The settings list scrolls to a wrong row | Tap the tab of the section again. The tab scrolls the list to the section header. |

## Related Documentation

- [Requirements](requirements.md)
- [Appearance Settings](appearance.md)
- [Global Battle Settings](global-battle.md)
- [Library](library.md)
- [Storage Settings](storage.md)
- [GitHub Backup](github-backup.md)
- [Fine-tune Settings](fine-tune.md)
- [Advanced Settings](advanced.md)
