# Auto Level CE

Automatically enhances a selected Craft Essence (CE) to increase its level.

## Overview

The Level CE script enhances a single target Craft Essence by feeding it fodder CEs. Unlike CE Bomb mode, this mode is designed to level a specific CE you've already selected and will stop when that CE reaches its maximum level.

## How to Start

1. Navigate to **Enhancement → Craft Essence** in the game
2. **Select the CE you want to level** (tap on it so it appears in the enhancement slot)
3. The script will automatically detect you're in CE enhancement mode when:
   - The CE Enhancement banner is visible
   - A CE is already selected (not empty)
4. Start the script

> **Important**: You must select a target CE before starting. The script distinguishes between Level CE mode and CE Bomb mode based on whether a CE is already selected.

## Workflow

```text
┌─────────────────────────────────────────┐
│         Start Level CE Script           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Verify Target CE is Selected         │
│    (Not empty enhancement slot)         │
└─────────────────────┬───────────────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │   Main Enhancement Loop │◄──────┐
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │  Check if CE is Locked  │       │
        │  (Auto-lock if needed)  │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │  Open Fodder Selection  │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Configure Filters     │       │
        │   (Display, Sort, etc.) │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Select Fodder CEs     │       │
        │   (Drag to select)      │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Confirm Enhancement   │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Is Target CE Max?     │       │
        └─────────────┬───────────┘       │
                      │                   │
         ┌────────────┴────────────┐      │
         │ Yes                     │ No   │
         ▼                         └──────┘
┌─────────────────────────────────────────┐
│    Exit: Target CE Max Level            │
└─────────────────────────────────────────┘
```

## Key Features

### Auto-Lock Target CE

- Automatically locks the target CE to prevent accidental use as fodder
- Can be disabled in settings
- Requires Android 8.0+ for long-press functionality

### Smart Display Adjustment

- Automatically sets CE display to small size for better visibility
- Can detect and click the correct corner for display toggle
- Configurable based on your screen layout

### Filter Configuration

- Automatically sets appropriate filters for fodder CEs
- Filters by rarity (based on your settings)
- Configures sort options for optimal fodder selection

### Smart Sort Features

- Enables smart sort for efficient CE organization
- Enables select sort for easier multi-selection
- Sorts by level to use lowest-level CEs first

## Settings

| Setting | Description |
|---------|-------------|
| Target CE Rarity | Rarity of the CE you're leveling |
| Fodder CE Rarity | Which CE rarities to use as fodder |
| Skip Auto-Lock Target CE | Don't automatically lock the target CE |
| Skip Automatic Display Change | Don't auto-adjust display size |
| Skip CE Filter Detection | Don't auto-configure filters |
| Skip Sort Detection | Don't auto-configure sort options |
| CE Display Change Area | Which corner to tap to change display |

![Level CE](<../assets/scripts/Level CE.png>)

![Level CE Dialog](<../assets/scripts/Level CE Dialog.png>)

## Exit Reasons

The script will stop and notify you when any of these conditions occur:

| Exit Reason | Description |
|-------------|-------------|
| **Target CE Max Level** | The target CE has reached its maximum level |
| **No Suitable Fodder CE Found** | No fodder CEs available that match your filter criteria |
| **No Suitable Target CE Found** | Could not identify a valid target CE |

## Differences from CE Bomb Mode

| Feature | Level CE | CE Bomb |
|---------|----------|---------|
| Target CE | Pre-selected by user | Auto-selected from list |
| Stop condition | Target CE max level | No more fodder available |
| Purpose | Level specific CE | Create multiple leveled CEs |
| Starting state | CE already in slot | Empty enhancement slot |

## Tips for Best Results

1. **Select your target CE first** before starting the script
2. **Use appropriate fodder rarities** to maximize enhancement value
3. **Enable auto-lock** to protect your target CE
4. **Configure display area** based on your screen layout
5. **Ensure sufficient QP** for enhancement costs

## Technical Notes

- Uses 7 columns × 4 rows grid for target CE selection
- Uses 7 columns × 3 rows grid for fodder CE selection
- Skips rows/columns where CEs have been exhausted
- Handles connection retries automatically
