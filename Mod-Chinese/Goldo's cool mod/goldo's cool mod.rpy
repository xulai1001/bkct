init -1 python:

    ## Please don't call your mod 'mymod'. It is a terrible name. ^^

    mymod_template = Mod(

                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "Goldo的MOD模板",
                folder = "Goldo's cool mod",
                creator = "Goldo",
                version = 1.0,
                pic = "title.png",
                description = """Goldo的MOD模板是一个简短的模组制作教程，展示了创建和管理事件的一些基本技巧。激活Mod后，您可以通过访问“帮助”菜单在游戏中测试一些事件。\n\n{b}对于普通玩家来说，安装这个Mod是没有用的。{/b}""",

                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("Surprise me tomorrow", "mymod_add_surprise_event"), ("Meet me at the thieves guild", "mymod_add_meet_event")],

                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "my_mod_init",
                update_label = "my_mod_update",

                ## Event dictionary (all mod events must be declared here)
                events = {
                          "surprise me" : StoryEvent("mymod_surprise"),
                          "meet me" : StoryEvent("mymod_meeting", location = "thieves guild", min_gold = 100),
                          "justice prevails" : StoryEvent("mymod_justice", condition = "mymod_stolen_gold"),
                          },
                home_rightmenu_add_buttons = ["test_mod_but"]*5
                )

## This label runs when the mod is activated
label my_mod_init():

    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
    $ mymod = mymod_template

    "You have just installed [mymod.name]. Don't let the name fool you: It's pretty lame."

    "The dialog you see now is part of the mod 'init' label. This label allows you to set up some variables and events for the mod upon activation."

    "For instance, please tell me the name of your nemesis."

    $ mymod.nemesis = renpy.input("Your nemesis:", default="Evil Bitch")

    mymod.nemesis "Hey, that's not very nice!"

    "I'd also like to know what kind of girls you like."

    # This demonstrates two ways of using variables: storing them with the Mod object (mymod.pic), or passing them on to an event as call_args (end_picture)

    menu:
        "你喜欢哪种发色的女孩？"

        "金发女郎":
            $ mymod.sec_pic = "events/thief (5).webp"
            $ end_picture = "events/thief captured (1).webp"

        "红发女郎":
            $ mymod.sec_pic = "events/thief (6).webp"
            $ end_picture = "events/thief captured (3).webp"

        "蓝发女郎":
            $ mymod.sec_pic = "events/thief (3).webp"
            $ end_picture = "events/thief captured (4).webp"


    "要在游戏中添加事件，请访问Mod选项菜单 [mymod.name]."

    ## Adding this event for later (it won't trigger until its condition is met)

    $ mymod.add_event("justice prevails", type="morning", call_args = [end_picture])

    return

label mymod_add_surprise_event():

    ## This adds a surprise event for tomorrow morning

    $ mymod.add_event("surprise me", type="alarm", delay=1)

    "好吧。准备好明天早上的惊喜吧。"

    return

label mymod_add_meet_event():

    ## This adds an event in the city. It won't trigger until the MC visits the location and conditions are met.

    $ mymod.add_event("meet me", type="city")

    "你收到了一封信。"

    "{i}明天盗贼公会见。记得带钱来。\n我有个有趣的提议给你。相信我，这太好了，不容错过。\n\n[mymod.nemesis]"

    you "嗯,有点意思。"

    return

label mymod_surprise():

    scene black
    show expression brothel.pic at top
    with fade

    play sound s_knocks

    you "我的天..."

    show sewer_monster with dissolve

    play sound s_fizzle

    show sewer_monster at jumping

    you "Haaaa!!!" with vpunch

    "惊喜!"

    return


label mymod_meeting():

    scene black
    show bg thieves_guild at top
    with fade

    you "So, this is the meeting point..."

    hide bg thieves_guild
    show expression mymod.sec_pic at top
    with dissolve

    mymod.nemesis "Hi!"

    play sound s_punch

    you "Hey!" with vpunch

    play sound s_gold

    $ MC.gold -= 100
    $ MC.interactions = 0

    mymod.nemesis "Thanks for the gold, sucker!"

    hide expression mymod.sec_pic
    show bg thieves_guild at top
    with dissolve

    "[mymod.nemesis] has stolen 100 gold from you, and depleted all your actions. Better get some sleep."

    $ mymod.set_condition("mymod_stolen_gold", True) # This is equivalent to '$ my_mod.flags["mymod_stolen_gold"] = True' but hopefully friendlier to non coders

    return

label mymod_justice(end_picture):

    ## This event triggers in the morning if condition is met ("mymod_stolen_gold")

    scene black
    show expression brothel.pic at top
    with fade

    show maya with dissolve

    maya "Hi, citizen."

    maya "I just caught this scoundrel."

    play sound s_surprise

    mymod.nemesis "Aw..."

    maya "Here, I think this is yours."

    play sound s_gold
    $ MC.gold += 100
    $ notify("Gold: " + "+100", pic="img_gold_24", col=c_gold)

    you "Thanks!"

    maya "By the way, she had this on her. Hope you enjoy yourself."

    scene black
    show expression end_picture at top
    with fade

    "This concludes [mymod.full_name]"

    "-剧终-"

    scene black with fade

    return

screen test_mod_but():

    textbutton "测试MOD":

        action Function(renpy.notify, "嘿，你按下了按钮!")
        tooltip "这是功能测试。点击这个按钮没有任何作用。"
