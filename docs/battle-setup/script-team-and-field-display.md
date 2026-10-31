---
title: Script Team and Field Display
description: Manage the servant team of a battle script and understand how the Script Maker's field display tracks order changes, manual switches, and transformations.
tags:
    - battle
    - skills
    - configuration
    - script-maker
---

# Script Team and Field Display

Each battle script owns a **team**: up to six servant slots (three starting members, three
substitutes) plus one Mystic Code. The team is stored with the script. It drives the Atlas labels
in the editor: servant names and faces on the skill rows, skill names and icons on the buttons,
Noble Phantasm names on the attack screen, and the servant behind each action in the action
history.

The **field display** is the arrangement that the editor resolves commands against. Skill codes
`a` to `i` and the NP card buttons always refer to the three field slots. The editor tracks which
team member each field slot currently shows.

## Manage the Team

1. Open the battle config in **Battle Scripts**.
2. On the script card, tap **Edit Team**.

The team screen lists the six slots grouped into starting members and substitutes, plus the
equipped Mystic Code.

| Action | Result |
| ------ | ------ |
| Tap an empty slot | Opens the Atlas servant picker for that slot. |
| Tap a filled slot | Opens the servant detail screen. |
| Drag the handle of a filled slot | Swaps the two servants; the order is saved when the drag ends. |
| Tap the delete icon | Removes the servant from the slot. |

On the servant detail screen, replace the servant or pick the **skill version** for each skill
slot. A servant can carry rank-up versions of a skill. The newest version is selected by default.
Slots without Atlas data keep the generic letter button.

The Mystic Code row opens the Mystic Code detail screen, where you equip or clear the code.

## How the Field Display Is Derived

The editor replays the recorded entries of the script from the start. It derives the arrangement
from three sources:

| Source | Effect on the display |
| ------ | --------------------- |
| **Order Change action** | Swaps the chosen starting member's field slot with the chosen substitute's slot, exactly like the in-game Order Change. |
| **Manual switch** (see below) | Swaps any two display slots. |
| **Transformation skill** | From that entry on, the acting slot resolves the transformed form's name, face, NP, and skills. |

Recording an Order Change updates the field display automatically. No extra step is needed.
Undo and redo also revert the arrangement together with the action, because the arrangement is
derived from the entry list itself.

A transformation applies from its entry onward. It stays attached to the party position, so it
travels with later Order Changes. A later transformation of the same slot replaces the earlier
form. This also covers transformations that revert.

## Switch Team Members Manually

**Switch team members** at the bottom of the editor opens the switch dialog. Tap one slot,
then another. The swap is recorded as its own undoable entry that persists with the script. It
never writes an Order Change command. It never reorders the stored team.

In-game, Order Change only swaps a starting member with a substitute. A swap inside one row
(two starting members, or two substitutes) cannot happen in-game. The dialog asks for
confirmation before it records such a swap. Use it only to mirror an arrangement that the app
cannot record. For example, use it for a party order that you arranged in-game before the
battle.

## Known Limitations

| Limitation | Detail |
| ---------- | ------ |
| Stage-gated skill versions | Skill versions that only exist in certain costumes or ascensions are listed and can become the default selection. The special-skill flow prefers always-available versions. |
| Duplicate servants | The same servant can be placed in two slots, although the game forbids duplicates in one party. |
| Transformations of old records | Scripts recorded before transformations were tracked keep showing the original servant; record the transformation again to track it. |
| Action-history staleness | History rows compare their recorded Atlas context against the final arrangement of the script. Rows recorded before a swap or transformation show as plain commands by design. |
| Skill version selection | The newest version is picked by the highest Atlas id. The data export does not carry the Atlas `priority` field, which the game uses for this. |

## Troubleshooting

| Problem | Review |
| ------- | ------ |
| Skill buttons show the wrong servant after an Order Change | The Order Change action must be recorded in the script; the display follows recorded actions, not the live game. |
| A slot shows the original servant after a transformation | The transformation skill must be recorded with its option in the script, and the Atlas data must contain the transformed form. |
| Translated names fall back to Japanese | The Atlas snapshot does not resolve the stored id; it updates when new Atlas data is downloaded. |

## Related Documentation

- [Script Maker Guide](script-maker.md) explains the editor, its screens, and command syntax.
- [Config](config.md) explains battle configs and their scripts.
