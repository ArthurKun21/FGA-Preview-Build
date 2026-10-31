---
title: Command Card Priority
description: Create command card rules and configure card, servant, chain, and custom card priorities for each wave and turn in FGA Preview.
tags:
  - battle
  - cards
  - NP
  - configuration
---

# Command Card Priority

Configure command card rules used by FGA during battle. Each rule contains its own wave and
turn settings, so you can save different strategies and choose which rule is active for a
battle config.

## Overview

The Command Card screen opens on the rule list. A rule contains card priorities, servant
priorities, brave-chain behavior, chain priorities, and other options for each wave and
turn. Rules belong to the current battle config.

Compared with `pre-2614`, a config can now have multiple named command-card rules instead
of one priority setup. Critical-star and servant-priority switches moved from config-wide
settings to individual wave/turn entries. The old **With NP Mighty** brave-chain option was
replaced by **Always**. Chain-type priorities, exact custom-card choices, and the hand
simulator are also available in the current editor.

## How to Access

1. Open a **Battle Config** from the main app
2. Tap **Command Card** to open the command card rule list

---

## Command Card Rules

The rule list can contain multiple named rules. Tap a rule to edit it; use its **Active**
selector to choose which rule the battle config uses. The active rule and the rule currently
open for editing are separate, so you can edit another rule without activating it.

- Tap **Add** to create a rule. New rules start with one wave and one turn.
- Tap a rule name to edit its name, notes, and settings.
- Use the rule navigation arrows to move between rules while editing.
- Delete a rule from its list item. At least one rule must remain.

Each rule can skip servant face-card checks independently. Open **Settings** from a rule's
detail screen to change this option or edit its notes.

## Wave and Turn Settings

Rules have up to three waves. Add waves with the floating toolbar and remove them by
deleting their entry. Each wave has one or more turns; add a turn to give that wave another
command-card setup. Select an entry to edit its settings. Removing the only turn in a wave
removes that wave; at least one wave and one turn per wave are retained.

Most command-card options are saved per wave and turn. This lets one turn use a different
card order, servant order, or chain strategy from the next.

### Turn options

| Option | What it controls |
|--------|------------------|
| **Use Custom Cards** | Enables matching against your saved custom three-card choices for this turn. |
| **Command Card** | Opens the face-card priority editor. Drag cards to set their order. |
| **Use Critical Star Priority** | Includes critical versions of eligible weak and normal cards in the priority list. |
| **Use Servant Priority** | Applies this turn's servant order when ranking cards. |
| **Brave Chains** | Chooses how the automation handles brave chains for this turn. |
| **Use Chain Priority** | Enables the chain-order rules below. |
| **Chain Priority** | Sets the order of chain types to try and which types are hidden. |
| **Rearrange Cards** | Enables the card rearrangement behavior for this turn. |
| **Simulation** | Lets you set up a sample hand and attack sequence, then inspect FGA's pick, ranked alternatives, and a step-by-step decision trace. |

### Face-card and servant priority

Face-card order and servant order are edited on separate screens. Drag items to reorder
them. Servant order is used only when **Use Servant Priority** is enabled for that turn;
otherwise face-card priority determines the order.

Critical-star priority and servant priority were config-wide switches in `pre-2614`. They
are now separate settings for each wave and turn. When migrating an old config, its former
global values are copied to every turn, so the initial behavior is preserved; you can then
customize individual turns.

## Chain Priority

Chain priority controls how FGA reorders face cards after it has ranked them by card or
servant priority. It is configured separately for each wave/turn.

1. Enable **Use Chain Priority** on the wave/turn entry.
2. Open **Chain Priority**.
3. Drag visible chain types into the order FGA should try them.
4. Hide a type to remove it from the active order. Hidden types can be shown again.

FGA tries the configured types from top to bottom and uses the first valid chain it can
form. The default active order is **Mighty**, **Buster**, **Arts**, **Quick**; **Avoid** is
available but hidden by default. If no configured chain can be formed, FGA applies any
remaining brave-chain preference; if that also cannot be satisfied, the card/servant
priority order remains in effect.

