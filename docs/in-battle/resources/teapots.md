---
title: Teapot Management
description: Automatically turn the Stargazer's Teapot on and off for a Bond Gained x2 bonus. Set teapot limits, track usage, and learn how FGA handles Ordeal Call quests.
tags:
    - battle
    - teapots
    - events
    - bond
    - consumables
---

# Teapot Management

FGA turns the Stargazer's Teapot on and off for you. This gives the whole party a Bond Gained x2 bonus on the quest.

## Overview

A teapot gives a Bond Gained x2 bonus when a quest completes. The bonus applies to the full party. It also applies to the sub-members.

FGA can do these tasks for you:

- Turn the teapot on before a battle starts.
- Turn the teapot off when you do not need it.
- Count each teapot that FGA uses.
- Stop when the teapot limit is reached.
- Handle the special Ordeal Call quest end screen.

## Key Features

- **Automatic On/Off**: FGA reads the teapot state on the screen and changes it when it is necessary.
- **Usage Limits**: You set the maximum number of teapots to use.
- **Auto Turn-Off**: FGA turns the teapot off when the limit is reached, or on the last run.
- **Budget Restore**: When the limit is used up, FGA restores the default limit. You can then use the limit again on the next session.
- **Ordeal Call Support**: Ordeal Call quests count the teapot at a different time. See [Ordeal Call Quests](#ordeal-call-quests).

## The Teapot Budget

A teapot limit is a budget. Each battle that finishes with the teapot on uses one item from the budget.

| Item | Behavior |
| ---- | -------- |
| Budget remaining | The number of teapots you can still use this session |
| One use | FGA uses one item each time a run finishes with the teapot on |
| Budget at zero | The teapot turns off and the limit restores to its default value |
| Default limit | The starting budget that the **Default** button restores |

When the budget reaches zero, FGA does two things in the same step. It turns the teapot off, and it restores the limit to the default value. This prevents FGA from turning the teapot on again by mistake.

## How FGA Manages Teapots

FGA checks the teapot at two screens. These are the party selection screen and the repeat screen.

```text
┌─────────────────────────────────────────┐
│        Party Selection Screen           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Does the popup dialog open?          │
└──────────┬───────────────────┬──────────┘
           │ Yes               │ No
           ▼                   ▼
┌─────────────────────┐  ┌───────────────────────┐
│ Manage teapot and   │  │ Manage teapot only    │
│ storm pod in popup  │  │ on the party screen   │
│ Then close popup    │  │ (no storm pods here)  │
└──────────┬──────────┘  └───────────┬───────────┘
           │                         │
           └────────────┬────────────┘
                        ▼
┌─────────────────────────────────────────┐
│             Battle Runs                 │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Repeat Screen                        │
│    • Normal repeat: teapot + storm pod  │
│    • Ordeal Call repeat: teapot only    │
└─────────────────────────────────────────┘
```

### 1. Party Selection Screen

Before a battle starts, FGA does these steps:

1. FGA reads the current teapot state.
2. FGA checks the config and the run progress.
3. FGA turns the teapot on when the limit permits it.
4. FGA turns the teapot off when the limit is reached, or when the teapot is not wanted.

Some servers show a popup dialog on the party screen. This is the "Auto Item Use" popup. When this popup opens, FGA manages the teapot and the [storm pods](storm-pods.md) inside the popup. FGA then closes the popup. When the popup does not open, FGA manages the teapot directly on the party screen. There are no storm pods in this case.

### 2. Repeat Screen

After a quest completes, FGA reads the teapot toggle again. The toggle is in a different place on each repeat layout:

- **Normal repeat mode**: The teapot shows next to the storm pod toggle.
- **Ordeal Call repeat mode**: Only the teapot shows.

FGA uses the correct spot for the layout that it finds.

## Toggle Rules

FGA uses these rules when it finds a teapot toggle:

| Teapot state | Condition | FGA action |
| ------------ | --------- | ---------- |
| On | Not wanted, limit reached, or last run | Count the finished run, then turn the teapot off |
| Off | Wanted and the limit is not reached | Turn the teapot on |
| On | Wanted and it must stay on | Count the finished run. Turn the teapot off if the budget just reached zero |

FGA counts a teapot only when it detects a toggle on the screen. This keeps the count correct.

## Configuration

### Enable Teapots

You set the teapot limit in the Battle Launcher. Do these steps:

1. Open the [Battle Launcher](../../battle-setup/launcher.md).
2. Go to the **Limits** section.
3. Turn on the **Teapots** checkbox.
4. Set the count with the stepper.

### Teapot Limit

| Setting | Behavior |
| ------- | -------- |
| Checkbox off | FGA does not use teapots |
| Count 1 to 999 | The maximum number of teapots to use this session |

You also set a **Default Teapots** value in the battle config. The **Default** button in the Launcher restores the limit to this value. The range for the default is 1 to 300.

!!! note
    Turn off **Skip Consumables Check** to use the teapot limit. When you turn on **Skip Consumables Check**, FGA does not check the consumables state. FGA then also turns off the teapot limit and the storm pod limit.

## Ordeal Call Quests

Ordeal Call quests use a different flow. After an Ordeal Call quest completes, there is no repeat screen. For this reason, FGA cannot toggle the teapot off at the usual time.

FGA does these steps for an Ordeal Call quest:

1. FGA counts the teapot at the quest end screen.
2. FGA leaves the teapot on, because the end screen does not let you toggle it off.
3. The next run turns the teapot off when it is necessary.

```text
Ordeal Call Flow:
Quest Start -> Battle -> Quest End (count here) -> Next Quest

There is no repeat screen between the quests.
```

FGA uses a safety net for the teapot and the storm pod. If a limit is left at zero or below, FGA turns that consumable off and restores its default value. FGA runs this net at reset time.

See [Storm Pods](storm-pods.md) for the Ordeal Call pods. FGA manages the pods with the same shared workflow.

## Usage Tracking

### During Session

FGA counts each teapot that it uses. The count increases only when FGA detects a teapot toggle and a run finishes with the teapot on.

```text
┌─────────────────────────────────────────┐
│         Teapot Status                   │
├─────────────────────────────────────────┤
│ Teapots Used: 3                         │
│ Teapot Limit: 10                        │
│ Remaining: 7                            │
└─────────────────────────────────────────┘
```

### Exit Summary

After the script completes, the Battle Exit screen shows the teapot count. The exit summary shows a chip such as "3 Teapot(s) used". FGA shows this chip only when the count is more than zero.

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ Teapots Used: 5                         │
│ ...                                     │
└─────────────────────────────────────────┘
```

The [Exit Reasons](../script-control/auto-battle-exit-reasons.md) screen lists every statistic, including the teapot count.

## Last Run Handling

When you are on the last run of a limited session, FGA does not waste a teapot:

| Scenario | Teapot Action |
| -------- | ------------- |
| More runs planned | Keep the teapot on for the next run |
| Last run | Turn the teapot off after the battle |
| Limit reached | Turn the teapot off immediately |

FGA knows that a run is the last run when the run limit is on and the run count is at or above the run limit.

## Tips for Best Results

1. **Match teapots to runs**: Set the teapot limit to the same value as, or less than, the run limit.
2. **Check your inventory**: Make sure that you have teapots before you start.
3. **Monitor usage**: Read the exit summary for the correct count.
4. **Test first**: Run one quest to make sure that FGA turns the teapot on.
5. **Consider Ordeal Call**: The special timing can change the count. See [Ordeal Call Quests](#ordeal-call-quests).

## Testing Teapot Configuration

Use these test cases to verify the setup:

| Test | Expected Result |
| ---- | --------------- |
| 1 run, 1 teapot | FGA turns the teapot off after the battle |
| 2 runs, 1 teapot | FGA turns the teapot off after the 1st battle |
| 1 run, 2 teapots | FGA turns the teapot off after the battle and leaves 1 teapot for the next session |
| 1 run, 0 teapots and the teapot state is on | FGA turns the teapot off before the battle starts |
| 3 Ordeal Call runs, 3 teapots | FGA counts all 3 teapots at the quest end screens |

## Troubleshooting

### The teapot does not turn on

- Make sure that the teapot limit is more than zero.
- Make sure that you have teapots in your inventory.
- Make sure that the **Teapots** checkbox is on.
- Make sure that **Skip Consumables Check** is off.

### The teapot count is wrong

- Ordeal Call quests count at the quest end screen.
- FGA counts only the toggles that it detects on the screen.
- Read the exit summary for the correct count.

### The teapot stays on after the limit is reached

- This can occur during a screen change.
- FGA corrects the state at the next management point.
- Check the teapot state on the party selection screen.

### The popup is not handled

- Update to the latest FGA version.
- Make sure that the popup is fully visible on the screen.

### The teapot state is stuck

- Close and open the quest screen again.
- Toggle the teapot state by hand.
- Restart the FGA script.

## Server Differences

| Server | Party Screen | Repeat Screen | Notes |
| ------ | ------------ | ------------- | ----- |
| NA/EN | Auto Item Use popup with teapot and storm pod | Teapot next to the storm pod | New layout |
| JP | Teapot toggle on the party screen bar only | Teapot only | No popup for the teapot |

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Storm Pods](storm-pods.md) - Ordeal Call storm pod management
- [Battle Launcher](../../battle-setup/launcher.md) - Set the run and teapot limits
- [Run Limits](../../app/advanced.md) - Configure run limitations
- [Materials Tracking](../tracking/materials-tracking.md) - Track event drops
