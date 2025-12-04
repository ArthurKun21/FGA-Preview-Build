# Auto Level Servant

Automatically enhances a servant's level using embers.

## Overview

The Level Servant script automatically feeds embers to your selected servant to increase their level. It can optionally handle ascension and even palingenesis (grailing) when the servant reaches maximum level for their current stage.

## How to Start

1. Navigate to **Enhancement → Servant** in the game
2. **Select the servant you want to level**
3. The script will automatically detect servant enhancement mode when:
   - The "Auto Select" button is visible
   - Or the servant ascension/grail banner is visible
4. Start the script

> **Important**: You must select a servant before starting. The script will exit if no servant is selected.

## Workflow

```text
┌─────────────────────────────────────────┐
│       Start Level Servant Script        │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Verify Servant is Selected           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │   Main Enhancement Loop │◄──────┐
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │  Is Auto Select Visible?│       │
        └─────────────┬───────────┘       │
                      │ Yes               │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Click Auto Select     │       │
        │   (Embers selected)     │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Confirm Ember Use     │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Click Enhance Button  │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Confirm Enhancement   │       │
        └─────────────┬───────────┘       │
                      │                   │
                      ▼                   │
        ┌─────────────────────────┐       │
        │   Check for Max Level   │       │
        └─────────────┬───────────┘       │
                      │                   │
         ┌────────────┴────────────┐      │
         │ Max Level              │ No    │
         ▼                        └───────┘
        Handle Max Level
        (Ascension/Grail/Exit)
```

## Key Features

### Auto Select Enhancement

- Uses the game's auto select feature to pick embers
- Automatically optimizes ember selection

### JP Server Auto-Fill (2025+)

- For JP servers, supports the auto-fill feature
- Automatically toggles auto-fill ON for faster enhancement
- Handles the new refund window after leveling

### Max Level Handling

When the servant reaches max level, the script can:

1. **Redirect to Ascension** - Navigate to ascension menu and perform ascension
2. **Redirect to Grail Menu** - Navigate to palingenesis menu
3. **Exit** - Stop the script at max level

### Ascension Automation

- Can automatically perform ascension when enabled
- Returns to enhancement menu after ascension
- Handles the 3rd ascension dialog properly

### Grail Automation

- There's no plan to support automatic grailing
- After Grailing servant, you can run the script again to continue leveling

### Temporary Servant Support

- Detects temporary (story support) servants
- Handles the additional confirmation dialog

## Settings

| Setting | Description |
|---------|-------------|
| Should Redirect Ascension | Navigate to ascension menu at max level |
| Should Perform Ascension | Automatically perform the ascension |
| Should Redirect Grail | Navigate to grail menu at max level |

## Exit Reasons

The script will stop and notify you when any of these conditions occur:

| Exit Reason | Description |
|-------------|-------------|
| **No Servant Selected** | No servant was selected in the enhancement slot |
| **No Embers or QP Left** | Ran out of embers to use or insufficient QP |
| **Max Level Achieved** | Servant reached maximum level (no redirect enabled) |
| **Redirect Ascension** | Navigated to ascension menu (ascension not enabled) |
| **Unable to Perform Ascension** | Could not complete the ascension process |
| **Redirect Grail** | Navigated to grail/palingenesis menu |
| **Perform Grail** | Currently in grail menu |
| **Abort** | Script was manually stopped by user |
| **Unexpected** | An unexpected error occurred |

## Workflow with Ascension

```text
┌─────────────────────────────────────────┐
│      Servant Reaches Max Level          │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│  Is "Redirect to Ascension" Enabled?    │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Yes                     │ No
         ▼                         ▼
┌─────────────────────┐   ┌─────────────────────┐
│ Navigate to         │   │ Check for Grail     │
│ Ascension Menu      │   │ Redirect            │
└─────────┬───────────┘   └─────────────────────┘
          │
          ▼
┌─────────────────────────────────────────┐
│  Is "Perform Ascension" Enabled?        │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Yes                     │ No
         ▼                         ▼
┌─────────────────────┐   ┌─────────────────────┐
│ Click Enhance       │   │ Exit: Redirect      │
│ Confirm Ascension   │   │ Ascension           │
└─────────┬───────────┘   └─────────────────────┘
          │
          ▼
┌─────────────────────────────────────────┐
│    Return to Enhancement Menu           │
│    Continue Leveling                    │
└─────────────────────────────────────────┘
```

## Tips for Best Results

1. **Select your servant** before starting the script
2. **Have sufficient embers** of the appropriate class
3. **Ensure adequate QP** for enhancement costs
4. **Configure ascension settings** based on your needs
5. **For JP users**: Auto-fill will speed up the process significantly

## Technical Notes

- Maximum 5 retries for confirmation dialogs
- Handles connection issues automatically
- Detects "Low QP" minimum ember selection dialog
- Supports both regular and temporary servants
- Debug mode may interfere with redirect detection
