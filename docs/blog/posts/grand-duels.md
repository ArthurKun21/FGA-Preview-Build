---
title: Setup for Grand Duels
description: Complete guide to setting up FGA Preview for Grand Duels with Grand Servant support configuration and CE slot management.
categories:
    - Guides
tags:
    - grand duels
    - grand servants
    - support
    - setup
    - JP server
date:
    created: 2025-12-10
    updated: 2026-10-27
---

# Setup for Grand Duels

Configure FGA Preview to automatically select the best Grand Servant supports for Grand Duel events.

<!-- more -->

## Overview

Grand Duels are a new special quest on the Japanese server. You battle with servants of a specific class. You can only use servants of the designated class, so support selection is crucial for success.

FGA Preview includes special support for Grand Duels. You can:

- **Target Grand Servants specifically** with enhanced filtering options
- **Configure all three CE slots** unique to Grand Servants
- **Set level requirements** to find the strongest supports

> [!WARNING]
> **JP Server Only**
>
> Grand Servant features are currently only available on the **Japanese server** and **in Grand Duels**. The Grand Servant options do not appear on other game servers.

---

## Introduction to Grand Duels

Grand Duels run for one week at a time. Each rotation features a specific servant class. During the event:

- **Free Period**: For the first week, you can participate without consuming Storm Pods
- **After Free Period**: Battles consume Storm Pods as usual
- **Class Restriction**: You can only bring servants of the featured class

The key advantage of Grand Duels is **Grand Servants** from your support list. These are special support servants that can equip up to three Craft Essences.

---

## Normal Support vs Grand Servant Support

Grand Servants in the support selection screen look different from normal supports.

![Grand Duel Support Screen](../../assets/post/grand-duels/grand-servants-in-grand-duel-support-screen.png)

### Key Differences

| Feature              | Normal Support            | Grand Servant Support                        |
| -------------------- | ------------------------- | -------------------------------------------- |
| **Visual Indicator** | Standard servant card     | Special golden outline/icon                  |
| **CE Slots**         | 1 slot                    | 3 slots                                      |
| **NP level parsing** | Standard NP text position | Alternate NP text position for Grand layouts |
| **Availability**     | All quests                | Grand Duels only                             |

### Grand Servant CE Slots Explained

Grand Servants can equip up to three Craft Essences. Each slot has specific restrictions:

| Slot       | CE Type            | Description                                                                                                                             |
| ---------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Slot 1** | Any CE             | Works the same as normal support CEs. Can be any Craft Essence.                                                                         |
| **Slot 2** | Bond CE Only       | Limited to Bond CEs only. Players can choose between keeping the Bond CE effect or a 50% NP starting charge.                            |
| **Slot 3** | Mana Prism CE Only | Limited to [Mana Prism shop CEs](https://fategrandorder.fandom.com/wiki/Category:Shop_Craft_Essences) such as Bella Lisa, Teatime, etc. |

---

## How to Set Up Grand Duel Support in FGA

Follow these steps to configure FGA for Grand Duel support selection.

### Step 1: Access Preferred Support Settings

1. Open FGA Preview
2. Open or create a **Battle Config**
3. Tap **Support Selection**
4. Select **Preferred** mode
5. Tap **Preferred Support** to open the configuration screen

### Step 2: Configure Servant Selection

![Grand Duel Preferred Servant](../../assets/post/grand-duels/grand-duel-preferred-servant.png)

In the **Preferred Servants** section:

1. Tap **Add** to select servant images
2. Select the Grand Servants you want to target
3. Tap **Save** to confirm

#### Grand Servant Tag Options

| Option              | Behavior                                                      | Preview                                                                               |
| ------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Any**             | Accept any servant (Grand or normal)                          | ![Servant](../../assets/post/grand-duels/frame_servant.png)                              |
| **Level 100**       | Only accept Grand Servants at level 100 or higher             | ![Grand Servant (100+)](../../assets/post/grand-duels/frame_grand_servant.png)           |
| **Above Level 100** | Only accept Grand Servants above level 100 (grailed servants) | ![Grailed Grand Servant](../../assets/post/grand-duels/frame_grand_servant_over_100.png) |

> [!TIP]
> Select **Above Level 100** to get a fully-invested Grand Servant with maximum stats.

> [!WARNING]
> The **Caster Grand Duel** runs at the same time as a Lotto event. The lotto drops overlap with the tag UI. This makes the tags hard to detect.
>
> In this case, use the **Any** option. Rely on the CE slot configuration to filter for Grand Servants.
>
> ![Grand Duel tag error](../../assets/post/grand-duels/grand-duel-tag-lotto-error.png)

### Step 3: Configure CE Slots

![Grand Duel Preferred Servant](../../assets/post/grand-duels/grand-duel-preferred-ces.png)

For Grand Servants, configure all three CE slots:

#### Slot 1 (Main CE)

1. Tap **Add** under **CE Slot 1**
2. Select the Craft Essences you want
3. Enable **Max Limit Break (MLB)** if you only want fully limit broken CEs
4. Tap **Save**

#### Slot 2 (Bond CE)

Select how FGA should handle the Bond CE slot:

| Option     | When to Use                                   |
| ---------- | --------------------------------------------- |
| **Skip**   | You don't care about the Bond CE slot         |
| **Any**    | Accept any Bond CE configuration              |
| **Bond**   | Only accept if using the Bond CE effect       |
| **Charge** | Only accept if using the 50% NP charge option |

#### Slot 3 (Mana Prism CE)

1. Tap **Add** under **CE Slot 3**
2. Select Mana Prism CEs (Bella Lisa, Teatime, etc.)
3. Enable **Max Limit Break (MLB)** if needed (Recommended)
4. Tap **Save**

> [!NOTE]
> Slot 3 only accepts Mana Prism shop CEs. Other CEs do not match Grand Servants.

---

## How FGA Detects Grand Servants

FGA detects Grand Servants with the following workflow:

```mermaid
flowchart TD
    A[Start Support Selection] --> B[Scan Support List]
    B --> C[Check for Grand CE<br/>Logo on Each Support]
    C --> D{Grand CE<br/>Detected?}
    D -->|Yes| E[Grand Servant]
    D -->|No| F[Normal Support]
    E --> G[Check All<br/>3 CE Slots]
    F --> H[Check CE<br/>Slot 1]
```

FGA enters "Grand Servant Mode" automatically when:

- You have CEs selected in **Slot 3**, OR
- You have a **Grand Servant Tag** option selected (not "Any"), OR
- You have a **Bond CE** option selected (not "Skip")

---

## Tips for Best Results

1. **Use NP Level Detection** - Select Grand Support Servants with higher NP levels for better performance.

    A new Optical Character Recognition (OCR) model improves NP level detection accuracy and makes it more reliable.

    ![NP Level Detection](../../assets/post/grand-duels/np-level-detection.png)

2. **Use Support Servant as Carry** - If possible, use a Grand Servant from your supports list as your main damage dealer. This maximizes synergy with support servants.

3. **Save Bond Grails** - Grand Duels offer high bond points. Use this opportunity to level up your Servants' bond levels. **More bond level means more SQ rewards!**

---

## Related Documentation

- [Support Selection](../../battle-setup/support.md) - Complete guide to support configuration
- [Support Image Maker](../../scripts/support-image-maker.md) - How to create servant and CE images
- [Battle Config](../../battle-setup/config.md) - Setting up battle configurations
