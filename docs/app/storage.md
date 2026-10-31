---
title: Storage Settings
description: Configure FGA Preview storage settings. Manage the data storage location, reset the support database, and create or restore a settings backup.
tags:
    - app
    - settings
    - storage
    - backup
    - support-database
---

# Storage Settings

## Overview

Storage Settings control where FGA keeps your data. FGA writes battle configs, screenshots, and other files to the storage location. You can also reset the support database and make a backup of your settings.

The Storage section holds three parts. The first part is the storage location. The second part resets the support database. The third part makes and restores a backup.

## Key Features

### Select the storage location

Tap **Storage Location** to open the folder picker. Tap **Edit** on the row to open the same picker. The path of the selected folder shows under the row title. The default internal storage shows as "Internal Storage".

You can also select an SD card or a folder that a cloud service syncs. A cloud folder can make FGA slower, because FGA reads and writes many small files.

!!! warning "The folder change moves your data"
    After you select a new folder, FGA moves the current data to that folder. FGA disables the row and the buttons while the move runs.

### Reset the support database

The support database holds the support images that FGA uses to read the support list.

Tap **Reset Support Database** to clear the database and build it again. The text above the button explains the action. While the reset runs, the screen shows a progress bar.

The reset runs in the background. Leave the settings screen and use other parts of FGA while the work runs.

### Make a backup of your settings

Tap **Create backup** to write all your battle configs and app settings into one JSON file.

!!! note "A backup and a restore touch only the settings in the file"
    A backup file holds a part of your settings. A restore writes over the settings in the file. A setting that the file does not contain stays unchanged.

### Restore a backup

Tap **Restore backup** and then tap **Choose file**. Select a JSON file that FGA wrote before. The import runs in the background, and a notification shows the progress.

Each config in the file appears in the Library with its original name and settings.

## Tips for Best Results

- Select a folder that you can open in a file manager. You can then share or read the files yourself.
- Keep one recent backup outside the device. Use a cloud service or a computer.
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

## Related Documentation

- [Settings](settings.md)
- [GitHub Backup](github-backup.md)
- [Library](library.md)
