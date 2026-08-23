---
title: Battle Configs Migration
description: Guide to the new changes due to the Battle Configs migration to proto datastore
tags:
    - battle configs
    - Preferred Support
    - Script Command Config
    - Command Card Config
    - Skill Maker
---

# Battle Configs Migration

## Overview

We have performed an overhaul of the Battle Config system of the app. This transforms from a key-pair system using Android's shared preferences into a nested class similar to a JSON using protobuf. This also helps us when we transition to having a desktop app for a unified data experience.

## Changes

### Scripts

- We have now modified to enable the user to add multiple scripts at the same Battle Config while at the same time allowing users to add `name` and `notes` on what does specific script do.
- Just like before, there can only be one active script at a time.

### Command Cards

- Like Scripts, command card there can be multiple command card preset to allow users to configure different command card configuration.
- `Use Servant Priority` is now standalone and no more need for `enable servant priority`
- `Use Critical Stars Priority` have been changed from overall command card setting into normal per turn setting just like the new `Use Servant Priority`

### Farming

- Users can now select multiple servers to enable to make the config appear on different server but the server would more options would take priority when updating the UI (e.g. Grand Servants with JP server)
- Materials, you can now individually add count per material as well as their default count when it rans out.

### Support

- Servants have now can take distinct options per servant. For example, Castoria can take skills 10/10/10 while Tamamo can take skills 10/X/10 only.
- We have also added option to customized the CE and friend option per servant too.

> [!Note]
>
> Still thinking of creating a feature when a certain servant was selected it would switch the script and command card configuration but this is still an idea.

## End Notes

- The app still support the importing of the old JSON configuration.
- The default export for configs are now using `.pb` extension.
- The last app version that still uses shared preferences is `pre-2614`.