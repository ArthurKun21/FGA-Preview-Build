---
title: Automatic Screen Detection
description: How FGA automatically recognizes and handles different game screens during battle automation.
tags:
    - battle
    - screens
    - detection
    - automation
---

# Automatic Screen Detection

FGA continuously monitors the game to recognize screens and take appropriate actions.

## Overview

The Battle Script uses pattern recognition to identify which screen FGO is currently showing. Every 0.5 seconds, FGA checks the screen against known patterns and handles each situation automatically, allowing seamless automation through complex quest sequences.

## How Screen Detection Works

```text
┌─────────────────────────────────────────┐
│         Continuous Loop                 │
│         (every 0.5 seconds)             │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Capture Current Screen               │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Check Against Known Patterns         │
│    • Menu icons                         │
│    • Button locations                   │
│    • Screen-specific indicators         │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Execute Appropriate Action           │
└─────────────────────┬───────────────────┘
                      │
                      ▼
                 Repeat Loop
```

## Detected Screens

### Quest Flow Screens

These screens appear during normal quest progression.

| Screen                       | How FGA Recognizes It      | Action Taken                    |
| ---------------------------- | -------------------------- | ------------------------------- |
| **Menu/Quest Selection**     | Menu icon visible          | Click quest, handle AP refill   |
| **Support Selection**        | Support screen indicator   | Select configured support       |
| **Party Selection**          | Party dots visible         | Select configured party         |
| **Boost Item Selection**     | Boost item buttons visible | Select configured boost or skip |
| **Quest Start Confirmation** | Cancel button visible      | Click start                     |

### Battle Screens

These screens appear during combat.

| Screen              | How FGA Recognizes It      | Action Taken                      |
| ------------------- | -------------------------- | --------------------------------- |
| **Battle Idle**     | Attack button ready        | Execute skills, then select cards |
| **Skill Animation** | Skill effects playing      | Wait for completion               |
| **Card Selection**  | Command cards visible      | Pick cards based on priority      |
| **NP Animation**    | NP starting (BetterFGO)    | Tap to skip                       |
| **Between Waves**   | Black screen during battle | Wait for next wave                |

### Result Screens

These screens appear after completing a quest.

| Screen                      | How FGA Recognizes It  | Action Taken                           |
| --------------------------- | ---------------------- | -------------------------------------- |
| **Bond Point Distribution** | Bond icon visible      | Screenshot (if enabled), click through |
| **Bond Level Up**           | Bond level indicator   | Screenshot, check target level         |
| **Master EXP**              | Master exp visible     | Click through                          |
| **Material Drops**          | Material rewards icon  | Track materials, screenshot            |
| **Quest Rewards**           | Quest reward indicator | Handle first clear rewards             |
| **Master Level Up**         | Level up animation     | Click through                          |
| **CE Reward Details**       | CE details screen      | Screenshot CE, close                   |

### Special Screens

These screens require specific handling.

| Screen                  | How FGA Recognizes It    | Action Taken                       |
| ----------------------- | ------------------------ | ---------------------------------- |
| **Friend Request**      | Friend request indicator | Accept or reject based on settings |
| **Story Dialog**        | Skip button visible      | Skip (if story skip enabled)       |
| **Popup/Info Windows**  | Close button visible     | Close automatically                |
| **Quest Repeat**        | Repeat button visible    | Continue to next run               |
| **Connection Issues**   | Retry button visible     | Retry automatically                |
| **Withdrawal Dialog**   | Withdraw button visible  | Handle based on settings           |
| **Rank Up Animation**   | Rank up indicator        | Click through                      |
| **Command Code Reward** | Command code screen      | Click through                      |
| **Daily Login**         | Login screen             | Handle login                       |

## Detection Priority

FGA checks screens in a specific order to ensure correct handling.

```text
Priority Order (highest to lowest):

1. Connection retry needed
2. Battle idle (execute turn)
3. Menu screen
4. NP animation starting (BetterFGO)
5. Bond level screen
6. Result screens
7. Material drops screen
8. Quest reward screen
9. Support selection
10. Quest repeat screen
11. Withdrawal needed
12. Story skip needed
13. Popup screens
14. Friend request screen
15. Command code rewards
16. Bond 10 CE rewards
17. CE reward details
18. Death animation
19. Rank up animation
20. Interlude end screen
21. Tips screen
```

## Handling Unexpected Situations

### Connection Issues

When network problems occur, FGA detects retry prompts and handles them automatically:

```text
┌─────────────────────────────────────────┐
│    Connection Error Detected            │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Click Retry Button                   │
└─────────────────────┬───────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────┐
│    Wait for Reconnection                │
└─────────────────────┬───────────────────┘
                      │
                      ▼
              Resume Normal Operation
```

### Story Dialogs

When story skip is enabled, FGA handles story elements:

1. Detects skip button on screen
2. Clicks skip button
3. Confirms skip in dialog
4. Continues to battle

### Popup Windows

Various popups (tips, warnings, info) are closed automatically by detecting and clicking the close button.

## Tips for Best Results

### Ensure Clean Detection

- **Avoid overlay apps** that might interfere with screen recognition
- **Keep game at standard resolution** for consistent pattern matching
- **Don't manually interact** while automation is running
- **Allow animations to complete** before expecting detection

### When Detection Fails

If FGA seems stuck on a screen:

1. Check if the screen is unusual or new (game updates can add screens)
2. Verify no other apps are overlaying FGO
3. Try restarting both FGA and FGO
4. Check that FGA has screen capture permissions

### Screen Timing

Some screens require specific timing:

- **Bond screens**: May need extra time to fully render before screenshot
- **Drop screens**: Material detection happens before clicking through
- **Support selection**: Scrolling and refreshing has built-in delays

## Troubleshooting

### Script Seems Stuck

**Problem**: The script isn't progressing despite the game showing an actionable screen.

**Possible Causes**:

- Screen isn't matching known patterns (check for game updates)
- Overlay app interfering with detection
- Permission issues with screen capture

**Solutions**:

1. Restart FGA and FGO
2. Check for app updates
3. Verify screen capture permissions
4. Check if any floating apps are active

### Clicking Wrong Location

**Problem**: FGA clicks somewhere but not where expected.

**Possible Causes**:

- Screen resolution mismatch
- Game window offset
- Navigation bar overlapping

**Solutions**:

1. Verify FGO is running in compatible resolution
2. Check navigation bar settings
3. Ensure no system elements overlap the game area

### Missing Screenshots

**Problem**: Bond or drop screenshots aren't being captured.

**Possible Causes**:

- Screen detected but screenshot timing off
- Storage permissions missing
- Screenshot setting disabled

**Solutions**:

1. Enable screenshot options in settings
2. Verify storage permissions
3. Check screenshot folder for existing captures
