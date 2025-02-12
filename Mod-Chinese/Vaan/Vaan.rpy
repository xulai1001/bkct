init -1 python:





    ## Please don't call your mod 'mymod'. It is a terrible name. ^^


    vaan_template = Mod(

                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "Vaan",
                folder = "Vaan",
                creator = "Vaan",
                version = 1.0,
                pic = "title.png",
                description = """A world of sex and adventure awaits!""",

                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("四处转转", "walk_around"), ("购买豪宅/进入豪宅", "buy_house")],

                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
             init_label = "vaan_init",


                ## Event dictionary (all mod events must be declared here)

                events = {

                         "Attack" : StoryEvent("brothel_attack", type="morning", chance=0.2, once=False, date=3),
                         "Attack2" : StoryEvent("brothel_attack", type="night", chance=0.2, once=False, date=3),

                          },
                         #home_rightmenu_add_buttons = ["guild_button"]





                 )











label vaan_init():









    $ vaan_house_built = False
    $ vaan_tavern_built = False
    $ vaan_office_built = False
    $ guild_mission_success = False
    $ guild_mission_failed = False


    default team_1 = None
    default team_2 = None





    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
    $ mymod = vaan_template

    "You have just installed [mymod.name]. Enjoy"


    "To add some events to your game, visit the mod option menu for [mymod.name]."

    ## Adding this event for later (it won't trigger until its condition is met)
return
screen walk_button():


 textbutton "四处转转" action [Hide('mod_menu_display'), Jump("walk_around")] xsize 215 ysize 45


screen guild_button():


 textbutton "购买豪宅"  action [Hide('mod_menu_display'), Jump("buy_house")] xsize 215 ysize 45









