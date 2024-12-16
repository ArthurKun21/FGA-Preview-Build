# Fate/Grand Automata

| Build                                                                                                                                                       | Stable                                                                                                                                                                 | Preview                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![CI](https://github.com/ArthurKun21/FGA-Preview/actions/workflows/ci.yml/badge.svg)](https://github.com/ArthurKun21/FGA-Preview/actions/workflows/ci.yml) | <a href="https://github.com/Fate-Grand-Automata/FGA/releases" target="_blank"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/Fate-Grand-Automata/FGA?include_prereleases"></a> | [![Preview Build](https://img.shields.io/github/release/ArthurKun21/FGA-Preview-Build.svg?maxAge=3600&label=download)](https://github.com/ArthurKun21/FGA-Preview-Build/releases) |

<a href='https://ko-fi.com/arthurkun21' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

Current things being worked on

1. [ ] Migration from hilt
  
2. [ ] Migrate Battle Configs from prefs to FGA folder.

     It will be on the `configs` folder. Plan to enable to allow users to create folder for organization.
   
3. [ ] Github Backup and Restore for configs
  
4. [ ] FGA Settings Backup and Restore
  
5. [ ] Config tags and filter tag

     It will make it easy to search for at battle launcher.

6. [ ] Battle History.

Ideas want to work on:

1. [ ] Work on Servant Profiles.
   
2. [ ] Spam V2, it will be based from Servant Profiles to provide better skill usage during spam. It will only take effect once the Command List is empty

3. [ ] On pause, show the remaining commands
   
4. [ ] Use the current storage settings to auto save all of the configs
   
5. [ ] Probably migrate from DocumentFile to Unifile like Mihon

6. [ ] Integration with Laplace from [Chaldea](https://github.com/chaldea-center/chaldea).

    The Idea is to able to get data from Laplace and then copy paste it into another text box.

7. [ ] Combine Card and Servant Priority.

8. [ ] Update the Card pick logic to maximize dmg/np gain
    - e.g. `NP(Servant A)-(Card from A)-(Card from B)` will become `NP(Servant A)-(Card from B)-(Card from A))`

9. [ ] Read less images from card pick logic
    - When 3 NP used. verify NPs can be used and no card checking.
    - When 2 NP used. Find the same one as the higher priority card in the same chain

10. [ ] Need to have full friend list to get the error when sending request with full list.
    
11. [ ] Select what is the wave/turn the script would start. This is now made possible thanks to the fast lazy column

12. [ ] Different scripts per support.

13. [ ] NP Level recognition

14. [ ] Auto Creation of Blue Apples, if available
  
15. [ ] Download Support Servants/CE from another repository. Instead of need to use Support Image Maker. Can just download support files.

Already done:

1. [X] Auto Servant Level
    - Other Servers are supported at Main Repository.

2. [X] Auto Skill Level

3. [X] Auto CE Bomb

4. [X] Auto Append Upgrade
    1. [X] Append 4 and 5 supported

5. [X] Auto Lottery-Gift Box loop
    1. [X] Transition to sell if both present box and servant space are full
       
6. [X] Auto Friend Point Summon to CE Bomb

7. [X] Auto Screenshot of bond level up

8. [X] Auto send friend request

9. [X] Option to return to menu once quest is done.

10. [X] Tea pots but per ~~battle config~~ server settings

11. [X] Recognized Crit stars
    
12. [X] Update the logic of parsing commands in `Skill Maker`.

    Would make the commands be able to know their wave and/or turn order.

13. [X] Append on support selection.
    1. [X] Append 4 and 5 supported

14. [X] Support Image Maker to Compose.

15. [X] Command Spell's Full HP/Full NP on the battle script

