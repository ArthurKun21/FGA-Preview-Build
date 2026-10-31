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

Configure the command card rules that FGA uses during battle. Each rule holds its own wave and
turn settings. Save several strategies, then choose one active rule for the battle config.

## Overview

The Command Card screen opens on the rule list. A rule contains card priorities, servant
priorities, brave-chain behavior, chain priorities, custom card choices, and other options for
each wave and turn. Rules belong to the current battle config.

Compared with `pre-2614`, a config can now hold several named command-card rules instead of one
priority setup. The critical-star and servant-priority switches moved from config-wide settings
to each wave and turn. The old **With NP Mighty** brave-chain option became **Always**.
Chain-type priorities, exact custom-card choices, and the hand simulator are also part of the
current editor.

## How to Access

1. Open a **Battle Config** from the main app
2. Tap **Command Card** in the config summary

---

## Command Card Rules

The rule list shows one card per rule. Rules without a name show as **Command Card Setup N**.

- Tap **Add** in the bottom bar to create a rule. A new rule starts with one wave and one turn.
- Tap a rule card to open the rule for editing. The active rule does not change.
- Tap **Active** on a rule to make that rule the active rule. The editor then edits that rule.
- Tap **Delete** on a rule item to delete it. The list always keeps one rule.
- Tap **Notes** on a rule item to edit the notes of that rule.
- Tap the up or down arrow in the bottom bar to open the previous or next rule. The app also
  makes that rule active.

The **Active** radio button and the **Delete** row show only when the config holds more than one
rule.

Rule items show setting chips and a wave and turn summary.

### Rule name and notes

Open a rule, then tap its name in the top bar to rename it. A dialog opens. Blank names are not
valid.

Tap **Notes** in the rule editor or in the rule settings to open the notes editor. Tap the save
icon to keep the text. Tap the back arrow to close the editor without saving.

### Rule settings

Each rule has a **Settings** screen. Open it with the settings row at the top of the rule
editor.

The screen holds the notes row and the **Skip servant face-card checks** switch. With this
switch on, the automation does not identify the servant on each face card. Servant priority,
brave chains, and custom card priority then have no effect. Card type and affinity priorities
still apply.

## Wave and Turn Settings

A rule can hold up to four waves. The wave and turn entries appear in one list. Each entry
header shows **WAVE N** or **WAVE N TURN M**.

- Tap **Create Wave N** in the bottom bar to add a wave after the focused wave. The new wave
  copies the last turn of the focused wave. The button shows **Wave limit reached** at four
  waves.
- Tap **Create Wave N Turn M** in the bottom bar to add a turn to the focused wave. The new turn
  copies the last turn in that wave.
- Tap the delete icon on an entry header to delete that entry. The icon shows only when the rule
  has more than one wave or the wave has more than one turn.
- Deleting the only turn in a wave deletes the wave. A rule always keeps one wave with one turn.

The app saves most command-card options per wave and turn. One turn can use a different card
order, servant order, or chain strategy from the next.

### Entry options

Each entry shows its options in this order. Most rows show chips with the current setting.

| Option | Kind | What it controls |
|--------|------|------------------|
| **Use Custom Cards Priority** | Switch | Enables matching against the saved custom three-card choices for this turn. |
| **Custom Cards** | Opens a screen | Edits the custom choices and their match order. Needs **Use Custom Cards Priority**. |
| **Card** | Opens a screen | Opens the face-card priority editor for this turn. |
| **Use Crit Stars Priority** | Switch | Adds critical variants of weak and normal cards to the priority list. |
| **Use Servant Priority** | Switch | Applies this turn's servant order when FGA ranks cards. |
| **Servant** | Opens a screen | Edits the servant order. Needs **Use Servant Priority**. |
| **Brave Chains** | Selector | Chooses how the automation handles brave chains for this turn. |
| **Use Chain Priority** | Switch | Enables the chain-order rules below. |
| **Chain Priority** | Opens a screen | Sets the order of chain types to try and which types are hidden. Needs **Use Chain Priority**. |
| **Rearrange Cards** | Switch | Enables the card rearrangement behavior for this turn. |
| **Simulation** | Opens a screen | Opens the card-selection simulator for this turn. |

## Chain Priority

Chain priority controls how FGA reorders face cards after it ranks them by card or servant
priority. Each wave and turn holds its own chain priority.

1. Enable **Use Chain Priority** on the wave and turn entry
2. Open **Chain Priority**
3. Drag the handle on a visible type to set the order. FGA tries the types from top to bottom.
4. Tap the hide icon to hide a type. Hidden types leave the active order. FGA disables the hide
   icon when only one active type remains.
5. Hidden types stay in the **Hidden** section. Tap the show icon to return a type to the end of
   the active order.

FGA tries the active types from top to bottom and uses the first valid chain it can form. The
default active order is **Mighty**, **Buster**, **Arts**, **Quick**. **Avoid** exists but starts
hidden.

