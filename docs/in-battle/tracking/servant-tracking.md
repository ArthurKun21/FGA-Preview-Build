---
title: Servant Tracking During Battle
description: How FGA tracks servants on the battlefield. Understand servant detection, face card matching, and order change handling.
tags:
    - battle
    - servants
    - tracking
    - cards
---

# Servant Tracking During Battle

Understand how FGA identifies and tracks servants throughout battle.

## Overview

FGA maintains a mapping of which servants are on the field and in which positions. This enables accurate face card attribution, support servant identification, and proper handling of servant swaps and deaths.

## Key Features

- **Position Tracking**: Know which servant is in each field slot
- **Face Card Matching**: Attribute command cards to correct servants
- **Support Detection**: Identify the friend's support servant
- **Order Change Handling**: Track servant swaps accurately
- **Death/Replacement**: Update tracking when servants die

## How Servant Tracking Works

```text
┌─────────────────────────────────────────┐
│        Battle Start                     │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Initialize Field Positions           │
│    Slots 1-3 = Team positions 1-3       │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Capture Servant Identification       │
│    • Skill icons                        │
│    • Face card images                   │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Each Turn: Verify Positions          │
│    Check if servants match expectations │
└─────────────────────────────────────────┘
```

## Field Slots and Team Slots

### Field Slots

Active positions during battle:

| Slot | Position | Description           |
| ---- | -------- | --------------------- |
| A    | Left     | First field position  |
| B    | Center   | Second field position |
| C    | Right    | Third field position  |

### Team Slots

All servants in your party:

| Slot | Position | Field Status        |
| ---- | -------- | ------------------- |
| 1    | First    | Starts on field (A) |
| 2    | Second   | Starts on field (B) |
| 3    | Third    | Starts on field (C) |
| 4    | Fourth   | Backup              |
| 5    | Fifth    | Backup              |
| 6    | Sixth    | Backup              |

## Servant Identification

### Skill Icon Detection

FGA captures skill icons to identify servants:

```text
┌─────────────────────────────────────────┐
│  Field Slot A                           │
│  ┌───┬───┬───┐                          │
│  │S1 │S2 │S3 │  ← Skill icons captured  │
│  └───┴───┴───┘                          │
└─────────────────────────────────────────┘
```

### Face Card Detection

Matches command cards to servants:

```text
Command Cards:
[Card 1] [Card 2] [Card 3] [Card 4] [Card 5]

FGA compares card faces to captured images
to determine which servant owns each card.
```

## Support Servant Handling

### Support Detection

FGA identifies the support servant by the support icon:

- Checks each field slot for support indicator
- Marks that slot as the support position
- Can treat support like own servant if configured

### Support Face Cards

By default, support cards may be handled differently:

| Setting      | Behavior                    |
| ------------ | --------------------------- |
| Treat as own | Include in servant priority |
| Separate     | May be deprioritized        |

## Order Change Tracking

When servants are swapped using Order Change skill:

```text
Before Swap:
Field: [A: Servant 1] [B: Servant 2] [C: Servant 3]
Backup: [Servant 4] [Servant 5] [Servant 6]

Order Change: Swap B with position 1 backup

After Swap:
Field: [A: Servant 1] [B: Servant 4] [C: Servant 3]
Backup: [Servant 2] [Servant 5] [Servant 6]
```

FGA updates its internal mapping to reflect the swap.

## Servant Death and Replacement

When a servant dies:

```text
┌─────────────────────────────────────────┐
│    Servant Death Detected               │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Wait for Replacement                 │
│    (from backup)                        │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Re-identify Servant in Slot          │
│    Update tracking map                  │
└─────────────────────────────────────────┘
```

## Special Cases

### Mélusine Ascension Change

Mélusine can change her appearance mid-battle:

- Her skill icons and face cards change
- FGA detects this and recaptures images
- Tracking continues accurately

### Transform Skills

Servants with transformation skills:

- Jekyll/Hyde transformations
- Ascension-changing skills
- FGA may need to recapture face cards

## Face Card Grouping

FGA groups cards by servant for features like:

- **Servant Priority**: Pick cards from preferred servants first
- **Brave Chains**: Form chains with same-servant cards
- **Avoid Chains**: Spread cards across servants

### Grouping Process

```text
Available Cards:
[Buster-A] [Arts-B] [Quick-A] [Buster-C] [Arts-A]

Grouped by Servant:
Servant A: [Buster] [Quick] [Arts]
Servant B: [Arts]
Servant C: [Buster]
```

## Skip Face Card Checking

When enabled, FGA skips detailed face card attribution:

| Setting  | Behavior                      |
| -------- | ----------------------------- |
| Enabled  | Cards not matched to servants |
| Disabled | Full servant attribution      |

Use when:

- Servant priority is not needed
- Performance is more important
- Simple card priority is sufficient

## Tips for Best Results

1. **Wait for battle to load**: Ensure servants are visible before turn starts
2. **Stable team composition**: Frequent deaths affect tracking accuracy
3. **Clear skill icons**: Ensure skills are visible for capture
4. **Test with your team**: Verify tracking works for your setup
5. **Check servant priority results**: Confirm correct cards are selected

## Troubleshooting

### Cards attributed to wrong servant

- Face card images may be similar
- Try enabling more detailed checking
- Verify servant tracking initialized correctly

### Order Change not tracked

- Ensure the swap completed fully
- FGA updates after skill animation
- Check if skill command syntax is correct

### Support not detected

- Support icon must be visible
- Check if using correct server settings
- Verify support is in expected position

### Tracking fails after death

- Backup servant may look different than expected
- FGA recaptures images automatically
- Allow time for replacement animation

### Mélusine tracking issues

- Ascension change detection may vary
- Ensure FGA version supports this feature
- Check timing of transformation

## Performance Considerations

Servant tracking involves:

- Image capture operations
- Pattern matching for faces
- Memory for stored images

### Optimization Settings

| Setting                 | Impact                       |
| ----------------------- | ---------------------------- |
| Skip face card checking | Faster, less accurate        |
| Parallel card checking  | Trade-off speed vs resources |
| Treat support as own    | Simplifies tracking          |

## Related Documentation

- [Face Card Priority](../card-selection/face-card-priority.md) - Card selection by servant
- [Brave Chains](../card-selection/brave-chains.md) - Chain formation
- [Skill Maker](../../battle-setup/skill-maker.md) - Order change commands
