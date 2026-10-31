---
title: Materials Selection
description: Configure material farming preferences in FGA Preview. Select target materials, set a count for each material, and let FGA stop the script when one material fills its quota.
tags:
    - battle
    - materials
    - farming
    - configuration
---

# Materials Selection

The Materials screen sets the materials that FGA tracks during a farming session. FGA counts the drops of each tracked material. FGA stops the script when one material reaches its own count.

## Overview

Fate/Grand Order materials come in three rarities. FGA sorts them into tabs for easy browsing.

| Tab        | Materials in this tab                                                                                                                    |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Copper** | Proofs, Bones, Fangs, Dust, Chains, Stingers, Fluids, Stakes, Gunpowder, and similar items. Blue skill gems for all classes are also here. |
| **Silver** | Seeds, Ghost Lanterns, Crystals, Jewels, Feathers, Gears, Pages, and similar items. Class pieces and red skill gems are also here.          |
| **Gold**   | Claws, Hearts, Dragon Scales, Spirit Roots, and other rare items. Class monuments and gold skill gems are also here.                        |

Each tracked material stores three values.

| Value             | What it does                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| **Count**         | The number of drops that FGA must still find for this material.                                     |
| **Default Count** | The count that FGA restores after this material reaches zero.                                       |
| **Enabled**       | Whether FGA counts this material. When the material is off, FGA does not scan it on the drop screen. |

## Open the Materials Screen

1. Open a battle config in the Library.
2. Go to the Farming section.
3. Tap the Materials card.

## Key Features

### Two Panes

The screen has a main list and an edit pane.

- On a wide window, the list and the edit pane show side by side.
- On a narrow window, the edit pane replaces the list. Tap the back arrow to return to the list.

### Material Selection

Tap a material in the list to add it to the battle config. FGA then opens the edit pane for that material.

A tracked material keeps its place in the list and shows two pill buttons on the right side.

| Button    | Action                                       |
| --------- | -------------------------------------------- |
| **Close** | Remove the material from the battle config.  |
| **Edit**  | Open the edit pane for this material.        |

The line below the material name shows the count and the default count in this form: `Limit: 10 (Default: 5)`. When the material is off, the line also shows `(Disabled)`.

Tap a tracked material to open its edit pane.

### The Edit Pane

The edit pane controls one material. These items control the material:

| Item                      | What it does                                                                                                     |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Enabled** switch        | Turns the material on or off. FGA counts only the materials that are on.                                         |
| **Count** stepper         | Sets how many drops FGA must still find. The range is 1 to 999. The stepper is off when the material is off.     |
| **Default Count** stepper | Sets the count for the next farming session. The range is 1 to 999.                                              |
| **Load Defaults**         | Replaces this material's settings with the saved global default. The button is off when no saved default exists. |
| **Save Defaults**         | Saves this material's current settings as the global default for this material.                                  |
| **Reset**                 | Turns the material on again. The count becomes 1 and the default count becomes 1.                                 |
| **Remove**                | Removes the material from the battle config.                                                                    |

When you remove a material that is open in the edit pane, the edit pane closes.

!!! note "How the two counts work together"
    The **Count** is the number of drops that remain. The **Default Count** is the value that the **Count** returns to after FGA reaches zero. Set the **Default Count** before you change the **Count**.

### Global Material Defaults

The defaults that you save are global. Every battle config on the device can load them.

Use **Save Defaults** in one battle config. Use **Load Defaults** in another battle config to copy the same count and default count for that material. Each material has its own saved default, and the saved default for one material does not change the other materials.

### Search Materials

The search field is in the top app bar.

1. Tap the search field.
2. Type part of a material name.
3. The list filters as you type.

Search ignores the difference between uppercase and lowercase letters. Example: `saber` finds `Monument Saber`, `Piece Saber`, and the Saber skill gems.

The clear button inside the field removes the query. The button is off when the field is empty.

### Search Button

On a narrow window, the floating toolbar shows a search button. Tap it to focus the search field. While the search field has focus, the button shows a clear icon. Tap it again to remove the query.