If no active type can form a chain, FGA applies the brave-chain preference for the turn. If that
preference also fails, the card and servant priority order stays in effect. A matching
custom-card choice always wins, because FGA checks custom cards first.

| Chain type | Meaning |
|------------|---------|
| **Mighty** | Try to click three cards of three different types (Buster, Arts, and Quick). |
| **Buster**, **Arts**, **Quick** | Try to click three cards of that type. NPs can contribute when the attack sequence uses an NP. |
| **Avoid** | Try to avoid same-type chains and brave chains. Some hands make this impossible. |

### Brave-chain behavior

A brave chain is three cards from one servant. The **Brave Chains** selector belongs to the same
wave and turn:

| Setting | Behavior |
|---------|----------|
| **Don't care** | No brave-chain preference. FGA applies the other priorities. |
| **With NP** | Try to form a brave chain around a selected NP when possible. |
| **Always** | Prefer a brave chain whenever the hand can form one, with or without an NP. Prefer a brave Mighty chain when possible. |
| **Avoid** | Try to avoid picking three cards from one servant. |

**Always** needs **Use Chain Priority**. The selector dims **Always** until you enable that
switch. If you turn **Use Chain Priority** off later, the saved **Always** value falls back to
**With NP**.

When chain priority is off, FGA uses the older brave-chain path. On that path, **Always**
behaves the same as **With NP**. When **With NP** or **Always** can force a brave chain, the
chain handlers accept only chains that are also brave chains.

## Custom Card Priority

Custom card priority lets you define ordered three-card patterns for a wave and turn. A matching
pattern sets the click order and skips the normal card sorting, chain selection, and
rearrangement.

### Add a custom choice

1. Enable **Use Custom Cards Priority** on the wave and turn entry
2. Open **Custom Cards** and tap **Add**
3. Tap cards to fill the three slots at the top. Each servant section offers Buster, Arts, and
   Quick for that servant position.
4. Tap a selected card at the top to deselect it
5. Tap **Done** when the count shows three cards
6. Drag the handle on a choice to set the match order. Tap the delete icon on a choice to delete
   it.

Rules for a choice:

- A position matches card type and servant position. Affinity and critical state are not part of
  the pattern.
- You can pick the same pattern up to three times. The hand must then hold that many matching
  cards.
- The **Done** button needs exactly three cards.
- Choices with fewer than three positions never match. Older saves can hold such choices.

Matching at battle time:

- FGA tests the choices from top to bottom. The first full match wins and sets the click order.
- When several hand cards match one position, FGA prefers the critical card with the higher
  percentage.
- When no choice fully matches, FGA falls back to the normal priority handling.

Limits:

- The selector disables its NP buttons. Choices contain face cards only.
- The rule-level **Skip servant face-card checks** switch prevents custom matching. Without
  servant identities, FGA has nothing to compare.

## Face-Card Priority

The face-card priority list orders Buster, Arts, and Quick cards by affinity and critical state.
Items near the top rank higher. Cards that the list cannot rank keep their original order at the
end.

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
| **RAN** | Resist Arts (critical state does not change resist cards) |

### Default Priority

With **Use Crit Stars Priority** off, the default order is:

```text
WBN, WAN, WQN, NBN, NAN, NQN, RBN, RAN, RQN
```

With the option on, critical variants of weak and normal cards come before their non-critical
variants:

```text
WBC, WBN, WAC, WAN, WQC, WQN, NBC, NBN, NAC, NAN, NQC, NQN, RBN, RAN, RQN
```

Cards near the top rank higher. Resist cards have no separate critical variant.

The editor always shows a complete list. When a saved list misses cards, the app restores them.
Missing cards without a Resist code go before the first Resist card. Missing Resist cards go at
the end.

### Reordering Cards

1. Open a wave and turn entry
2. Tap **Card**
3. Drag the handle on an item, or tap the arrows on the item
4. FGA picks the items at the top first

The badge on each item shows its position. The screen shows **Highest priority** at the top and
**Lowest priority** at the bottom.

---

## Servant Priority

When **Use Servant Priority** is on for a wave and turn, FGA picks cards from the first servants
first. Each entry holds its own servant order. The servant list always shows all six team
positions.

### Team Slots

Each servant has a team position from 1 to 6:

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
Example for one wave and turn: Servant order = 3, 1, 2
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
        [Servant 3 Arts] -> [Servant 3 Quick] -> [Servant 1 Buster] -> ...
