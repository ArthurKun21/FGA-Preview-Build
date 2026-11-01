---
title: Auto Lottery
description: Automatically spin event lottery boxes in Fate/Grand Order using FGA Preview. Handle present box overflow and collect rewards efficiently during FGO events.
tags:
  - scripts
  - lottery
  - events
  - automation
  - farming
---

# Auto Lottery

Spins lottery boxes automatically during event lotteries to collect rewards efficiently.

## Overview

The Lottery script opens lottery boxes continuously during Fate/Grand Order events. It handles present box overflow. When the present box becomes full, it can collect embers or sell items.

## How to Start

1. Open the **Event Lottery** screen in the game
2. The script detects the lottery screen when:
   - The lottery cost indicator is visible (JP/EN servers)
   - The lottery box finished indicator is visible
3. Make sure you have lottery currency (event items) to spend

## Workflow

```mermaid
flowchart TD
    A[Start Lottery Script] --> B[Initialize Spin Settings<br/>Click count, long press duration]
    B --> C[Main Spin Loop]
    C --> D[Check Current State]
    D --> E{State?}
    E -->|Present Box Full| F[Handle Full Present Box]
    E -->|Lottery Done| G[Verify Done<br/>Double check]
    E -->|Keep Spinning| C
    F --> H[Collect or Sell Embers]
    G --> I[Exit with<br/>Out of Currency]
```

## Key Features

### Server-Specific Spinning

You can select which gesture FGA uses to press the **Spin** button.

| Option          | Behavior                                                       |
| --------------- | -------------------------------------------------------------- |
| **Multi-Click** | Taps the spin button multiple times quickly.                   |
| **Long Press**  | Presses and holds the spin button for a configurable duration. |
| **Mixed**       | Alternates between multi-click and long press.                 |

> [!NOTE]
> All servers now use the same configuration options for consistency.

### Present Box Full Handling

When the present box becomes full, the script can:

1. **Collect Embers from Gift Box** - Opens the gift box to receive gold embers
2. **Redirect to Sell Menu** - After collecting embers, opens the sell menu for excess items
3. **Stop the script** - Exit with a present box full notification

### Lottery Completion Detection

- Double-checks when the lottery appears done to avoid false positives
- Tries spins and checks whether the "done" indicator stays

## Settings

| Setting                             | Description                                 |
| ----------------------------------- | ------------------------------------------- |
| Receive Embers When Gift Box Full   | Enable automatic ember collection           |
| Loop Into Lottery After Present Box | Return to lottery after collecting embers   |
| Move to Sell After Present Box      | Open the sell menu after collecting         |
| Max Gold Ember Total Count          | Limit on gold embers to collect per session |

![Lottery](../assets/other-scripts/lottery.png)

![Lottery Dialog](../assets/scripts/Lottery.png)

## Spin Configuration

| Setting                   | Description                              |
| ------------------------- | ---------------------------------------- |
| Lotto Spin Count          | Number of clicks per spin cycle (non-JP) |
| Lotto Long Press Duration | Duration of long press for spinning (JP) |

## Exit Reasons

The script stops and notifies you when one of these conditions occurs:

| Exit Reason                                    | Description                                      |
| ---------------------------------------------- | ------------------------------------------------ |
| **Ran Out of Currency**                        | No more lottery currency to spend                |
| **Present Box Full**                           | Present box is full and auto-collect is disabled |
| **No Embers Found**                            | Found no embers in the gift box                  |
| **Cannot Select Any More**                     | Reached the limit of selectable items            |
| **Present Box Full and Cannot Select Anymore** | Box is full and reached the selection limit      |
| **Reached Sell Banner**                        | Reached the sell menu                            |
| **Unable to Verify Sell**                      | Could not confirm it reached the sell menu       |
| **Aborted**                                    | You stopped the script manually                  |

![Lottery Full](../assets/other-scripts/lottery-full.png)

## Tips for Best Results

1. **Clear your present box** before starting for longer uninterrupted runs
2. **Set ember collection limits** to avoid unnecessary inventory management
3. **Set the present box to show embers**. This triggers the auto gift box collection
4. **For JP users**: Use `multi-click` from box 1 to box 10. Then switch to long press for faster spinning from box 11 onward.

## Present Box Integration

When the present box becomes full during the lottery:

```text
┌─────────────────────────────────────────┐
│        Present Box Full Detected        │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Is "Receive Embers" enabled?         │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Yes                     │ No
         ▼                         ▼
┌─────────────────┐      ┌─────────────────┐
│ Navigate to     │      │ Exit: Present   │
│ Gift Box        │      │ Box Full        │
└────────┬────────┘      └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Collect Gold Embers (AutoGiftBox)    │
└─────────────────────┬───────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Is "Loop Into Lottery" enabled?      │
└─────────────────────┬───────────────────┘
         │
         ▼
   Return to Lottery or Exit
```
