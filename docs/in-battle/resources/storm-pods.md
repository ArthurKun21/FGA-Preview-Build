---
title: Storm Pod Management
description: Automatically turn Ordeal Call Storm Pods on and off for bonus drops. Set pod limits, track usage, and learn how FGA handles Ordeal Call quests.
tags:
    - battle
    - storm-pods
    - ordeal-call
    - events
    - consumables
---

# Storm Pod Management

FGA turns the Ordeal Call Storm Pods on and off for you. Storm Pods give a bonus drop of "Sand of Starlight" on the quest.

## Overview

Ordeal Call quests use Storm Pods. Each Ordeal Call run uses one Storm Pod. When a Storm Pod is on, the quest gives more "Sand of Starlight" drops.

FGA manages the Storm Pods with the same shared workflow as the [teapots](teapots.md). Do these things with FGA:

- Turn the Storm Pod on before a battle starts.
- Turn the Storm Pod off when you do not need it.
- Count each Storm Pod that FGA uses.
- Stop when the pod limit is reached.
- Handle the special Ordeal Call quest end screen.

!!! note
    Storm Pods show only with the teapots. On the party screen, the pods appear in the "Auto Item Use" popup. On the repeat screen, the pods appear in the newer repeat layout. When there is no popup on the party screen, there are no Storm Pods to manage.

## Key Features