### Empty Results

When no material in the current tab matches the query, FGA shows `No Items Found`. Change the query, or move to another tab.

### Rarity Tabs

Tap a tab to see the materials in that rarity.

- The tab name shows the number of tracked materials in that rarity.
- While a query is active, the tab name also shows the number of matching materials in that rarity.

### Toolbar Actions

The floating toolbar at the bottom shows three buttons.

| Button    | Action                                                                       | When the button is on                                         |
| --------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Reset** | Restore the tracked materials to the state from when you opened the screen.  | Your current selections are different from the initial state. |
| **Undo**  | Reverse your last change.                                                    | You made at least one change in this session.                 |
| **Clear** | Remove all tracked materials.                                                | You track at least one material.                              |

**Reset** returns the material list to its state when you opened the screen. **Reset** also clears the undo history.

## How FGA Uses the Limits

FGA counts the drops of each material that is on. FGA uses the count of each material by itself. FGA does not add the counts of all materials together.

1. FGA reads the drop screen and counts each material that is on.
2. FGA compares the drops of the current run with the remaining count of that material.
3. When the drops reach the count, FGA stops the script. The exit reason is `Limit Materials`.
4. FGA turns that material off and restores its count to its default count.

The exit summary shows the total number of materials that you collected in the session. This total includes every tracked material, not only the material that reached its count.

A material that is off is not counted, and FGA does not stop the script for it.

### Change the Limits Before a Run

The Battle Launcher also shows the material limits for the selected battle config. You can change the count and turn a material on or off there before you start a run.

## Migration From Older Versions

FGA moves your old material settings automatically when it opens an older battle config.

- The old shared material limit becomes the **Count** and the **Default Count** of each tracked material.
- The old material-limit switch becomes the **Enabled** state of each tracked material.
- The material stepper in the Default Run Configuration panel is gone.
- Set the counts in the Materials editor or in the Battle Launcher.

This change also changes when FGA stops the script. An old config with a shared limit of 5 stopped after 5 drops in total. The same config now stops after 5 drops of each tracked material.

!!! info "Configs that had no material limit"
    An older config with the material limit turned off keeps its tracked materials, but each material is off. Turn a material on when you want FGA to stop the script for it.

## Tips for Best Results

### Track only the materials that you need

Each tracked material adds work to each drop screen. Add only the materials that drop in your quest.

### Set the default count first

Set the **Default Count** to the number that you want for each future farming session. Then change the **Count** for the current session.

### Save the counts that you use often

Use **Save Defaults** on the materials that you farm often. Use **Load Defaults** on a new battle config instead of typing the numbers again.

### Check the tab counts before a run

The number on each tab shows the tracked materials in that rarity. Check that the numbers match your farming plan.

### Use Clear when you change quests

Tap **Clear**, then add the materials for the new quest.

## Troubleshooting

### FGA does not count a material

1. Make sure that the material is on. The edit pane shows the **Enabled** switch.
2. Make sure that the material drops in your quest.

### FGA stops the script too early

One material can reach its count before the other materials. Check the **Count** of each material that is on.

### The Load Defaults button is off

There is no saved default for that material yet. Tap **Save Defaults** on the material first. After that, **Load Defaults** becomes available.

### Materials are not detected

1. Make sure that the material is on.
2. Make sure that the material drops in your quest.
3. Make sure that the full drop screen is visible.

### Search shows no results

1. Check the spelling of your query.
2. Use a shorter query.
3. Clear the query and browse the tabs.

### Selections are not saved

Your selections save to the battle config automatically. If the selections do not persist:

1. Leave the screen with the back arrow.
2. Do not force-close the app before the changes sync.

### Wrong materials after Undo

The undo system stores the full material list before each change. Many quick taps create many undo states. Use **Reset** to return to the initial state.

## Related Documentation

- [Battle Config](config.md) - Full battle configuration settings
- [Battle Launcher](launcher.md) - Start and monitor farming runs
- [Materials and Drop Tracking](../in-battle/tracking/materials-tracking.md) - How FGA counts drops during a run
