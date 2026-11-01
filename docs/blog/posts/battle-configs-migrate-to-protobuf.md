---
title: Battle Configs Migrate to Protobuf
description: Battle configs now use protobuf storage. Browse the full list of new features, changed behavior, and removed functionality in this update.
categories:
    - Announcements
tags:
    - battle configs
    - migration
    - protobuf
    - storage
    - changelog
date:
    created: 2026-11-01
---

# Battle Configs Migrate to Protobuf

FGA Preview now stores battle configs in protobuf files and converts your existing configs automatically. This post lists what is new, what changed, and what the app removed in this update.

<!-- more -->

## Overview

Older versions of FGA Preview stored each battle config as text keys in a settings file. This format had no defined structure. The app packed complex values, such as card priority lists, into text strings. Copies and backups of a config could lose detail.

Now the app stores each battle config in a protobuf file. A protobuf file has a defined structure with a type for each value. The app can copy this file exactly. The new format also supports features that the old format could not store.

This post covers the storage change and all feature changes in this update.

---

## The New Storage Format

|                     | Old storage                             | New storage                                                        |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------ |
| **File per config** | Settings file with text keys            | Protobuf file with a defined structure                             |
| **Complex values**  | Packed into text strings                | Stored as typed fields                                             |
| **Copies and backup** | Guessed value types, some detail lost | Exact copy of the config                                           |
| **Script profiles** | One per config                          | Several per config                                                 |
| **Game servers**    | One server per config                   | A list of servers per config                                       |
| **Usage records**   | Count and last-used time                | Count, use time, created date, last-used time                      |
| **Shared defaults** | One global settings file                | Separate file for default materials, support variations, and teams |

---

## How the Migration Works

When you update the app and start it, the migration runs automatically:

1. The app finds your old config files.
2. The app converts each config to the new format.
3. A progress screen shows how many configs the app converted.
4. When the migration finishes, you use the app as before.

The migration protects your data:

- A config that fails to convert stays pending. The app retries it later.
- A damaged value falls back to its default. The rest of the config imports unchanged.
- The app does not remove your old files. They stay on disk after the migration.

> [!NOTE]
> Keep your old files until you check your configs. Do not remove the app data before that.

---

## New Functionality

### Battle Configs

- **Multiple script profiles.** A config can hold several named scripts. Each profile has its own notes, start wave, start turn, and team.
- **Multiple card rules.** A config can hold several named card rules. Each rule sets card priority, servant priority, brave chains, chain priority, rearrange, and critical stars per wave and turn.
- **Custom card priority.** Each wave and turn can hold an exact list of card picks. Custom picks skip the normal priority rules. Picks for Noble Phantasm cards are not available yet.
- **Global teams.** The app stores teams separately from configs. Several script profiles can select the same team. Each profile records the teams it used.
- **Multi-server.** A config can target a list of game servers.
- **Settings for each support servant.** Each preferred servant can set max ascension, NP level, skill levels, append skills, and grand servant type. It can also set image matching, a custom CE, a custom friend, and friend requests. Config-level defaults apply when a servant does not set a value.
- **Storm pod limits.** A config can cap Ordeal Call storm pods like teapots. The app turns the limit off when the pods run out.
- **Default limits per config.** Each config sets its own default counts for runs, CEs, teapots, and storm pods. The app restores them when a limit runs out.
- **Usage records.** A config records its created date, use count, total use time, and last-used time.

### Config Management

- **Rescan.** The Library can rescan the stored config files. The rescan repairs the list when files change outside the app.
- **Export and import as protobuf files.** The app exports a config as a `.pb` file. The app imports `.pb` files, old JSON backups, and `.fga ext` files.
- **Raw data viewer.** A screen shows the config data as formatted JSON. You can copy it to the clipboard.
- **Library tools.** The Library has search, sorting by use and name, multi-select, and a tab per game server.

### Backup

- **GitHub backup.** The app can save your config files to your own GitHub repository. The app compares local files with the backup and applies your choice per file.
- **Settings backup.** One backup file holds your app settings and your battle configs.

### Script Maker

