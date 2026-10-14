---
title: Support Selection
description: Configure preferred support selection in FGA Preview. Set preferred servants, Craft Essences, NP levels, append skills, and friend preferences for automated farming.
tags:
  - battle
  - support
  - servants
  - configuration
---

# Support

This page describes support selection. FGA uses these settings to pick a support servant from the support list in the game.

## Overview

The **Preferred Support** screen holds the requirements for a support. FGA reads each entry on the support screen. It selects the first entry that meets all of your requirements.

The requirements come from three groups:

| Group | What it controls |
|-------|------------------|
| **Servants** | The servants that you accept, and the filters for each servant. |
| **Craft Essences** | The CEs that the support must equip. |
| **Friends** | The friend names that you accept. |

You can add servants and CEs from the atlas data, or from the support images on your device. An atlas entry needs no image on your device. FGA downloads the atlas images when it needs them.

The atlas data comes from the `fga-data` snapshot. The app ships with a bundled copy of the snapshot. You can also download a newer release.

## How to Access

1. Open a **Battle Config** from the main app.
2. Tap **Support Selection**.
3. Select **Preferred** mode.
4. Tap **Preferred Support**.

!!! note "Preferred mode needs one criterion"
    Preferred mode needs at least one of these two items:

    - One enabled servant.
    - One default Craft Essence.

    Friend settings only narrow an existing search. They do not start a search. If you set no servant and no CE, the battle script stops. The exit reason is `SupportSelectionPreferredNotSet`.

---

## Support Class Selection

Choose the class tab that FGA searches.

| Class | Description |
|-------|-------------|
| **None** | Does not filter by class. FGA searches the current tab. |
| **All** | Searches the "All" tab. |
| **Saber** | Searches only Saber supports. |
| **Archer** | Searches only Archer supports. |
| **Lancer** | Searches only Lancer supports. |
| **Rider** | Searches only Rider supports. |
| **Caster** | Searches only Caster supports. |
| **Assassin** | Searches only Assassin supports. |
| **Berserker** | Searches only Berserker supports. |
| **Extra** | Searches the Extra class (Ruler, Avenger, and similar classes). |
| **Mix** | Searches the Mix or Event tab. |

### Also Check All

When you enable this option and you select a class, FGA also searches the "All" tab. It searches the "All" tab after it finds no match in the class tab.

!!! note
    This option is not available when you select "None", "All", or "Mix".

### Enable Send Friend Request

This switch is the master switch for all friend request features.

- The switch is off by default.
- When the switch is off, FGA rejects every friend request after battle.
- FGA keeps the per-servant switch and the default CE switch disabled while the master switch is off.

---

## Preferred Servants

### Add a Servant From the Atlas

1. Tap **Add** in the Preferred Servants section. The atlas list opens.
2. Find the servant in the list.
3. Tap the servant. The app adds the servant and opens its detail screen.

The atlas list contains the servants from the `fga-data` snapshot.

### Atlas List Options

The top bar of the atlas list has a search field and two icons.

| Control | Function |
|---------|----------|
| Search field | Filters the list by name. |
| Display options icon | Opens the view, sort, and filter options. |
| Support images icon | Opens the support images that you stored on your device. |

The **Display options** pane has three sections.

| Section | Options |
|---------|---------|
| View | List view or Grid view. |
| Sort by | No. low to high, No. high to low, Name A to Z, Name Z to A, Rarity low to high, or Rarity high to low. |
| Filters | Rarity chips, and class chips for servants. Tap **Clear all** to remove every filter. |

- The search text and the filters apply to the open list only.
- The view mode and the sort order persist for each kind.
- The filter chips apply to the open picker only. They do not persist.

### Add a Servant From Stored Support Images

1. Tap **Add** in the Preferred Servants section. The atlas list opens.
2. Tap the support images icon in the top bar.
3. Tap a servant entry.

- Entries that you already added have a check mark. You cannot add them a second time.
- Tap an entry that you already added to open its detail screen.

!!! tip "Image source"
    You must first create servant images with the **Support Image Maker** feature. Without images, FGA cannot identify servants.

### Servant Detail Screen

The app opens the servant detail screen after it adds a servant.

- An atlas servant has a carousel of face images. The app loads these faces from the atlas data.
- An image servant has a carousel of your stored support images.

Tap the remove icon in the top bar. This action removes the servant from this config.

### Servant Settings

Each servant has its own settings. Open the servant card to change them.