| Chain type | Meaning |
|------------|---------|
| **Mighty** | Try to use three different card types (Buster, Arts, and Quick). |
| **Buster**, **Arts**, **Quick** | Try to use a chain of three cards of that type. NP types can contribute when the attack sequence uses an NP. |
| **Avoid** | Try to avoid both same-type chains and brave chains. This can be impossible for some hands. |

### Brave-chain behavior

A brave chain is three cards from the same servant. The **Brave Chains** setting applies
to the same wave/turn:

| Setting | Behavior |
|---------|----------|
| **Don't care** | No brave-chain preference; apply the other priorities. |
| **With NP** | Try to form a brave chain around a selected NP when available. |
| **Always** | Prefer a brave chain whenever the available cards can form one, with or without an NP. When possible, prefer a brave Mighty chain. |
| **Avoid** | Try to avoid selecting three cards from the same servant. |

**Always** requires **Use Chain Priority**. In `pre-2614`, the corresponding setting was
**With NP Mighty**; the current **Always** setting can also seek a brave chain without an NP.

When chain priority is off, the older brave-chain selection path is used; the ordered chain
list does not apply. When **With NP** or **Always** can force a brave chain, that preference
is considered by chain selection. Chain priority does not override a matching custom-card
choice, which is checked first.

## Custom Card Priority

Custom card priority lets you define ordered three-face-card patterns for a specific
wave/turn. A matching pattern controls the click order and bypasses the ordinary
card/servant sorting, chain selection, and rearrangement steps.

### Add a custom choice

1. Enable **Use Custom Cards** on the wave/turn entry.
2. Open **Custom Cards** and tap **Add**.
3. Select exactly three face cards. For each, choose Buster, Arts, or Quick for the servant
   position shown in the selector. The same card pattern can be used more than once only
   when the hand contains distinct matching cards.
4. Tap **Done** when all three positions are filled.
5. Add other choices as needed, then drag them to set match order.

Each choice matches card type and servant position; affinity and critical percentage are
not part of the custom pattern. Choices are tested from top to bottom, and the first full
match wins. If none fully match the current hand, FGA falls back to normal priority
handling.

The selector currently disables its NP choices, so custom patterns can be made from face
cards only. Also, the rule-level **Skip Servant Face Card Checks** setting prevents custom
matching because the automation has no face-card identities to compare.

---

## Face-Card Priority

The face-card priority list orders Buster, Arts, and Quick cards by affinity and critical
status. Drag cards to set their order; items nearer the top rank higher.

### Card Types

| Abbreviation | Meaning |
|--------------|---------|
| **B** | Buster card |
| **A** | Arts card |
| **Q** | Quick card |

### Card Affinities

| First letter | Meaning |
|--------|---------|
| **W** | Weak (class advantage - more damage) |
| **N** | Normal (neutral damage) |
| **R** | Resist (class disadvantage - less damage) |

### Critical Modifier

| Last letter | Meaning |
|--------|---------|
| **C** | Critical-card variant |
| **N** | Non-critical variant |

### Examples

| Code | Full Name |
|------|-----------|
| **WBC** | Weak Buster critical |
| **WBN** | Weak Buster non-critical |
| **NBC** | Normal Buster critical |
| **NBN** | Normal Buster non-critical |
| **RAN** | Resist Arts (critical status does not change resist cards) |

### Default Priority

With **Use Critical Star Priority** off, the default order is:

```text
WBN, WAN, WQN, NBN, NAN, NQN, RBN, RAN, RQN
```

With the option on, critical variants of weak and normal cards are inserted before their
non-critical variants:

```text
WBC, WBN, WAC, WAN, WQC, WQN, NBC, NBN, NAC, NAN, NQC, NQN, RBN, RAN, RQN
```

Cards closer to the beginning are ranked higher. Resist cards have no separate critical
variant.

### Reordering Cards

1. Open a wave/turn entry and tap **Command Card**
2. Drag cards up or down using the handle icon
3. Higher position = higher priority

---

## Servant Priority

When **Use Servant Priority** is enabled for a wave/turn, configure which servant's cards
are selected first for that entry. Each entry has its own servant order.

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
Example for one wave/turn: Servant Priority = [3, 1, 2]
         Face-card order: Buster > Arts > Quick

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