label master_bedroom:


 $ girl1, girl2, girl3, girl4 = rand_choice(brothel.master_bedroom.girls, 4)




 if brothel.master_bedroom.level >= 1:

     show expression brothel.master_bedroom.get_pic()

 else:

     "You don't have a master bedroom yet."

     jump main






 if len(brothel.master_bedroom.girls) >= 1:

     "You wake up in the morning, surrounded by the pretty girls that stayed behind."

     python:

         for girl in brothel.master_bedroom.girls:
             if girl.love >= 25 and girl.get_stat("obedience") >= 30:
                 bedroom_pic = girl.get_pic("rest", naked_filter=True, soft=True)
                 renpy.show_screen("show_event", bedroom_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 approach = [girl.name + " is just waking up.","You notice " + girl.name + " still half asleep, moving left and right", girl.name + "is already up and getting dressed", "You also see " + girl.name + ", still sleeping.", "The girls are being woken up by " + girl.name + ", who looks towards you and gives you a wink.", girl.name + " is looking at the ceiling.", "Another girl comes back to bed " + girl.name + ", who looks excited.", "You hear " + girl.name + " shouting your name as she probably went to the bathroom.", "You hear " + girl.name + " talking to one of the other girls in bed.", "While the girls are happily surrounding you " + girl.name + ", is getting up and looks at you with a smile."]

                 add_dialogue("class", ("very extravert"), ("It was a great night!", "Ooooh, time to see what the new day will show.", "So many girls here, it was quite fun!"))
                 add_dialogue("class", ("very introvert"), ("I need to go.", "I will go and have breakfast", "It was good, but i need to go back to my room."))
                 add_dialogue("class", ("very idealist"), ("Oh my god! There are so many people here!", "Let's have a study session after!", "Going to go downstairs."))
                 add_dialogue("class", ("very materialist"), ("Heeey, would you like to get some breakfast after?", "[MC.name], it's so nice sleeping here, your bed is amazing!", "I'm going to sleep for a bit more, you don't mind right? I'm so tireeed!"))
                 add_dialogue("class", ("very lewd"), ("It's so hot, sleeping with so many girls in the same bed.", "I'm going to change, don't peak [MC.name]!" "I'm sure there's more we can learn when there aren't that many people around. Like how to handle your cock!", "My underwear is so sexy, don't you think?"))
                 add_dialogue("class", ("very modest"), ("I hope you enjoyed sleeping with me, i did!", "[MC.name], i am so happy you chose me as one of the girls to sleep here.", "Oh [MC.name], good morning! Hope you slept well."))
                 add_dialogue("class", ("very dom"), ("So many girls around, someone kept pulling the blankets!", "I don't mind sleeping with you and the other girls, as long as they know i'm in charge!", "We should do this again! I enjoyed sleeping with you and all the pretty girls. I might have to teach them to obey me better next time!"))
                 add_dialogue("class", ("very sub"), ("[MC.name], i hope you enjoyed my company.", "[MC.name], can i please go back now, unless you still need me?", "Hey [MC.name], good morning, i'll go and make us some breakfast!"))
                 add_dialogue("class", ("pervert"), ("*giggle* You were totally checking out my butt, weren't you?", "Last night was amazing, look at all the girls here with their big tits and sexy asses, i want to have sex again sometime.", "We should keep going, i'm ready to do it again!"))
                 add_dialogue("class", ("generic", "meek", "loyal", "helper"), ("I treasure the time I spend with you. I love sleeping here!", "I hope i didn't wake you up! Going back to my room soon.", "I love sleeping next to my master, i hope we will make this an every night thing."))
                 add_dialogue("class", ("creep", "yandere"), ("I loved sleeping next to all the hot and sexy bodies.", "Do you want to see my tits? I'll show them to everyone. It's part of my morning routine", "I watched you sleep almost all night!"))
                 add_dialogue("class", ("generic", "nerd", "class president", "tsundere"), ("Your bed was okay, but it could use a few more pillows.", "We need to get a bigger bed if there will be so many girls here each night.", "I have to wash up and go back to work."))

                 renpy.say("",rand_choice(approach))

                 renpy.show_screen("show_event", bedroom_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 girl.say("class")


                 continue

         else:

             "You wake up feeling well rested, the girls have already gone up and went out."




     you "I was thinking, why don't we have some fun before we get up?"
     if len(brothel.master_bedroom.girls) >= 1:

         girl1.char "I think it's a great idea!"

         girl2.char "You should always start your day positively!"


         if girl3.is_("very dom") or girl.is_("dom"):

             girl3.char "I guess so, but you better please me!"

         else:
             girl3.char "I could use some fun before we get out of bed!"


     else:
         girl1.char "Of course, that's what i'm here for!"



     "The girls get up and start taking off their clothes while you watch from bed."



     python:

          for girl in brothel.master_bedroom.girls:

             strip_pic = girl.get_pic("rest", and_tags=["strip"], soft=True)
             renpy.show_screen("show_event", strip_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             approach = [girl.name + " is loving it.","You notice " + girl.name + " giggling while taking her clothes off", girl.name + "is already ahead of everyone and taking her clothes off.", "You watch " + girl.name + ", she is so hot!", "You notice " + girl.name + ", who looks towards you and gives you a wink.", girl.name + " is showing off for you.", "You see " + girl.name + ", who looks excited.", "You hear " + girl.name + " shouting your name as she probably went to the bathroom.", "You hear " + girl.name + " talking to one of the other girls in bed.", "While the girls are happily surrounding you " + girl.name + ", is getting up and looks at you with a smile."]

             renpy.say("",rand_choice(approach))


             renpy.show_screen("show_event", strip_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)








     "The girls are done showing off and have started to come towards you."

     "They take out your cock and start playing with it."


     python:

          for girl in brothel.master_bedroom.girls:
              bedroom_pic = girl.get_pic("rest", and_tags=["oral"], strict=True)
              renpy.show_screen("show_event", bedroom_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
              approach = [girl.name + " is loving it.","You notice " + girl.name + " enjoying herself", girl.name + "is already taking it deep in her mouth", "You watch " + girl.name + ", still watching the other girls.", "Looking on, " + girl.name + ", finally got her turn.", girl.name + " is waiting patiently, she finally got to your cock.", "Another girl comes over " + girl.name + ", who looks excited.", "You hear " + girl.name + " shouting your name as she probably went to the bathroom.", "You hear " + girl.name + " talking to one of the other girls in bed.", "While the girls are happily surrounding you " + girl.name + ", is getting up and looks at you with a smile."]

              add_dialogue("service", ("very extravert"), ("I love it!", "Ooooh, such a great taste.", "So many girls here, this is fun!"))
              add_dialogue("service", ("very introvert"), ("I need to go, too many people here", "I will do it for you.", "I'm so embarassed."))
              add_dialogue("service", ("very idealist"), ("Oh my god! There are so many people here!", "This feels great in my mouth!", "This feels amazing!"))
              add_dialogue("service", ("very materialist"), ("Heeey, would you like to get some breakfast after?", "[MC.name], it's so big! I can hardly fit it in my mouth!", "Hope you buy me something shiny after this!"))
              add_dialogue("service", ("very lewd"), ("I love it when they all watch me suck your cock.", "I love your cock, [MC.name]!", "I've been thinking about your cock all morning!", "Oh my god, i'm going to cum just from sucking it!"))
              add_dialogue("service", ("very modest"), ("I hope you're enjoying it!", "[MC.name], i am so happy you chose me as one of the girls to sleep here.", "Oh [MC.name], this is how you start a morning!"))
              add_dialogue("service", ("very dom"), ("So many girls around, let me have it!", "It's my turn, let me suck it.", "It's so big, i love your cock. I can suck it better than anyone here!"))
              add_dialogue("service", ("very sub"), ("[MC.name], i hope you're enjoying my blowjob.", "[MC.name], i love pleasing you. Give it to me!", "Yes, master. It's my turn now."))
              add_dialogue("service", ("pervert"), ("*giggle* Give me some dick!", "I need your big dick! Hope you cum for me.", "Hope you can handle all of us!"))
              add_dialogue("service", ("generic", "meek", "loyal", "helper"), ("I love sucking your cock. I will show them how to do it!", "Give it to me. I know how to please you best.", "Stop taking his cock away from me, it's all mine!"))
              add_dialogue("service", ("creep", "yandere"), ("I just woke up and i'm already getting something to suck, yay!", "I can service you a hundred times today!", "I want to drain your cum, give it to me."))
              add_dialogue("service", ("generic", "nerd", "class president", "tsundere"), ("I guess i have to do it, let's get this over with. Give it  here.", "I'll show you all how to do it properly. At least you'll learn something from me.", "I have to wash up and go back to work after this."))

              renpy.say("",rand_choice(approach))

              renpy.show_screen("show_event", bedroom_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
              girl.say("service")






     "The girls are doing an amazing job and they help you cum all over them."

     python:

         for girl in brothel.master_bedroom.girls:
             bedroom_pic = girl.get_pic("rest", and_tags=["cumshot"], strict=True)
             renpy.show_screen("show_event", bedroom_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             approach = [girl.name + " is loving it.","You notice " + girl.name + " enjoying herself", girl.name + "is getting showered with your cum", "You watch " + girl.name + ", still watching the other girls.", "Looking on, " + girl.name + ", finally got her turn.", girl.name + " is waiting patiently, she finally got some.", "Another girl comes over " + girl.name + ", who looks excited.", "You hear " + girl.name + " shouting your name as she probably went to the bathroom.", "You hear " + girl.name + " talking to one of the other girls and laughing.", "While the girls are happily surrounding you " + girl.name + ", is getting up and looks at you with a smile."]

             add_dialogue("service", ("very extravert"), ("I love it!", "Ooooh, such a great taste.", "So many girls here, this is fun!"))
             add_dialogue("service", ("very introvert"), ("I need to go, too many people here", "I will do it for you.", "I'm so embarassed."))
             add_dialogue("service", ("very idealist"), ("Oh my god! There are so many people here!", "This feels great, it's so hot!", "This feels amazing!"))
             add_dialogue("service", ("very materialist"), ("Heeey, would you like to get some breakfast after?", "[MC.name], so much cum! It's all over me", "Hope you buy me something shiny after this!"))
             add_dialogue("service", ("very lewd"), ("I love it when they all watch me take it all.", "I love your cock, [MC.name]!", "I want it so much, give it to me, master!", "Oh my god, i'm going to cum just from this!"))
             add_dialogue("service", ("very modest"), ("I hope you enjoyed it!", "[MC.name], i loved pleasing you.", "Oh [MC.name], this is how you start a morning!"))
             add_dialogue("service", ("very dom"), ("So many girls around, let me have it!", "It's my turn, give me your cum.", "It's so big, i love your cum. I can take it better than anyone!"))
             add_dialogue("service", ("very sub"), ("[MC.name], i hope you're enjoying my blowjob.", "[MC.name], i love pleasing you. Give it to me!", "Yes, master. It's my turn now."))
             add_dialogue("service", ("pervert"), ("*giggle* Give me some dick!", "I need your big dick! Hope you cum for me.", "Hope you can handle all of us!"))
             add_dialogue("service", ("generic", "meek", "loyal", "helper"), ("I loved sucking your cock, call me anytime you want to do it again!", "Give it to me. I know how to please you best.", "Give it here, i deserve it!"))
             add_dialogue("service", ("creep", "yandere"), ("I just woke up and i'm already getting my fix, yay!", "I can service you a hundred times today!", "I want to drain your cum, give it to me."))
             add_dialogue("service", ("generic", "nerd", "class president", "tsundere"), ("I guess i have to do it, let's get this over with. Give it  here.", "I'll show you all how to do it properly. At least you'll learn something from me.", "I have to wash up and go back to work after this."))

             renpy.say("",rand_choice(approach))

             renpy.show_screen("show_event", bedroom_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             girl.say("service")
             renpy.hide_screen("show_event")



     jump main



 else:

     "You wake up feeling well rested, time to go back to work."

     jump main











label walk_around:




$ renpy.show_screen("show_img", brothel.pic, _layer = "master")

if MC.interactions <= 1:
     "You've been working too hard and have no energy left, you decide it's too much effort to be walking around and rather stay here."
     jump main






else:
 "It's a boring day, you decide that you want to take some time off from managing the brothel and go for a walk."



 you "Let's take a walk around the brothel and maybe even go around town. I need some time away from work!"

 menu:

    "Date":
     jump date




    "Teach a girl":
     jump teach


    "Study":
     jump study




    "Fuck random girl":
     jump fgirl







## For selecting girl instead of getting them random ##
    "Find a girl":

     "You decide you want to see a specific girl and perhaps do something with her. But there are so many beautiful girls in the brothel, you wonder which one to look for."

     $ girl = long_menu("Choose which girl to summon", [(g.name, g) for g in MC.girls])

     "You decide to go look for [girl.name]. Hoping to find her somewhere around here."
     if len(MC.girls) == 0: # Important to check that there are enough girls in the brothel before attempting this
         "No girls in brothel"

         jump main





     menu:


         "Fuck her": ## For selecting girl instead of getting them random ##

             "You decide you need some release and you head out to find a girl around. There are so many of them, you'd rather just walk around and see who you can find. You see someone standing outside and go to talk to her."

             $ pic = girl.get_pic("profile")

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

             you "[girl.name], how about we go somewhere private and have some fun? Just you and me?"

             if girl.get_stat("libido") <= 60 or girl.love <= 40:

                 girl.char "Just you and me huh? I am sorry [MC.name], but not today. Some other time okay?"

                 you "Whatever, i'll just find someone else"

                 $ girl.change_love(-4)
                 $ girl.change_fear(4)
                 $ MC.interactions -= 2
                 hide screen show_event

                 jump main

             else:

                 girl.char "I would love to, i know just the place, let's go to the basement!"

                 "You reach the basement and you can't hold it anymore, you start taking her clothes off. You fondle her tits and ass, after a bit, you feel her getting wet."

                 play sound s_mmmh


                 $ pic = girl.get_pic("strip", and_tags=["fondle", "grope", "mc"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "That feels amazing, i want to suck your dick!"

                 $ pic = girl.get_pic("service", and_tags=["oral", "mc"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 with fade

                 play sound s_sucking


                 you "Take it deep babe!"

                 $ pic = girl.get_pic("service", and_tags=["deep", "mc"], not_tags=["bisexual", "group"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She hears your instructions and deepthroats your cock, she looks to be enjoying it even more than you!"

                 play sound s_mmmh


                 "After a while she gets up and walks a few steps in front of you! She gives a great look of her ass and pussy, you know what she wants!"


                 $ pic = girl.get_pic("naked", and_tags=["tempt", "mc"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "I want you to fuck me hard, i've been a bad slut!"

                 "You can't take the temptations anymore and put it inside her."

                 $ pic = girl.get_pic("sex", and_tags=["piledriver", "spooning", "mc"], not_tags=["public", "group", "bisexual", "cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 with fade

                 play sound s_moans_quiet

                 girl.char "Just like that, fuck me hard."


                 you "Turn around now slut! Bend over, i want to see that ass"

                 "She takes out your cock and bends over, you put it back in and start fucking her even harder"

                 $ pic = girl.get_pic("sex", and_tags=["doggy", "mc"], not_tags=["public", "group", "bisexual", "cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 with fade

                 play sound s_moans_quiet


                 girl.char "I'm getting close, i'm cumming."

                 $ pic = girl.get_pic("sex", and_tags=["orgasm", "mc"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 girl.char "That was amazing, i came so hard!"

                 you "It's not over yet, slut."

                 "Before she can even react, you put it in her ass. She's surprised at first, but she gets used to it pretty fast."

                 $ pic = girl.get_pic("anal", and_tags=["doggy", "mc"], not_tags=["public", "group", "bisexual", "cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 with fade

                 girl.char "It feels so good, fuck me as hard as you can."


                 you "Get on top, i want to look at you. You can choose where to put it!"


                 $ act = rand_choice(["sex", "anal"])
                 $ pic2 = girl.get_pic(act, and_tags=["cowgirl", "mc"], not_tags=["group", "bisexual", "cumshot"])
                 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 with fade
                 if act == "sex":
                     "She gets on top of you and puts it in her pussy!"

                     girl.char "I love your cock so much, i want to ride it until it cums!"

                     you "Keep going little slut, i'm getting close!"



                     $ pic5 = girl.get_pic("sex", and_tags=["cowgirl", "mc"], not_tags=["group", "bisexual", "cumshot"])

                     show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                     "She rides you even harder and there's only so much you can take, you're close to cumming."

                     $ fix = rand_choice(["inside", "on-body", "on-face", "in-mouth"])

                     if fix == "inside":

                         you "I'll fill your pussy!"


                         $ pic = girl.get_pic("sex", and_tags=["creampie", "inside", "mc"], not_tags=["group", "bisexual"])

                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                         girl.char "It feels so hot inside me!"
                         hide screen show_event
                         show screen home
                         $ girl.change_love(+10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main


                     elif fix == "on-body":

                         "You take it out and cum on her body."

                         girl.char "There's so much cum, all over me!"

                         $ pic = girl.get_pic("cumshot", and_tags=["on-body", "mc"], not_tags=["group", "bisexual"])
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                         "You take your cock out and cum all over her body."

                         girl.char "Wow, that was amazing. I've never been fucked so hard in my life!"
                         with fade
                         hide screen show_event
                         show screen home
                         $ girl.change_love(+10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main


                     elif fix == "on-face":

                         you "On your knees, slut. I'll paint your pretty face!"

                         $ pic = girl.get_pic("cumshot", and_tags=["on-face", "mc"], not_tags=["group", "bisexual"])
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                         with fade
                         hide screen show_event
                         show screen home
                         $ girl.change_love(+10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main



                     elif fix == "in-mouth":

                         you "Open your mouth, i'll feed you my cum!"

                         $ pic = girl.get_pic("cumshot", and_tags=["in-mouth", "mc"], not_tags=["group", "bisexual"])
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                         "She opens her mouth wide and you pour it inside!"

                         girl.char "I love the taste of your cum, [MC.name]. There's so much of it!"

                         with fade

                         hide screen show_event

                         show screen home
                         $ girl.change_love(10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main















                 elif act == "anal":

                     "She gets on top of you and puts it in her ass"

                     girl.char "I love your cock so much, i want to ride it until it cums!"

                     you "Keep going little slut, i'm getting close!"








                     $ pic4 = girl.get_pic("anal", and_tags=["cowgirl", "mc"], not_tags=["group", "bisexual", "cumshot"])

                     show screen show_event(pic4, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                     you "That ass is so tight!"

                     girl.char "I love getting my ass fucked, harder!"

                     play sound s_aah

                     "She rides you even harder and there's only so much you can take, you're close to cumming. Her ass is so tight, you can't hold it any longer!"

                     $ fix = rand_choice(["inside", "on-body", "on-face", "in-mouth"])

                     if fix == "inside":

                         you "I'll fill your ass!"


                         $ pic = girl.get_pic("anal", and_tags=["creampie", "inside", "mc"], not_tags=["group", "bisexual"])

                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                         girl.char "It feels so hot inside me! Cum inside my little asshole!"
                         hide screen show_event
                         show screen home
                         $ girl.change_love(10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main


                     elif fix == "on-body":

                         "You take it out and cum on her body."

                         girl.char "There's so much cum, all over me!"

                         $ pic = girl.get_pic("cumshot", and_tags=["on-body", "mc"], not_tags=["group", "bisexual"])
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                         with fade
                         you "I'm done for now, we can do it again sometime!"

                         girl.char "I'll be waiting!"


                         hide screen show_event
                         show screen home
                         $ girl.change_love(10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main


                     elif fix == "on-face":

                         you "On your knees, slut. I'll paint your pretty face!"

                         $ pic = girl.get_pic("cumshot", and_tags=["on-face", "mc"], not_tags=["group", "bisexual"])
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                         with fade
                         hide screen show_event
                         show screen home
                         $ girl.change_love(10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main



                     elif fix == "in-mouth":

                         you "Open your mouth, i'll feed you my cum!"

                         $ pic = girl.get_pic("cumshot", and_tags=["in-mouth", "mc"], not_tags=["group", "bisexual"])
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                         "She opens her mouth wide and you pour it inside!"

                         girl.char "I love the taste of your cum, [MC.name]. There's so much of it!"

                         with fade

                         hide screen show_event
                         show screen home
                         $ girl.change_love(10)
                         $ girl.change_fear(-10)
                         $ MC.interactions -= 2


                         jump main




         "Model": ## For selecting girl instead of getting them random ##
             "You decide to go downstairs to clear your head. On your way down you can see [girl.name] coming over to you"

             show screen night(girl.profile)

             girl.char "Master, is there anything i can do for you?"

             you "I was thinking, i've seen you wear so many outfits around the brothel, how about we go inside your room and you can show them off to me?"

             if girl.get_stat("libido") <= 85 or girl.fear >= 20 or girl.get_stat("obedience") <= 60:

                 girl.char "Sorry boss, i have work to do, i need to prepare for the night"

                 you "Okay, some other time then, go prepare."

                 show screen home

                 jump main

             elif girl.is_("very dom") or (intensity >= 2 and girl.is_("dom")):

                 girl.char "Fine, but only, because i need a second opinion on some of the outfits!"

             else:
                 girl.char "That's a great idea, let's go to my room and you can tell me which ones you like the best!"

                 you "That's sounds great, let's go!"



             "You go over to the girl's room and she goes behind a wall while you wait for her."

             girl.char "[MC.name], which outfit would you like to see?"

             jump choices



             menu:




                 "Schoolgirl":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("student", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main


                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("student", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("student", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("student", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("student", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("student", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("student", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("student", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main


                 "Teacher":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("teacher", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main

                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("teacher", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("teacher", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("teacher", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("teacher", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("teacher", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("teacher", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("teacher", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main

                 "Nurse":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("nurse", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main


                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("nurse", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("nurse", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("nurse", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("nurse", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("nurse", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("nurse", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("nurse", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main


                 "Santa":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("santa", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main


                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("santa", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("santa", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("santa", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("santa", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("santa", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("santa", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("santa", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main
                 "Bride":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("bride", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main
                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("bride", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("bride", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("bride", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("bride", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("bride", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("bride", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("student", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main
                 "Catgirl":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("catgirl", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main

                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("catgirlt", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("catgirlt", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("catgirlt", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("catgirlt", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("catgirlt", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("catgirlt", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("catgirlt", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main
                 "Maid":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("maid", "apron", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main

                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("maid", "apron", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("maid", "apron", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("maid", "apron", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("maid", "apron", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("maid", "apron", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("maid", "apron", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("maid", "apron", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main








                         "Let me see another outfit":
                             jump choices

                     jump main

                 "Bunnygirl":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("bunny", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                     if not pic:

                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main


                     girl.char "What do you think?"


                     menu:
                        "You look so hot!":
                            girl.char "Thank you, i'm glad you like it."

                            you "How about you show it off a little bit?"
                            with fade

                            "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                            $ pic = girl.get_pic("bunny", and_tags=["tempt", "libido"], not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            girl.char "Do you mean like this?"

                            you "Keep going! You look amazing!"

                            $ pic = girl.get_pic("bunny", and_tags=["strip", "naked", "panties"], not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            girl.char "How about i take off a few layers?"

                            you "Looks like i'm getting the full service here huh?"

                            play sound s_kind_laugh
                            $ pic = girl.get_pic("bunny", and_tags=["naked", "panties"], not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            girl.char "You are my boss after all."

                            you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                            play sound s_kind_laugh

                            girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                            $ pic = girl.get_pic("bunny", and_tags=["sex", "service", "anal", "fetish"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            with fade

                            play sound s_mmmh

                            girl.char "It feels so good, i never want it to end!"



                            $ pic = girl.get_pic("bunny", and_tags=["sex", "service", "anal", "fetish"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            "You keep going harder for a while until you feel you're about to cum."

                            you "I'm cumming, take it little slut!"

                            $ pic = girl.get_pic("bunny", and_tags=["cumshot"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            play sound s_mmmh

                            girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                            play sound s_kind_laugh

                            $ pic = girl.get_pic("bunny", and_tags=["naked"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                            you "Just give it to Sill, she'll take care of it."

                            "You leave the room and go back to work, you leave her to deal with it."


                            $ girl.change_fear(-10)
                            $ girl.change_love(10)
                            hide screen show_event

                            jump main








                        "Let me see another outfit":
                            jump choices

                     jump main
                 "Dress":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("dress", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)



                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main

                     girl.char "What do you think?"


                     menu:
                        "You look so hot!":
                            girl.char "Thank you, i'm glad you like it."

                            you "How about you show it off a little bit?"
                            with fade

                            "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                            $ pic = girl.get_pic("dress", and_tags=["tempt", "libido"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            girl.char "Do you mean like this?"

                            you "Keep going! You look amazing!"

                            $ pic = girl.get_pic("dress", and_tags=["strip", "naked", "panties"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            girl.char "How about i take off a few layers?"

                            you "Looks like i'm getting the full service here huh?"

                            play sound s_kind_laugh
                            $ pic = girl.get_pic("dress", and_tags=["naked", "panties"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            girl.char "You are my boss after all."

                            you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                            play sound s_kind_laugh

                            girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                            $ pic = girl.get_pic("dress", and_tags=["sex", "service", "anal", "fetish"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            with fade

                            play sound s_mmmh

                            girl.char "It feels so good, i never want it to end!"



                            $ pic = girl.get_pic("dress", and_tags=["sex", "service", "anal", "fetish"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                            "You keep going harder for a while until you feel you're about to cum."

                            you "I'm cumming, take it little slut!"

                            $ pic = girl.get_pic("dress", and_tags=["cumshot"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                            play sound s_mmmh

                            girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                            play sound s_kind_laugh

                            $ pic = girl.get_pic("dress", and_tags=["naked"])
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                            you "Just give it to Sill, she'll take care of it."

                            "You leave the room and go back to work, you leave her to deal with it."


                            $ girl.change_fear(-10)
                            $ girl.change_love(10)
                            hide screen show_event

                            jump main








                        "Let me see another outfit":
                            jump choices

                     jump main

                 "Lingerie":

                     "You wait for her to finish and she comes out with the outfit"

                     $ pic = girl.get_pic("lingerie", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)



                     if not pic:
                         girl.char "Sorry, i don't have that one!"

                         you "Ah, i must have seen it on another girl then!"

                         girl.char "Would you like to see my other ones or come back when i have it?"

                         menu:

                            "Check another outfit":
                             jump choices



                            "Let's do it some other time":

                             show screen home

                             jump main

                     girl.char "What do you think?"


                     menu:
                         "You look so hot!":
                             girl.char "Thank you, i'm glad you like it."

                             you "How about you show it off a little bit?"
                             with fade

                             "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                             $ pic = girl.get_pic("lingerie", and_tags=["tempt", "libido"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "Do you mean like this?"

                             you "Keep going! You look amazing!"

                             $ pic = girl.get_pic("lingerie", and_tags=["strip", "naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "How about i take off a few layers?"

                             you "Looks like i'm getting the full service here huh?"

                             play sound s_kind_laugh
                             $ pic = girl.get_pic("lingerie", and_tags=["naked", "panties"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             girl.char "You are my boss after all."

                             you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                             play sound s_kind_laugh

                             girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                             $ pic = girl.get_pic("lingerie", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             with fade

                             play sound s_mmmh

                             girl.char "It feels so good, i never want it to end!"



                             $ pic = girl.get_pic("lingerie", and_tags=["sex", "service", "anal", "fetish"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                             "You keep going harder for a while until you feel you're about to cum."

                             you "I'm cumming, take it little slut!"

                             $ pic = girl.get_pic("lingerie", and_tags=["cumshot"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             play sound s_mmmh

                             girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                             play sound s_kind_laugh

                             $ pic = girl.get_pic("lingerie", and_tags=["naked"])
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                             you "Just give it to Sill, she'll take care of it."

                             "You leave the room and go back to work, you leave her to deal with it."


                             $ girl.change_fear(-10)
                             $ girl.change_love(10)
                             hide screen show_event

                             jump main





                         "Let me see another outfit":
                             jump choices


    "Model":
     jump model



    "Walk around to kill some time":


     $ choice = rand_choice(["1", "2", "3", "4", "5", "6"])

     if choice  == "1":
         jump two_girls


     elif choice  == "2":
         jump follow

     elif choice == "3":

         jump model

     elif choice == "4":

         jump fgirl

     elif choice == "5":
         jump study

     elif choice == "6":
         jump teach



     jump main







    "Fight":
     jump fight

    "Two girls talking":


     jump two_girls



    "Follow the moans you hear from a room nearby":
     jump follow


    "No time to be walking around":

     "You decide to stay in your office and keep working, perhaps you'll go for a walk later."

     jump main

label study:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)
 $ girl1, girl2 = rand_choice(MC.girls, 2)
 $ girl3, girl4 = rand_choice(MC.girls, 2)
 if len(MC.girls) == 0: # Important to check that there are enough girls in the brothel before attempting this
     "No girls in the brothel"
     scene black with fade
     show screen home

 "You decide to try and teach the girls some of the things you know about running the brothel and help them get better at their jobs. You find a room which is big enough to make into a classroom and decide to invite anyone willing to learn, to come over."

 with fade




 image classroom = "mods/vaan/classroom.png"
 show classroom

 "With help of your security guards, you move a few desks around and after a few hours, it's ready! You take your spot at the front and wait to see who comes."

 "After some time, the girls arrive in the classroom one by one and they try to find a seat."

 python:
     girl = MC.girls[5]
     for girl in able_girls:
         if girl.love >= 25 and girl.get_stat("obedience") >= 30:
             student_pic = girl.get_pic("student", naked_filter=True, soft=True)
             renpy.show_screen("show_event", student_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             approach = [girl.name + " comes over, she looks so how in her skirt.","You notice " + girl.name + " rushing towards you, her boobs jugling up and down in her tight schoolgirl uniform.", girl.name + " wishes to speak to you.", "You also see " + girl.name + ", coming over.", "The girls are joined by " + girl.name + ", who looks towards you.", girl.name + " with books in her arms, she is eager to learn.", "Another girl joins the group " + girl.name + ", who looks excited.", "You hear " + girl.name + " shouting your name as she runs up to you.", "You hear " + girl.name + " calling for you loudly, eager to express what's on her mind.", "While the girls are happily surrounding you " + girl.name + ", looks from the distance with an approving smile."]

             add_dialogue("class", ("very extravert"), ("Would you like to study with me!", "I hope my skirt is long enough!", "This class will be amazing!"))
             add_dialogue("class", ("very introvert"), ("I-is this a good time? I was hoping you can help me after class!", "I was wondering if you had some time to show me how this works..."))
             add_dialogue("class", ("very idealist"), ("Oh my god! There are so many people here!", "Let's have a study session after!", "Going to go sit at the back! Can't wait to learn!"))
             add_dialogue("class", ("very materialist"), ("Heeey, would you like to go for coffee after?", "[MC.name], what a nice surprise! This class will help me excel!", "I'm going to sleep for a bit, you don't mind right? I'm so tireeed!"))
             add_dialogue("class", ("very lewd"), ("How do i look? Do you like my skirt? Made it short and will sit at the front, just for you!", "I'm going out with some girls after class, do you want to join? I'm sure there's more we can learn when there aren't that many people around. Like how to handle your cock!", "My uniform is so sexy, don't you think?"))
             add_dialogue("class", ("very modest"), ("I hope you like my uniform, got it to show off to you!", "[MC.name], i am so happy you're going to teach us! Please go easy on the homework!", "Oh [MC.name], i'll sit in the middle, hope i can see from there."))
             add_dialogue("class", ("very dom"), ("Going to sit at the back, not like there's much more i can learn. I already know everything!", "What do you think of my schoolgirl uniform? It's sexy isn't it? I bet you wish you can do all kinds of things to me? Stick around after class and i might just let you, haha!", "If this gets boring, i'll leave!"))
             add_dialogue("class", ("very sub"), ("[MC.name], i'm so embarassed, i think my skirt is too revealing, i hope i can learn a lot from you!", "[MC.name], i will follow your instructions!", "Hey [MC.name], it's really good to see you, i will obey your every command and will do my homework!"))
             add_dialogue("class", ("pervert"), ("*giggle* You were totally checking out my butt, weren't you?", "I've been waiting for this! I had a fantasy of getting fucked by my teacher!", "Hope you'll give me detention after class and stay around to really teach me a lesson, haha!"))
             add_dialogue("class", ("generic", "meek", "loyal", "helper"), ("I treasure the time I spend with you. This class will be amazing!", "I will listen and learn from you, will also tell the other girls to keep quiet if they interrupt you!", "I did my homework from last time, anything for you!", "I can stay behind after class and help you if you need anything!"))
             add_dialogue("class", ("creep", "yandere"), ("I hope you punish me after class! I've been a bad girl.", "Care to make me strip in front of the class and spank me? I never learn my lesson!", "Are you going to send me to the principal's office after class? I could really use a good punishment, if you know what i mean haha."))
             add_dialogue("class", ("generic", "nerd", "class president", "tsundere"), ("I'm hear to learn and nothing more!", "Finally, a better way to spend my time, learning about the world, thank you for this [MC.name]!", "I love learning new things, thanks for the invite! I hope the other girls are quiet and don't interrupt!"))

             renpy.say("",rand_choice(approach))

             renpy.show_screen("show_event", student_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             girl.say("class")

             student_pic = None
             continue


 "You start the lesson and you teach girls about life inside and outside of the brothel. You share your experiences and thoughts, and you hope you get through to them."


 with fade

 "Half way through your class you notice two of the girls not paying attention and talking to each other."


 you "[girl1.name], [girl2.name], if i'm boring you, you are welcome to leave!"

 if girl1 or girl2.is_("very dom") or (intensity >= 2 and girl.is_("dom")):

     girl1.char "Like i care, what are you going to do, punish us?"

     girl2.char "Yes, we were talking about something important!"
 else:

     girl.char "I'm sorry boss, we were discussing something."

     gir2.char "We feel like, we already know most of this."


 you "I'm going to punish you both, step in front of the class."
 with dissolve


 "The girls go in front of the class and wait for your command."

 you "Take your clothes off and bend over, i'm going to punish you."

 $ pic = girl1.get_pic("strip", and_tags=["student", "public"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic:
     $ pic = girl1.get_pic("strip", and_tags=["student"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "They both start stripping and bend over, waiting to see what happens next, as the rest of the class looks on."

 play sound s_aah


 $ pic = girl2.get_pic("strip", and_tags=["student", "public"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic:
     $ pic = girl2.get_pic("strip", and_tags=["student"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 you "Good, now the whole class can see you! Hope you feel ashamed for not listening!"




 if girl1 or girl2.is_("very dom") or (intensity >= 2 and girl.is_("dom")):

     girl1.char "What, you just want a reason to touch us, you pervert!"

     girl2.char "You've been trying to see under our skirts all day, we saw you looking!"

 elif girl1.get_stat("libido") >= 60 or girl2.get_stat("libido") >= 60:
     girl.char "Looks like our plan worked."

     gir2.char "I can't wait to get a spanking in front of everyone."


 else:

     girl.char "Might as well get this over with."

     girl2.char "Oh no, not again..."





 "You have a look at their asses and then start spanking them in front of the class!"

 play sound s_aah

 $ pic = girl1.get_pic("fetish", and_tags=["spanking", "student", "public"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic:
     $ pic = girl1.get_pic("fetish", and_tags=["spanking", "student"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     if not pic:
         $ pic = girl1.get_pic("fetish", and_tags=["spanking", "student"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



 girl1.char "It hurts, everyone is looking!"

 girl3.char "Wow, he's really doing it! This is so hot."


 girl4.char "I didn't think he would actually do it, embarassing!"

 play sound s_aah


 $ pic = girl2.get_pic("fetish", and_tags=["spanking", "student", "public"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic:
     $ pic = girl2.get_pic("fetish", and_tags=["spanking", "student"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     if not pic:
         $ pic = girl2.get_pic("fetish", and_tags=["spanking", "student"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




 you "Both your asses are red. Now apologise and go back!"


 girl1.char "We're sorry!"

 girl2.char "Yes, we'll pay attention from now on."

 you "Good, see me after class!"

 girl.char "Haha, you know what that means, you'll get a special kind of punishment."

 girl4.char "I wish that was me, haha!"





 "After class, everyone leaves and the two girls stay behind."


 $ pic2 = girl1.get_pic("student", strict=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))

 girl1.char "What do you need from us?"

 you "You will soon find out."

 $ pic2 = girl2.get_pic("student", strict=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))

 girl2.char "Let me guess, you want to punish us some more?"

 you "That's exactly what i'm going to do!"

 you "Take of your clothes!"

 $ pic = girl1.get_pic("strip", and_tags=["student", "public"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic:
     $ pic = girl1.get_pic("strip", and_tags=["student"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "They both start stripping again, they know what's going to happen and look ready for it."

 play sound s_mmmh


 $ pic = girl2.get_pic("strip", and_tags=["student", "public"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic:
     $ pic = girl2.get_pic("strip", and_tags=["student"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl1.char "Where do you want to start from?"

 girl2.char "What do you want to do with us?"

 $ pic = girl2.get_pic("naked", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 with dissolve

 you "You look so hot, i can't wait to take you on my desk!"

 girl1.char "We're already naked, let's do it!"


 $ pic = girl1.get_pic("naked", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



 you "Get on your knees and suck it!"

 "Both of them are ready to serve, they get on their knees and take your cock out!"

 $ pic = girl2.get_pic("service", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 with dissolve

 girl2.char "I'm starting to get wet!"
 girl1.char "From being punished? Slut!"


 $ pic = girl1.get_pic("service", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl1.char "This isn't such a bad punishment."

 girl2.char "I'm enjoying it, please punish us more, teacher!"


 you "Get on the desk, i want to fuck you!"

 girl1.char "My pussy is so wet, i want it!"


 $ pic = girl2.get_pic("sex", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 with dissolve


 $ pic = girl1.get_pic("sex", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl2.char "Keep fucking us, [MC.name]. I love it!"

 girl1.char "Punish us, teacher!"


 you "Bend over, i'll fuck your asses now!"

 with fade
 $ pic = girl2.get_pic("anal", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 with dissolve

 "You thrust it deep inside [girl2.name]'s ass!"

 play sound s_mmmh

 girl2.char "I love it!"

 girl1.char "What a slut! You deserve the punishment for talking so much during class!"

 you "Your turn now, [girl1.name]!"

 $ pic = girl1.get_pic("anal", and_tags=["student"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 with dissolve

 girl1.char "Yes, push it in, give it to me!"

 girl2.char "Not talking tough now bitch, are you? Fuck her ass harder, teacher!"


 you "I'm going to cum!"

 menu:
     "Cum inside pussy":

         you "Take it in, sluts!"

         $ pic = girl1.get_pic("sex", and_tags=["inside", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl1.get_pic("sex", and_tags=["creampie", "student"], strict=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl1.get_pic("sex", and_tags=["creampie", "inside"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




         girl1.char "So deep, i love it!"

         $ pic = girl2.get_pic("sex", and_tags=["inside", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl2.get_pic("sex", and_tags=["creampie", "student"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl2.get_pic("sex", and_tags=["creampie", "inside"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         girl2.char "My pussy is full!"
         "You all dress up and leave after, the girls have learned their lesson."

     "Cum inside ass":

         you "I'll fill your tight assholes!"
         $ pic = girl1.get_pic("anal", and_tags=["inside", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl1.get_pic("anal", and_tags=["creampie", "student"], strict=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl1.get_pic("anal", and_tags=["creampie", "inside"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         girl1.char "So deep inside my ass, i love it!"






         $ pic = girl2.get_pic("anal", and_tags=["inside", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl2.get_pic("anal", and_tags=["creampie", "student"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl2.get_pic("anal", and_tags=["creampie", "inside"], strict=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         girl2.char "My ass is full!"

         "You all dress up and leave after, the girls have learned their lesson."


     "Cum on face":
         you "I'll cum on your pretty faces!"
         $ pic = girl1.get_pic("cumshot", and_tags=["on-face", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl1.get_pic("cumshot", and_tags=["on-face", "student"], strict=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl1.get_pic("cumshot", and_tags=["on-face"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         girl1.char "Yes, [MC.name], paint my face!"




         $ pic = girl2.get_pic("cumshot", and_tags=["on-face", "student"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl2.get_pic("cumshot", and_tags=["on-face", "student"], strict=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl2.get_pic("cumshot", and_tags=["on-face"], strict=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         girl2.char "Yes, [MC.name], give it to me too!"

         "You all dress up and leave after, the girls have learned their lesson."



     "Cum in mouth":

         you "Open your mouths, sluts! I'll feed it to you!"
         $ pic = girl1.get_pic("cumshot", and_tags=["in-mouth", "student"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl1.get_pic("cumshot", and_tags=["in-mouth", "student"], strict=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl1.get_pic("cumshot", and_tags=["in-mouth"], strict=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         $ pic = girl2.get_pic("cumshot", and_tags=["in-mouth", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl2.get_pic("cumshot", and_tags=["on-face", "student"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl2.get_pic("cumshot", and_tags=["in-mouth"], strict=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



     "Cum on body":
         you "You're not getting it inside you today, this is your final punishment. I'll cum outside!"

         you "Open your mouths, sluts! I'll feed it to you!"
         $ pic = girl1.get_pic("cumshot", and_tags=["on-body", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl1.get_pic("cumshot", and_tags=["in-mouth", "student"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl1.get_pic("cumshot", and_tags=["on-body"], strict=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         $ pic = girl2.get_pic("cumshot", and_tags=["on-body", "student"], strict=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         if not pic:
             $ pic = girl2.get_pic("cumshot", and_tags=["on-body", "student"], strict=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:
                 $ pic = girl2.get_pic("cumshot", and_tags=["on-body"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         with dissolve














 $ girl1.change_love(10)
 $ girl1.change_fear(-14)
 $ girl.change_love(10)
 $ girl.change_fear(-14)

 $ girl2.change_love(10)
 $ girl2.change_fear(-14)

 $ girl3.change_love(10)
 $ girl3.change_fear(-14)

 $ girl4.change_love(10)
 $ girl4.change_fear(-14)

 $ MC.interactions -= 2
 hide screen show_event


 jump main











label two_girls:



      $ girl1, girl2 = rand_choice(MC.girls, 2)
      $ pic = girl2.get_pic
      $ rel = girl1.get_friendship(girl2)
      $ pic1 = girl1.get_pic

      $ rel = girl1.get_friendship(girl2)

      if len(MC.girls) <= 2: # Important to check that there are enough girls in the brothel before attempting this
          "No friends in the group"
          scene black with fade
          show screen home










      if girl1.love, girl2.love >= 50:


          show screen night(girl1.profile)

          girl1.char "Hey [MC.name], [girl2.name] and I have recently become close friends and we were wondering if we could expand our friendship by getting someone to have sex with us. Would you like to join us?"

          show screen night(girl2.profile)
          girl2.char "We've been very lonely, would you like to join us?"
          menu:


             "Not right now":
                  girl1.char "I guess, we'll just have to take care of each other!"
                  girl2.char "Hopefully master will join us next time! I'll go get my toys."
                  "Walking past their rooms, i can hear them play with each other."
                  play sound s_moans_quiet
                  jump main




             "Let's do it":

              MC.char "Both of you bend over, i'll fuck you deep and make you my whores"

              show screen show_event(girl1.get_pic("sex", and_tags=["doggy", "mc"], not_tags=["cumshot", "group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))

              girl1.char "Fuck me master, oh, i love it!"
              girl2.char "That's it, make her scream like a slut, my turn now, you had your fun!"

              MC.char "[girl2.name] bend over slut, i'll give it to you next."

              girl2.char "Put it in [MC.name], i can't wait anymore!"

              show screen show_event(girl2.get_pic("sex", and_tags=["doggy", "mc"], not_tags=["cumshot", "group"]), x=config.screen_width, y=int(config.screen_height*0.8))

              girl1.char "She's a real pro, give her your cum master!"
              MC.char "I'm getting close, take it!"

              show screen show_event(girl1.get_pic("sex", and_tags=["cumshot", "mc"], not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))
              girl1.char "Oh god, yes! It's filling me up!"

              girl2.char "My turn, my turn! I want master's cum!"
              with dissolve
              show screen show_event(girl2.get_pic("sex", and_tags=["cumshot", "mc"], not_tags=["bisexual", "group"]), x=config.screen_width, y=int(config.screen_height*0.8))

              girl2.char "That was amazing!"
              $ girl1.change_mood(+2)
              $ girl2.change_mood(+2)
              $ girl1.change_love(+2)
              $ girl1.change_fear(-10)
              $ girl2.change_fear(-10)
              $ MC.interactions -= 2


              hide screen show_event

              jump main

      else:


          "No Friends in group."

          jump main



label follow:
$ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
$ girl = rand_choice(able_girls)


"You see one of the girls touching herself and looking like she needs release! She sees you and comes over to talk to you"
show screen night(girl.profile)

girl.char "[MC.name], i was wondering if you can summon one of the mosters from the farm with one of your spells if possible? I need some release!"



menu:





 "Summon tentacle monster":

     you "There's a new monster that i've been trying to train and use, you will be the perfect test subject for it."

     "She looks a bit nervous."

     girl.char "What kind of monster is it? I don't want it to hurt me or be too rough."

     you "You wanted to play, so now you have to do it!"



     if girl.get_stat("obedience") < 80:

          girl.char "No way, i'm leaving. I don't want some random monster to use me like a toy. I'm not a test subject. It might even kill me!"
          "She leaves before you can say anything."
          $ girl.change_stat("obedience", -10)
          $ girl.change_love(-8)
          $ girl.change_fear(5)
          $ MC.interactions -= 2





     else:
         girl.char "Okay, we can give it a go, but promise me it won't hurt me!"

         you "It won't but it might get a bit carried away, it's a monster created specifically for sex and nothing else. It's a tenticle monster!"

         girl.char "A tenticle monster? I've heard of those before, they are quite rapey!"

         you "They are, but i have gotten this one under control, although i doubt it will stop if you ask it to."

         girl.char "It's fine, let's give it a try, i always wanted to know what one feels like!"



         "You take the girl to the basement and decide to try the summon tenticle monster spell. You draw a circle and and say the incantation, you both see a bright light and lightning come out of the circle."

         play sound s_lightning

         "Before you know it, a tentacle monster appears and it's already ready to do what it does best. Use it's tentactles on any girl it can find."

         girl.char "I'm ready, take me!"



         "The monster tears her clothes and wraps it's tentacles around her."

         play sound s_scream

         $ pic = girl.get_pic
         show screen show_event(girl.get_pic("tentacles",   and_tags=["strip", "naked"], not_tags=["bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))

         "The monster gropes the girl and doesn't let her go."

         $ pic = girl.get_pic
         show screen show_event(girl.get_pic("tentacles",   and_tags=["fondle", "finger", "grope", "bondage"], not_tags=["bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))

         play sound s_scream

         "As the girl screams the monster is ready to finally get inside her, it reaches inside all her holes and starts fucking her"

         $ pic = girl.get_pic
         show screen show_event(girl.get_pic("tentacles",   and_tags=["sex", "anal", "service", "fetish"], not_tags=["bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))
         with fade

         "[girl.name] looks scared at first, not knowing what to expect, but then slowly starts to get used to it. You're taking notes of it's behavior and try to command it while it's doing that"

         you "That's a good boy, make sure you don't hurt her now, she needs to go back to work after."

         play sound s_roar

         "It get out a roar to show you it understands and will obey your command. Looks like it's far from finished with her though as it's starts fucking her even harder!"

         $ pic = girl.get_pic
         show screen show_event(girl.get_pic("tentacles",   and_tags=["sex", "anal", "service", "fetish"], not_tags=["bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))

         girl.char "Not sure how much more of this i can handle, it's cumming!"

         play sound s_aah


         $ pic = girl.get_pic
         show screen show_event(girl.get_pic("tentacles",   and_tags=["cumshot"], not_tags=["bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))

         $ girl.change_energy(-30)

         "The monster cums inside her and all over her body, but it looks like this is far from over! You're starting to worry that it might fuck her until it kills her, so you ask [girl.name] if she wants to end it."

         you "[girl.name], it looks like it's not finished yet, do you want me to stop it or should we go on?"


     if girl.energy >= 50 and girl.get_stat("libido") >= 100:

         girl.char "Please...keep...fucking me, i don't...want this...to ever end."

         "She can barely talk after the monster had it's way with her, but you understand what she's trying to say."

         you "Get on with it, tear that slut apart!"

         play sound s_roar

         show screen show_event(girl.get_pic("tentacles",   and_tags=["group", "sex"], not_tags=["bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))

         "The monster starts fucking her again and it keeps getting faster and faster"

         play sound s_aah

         girl.char "Don't stop fucking me, use me like your sex toy!"
         with fade

         show screen show_event(girl.get_pic("tentacles", not_tags=["bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))

         "The monster keeps going and it looks like it's close to cumming, just on time too, the girl looks like she's about to pass out!"

         you "I think it's about to cum, fuck that slut, fill her in!"

         girl.char "It's coming...i can feel it!"
         with fade

         play sound s_roar

         show screen show_event(girl.get_pic("tentacles", and_tags=["cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))
         with fade

         "The monster goes back to where it came from and all that's left is the girl in a pool of cum"

         with dissolve

         show screen show_event(girl.get_pic("naked", and_tags=["monster", "tentacles", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))

         girl.char "It was...amazing!"

         "You grab her and you take her to her room."
         with fade

         show screen show_event(girl.get_pic("rest", and_tags=["naked", "hurt"]), x=config.screen_width, y=int(config.screen_height*0.8))


         you "You might want to take a shower later, and change your bed sheets!"


         girl.char "Yes...master."

         you "Look at you, you can barely even talk. That monster gave you the fucking of a lifetime, you're such a filthy whore"

         girl.char "Yes...master...i'm a...filthy...whore. Need...sleep."

         "You close the door and go about your day, leaving her in the room"


         $ girl.change_fear(-13)
         $ MC.interactions -= 2
         $ girl.change_love(13)


         hide screen show_event
         jump main

     else:
         play sound scream



         girl.char "Please...make...it...stop"

         show screen show_event(girl.get_pic("tentacles",   and_tags=["hurt"], not_tags=["bisexual", "cumshot"]), x=config.screen_width, y=int(config.screen_height*0.8))

         "The girl can barely talk, you wonder if she will even be able to work today. You send the monster back and it drops [girl.name] on the floor . Her entire body is covered in cum and it's also leaking out of every hole in her body. She looks at you with her last bit of energy left."

         show screen show_event(girl.get_pic("naked",   and_tags=["cumshower", "hurt"], not_tags=["bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))

         girl.char "It...was...too...much. Everything hurts, i...won't be able...to stand...for days."

         "You pick her up and take her upstairs."

         show screen show_event(girl.get_pic("rest",   and_tags=["hurt"]]), x=config.screen_width, y=int(config.screen_height*0.8))

         "It might take a few days until she feels better."

         you "You can take a few days off until you feel better, it looked exhausting. I'll check on you every now and then, to see if you're feeling better. Get some rest"


         if girl.love >= 50:
             girl.char "Thank you, [MC.name]."




         if girl.love <= 50:
             girl.char "I hate you...how could you...let it rape me!"
             "You close the door and get on with your work"
             $ girl.get_hurt(1+dice(4))

             $ girl.change_stat("obedience", -10)
             $ girl.fear(10)
             $ MC.interactions -= 2
             $ girl.love(-10)
             hide screen show_event

             show screen home
             jump main



 "I don't have time right now":

     "You tell her you don't have enough time and that she needs to find her own way of pleasing herself. You remind her that she is not allowed to have sex with anyone outside of the girls and you, unless she asks!"


     "She looks angry, but agrees and goes back to her room. After a while you walk by and hear her playing with her sex toys"


     play sound s_mmmh


     "You open the door and see her playing with her pussy and talking to herself."
     $ pic = girl.get_pic
     show screen show_event(girl.get_pic("rest",   and_tags=["masturbate", "toys"], not_tags=["bisexual", "group", "lesbian"]), x=config.screen_width, y=int(config.screen_height*0.8))


     girl.char "Yes [MC.name], please fuck me with that big cock of yours. I'll be a good girl from now on."

     $ pic = girl.get_pic
     show screen show_event(girl.get_pic("rest",   and_tags=["masturbate", "toys", "orgasm"], not_tags=["bisexual", "group", "lesbian"]), x=config.screen_width, y=int(config.screen_height*0.8))
     girl.char "I'm cumming, it feels so good!!! I've been waiting for this all day!"
     play sound s_moans_quiet
     "You close the door and leave her. It was a nice show!"
     $ girl.change_stat("obedience", 10)
     $ girl.change_love(8)
     $ MC.interactions -= 2


     hide screen show_event

     jump main











 "Sure (summon a normal monster)":

     "You use some of your power to bring out a monster for the girl to have fun with"

     MC.char "Obey the girl's command and let her use you as she sees fit!"

     girl.char "Thank you master! Now then, let me play with that big cock!"
     $ pic1 = girl.get_pic
     show screen show_event(girl.get_pic("dom",   and_tags=["monster", "beast", "big cock"], not_tags=["cumshot", "group"]), x=config.screen_width, y=int(config.screen_height*0.8))
     with fade
     show screen show_event(girl.get_pic("sex", "service", "anal",    and_tags=["monster", "beast", "big cock"], not_tags=["cumshot", "group"]), x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     girl.char "I can feel you're about to cum. Do it, give me all that monster cum"
     show screen show_event(girl.get_pic("cumshot",   and_tags=["monster", "beast", "big cock"], not_tags=["bisexual", "group"]), x=config.screen_width, y=int(config.screen_height*0.8))
     with fade
     girl.char "I needed that"
     MC.char "It's not over yet slut! You made me horny watching you fuck that thing, so now, you'll have to take care of me too!"

     "You lift the girl from the ground and you bend her over, then you start fucking her pussy."
     show screen show_event(girl.get_pic("sex",    and_tags=["doggy", "sub"], not_tags=["cumshot", "group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     girl.char "It feels good master, please keep fucking me!"
     show screen show_event(girl.get_pic("sex",    and_tags=["doggy", "sub"], not_tags=["cumshot", "group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))
     with fade
     MC.char "I'm about to cum! Take it all!"
     show screen show_event(girl.get_pic("cumshot",    and_tags=["sex", "doggy"], not_tags=["group", "bisexual"]), x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     girl.char "Thank you master, happy to please you!"
     $girl.change_love(4)
     $girl.change_fear(-10)
     $ MC.interactions -= 2


     scene black with fade

     hide screen show_event

     jump main









label model:

 $ MC.interactions -= 2
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)

 "You decide to go downstairs to clear your head. On your way down you can see [girl.name] coming over to you"

 show screen night(girl.profile)

 girl.char "Master, is there anything i can do for you?"

 you "I was thinking, i've seen you wear so many outfits around the brothel, how about we go inside your room and you can show them off to me?"

 if girl.get_stat("libido") <= 85 or girl.fear >= 20 or girl.get_stat("obedience") <= 60:

     girl.char "Sorry boss, i have work to do, i need to prepare for the night"

     you "Okay, some other time then, go prepare."

     show screen home

     jump main

 elif girl.is_("very dom") or (intensity >= 2 and girl.is_("dom")):

     girl.char "Fine, but only, because i need a second opinion on some of the outfits!"

 else:
     girl.char "That's a great idea, let's go to my room and you can tell me which ones you like the best!"

     you "That's sounds great, let's go!"



 "You go over to the girl's room and she goes behind a wall while you wait for her."

 girl.char "[MC.name], which outfit would you like to see?"

 jump choices

 label choices:

 menu:




     "Schoolgirl":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("student", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main


         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("student", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("student", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("student", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("student", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("student", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("student", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("student", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main


     "Teacher":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("teacher", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main

         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("teacher", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("teacher", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("teacher", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("teacher", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("teacher", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("teacher", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("teacher", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main

     "Nurse":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("nurse", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main


         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("nurse", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("nurse", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("nurse", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("nurse", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("nurse", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("nurse", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("nurse", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main


     "Santa":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("santa", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main


         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("santa", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("santa", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("santa", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("santa", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("santa", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("santa", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("santa", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main
     "Bride":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("bride", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main
         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("bride", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("bride", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("bride", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("bride", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("bride", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("bride", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("student", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main
     "Catgirl":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("catgirl", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main

         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("catgirlt", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("catgirlt", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("catgirlt", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("catgirlt", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("catgirlt", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("catgirlt", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("catgirlt", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main
     "Maid":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("maid", "apron", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main

         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("maid", "apron", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("maid", "apron", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("maid", "apron", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("maid", "apron", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("maid", "apron", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("maid", "apron", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("maid", "apron", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main








             "Let me see another outfit":
                 jump choices

         jump main

     "Bunnygirl":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("bunny", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

         if not pic:

             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main


         girl.char "What do you think?"


         menu:
            "You look so hot!":
                girl.char "Thank you, i'm glad you like it."

                you "How about you show it off a little bit?"
                with fade

                "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                $ pic = girl.get_pic("bunny", and_tags=["tempt", "libido"], not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "Do you mean like this?"

                you "Keep going! You look amazing!"

                $ pic = girl.get_pic("bunny", and_tags=["strip", "naked", "panties"], not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "How about i take off a few layers?"

                you "Looks like i'm getting the full service here huh?"

                play sound s_kind_laugh
                $ pic = girl.get_pic("bunny", and_tags=["naked", "panties"], not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "You are my boss after all."

                you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                play sound s_kind_laugh

                girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                $ pic = girl.get_pic("bunny", and_tags=["sex", "service", "anal", "fetish"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with fade

                play sound s_mmmh

                girl.char "It feels so good, i never want it to end!"



                $ pic = girl.get_pic("bunny", and_tags=["sex", "service", "anal", "fetish"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                "You keep going harder for a while until you feel you're about to cum."

                you "I'm cumming, take it little slut!"

                $ pic = girl.get_pic("bunny", and_tags=["cumshot"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                play sound s_mmmh

                girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                play sound s_kind_laugh

                $ pic = girl.get_pic("bunny", and_tags=["naked"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                you "Just give it to Sill, she'll take care of it."

                "You leave the room and go back to work, you leave her to deal with it."


                $ girl.change_fear(-10)
                $ girl.change_love(10)
                hide screen show_event

                jump main








            "Let me see another outfit":
                jump choices

         jump main
     "Dress":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("dress", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)



         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main

         girl.char "What do you think?"


         menu:
            "You look so hot!":
                girl.char "Thank you, i'm glad you like it."

                you "How about you show it off a little bit?"
                with fade

                "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                $ pic = girl.get_pic("dress", and_tags=["tempt", "libido"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "Do you mean like this?"

                you "Keep going! You look amazing!"

                $ pic = girl.get_pic("dress", and_tags=["strip", "naked", "panties"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "How about i take off a few layers?"

                you "Looks like i'm getting the full service here huh?"

                play sound s_kind_laugh
                $ pic = girl.get_pic("dress", and_tags=["naked", "panties"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                girl.char "You are my boss after all."

                you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                play sound s_kind_laugh

                girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                $ pic = girl.get_pic("dress", and_tags=["sex", "service", "anal", "fetish"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                with fade

                play sound s_mmmh

                girl.char "It feels so good, i never want it to end!"



                $ pic = girl.get_pic("dress", and_tags=["sex", "service", "anal", "fetish"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                "You keep going harder for a while until you feel you're about to cum."

                you "I'm cumming, take it little slut!"

                $ pic = girl.get_pic("dress", and_tags=["cumshot"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                play sound s_mmmh

                girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                play sound s_kind_laugh

                $ pic = girl.get_pic("dress", and_tags=["naked"])
                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)




                you "Just give it to Sill, she'll take care of it."

                "You leave the room and go back to work, you leave her to deal with it."


                $ girl.change_fear(-10)
                $ girl.change_love(10)
                hide screen show_event

                jump main








            "Let me see another outfit":
                jump choices

         jump main

     "Lingerie":

         "You wait for her to finish and she comes out with the outfit"

         $ pic = girl.get_pic("lingerie", not_tags=["service", "sex", "anal", "fetish", "group", "bisexual"])
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)



         if not pic:
             girl.char "Sorry, i don't have that one!"

             you "Ah, i must have seen it on another girl then!"

             girl.char "Would you like to see my other ones or come back when i have it?"

             menu:

                "Check another outfit":
                 jump choices



                "Let's do it some other time":

                 show screen home

                 jump main

         girl.char "What do you think?"


         menu:
             "You look so hot!":
                 girl.char "Thank you, i'm glad you like it."

                 you "How about you show it off a little bit?"
                 with fade

                 "[girl.name] doesn't wait for you to ask a second time and stars walking around and dancing in her outfit/"

                 $ pic = girl.get_pic("lingerie", and_tags=["tempt", "libido"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "Do you mean like this?"

                 you "Keep going! You look amazing!"

                 $ pic = girl.get_pic("lingerie", and_tags=["strip", "naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "How about i take off a few layers?"

                 you "Looks like i'm getting the full service here huh?"

                 play sound s_kind_laugh
                 $ pic = girl.get_pic("lingerie", and_tags=["naked", "panties"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 girl.char "You are my boss after all."

                 you "You made me go hard down there with your sexy outfits, how about you take care of it?"

                 play sound s_kind_laugh

                 girl.char "I thought you'd never ask. Let's do it. Let's have some fun!"

                 $ pic = girl.get_pic("lingerie", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 with fade

                 play sound s_mmmh

                 girl.char "It feels so good, i never want it to end!"



                 $ pic = girl.get_pic("lingerie", and_tags=["sex", "service", "anal", "fetish"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                 "You keep going harder for a while until you feel you're about to cum."

                 you "I'm cumming, take it little slut!"

                 $ pic = girl.get_pic("lingerie", and_tags=["cumshot"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 play sound s_mmmh

                 girl.char "That felt so good, but i'll need to clean my outfit now, because you made a mess out of it!"
                 play sound s_kind_laugh

                 $ pic = girl.get_pic("lingerie", and_tags=["naked"])
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
                 you "Just give it to Sill, she'll take care of it."

                 "You leave the room and go back to work, you leave her to deal with it."


                 $ girl.change_fear(-10)
                 $ girl.change_love(10)
                 hide screen show_event

                 jump main





             "Let me see another outfit":
                 jump choices
label fgirl:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)
 "You decide you need some release and you head out to find a girl around. There are so many of them, you'd rather just walk around and see who you can find. You see someone standing outside and go to talk to her."
 $ pic = girl.get_pic("profile")

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 you "[girl.name], how about we go somewhere private and have some fun? Just you and me?"

 if girl.get_stat("libido") <= 60 or girl.love <= 40:

     girl.char "Just you and me huh? I am sorry [MC.name], but not today. Some other time okay?"

     you "Whatever, i'll just find someone else"

     "You need at least 60 libido and 40 love"

     $ girl.change_love(-4)
     $ girl.change_fear(4)
     $ MC.interactions -= 2
     hide screen show_event

     jump main

 else:

     girl.char "I would love to, i know just the place, let's go to the basement!"

     "You reach the basement and you can't hold it anymore, you start taking her clothes off. You fondle her tits and ass, after a bit, you feel her getting wet."

     play sound s_mmmh


     $ pic = girl.get_pic("strip", and_tags=["fondle", "grope", "mc"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     girl.char "That feels amazing, i want to suck your dick!"

     $ pic = girl.get_pic("service", and_tags=["oral", "mc"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     play sound s_sucking


     you "Take it deep babe!"

     $ pic = girl.get_pic("service", and_tags=["deep", "mc"], not_tags=["bisexual", "group"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "She hears your instructions and deepthroats your cock, she looks to be enjoying it even more than you!"

     play sound s_mmmh


     "After a while she gets up and walks a few steps in front of you! She gives a great look of her ass and pussy, you know what she wants!"


     $ pic = girl.get_pic("naked", and_tags=["tempt", "mc"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     girl.char "I want you to fuck me hard, i've been a bad slut!"

     "You can't take the temptations anymore and put it inside her."

     $ pic = girl.get_pic("sex", and_tags=["piledriver", "spooning", "mc"], not_tags=["public", "group", "bisexual", "cumshot"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     play sound s_moans_quiet

     girl.char "Just like that, fuck me hard."


     you "Turn around now slut! Bend over, i want to see that ass"

     "She takes out your cock and bends over, you put it back in and start fucking her even harder"

     $ pic = girl.get_pic("sex", and_tags=["doggy", "mc"], not_tags=["public", "group", "bisexual", "cumshot"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     play sound s_moans_quiet


     girl.char "I'm getting close, i'm cumming."

     $ pic = girl.get_pic("sex", and_tags=["orgasm", "mc"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl.char "That was amazing, i came so hard!"

     you "It's not over yet, slut."

     "Before she can even react, you put it in her ass. She's surprised at first, but she gets used to it pretty fast."

     $ pic = girl.get_pic("anal", and_tags=["doggy", "mc"], not_tags=["public", "group", "bisexual", "cumshot"])
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     with fade

     girl.char "It feels so good, fuck me as hard as you can."


     you "Get on top, i want to look at you. You can choose where to put it!"


     $ act = rand_choice(["sex", "anal"])
     $ pic2 = girl.get_pic(act, and_tags=["cowgirl", "mc"], not_tags=["group", "bisexual", "cumshot"])
     show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     with fade
     if act == "sex":
         "She gets on top of you and puts it in her pussy!"

         girl.char "I love your cock so much, i want to ride it until it cums!"

         you "Keep going little slut, i'm getting close!"



         $ pic5 = girl.get_pic("sex", and_tags=["cowgirl", "mc"], not_tags=["group", "bisexual", "cumshot"])

         show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

         "She rides you even harder and there's only so much you can take, you're close to cumming."

         $ fix = rand_choice(["inside", "on-body", "on-face", "in-mouth"])

         if fix == "inside":

             you "I'll fill your pussy!"


             $ pic = girl.get_pic("sex", and_tags=["creampie", "inside", "mc"], not_tags=["group", "bisexual"])

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

             girl.char "It feels so hot inside me!"
             hide screen show_event
             show screen home
             $ girl.change_love(+10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main


         elif fix == "on-body":

             "You take it out and cum on her body."

             girl.char "There's so much cum, all over me!"

             $ pic = girl.get_pic("cumshot", and_tags=["on-body", "mc"], not_tags=["group", "bisexual"])
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

             "You take your cock out and cum all over her body."

             girl.char "Wow, that was amazing. I've never been fucked so hard in my life!"
             with fade
             hide screen show_event
             show screen home
             $ girl.change_love(+10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main


         elif fix == "on-face":

             you "On your knees, slut. I'll paint your pretty face!"

             $ pic = girl.get_pic("cumshot", and_tags=["on-face", "mc"], not_tags=["group", "bisexual"])
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             with fade
             hide screen show_event
             show screen home
             $ girl.change_love(+10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main



         elif fix == "in-mouth":

             you "Open your mouth, i'll feed you my cum!"

             $ pic = girl.get_pic("cumshot", and_tags=["in-mouth", "mc"], not_tags=["group", "bisexual"])
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

             "She opens her mouth wide and you pour it inside!"

             girl.char "I love the taste of your cum, [MC.name]. There's so much of it!"

             with fade

             hide screen show_event

             show screen home
             $ girl.change_love(10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main















     elif act == "anal":

         "She gets on top of you and puts it in her ass"

         girl.char "I love your cock so much, i want to ride it until it cums!"

         you "Keep going little slut, i'm getting close!"








         $ pic4 = girl.get_pic("anal", and_tags=["cowgirl", "mc"], not_tags=["group", "bisexual", "cumshot"])

         show screen show_event(pic4, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

         you "That ass is so tight!"

         girl.char "I love getting my ass fucked, harder!"

         play sound s_aah

         "She rides you even harder and there's only so much you can take, you're close to cumming. Her ass is so tight, you can't hold it any longer!"

         $ fix = rand_choice(["inside", "on-body", "on-face", "in-mouth"])

         if fix == "inside":

             you "I'll fill your ass!"


             $ pic = girl.get_pic("anal", and_tags=["creampie", "inside", "mc"], not_tags=["group", "bisexual"])

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

             girl.char "It feels so hot inside me! Cum inside my little asshole!"
             hide screen show_event
             show screen home
             $ girl.change_love(10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main


         elif fix == "on-body":

             "You take it out and cum on her body."

             girl.char "There's so much cum, all over me!"

             $ pic = girl.get_pic("cumshot", and_tags=["on-body", "mc"], not_tags=["group", "bisexual"])
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             with fade
             you "I'm done for now, we can do it again sometime!"

             girl.char "I'll be waiting!"


             hide screen show_event
             show screen home
             $ girl.change_love(10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main


         elif fix == "on-face":

             you "On your knees, slut. I'll paint your pretty face!"

             $ pic = girl.get_pic("cumshot", and_tags=["on-face", "mc"], not_tags=["group", "bisexual"])
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
             with fade
             hide screen show_event
             show screen home
             $ girl.change_love(10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main



         elif fix == "in-mouth":

             you "Open your mouth, i'll feed you my cum!"

             $ pic = girl.get_pic("cumshot", and_tags=["in-mouth", "mc"], not_tags=["group", "bisexual"])
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

             "She opens her mouth wide and you pour it inside!"

             girl.char "I love the taste of your cum, [MC.name]. There's so much of it!"

             with fade

             hide screen show_event
             show screen home
             $ girl.change_love(10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2


             jump main








label teach:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)

 "You hear a knock on the door, you're surprised to see [girl.name]."

 $ pic = girl.get_pic("student", not_tags=["public", "sex", "service", "anal"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl.char "[MC.name], i was wondering if i could get some extra sessions? I feel like i could learn so much more from training with you? Better than having to go to classes outside of the brothel."

 you "Of course [girl.name], i will see you at the class room in 10 mins."

 girl.char "Thank you, i'll go get my books!"

 with fade

 image classroom = "mods/vaan/classroom.png"
 show classroom

 "You make your way to the classroom and soon, the girl appears, ready to take the class."

 $ pic2 = girl.get_pic("student", not_tags=["public", "sex", "service", "anal"], strict=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))

 you "Nice to see you [girl.name], let's begin."

 "She takes a seat at the front desk and you begin your lecture on different subjects and live experiences."


 hide screen show_event

 "After an hour you give her an exam and leave her to do it."

 $ pic2 = girl.get_pic("student", and_tags=["study"], not_tags=["public", "sex", "service", "anal"], strict=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))
 if not pic2:
     $ pic2 = girl.get_pic("study", strict=True)
     show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))



 "You sit on your chair while the girl is concentrating on doing the exam, you see her writing and while you wait, you drift off, thinking about what to do after."


 "You fall asleep while waiting for her to finish without realising it."


 hide screen show_event

 "You get woken up by someone playing with your cock and you realise it's [girl.name]."


 $ pic = girl.get_pic("student", and_tags=["service"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl.char "Sorry to wake you up, boss! I finished my exam and was waiting for you to wake up."

 girl.char "I thought that it will be good for me to get a more *hands on* experience while i waited."

 play sound s_kind_laugh

 you "That's a great idea, [girl.name]. Let's see if you learned anything from our lesson."

 with fade

 $ pic = girl.get_pic("student", and_tags=["service"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "The girl starts sucking your cock with a smile on her face, she is determined to show you what she's learned!"

 you "This feels good, but how about we do something else? Take off your clothes and bend over for me."

 girl.char "Of course, master. Let's have some fun!"

 $ pic = girl.get_pic("student", and_tags=["strip"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "She slowly takes her uniform off and it looks like she's already ready to go!"



 girl.char "I'm ready for you, please teach me even more!"

 $ pic = girl.get_pic("student", and_tags=["tempt", "naked"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



 you "That's a good girl, looks like you'll get an A+ for this class. Bend over for me."


 $ pic = girl.get_pic("sex", and_tags=["doggy", "student", "teacher"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "You bend her over and put your dick inside her. She's enjoying it a lot and can hardly control herself."

 play sound s_mmmh

 girl.char "Let me get on top, i have to work for that A+ after all!"

 with fade

 $ pic = girl.get_pic("sex", and_tags=["cowgirl", "student", "teacher"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "She gets on top of you and enjoys riding you, you can see she's trying hard to please you."

 you "That's a good student, i think you're already ahead of of everyone else!"


 girl.char "I'm so happy! I wanted to show you how much i pay attention to your classes!"


 $ pic = girl.get_pic("sex", and_tags=["piledriver", "student", "teacher"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You keep going back and forth with her around the classroom, you hope one the other girls doesn't come in and see you. You're meant to be teaching in this classroom after all!"

 girl.char "This is the best exam i've ever had! I wish all the exams were like this! The only you gave me before that was quite hard! I wasn't sure i would pass, but now i have a feeling i will, haha!"

 play sound s_mmmh

 you "You will definitely pass, i don't even need to see your test to know you've given all the right answers!"

 play sound s_kind_laugh

 with fade


 $ pic = girl.get_pic("sex", and_tags=["spooning", "student", "teacher"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You turn around the girl again and keep fucking her, you've been going at it for a while and you'll soon cum."


 girl.char "Yes, [MC.name], give it to me! I've been wanting it since the moment i entered the classroom!"


 $ fix = rand_choice(["inside", "on-body"])



 if fix == "inside":
     $ pic = girl.get_pic("cumshot", and_tags=["student", "sex", "inside", "creampie"], not_tags=["group", "bisexual"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     you "Cumming, I want to cum inside that schoolgirl pussy!"


     girl.char "Yes, give it to me, master! Deep inside!"

     play sound s_mmmh



     girl.char "There's so much of it inside me!"
     you "That's what happens when you're wearing that schoolgirl uniform, you're so hot, babe!"
     girl.char "Thank you, master. I'll try to wear it outside of class too!"
     $ MC.interactions -= 2
     $ girl.change_fear(-10)
     $ girl.change_love(10)

     hide screen show_event

     jump main









 if fix == "on-body":
     $ pic5 = girl.get_pic("cumshot", and_tags=["student", "on-body", "on-face", "in-mouth"], not_tags=["group", "bisexual"], soft=True)
     show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8))


     you "Get on your knees, i'm going to shower you with cum!"


     girl.char "Yes, give it to me, [MC.name]! I want it all over me!"

     play sound s_mmmh



     girl.char "There's so much of it, you must have been thinking about me a lot too!"
     you "That's what happens when you're wearing that schoolgirl skirt, you're so hot, babe!"
     girl.char "Thank you, master. I'll get an even shorter one next time! Haha"
     $ MC.interactions -= 2
     $ girl.change_fear(-10)
     $ girl.change_love(10)
     hide screen show_event

     jump main









 $ pic5 = girl.get_pic("naked", and_tags=["student", "cumshot"], not_tags=["group", "bisexual"], soft=True)
 show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8))
 girl.char "I hope i passed your exam now!"

 you "You sure did, but make sure you come back for extra lessons when you can. There's a lot more i can teach you!"

 girl.char "I definitely will, need to go take a shower now! I will see you later!"

 you "See you later, [girl.name]!"

 hide screen show_event

 jump main








label brothel_attack:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)
 $ target_girls = MC.girls

 if len(able_girls) <=4:

     return



 python:
     attackers = rand_choice(("marauding ogres", "gooey monsters", "rogue mercenaries"))
     if attackers == "gooey monsters" and is_censored("monster"):
         attackers = "rogue mercenaries"

     pic1 = "events/" + rand_choice(security_pics["brothel defense"])
     pic2 = "events/" + rand_choice(security_pics[attackers])

     target_girls = rand_choice(target_girls, 1 + dice(3)) #how many girls get attacked
     kidnap_target = rand_choice(target_girls)
     girl_nb = len(target_girls)

     defended_girls = []
     hurt_girls = []
     kidnapped_girls = []

 show expression pic1 at top as bg with dissolve

 play sound s_crowd_riot

 security "{color=[c_red]}[brothel.name] is being raided by [attackers]!{/color}\nYou rush outside with the defenders."

 play sound s_clash
 pause 0.2
 play sound2 s_clash

 security "Your first assault breaks their line and they quickly scatter. That's when you hear a scream."

 play sound s_woman_scream
 ev_girl1 "EEEEK!" with vpunch

 hide bg
 show expression bg_bro at top
 with dissolve

 security "Some of the attackers have sneaked out the back of [brothel.name] while the security guards were distracted! You rush back to the brothel to help.\n{color=[c_red]}[girl_nb] of your girls are under attack, but you can only help one!{/color}"

 python:
     menu_list = [["Choose a girl to defend", None]]

     for girl in target_girls:
         menu_list.append([girl.fullname.capitalize() + ", Level " + str(girl.level) + ", Defense " + str_int(girl.get_defense()), girl])

 $ girl = menu(menu_list)

 python:
     for g in target_girls:
         if girl == g:
             g.love += 5
         else:
             g.love -= 5

 hide bg_bro
 $ renpy.show_screen("show_event", girl.profile, x=config.screen_width, y=int(config.screen_height*0.8), _layer = "master")

 with dissolve

 play sound s_scream_loud
 girl.char "EEEEK!!! [MC.name], i need some help over here!" with vpunch

 if attackers == "marauding ogres":
     $ strength = 12
     $ magic = 6
     $ hit = "the handle of his giant axe"
     show ogre at totheleft as enemy with dissolve

 elif attackers == "gooey monsters":
     $ strength = 9
     $ magic = 11
     $ hit = "a whipping tentacle"
     show sewer_monster as enemy at truecenter with dissolve

 elif attackers == "rogue mercenaries":
     $ strength = 10
     $ magic = 10
     $ hit = "the flat of his sword"
     show masked_thug at totheleft as enemy with dissolve

 "You reach [girl.fullname] just in time to confront her attacker."

 if attackers == "marauding ogres":
     show ogre at left as enemy with move

 elif attackers == "gooey monsters":
     show sewer_monster as enemy at centerleft with move

 elif attackers == "rogue mercenaries":
     show masked_thug at left as enemy with move

 # Pick challenge
 $ tt = show_tt("top_right")
 $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight", "fight", strength), ("Fire a spell", "cast", magic)])
 hide screen tool

 if chal == "fight":
     $ renpy.block_rollback()

     play sound s_sheath

     call challenge(chal, strength) from _call_challenge_80 # result is stored in the _return variable
     $ r = _return

     if r:
         play sound s_sheath

         with vpunch

         play sound2 s_crash

         hide enemy with pixellate

         "With righteous fury, you cut down your opponent before he has a chance to react.\n{color=[c_green]}[girl.name] is safe.{/color}"

     else:
         play sound s_punch

         with vpunch

         "Your opponent strikes the air out of you with a mighty blow from [hit]. You are sent flying backwards. Your head hits something hard."


 elif chal == "cast":
     $ renpy.block_rollback()

     play sound s_spell

     call challenge(chal, magic) from _call_challenge_81 # result is stored in the _return variable
     $ r = _return

     if r:
         play sound s_lightning
         with flash

         if attackers == "rogue mercenaries":
             show thug2 burnt as enemy with move:
                 xalign 0.4
                 time 0.5

         hide enemy with pixellate

         "The assailant is pulverized by a mighty bolt of lightning from your staff. {color=[c_green]}[girl.name] is safe.{/color}"

     else:
         play sound s_fizzle

         "As you try to cast a spell, you realize too late your opponent is protected by a magic ward. He hits you hard with [hit], sending you crumbling on the floor."

         play sound s_punch
         with vpunch

 if r:

     $ target_girls.remove(girl)
     $ defended_girls.append(girl)

     $ text1 = "While you were fighting, the other attackers rampaged through your brothel. "

 else:
     if girl.test_shield():
         play sound s_spell
         $ sec_pic = "events/" + rand_choice(security_pics["girl shield"])

         hide screen show_event
         show screen show_event(Picture(path=sec_pic), x=config.screen_width, y=int(config.screen_height*0.8))
         with dissolve

         "[girl.fullname] is left alone, but her magic shield blinded her attacker and protected her from harm."

         $ target_girls.remove(girl)
         $ defended_girls.append(girl)

     elif girl.get_defense() + dice(6) >= strength:
         play sound s_sheath

         python:
             sec_pic = girl.get_pic("fight", strict=True, naked_filter=True, soft=True)
             if not sec_pic:
                 sec_pic = girl.get_pic("fight", strict=True)
                 if not sec_pic:
                     sec_pic = Picture(path="events/" + rand_choice(security_pics["default girl fight"]))

         hide screen show_event
         scene black with fade
         show screen show_event(sec_pic, x=config.screen_width, y=int(config.screen_height*0.8))
         with dissolve

         "[girl.fullname] is left to fend alone for herself, but she is far from defenseless. Attacking from behind while your opponent is busy pummeling you, she stabs him in the back repeatedly, and he runs away squealing."

         girl.char "Take that you filthy animal! I warned you not come near me!"

         $ target_girls.remove(girl)
         $ defended_girls.append(girl)

     else:
         play sound s_woman_scream

         python:
             sec_pic = girl.get_pic("hurt", not_tags=["rest"], naked_filter=True, soft=True, strict=True)
             if not sec_pic:
                 sec_pic = girl.get_pic("hurt", not_tags=["rest"], strict=True)
                 if not sec_pic:
                     sec_pic = Picture(path="events/" + rand_choice(security_pics["assassin"]))

         hide screen show_event
         scene black with fade
         show screen show_event(sec_pic, x=config.screen_width, y=int(config.screen_height*0.8))
         with dissolve

         "[girl.fullname] is left to fend alone for herself. She tries to grab a stick for defense, but her opponent swipes it away effortlessly."

         girl.char "Nooo!!!" with vpunch

     $ lost_gold = int(MC.gold * 0.15)
     $ MC.gold -= lost_gold
     $ text1 = "While you were passed out, the [attackers] ransacked your brothel, {color=[c_red]}taking off with [lost_gold] gold.{/color} "




 python:

     for girl in target_girls:
         if girl.test_shield():
             defended_girls.append(girl)
         elif girl.get_defense() + dice(6) >= strength + dice(6):
             defended_girls.append(girl)
         elif girl == kidnap_target:
             kidnapped_girls.append(girl)
             MC.girls.remove(girl)
             game.kidnapped.append(girl)
             girl.kidnapper = attackers
#                    text2 += "\n{color=[c_red]}" + girl.fullname + " has been kidnapped!{/color}"
             girl.track_event("dirty", arg = attackers + ".")
         else:
             girl.get_hurt(1+dice(4))
             if girl.hurt > 0:
                 hurt_girls.append(girl)
                 girl.track_event("hurt", arg = attackers + ".")


     if len(defended_girls) > 1:
         text1 += and_text([g.fullname for g in defended_girls]) + " defended themselves. {color=[c_red]}"
     elif len(defended_girls) > 0:
         text1 += defended_girls[0].fullname + " defended herself. {color=[c_red]}"

     if len(hurt_girls) > 1:
         text1 += and_text([g.fullname for g in defended_girls]) + " were hurt.\n"

     elif len(hurt_girls) > 0:
         text1 += hurt_girls[0].fullname + " was hurt.\n"


     if kidnapped_girls:
         text1 += "{b}" + kidnapped_girls[0].fullname + " was kidnapped!{/b}"

         if attackers == "rogue mercenaries":

             calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues", type = "night"))

         if attackers == "marauding ogres":
             calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts", type = "night"))


         if attackers == "gooey monsters":
             calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters", type = "night"))



 hide screen show_event
 scene black

 if hurt_girls:
     show expression pic2 at top
 else:
     show expression pic1 at top
 with fade

 if kidnapped_girls or hurt_girls:
     $ renpy.say(security_breach, text1)
 else:
     $ renpy.say(security, text1)

 $ brothel.alert_level = 1
 $ brothel.threat = 0

 jump main


label kidnapped_rogues:


 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return

 "[girl1.name] was taken to the hideout of the bandits."

 play sound s_scream

 with fade


 $ pic = girl1.get_pic("dirty")

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 thug1 "Stop screaming or i'll give you something to really scream about!"


 girl1.char "What do you want from me? Leave me alone!"


 thug2 "You'll be a good little slut for us and you'll do everything we tell you to or else!"

 if girl1.fear <= -19:

     girl1.char "Go to hell! [MC.name] will be here soon and you'll all be sorry!"


     play sound s_crowd_laugh


     thug3 "By the time he gets here, there won't be much of you to save! Now take your clothes off!"



     girl1.char "Not going to happen!"


     play sound s_punch


     $ pic = girl1.get_pic("dirty", and_tags=["hurt"], not_tags=["service", "sex", "anal"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_scream


     thug3 "You do what we tell you to, or you won't survive the night!"


     "The girl takes her clothes off afraid of what might happen if she didn't obey."

     $ pic = girl1.get_pic("dirty", and_tags=["strip"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_crowd_cheer


     thug1 "That's more like it, looking good!"


 else:

     girl1.char "Go to hell! I won't let you touch me!"


     play sound s_crowd_laugh


     thug3 "You'll learn to obey one way or the other! We'll train you to be our pet!"



     girl1.char "Not going to happen!"


     play sound s_punch


     $ pic = girl1.get_pic("hurt", not_tags=["service", "sex"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_scream


     thug3 "You do what we tell you to, or you won't survive the night!"


     "The girl takes her clothes off afraid of what might happen if she didn't obey."

     $ pic = girl1.get_pic("strip", and_tags=["sub"], not_tags=["service", "sex"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_crowd_cheer


     thug1 "That's more like it, looking good!"

     with fade


 thug2 "In the next few days you will be trained to obey and service every single bandit in our group. When we're done with you, you'll be nothing but a good cum dump for us, just like the other girls!"
 $ pic = girl1.get_pic("naked", strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 thug2 "Now go back to your cell!"

 with fade

 $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 $renpy.pause()


 "The girl is a bit relieved that they didn't go further, but couldn't stop and wonder what will happen to her tomorrow!"
 $ girl1.change_fear(10)
 $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues2", type = "night"))
 jump main

 label kidnapped_rogues2:

 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return

 "Another day has passed and [girl1.name] has been taken out by the bandits. Her fate looks bleak."

 $ pic = girl1.get_pic("dirty")

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 thug1 "Undress, it's time to have some fun with you."


 if girl1.fear <= 0:

     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(10)


     jump main


 else:

     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please, let me go home!"

     thug1 "Hahaha, like that would ever happen, you will be trained with the rest of these girls and once you're ready, you'll meet the boss!"

     thug2 "Now, let's beging your training, learn to serve slut!"

     "They bring her to her knees and she starts sucking them off."

     $ pic = girl1.get_pic("dirty", and_tags=["service"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "She's a natural, gather around boys, she's very good!"

     girl1.char "I hate you all!"

     $ pic = girl1.get_pic("dirty", and_tags=["service", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "After a few hours, they're done with her and bring her back to her room."

     thug1 "That was good, let's go out and find some more.!"




     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     $ girl1.change_fear(+7)


     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues3", type = "night"))

     jump main




 label kidnapped_rogues3:

  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been taken out by the bandits. She is not aware of what will happen to her today, but is very scared."

  $ pic = girl1.get_pic("dirty")

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  thug1 "Undress, it's time to have some fun with you."


  if girl1.fear <= 0:

     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main


  else:

     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please, let me go home!"

     thug1 "Hahaha, we have something special for you today, it's time you learned to take some cocks."

     thug2 "Enough talk, spread your legs slut, i've been waiting for this for quite some time now!"

     "The girl tries to fight back and screams but there are too many of them, they pin her to the floor as she slowly gives up."

     $ pic = girl1.get_pic("dirty", and_tags=["sex"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That feels so good, i've been waiting for this for some time now."

     girl1.char "Let me go!"

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug2 "Shut up you slut, you're done when we say you are! Every single one of our guys will take you today!"

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["sex"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "That's a good girl, it will be over soon."

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That felt amazing, who's next boys?"



     thug2 "It's my turn now, had an exhausting day, need some relief."

     "After a few hours, they're done with her and bring her back to her room."

     thug1 "That was good, let's get some food, after that, bring out one of the other whores!"


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she can barely breathe."

     girl1.char "There were so many...i don't want to live anymore."



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues4", type = "night"))
     $ girl1.change_fear(+7)

     jump main





 label kidnapped_rogues4:
    $ girl1 = rand_choice(kidnapped_girls)
    if girl1 not in game.kidnapped:
        return


    "Another day has passed and [girl1.name] has been dragged out by the bandits. She is silent and doesn't speak to them."

    $ pic = girl1.get_pic("dirty")

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

    thug1 "Undress, it's time to have some fun with you. You still need plenty of training"


    if girl1.fear <= 0:

     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     thug1 "I'll have to punish you for dissobeying me. Send her to the dungeon for punishment."

     hide screen show_event

     $ girl1.change_fear(+10)


     jump main




    else:

     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "..."

     thug1 "Hahaha, we have something special for you today, it's time you learned to take some cocks in that nice ass of yours."

     thug2 "She's not in a talking mood today, she's learning."

     "The girl tries to fight back and screams but there are too many of them, they pin her to the floor as she slowly gives up."

     $ pic = girl1.get_pic("dirty", and_tags=["anal"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That feels so good, i've been waiting for this for some time now."

     girl1.char "I hate you."

     "She starts crying, which turns on the bandits even more, they keep taking turns on her while they laugh and humiliate her."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug2 "Shut up you slut, you're done when we say you are! Every single one of our guys will take you today!"

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["anal"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "That's a good girl, it will be over soon."

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That felt amazing, who's next boys?"



     thug2 "Her asshole is so tight, it will make me cum fast. I'll come back later for seconds, hahaha."

     "After a few hours, they're done with her and bring her back to her room."

     thug1 "That was good, let's get some food, after that, bring out one of the other whores!"


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, her asshole is leaking cum and it hurts so much she can barely walk."

     girl1.char "There were so many...i don't want to live anymore. It hurts."

     $ girl1.change_fear(+7)

     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues5", type = "night"))

     jump main

 label kidnapped_rogues5:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been dragged out by the bandits. She is acting a bit different today, like she has given up hope."

 $ pic = girl1.get_pic("dirty", "sub")

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 thug1 "Undress, it's time to have some fun with you. You still need plenty of training"


 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     thug1 "I'll have to punish you for dissobeying me. Send her to the dungeon for punishment."

     hide screen show_event

     $ girl1.change_fear(+10)


     jump main






 else:
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, i understand,"

     thug1 "Hahaha, what a good and obedient girl you're becoming, we'll soon be able to introduce you to the boss and then he can decide if you're ready for the ceremony."
     girl.char "Ceremony?"

     thug3 "All in due time girl."

     thug2 "Get down, time to service the men"

     "She goes on her knees and begins her new daily routine."

     $ pic = girl1.get_pic("dirty", and_tags=["service", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That feels so good, i've been waiting for this for some time now."

     girl1.char "Please, one at a time."

     "The girl is taking on each cock one after the other."

     $ pic = girl1.get_pic("dirty", and_tags=["servce", "sub", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug2 "That's a good girl, you're learning, just like the others. You're nothing more but our cumsluts."

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["service", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "That's a good girl, it will be over soon."

     "The girl is waiting for all of them to finish one by one, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["service", "sub" "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That felt amazing, who's next boys?"



     thug2 "Her mouth is so good, she's a real cocksucker, the boss will be happy with what we've done."

     "After a few hours, they're done with her and bring her back to her room."

     thug1 "She is nearly ready."


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, her asshole is leaking cum and it hurts so much she can barely walk."

     girl1.char "There were so many...i don't want to live anymore. It hurts."

     $ girl1.change_fear(+7)

     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues6", type = "night"))

     jump main


 label kidnapped_rogues6:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen."

 $ pic = girl1.get_pic("dirty", and_tags=["sub"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 thug1 "Undress, it's time to have some fun with you."


 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, please use me any way you want."

     thug1 "Hahaha, any way we want? Just a few days ago you were asking us to leave you alone."

     thug2 "Do you want us to fuck you now, slut?"

     girl.char "Yes, please use me."

     "The girl gets ready to receive their cocks while the bandits laugh."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That feels so good, i've been waiting for this for some time now."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug2 "Good, learn your place."

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "That's a good girl, it will be over soon."

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That felt amazing, who's next boys?"



     thug2 "It's my turn now, had an exhausting day, need some relief."

     "After a few hours, they're done with her and bring her back to her room."

     thug1 "That was good, let's get some food, after that, bring out one of the other whores!"


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

     girl1.char "Why didn't i fight back...am i getting used to be treated like a common whore. Someone, help."



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues7", type = "night"))
     $ girl1.change_fear(+7)

     jump main





 label kidnapped_rogues7:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen."

 $ pic = girl1.get_pic("dirty", and_tags=["sub"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 thug1 "Undress, it's time to have some fun with you."


 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, please use me any way you want."

     thug1 "Hahaha, any way we want? Just a few days ago you were asking us to leave you alone."

     thug2 "Do you want us to fuck you now, slut?"

     girl.char "Yes, please use me."

     "The girl gets ready to receive their cocks while the bandits laugh."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That feels so good, i've been waiting for this for some time now."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug2 "Good, learn your place."

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "That's a good girl, it will be over soon."

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug1 "That felt amazing, who's next boys?"



     thug2 "It's my turn now, had an exhausting day, need some relief."

     "After a few hours, they're done with her and bring her back to her room."

     thug1 "That was good, She is ready, let's present her to the boss tomorrow!"




     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

     girl1.char "The boss? Who is he? Is he the reason why this has happened to me?"



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues8", type = "night"))
     $ girl1.change_fear(+7)

     jump main

 label kidnapped_rogues8:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen. Or at least she did, she forgot today is the day she meets their boss"

 $ pic = girl1.get_pic("dirty", and_tags=["ceremony"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 mthug "We finally meet girl, this is where your initiation begins."

 girl1.char "Initiation?"

 mthug "This is where i decide whether you're worth keeping and if you are, you will participate in an orgy with the rest of the girls we have."

 girl.char "That's ridiculous and if i decide not to *participate*?"

 mthug "You will be returned to my men for training."

 mthug "The goal of the ceremony is simple, to get you pregnant, your children will be used as soldiers or help around camp."

 mthug "So, what will it be? If you choose yes, then i will become your new master, you will do as i tell you or be punished."




 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "strip"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, please use me any way you want, master."

     mthug "Hahaha, any way i want? That's what i call obedience!"

     mthug "Get ready to serve me slut, first i want you to suck it."

     girl1.char "Yes, please use me, master."

     "The girl gets on her knees and tries to please."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "service"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     mthug "That feels so good, i've been waiting for this for some time now."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "service", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     mthug "Good, you've passed the first step, next, i want your pussy."

     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "sex"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     mthug "That's a good girl, i can see my man have trained you properly."

     "The girl is obediently taking his cock and moaning, she looks like she wants more."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "sex", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     mthug "That felt amazing, now for the final stage, let's see how tight your asshole is."

     "She gets in position and is prepare to take yet another cock into her asshole, she's done it so many times, she doesn't think much of it."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "anal"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     mthug "Good slut, here it comes."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "anal", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "He cums inside each of her holes and when it all done the girl can barely talk."


     mthug "You did good, i'm glad to say you've passed, get ready for the initiation tomorrow, you and the rest of these girls will take every men's cock, all at the same time."

     mthug "If you manage to do it, you will become one of us and will be further bred every signle day until you become pregnant. If not, you will be put back in the cage and be trained like the animal you are."

     girl1.char "Yes, master."

     "With that she is taken back to her room to rest."


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

     girl1.char "An orgy? Every man will fill all my holes, i will probably even become pregnant, for some reason i no longer feel afraid. I am starting to feel excited."



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_rogues9", type = "night"))
     $ girl1.change_fear(+7)

     jump main

 label kidnapped_rogues9:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "The day has finally come, [girl.name] is taken out of her cell and is taken to a huge hall filled with men and women."

 mthug "The time has finally come for the inititation, my brothers, these are the girls i've chosen for this initiation. You are welcome to try any number of them you want."

 mthug "It's time to celebrate, go and indulge yourselves, you deserve it! There's plenty of whores for everyone, you don't need to ask, just go and take whoever you want and make the slut yours!"

 play sound s_crowd_cheer

 $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "strip"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "The girl looks around and can see all the bandits already grabbing girls and forcing them to the ground to fuck."

 $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "fondle"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "At the same time a lot of them are already around her and touching her any way they want."




 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     thug1 "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     thug2 "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "service"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please, be gentle."

     thug1 "Less talking, more sucking!"

     thug2 "Get ready to serve me slut, first i want you to suck it."

     girl1.char "I understand."

     "The girl gets on her knees and tries to please."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "service", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "That feels so good, i've been waiting for this for some time now."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "sex"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "They keep cumming inside her and all over her one after the other."



     thug1 "My turn now, i haven't fucked this one yet"


     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "sex", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     with fade

     "There are so many of them, she feels like she's about to cry."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "anal"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug2 "My turn now, let me fuck this one's asshole."

     "The girl is obediently taking his cock and moaning, she looks like she wants more."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "anal", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     thug3 "This feels so good, i'm cumming."


     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "double"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "They are filling all her wholes and cumming one of the other, as soon as one finishes, another bandit puts his cock in."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "This feels so good, going to try that other one."

     mthug "Very good men, if any of these whores can still walk out after this, then you haven't used her properly!"


     "It's been a few hours, but to her it feels like it's been a week."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "aftersex", "cumshot"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "Every single guy has been satisfied and they left the girls lying on the floor, they didn't bother locking them in the rooms, because the girls can barely even breathe as it is."

     "They aren't going anywhere anytime soon."

     girl1.char "I'm going to get pregnant...there were so many of them...not like this."



     $ calendar.set_alarm(calendar.time + 3, StoryEvent("kidnapped_rogues10", type = "night"))
     $ girl1.change_fear(+7)

     jump main

 label kidnapped_rogues10:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "A few more days have passed, [girl1.name] has become even more obedient, whether she likes it or not. The bandits have made her pregnant after they kept gang raping her for days."


  $ pic = girl1.get_pic("dirty", and_tags=["pregnant"], strict=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  "She has now become one of them, perhaps there is still a chance for you to save her, but even if you did, she will never come back the same."




 label kidnapped_beasts:


  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "[girl1.name] was taken to the hideout of the beasts."

  play sound s_scream

  with fade


  $ pic = girl1.get_pic("dirty")

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  akuma "Stop screaming or i'll give you something to really scream about!"


  girl1.char "What do you want from me? Leave me alone!"


  gouki "You'll be a good little slut for us and you'll do everything we tell you to or else!"

  if girl1.fear <= -19:

      girl1.char "Go to hell! [MC.name] will be here soon and you'll all be sorry!"


      play sound s_crowd_laugh


      akuma "By the time he gets here, there won't be much of you to save! Now take your clothes off!"



      girl1.char "Not going to happen!"


      play sound s_punch


      $ pic = girl1.get_pic("dirty", and_tags=["hurt", "beast"], not_tags=["service", "sex", "anal"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      play sound s_scream


      gouki "You do what we tell you to, or you won't survive the night!"


      "The girl takes her clothes off afraid of what might happen if she didn't obey."

      $ pic = girl1.get_pic("dirty", and_tags=["strip", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      play sound s_crowd_cheer


      akuma "That's more like it, looking good!"


  else:

      girl1.char "Go to hell! I won't let you touch me!"


      play sound s_crowd_laugh


      gouki "You'll learn to obey one way or the other! We'll train you to be our pet!"



      girl1.char "Not going to happen!"


      play sound s_punch


      $ pic = girl1.get_pic("hurt", not_tags=["service", "sex"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      play sound s_scream


      akuma "You do what we tell you to, or you won't survive the night!"


      "The girl takes her clothes off afraid of what might happen if she didn't obey."

      $ pic = girl1.get_pic("strip", and_tags=["sub", "beast"], not_tags=["service", "sex"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      play sound s_crowd_cheer


      gouki "That's more like it, looking good!"

      with fade


  akuma "In the next few days you will be trained to obey and service every single bandit in our group. When we're done with you, you'll be nothing but a good cum dump for us, just like the other girls!"
  $ pic = girl1.get_pic("naked", strict=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  akuma "Now go back to your cell!"

  with fade

  $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  $renpy.pause()


  "The girl is a bit relieved that they didn't go further, but couldn't stop and wonder what will happen to her tomorrow!"
  $ girl1.change_fear(10)
  $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts2", type = "night"))
  jump main

  label kidnapped_beasts2:

  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been taken out by the bandits. Her fate looks bleak."

  $ pic = girl1.get_pic("dirty")

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  akuma "Undress, it's time to have some fun with you."


  if girl1.fear <= 0:

      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "beast"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      hide screen show_event
      $ girl1.change_fear(10)


      jump main


  else:

      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Please, let me go home!"

      akuma "Hahaha, like that would ever happen, you will be trained with the rest of these girls and once you're ready, you'll meet the boss!"

      gouki "Now, let's beging your training, learn to serve slut!"

      "They bring her to her knees and she starts sucking them off."

      $ pic = girl1.get_pic("dirty", and_tags=["service", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "She's a natural, gather around boys, she's very good!"

      girl1.char "I hate you all!"

      $ pic = girl1.get_pic("dirty", and_tags=["service", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      "After a few hours, they're done with her and bring her back to her room."

      akuma "That was good, let's go out and find some more.!"




      $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      $ girl1.change_fear(+7)


      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts3", type = "night"))

      jump main




  label kidnapped_beasts3:

   $ girl1 = rand_choice(kidnapped_girls)
   if girl1 not in game.kidnapped:
       return


   "Another day has passed and [girl1.name] has been taken out by the bandits. She is not aware of what will happen to her today, but is very scared."

   $ pic = girl1.get_pic("dirty")

   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

   akuma "Undress, it's time to have some fun with you."


   if girl1.fear <= 0:

      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse", "beast"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      hide screen show_event
      $ girl1.change_fear(+8)

      jump main


   else:

      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Please, let me go home!"

      akuma "Hahaha, we have something special for you today, it's time you learned to take some cocks."

      gouki "Enough talk, spread your legs slut, i've been waiting for this for quite some time now!"

      "The girl tries to fight back and screams but there are too many of them, they pin her to the floor as she slowly gives up."

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That feels so good, i've been waiting for this for some time now."

      girl1.char "Let me go!"

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "Shut up you slut, you're done when we say you are! Every single one of our guys will take you today!"

      hide screen show_Event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["sex", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That's a good girl, it will be over soon."

      "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That felt amazing, who's next boys?"



      gouki "It's my turn now, had an exhausting day, need some relief."

      "After a few hours, they're done with her and bring her back to her room."

      akuma "That was good, let's get some food, after that, bring out one of the other whores!"


      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["rest", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      "The girl is taken back to her cell, she can barely breathe."

      girl1.char "There were so many...i don't want to live anymore."



      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts4", type = "night"))
      $ girl1.change_fear(+7)

      jump main





  label kidnapped_beasts4:
     $ girl1 = rand_choice(kidnapped_girls)
     if girl1 not in game.kidnapped:
         return


     "Another day has passed and [girl1.name] has been dragged out by the bandits. She is silent and doesn't speak to them."

     $ pic = girl1.get_pic("dirty")

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "Undress, it's time to have some fun with you. You still need plenty of training"


     if girl1.fear <= 0:

      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      gouki "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "beast"], strict=True)

      girl1.char "Let me go you filthy animals!"

      akuma "She's a real fighter, we're going to have lots of fun with her."

      akuma "I'll have to punish you for dissobeying me. Send her to the dungeon for punishment."

      hide screen show_event

      $ girl1.change_fear(+10)


      jump main




     else:

      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "..."

      akuma "Hahaha, we have something special for you today, it's time you learned to take some cocks in that nice ass of yours."

      gouki "She's not in a talking mood today, she's learning."

      "The girl tries to fight back and screams but there are too many of them, they pin her to the floor as she slowly gives up."

      $ pic = girl1.get_pic("dirty", and_tags=["anal", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That feels so good, i've been waiting for this for some time now."

      girl1.char "I hate you."

      "She starts crying, which turns on the bandits even more, they keep taking turns on her while they laugh and humiliate her."

      $ pic = girl1.get_pic("dirty", and_tags=["anal", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "Shut up you slut, you're done when we say you are! Every single one of our guys will take you today!"

      hide screen show_Event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["anal", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "That's a good girl, it will be over soon."

      "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

      $ pic = girl1.get_pic("dirty", and_tags=["anal", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That felt amazing, who's next boys?"



      gouki "Her asshole is so tight, it will make me cum fast. I'll come back later for seconds, hahaha."

      "After a few hours, they're done with her and bring her back to her room."

      akuma "That was good, let's get some food, after that, bring out one of the other whores!"


      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["rest", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      "The girl is taken back to her cell, her asshole is leaking cum and it hurts so much she can barely walk."

      girl1.char "There were so many...i don't want to live anymore. It hurts."

      $ girl1.change_fear(+7)

      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts5", type = "night"))

      jump main

  label kidnapped_beasts5:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been dragged out by the bandits. She is acting a bit different today, like she has given up hope."

  $ pic = girl1.get_pic("dirty", "sub")

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  akuma "Undress, it's time to have some fun with you. You still need plenty of training"


  if girl1.fear <= 0:
      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse", "beast"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "beast"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      akuma "I'll have to punish you for dissobeying me. Send her to the dungeon for punishment."

      hide screen show_event

      $ girl1.change_fear(+10)


      jump main






  else:
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Yes, i understand,"

      akuma "Hahaha, what a good and obedient girl you're becoming, we'll soon be able to introduce you to the boss and then he can decide if you're ready for the ceremony."
      girl.char "Ceremony?"

      gouki "All in due time girl."

      gouki "Get down, time to service the men"

      "She goes on her knees and begins her new daily routine."

      $ pic = girl1.get_pic("dirty", and_tags=["service", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That feels so good, i've been waiting for this for some time now."

      girl1.char "Please, one at a time."

      "The girl is taking on each cock one after the other."

      $ pic = girl1.get_pic("dirty", and_tags=["servce", "sub", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "That's a good girl, you're learning, just like the others. You're nothing more but our cumsluts."

      hide screen show_Event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["service", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "That's a good girl, it will be over soon."

      "The girl is waiting for all of them to finish one by one, she can't count how many it has been."

      $ pic = girl1.get_pic("dirty", and_tags=["service", "sub", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That felt amazing, who's next boys?"



      gouki "Her mouth is so good, she's a real cocksucker, the boss will be happy with what we've done."

      "After a few hours, they're done with her and bring her back to her room."

      akuma "She is nearly ready."


      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      "The girl is taken back to her cell, her asshole is leaking cum and it hurts so much she can barely walk."

      girl1.char "There were so many...i don't want to live anymore. It hurts."

      $ girl1.change_fear(+7)

      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts6", type = "night"))

      jump main


  label kidnapped_beasts6:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen."

  $ pic = girl1.get_pic("dirty", and_tags=["sub"])

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  akuma "Undress, it's time to have some fun with you."


  if girl1.fear <= 0:
      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      hide screen show_event
      $ girl1.change_fear(+8)

      jump main




  else:
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Yes, please use me any way you want."

      akuma "Hahaha, any way we want? Just a few days ago you were asking us to leave you alone."

      gouki "Do you want us to fuck you now, slut?"

      girl.char "Yes, please use me."

      "The girl gets ready to receive their cocks while the bandits laugh."

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That feels so good, i've been waiting for this for some time now."

      girl1.char "Yes, i am here to serve."

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "Good, learn your place."

      hide screen show_Event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "That's a good girl, it will be over soon."

      "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That felt amazing, who's next boys?"



      gouki "It's my turn now, had an exhausting day, need some relief."

      "After a few hours, they're done with her and bring her back to her room."

      akuma "That was good, let's get some food, after that, bring out one of the other whores!"


      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

      girl1.char "Why didn't i fight back...am i getting used to be treated like a common whore. Someone, help."



      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts7", type = "night"))
      $ girl1.change_fear(+7)

      jump main





  label kidnapped_beasts7:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen."

  $ pic = girl1.get_pic("dirty", and_tags=["sub"])

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  akuma "Undress, it's time to have some fun with you."


  if girl1.fear <= 0:
      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      hide screen show_event
      $ girl1.change_fear(+8)

      jump main




  else:
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Yes, please use me any way you want."

      akuma "Hahaha, any way we want? Just a few days ago you were asking us to leave you alone."

      gouki "Do you want us to fuck you now, slut?"

      girl.char "Yes, please use me."

      "The girl gets ready to receive their cocks while the bandits laugh."

      $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That feels so good, i've been waiting for this for some time now."

      girl1.char "Yes, i am here to serve."

      $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "Good, learn your place."

      hide screen show_Event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "That's a good girl, it will be over soon."

      "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

      $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      akuma "That felt amazing, who's next boys?"



      gouki "It's my turn now, had an exhausting day, need some relief."

      "After a few hours, they're done with her and bring her back to her room."

      akuma "That was good, She is ready, let's present her to the boss tomorrow!"




      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

      girl1.char "The boss? Who is he? Is he the reason why this has happened to me?"



      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts8", type = "night"))
      $ girl1.change_fear(+7)

      jump main

  label kidnapped_beasts8:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen. Or at least she did, she forgot today is the day she meets their boss"

  $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "beast"])

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  demon "We finally meet girl, this is where your initiation begins."

  girl1.char "Initiation?"

  demon "This is where i decide whether you're worth keeping and if you are, you will participate in an orgy with the rest of the girls we have."

  girl.char "That's ridiculous and if i decide not to *participate*?"

  demon "You will be returned to my men for training."

  demon "The goal of the ceremony is simple, to get you pregnant, your children will be used as soldiers or help around camp."

  demon "So, what will it be? If you choose yes, then i will become your new master, you will do as i tell you or be punished."




  if girl1.fear <= 0:
      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse", "beast"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      hide screen show_event
      $ girl1.change_fear(+8)

      jump main




  else:
      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "strip", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Yes, please use me any way you want, master."

      demon "Hahaha, any way i want? That's what i call obedience!"

      demon "Get ready to serve me slut, first i want you to suck it."

      girl1.char "Yes, please use me, master."

      "The girl gets on her knees and tries to please."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "service", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      demon "That feels so good, i've been waiting for this for some time now."

      girl1.char "Yes, i am here to serve."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "service", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      demon "Good, you've passed the first step, next, i want your pussy."

      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "sex", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      demon "That's a good girl, i can see my man have trained you properly."

      "The girl is obediently taking his cock and moaning, she looks like she wants more."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "sex", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      demon "That felt amazing, now for the final stage, let's see how tight your asshole is."

      "She gets in position and is prepare to take yet another cock into her asshole, she's done it so many times, she doesn't think much of it."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "anal", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      demon "Good slut, here it comes."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "anal", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      "He cums inside each of her holes and when it all done the girl can barely talk."


      demon "You did good, i'm glad to say you've passed, get ready for the initiation tomorrow, you and the rest of these girls will take every men's cock, all at the same time."

      demon "If you manage to do it, you will become one of us and will be further bred every signle day until you become pregnant. If not, you will be put back in the cage and be trained like the animal you are."

      girl1.char "Yes, master."

      "With that she is taken back to her room to rest."


      hide screen show_event
      with fade


      $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

      girl1.char "An orgy? Every man will fill all my holes, i will probably even become pregnant, for some reason i no longer feel afraid. I am starting to feel excited."



      $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_beasts9", type = "night"))
      $ girl1.change_fear(+7)

      jump main

  label kidnapped_beasts9:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "The day has finally come, [girl.name] is taken out of her cell and is taken to a huge hall filled with men and women."

  demon "The time has finally come for the inititation, my brothers, these are the girls i've chosen for this initiation. You are welcome to try any number of them you want."

  demon "It's time to celebrate, go and indulge yourselves, you deserve it! There's plenty of whores for everyone, you don't need to ask, just go and take whoever you want and make the slut yours!"

  play sound s_crowd_cheer

  $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "strip", "beast"])

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "The girl looks around and can see all the bandits already grabbing girls and forcing them to the ground to fuck."

  $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "fondle", "beast"])

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "At the same time a lot of them are already around her and touching her any way they want."




  if girl1.fear <= 0:
      $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Go to hell, don't you dare touch me, you animal!"
      akuma "Looks like you still haven't learned, hahaha."
      "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
      $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

      girl1.char "Let me go you filthy animals!"

      gouki "She's a real fighter, we're going to have lots of fun with her."

      hide screen show_event
      $ girl1.change_fear(+8)

      jump main




  else:
      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "service", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      girl1.char "Please, be gentle."

      akuma "Less talking, more sucking!"

      gouki "Get ready to serve me slut, first i want you to suck it."

      girl1.char "I understand."

      "The girl gets on her knees and tries to please."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "service", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "That feels so good, i've been waiting for this for some time now."

      girl1.char "Yes, i am here to serve."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "sex"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      "They keep cumming inside her and all over her one after the other."



      akuma "My turn now, i haven't fucked this one yet"


      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "sex", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      hide screen show_event
      with fade

      "There are so many of them, she feels like she's about to cry."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "anal", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "My turn now, let me fuck this one's asshole."

      "The girl is obediently taking his cock and moaning, she looks like she wants more."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "anal", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      gouki "This feels so good, i'm cumming."


      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "double", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


      "They are filling all her wholes and cumming one of the other, as soon as one finishes, another bandit puts his cock in."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      "This feels so good, going to try that other one."

      demon "Very good men, if any of these whores can still walk out after this, then you haven't used her properly!"


      "It's been a few hours, but to her it feels like it's been a week."

      $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "aftersex", "cumshot", "beast"], strict=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      "Every single guy has been satisfied and they left the girls lying on the floor, they didn't bother locking them in the rooms, because the girls can barely even breathe as it is."

      "They aren't going anywhere anytime soon."

      girl1.char "I'm going to get pregnant...there were so many of them...not like this."



      $ calendar.set_alarm(calendar.time + 3, StoryEvent("kidnapped_beasts10", type = "night"))
      $ girl1.change_fear(+7)

      jump main

  label kidnapped_beasts10:
   $ girl1 = rand_choice(kidnapped_girls)
   if girl1 not in game.kidnapped:
       return


   "A few more days have passed, [girl1.name] has become even more obedient, whether she likes it or not. The orcs and other beasts have made her pregnant after they kept gang raping her for days."


   $ pic = girl1.get_pic("dirty", and_tags=["pregnant", "beast"], strict=True)
   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


   "She has now become one of them, perhaps there is still a chance for you to save her, but even if you did, she will never come back the same."






 label kidnapped_monsters:


   $ girl1 = rand_choice(kidnapped_girls)
   if girl1 not in game.kidnapped:
       return


   "[girl1.name] was taken to the cave of the monsters."

   play sound s_scream

   with fade


   $ pic = girl1.get_pic("profile")

   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

   play sound s_roar


   girl1.char "What do you want from me? Leave me alone!"


   "[girl.name] is being surrounded by the monsters as their tentacles get closer to her."

   if girl1.fear <= -25:

       girl1.char "Go to hell! [MC.name] will be here soon and you'll all be sorry!"


       play sound s_evil_laugh


       play sound s_roar



       girl1.char "Not going to happen!"


       play sound s_punch


       $ pic = girl1.get_pic("hurt", strict=True)

       show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

       play sound s_scream


       "One of the monsters hit her and she feel to ground. She can feel the monsters getting angry with her."


       "The girl takes her clothes off afraid of what might happen if she didn't obey."

       $ pic = girl1.get_pic("strip", and_tags=["monster"], not_tags=["service", "sex"], strict=True)
       show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

       play sound s_evil_laugh





   else:

       girl1.char "Go to hell! I won't let you touch me!"


       play sound s_roar






       girl1.char "Not going to happen!"


       play sound s_punch


       $ pic = girl1.get_pic("hurt", not_tags=["service", "sex"], strict=True)

       show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

       play sound s_scream


       "One of the monsters hit her and she feel to ground. She can feel the monsters getting angry with her."

       "The girl takes her clothes off afraid of what might happen if she didn't obey."

       $ pic = girl1.get_pic("strip", and_tags=["sub", "monster"], strict=True)
       show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

       play sound s_evil_laugh


       girl1.char "I hate you all! Let me go!"

       with fade


   "The monsters call their servers who grab her and throw her into a cell. It seems like they are done with her for tonight."
   $ pic = girl1.get_pic("naked", not_tags=["service", "sex"], strict=True)
   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


   girl1.char "I guess i could use some rest, i need to find a way out of here as soon as i regain my strenght. I hope [MC.name] is looking for me."

   $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


   "The girl is a bit relieved that they didn't go further, but couldn't stop and wonder what will happen to her tomorrow!"
   $ renpy.pause()
   hide screen show_event


   $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters2", type = "night"))
   $ girl1.change_fear(+7)

   jump main



   jump main

 label kidnapped_monsters2:

 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. Her fate looks bleak."

 $ pic = girl1.get_pic("dirty")

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 play sound s_roar

 "The monsters's servents tell the girl to undress"


 if girl1.fear <= 0:

     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     play sound s_roar
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "tentacles"], strict=True)

     girl1.char "Let me go you filthy animals!"

     play sound s_roar

     hide screen show_event
     $ girl1.change_fear(10)


     jump main


 else:

     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please, let me go home!"

     play sound s_roar

     "They bring her to her knees and their tentacles go all over her."

     $ pic = girl1.get_pic("dirty", and_tags=["service", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "She's a natural, gather around boys, she's very good!"

     girl1.char "I hate you all!"

     $ pic = girl1.get_pic("dirty", and_tags=["service", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "After a few hours, they're done with her and bring her back to her room."

     akuma "That was good, let's go out and find some more.!"




     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     $ girl1.change_fear(+7)


     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters3", type = "night"))

     jump main




 label kidnapped_monsters3:

  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
      return


  "Another day has passed and [girl1.name] has been taken out by the bandits. She is not aware of what will happen to her today, but is very scared."

  $ pic = girl1.get_pic("dirty")

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  akuma "Undress, it's time to have some fun with you."


  if girl1.fear <= 0:

     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse", "tentacles"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     akuma "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     gouki "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main


  else:

     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please, let me go home!"

     akuma "Hahaha, we have something special for you today, it's time you learned to take some cocks."

     gouki "Enough talk, spread your legs slut, i've been waiting for this for quite some time now!"

     "The girl tries to fight back and screams but there are too many of them, they pin her to the floor as she slowly gives up."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That feels so good, i've been waiting for this for some time now."

     girl1.char "Let me go!"

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     gouki "Shut up you slut, you're done when we say you are! Every single one of our guys will take you today!"

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["sex", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That's a good girl, it will be over soon."

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That felt amazing, who's next boys?"



     gouki "It's my turn now, had an exhausting day, need some relief."

     "After a few hours, they're done with her and bring her back to her room."

     akuma "That was good, let's get some food, after that, bring out one of the other whores!"


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she can barely breathe."

     girl1.char "There were so many...i don't want to live anymore."



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters4", type = "night"))
     $ girl1.change_fear(+7)

     jump main





 label kidnapped_monsters4:
    $ girl1 = rand_choice(kidnapped_girls)
    if girl1 not in game.kidnapped:
        return


    "Another day has passed and [girl1.name] has been dragged out by the bandits. She is silent and doesn't speak to them."

    $ pic = girl1.get_pic("dirty")

    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

    akuma "Undress, it's time to have some fun with you. You still need plenty of training"


    if girl1.fear <= 0:

     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     gouki "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "tentacles"], strict=True)

     girl1.char "Let me go you filthy animals!"

     akuma "She's a real fighter, we're going to have lots of fun with her."

     akuma "I'll have to punish you for dissobeying me. Send her to the dungeon for punishment."

     hide screen show_event

     $ girl1.change_fear(+10)


     jump main




    else:

     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "..."

     akuma "Hahaha, we have something special for you today, it's time you learned to take some cocks in that nice ass of yours."

     gouki "She's not in a talking mood today, she's learning."

     "The girl tries to fight back and screams but there are too many of them, they pin her to the floor as she slowly gives up."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That feels so good, i've been waiting for this for some time now."

     girl1.char "I hate you."

     "She starts crying, which turns on the bandits even more, they keep taking turns on her while they laugh and humiliate her."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     gouki "Shut up you slut, you're done when we say you are! Every single one of our guys will take you today!"

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["anal", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     gouki "That's a good girl, it will be over soon."

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That felt amazing, who's next boys?"



     gouki "Her asshole is so tight, it will make me cum fast. I'll come back later for seconds, hahaha."

     "After a few hours, they're done with her and bring her back to her room."

     akuma "That was good, let's get some food, after that, bring out one of the other whores!"


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, her asshole is leaking cum and it hurts so much she can barely walk."

     girl1.char "There were so many...i don't want to live anymore. It hurts."

     $ girl1.change_fear(+7)

     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters5", type = "night"))

     jump main

 label kidnapped_monsters5:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been dragged out by the bandits. She is acting a bit different today, like she has given up hope."

 $ pic = girl1.get_pic("dirty", "sub")

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 akuma "Undress, it's time to have some fun with you. You still need plenty of training"


 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse", "tentacles"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     akuma "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "tentacles"], strict=True)

     girl1.char "Let me go you filthy animals!"

     gouki "She's a real fighter, we're going to have lots of fun with her."

     akuma "I'll have to punish you for dissobeying me. Send her to the dungeon for punishment."

     hide screen show_event

     $ girl1.change_fear(+10)


     jump main






 else:
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, i understand,"

     akuma "Hahaha, what a good and obedient girl you're becoming, we'll soon be able to introduce you to the boss and then he can decide if you're ready for the ceremony."
     girl.char "Ceremony?"

     gouki "All in due time girl."

     gouki "Get down, time to service the men"

     "She goes on her knees and begins her new daily routine."

     $ pic = girl1.get_pic("dirty", and_tags=["service", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That feels so good, i've been waiting for this for some time now."

     girl1.char "Please, one at a time."

     "The girl is taking on each cock one after the other."

     $ pic = girl1.get_pic("dirty", and_tags=["servce", "sub", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     gouki "That's a good girl, you're learning, just like the others. You're nothing more but our cumsluts."

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["service", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     gouki "That's a good girl, it will be over soon."

     "The girl is waiting for all of them to finish one by one, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["service", "sub", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That felt amazing, who's next boys?"



     gouki "Her mouth is so good, she's a real cocksucker, the boss will be happy with what we've done."

     "After a few hours, they're done with her and bring her back to her room."

     akuma "She is nearly ready."


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, her asshole is leaking cum and it hurts so much she can barely walk."

     girl1.char "There were so many...i don't want to live anymore. It hurts."

     $ girl1.change_fear(+7)

     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters6", type = "night"))

     jump main


 label kidnapped_monsters6:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen."

 $ pic = girl1.get_pic("dirty", and_tags=["sub"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 akuma "Undress, it's time to have some fun with you."


 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     akuma "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     gouki "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, please use me any way you want."





     girl.char "Yes, please use me."

     "The girl gets ready to receive their cocks while the bandits laugh."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     akuma "That feels so good, i've been waiting for this for some time now."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_roar
     "The monsters approve of her attitude and soon beging to penetrate her pussy."

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_roar

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



     "After a few hours, they're done with her and bring her back to her room."




     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

     girl1.char "Why didn't i fight back...am i getting used to be treated like a common whore. Someone, help."



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters7", type = "night"))
     $ girl1.change_fear(+7)

     jump main





 label kidnapped_monsters7:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen."

 $ pic = girl1.get_pic("dirty", and_tags=["sub"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "The human servant talks to the girl, he is a slave of the monster's will."

 "Undress, it's time to have some fun with you. My masters have a special plan."


 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     play sound s_roar
     "The monster grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     play sound s_roar

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, please use me any way you want."

     play sound s_roar

     girl.char "Yes, please use me."

     "The girl gets ready to receive their cocks while the bandits laugh."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please use me any way you want."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["sex", "sub", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "The monster approves and wraps it's tentacles around her."

     hide screen show_Event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_roar

     "The girl is helplessly waiting for all of them to finish, she can't count how many it has been."

     $ pic = girl1.get_pic("dirty", and_tags=["anal", "sub", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))







     "After a few hours, they're done with her and bring her back to her room."

     play sound s_roar




     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

     girl1.char "The boss? Who is he? Is he the reason why this has happened to me?"



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters8", type = "night"))
     $ girl1.change_fear(+7)

     jump main

 label kidnapped_monsters8:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "Another day has passed and [girl1.name] has been taken out by the bandits. She knows what's about to happen. Or at least she did, she forgot today is the day she meets the main leader."

 $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "tentacles"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "The leader uses one of the human servants to communicate through, the human barely knows what's going on, he is a slave to his master's will"

 "We finally meet girl, this is where your initiation begins."

 girl1.char "Initiation?"

 "This is where i decide whether you're worth keeping and if you are, you will participate in an orgy with the rest of the girls we have."

 girl.char "That's ridiculous and if i decide not to *participate*?"

 "You will be returned to my men for training."

 "The goal of the ceremony is simple, to get you pregnant, your children will be used as soldiers or help around camp."

 "So, what will it be? If you choose yes, then i will become your new master, you will do as i tell you or be punished."




 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse", "tentacles"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     akuma "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     play sound s_roar

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "strip", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Yes, please use me any way you want, master."

     "Hahaha, any way i want? That's what i call obedience!"

     "Get ready to serve me slut, first i want you to suck it."

     girl1.char "Yes, please use me, master."

     "The girl gets on her knees and tries to please."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "service", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "That feels so good, i've been waiting for this for some time now."

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "service", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "Good, you've passed the first step, next, i want your pussy."

     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "sex", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "That's a good girl, i can see my man have trained you properly."

     "The girl is obediently taking his cock and moaning, she looks like she wants more."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "sex", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "That felt amazing, now for the final stage, let's see how tight your asshole is."

     "She gets in position and is prepare to take yet another cock into her asshole, she's done it so many times, she doesn't think much of it."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "anal", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "Good slut, here it comes."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "anal", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "He cums inside each of her holes and when it all done the girl can barely talk."


     "You did good, i'm glad to say you've passed, get ready for the initiation tomorrow, you and the rest of these girls will take every men's cock, all at the same time."

     "If you manage to do it, you will become one of us and will be further bred every signle day until you become pregnant. If not, you will be put back in the cage and be trained like the animal you are."

     girl1.char "Yes, master."

     "With that she is taken back to her room to rest."


     hide screen show_event
     with fade


     $ pic = girl1.get_pic("dirty", and_tags=["rest"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     "The girl is taken back to her cell, she is lying in her bed, thinking about the day and what will happen tomorrow."

     girl1.char "An orgy? Every man will fill all my holes, i will probably even become pregnant, for some reason i no longer feel afraid. I am starting to feel excited."



     $ calendar.set_alarm(calendar.time + 1, StoryEvent("kidnapped_monsters9", type = "night"))
     $ girl1.change_fear(+7)

     jump main

 label kidnapped_monsters9:
 $ girl1 = rand_choice(kidnapped_girls)
 if girl1 not in game.kidnapped:
     return


 "The day has finally come, [girl.name] is taken out of her cell and is taken to a huge hall filled with all kinds of monsters and women."

 play sound s_roar

 "The monsters communicate through gestures and roars, after they are done, they focus on all the girls around them. It seems like this ritual has begun, [girl1.name] tries to run, but she has nowhere to go."

 play sound s_roar

 $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "strip", "tentacles"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "The girl looks around and can see all the bandits already grabbing girls and forcing them to the ground to fuck."

 $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "fondle", "tentacles"])

 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "At the same time a lot of them are already around her and touching her any way they want."




 if girl1.fear <= 0:
     $ pic = girl1.get_pic("dirty", and_tags=["angry", "refuse"], strict=True)

     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Go to hell, don't you dare touch me, you animal!"
     akuma "Looks like you still haven't learned, hahaha."
     "The bandits grabs the girl and forces her to undress, they grope and fondle her while she screams for help."
     $ pic = girl1.get_pic("dirty", and_tags=["strip", "naked"], strict=True)

     girl1.char "Let me go you filthy animals!"

     gouki "She's a real fighter, we're going to have lots of fun with her."

     hide screen show_event
     $ girl1.change_fear(+8)

     jump main




 else:
     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "service", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     girl1.char "Please, be gentle."

     play sound s_roar

     girl1.char "Noo, waiit."

     "The girl gets on her knees and tries to please."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "service", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_roar

     girl1.char "Yes, i am here to serve."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "sex"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "They keep cumming inside her and all over her one after the other."



     play sound s_roar


     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "sex", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     hide screen show_event
     with fade

     "There are so many of them, she feels like she's about to cry."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "anal", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_roar

     "The girl is obediently taking his tentacle in her asshole and moaning, she looks like she wants more."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "anal", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "It looks like the monsters are about to cum."


     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "double", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "They are filling all her wholes and cumming one of the other, as soon as one finishes, another bandit puts his cock in."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "group", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_roar

     "The servents watch on with approval, as the monsters rape the girls and toss them around left and right."


     "It's been a few hours, but to her it feels like it's been a week."

     $ pic = girl1.get_pic("dirty", and_tags=["ceremony", "aftersex", "cumshot", "tentacles"], strict=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "Every single monster has been satisfied and they left the girls lying on the floor, they didn't bother locking them in the rooms, because the girls can barely even breathe as it is."

     "They aren't going anywhere anytime soon."

     girl1.char "I'm going to get pregnant...there were so many of them...not like this."



     $ calendar.set_alarm(calendar.time + 3, StoryEvent("kidnapped_monsters10", type = "night"))
     $ girl1.change_fear(+7)


     jump main

 label kidnapped_monsters10:
  $ girl1 = rand_choice(kidnapped_girls)
  if girl1 not in game.kidnapped:
     return

  "A few more days have passed, [girl1.name] has become even more obedient, whether she likes it or not. The tentacle monsters have made her pregnant after they kept raping her for days."


  $ pic = girl1.get_pic("dirty", and_tags=["pregnant", "tentacles"], strict=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  "She has now become one of them, perhaps there is still a chance for you to save her, but even if you did, she will never come back the same."
