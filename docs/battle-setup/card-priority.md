---
title: Command Card Priority
description: Configure command card selection priority in FGA Preview. Set up Buster, Arts, Quick chain preferences and NP card priorities for automated battles.
tags:
  - battle
  - cards
  - NP
  - configuration
---

# Command Card Priority

Configure how FGA selects and prioritizes command cards during battle.

## Overview

The Command Card screen lets you control how the app chooses which attack cards to click during battle. You can set up priorities for different card types, servant order, and chain strategies for each wave of a quest.

## How to Access

1. Open a **Battle Config** from the main app
2. Tap on **Command Card** to open the priority settings

---

## Main Settings

### Use Servant Priority

When enabled, cards are first grouped by servant before applying card priorities.

- **Off**: Cards are selected purely by card type priority (Buster, Arts, Quick)
- **On**: Cards from preferred servants are chosen first, then sorted by card type within each servant's cards

**Example**: If Servant 1 is your highest priority and has a Quick card, it will be selected before Servant 2's Buster card, even if Buster is normally prioritized higher.

### Use Critical Star Priority

When enabled, cards with high critical hit chances are prioritized.

- **Off**: Critical chance is ignored
- **On**: Cards with higher critical percentages are preferred within the same priority level

---

## Wave Configuration

Each quest can have up to 3 waves, and you can set different priorities for each wave. This is useful because your strategy might change as you progress through a quest.

### Adding and Removing Waves

- **Add Wave**: Tap the floating action button (+) to add a new wave configuration (maximum 3)
- **Remove Wave**: Tap the delete icon on a wave card to remove it

---

## Card Priority

The card priority list determines which card types are selected first. Cards at the top have the highest priority.

### Card Types

| Abbreviation | Meaning |
|--------------|---------|
| **B** | Buster card |
| **A** | Arts card |
| **Q** | Quick card |

### Card Affinities

| Prefix | Meaning |
|--------|---------|
| **W** | Weak (class advantage - more damage) |
| _(none)_ | Normal (neutral damage) |
| **R** | Resist (class disadvantage - less damage) |

### Critical Modifier

| Suffix | Meaning |
|--------|---------|
| **C** | Critical (high critical chance) |
| _(none)_ | Non-critical |

### Examples

| Code | Full Name |
|------|-----------|
| **WBC** | Weak Buster Critical |
| **WB** | Weak Buster |
| **BC** | Buster Critical |
| **B** | Buster |
| **WAC** | Weak Arts Critical |
| **RA** | Resist Arts |

### Default Priority

The default card priority order is:

```text
WBC, WAC, WQC, WB, WA, WQ, BC, AC, QC, B, A, Q, RB, RA, RQ
```

This means:

1. Weak cards with critical chance are picked first (best damage)
2. Then weak cards without critical
3. Then normal cards with critical
4. Then normal cards
5. Finally resist cards (lowest priority)

### Reordering Cards

1. Tap **Edit** on the Card Priority section
2. Drag cards up or down using the handle icon
3. Higher position = higher priority

---

## Servant Priority

When "Use Servant Priority" is enabled, you can configure which servant's cards are selected first.

### Team Slots

Servants are identified by their team position (1-6):

| Position | Description |
|----------|-------------|
| **1** | First servant (leftmost in party) |
| **2** | Second servant |
| **3** | Third servant |
| **4** | Fourth servant (first backup) |
| **5** | Fifth servant (second backup) |
| **6** | Sixth servant (third backup) |

### How It Works

```text
Example: Servant Priority = [3, 1, 2]
         Card Priority = [B, A, Q]

Step 1: Group cards by servant
        Servant 3: Arts, Quick
        Servant 1: Buster, Arts
        Servant 2: Quick, Buster

Step 2: For each servant (in priority order), sort their cards
        Servant 3: Arts, Quick (Arts > Quick by card priority)
        Servant 1: Buster, Arts (Buster > Arts)
        Servant 2: Buster, Quick (Buster > Quick)

Step 3: Final order
        [Servant 3 Arts] → [Servant 3 Quick] → [Servant 1 Buster] → ...
```

### Reordering Servants

1. Tap **Edit** on the Servant Priority section
2. Drag servants up or down using the handle icon
3. Servants at the top have their cards selected first

---

## Brave Chains

Brave Chains occur when you select three cards from the same servant, giving bonus damage.

### Options

| Option | Behavior |
|--------|----------|
| **None** | No special handling for brave chains |
| **With NP** | Try to form brave chains with NP cards |
| **With NP Mighty** | Try to form mighty chains (3 different card types) with NP |
| **Avoid** | Actively avoid brave chains by spreading cards across servants |

### When to Use Each

- **None**: Default, let card priority decide naturally
- **With NP**: When your main damage dealer is using their NP and you want to maximize their damage
- **With NP Mighty**: When you want varied card types for the mighty chain bonus
- **Avoid**: When you want to spread damage or generate stars/NP for multiple servants

---

## Rearrange Cards

When enabled, cards are rearranged to optimize damage within the selected cards.

### How Rearrange Cards Works

In FGO, the 3rd card in a chain gets bonus damage. When rearrange is enabled:

1. The app selects the top 3 cards by priority
2. It moves the 2nd highest priority card to the 3rd position
3. This gives the bonus damage to a better card

**Example**:

- Without rearrange: Card A → Card B → Card C (in priority order)
- With rearrange: Card A → Card C → Card B (Card B gets 3rd position bonus)

---

## Per-Wave Strategy Example

Here's an example of how you might configure different waves:

### Wave 1 (Farming weak enemies)

- **Card Priority**: Quick-focused for NP generation
- **Brave Chain**: None
- **Rearrange**: Off

### Wave 2 (Medium enemies)

- **Card Priority**: Arts-focused to charge NP
- **Brave Chain**: Avoid (spread damage)
- **Rearrange**: On

### Wave 3 (Boss wave)

- **Card Priority**: Buster-focused for maximum damage
- **Brave Chain**: With NP (maximize main DPS output)
- **Rearrange**: On

---

## Tips for Effective Configuration

1. **Match priorities to your team**: If your main damage dealer uses Buster cards, prioritize Buster
2. **Consider class advantage**: The "Weak" prefix cards deal more damage against enemies weak to your servants
3. **Use servant priority for focused damage**: Set your main DPS servant as highest priority
4. **Enable critical stars for inconsistent teams**: If your critical star generation varies, enable this to capitalize on lucky draws
5. **Set up multiple waves**: Different priorities for different phases of a quest can significantly improve clear times

---

## Troubleshooting

### Cards aren't being selected in my expected order

- Check if "Use Servant Priority" is affecting the selection
- Verify the card priority list order
- Remember that critical stars can affect selection when enabled

### Brave chains aren't forming

- Ensure "Brave Chain" is set to "With NP" or "With NP Mighty"
- The servant needs to have 3 cards available on screen
- NPs must be ready for NP-based brave chains

### The app is picking resist cards

- Move resist cards lower in the priority list
- Or remove them entirely if you never want them selected

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - Overall battle automation
- [Skill Maker](skill-maker.md) - Configure skill execution during battle
