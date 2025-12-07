---
title: Skill Execution During Battle
description: How FGA casts servant skills, master skills, and command spells during combat. Understand skill targeting and order changes.
tags:
    - battle
    - skills
    - commands
    - automation
---

# Skill Execution During Battle

Automatic casting of servant skills, master skills, and command spells.

## Overview

FGA executes your configured skill commands during battle, handling all the UI interactions needed to activate skills, select targets, and wait for animations. This includes servant skills, master skills from your Mystic Code, and even Command Spells for emergency situations.

## Key Features

- **Servant Skills**: Cast skills from your three field servants
- **Master Skills**: Use Mystic Code abilities
- **Command Spells**: Emergency revival and buffs
- **Target Selection**: Automatically select skill targets
- **Order Change**: Swap servants mid-battle
- **Animation Handling**: Wait for skill effects to complete

## Skill Types

### Servant Skills

Each servant has three skills (S1, S2, S3):

| Skill Position    | Command |
| ----------------- | ------- |
| Servant A Skill 1 | a1      |
| Servant A Skill 2 | a2      |
| Servant A Skill 3 | a3      |
| Servant B Skill 1 | b1      |
| Servant C Skill 3 | c3      |

### Master Skills

Your Mystic Code provides three skills:

| Skill Position | Command      |
| -------------- | ------------ |
| Master Skill 1 | j1 / master1 |
| Master Skill 2 | j2 / master2 |
| Master Skill 3 | j3 / master3 |

### Command Spells

For emergencies (limited uses):

| Spell | Effect              |
| ----- | ------------------- |
| CS1   | Varies by selection |
| CS2   | Varies by selection |
| CS3   | Varies by selection |

## Skill Execution Flow

```text
┌─────────────────────────────────────────┐
│        Skill Command Received           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Click Skill Button                   │
│    (Servant portrait or Master button)  │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Check for Target Selection           │
│    Does skill need a target?            │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Needs Target?           │ No
         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│  Select Target  │    │  Skill Activates│
│  (A, B, or C)   │    │  Immediately    │
└────────┬────────┘    └────────┬────────┘
         │                      │
         └──────────┬───────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│    Wait for Animation                   │
│    Battle screen to reappear            │
└─────────────────────────────────────────┘
```

## Target Selection

### Ally Targets

For skills that target allies:

| Target | Position       | Command Modifier |
| ------ | -------------- | ---------------- |
| A      | Left servant   | (a)              |
| B      | Center servant | (b)              |
| C      | Right servant  | (c)              |

Example: `a1(b)` = Servant A's Skill 1 targeting Servant B

### Enemy Targets

For skills that target enemies:

| Target | Position     |
| ------ | ------------ |
| 1      | Left enemy   |
| 2      | Center enemy |
| 3      | Right enemy  |

### Multi-Target Skills

Some skills allow multiple targets:

```text
Example: Skill with 2 targets
Command: a2(a)(b)

First target: Servant A
Second target: Servant B
```

## Order Change (Servant Swap)

Swap a field servant with a backup:

### Command Format

```text
x[starting][sub]

starting: Field position (1-3)
sub: Backup position (1-3)

Example: x23 = Swap field position 2 with backup position 3
```

### Swap Process

```text
┌─────────────────────────────────────────┐
│    Click Master Skill (Order Change)    │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Select Field Servant                 │
│    (Position to swap out)               │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Select Backup Servant                │
│    (Position to swap in)                │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Confirm Swap                         │
│    Update servant tracking              │
└─────────────────────────────────────────┘
```

## Skill Confirmation Dialog

Some skills show a confirmation dialog:

```text
┌─────────────────────────────────────────┐
│    Use this skill?                      │
│                                         │
│    [ Cancel ]    [ OK ]                 │
└─────────────────────────────────────────┘
```

FGA handles these automatically:

- Detects confirmation dialog
- Clicks OK to confirm
- Continues with next action

## Animation Waiting

After skill activation:

1. FGA waits for battle screen to disappear
2. Skill animation plays
3. FGA waits for battle screen to return
4. Continues with next command

### Timeout Handling

- Default wait: 5 seconds
- If screen doesn't return, may retry
- Prevents soft-locks from slow animations

## Using Command Spells

### Opening the Menu

```text
┌─────────────────────────────────────────┐
│    Click Command Spell icon             │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Wait for menu to open                │
│    Verify Cancel button visible         │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Select specific spell                │
│    Handle targets if needed             │
└─────────────────────────────────────────┘
```

### Available Spells

| Spell     | Typical Use                   |
| --------- | ----------------------------- |
| NP Charge | 100% NP for one servant       |
| Heal      | Restore HP                    |
| Revive    | Resurrect party (if defeated) |

## Special Skill Handling

### Transform Skills (Mélusine)

When a servant transforms:

1. FGA detects transformation
2. Updates servant tracking
3. Recaptures new skill icons
4. Continues normally

### Skills with Multiple Effects

Some skills have multiple phases:

1. First effect activates
2. May need second target selection
3. FGA handles each phase

## Tips for Best Results

1. **Test skill commands**: Verify timing before long sessions
2. **Account for animations**: Some skills have long animations
3. **Check skill availability**: Ensure skills aren't on cooldown
4. **Order matters**: Skills execute in command order
5. **Verify targets**: Confirm target syntax is correct

## Common Skill Command Patterns

### Standard Buff Setup

```text
Wave 1: a1, b1, c1
(All servants use Skill 1)
```

### Boss Wave Setup

```text
Wave 3: master1(a), a1, a2, a3, b2(a)
(Master buffs A, A uses all skills, B targets A)
```

### Order Change Pattern

```text
Wave 1: a1, a2, x13, ...
(A uses skills, then swaps with backup 3)
```

## Troubleshooting

### Skill not being cast

- Check if skill is on cooldown
- Verify command syntax is correct
- Ensure servant has enough NP/resources

### Wrong target selected

- Check target syntax (a, b, c)
- Verify servant positions haven't changed
- Order change may have moved servants

### Animation timeout

- Slow device may need longer wait
- Some skills have extended animations
- Check network connection

### Skill confirmation not handled

- FGA detects and handles automatically
- May fail on unusual dialog layouts
- Check if game version is supported

### Order change fails

- Verify backup position exists
- Check if servant isn't defeated
- Ensure Master Skill includes Order Change

## Related Documentation

- [Skill Maker](../../battle-setup/skill-maker.md) - Create skill commands
- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Servant Tracking](../tracking/servant-tracking.md) - Position tracking
