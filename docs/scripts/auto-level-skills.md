---
title: Auto Level Skills
description: Automatically upgrade servant skills in Fate/Grand Order using FGA Preview. Configure target skill levels and let the script handle the enhancement process.
tags:
  - scripts
  - skills
  - automation
  - enhancement
---

# Auto Level Skills

Automatically upgrades servant skills to your desired level.

## Overview

The Level Skill script automatically enhances your servant's skills by repeatedly clicking the upgrade button until they reach the target level. It supports upgrading all three skills with individual target levels and provides detailed exit state information.

## How to Start

1. Navigate to **Enhancement → Skill** in the game
2. **Select the servant** whose skills you want to upgrade
3. The script will automatically detect skill enhancement mode when:
   - The "Skills" banner is visible in the enhancement menu
4. **Configure which skills to upgrade** and their target levels in settings
5. Start the script

!!! tip Important
    You must select a servant before starting. The script will exit if no servant is selected.

## Workflow

```text
┌─────────────────────────────────────────┐
│        Start Level Skill Script         │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Verify Servant is Selected           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │   For Each Skill (1-3)  │
        └─────────────┬───────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │  Should Upgrade This    │
        │  Skill? (Check setting) │
        └─────────────┬───────────┘
                      │
         ┌────────────┴────────────┐
         │ Yes                     │ No
         ▼                         ▼
┌─────────────────────┐   ┌─────────────────────┐
│ Click Skill Icon    │   │ Skip to Next Skill  │
└─────────┬───────────┘   └─────────────────────┘
          │
          ▼
    ┌─────────────────────────┐
    │   Skill Upgrade Loop    │◄──────┐
    └─────────────┬───────────┘       │
                  │                   │
                  ▼                   │
    ┌─────────────────────────┐       │
    │  Read Current Level     │       │
    │  (Using OCR)            │       │
    └─────────────┬───────────┘       │
                  │                   │
                  ▼                   │
    ┌─────────────────────────┐       │
    │  Target Level Reached?  │       │
    └─────────────┬───────────┘       │
                  │                   │
     ┌────────────┴────────────┐      │
     │ Yes                     │ No   │
     ▼                         ▼      │
   Move to                Click Enhance│
   Next Skill             Button      │
                              │       │
                              ▼       │
                  ┌─────────────────┐ │
                  │ Confirm Upgrade │ │
                  └────────┬────────┘ │
                           └──────────┘
```

## Key Features

### Individual Skill Configuration

- Configure each skill (1, 2, 3) independently
- Set specific target levels for each skill
- Enable/disable upgrade for each skill

### OCR Level Detection

- Uses optical character recognition to read current skill level
- Accurately tracks progress during enhancement
- Detects when target level is reached

### Resource Monitoring

- Detects insufficient QP (currency)
- Detects insufficient materials
- Stops and reports which resource ran out

### Comprehensive Exit State

- Reports starting level for each skill
- Reports ending level for each skill
- Reports why each skill stopped (target met, out of mats, etc.)

## Settings

| Setting | Description |
|---------|-------------|
| Should Upgrade Skill One | Enable/disable skill 1 upgrade |
| Should Upgrade Skill Two | Enable/disable skill 2 upgrade |
| Should Upgrade Skill Three | Enable/disable skill 3 upgrade |
| Skill One Upgrade Value | Number of levels to upgrade skill 1 |
| Skill Two Upgrade Value | Number of levels to upgrade skill 2 |
| Skill Three Upgrade Value | Number of levels to upgrade skill 3 |

!!! note
    Target level = Minimum (starting) level + Upgrade value

![Level Skill](<../assets/scripts/Level Skill.png>)

![Level Skill Dialog](<../assets/scripts/Level Skill Dialog.png>)

![Level Skill with unavailable slots](<../assets/scripts/Level Skill Limited.png>)

![Level Skill with unavailable slots Dialog](<../assets/scripts/Level Skill Limited Dialog.png>)

## Exit Reasons

### Overall Script Exit

| Exit Reason | Description |
|-------------|-------------|
| **Done** | All configured skills have been processed |
| **No Servant Selected** | No servant was selected in the enhancement slot |
| **Ran Out of QP** | Insufficient QP to continue upgrades |
| **Abort** | Script was manually stopped by user |
| **Unexpected** | An unexpected error occurred |

### Individual Skill Exit

Each skill can exit with one of these reasons:

| Skill Exit Reason | Description |
|-------------------|-------------|
| **Target Level Met** | Skill reached the configured target level |
| **Out of Mats** | Insufficient materials for this skill |
| **Out of QP** | Insufficient QP for upgrade |
| **Exit Early (QP)** | Skipped because previous skill ran out of QP |
| **No Skill Upgrade Error** | Upgrade value was 0 |

## Exit State Summary

After the script completes, you receive a detailed summary:

```text
┌─────────────────────────────────────────┐
│           Exit State Summary            │
├─────────────────────────────────────────┤
│ Skill 1:                                │
│   • Checked: Yes/No                     │
│   • Available: Yes/No                   │
│   • Starting Level: X                   │
│   • Ending Level: Y                     │
│   • Target Level: Z                     │
│   • Exit Reason: Target Met / Out of X  │
├─────────────────────────────────────────┤
│ Skill 2: (same format)                  │
├─────────────────────────────────────────┤
│ Skill 3: (same format)                  │
└─────────────────────────────────────────┘
```

## QP Cascade Effect

If a skill runs out of QP, subsequent skills will be marked with "Exit Early (QP)":

```text
Skill 1: Out of QP ──► Skill 2: Exit Early (QP) ──► Skill 3: Exit Early (QP)
```

This prevents unnecessary attempts when QP is already depleted.

## Tips for Best Results

1. **Check your materials** before starting to ensure all skills can be upgraded
2. **Have sufficient QP** for all planned upgrades
3. **Set realistic targets** based on your available resources
4. **Note skill availability** - Skills 2 and 3 may be locked on newer servants
5. **Configure all three skills** if you want to upgrade multiple in one run

## Technical Notes

- Skills 2 and 3 availability is checked before attempting upgrade
- Temporary servants are handled with additional confirmation
- Uses regex pattern matching for level detection: `(\d+)(?:/1|/10)?`
- Connection retries are handled automatically