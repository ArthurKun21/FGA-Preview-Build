---
title: Battle Launcher
description: Launch and manage FGA Preview battle configurations. Select configs, start automated farming, and monitor battle progress.
tags:
  - battle
  - launcher
  - farming
  - automation
---

# Battle Launcher

The Battle Launcher is the main control panel for configuring and starting battle automation.

## Overview

The Battle Launcher appears when you open the FGA overlay and have battle configs available. It provides quick access to run options, configuration information, and settings without leaving the game.

## How to Access

1. Create at least one **Battle Config** in the FGA app
2. Open FGO and navigate to a quest screen
3. Tap the FGA overlay button to open the launcher
4. The Battle Launcher displays automatically

---

## Layout

The Battle Launcher is divided into two main sections:

```text
┌─────────────────────────────────────────────────────────────┐
│                      Battle Launcher                        │
├───────────────────────┬─────────────────────────────────────┤
│                       │                                     │
│   Battle Config       │        Details Panel                │
│   List                │                                     │
│                       │   ┌─────┬─────┬─────────┐           │
│   • Config 1          │   │ Run │Info │Settings │           │
│   • Config 2  ★       │   └─────┴─────┴─────────┘           │
│   • Config 3          │                                     │
│   ...                 │   (Content changes based on tab)    │
│                       │                                     │
└───────────────────────┴─────────────────────────────────────┘
```

---

## Battle Config List

The left panel shows all your battle configurations.

### Selecting a Config

- Tap on any config name to select it
- The selected config is highlighted
- A heart icon (❤) indicates favorite configs

### Sorting Configs

Use the sort button at the top of the list to organize configs by:

- **Name** (alphabetical)
- **Favorites** (favorites first)
- **Recent** (recently used first)

---

## Details Panel

The right panel has three tabs accessible via the bottom icons:

| Icon | Tab | Purpose |
|------|-----|---------|
| 🏃 | **Run** | Configure AP refill and run limits |
| ℹ️ | **Info** | View config details at a glance |
| ⚙️ | **Settings** | Quick access to common settings |

---

## Run Options Tab

Configure how many times and how the script should run.

### AP Refill

Control how FGA handles running out of AP (stamina).

#### Refill Count

Set how many apples of the selected type to use:

- Use **-100**, **-10**, **-1**, **+1**, **+10**, **+100** buttons
- Or tap the number directly to edit

#### Refill Resources

Select which apple type to use when AP runs out:

| Resource | Description |
|----------|-------------|
| **Copper** | Copper Apple (10 AP) |
| **Bronze/Blue** | Bronze/Blue Apple (40 AP, resource-limited) |
| **Silver** | Silver Apple (50% max AP) |
| **Gold** | Gold Apple (100% max AP) |
| **SQ** | Saint Quartz (100% max AP, resource-limited) |

!!! note
    Only one resource type can be selected at a time. Tap to toggle selection.

#### Wait for AP Regeneration

When enabled, the script will wait for natural AP regeneration instead of using apples when you run out.

It checks every 1 minute if it can do the quest.

#### Stamina Over Recharge

When enabled and using Copper, Bronze, or Silver apples, allows AP to exceed your maximum.

!!! note
    This option is not available for Gold apples or Saint Quartz.

### Run Limits

Set conditions for when the script should stop.

#### Limit by Runs

Stop after completing a specific number of quest runs.

- Check the box to enable
- Set the target number of runs

#### Limit by Materials

Stop after collecting a specific number of materials.

- Check the box to enable
- Set the target material count
- Works with materials configured in your battle config
- This is the combine amount across all materials
    - E.g., if farming for 3 different items and set limit to 10, the script stops after collecting a total of 10 items across all types

#### Limit by Craft Essences

Stop after collecting a specific number of CE drops.

- Check the box to enable
- Set the target CE count

#### Teapots

Use teapots to instantly complete battles.

- Check the box to enable teapot usage
- Set the maximum number of teapots to use

### Limit Controls

| Button | Action |
|--------|--------|
| **Default** | Reset all limits to config defaults |
| **Reset All** | Clear all limits and set counts to 1 |

---

## Information Tab

View a summary of the selected battle config without opening the full editor.

### Notes

Displays any notes you've added to the config.

### Skill Command

Shows the configured skill sequence as visual icons.

### Materials

Lists target materials configured for this config.

### Party

Shows which party slot is configured:

- **Any**: FGA won't change party
- **1-10**: Specific party slot to select

### Command Card Priority

Displays card priority settings for each wave:

- Card type order (Buster, Arts, Quick)
- Servant priority (if enabled)
- Brave chain settings
- Rearrange cards option

### Support Settings

Shows support selection configuration:

- Support class tab
- Selection mode (Preferred/First/Manual)
- Preferred servants and CEs (if using Preferred mode)
- Friend requirements

---

## Settings Tab

Quick access to common settings organized by scope.

### Per Battle Config

Settings specific to the selected config:

| Setting | Description |
|---------|-------------|
| **Auto Accept Friend Request** | Automatically send friend requests during farming |

### Per Server

Settings that apply to the current game server:

| Setting | Description |
|---------|-------------|
| **Return to Menu** | Return to main menu after completing runs |
| **Exit on Preset Quest** | Stop if a preset/daily quest is detected |
| **Manual Battle Config** | Allow manually switching configs during runs |

### Per App

Settings that apply globally:

| Setting | Description |
|---------|-------------|
| **Exit on Manual Selection** | Stop script if you manually select a support |
| **Debug Mode** | Enable detailed logging for troubleshooting |

---

## Starting a Battle Run

1. Select your desired battle config from the list
2. Configure run options (refills, limits)
3. Ensure you're on a quest selection screen in FGO
4. Tap the **Play** button on the FGA overlay

---

## Run Progress

During execution, FGA tracks:

- **Completed runs**: Number of quests finished
- **Materials collected**: If material limit is set
- **CEs collected**: If CE limit is set
- **Apples used**: Count per type

The script stops when any configured limit is reached.

---

## Tips for Effective Farming

### Efficient Apple Usage

1. **Set exact apple counts**: Prevent accidentally using more apples than intended
2. **Use appropriate apple types**: Bronze/Silver for short sessions, Gold for extended farming
3. **Enable Wait AP Regen**: For casual overnight farming without apple usage

### Configuration Run Limits

1. **Combine limits**: Use both run limits and material limits for safety
2. **Set material limits**: Stop exactly when you have enough materials
3. **Use CE limits**: For event farming where CE drops matter

### Before Starting

1. **Check your config**: Review the Info tab to verify settings
2. **Verify support settings**: Ensure your preferred supports are correctly configured
3. **Confirm party slot**: Make sure the right team is selected

### Run until out of AP is depleted

1. **Do not set a refill resource**: Leave all resource options unselected
2. **Do not set any limits**: Leave all limit checkboxes unchecked
3. **Run the script**: It will continue until your AP is fully depleted and exit.

---

## Troubleshooting

### Config not appearing in list

- Ensure the config is saved in the FGA app
- Check if the config is hidden by the current sort filter

### Apples not being used

- Verify a refill resource is selected (highlighted)
- Check that the refill count is greater than 0

### Script stopping too early

- Review all limit settings
- Check if a limit was accidentally enabled

### Script not stopping

- Ensure at least one limit is configured
- Material/CE limits require proper detection setup

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - How the battle automation works
- [Command Card](../battle-setup/card-priority.md) - Card priority configuration
- [Preferred Support](../battle-setup/support.md) - Support selection setup
- [Skill Maker](../battle-setup/skill-maker.md) - Skill command configuration
