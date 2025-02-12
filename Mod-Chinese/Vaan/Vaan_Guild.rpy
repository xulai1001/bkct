label pool_party:
 "You think about what to do and decide to take a dip in the pool and relax. You see that some of the girls are already there and they look happy to see you."

 "Just as you are about to sit down some of the girls come over to you with smiles on their faces."
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]


 image pool = "mods/vaan/pool.png"

 show pool







 python:
    for girl in MC.girls:
        if girl.love >= 50 and girl.love >= girl.fear + 50:
            holiday_pic = girl.get_pic("swim", naked_filter=True, soft=True)

            approach = [girl.name + " comes over, she looks so how in her bikini.","You notice " + girl.name + " rushing towards you, her boobs jugling up and down in her tight swimsuit.", girl.name + " wishes to speak to you.", "You also see " + girl.name + ", coming over.", "the girls are joined by " + girl.name + ", who looks towards you.", girl.name + " tugs on your arm, eager to say something.", "Another girl joins the group " + girl.name + ", who looks excited.", "You hear " + girl.name + " shouting your name as she runs up to you.", "You hear " + girl.name + " calling for you loudly, eager to express what's on her mind.", "While the girls are happily surrounding you " + girl.name + ", looks from the distance with an approving smile."]

            add_dialogue("pool party", ("very extravert"), ("Would you like to play with me!", "I have a beach ball that we can play with!", "You never come down here to relax, i'm so happy to see you!"))
            add_dialogue("pool party", ("very introvert"), ("I-is this a good time? I love you, [MC.name]!", "I was wondering if you had some time for me too..."))
            add_dialogue("pool party", ("very idealist"), ("Oh my god! There are so many people here!", "Let's have a party, what do you say [MC.name]?", "The sun is so warm, nice of you to join us!"))
            add_dialogue("pool party", ("very materialist"), ("Heeey, would you like to go for a swim?", "[MC.name], what a nice surprise!", "I'm going to go tan for a bit, you are welcome to join me!"))
            add_dialogue("pool party", ("very lewd"), ("How do i look? Do you like my swimsuit?", "I'm going to tan with some of the other girls, would you like to rub some lotion on me? You can even use the special sunscreen, if you know what i mean *wink.", "I'm going to jump in the water, my bikini gets really tight when i get wet, do you want to see?"))
            add_dialogue("pool party", ("very modest"), ("I hope you like my bikini, got them to show off to you!", "[MC.name], i am so happy you came down to see us!", "Oh [MC.name], it's nice to see you. Hope you'll stay with us for a bit."))
            add_dialogue("pool party", ("very dom"), ("You're awesome. You know that, right? I've had so much fun here, with you. Why stop now, we should have a pool party!", "What do you think of my bikini? It's amazing isn't it? I bet you wish you can do all kinds of things to me? Stick around and i might just let you, haha!", "How nice of you to join us. Stay and watch me wrestle the girls in the pool! If you're lucky, you might see someone's bikini fall off!"))
            add_dialogue("pool party", ("very sub"), ("[MC.name], i'm so embarassed, i think my bikini is too revealing, i didn't expect to see you here!", "[MC.name], is everything okay, do you need something from me?", "Hey [MC.name], it's really good to see you, the water is nice and warm today. Would you like to go in together?"))

            renpy.say("",rand_choice(approach))

            renpy.show_screen("show_event", holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            girl.say("pool party")
            renpy.hide_screen("show_event")
            holiday_pic = None
            continue


            # show screen show_event(holiday_pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
            # with dissolve
            # call dialogue(girl, "slave love")
            # hide screen show_event




















 "The girls look to be enjoying themselves in the sun, you all play around for an hour and after some time you find a chair to relax."

 "A few of them follow you back with a smirk on their faces, you think you know what they want. One of them move closer, while the others gigle behind her."
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl1 = rand_choice(able_girls)
 $ girl2 = rand_choice(able_girls)
 $ girl3 = rand_choice(able_girls)
 $ girl = rand_choice(able_girls)
 $ girl4 = rand_choice(able_girls)


 play sound s_girls_laugh

 show screen show_event(girl.get_pic("profile"), x=config.screen_width, y=int(config.screen_height*0.8))

 girl.char "[MC.name], we were wondering would you like to have some fun. We mean the other kind of fun? Do you think you can handle all of us at once?"
 play sound s_girls_laugh

 you "I've been watching you all in your sexy bikinis all day, i have been thinking about it since the moment i showed up! Come over here!"
 with fade



 "The girls can't wait to try, there more of them around you than you can count! They take off your trunks and go down, while you wait for them to figure out who's going first!"
 python:
  for girl in MC.girls:
     girl_pic = girl.get_pic("handjob", "oral", "titjob", and_tags=["swim", "mc"], not_tags=["cumshot", "group"], soft=True)


     renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8))
     add_dialogue("pool service", ("very extravert"), ("Been waiting all day for this!", "I love your cock!", "It's so big!"))
     add_dialogue("pool service", ("very introvert"), ("I hope i can please you, [MC.name]!", "I was wondering if i can have it too, please!"))
     add_dialogue("pool service", ("very idealist"), ("Oh wow, i'm so horny.", "It's my turn now, I want it!", "I'm so wet right now!"))
     add_dialogue("pool service", ("very materialist"), ("Such a great taste, i love it!", "[MC.name], i love your cock!", "I've been waiting for my turn all day, finally!"))
     add_dialogue("pool service", ("very lewd"), ("Such a big cock, i can't wait anymore, move aside!", "I told you earlier i would get that special sunscreen didn't i?", "This is so hot! I love competing with the other girls for your dick."))
     add_dialogue("pool service", ("very modest"), ("It tastes amazing!", "[MC.name], please go easy on me!", "Oh [MC.name], i'm going to cum!"))
     add_dialogue("pool service", ("very dom"), ("Move away, sluts, he's mine! I guess today is the day everyone gets to see me suck your cock!", "Watch me suck that cock sluts, you know i'm the best one at sucking it!", "Finally, my turn is here! I've been waiting all day to get to your cock."))
     add_dialogue("pool service", ("very sub"), ("[MC.name], everyone is watching, but i'll do my best!", "[MC.name], i hope i can pleasure you better than the rest!", "Does it feel good? I'm so turned on when everyone is watching."))
     girl.say("pool service")

     continue















 you "Girls, that feels amazing!"

 girl1.char "We're not done yet, i want to ride that cock!"

 girl2.char "I want it inside of me. I get to go next!"

 girl1.char "Wait for your turn!"


 girl3.char "Get to it already! We're all waiting. [MC.name] will probably cum by the time you finish!"

 you "I'll start with your pussies, get ready"


 python:
    for girl in MC.girls:
        girl_pic = girl.get_pic("sex", and_tags=["swim", "mc"], not_tags=["cumshot", "group", "bisexual"], soft=True)


        renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8))
        add_dialogue("pool sex", ("very extravert"), ("Been waiting all day for this! Put it in [MC.name].", "I love your cock! I want it inside me!", "It's so big!"))
        add_dialogue("pool sex", ("very introvert"), ("Please use me, any way you want.", "I was wondering if i can have it too, deep inside me."))
        add_dialogue("pool sex", ("very idealist"), ("Ass or pussy? You can use whichever!", "It's my turn now, step away!", "I hope you have enough left for me!"))
        add_dialogue("pool sex", ("very materialist"), ("I wonder how it will feel! I can't wait to find out!", "[MC.name], put it in, i can't wait any longer!", "I've been waiting for my turn all day, finally!"))
        add_dialogue("pool sex", ("very lewd"), ("I want, i want, i want it! Fuck me hard, [MC.name]!", "Put it in, you can use me any way you want!", "This is so hot! Move aside, sluts! That cock is mine, i will make you cum, [MC.name]."))
        add_dialogue("pool sex", ("very modest"), ("It feels great!", "[MC.name], please go easy on me!", "Oh [MC.name], i'm going to cum! Please keep going!"))
        add_dialogue("pool sex", ("very dom"), ("That cock won't last much longer, you better cum inside me!", "Watch me take it in whores, you know i'm the best one here!", "Finally, my turn is here! I'm the only one who deserves your cum!"))
        add_dialogue("pool sex", ("very sub"), ("[MC.name], everyone is watching, but i'll do my best!", "[MC.name], i hope i can pleasure you better than the rest!", "Does it feel good? I'm so turned on when everyone is watching."))
        add_dialogue("pool sex", ("pervert"), ("*giggle* You were totally checking out my butt, weren't you?", "I've been waiting for this!", "Hope you have enough left for me, otherwise you'd have to fuck me again later!"))
        add_dialogue("pool sex", ("generic", "meek", "loyal", "helper"), ("I treasure the time I spend with you.", "Please fuck me in front of everyone, make them know i'm number one for you!", "Do you see this girls? I told you he loves me the most!", "He is fucking me so hard, it means he loves me more than the rest of you!"))
        add_dialogue("pool sex", ("creep", "yandere"), ("Fuck me hard!", "Don't you dare stop, or i'll hit someone!", "Fuck me harder, i know you can do it!"))
        add_dialogue("pool sex", ("generic", "nerd", "class president", "tsundere"), ("The rest of you better step aside, i'm about to show you how it's done!", "Take notes bitches, i'll show you how to please guys, do it harder [MC.name]!", "I'll make you cum using a technique i learned!"))
        girl.say("pool sex")



        continue



 you "Time to switch, bring your asses to me!"

 "The girls take their turns again, this time you switch to fucking their assholes!"

 python:
    for girl in MC.girls:
        girl_pic = girl.get_pic("anal", and_tags=["swim", "mc"], not_tags=["cumshot", "group"], soft=True)


        renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8))
        add_dialogue("pool anal", ("very extravert"), ("Been waiting all day for this! Put it in [MC.name], my ass loves it!.", "I love your cock! I want it inside me! Hope my asshole is tight!", "It's so big! Too big for my ass!"))
        add_dialogue("pool anal", ("very introvert"), ("Please use my ass, any way you want!", "I was wondering if i can have it too, deep inside my ass!"))
        add_dialogue("pool anal", ("very idealist"), ("You want my ass this time, no problem!", "It's my turn now, step away sluts! Master wants my ass!", "I hope you have enough left for me! My ass is tight!"))
        add_dialogue("pool anal", ("very materialist"), ("I wonder how it will feel! I can't wait to find out!", "[MC.name], put it in, i can't wait any longer!", "Hope you like my ass!"))
        add_dialogue("pool anal", ("very lewd"), ("My asshole can't wait! Fuck me hard, [MC.name]!", "Put it in, you can use me any way you want! My ass is amazing isn't it?", "This is so hot! Move aside, sluts! That cock is mine, i will make you cum, [MC.name]. My ass is quite trained, isn't it?"))
        add_dialogue("pool anal", ("very modest"), ("It feels great! My asshole is stretching!", "[MC.name], please go easy on me!", "Oh [MC.name], i'm going to cum! Please keep going!"))
        add_dialogue("pool anal", ("very dom"), ("Inside my ass, hah, dirty boy!", "Watch me take it in whores, you know i'm the best one here! My ass is is the best!", "You've never had an ass like this before and you never will again!"))
        add_dialogue("pool anal", ("very sub"), ("[MC.name], everyone is watching, but i'll do my best!", "[MC.name], i hope i can pleasure you better than the rest!", "Does it feel good? I'm so turned on when everyone is watching."))
        add_dialogue("pool anal", ("pervert"), ("Fuch that ass, don't you dare stop until you cum, yeees!", "My ass is ready, fuck me!", "Yes, my ass is yours! Fuck me, fuck me!"))
        add_dialogue("pool anal", ("generic", "meek", "loyal", "helper"), ("I treasure the time I spend with you. Please fuck my tight little ass!", "Please fuck me in front of everyone, make them know i'm number one for you!", "Do you see this girls? I told you he loves me the most! My ass is his", "He is fucking me so hard, it means he loves me more than the rest of you! Use my ass!"))
        add_dialogue("pool anal", ("creep", "yandere"), ("Fuck me hard!", "You want to use my ass huh? Fine, make sure you fuck it hard!", "Fuck me harder, i know you can do it! My ass is loving the attention"))
        add_dialogue("pool anal", ("generic", "nerd", "class president", "tsundere"), ("The rest of you better step aside, i'm about to show you how it's done!", "Take notes bitches, i'll show you how to please a guys, do it harder [MC.name]!", "I'll make you cum using a technique i learned!"))
        girl.say("pool anal")




 you "I'm going to cum, don't worry, there's enough for everyone!"

 python:
    for girl in MC.girls:
        girl_pic = girl.get_pic("cumshot", and_tags=["swim", "mc"], not_tags=["group"], soft=True)

        renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8))
        add_dialogue("pool cum", ("very extravert"), ("Give me all your cum!", "Yes, i want it. Cum inside me!", "So much cum!"))
        add_dialogue("pool cum", ("very introvert"), ("In front of everyone, embarassing!", "Please cum, although it's embarassing!"))
        add_dialogue("pool cum", ("very idealist"), ("Yes, cum anywhere you want!", "It's my turn now, love me some cum!", "I hope you have enough left for me! Paint me any way you want!"))
        add_dialogue("pool cum", ("very materialist"), ("I wonder how it will feel! I can't wait to find out!", "[MC.name], give it to me, i've been a good slut!", "Yes, give it here!"))
        add_dialogue("pool cum", ("very lewd"), ("All the cum!", "Put it in, or cum on me, i don't care, just do it!", "This is so hot! Move aside, sluts! That cock is mine, i will take your cum, [MC.name]."))
        add_dialogue("pool cum", ("very modest"), ("It feels great!", "[MC.name], please cum on me!", "Oh [MC.name], i can't wait to receive it!"))
        add_dialogue("pool cum", ("very dom"), ("Inside my ass, hah, dirty boy! Cum where you want!", "Yes, in front of everyone, cum for me!", "I love it, cum loads more!"))
        add_dialogue("pool cum", ("very sub"), ("[MC.name], everyone is watching, but i'll do my best!", "[MC.name], i hope i can pleasure you better than the rest! Please let me receive it!", "Does it feel good? I'm so turned on when everyone is watching. Cum for me, please!"))
        add_dialogue("pool cum", ("pervert"), ("Give me your cum, i want it sooo bad. Watch me take it all, sluts!", "Cum inside me, i want to feel it! Or anywhere else, just let me have it!", "I can feel it, it's coming!"))
        add_dialogue("pool cum", ("generic", "meek", "loyal", "helper"), ("Cum for me, please! I deserve it!", "Give me your cum, show them i'm yours!", "Do you see this girls? I told you he loves me the most! He came for me so much!", "You came so much, [MC.name]. I think the others are jealous now!"))
        add_dialogue("pool cum", ("creep", "yandere"), ("Cum for me now! Don't make me angry!", "Cum, cum, cum! I want it allll!", "Cum all over me, i don't care who sees it!"))
        add_dialogue("pool cum", ("generic", "nerd", "class president", "tsundere"), ("Finally, i worked so hard to get it!", "My technique worked, who says studying doesn't pay off. All that cum, [MC.name]! I guess this is my reward", "I love it!"))
        girl.say("pool cum")



 "After you and the girls are done, it's time to head back inside. One by one they go back, half naked, ready for work!"

 python:
    for girl in MC.girls:
        girl_pic = girl.get_pic("naked", and_tags=["swim", "beach", "strip", "mc"], not_tags=["group", "service", "sex"], soft=True)

        renpy.show_screen("show_event", girl_pic, x=config.screen_width, y=int(config.screen_height*0.8))
        add_dialogue("pool finished", ("very extravert"), ("We should do it again!", "That was amazing!", "Loved it, bye [MC.name]."))
        add_dialogue("pool finished", ("very introvert"), ("In front of everyone, embarassing!", "Naked, embarassing, have to go back and change!", "See you later, no time to change here, everyone can see me naked"))
        add_dialogue("pool finished", ("very idealist"), ("We should have more parties like this!", "That was great, thank you!", "[MC.name], that was some party! Hope you come back again!"))
        add_dialogue("pool finished", ("very materialist"), ("Starting to get coold, need to head back inside!", "[MC.name], have i been great or what? Hope to see you again here soon!", "Yes! That was the craziest sex i've ever had!"))
        add_dialogue("pool finished", ("very lewd"), ("All the cum! I'm never washing it off!", "Oh wooow, i'll stick around. Half naked with your cum all over me, if you don't mind!", "This was so hot! See you soon."))
        add_dialogue("pool finished", ("very modest"), ("It felt great! Hope you can invite me next time you're here!", "[MC.name], please help me get dressed if you can.", "Oh [MC.name], that was great!"))
        add_dialogue("pool finished", ("very dom"), ("Where are my clothes, sigh...It doesn't matter, going back in!", "In front of everyone, hope they don't think i'm a slut, ah who cares, going back!", "I love it, next time save more cum for me! You gave too much to the others!"))
        add_dialogue("pool finished", ("very sub"), ("[MC.name], everyone is watching, but i did my best for you!", "[MC.name], i hope i can pleasure you again next time!", "Did it feel good? It fels amazing for me! Hope i managed to please you!"))
        add_dialogue("pool finished", ("pervert"), ("So much cum, will go masturbate, thinking about what just happened!", "Can't believe it happened, it feels like a dream. You fucked us all! Hope you stop by again soon!", "I can still feel your cum! You don't mind if i walk around with it for a bit do you?"))
        add_dialogue("pool finished", ("generic", "meek", "loyal", "helper"), ("Hope you are pleased! I wanted more time with you, but the others kept pushing me back! Everyone wanted their turn!", "That showed them, they all know that i'm your number one now!", "Do you see this girls? I told you he loves me the most! He came for me so much! Time to dress up and head back!", "You came so much, [MC.name]. I think the others are jealous now! But i don't care, because i love you!"))
        add_dialogue("pool finished", ("creep", "yandere"), ("Ugh, need to clean myself.", "Where are my clothes? If someone took them away, i'll make you sorry!", "That was great, but not doing it again anytime soon! Too many people for my liking!"))
        add_dialogue("pool finished", ("generic", "nerd", "class president", "tsundere"), ("Guess i showed them! Time to dress up!", "Time to go back and do some studying before work, see you [MC.name]", "I love it! I feel so energized now! Going to catch up on reading before the guests come in!"))
        girl.say("pool finished")


 hide screen show_event

 show screen home


 $ girl.change_love(10)
 $ girl.change_fear(-14)
 $ MC.interactions -= 2

 jump main




label buy_house:

 if vaan_house_built:

     call screen guild


 if not vaan_house_built:
     image guild = "mods/vaan/guild.png"

     "You walk around through the city and see that there's a guild house for sale. The guild who used to work here went bankrupt."

     "Would you like to buy the guild house? It will cost 100000 gold."




     menu:

         "Yes":
          if MC.gold < 100000:
             "You don't have enough gold. Hopefully you'll have the money by next month, you'll try again then."



             jump main


          else:



             "Congratulations! This brand new guild house is all yours. You can buy upgrades for it and expand it even more."

             $ vaan_house_built = True
             $ MC.gold -= 100000 # Better to use MC.change_gold(-50000) to have the notifications work automatically and some built-in sanity checks.
             $ MC.change_prestige(10)

             call screen guild





         "No":

             "You have no plans of buying a house, so you just pass it by."

             "Once you've chosen this, you won't be able to go back, by the time you do, someone will have probably bought it."


             jump main


         "Postpone":

             "You want to try and come back in a week, hopefully you'll have the money by then. Maybe you can get a loan from the bank."




             jump main

