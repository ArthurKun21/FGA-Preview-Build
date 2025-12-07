---
title: Party Selection and Team Setup
description: Configure automatic party selection in FGA. Set up your preferred team slot for farming automation.
tags:
    - battle
    - party
    - team
    - configuration
---

# Party Selection and Team Setup

Automatically select your configured party before starting quests.

## Overview

FGA can automatically select the correct party slot before entering battle, ensuring your farming team is always active. Configure which party slot to use, and FGA handles the selection even if a different party is currently active.

## Key Features

- **Automatic Selection**: Picks your configured party slot
- **Current Party Detection**: Identifies which party is active
- **Smart Switching**: Handles game quirks with party changes
- **Preset Quest Detection**: Identifies quests with locked parties
- **Persistent Selection**: Same party used for subsequent runs

## How Party Selection Works

```text
┌─────────────────────────────────────────┐
│        Party Selection Screen           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Detect Currently Selected Party      │
│    Look for selection indicator         │
└─────────────────────┬───────────────────┘
                      │
         ┌────────────┴────────────┐
         │ Correct Party?          │ Yes
         ▼                         ▼
┌─────────────────┐    ┌─────────────────┐
│ Click Target    │    │ Proceed with    │
│ Party Slot      │    │ Current Party   │
└────────┬────────┘    └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│    Wait for Selection Animation         │
└─────────────────────────────────────────┘
```

## Party Slots

FGA supports all party slots available on your server:

- **JP and CN servers**: 15 party slots
- **Other servers**: 10 party slots

| Slot | Position   | Use Case               |
| ---- | ---------- | ---------------------- |
| 1    | First      | Default farming team   |
| 2    | Second     | Alternative farm setup |
| 3    | Third      | Event team             |
| 4-10 | Additional | Specialized teams      |

### Slot Selection

Party slots appear as dots above the party display:

```text
   [•] [○] [○] [○] [○] [○] [○] [○] [○] [○]
    1   2   3   4   5   6   7   8   9  10

   [•] = Currently selected
   [○] = Available to select
```

## Configuration

### Setting Your Party

1. Open your Battle Config
2. Find the Party Selection setting
3. Choose your desired slot (1-10)
4. Save the configuration

### No Party Selection

Set to "Not Set" if you want to:

- Use whatever party is currently active
- Manually select party before starting
- Let the game decide (for some quests)

## Selection Logic

### Same Party Handling

FGO has a quirk where the "Start Quest" button becomes unresponsive if you select the same party that's already active:

```text
Current Party: 3
Target Party: 3

FGA's Solution:
1. Click different party (e.g., Party 4)
2. Wait for animation
3. Click target Party 3
4. Now Start Quest button works
```

### Detection Failure Handling

If FGA can't detect the current party:

1. Clicks a temporary different party
2. Waits for selection
3. Clicks the target party
4. Ensures reliable selection

## Preset Quest Detection

Some quests lock you into a specific party (story quests, tutorials):

### Detection

FGA checks for the party selection indicator:

- If no party selection available → Preset quest detected
- Based on settings, may exit or continue

### Exit on Preset Quest

When enabled:

```text
Exit Reason: PresetQuest

FGA detected a preset quest where party
selection is not available. The script
has stopped to prevent issues.
```

## Persistent Selection

After selecting a party once:

- Game remembers your selection
- FGA skips re-selection on subsequent runs
- Improves automation speed

### Reset Conditions

Selection tracking resets when:

- Script is restarted
- Different quest is selected
- App is closed and reopened

## Tips for Best Results

1. **Set up dedicated farm parties**: Create parties specifically for automation
2. **Use consistent slot numbers**: Same slot across different configs
3. **Name your parties**: Makes manual verification easier
4. **Check party before long sessions**: Verify correct team is configured
5. **Test with one run first**: Confirm party selection works

## Party Setup Recommendations

### Farming Party Layout

| Position | Servant Type   | Purpose         |
| -------- | -------------- | --------------- |
| 1        | Support slot   | Friend's farmer |
| 2        | AoE damage     | Wave clear      |
| 3        | Buffer/Support | Enhance damage  |
| 4        | Backup DPS     | Emergency       |
| 5-6      | Bond farming   | Passive bond    |

### Event Party Layout

| Position | Servant Type   | Purpose          |
| -------- | -------------- | ---------------- |
| 1-3      | Event bonus    | Maximize drops   |
| 4-6      | Bonus servants | Additional drops |

## Troubleshooting

### Party not being selected

- Verify party slot is configured correctly
- Check if party selection screen is visible
- Ensure the slot number exists (1-10)

### Wrong party selected

- Check your Battle Config settings
- Verify you're using the correct config
- Party slot numbers start at 1, not 0

### Start Quest button not working

- FGA handles this with temporary party switch
- May need to wait longer between selections
- Try manual party switch if persists

### Preset Quest stopping script

- Disable "Exit on Preset Quest" if intended
- Some story quests require preset parties
- Check if quest should allow party selection

### Selection animation takes too long

- FGA waits ~1.2 seconds for animation
- Slower devices may need longer
- Generally not a problem for most devices

## Party Selection vs Support Selection

| Feature     | Party Selection     | Support Selection     |
| ----------- | ------------------- | --------------------- |
| Purpose     | Choose your team    | Choose friend servant |
| Timing      | Before quest starts | After party selection |
| Options     | 10 preset slots     | Friend list search    |
| Persistence | Remembered          | Searched each time    |

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Support Selection](../../battle-setup/support.md) - Configure support servant
- [Battle Configuration](../../battle-setup/config.md) - Full config setup
