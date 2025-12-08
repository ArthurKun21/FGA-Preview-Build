---
title: Support Selection Modes
description: Learn about the three support selection modes in FGA Preview - First, Manual, and Preferred. Choose the right mode for your farming needs.
tags:
    - support
    - selection
    - configuration
---

# Support Selection Modes

FGA Preview offers three different modes for selecting support servants during battle automation. Each mode serves different use cases depending on your farming needs.

## Overview

When FGA reaches the support selection screen, it needs to decide which support servant to pick. The selection mode determines how this decision is made - from fully automatic to fully manual control.

| Mode          | Description                                       | Best For                                  |
| ------------- | ------------------------------------------------- | ----------------------------------------- |
| **First**     | Automatically selects the first available support | Speed farming, no specific support needed |
| **Manual**    | Exits automation for you to select manually      | Precise control, testing setups           |
| **Preferred** | Searches for specific servants, CEs, or friends   | Optimized farming with specific supports  |

## First Mode

First mode selects the first visible support servant without any filtering.

### How First Mode Works

1. FGA waits for the support list to load
2. Clicks on the first support entry
3. Continues with battle if selection succeeds
4. Refreshes the list if the selection fails (friend has no servant set)

### When to Use First Mode

- Farming quests where any support works
- Event bonus supports where you want maximum speed
- Testing automation setups quickly
- When you don't care about specific support skills or CEs

### Limitations

- No control over which servant is selected
- Cannot filter by friend status
- Cannot check for specific skills or Noble Phantasm levels

---

## Manual Mode

Manual mode exits the automation script when it reaches the support selection screen.

### How Manual Mode Works

1. FGA detects the support selection screen
2. Script exits immediately
3. You manually select your desired support
4. You must start the script again after you make your selection

### When to Use Manual Mode

- When you need a very specific support for challenging content
- Testing different support configurations
- Quests where automation decisions need human oversight
- Situations where preferred mode cannot match your needs

### Important Behavior

Manual mode stops the script entirely at the support screen. You must:

- Select a support yourself
- The script will not continue automatically
- You may need to restart the script after selection

---

## Preferred Mode

Preferred mode searches for specific support servants, Craft Essences, and friends based on your configured criteria.

### How Preferred Mode Works

1. FGA loads your preferred servant, CE, and friend settings
2. Scans each visible support entry
3. Checks if each entry matches ALL your criteria
4. Selects the first matching support
5. Scrolls down if no match is found
6. Refreshes the list after exhausting scroll options

### Configuring Preferred Mode

Preferred mode requires setup through the Battle Config:

1. Open your **Battle Config**
2. Navigate to **Support Selection**
3. Select **Preferred** mode
4. Tap **Preferred Support** to configure

See the detailed guides for each component:

- [Preferred Servant Selection](preferred-servant.md) - Configure servant matching
- [Preferred CE Selection](preferred-ce.md) - Configure Craft Essence matching
- [Preferred Friend Selection](preferred-friend.md) - Configure friend filtering
- [Grand Servant Mode](grand-servant.md) - JP server exclusive features

### Matching Logic

For a support to be selected, it must satisfy ALL enabled criteria:

| Criteria       | Condition                                           |
| -------------- | --------------------------------------------------- |
| Servant        | Matches any configured servant image                |
| Ascension      | Shows max ascension star (if enabled)               |
| Skills         | Required skills are at level 10 (if enabled)        |
| Append Skills  | Required append skills are at level 10 (if enabled) |
| Noble Phantasm | NP level meets minimum (if enabled)                 |
| Craft Essence  | Matches any configured CE image                     |
| MLB Status     | CE shows limit break star (if enabled)              |
| Friend Status  | Is a friend (if Friends Only enabled)               |
| Friend Name    | Matches preferred friend (if configured)            |

### Search Behavior

```text
┌───────────────────────┐
│ Check Class Tab       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Scan Visible Supports │◄───────┐
└───────────┬───────────┘        │
            │                    │
        ┌───┴───┐                │
        │ Match │                │
        │ Found?│                │
        ▼       ▼                │
   ┌────────┐  ┌────────┐        │
   │ Select │  │ Scroll │────────┘
   │ Done   │  │  Down  │
   └────────┘  └────┬───┘
                    │
              ┌─────┴─────┐
              │ Bottom of │
              │   List?   │
              ▼           ▼
         ┌────────┐  ┌────────┐
         │ Check  │  │Refresh │
         │  All   │  │  List  │
         └────────┘  └────────┘
```

### Fallback Behavior

When no match is found after scrolling:

1. **Also Check All** (if enabled): Switches to the "All" class tab
2. **Refresh**: Updates the support list
3. **Repeat**: Continues searching until max refresh limit

---

## Choosing the Right Mode

| Scenario                                   | Recommended Mode         |
| ------------------------------------------ | ------------------------ |
| Daily farming with any servant             | First                    |
| Event farming needing specific CEs         | Preferred                |
| Challenging quest needing specific support | Manual or Preferred      |
| Speed testing battle configs               | First                    |
| Farming with friend points in mind         | Preferred (Friends Only) |

## Tips for Best Results

- **Start with Preferred**: Configure your ideal support first
- **Have fallbacks ready**: Add multiple acceptable servants/CEs
- **Use class filters**: Reduce search time by selecting specific class tabs
- **Enable Also Check All**: Provides backup if class tab has no matches
- **Adjust refresh limits**: Increase if your requirements are strict

## Troubleshooting

### Script keeps refreshing without selecting

- Your criteria may be too strict
- Try disabling some optional checks (MLB, Max Skills, NP Level)
- Ensure your support images are correctly captured

### First mode selects empty support

- Some friends may not have set a support
- This is rare but can happen
- Script will automatically retry

### Manual mode won't continue

- This is expected behavior
- Manual mode requires you to complete the selection
- Restart the script if needed

---

## Related Documentation

- [Support Class Selection](class-picker.md) - Configure class tab filtering
- [Support List Refresh](refresh.md) - Understand refresh mechanics
