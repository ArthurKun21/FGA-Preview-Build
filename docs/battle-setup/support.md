---
title: Support Selection
description: Configure support servant selection in FGA Preview. Set up preferred servants, CEs, NP levels, append skills, and friend preferences for automated farming.
tags:
  - battle
  - support
  - servants
  - configuration
---

# Support

Configure how FGA selects support servants from your friends list during battle.

## Overview

The Preferred Support screen lets you specify exactly which support servants, Craft Essences, and friends you want FGA to select. The app will scroll through your support list looking for matches based on your criteria.

## How to Access

1. Open a **Battle Config** from the main app
2. Tap on **Support Selection**
3. Select **Preferred** mode
4. Tap **Preferred Support** to configure preferences

---

## Support Class Selection

Choose which servant class tab to search in.

| Class | Description |
|-------|-------------|
| **None** | Don't filter by class (search current tab) |
| **All** | Search the "All" tab |
| **Saber** | Search only Saber supports |
| **Archer** | Search only Archer supports |
| **Lancer** | Search only Lancer supports |
| **Rider** | Search only Rider supports |
| **Caster** | Search only Caster supports |
| **Assassin** | Search only Assassin supports |
| **Berserker** | Search only Berserker supports |
| **Extra** | Search Extra class (Ruler, Avenger, etc.) |
| **Mix** | Search the Mix/Event tab |

### Also Check All

When enabled and a specific class is selected, FGA will also check the "All" tab if no match is found in the class tab.

!!! note
    This option is not available when "None", "All", or "Mix" is selected.

---

## Preferred Servants

Select which support servants you want FGA to look for.

### Adding Servants

1. Tap **Add** in the Preferred Servants section
2. Select one or more servant images from your collection
3. Tap **Save** to confirm

**Important**: You must first create servant images using the **Support Image Maker** feature. Without images, FGA cannot identify servants.

### Servant Filters

Once you've selected servants, you can apply additional filters:

#### Max Ascended

When enabled, only selects servants showing the golden ascension star (final ascension artwork).

#### Max Skills

Specify which skills must be at level 10:

| Display | Meaning |
|---------|---------|
| **10** | Skill must be maxed |
| **X** | Skill level doesn't matter |

Example: `10 / X / 10` means skills 1 and 3 must be maxed, skill 2 can be any level.

#### Check Append Skills

When enabled, checks append skill levels in addition to regular skills.

**Append Skills Display** (when enabled):

- On JP server: Shows 5 append skill slots
- On other servers: Shows 3 append skill slots

#### Noble Phantasm Level

When enabled, only selects servants with at least the specified NP level (1-5).

!!! note
    NP1 is always available, so setting minimum to 1 will match any servant.

!!! info "Servant's NP level match the setting but wasn't selected"
    Due to optical character recognition (OCR) limitations, NP level detection may not always be accurate.

    Although thanks to recent migration from Tesseract to PaddleOCR, detection accuracy has improved.