- **Undo and redo** for edits.
- **Servant images from the Atlas database** while you edit scripts.
- **A custom target maker** for skill commands.

### Support Images

- **Atlas-linked support database.** Support servant and CE images come from the Atlas database. The images stay current with the game data.
- **Pick from your own images.** The preferred support selection can use your stored images in addition to the Atlas database.
- **Your stored images stay.** The Support Gallery still works for backwards compatibility. The Support Image Maker still extracts new images from the support screen.

### Other Script Features

- **Card simulation.** Try command card orders in a simulation.
- **Cards between Noble Phantasms.** Scripts can select command cards between NP attacks.
- **Wait during manual support selection.** The app can wait for your pick instead of exiting.
- **Stop on bond level 16.**
- **Skip the teapot check.**
- **Remaining commands at pause.** The app can show the commands that remain when you pause.

---

## Changed Behavior

### Material Limits Count Each Material Separately

This change affects when farming stops.

Old behavior: the app compared one shared counter against the total of all drops. A limit of 5 stopped the farm after 5 drops in total.

New behavior: each tracked material has its own count. The farm stops when one material reaches its count.

> [!WARNING]
> A migrated config that tracks 2 materials with a limit of 5 now stops only after each material drops 5 times. This makes farming longer than before. Check the material limits in your migrated configs.

### Other Changes

- **Cards without a rank go last.** Old versions dropped cards that your priority list did not name. Now the app uses these cards at the end. The critical percentage breaks ties.
- **Critical cards have explicit tokens.** Card priority lists mark each card as critical (`C`) or normal (`N`). The app converts old lists and keeps their order.
- **Card options moved to each turn.** Old versions had one critical-star option and one servant-priority option per config. Each turn now holds its own options. The migration copies your old options to every turn.
- **Party selection uses None.** A config without a party now stores `None`. Old versions stored the value `-1`.
- **BetterFGO variants.** A config stores base servers only. The app resolves BetterFGO variants when the script runs.
- **Generated names.** A new config gets a name like `C-xxxxxx`. Old configs used the name `--`.
- **Last-used time after first use.** The last-used time appears only after you run a config. An unused config shows no timestamp.
- **Attack card token in new commands.** New commands that pick exact attack cards use the token `N`. Old commands with the token `n` continue to work.
- **Clean removal.** When you remove the selected config, the app clears the selection.

---

## Removed

- **Manual command editor in the Script Maker.** Edit commands in the visual wave and turn editor.
- **Extract Default Support Images.** The settings button with this name is gone. The Atlas database provides default support images now.
- **Single-server option.** Select one or more servers instead.
- **One script and one card setup per config.** Use profiles and rules instead.
- **JSON files as the config backup format.** The app exports `.pb` files now. The app still imports your old JSON backups.

---

## Useful Information

- **Your old config files stay on disk.** The app never removes them.
- **Where your configs live.** The app stores each config as `data/battle/<id>.pb` in its internal storage. A separate file `data/battleConfigDefaults.pb` holds default materials, support variations, and teams.
- **Corrupted configs stay on disk.** The rescan removes a corrupted config from the list. The file stays on disk for manual recovery.
- **Check your configs after the migration.** Check the material limits first.

---

## Related Documentation

- [Battle Config](../../battle-setup/config.md) - Config groups and settings
- [Materials](../../battle-setup/materials.md) - Per-material limits
- [Teams](../../battle-setup/teams.md) - Global teams
- [Card Priority](../../battle-setup/card-priority.md) - Card rule editor
- [Script Maker](../../battle-setup/script-maker.md) - Visual script editor
- [Support Selection](../../battle-setup/support.md) - Preferred support configuration
- [Custom Card Priority](../../scripts/in-battle/card-selection/custom-card-priority.md) - Exact card picks
- [Storm Pods](../../scripts/in-battle/resources/storm-pods.md) - Storm pod limits
- [Support Image Maker](../../scripts/support-image-maker.md) - Extract support images from the game screen
- [GitHub Backup](../../app/github-backup.md) - Back up configs to GitHub
- [Storage](../../app/storage.md) - Storage locations and settings backup
- [Library](../../app/library.md) - Config list, tabs, and sorting
