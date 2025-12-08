---
title: Skill Maker Guide
description: Build battle commands visually in FGA Preview. Configure servant skills, master skills, order changes, NP usage, and enemy targeting for automated battles.
tags:
    - battle
    - skills
    - commands
    - configuration
---

# Skill Maker Guide

Build battle commands visually so you do not have to memorize the full command string. This guide walks you through the Skill Maker screen and gives ready-to-use references for every button.

---

## Overview

The Skill Maker is FGA's visual command builder. Instead of typing complex command strings like `abc1jkl456` by hand, you tap buttons to build commands step by step. Each tap adds an entry to the command string that the Battle script executes during automated gameplay.

**What problem does it solve?**

- Eliminates the need to memorize skill codes (`a-i` for servants, `j-l` for master)
- Prevents typos and syntax errors in command strings
- Provides a visual history of your commands for easy editing
- Shows real-time wave and turn tracking as you build

**Who should use it?**

Every FGA user who wants to automate battles with specific skill rotations. Whether you are setting up a simple 3-turn farm or a complex looping setup with Order Changes, the Skill Maker makes command creation intuitive.

---

## Key Features

- **Visual command building**: Tap buttons instead of typing codes
- **Color-coded skills**: Red for Servant 1, yellow for Servant 2, blue for Servant 3
- **Smart targeting**: Double-tap skills that need targets to open a selection menu
- **History bar**: Scroll through and edit commands you have already added
- **Wave and turn tracking**: See exactly where you are in the battle sequence
- **Support for special skills**: Transform skills, choice skills, and NP type changes
- **Order Change support**: Easily swap front-line and back-line servants
- **Multiple enemy formations**: Handle 3-enemy, 6-enemy, and raid battles

---

## How to Access

1. Open FGA settings.
2. Go to **Battle Config** → **Skill Command**.
3. Tap **Edit** to launch the Skill Maker screen.

---

## Screen Layout

```text
┌─────────────────────────────────────────────────────────────┐
│  [Save]        [Settings] [Wave/Turn]    [Delete] [Clear]   │
├─────────────────────────────────────────────────────────────┤
│  Command History Bar (scrollable)                           │
│  [Start] → [a] → [b] → [c] → [1] → [,] → ...               │
├─────────────────────────────────────────────────────────────┤
│                    Enemy Targets                            │
│              [Enemy 1] [Enemy 2] [Enemy 3]                  │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┬──────────────┬──────────────┐            │
│  │  SERVANT 1   │  SERVANT 2   │  SERVANT 3   │            │
│  │  [S1][S2][S3]│  [S1][S2][S3]│  [S1][S2][S3]│            │
│  └──────────────┴──────────────┴──────────────┘            │
├─────────────────────────────────────────────────────────────┤
│  [Master Skills]    [Order Change]    [Command Spells]      │
│                                                             │
│           [Attack]  ←  Main action buttons  →  [End Turn]   │
└─────────────────────────────────────────────────────────────┘
```

- **Top bar**: Save the command, open settings, see the current wave/turn, or delete/clear entries.
- **History bar**: Scroll through every entry you have added; tap to select one for editing.
- **Enemy targets**: Set the current enemy target before adding skills or attacks.
- **Servant rows**: Tap servant skills, then add targets when needed.
- **Master bar**: Use Mystic Code skills, Order Change, and Command Spells.
- **Action row**: Add attacks, Noble Phantasms (NPs), cards before NPs, and end turns.

---

## Understand How Command Strings Are Built

Each tap appends a code to the command string that FGA runs during battle. Example command:

```text
abc1jkl2456,
```

| Segment | Meaning |
| ------- | ------- |
| `ab` | Use Servant 1 skills 1, 2 |
| `c1` | Use Servant 1 skill 3 to target servant A (front position) |
| `jk` | Use Master skills 1, 2 |
| `l2` | Use Master skill 3 to target servant B (second position) |
| `456` | Fire all three NPs |
| `,` | End turn |

!!! tip "Command Flow"
    The command runs left to right. End each turn with `,` or use `,#,` when you expect a wave change.

---

## Build Commands Step by Step

### Use Servant Skills With or Without Targets

- Single tap a servant skill to add it without a target.
- Double tap to open target selection when the skill needs a target.
- Color coding keeps skills easy to spot: red for Servant 1 (`a`, `b`, `c`), yellow for Servant 2 (`d`, `e`, `f`), blue for Servant 3 (`g`, `h`, `i`).

### Aim Skills at Allies or Options

