---
title: Grand Servant Selection
description: Configure FGA Preview for JP server Grand Servant support selection with multi-slot CEs, Bond CE requirements, and special level filtering.
tags:
    - support
    - grand servant
    - jp server
    - configuration
---

# Grand Servant Selection

Configure FGA to identify and select Grand Servants on the Japanese (JP) server, including their unique multi-slot CE system, Bond CE requirements, and level-based filtering.

## Overview

Grand Servants are a JP server exclusive feature where players can showcase a single servant with enhanced support capabilities. These servants can equip up to 3 Craft Essences and display a special Grand Servant indicator.

**Important**: Grand Servant features are only available on JP server. Other server versions do not support these options.

## Key Features

- **Grand Servant detection**: Identify Grand Servants by their special logo
- **Level-based filtering**: Target specific Grand Servant levels
- **Triple CE slot support**: Configure preferences for all 3 CE slots
- **Bond CE requirements**: Specify Bond CE type preferences
- **Automatic mode switching**: FGA adjusts matching for Grand vs normal supports

---

## Grand Servant Detection

FGA identifies Grand Servants by detecting the Grand Servant logo/icon on the support card.

### Grand Servant Indicator

The Grand CE icon appears on support cards when a servant is set up as a Grand Servant. FGA scans for this indicator to determine whether to use Grand Servant matching logic.

### Automatic Detection

Grand Servant mode activates automatically when ANY of these conditions is true:

| Condition                      | Description                              |
| ------------------------------ | ---------------------------------------- |
| **Slot 3 CEs configured**      | You have CEs set for the third slot      |
| **Grand Servant level filter** | Grand Servant filter is not set to "Any" |
| **Bond CE preference**         | Bond CE is not set to "Skip"             |

When Grand Servant mode is active, FGA uses adjusted screen regions optimized for the Grand Servant display format.

---

## Grand Servant Level Filter

Filter Grand Servants by their level.

### Filter Options

| Option              | Behavior                                             |
| ------------------- | ---------------------------------------------------- |
| **Any**             | Accept any servant (Grand or normal)                 |
| **Level 100**       | Only accept Grand Servants at exactly level 100      |
| **Above Level 100** | Only accept Grand Servants above level 100 (grailed) |

### How Level Detection Works

FGA searches for specific Grand Servant level indicators:

- **Level 100**: Detects either the standard Grand Servant logo OR the "Above 100" indicator
- **Above Level 100**: Only detects the grailed Grand Servant indicator

This ensures you can target servants that have been grailed beyond the normal level cap.

---

## Grand Servant CE Configuration

Grand Servants can equip up to 3 Craft Essences. Each slot has different configuration options.

### Slot 1: Main CE

The primary CE slot, functioning similar to normal support CE selection:

| Setting       | Description                   |
| ------------- | ----------------------------- |
| **CE Images** | Select preferred CEs to match |
| **MLB**       | Only accept limit broken CEs  |

Configure through the standard CE selection in Preferred Support settings.

### Slot 2: Bond CE

The second slot is designed specifically for Bond CEs.

| Option     | Behavior                       |
| ---------- | ------------------------------ |
| **Skip**   | Don't check the Bond CE slot   |
| **Any**    | Accept any Bond CE type        |
| **Bond**   | Only accept regular Bond CEs   |
| **Charge** | Only accept NP Charge Bond CEs |

**Bond CE Types Explained:**

| Type             | Description            | Use Case            |
| ---------------- | ---------------------- | ------------------- |
| **Regular Bond** | Standard Bond 10 CE    | General stat boosts |
| **Charge Bond**  | Bond CE with NP charge | Loop/farming builds |

**Note**: FGA detects Bond CEs by their characteristic icon, not the full CE image. The similarity threshold for Bond CE detection is set to 60%.

### Slot 3: Third CE

The third CE slot for additional support:

| Setting        | Description                                 |
| -------------- | ------------------------------------------- |
| **CE Images**  | Select preferred CEs (separate from Slot 1) |
| **MLB Slot 3** | Only accept limit broken CEs in slot 3      |

