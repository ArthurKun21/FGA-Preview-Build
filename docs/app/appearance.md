---
title: Appearance Settings
description: Customize FGA Preview appearance settings. Configure theme (light/dark/system), language preferences, and date/time formatting for the app interface.
tags:
    - app
    - settings
    - theme
    - language
    - date-time
---

# Appearance Settings

## Overview

Appearance Settings control how the app looks and displays information. You can pick a color theme, change the interface language, and choose how dates and times are formatted. These options are cosmetic and do not affect automation behavior.

## Key Features

### Choose your preferred language

Select the language for all menus, labels, and messages in the app. Available languages:

| Language                       | Code  |
| ------------------------------ | ----- |
| English                        | en    |
| Japanese                       | ja    |
| Korean                         | ko    |
| Chinese (Simplified)           | zh-CN |
| Chinese (Traditional / Taiwan) | zh-TW |
| Vietnamese                     | vi    |

The app restarts briefly after changing the language.

### Set the color theme

Pick a theme that matches your preference or environment:

| Theme  | Description                                                    |
| ------ | -------------------------------------------------------------- |
| Light  | Bright backgrounds with dark text.                             |
| Dark   | Dark backgrounds with light text, easier on the eyes at night. |
| System | Follows your device's system-wide dark-mode setting.           |

### Show relative time

Enable **Use relative time** to display timestamps like "5 minutes ago" or "yesterday" instead of exact dates. This makes recent activity easier to scan at a glance.

### Use 24-hour clock format

Toggle **24-hour format** on to display times such as 14:30 instead of 2:30 PM. This is common in military and many international contexts.

### Select a date format

Pick a date style that matches your region:

| Format       | Example            |
| ------------ | ------------------ |
| Default      | Uses device locale |
| MM/dd/yy     | 12/06/25           |
| dd/MM/yy     | 06/12/25           |
| yyyy-MM-dd   | 2025-12-06         |
| dd MMM yyyy  | 06 Dec 2025        |
| MMM dd, yyyy | Dec 06, 2025       |

The preview in the settings shows a live example of your chosen format.

## Tips for Best Results

- Use **System** theme to automatically switch between light and dark based on your phone's schedule.
- Pick a date format that matches how you read dates locally so config timestamps are intuitive.
- Relative time is handy when sorting by "recently used" in the Library, since you can see how long ago a config ran.

## Troubleshooting

- **Language change did not apply:** The app may need a manual restart if it fails to refresh automatically.
- **Theme flickers or looks wrong:** Force-close the app and reopen it to reload the theme correctly.
- **Date format shows wrong example:** Ensure your device's system locale is set correctly, then re-select the format.