- **Automatic On/Off**: FGA reads the pod state on the screen and changes it when it is necessary.
- **Usage Limits**: You set the maximum number of pods to use. The range is 1 to 9.
- **Auto Turn-Off**: FGA turns the pod off when the limit is reached, or on the last run.
- **Budget Restore**: When the limit is used up, FGA restores the default limit. You can then use the limit again on the next session.
- **Ordeal Call Support**: Ordeal Call quests count the pod at a different time. See [Ordeal Call Quests](#ordeal-call-quests).

## The Pod Budget

A pod limit is a budget. Each Ordeal Call run that finishes with the pod on uses one item from the budget.

| Item | Behavior |
| ---- | -------- |
| Budget remaining | The number of pods you can still use this session |
| One use | FGA uses one item each time a run finishes with the pod on |
| Budget at zero | The pod turns off and the limit restores to its default value |
| Default limit | The starting budget that the **Default** button restores |

When the budget reaches zero, FGA does two things in the same step. It turns the pod off, and it restores the limit to the default value. This prevents FGA from turning the pod on again by mistake.

## How FGA Manages Storm Pods

FGA checks the pods at the same two screens as the teapots. These are the party selection screen and the repeat screen.

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
│ Manage pod + teapot │  │ Teapot only           │
│ inside popup,       │  │ (no pods here)        │
│ then close popup    │  │                       │
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
│    • Normal repeat: teapot + pod        │
│    • Ordeal Call repeat: teapot only    │
└─────────────────────────────────────────┘
```

### 1. Party Selection Screen

Before a battle starts, FGA checks the pod state. The pod shows only inside the popup dialog:

1. FGA opens the popup dialog on the party screen.
2. FGA reads the pod state in the popup.
3. FGA turns the pod on when the limit permits it.
4. FGA turns the pod off when the limit is reached, or when the pod is not wanted.
5. FGA closes the popup.

When the popup does not open, FGA does not manage the pods. FGA manages only the teapots in this case.

### 2. Repeat Screen

After a quest completes, FGA reads the pod toggle again. The pod shows only in the newer repeat layout:

- **Normal repeat mode**: The pod shows next to the teapot toggle.
- **Ordeal Call repeat mode**: Only the teapot shows. FGA does not read the pod here.

## Toggle Rules

FGA uses these rules when it finds a pod toggle:

| Pod state | Condition | FGA action |
| --------- | --------- | ---------- |
| On | Not wanted, limit reached, or last run | Count the finished run, then turn the pod off |
| Off | Wanted and the limit is not reached | Turn the pod on |
| On | Wanted and it must stay on | Count the finished run. Turn the pod off if the budget just reached zero |

FGA counts a pod only when it detects a toggle on the screen. This keeps the count correct.

## Configuration

### Enable Storm Pods

You set the pod limit in the Battle Launcher. Do these steps:

1. Open the [Battle Launcher](../../battle-setup/launcher.md).
2. Go to the **Limits** section.
3. Turn on the **Ordeal Call Storm Pods** checkbox.
4. Set the count with the stepper. The range is 1 to 9.

### Pod Limit

| Setting | Behavior |
| ------- | -------- |
| Checkbox off | FGA does not use pods |
| Count 1 to 9 | The maximum number of pods to use this session |

You also set a **Default Ordeal Call Pods** value in the battle config. The **Default** button in the Launcher restores the limit to this value. The range for the default is 1 to 9.

!!! note
    Turn off **Skip Consumables Check** to use the pod limit. When you turn on **Skip Consumables Check**, FGA does not check the consumables state. FGA then also turns off the teapot limit and the pod limit.

## Ordeal Call Quests

Ordeal Call quests use a different flow. After an Ordeal Call quest completes, there is no repeat screen. For this reason, FGA cannot toggle the pod off at the usual time.

FGA does these steps for an Ordeal Call quest:

1. FGA counts the pod at the quest end screen.
2. FGA leaves the pod on, because the end screen does not let you toggle it off.
3. The next run turns the pod off when it is necessary.

```text
Ordeal Call Flow:
Quest Start -> Battle -> Quest End (count here) -> Next Quest

There is no repeat screen between the quests.
```

FGA uses a safety net for the pod and the teapot. If a limit is left at zero or below, FGA turns that consumable off and restores its default value. FGA runs this net at reset time.

See [Teapots](teapots.md) for the Stargazer's Teapot. FGA manages the teapot with the same shared workflow.

## Usage Tracking

### During Session

FGA counts each pod that it uses. The count increases only when FGA detects a pod toggle and a run finishes with the pod on.

```text
┌─────────────────────────────────────────┐
│         Storm Pod Status                │
├─────────────────────────────────────────┤
│ Storm Pods Used: 2                      │
│ Pod Limit: 3                            │
│ Remaining: 1                            │
└─────────────────────────────────────────┘
```

### Exit Summary

After the script completes, the Battle Exit screen shows the pod count. The exit summary shows a chip such as "2 Storm Pod(s) used".

FGA shows this chip only when a pod was detected and counted. If FGA never finds a pod toggle, the chip stays hidden. This is different from the teapots. The teapot count starts at zero, but the pod count stays empty until a pod is involved.

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ Storm Pods Used: 2                      │
│ ...                                     │
└─────────────────────────────────────────┘
```

The [Exit Reasons](../script-control/auto-battle-exit-reasons.md) screen lists every statistic, including the pod count.

## Last Run Handling

When you are on the last run of a limited session, FGA does not waste a pod:

| Scenario | Pod Action |
| -------- | ---------- |
| More runs planned | Keep the pod on for the next run |
| Last run | Turn the pod off after the battle |
| Limit reached | Turn the pod off immediately |

FGA knows that a run is the last run when the run limit is on and the run count is at or above the run limit.

## Tips for Best Results

1. **Match pods to runs**: Set the pod limit to the same value as, or less than, the run limit.
2. **Check your inventory**: Make sure that you have pods before you start.
3. **Monitor usage**: Read the exit summary for the correct count.
4. **Test first**: Run one Ordeal Call quest to make sure that FGA turns the pod on.
5. **Consider the popup**: The pods show only when the popup opens. See [Ordeal Call Quests](#ordeal-call-quests).

## Testing Storm Pod Configuration

Use these test cases to verify the setup:

| Test | Expected Result |
| ---- | --------------- |
| 1 run, 1 pod | FGA turns the pod off after the battle |
| 2 runs, 1 pod | FGA turns the pod off after the 1st battle |
| 1 run, 2 pods | FGA turns the pod off after the battle and leaves 1 pod for the next session |
| 1 run, 0 pods and the pod state is on | FGA turns the pod off before the battle starts |
| 3 Ordeal Call runs, 3 pods | FGA counts all 3 pods at the quest end screens |

## Troubleshooting

### The pod does not turn on

- Make sure that the pod limit is more than zero.
- Make sure that you have pods in your inventory.
- Make sure that the **Ordeal Call Storm Pods** checkbox is on.
- Make sure that **Skip Consumables Check** is off.
- Make sure that you run an Ordeal Call quest.

### The pod count is wrong

- Ordeal Call quests count at the quest end screen.
- FGA counts only the toggles that it detects on the screen.
- Read the exit summary for the correct count.

### The pod stays on after the limit is reached

- This can occur during a screen change.
- FGA corrects the state at the next management point.
- Check the pod state in the popup on the party selection screen.

### The popup is not handled

- Update to the latest FGA version.
- Make sure that the popup is fully visible on the screen.

### The pod state is stuck

- Close and open the quest screen again.
- Toggle the pod state by hand.
- Restart the FGA script.

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Teapots](teapots.md) - Stargazer's Teapot management
- [Battle Launcher](../../battle-setup/launcher.md) - Set the run and pod limits
- [Run Limits](../../app/advanced.md) - Configure run limitations
- [Materials Tracking](../tracking/materials-tracking.md) - Track event drops
