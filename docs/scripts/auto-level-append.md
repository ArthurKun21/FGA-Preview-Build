---
title: Auto Level Append
description: Automatically unlock and upgrade servant append skills in Fate/Grand Order using FGA Preview. Manage servant coins, materials, and QP for append skill leveling.
tags:
  - scripts
  - append skills
  - servant coins
  - automation
  - enhancement
---

# Auto Level Append

Automatically unlocks and upgrades servant append skills.

## Overview

The Level Append script automatically manages your servant's append skills - both unlocking them (using servant coins) and upgrading their levels (using materials and QP). It supports all append skills and provides detailed status reporting.

## What are Append Skills?

Append Skills are additional passive skills that can be unlocked using Servant Coins. Once unlocked, they can be leveled up using materials and QP, similar to regular skills. Each servant has 3 append skills (5 on JP servers after the [9th anniversary](https://fategrandorder.fandom.com/wiki/Fate/Grand_Order_%EF%BD%9E9th_Anniversary%EF%BD%9E#[VI])).

## Technical Difficulties

Unlike regular skills, append skills' screen have their level text unable to be read via OCR. Therefore, the script relies on counting upgrade attempts to track levels.

## How to Start

1. Navigate to **Enhancement → Append Skill** in the game
2. **Select the servant** whose append skills you want to manage
3. The script will automatically detect append enhancement mode when:
   - The "Append" banner is visible in the enhancement menu
4. **Configure which appends to unlock/upgrade** in settings
5. Start the script

!!! tip "Important"
    You must select a servant before starting. The script will exit if no servant is selected.

![Level Append](<../assets/scripts/Level Append Old.png>)

Other servers with 3 appends

![Level Append Extended](<../assets/scripts/Level Append Extended.png>)

JP version with 5 appends

## Workflow

```text
┌─────────────────────────────────────────┐
│       Start Level Append Script         │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Verify Servant is Selected           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │  For Each Append (1-3)  │
        │  (1-5 on JP servers)    │
        └─────────────┬───────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │  Check Configuration:   │
        │  • Unlock needed?       │
        │  • Upgrades needed?     │
        └─────────────┬───────────┘
                      │
         ┌────────────┴────────────┐
         │ Action needed          │ No
         ▼                         ▼
┌─────────────────────┐   ┌─────────────────────┐
│ Click Append Icon   │   │ Mark as Not Selected│
└─────────┬───────────┘   │ Move to Next        │
          │               └─────────────────────┘
          ▼
    ┌─────────────────────────┐
    │ Need to Unlock First?   │
    └─────────────┬───────────┘
                  │
     ┌────────────┴────────────┐
     │ Yes                     │ No
     ▼                         │
┌─────────────────────┐        │
│ Perform Unlock      │        │
│ (Uses Servant Coins)│        │
└─────────┬───────────┘        │
          │                    │
          ▼                    │
    ┌─────────────────────────┐│
    │   Upgrade Loop          ││◄─────┐
    └─────────────┬───────────┘│      │
                  │◄───────────┘      │
                  ▼                   │
    ┌─────────────────────────┐       │
    │  Upgrades Remaining?    │       │
    └─────────────┬───────────┘       │
                  │                   │
     ┌────────────┴────────────┐      │
     │ Yes                     │ No   │
     ▼                         ▼      │
   Click Enhance        Move to       │
   Button               Next Append   │
        │                             │
        ▼                             │
   Confirm Upgrade ───────────────────┘
```

## Key Features

### Unlock + Upgrade Workflow

- Can unlock append skills using servant coins
- Can upgrade unlocked append skills
- Handles both operations in sequence

### Server-Aware Configuration

- JP servers: Supports 5 append skills (after the 9th anniversary)
- Other servers: Supports 3 append skills

### Resource Monitoring

- Detects insufficient QP
- Detects insufficient materials
- Detects insufficient servant coins for unlock
- Reports specific issues for each append

### Comprehensive Exit State

- Reports unlock status for each append
- Reports number of upgrades performed
- Reports exit reason for each append

## Settings

| Setting | Description |
|---------|-------------|
| Should Unlock Append One | Enable unlocking of append 1 |
| Should Unlock Append Two | Enable unlocking of append 2 |
| Should Unlock Append Three | Enable unlocking of append 3 |
| Should Unlock Append Four | Enable unlocking of append 4 (JP only) |
| Should Unlock Append Five | Enable unlocking of append 5 (JP only) |
| Upgrade Append One | Number of levels to upgrade append 1 |
| Upgrade Append Two | Number of levels to upgrade append 2 |
| Upgrade Append Three | Number of levels to upgrade append 3 |
| Upgrade Append Four | Number of levels to upgrade append 4 (JP only) |
| Upgrade Append Five | Number of levels to upgrade append 5 (JP only) |

!!! note
    The app automatically detects which appends are locked/unlocked.

![Level Append Dialog](<../assets/scripts/Level Append Dialog.png>)

![Level Append Extended Dialog](<../assets/scripts/Level Append Extended Dialog.png>)

## Exit Reasons

### Overall Script Exit

| Exit Reason | Description |
|-------------|-------------|
| **Done** | All configured appends have been processed |
| **No Servant Selected** | No servant was selected |
| **Ran Out of QP** | Insufficient QP to continue |
| **Abort** | Script was manually stopped |
| **Unexpected** | An unexpected error occurred |

### Individual Append Exit

Each append can exit with one of these reasons:

| Append Exit Reason | Description |
|--------------------|-------------|
| **Success** | Append successfully upgraded to target |
| **Unlock Success** | Append unlocked (no upgrades configured) |
| **Not Selected** | Append was not configured for upgrade |
| **Ran Out of QP** | Insufficient QP |
| **Ran Out of Mats** | Insufficient materials |
| **Exit Early (QP)** | Skipped due to previous QP shortage |
| **Unable to Unlock** | Could not unlock (insufficient coins or error) |
| **Unable to Upgrade Further** | Could not continue upgrading |
| **Lag** | Timeout waiting for UI response |

## Exit State Summary

After the script completes, you receive a detailed summary:

```text
┌─────────────────────────────────────────┐
│         Append Exit State Summary       │
├─────────────────────────────────────────┤
│ Append 1:                               │
│   • Upgrade Level Target: X             │
│   • Should Unlock: Yes/No               │
│   • Upgrades Performed: Y               │
│   • Exit Reason: Success / Out of X     │
├─────────────────────────────────────────┤
│ Append 2: (same format)                 │
├─────────────────────────────────────────┤
│ Append 3: (same format)                 │
├─────────────────────────────────────────┤
│ Append 4: (JP only)                     │
├─────────────────────────────────────────┤
│ Append 5: (JP only)                     │
└─────────────────────────────────────────┘
```

## Unlock Workflow Detail

```text
┌─────────────────────────────────────────┐
│         Unlock Append Skill             │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Click Enhance Button (2 retries)     │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Wait for OK Button to Appear         │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ OK Visible             │ Not Visible
         ▼                         ▼
┌─────────────────────┐   ┌─────────────────────┐
│ Click OK to Confirm │   │ Exit: Unable to     │
│ Unlock              │   │ Unlock              │
└─────────┬───────────┘   └─────────────────────┘
          │
          ▼
┌─────────────────────────────────────────┐
│    Wait for Append Banner to Disappear  │
│    (Animation completion)               │
└─────────────────────────────────────────┘
```

## QP Cascade Effect

If an append runs out of QP, subsequent appends will be marked accordingly:

```text
Append 1: Out of QP ──► Append 2: Exit Early (QP) ──► Append 3: Exit Early (QP)
```

## Tips for Best Results

1. **Check servant coin balance** before attempting unlocks
2. **Verify materials** for planned upgrade levels
3. **Ensure adequate QP** for all operations
4. **Configure all appends** you want to process in one run
5. **Check locked status** - the app detects this automatically

## Technical Notes

- Uses 2 retries for unlock and upgrade initiation
- Waits up to 20 iterations (3 seconds each) for banner animations
- Handles connection issues automatically
- JP servers have 5 append skills; other servers have 3
- Unlock requires servant coins; upgrades require materials + QP
