---
title: CE Drop Detection and Tracking
description: Track Craft Essence drops during FGA farming. Get notifications when CEs drop and set limits to stop farming.
tags:
    - battle
    - drops
    - CE
    - farming
---

# CE Drop Detection and Tracking

Detect and track Craft Essence drops during farming sessions.

## Overview

FGA can detect when Craft Essences drop from quests, notify you immediately, and optionally stop farming when a target number of CEs have dropped. This is especially useful when farming for event CEs or specific drop CEs.

## Key Features

- **Drop Detection**: Identifies CE drops on result screens
- **Star Verification**: Confirms actual CE drops using star icons
- **Immediate Notifications**: Alert when CE drops occur
- **Limit Enforcement**: Stop after collecting target CEs
- **Auto-Decrement**: Reduce remaining limit automatically

## How CE Detection Works

```text
┌─────────────────────────────────────────┐
│        Quest Result Screen              │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Scan for CE Drop Icons               │
│    Search entire visible area           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    For Each Potential CE:               │
│    • Check for CE icon                  │
│    • Verify star pattern nearby         │
│    • Confirm actual CE drop             │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    If CE Confirmed:                     │
│    • Increment counter                  │
│    • Send notification                  │
│    • Check against limit                │
└─────────────────────────────────────────┘
```

## Detection Method

### Two-Stage Verification

FGA uses a two-stage process to avoid false positives:

#### Stage 1: CE Icon Detection

Scans for the Craft Essence drop icon pattern on the result screen.

#### Stage 2: Star Verification

Checks for the star rating indicator near the CE icon:

```text
┌─────────────────┐
│   [CE Icon]     │
│   ★★★★★        │  ← Stars confirm it's a CE
└─────────────────┘
```

This prevents mistaking other items for CE drops.

## Configuration

### Enable CE Tracking

1. Open your Battle Config
2. Find CE Drop settings
3. Enable "Track CE Drops"
4. Optionally set a limit

### CE Limit Settings

| Setting     | Behavior                 |
| ----------- | ------------------------ |
| Disabled    | Track but don't stop     |
| Enabled + 1 | Stop after first CE drop |
| Enabled + N | Stop after N CEs drop    |

## Stop Conditions

### Stop on Any CE

When "Stop on CE" is enabled:

- Any CE drop triggers script stop
- Current run completes first
- Exit summary shows CE count

### Stop at Limit

When limit is configured:

```text
Before Run:
- CE Limit: 5

After Each Drop:
- Count compared to limit
- Continue if count < limit
- Stop if count >= limit
```

## Notifications

When a CE drops, FGA sends a notification:

```text
┌─────────────────────────────────────────┐
│  FGA: CE Dropped!                       │
│  A Craft Essence has dropped.           │
└─────────────────────────────────────────┘
```

This alerts you even if not watching the screen.

## Auto-Decrement

After script completion:

```text
Before Run:
- CE Limit: 10

During Run:
- CEs Dropped: 3

After Run:
- CE Limit: 7 (auto-decremented)
```

When limit reaches 0:

- CE limiting is disabled
- Limit resets to default value
- Tracking continues without stopping

## Exit Summary

View CE statistics after completion:

```text
┌─────────────────────────────────────────┐
│         Battle Exit Summary             │
├─────────────────────────────────────────┤
│ CE Drop Count: 3                        │
│ ...                                     │
└─────────────────────────────────────────┘
```

## Exit Reasons

### Limit CEs

```text
Exit Reason: LimitCEs (Count: 5)

FGA has stopped because the configured
CE drop limit has been reached.
```

### CE Get (Stop on CE)

```text
Exit Reason: CEGet

FGA has stopped because a Craft Essence
dropped and "Stop on CE" is enabled.
```

## Tips for Best Results

1. **Know drop rates**: CE drops are rare, set reasonable limits
2. **Use for event CEs**: Most useful for limited event drops
3. **Enable notifications**: Get alerted even when away
4. **Combine with screenshots**: Keep visual records of drops
5. **Check drop screen timing**: Ensure screen loads fully

## Common CE Farming Scenarios

### Event CE Farming

- Set limit based on desired copies
- Enable notifications for immediate alerts
- Consider MLB requirements (5 copies)

### Story CE Farming

- Rare drops from story quests
- Low limits recommended (1-3)
- May take many runs

### Random Drop CEs

- Very low drop rates
- Use unlimited tracking
- Review exit summaries periodically

## Troubleshooting

### CE drops not detected

- Verify drop screen is fully loaded
- Check if CE icon is visible on screen
- Ensure FGA version supports current CE images
- Screen resolution may affect detection

### False positives (wrong count)

- Star verification should prevent this
- Check if other items look similar
- Report persistent issues

### Notifications not appearing

- Check device notification settings
- Verify FGA notification permissions
- Ensure notifications are enabled in app

### Script not stopping at limit

- Confirm limit is greater than 0
- Check if limiting is enabled
- Verify correct Battle Config is active

### Auto-decrement not working

- Only triggers on successful completion
- Manual stops may not decrement
- Check settings after run

## CE Drops vs Material Drops

| Feature      | CE Drops     | Materials       |
| ------------ | ------------ | --------------- |
| Detection    | Icon + stars | Material images |
| Rarity       | Very rare    | Variable        |
| Notification | Immediate    | Exit summary    |
| Limit type   | Count of CEs | Total materials |

## Related Documentation

- [Auto Battle](../auto-battle.md) - Overall battle automation
- [Materials Tracking](materials-tracking.md) - Track material drops
- [Run Limits](../../app/advanced.md) - Configure limits
