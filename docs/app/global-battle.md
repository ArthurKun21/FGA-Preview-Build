---
title: Global Battle Settings
description: Configure FGA Preview global battle settings. Select game server detection, story skip, boost items, screenshot options, and exception handling for all battle configurations.
tags:
    - app
    - settings
    - battle
    - game-server
    - screenshots
---

# Global Battle Settings

## Overview

Global Battle Settings apply to every battle configuration that you create. They control how FGA detects the game server, how it handles story scenes, how it manages resources, and how it captures screenshots.

You set these options once. All scripts then use the same values.

The Battle section holds five settings, a Battle Exit Exceptions group, and a Screenshot group.

## Key Features

### Game server detection

FGA supports multiple Fate/Grand Order servers. The default **Auto-detect** mode uses the accessibility service to find the FGO app package that runs. It then selects the correct server.

You can also lock one server. Select a server when auto-detection fails.

| Server              | Notes                            |
| ------------------- | -------------------------------- |
| Auto-detect         | The recommended option           |
| NA                  | The North America / Global server |
| NA (Better FGO)     | The BetterFGO variant of NA      |
| JP                  | The Japanese server              |
| JP (Better FGO)     | The BetterFGO variant of JP      |
| CN                  | The Chinese server               |
| TW                  | The Taiwan server                |
| KR                  | The Korean server                |

!!! note "Android only"
    The **Game Server** row shows only on Android. See [Settings](settings.md) for the full list of Android-only rows.

### Skip story scenes

Enable **Story Skip** to move through the dialogue and the cutscenes of a quest. A farming run then finishes faster when story plays between the battles.

!!! warning "Story skip has a limit"
    The script cannot bypass a story part that needs a choice from the player. If the story makes you choose an option, FGA waits until you choose it.

### Boost item selection

Some events use items that boost the performance of a servant. Select how FGA handles the boost-item popup:

| Option   | Behavior                                              |
| -------- | ----------------------------------------------------- |
| Disabled | Do not touch the popup. You handle the popup yourself |
| Skip     | Close the popup without a selection                    |
| 1        | Select the item in the first slot                      |
| 2        | Select the item in the second slot                     |
| 3        | Select the item in the third slot                      |

### Hide Saint Quartz in the refill list

Enable **Hide SQ in AP Resources** to remove Saint Quartz from the list when FGA offers to refill AP. The option prevents the use of premium currency during an automated run.

### Treat support servants like your own

A support servant can get so many buffs that the "Support" tag is partly hidden. FGA can then read the servant as one of your own servants. Enable **Treat Support like own Servants** to work around this case.

!!! warning "This option changes card checks"
    With the option enabled, FGA does not look for the "Support" icon on face cards. If two of the same servant are in your party, card priority can break.

## Battle Exit Exceptions

The Battle Exit Exceptions group holds six settings. Each setting stops the script when a condition becomes true.

### Stop on bond level up

Enable **Stop on Bond Level Up** to stop the script when a servant reaches the target bond level.

Select the **Bond Level Target** to set the level that stops the script. The range is 10 to 16. FGA disables the selector until you enable **Stop on Bond Level Up**.

### Exit on manual support selection

Enable **Exit manual support selection** to stop the script when the support list opens. You then pick your friend support before the run continues.

### Enable withdraw

Enable **Enable Withdraw** to let FGA retreat from a battle when a failure condition becomes true. Without the option, FGA continues or retries the battle.

### Stop on CE get

Enable **Stop on CE GET** to stop the script when a Craft Essence drops after a quest. The option helps when you farm a limited event CE, because you can review or lock the CE at once.

### Stop on first-clear rewards

Enable **Stop on first-clear rewards** to stop the script when a quest gives first-time completion rewards. You then collect the rewards before you start the script again.

## Screenshot

The Screenshot group holds three settings.

### Material drops

Enable **Material Drops** to capture the drop screen at the end of each quest. The image goes to the `drops` folder in your storage location.

### Save unmodified screenshots

Enable **Save unmodified screenshots** to store the raw image with the annotated image. Use this option when you want the original image without marks.

### Screenshot bond

Enable **Screenshot Bond** to capture the bond screen that shows after a battle. The image goes to the `bond` folder in your storage location.

!!! note "Bond screenshots can be missed"
    The script clicks the results screen automatically. That click can sometimes skip a bond screen before the capture.

## Tips for Best Results

- Keep **Auto-detect** for the game server. Select a server only when the detection fails.
- Enable **Hide SQ in AP Resources** to prevent the use of premium currency.
- Set a **Bond Level Target** and enable **Stop on Bond Level Up** when you farm bond points.
- Use the screenshot options with the bond options to keep a record of your runs. See [Storage Settings](storage.md).

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| FGA detects the wrong server | Select the correct server in the **Game Server** row. Keep the manual selection until the detection works again. |
| Story skip does not work | The quest can need a dialogue choice. FGA cannot make that choice for you. |
| Screenshots are not saved | Check the storage location in Storage Settings. Then check that FGA can write to the selected folder. |
| The bond stop starts too early or not at all | The optical character recognition can read a bond level wrong. Read the bond screenshots to check the level. |
| A support servant breaks card priority | Enable **Treat Support like own Servants**. Then remove one of the two same servants from the party. |

## Related Documentation

- [Settings](settings.md)
- [Card Priority](../battle-setup/card-priority.md)
- [Withdraw](../in-battle/script-control/withdraw.md)
- [Auto Battle Exit Reasons](../in-battle/script-control/auto-battle-exit-reasons.md)
