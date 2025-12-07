---
title: Preferred CE Selection
description: Configure FGA Preview to find and select support servants with specific Craft Essences. Includes MLB requirements and Grand Servant multi-slot CE support.
tags:
    - support
    - craft essence
    - ce
    - selection
    - configuration
---

# Preferred CE Selection

Configure FGA to search for support servants equipped with specific Craft Essences (CEs), with options for Max Limit Break (MLB) requirements and Grand Servant multi-slot CE support.

## Overview

Preferred CE Selection allows you to specify which Craft Essences a support servant should have equipped. FGA scans the CE portion of each support entry, comparing against your configured CE images.

## Key Features

- **Image-based CE matching**: Select CEs by their image
- **MLB verification**: Only accept limit broken CEs showing the golden star
- **Blank CE detection**: Automatically reject supports with no CE equipped
- **Grand Servant support**: Configure up to 3 CE slots for JP server Grand Servants
- **Multiple CE options**: Add several CEs as acceptable choices

---

## Normal Support CE Selection

For standard supports (non-Grand Servants), each support has one CE slot.

### Adding CE Images

1. Use the **Support Image Maker** script to capture CE images
2. Open your Battle Config and navigate to **Preferred Support**
3. Tap **Add** in the CE section
4. Select one or more CE images
5. Tap **Save** to confirm

### Max Limit Break (MLB)

When enabled, FGA only selects supports where the CE displays the golden limit break star.

| Setting      | Behavior                             |
| ------------ | ------------------------------------ |
| **Disabled** | Accept any CE matching the image     |
| **Enabled**  | Only accept CEs showing the MLB star |

The MLB star appears on the CE when it has been fully limit broken (5 copies merged).

### Blank CE Handling

When you have CE preferences configured:

| CE List     | Blank CE Behavior                     |
| ----------- | ------------------------------------- |
| **Empty**   | Supports with blank CEs are rejected  |
| **Has CEs** | Must match one of your configured CEs |

If you don't configure any CEs, FGA still checks that the support has some CE equipped (not blank).

---

## Grand Servant CE Selection (JP Server Only)

Grand Servants on the Japanese server can equip up to 3 Craft Essences. FGA supports checking all three slots.

### CE Slot 1 (Main CE)

The primary CE slot, functioning similar to normal support CE selection:

- Configure preferred CEs through the main CE selection
- Enable MLB requirement if needed
- Matches the first CE displayed on the Grand Servant

### CE Slot 2 (Bond CE)

The second slot is specifically designed for Bond CEs. Configure the Bond CE requirement:

| Option     | Behavior                                    |
| ---------- | ------------------------------------------- |
| **Skip**   | Don't check the second CE slot              |
| **Any**    | Accept any Bond CE (regular or charge type) |
| **Bond**   | Only accept regular Bond CEs                |
| **Charge** | Only accept NP Charge Bond CEs              |

**Bond CE Types:**

| Type                | Description                    |
| ------------------- | ------------------------------ |
| **Regular Bond CE** | Standard Bond 10 Craft Essence |
| **Charge Bond CE**  | Bond CE with NP charge effect  |

When checking for Bond CEs:

- FGA first verifies the slot is not blank
- Then checks for the specific Bond CE type icon

### CE Slot 3 (Third CE)

The third CE slot for Grand Servants:

- Configure separately from Slot 1 CEs
- Has its own MLB toggle independent of Slot 1
- Uses the same image matching as Slot 1

---

## How CE Matching Works

### Normal Support Matching

```text
┌─────────────────────────────┐
│ Load CE Images              │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ For Each Support Entry:     │
│ ┌─────────────────────────┐ │
│ │ No CEs configured?      │ │
│ │ → Check not blank       │ │
│ └───────────┬─────────────┘ │
│             │               │
│             ▼               │
│ ┌─────────────────────────┐ │
│ │ Search for CE image     │ │
│ │ in support region       │ │
│ └───────────┬─────────────┘ │
│             │               │
│             ▼               │
│ ┌─────────────────────────┐ │
│ │ Check MLB star          │ │
│ │ (if enabled)            │ │
│ └─────────────────────────┘ │
└─────────────────────────────┘
```

### Grand Servant Matching

```text
┌─────────────────────────────┐
│ Check Slot 1 (Main CE)      │
│ • Match configured CEs      │
│ • Check MLB if enabled      │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Check Slot 2 (Bond CE)      │
│ • Skip, Any, Bond, or Charge│
│ • Verify not blank          │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Check Slot 3 (Third CE)     │
│ • Match configured CEs      │
│ • Check MLB if enabled      │
└─────────────────────────────┘
```

### MLB Detection

The limit break star is detected using image matching:

- For normal CEs: Checks the standard MLB star position
- For Grand Servant triple-slot CEs: Checks adjusted positions for each slot
- Similarity threshold is configurable in support preferences

---

## Configuring Multiple CEs

You can add multiple CEs as acceptable options:

| Configuration    | Behavior                          |
| ---------------- | --------------------------------- |
| **Single CE**    | Only matches that specific CE     |
| **Multiple CEs** | Matches ANY of the configured CEs |

This is useful for:

- Event CEs with different artwork versions
- Accepting multiple bonus CEs during events
- Having fallback options for rarer CEs

---

## Tips for Best Results

### Event Farming

- Add all event bonus CEs to increase match chances
- Consider disabling MLB early in events when few exist
- Update CE images when event CEs are released

### MLB Requirements

- MLB CEs may be rare among friends early in events
- Start with MLB disabled, enable after event progresses
- Some friends may have MLB but show different artwork

### Image Capture Quality

- Capture CEs using Support Image Maker
- Avoid capturing during animations
- Include enough of the CE image to be distinctive

### Grand Servant CEs

- Slot 2 uses icon matching, not full CE matching
- Bond CEs are identified by their characteristic icon
- Slot 3 requires separate CE images from Slot 1

---

## Troubleshooting

### CE not being matched

- **Verify image quality**: Recapture using Support Image Maker
- **Check MLB setting**: Disable if CE might not be limit broken
- **Multiple versions**: Some CEs have different artwork versions

### MLB not detected

- Ensure the MLB star is visible on the support screen
- Check similarity threshold in support preferences
- The star must be in the expected position

### Grand Servant CE slots not checking

- Grand Servant mode is JP server only
- Verify your Battle Config is set to JP server
- Check that Grand Servant mode is properly enabled

### Blank CE keeps getting selected

- This shouldn't happen if you have CEs configured
- Verify your CE list is not empty
- Check that the support is actually showing a CE

### Bond CE type not matching

- The Bond CE icon detection uses 60% similarity
- Some Bond CE variations may not match perfectly
- Try using "Any" instead of specific type

---

## Related Documentation

- [Grand Servant Selection](grand-servant.md) - Complete Grand Servant configuration
- [Preferred Servant Selection](preferred-servant.md) - Configure servant matching
- [Support Image Maker](../other-scripts/support-image-maker.md) - Create CE images
