---
title: Battle Launcher
description: Start and manage FGA Preview battle configurations. Select configs, run automated farming, and monitor battle progress.
tags:
  - battle
  - launcher
  - farming
  - automation
---

# Battle Launcher

The Battle Launcher is the main control panel for battle automation. You use it to select a battle config, set the run limits, and start a farming run.

## Overview

The Battle Launcher opens when you tap the FGA overlay button and you have one or more battle configs. It gives you quick access to run options, config details, and settings. You do not need to leave the game.

## How to Access

1. Create at least one **Battle Config** in the FGA app.
2. Open FGO and go to a quest screen.
3. Tap the FGA overlay button.
4. The Battle Launcher opens.

---

## Layout

The Battle Launcher has two main sections.

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

The left panel lists all your battle configs.

### Select a Config

- Tap a config name to select it.
- FGA fills the selected config with the primary color.
- A heart icon shows the favorite configs.

### Sort Configs

Use the sort button at the top of the list. You can sort the configs by these options.

| Sort option | Order |
|-------------|-------|
| **Name (A–Z)** | Alphabetical order, ascending |
| **Name (Z–A)** | Alphabetical order, descending |
| **Most Used** | Highest usage count first |
| **Least Used** | Lowest usage count first |
| **Recently Used** | Most recent last-used time first |
| **Older Used** | Oldest last-used time first |

---

## Details Panel

The right panel has three tabs. Tap the icons at the bottom to change the tab.

| Icon | Tab | Purpose |
|------|-----|---------|
| 🏃 | **Run** | Set the AP refill and the run limits |
| ℹ️ | **Info** | Read a summary of the config |
| ⚙️ | **Settings** | Change common settings |

---

## Run Options Tab

The Run tab controls how many times the script runs and how it refills AP.

### Refill

The Refill section controls what FGA does when AP runs out.

#### Refill Count

Set how many apples of the selected type FGA can use.

- Use the **-100**, **-10**, **+10**, and **+100** buttons.
- Or edit the number in the stepper.

FGA keeps a separate count for each apple type.

#### Refill Resources

Select the apple type to use when AP runs out.

| Resource | Description |
|----------|-------------|
| **Copper** | Copper Apple. Restores a small amount of AP. |
| **Bronze/Blue** | Bronze/Blue Apple. Restores a medium amount of AP. |
| **Silver** | Silver Apple. Restores 50% of max AP. |
| **Gold** | Gold Apple. Restores 100% of max AP. |
| **SQ** | Saint Quartz. Restores 100% of max AP. |

Tap a resource to select it. Tap the selected resource again to clear the selection. Only one resource is active at a time.

!!! note
    If you turn on **Hide SQ in AP Resources**, the SQ resource does not show in this list. This prevents an accidental use of SQ. See the Settings tab.

#### Wait for AP Regeneration

When you turn on this option, the script waits for AP to regenerate on its own. It does not use apples. The script checks every 1 minute if AP is enough for another run.

#### Over Recharge AP

When you turn on this option, FGA refills AP above your maximum. FGA uses the largest number of apples that fits.

!!! note
    This option is available only for Copper, Bronze, and Silver apples. FGA disables this option for Gold apples and Saint Quartz.

### Command Execution Start From

This selector sets the start point of the skill command. It shows the wave and turn steps of the selected script. You pick the step where the skill command starts to run.

- The selector shows only when the config has a script.
- Tap the header to open the step list.
- Select the step to change the start point.

### Limits

The Limits section sets the conditions that stop the script.

Each limit has a checkbox and a count. Turn on the checkbox to enable the limit. Set the count with the stepper. The text under each limit shows the default count for that limit.

#### Runs

Stop the script after it finishes a set number of quest runs.

#### CEs

Stop the script after it collects a set number of Craft Essence drops.

#### Skip Consumables Check

When you turn on this switch, the script does not check the consumables state. FGA then disables the Teapots and Ordeal Call Storm Pods limits. Turn off this switch to check the consumables state again.

#### Teapots

Use teapots to finish battles at once. Set the maximum number of teapots to use.

!!! note
    Turn off **Skip Consumables Check** to use this limit.

#### Ordeal Call Storm Pods

Use Ordeal Call Storm Pods to finish battles at once. Set the maximum number of pods to use. The count range is 1 to 9.

!!! note
    Turn off **Skip Consumables Check** to use this limit.

#### Materials

Each tracked material has its own limit. Turn on a material to count it. Set the count that FGA must still find for that material. The text under each material shows its default count.

FGA stops the script when one enabled material reaches its own count. See [Materials Selection](materials.md) for how to add or remove tracked materials.

