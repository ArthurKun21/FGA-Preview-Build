---
title: Energy Refill and AP Management
description: Configure automatic AP refill with apples in FGA. Manage stamina resources, set refill limits, and optimize apple usage for farming.
tags:
    - battle
    - stamina
    - apples
    - refill
---

# Energy Refill and AP Management

Automatically manage your AP (Action Points) during farming sessions.

## Overview

FGA can automatically refill your AP when it runs out by using various apple types or Saint Quartz. Configure which resources to use, set limits on consumption, and optionally wait for natural AP regeneration instead of using items.

## Key Features

- **Multiple Apple Types**: Support for all apple colors and Saint Quartz
- **Refill Limits**: Control maximum resources used
- **Auto-Decrement**: Automatically reduce remaining limit after use
- **AP Regeneration Wait**: Option to wait instead of using apples
- **Stamina Over-Recharge**: Use multiple apples at once when available

## Refill Resources

| Resource         | AP Restored | Max Per Refill |
| ---------------- | ----------- | -------------- |
| **Gold Apple**   | Full AP     | 1              |
| **Silver Apple** | 50% AP      | 2              |
| **Bronze/Blue Apple** | 40 AP      | 3 or 4 Depends on Master Level           |
| **Copper Apple** | 10 AP       | Depends on Master Level             |
| **Saint Quartz** | Full AP     | 1              |

### Resource Priority

When multiple resources are configured, FGA uses the first available resource in your configured order.

## How Energy Refill Works

```text
┌─────────────────────────────────────────┐
│       Stamina Screen Detected           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Check Refill Settings                │
│    • Refill enabled?                    │
│    • Resources configured?              │
│    • Limit reached?                     │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Can Refill?             │ Cannot
         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│  Select Apple   │    │  Wait for Regen │
│  Click Refill   │    │  or Exit Script │
└────────┬────────┘    └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Confirm Refill Amount                │
│    (for multi-use apples)               │
└─────────────────────┬───────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Update Refill Counter                │
└─────────────────────────────────────────┘
```

## Configuration Options

### Selecting Refill Resources

Select which apple types FGA can use:

1. Open your server configuration
2. Navigate to refill settings
3. Select resources in priority order
4. Gold apples are typically first choice

### Refill Limit

Set the maximum number of refills per session:

| Setting  | Behavior                          |
| -------- | --------------------------------- |
| 0        | Refill disabled                   |
| 1-99     | Maximum refills allowed           |
| No limit | Unlimited refills (use carefully) |

### Wait for AP Regeneration

When enabled, FGA waits for natural AP regen instead of using apples:

- Checks every 60 seconds
- Useful for overnight farming
- Conserves apple resources
- Only activates when refill not possible/allowed

## Apple Efficiency

### Gold Apples

- Best for high-AP quests (40 AP)
- Full refill regardless of max AP
- Most valuable resource

### Silver Apples

- Can use up to 2 per refill if AP allows
- Balanced efficiency

### Bronze or Blue Apples

- Gives flat 40 AP
- Common from event/main story rewards

### Copper Apples

- Gives flat 10 AP
- Good for exact AP needs

## Stamina Over-Recharge

Some apple types can be used multiple times in one refill action:

```text
Example: 200 max AP, currently 0 AP

Silver Apple (50%):
- First use: +100 AP
- Second use: +100 AP (if enabled)
- Result: 200/200 AP, 2 refills counted

Bronze Apple (30%):
- First use: +60 AP
- Second use: +60 AP
- Third use: +60 AP
- Result: 180/200 AP, 3 refills counted
```

FGA reads the stamina values to determine how many apples to use.

## Auto-Decrement Limits

After the script ends, FGA automatically reduces your refill limit:

```text
Before Run:
- Refill Limit: 10

During Run:
- Refills Used: 3

After Run:
- Refill Limit: 7 (auto-decremented)
```

When the limit reaches 0:

- Refill is disabled
- Limit resets to default value
- You must manually re-enable

## Last Run Behavior

On the final run of a limited session:

| Setting        | Behavior                      |
| -------------- | ----------------------------- |
| Normal         | Uses apples if available      |
| Wait for Regen | Waits instead of using apples |

This helps conserve resources when you're about to stop farming.

## Tips for Best Results

1. **Match apples to quest AP cost**: Use bronze for low-cost quests
2. **Set conservative limits**: Start with lower limits until comfortable
3. **Check resource priority**: Order matters when multiple are enabled
4. **Use wait for regen overnight**: Save apples during long sessions
5. **Monitor refill counter**: Track usage in exit summary

## Refill Counter in Exit Summary

After script completion, view refill statistics:

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ Times Refilled: 5                       │
│ Refill Limit: 10                        │
│ ...                                     │
└─────────────────────────────────────────┘
```

## Troubleshooting

### Refill not happening when AP runs out

- Verify refill is enabled in settings
- Check if refill limit is reached
- Ensure resources are selected
- Confirm you have apples in inventory

### Wrong apple type being used

- Check resource priority order
- Higher priority resources are used first
- Reorder in settings if needed

### Script exits instead of refilling

- Refill limit may be reached
- No configured resources available
- Wait for regen might be enabled

### Refill counter seems wrong

- Multi-use apples count as multiple refills
- Silver = up to 2, Bronze = up to 3
- Check stamina over-recharge behavior

### Auto-decrement not working

- Only happens after successful script completion
- Manual stops may not trigger decrement
- Check your settings after run

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Run Limits](../../app/advanced.md) - Configure run limitations