1. Double tap the skill button.
2. Pick the target servant (A, B, or C).
3. If the skill has special options, choose from Transform, Choice, or NP Type Change when prompted.

### Trigger Master Skills from the Mystic Code

Tap **Master Skills** and pick:

- `j` for Mystic Code skill 1.
- `k` for Mystic Code skill 2.
- `l` for Mystic Code skill 3.

Some Master skills ask for a target—select one when prompted.

### Swap Servants with Order Change

1. Tap **Order Change**.
2. Select the starting (front) servant: 1, 2, or 3.
3. Select the sub (back) servant: 1, 2, or 3.
4. Confirm to add `x[start][sub]` (for example, `x13` swaps front 1 with back 3).

### Spend Command Spells Carefully

Tap **Command Spells** to add:

| Code | Spell | Effect |
| ---- | ----- | ------ |
| `o` | CS1 | Full NP charge (choose a servant) |
| `p` | CS2 | Full HP heal (choose a servant) |

!!! warning "Limited Resource"
    Command Spells are limited to 3 per day; only add them when you truly need them.

### Pick Enemies Before Firing Skills or NPs

1. Tap an enemy target button (Enemy 1, 2, or 3 or raid-specific buttons when shown).
2. The choice stays active until you change it, so you can add several skills aimed at the same target.

### End Turns and Set Attacks from the Action Row

- Tap **Attack** to open NP selection and card options.
- Select NPs to fire this turn: `4` (Servant 1), `5` (Servant 2), `6` (Servant 3).
- Choose cards before NP: `n0` (none), `n1` (one card), or `n2` (two cards).
- Finish the turn with `,` or finish the wave with `,#,`.

### Handle Special Skill Behaviors

- **Transform skills**: double tap, choose the NP type, and add `[Tfrm]`.
- **Choice skills with 2 options**: pick `[Ch2A]` or `[Ch2B]`.
- **Choice skills with 3 options**: pick `[Ch3A]`, `[Ch3B]`, or `[Ch3C]`.
- **NP type change with 2 options**: use `7` (left) or `8` (right).
- **NP type change with 3 options**: pick from the on-screen options when prompted.

### Target Multiple Skills When Needed

Use parentheses to add one skill that uses multiple skill targets. For example:

```text
b([Ch2B]2)
```

This example targets servants `[Ch2B]` and `2` with skill `b`. This example with multiple skill target is from Kukulcan's 2nd skill, which uses both a choice option and a target.

---

## Reference Tables

### Servant Skills

| Code | Servant | Skill |
| ---- | ------- | ----- |
| `a` | Servant 1 | Skill 1 |
| `b` | Servant 1 | Skill 2 |
| `c` | Servant 1 | Skill 3 |
| `d` | Servant 2 | Skill 1 |
| `e` | Servant 2 | Skill 2 |
| `f` | Servant 2 | Skill 3 |
| `g` | Servant 3 | Skill 1 |
| `h` | Servant 3 | Skill 2 |
| `i` | Servant 3 | Skill 3 |

### Master Skills (Mystic Code)

| Code | Skill |
| ---- | ----- |
| `j` | Master Skill 1 |
| `k` | Master Skill 2 |
| `l` | Master Skill 3 |

### Command Spells

| Code | Effect |
| ---- | ------ |
| `o` | Full NP charge (single servant) |
| `p` | Full HP heal (single servant) |

### Noble Phantasms

| Code | NP |
| ---- | -- |
| `4` | Servant 1 NP |
| `5` | Servant 2 NP |
| `6` | Servant 3 NP |

### Skill Targets

| Code | Target |
| ---- | ------ |
| `1` | Target Servant A (position 1) |
| `2` | Target Servant B (position 2) |
| `3` | Target Servant C (position 3) |
| `7` | Left option (NP type change or 2-option skills) |
| `8` | Right option (NP type change or 2-option skills) |

### Enemy Targets

| Code | Target | Formation |
| ---- | ------ | --------- |
| `t1` | Enemy 1 (left) | 3-enemy |
| `t2` | Enemy 2 (center) | 3-enemy |
| `t3` | Enemy 3 (right) | 3-enemy |
| `t4` | Enemy A | 6-enemy |
| `t5` | Enemy B | 6-enemy |
| `t6` | Enemy C | 6-enemy |
| `t7` | Enemy D | 6-enemy |
| `t8` | Enemy E | 6-enemy |
| `t9` | Enemy F | 6-enemy |
| `tR` | Raid Boss | Raid |
| `tX` | Raid Minion 1 | Raid |
| `tY` | Raid Minion 2 | Raid |
| `tZ` | Raid Minion 3 | Raid |