label buy_tavern:

 if vaan_tavern_built:

     call screen guild_tavern


 if not vaan_tavern_built:
     "You find yourself in huge room full of tables a bar and a few other smaller rooms within it. This used to be a tavern for the guild before you, here heroes would drink and relax after a mission."


     "Do you want to restore it to it's former glory? Perhaps even add a few rooms to it?"



     menu:

         "Yes":
          if MC.gold < 30000:
             "You don't have enough gold."



             jump buy_tavern


          else:



             "Congratulations! The Tavern has been restored."

             $ vaan_tavern_built = True
             $ MC.gold -= 30000 # Better to use MC.change_gold(-50000) to have the notifications work automatically and some built-in sanity checks.
             $ MC.change_prestige(10)

             call screen guild_tavern




         "No":

             "You don't have the money or simply don't want to do it right now, so you just go back."




             call screen guild


label buy_office:

 if vaan_office_built:

     call screen guild_office


 if not vaan_tavern_built:
     "You find yourself in huge room  with an old desk in the middle. This used to be the leader's office for the guild before you, here heroes would get recruited and sent out to missions."


     "Do you want to restore it to it's former glory? Perhaps even make it better?"



     menu:

         "Yes":
          if MC.gold < 30000:
             "You don't have enough gold."



             jump buy_office


          else:



             "Congratulations! The Office has been restored."

             $ vaan_office_built = True
             $ MC.gold -= 30000 # Better to use MC.change_gold(-50000) to have the notifications work automatically and some built-in sanity checks.
             $ MC.change_prestige(10)

             call screen guild_office




         "No":

             "You don't have the money or simply don't want to do it right now, so you just go back."




             call screen guild
























