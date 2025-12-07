---
title: Battle Withdrawal and Retreat
description: Handle battle withdrawal in FGA. Configure automatic retreat options when battles go wrong.
tags:
    - battle
    - withdraw
    - retreat
    - safety
---

# Battle Withdrawal and Retreat

Safely retreat from battles when things go wrong.

## Overview

When your team is defeated or you need to abandon a battle, FGA can automatically handle the withdrawal process. Configure whether to allow automatic withdrawals or stop the script when retreat is needed.

## Key Features

- **Automatic Withdrawal**: Handle retreat dialogs without intervention
- **Withdrawal Tracking**: Count how many times you've retreated
- **Configurable Behavior**: Choose to allow or disallow withdrawals
- **Clean Exit**: Properly close all withdrawal dialogs

## How Withdrawal Works

```text
┌─────────────────────────────────────────┐
│        Team Defeated                    │
│        or Manual Retreat                │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Withdrawal Dialog Appears            │
│    "Do you want to withdraw?"           │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Withdraw Enabled?       │ Disabled
         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│  Click Accept   │    │  Stop Script    │
│  Handle Dialogs │    │  with Error     │
└────────┬────────┘    └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Click Close on Results               │
└─────────────────────┬───────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Increment Withdraw Counter           │
│    Continue to Next Run                 │
└─────────────────────────────────────────┘
```

## Withdrawal Dialog Flow

FGA handles the complete withdrawal sequence:

### Step 1: Detection

```text
┌─────────────────────────────────────────┐
│                                         │
│    Your party has been defeated         │
│                                         │
│    [ Use Command Spell ] [ Withdraw ]   │
│                                         │
└─────────────────────────────────────────┘
```

FGA detects the "Withdraw" button on screen.

### Step 2: Confirmation

```text
┌─────────────────────────────────────────┐
│                                         │
│    Abandon this battle?                 │
│                                         │
│    [ Cancel ]  [ Accept ]               │
│                                         │
└─────────────────────────────────────────┘
```

FGA clicks "Accept" to confirm withdrawal.

### Step 3: Close Results

```text
┌─────────────────────────────────────────┐
│                                         │
│    Battle Abandoned                     │
│                                         │
│    [ Close ]                            │
│                                         │
└─────────────────────────────────────────┘
```

FGA clicks "Close" to finish the withdrawal.

## Configuration

### Enable/Disable Withdrawal

| Setting  | Behavior                           |
| -------- | ---------------------------------- |
| Enabled  | Automatically handle withdrawals   |
| Disabled | Stop script when withdrawal needed |

### When to Disable Withdrawal

Consider disabling if:

- You want to manually intervene when losing
- You prefer to use Command Spells manually
- You're testing a new team composition
- You want to investigate why battles fail

## Withdrawal Tracking

### Counter

FGA tracks withdrawals during the session:

```text
┌─────────────────────────────────────────┐
│         Battle Statistics               │
├─────────────────────────────────────────┤
│ Withdraw Count: 2                       │
└─────────────────────────────────────────┘
```

### Exit Summary

After script completion:

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ Times Ran: 50                           │
│ Withdraw Count: 3                       │
│ ...                                     │
└─────────────────────────────────────────┘
```

## Why Withdrawals Happen

Common reasons for needing to withdraw:

| Cause               | Solution                    |
| ------------------- | --------------------------- |
| Under-leveled team  | Level up servants           |
| Wrong class matchup | Adjust party composition    |
| Boss mechanics      | Learn fight patterns        |
| Bad RNG             | May need multiple attempts  |
| Missing skills      | Use skill commands properly |

## Tips for Best Results

1. **Review withdrawals**: High counts indicate team problems
2. **Check your setup**: Verify skill commands are correct
3. **Consider difficulty**: Some quests may be too hard to farm
4. **Use appropriate teams**: Match class advantages
5. **Monitor patterns**: Same quest failing repeatedly needs adjustment

## Exit Reason: Withdraw Disabled

When withdrawal is disabled and a retreat is needed:

```text
Exit Reason: WithdrawDisabled

FGA detected a withdrawal dialog but automatic
withdrawal is disabled in settings. The script
has stopped to allow manual intervention.
```

This gives you the chance to:

- Use Command Spells to revive
- Use Saint Quartz to continue
- Manually withdraw

## Alternative: Command Spells

Instead of withdrawing, you can use Command Spells:

| Spell Use | Effect                        |
| --------- | ----------------------------- |
| Revive    | Full party HP restore         |
| NP Charge | 100% NP gauge for one servant |
| Heal      | Partial HP recovery           |

FGA can be configured to use Command Spells in skill commands, but automatic revival on defeat is not supported.

## Troubleshooting

### Script stops unexpectedly on defeat

- Withdrawal may be disabled in settings
- Check your battle configuration
- Enable withdrawal if you want automatic handling

### Withdrawal counter increasing rapidly

- Your team is failing frequently
- Review party composition
- Check skill command timing
- Consider easier quests

### Withdrawal dialog not detected

- Ensure screen is not obscured
- Check for device-specific issues
- Verify FGA version is current

### Script continues after failed battle without counting withdrawal

- The battle may have ended differently
- Check if Command Spells were used
- Verify withdrawal dialog appeared

## Command Spell Alternative

If you prefer to use Command Spells instead of withdrawing:

1. Disable automatic withdrawal
2. Script stops on defeat
3. Manually use Command Spell
4. Script continues from battle

This approach conserves quest progress but requires manual intervention.

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Skill Maker](../../battle-setup/skill-maker.md) - Command Spell usage
