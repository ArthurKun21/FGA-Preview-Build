---
title: GitHub Backup
description: Store FGA Preview battle configs in a GitHub repository. Configure the account, repository, and access token, then review and apply sync changes.
tags:
    - app
    - settings
    - github
    - backup
    - sync
---

# GitHub Backup

## Overview

GitHub Backup stores your battle configs in a GitHub repository. The configs stay on your device, and the repository holds a copy.

FGA does not send or write data until you start a sync. A sync runs in two steps. First, FGA compares the device with the repository. Second, you pick a resolution for each difference and tap **Apply**.

FGA does not sync in the background. A sync starts only when you open the sync screen and tap a button.

## Key Features

### Configure the backup

Open **Settings**. Tap **GitHub Backup**. Tap **Configure GitHub**.

The configuration pane holds three fields:

| Field            | Contents                                                                                                    |
| ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Account name     | The GitHub user or organization that owns the repository                                                     |
| Repository name  | The repository that holds the backup. Create a repository at github.com/new if you do not have one yet       |
| Access token     | A personal access token with the `repo` scope                                                               |

Tap **Show** to read the token text. Tap **Hide** to mask the token text again.

The token grants access to the repository. FGA stores the token encrypted on the device, and sends the token only in requests to GitHub.

Tap **Save** to store the account name, the repository name, and the token. FGA needs an account name and a repository name before it can save.

### Test the connection

Tap **Test connection** to check the values before the first sync. The result shows below the token field:

| Result | Meaning |
| ------ | ------- |
| Connected as `<login>`. The repository is accessible | The account, the repository, and the token are correct |
| The token was rejected. Check the token and its repo scope | GitHub did not accept the token |
| The repository was not found. Check the account and repository names, or create the repository at github.com/new | FGA did not find the repository. The account name or the repository name is wrong |
| Could not reach GitHub. Check your connection and try again | The device cannot reach GitHub |

### Read the GitHub Backup section

The GitHub Backup section shows four rows:

| Row | Contents |
| --- | -------- |
| Account | The configured account name, or "Not configured" |
| Repository | The configured repository name, or "Not configured" |
| Last sync | The time of the last sync, or "Never" |
| Sync battle configs | Opens the sync screen |

The **Last sync** row uses the date and time formats from the Appearance section.

The **Sync battle configs** row is disabled until you configure the backup.

### Sync battle configs

Tap **Sync battle configs** to open the sync screen. The screen holds two buttons and the diff list.

Tap **Check for changes** to compare the device with the backup repository. The button shows "Checking…" while FGA reads the repository.

The diff list groups each config by its state:

| State | Group header | Resolutions |
| ----- | ------------ | ----------- |
| The config exists only on the device | Only on this device | Upload, Delete local, Ignore |
| The config exists only in the backup | Only in the backup | Download, Delete backup, Ignore |
| The config changed on the device and in the backup | Changed on both sides — pick a version | Keep local, Keep backup, Delete local, Delete backup, Ignore |

The list also shows the number of configs that are already up to date.

Tap a resolution chip to select it. Tap the chip again to clear the selection. FGA enables the **Apply** button only when every changed config has a resolution. If a changed config has no resolution, the screen shows "Resolve every changed config to apply."

Tap **Apply** to run the sync. A notification shows the progress while the sync runs.

Each config row shows the status of the last apply:

| Status | Meaning |
| ------ | ------- |
| Pending | The apply did not reach this config yet |
| Syncing | FGA processes this config now |
| Synced | The apply finished for this config |
| Failed | The apply failed for this config. The row shows the reason |

## Tips for Best Results

- Tap **Check for changes** before every apply. The diff then shows the current state of the backup.
- Use a private repository. The battle configs are your own data.
- Use **Ignore** for configs that you want to skip in one apply. The config stays out of the sync.
- Keep a local backup file in Storage Settings as well. A backup file restores the settings on a new device without a network.

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| GitHub Backup is not configured yet. | Open **Configure GitHub**. Enter the account name, the repository name, and the access token. Tap **Save**. |
| The access token was rejected. Check the token and its repo scope. | Create a new personal access token with the `repo` scope. Enter the token. Tap **Save**. |
| The backup repository was not found. | Check the account name and the repository name. Create the repository at github.com/new if it does not exist. |
| The backup changed while syncing. Check for changes and resolve again. | Another device wrote to the repository during the apply. Tap **Check for changes** and resolve the diff again. |
| GitHub API rate limit reached. Try again later. | Wait a few minutes. Then tap **Check for changes** again. |
| Could not reach GitHub. Check your connection and try again. | Check the network connection of the device. Then tap **Check for changes** again. |
| The **Apply** button stays disabled | A config in "Changed on both sides" has no resolution. Select a resolution for every changed config. |

## Related Documentation

- [Settings](settings.md)
- [Storage Settings](storage.md)