### Special Commands

| Code | Action |
| ---- | ------ |
| `x` | Order Change (followed by starting + sub position) |
| `n` | Cards before NP (followed by count 0-2) |
| `,` | End turn (same wave) |
| `,#,` | End wave (next wave) |

### Special Skill Targets

| Code | Usage |
| ---- | ----- |
| `[Ch2A]` | Choice skill Option A (2-choice skills) |
| `[Ch2B]` | Choice skill Option B (2-choice skills) |
| `[Ch3A]` | Choice skill Option A (3-choice skills) |
| `[Ch3B]` | Choice skill Option B (3-choice skills) |
| `[Ch3C]` | Choice skill Option C (3-choice skills) |
| `[Tfrm]` | Transform skill |

### Multi-Target Syntax

| Syntax | Meaning |
| ------ | ------- |
| `([Ch2B]2)` | Target multiple skill targets, such as a choice option and a servant |

---

## Edit or Restore Entries from the History Bar

- Tap any entry to highlight it, then use **Delete** to remove it or **Clear** to remove everything after it.
- Long press to reorder entries when you want to move a skill earlier in the turn.
- Use the navigation arrows to scroll through long commands without losing your place.

---

## Tune Settings for Targeting and Formation

Open **Settings** from the top bar:

| Setting | Description |
| ------- | ----------- |
| **Smart Target** | Remembers the last target you used for each skill type to save taps. |
| **Enemy Formation** | Choose 3-enemy, 6-enemy, or raid to match the battle so targeting buttons stay accurate. |

---

## Example Command Strings

### Simple 3-Turn Farm

```text
abc1jkl,#,def2,#,ghi3
```

- Wave 1: Servant 1 skills 1 and 2 on (self/all/no target) and skill 3 on target A, then Master skills.
- Wave 2: Servant 2 skills 1 and 2 on (self/all/no target) and skill 3 on target B.
- Wave 3: Servant 3 skills 1 and 2 on (self/all/no target) and skill 3 on target C.

### Looping Setup

```text
a1b1c1j1456,#,456,#,456
```

- Wave 1: All Servant 1 skills at target A, Master skill 1 at target A, all NPs.
- Wave 2: All NPs.
- Wave 3: All NPs.

### With Order Change Mid-Battle

```text
a1b1x13k2456,#,456,#,456
```

- Wave 1: Servant 1 skills (a, b) at target A, swap front 1 with back 3, Master skill 2 at target B, all NPs.
- Waves 2 and 3: All NPs.

---

## Tips for Best Results

1. **Start with simple commands**: Begin with basic skill sequences before adding Order Changes or special skills. Test each wave independently to ensure it works.

2. **Use the history bar for editing**: Tap any entry in the history bar to select it, then use **Delete** to remove just that entry or **Clear** to remove everything after it.

3. **Double-tap for targeted skills**: When a skill needs a target (like single-target buffs), double-tap the skill button to open the target selection menu instead of single-tapping.

4. **Match enemy formation settings**: Before building commands, set the **Enemy Formation** in settings to match the battle (3-enemy, 6-enemy, or raid) so targeting buttons appear correctly.

5. **Save frequently**: Tap **Save** often while building complex commands. If you make a mistake, you can reload your last saved version instead of starting over.

---

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| Skills do not execute during battle | Check that skill cooldowns are available. Confirm the target you selected matches your actual party order in the game. |
| Wrong servant gets targeted | Verify target codes `1`, `2`, `3` match your current front-line positions. Remember that Order Change affects positions. |
| Command string is too long to manage | Split complex setups into separate battle configs. Use one config per farming node for easier maintenance. |
| NP does not fire when expected | Confirm NP codes `4`, `5`, `6` are included in the turn. Check that the servant's NP gauge is full before executing. |
| Order Change does not swap servants | Verify you selected both a starting position (1-3) and a sub position (1-3). The format should be `x[start][sub]`, for example `x13`. |
| Enemy targeting seems off | Check the **Enemy Formation** setting matches the actual battle. Use `t1`, `t2`, `t3` for standard 3-enemy battles. |
| Special skill options not appearing | For choice skills, double-tap the skill to open the extended menu with `[Ch2A]`, `[Ch2B]`, or 3-option variants. |

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) — Explains how the battle automation runs the command string.
- [Card Priority](card-priority.md) — Covers how face cards are chosen when NP is not used.
