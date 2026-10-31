---
title: Script Maker Guide
description: Create and manage battle scripts in FGA Preview. Set skills, attacks, targets, Master Skills, and start points for automated battles.
tags:
    - battle
    - skills
    - commands
    - configuration
---

# Script Maker Guide

Script Maker creates battle scripts. A battle script is a list of commands. Automation runs the commands during a battle.

A battle config can hold several scripts. One script is active for each battle. Each script has its own commands, name, notes, start point, team, and Mystic Code.

The team holds up to six servants and one Mystic Code. The editor reads servant names, faces, skills, and Mystic Codes from the Atlas data. See [Script Team and Field Display](script-team-and-field-display.md).

## Open Script Maker

1. Open a battle config.
2. Under **Battle Scripts**, tap the script card.

The script list opens. Tap a script card to open its editor.

## Manage the Script List

The script list shows the exit settings and every script. When the config has more than one script, the list also shows an **Active** selector at the top. Use this selector to set the script that automation runs.

Each script card shows the script name, its notes, and the team preview. The preview lists one icon per team slot and the equipped Mystic Code. Tap **Edit Team** on the preview to open the team screen. See [Script Team and Field Display](script-team-and-field-display.md).

Tap a card to expand it. The expanded card shows:

- A summary of the commands, grouped by wave and turn.
- The start selector. See [Set the Start Point](#set-the-start-point).

Each card also has these actions:

| Action | Use |
| ------ | --- |
| **Notes** | Add or edit the notes for the script. |
| **Delete** | Delete the script. A confirmation dialog opens first. This action appears only when the config has more than one script. |

Viewing a script does not make it active. Only the **Active** selector changes the script that automation runs.

Use the toolbar at the bottom of the list:

- **Add** creates a script.
- The up and down arrows open the previous or next script. The toolbar shows the position, such as 2 of 3.

## Rename a Script

Tap the script name in the editor title bar. Enter a name, then tap **Confirm**. The name cannot be blank. A script without a name uses its position, such as **Script 2**.

## Set Exit Settings

The battle config has two exit settings. The script list shows them at the top.

- **Out of Commands Exit** ends the battle when the script has no commands left.
- **Off-script Exit** ends the battle when the battle reaches a wave or turn that the script does not define.

## Set the Start Point

The start point sets where automation starts a script on the first run. Use the start selector on the expanded script card.

- The start point applies to the first run only. Later runs start at the first command.
- If the start point is no longer valid, automation starts at the first command.

## Save Changes

The editor saves your changes when you tap **Back**. The editor has no Save button.

## Editor Layout

```text
┌──────────────────────────────────────────────────────────┐
│ [Script name]                    [Settings] [Clear All]  │
├──────────────────────────────────────────────────────────┤
│ Wave/turn chip | Action history | [Undo][Redo][History]  │
├──────────────────────────────────────────────────────────┤
│ Enemy targets                                            │
├──────────────────────────────────────────────────────────┤
│ Servant 1 [target chip] [a] [b] [c]                      │
│ Servant 2 [target chip] [d] [e] [f]                      │
│ Servant 3 [target chip] [g] [h] [i]                      │
│ Gesture hint                                             │
│ [Switch team members]                                    │
├──────────────────────────────────────────────────────────┤
│ [Command Spell] [Master Skills] [Order Change] [Attack]  │
└──────────────────────────────────────────────────────────┘
```

- **Top bar**: Rename the script, open **Settings**, or clear all actions.
- **Action history**: Lists the actions of the script in order. Tap an action to select it. New actions are added after the selected action.
- **Undo, Redo, History**: Undo or redo an edit, or open the Action History pane. See [Undo, Redo, and Action History](#undo-redo-and-action-history).
- **Wave and turn indicator**: Shows the wave and turn of the selected action.
- **Enemy targets**: Contains the enemy buttons for the selected enemy formation.
- **Servant rows**: Contain the skill buttons and target chips for each servant.
- **Switch team members**: Opens the switch dialog for the field display.
- **Bottom bar**: Opens Command Spell, Master Skills, Order Change, and Attack.

The layout changes to fit the screen size. On small screens in portrait, the action history sits above the row with the Undo, Redo, and History buttons. On all other screen sizes, they share one row.

## Add Skills and Targets

Each servant has three skills. The codes are `a` to `i`: `a` to `c` for Servant 1, `d` to `f` for Servant 2, and `g` to `i` for Servant 3.

### Select a Target

Each servant row has a target chip labeled **Servant 1**, **Servant 2**, or **Servant 3**.

- Tap a chip to select that servant as the target.
- Tap the selected chip again to clear the target.

The selected target stays active until you change it.

### Set Smart Target

Smart Target sets which gesture adds a skill directly. Open **Settings** and select a Smart Target option.

| Smart Target | Tap a skill | Long press a skill |
| ------------ | ----------- | ------------------ |
| On | Adds the skill with the selected target. | Opens **Choose Target**. |
| Off | Opens **Choose Target**. | Adds the skill with the selected target. |

If you select no servant target, the direct gesture adds the skill without a target.

The hint below the servant rows states the current gestures. The hint uses the word **Hold** for a long press.

The Smart Target table applies to skill buttons without Atlas data. See the next section.

### Servant Skills with Atlas Data

When the team has a servant in a field slot, that servant's row uses the Atlas data:

- The row and the target chip show the servant's face and name.
- Each skill button shows the icon of its Atlas skill.
- A button without an Atlas skill keeps its letter code.

A skill button with an Atlas skill ignores the Smart Target setting. The button behaves as if Smart Target is On.

| Atlas target type | Tap the skill button |
| ----------------- | -------------------- |
| Special options | Opens the special option screen. See [Select Special Options](#select-special-options). |
| All allies | Adds the plain command at once. |
| One servant, or no target data | Adds the skill with the selected target chip. Without a selected chip, **Choose Target** opens. |

Long press a skill button with an Atlas skill to open the skill description. The description shows the skill name, icon, cooldown, and skill text.

- Tap **Use** to add the skill. **Use** does the same as a tap on the skill button.
- Tap **Dismiss** to close the description without a change.

See [Script Team and Field Display](script-team-and-field-display.md) to learn how the editor assigns servants to the field slots.

### Choose a Target

**Choose Target** lists **Servant 1**, **Servant 2**, **Servant 3**, **No Target**, and **Custom Target**. When the team has servants, each servant button shows that servant's face and name.

Select one option to add the skill with that target.

### Build a Custom Target

Some skills apply several targets in a row. Use the Custom Target screen to build such a sequence.

1. Tap **Custom Target** on the **Choose Target** screen.
2. Tap the targets in the order in which the skill should perform them.
3. Tap **Apply**. Tap **Cancel** to discard the sequence.

The screen lists these target groups:

| Group | Options |
| ----- | ------- |
| Field Targets | Servant 1, Servant 2, Servant 3. Also Left and Right when only two servants are on the field. |
| Choice (2 Options) | Option 1 or Option 2 of a two-choice popup. |
| Choice (3 Options) | Option 1, 2, or 3 of a three-choice popup. |
| Transform | The transform action. |

The **Selected Targets** section shows the sequence in order. Tap a target in the section to remove it.

For Master Skills and Command Spells, only the first target of the sequence applies.

The result is one command with several targets, such as `e([Ch2A]2)`. See [Servant Targets and Special Options](#servant-targets-and-special-options).

### Select Special Options

Some skills open a popup in the game: a choice between two or three options, an NP type change, or a transform. Script Maker reads these skills and their options from the Atlas data. New servants and new options appear with an Atlas data update. You do not need to update the app.

When you tap a skill that has special options, the Choose Target screen shows a **Servants with special skills** section. It lists every servant whose skill in the same position has special options. Each card shows the servant face icon and the skill icon.

- Tap the card to open the special option screen.
- Tap the info button on the card to see the skill description and an image of the in-game popup.

The special option screen shows the skill icon, name, and cooldown, and the skill description. The screen also shows:

| Item | Meaning |
| ---- | ------- |
| Transform line | The form of a transform that is not tied to an option. |
| Popup title | The title of the in-game popup. |
| Option buttons | One button per popup option. The labels are the option names from the Atlas data. |
| Transform caption | Below an option button, the form that this option changes the servant into. A caption for a different servant also shows the face icon of that form. |
| Transform button | The only button for a skill that only transforms the servant. |
| Info button | Shows the image of the in-game popup. |

Tap an option button to add the skill with that option. Some options also need a servant target. Choose Target opens when you tap such an option. Select the servant there.

Some skills need a special option and a target. Parentheses hold both. For example, `e([Ch2A]2)`.

## Configure Master Skills

Tap **Master Skills** to open the Master Skills screen. The **Mystic Code** row contains the Mystic Code of the script.

- Tap **Mystic Code** to choose a Mystic Code from the Atlas data. The selected code shows its skill names and icon.
- Use **Display options** to change how the Mystic Code icon appears.
- Clear the selection to use the default Master Skill buttons. The row shows **No mystic code set** when you select no code.

The **Master Skills** button in the bottom bar shows the icon of the equipped Mystic Code. Without an equipped code, the button shows the standard icon.

Master Skill codes are `j`, `k`, and `l`. Each Master Skill uses the target type that the Atlas data defines for it.

| Target type | Result |
| ----------- | ------ |
| No target | Adds the skill at once. |
| One servant | The direct gesture adds the skill with the selected servant. The other gesture opens **Choose Target** with Servant 1, 2, and 3 only. |
| Order Change | Opens **Order Change**. |

## Set Order Change

Tap **Order Change** in the bottom bar.

1. Select the starting member. This servant is in the front line.
2. Select the sub member. This servant is in the back line.
3. Tap **Ok** to add the action. Tap **Cancel** to close the screen without a change.

The command text is `l[x13]`. Master Skill 3 switches front position 1 with back position 3.

If the last action is a bare `l` (Master Skill 3 with no target), Script Maker deletes it before it adds the Order Change action.

Recording an Order Change also moves the matching servants in the editor's field display, so later skill codes keep resolving against the right servants. See [Script Team and Field Display](script-team-and-field-display.md).

## Add Command Spells

Tap **Command Spell**. The dialog title shows how many uses remain, such as **Command Spell (2)**.

Tap a spell, then choose a servant target.

| Code | Spell | Effect |
| ---- | ----- | ------ |
| `o` | CS1 | Full NP charge |
| `p` | CS2 | Full HP restore |

Each script can contain up to three command spells. If no uses remain, Script Maker shows **Ran out of Command Spell(s)** instead.

## Add an Attack

Tap **Attack** to open the attack screen.

1. Select up to three cards. Select NP cards for Servant 1, 2, or 3, and Command Cards as needed.
2. Select a Command Card more than once if needed. Each NP card can appear only once.
3. Command Cards fill the empty slots.
4. Tap a card in the sequence to delete it.
5. Tap **Next Turn in same wave** or **Next Wave**.

**Next Turn in same wave** adds the attack and moves to the next turn. **Next Wave** adds the attack and moves to the next wave.

When the team has servants, each NP button shows that servant's face and NP name. The attack sequence shows the same face and NP name for each NP card.

| Code | Meaning |
| ---- | ------- |
| `{` and `}` | Start and end one attack. |
| `4`, `5`, `6` | NP for Servant 1, 2, or 3. |
| `N` | Command Card. |
| `n0`, `n1`, `n2` | Legacy codes for zero, one, or two Command Cards before the NP. |
| `,` | End the turn. |
| `,#,` | End the wave. |

For example, `{4NN},` is one attack in a turn. It uses the NP for Servant 1, and two Command Cards fill the other slots.

## Set Enemy Targets

Open **Settings**. Select the **Enemy Formation**: **3**, **6**, **Raid**, or **Raid v2**. The enemy buttons match the formation.

The **Raid** formation shows the raid boss button on top, and three minion buttons below. The **Raid v2** formation shows the raid boss button on top, and six minion buttons in two rows of three.

- Tap an enemy to add an enemy target action to the command.
- Tap the same enemy again to clear it.

Select an enemy target before you add an action that needs an enemy target. The button label matches the target name in the table. On a small screen, the button shows only the letter or the minion number.

| Code | Target | Formation |
| ---- | ------ | --------- |
| `t1` | Enemy A, left | 3 enemies |
| `t2` | Enemy B, center | 3 enemies |
| `t3` | Enemy C, right | 3 enemies |
| `t[A-L2]` to `t[F-L2]` | Enemy A to Enemy F | 6 enemies |
| `t[RaidBoss-L3]` | Raid boss | Raid |
| `t[RM1-L3]` to `t[RM3-L3]` | Raid minion 1 to 3 | Raid |
| `t[RaidBoss-L4]` | Raid boss | Raid v2 |
| `t[RM1-L4]` to `t[RM6-L4]` | Raid minion 1 to 6 | Raid v2 |

Script Maker writes the codes in the table when you tap an enemy button. It also reads the legacy codes `t4` to `t9` for the 6-enemy formation, and `tR`, `tX`, `tY`, and `tZ` for the Raid formation. A legacy code targets the same enemy as the new code. The Raid v2 formation has no legacy codes.

## Undo, Redo, and Action History

The editor records every change you make. You can undo and redo edits for as long as the editor is open.

- Tap **Undo** to revert the last edit. Tap **Redo** to apply it again.
- Tap **History** to open the Action History pane.

The Action History pane lists every recorded action. The **Current** label marks the state of the script now.

- Tap an earlier entry to restore the script to the state right after that action.
- Tap a later entry to move forward again.
- A dialog opens before a large jump. It states how many actions the restore undoes or redoes. Tap **Confirm** to continue.

Tap **Clear All** in the top bar, then tap **Clear**, to delete every action from the script. Clear All is itself an action, so you can undo it.

## Remaining Commands During a Run

When you pause a battle, the pause screen lists the commands that the current run has not run yet. The list groups commands by wave and turn. A command leaves the list after automation runs it.

## Command Reference

### Servant Skills

| Code | Servant | Skill | Color |
| ---- | ------- | ----- | ----- |
| `a`, `b`, `c` | Servant 1 | Skills 1, 2, 3 | Red |
| `d`, `e`, `f` | Servant 2 | Skills 1, 2, 3 | Blue |
| `g`, `h`, `i` | Servant 3 | Skills 1, 2, 3 | Orange |

### Master Skills and Command Spells

| Code | Action |
| ---- | ------ |
| `j`, `k`, `l` | Master Skills 1, 2, 3 |
| `o` | Command Spell CS1: full NP charge |
| `p` | Command Spell CS2: full HP restore |

### Servant Targets and Special Options

| Code | Meaning |
| ---- | ------- |
| `1`, `2`, `3` | Target Servant 1, 2, or 3 |
| `7`, `8` | Left or right button for a two-option action |
| `K`, `U` | Legacy codes for the first or second option |
| `[Ch2A]`, `[Ch2B]` | Option A or B for a two-choice skill |
| `[Ch3A]`, `[Ch3B]`, `[Ch3C]` | Option A, B, or C for a three-choice skill |
| `[Tfrm]` | Transform action |
| `[x12]` | Order Change target. Use it with Master Skill 3, such as `l[x12]`. |

Some skills need more than one target. Use parentheses for multiple targets. For example, `e([Ch2A]2)` applies skill `e` with option A and servant target 2.

Order Change in older command text can use `x12` without Master Skill 3. Script Maker still reads this form.

## Example Commands

The examples below use command text. The editor writes attacks in braces, such as `{4NN},`. Command text without braces is also valid.

### Three-Wave Farm

```text
abc1jkl,#,def2,#,ghi3
```

- Wave 1: skills `a` and `b`, skill `c` on Servant 1, then Master Skills `j`, `k`, and `l`.
- Wave 2: skills `d` and `e`, skill `f` on Servant 2.
- Wave 3: skills `g` and `h`, skill `i` on Servant 3.

### NP Loop

```text
a1b1c1j1456,#,456,#,456
```

- Wave 1: skills `a`, `b`, and `c` on Servant 1, Master Skill `j` on Servant 1, then NPs 4, 5, and 6.
- Waves 2 and 3: NPs 4, 5, and 6.

### Order Change

```text
a1b1l[x13]k2456,#,456,#,456
```

- Wave 1: skills `a` and `b` on Servant 1.
- Order Change switches front position 1 with back position 3.
- Master Skill `k` on Servant 2, then NPs 4, 5, and 6.
- Waves 2 and 3: NPs 4, 5, and 6.

## Troubleshooting

| Problem | Review |
| ------- | ------ |
| Automation uses a different script | Use the **Active** selector at the top of the script list. |
| A skill uses the wrong target | Review the target chip for the servant row. Review the Smart Target setting and the gesture you used. |
| A skill adds without a target | You did not select a servant target. Tap a target chip before you tap the skill. |
| A skill option screen does not appear | Only skills with special options open the special option screen. |
| A skill button shows a letter, not an icon | The team has no servant in that slot. Or the Atlas data has no skill for that slot. |
| A long press opens a skill description | Skills with Atlas data use the long press for the description. Tap **Use** in the description to add the skill. |
| History rows show the command only | The team changed after you recorded the actions. The rows show Atlas data again when the team matches. |
| Names show in Japanese | The Atlas data has no translation for your language. The app shows the Atlas original. |
| Automation starts at the wrong command | Review the start selector on the script card. The start point applies to the first run only. |
| An enemy button does not appear | Review the **Enemy Formation** setting in **Settings**. |
| Order Change does not select the expected servants | Review the starting and sub members. The command text uses `l[x..]`. |
| Command Spell cannot be added | Each script allows three command spells. Delete one from the script to add another. |
| An edit went wrong | Tap **Undo** to revert it. Or open the Action History pane and restore an earlier state. |
| Automation exits at a turn | Review the **Off-script Exit** and **Out of Commands Exit** settings. |

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) explains how automation executes battle commands.
- [Card Priority](card-priority.md) explains how automation selects face cards.
- [Script Team and Field Display](script-team-and-field-display.md) explains script servant teams, the field display, order changes, and transformations.