### Limit Controls

| Button | Action |
|--------|--------|
| **Default** | Restore every limit to the default value set in the config |
| **Reset All** | Turn off all limits and set every count to 1 |

!!! note
    FGA disables the **Reset All** button until you change a limit.

---

## Information Tab

The Info tab shows a summary of the selected config. You do not need to open the full editor.

The summary shows these items.

- The config name and notes.
- The configured script and skill sequence.
- The target materials and their counts.
- The party slot.
- The command card priority for each wave.
- The support selection settings.
- The records, such as the last used time and the usage count.

You can also do these tasks in the Info tab.

- Select a different script for the config.
- Turn a preferred support servant on or off.

FGA shows the timestamps with the date and time format that you set in the app settings.

---

## Settings Tab

The Settings tab groups common settings by scope.

### Per Server

These settings apply to the current game server.

| Setting | Description |
|---------|-------------|
| **Return to Main screen** | Return to the main menu after the runs finish |
| **Exit on Preset Quest** | Stop the script when it finds a preset or daily quest |
| **Send Friend Request** | Override the friend request behavior of the battle config |
| **Manual Battle Config** | Turn off battle screen automation |

!!! note "Send Friend Request override"
    The **Send Friend Request** setting has three states.

    - **Default**: FGA follows the friend request settings of the battle config.
    - **Always**: FGA sends a request on every friend request screen.
    - **Never**: FGA rejects every request.

    See [Support Selection](support.md) for the friend request settings of the battle config.

### Per App

These settings apply to the whole app.

| Setting | Description |
|---------|-------------|
| **Story Skip** | Skip the quest story |
| **Hide SQ in AP Resources** | Hide the SQ resource so you cannot tap it by mistake |
| **Treat Support like own Servants** | Use normal face card checks instead of the Support icon check |
| **Stop on Bond Level Up** | Stop the script when a servant reaches the target bond level |
| **Bond Level Target** | The bond level that stops the script. The range is 10 to 16. |
| **Screenshot Bond** | Save a screenshot of each bond level up to the `bond` folder |
| **Exit on Manual Support Selection** | Stop the script when you select a support by hand |
| **Debug Mode** | Write detailed logs for problem reports |

!!! note
    The **Bond Level Target** setting is active only when **Stop on Bond Level Up** is on.

---

## Start a Battle Run

1. Select a battle config from the list.
2. Set the run options, such as the refill and the limits.
3. Go to a quest selection screen in FGO.
4. Tap the **Play** button on the FGA overlay.

---

## Run Progress

During a run, FGA tracks these values.

- The number of completed runs.
- The materials collected, when you set a material limit.
- The CEs collected, when you set a CE limit.
- The apples used, per type.

The script stops when it reaches one limit. When the script reaches a limit, that limit turns off and its count returns to the default value.

---

## Tips

### Use Apples With Care

1. Set an exact apple count. This stops FGA from using more apples than you want.
2. Use Bronze or Silver apples for short sessions. Use Gold apples for long sessions.
3. Turn on **Wait for AP Regeneration** for casual overnight runs that use no apples.

### Set Safe Limits

1. Use more than one limit. A run limit and a material limit together give more safety.
2. Set a material limit. This stops the script when you have enough of that material.
3. Set a CE limit. This helps during events where CE drops matter.

### Before You Start

1. Read the Info tab. Check that the settings are correct.
2. Check the support settings. Make sure your preferred supports are correct.
3. Check the party slot. Make sure the correct team is ready.

### Run Until AP Runs Out

1. Do not select a refill resource.
2. Do not turn on any limit.
3. Start the script. It runs until your AP is empty, and then it stops.

---

## Troubleshooting

### A config does not show in the list

- Make sure you save the config in the FGA app.
- Check that the current sort filter does not hide the config.

### FGA does not use apples

- Make sure you select a refill resource.
- Make sure the refill count is more than 0.

### The script stops too early

- Read all the limit settings.
- Check that you did not turn on a limit by mistake.

### The script does not stop

- Make sure at least one limit is on.
- Material and CE limits need correct drop detection to work.

### The Teapots or Ordeal Call limit is not available

- Turn off **Skip Consumables Check**. This switch turns off both limits.

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - How the battle automation works
- [Battle Config](config.md) - Full battle configuration settings
- [Materials Selection](materials.md) - Set the tracked materials and their counts
- [Command Card Priority](card-priority.md) - Card priority configuration
- [Script Maker](script-maker.md) - Skill command configuration
- [Preferred Support](support.md) - Support selection setup
- [Materials and Drop Tracking](../in-battle/tracking/materials-tracking.md) - How FGA counts drops during a run
