# Changelog

## Unreleased

### New features

- Battle script got its own script execution updated with scheduler.
  - BFGO NP Skip was given higher priority at certain points of time making it reliable to skip 3 NPs in a row.
  - Some parts of the battle script are turned off at certain points in time
  - Some of the screen checks are only checked every N turns during certain periods of time because they are unlikely to match.
  - The above changes should, in theory, reduce the processing power needed due to not checking all of the screen matches every time.
- Added missing image template for the Command Spell for KR/CN/TW (untested, but should work in theory)
- Added Command Card Screen detection (will be referred to as the Attack screen)
  - This is the part of the battle script where you will have to choose command cards
  - In case of a lag, the script should be able to recover using this as the starting point
- Added retry to open the attack screen.
  - Often, lag can prevent the attack screen from opening. We have added a retry mechanism for this.
- Partial Support for Android 17
- Added two new materials
  - https://apps.atlasacademy.io/db/JP/item/6564
    
    ![Pearl of Creation](https://static.atlasacademy.io/JP/Items/6564.png)

  - https://apps.atlasacademy.io/db/JP/item/6565

    ![Black Sea Amber](https://static.atlasacademy.io/JP/Items/6565.png)

### Fixes

- Support Image Maker was crashing because I accidentally deleted a string, re-added now.
- Database crash loading on the Battle configs should be resolved now

## 2541

2026-05-08

- feat(battle): Card Priority Per Turn setup (ArthurKun21/FGA-Preview#1232) (@ArthurKun21)
- feat(battle): add toggle servant priority per wave and/or turn (ArthurKun21/FGA-Preview#1233) (@ArthurKun21)
- feat(battle): Servant Priority per Turn setup (ArthurKun21/FGA-Preview#1234) (@ArthurKun21)
- chore(battle): centralized crud command card data operations (ArthurKun21/FGA-Preview#1236) (@ArthurKun21)
- feat(battle): Brave Chain per Turn setup (ArthurKun21/FGA-Preview#1239) (@ArthurKun21)
- feat(battle): Rearrange Card per Turn setup (ArthurKun21/FGA-Preview#1240) (@ArthurKun21)
- feat(ui): Add support for creating turn config at command card screen (ArthurKun21/FGA-Preview#1241) (@ArthurKun21)
- Update dependency io.ktor:ktor-client-java to v3.4.3 (ArthurKun21/FGA-Preview#1225) (@renovate[bot])
- Update kotlin to v2.3.21 (ArthurKun21/FGA-Preview#1226) (@renovate[bot])
- Update metro to v1 (ArthurKun21/FGA-Preview#1235) (@renovate[bot])
- Update onnxruntime to v1.25.1 (ArthurKun21/FGA-Preview#1237) (@renovate[bot])
- Update Gradle to v9.5.0 (ArthurKun21/FGA-Preview#1238) (@renovate[bot])
- chore(skill-maker): Remove Start SkillMakerEntry and related logic (ArthurKun21/FGA-Preview#1249) (@ArthurKun21)
- feat(data): added 2nd Ok template for KR (ArthurKun21/FGA-Preview#1250) (@ArthurKun21)
- chore(skill-maker): simplify SkillMakerEntryModel methods and logic (ArthurKun21/FGA-Preview#1251) (@ArthurKun21)
- feat(skill-maker): implement dsl configuration for special skills (ArthurKun21/fga-preview#1252) (@ArthurKun21)
- feat(di): Metro modernization (ArthurKun21/fga-preview#1254) (@ArthurKun21)
- fix: update highlight logic for image matching (ArthurKun21/FGA-Preview#1255) (@ArthurKun21)
- fix(skill-maker): NPs getting sorted, should follow order (ArthurKun21/fga-preview#1257) (@ArthurKun21)
- feat(battle): increase max waves for card priority from 3 to 4 (ArthurKun21/fga-preview#1258) (@ArthurKun21)
- feat(support): Track preferred support picks during auto-battle runs (ArthurKun21/fga-preview#1259) (@ArthurKun21)
- fix(support): Break loop when user navigated away from support screen (ArthurKun21/FGA-Preview#1260) (@ArthurKun21)
- Update filekit to v0.14.1 (ArthurKun21/FGA-Preview#1253) (@renovate[bot])
- Update dependency org.jetbrains.androidx.navigation3:navigation3-ui to v1.1.1 (ArthurKun21/FGA-Preview#1261) (@renovate[bot])
- Update agp to v9.2.1 (ArthurKun21/FGA-Preview#1262) (@renovate[bot])
- fix(ui): Prioritize selected support entries in support selection (ArthurKun21/FGA-Preview#1263) (@ArthurKun21)
- fix(launcher): battle config data are missing some data and uses default (ArthurKun21/FGA-Preview#1264) (@ArthurKun21)
- feat(ui): track and re-display last script exit status (ArthurKun21/fga-preview#1246) (@ArthurKun21)
- feat(data): integrate database with image loader of support images (ArthurKun21/fga-preview#1265) (@ArthurKun21)
- Update dependency androidx.paging:paging-compose to v3.5.0 (ArthurKun21/fga-preview#1266) (@renovate[bot])
- Update dependency org.jetbrains.kotlinx:kotlinx-datetime to v0.8.0-0.6.x-compat (ArthurKun21/FGA-Preview#1267) (@renovate[bot])
- feat(ui): change the wave/turn buttons to fab in command card screen (ArthurKun21/FGA-Preview#1269) (@ArthurKun21)

### Breaking Changes

#### Command Card Selection

- Card Priority, Servant Priority, etc., now support turn-based configuration.
- Updated the serialization format for Card and Servant Priority. Configurations saved in this version are not backward-compatible with older versions but still maintains backward-compatibility with older versions.
- Changed the text for new wave configuration from `"
"` to `"[w]"` and added `"[t]"` for the new turn configuration.
- `Use Servant Priority` is now turned into `Enable Servant Priority`, and you can now adjust if you want servant priority or not per wave and/or turn.
- Increase card priority waves from 3 to 4

<img width="524" height="355" alt="image" src="https://github.com/user-attachments/assets/ea653f95-32d9-4012-8f00-72049f740209" />

<img width="774" height="84" alt="image" src="https://github.com/user-attachments/assets/d5f895bf-1be0-48a1-b5d2-13b8be0855bf" />

### Fix

- There were some problem in UI where setting NPs causes it to be sorted out. We already address this problem
    - For technical reason, it was due to us using set instead of list causing it to lost the order, we have now moved it to List
- When users are manually navigating away from support screen while the auto battle is on, it will cause an infinite loop with the script. We have now fixed this by adding a checking the screen and exit that portion of the script when no longer in the support screen.
- We have now fixed the preferred support selection and it will now sorted the already selected supports on opening preferred support selection screen. This got broken when we migrated from manual query to using database.

    <img width="532" height="410" alt="image" src="https://github.com/user-attachments/assets/51fe5dc6-c640-49a6-9ff5-2cda189d7251" />
  
- Fixed the Battle Launcher not updating all of the battle config data causing incorrect values on the summary screen.

### Feat

- Added tracking of preferred support Servants/CEs/Friends. Can show you how many time a certain preferred support got picked

    <img width="505" height="658" alt="image" src="https://github.com/user-attachments/assets/cf66a817-7b01-437d-95f7-230f76773e0e" />
  
- Added tracking of last script exit window. You can now see the results of your last script run if you accidentally closed the results fast.

    <img width="174" height="87" alt="image" src="https://github.com/user-attachments/assets/7a442c8c-5b0f-404f-9d59-e4a4445286b8" />

## 2509

2026-04-26

- feat(skill-maker): add support for Prelati (ArthurKun21/FGA-Preview#1231) (@ArthurKun21)

### Feat

- Added [Prelati](https://apps.atlasacademy.io/db/JP/servant/467) to the Skill Maker

    <img width="150" height="150" alt="image" src="https://static.atlasacademy.io/JP/Faces/f_5056000.png" />

    <img width="429" height="92" alt="image" src="https://github.com/user-attachments/assets/3029a130-188e-455e-93a7-7824d7c77274" />

## 2508

2026-04-25

- Update agp to v9.1.1 (ArthurKun21/FGA-Preview#1203) (@renovate[bot])
- Update compose.multiplatform.material3 to v1.11.0-alpha06 (ArthurKun21/FGA-Preview#1204) (@renovate[bot])
- feat(battle): Allow users to choose which command to start script execution from (ArthurKun21/FGA-Preview#1205) (@ArthurKun21)
- fix(battle): improve logic for out of commands/off-script exit (ArthurKun21/fga-preview#1206) (@ArthurKun21)
- fix(battle): invalid command at script causes the app to crash (ArthurKun21/fga-preview#1207) (@ArthurKun21)
- chore: simplify nav3 saved state configs (ArthurKun21/FGA-Preview#1208) (@ArthurKun21)
- feat(gradle): Enable unused return checker (ArthurKun21/fga-preview#1209) (@ArthurKun21)
- feat(battle/bfgo): improve 1st NP Skip detection and execution (ArthurKun21/FGA-Preview#1194) (@ArthurKun21)
- fix(battle): resolved duplicate start command index issue (ArthurKun21/FGA-Preview#1212) (@ArthurKun21)
- test: fix leftover compose string tests (ArthurKun21/fga-preview#1213) (@ArthurKun21)
- fix(battle): resolve wave and turn override issues (ArthurKun21/FGA-Preview#1215) (@ArthurKun21)
- fix(ui): Update Skill Maker command colors and corrected servant color grouping (ArthurKun21/FGA-Preview#1216) (@ArthurKun21)
- Update onnxruntime to v1.25.0 (ArthurKun21/FGA-Preview#1218) (@renovate[bot])
- Update dependency sh.calvin.reorderable:reorderable to v3.1.0 (ArthurKun21/FGA-Preview#1219) (@renovate[bot])
- Update agp to v9.2.0 (ArthurKun21/FGA-Preview#1220) (@renovate[bot])
- Update compose.multiplatform.material3 to v1.11.0-alpha07 (ArthurKun21/FGA-Preview#1222) (@renovate[bot])
- Update dependency org.jetbrains.androidx.navigation3:navigation3 to v1.1.0 (ArthurKun21/FGA-Preview#1223) (@renovate[bot])
- fix(ui): start command selector collapsed by default (ArthurKun21/FGA-Preview#1227) (@ArthurKun21)
- docs: create DESIGN.md (ArthurKun21/fga-preview#1228) (@ArthurKun21)

### Feat

- Added the ability to start the script at a different step of the battle script

    <img width="576" height="382" alt="image" src="https://github.com/user-attachments/assets/132220ad-c212-4447-b016-cb7f53486ef3" />

    <img width="750" height="367" alt="image" src="https://github.com/user-attachments/assets/9a2879ee-786a-412d-81a0-251fadd24797" />

    For the initial run, it overrides the wave and/or turn based on the wave and turn from the selected step in the battle script. Subsequent runs will follow the normal battle script flow.

#### BFGO NP Skip

- Updated NP skip detection for better FGO, new logic currently only improves the 1st NP skip detection. For further improvements of the consecutive NP Skip detection(2nd and 3rd NP still uses old logic). It is going to require a lot of work to make it work reliably so it is going to be a future update.

### Fixes

#### UI

- I, mistakenly, used `skill1` instead of `servant1` when I was updating the colors for skill maker commands, this caused the colors to be same for `a` `d` and `g` instead of `a` `b` and `c` and so on. This has now been revert back to older color scheme. Also took the opportunity to update the other skill command colors as well.

#### Battle

- Improve the logic for checking out of commands/off script.
- When you imported a battle script with an invalid command, running it will cause the app to crash due to the error not being catch properly. Now it will show the error message properly instead of crashing the app.

## 2489

2026-04-13

- Update metro to v0.12.0 (ArthurKun21/FGA-Preview#1172) (@renovate[bot])
- Update gradle/actions action to v6 (ArthurKun21/FGA-Preview#1171) (@renovate[bot])
- Update dependency androidx.work:work-runtime to v2.11.2 (ArthurKun21/FGA-Preview#1173) (@renovate[bot])
- Update dependency androidx.browser:browser to v1.10.0 (ArthurKun21/FGA-Preview#1174) (@renovate[bot])
- fix: coil and compose resources not working in windows desktop (ArthurKun21/FGA-Preview#1175) (@ArthurKun21)
- feat(desktop): create jvm equivalent for work manager (ArthurKun21/FGA-Preview#1177) (@ArthurKun21)
- Update compose.multiplatform.material3 to v1.11.0-alpha05 (ArthurKun21/FGA-Preview#1178) (@renovate[bot])
- Update metro to v0.12.1 (ArthurKun21/FGA-Preview#1180) (@renovate[bot])
- fix(battle): update TW to the new face card region (ArthurKun21/FGA-Preview#1182) (@ArthurKun21)
- fix(support): infinite support loop when no scrollbar (ArthurKun21/FGA-Preview#1183) (@ArthurKun21)
- feat(battle): preload support images for preferred support on script start (ArthurKun21/fga-preview#1184) (@ArthurKun21)
- Update dependency com.github.ArthurKun21:compose-overlay-window to v1.5.5 (ArthurKun21/FGA-Preview#1185) (@renovate[bot])
- feat(support): add CE slot matching for Grand Servants (ArthurKun21/fga-preview#1186) (@ArthurKun21)
- feat(db): Switch to AndroidX bundled sqlite driver (ArthurKun21/FGA-Preview#1187) (@ArthurKun21)
- Update dependency io.ktor:ktor-client-java to v3.4.2 (ArthurKun21/FGA-Preview#1179) (@renovate[bot])
- Update dependency com.cheonjaeung.compose.grid:grid to v2.7.1 (ArthurKun21/FGA-Preview#1188) (@renovate[bot])
- Update metro to v0.13.0 (ArthurKun21/FGA-Preview#1189) (@renovate[bot])
- Update metro to v0.13.1 (ArthurKun21/FGA-Preview#1191) (@renovate[bot])
- Update metro to v0.13.2 (ArthurKun21/FGA-Preview#1192) (@renovate[bot])
- Update generic.datastore to v2.0.0-alpha08 (ArthurKun21/FGA-Preview#1193) (@renovate[bot])
- Update dependency org.jetbrains.kotlinx:kotlinx-serialization-json to v1.11.0 (ArthurKun21/FGA-Preview#1196) (@renovate[bot])
- fix(ui): some dialog have transparent background (ArthurKun21/FGA-Preview#1197) (@ArthurKun21)
- chore(gradle): add support for GitHub packages (ArthurKun21/fga-preview#1198) (@ArthurKun21)
- fix(ui): replace SearchBar with TopAppBar with TextField for better keyboard handling (ArthurKun21/FGA-Preview#1199) (@ArthurKun21)
- fix: update bond level up stop summary to clarify it also stops when above target level is reached (ArthurKun21/FGA-Preview#1200) (@ArthurKun21)
- fix(javacv): dll loading issue on windows by using jdk 25 (ArthurKun21/fga-preview#1201) (@ArthurKun21)

### Fixes

- Fix the infinite support screen refresh
- Fix the face card for TW, now all servers uses the new servant face card region.
- Fix the textfield UI for Support Gallery, Library and Material selection screen where the keyboard won't open for Android even though the textfield is focused.
- Fix the dialog UI for Support Gallery and Preferred Support where the background is transparent instead of solid color.
- Update the text for `stop on bond level up` to clarify that it is also includes above the selected target bond level as well.

### Feat

#### Support New Feat

- Added new configuration for grand servants to enable choosing if the user wants to match both CE Slot 1 and 3 or just either one of them. Selecting "Either" should match the current behavior of the main repository.

    <img width="555" height="167" alt="image" src="https://github.com/user-attachments/assets/475dbc4b-17a0-48b7-b7b5-b07bdbb5bffd" />

- Added preloading of supports at the start of battle script. This should help with the user to know if there's any problem with the support images much earlier rather than waiting until the support screen to show up and then finding out that the images are not loading.

## 2463

2026-03-23

- feat(ui): Improve Home Screen UI (ArthurKun21/FGA-Preview#983) (@ArthurKun21)
- feat: create local database for Support (ArthurKun21/FGA-Preview#981) (@ArthurKun21)
- Update metro to v0.9.4 (ArthurKun21/FGA-Preview#987) (@renovate[bot])
- chore: rename Images to Template (ArthurKun21/FGA-Preview#991) (@ArthurKun21)
- Update dependency androidx.paging:paging-compose to v3.3.6 (ArthurKun21/FGA-Preview#990) (@renovate[bot])
- chore(deps): migrate to compose multiplatform deps except material3 (ArthurKun21/FGA-Preview#994) (@ArthurKun21)
- chore: migrate JVM models module into KMP shared library (ArthurKun21/FGA-Preview#997) (@ArthurKun21)
- chore: move app string resources to shared module's compose resources (ArthurKun21/FGA-Preview#1002) (@ArthurKun21)
- Update compose.multiplatform to v1.10.0 (ArthurKun21/FGA-Preview#1000) (@renovate[bot])
- chore(gradle): Update Gradle Build and documentation (ArthurKun21/FGA-Preview#1005) (@ArthurKun21)
- chore: update renovate configuration for Jetbrains libraries (@ArthurKun21)
- feat: add multiplatform libimaging module and convert libocr to KMP (ArthurKun21/FGA-Preview#1006) (@ArthurKun21)
- fix(di): resolve compiler warning when binding internal class to public interface (ArthurKun21/FGA-Preview#1011) (@ArthurKun21)
- Update androidx.compose.material3 to v1.5.0-alpha12 (ArthurKun21/FGA-Preview#1009) (@renovate[bot])
- Update androidx.compose.material3.adaptive to v1.3.0-alpha06 (ArthurKun21/FGA-Preview#1010) (@renovate[bot])
- chore: separate libautomata from data module dependency (ArthurKun21/FGA-Preview#1014) (@ArthurKun21)
- docs: Update documentation (@ArthurKun21)
- chore(deps): update to agp 9.0 (ArthurKun21/FGA-Preview#1016) (@ArthurKun21)
- chore: add core library desugaring (ArthurKun21/FGA-Preview#1017) (@ArthurKun21)
- chore(metro): optimized dependency injection bindings (ArthurKun21/FGA-Preview#1019) (@ArthurKun21)
- Update Gradle to v9.3.0 (ArthurKun21/FGA-Preview#1018) (@renovate[bot])
- feat(ui): integrate local support DB into Preferred Support screen (ArthurKun21/FGA-Preview#1020) (@ArthurKun21)
- feat: switch to uuid7 (ArthurKun21/FGA-Preview#1021) (@ArthurKun21)
- feat(battle): introduce modular battle command parser (with tests and docs) (ArthurKun21/FGA-Preview#1022) (@ArthurKun21)
- fix: use ComposeString for unified localization of strings in scripts module (ArthurKun21/FGA-Preview#1023) (@ArthurKun21)
- feat(logging): store logcat entries in database for script runs (ArthurKun21/FGA-Preview#1025) (@ArthurKun21)
- Update metro to v0.10.0 (ArthurKun21/FGA-Preview#1024) (@renovate[bot])
- feat: update Custom FGA colors to use light and dark colors (ArthurKun21/FGA-Preview#1026) (@ArthurKun21)
- Update dependency org.jetbrains.kotlinx:kotlinx-serialization-json to v1.10.0 (ArthurKun21/FGA-Preview#1027) (@renovate[bot])
- chore(ui): replace duplicate SegmentedListItem implementations with shared component (ArthurKun21/FGA-Preview#1029) (@ArthurKun21)
- Update dependency org.opencv:opencv to v4.13.0 (ArthurKun21/FGA-Preview#1030) (@renovate[bot])
- feat(ui): Update Battle Config Screen (ArthurKun21/FGA-Preview#1032) (@ArthurKun21)
- Update dependency com.diffplug.spotless:spotless-plugin-gradle to v8.2.0 (ArthurKun21/FGA-Preview#1031) (@renovate[bot])
- docs: Update Documentation (@ArthurKun21)
- Update metro to v0.10.1 (ArthurKun21/FGA-Preview#1034) (@renovate[bot])
- chore(ui): consolidate NavDisplay for consistent experience (ArthurKun21/FGA-Preview#1036) (@ArthurKun21)
- fix: unit tests not running after agp 9 upgrade (ArthurKun21/FGA-Preview#1038) (@ArthurKun21)
- Update mockk to v1.14.9 (ArthurKun21/FGA-Preview#1037) (@renovate[bot])
- feat(scripts): Set up retryable actions (ArthurKun21/FGA-Preview#1035) (@ArthurKun21)
- chore: move notifications and toasts into libautomata (ArthurKun21/FGA-Preview#1039) (@ArthurKun21)
- feat: convert libAutomata to KMP (ArthurKun21/FGA-Preview#1040) (@ArthurKun21)
- chore: extract the Preference Keys into an internal object (ArthurKun21/FGA-Preview#1043) (@ArthurKun21)
- chore: remove alpha maven repositories for compose multiplatform (@ArthurKun21)
- Update dependency com.diffplug.spotless:spotless-plugin-gradle to v8.2.1 (ArthurKun21/FGA-Preview#1041) (@renovate[bot])
- Update dependency androidx.work:work-runtime to v2.11.1 (ArthurKun21/FGA-Preview#1044) (@renovate[bot])
- Update metro to v0.10.2 (ArthurKun21/FGA-Preview#1045) (@renovate[bot])
- Update activity to v1.12.3 (ArthurKun21/FGA-Preview#1048) (@renovate[bot])
- Update dependency com.github.ArthurKun21:compose-overlay-window to v1.5.3 (ArthurKun21/FGA-Preview#1049) (@renovate[bot])
- Update dependency androidx.paging:paging-compose to v3.4.0 (ArthurKun21/FGA-Preview#1051) (@renovate[bot])
- Update Gradle to v9.3.1 (ArthurKun21/FGA-Preview#1052) (@renovate[bot])
- Update lifecycle.multiplatform to v2.10.0-alpha08 (ArthurKun21/FGA-Preview#1054) (@renovate[bot])
- Update kotlin to v2.3.10 (ArthurKun21/FGA-Preview#1055) (@renovate[bot])
- Update dependency com.microsoft.onnxruntime:onnxruntime-android to v1.24.1 (ArthurKun21/FGA-Preview#1056) (@renovate[bot])
- Update metro to v0.10.3 (#1057) (@renovate[bot])
- chore: enable explicit APIs (ArthurKun21/FGA-Preview#1058) (@ArthurKun21)
- Update compose.multiplatform to v1.10.1 (ArthurKun21/FGA-Preview#1059) (@renovate[bot])
- Update activity to v1.12.4 (ArthurKun21/FGA-Preview#1063) (@renovate[bot])
- Update dependency androidx.paging:paging-compose to v3.4.1 (ArthurKun21/FGA-Preview#1064) (@renovate[bot])
- Update androidx.compose.material3 to v1.5.0-alpha14 (ArthurKun21/FGA-Preview#1046) (@renovate[bot])
- Update androidx.compose.material3.adaptive to v1.3.0-alpha08 (ArthurKun21/FGA-Preview#1047) (@renovate[bot])
- Update dependency com.android.tools.build:gradle to v9.0.1 (ArthurKun21/FGA-Preview#1065) (@renovate[bot])
- Update metro to v0.10.4 (ArthurKun21/FGA-Preview#1066) (@renovate[bot])
- feat: add jvm to localdb module (ArthurKun21/FGA-Preview#1067) (@ArthurKun21)
- fix(di): aggregation scopes should be abstract classes, not annotations (ArthurKun21/FGA-Preview#1069) (@ArthurKun21)
- chore: update handling of work manager (ArthurKun21/FGA-Preview#1070) (@ArthurKun21)
- feat: remove Material icons deps and update icons (ArthurKun21/FGA-Preview#1071) (@ArthurKun21)
- feat: add jvm source to libimaging and libocr (ArthurKun21/fga-preview#1072) (@ArthurKun21)
- feat: create initial jvm source for libautomata (ArthurKun21/fga-preview#1073) (@ArthurKun21)
- feat: Split APKs (ArthurKun21/FGA-Preview#1075) (@ArthurKun21)
- docs: Update Agents.md and other agents related docs (ArthurKun21/FGA-Preview#1077) (@ArthurKun21)
- feat: KMP Multiplatform permissions (ArthurKun21/FGA-Preview#1076) (@ArthurKun21)
- feat: move settings screen to main tabs (ArthurKun21/FGA-Preview#1078) (@ArthurKun21)
- feat!: remove onboarding screen (ArthurKun21/FGA-Preview#1079) (@ArthurKun21)
- feat: added the permissions check on Home Screen (ArthurKun21/FGA-Preview#1080) (@ArthurKun21)
- feat: move Fine-Tune back to Settings Screen (ArthurKun21/FGA-Preview#1081) (@ArthurKun21)
- Update onnxruntime to v1.24.2 (ArthurKun21/FGA-Preview#1082) (@renovate[bot])
- Update dependency org.junit.jupiter:junit-jupiter-engine to v6.0.3 (ArthurKun21/FGA-Preview#1068) (@renovate[bot])
- feat: partial migration of data module to kmp (ArthurKun21/FGA-Preview#1083) (@ArthurKun21)
- chore: enable explicit API on data module (ArthurKun21/FGA-Preview#1084) (@ArthurKun21)
- feat: migrate App Preferences to KMP (ArthurKun21/FGA-Preview#1085) (@ArthurKun21)
- feat(ui): add marker to permission items for better accessibility (ArthurKun21/FGA-Preview#1086) (@ArthurKun21)
- feat: migrate storage to kmp (ArthurKun21/fga-preview#1088) (@ArthurKun21)
- feat: update Image Loader into KMP (ArthurKun21/fga-preview#1090) (@ArthurKun21)
- chore(gradle): simplify build settings  (ArthurKun21/FGA-Preview#1091) (@ArthurKun21)
- feat: update the di wiring on data module (ArthurKun21/FGA-Preview#1092) (@ArthurKun21)
- Update dependency org.bytedeco:opencv-platform to v4.13.0-1.5.13 (ArthurKun21/FGA-Preview#1089) (@renovate[bot])
- feat: Update di wiring on libautomata (ArthurKun21/FGA-Preview#1093) (@ArthurKun21)
- feat: move UI components to compose App module (ArthurKun21/fga-preview#1094) (@ArthurKun21)
- Update coil to v3.4.0 (ArthurKun21/FGA-Preview#1097) (@renovate[bot])
- Update dependency io.github.vinceglb:filekit-core to v0.13.0 (ArthurKun21/FGA-Preview#1098) (@renovate[bot])
- feat: migrate Scripts module to kmp (ArthurKun21/fga-preview#1100) (@ArthurKun21)
- Update metro to v0.11.0 (ArthurKun21/fga-preview#1099) (@renovate[bot])
- fix(metro): Parameter names must match the constructor exactly (ArthurKun21/fga-preview#1101) (@ArthurKun21)
- chore(gradle): migrate from buildSrc to build-logic (ArthurKun21/FGA-Preview#1102) (@ArthurKun21)
- feat: further preparation of composeApp module (ArthurKun21/fga-preview#1103) (@ArthurKun21)
- Update metro to v0.11.1 (ArthurKun21/fga-preview#1104) (@renovate[bot])
- feat: move fine tune screen to composeApp (ArthurKun21/FGA-Preview#1105) (@ArthurKun21)
- feat: migrate command card screen to compose app (ArthurKun21/fga-preview#1106) (@ArthurKun21)
- feat: migrate material screen to compose App (ArthurKun21/FGA-Preview#1107) (@ArthurKun21)
- feat: migrate Support Image Maker screen to compose App (ArthurKun21/fga-preview#1108) (@ArthurKun21)
- Update actions/upload-artifact action to v7 (ArthurKun21/FGA-Preview#1109) (@renovate[bot])
- feat: add Media Projection re-request when the token is invalidated (ArthurKun21/FGA-Preview#1110) (@ArthurKun21)
- feat: add Accessibility Service validator and re-request (ArthurKun21/FGA-Preview#1111) (@ArthurKun21)
- fix: missing string resources config in script module (ArthurKun21/FGA-Preview#1112) (@ArthurKun21)
- feat(support): raise error for missing support images (ArthurKun21/FGA-Preview#1113) (@ArthurKun21)
- feat(storage): use internal storage as default (ArthurKun21/fga-preview#1114) (@ArthurKun21)
- Update compose.multiplatform.adaptive to v1.3.0-alpha05 (ArthurKun21/FGA-Preview#1115) (@renovate[bot])
- Update compose.multiplatform.material3 to v1.11.0-alpha03 (ArthurKun21/FGA-Preview#1116) (@renovate[bot])
- feat: migrate skill maker screen to composeApp (ArthurKun21/FGA-Preview#1117) (@ArthurKun21)
- feat: migrate Support Gallery screen to compose App (ArthurKun21/FGA-Preview#1118) (@ArthurKun21)
- feat: migrate Preferred Support Screen to compose App (ArthurKun21/FGA-Preview#1119) (@ArthurKun21)
- feat(di): partial migration of metro di configs to compose app (ArthurKun21/FGA-Preview#1120) (@ArthurKun21)
- feat(gradle): migrate build constants to compose app (ArthurKun21/FGA-Preview#1121) (@ArthurKun21)
- feat(skill maker): add flora (ArthurKun21/fga-preview#1122) (@ArthurKun21)
- Update metro to v0.11.2 (ArthurKun21/FGA-Preview#1123) (@renovate[bot])
- Update dependency com.cheonjaeung.compose.grid:grid to v2.7.0 (ArthurKun21/FGA-Preview#1124) (@renovate[bot])
- feat(support): add more support template images (ArthurKun21/FGA-Preview#1125) (@ArthurKun21)
- feat: migrate exit launchers to compose app (ArthurKun21/FGA-Preview#1131) (@ArthurKun21)
- Update spotless to v8.3.0 (ArthurKun21/FGA-Preview#1126) (@renovate[bot])
- Update dependency io.ktor:ktor-client-java to v3.4.1 (ArthurKun21/FGA-Preview#1127) (@renovate[bot])
- Update agp to v9.1.0 (ArthurKun21/FGA-Preview#1128) (@renovate[bot])
- Update Gradle to v9.4.0 (ArthurKun21/FGA-Preview#1129) (@renovate[bot])
- Update compose.multiplatform to v1.10.2 (ArthurKun21/FGA-Preview#1130) (@renovate[bot])
- Update onnxruntime to v1.24.3 (ArthurKun21/FGA-Preview#1132) (@renovate[bot])
- feat: update some toast usages with snackbar (ArthurKun21/FGA-Preview#1133) (@ArthurKun21)
- feat: use FileKit for import and export (ArthurKun21/FGA-Preview#1134) (@ArthurKun21)
- feat: migrate Battle Config Screen to composeApp (ArthurKun21/FGA-Preview#1135) (@ArthurKun21)
- feat: create abstraction for background services in compose app (ArthurKun21/FGA-Preview#1136) (@ArthurKun21)
- feat: migrate Library screen to compose app (ArthurKun21/FGA-Preview#1137) (@ArthurKun21)
- feat: migrate home screen to compose app (ArthurKun21/FGA-Preview#1138) (@ArthurKun21)
- feat: migrate settings screen to compose app (ArthurKun21/FGA-Preview#1141) (@ArthurKun21)
- Update dependency androidx.paging:paging-compose to v3.4.2 (ArthurKun21/FGA-Preview#1139) (@renovate[bot])
- ci: Update PR branch workflow (ArthurKun21/fga-preview#1144) (@ArthurKun21)
- Update activity to v1.13.0 (ArthurKun21/FGA-Preview#1140) (@renovate[bot])
- Update dependency androidx.core:core-ktx to v1.18.0 (ArthurKun21/FGA-Preview#1142) (@renovate[bot])
- Update okio to v3.17.0 (ArthurKun21/FGA-Preview#1143) (@renovate[bot])
- Update compose.multiplatform.material3 to v1.11.0-alpha04 (ArthurKun21/FGA-Preview#1146) (@renovate[bot])
- Update lifecycle.multiplatform to v2.10.0-beta01 (ArthurKun21/FGA-Preview#1147) (@renovate[bot])
- Update compose.multiplatform.adaptive to v1.3.0-alpha06 (ArthurKun21/fga-preview#1145) (@renovate[bot])
- chore(gradle): replace deprecated build settings (ArthurKun21/fga-preview#1148) (@ArthurKun21)
- feat(desktop): initial desktop app setup (ArthurKun21/fga-preview#1149) (@ArthurKun21)
- fix(navigation): simplify adaptive navigation layout (ArthurKun21/FGA-Preview#1151) (@ArthurKun21)
- feat: migrate app module from java to kotlin source (ArthurKun21/FGA-Preview#1153) (@ArthurKun21)
- Update sqldelight to v2.3.1 (ArthurKun21/FGA-Preview#1152) (@renovate[bot])
- Update kotlin to v2.3.20 (ArthurKun21/FGA-Preview#1154) (@renovate[bot])
- Update metro to v0.11.3 (ArthurKun21/FGA-Preview#1155) (@renovate[bot])
- Update sqldelight to v2.3.2 (ArthurKun21/FGA-Preview#1156) (@renovate[bot])
- feat(skill-maker): update UI for the bottom bar items to be adaptive (ArthurKun21/FGA-Preview#1157) (@ArthurKun21)
- feat(skill-maker): replace tooltip move controls with inline buttons in history UI (ArthurKun21/FGA-Preview#1158) (@ArthurKun21)
- Update metro to v0.11.4 (ArthurKun21/FGA-Preview#1159) (@renovate[bot])
- Update spotless to v8.4.0 (ArthurKun21/FGA-Preview#1163) (@renovate[bot])
- Update compose.multiplatform to v1.10.3 (ArthurKun21/FGA-Preview#1164) (@renovate[bot])
- Update Gradle to v9.4.1 (ArthurKun21/FGA-Preview#1165) (@renovate[bot])
- Update dependency com.ibm.icu:icu4j to v78.3 (ArthurKun21/FGA-Preview#1160) (@renovate[bot])
- Update lifecycle.multiplatform to v2.10.0 (ArthurKun21/FGA-Preview#1166) (@renovate[bot])
- feat(ui): added images to the refill resources (ArthurKun21/FGA-Preview#1167) (@ArthurKun21)
- fix(battle): update EN to the new face card region (ArthurKun21/FGA-Preview#1168) (@ArthurKun21)
- revert(logging): roll back database logging pending future update (ArthurKun21/FGA-Preview#1169) (@ArthurKun21)
- feat(launcher): added more Battle Settings (ArthurKun21/FGA-Preview#1170) (@ArthurKun21)

### Breaking Changes

- Update the Battle Script Command Parser. You can now add whitespaces, tabs and new lines for better readability. All of this are going to be ignored when parsing the commands.

    <img width="1070" height="386" alt="image" src="https://github.com/user-attachments/assets/56b8a52b-f520-420c-9741-74358894c508" />

    It also reacts if you type in a wrong command right after you type

    <img width="545" height="258" alt="image" src="https://github.com/user-attachments/assets/1b192526-6081-4b9c-9398-fa9b1f1ada75" />
  
> [!IMPORTANT]
>
> Any existing battle scripts edited after this version will no longer be compatible with older versions of the app. If you want to use it, you gotta update to remove the whitespaces, tabs and new lines.

### Features

- Update Home Screen UI. Added server clock and a simple gallery list detail view of the current supports. Links in Home Screen are now displayed to users.

    <img width="1442" height="502" alt="image" src="https://github.com/user-attachments/assets/8a8ebf13-f011-402e-bae5-a27aadaec450" />

- Added the Support Gallery Screen, it was mostly for viewing support template images in the support directory. This function can also be viewed as well on Preferred Support Screen.
- On app startup, there would be once in a whole app lifecycle where it will scan of the support images in the support directory in order to ensure that the paths are up to date.
- Added Images next to Support Template Images

    <img width="775" height="383" alt="image" src="https://github.com/user-attachments/assets/ed5fcf09-221b-4338-a3ae-bc244ccf8fc4" />

    <img width="795" height="347" alt="image" src="https://github.com/user-attachments/assets/d0122f8e-f205-4165-967a-45667b4e28ce" />

- On Preferred Support Screen, you can now see support's template images. This will help you when you forgot the name but remember the image like me.

    <img width="524" height="429" alt="image" src="https://github.com/user-attachments/assets/46175ad2-16a0-427c-bdba-51fef43aa321" />

- Battle Config got some design update as well. Notes, like edit skill command, are now happening on a separate screen for better User experience.
- The summary in Battle Launcher for the current battle config have now been updated to show all of the current settings in the battle config. It used to be few info only because I got tired to code it in.

- Storage now defaults to internal Storage unless changed by user. This gives a workaround to issues with certain devices
    - [Fate-Grand-Automata#1673](https://redirect.github.com/Fate-Grand-Automata/FGA/issues/1673)
    - [Fate-Grand-Automata#1168](https://redirect.github.com/Fate-Grand-Automata/FGA/issues/1168)
    - [Fate-Grand-Automata#999](https://redirect.github.com/ArthurKun21/FGA-Preview/issues/999)

- When the support images cannot be found. Will now throw an error, this should help when there's problems with storage permissions or if the support images are not properly extracted or not found in the storage.

- Added Servant Templates Images
    - [Omii-san](https://apps.atlasacademy.io/db/JP/servant/463)
    - [Flora](https://apps.atlasacademy.io/db/JP/servant/464)

- Added CE Templates Images
    - [Great Library of Memories](https://apps.atlasacademy.io/db/JP/craft-essence/2583)

- Added Flora option in Skill Maker

- Updated the Skill Maker UI to actually inline the movement button instead of having it on tooltip. This should make it easier to move the commands.

- APKs are now split into different architectures to reduce the APK size with a universal APK option for users who want to have all architectures in one APK. This should help with the installation of the app as well as reduce the storage used by the app.

- Battle Launcher have now been updated to include more common settings.

- Battle Launcher now uses the refill resources images for better visuals

- Added re-request of Media Projection(for screenshot) and Accessibility Service when they're lost. This problem was observed on some devices particularly on Samsung devices when the screen was turned off.

### Fixes

- EN have now updated its UI to the accomodate the Alignment and Attribute.

    - <img width="400" height="347" alt="image" src="https://webview.fate-go.us/wp-content/uploads/2026/03/0323_olgamally_quest_2/info_06_sf9b1.png" />

### Misc

- Some optimization for running scripts. This is due to updating some of the inner workings of the dependency injection which ties in the program together.

> [!NOTE]
>
> We are preparing for v2 of the Supports in the future. This will enable to download the latest support images with support for Translations. But this is going to take a lot of time so we just released the database with the current support template images.

## 2304

2026-01-08

- chore(deps): update compose bom to stable and split material3 deps (ArthurKun21/FGA-Preview#958) (@ArthurKun21)
- Update metro to v0.9.2 (ArthurKun21/FGA-Preview#949) (@renovate[bot])
- chore: move ScriptAreaTransforms to libAutomata module (ArthurKun21/FGA-Preview#959) (@ArthurKun21)
- Update metro to v0.9.3 (ArthurKun21/FGA-Preview#968) (@renovate[bot])
- fix(battle): Update the Quest Reward template image for NA (ArthurKun21/FGA-Preview#971) (@ArthurKun21)
- fix(battle): Update skill confirmation template image for TW (@reconman)
- feat: add Reliquary of Departed Souls to the materials (ArthurKun21/FGA-Preview#972) (@ArthurKun21)
- docs: Update documentation for various guides and markdowns (ArthurKun21/FGA-Preview#973) (@ArthurKun21)
- chore: update metro di configuration (ArthurKun21/FGA-Preview#974) (@ArthurKun21)
- fix(FriendPoint): repeat summon for 100x summons (ArthurKun21/FGA-Preview#970) (@ArthurKun21)
- Update dependency com.github.ArthurKun21:compose-overlay-window to v1.5.2 (ArthurKun21/FGA-Preview#978) (@renovate[bot])
- Update dependency org.junit:junit-bom to v6.0.2 (ArthurKun21/FGA-Preview#982) (@renovate[bot])

### Fixes

- Updated the Quest Reward template image for NA server as it appears to have been updated.
- Updated the skill confirmation template image for TW server
- Fixed the repeat FP summon logic due to missing template image for 100x summon.

### Feat

- Added Reliquary of Departed Souls to the materials list. I actually forgot about this.
- Added fallback method for FP summon when 100x summmon isn't detected. It uses the `sell` button to determine that we are on the repeat fp summon screen.

---

[OLDER CHANGELOG.md](CHANGELOG_OLD.md)