label guild_vip_room:

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)
 image guild = "mods/vaan/vip_room.png"
 show guild
 "You find yourself in a room with a dance pole. You call one of the girls to come join you."

 $ pic = girl.get_pic("profile", soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "This room is nice and private where no one can see, would you like me to give you a nice private dance?"


 you "Of course! I want to see you on that pole, girl!"

 girl.char "Hahaha, very well."


 $ pic = girl.get_pic("mc", and_tags=["dancer"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 you "Oh wow, keep it up!"

 "The girl, is happy you're enjoying her dance, she starts dancing provocative, she is enjoying herself a lot."


 $ pic = girl.get_pic("mc", and_tags=["dancer", "tempt"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 you "How about you take your clothes off?"


 girl.char "Of course."



 $ pic = girl.get_pic("mc", and_tags=["dancer", "strip"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



 girl.char "Do you like what you see?"





 $ pic = girl.get_pic("mc", and_tags=["dancer", "naked"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "The girl is dancing naked in front of you, you wonder if you can take it further and try to grab her."


 play sound s_mmmh

 "She seems to be enjoying it."


 $ pic = girl.get_pic("mc", and_tags=["dancer", "naked", "fondle"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "You grab and kiss her all over, while she still tries to move around and dance for you."


 girl.char "I'm feeling so horny, how about a blowjob?"


 "She doesn't wait for you to answer and goes down on your dick."


 $ pic = girl.get_pic("mc", and_tags=["dancer", "service"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "Oh wow, it's such a big cock, i love it."



 you "I'm not done yet girl, i want to fuck you."


 $ pic = girl.get_pic("mc", and_tags=["dancer", "sex"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 play sound s_mmmh


 "She is happy to please and you push your cock inside her, you start fucking her where she is."


 girl.char "That feels amazing, keep going."


 $ pic2 = girl.get_pic("mc", and_tags=["dancer", "sex"], soft=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))


 "You keep fucking her and soon you decide to change things."

 you "How about putting it in your ass."

 girl.char "Well, what the hell, put it in!"



 $ pic = girl.get_pic("mc", and_tags=["dancer", "anal"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You put your cock deep inside her as she keeps moaning, if it wasn't so loud outide someone would have probably heard you."


 you "I'm coming! Take it."


 $ pic3 = girl.get_pic("mc", and_tags=["dancer", "cumshot"], soft=True)
 show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "That felt amazing, i'll going out, need to get a drink."

 you "Me too, i'll go and check on the others."


 show screen guild_bar


screen guild_living_room:

 image "Mods/Vaan/living_room.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏


 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 200

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "在沙发上靠一会" action [Hide("guild_living_room"), Jump("living_room_random_encounter")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_living_room"), Show("guild")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "四处看看" action [Hide("guild_living_room"), Jump("living_room_girl")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_kitchen"), Show("guild")] xsize 215 ysize 45



screen guild_kitchen:

 image "Mods/Vaan/kitchen.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏


 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 200

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "四处看看" action Jump("kitchen_girl") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_kitchen"), Show("guild")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "吃   饭" action Jump("kitchen_random_encounter") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_kitchen"), Show("guild")] xsize 215 ysize 45









screen guild_bedroom:

 image "Mods/Vaan/bedroom.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏

 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 200
     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "叫个妹子" action [Hide("guild_rest"), Jump("call_girl")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "睡上一觉" action [Hide("guild_bedroom"), Jump("end_day")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_bedroom"), Show("guild")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "洗个澡" action [Hide("guild_bedroom"), Jump("spy_showers")] xsize 215 ysize 45






screen female_only_side:
  image "Mods/Vaan/female_side.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏


  grid 2 3:
      xalign 0.5
      yalign 0.5
      spacing 200
      frame:
          xpadding 40
          ypadding 20
          xalign 0.5
          yalign 0.5
          textbutton "进入更衣室" action Jump("spy_lockers") xsize 215 ysize 45

      frame:
          xpadding 40
          ypadding 20
          xalign 0.5
          yalign 0.5
          textbutton "女性泳池" action [Hide("female_only_side"), Jump("spy_bathhouse")] xsize 215 ysize 45

      frame:
          xpadding 40
          ypadding 20
          xalign 0.5
          yalign 0.5
          textbutton "返  回" action [Hide("female_only_side"), Show("guild")] xsize 215 ysize 45

      frame:
          xpadding 40
          ypadding 20
          xalign 0.5
          yalign 0.5
          textbutton "返  回" action [Hide("female_only_side"), Show("guild")] xsize 215 ysize 45

      frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "休  息" action [Hide("female_only_side"), Jump("spy_bedroom")] xsize 215 ysize 45

      frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "naked" action [Hide("female_only_side"), Jump("spy_naked")] xsize 215 ysize 45





screen guild_tavern:

 image "Mods/Vaan/tavern.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏




 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 200
     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "小型酒吧" action Jump("drink") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "贵宾室" action Jump("entertainment") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_tavern"), Show("guild")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         text "public" yalign 0.5 xalign 0.5












screen guild_office:

  image "Mods/Vaan/office.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏




  grid 2 3:
     xalign 0.5
     yalign 0.5
     spacing 200
     frame:
         xpadding 5
         ypadding 5
         xalign 0.0
         yalign 0.5
         textbutton "Send on a mission" action [Hide("guild_office"), Show("guild_teams")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.0
         yalign 0.3
         textbutton "返  回" action [Hide("guild_office"), Show("guild")] xsize 215 ysize 45



     frame:
         xpadding 5
         ypadding 5
         xalign 0.0
         yalign 0.5
         textbutton "Do some work" action [Hide("guild_office"), Jump("office_girl")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.0
         yalign 0.3
         textbutton "Summon a girl" action [Hide("guild_office"), Jump("office_call_girl")] xsize 215 ysize 45



     frame:
         xpadding 5
         ypadding 5
         xalign 0.0
         yalign 0.3
         textbutton "返  回" action [Hide("guild_office"), Show("guild")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.0
         yalign 0.3
         textbutton "Prostitute" action [Hide("guild_office"), Jump("hooker")] xsize 215 ysize 45












screen guild_teams:
 $ triss_merigold = [g for g in able_girls if g.fullname == "Triss Merigold"]
 $ yennefer_vengerberg = [g for g in able_girls if g.fullname == "Yennefer Vengerberg"]
 $ girl1 = triss_merigold[0]
 $ girl2 = yennefer_vengerberg[0]
 $ girl1_def = girl1.get_defense()
 $ girl2_def = girl2.get_defense()
 $ team1_def = girl1.get_defense() + girl2.get_defense()


 image "Mods/Vaan/office.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏
 grid 1 2:
    xalign 0.5
    yalign 0.5
    spacing 200
    frame:
        xpadding 40
        ypadding 20
        xalign 0.0
        yalign 0.5
        textbutton "Team 1 - [team1_def]" action Jump("guild_team_1") xsize 215 ysize 45


    frame:
        xpadding 40
        ypadding 20
        xalign 0.0
        yalign 0.3
        textbutton "返  回" action [Hide("guild_teams"), Show("guild")] xsize 215 ysize 45





screen guild_gym:
 image "Mods/Vaan/gym.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏



 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 200
     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "进入更衣室" action Jump("spy_lockers") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "进入健身房" action Jump("fight") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_gym"), Show("guild")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         text "naked" yalign 0.5 xalign 0.5

screen guild_pool:
 image "Mods/Vaan/pool.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏



 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 200

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "进入泳池" action Jump("pool_alone") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "晒日光浴" action Jump("pool_party") xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_pool"), Show("guild")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "做个按摩" action Jump("mc_masseuse") xsize 215 ysize 45





screen guild_inside:

 image "Mods/Vaan/guild_inside.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏


 grid 2 4:
     xalign 0.5
     yalign 0.5
     spacing 200
     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "户外泳池" action [Hide("guild"), Show("guild_pool")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "返  回" action [Hide("guild_inside"), Show("guild")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "健身房" action [Hide("guild_inside"), Show("guild_gym")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "室  外" action [Hide("guild_inside"), Jump("buy_tavern")] xsize 215 ysize 45



     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "会议室" action [Hide("guild_inside"), Jump("buy_office")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "女更衣室" action [Hide("guild_inside"), Show("female_only_side")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "休  息" action [Hide("guild_inside"), Show("guild_rest")] xsize 215 ysize 45

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         textbutton "厨  房" action [Hide("guild_inside"), Show("guild_kitchen")] xsize 215 ysize 45



screen guild:
 image "Mods/Vaan/guild.png" xpos 0 ypos 0 fit "cover" #尺寸修改为填充全屏


 grid 1 2:            # 2列1行 修改为1列 2行
     xalign 0.5
     yalign 0.7 #Y设置为0.7
     spacing 40 #20修改为40
            

     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         #xsize 400
         #ysize 300
         textbutton "进入豪宅" action [Hide("guild"), Show("guild_inside")] xsize 215 ysize 45


     frame:
         xpadding 5
         ypadding 5
         xalign 0.5
         yalign 0.5
         #xsize 400
         #ysize 300
         textbutton "离开这里" action [Hide("guild"), Jump("main")] xsize 215 ysize 45            
            


label living_room_girl:

 image living_room = "Mods/Vaan/living_room.png"

 show living_room

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)


 if len(able_girls) == 0:
     "You stick around in the living room for a big and go back out."
     jump main










 "You go to the living room to sit on the couch and have a warm drink. You see that [girl.name] is already there."

 $ pic = girl.get_pic("public", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "She hasn't noticed you yet."


 girl.char "Oh hey, [MC.name]. How are you doing? Any missions for me?"


 you "Not for now, everything seems quiet, i'll have to check later."

 $ pic = girl.get_pic("public", and_tags=["mc"], naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "Well, let me know if you have something for me."


 "She walks away."

 menu:

    "Let her go":

     $ pic = girl.get_pic("public", and_tags=["mc", "tempt"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She walks away, teasing you with her tight ass."

     you "I'm too hungry to do anything about you, ughh."

     hide screen show_event

     show screen guild_living_room




    "Grab her and pull her close to you":

     you "Actually, i do have something for you."


     $ pic = girl.get_pic("public", and_tags=["mc", "kiss", "fondle"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     if girl.love <= 15:


         girl.char "What do you think you're doing?"

         you "I thought we could have some fun?"

         $ girl.say("slave lecture refuses")

         $ MC.change_prestige(15)
         $ girl.change_stat("obedience", -5)
         $ girl.change_stat("fear", +6)
         $ girl.change_stat("love", -7)


         hide screen show_event

         show screen guild_living_room

     else:

         girl.char "Oh, i see. I'm a bit bored too, let's have some fun."

         $ girl.say("free_play very interested")

         label living_room_girl2:

         menu:


            "On chair":

             $ pic = girl.get_pic("public", and_tags=["mc", "kiss", "fondle", "chair"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "Come over here, [girl.name]!"

             $ girl.say("free_play very interested")

             $ MC.change_prestige(4)
             $ girl.change_stat("obedience", +5)
             $ girl.change_stat("fear", -6)
             $ girl.change_stat("love", +5)


             jump living_room_girl2



            "On living room table":

             $ pic = girl.get_pic("public", and_tags=["mc", "kiss", "fondle", "table"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "Come over here, [girl.name]!"

             $ girl.say("free_play interested")
             $ MC.change_prestige(14)
             $ girl.change_stat("obedience", +3)
             $ girl.change_stat("fear", -1)
             $ girl.change_stat("love", +4)


             jump living_room_girl2




            "On living room plot":

             $ pic = girl.get_pic("public", and_tags=["mc", "kiss", "fondle", "desk"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "Come over here, [girl.name]!"

             $ girl.say("slave train interested")
             $ MC.change_prestige(7)
             $ girl.change_stat("obedience", +2)
             $ girl.change_stat("fear", -7)
             $ girl.change_stat("love", +8)



             jump living_room_girl2



            "Move on":


             jump living_room_girl3



label living_room_girl3:


 you "Let's take this off."


 if girl.love <= 25:


     $ pic = girl.get_pic("public", and_tags=["mc", "kiss", "boobs", "strip"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     $ girl.say("free_play refuses")

     $ girl.say("free_play not interested after")


     you "Sorry, thought you wanted to do something else."


     girl.char "You thought wrong."

     hide screen show_event

     call screen guild_living_room




 else:

     $ pic = girl.get_pic("public", and_tags=["mc", "kiss", "boobs", "strip"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     if not pic:

         $ pic = girl.get_pic("public", and_tags=["mc", "naked", "strip"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



     play sound s_moans

     you "How about we take this further? Get down and give me a blowjob."

     $ girl.say("free_play interested")

     $ girl.say("free_play very interested")




label living_room_girl4:

 menu:

     "On chair":


         label living_room_call_girl_chair:





         menu:


            "Service":

             "You sit on your chair while she services you."

             $ pic = girl.get_pic("service", and_tags=["public", "chair", "mc"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                  $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             $ pic = girl.get_pic("service", and_tags=["public", "chair", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                  $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl.say("slave train service success")

             $ girl.say("slave train interested")





             jump living_room_call_girl_chair











            "Sex":

             "You sit on your chair while she services you."

             $ pic = girl.get_pic("sex", and_tags=["public", "chair", "mc"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                  $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             $ pic = girl.get_pic("sex", and_tags=["public", "chair", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                  $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             you "That's it, take it deep."


             jump living_room_call_girl_chair



            "Anal":

             "You sit on your chair while she services you."

             $ pic = girl.get_pic("anal", and_tags=["public", "chair", "mc"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                  $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             $ pic = girl.get_pic("anal", and_tags=["public", "chair", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                  $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             you "Good little slut."


             jump living_room_call_girl_chair





            "Finish":

             "You have reached your limit and are ready to cum."

             menu:

               "In her mouth":

                 $ pic = girl.get_pic("mc", and_tags=["chair", "cumshot", "in-mouth", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She drinks it all with a happy look on her face."

                 you "Now that's what i call service."

                 girl.char "Thank you! Need to go back now!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 "She fixes her clothes and goes somewhere else."


                 hide screen show_event

                 show screen guild_living_room






               "On her face":

                 $ pic = girl2.get_pic("mc", and_tags=["chair", "cumshot", "on-face", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my face!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks outside."

                 hide screen show_event

                 show screen guild_living_room



               "On her body":


                 $ pic = girl.get_pic("mc", and_tags=["chair", "cumshot", "on-body", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 girl.char "I'll go freshen up now, that was great!"

                 hide screen show_event

                 show screen guild_living_room



               "Pussy":


                 "You put your dick inside her pussy and cum deep inside."


                 $ pic = girl.get_pic("mc", and_tags=["chair", "sex", "inside", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 girl.char "I'll go freshen up now, that was great!"


                 hide screen show_event

                 show screen guild_living_room


               "Ass":





                  "You put your dick inside her pussy and cum deep inside."


                  $ pic = girl.get_pic("mc", and_tags=["chair", "anal", "inside", "public"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                  girl.char "Oh how, there's so much of it."

                  you "This was amazing."

                  $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                  girl.char "See you around!"
                  hide screen show_event

                  show screen guild_living_room









             $ MC.change_prestige(10)
             $ girl.change_stat("obedience", +10)
             $ girl.change_stat("fear", -10)
             $ girl.change_stat("love", +12)

             hide screen show_event
             scene black with fade
             jump main


            "Go back":

             jump living_room_girl4




     "On living room plot":


          label living_room_call_girl_desk:





          menu:


             "Service":
                 "You sit on your desk while she services you."

                 $ pic = girl.get_pic("service", and_tags=["public", "desk", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("service", and_tags=["public", "desk", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")





                 jump living_room_call_girl_desk














             "Sex":
                 "You put her on the living room plot and start fucking her."

                 $ pic = girl.get_pic("sex", and_tags=["public", "desk", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("sex", and_tags=["public", "desk", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump living_room_call_girl_desk





             "Anal":
                 "You put her on the living room plot and start fucking her ass."

                 $ pic = girl.get_pic("anal", and_tags=["public", "desk", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("anal", and_tags=["public", "desk", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "I've been needing some relief all day."


                 jump living_room_call_girl_desk







             "Finish":
                 "You have reached your limit and are ready to cum."

                 menu:

                   "In her mouth":

                     $ pic = girl.get_pic("mc", and_tags=["desk", "cumshot", "in-mouth", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She drinks it all with a happy look on her face."

                     you "Now that's what i call service."

                     girl.char "Thank you! Need to go back now!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     "She fixes her clothes and goes back outside."


                     hide screen show_event

                     show screen guild_living_room






                   "On her face":

                     $ pic = girl2.get_pic("mc", and_tags=["desk", "cumshot", "on-face", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my face!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_living_room



                   "On her body":


                     $ pic = girl.get_pic("mc", and_tags=["desk", "cumshot", "on-body", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Oh how, there's so much of it."

                     you "This was amazing."


                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_living_room



                   "Pussy":


                     "You put your dick inside her pussy and cum deep inside."


                     $ pic = girl.get_pic("mc", and_tags=["desk", "sex", "inside", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Oh how, there's so much of it."

                     you "This was amazing."


                     girl.char "I need to go, forgot i had something to do. I'll give you a call later."

                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."


                     hide screen show_event

                     show screen guild_living_room


                   "Ass":





                      "You put your dick inside her pussy and cum deep inside."


                      $ pic = girl.get_pic("mc", and_tags=["desk", "anal", "inside", "public"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                      girl.char "Not on my clothes!"

                      you "Sorry, i couldn't hold it."

                      girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                      $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                      "She moves fast and walks to the restrooms to clean up."
                      hide screen show_event

                      show screen guild_living_room









                 $ MC.change_prestige(10)
                 $ girl.change_stat("obedience", +10)
                 $ girl.change_stat("fear", -10)
                 $ girl.change_stat("love", +12)

                 hide screen show_event
                 scene black with fade
                 jump main




             "Go back":

              jump living_room_girl4





     "On living room table":


          label living_room_call_girl_table:





          menu:


             "Service":
                 "You put her on your living room table."

                 $ pic = girl.get_pic("service", and_tags=["public", "table", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("service", and_tags=["public", "table", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "Deep in your mouth, slut."


                 jump living_room_call_girl_table














             "Sex":
                 "You sit on your table while she services you."

                 $ pic = girl.get_pic("sex", and_tags=["public", "table", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 you "You like that, little girl?"

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("sex", and_tags=["public", "table", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump living_room_call_girl_table





             "Anal":
                 "You sit on your table while she services you."

                 $ pic = girl.get_pic("anal", and_tags=["public", "table", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("anal", and_tags=["public", "table", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You can do better, come on."


                 jump living_room_call_girl_table







             "Finish":
                 "You have reached your limit and are ready to cum."

                 menu:

                   "In her mouth":

                     $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "in-mouth", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She drinks it all with a happy look on her face."

                     you "Now that's what i call service."

                     girl.char "Thank you! Need to go back now!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     "She fixes her clothes and goes back to work."


                     hide screen show_event

                     show screen guild_living_room






                   "On her face":

                     $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "on-face", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my face!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She goes back to doing what she was before that."

                     you "You did amazing."

                     girl.char "Thanks, i always aim to please, haha."

                     hide screen show_event

                     show screen guild_living_room



                   "On her body":


                     $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "on-body", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Give it to me!"

                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_living_room



                   "Pussy":


                     "You put your dick inside her pussy and cum deep inside."


                     $ pic = girl.get_pic("mc", and_tags=["table", "sex", "inside", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She goes back to doing what she was before that."

                     you "You did amazing."

                     girl.char "Thanks, i always aim to please, haha."


                     hide screen show_event

                     show screen guild_living_room


                   "Ass":





                      "You put your dick inside her pussy and cum deep inside."


                      $ pic = girl.get_pic("mc", and_tags=["table", "anal", "inside", "public"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                      girl.char "Not on my clothes!"

                      you "Sorry, i couldn't hold it."

                      girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                      $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                      "She goes back to doing what she was before that."

                      you "You did amazing."

                      girl.char "Thanks, i always aim to please, haha."
                      hide screen show_event

                      show screen guild_living_room









                 $ MC.change_prestige(10)
                 $ girl.change_stat("obedience", +10)
                 $ girl.change_stat("fear", -10)
                 $ girl.change_stat("love", +12)

                 hide screen show_event
                 scene black with fade
                 jump main




             "Go back":

              jump living_room_girl4
















label living_room_random_encounter:

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl1 = rand_choice(MC.girls)
 $ girl2 = rand_choice(MC.girls)

 "You feel like tou need to take a rest for a bit, you go and relax on the sofa."

 if len(able_girls) == 0:
     "You watched TV for an hour and feel relaxed, time to go back to work."

     jump main


 image living_room = "Mods/Vaan/living_room.png"

 show living_room


 "You go into the living room and sit down on the couch. You see [girl.name] and [girl2.name] there."

 $ pic = girl1.get_pic("public", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 you "Girls, i know you like being here, but you have your own quarters in the guild. Alternatively, you can go back to the hotel."

 girl1.char "Oh, come on. There are so many other girls there, it's so much quieter here."

 $ pic = girl2.get_pic("public", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl2.char "Besides, you shouldn't have given us a key if you didn't want us to come over to your side of the guild."


 you "I didn't..."

 play sound s_laugh

 girl1.char "Well, door is unlocked, so we invited ourselves in."


 $ pic = girl2.get_pic("public", and_tags="tempt", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl2.char "Is that a problem? Hope we aren't annoying you?"


 you "I guess it's fine."


 $ pic = girl1.get_pic("public", and_tags="tempt", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl1.char "Are you sure?"


 you "Yes, i'm heading out either way."



 if girl1.love > 25:

     girl1.char "Why the rush, stay with us. We have a surprise for you, for being such an amazing host."


     menu:


        "I guess i can stay for a bit":


         $ pic = girl1.get_pic("public", and_tags=["tempt", "strip", "boobs"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




         girl1.char "Perfect."



         "She gets on her knees and takes out your cock."


         girl1.char "Well, [girl2.name], are you going to join me or what?"



         if girl2.love < 30:


             girl2.char "What are you doing? No way!"


             $ girl2.say("slave train refused")



             $ MC.change_prestige(18)
             $ girl2.change_stat("obedience", -4)
             $ girl2.change_stat("fear", +4)
             $ girl2.change_stat("love", -3)


             $ pic = girl2.get_pic("public", and_tags=["tempt", "naked"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "I guess it's just me then."


             "She gets on the floor and starts sucking you off."

             $ pic = girl1.get_pic("public", and_tags=["service", "handjob"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                 $ pic = girl1.get_pic("public", and_tags=["service", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))








             $ girl1.say("slave train interested")






             you "That feels amazing!"


             $ girl1.say("slave magic service success")

             play sound s_moans

             $ pic = girl1.get_pic("public", and_tags=["service", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))





             you "Keep going!"


             play sound s_moans



             "You cum all over her."




             $ pic = girl1.get_pic("public", and_tags=["service", "on-face"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             girl1.char "I forgot! I was going to go to the gym!"



             you "You better now be late."


             $ pic = girl1.get_pic("public", and_tags=["aftersex"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             girl1.char "See you around, [MC.name]!"


             you "See you!"



             $ MC.change_prestige(18)
             $ girl1.change_stat("obedience", +2)
             $ girl1.change_stat("fear", -4)
             $ girl1.change_stat("love", +3)


             hide screen show_event


             call screen guild_living_room












         else:
             $ pic = girl2.get_pic("public", and_tags=["tempt", "strip", "boobs"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl2.char "Count me in."




             $ girl2.say("slave train interested")



             "They both get on their knees and start sucking you off."


             $ pic = girl2.get_pic("public", and_tags=["service"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl1.say("slave train interested")




             $ pic = girl1.get_pic("public", and_tags=["service", "handjob"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                 $ pic = girl1.get_pic("public", and_tags=["service", "pral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "That feels amazing!"


             $ girl2.say("slave magic service success")

             play sound s_moans

             $ pic = girl2.get_pic("public", and_tags=["service", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             you "Keep going!"


             play sound s_moans



             "You cum all over them."



             $ pic = girl2.get_pic("public", and_tags=["service", "on-face"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             girl2.char "There's so much!"



             $ pic = girl1.get_pic("public", and_tags=["service", "on-face"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl2.say("free_play interested")

             $ pic = girl1.get_pic("public", and_tags=["aftersex"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             $ girl1.say("free_play interested")


             you "That was great, need to get going now."


             $ pic = girl2.get_pic("public", and_tags=["aftersex"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             girl1.char "Us too, see you later!"

             girl2.char "See you, [MC.name]"


             $ MC.change_prestige(18)
             $ girl2.change_stat("obedience", +5)
             $ girl2.change_stat("fear", -2)
             $ girl2.change_stat("love", +2)

             $ MC.change_prestige(18)
             $ girl1.change_stat("obedience", +2)
             $ girl1.change_stat("fear", -4)
             $ girl1.change_stat("love", +3)


             hide screen show_event


             call screen guild_living_room




        "I have to go":


         girl1.char "Okay, see you."



         hide screen show_event


         call screen guild_living_room









 else:

     girl1.char "Okay, see you."



     hide screen show_event


     call screen guild_living_room

label hooker:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)
 $ score = girl.get_stat("libido")

 show screen night(girl.profile)

 "You see of the girls preparing for the night and you come up with an idea to make extra money"

 you "[girl.name], i want you to be a hooker for the night, go put on something slutty for the night and come back"

 girl.char "Do you like watching me take my clothes off? I don't mind, you can watch!"
 show screen show_event(girl.get_pic("strip",   and_tags=["naked", "panties"]), x=config.screen_width, y=int(config.screen_height*0.8))

 if score >= 100:
      girl.char "I love it when you watch me take my clothes off, do you think i'm hot?"
      $ pic3 = girl.get_pic("strip",   and_tags=["lingerie", "naked"], strict=True)
      show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 with fade

 girl.char "How does this look, [MC.name]?"

 $ pic1 = girl.get_pic("hooker", strict=True)

 show screen show_event(pic1, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade

 you "That's amazing, go out and let them have you!"

 "Crowds started to gather just outside the door as you hear her moans. You come closer to see how she is doing."

 girl.char "I'm here boys, come get me."
 $ pic5 = girl.get_pic("hooker", "public", strict=True)

 show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 "They started to touch and strip her, she's in for a huge fucking."

 "She can't stop it now even if she wanted to."

 girl.char "Let me take care of that for you, oh and you too. Wow, there's so many of you!"
 $ pic2 = girl.get_pic("service",  and_tags=["hooker"], strict=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


 $ renpy.show_screen("show_img", brothel.pic, _layer = "master")

 girl.char "Fuck me harder! Boss said you can have me any way you like, as long as you pay!"
 $ pic2 = girl.get_pic("sex",  and_tags=["hooker"], strict=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade

 girl.char "Make me your whore, fuck me harder!"
 $ pic3 = girl.get_pic("sex",  and_tags=["hooker"], strict=True)
 show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade

 girl.char "Keep going boys, i can take a lot more!"

 $ pic = girl.get_pic("anal",  and_tags=["hooker"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade


 girl.char "You guys can come too, let's do it!"


 $ pic = girl.get_pic("group",  and_tags=["hooker"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade


 girl.char "Yes!!! Give it to me!"


 $ pic = girl.get_pic("group",  and_tags=["hooker", "cumshot"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


 with fade





 girl.char "I don't think i can take anymore, but you guys go inside and have fun!"

 hide screen show_event
 $ renpy.show_screen("show_img", brothel.pic, _layer = "master")
 with fade
 "After some time, the girl comes back covered in cum."

 girl.char "I serviced as much as i could, boss. They all seemed to enjoy it"

 $ pic4 = girl.get_pic("aftersex",   and_tags=["hooker", "cumshot"], strict=True)
 show screen show_event(pic4, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 you "That's great, go back. You did an amazing job!"

 girl.char "They fucked me so hard, i need some rest."


 $ girl2.change_stat("obedience", +6)
 $ girl2.change_stat("fear", -5)
 $ girl2.change_stat("love", +3)

 $ MC.interactions -= 2

 scene black with fade
 hide screen show_event
 show screen home

 jump main

label kitchen_random_encounter:

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl1 = rand_choice(MC.girls)
 $ girl2 = rand_choice(MC.girls)

 "You feel hungry and go to the kitchen."

 if len(able_girls) == 0:
     "You had some food and you're no longer hungry, you go back to your daily routines."

     jump main


 image kitchen = "Mods/Vaan/kitchen.png"

 show kitchen


 "You go into the kitchen and prepare some food. You see [girl.name] and [girl2.name] there."

 $ pic = girl1.get_pic("waitress", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 you "Girls, i know you like being here, but you have your own quarters in the guild. Alternatively you can go back to the hotel."

 girl1.char "Oh, come on. There are so many other girls there, it's so much quieter here."

 $ pic = girl2.get_pic("waitress", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl2.char "Besides, you shouldn't have given us a key if you didn't want us to come over to your side of the guild."


 you "I didn't..."

 play sound s_laugh

 girl1.char "Well, door is unlocked, so we invited ourselves in."


 $ pic = girl2.get_pic("waitress", and_tags="tempt", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl2.char "Is that a problem? Hope we aren't annoying you?"


 you "I guess it's fine."


 $ pic = girl1.get_pic("waitress", and_tags="tempt", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl1.char "Are you sure?"


 you "Yes, i'm heading out either way."



 if girl1.love > 25:

     girl1.char "Why the rush, stay with us. We have a surprise for you, for being such an amazing host."


     menu:


        "I guess i can stay for a bit":


         $ pic = girl1.get_pic("waitress", and_tags=["tempt", "strip", "boobs"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




         girl1.char "Perfect."



         "She gets on her knees and takes out your cock."


         girl1.char "Well, [girl2.name], are you going to join me or what?"



         if girl2.love < 30:


             girl2.char "What are you doing? No way!"


             $ girl2.say("slave train refused")



             $ MC.change_prestige(18)
             $ girl2.change_stat("obedience", -4)
             $ girl2.change_stat("fear", +4)
             $ girl2.change_stat("love", -3)


             $ pic = girl2.get_pic("waitress", and_tags=["tempt", "naked"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "I guess it's just me then."


             "She gets on the floor and starts sucking you off."

             $ pic = girl1.get_pic("waitress", and_tags=["service", "handjob"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                 $ pic = girl1.get_pic("waitress", and_tags=["service", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))








             $ girl1.say("slave train interested")






             you "That feels amazing!"


             $ girl1.say("slave magic service success")

             play sound s_moans

             $ pic = girl1.get_pic("waitress", and_tags=["service", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))





             you "Keep going!"


             play sound s_moans



             "You cum all over her."




             $ pic = girl1.get_pic("waitress", and_tags=["service", "on-face"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             girl1.char "I forgot! I was going to go to the gym!"



             you "You better now be late."


             $ pic = girl1.get_pic("waitress", and_tags=["aftersex"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             girl1.char "See you around, [MC.name]!"


             you "See you!"



             $ MC.change_prestige(18)
             $ girl1.change_stat("obedience", +2)
             $ girl1.change_stat("fear", -4)
             $ girl1.change_stat("love", +3)


             hide screen show_event


             call screen guild_living_room












         else:
             $ pic = girl2.get_pic("waitress", and_tags=["tempt", "strip", "boobs"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl2.char "Count me in."




             $ girl2.say("slave train interested")



             "They both get on their knees and start sucking you off."


             $ pic = girl2.get_pic("waitress", and_tags=["service"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl1.say("slave train interested")




             $ pic = girl1.get_pic("waitress", and_tags=["service", "handjob"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                 $ pic = girl1.get_pic("waitress", and_tags=["service", "pral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "That feels amazing!"


             $ girl2.say("slave magic service success")

             play sound s_moans

             $ pic = girl2.get_pic("waitress", and_tags=["service", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             you "Keep going!"


             play sound s_moans



             "You cum all over them."



             $ pic = girl2.get_pic("waitress", and_tags=["service", "on-face"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             girl2.char "There's so much!"



             $ pic = girl1.get_pic("waitress", and_tags=["service", "on-face"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl2.say("free_play interested")

             $ pic = girl1.get_pic("waitress", and_tags=["aftersex"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             $ girl1.say("free_play interested")


             you "That was great, need to get going now."


             $ pic = girl2.get_pic("waitress", and_tags=["aftersex"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             girl1.char "Us too, see you later!"

             girl2.char "See you, [MC.name]"


             $ MC.change_prestige(18)
             $ girl2.change_stat("obedience", +5)
             $ girl2.change_stat("fear", -2)
             $ girl2.change_stat("love", +2)

             $ MC.change_prestige(18)
             $ girl1.change_stat("obedience", +2)
             $ girl1.change_stat("fear", -4)
             $ girl1.change_stat("love", +3)


             hide screen show_event


             call screen guild_living_room






























        "I have to go":


         girl1.char "Okay, see you."



         hide screen show_event


         call screen guild_living_room









 else:

     girl1.char "Okay, see you."



     hide screen show_event


     call screen guild_living_room












label kitchen_girl:

 image kitchen = "Mods/Vaan/kitchen.png"

 show kitchen

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)


 if len(able_girls) == 0:
     "You can't seem to find any girls around and the bar is empty. At least it's quiet, you pour yourself a drink and stick around for an hour, then go back out."
     jump main










 "You go to the kitchen to grab something to eat and see [girl.name]."

 $ pic = girl.get_pic("waitress", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "She hasn't noticed you yet."


 girl.char "Oh hey, [MC.name]. How are you doing? Any missions for me?"


 you "Not for now, everything seems quiet, i'll have to check later."

 $ pic = girl.get_pic("waitress", and_tags=["mc"], naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "Well, let me know if you have something for me."


 "She walks away."

 menu:

    "Let her go":

     $ pic = girl.get_pic("waitress", and_tags=["mc", "tempt"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She walks away, teasing you with her tight ass."

     you "I'm too hungry to do anything about you, ughh."

     hide screen show_event

     show screen guild_kitchen




    "Grab her and pull her close to you":

     you "Actually, i do have something for you."


     $ pic = girl.get_pic("waitress", and_tags=["mc", "kiss", "fondle"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     if girl.love <= 15:


         girl.char "What do you think you're doing?"

         you "I thought we could have some fun?"

         $ girl.say("slave lecture refuses")

         $ MC.change_prestige(15)
         $ girl.change_stat("obedience", -5)
         $ girl.change_stat("fear", +6)
         $ girl.change_stat("love", -7)


         hide screen show_event

         show screen guild_kitchen

     else:

         girl.char "Oh, i see. I'm a bit bored too, let's have some fun."

         $ girl.say("free_play very interested")

         label kitchen_girl2:

         menu:


            "On chair":

             $ pic = girl.get_pic("waitress", and_tags=["mc", "kiss", "fondle", "chair"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "Come over here, [girl.name]!"

             $ girl.say("free_play very interested")

             $ MC.change_prestige(4)
             $ girl.change_stat("obedience", +5)
             $ girl.change_stat("fear", -6)
             $ girl.change_stat("love", +5)


             jump kitchen_girl2



            "On kitchen table":

             $ pic = girl.get_pic("waitress", and_tags=["mc", "kiss", "fondle", "table"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "Come over here, [girl.name]!"

             $ girl.say("free_play interested")
             $ MC.change_prestige(14)
             $ girl.change_stat("obedience", +3)
             $ girl.change_stat("fear", -1)
             $ girl.change_stat("love", +4)


             jump kitchen_girl2




            "On kitchen plot":

             $ pic = girl.get_pic("waitress", and_tags=["mc", "kiss", "fondle", "desk"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "Come over here, [girl.name]!"

             $ girl.say("slave train interested")
             $ MC.change_prestige(7)
             $ girl.change_stat("obedience", +2)
             $ girl.change_stat("fear", -7)
             $ girl.change_stat("love", +8)



             jump kitchen_girl2



            "Move on":


             jump kitchen_girl3



label kitchen_girl3:


 you "Let's take this off."


 if girl.love <= 25:


     $ pic = girl.get_pic("waitress", and_tags=["mc", "kiss", "boobs", "strip"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     $ girl.say("free_play refuses")

     $ girl.say("free_play not interested after")


     you "Sorry, thought you wanted to do something else."


     girl.char "You thought wrong."

     hide screen show_event

     call screen guild_kitchen




 else:

     $ pic = girl.get_pic("waitress", and_tags=["mc", "kiss", "boobs", "strip"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     if not pic:

         $ pic = girl.get_pic("waitress", and_tags=["mc", "naked", "strip"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



     play sound s_moans

     you "How about we take this further? Get down and give me a blowjob."

     $ girl.say("free_play interested")

     $ girl.say("free_play very interested")




label kitchen_girl4:

 menu:

     "On chair":


         label kitchen_call_girl_chair:





         menu:


            "Service":

             "You sit on your chair while she services you."

             $ pic = girl.get_pic("service", and_tags=["waitress", "chair", "mc"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                  $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             $ pic = girl.get_pic("service", and_tags=["waitress", "chair", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                  $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl.say("slave train service success")

             $ girl.say("slave train interested")





             jump kitchen_call_girl_chair











            "Sex":

             "You sit on your chair while she services you."

             $ pic = girl.get_pic("sex", and_tags=["waitress", "chair", "mc"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                  $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             $ pic = girl.get_pic("sex", and_tags=["waitress", "chair", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                  $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             you "That's it, take it deep."


             jump kitchen_call_girl_chair



            "Anal":

             "You sit on your chair while she services you."

             $ pic = girl.get_pic("anal", and_tags=["waitress", "chair", "mc"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                  $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             $ pic = girl.get_pic("anal", and_tags=["waitress", "chair", "oral"], naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             if not pic:

                  $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             $ girl.say("slave train service success")

             $ girl.say("slave train interested")


             you "Good little slut."


             jump kitchen_call_girl_chair





            "Finish":

             "You have reached your limit and are ready to cum."

             menu:

               "In her mouth":

                 $ pic = girl.get_pic("mc", and_tags=["chair", "cumshot", "in-mouth", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She drinks it all with a happy look on her face."

                 you "Now that's what i call service."

                 girl.char "Thank you! Need to go back now!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 "She fixes her clothes and goes back to work."


                 hide screen show_event

                 show screen guild_kitchen






               "On her face":

                 $ pic = girl2.get_pic("mc", and_tags=["chair", "cumshot", "on-face", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my face!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."

                 hide screen show_event

                 show screen guild_kitchen



               "On her body":


                 $ pic = girl.get_pic("mc", and_tags=["chair", "cumshot", "on-body", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."

                 hide screen show_event

                 show screen guild_kitchen



               "Pussy":


                 "You put your dick inside her pussy and cum deep inside."


                 $ pic = girl.get_pic("mc", and_tags=["chair", "sex", "inside", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."


                 hide screen show_event

                 show screen guild_kitchen


               "Ass":





                  "You put your dick inside her pussy and cum deep inside."


                  $ pic = girl.get_pic("mc", and_tags=["chair", "anal", "inside", "waitress"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                  girl.char "Not on my clothes!"

                  you "Sorry, i couldn't hold it."

                  girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                  $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                  "She moves fast and walks to the restrooms to clean up."
                  hide screen show_event

                  show screen guild_kitchen









             $ MC.change_prestige(10)
             $ girl.change_stat("obedience", +10)
             $ girl.change_stat("fear", -10)
             $ girl.change_stat("love", +12)

             hide screen show_event
             scene black with fade
             jump main


            "Go back":

             jump kitchen_girl4




     "On kitchen plot":


          label kitchen_call_girl_desk:





          menu:


             "Service":
                 "You sit on your desk while she services you."

                 $ pic = girl.get_pic("service", and_tags=["waitress", "desk", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("service", and_tags=["waitress", "desk", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")





                 jump kitchen_call_girl_desk














             "Sex":
                 "You put her on the kitchen plot and start fucking her."

                 $ pic = girl.get_pic("sex", and_tags=["waitress", "desk", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("sex", and_tags=["waitress", "desk", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump kitchen_call_girl_desk





             "Anal":
                 "You put her on the kitchen plot and start fucking her ass."

                 $ pic = girl.get_pic("anal", and_tags=["waitress", "desk", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("anal", and_tags=["waitress", "desk", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "I've been needing some relief all day."


                 jump kitchen_call_girl_desk







             "Finish":
                 "You have reached your limit and are ready to cum."

                 menu:

                   "In her mouth":

                     $ pic = girl.get_pic("mc", and_tags=["desk", "cumshot", "in-mouth", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She drinks it all with a happy look on her face."

                     you "Now that's what i call service."

                     girl.char "Thank you! Need to go back now!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     "She fixes her clothes and goes back to work."


                     hide screen show_event

                     show screen guild_kitchen






                   "On her face":

                     $ pic = girl2.get_pic("mc", and_tags=["desk", "cumshot", "on-face", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my face!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_kitchen



                   "On her body":


                     $ pic = girl.get_pic("mc", and_tags=["desk", "cumshot", "on-body", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_kitchen



                   "Pussy":


                     "You put your dick inside her pussy and cum deep inside."


                     $ pic = girl.get_pic("mc", and_tags=["desk", "sex", "inside", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."


                     hide screen show_event

                     show screen guild_kitchen


                   "Ass":





                      "You put your dick inside her pussy and cum deep inside."


                      $ pic = girl.get_pic("mc", and_tags=["desk", "anal", "inside", "waitress"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                      girl.char "Not on my clothes!"

                      you "Sorry, i couldn't hold it."

                      girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                      $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                      "She moves fast and walks to the restrooms to clean up."
                      hide screen show_event

                      show screen guild_kitchen









                 $ MC.change_prestige(10)
                 $ girl.change_stat("obedience", +10)
                 $ girl.change_stat("fear", -10)
                 $ girl.change_stat("love", +12)

                 hide screen show_event
                 scene black with fade
                 jump main




             "Go back":

              jump kitchen_girl4





     "On kitchen table":


          label kitchen_call_girl_table:





          menu:


             "Service":
                 "You put her on your kitchen table."

                 $ pic = girl.get_pic("service", and_tags=["waitress", "table", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("service", and_tags=["waitress", "table", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "Deep in your mouth, slut."


                 jump kitchen_call_girl_table














             "Sex":
                 "You sit on your table while she services you."

                 $ pic = girl.get_pic("sex", and_tags=["waitress", "table", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 you "You like that, little girl?"

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("sex", and_tags=["waitress", "table", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump kitchen_call_girl_table





             "Anal":
                 "You sit on your table while she services you."

                 $ pic = girl.get_pic("anal", and_tags=["waitress", "table", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("anal", and_tags=["waitress", "table", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You can do better, come on."


                 jump kitchen_call_girl_table







             "Finish":
                 "You have reached your limit and are ready to cum."

                 menu:

                   "In her mouth":

                     $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "in-mouth", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She drinks it all with a happy look on her face."

                     you "Now that's what i call service."

                     girl.char "Thank you! Need to go back now!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     "She fixes her clothes and goes back to work."


                     hide screen show_event

                     show screen guild_kitchen






                   "On her face":

                     $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "on-face", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my face!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_kitchen



                   "On her body":


                     $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "on-body", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_kitchen



                   "Pussy":


                     "You put your dick inside her pussy and cum deep inside."


                     $ pic = girl.get_pic("mc", and_tags=["table", "sex", "inside", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."


                     hide screen show_event

                     show screen guild_kitchen


                   "Ass":





                      "You put your dick inside her pussy and cum deep inside."


                      $ pic = girl.get_pic("mc", and_tags=["table", "anal", "inside", "waitress"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                      girl.char "Not on my clothes!"

                      you "Sorry, i couldn't hold it."

                      girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                      $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "waitress"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                      "She moves fast and walks to the restrooms to clean up."
                      hide screen show_event

                      show screen guild_kitchen









                 $ MC.change_prestige(10)
                 $ girl.change_stat("obedience", +10)
                 $ girl.change_stat("fear", -10)
                 $ girl.change_stat("love", +12)

                 hide screen show_event
                 scene black with fade
                 jump main




             "Go back":

              jump kitchen_girl4
































label office_call_girl:

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl1 = rand_choice(MC.girls)



 if len(able_girls) == 0:


     "You can't seem to find any girls around and the bar is empty. At least it's quiet, you pour yourself a drink and stick around for an hour, then go back out."
     jump main



 image office = "Mods/Vaan/office.png"

 show office



 "You sit in your desk and decide to have some fun with one of the girls."


 $ girl = long_menu("Choose which girl to summon", [(g.name, g) for g in MC.girls])



 you "[girl.name], can you come over to my office?"


 if girl.get_stat("obedience") <= 20:

     girl.char "I'm busy right now [MC.name]. Another time."

     "She doesn't have enough obedience, it seems. I need to get her to start listening to me."

     jump main




 else:


     girl.char "Of course [MC.name]. I'll be right there."





 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "You wanted to see me?"

 you "I'm feeling a bit tired, how about you help me relax a bit?"


 if girl.get_stat("obedience") <= 35:

     girl.char "I'm busy right now [MC.name]. Another time."

     "She doesn't have enough obedience, it seems. I need to get her to start listening to me."

     hide screen show_event

     jump main


 else:

     girl.char "Of course, let's do it."


     "You step over to her and start undressing her."

     $ pic = girl.get_pic("kiss", and_tags=["strip", "office", "mc"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     if not pic:

         $ pic = girl.get_pic("kiss", and_tags=["strip", "universal", "mc"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     if not pic:

         $ pic = girl.get_pic("kiss", and_tags=["strip", "mc"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




     play sound s_moans

     girl.char "That feels good."

     girl.char "Keep going."


     $ girl.say("free_touch_kiss")


     $ pic = girl.get_pic("kiss", and_tags=["strip", "boobs", "office", "mc"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     if not pic:

         $ pic = girl.get_pic("kiss", and_tags=["strip", "naked", "mc"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))





     you "Get down, [girl.name]."


     $ pic = girl.get_pic("service", and_tags=["office", "mc"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     $ girl.say("slave train service success")


     $ pic = girl.get_pic("service", and_tags=["office", "oral", "mc"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     $ girl.say("slave train service success")


     "You grab her and lift here up, where do you want to move her?"


     label office_call_girl2:


     menu:

         "On chair":


             label office_call_girl_chair:





             menu:


                "Service":

                 "You sit on your chair while she services you."

                 $ pic = girl.get_pic("service", and_tags=["office", "chair", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("service", and_tags=["office", "chair", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump office_call_girl_chair











                "Sex":

                 "You sit on your chair while she services you."

                 $ pic = girl.get_pic("sex", and_tags=["office", "chair", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("sex", and_tags=["office", "chair", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump office_call_girl_chair



                "Anal":

                 "You sit on your chair while she services you."

                 $ pic = girl.get_pic("anal", and_tags=["office", "chair", "mc"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 $ pic = girl.get_pic("anal", and_tags=["office", "chair", "oral"], naked_filter=True, soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 if not pic:

                      $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 $ girl.say("slave train service success")

                 $ girl.say("slave train interested")


                 you "You're such a good girl."


                 jump office_call_girl_chair





                "Finish":

                 "You have reached your limit and are ready to cum."

                 menu:

                   "In her mouth":

                     $ pic = girl.get_pic("mc", and_tags=["chair", "cumshot", "in-mouth", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She drinks it all with a happy look on her face."

                     you "Now that's what i call service."

                     girl.char "Thank you! Need to go back now!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     "She fixes her clothes and goes back to work."


                     hide screen show_event

                     show screen guild_office






                   "On her face":

                     $ pic = girl2.get_pic("mc", and_tags=["chair", "cumshot", "on-face", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my face!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_office



                   "On her body":


                     $ pic = girl.get_pic("mc", and_tags=["chair", "cumshot", "on-body", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."

                     hide screen show_event

                     show screen guild_office



                   "Pussy":


                     "You put your dick inside her pussy and cum deep inside."


                     $ pic = girl.get_pic("mc", and_tags=["chair", "sex", "inside", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     girl.char "Not on my clothes!"

                     you "Sorry, i couldn't hold it."

                     girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                     $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "She moves fast and walks to the restrooms to clean up."


                     hide screen show_event

                     show screen guild_office


                   "Ass":





                      "You put your dick inside her pussy and cum deep inside."


                      $ pic = girl.get_pic("mc", and_tags=["chair", "anal", "inside", "office"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                      girl.char "Not on my clothes!"

                      you "Sorry, i couldn't hold it."

                      girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                      $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                      "She moves fast and walks to the restrooms to clean up."
                      hide screen show_event

                      show screen guild_office









                 $ MC.change_prestige(10)
                 $ girl.change_stat("obedience", +10)
                 $ girl.change_stat("fear", -10)
                 $ girl.change_stat("love", +12)

                 hide screen show_event
                 scene black with fade
                 jump main


                "Go back":

                 jump office_call_girl2



         "On couch":


              label office_call_girl_couch:





              menu:


                 "Service":
                     "You put her on your couch and push your dick in her mouth."

                     $ pic = girl.get_pic("service", and_tags=["office", "couch", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("service", and_tags=["office", "couch", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_couch














                 "Sex":
                     "You sit on your couch while she services you."

                     $ pic = girl.get_pic("sex", and_tags=["office", "couch", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("sex", and_tags=["office", "couch", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_couch





                 "Anal":
                     "You sit on your couch while she services you."

                     $ pic = girl.get_pic("anal", and_tags=["office", "couch", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("anal", and_tags=["office", "couch"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_couch







                 "Finish":
                     "You have reached your limit and are ready to cum."

                     menu:

                       "In her mouth":

                         $ pic = girl.get_pic("mc", and_tags=["couch", "cumshot", "in-mouth", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She drinks it all with a happy look on her face."

                         you "Now that's what i call service."

                         girl.char "Thank you! Need to go back now!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                         "She fixes her clothes and goes back to work."


                         hide screen show_event

                         show screen guild_office






                       "On her face":

                         $ pic = girl2.get_pic("mc", and_tags=["couch", "cumshot", "on-face", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my face!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."

                         hide screen show_event

                         show screen guild_office



                       "On her body":


                         $ pic = girl.get_pic("mc", and_tags=["couch", "cumshot", "on-body", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my clothes!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."

                         hide screen show_event

                         show screen guild_office



                       "Pussy":


                         "You put your dick inside her pussy and cum deep inside."


                         $ pic = girl.get_pic("mc", and_tags=["couch", "sex", "inside", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my clothes!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."


                         hide screen show_event

                         show screen guild_office


                       "Ass":





                          "You put your dick inside her pussy and cum deep inside."


                          $ pic = girl.get_pic("mc", and_tags=["couch", "anal", "inside", "office"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                          girl.char "Not on my clothes!"

                          you "Sorry, i couldn't hold it."

                          girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          "She moves fast and walks to the restrooms to clean up."
                          hide screen show_event

                          show screen guild_office









                     $ MC.change_prestige(10)
                     $ girl.change_stat("obedience", +10)
                     $ girl.change_stat("fear", -10)
                     $ girl.change_stat("love", +12)

                     hide screen show_event
                     scene black with fade
                     jump main




                 "Go back":

                  jump office_call_girl2



         "On desk":


              label office_call_girl_desk:





              menu:


                 "Service":
                     "You sit on your desk while she services you."

                     $ pic = girl.get_pic("service", and_tags=["office", "desk", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("service", and_tags=["office", "desk", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_desk














                 "Sex":
                     "You sit on your desk while she services you."

                     $ pic = girl.get_pic("sex", and_tags=["office", "desk", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("sex", and_tags=["office", "desk", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_desk





                 "Anal":
                     "You sit on your desk while she services you."

                     $ pic = girl.get_pic("anal", and_tags=["office", "desk", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("anal", and_tags=["office", "desk", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_desk







                 "Finish":
                     "You have reached your limit and are ready to cum."

                     menu:

                       "In her mouth":

                         $ pic = girl.get_pic("mc", and_tags=["desk", "cumshot", "in-mouth", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She drinks it all with a happy look on her face."

                         you "Now that's what i call service."

                         girl.char "Thank you! Need to go back now!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                         "She fixes her clothes and goes back to work."


                         hide screen show_event

                         show screen guild_office






                       "On her face":

                         $ pic = girl2.get_pic("mc", and_tags=["desk", "cumshot", "on-face", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my face!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."

                         hide screen show_event

                         show screen guild_office



                       "On her body":


                         $ pic = girl.get_pic("mc", and_tags=["desk", "cumshot", "on-body", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my clothes!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."

                         hide screen show_event

                         show screen guild_office



                       "Pussy":


                         "You put your dick inside her pussy and cum deep inside."


                         $ pic = girl.get_pic("mc", and_tags=["desk", "sex", "inside", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my clothes!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."


                         hide screen show_event

                         show screen guild_office


                       "Ass":





                          "You put your dick inside her pussy and cum deep inside."


                          $ pic = girl.get_pic("mc", and_tags=["desk", "anal", "inside", "office"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                          girl.char "Not on my clothes!"

                          you "Sorry, i couldn't hold it."

                          girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          "She moves fast and walks to the restrooms to clean up."
                          hide screen show_event

                          show screen guild_office









                     $ MC.change_prestige(10)
                     $ girl.change_stat("obedience", +10)
                     $ girl.change_stat("fear", -10)
                     $ girl.change_stat("love", +12)

                     hide screen show_event
                     scene black with fade
                     jump main




                 "Go back":

                  jump office_call_girl2





         "On office table":


              label office_call_girl_table:





              menu:


                 "Service":
                     "You put her on your office table."

                     $ pic = girl.get_pic("service", and_tags=["office", "table", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("service", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("service", and_tags=["office", "table", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("service", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_table














                 "Sex":
                     "You sit on your table while she services you."

                     $ pic = girl.get_pic("sex", and_tags=["office", "table", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("sex", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     you "You like that, little girl?"

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("sex", and_tags=["office", "table", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("sex", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_table





                 "Anal":
                     "You sit on your table while she services you."

                     $ pic = girl.get_pic("anal", and_tags=["office", "table", "mc"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                     if not pic:

                          $ pic = girl.get_pic("anal", and_tags=["universal", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     $ pic = girl.get_pic("anal", and_tags=["office", "table", "oral"], naked_filter=True, soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     if not pic:

                          $ pic = girl.get_pic("anal", and_tags=["universal", "oral", "mc"], naked_filter=True, soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                     $ girl.say("slave train service success")

                     $ girl.say("slave train interested")


                     you "You're such a good girl."


                     jump office_call_girl_table







                 "Finish":
                     "You have reached your limit and are ready to cum."

                     menu:

                       "In her mouth":

                         $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "in-mouth", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She drinks it all with a happy look on her face."

                         you "Now that's what i call service."

                         girl.char "Thank you! Need to go back now!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                         "She fixes her clothes and goes back to work."


                         hide screen show_event

                         show screen guild_office






                       "On her face":

                         $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "on-face", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my face!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."

                         hide screen show_event

                         show screen guild_office



                       "On her body":


                         $ pic = girl.get_pic("mc", and_tags=["table", "cumshot", "on-body", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my clothes!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."

                         hide screen show_event

                         show screen guild_office



                       "Pussy":


                         "You put your dick inside her pussy and cum deep inside."


                         $ pic = girl.get_pic("mc", and_tags=["table", "sex", "inside", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                         girl.char "Not on my clothes!"

                         you "Sorry, i couldn't hold it."

                         girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                         $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                         "She moves fast and walks to the restrooms to clean up."


                         hide screen show_event

                         show screen guild_office


                       "Ass":





                          "You put your dick inside her pussy and cum deep inside."


                          $ pic = girl.get_pic("mc", and_tags=["table", "anal", "inside", "office"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                          girl.char "Not on my clothes!"

                          you "Sorry, i couldn't hold it."

                          girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "office"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          "She moves fast and walks to the restrooms to clean up."
                          hide screen show_event

                          show screen guild_office









                     $ MC.change_prestige(10)
                     $ girl.change_stat("obedience", +10)
                     $ girl.change_stat("fear", -10)
                     $ girl.change_stat("love", +12)

                     hide screen show_event
                     scene black with fade
                     jump main




                 "Go back":

                  jump office_call_girl2




























label drink:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl1 = rand_choice(MC.girls)
 $ girl2 = rand_choice(MC.girls)
 if len(able_girls) == 0:


     "You can't seem to find any girls around and the bar is empty. At least it's quiet, you pour yourself a drink and stick around for an hour, then go back out."
     jump main

 image tavern = "Mods/Vaan/tavern.png"

 show tavern

 "You walk into the guild Tavern to have a drink."

 "You see [girl1.name] acting as the bartender to serve you and the girls around."

 $ pic = girl1.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl1.char "Can i get you anything, [MC.name]?"

 you "Just get me a beer, i'll go and sit down for a bit."

 girl1.char "Sure, i'll get [girl2.name] to bring it to you, enjoy!"

 "After a while you see [girl2.name] with your drink."

 $ pic = girl2.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl2.char "Here you go, mind if i sit with you?"


 menu:

    "Yes":

     you "Sorry, [girl2.name]. I'd rather drink alone."

     $ pic = girl2.get_pic("waitress", and_tags=["public"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     girl2.char "I understand, call me if you need anything."

     "She goes back to the bar."

     "You pour yourself a drink and stick around for an hour, then go back out."

     scene black with fade
     jump main


    "No, be my guest.":

     "She sits next to you and you chat with her for a few minutes."

     $ pic = girl2.get_pic("profile", naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_laugh

     you "Thanks for your time, you know we could go back to my room upstairs..."

     if girl2.love < 30:

         girl2.char "Sorry, but i'll have to help [girl1.name]. Some of the girls might come in later and it's good to have someone tending the bar."

         girl2.char "Besides, it's quite fun."

         "You talk with her for a bit more, then finish your drinks and go out of the Tavern."

         $ girl.change_stat("obedience", -3)
         $ girl.change_stat("love", -4)
         hide screen show_event
         scene black with fade
         show screen guild_tavern


     else:
         girl2.char "I have an even better idea, come with me!"

         you "She takes you to a secluded area in the tavern, you can still hear the other girls talking, but the music is quite cloud, no one will notice you're here."


         "While you're looking around, she gives you a kiss."


         $ pic = girl2.get_pic("mc", and_tags=["kiss", "public", "public"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She pushes her body onto you and you grab her and start taking her clothes off."


         $ pic = girl2.get_pic("mc", and_tags=["kiss", "public", "fondle", "grope", "public"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         girl2.char "[girl1.name] is fun and having our own Guild is nice, it means we can drink whenever we want, but it gets a bit boring. I'm glad you came in."


         you "Me too, i came for a drink, but will leave with a lot more, it seems."


         play sound s_laugh


         $ pic = girl2.get_pic("mc", and_tags=["kiss", "public", "fondle", "grope", "strip", "naked", "public"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She gets on her knees and looks at you."

         girl2.char "I hope you're ready!"

         $ pic = girl2.get_pic("mc", and_tags=["service", "public", "public"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She takes out your cock and plays with it."

         you "Suck it, [girl2.name]."


         $ pic = girl2.get_pic("mc", and_tags=["service", "oral", "public", "public"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You hope nobody sees you while you're enjoying her blowjob."


         "You keep looking around to see if anyone is watching."

         $ pic = girl2.get_pic("mc", and_tags=["service", "deep", "public", "public"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "A few more girls showed up, they must have finished their shift at the Hotel."

         "They're making so much noise and the loud music means no one can hear you."

         you "That's enough babe, i want to fuck you."

         if girl2.love < 50:

             girl2.char "Sorry, [MC.name]. I need to be back to [girl1.name] soon. It's getting busier."

             "She keeps sucking it harder and you seen feel like you're about to cum."


             menu:

               "In her mouth":

                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "in-mouth", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She drinks it all with a happy look on her face."

                 you "Now that's what i call service."

                 girl2.char "Thank you! Need to go back now!"
                 $ pic = girl2.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 "She fixes her clothes and goes back to the bar."






               "On her face":

                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "on-face", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl2.char "Not on my face!"

                 you "Sorry, i couldn't hold it."

                 girl2.char "I'll have to go wash up, before any of the other girls notice!"
                 $ pic = girl2.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."



               "On her body":


                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "on-body", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl2.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl2.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                 $ pic = girl2.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."




             $ MC.change_prestige(1)
             $ girl.change_stat("obedience", +10)
             $ girl.change_stat("fear", -10)
             $ girl.change_stat("love", +12)
             scene black with fade
             jump main



         else:

             "I guess we could, but you'll have to cum fast!"

             you "Only way i know how! Wait what?"

             "While you make jokes she takes off her panties and pushes herself onto your cock."


             $ pic = girl2.get_pic("mc", and_tags=["sex", "doggy", "public", "public"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "You hope nobody sees you while you grab her from behind and thrust your dick in her."


             "You keep looking around to see if anyone is watching."

             $ pic = girl2.get_pic("mc", and_tags=["doggy", "public", "public"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "A few more girls showed up, they must have finished their shift at the Hotel."

             "They're making so much noise and the loud music means no one can hear you."



             play sound s_moans


             you "You have to keep quiet, otherwise people will notice!"


             menu:

               "In her mouth":

                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "in-mouth", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She drinks it all with a happy look on her face."

                 you "Now that's what i call service."

                 girl2.char "Thank you! Need to go back now!"

                 $ pic = girl2.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 "She fixes her clothes and goes back to the bar."




               "On her face":

                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "on-face", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl2.char "Not on my face!"

                 you "Sorry, i couldn't hold it."

                 girl2.char "I'll have to go wash up, before any of the other girls notice!"

                 $ pic = girl2.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."



               "On her body":


                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "on-body", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl2.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl2.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                 "She moves fast and walks to the restrooms to clean up."




               "Inside":

                 $ pic = girl2.get_pic("mc", and_tags=["public", "cumshot", "on-body", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "You came deep inside her, her legs are shaking and the cum started to drip out."


                 girl2.char "Oh wow, that's a lot!"


                 $ pic = girl2.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "public"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She picks up her clothes and goes to the restroom."

                 "You go back to finish your drink and you leave after."





             $ MC.change_prestige(1)
             $ girl.change_stat("obedience", +6)
             $ girl.change_stat("fear", -7)
             $ girl.change_stat("love", +5)
             scene black with fade
             jump main




label call_girl:

 image rest = "Mods/Vaan/rest.png"
 show rest


 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)


 "You lie in bed and think about the day you had. You can't seem to fall asleep and you wonder if you can call one of the girls staying in the guild house to come over."


 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "You called, boss?"

 you "Yes, i wondered if you would like to come sleep here tonight, i want to have some fun."


 if girl.love < 15:

     girl.char "Sorry, boss. I'll need to get some rest. Another work day tomorrow."

     you "Ah, that's fair. I'll see you tomorrow then."

     girl.char "Have a goodnight sleep too, [MC.name]."

     "You stay awake for a bit more and you finally go back to sleep."
     $ girl.change_stat("obedience", -6)
     $ girl.change_stat("fear", +3)
     $ girl.change_stat("love", -2)

     jump end_day




 else:
     girl.char "I couldn't sleep either. Let's do it."

     play sound s_laugh



     $ pic = girl.get_pic("mc", and_tags=["rest", "tempt"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She climbs on the bed and looks at you with a smile."


     girl.char "Do you like what i'm wearing?"

     you "I do! You look so hot!"

     $ pic = girl.get_pic("mc", and_tags=["rest", "kiss", "fondle"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "You touch her everywhere and kiss her while she lets out a moan."

     play sound s_mmmh

     $ pic = girl.get_pic("mc", and_tags=["rest", "kiss", "fondle", "strip"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "You take off her clothes slowly while you kiss her, she touches your cock and smiles."


     girl.char "Let's see what we have here!"


     $ pic = girl.get_pic("mc", and_tags=["rest", "handjob"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "She plays with your cock for a bit and teases you even more."

     girl.char "Time to take this off completely."



     $ pic = girl.get_pic("mc", and_tags=["rest", "strip", "naked"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She takes off all her clothes and goes back to on your dick."


     you "Suck it, [girl.name]."


     $ pic = girl.get_pic("mc", and_tags=["rest", "service", "oral"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She takes it in her mouth and looks at you."

     girl.char "I'm so happy i came, would have been all alone in my room tonight."


     you "I'm happy you came too."

     $ pic = girl.get_pic("mc", and_tags=["rest", "service", "oral"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She keeps sucking on your cock and you're soon ready to cum."

     girl.char "Cum wherever you want, boss! I want it all!"

     menu:

       "In her mouth":

         $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "in-mouth"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Yes, i want it all, give it to me!"

         "You spray it in her mouth and she drinks it all with a smile."

         girl.char "That was great! Thank you!"



       "On her face":

         $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "on-face"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Yes, i want it all, give it to me!"

         "You spray it on her face and she takes it all with a smile."

         girl.char "That was great! Thank you!"

       "On her body":


         $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "on-body"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Yes, i want it all, give it to me!"

         "You cum all over her. While she laughs."

         girl.char "That was great! It's all over me"



     you "How about we keep going? I want to to fuck!"


     girl.char "Blowjob wasn't enough eh? I don't know..."

     if girl.love < 50:


         girl.char "I'm too tired, how about we just go to sleep?"

         you "Okay, i guess we can. I got proper service at least!"

         girl.char "And i got cum all over, we both win haha!"

         $ pic = girl.get_pic("mc", and_tags=["rest", "aftersex", "wet"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         girl.char "I'm just going to go wash up, maybe take a shower."

         you "That's fine, i'm so tired i can hardly stay awake either way."

         "You manage to go to finally go to sleep for the night."
         $ girl.change_stat("obedience", +3)
         $ girl.change_stat("fear", -3)
         $ girl.change_stat("love", +3)

         jump end_day


     if girl.love > 50:


         girl.char "Ah, what the hell. Let's do it!"

         "Without waiting she pushes you on the bed and jumps on your cock."


         $ pic = girl.get_pic("mc", and_tags=["rest", "sex", "cowgirl"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         play sound s_mmmh

         you "Hell, yes! Keep going [girl.name]!"

         girl.char "I can really use a good fucking and since you've been so nice to me lately, i don't see why not!"

         $ pic = girl.get_pic("mc", and_tags=["rest", "sex", "doggy"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You bend her over and start fucking her from behind."

         "She doesn't stop moaning the entire time, she's loving your cock."

         play sound s_mmmh


         you "Come over here!"

         girl.char "Do it harder!"


         $ pic = girl.get_pic("mc", and_tags=["rest", "sex", "spooning"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You keep fucking her like there's no tomorrow! She's loving it!"

         girl.char "Yes, [MC.name], it's so deep.!"



         $ pic = girl.get_pic("mc", and_tags=["rest", "sex", "piledriver"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         "You feel like you're close to cumming, you won't be able to hold it."


         $ pic = girl.get_pic("mc", and_tags=["rest", "sex", "orgasm"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         play sound s_mmmh


         "She came hard and hearing the sounds she's making you can't hold it any longer."

         menu:

           "In her mouth":
             "You take it out and push it in her mouth."
             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "in-mouth"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "Tastes so nice."

             "You spray it in her mouth and she drinks it all with a smile."

             girl.char "That was great! Thank you!"


           "On her face":
             "You stop fucking her and get your dick close to her face."

             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "on-face"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "Yes, on my face!"

             "You spray it on her face and she takes it all with a smile."

             girl.char "That was great! Thank you!"
           "On her body":

             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "on-body"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             girl.char "Yes, i want it all, cum all over me!"

             "You cum all over her. While she laughs."

             girl.char "Oh wow, i won't be able to move properly for a while, i need rest."



           "Inside her":

             "You start fucking her harder and faster."

             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "inside"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "It's inside me, it feels so good!"

             "You cum deep inside her and you take your cock out to admire your work!"

             $ pic = girl.get_pic("mc", and_tags=["rest", "aftersex", "cumshot"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She manages to gather some strength to lift herself up and looks at you with a smile."

             girl.char "This was amazing, i'll go wash up and then we can go to sleep!"


     $ pic = girl.get_pic("mc", and_tags=["rest", "aftersex", "wet"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     you "That's fine, i'm so tired i can hardly stay awake either way."

     "You manage to go to finally go to sleep for the night."

     $ MC.change_prestige(1)
     $ girl.change_stat("obedience", +10)
     $ girl.change_stat("fear", -10)
     $ girl.change_stat("love", +12)



     jump end_day





































label wet_naked:

 image naked = "mods/vaan/naked.png"
 show naked



 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)
 $ girl2 = rand_choice(MC.girls)
 $ girl_def = 4 + girl.get_defense()

 "You try and enter the naked to wet on the girls dressing up."

 "This area is meant for them only, so if you're seen, they might get angry."

 "Do you still want to enter?"

 menu:

    "Yes":

     $ tt = show_tt("top_right")
     $ chal = renpy.call_screen("challenge_menu", challenges=[("wet", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
     hide screen tool

     if chal == "speed":
         $ renpy.block_rollback()
         you "You move closer to the naked area, hoping to see someone and not get caught!"

         play sound s_laugh

         "You hear some laughing. You try to get closer."

         call challenge(chal, girl_def) from _call_challenge_85 # result is stored in the _show screen home variable

         $ r = _return

         if r:

             $ pic = girl.get_pic("wet", and_tags=["naked", "public"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             "You successfully see [girl.name] in the shower, she hasn't noticed you yet."



             $ pic = girl.get_pic("wet", and_tags=["naked", "strip", "public"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "You can hardy control yourself, you might get caught, but you're starting to feel like this is worth it."


             menu:


                "Continue weting":


                 $ tt = show_tt("top_right")
                 $ chal = renpy.call_screen("challenge_menu", challenges=[("wet", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
                 hide screen tool

                 if chal == "speed":
                     $ renpy.block_rollback()
                     you "You move even closer, you see another girl."

                     play sound s_laugh

                     "You hear some laughing. You try to get closer."

                     call challenge(chal, girl_def) from _call_challenge_86 # result is stored in the _show screen home variable

                     $ r = _return

                     if r:

                          $ pic = girl2.get_pic("wet", and_tags=["naked", "wet", "public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                          "You successfully see [girl2.name] in the shower, she hasn't noticed you yet."

                          girl2.char "So, [girl.name], what have you been up to lately?"



                          $ pic = girl2.get_pic("wet", and_tags=["naked", "strip", "public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          "You can hardy control yourself, you might get caught, but you're starting to feel like this is worth it."


                          girl.char "Not much, just needed to relax in the spa for a bit, had a great training session!"



                          girl2.char "That's amazing, i need to get stronger too!"


                          $ pic = girl.get_pic("wet", and_tags=["naked", "strip", "public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                          "You feel like you've seen enough and you leave before anyone sees you."


                          hide screen show_event



                          jump main



                     else:

                         "You've been spotted!"


                         $ pic = girl.get_pic("wet", and_tags=["naked", "angry", "sensitivity"], soft=True)
                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                         girl.char "What are you doing here?"

                         you "I'm sorry, i was looking for the public spa and got lost!"


                         if girl.love <= 60:

                             girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                             girl2.char "Let's send kick him out!"


                             "The girls surround you and start hitting you. You're being dragged to the out of the room room."


                             hide screen show_event


                             jump main



                         else:

                             girl.char "Couldn't resist peaking huh? I knew i made the right choice coming to the public baths."

                             $ pic = girl.get_pic("wet", and_tags=["naked", "libido"], soft=True)
                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                             girl.char "Why don't you join me?"



                             menu:

                                "Hell yes!":


                                 hide screen show_event
                                 with fade


                                 jump main



                                "I have to go!":


                                 $ pic = girl.get_pic("wet", and_tags=["naked", "libido"], soft=True)
                                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                                 "You see the girl watching you, she wants to come in the shower with her."


                                 "You wonder if this could be a trap and she'll call the other girls! Even though there's no one else here, so it's obviously not!"

                                 you "Sorry...I have to go!"


                                 girl.char "Really? I would miss on the opportunity to take a shower with me?"

                                 girl.char "Humph, fine, just leave me alone!"


                                 "Either way, you want to leave and you head back, she looks disappointed."


                                 hide screen show_event
                                 with fade


                                 jump main













                "Take your cock out and masturbate":


                 "Take your cock out and masturbate"










                "Leave":

                 "Take your cock out and masturbate"











             hide screen show_event
             jump main



         else:

             "You've been spotted!"


             $ pic = girl.get_pic("wet", and_tags=["naked", "angry", "sensitivity"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             girl.char "What are you doing here?"

             you "I'm sorry, i was looking for the public spa and got lost!"


             if girl.love <= 60:

                 girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                 girl2.char "Let's kick him out!"


                 "The girls surround you and start hitting you. You're being dragged out of the room."


                 hide screen show_event


                 jump main



             else:

                 girl.char "Couldn't resist peaking huh? I knew i made the right choice coming to the public baths."

                 $ pic = girl.get_pic("wet", and_tags=["naked", "libido"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "Why don't you join me?"



                 menu:


                    "Hell yes!":


                     hide screen show_event
                     with fade


                     jump main



                    "I have to go!":


                     $ pic = girl.get_pic("wet", and_tags=["naked", "libido"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                     "You see the girl watching you, she wants to come in the shower with her."


                     "You wonder if this could be a trap and she'll call the other girls! Even though there's no one else here, so it's obviously not!"

                     you "Sorry...I have to go!"


                     girl.char "Really? I would miss on the opportunity to take a shower with me?"

                     girl.char "Humph, fine, just leave me alone!"


                     "Either way, you want to leave and you head back, she looks disappointed."


                     hide screen show_event
                     with fade


                     jump main




































label wet_rest:



  image rest = "mods/vaan/rest.png"
  show rest



  $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
  $ girl = rand_choice(MC.girls)
  $ girl2 = rand_choice(MC.girls)
  $ girl_def = 4 + girl.get_defense()
  $ ntr_girl = girl.has_trait("Owned")


  "You try and enter the rest to wet on a girl."

  "This area is meant for girls only, so if you're seen, they might get angry."

  "Do you still want to enter?"

  menu:

     "Yes":

      $ tt = show_tt("top_right")
      $ chal = renpy.call_screen("challenge_menu", challenges=[("wet", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
      hide screen tool

      if chal == "speed":
          $ renpy.block_rollback()
          you "You move closer to the rest area, hoping to see someone and not get caught!"

          play sound s_laugh

          "You wonder which room to pick, you choose a random one, you open it and check around the room. It's [girl.name]'s room!" #there will be a second event, random choice between sleeping and awake

          call challenge(chal, girl_def) from _call_challenge_87 # result is stored in the _show screen home variable

          $ r = _return

          if r:

              $ pic = girl.get_pic("wet", and_tags=["rest"], strict=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


              "You successfully see [girl.name] sleeping in bed, she hasn't noticed you yet. You close the door behind you and move closer."



              $ pic = girl.get_pic("wet", and_tags=["rest"], strict=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

              "You can hardy control yourself, you might get caught, but you're starting to feel like this is worth it."



          else:

              "You've been spotted!"


              $ pic = girl.get_pic("wet", and_tags=["rest", "angry"], strict=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


              girl.char "What are you doing here?"

              you "I'm sorry, i got drunk and thought this was my room!"


              if girl.love <= 60:

                  girl.char "Yeah, right! Get away from me!"

                  "She stars screaming and you can see other girls open their doors and run towards her room to see what happened. They see you and don't look happy."

                  girl2.char "Let's kick him out!"


                  "The girls surround you and start hitting you. You're being dragged out of the room."


                  hide screen show_event


                  jump main



              else:

                  you "Couldn't resist peaking huh? I knew i made the right choice coming to the public baths."

                  $ pic = girl.get_pic("wet", and_tags=["rest", "libido"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                  girl.char "Why don't you join me?"



                  menu:


                     "Hell yes!":


                      hide screen show_event
                      with fade


                      jump main



                     "I have to go!":


                      $ pic = girl.get_pic("wet", and_tags=["rest", "libido"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                      "You see the girl watching you, she wants you to come in bed with her."


                      "You wonder if this could be a trap and she'll call the other girls! Even though there's no one else here, so it's obviously not!"

                      you "Sorry...I have to go!"


                      girl.char "Really? I would miss on the opportunity to fuck me?"

                      girl.char "Humph, fine, just leave me alone!"


                      "Either way, you want to leave and you head back, she looks disappointed."


                      hide screen show_event
                      with fade


                      jump main











              menu:


                 "Get closer":


                  $ tt = show_tt("top_right")
                  $ chal = renpy.call_screen("challenge_menu", challenges=[("wet", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
                  hide screen tool

                  if chal == "speed":
                      $ renpy.block_rollback()
                      you "You move even closer."

                      play sound s_laugh

                      "She hasn't heard you so far."

                      you "This could be my lucky day!"

                      call challenge(chal, girl_def) from _call_challenge_88 # result is stored in the _show screen home variable

                      $ r = _return

                      if r:

                           $ pic = girl2.get_pic("wet", and_tags=["rest"], soft=True)
                           show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                           "You come closer to [girl.name] and wonder whether you should turn back or keep going."

                           you "A little bit more won't hurn now would it?"





                           menu:

                            "Touch her":

                             "You feel like you can go further, hopefully she won't notice! Right?"


                             label sleep_touch:

                             menu:


                                "Grab her boobs":

                                 $ tt = show_tt("top_right")
                                 $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
                                 hide screen tool

                                 if chal == "speed":
                                     $ renpy.block_rollback()
                                     you "You start playing with her."

                                     $ pic = girl2.get_pic("wet", and_tags=["rest", "fondle"], soft=True)
                                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                                     play sound s_laugh

                                     you "Your tits feel so good"

                                     you "This could be my lucky day!"

                                     call challenge(chal, girl_def) from _call_challenge_89 # result is stored in the _show screen home variable

                                     $ r = _return

                                     if r:

                                          $ pic = girl2.get_pic("wet", and_tags=["rest", "fondle"], soft=True)
                                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                          you "You're all mine now babe!"

                                          "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                                          menu:

                                            "Do it some more":

                                             hide screen show_event

                                             jump sleep_touch





                                            "Go further":


                                             jump sleep_round2





                                            "Go back":


                                             "You decide to leave the room before she sees you."


                                             you "This was good, should come back again another night."


                                             hide screen show_event

                                             jump main















                                     else:

                                         "You've been spotted!"


                                         $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "sensitivity"], soft=True)
                                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                         girl.char "What are you doing here?"

                                         you "I'm sorry, i was looking for the public spa and got lost!"


                                         if girl.love <= 60:

                                             girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                                             girl2.char "Let's kick him out!"


                                             "The girls surround you and start hitting you. You're being dragged out of the room."


                                             hide screen show_event


                                             jump main





                                "Grab her ass":

                                     $ tt = show_tt("top_right")
                                     $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
                                     hide screen tool

                                     if chal == "speed":
                                         $ renpy.block_rollback()
                                         you "You start playing with her."

                                         $ pic = girl2.get_pic("wet", and_tags=["rest", "grope"], soft=True)
                                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                                         play sound s_laugh

                                         you "Your tits feel so good"

                                         you "This could be my lucky day!"

                                         call challenge(chal, girl_def) from _call_challenge_90 # result is stored in the _show screen home variable

                                         $ r = _return

                                         if r:

                                              $ pic = girl2.get_pic("wet", and_tags=["rest", "grope"], soft=True)
                                              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                              you "You're all mine now babe!"

                                              "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                                              menu:

                                                "Do it some more":


                                                 hide screen show_event

                                                 jump sleep_touch





                                                "Go further":


                                                 jump sleep_round2





                                                "Go back":


                                                 "You decide to leave the room before she sees you."


                                                 you "This was good, should come back again another night."


                                                 hide screen show_event

                                                 jump main


                                         else:

                                             "You've been spotted!"


                                             $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "sensitivity"], soft=True)
                                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                             girl.char "What are you doing here?"

                                             you "I'm sorry, i was looking for the public spa and got lost!"


                                             if girl.love <= 60:

                                                 girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                                                 girl2.char "Let's kick him out!"


                                                 "The girls surround you and start hitting you. You're being dragged out of the room."


                                                 hide screen show_event


                                                 jump main





                                "Finger her pussy":

                                     $ tt = show_tt("top_right")
                                     $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
                                     hide screen tool

                                     if chal == "speed":
                                         $ renpy.block_rollback()
                                         you "You start playing with her."

                                         $ pic = girl2.get_pic("wet", and_tags=["rest", "finger"], soft=True)
                                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                                         play sound s_laugh

                                         you "Your tits feel so good"

                                         you "This could be my lucky day!"

                                         call challenge(chal, girl_def) from _call_challenge_91 # result is stored in the _show screen home variable

                                         $ r = _return

                                         if r:

                                              $ pic = girl2.get_pic("wet", and_tags=["rest", "finger"], soft=True)
                                              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                              you "You're all mine now babe!"

                                              "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                                              menu:

                                                "Do it some more":


                                                 hide screen show_event

                                                 jump sleep_touch





                                                "Go further":


                                                 jump sleep_round2





                                                "Go back":


                                                 "You decide to leave the room before she sees you."


                                                 you "This was good, should come back again another night."


                                                 hide screen show_event

                                                 jump main


                                         else:

                                             "You've been spotted!"


                                             $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "sensitivity"], soft=True)
                                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                             girl.char "What are you doing here?"

                                             you "I'm sorry, i was looking for the public spa and got lost!"


                                             if girl.love <= 60:

                                                 girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                                                 girl2.char "Let's kick him out!"


                                                 "The girls surround you and start hitting you. You're being dragged out of the room."


                                                 hide screen show_event


                                                 jump main










                                "Finger her ass":

                                     $ tt = show_tt("top_right")
                                     $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
                                     hide screen tool

                                     if chal == "speed":
                                         $ renpy.block_rollback()
                                         you "You start playing with her."

                                         $ pic = girl2.get_pic("wet", and_tags=["rest", "fisting"], soft=True)
                                         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                                         play sound s_laugh

                                         you "Your tits feel so good"

                                         you "This could be my lucky day!"

                                         call challenge(chal, girl_def) from _call_challenge_92 # result is stored in the _show screen home variable

                                         $ r = _return

                                         if r:

                                              $ pic = girl2.get_pic("wet", and_tags=["rest", "fisting"], soft=True)
                                              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                              you "You're all mine now babe!"

                                              "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                                              menu:

                                                "Do it some more":


                                                 hide screen show_event

                                                 jump sleep_touch





                                                "Go further":


                                                 jump sleep_round2





                                                "Go back":


                                                 "You decide to leave the room before she sees you."


                                                 you "This was good, should come back again another night."


                                                 hide screen show_event

                                                 jump main


                                         else:

                                             "You've been spotted!"


                                             $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "sensitivity"], soft=True)
                                             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                                             girl.char "What are you doing here?"

                                             you "I'm sorry, i was looking for the public spa and got lost!"


                                             if girl.love <= 60:


                                                 girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                                                 girl2.char "Let's kick him out!"


                                                 "The girls surround you and start hitting you. You're being dragged out of the room."

                                                 hide screen show_event


                                                 jump main

                            "Turn back":


                             "You decide to leave and go back, this isn't worth it."

                             hide screen show_event

                             jump main








                      else:

                          "You've been spotted!"


                          $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "sensitivity"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                          girl.char "What are you doing here?"

                          you "I'm sorry, i was looking for the public spa and got lost!"


                          if girl.love <= 60:

                              girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                              girl2.char "Let's kick him out!"


                              "The girls surround you and start hitting you. You're being dragged out of the room."


                              hide screen show_event


                              jump main



                          else:

                              girl.char "Couldn't resist peaking huh? I knew i made the right choice coming to the public baths."

                              $ pic = girl.get_pic("wet", and_tags=["rest", "libido"], soft=True)
                              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                              girl.char "Why don't you join me?"



                              menu:

                                 "Hell yes!":


                                  hide screen show_event
                                  with fade


                                  jump main



                                 "I have to go!":


                                  $ pic = girl.get_pic("wet", and_tags=["rest", "libido"], soft=True)
                                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                                  "You see the girl watching you, she wants to come in the shower with her."


                                  "You wonder if this could be a trap and she'll call the other girls! Even though there's no one else here, so it's obviously not!"

                                  you "Sorry...I have to go!"


                                  girl.char "Really? I would miss on the opportunity to take a shower with me?"

                                  girl.char "Humph, fine, just leave me alone!"


                                  "Either way, you want to leave and you head back, she looks disappointed."


                                  hide screen show_event
                                  with fade


                                  jump main







              hide screen show_event
              jump main


label sleep_round2:

 "You decide to take her clothes off."

 $ pic = girl2.get_pic("wet", and_tags=["rest", "naked"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 you "Now, i can see everything."




 menu:




    "Grab her boobs":


      $ tt = show_tt("top_right")
      $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
      hide screen tool
      if chal == "speed":

          $ renpy.block_rollback()
          you "You start playing with her."

          $ pic = girl2.get_pic("wet", and_tags=["rest", "fondle", "naked"], soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

          play sound s_laugh

          you "Your tits feel so good"

          you "This could be my lucky day!"

          call challenge(chal, girl_def) from _call_challenge_93 # result is stored in the _show screen home variable

          $ r = _return

          if r:

               $ pic = girl2.get_pic("wet", and_tags=["rest", "fondle", "naked"], soft=True)
               show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


               you "You're all mine now babe!"

               "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


               menu:

                 "Do it some more":

                  hide screen show_event

                  jump sleep_touch





                 "Go further":


                  jump sleep_round2





                 "Go back":


                  "You decide to leave the room before she sees you."


                  you "This was good, should come back again another night."


                  hide screen show_event

                  jump main















          else:

              "You've been spotted!"


              $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "naked"], soft=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


              girl.char "What are you doing here?"

              you "I'm sorry, i was looking for the public spa and got lost!"


              if girl.love <= 60:

                  girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                  girl2.char "Let's kick him out!"


                  "The girls surround you and start hitting you. You're being dragged out of the room."


                  hide screen show_event


                  jump main







    "Grab her ass":

         $ tt = show_tt("top_right")
         $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
         hide screen tool

         if chal == "speed":
             $ renpy.block_rollback()
             you "You start playing with her."

             $ pic = girl2.get_pic("wet", and_tags=["rest", "grope", "naked"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_laugh

             you "Your tits feel so good"

             you "This could be my lucky day!"

             call challenge(chal, girl_def) from _call_challenge_94 # result is stored in the _show screen home variable

             $ r = _return

             if r:

                  $ pic = girl2.get_pic("wet", and_tags=["rest", "grope", "naked"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                  you "You're all mine now babe!"

                  "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                  menu:

                    "Do it some more":


                     hide screen show_event

                     jump sleep_touch





                    "Go further":


                     jump sleep_round2





                    "Go back":


                     "You decide to leave the room before she sees you."


                     you "This was good, should come back again another night."


                     hide screen show_event

                     jump main


             else:

                 "You've been spotted!"


                 $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "naked"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "What are you doing here?"

                 you "I'm sorry, i was looking for the public spa and got lost!"


                 if girl.love <= 60:

                     girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                     girl2.char "Let's kick him out!"


                     "The girls surround you and start hitting you. You're being dragged out of the room."


                     hide screen show_event


                     jump main





    "Finger her pussy":

         $ tt = show_tt("top_right")
         $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
         hide screen tool

         if chal == "speed":
             $ renpy.block_rollback()
             you "You start playing with her."

             $ pic = girl2.get_pic("wet", and_tags=["rest", "finger", "naked"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_laugh

             you "Your tits feel so good"

             you "This could be my lucky day!"

             call challenge(chal, girl_def) from _call_challenge_95 # result is stored in the _show screen home variable

             $ r = _return

             if r:

                  $ pic = girl2.get_pic("wet", and_tags=["rest", "finger", "naked"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                  you "You're all mine now babe!"

                  "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                  menu:

                    "Do it some more":


                     hide screen show_event

                     jump sleep_touch





                    "Go further":


                     jump sleep_round2





                    "Go back":


                     "You decide to leave the room before she sees you."


                     you "This was good, should come back again another night."


                     hide screen show_event

                     jump main


             else:

                 "You've been spotted!"


                 $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "naked"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "What are you doing here?"

                 you "I'm sorry, i was looking for the public spa and got lost!"


                 if girl.love <= 60:

                     girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                     girl2.char "Let's kick him out!"


                     "The girls surround you and start hitting you. You're being dragged out of the room."


                     hide screen show_event


                     jump main










    "Finger her ass":

         $ tt = show_tt("top_right")
         $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
         hide screen tool

         if chal == "speed":
             $ renpy.block_rollback()
             you "You start playing with her."

             $ pic = girl2.get_pic("wet", and_tags=["rest", "fisting", "naked"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_laugh

             you "Your tits feel so good"

             you "This could be my lucky day!"

             call challenge(chal, girl_def) from _call_challenge_96 # result is stored in the _show screen home variable

             $ r = _return

             if r:

                  $ pic = girl2.get_pic("wet", and_tags=["rest", "fisting", "naked"], soft=True)
                  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                  you "You're all mine now babe!"

                  "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                  menu:

                    "Do it some more":


                     hide screen show_event

                     jump sleep_touch





                    "Go further":


                     jump sleep_round2





                    "Go back":


                     "You decide to leave the room before she sees you."


                     you "This was good, should come back again another night."


                     hide screen show_event

                     jump main


             else:

                 "You've been spotted!"


                 $ pic = girl.get_pic("wet", and_tags=["rest", "angry", "naked"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "What are you doing here?"

                 you "I'm sorry, i was looking for the public spa and got lost!"


                 if girl.love <= 60:


                     girl.char "Yeah, right! Girls, [MC.name] is here! We have an intruder."

                     girl2.char "Let's kick him out!"


                     "The girls surround you and start hitting you. You're being dragged out of the room."

                     hide screen show_event


                     jump main














label wet_bathhouse:

 image bathhouse = "mods/vaan/bathhouse.png"
 show bathhouse

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)

 "You try and enter the bathhouse to wet on the girls dressing up."


 $ pic = girl.get_pic("wet", and_tags=["beach"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You successfully see [girl.name] changing, she hasn't noticed you yet."


 hide screen show_event
 jump main



label wet_lockers:

 image lockers = "mods/vaan/lockers.png"
 show lockers

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(MC.girls)

 "You try and enter the lockers to wet on the girls dressing up."


 $ pic = girl.get_pic("wet", and_tags=["changing room"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You successfully see [girl.name] changing, she hasn't noticed you yet."


 hide screen show_event
 jump main

 label mc_masseuse:

  $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
  $ girl = rand_choice(MC.girls)

  "You've gotten so many massages from the girls, that you decided to try and learn how to do it yourself, it will also help you get closer to them in many ways."

  "You go into the spa room of the guild house and tell the girls they can come over for a massage if they want to."

  "Just as you get ready you see [girl.name] come over. She looks quite happy."

  $ pic = girl.get_pic("profile", soft=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  girl.char "Thank you [MC.name], i could really use a nice massage, but don't think about doing anything."

  you "Of course not, this is only for me to be able to get better at this."

  girl.char "Of course it is, where would you like me to lie?"

  $ pic = girl.get_pic("mc", and_tags=["masseuse"], soft=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  you "Over here is fine, let's get started."


  girl.char "That feels so great!"

 label masseuse_touch:

   menu:


        "Grab her boobs":

         $ tt = show_tt("top_right")
         $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
         hide screen tool

         if chal == "speed":
             $ renpy.block_rollback()
             you "You start playing with her."

             $ pic = girl.get_pic("mc", and_tags=["masseuse", "fondle"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_laugh

             you "Are you enjoying it?"

             "The girl has gone quiet."

             call challenge(chal, girl_def) from _call_challenge_101 # result is stored in the _show screen home variable

             $ r = _return

             if r:

                  $ pic2 = girl.get_pic("mc", and_tags=["masseuse", "fondle"], soft=True)
                  show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))


                  girl.char "Keep going."

                  "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                  menu:

                    "Do it some more":

                     hide screen show_event

                     jump masseuse_touch





                    "Go further":


                     jump masseuse_round2





                    "Finish":


                     "You decide to finish the massage"


                     girl.char "This was good, should come back again another time."

                     $ MC.change_prestige(1)
                     $ girl.change_stat("obedience", +4)
                     $ girl.change_stat("fear", -2)
                     $ girl.change_stat("love", +4)


                     hide screen show_event

                     jump main















             else:

                 "She hates it!"


                 $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 girl.char "Where do you think you're touching?"

                 you "I'm sorry, my hand slipped!"


                 if girl.love <= 60:

                     girl.char "Yeah, right! I'm leaving!"


                     you "Sorry!"

                     "She takes her things and leaves."

                     $ MC.change_prestige(+20)
                     $ girl.change_stat("obedience", -4)
                     $ girl.change_stat("fear", +3)
                     $ girl.change_stat("love", -5)




                     hide screen show_event


                     jump main





        "Grab her ass":

             $ tt = show_tt("top_right")
             $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
             hide screen tool

             if chal == "speed":
                 $ renpy.block_rollback()
                 you "You start playing with her."

                 $ pic = girl.get_pic("mc", and_tags=["masseuse", "grope"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 play sound s_laugh

                 you "This feels so good."

                 "She is still quiet."

                 call challenge(chal, girl_def) from _call_challenge_102 # result is stored in the _show screen home variable

                 $ r = _return

                 if r:

                      $ pic = girl.get_pic("mc", and_tags=["masseuse", "grope"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                      play sound s_moans

                      "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                      menu:

                        "Do it some more":


                         hide screen show_event

                         jump masseuse_touch





                        "Go further":


                         jump masseuse_round2





                        "Finish":


                         "You decide to finish the massage"


                         girl.char "This was good, should come back again another time."
                         $ MC.change_prestige(+10)
                         $ girl.change_stat("obedience", +6)
                         $ girl.change_stat("fear", -7)
                         $ girl.change_stat("love", +4)


                         hide screen show_event

                         jump main


                 else:

                     $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     girl.char "Where do you think you're touching?"

                     you "I'm sorry, my hand slipped!"


                     if girl.love <= 60:

                         girl.char "Yeah, right! I'm leaving!"


                         you "Sorry!"

                         "She takes her things and leaves."



                         $ girl.change_stat("obedience", -6)
                         $ girl.change_stat("fear", +4)
                         $ girl.change_stat("love", -7)




                         hide screen show_event


                         jump main





        "Finger her pussy":

             $ tt = show_tt("top_right")
             $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
             hide screen tool

             if chal == "speed":
                 $ renpy.block_rollback()
                 you "You start playing with her."

                 $ pic = girl.get_pic("mc", and_tags=["masseuse", "finger"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 play sound s_laugh

                 "You start fingering her pussy."

                 "She has gone silent."

                 call challenge(chal, girl_def) from _call_challenge_103 # result is stored in the _show screen home variable

                 $ r = _return

                 if r:

                      $ pic = girl.get_pic("mc", and_tags=["masseuse", "finger"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                      you "Enjoying it?"

                      girl.char "Yes, keep going."


                      menu:

                        "Do it some more":


                         hide screen show_event

                         jump masseuse_touch





                        "Go further":


                         jump masseuse_round2





                        "Finish":


                         "You decide to finish the massage."


                         girl.char "This was good, should come back again another time."


                         $ MC.change_prestige(+10)
                         $ girl.change_stat("obedience", +8)
                         $ girl.change_stat("fear", -7)
                         $ girl.change_stat("love", +10)


                         hide screen show_event

                         jump main


                 else:

                     $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     girl.char "Where do you think you're touching?"

                     you "I'm sorry, my hand slipped!"


                     if girl.love <= 60:

                         girl.char "Yeah, right! I'm leaving!"


                         you "Sorry!"

                         "She takes her things and leaves."



                         $ girl.change_stat("obedience", -10)
                         $ girl.change_stat("fear", +5)
                         $ girl.change_stat("love", -6)




                         hide screen show_event


                         jump main










        "Finger her ass":

             $ tt = show_tt("top_right")
             $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
             hide screen tool

             if chal == "speed":
                 $ renpy.block_rollback()
                 you "You start playing with her."

                 $ pic = girl.get_pic("mc", and_tags=["masseuse", "fisting"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 play sound s_laugh

                 you "Just relax, girl. It will go in easier."



                 call challenge(chal, girl_def) from _call_challenge_104 # result is stored in the _show screen home variable

                 $ r = _return

                 if r:

                      $ pic = girl2.get_pic("masseuse", and_tags=["fisting"], soft=True)
                      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                      you "Enjoying it?"

                      girl.char "Yes, keep going. It hurts a bit, but i'll get used to it."

                      menu:

                        "Do it some more":


                         hide screen show_event

                         jump masseuse_touch





                        "Go further":


                         jump masseuse_round2





                        "Finish":


                         "You decide to finish the massage"


                         girl.char "This was good, should come back again another time."


                         $ MC.change_prestige(+10)
                         $ girl.change_stat("obedience", +7)
                         $ girl.change_stat("fear", -3)
                         $ girl.change_stat("love", +9)


                         hide screen show_event

                         jump main


                 else:

                     $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity"], soft=True)
                     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                     girl.char "Where do you think you're touching?"

                     you "I'm sorry, my hand slipped!"


                     if girl.love <= 60:


                         girl.char "Yeah, right! I'm leaving!"


                         you "Sorry!"

                         "She takes her things and leaves."


                         $ MC.change_prestige(+20)
                         $ girl.change_stat("obedience", -7)
                         $ girl.change_stat("fear", +8)
                         $ girl.change_stat("love", -10)




                         hide screen show_event


                         jump main



label masseuse_round2:

 "You decide to take her clothes off."

 $ pic = girl2.get_pic("masseuse", and_tags=["mc", "naked", "strip"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 you "Let's take it off."

 menu:


      "Grab her boobs":

       $ tt = show_tt("top_right")
       $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
       hide screen tool

       if chal == "speed":
           $ renpy.block_rollback()
           you "You start playing with her."

           $ pic = girl.get_pic("mc", and_tags=["masseuse", "fondle", "naked"], soft=True)
           show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

           play sound s_laugh

           you "Are you enjoying it?"

           "The girl has gone quiet."

           call challenge(chal, girl_def) from _call_challenge_105 # result is stored in the _show screen home variable

           $ r = _return

           if r:

                $ pic2 = girl.get_pic("mc", and_tags=["masseuse", "fondle", "naked"], soft=True)
                show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))


                girl.char "Keep going."

                "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                menu:

                  "Do it some more":

                   hide screen show_event

                   jump masseuse_touch





                  "Go further":


                   jump masseuse_round2





                  "Finish":


                   "You decide to finish the massage"


                   girl.char "This was good, should come back again another time."

                   $ MC.change_prestige(+20)
                   $ girl.change_stat("obedience", +3)
                   $ girl.change_stat("fear", -5)
                   $ girl.change_stat("love", +6)


                   hide screen show_event

                   jump main















           else:

               "She hates it!"


               $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity", "naked"], soft=True)
               show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


               girl.char "Where do you think you're touching?"

               you "I'm sorry, my hand slipped!"


               if girl.love <= 60:

                   girl.char "Yeah, right! I'm leaving!"


                   you "Sorry!"

                   "She takes her things and leaves."



                   $ girl.change_stat("obedience", -3)
                   $ girl.change_stat("fear", +5)
                   $ girl.change_stat("love", -4)




                   hide screen show_event


                   jump main





      "Grab her ass":

         $ tt = show_tt("top_right")
         $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
         hide screen tool

         if chal == "speed":


               $ renpy.block_rollback()
               you "You start playing with her."

               $ pic = girl.get_pic("mc", and_tags=["masseuse", "grope", "naked"], soft=True)
               show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

               play sound s_laugh

               you "This feels so good."

               "She is still quiet."

               call challenge(chal, girl_def) from _call_challenge_106 # result is stored in the _show screen home variable

               $ r = _return

               if r:

                    $ pic = girl.get_pic("mc", and_tags=["masseuse", "grope", "naked"], soft=True)
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                    play sound s_moans

                    "You keep groping her for a bit and wonder if you should take it further, play with her some more or leave."


                    menu:

                      "Do it some more":


                       hide screen show_event

                       jump masseuse_touch





                      "Go further":


                       jump masseuse_round2





                      "Finish":


                       "You decide to finish the massage"


                       girl.char "This was good, should come back again another time."

                       $ MC.change_prestige(+25)
                       $ girl.change_stat("obedience", +10)
                       $ girl.change_stat("fear", -3)
                       $ girl.change_stat("love", +10)


                       hide screen show_event

                       jump main


               else:

                   $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity", "naked"], soft=True)
                   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                   girl.char "Where do you think you're touching?"

                   you "I'm sorry, my hand slipped!"


                   if girl.love <= 60:

                       girl.char "Yeah, right! I'm leaving!"


                       you "Sorry!"

                       "She takes her things and leaves."



                       $ girl.change_stat("obedience", -10)
                       $ girl.change_stat("fear", +10)
                       $ girl.change_stat("love", -10)




                       hide screen show_event


                       jump main





      "Finger her pussy":

           $ tt = show_tt("top_right")
           $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
           hide screen tool

           if chal == "speed":
               $ renpy.block_rollback()
               you "You start playing with her."

               $ pic = girl.get_pic("mc", and_tags=["masseuse", "finger", "naked"], soft=True)
               show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

               play sound s_laugh

               "You start fingering her pussy."

               "She has gone silent."

               call challenge(chal, girl_def) from _call_challenge_107 # result is stored in the _show screen home variable

               $ r = _return

               if r:

                    $ pic = girl.get_pic("mc", and_tags=["masseuse", "finger", "naked"], soft=True)
                    show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                    you "Enjoying it?"

                    girl.char "Yes, keep going."


                    menu:

                      "Do it some more":


                       hide screen show_event

                       jump masseuse_touch





                      "Go further":


                       jump masseuse_round2





                      "Finish":


                       "You decide to finish the massage."


                       girl.char "This was good, should come back again another time."


                       $ MC.change_prestige(+20)
                       $ girl.change_stat("obedience", +10)
                       $ girl.change_stat("fear", -10)
                       $ girl.change_stat("love", +10)


                       hide screen show_event

                       jump main


               else:

                   $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity", "naked"], soft=True)
                   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                   girl.char "Where do you think you're touching?"

                   you "I'm sorry, my hand slipped!"


                   if girl.love <= 60:

                       girl.char "Yeah, right! I'm leaving!"


                       you "Sorry!"

                       "She takes her things and leaves."


                       $ girl.change_stat("obedience", -7)
                       $ girl.change_stat("fear", +7)
                       $ girl.change_stat("love", -6)




                       hide screen show_event


                       jump main










      "Finger her ass":

           $ tt = show_tt("top_right")
           $ chal = renpy.call_screen("challenge_menu", challenges=[("Play", "speed",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
           hide screen tool

           if chal == "speed":
               $ renpy.block_rollback()
               you "You start playing with her."

               $ pic = girl.get_pic("mc", and_tags=["masseuse", "fisting", "naked"], soft=True)
               show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

               play sound s_laugh

               you "Just relax, girl. It will go in easier."



               call challenge(chal, girl_def) from _call_challenge_108 # result is stored in the _show screen home variable

               $ r = _return

               if r:

                 $ pic = girl2.get_pic("masseuse", and_tags=["fisting", "naked"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 you "Enjoying it?"

                 girl.char "Yes, keep going. It hurts a bit, but i'll get used to it."

                 menu:

                   "Do it some more":


                    hide screen show_event

                    jump masseuse_touch





                   "Go further":


                    jump masseuse_round2





                   "Finish":


                    "You decide to finish the massage"


                    girl.char "This was good, should come back again another time."

                    $ MC.change_prestige(+20)
                    $ girl.change_stat("obedience", +7)
                    $ girl.change_stat("fear", -1)
                    $ girl.change_stat("love", +8)


                    hide screen show_event

                    jump main




               else:

                   $ pic = girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity", "naked"], soft=True)
                   show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                   girl.char "Where do you think you're touching?"

                   you "I'm sorry, my hand slipped!"


                   if girl.love <= 60:


                       girl.char "Yeah, right! I'm leaving!"


                       you "Sorry!"

                       "She takes her things and leaves."


                       $ girl.change_stat("obedience", -3)
                       $ girl.change_stat("fear", +2)
                       $ girl.change_stat("love", -2)




                       hide screen show_event


                       jump main











label fight:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ girl = rand_choice(able_girls)
 $ girl_def = 4 + girl.get_defense()
 $ renpy.show_screen("show_img", brothel.pic, _layer = "master")

 if len(able_girls) == 0:


     "You can't seem to find any girls around."
     jump main

 "You hear a noise outside, someone's practicing with a sword or perhaps a people are fighting. You go out to investigate"
 with fade

 "You get closer to the noice and see [girl.name]!"
 $ pic = girl.get_pic("fight", and_tags=["mc"], strict=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 you "That's very good [girl.name]. How would you like to try and fight me?"

 if girl.is_("very dom") or girl.is_("dom"):
     girl.char "Sure, would be an easy fight. Once you lose, get ready to eat my pussy"
     you "Very wll, but if you lose. I'll make you my whore and fuck you all day, how does that sound?"
     girl.char "Hah, you think i'm scared of you? I'm going to enjoy this fight"

 else:
     girl.char "Of course, i think it will be good to test my skills on a real opponent. Thank you, [MC.name]!"
     you "Don't mention it, how about we make a little bet? If you win, i'll give you some gold, if i win, i would like you to service me."

     if girl.love >= 45:

         girl.char "Sure, i'm looking forward to it. Sounds like a win-win situation to me."

     elif girl.love <=45:

         girl.char "No, thank you!"


 $ tt = show_tt("top_right")
 $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight [girl.name]", "fight",  girl_def), ("Use magic on her", "control",  girl_def)], cancel=("Give up", False))
 hide screen tool

 if chal == "fight":
     $ renpy.block_rollback()
     "You ready your weapon."
     you "It's over for you girl, you better get that mouth ready!"

     play sound s_laugh

     girl.char "Not yet, this is far from over!"

     call challenge(chal, girl_def) from _call_challenge_76 # result is stored in the _show screen home variable
     $ r = _return
     if r:

         play sound "sword sheath.mp3"
         with vpunch
         "The girl fights back with everything she can, but she is no match for your skill. You are starting to win this fight!"

         play sound s_sheath

         with vpunch

         pause 0.3

         play sound s_sheath

         with vpunch

         pause 0.2

         play sound s_laugh

         "She is slowly getting tired and soon it might be time for the final blow."

         play sound s_punch
         with vpunch
         pause 0.2

         play sound2 s_scream

         "You try to go easy on her and not harm her. You counter her last hit and manage to bring her to the ground"

         play sound s_crash
         with vpunch

         "The girl is stunned and falls flat on the ground in a cloud of dust. She screams and looks a bit hurt, but nothing she can't shake off."

         play sound s_scream

         you "It was a good fight. You show plenty of promise!"

         girl.char "Thank you [MC.name], i will try and get better. One day i'll be as good as you!"

         you "Now, about our bet!"

         girl.char "I was hoping you forgot about that!"
         you "Haha, like i would forget, now take your clothes off and show me your body like a good little girl"

         if girl.is_("very dom") or girl.is_("dom"):

             girl.char "Very well, a deal is a deal. I'm sure you've been waiting a long time for this. I'm sure you'll cum just from looking at my body either way"


             $ pic = girl.get_pic("dom", and_tags=["strip", "nature", "town"], not_tags=["group", "bisexual", "lesbian"], soft=True)

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "You like what you see? You finally get to see my body, i'm sure it's a great moment for you!"
             you "It really is, i want to fuck you now!"

             girl.char "Hah, impatient little boy. Fine, come claim your price, this is the first and last time it happens, so enjoy while it lasts"

             $ pic2 = girl.get_pic("dom", and_tags=["sex", "fight", "mc"], not_tags=["group", "bisexual", "lesbian"], soft=True)
             show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))



             girl.char "This is what you've been wanting for quite some time now isn't it? You finally got my pussy, i bet it feels good!"

             you "It's not over yet, i want your ass now!"

             girl.char "Why would i do that?"

             you "Because if you don't i will beat you again!"

             girl.char "Hahaha, i'll let you have it this time, i guess you earned it. But watch your tongue!"

             "The moment you waited for is finally here, you get to fuck your ass and she seems willing to do it. Her ass is so tight, you won't be able to hold on for much!"

             $ pic3 = girl.get_pic("dom", and_tags=["anal", "fight", "mc"], not_tags=["group", "strap-on", "bisexual", "lesbian"], soft=True)

             show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_aah

             you "It feels so good, i've been waiting for this for so long!"

             girl.char "You finally get to own my ass, even for a little bit. I doubt you'll be able to hold on for long though, hahaha!"

             you "I can't hold much longer, cumming!"

             girl.char "Just like i thought, pathetic."


             if girl.love >= 50:

                 girl.char "It's okay, you can cum inside, just this once!"

                 "You don't wait for second invite and cum deep inside her ass."
                 play sound s_mmmh
                 $ pic4 = girl.get_pic("dom", and_tags=["anal", "inside", "mc"], not_tags=["group", "bisexual", "lesbian"], strict=True)
                 show screen show_event(pic4, x=config.screen_width, y=int(config.screen_height*0.8))

                 girl.char "That's it, let it out for mommy, good boy!"

                 hide screen show_event

                 girl.char "Hope you enjoyed it, it won't happen again anytime soon!"

                 "You both dress up and head back inside"
                 $ girl.change_love(2)
                 $ girl.change_fear(-10)
                 $ MC.interactions -= 2
                 hide screen show_event

                 jump main







             elif girl.love <= 50:

                 girl.char "Not inside, like i would ever let a loser like you cum inside me!"

                 "She takes your cock out and let's you cum outside!"

                 $ pic5 = girl.get_pic("dom", and_tags=["cumshot", "mc"], not_tags=["group", "bisexual", "lesbian", "inside", "creampie"], soft=True)
                 show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8))

                 girl.char "Hope you enjoyed it, it won't happen again anytime soon!"

                 you "Can i cum inside you next time?"

                 girl.char "Like that would ever happen, go away now. I want to be alone!"



                 $ girl.change_love(2)
                 $ girl.change_fear(-10)
                 $ MC.interactions -= 2
                 hide screen show_event

                 jump main












         else:

             you "Turn around, i want to claim my prize!"

             girl.char "Yes, master. Please go easy on me."

             "She turns around, you take off her panties and start fucking her"

             $ pic6 = girl.get_pic("sex", and_tags=["doggy", "fight", "mc"], not_tags=["group", "bisexual", "lesbian", "cumshot"], soft=True)
             show screen show_event(pic6, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_mmmh

             you "That feels good, going to cum soon!"

             girl.char "Yes, master! I want your cum, claim me as your prize!"

             with fade

             $ pic = girl.get_pic
             show screen show_event(pic("sex", and_tags=["doggy", "mc", "fight", "cumshot"], not_tags=["group", "bisexual", "lesbian"]), x=config.screen_width, y=int(config.screen_height*0.8))


             you "It feels so good, take it bitch!"

             play sound s_mmmh

             hide screen show_event


             $ pic8 = girl.get_pic("profile", soft=True)
             show screen show_event(pic8, x=config.screen_width, y=int(config.screen_height*0.8))


             you "That felt so good!"

             girl.char "Looking forward to our next sparring session, haha!"

             you "Me too, have to head back inside, but you can keep practicing if you want, you are definitely showing promise!"

             girl.char "Thank you, a bit warmed out from all the *training* we did. But will try again tomorrow!"

             $ girl.change_mood(2)

             $ girl.change_love(2)
             $ girl.change_fear(-10)
             $ girl.change_fear(-10)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2

             with fade

             hide screen show_event
             with fade

             jump main















     else:

         "You lost the fight"
         $ renpy.block_rollback()

         you "How did i lose against a little girl?"

         "She looks at you with a smirk and you wonder what she intends to do with you."
         $ result = 0


         if girl.is_("very dom") or girl.is_("dom"):

             girl.char "Pathetic, i told you i would win. Now stand still, you're going to be my little bitch"
             you "Do what you want, you won!"
             girl.char "Call me mistress, my little bitch!"
             you "Yes, mistress!"
             girl.char "Good, now stand still, i'll teach you not to mess with me!"
             $ pic = girl.get_pic("dom", and_tags=["strap-on", "anal", "mc"], not_tags=["group", "bisexual", "lesbian"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             with fade
             girl.char "That's a good boy, make me come and i'll leave you alone for now!"
             you "Yes, mistress."
             $ pic2 = girl.get_pic("dom", and_tags=["anal", "strap-on", "mc"], not_tags=["bisexual", "group", "lesbian"])
             show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))
             girl.char "I'm almost there, slave! Make your mistress come!"
             with fade
             $ pic3 = girl.get_pic("dom", and_tags=["strap-on", "cumshot", "mc"], not_tags=["bisexual", "group", "lesbian"])
             show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))
             with fade

             $ pic3 = girl.get_pic("dom", not_tags=["bisexual", "group", "lesbian"])
             show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))
             girl.char "That's a good boy, maybe next time i'll let you fuck me!"



             $ girl.change_mood(2)
             $ girl.change_love(2)
             $ girl.change_fear(-10)
             $ MC.interactions -= 2

             hide screen show_event













             jump main



label pool_alone:


  if len(MC.girls) == 0: # Important to check that there are enough girls in the brothel before attempting this
      "No girls in brothel"

      jump main

  "You decide to go check the pool in the brothel, hoping it will be quieter."





  "You see [girl.name] is there and you go over to say hello."
  $ pic = girl.get_pic("beach", and_tags=["swim"], not_tags=["cumshot"], soft=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  you "Hi [girl.name], enjoying some time off?"

  girl.char "Yes, the sun is shining bright."

  you "Would you like me to put some sunscreen on you?"


  if girl.get_stat("libido") <= 60 or girl.get_stat("obedience") <= 60:
      girl.char "No thanks, i just want to relax if you don't mind?"

      you "Of course, i'll go somewhere else."
      hide screen show_event
      jump main




  else:

      girl.char "Of course, let me get up and get ready."

      $ pic = girl.get_pic("beach", and_tags=["swim", "libido", "tempt"], soft=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      if not pic:
          $ pic = girl.get_pic("beach", and_tags=["swim", "libido", "tempt"], soft=True)

          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


      "You look at the girl and you can't help but thinking how sexy she is."

  you "Okay, lie down and let's get started."
  with fade

  $ pic = girl.get_pic("service", and_tags=["mc", "beach", "grope"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "You start massaging her ass and she seems to enjoy it."

  play sound s_mmmh
  with dissolve


  you "I guess this sound means you're enjoying yourself, let's see if we can go deeper."

  $ pic = girl.get_pic("service", and_tags=["swim", "beach", "mc"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  play sound s_aah
  with dissolve

  girl.char "This feels so good, let me turn around so you can get all of my areas!"


  "She lies on her back and you start massaging her boobs."


  $ pic = girl.get_pic("service", and_tags=["massause", "swim", "beach", "fondle"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  play sound s_mmmh

  you "Does it feel good for you?"

  girl.char "It feels amazing, please keep going!"

  you "How about you take your bikini off, so that i can reach even further?"


  girl.char "That sounds like a great idea."
  with fade

  $ pic = girl.get_pic("swim", and_tags=["beach", "strip", "naked", "tempt"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "She gets up to take her bikini off and does it slowly to tease you!"

  with fade

  $ pic = girl.get_pic("naked", and_tags=["beach", "tempt"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



  you "Let's keep going then."

  girl.char "Do you like what you see?"


  you "Of course! You look so hot!"

  play sound s_kind_laugh

  girl.char "Awww, thank you!"

  with fade


  "She lies back on her towel and you start massaging her again."


  $ pic = girl.get_pic("naked", and_tags=["beach", "grope", "massause"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  play sound s_mmmh

  girl.char "That feels amazing, your hands are magic, [MC.name]!"


  you "Thank you, now how about you turn around, so that i can put some on your tits?"


  with fade

  $ pic = girl.get_pic("naked", and_tags=["beach", "fondle", "massause"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  "The girl turns around and you start massaging her boobs. She let's out a small moan, she's starting to get turned on."


  you "Can i massage your pussy next?"


  if girl.get_stat("libido") <= 60 and girl.get_stat("love") <= 60:

      girl.char "I think we can stop here, it's getting a bit hot and i should go back inside."

      $ pic = girl.get_pic("beach", and_tags=["swim", "libido"], soft=True)

      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

      you "Okay, i'll stay here for a bit more..."

      "She gets up and goes back inside, you're disappointed that you couldn't get her to go further."






      hide screen show_event

      jump main





  else:


      girl.char "I think you should, i'm getting a bit wet down there."

      girl.char "If you don't, i'll have to take care of that problem all by myself."

      you "Well...we can't have that happening!"



  $ pic = girl.get_pic("naked", and_tags=["beach", "finger", "massause"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "You start fingering her and her moans are starting to get louder and louder."

  play sound s_mmmh


  "You start mixing the massage by touching her entire body all over."

  $ pic = girl.get_pic("naked", and_tags=["beach", "fondle", "massause"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  "She keeps moving and going back and forth while your hands are feeling her."


  $ pic = girl.get_pic("naked", and_tags=["beach", "grope", "massause"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  girl.char "It feels so good, i'm going to cum soon!"

  you "That's what i want to hear, get ready!"


  $ pic = girl.get_pic("naked", and_tags=["beach", "finger", "massause"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "You bring back your focus on her pussy and she's no longer able to hold her voice."


  "The girl starts screaming with pleasure and you can feel she's about to cum."

  girl.char "Master, i'm coming!"


  play sound s_orgasm


  $ pic = girl.get_pic("orgasm", and_tags=["beach", "swim", "squirt"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  hide screen show_event


  "Her legs shake from the pleasure and you give her some time to rest."

  girl.char "Oh wow, master! That was amazing! Is there anything i can do to repay the favour?"


  you "Well, now that you mention it."

  "You take out your dick and you see a smile on her face."

  girl.char "Of course, it's your turn now!"



  $ pic = girl.get_pic("service", and_tags=["beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  "She gets on her knees and starts sucking your cock."

  "You're enjoying yourself and have a look around to see if anyone is looking while she's doing her business."

  with fade

  $ pic = girl.get_pic("service", and_tags=["oral", "beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  you "Just like that, it feels amazing."

  girl.char "I'm glad you're enjoying it, it's the least i can do after the massage you gave me!"

  "Get up now, i want to fuck!"

  girl.char "Of course, master!"

  $ pic = girl.get_pic("sex", and_tags=["beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  play sound s_orgasm


  "She gets up and you push your cock deep inside her pussy."

  $ pic = girl.get_pic("sex", and_tags=["doggy", "beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  you "This feels so good!"

  with fade

  $ pic = girl.get_pic("sex", and_tags=["cowgirl", "beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  play sound s_aah

  girl.char "This feels amazing, [MC.name]!"


  you "How about we try your asshole?"

  girl.char "If that's what you want!"

  with fade


  $ pic = girl.get_pic("anal", and_tags=["beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


  "You take your cock and push it inside her ass, she's surpised at first, but she's able to handle it after some time."


  $ pic = girl.get_pic("anal", and_tags=["doggy", "beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  play sound s_aah


  girl.char "I hope it feels good for you, master!"

  you "This feels amazing! I don't ever want to stop!"


  "You keep going at it while her tight ass is squeezing your cock."

  with dissolve

  girl.char "Here, let me get on top."


  $ pic = girl.get_pic("anal", and_tags=["doggy", "beach", "swim"], not_tags=["group", "creampie", "inside"], soft=True)

  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  "The girl takes control and starts riding your cock even harder."

  "Her tight ass keeps squeezing your cock and you feel like you're reaching your limit."


  you "Just like that [girl.name], you're a natural at this."

  girl.char "Thank you master! I aim to please. I hope you're enjoing it as much as i enjoying your massage."

  "She's riding you hard and you can't seem to be able to handle it anymore."

  you "I'm going to cum!"


  $ fix = rand_choice(["inside", "on-body", "in-mouth", "anal"])



  if fix == "inside":
      $ pic = girl.get_pic("sex", and_tags=["beach", "swim", "inside", "creampie"], not_tags=["group", "bisexual"], soft=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


      you "I want to go back in your pussy and cum inside!"


      girl.char "Yes, give it to me, master! Deep inside!"

      play sound s_mmmh



      girl.char "There's so much of it inside me!"
      you "Thanks, [girl.name], i needed that!"
      girl.char "Anytime, [MC.name]!"



      hide screen show_event
      $ MC.interactions -= 2
      $ girl.change_fear(-10)
      $ girl.change_love(10)
      jump main









  if fix == "on-body":
      $ pic5 = girl.get_pic("cumshot", and_tags=["swim", "on-body", "on-face"], not_tags=["group", "bisexual"], soft=True)
      show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8))


      you "Get on your knees, i'm going to shower you with cum!"


      girl.char "Yes, give it to me, [MC.name]! I want it all over me!"

      play sound s_mmmh



      girl.char "I hope you enjoying it, i tried my best after the massage you gave me!"
      you "I did, next time i'll give you an even better one!"
      girl.char "Haha, i'm going to head back inside! See you later!"
      hide screen show_event
      $ MC.interactions -= 2
      $ girl.change_fear(-10)
      $ girl.change_love(10)
      jump main


  if fix == "in-mouth":
      $ pic = girl.get_pic("cumshot", and_tags=["beach", "swim", "in-mouth"], not_tags=["group", "bisexual"], soft=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


      you "Get on your knees and open your mouth, babe!"


      girl.char "Yes, give it to me, master! I want to taste it!"

      play sound s_mmmh



      "She swallows all the cum and gives you a smile."
      you "You look so hot with my cum in your mouth! We should do it again soon!"
      girl.char "I enjoyed it as much as you, probably even more! Thanks for the massage and for your cum!"

      "She gets up and goes back inside."



      hide screen show_event
      $ MC.interactions -= 2
      $ girl.change_fear(-10)
      $ girl.change_love(10)
      jump main


  if fix == "anal":
      $ pic = girl.get_pic("anal", and_tags=["beach", "swim", "inside", "creampie"], not_tags=["group", "bisexual"], soft=True)
      show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


      you "I'm going to cum!"


      girl.char "Yes, give it to me, master! Deep inside!"

      play sound s_mmmh

      "You cum inside her ass and take your cock out. With your cum overflowing inside!"

      girl.char "There's so much of it inside me!"
      you "Your ass is so tight, i couldn't last any longer! It was amazing!"
      girl.char "Thank you! It felt good having your cock inside me too, not to mention the massage! I have to go back inside now, thank you for the time!"





      hide screen show_event
      $ MC.interactions -= 2
      $ girl.change_fear(-10)
      $ girl.change_love(10)
      jump main

label entertainment:
 # Make a list of girls that are present in the brothel and not injured or burned out
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]

 # Take the list above and reduce it to a smaller list, leaving only girls with the "dancer" job
 $ dancer_girls = [g for g in able_girls if g.job == "dancer"]

 # Give dancer_girls to rand_choice, which will pick a random thing from any list you put inside its brackets
 $ girl = rand_choice(dancer_girls)

 if len(dancer_girls) == 0: # Important to check that there are enough girls in the brothel before attempting this
     "No dancers assigned. You go back upstairs."
     scene black with fade
     jump main

 $ renpy.show("strip club")


 "You decide to go and relax a bit in the strip club and one of the girls comes over to you."

 show screen night(girl.profile)

 girl.char "[MC.name] would you like to get a lap dance?"

 you "I guess i could use some time off, let's go to one of the vip rooms"

 "She looks happy and guides you to the room"


 if girl.is_("very dom") or (intensity >= 2 and girl.is_("dom")):

      girl.char "Let's get this over with!"
 if girl.fear >= 10 or girl.love <= 30:

     girl.char"This is so embarassing, but i will do it."

 else:

     girl.char "It's not every day i get to dance for you, this will be fun, i hope you enjoy it."



 "You sit down and she starts dancing in front of you."
 $ pic1 = girl.get_pic("dancer", and_tags=["mc"], soft=True)

 show screen show_event(pic1, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade

 girl.char "This feels so hot, the way you look at me."

 $ pic3 = girl.get_pic("dancer", and_tags=["mc"], soft=True)



 show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
 with fade

 you "You're so hot [girl.name], we should do this more often."

 if girl.get_stat("libido") >= 85:
     "She looks to be enjoying it and gets into it even more. I feel so hot, i'm getting wet!"

     $ pic2 = girl.get_pic("dancer", and_tags=["mc", "temp", "libido"], soft=True)

     show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     girl.char "Would you like me to keep going? I have a lot more to show you."

     $ pic4 = girl.get_pic("dancer", and_tags=["mc", "temp", "libido"], soft=True)

     show screen show_event(pic4, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     you "Hell yes, keep going baby!"

     girl.char "It's getting how, i'll take some clothes off!"

     $ pic5 = girl.get_pic("dancer", and_tags=["mc", "strip", "panties", "naked"], soft=True)
     show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     "The girl takes her clothes off with a smile, she looks to be enjoying it even more now!"

     with fade

     $ pic6 = girl.get_pic("dancer", and_tags=["mc", "strip", "panties", "naked"], soft=True)
     show screen show_event(pic6, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     you "This just keeps getting better and better!"

     girl.char "I'm glad you're enjoying it, time to take my panties off too!"

     $ pic7 = girl.get_pic("dancer", and_tags=["mc", "naked", "strip"], soft=True)
     show screen show_event(pic7, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     girl.char "How do i look?"

     $ pic8 = girl.get_pic("dancer", and_tags=["mc", "naked"], soft=True)
     show screen show_event(pic8, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     you "You look amazing, even better when you turn around, that ass is beatiful!"

     play sound s_kind_laugh


     girl.char "Thank you, is there anything else you want to do?"

     you "I want to fuck you now."

     girl.char "I'm so wet, i have been waiting for this all night."

     "You show her your cock and she starts playing with it."
     play sound s_mmmh


     $ pic9 = girl.get_pic("dancer", and_tags=["mc", "service"], not_tags=["public"], soft=True)
     show screen show_event(pic9, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade
     girl.char "It tastes soooo good."

     you "Can't take it anymore, i have to fuck you."

     girl.char "Yes, put it in me!"

     $ pic11 = girl.get_pic("dancer", and_tags=["mc", "sex"], not_tags=["public"], soft=True)
     show screen show_event(pic11, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade
     you "That feels so good!"
     play sound s_mmmh

     girl.char "Keep fucking me!"
     $ pic14 = girl.get_pic("dancer", and_tags=["mc", "sex"], not_tags=["public"], soft=True)
     show screen show_event(pic14, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     you "I can't hold it, cumming!"

     girl.char "Yes, cum all over me! I'm all yours."

     "You can't wait any longer and you release it on the girl."

     $ pic15 = girl.get_pic("cumshot", and_tags=["dancer", "mc"], not_tags=["public"], soft=True)
     show screen show_event(pic15, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     "She collapses on the floor from her orgasm, she looks at you with smile."
     $ pic16 = girl.get_pic("aftersex", and_tags=["cumshot"], not_tags=["public"], soft=True)

     show screen show_event(pic16, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     girl.char "I guess we're finished?"

     you "Not yet, i want your ass next!"

     girl.char "Haha, someone is full of energy! Very well,"

     "You lift her from the floor and put it in her ass."

     $ pic17 = girl.get_pic("dancer", and_tags=["anal", "mc"], not_tags=["public"], soft=True)
     show screen show_event(pic17, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     play sound s_mmmh

     girl.char "It's so big, i don't know how much i can take!"

     you "Take it deeper you little slut!"

     $ pic18 = girl.get_pic("dancer", and_tags=["anal", "mc"], not_tags=["public"], soft=True)
     show screen show_event(pic18, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     "You force it deeper, but she's not complaining, she looks even more excited."

     you "I'm close, take it all slut!"

     $ pic19 = girl.get_pic("cumshot", and_tags=["anal", "dancer", "mc"], not_tags=["public"], soft=True)
     show screen show_event(pic19, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)
     with fade

     girl.char "Yes, give it to me, i've been a bad slut!"

     "She falls on the ground again with your cum all over her."

     $ pic20 = girl.get_pic("aftersex", and_tags=["mc", "bukkake"], not_tags=["public"], soft=True)
     show screen show_event(pic20, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     you "That felt good, going back now. Thank you for this!"

     play sound s_kind_laugh

     girl.char "I should be the one thanking you, see you around. Come back any time!"

     $ MC.interactions -= 2
     $ girl.change_fear(-10)
     $ girl.change_love(10)
     hide screen show_event




     jump main


 else:


     girl.char "Okay, i did what you wanted, i'm leaving now!"

     $ pic = girl.get_pic("strip", and_tags=["naked", "refuse", "embarassed", "angry"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)



     you "Hey, wait!"

     "She picks up her clothes and leaves."
     $ MC.interactions -= 2
     $ girl.change_fear(+5)

     hide screen show_event


     jump main



 jump main

label office_girl:

 image office = "Mods/Vaan/office.png"
 show office

 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]

 $ girl = rand_choice(able_girls)

 if len(able_girls) == 0: # Important to check that there are enough girls in the brothel before attempting this
     "No girls in the guild at the moment. You go back upstairs."
     scene black with fade
     jump main



 "You tell the girls that you're in the office, doing work and they can come over to you if they're having problems with anything."


 "After a few hours someone knocks on the door."

 girl.char "[MC.name], permission to come in, sir?"

 you "Granted! Come in!"

 $ pic = girl.get_pic("profile", soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 "It's [girl.name], she must need something."

 girl.char "Boss, i heard you're in the office and come over to see if you need anything?"


 you "I do actually, i've been working on some of the missions we got assigned and could use some help to relax."

 girl.char "What would you want me to do?"

 you "How about you get under my desk and give me a blowjob?"

 play sound s_laugh


 if girl.love < 20:

     girl.char "I would have to pass, came to see if you need help on any of the documents."

     you "Ah, well you can have a look at these and go sit on the sofa if you want?"

     girl.char "Sure, i would be happy to!"

     $ MC.change_prestige(10)
     $ girl.change_fear(+5)
     $ girl.change_stat("obedience", -10)



     scene black with fade
     jump main



 else:

     girl.char "I was hoping for a different kind of job, but i guess this will do?"

     you "You can help me with the mission profiles after, how does that sound?"

     play sound s_laugh

     "She goes underneath the desk and takes out your cock."


     $ pic = girl.get_pic("mc", and_tags=["service", "office"], not_tags=["public"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     girl.char "Sounds good enough to me!"

     "You keep working while she sucks your cock, she seems to be concentrating on pleasing you more than actually talking."


     $ pic = girl.get_pic("mc", and_tags=["oral", "office"], not_tags=["public"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     you "That feels great, [girl.name]. Someone looking to get a promotion."

     girl.char "I think you could use a secretary, i would fit that job."


     if girl.love >= 50:

              "She stands up and sits on your lap."



              $ pic = girl.get_pic("mc", and_tags=["sex", "cowgirl", "office"], not_tags=["public"], soft=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


              girl.char "I think you would find me very helpful."

              "You keep fucking her for a while and tell her to bend over your desk."


              $ pic = girl.get_pic("mc", and_tags=["sex", "doggy", "office"], not_tags=["cumshot", "public"], soft=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

              you "Just like that babe."

              girl.char "That feels great boss. You can have me any way you want!"

              play sound s_mmmh
              label office_girl2:



              "Choose position."


              menu:

                 "Doggy":
                  $ pic2 = girl.get_pic("mc", and_tags=["sex", "doggy", "office"], not_tags=["public"], soft=True)
                  show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "You keep going for a bit more and you feel like you're going to cum soon."


                  jump office_girl2







                 "Cowgirl":

                  $ pic3 = girl.get_pic("mc", and_tags=["sex", "cowgirl", "office"], not_tags=["public"], soft=True)
                  show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "She gets on top of you again and rides you hard while moaning."
                  jump office_girl2






                 "Spooning":

                  $ pic = girl.get_pic3("mc", and_tags=["sex", "spooning", "office"], not_tags=["public"], soft=True)
                  show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "You keep fucking her harder."
                  jump office_girl2





                 "Piledriver":

                  $ pic = girl.get_pic3("mc", and_tags=["sex", "piledriver", "office"], not_tags=["public"], soft=True)
                  show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "You push her down and start fucking her again."
                  jump office_girl2


                 "Finish":


                     menu:
                         "In her mouth":
                            "You take it out and push it in her mouth."
                            $ pic = girl.get_pic("mc", and_tags=["cumshot", "in-mouth", "office"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "Tastes so nice."

                            "You spray it in her mouth and she drinks it all with a smile."

                            $ pic = girl.get_pic("mc", and_tags=["cumshot", "in-mouth", "office"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "That was great! Keep me in mind when you do offer a secretary position."

                            $ pic = girl.get_pic("mc", and_tags=["aftersex", "cumshot", "office"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            if not pic:

                                $ pic = girl.get_pic("mc", and_tags=["aftersex", "office"], not_tags=["public"], soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            play sound s_laugh

                            you "Will do, you would make an excellent employee, how about you help with the papers now?"
                            $ MC.change_prestige(+20)
                            $ girl.change_stat("obedience", +3)
                            $ girl.change_stat("fear", -5)
                            $ girl.change_stat("love", +6)


                            scene black with fade
                            jump main

                         "On her face":
                            "You stop fucking her and get your dick close to her face."

                            $ pic = girl.get_pic("mc", and_tags=["cumshot", "on-face", "office"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "Yes, on my face!"

                            "You spray it on her face and she takes it all with a smile."

                            $ pic = girl.get_pic("mc", and_tags=["aftersex", "cumshot", "office"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            if not pic:

                                $ pic = girl.get_pic("mc", and_tags=["aftersex", "office"], not_tags=["public"], soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "That was great! Keep me in mind when you do offer a secretary position."
                            $ MC.change_prestige(20)
                            $ girl.change_stat("obedience", +3)
                            $ girl.change_stat("fear", -5)
                            $ girl.change_stat("love", +6)



                            scene black with fade
                            jump main
                         "On her body":
                          $ pic = girl.get_pic("mc", and_tags=["cumshot", "on-body", "office"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                          girl.char "Yes, i want it all, cum all over me!"
                          "You cum all over her. While she laughs."

                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "cumshot", "office"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          if not pic:
                              $ pic = girl.get_pic("mc", and_tags=["aftersex", "office"], not_tags=["public"], soft=True)
                              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          $ MC.change_prestige(20)
                          $ girl.change_stat("obedience", +3)
                          $ girl.change_stat("fear", -5)
                          $ girl.change_stat("love", +6)



                          scene black with fade
                          jump main

                          girl.char "That was great! Keep me in mind when you do offer a secretary position."
                          you "I will, you can stick around and do the documents now if you want."
                          girl.char "Of course!"
                          $ MC.change_prestige(+20)
                          $ girl.change_stat("obedience", +3)
                          $ girl.change_stat("fear", -5)
                          $ girl.change_stat("love", +6)

                          scene black with fade
                          jump main



                         "Inside her":

                          "You start fucking her harder and faster."

                          $ pic = girl.get_pic("mc", and_tags=["cumshot", "inside", "office"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          girl.char "It's inside me, it feels so good!"

                          "You cum deep inside her and you take your cock out to admire your work!"

                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "inside", "office"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                          if not pic:

                                $ pic = girl.get_pic("mc", and_tags=["aftersex", "office"], not_tags=["public"], soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                          girl.char "That was great! Keep me in mind when you do offer a secretary position."


                          you "I will, you can stick around and do the documents now if you want."

                          girl.char "Of course!"
                          $ MC.change_prestige(+20)
                          $ girl.change_stat("obedience", +3)
                          $ girl.change_stat("fear", -5)
                          $ girl.change_stat("love", +6)

                          scene black with fade
                          jump main




     else:


         "She keeps going faster and you are about to cum. You try and focus on the work and let her deal with it under the desk."


         $ pic = girl.get_pic("mc", and_tags=["service", "cumshot", "office"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Oh wow, [MC.name]! It's all over me, hahaha."


         you "That felt great, you're amazing!"



         $ pic = girl.get_pic("mc", and_tags=["aftersex", "naked", "office"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Thank you, i'll have a look at the pile and see what i can help with."


         you "You're the best, babe. Thanks!"


         play sound s_laugh

         hide screen show_event

         $ MC.change_prestige(20)
         $ girl.change_stat("obedience", +6)
         $ girl.change_stat("fear", -2)
         $ girl.change_stat("love", +3)

         scene black with fade
         jump main
