# Fate/Grand Automata

| Stable | Preview |
|---------|---------|
| <a href="https://github.com/Fate-Grand-Automata/FGA/releases" target="_blank"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/Fate-Grand-Automata/FGA?include_prereleases"></a> | [![Preview Build](https://img.shields.io/github/release/ArthurKun21/FGA-Preview-Build.svg?maxAge=3600&label=download)](https://github.com/ArthurKun21/FGA-Preview-Build/releases) |


<a href='https://ko-fi.com/arthurkun21' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## APP

![FGA Preview](https://github.com/user-attachments/assets/890f2031-d7a8-49d1-87dd-3bf54c55e545)

## Scripts

### Auto Level Skills

![Auto Level Skill](https://github.com/user-attachments/assets/8d3810e0-dd60-44c0-813c-a02912890f53)

### Auto Level CE

![Auto Level CE](https://github.com/user-attachments/assets/7b9d452c-2356-43c8-97b4-e71bc6c49bc7)

### Auto Level Append

![Auto Level Append](https://github.com/user-attachments/assets/d70caf20-053b-4dfe-a831-d883049d6b08)

### Improved Support Selection

- Support Appends
- NP Level Detection
- Support for Grand Servant system

![Improved Support Selection](https://github.com/user-attachments/assets/00ec91c8-6d8e-4670-b9e1-ba6e66674f58)

## TODO

Current things being worked on

1. [ ] Migration from hilt to kotlin-inject/metro
  
2. [ ] Migrate Battle Configs from prefs to FGA folder.

     It will be on the `configs` folder. Plan to enable to allow users to create folder for organization.

3. [ ] Migrate from shared preferences to datastore
   
4. [ ] Github Backup and Restore for configs
  
5. [ ] FGA Settings Backup and Restore
  
6. [ ] Config tags and filter tag

     It will make it easy to search for at battle launcher.

7. [ ] Battle History.

Ideas want to work on:

1. [ ] Work on Servant Profiles.
   
2. [ ] Spam V2, it will be based from Servant Profiles to provide better skill usage during spam. It will only take effect once the Command List is empty

3. [ ] On pause, show the remaining commands
   
4. [ ] Use the current storage settings to auto save all of the configs

5. [ ] Integration with Laplace from [Chaldea](https://github.com/chaldea-center/chaldea).

    The Idea is to able to get data from Laplace and then copy paste it into another text box.

6. [ ] Combine Card and Servant Priority.

7. [ ] Update the Card pick logic to maximize dmg/np gain
    - e.g. `NP(Servant A)-(Card from A)-(Card from B)` will become `NP(Servant A)-(Card from B)-(Card from A))`

8. [ ] Read less images from card pick logic
    - When 3 NP used. verify NPs can be used and no card checking.
    - When 2 NP used. Find the same one as the higher priority card in the same chain

9. [ ] Need to have full friend list to get the error when sending request with full list.
    
10. [ ] Select what is the wave/turn the script would start. This is now made possible thanks to the fast lazy column

11. [ ] Different scripts per support.

12. [ ] Auto Creation of Blue Apples, if available
  
13. [ ] Download Support Servants/CE from another repository. Instead of need to use Support Image Maker. Can just download support files.

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
    
16. [X] Probably migrate from DocumentFile to Unifile like Mihon
    
17. [X] Stop on Bond Level Up
    
18. [X] NP Level recognition

19. [X] Grand Servant Support(mostly good)

