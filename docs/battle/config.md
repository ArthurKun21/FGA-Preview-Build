# Battle Config

This is how to setup the battle config.

## Identity

- **Name** - The name of the battle config
- **Notes** - A multi-line text field for additional information. It cannot contain images only text would be rendered.

Clicking either the name or notes would popup a dialog to edit it.

| Name and notes | Name and notes dialog |
| --- | --- |
| ![Name and notes](../assets/battle/name-and-notes.png) | ![Name and notes dialog](../assets/battle/name-and-notes-dialog.png) |

## Command

Clicking the command would redirect you to the [Skill Maker Screen](skill-maker.md) while clicking the `terminal` icon would show a popup dialog for quick edit

| Skill command | Skill command dialog |
| --- | --- |
| ![skill command](../assets/battle/skill-command.png) | ![skill command dialog](../assets/battle/skill-command-dialog.png) |

## Default Run Configuration

![Default Run Configuration](../assets/battle/default-run-config.png)

When a run ended, the default run configuration values will be used for the initial values of the next run.

### Limitation

Due to current architectural limitations, we can't update the current configuration. Run/materials/CE/teapots need to reach their limits before the default values are applied.

As a workaround, we added a button in the Battle Launcher to reset the configuration to its default values.

The current migration to Datastore would hopefully resolve this issue.

## Command Card

This is the section where you'll configure the command card priority for the battle.

| Command Card Option | Command Card Option Description |
| --- | --- |
| Skip servant face-card checks | If enabled, the app will not check if the servant face card matches allowing for faster picking of cards in exchange of possibly weaker cards. |
| Use Servant Priority | If enabled, the app will prioritize the servant's cards before the command card type |
| Use Crit Stars Priority | If enabled, the app will prioritize cards with high chance to do critical damage. The default percentage is 80 ~ 100% |

Below the Command Card options is the summary of the current command card priority.

The summary is clickable and will redirect you to the [Command Card Priority](card-priority.md) page.

For more information about command cards, go to [Command Card Priority](card-priority.md)