1. Open a wave/turn entry and tap **Servant**
2. Drag servants up or down using the handle icon
3. Servants at the top have their cards selected first

---

## Rearrange Cards

When enabled, the automation may reorder selected cards to improve the attack sequence,
including NP ordering and the third-card bonus.

### How Rearrange Cards Works

Rearrangement works with the brave-chain behavior and face-card priorities for that turn.
Use **Simulation** on the entry to set up a sample hand, edit card and NP details, and
inspect FGA's pick, ranked alternatives, and the decision trace.

---

## Card Selection Simulation

Open **Simulation** from a wave/turn entry to see how the current settings handle a sample
hand. The simulation uses the same card-selection pipeline as battle automation.

### Set up the sample hand

- The sample starts with five command cards and three NP cards. Tap a command card to edit
  its type, affinity, servant slot, critical status and percentage, or stunned state.
- Toggle an NP to include or remove it from this simulated attack. Tap an NP to edit its
  card type, affinity, or stunned state.
- Drag the **Attack Sequence** to move enabled NPs among the three attack slots. Card slots
  are filled from the configured face-card priority.
- Use **Reset** in the top bar to restore the sample hand and default attack sequence.

The hand is temporary and is not saved to the battle config. It is shared while moving
between wave/turn entries in the open command-card editor and is reset when the simulation
is reset or the editor is closed.

### Read the results

The screen shows FGA's actual pick, all simulated candidate picks ranked best to worst,
and a **How FGA decided** trace:

1. **Custom card priority** shows whether a custom choice matched, why matching was skipped,
   or which requested cards failed to match. A successful match bypasses the later stages.
2. **Face-card priority** shows the cards ordered by servant priority (when enabled) and
   card priority, including the critical-percentage tie-break.
3. **Chain reorder** shows the chain or brave-chain behavior and any rearrangement applied.
4. **Take** shows how many face cards fill the non-NP positions in the attack sequence.
5. **Final click sequence** shows the NPs and selected face cards in the order FGA would
   click them.

The pick marked as FGA's pick is the live pipeline's answer for that sample. The ranked
list compares other possible three-card picks under the simulator's ranking. If a custom
choice matches, its configured card order determines that pick.

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

1. **Match priorities to your team**: If your main damage dealer uses Buster cards, prioritize Buster within each turn.
2. **Consider class advantage**: Weak-affinity cards generally deal more damage; rank them accordingly.
3. **Use servant priority for focused damage**: Set your main DPS servant first on turns where servant priority is enabled.
4. **Tune critical-star priority by turn**: Enable it only for turns where critical cards matter to your strategy.
5. **Use named rules for alternate plans**: Keep separate rules for different parties or quests and activate the one you need.

---

## Troubleshooting

### Cards aren't being selected in my expected order

- Confirm the intended rule is marked **Active** in the rule list.
- Check that the edited wave/turn is the one used by the battle.
- Check whether **Use Servant Priority**, **Use Critical Star Priority**, or **Use Chain Priority** is enabled if the expected order depends on it.
- Custom-card choices take precedence when one fully matches. If none match, normal priority handling is used.

### Brave chains aren't forming

- Check the selected brave-chain option for that wave/turn.
- **With NP** needs an NP to be selected; **Always** needs **Use Chain Priority** enabled for its full behavior.
- Brave chains depend on the available cards and NPs, so an option is a preference, not a guarantee.

### The app is picking a card I expected to be lower priority

- Check the full three-letter card code and its position in the face-card editor.
- Resist cards remain in the completed priority list; move them to the bottom instead of trying to remove them.

### Support servant aren't being prioritized

- If you put too many buffs on the support servant, you may encounter the [super-buff bug](https://github.com/Fate-Grand-Automata/FGA/issues/1076). Consider turning on the `Treat support servants like your own` option in Global Battle Settings (`Settings` -> `Battle` -> `Treat support servants like your own`).

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - Overall battle automation
- [Script Maker](script-maker.md) - Configure skill execution during battle
- [Global Battle Settings](../app/global-battle.md#treat-support-servants-like-your-own) - Treat support servants like your own option
