---
title: Skill Maker Guide
description: Create and manage battle scripts in FGA Preview. Set skills, attacks, targets, Master Skills, and start points for automated battles.
tags:
    - battle
    - skills
    - commands
    - configuration
---

# Skill Maker Guide

Skill Maker creates battle scripts. A battle script is a list of commands. Automation runs the commands during a battle.

A battle config can contain several scripts. One script is active for each battle. Each script has its own commands, name, notes, start point, and Mystic Code.

## Open Skill Maker

1. Open a battle config.
2. In **Battle Scripts**, tap the script card.

Skill Maker opens the script list. Tap a script to open its editor.

## Manage the Script List

The script list lists the exit settings and every script. Each script card has these items:

| Item | Use |
| ---- | --- |
| **Active** | Select the script that automation uses. Only one script is active. |
| **Delete** | Delete the script. This item appears only when the config has more than one script. |
| **Notes** | Add or edit the notes for the script. |
| **Edit** | Open the command text editor for the script. |

Each card also contains a summary of the commands by wave and turn, and the start selector.

Use the toolbar at the bottom of the list:

- **Add** creates a script.
- The up and down arrows open the previous or next script.

## Rename a Script

Tap the script name in the editor title bar. Enter a name, then tap **Confirm**. The name cannot be blank. A script without a name uses its position, such as **Script 2**.

## Set Exit Settings

The battle config has two exit settings. The script list lists them at the top.

- **Out of Commands Exit** ends the battle when the script has no commands left.
- **Off-script Exit** ends the battle when the battle reaches a wave or turn that the script does not define.

## Set the Start Point

The start point sets where automation starts a script. Use the start selector on the script card.

- The start point applies to the first run only. Later runs start at the first command.
- If the start point is no longer valid, automation starts at the first command.
- Saving the command text resets the start point to the first command.

## Save Changes

The editor saves your changes when you tap **Back**. The editor has no Save button for skills and targets.