```

The critical percentage breaks ties between cards with the same priority code. Cards that the
priority list cannot rank keep their original order at the end.

### Reordering Servants

1. Open a wave and turn entry
2. Tap **Servant**
3. Drag the handle on an item, or tap the arrows on the item
4. Servants at the top give up their cards first

---

## Rearrange Cards

When enabled, the automation may reorder the picked cards to improve the attack sequence. With
one NP and one card before the NP, FGA moves the highest-priority card to the position after the
NP. Otherwise FGA can move the second card to the last position to raise the third-card bonus.

Rearrangement works with the brave-chain behavior and face-card priorities for that turn. Use
**Simulation** to check the effect on a sample hand.

---

## Card Selection Simulation

Open **Simulation** from a wave and turn entry to see how the current settings handle a sample
hand. The simulation uses the same card-selection pipeline as the battle automation.

### Set up the sample hand

- The sample starts with five command cards and three NP cards.
- Tap a command card to edit its type, affinity, servant slot, critical state, critical
  percentage, or stunned state.
- Tap the toggle on an NP to enable or disable it for the simulated attack. Tap an NP to edit
  its enabled state, card type, affinity, or stunned state.
- Drag the **Attack Sequence** items to move enabled NPs between the three attack slots.
  Face-card slots fill from the configured face-card priority.
- Tap **Reset** in the top bar to restore the sample hand and the default attack sequence.

The hand is temporary and is not saved to the battle config. It stays while you move between
wave and turn entries in the open editor. The hand clears when you reset it or close the editor.

### Read the results

The screen shows FGA's pick, all possible picks ranked best to worst, and a **How FGA decided**
trace:

1. **Custom card priority** shows whether a custom choice matched, why FGA skipped matching, or
   which requested cards failed to match. A successful match skips the later stages.
2. **Face-card priority** shows the cards ordered by servant priority, when enabled, and card
   priority. The critical percentage breaks ties.
3. **Chain reorder** shows the chain or brave-chain behavior and any rearrangement.
4. **Take** shows how many face cards fill the non-NP positions in the attack sequence.
5. **Final click sequence** shows the NPs and picked face cards in the order FGA clicks them.

Result rows show a rank number and badges for the chain type, brave chain, and custom selection.
The pick marked as FGA's pick is the live pipeline's answer for that sample. The ranked list
compares the other possible three-card picks under the simulator ranking. The result count
depends on the enabled NPs: 60 candidates with none, 20 with one, 5 with two, and 1 with three.

---

## Per-Wave Strategy Example

Here is an example of how you can configure different waves:

### Wave 1 (Farming weak enemies)

- **Card Priority**: Quick-focused for NP generation
- **Brave Chains**: Don't care
- **Rearrange**: Off

### Wave 2 (Medium enemies)

- **Card Priority**: Arts-focused to charge NP
- **Brave Chains**: Avoid (spread damage)
- **Rearrange**: On

### Wave 3 (Boss wave)

- **Card Priority**: Buster-focused for maximum damage
- **Brave Chains**: With NP (maximize main DPS output)
- **Rearrange**: On

---

## Tips for Effective Configuration

1. **Match priorities to your team**: If your main damage dealer uses Buster cards, put Buster
   cards high in each turn.
2. **Consider class advantage**: Weak-affinity cards generally deal more damage. Rank them
   high.
3. **Use servant priority for focused damage**: Put your main DPS servant first on turns where
   servant priority is on.
4. **Tune crit stars priority by turn**: Enable it only for turns where critical cards matter to
   your strategy.
5. **Use named rules for alternate plans**: Keep separate rules for different parties or quests
   and activate the one you need.

---

## Troubleshooting

### Cards are not picked in my expected order

- Check that the rule you want is the active rule in the rule list.
- Check that you edited the wave and turn that the battle uses.
- Check the **Use Servant Priority**, **Use Crit Stars Priority**, and **Use Chain Priority**
  switches when your expected order depends on them.
- A matching custom-card choice takes precedence. When no choice matches, FGA uses the normal
  priority handling.

### Brave chains are not forming

- Check the **Brave Chains** option for that wave and turn.
- **With NP** needs an NP in the attack sequence. **Always** needs **Use Chain Priority**.
- **Skip servant face-card checks** in the rule settings blocks brave chains.
- Brave chains depend on the available cards and NPs. An option is a preference, not a
  guarantee.

### The app picks a card that I expected lower in the order

- Check the full three-letter card code and its position in the face-card editor.
- Resist cards stay in the completed priority list. Put them at the bottom.

### Support servants are not prioritized

- Check that **Use Servant Priority** is on for that wave and turn.
- **Skip servant face-card checks** in the rule settings blocks servant priority.
- With many buffs on the support servant, you can hit the
  [super-buff bug](https://github.com/Fate-Grand-Automata/FGA/issues/1076). Consider the `Treat
  support servants like your own` option in Global Battle Settings (**Settings** -> **Battle** ->
  **Treat support servants like your own**).

### Custom cards are not used

- Check that **Use Custom Cards Priority** is on for that wave and turn.
- **Skip servant face-card checks** in the rule settings blocks custom matching.
- A choice needs three matching cards in the hand. Affinity and critical state are not part of
  the match.
- Choice positions match card type and servant position only. Check the servant position of each
  card.

---

## Related Documentation

- [Auto Battle](../in-battle/auto-battle.md) - Overall battle automation
- [Script Maker](script-maker.md) - Configure skill execution during battle
- [Global Battle Settings](../app/global-battle.md#treat-support-servants-like-your-own) - Treat support servants like your own option
