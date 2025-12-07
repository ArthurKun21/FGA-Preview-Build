---
title: Storage Settings
description: Configure FGA Preview storage settings. Manage data storage location, extract support images, and create or restore configuration backups.
tags:
    - app
    - settings
    - storage
    - backup
    - support-images
---

# Storage Settings

## Overview

Storage Settings determine where FGA keeps your battle configurations, support images, screenshots, and other data files. You can also extract default support images and create backups of your settings to restore later or move to another device.

## Key Features

### Set the storage folder

Tap **Storage folder** to choose where FGA saves its files. The path displays below the option and can point to internal storage, an SD card, or a cloud-synced folder (though cloud sync may slow down operations).

### Extract default support images

Tap **Extract default support images** to copy the built-in servant and craft essence images to your storage folder. FGA uses these images for support-list recognition. This process runs in the background and shows a notification when finished.

### Create a configuration backup

Tap **Create backup** to export all your battle configurations and app settings into a single JSON file. Store this file in a safe location such as Downloads, Google Drive, or another backup service. Backups make it easy to restore your setup after reinstalling or when migrating to a new device.

### Restore a previous backup

Tap **Restore backup** and select a JSON file previously exported by FGA. The import runs in the background; watch the notification for progress. Each restored configuration appears in the Library with its original name and settings.

## Tips for Best Results

- Pick a storage folder you can access from a file manager in case you need to share or inspect files.
- Extract support images after a major game update if new servants or craft essences were added.
- Keep at least one recent backup stored outside your device (cloud storage or computer) to protect against data loss.
- Enable notifications so you see extraction and backup progress alerts.

## Troubleshooting

- **Storage folder does not save:** Make sure you granted FGA access to the folder when the system picker appeared. Re-select the folder if permission was denied.
- **Support images not found:** Tap Extract default support images again. If extraction fails, check available storage space.
- **Backup file is empty or corrupted:** Try exporting again to a different folder. If the problem persists, ensure FGA has write access to the target location.
- **Restore does nothing:** Confirm the file is a valid FGA backup JSON. Other JSON files or corrupted exports will not import correctly.
