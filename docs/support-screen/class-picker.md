---
title: Support Class Selection
description: Configure FGA Preview to search specific class tabs on the support screen for faster and more targeted servant selection.
tags:
    - support
    - class
    - selection
    - configuration
---

# Support Class Selection

Configure which servant class tab FGA searches when looking for support servants. Selecting a specific class reduces search time and targets your desired servant type.

## Overview

The support screen in FGO displays servants organized by class tabs. FGA can automatically navigate to a specific class tab before searching, making support selection faster and more targeted.

## Key Features

- **Class tab navigation**: Automatically select a specific class tab
- **Also Check All option**: Fallback to the All tab if no match is found
- **Mix/Event tab support**: Target event-specific servant lineups
- **Speed optimization**: Reduce search time by narrowing scope

---

## Available Class Options

| Class         | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| **None**      | Don't navigate, search current tab                              |
| **All**       | Navigate to the "All" tab                                       |
| **Saber**     | Navigate to Saber class tab                                     |
| **Archer**    | Navigate to Archer class tab                                    |
| **Lancer**    | Navigate to Lancer class tab                                    |
| **Rider**     | Navigate to Rider class tab                                     |
| **Caster**    | Navigate to Caster class tab                                    |
| **Assassin**  | Navigate to Assassin class tab                                  |
| **Berserker** | Navigate to Berserker class tab                                 |
| **Extra**     | Navigate to Extra class tab (Ruler, Avenger, Moon Cancer, etc.) |
| **Mix**       | Navigate to the Mix/Event tab                                   |

### Selecting a Class

1. Open your Battle Config
2. Navigate to **Support Selection** → **Preferred Support**
3. Select your desired class from the **Support Class** dropdown

---

## Also Check All Option

When enabled, FGA will also search the "All" tab if no match is found in the selected class tab.

### How Also Check All Works

```text
┌─────────────────────────────┐
│ Search Selected Class Tab   │
└─────────────┬───────────────┘
              │
              ▼
      ┌───────┴───────┐
      │ Match Found?  │
      ▼               ▼
   ┌──────┐       ┌──────┐
   │ Yes  │       │ No   │
   └──┬───┘       └──┬───┘
      │              │
      ▼              ▼
┌──────────┐   ┌──────────────┐
│ Select   │   │ Also Check   │
│ Support  │   │ All enabled? │
└──────────┘   └──────┬───────┘
                      │
              ┌───────┴───────┐
              ▼               ▼
         ┌──────┐       ┌──────────┐
         │ Yes  │       │ No       │
         └──┬───┘       └────┬─────┘
            │                │
            ▼                ▼
    ┌───────────────┐  ┌────────────┐
    │ Switch to All │  │ Refresh    │
    │ Tab & Search  │  │ List       │
    └───────────────┘  └────────────┘
```

### When Also Check All is Available

The "Also Check All" option is only available for certain class selections:

| Class                   | Also Check All |
| ----------------------- | -------------- |
| **None**                | Not available  |
| **All**                 | Not available  |
| **Mix**                 | Not available  |
| **Saber through Extra** | Available      |

The option doesn't appear for None, All, or Mix because:

- **None**: No class tab is selected
- **All**: Already searching all classes
- **Mix**: Event tab is separate from class structure

---

## Class Selection Strategies

### Single Class Targeting

Best when you know exactly which class servant you need:

```text
Support Class: Caster
Also Check All: Disabled
```

Use cases:

- Farming with a specific Caster DPS
- Events requiring specific class servants
- Consistent farming setups

### Class with All Fallback

Provides flexibility while still prioritizing a specific class:

```text
Support Class: Berserker
Also Check All: Enabled
```

Use cases:

- Prefer Berserker supports but accept alternatives
- When friend list may have your servant in different slots
- Balancing speed with availability

### No Class Filter

Searches whatever tab is currently displayed:

```text
Support Class: None
Also Check All: Not applicable
```

Use cases:

- Very specific servant that could be in any class
- When you'll manually navigate before starting
- Simple setups without class preference

### All Classes Search

Comprehensive search across all servants:

```text
Support Class: All
Also Check All: Not applicable
```

Use cases:

- Looking for rare event CEs across all classes
- Support setup is more important than class
- Maximum flexibility needed

### Event/Mix Tab

Targets the special event support tab:

```text
Support Class: Mix
Also Check All: Not applicable
```

Use cases:

- Event farming requiring event supports
- Special campaign supports
- Event CE hunting

---

## Tips for Best Results

### Speed Optimization

- Selecting a specific class is faster than searching "All"
- Use "Also Check All" only when needed
- Narrow your search to reduce scroll and refresh cycles

### Event Farming

- Check the Mix tab for event-specific support setups
- Event supports may appear in the Mix tab first
- Update class selection as events change

### Consistent Setups

- If you always use the same class, set it in your config
- Create multiple configs for different class needs
- Use descriptive config names (e.g., "Caster Farming")

### Friend Coordination

- Ask friends to put servants in expected class slots
- Coordinate event CE placement with class slots
- Check which classes your friends typically populate

---

## Troubleshooting

### Wrong class tab selected

- Verify your Support Class setting in the config
- Check that the game is on the support selection screen
- The script navigates to your selected class after the screen loads

### Also Check All not working

- Only available for specific class selections
- Not available for None, All, or Mix
- Verify the option is actually enabled

### Mix tab not appearing

- Mix/Event tab may not exist during non-event periods
- Some servers may have different tab configurations
- Check the current FGO event schedule

### Class selection taking too long

- Class tab navigation adds a small delay
- This is normal and ensures reliable tab selection
- The delay is minimal (about 0.5 seconds)

### Support in wrong tab

- Friends may place servants in unexpected tabs
- Use "Also Check All" for more flexible matching
- Consider using "All" class if placement is inconsistent

---

## Related Documentation

- [Selection Modes](selection-modes.md) - Overview of selection modes
- [Support Refresh](refresh.md) - Refresh and scroll behavior
- [Preferred Servant Selection](preferred-servant.md) - Configure servant matching