| Setting | Behavior |
|---------|----------|
| **Use this Servant?** | Enables or disables this servant. A disabled servant stays in the config, but FGA does not search for it. |
| **Auto Send Friend Request** | Sends a friend request for this servant. The master switch must be on. |
| **Max-ascended** | Accepts only servants that have the golden ascension star. |
| **Max Skills** | Sets which of the three skills must be at level 10. |
| **Max Appends** | Turns on the append skill level check. |
| **Noble Phantasm (Minimum NP Level)** | Sets the minimum NP level from 1 to 5. |
| **Grand Servant** | Sets the Grand servant requirement. This setting appears only on servers that support Grand servants. |
| **Servant Matching** | Sets the image matching mode and threshold for this servant. |

#### Max Skills

Tap a skill button to change the requirement for that skill.

| Display | Meaning |
|---------|---------|
| **10** | The skill must be maxed at level 10. |
| **X** | The skill level does not matter. |

For example, `10 / X / 10` means that skills 1 and 3 must be maxed. Skill 2 can be at any level.

The summary badge has the same value. For example, the badge is `X / X / X` when you set no skill requirement.

#### Max Appends

Turn on this switch to check append skill levels. The editor has five append skill rows. Tap a row to require that append skill at level 10.

- The row is `10` when you require that append skill.
- The row is a dash when you do not require that append skill.
- The summary badge is **Any** when the switch is off.

!!! note "How FGA reads append skills"
    The support list has either the skill levels or the append skill levels.

    FGA switches the list to the append display, reads the levels under one screen snapshot, and then switches back to the skill display.

    FGA reads the five append skill level icons at the Japanese server positions on every server.

    FGA skips the check for an entry that has the **Follow** indicator. A follow entry has your own append skills, which do not apply.

#### Noble Phantasm

Set the minimum NP level. FGA accepts a servant when its NP level is equal to or above this value.

- Level 1 accepts any servant. FGA then does not read the NP text.
- FGA reads the NP level from a different region in the Grand layout.
- A failed text read returns level 1. So a failed read fails only when you require level 2 or higher.

!!! info "The NP level matches the setting but FGA did not select the servant"
    Optical character recognition (OCR) can read the NP level incorrectly.

    The move from Tesseract to PaddleOCR improved the read accuracy.