Slot 3 has its own MLB toggle independent of Slot 1.

---

## How Grand Servant Matching Works

### Detection Flow

```text
┌─────────────────────────────┐
│ Check for Grand CE Logo     │
│ in support card region      │
└─────────────┬───────────────┘
              │
              ▼
      ┌───────┴───────┐
      │ Grand Logo    │
      │  Found?       │
      ▼               ▼
   ┌──────┐       ┌──────┐
   │ Yes  │       │ No   │
   └──┬───┘       └──┬───┘
      │              │
      ▼              ▼
┌──────────┐   ┌──────────────┐
│ Use Grand│   │ Check if mode│
│ Matching │   │ forces Grand │
└──────────┘   └──────────────┘
```

### Grand Matching Checks

When Grand Servant mode is active:

1. **Level Check**: Verify Grand Servant level meets requirements
2. **Slot 1 CE**: Match main CE and check MLB if enabled
3. **Slot 2 Bond CE**: Verify Bond CE type (unless Skip)
4. **Slot 3 CE**: Match third CE and check MLB if enabled
5. **Standard Checks**: Servant skills, ascension, NP level still apply

### Blank CE Detection

For Grand Servants, FGA checks for blank CEs differently:

- Slot 2 uses a specific blank Bond CE image for detection
- Detection region is adjusted for Grand Servant layout

**Note**: The blank Bond CE image is currently optimized for JP server only.

---

## Configuration Examples

### Maximum Grailed Grand Servant

```text
Grand Servant: Above Level 100
Servant: [Your preferred servant images]
Max Ascended: Enabled
Skills: 10/10/10
Slot 1 CE: [Event CE], MLB: Enabled
Slot 2 Bond CE: Any
Slot 3 CE: [Support CE], MLB: Disabled
```

### Any Grand with Charge Bond

```text
Grand Servant: Level 100
Servant: [Your preferred servant images]
Slot 1 CE: [Event CE], MLB: Disabled
Slot 2 Bond CE: Charge
Slot 3 CE: Empty
```

### Non-Grand Compatible Setup

```text
Grand Servant: Any
Servant: [Your preferred servant images]
Skills: X/10/X
CE: [Event CE], MLB: Enabled
```

---

## Tips for Best Results

### Grand Servant Availability

- Not all friends will have Grand Servants set up
- Grand Servant configuration takes extra effort for players
- Consider having fallback non-Grand requirements

### Bond CE Considerations

- Regular Bond CEs provide various stat bonuses
- Charge Bond CEs are rarer but valuable for farming
- "Any" Bond CE option increases match chances

### Level Filter Usage

- "Above Level 100" is very restrictive
- "Level 100" includes more potential matches
- "Any" provides maximum flexibility

### Multi-CE Matching

- Each slot must match for the support to be selected
- Empty CE lists for slots are skipped
- MLB requirements apply per-slot

---

## Troubleshooting

### Grand Servant options not appearing

- Grand Servant features are JP server only
- Check your Battle Config server setting
- Ensure you're using a JP server profile

### Grand Servant not being detected

- The Grand CE logo must be visible on the support card
- Friend may not have set up a Grand Servant
- Try using "Any" to allow normal supports as fallback

### Bond CE not matching

- Bond CE detection uses icon matching (60% similarity)
- Try "Any" instead of specific Bond CE type
- The Bond CE icon must be visible in the expected region

### Slot 3 CE not checking

- Ensure you have CEs configured for Slot 3
- Slot 3 is only checked for Grand Servants
- Verify the CE images are properly captured

### Level detection failing

- Grailed servants above 100 use a different indicator
- "Level 100" accepts both 100 and grailed indicators
- "Above Level 100" is more strict

### Wrong slots being matched

- Grand Servant CE slots have specific positions
- If matching seems off, verify you're targeting the right slot
- Recapture CE images using Support Image Maker

---

## Related Documentation

- [Preferred Servant Selection](preferred-servant.md) - Standard servant configuration
- [Preferred CE Selection](preferred-ce.md) - CE matching details
- [Support Selection Modes](selection-modes.md) - Overall selection configuration
