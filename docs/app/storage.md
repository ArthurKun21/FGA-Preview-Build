---
title: Storage Settings
description: Configure FGA Preview storage settings. Manage the data storage location, reset the support database, create or restore a settings backup, and set up an automatic backup of battle configs.
tags:
    - app
    - settings
    - storage
    - backup
    - auto-backup
    - support-database
---

# Storage Settings

## Overview

Storage Settings control where FGA keeps your data. FGA writes battle configs, screenshots, and other files to the storage location. You can also reset the support database, make a backup of your settings, and configure an automatic backup of your battle configs.

The Storage section holds four parts. The first part is the storage location. The second part resets the support database. The third part makes and restores a backup. The fourth part configures the automatic backup of battle configs.

## Key Features

### Select the storage location

Tap **Storage Location** to open the folder picker. Tap **Edit** on the row to open the same picker. The path of the selected folder shows under the row title. The default internal storage shows as "Internal Storage".

You can also select an SD card or a folder that a cloud service syncs. A cloud folder can make FGA slower, because FGA reads and writes many small files.

> [!WARNING]
> **The folder change moves your data**
>
> After you select a new folder, FGA moves the current data to that folder. FGA disables the row and the buttons while the move runs.

### Reset the support database

The support database holds the support images that FGA uses to read the support list.

Tap **Reset Support Database** to clear the database and build it again. The text above the button explains the action. While the reset runs, the screen shows a progress bar.

The reset runs in the background. Leave the settings screen and use other parts of FGA while the work runs.

### Make a backup of your settings

Tap **Create backup** to write your app settings into one JSON file.

> [!NOTE]
> **A backup and a restore touch only the settings in the file**
>
> A backup file holds a part of your settings. A restore writes over the settings in the file. A setting that the file does not contain stays unchanged.

### Restore a backup

Tap **Restore backup** and then tap **Choose file**. Select a JSON file that FGA wrote before. The import runs in the background, and a notification shows the progress.

FGA applies the restored settings to the app.

### Configure auto backup

Auto backup writes a zip archive with your battle configs to the `configs` folder of the storage location. The archive name contains the date and the time. FGA keeps the last 4 archives and deletes older archives. An auto backup contains only your battle configs. Use **Create backup** for your app settings.

> [!NOTE]
> **Auto backup needs a storage location**
>
> FGA disables the auto backup controls while the storage location is "Internal Storage". Select a storage location first.

Set the **Backup interval** to **Daily**, **Every 2 days**, or **Weekly**. Choose **Off** to stop the automatic backups.

The row **Last auto backup** shows the date and the time of the last successful backup. The row shows **Never** before the first backup.

On Android, a scheduled job runs the backup. The job waits until the battery is not low. On the desktop version, FGA runs the backup only while the app is open. FGA shows a notification on Android, or a message on the desktop version, when a backup fails.

FGA skips a config file that it cannot read. One damaged file does not stop the backup.

To restore the configs, unzip an archive, and import the `.pb` files in the Library.

## Tips for Best Results

- Select a folder that you can open in a file manager. You can then share or read the files yourself.
- Keep one recent backup outside the device. Use a cloud service or a computer.
- Keep the storage location in a folder that a cloud service syncs. The service then keeps a copy of each auto backup.
- Reset the support database when support images do not load after a game update.
- Enable notifications so that you see the progress of a move, a reset, or a restore. See [Advanced Settings](advanced.md).

## Troubleshooting

| Problem | Solution |
| ------- | -------- |
| The new storage folder does not save | Grant FGA access to the folder when the system picker opens. Then select the folder again. |
| The storage rows and buttons are disabled | A move or a reset runs. Wait until the work finishes. |
| Support images do not load | Tap **Reset Support Database**. Check the free space on the device if the reset fails. |
| The backup file is empty or damaged | Write the backup again to a different folder. Then check that FGA can write to that folder. |
| The restore does nothing | Check that the file is a valid FGA backup JSON. Another JSON file or a damaged export does not import. |
| You cannot change the auto backup interval | Select a storage location first. The backup writes into the `configs` folder of the storage location. |
| The auto backup does not run | Check the interval under **Auto backup**. On the desktop version, FGA runs the backup only while the app is open. |

## Related Documentation

- [Settings](settings.md)
- [GitHub Backup](github-backup.md)
- [Library](library.md)