!!! warning "Server support limitation"
    NP level detection currently works on **English** and **Japanese** servers only.

    Please [create an issue on GitHub](https://github.com/ArthurKun21/FGA-Preview-Build/issues/new?template=feature_request.yml) so we can coordinate adding support for other languages.

#### Grand Servant

| Option | Behavior |
|--------|----------|
| **Any Servant** | Accepts any servant. |
| **Any Grand Servant** | Accepts a Grand servant at level 100 or higher. |
| **Only Grand Servant Above Level 100** | Accepts a Grand servant above level 100. |

!!! warning
    The Grand servant tag currently works in **Grand Duels** only. Use in a normal quest can return no match.

FGA treats an entry as a Grand servant when it finds the Grand CE logo on that entry. FGA also treats an entry as a Grand servant when you set this option, or when the CE configuration uses a Grand slot.

- On a server without Grand support, this option has no effect.
- FGA checks the Grand requirement in the Grand layout only.

---

## Preferred Craft Essences

### Default CE and Custom CE

- **Default Preferred Craft Essences** - The app applies these CEs to every servant.
- **Custom Preferred Craft Essences** - The app applies these CEs to one servant only.

Each servant has a **Default** page and a **Custom** page for CEs. Tap the toggle at the top to change the page. The app saves your choice, so your custom data stays when you return to the **Default** page.

### CE Slots

| Slot | Applies to | Contents |
|------|------------|----------|
| **Slot 1** | Every support | One or more preferred CEs. |
| **Slot 2** | Grand servants only | A bond CE requirement. |
| **Slot 3** | Grand servants only | One or more preferred CEs. |

The slot 2 and slot 3 settings appear only on servers that support Grand servants.

#### Slot 1

1. Tap **Add Preferred Support** in slot 1.
2. Pick a CE from the atlas list, or tap the support images icon to pick from your stored images.
3. Tap the CE.

- FGA rejects a normal support that has a blank CE when you configure CEs in slot 1.
- In the Grand layout, the blank CE check does not apply.

#### Slot 2 (Bond CE)

| Option | Behavior |
|--------|----------|
| **Skip** | Does not check slot 2. |
| **Any** | Accepts any bond CE. |
| **Bond CE** | Accepts a regular bond CE only. |
| **NP Charge** | Accepts an NP charge bond CE only. |

#### Slot 3

1. Tap **Add Preferred Support** in slot 3.
2. Pick a CE from the atlas list, or tap the support images icon to pick from your stored images.
3. Tap the CE.

Use [Mana Prism shop CEs](https://fategrandorder.fandom.com/wiki/Category:Shop_Craft_Essences) in slot 3.

### Max Limit Break (MLB)

Each CE entry has its own **Max-limit broken** switch. Turn on the switch to require the MLB star for that CE.

- The switch applies to that CE only.
- The switch applies to that CE in slot 1 and in slot 3.

### CE Matching

Each CE entry has its own matching settings.

| Setting | Behavior |
|---------|----------|
| **CE Matching** | Sets the matching mode for that CE. |
| **Override matching threshold** | Turns on a custom matching threshold for that CE. |
| **Matching Threshold** | Sets the threshold. Tap the reset control to return to the mode default. |

See [Image Matching](#image-matching) for the mode and threshold details.

### Grand Servant CE Match

This setting decides how FGA combines the slot 1 result and the slot 3 result. The setting applies to the default CE and to each custom CE.

| Option | Behavior |
|--------|----------|
| **Match Both** | Slot 1 and slot 3 must both match your preferred CEs. |
| **Match Either** | Slot 1 or slot 3 must match your preferred CEs. |

!!! note
    The control stays disabled until you configure CEs in slot 1 and slot 3. An empty slot always matches. So **Match Either** with an empty slot would pass without a real match.

### Send Friend Request on Default CE Match

This switch is in the default CE screen. It controls the friend request that follows a default CE match.

- The master switch **Enable Send Friend Request** must be on.
- The switch is on by default.

When FGA picks a support that uses the default CE, and the picked CE matches your default configuration, FGA sends the friend request. When the picked servant uses a custom CE, this switch has no effect on that pick.

FGA rejects the friend request when your friend list is full.

---

## Friend Selection

### Default Friend and Custom Friend

- **Default Preferred Friends** - The app applies these friend settings to every servant.
- **Custom Preferred Friends** - The app applies these friend settings to one servant only.

Each servant has a **Default** page and a **Custom** page for friends, the same as the CE pages.

### Friends Only

Turn on this switch to accept only supports from players on your friends list. FGA then rejects every support that is not from a friend.

!!! note
    The friend names apply only when **Friends Only** is on. When the switch is off, FGA ignores the stored names and accepts any player.

### Preferred Friends

1. Tap **Add Preferred Support** in the friend section.
2. Pick one or more friend name images.
3. Tap **Save**.

FGA requires a match on one of these names. When you set no name, FGA applies the **Friends Only** gate only.

---

## Image Matching

Each servant and each CE entry has its own matching settings. The settings apply to that entry only.

### Matching Mode

| Mode | How it works | Default similarity |
|------|--------------|--------------------|
| **Grayscale** | Converts both images to grayscale and uses normalized correlation. A higher score is better. | 80 percent |
| **Colored** | Keeps both images in color and uses normalized squared difference. A lower difference is better. | 95 percent |

- The slider sets a similarity value as a percent.
- The **Grayscale** range is 50 to 100 percent.
- The **Colored** range is 80 to 100 percent.
- A higher value requires a closer match in both modes.

### Threshold Override

Turn on **Override matching threshold** to set a custom threshold. Then drag the slider.

- The slider range depends on the mode.
- Tap the reset control to return to the default similarity of the mode.
- A mode change resets the threshold to the default of the new mode.
- The summary badge has the custom threshold when the override is on.

!!! tip "When to change the threshold"
    Lower the threshold when FGA cannot find an entry that you can see on the screen.

    Raise the threshold when FGA picks the wrong entry.

    Test a change on one quest before you start a long farming run.

---

## Support Image Maker

Entries from the atlas data need no image on your device. Entries from your stored images do.

### Create Support Images

1. Navigate to the **Support Selection** screen in FGO.
2. Start the **Support Image Maker** script.
3. Tap each servant, CE, or friend that you want to save.
4. The app saves the images on your device.

### Image Storage Location

The app stores the images in your FGA support images folder:

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
         │  Preload support images │
         │   (fail early on error) │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │ Navigate to the class  │
         │    tab (if set)        │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   Scan visible list    │◄──────┐
         └────────────┬───────────┘       │
                      │                   │
                      ▼                   │
         ┌────────────────────────┐       │
         │   Check each entry     │       │
         │   • Servant match?     │       │
         │   • CE match?          │       │
         │   • Friend match?      │       │
         │   • Skills maxed?      │       │
         │   • NP level OK?       │       │
         │   • Grand level OK?    │       │
         └────────────┬───────────┘       │
                      │                   │
           ┌──────────┴──────────┐        │
           │ Match               │ No     │
           │ found?              │ Match  │
           ▼                     ▼        │
     ┌──────────┐        ┌────────────┐   │
     │  Select  │        │ Scroll     │───┘
     │  Support │        │ Down       │
     └──────────┘        └─────┬──────┘
                               │
                     ┌─────────┴─────────┐
                     │ Bottom            │
                     │ of list?          │
                     ▼                   ▼
              ┌────────────┐      ┌────────────┐
              │ Check "All"│      │ Refresh    │
              │ Tab        │      │ List       │
              └────────────┘      └────────────┘
```

### Image Preloading

FGA loads the support images once at the start of a run. This includes the atlas images for atlas entries. The load happens before FGA opens the support screen, so a load error appears early.

### Append Skill Check

FGA reads each entry under one screen snapshot. It collects the entries that need an append skill check, and then it checks those entries in one pass. It switches the list to the append display once, reads every level, and switches back.

---

## Matching Priority

FGA collects matches in screen order from top to bottom. The first match wins.

- The servant order in your config only decides which servant an entry belongs to.
- When more than one servant can match the same entry, the first servant in your config wins.

### Match Requirements

A support must meet all of these conditions before FGA selects it:

1. **Servant matches** (when you configure servants)
2. **CE matches** (when you configure CEs, or when the CE must not be blank)
3. **Friend matches** (when **Friends Only** is on)
4. **Ascension matches** (when **Max-ascended** is on for that servant)
5. **Skills match** (when you set **Max Skills** for that servant)
6. **Append skills match** (when **Max Appends** is on for that servant)
7. **NP level matches** (when you set a minimum NP level above 1 for that servant)
8. **Grand servant matches** (when you set the Grand option for that servant, JP only)

---

## Tips for Effective Configuration

### For Faster Matching

1. **Use specific class tabs** - A class reduces the search space.
2. **Enable "Also Check All"** - This gives a fallback when the class tab has no match.
3. **Do not over-specify** - Each extra requirement reduces the number of matches.

### For Reliable Matching

1. **Use clear images** - Take atlas entries, or make sharp support images with the Support Image Maker.
2. **Update images after ascension** - Capture a servant again after its artwork changes.
3. **Add multiple servants** - Fallback options prevent a failed selection.
4. **Keep the filters per servant** - Set the filters on each servant, and not on all of them.

### For Events

1. **Look for event CEs** - Many farming supports carry event bonus CEs.
2. **Use the Mix tab** - Event supports often appear in the Mix or Event class tab.
3. **Temporarily disable MLB** - Early in an event, MLB CEs are rare.

---

## Troubleshooting

### FGA does not select a support

- Check the images. Make sure that the servant and CE images are correct.
- Check the class tab. Make sure that you search the correct class.
- Relax the requirements. Turn off **Max-ascended**, **Max Skills**, or the NP level check.
- Check the MLB switch. Turn off the MLB requirement when a support may not have it.
- Check the per-servant filters. Each servant has its own filters.
- Check **Friends Only**. Turn it off when you do not need friends only.

### Script stops with "SupportSelectionPreferredNotSet"

- Add at least one enabled servant, or configure one default Craft Essence.
- Friend names alone do not start a search.

### Script keeps refreshing the list

- FGA found no matching support.
- Add more servant or CE options.
- Check whether your requirements are too strict.

### Wrong support selected

- Your images can match more than one servant.
- Capture more specific images.
- Add extra filter requirements.
- Raise the matching threshold.

### The atlas list has no servant or CE

- Download the atlas data snapshot first.
- Check the search text and the filter chips.
- Reload the atlas data from the app settings.

### Grand Servant features do not appear

- Grand Servant is a JP server feature.
- Make sure that your Battle Config uses the JP server.

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - Overall battle automation
- [Support Image Maker](../other-scripts/support-image-maker.md) - Create support images
- [Preferred Servant](../support-screen/preferred-servant.md) - Servant filters in detail
- [Preferred CE](../support-screen/preferred-ce.md) - Craft Essence filters in detail
- [Preferred Friend](../support-screen/preferred-friend.md) - Friend filters in detail
- [Grand Servant](../support-screen/grand-servant.md) - Grand Servant detection and handling
