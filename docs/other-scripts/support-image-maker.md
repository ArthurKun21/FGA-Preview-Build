---
title: Support Image Maker
description: Extract support servant and CE images in FGA Preview. Capture images from the support selection screen for automated support preferences.
tags:
  - scripts
  - support
  - images
  - servants
  - CE
---

# Support Image Maker

Automatically extracts support servant, CE, and friend images from the support selection screen for use in support preferences.

## Overview

The Support Image Maker script captures images of support servants, Craft Essences (CEs), and friend names from the support selection screen. These images are used to configure support preferences for automated farming - allowing FGA to select specific servants or CEs during battle setup.

## How to Start

1. Navigate to the **Support Selection** screen in the game (either from quest start or friend list)
2. Ensure the support entries you want to capture are visible on screen
3. Start the Support Image Maker script
4. The script will extract images from up to 2 visible support entries

## Workflow

```text
┌─────────────────────────────────────────┐
│    Start Support Image Maker Script     │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│     Clean Temporary Extract Folder      │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│   Detect Support Screen Type            │
│   (Support Selection vs Friend List)    │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│   Find Support Entry Bounds on Screen   │
│   (Up to 2 entries)                     │
└─────────────────────┬───────────────────┘
                      │
                      ▼
        ┌─────────────────────────┐
        │  For Each Support Entry │
        └─────────────┬───────────┘
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
    ┌─────────────┐          ┌─────────────┐
    │   Normal    │          │    Grand    │
    │   Servant   │          │   Servant   │
    └──────┬──────┘          └──────┬──────┘
           │                        │
           ▼                        ▼
    ┌─────────────┐          ┌─────────────┐
    │ Extract:    │          │ Extract:    │
    │ - Servant   │          │ - Servant   │
    │ - CE        │          │ - CE Slot 1 │
    │ - Friend    │          │ - Friend    │
    └──────┬──────┘          └──────┬──────┘
           │                        │
           └────────────┬───────────┘
                        │
                        ▼
┌─────────────────────────────────────────┐
│   Save Images to Temporary Directory    │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│     Open Image Review Screen            │
│     (Name and save images)              │
└─────────────────────────────────────────┘
```

## Image Types

The script extracts three types of images from each support entry:

### Servant Image

- Captures the servant portrait from the support card
- Used to identify specific servants during support selection
- Recommended naming: `[Servant Name]/[Ascension]` (e.g., `Waver/Final`)

### CE Image

- Captures the Craft Essence equipped on the support servant
- For Grand Servants: Extracts from CE Slot 1 position
- Used to select supports with specific CEs (e.g., event bonus CEs)

### Friend Image

- Captures the friend/master name from the support card
- Used to prioritize specific friends on your support list
- Position differs between support selection and friend list screens

## Grand Servant Handling

Grand Servants have a different support card layout with multiple CE slots. The script:

1. Detects the Grand CE logo on the support card
2. Adjusts extraction coordinates for the Grand layout
3. Extracts CE from Slot 1 (top CE slot)
4. Uses Grand-specific friend name region

## After Extraction

Once the script completes, you'll see the **Support Image Review** screen:

1. **Preview extracted images** - See all captured servant, CE, and friend images
2. **Enable/disable images** - Check the checkbox for images you want to save
3. **Name your images** - Enter descriptive names for organization:
   - Servant images: Enter servant name and ascension/costume
   - CE images: Enter CE name
   - Friend images: Enter friend's master name
4. **Save** - Images are saved to your support image directory

### Naming Tips

- Use descriptive names for easy identification later
- For servants, include ascension or costume info
- Avoid special characters: `< > " | : * ? \ /`
- Names can include subdirectories using `/` (e.g., `Waver/Bond CE`)

## Exit Reasons

| Exit Reason | Description |
|-------------|-------------|
| **Success** | Images extracted successfully. Review screen will open. |
| **Not Found** | No support entries found on screen. Make sure you're on the support selection screen with visible entries. |

## Tips for Best Results

1. **Scroll to desired supports** - Position the servants you want to capture before starting
2. **Use clear support cards** - Avoid partially visible entries at screen edges
3. **Maximum 2 entries** - The script captures up to 2 support entries per run
4. **Re-run as needed** - Run the script multiple times to capture different supports
5. **Consistent naming** - Use consistent naming conventions for easier management

## Settings

This script has no configurable settings. It automatically:

- Detects screen type (support selection vs friend list)
- Handles both normal and Grand servant layouts
- Saves to the app's support image temporary directory

## Related Features

After creating support images, use them in:

- **Battle Script** → Support Selection settings
- Configure preferred servants, CEs, and friends for automated farming