The command text editor has its own **Save** button. See [Edit Command Text](#edit-command-text).

## Editor Layout

```text
┌──────────────────────────────────────────────────────────┐
│ [Script name]          [Settings] [Delete] [Clear All]   │
├──────────────────────────────────────────────────────────┤
│ Wave and turn indicator | Action history                 │
├──────────────────────────────────────────────────────────┤
│ Enemy targets                                            │
├──────────────────────────────────────────────────────────┤
│ Servant 1 [target chip] [a] [b] [c]                      │
│ Servant 2 [target chip] [d] [e] [f]                      │
│ Servant 3 [target chip] [g] [h] [i]                      │
│ Gesture hint                                             │
├──────────────────────────────────────────────────────────┤
│ [Command Spell] [Master Skills] [Order Change] [Attack]  │
└──────────────────────────────────────────────────────────┘
```

- **Top bar**: Rename the script, open **Settings**, delete the selected action, or clear all actions.
- **Action history**: Lists the actions of the script. Tap an action to select it.
- **Wave and turn indicator**: Displays the wave and turn of the selected action.
- **Enemy targets**: Contains the enemy buttons for the selected enemy formation.
- **Servant rows**: Contain the skill buttons and target chips for each servant.
- **Bottom bar**: Opens Command Spell, Master Skills, Order Change, and Attack.

The layout changes to fit the screen size.

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

### Choose a Target

**Choose Target** lists **Servant 1**, **Servant 2**, **Servant 3**, and **No Target**. Select one option to add the skill with that target.

### Select Special Options

Some skills have extra options. Skill Maker opens a special option screen for these skills. Options can include:

- A choice between two or three options.
- An NP type change with two or three types.
- A transform.

For some servants, the screen has a card grid. Tap a card to select it. Tap the selected card again to clear it. Follow the label above the cards.

Some skills need a special option and a target. Parentheses hold both. For example, `e([Ch2A]2)`.

## Configure Master Skills

Tap **Master Skills** to open the Master Skills screen. The **Mystic Code** row contains the Mystic Code of the script.

- Tap **Mystic Code** to choose a Mystic Code from the Atlas data. The selected code displays its skill names and icon.
- Use **Display options** to change how the Mystic Code icon appears.
- Clear the selection to use the default Master Skill buttons. The row displays **No mystic code set** when you select no code.

Master Skill codes are `j`, `k`, and `l`. Each Master Skill uses the target type that the Atlas data defines for it.

| Target type | Result |
| ----------- | ------ |
| No target | Adds the skill at once. |
| One servant | The direct gesture adds the skill with the selected servant. The other gesture opens **Choose Target** with Servant 1, 2, and 3 only. |
| Order Change | Opens **Order Change**. |
| Special option | Opens the special option screen. |

## Set Order Change

Tap **Order Change** in the bottom bar.

1. Select the starting member. This servant is in the front line.
2. Select the sub member. This servant is in the back line.
3. Tap **Ok** to add the action. Tap **Cancel** to close the screen without a change.

The command text is `l[x13]`. Master Skill 3 switches front position 1 with back position 3.

If the last action is a bare `l` (Master Skill 3 with no target), Skill Maker deletes it before it adds the Order Change action.

## Add Command Spells

Tap **Command Spell**. The dialog title displays how many uses remain, such as **Command Spell (2)**.

Tap a spell, then choose a servant target.

| Code | Spell | Effect |
| ---- | ----- | ------ |
| `o` | CS1 | Full NP charge |
| `p` | CS2 | Full HP restore |

Each script can contain up to three command spells. If no uses remain, Skill Maker displays **Ran out of Command Spell(s)** instead.

## Add an Attack

Tap **Attack** to open the attack screen.

1. Select up to three cards. Select NP cards for Servant 1, 2, or 3, and Command Cards as needed.
2. Select a Command Card more than once if needed. Each NP card can appear only once.
3. Command Cards fill the empty slots.
4. Tap a card in the sequence to delete it.
5. Tap **Next Turn in same wave** or **Next Wave**.

**Next Turn in same wave** adds the attack and moves to the next turn. **Next Wave** adds the attack and moves to the next wave.

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

Open **Settings** and select the **Enemy Formation**: **3**, **6**, or **Raid**. The enemy buttons match the formation.

- Tap an enemy to add an enemy target action to the command.
- Tap the same enemy again to clear it.

Select an enemy target before you add an action that needs one.

| Code | Target | Formation |
| ---- | ------ | --------- |
| `t1` | Enemy 1, left | 3 enemies |
| `t2` | Enemy 2, center | 3 enemies |
| `t3` | Enemy 3, right | 3 enemies |
| `t4` to `t9` | Enemies A to F | 6 enemies |
| `tR` | Raid boss | Raid |
| `tX` | Raid minion 1 | Raid |
| `tY` | Raid minion 2 | Raid |
| `tZ` | Raid minion 3 | Raid |

## Edit the Action History

- Tap an action to select it.
- Tap the up or down arrow to move the selected action earlier or later.
- Tap **Delete** in the top bar to delete the selected action.
- Tap **Clear All**, then tap **Clear** to delete every action from the script.

## Edit Command Text

Use the command text editor to change the command text by wave and turn.

1. Open the script list.
2. Tap **Edit** on the script card.
3. Change the text in a wave or turn card.
4. Tap **Save** in the top bar.

- **Add Wave** adds a wave with one empty turn.
- **Add Turn** adds a turn to the last wave.
- The delete icon on a card deletes that turn. A wave without turns is also deleted. You cannot delete the last turn.
- An error message appears on the card that has the error. A banner lists errors for the whole command, such as more than three command spells.
- You cannot tap **Save** while an error exists.
- Saving resets the start point to the first command.

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

Order Change in older command text can use `x12` without Master Skill 3. Skill Maker still reads this form.

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
| Automation uses a different script | Select **Active** on the script that you want in the script list. |
| A skill uses the wrong target | Review the target chip for the servant row. Review the Smart Target setting and the gesture you used. |
| A skill adds without a target | You did not select a servant target. Tap a target chip before you tap the skill. |
| A skill option screen does not appear | Only skills with special options open the special option screen. |
| Automation starts at the wrong command | Review the start selector on the script card. The start point applies to the first run only. |
| An enemy button does not appear | Review the **Enemy Formation** setting in **Settings**. |
| Order Change does not select the expected servants | Review the starting and sub members. The command text uses `l[x..]`. |
| Command Spell cannot be added | Each script allows three command spells. Delete one from the script to add another. |
| The text editor cannot save | Fix the error shown on the card or in the banner. You cannot tap **Save** until you fix the error. |
| Automation exits at a turn | Review the **Off-script Exit** and **Out of Commands Exit** settings. |

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) explains how automation executes battle commands.
- [Card Priority](card-priority.md) explains how automation selects face cards.