!!! warning "Server support limitation"
    NP level detection currently **only** works on **English** and **Japanese** servers.

    Please [create an issue on GitHub](https://github.com/ArthurKun21/FGA-Preview-Build/issues/new?template=feature_request.yml) so we can coordinate adding support for other languages.

---

## Grand Servant Support (JP Server)

Grand Servants are a new feature on the Japanese server where players can equip up to 3 Craft Essences on a single support servant.

### Grand Servant Tag Options

| Option | Behavior |
|--------|----------|
| **Any** | Accept any servant (Grand or normal) |
| **Level 100** | Only accept Grand Servants at exact level 100 or higher |
| **Above Level 100** | Only accept Grand Servants above level 100 |

!!! warning
    Grand Servant tag currently only works on **Grand Duels** as such using it in normal quests may lead to no matches being found.

---

## Preferred Craft Essences

Select which Craft Essences the support servant should have equipped.

### For Normal Supports

- **CE Selection**: Choose one or more CEs to look for
- **Max Limit Break (MLB)**: When enabled, only selects if the CE has the MLB star

### For Grand Servants (JP Server)

Grand Servants have 3 CE slots:

#### Slot 1 (Main CE)

- Select preferred CEs
- Enable MLB if you want only limit broken versions

#### Slot 2 (Bond CE)

| Option | Behavior |
|--------|----------|
| **Skip** | Don't check slot 2 |
| **Any** | Accept any Bond CE (regular or charge type) |
| **Bond** | Only accept regular Bond CEs |
| **Charge** | Only accept NP Charge Bond CEs |

#### Slot 3 (Third CE)

- Select preferred CEs
- Enable MLB separately for slot 3
- You can only use [Mana Prism shop CEs](https://fategrandorder.fandom.com/wiki/Category:Shop_Craft_Essences) for slot 3

### Adding CE Images

1. Tap **Add** in the CE section
2. Select one or more CE images from your collection
3. Tap **Save** to confirm

!!! tip
    CE images should be created using the **Support Image Maker** feature for best results.

---

## Friend Selection

Control whether FGA only selects from your friends list.

### Friends Only

When enabled, FGA will only select support servants from players on your friends list (not randoms or follow-only players).

### Preferred Friends

When "Friends Only" is enabled, you can specify particular friends:

1. Tap **Add** in the Friends section
2. Select friend name images from your collection
3. Tap **Save** to confirm

**How it works**: If preferred friends are set, FGA will prioritize those friends. If none are found, it will select any friend that matches your servant/CE criteria.

---

## Support Image Maker

Before using Preferred Support, you need to create images for servants, CEs, and friends.

### Creating Support Images

1. Navigate to the **Support Selection** screen in FGO
2. Start FGA's **Support Image Maker** script
3. Tap on each servant/CE/friend you want to save
4. Images are automatically saved to your device

### Image Storage Location

Images are stored in your FGA support images folder:

- Servants: `support/servant/`
- Craft Essences: `support/ce/`
- Friends: `support/friend/`

---

## How Support Selection Works

```text
┌─────────────────────────────────────────┐
│       Start Support Selection           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │  Navigate to Class Tab │
         │    (if configured)     │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   Scan Visible List    │◄──────┐
         └────────────┬───────────┘       │
                      │                   │
                      ▼                   │
         ┌────────────────────────┐       │
         │   Check Each Support   │       │
         │   • Servant match?     │       │
         │   • CE match?          │       │
         │   • Friend match?      │       │
         │   • Skills maxed?      │       │
         │   • NP level OK?       │       │
         └────────────┬───────────┘       │
                      │                   │
           ┌──────────┴──────────┐        │
           │ Match               │ No     │
           │ Found?              │ Match  │
           ▼                     ▼        │
     ┌──────────┐        ┌────────────┐   │
     │  Select  │        │ Scroll     │───┘
     │  Support │        │ Down       │
     └──────────┘        └─────┬──────┘
                               │
                     ┌─────────┴─────────┐
                     │ Bottom            │
                     │ of List?          │
                     ▼                   ▼
              ┌────────────┐      ┌────────────┐
              │ Check "All"│      │ Refresh    │
              │ Tab        │      │ List       │
              └────────────┘      └────────────┘
```

---

## Matching Priority

When multiple supports match your criteria, FGA selects the **first match** found while scrolling through the list.

### Match Requirements

For a support to be selected, ALL of these must be true:

1. **Servant matches** (if servants are specified)
2. **CE matches** (if CEs are specified, or no blank CE if none specified)
3. **Friend matches** (if Friends Only is enabled)
4. **Ascension matches** (if Max Ascended is enabled)
5. **Skills match** (if Max Skills are specified)
6. **Append skills match** (if Check Append is enabled)
7. **NP level matches** (if Check NP Level is enabled)
8. **Grand Servant matches** (if Grand filtering is enabled, JP only)

---

## Tips for Effective Configuration

### For Faster Matching

1. **Use specific class tabs**: Selecting a class reduces the search space
2. **Enable "Also Check All"**: Provides a fallback if the class tab doesn't have matches
3. **Don't over-specify**: Each additional requirement reduces available matches

### For Reliable Matching

1. **Create clear images**: Use Support Image Maker for accurate servant/CE detection
2. **Update images after ascension**: Re-capture servants after they change artwork
3. **Add multiple servants**: Having fallback options prevents failed selections

### For Events

1. **Look for event CEs**: Many farming supports equip event bonus CEs
2. **Use the Mix tab**: Event supports often appear in the Mix/Event class tab
3. **Temporarily disable MLB**: Early in events, MLB CEs may be rare

---

## Troubleshooting

### Support not being selected

- **Check images**: Ensure servant/CE images are captured correctly
- **Verify class tab**: Make sure you're searching the right class
- **Relax requirements**: Try disabling Max Ascended, Max Skills, or NP Level checks
- **Check MLB setting**: Disable MLB requirement if supports might not have it

### Script keeps refreshing the list

- No matching support was found
- Try adding more servant/CE options
- Check if your requirements are too strict

### Wrong support selected

- Your images may match multiple servants
- Re-capture more specific images
- Add additional filter requirements

### Grand Servant features not showing

- Grand Servant is JP server only so far
- Ensure your Battle Config is set to JP server

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - Overall battle automation
- [Support Image Maker](../other-scripts/support-image-maker.md) - Create support images
