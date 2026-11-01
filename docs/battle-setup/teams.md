---
title: Teams
description: Create and manage battle teams in FGA Preview. Place servants, select skill versions, and equip a Mystic Code. Share one team between several battle scripts.
tags:
    - battle
    - configuration
    - servants
    - teams
---

# Teams

A team is a named party of up to six servants and one Mystic Code. Slots 1 to 3 are the starting members. Slots 4 to 6 are the substitutes.

Teams are global. You create each team once. You can then select it in several battle scripts. The team drives the Atlas labels in Script Maker: servant names and faces, skill names and icons, and Noble Phantasm names.

## Open the Teams Screen

Tap **Teams** in the bottom navigation bar. The screen lists every team with its preview.

## Manage the Team List

Each card has the team name, its notes, and a preview. The preview lists one icon per team slot and the equipped Mystic Code. The title bar gives the number of teams.

| Action | Use |
| ------ | --- |
| **Add** (floating button) | Create a team. The app names it **Team N** and opens its editor. |
| Tap a card | Open the team editor. |
| **Edit** (pencil icon) | Rename the team. A team without a name uses **Unnamed team**. |
| **Notes** | Add or edit the notes for the team. |
| **Delete** | Delete the team. A confirmation dialog opens first. |

A script that used a deleted team selects no team. The script itself does not change.

## Edit a Team

The editor lists the Mystic Code row and the six servant slots.

| Action | Use |
| ------ | --- |
| Tap an empty slot | Open the servant picker for that slot. |
| Tap a filled slot | Open the servant detail screen. |
| Drag the handle of a filled slot | Swap the two servants. The app saves the order when the drag ends. |
| Tap the delete icon | Clear the servant slot. |
| Tap **Mystic Code** | Open the Mystic Code screen. |

## Choose a Servant

The servant picker lists the servants from the Atlas data. Tap a servant to place it in the slot. The app selects the newest Atlas skill version for each skill slot.

From the servant detail screen you can change the servant, or clear the slot.

### Select a Skill Version

A servant can carry several versions of one skill, such as a rank-up version. Each skill slot lists every version that the Atlas data has.

- Tap a version to select it for that slot.
- The app selects the newest version by default.
- A skill slot without Atlas data keeps the generic configuration in Script Maker.

## Equip the Mystic Code

Tap **Mystic Code** in the team editor. The screen lists the equipped code and its skills.

| Action | Use |
| ------ | --- |
| **Select** or **Change** | Open the Mystic Code picker. |
| **Clear** (trash icon) | Clear the code. The team then uses the default Master Skill buttons. |

## Use a Team in Several Scripts

Open a battle script and tap **Select team** on the script card. See [Select the Team](script-maker.md#select-the-team).

Several scripts can select the same team. When you edit the team, the change applies to every script that selects it.

## Troubleshooting

| Problem | Review |
| ------- | ------ |
| A script card has empty team slots | The script selects no team. Tap **Select team** on the script card. |
| The Mystic Code does not apply to a script | The script selects a different team. Each team carries its own Mystic Code. |
| A servant slot has a generic placeholder | The slot is empty. Or the Atlas data cannot resolve the servant. |

## Related Documentation

- [Script Maker Guide](script-maker.md) explains the editor and the team selector.
- [Script Team and Field Display](script-team-and-field-display.md) explains how the editor maps the team to the field slots.
- [Config](config.md) explains battle configs and their scripts.
