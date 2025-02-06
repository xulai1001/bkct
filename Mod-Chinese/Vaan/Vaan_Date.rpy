label guild_vip_room_date:


 image guild = "mods/vaan/vip_room.png"
 show guild
 "You find yourself in a room with a dance pole. You sit around and have a drink, she gets a bit tipsy and looks at you."

 $ pic = date_girl.get_pic("profile", soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 date_girl.char "This room is nice and private where no one can see, would you like me to give you a nice private dance?"


 you "Of course! I want to see you on that pole, date_girl!"

 date_girl.char "Hahaha, very well."


 $ pic = date_girl.get_pic("mc", and_tags=["dancer"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 you "Oh wow, keep it up!"

 "The date_girl, is happy you're enjoying her dance, she starts dancing provocative, she is enjoying herself a lot."


 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "tempt"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 you "How about you take your clothes off?"


 date_girl.char "Of course."



 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "strip"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



 date_girl.char "Do you like what you see?"





 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "naked"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "The date_girl is dancing naked in front of you, you wonder if you can take it further and try to grab her."


 play sound s_mmmhs_quiet

 "She seems to be enjoying it."


 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "naked", "fondle"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 "You grab and kiss her all over, while she still tries to move around and dance for you."


 date_girl.char "I'm feeling so horny, how about a blowjob?"


 "She doesn't wait for you to answer and goes down on your dick."


 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "service"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 date_girl.char "Oh wow, it's such a big cock, i love it."



 you "I'm not done yet date_girl, i want to fuck you."


 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "sex"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 play sound s_mmmhs_quiet


 "She is happy to please and you push your cock inside her, you start fucking her where she is."


 date_girl.char "That feels amazing, keep going."


 $ pic2 = date_girl.get_pic("mc", and_tags=["dancer", "sex"], soft=True)
 show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))


 "You keep fucking her and soon you decide to change things."

 you "How about putting it in your ass."

 date_girl.char "Well, what the hell, put it in!"



 $ pic = date_girl.get_pic("mc", and_tags=["dancer", "anal"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You put your cock deep inside her as she keeps moaning, if it wasn't so loud outide someone would have probably heard you."


 you "I'm coming! Take it."


 $ pic3 = date_girl.get_pic("mc", and_tags=["dancer", "cumshot"], soft=True)
 show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))


 date_girl.char "That felt amazing, i'll going out, need to get a drink."

 you "Me too, i'll go and check on the others."


 show screen guild_tavern




screen guild_bedroom_date:

 image "Mods/Vaan/bedroom.png" xalign 0.0 yalign 0.0

 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 20
     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Have sex" action [Hide("guild_bedroom_date"), Jump("bedroom_sex_date")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go to sleep" action [Hide("guild_bedroom_date"), Jump("end_day")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go back" action [Hide("guild_bedroom_date"), Show("guild")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Shower" action [Hide("guild_bedroom_date"), Jump("spy_showers")]






screen guild_tavern_date:


 image "Mods/Vaan/tavern.png" xalign 0.0 yalign 0.0



 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 20
     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Table" action Jump("drink_date")

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "VIP Room" action Jump("entertainment_date")

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go back" action [Hide("guild_tavern_date"), Show("guild_date")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         text "tavern" yalign 0.5 xalign 0.5







screen guild_office_date:

 image "Mods/Vaan/office_night.png" xalign 0.0 yalign 0.0



 grid 2 2:


     xalign 0.5
     yalign 0.5
     spacing 20
     frame:
         xpadding 40
         ypadding 20
         xalign 0.0
         yalign 0.5
         textbutton "Nothing here for now" action Jump("spy_lockers_date")



     frame:
         xpadding 40
         ypadding 20
         xalign 0.0
         yalign 0.3
         textbutton "Go back" action [Hide("guild_office_date"), Show("guild_date")]



     frame:
         xpadding 40
         ypadding 20
         xalign 0.0
         yalign 0.5
         textbutton "Show her your office" action Jump("office_girl_date")



     frame:
         xpadding 40
         ypadding 20
         xalign 0.0
         yalign 0.3
         textbutton "Go back" action [Hide("guild_office_date"), Show("guild_date")]












screen guild_gym_date:
 image "Mods/Vaan/gym.png" xalign 0.0 yalign 0.0



 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 20
     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go inside the lockers" action Jump("spy_lockers_date")

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go inside the gym" action Jump("fight_date")

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go back" action [Hide("guild_gym_date"), Show("guild_date")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         text "Showers" yalign 0.5 xalign 0.5

screen guild_pool_date:
 image "Mods/Vaan/pool.png" xalign 0.0 yalign 0.0



 grid 2 2:
     xalign 0.5
     yalign 0.5
     spacing 20

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go inside the pool" action Jump("pool_alone_date")

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Sunbathe" action Jump("pool_alone_date")

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go back" action [Hide("guild_pool_date"), Show("guild_date")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Give her a massage" action Jump("mc_masseuse_date")






screen guild_date:
 image "Mods/Vaan/guild.png" xalign 0.0 yalign 0.0


 grid 2 4:
     xalign 0.5
     yalign 0.5
     spacing 20
     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Check out the pool" action [Hide("guild_date"), Show("guild_pool_date")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go back" action [Hide("guild_date"), Jump("main")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Go to the gym" action [Hide("guild_date"), Show("guild_gym_date")]

     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5

         if not vaan_tavern_built:

             textbutton "Tavern" action NullAction() # This is needed to make the button sensitive and use tooltips
             tooltip "You haven't built this yet."


         else:
             textbutton "Tavern" action [Hide("guild_date"), Show("guild_tavern_date")]




     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         if not vaan_office_built:
             tooltip "You haven't built this yet."
             textbutton "Office" action NullAction() # This is needed to make the button sensitive and use tooltips


         else:
             textbutton "Office" action [Hide("guild_date"), Show("guild_office_date")]


     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Female only side" action [Hide("guild_date"), Show("date_girls_only_side_date")]


     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Female only side" action [Hide("guild_date"), Show("date_girls_only_side_date")]



     frame:
         xpadding 40
         ypadding 20
         xalign 0.5
         yalign 0.5
         textbutton "Bedroom" action [Hide("guild_date"), Show("guild_bedroom_date")]




label pool_alone_date:

  $ date_girl = girl


  "You decide to go check the pool in the house, [girl.name] looks excited."


  $ pic = girl.get_pic("beach", and_tags=["swim"], not_tags=["cumshot"], soft=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  you "Hi [girl.name], enjoying some time off?"

  girl.char "Yes, the sun is shining bright."

  you "Would you like me to put some sunscreen on you?"


  if girl.get_stat("libido") <= 60 or girl.get_stat("obedience") <= 60:
      girl.char "No thanks, i just want to relax if you don't mind?"


      "After you chat for a few hours she leaves and goes back home."

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
label entertainment_date:
 # Make a list of girls that are present in the brothel and not injured or burned out


 # Take the list above and reduce it to a smaller list, leaving only girls with the "dancer" job


 # Give dancer_girls to rand_choice, which will pick a random thing from any list you put inside its brackets
 $ girl = date_girl


 $ renpy.show("strip club")


 "You decide to go and relax a bit in the strip club and one of the girls comes over to you."

 show screen night(girl.profile)

 girl.char "[MC.name] would you like to get a lap dance?"

 you "I guess i could use some time off, let's go to one of the vip rooms"

 "She looks happy and guides you to the room"


 if girl.is_("very dom") or girl.is_("dom"):

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




label spy_showers_date:

 image lockers = "mods/vaan/showers.png"
 show lockers


 "You try and enter the showers to spy on [date_girl.name] dressing up."


 $ pic = date_girl.get_pic("spy", and_tags=["showers"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You successfully see [date_girl.name] in the shower, she hasn't noticed you yet."


 hide screen show_event
 jump main



label spy_bedroom_date:




 "You try and enter the room of one of the girls who's sleeping."


 $ pic = date_girl.get_pic("spy", and_tags=["rest, sensitivity, mc"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You successfully see [date_girl.name] changing, she hasn't noticed you yet."


 hide screen show_event
 jump main




label spy_bathhouse_date:

 image lockers = "mods/vaan/bathhouse.png"
 show lockers


 "You try and enter the bathhouse to spy on the girls dressing up."


 $ pic = date_girl.get_pic("spy", and_tags=["pool"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You successfully see [date_girl.name] changing, she hasn't noticed you yet."


 hide screen show_event
 jump main



label spy_lockers_date:

 image lockers = "mods/vaan/lockers.png"
 show lockers


 "You try and enter the lockers to spy on the girls dressing up."


 $ pic = date_girl.get_pic("spy", and_tags=["changing room"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You successfully see [date_girl.name] changing, she hasn't noticed you yet."


 hide screen show_event
 jump main

 label mc_masseuse_date:
  $ date_girl = girl


  "You've gotten so many massages from the girls, that you decided to try and learn how to do it yourself, it will also help you get closer to them in many ways."

  "You go into the spa room and tell [girl.name] that you want to give her a massage."

  "Just as you get ready you see [date_girl.name] come over. She looks quite happy."

  $ pic = date_girl.get_pic("profile", soft=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  date_girl.char "Thank you [MC.name], i could really use a nice massage, but don't think about doing anything."

  you "Of course not, this is only for me to be able to get better at this."

  date_girl.char "Of course it is, where would you like me to lie?"

  $ pic = date_girl.get_pic("mc", and_tags=["masseuse"], soft=True)
  show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

  you "Over here is fine, let's get started."


  date_girl.char "That feels so great!"

  "You try to get a bit of a feel while you're massaging, you just couldn't resist the urge, hopefully she won't notice!"

label massage2_date:

 "You keep massaging her and you think you might be able to go further."

 you "I would be able to reach better if we take off your clothes."

 date_girl.char "I don't know, i think you're planning something."

 you "I am really now, i just want to give you the best massage possible!"

 if date_girl.get_stat("sensitivity") <= 40:
     date_girl.char "No, why would i do that?"

     $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "angry", "sensitivity"],  soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     you "Sorry, i was just asking!"


     date_girl.char "I'm leaving, can't believe i even let you touch me, pervert!"


     "She leaves soon after."

     hide screen show_event

     jump main






 else:

     date_girl.char "Of course, that's not a problem. Just don't touch anywhere where you're not supposed to!"

     you "Of course, i'm a professional!"


     $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "strip", "naked"],  soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "You can finally see her sexy body and you can't wait to start massaging her. She will be more sensitive now, so you'll have to be more careful!"


     "You take your time while looking with her and wonder where to begin."


     menu:
         "Grab her ass":

             "You try to grope her and she barely noticed, or perhaps she is secretly enjoying it."

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "naked", "grope"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                 "Hey, get back to what you were doing!"

                 you "I'm sorry, of course, my hand slipped!"
                 jump massage_date

             date_girl.char "Yes, more!"

             you "Glad you're enjoying it."
             jump massage_date


         "Grab her tits":

             "You want to try and ask her to turn around, to play around with her tits, she might notice, but you can just make an excuse and say you made a mistake."
             you "Can you turn around now? I would like to to massage the front"

             date_girl.char "Of course, it feels so good!"

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "naked", "fondle"],  soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                 "Hey, get back to what you were doing!"

                 you "I'm sorry, of course, my hand slipped!"
                 jump massage_date


             date_girl.char "Yes, more!"

             you "Glad you're enjoying it."
             jump massage_date



         "Finger her pussy":

             you "She's been moaning a little bit, maybe i can try and go a bit further"

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "naked", "finger"],  soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                 "Hey, get back to what you were doing!"

                 you "I'm sorry, of course, my hand slipped!"
                 jump massage_date

             date_girl.char "Yes, more!"

             you "Glad you're enjoying it."
             jump massage_date


         "Finger her ass":
             you "She has a nice ass, maybe i can play with it further!"

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "naked", "fisting"],  soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             if not pic:

                 "Hey, get back to what you were doing!"

                 you "I'm sorry, of course, my hand slipped!"
                 jump massage_date

             date_girl.char "Yes, more!"

             you "Glad you're enjoying it."
             jump massage_date


         "Masturbate":

             "You take your dick out and start jerking off. Hoping she won't see you."

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "masturbate"],  soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             date_girl.char "Is everything okay?"

             you "Yes, everything is fine, just need to get more lotion for your beautiful body!"

             date_girl.char "Awww, thank you!"


             you "You jerk off thinking about fucking and soon, you release your cum on her."

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "cumshot"],  soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             date_girl.char "Oh, that feels so warm."

             you "It's a special kind of cream, hope you like it!"

             date_girl.char "I love it!"

             "You finish the massage and she leaves after."

             jump main


         "Finish the massage":
             "You feel like she is close to having an orgasm, so you keep pressing further."

             play sound s_mmmhs_quiet

             "She can hardly contain herself."

             date_girl.char "Oh wow, this is the best massage ever, don't stop!"

             $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "orgasm"],  soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             "She screams loudly of pleasure and soon she looks at you with a smile."




             date_girl.char "Thank you so much, that felt amazing! I'll be sure to come back again."



             you "Of course, anytime you want"



             jump main

label massage_date:


  menu:

      "Grab her ass":


          "You try to grope her and she barely noticed, or perhaps she is secretly enjoying it."

          $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "grope"], soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
          if not pic:

              "Hey, get back to what you were doing!"
              you "I'm sorry, of course, my hand slipped!"
              jump massage_date

          date_girl.char "Yes, more!"

          you "Glad you're enjoying it."
          jump massage_date


      "Grab her tits":

          "You want to try and ask her to turn around, to play around with her tits, she might notice, but you can just make an excuse and say you made a mistake."
          you "Can you turn around now? I would like to to massage the front"

          date_girl.char "Of course, it feels so good!"

          $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "fondle"],  soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
          if not pic:

              "Hey, get back to what you were doing!"

              you "I'm sorry, of course, my hand slipped!"
              jump massage_date

          date_girl.char "Yes, more!"

          you "Glad you're enjoying it."

          jump massage_date

      "Finger her pussy":

          you "She's been moaning a little bit, maybe i can try and go a bit further"
          $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "finger"],  soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
          if not pic:

              "Hey, get back to what you were doing!"

              you "I'm sorry, of course, my hand slipped!"
              jump massage_date

          date_girl.char "Yes, more!"

          you "Glad you're enjoying it."
          jump massage_date

      "Finger her ass":
          you "She has a nice ass, maybe i can play with it further!"

          $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "finger", "fisting"],  soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
          if not pic:

              "Hey, get back to what you were doing!"
              you "I'm sorry, of course, my hand slipped!"
              jump massage_date
          date_girl.char "Yes, more!"

          you "Glad you're enjoying it."
          jump massage_date
      "Go further":
          jump massage2_date

      "Masturbate":

          "You take your dick out and start jerking off. Hoping she won't see you."

          $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "masturbate"],  soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

          date_girl.char "Is everything okay?"

          you "Yes, everything is fine, just need to get more lotion for your beautiful body!"

          date_girl.char "Awww, thank you!"

          you "You jerk off thinking about fucking and soon, you release your cum on her."

          $ pic = date_girl.get_pic("mc", and_tags=["masseuse", "cumshot"],  soft=True)
          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

          date_girl.char "Oh, that feels so warm."

          you "It's a special kind of cream, hope you like it!"

          date_girl.char "I love it!"

          "You finish the massage and she leaves after."

          jump main
      "Finish the massage":
          date_girl.char "Thank you so much, that felt amazing! I'll be sure to come back again."

          you "Of course, anytime you want"
          jump main


label fight_date:

 $ date_girl_def = 4 + date_girl.get_defense()
 $ renpy.show_screen("show_img", brothel.pic, _layer = "master")

 if len(able_girls) == 0:


     "You can't seem to find any date_girls around."
     jump main

 "You hear a noise outside, someone's practicing with a sword or perhaps a people are fighting. You go out to investigate"
 with fade

 "You get closer to the noice and see [date_girl.name]!"
 $ pic = date_girl.get_pic("fight", and_tags=["mc"])
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 you "That's very good [date_girl.name]. How would you like to try and fight me?"

 if date_girl.is_("very dom") or date_girl.is_("dom"):
     date_girl.char "Sure, would be an easy fight. Once you lose, get ready to eat my pussy"
     you "Very wll, but if you lose. I'll make you my whore and fuck you all day, how does that sound?"
     date_girl.char "Hah, you think i'm scared of you? I'm going to enjoy this fight"

 else:
     date_girl.char "Of course, i think it will be good to test my skills on a real opponent. Thank you, [MC.name]!"
     you "Don't mention it, how about we make a little bet? If you win, i'll give you some gold, if i win, i would like you to service me."

     if date_girl.love >= 45:

         date_girl.char "Sure, i'm looking forward to it. Sounds like a win-win situation to me."

     elif date_girl.love <=45:

         date_girl.char "No, thank you!"


 $ tt = show_tt("top_right")
 $ chal = renpy.call_screen("challenge_menu", challenges=[("Fight [date_girl.name]", "fight",  date_girl_def), ("Use magic on her", "control",  date_girl_def)], cancel=("Give up", False))
 hide screen tool

 if chal == "fight":
     $ renpy.block_rollback()
     "You ready your weapon."
     you "It's over for you date_girl, you better get that mouth ready!"

     play sound s_laugh

     date_girl.char "Not yet, this is far from over!"

     call challenge(chal, date_girl_def) from _call_challenge_100 # result is stored in the _show screen home variable
     $ r = _return
     if r:

         play sound "sword sheath.mp3"
         with vpunch
         "The date_girl fights back with everything she can, but she is no match for your skill. You are starting to win this fight!"

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

         "The date_girl is stunned and falls flat on the ground in a cloud of dust. She screams and looks a bit hurt, but nothing she can't shake off."

         play sound s_scream

         you "It was a good fight. You show plenty of promise!"

         date_girl.char "Thank you [MC.name], i will try and get better. One day i'll be as good as you!"

         you "Now, about our bet!"

         date_girl.char "I was hoping you forgot about that!"
         you "Haha, like i would forget, now take your clothes off and show me your body like a good little date_girl"

         if date_girl.is_("very dom") or date_girl.is_("dom"):

             date_girl.char "Very well, a deal is a deal. I'm sure you've been waiting a long time for this. I'm sure you'll cum just from looking at my body either way"


             $ pic = date_girl.get_pic("dom", and_tags=["strip", "nature", "town"], not_tags=["group", "bisexual", "lesbian"], soft=True)

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             date_girl.char "You like what you see? You finally get to see my body, i'm sure it's a great moment for you!"
             you "It really is, i want to fuck you now!"

             date_girl.char "Hah, impatient little boy. Fine, come claim your price, this is the first and last time it happens, so enjoy while it lasts"

             $ pic2 = date_girl.get_pic("dom", and_tags=["sex", "fight", "mc"], not_tags=["group", "bisexual", "lesbian"], soft=True)
             show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))



             date_girl.char "This is what you've been wanting for quite some time now isn't it? You finally got my pussy, i bet it feels good!"

             you "It's not over yet, i want your ass now!"

             date_girl.char "Why would i do that?"

             you "Because if you don't i will beat you again!"

             date_girl.char "Hahaha, i'll let you have it this time, i guess you earned it. But watch your tongue!"

             "The moment you waited for is finally here, you get to fuck your ass and she seems willing to do it. Her ass is so tight, you won't be able to hold on for much!"

             $ pic3 = date_girl.get_pic("dom", and_tags=["anal", "fight", "mc"], not_tags=["group", "bisexual", "lesbian"], soft=True)

             show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_aah

             you "It feels so good, i've been waiting for this for so long!"

             date_girl.char "You finally get to own my ass, even for a little bit. I doubt you'll be able to hold on for long though, hahaha!"

             you "I can't hold much longer, cumming!"

             date_girl.char "Just like i thought, pathetic."


             if date_girl.love >= 50:

                 date_girl.char "It's okay, you can cum inside, just this once!"

                 "You don't wait for second invite and cum deep inside her ass."
                 play sound s_mmmh
                 $ pic4 = date_girl.get_pic("dom", and_tags=["anal", "inside", "mc"], not_tags=["group", "bisexual", "lesbian"], soft=True)
                 show screen show_event(pic4, x=config.screen_width, y=int(config.screen_height*0.8))

                 date_girl.char "That's it, let it out for mommy, good boy!"

                 hide screen show_event

                 date_girl.char "Hope you enjoyed it, it won't happen again anytime soon!"

                 "You both dress up and head back inside"
                 $ date_girl.change_love(2)
                 $ date_girl.change_fear(-10)
                 $ MC.interactions -= 2
                 hide screen show_event

                 jump main







             elif date_girl.love <= 50:

                 date_girl.char "Not inside, like i would ever let a loser like you cum inside me!"

                 "She takes your cock out and let's you cum outside!"

                 $ pic5 = date_girl.get_pic("dom", and_tags=["cumshot", "mc"], not_tags=["group", "bisexual", "lesbian", "inside", "creampie"], soft=True)
                 show screen show_event(pic5, x=config.screen_width, y=int(config.screen_height*0.8))

                 date_girl.char "Hope you enjoyed it, it won't happen again anytime soon!"

                 you "Can i cum inside you next time?"

                 date_girl.char "Like that would ever happen, go away now. I want to be alone!"



                 $ date_girl.change_love(2)
                 $ date_girl.change_fear(-10)
                 $ MC.interactions -= 2
                 hide screen show_event

                 jump main












         else:

             you "Turn around, i want to claim my prize!"

             date_girl.char "Yes, master. Please go easy on me."

             "She turns around, you take off her panties and start fucking her"

             $ pic6 = date_girl.get_pic("sex", and_tags=["doggy", "fight", "mc"], not_tags=["group", "bisexual", "lesbian", "cumshot"], soft=True)
             show screen show_event(pic6, x=config.screen_width, y=int(config.screen_height*0.8))

             play sound s_mmmh

             you "That feels good, going to cum soon!"

             date_girl.char "Yes, master! I want your cum, claim me as your prize!"

             with fade

             $ pic = date_girl.get_pic
             show screen show_event(pic("sex",   and_tags=["doggy", "mc", "fight", "cumshot"], not_tags=["group", "bisexual", "lesbian"]), x=config.screen_width, y=int(config.screen_height*0.8))


             you "It feels so good, take it bitch!"

             play sound s_mmmhs_quiet

             hide screen show_event


             $ pic8 = date_girl.get_pic("profile", soft=True)
             show screen show_event(pic8, x=config.screen_width, y=int(config.screen_height*0.8))


             you "That felt so good!"

             date_girl.char "Looking forward to our next sparring session, haha!"

             you "Me too, have to head back inside, but you can keep practicing if you want, you are definitely showing promise!"

             date_girl.char "Thank you, a bit warmed out from all the *training* we did. But will try again tomorrow!"

             $ date_girl.change_mood(2)

             $ date_girl.change_love(2)
             $ date_girl.change_fear(-10)
             $ date_girl.change_fear(-10)
             $ date_girl.change_fear(-10)
             $ MC.interactions -= 2

             with fade

             hide screen show_event
             with fade

             jump main















     else:

         "You lost the fight"
         $ renpy.block_rollback()

         you "How did i lose against a little girl?"

         "She looks at you with an evil smile and you wonder what she intends to do with you."
         $ result = 0


         if date_girl.is_("very dom") or (intensity >= 2 and date_girl.is_("dom")):

             date_girl.char "Pathetic, i told you i would win. Now stand still, you're going to be my little bitch"
             you "Do what you want, you won!"
             date_girl.char "Call me mistress, my little bitch!"
             you "Yes, mistress!"
             date_girl.char "Good, now stand still, i'll teach you not to mess with me!"
             $ pic = date_girl.get_pic("dom", and_tags=["strap-on", "anal", "mc"], not_tags=["group", "bisexual", "lesbian"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             with fade
             date_girl.char "That's a good boy, make me come and i'll leave you alone for now!"
             you "Yes, mistress."
             $ pic2 = date_girl.get_pic("dom", and_tags=["anal", "strap-on", "mc"], not_tags=["bisexual", "group", "lesbian"])
             show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8))
             date_girl.char "I'm almost there, slave! Make your mistress come!"
             with fade
             $ pic3 = date_girl.get_pic("dom", and_tags=["strap-on", "cumshot", "mc"], not_tags=["bisexual", "group", "lesbian"])
             show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8))
             with fade

             $ pic = date_girl.get_pic("profile", naked_filter=True, soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             date_girl.char "That's a good boy, maybe next time i'll let you fuck me!"



             $ date_girl.change_mood(2)
             $ date_girl.change_love(2)
             $ date_girl.change_fear(-10)
             $ MC.interactions -= 2

             hide screen show_event













             jump main









         else:
             date_girl.char "I won! I'm going to go home now, but this was fun!"
             jump main


label park_date:




 $ girl = date_girl

 "You decide to go to the park and relax."


 image park = "mods/vaan/park.png"

 show park




 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "The park is huge, full of trees, plants and animals. You walk around to find a place to sit and relax on the grass."


 girl.char "This was a great idea, i haven't been able to relax outdoors like this in so long."


 you "It's quite nice, the weather is great and it's quite warm outside too."


 $ pic = girl.get_pic("date, mc", and_tags=["nature"], naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "You walk around a bit more and finally find a place to sit."


 "You talk about life, working in the hotel and things you have in common."

 python:

     for girl in MC.girls:



         ## Dialogue dictionary ##

         dialogue_dict = defaultdict(return_ddict_list)




         add_dialogue("date_girl", ("generic"), "You're all right. I think you're kind.", love=0)
         add_dialogue("date_girl", ("generic"), "I like you. I enjoy being with you.", love=1)
         add_dialogue("date_girl", ("generic"), "I'm so happy to be here, thank you for inviting me.")


         add_dialogue("date_girl", ("generic"), ("My favorite [thing] is [best].")) # Argument is 'thing', 'favourite'
         add_dialogue("date_girl", ("generic"), ("One [thing] I really don't like is [worst]. Ew!", "One [thing] I hate is [worst].")) # Argument is 'thing', 'least favourite'


         date_girl.say("date_girl")


 date_girl.char "Thank you for this, i'm having an amzing time, is there anything you want to do?"

 label park_date2:

 $ girl = date_girl


 menu:


    "Nothing else really":


     you "Let's just enjoy our time and go back home."


     $ pic = girl.get_pic("date, mc", and_tags=["nature", "tempt"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She moves around provocatively like she's trying to tell you, you made the right choice."


     $ pic = girl.get_pic("date, mc", and_tags=["nature", "strip"], naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     girl.char "Keep going like that and maybe next time you'll get a piece of this."


     you "I would love that, very much."

     girl.char "Or maybe you won't have to wait until next time, the day is still young."


     play sound s_laugh


     $ date_girl.change_stat("obedience", +5)
     $ date_girl.change_stat("fear", -4)
     $ date_girl.change_stat("love", +5)

     jump date_back





    "Try to get a blowjob":

     you "There aren't that many people around, how about we go hide behind that big three and you can give me a blowjob?"

     if girl.love < 25:

         girl.char "I think you're moving a bit too fast aren't you? I barely even know you!"

         python:
             for girl in MC.girls:

                 add_dialogue("date_girl2", ("generic"), ("Are you trying to push my buttons?", "You're obsessed with this, aren't you?", "Ugh, no way..."))
                 add_dialogue("date_girl2", ("generic"), ("And what if I say no?", "I don't want to.", "I'm gonna pass on that one."))

                 date_girl.say("date_girl")




         girl.char "I'm still happy to do something else though?"

         $ date_girl.change_stat("obedience", -10)
         $ date_girl.change_stat("fear", -6)
         $ date_girl.change_stat("love", -9)

         jump park_date2

     else:

         python:
             for girl in MC.girls:

                 add_dialogue("date_girl2", ("generic"), ("You've been looking at me all day, might as well", "You're obsessed with this, aren't you?", "Ugh, fine..."))
                 add_dialogue("date_girl2", ("generic"), ("Let's do it.", "Where should we go?", "I've been waiting for this"))
                 add_dialogue("date_girl2", ("generic"), ("Come on, [MC.name].", "If you really want to, i don't mind [MC.name].", "I think i saw a good place, follow me."))

                 date_girl.say("date_girl2")




         "You go somewhere private and she gets on her knees."

         $ pic = girl.get_pic("date, mc", and_tags=["nature", "service"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         python:
             for girl in MC.girls:

                 add_dialogue("date_girl2", ("generic"), ("You've been looking at me all day, might as well", "You're obsessed with this, aren't you?", "Ugh, fine..."))
                 add_dialogue("date_girl2", ("generic"), ("Let's do it.", "Where should we go?", "I've been waiting for this"))
                 add_dialogue("date_girl2", ("generic"), ("Come on, [MC.name].", "If you really want to, i don't mind [MC.name].", "I think i saw a good place, follow me."))

                 date_girl.say("date_girl2")


         $ pic = girl.get_pic("date, mc", and_tags=["nature", "oral"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         "She keeps going while you keep a lookout."

         you "Take it deep, my little slut. I know you can do it."


         $ pic = girl.get_pic("date, mc", and_tags=["nature", "deep"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         python:
             for girl in MC.girls:


                 add_dialogue("date_girl2", ("generic"), ("[MC.name], I want your cum", "Please don't make me beg... Give it to me"))
                 add_dialogue("date_girl2", ("generic"), ("It's so shameful doint it here, but i feel turned on.", "You love cumming all over me don't you?", "What a great way to spend a day in the park, hahaha."))
                 add_dialogue("date_girl2", ("generic"), ("[MC.name], your cum tastes so nice... AAAAAH! It's so good to be a bad girl...", "I hope no one saw this." "Let's go before someone sees us."))

                 date_girl.say("date_girl2")


         "You feel like you're close to cumming."


         menu:

           "In her mouth":

             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "in-mouth"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             python:
                 for girl in MC.girls:


                     add_dialogue("date_girl2", ("generic"), ("[MC.name], I want your cum", "Please don't make me beg... Give it to me"))
                     add_dialogue("date_girl2", ("generic"), ("It's so shameful doint it here, but i feel turned on.", "You love cumming all over me don't you?", "What a great way to spend a day in the park, hahaha."))
                     add_dialogue("date_girl2", ("generic"), ("[MC.name], your cum tastes so nice... AAAAAH! It's so good to be a bad girl...", "I hope no one saw this." "Let's go before someone sees us."))

                     date_girl.say("date_girl2")


             hide screen show_event

             $ date_girl.change_stat("obedience", +3)
             $ date_girl.change_stat("fear", -1)
             $ date_girl.change_stat("love", +2)

             jump date_back



           "On her face":

             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "on-face"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



             python:
                 for girl in MC.girls:


                     add_dialogue("date_girl2", ("generic"), ("[MC.name], I want your cum", "Please don't make me beg... Give it to me"))
                     add_dialogue("date_girl2", ("generic"), ("It's so shameful doint it here, but i feel turned on.", "You love cumming all over me don't you?", "What a great way to spend a day in the park, hahaha."))
                     add_dialogue("date_girl2", ("generic"), ("[MC.name], your cum tastes so nice... AAAAAH! It's so good to be a bad girl...", "I hope no one saw this." "Let's go before someone sees us."))

                     date_girl.say("date_girl2")


             hide screen show_event
             $ date_girl.change_stat("obedience", +9)
             $ date_girl.change_stat("fear", -8)
             $ date_girl.change_stat("love", +7)

             jump date_back

           "On her body":


             $ pic = girl.get_pic("mc", and_tags=["rest", "cumshot", "on-body"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))




             python:
                 for girl in MC.girls:


                     add_dialogue("date_girl2", ("generic"), ("[MC.name], I want your cum", "Please don't make me beg... Give it to me"))
                     add_dialogue("date_girl2", ("generic"), ("It's so shameful doint it here, but i feel turned on.", "You love cumming all over me don't you?", "What a great way to spend a day in the park, hahaha."))
                     add_dialogue("date_girl2", ("generic"), ("[MC.name], your cum tastes so nice... AAAAAH! It's so good to be a bad girl...", "I hope no one saw this." "Let's go before someone sees us."))

                     date_girl.say("date_girl2")


             hide screen show_event

             $ date_girl.change_stat("obedience", +7)
             $ date_girl.change_stat("fear", -2)
             $ date_girl.change_stat("love", +3)

             jump date_back
















    "Sex":

     "Not Yet"


    "Anal":

     "Not Yet"



























label town_date:
 $ girl = date_girl
 "You decide to go to into town and see what's there to see."




 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "They bring new stock every week, let's go around and do some shopping!"

 "Where should you go?"

 menu:

    "Shopping":


     "You give in and decide to go around and see what's in the stores."


     $ pic = girl.get_pic("mc", and_tags=["date", "town", "tempt"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She walks around and keeps playfully showing off for you. It's been an hour although it feels like days for you."


     girl.char "Oh wow, i didn't know they have this store here. Should we go and check? I want to buy some new clothes."


     you "Maybe we can go to that tavern you spoke about?"


     play sound s_laugh


     girl.char "Hahaha, too late now, come on! I want to see what they have, if you do it, i might do a little show for you!"

     $ pic = girl.get_pic("mc", and_tags=["date", "town", "tempt", "strip"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She moves around a little bit and shows you her tits in public, you can't help but want to go, you might be able to see more!"


     "She went into the dressing room and you wonder whether you should try your luck and peak on her."


     menu:





        "Wait for her":

         "You sat where you were until she came out of the dressing room."

         girl.char "How do i look?"

         $ pic = girl.get_pic("mc", and_tags=["date", "dress"], not_tags=["sex", "service", "anal", "group"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         you "It looks amazing!"

         girl.char "Glad you like it, i'll go an pay and we can go."

         $ date_girl.change_stat("obedience", +5)
         $ date_girl.change_stat("fear", -4)
         $ date_girl.change_stat("love", +5)

         jump date_back


        "Spy on her":

         "You take a peak and you manage to see her."

         $ pic = date_girl.get_pic("spy", and_tags=["changing room"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         "She takes of her clothes while you try to not get caught"


         $ pic = date_girl.get_pic("spy", and_tags=["changing room", "strip", "underwear"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You can see her sexy underwear and you can't help but get a boner. You wonder if it's too much to take it out and jerk off to her."


         menu:


            "Keep spying":

             "You decide against it."

             "Instead you keep watching her for a bit more."

             $ pic = date_girl.get_pic("spy", and_tags=["changing room", "naked", "strip"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "I don't want to get caught, i need to go back."

             "You wait for a bit more and she comes out."


             girl.char "How do i look?"
             $ pic = girl.get_pic("mc", and_tags=["date", "dress"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             you "It looks amazing!"
             girl.char "Glad you like it, i'll go an pay and we can go."

             $ date_girl.change_stat("obedience", +5)

             $ date_girl.change_stat("fear", -4)

             $ date_girl.change_stat("love", +5)

             jump date_back


            "Take your cock out":


             $ pic = date_girl.get_pic("spy", and_tags=["changing room", "masturbate"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "It's too much for you and you can't help but jerk off while you watch her."



             $ pic = date_girl.get_pic("spy", and_tags=["changing room", "strip", "naked"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             "She is taking her clothes off completely and you feel like you're about to burst."



             $ pic = date_girl.get_pic("spy", and_tags=["changing room", "naked"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             "You can't hold it anymore and cum on the door, hoping no one noticed."


             $ pic = date_girl.get_pic("spy", and_tags=["changing room", "masturbate", "cumshot"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "That felt great, need to go back before she sees me!"


             "You wait for a bit more and she comes out."


             girl.char "How do i look?"
             $ pic = girl.get_pic("mc", and_tags=["date", "dress"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             you "It looks amazing!"
             girl.char "Glad you like it, i'll go an pay and we can go."
             $ date_girl.change_stat("obedience", +5)
             $ date_girl.change_stat("fear", -4)
             $ date_girl.change_stat("love", +5)

             jump date_back





    "Tavern":

     you "Let's go have some fun in the tavern, get a drink and dance with the folk."

     girl.char "Sounds great, let's go!"



     $ pic = date_girl.get_pic("mc", and_tags=["date", "town"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "There's music playing as you approach the tavern, you can already see people outside laughing and having a drink."


     $ pic = date_girl.get_pic("mc", and_tags=["date", "public"], not_tags=["service", "sex", "anal", "group"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "You find a table and have a drink."


     girl.char "Wow, this place is amazing!"




     "After a few drinks you feel quite a bit drunk and want to do something stupid."


     menu:




        "Ask for a blowjob":

         you "I was wondering, do you want to go somewhere private? I was wondering if you wanted to do something?"
         date_girl.char "Oh, like what?"
         you "How about a blowjob?"

         if date_girl.love <= 20:
             date_girl.char "I don't think so. Is that why you wanted to go out? I expected better from you. I'm going to go home..."
             you "I'm sorry, i thought you would be fine with it."
             date_girl.char "Goodbye!!!"
             "She walks off angrily, you could have played that better, you think to yourself."
             $ date_girl.change_stat("obedience", -3)
             $ date_girl.change_stat("fear", +9)
             $ date_girl.change_stat("love", -4)

         else:
             date_girl.char "Sure, let's go over there, not too many people."
             $ pic = date_girl.get_pic("mc", and_tags=["beach", "service"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             "She gets on her knees and stars sucking you off."

             date_girl.char "Enjoying it?"

             you "Hell yeah, it feels amazing."

             $ pic = date_girl.get_pic("mc", and_tags=["beach", "service", "oral"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She keeps going while you look around to see if anyone is watching."
             date_girl.char "I didn't expect i would be doing this here."

             play sound s_laugh
             you "Well, i always try to surprise."

             "You feel like you can'd hold it anymore."

             you "I'm cumming, babe."
             $ pic = date_girl.get_pic("beach", and_tags=["mc", "service", "cumshot"], soft=True)

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             you "I'll paint your pretty face and mouth, open up."

             "She takes it all with a smile on her face."

             $ pic = date_girl.get_pic("mc", and_tags=["beach", "aftersex"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             date_girl.char "That felt great, let's go back to the hotel."

             you "Of course, let's go."

             $ date_girl.change_stat("obedience", +10)
             $ date_girl.change_stat("fear", -2)
             $ date_girl.change_stat("love", +10)

             hide screen show_event
             jump date_back

        "Ask for Sex":

         you "I was wondering, do you want to go somewhere private? I was wondering if you wanted to do something?"

         date_girl.char "Oh, like what?"

         you "How about sex?"

         if date_girl.love <= 40:

             date_girl.char "I don't think so. Is that why you wanted to go out? I expected better from you. I'm going to go home..."

             you "I'm sorry, i thought you would be fine with it. We've already done other things..."

             date_girl.char "And because we've done other things, you think it will be fine to do that too?"

             "She walks off angrily, you could have played that better, you think to yourself."

             $ date_girl.change_stat("obedience", -4)
             $ date_girl.change_stat("fear", +3)
             $ date_girl.change_stat("love", -1)
             jump main





         else:
             date_girl.char "Sure, let's go over there, not too many people."
             $ pic = date_girl.get_pic("mc", and_tags=["public", "sex", "doggy"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She bends over and lets you fuck her."
             date_girl.char "Enjoying it?"
             you "Hell yeah, it feels amazing."

             $ pic = date_girl.get_pic("mc", and_tags=["public", "mc", "sex"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She keeps going while you look around to see if anyone is watching."

             date_girl.char "I didn't expect i would be doing this here."

             play sound s_laugh

             you "Well, i always try to surprise."

             "You feel like you can'd hold it anymore."

             you "I'm cumming, babe."

             $ pic = date_girl.get_pic("mc", and_tags=["public", "sex", "cumshot"], soft=True)

             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             you "I'll paint your pretty face and mouth, open up."

             "She takes it all with a smile on her face."

             $ pic = date_girl.get_pic("mc", and_tags=["public", "aftersex"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             date_girl.char "That felt great, let's go back to the hotel."
             you "Of course, let's go."

             $ date_girl.change_stat("obedience", +8)
             $ date_girl.change_stat("fear", -10)
             $ date_girl.change_stat("love", +10)

             hide screen show_event

             jump date_back






        "Ask for Anal":

         you "I was wondering, do you want to go somewhere private? I was wondering if you wanted to do something?"

         date_girl.char "Oh, like what?"

         you "How about you let me put it in your ass?"


         if date_girl.love <= 75:
             date_girl.char "I don't think so. Is that why you wanted to go out? I expected better from you. I'm going to go home..."

             you "I'm sorry, i thought you would be fine with it. We've already done other things..."
             date_girl.char "And because we've done other things, you think it will be fine to do that too?"

             "She walks off angrily, you could have played that better, you think to yourself."

             $ date_girl.change_stat("obedience", -3)
             $ date_girl.change_stat("fear", +5)
             $ date_girl.change_stat("love", -7)




         else:
             date_girl.char "Sure, let's go over there, not too many people."


             $ pic = date_girl.get_pic("mc", and_tags=["public", "anal", "doggy"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She bends over and let's you fuck her."

             date_girl.char "Enjoying it?"

             you "Hell yeah, it feels amazing."

             $ pic = date_girl.get_pic("mc", and_tags=["public", "anal"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She keeps going while you look around to see if anyone is watching."

             date_girl.char "Fuck me harder! Keep going!"

             play sound s_laugh

             you "You ass feels so tight, [date_girl.name]."


             "You feel like you can'd hold it anymore."

             you "I'm cumming, babe."


             $ pic = date_girl.get_pic("mc", and_tags=["public", "anal", "cumshot"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "I'll paint your pretty face and mouth, open up."

             "She takes it all with a smile on her face."



             $ pic = date_girl.get_pic("mc", and_tags=["public",  "aftersex"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             date_girl.char "That felt great, let's go back to the hotel."


             you "Of course, let's go."


             $ date_girl.change_stat("obedience", +1)
             $ date_girl.change_stat("fear", -4)
             $ date_girl.change_stat("love", +2)


             hide screen show_event

             jump date_back



label date_beach:



 "The day has finally arrived, you're prepared to have a good time with [date_girl.name]"


 "You wait outside the hotel for her and you can soon see her come over too."


 $ pic = date_girl.get_pic("profile", soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 date_girl.char "Let's go, the beach awaits!"


 image beach = "mods/vaan/beach.png"

 show beach
 "After half an hour, you finally made it to the beach!"


 $ pic = date_girl.get_pic("date", and_tags=["beach", "mc"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 date_girl.char "It's quite warm today!"

 $ pic = date_girl.get_pic("date", and_tags=["beach", "mc"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
 "You spend your day on the beach and [date_girl.name] seems to enjoy it."


 date_girl.char "The water is quite warm, should we walk around for a bit?"


 you "Sure."

 $ pic = date_girl.get_pic("date", and_tags=["beach", "mc"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 "As you walk with her, you think about your next move."


 "She looks so hot in her swimsuit, you want to fuck her."

 $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "tempt"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 menu:

    "Ask for a blowjob":

     you "I was wondering, do you want to go somewhere private? I was wondering if you wanted to do something?"

     date_girl.char "Oh, like what?"

     you "How about a blowjob?"


     if date_girl.love <= 20:

         date_girl.char "I don't think so. Is that why you wanted to go out? I expected better from you. I'm going to go home..."

         you "I'm sorry, i thought you would be fine with it."

         date_girl.char "Goodbye!!!"

         "She walks off angrily, you could have played that better, you think to yourself."

         $ date_girl.change_stat("obedience", -6)
         $ date_girl.change_stat("fear", +8)
         $ date_girl.change_stat("love", -7)


     else:

         date_girl.char "Sure, let's go over there, not too many people."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "service"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She gets on her knees and stars sucking you off."

         date_girl.char "Enjoying it?"

         you "Hell yeah, it feels amazing."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "service", "oral"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She keeps going while you look around to see if anyone is watching."

         date_girl.char "I didn't expect i would be doing this here."

         play sound s_laugh

         you "Well, i always try to surprise."


         "You feel like you can'd hold it anymore."

         you "I'm cumming, babe."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "service", "cumshot"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         you "I'll paint your pretty face and mouth, open up."

         "She takes it all with a smile on her face."




         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "aftersex"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         date_girl.char "That felt great, let's go back to the hotel."


         you "Of course, let's go."


         $ date_girl.change_stat("obedience", +6)
         $ date_girl.change_stat("fear", -4)
         $ date_girl.change_stat("love", +6)


         hide screen show_event

         jump date_back


    "Ask for Sex":

     you "I was wondering, do you want to go somewhere private? I was wondering if you wanted to do something?"

     date_girl.char "Oh, like what?"

     you "How about sex?"


     if date_girl.love <= 40:

         date_girl.char "I don't think so. Is that why you wanted to go out? I expected better from you. I'm going to go home..."

         you "I'm sorry, i thought you would be fine with it. We've already done other things..."

         date_girl.char "And because we've done other things, you think it will be fine to do that too?"

         "She walks off angrily, you could have played that better, you think to yourself."

         $ date_girl.change_stat("obedience", -8)
         $ date_girl.change_stat("fear", +4)
         $ date_girl.change_stat("love", -9)


     else:

         date_girl.char "Sure, let's go over there, not too many people."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "sex", "doggy"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She bends over and let's you fuck her."

         date_girl.char "Enjoying it?"

         you "Hell yeah, it feels amazing."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "sex"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She keeps going while you look around to see if anyone is watching."

         date_girl.char "I didn't expect i would be doing this here."

         play sound s_laugh

         you "Well, i always try to surprise."


         "You feel like you can'd hold it anymore."

         you "I'm cumming, babe."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "sex", "cumshot"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         you "I'll paint your pretty face and mouth, open up."

         "She takes it all with a smile on her face."




         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "aftersex"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         date_girl.char "That felt great, let's go back to the hotel."


         you "Of course, let's go."


         $ date_girl.change_stat("obedience", +8)
         $ date_girl.change_stat("fear", -10)
         $ date_girl.change_stat("love", +10)


         hide screen show_event

         jump date_back


    "Ask for Anal":

     you "I was wondering, do you want to go somewhere private? I was wondering if you wanted to do something?"

     date_girl.char "Oh, like what?"

     you "How about you let me put it in your ass?"


     if date_girl.love <= 40:

         date_girl.char "I don't think so. Is that why you wanted to go out? I expected better from you. I'm going to go home..."

         you "I'm sorry, i thought you would be fine with it. We've already done other things..."

         date_girl.char "And because we've done other things, you think it will be fine to do that too?"

         "She walks off angrily, you could have played that better, you think to yourself."

         $ date_girl.change_stat("obedience", -3)
         $ date_girl.change_stat("fear", +5)
         $ date_girl.change_stat("love", -7)


     else:

         date_girl.char "Sure, let's go over there, not too many people."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "anal", "doggy"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She bends over and let's you fuck her."

         date_girl.char "Enjoying it?"

         you "Hell yeah, it feels amazing."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "anal"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She keeps going while you look around to see if anyone is watching."

         date_girl.char "Fuck me harder! Keep going!"

         play sound s_laugh

         you "You ass feels so tight, [date_girl.name]."


         "You feel like you can'd hold it anymore."

         you "I'm cumming, babe."


         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "anal", "cumshot"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         you "I'll paint your pretty face and mouth, open up."

         "She takes it all with a smile on her face."




         $ pic = date_girl.get_pic("date", and_tags=["beach", "mc", "aftersex"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         date_girl.char "That felt great, let's go back to the hotel."


         you "Of course, let's go."


         $ date_girl.change_stat("obedience", +1)
         $ date_girl.change_stat("fear", -4)
         $ date_girl.change_stat("love", +2)


         hide screen show_event

         jump date_back

label date_back:

 $ girl = date_girl

 "On the way back you wonder what to do, you wonder whether you should ask her to stay over."


 menu:

    "Bring her to your Guild House":

     if vaan_house_built:

         call screen guild_date


     else:

         "You haven't bought a Guild House yet."


         jump date_back



    "Go home":

     "You're pretty tired and decide to head back home."

     girl.char "I had a great time! We should do this again sometime."

     you "Definitely!"

     $ pic = date_girl.get_pic("date", and_tags=["mc", "kiss", "town"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
     if not pic:
         $ pic = date_girl.get_pic("date", and_tags=["mc", "kiss", "public"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



     "You give her a kiss and head back home."

     hide screen show_event

     jump main









































label date:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ date_girl = long_menu("Choose which girl to ask out", [(g.name, g) for g in MC.girls])


 if len(MC.girls) == 0: # Important to check that there are enough date_girls in the brothel before attempting this

     "There are no girls to ask out."

     jump main





 "You've been thinking about [date_girl.name] lately and that sweet ass of hers. You think it might be time to try and ask her on a date."




 $ pic = date_girl.get_pic("profile", soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 if date_girl.fear >= 0:

     date_girl.char "Yes, [MC.name]? Can i help you?"


     you "Hi [date_girl.name], i was wondering if you want to go out?"


     date_girl.char "No, thank you, i have some other things to do."


     you "Ah, some other time then."

     hide screen show_event

     jump main


 if date_girl.fear <= 0:

     date_girl.char "Yes, [MC.name]? Can i help you?"


     you "Hi [date_girl.name], i was wondering if you want to go out?"


     date_girl.char "I guess so, when do you want to go?"


     menu:
        "Monday":

             date_girl.char "Monday is fine, where do you want to go?"



             menu:




                "Beach":

                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Monday"))


                 hide screen show_event

                 jump main








                "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Monday"))





                 hide screen show_event



                 jump main








                "Park":

                    date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                    you "That's great, see you then!"


                    date_girl.char "Can't wait!"


                    $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Thursday"))







                    hide screen show_event

                    jump main










        "Tuesday":

         date_girl.char "Tuesday is fine, where do you want to go?"



         menu:
             "Beach":
                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"

                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Tuesday"))

                 hide screen show_event



                 jump main





             "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Tuesday"))



                 hide screen show_event





                 jump main



             "Park":

                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Tuesday"))







                 hide screen show_event

                 jump main






        "Wednesday":


         date_girl.char "Wednesday is fine, where do you want to go?"



         menu:

             "Beach":
                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Wednesday"))
                 hide screen show_event

                 jump main







             "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Wednesday"))





                 hide screen show_event



                 jump main




             "Park":

                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Wednesday"))







                 hide screen show_event

                 jump main







        "Thursday":
         date_girl.char "Thursday is fine, where do you want to go?"



         menu:
             "Beach":
                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Thursday"))
                 hide screen show_event
                 hide screen show_event


             "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Thursday"))
                 hide screen show_event

                 jump main





             "Park":

                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Thursday"))







                 hide screen show_event

                 jump main


        "Friday":
         date_girl.char "Fridayy is fine, where do you want to go?"



         menu:
             "Beach":
                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Friday"))


                 hide screen show_event


             "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Friday"))
                 hide screen show_event

                 jump main


             "Park":

                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Friday"))




                 hide screen show_event

                 jump main
        "Saturday":

         date_girl.char "Saturday is fine, where do you want to go?"



         menu:
             "Beach":
                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Saturday"))



                 hide screen show_event



             "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Saturday"))







                 hide screen show_event

                 jump main

             "Park":

                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Saturday"))

                 hide screen show_event

                 jump main

        "Sunday":


         date_girl.char "Sunday is fine, where do you want to go?"



         menu:

             "Beach":
                 date_girl.char "Great, i can't wait! We can go swim in the water or just lie around in the sand, sounds fun!"


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "date_beach", weekday="Sunday"))


                 hide screen show_event


                 jump main




             "Town":


                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "town_date", weekday="Sunday"))


                 hide screen show_event

                 jump main



             "Park":

                 date_girl.char "Great, i can't wait! We can go shopping or maybe a restaurant. There's also a nice tavern where people go to dance and drink."


                 you "That's great, see you then!"


                 date_girl.char "Can't wait!"


                 $ calendar.set_alarm(calendar.time, StoryEvent(label = "park_date", weekday="Sunday"))

                 hide screen show_event

                 jump main









label bedroom_sex_date:

 image bedroom = "mods/vaan/bedroom.png"
 show bedroom


 $ girl = date_girl


 "You bring [girl.name] over to your bedroom and she looks at you with a smile."


 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "Your bedroom is huge!"

 you "Thank you, you know what else is huge?"

 play sound s_laugh

 girl.char "Well, i imagine you'll show me?"




 if girl.love < 15:

     girl.char "Sorry, [MC.name]. I'll need to get back home. Another work day tomorrow."

     you "Ah, that's fair. I'll see you tomorrow then."

     girl.char "Have a goodnight sleep too, [MC.name]."

     "You stay awake for a bit more after she leaves and you finally go back to sleep."

     jump end_day




 else:
     girl.char "Well, i came this far. Might as well end the night properly."

     play sound s_laugh



     $ pic = girl.get_pic("mc", and_tags=["bedroom", "tempt"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She climbs on the bed and looks at you with a smile."


     girl.char "Do you like what i'm wearing?"

     you "I do! You look so hot!"

     $ pic = girl.get_pic("mc", and_tags=["rest", "kiss", "fondle"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "You touch her everywhere and kiss her while she lets out a moan."

     play sound s_mmmh

     $ pic = girl.get_pic("mc", and_tags=["bedroom", "kiss", "fondle", "strip"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "You take off her clothes slowly while you kiss her, she touches your cock and smiles."


     girl.char "Let's see what we have here!"


     $ pic = girl.get_pic("mc", and_tags=["bedroom", "handjob"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     "She plays with your cock for a bit and teases you even more."

     girl.char "Time to take this off completely."



     $ pic = girl.get_pic("mc", and_tags=["bedroom", "strip", "naked"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She takes off all her clothes and goes back to on your dick."


     you "Suck it, [girl.name]."


     $ pic = girl.get_pic("mc", and_tags=["bedroom", "service", "oral"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She takes it in her mouth and looks at you."

     girl.char "I'm so happy i came, would have been all alone in my room tonight."


     you "I'm happy you came too."

     $ pic = girl.get_pic("mc", and_tags=["bedroom", "service", "oral"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     "She keeps sucking on your cock and you're soon ready to cum."

     girl.char "Cum wherever you want, boss! I want it all!"

     menu:

       "In her mouth":

         $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "in-mouth"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Yes, i want it all, give it to me!"

         "You spray it in her mouth and she drinks it all with a smile."

         girl.char "That was great! Thank you!"



       "On her face":

         $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "on-face"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Yes, i want it all, give it to me!"

         "You spray it on her face and she takes it all with a smile."

         girl.char "That was great! Thank you!"

       "On her body":


         $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "on-body"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Yes, i want it all, give it to me!"

         "You cum all over her. While she giggles."

         girl.char "That was great! It's all over me"



     you "How about we keep going? I want to to fuck!"


     girl.char "Blowjob wasn't enough eh? I don't know..."

     if girl.love < 50:


         girl.char "I'm too tired, how about we just go to sleep?"

         you "Okay, i guess we can. I got proper service at least!"

         girl.char "And i got cum all over, we both win haha!"

         $ pic = girl.get_pic("mc", and_tags=["bedroom", "aftersex", "wet"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         girl.char "I'm just going to go wash up, maybe take a shower."

         you "That's fine, i'm so tired i can hardly stay awake either way."

         "You manage to go to finally go to sleep for the night."

         hide screen show_event

         jump end_day


     elif girl.love > 50:


         girl.char "Ah, what the hell. Let's do it!"

         "Without waiting she pushes you on the bed and jumps on your cock."


         $ pic = girl.get_pic("mc", and_tags=["bedroom", "sex", "cowgirl"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
         play sound s_mmmh

         you "Hell, yes! Keep going [girl.name]!"

         girl.char "I can really use a good fucking and since you've been so nice to me lately, i don't see why not!"

         $ pic = girl.get_pic("mc", and_tags=["bedroom", "sex", "doggy"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You bend her over and start fucking her from behind."

         "She doesn't stop moaning the entire time, she's loving your cock."

         play sound s_mmmh


         you "Come over here!"

         girl.char "Do it harder!"


         $ pic = girl.get_pic("mc", and_tags=["bedroom", "sex", "spooning"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You keep fucking her like there's no tomorrow! She's loving it!"

         girl.char "Yes, [MC.name], it's so deep.!"



         $ pic = girl.get_pic("mc", and_tags=["bedroom", "sex", "piledriver"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         "You feel like you're close to cumming, you won't be able to hold it."


         $ pic = girl.get_pic("mc", and_tags=["bedroom", "sex", "orgasm"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         play sound s_mmmh


         "She came hard and hearing the sounds she's making you can't hold it any longer."

         menu:

           "In her mouth":
             "You take it out and push it in her mouth."
             $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "in-mouth"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "Tastes so nice."

             "You spray it in her mouth and she drinks it all with a smile."

             girl.char "That was great! Thank you!"


             hide screen show_event

             jump end_day


           "On her face":
             "You stop fucking her and get your dick close to her face."

             $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "on-face"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "Yes, on my face!"

             "You spray it on her face and she takes it all with a smile."

             girl.char "That was great! Thank you!"


             hide screen show_event

             jump end_day
           "On her body":

             $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "on-body"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
             girl.char "Yes, i want it all, cum all over me!"

             "You cum all over her. While she giggles."

             girl.char "Oh wow, i won't be able to move properly for a while, i need rest."
             hide screen show_event

             jump end_day



           "Inside her":

             "You start fucking her harder and faster."

             $ pic = girl.get_pic("mc", and_tags=["bedroom", "cumshot", "inside"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             girl.char "It's inside me, it feels so good!"

             "You cum deep inside her and you take your cock out to admire your work!"

             $ pic = girl.get_pic("mc", and_tags=["bedroom", "aftersex", "cumshot"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "She manages to gather some strength to lift herself up and looks at you with a smile."

             girl.char "This was amazing, i'll go wash up and then we can go to sleep!"


             $ pic = girl.get_pic("mc", and_tags=["bedroom", "aftersex", "wet"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


             you "That's fine, i'm so tired i can hardly stay awake either way."

             "You manage to go to finally go to sleep for the night."

             hide screen show_event

             jump end_day




     hide screen show_event

     jump end_day



label drink_date:
 $ able_girls = [g for g in MC.girls if not (g.away or g.hurt or g.exhausted)]
 $ date_girl = girl


 image tavern = "Mods/Vaan/tavern.png"

 show tavern

 "You walk into the guild Tavern to have a drink with [girl.name]."



 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

 girl.char "Can i get you anything, [MC.name]?"

 you "Just get me a beer, i'll go and sit down for a bit."

 girl.char "Sure, i'll get [girl.name] to bring it to you, enjoy!"

 "After a while you see [girl.name] with your drink."

 $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


 girl.char "Here you go, mind if i sit with you?"


 menu:

    "Yes":

     you "Sorry, [girl.name]. I'd rather drink alone."

     $ pic = girl.get_pic("waitress", naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


     girl.char "I understand, call me if you need anything."

     "She goes back to the bar."

     "You pour yourself a drink and stick around for an hour, then go back out."

     scene black with fade
     jump main


    "No, be my guest.":

     "She sits next to you and you chat with her for a few minutes."

     $ pic = girl.get_pic("profile", naked_filter=True, soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

     play sound s_laugh

     you "Thanks for your time, you know we could go back to my room upstairs..."

     if girl.love < 30:

         girl.char "Sorry, but i'll have to help [girl.name]. Some of the girls might come in later and it's good to have someone tending the bar."

         girl.char "Besides, it's quite fun."

         "You talk with her for a bit more, then finish your drinks and go out of the Tavern."

         $ girl.change_stat("obedience", -3)
         $ girl.change_stat("love", -4)

         scene black with fade
         jump main


     else:
         girl.char "I have an even better idea, come with me!"

         you "She takes you to a secluded area in the tavern, you can still hear the other girls talking, but the music is quite cloud, no one will notice you're here."


         "While you're looking around, she gives you a kiss."


         $ pic = girl.get_pic("mc", and_tags=["kiss", "public", "tavern"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She pushes her body onto you and you grab her and start taking her clothes off."


         $ pic = girl.get_pic("mc", and_tags=["kiss", "public", "fondle", "grope", "tavern"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


         girl.char "[girl.name] is fun and having our own Guild is nice, it means we can drink whenever we want, but it gets a bit boring. I'm glad you came in."


         you "Me too, i came for a drink, but will leave with a lot more, it seems."


         play sound s_laugh


         $ pic = girl.get_pic("mc", and_tags=["kiss", "public", "fondle", "grope", "strip", "naked", "tavern"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She gets on her knees and looks at you."

         girl.char "I hope you're ready!"

         $ pic = girl.get_pic("mc", and_tags=["service", "public", "tavern"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "She takes out your cock and plays with it."

         you "Suck it, [girl.name]."


         $ pic = girl.get_pic("mc", and_tags=["service", "oral", "public", "tavern"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "You hope nobody sees you while you're enjoying her blowjob."


         "You keep looking around to see if anyone is watching."

         $ pic = girl.get_pic("mc", and_tags=["service", "deep", "public", "tavern"], naked_filter=True, soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

         "A few more girls showed up, they must have finished their shift at the Hotel."

         "They're making so much noise and the loud music means no one can hear you."

         you "That's enough babe, i want to fuck you."

         if girl.love < 50:

             girl.char "Sorry, [MC.name]. I need to be back to [girl.name] soon. It's getting busier."

             "She keeps sucking it harder and you seen feel like you're about to cum."


             menu:

               "In her mouth":

                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "in-mouth", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She drinks it all with a happy look on her face."

                 you "Now that's what i call service."

                 girl.char "Thank you! Need to go back now!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 "She fixes her clothes and goes back to the bar."






               "On her face":

                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "on-face", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my face!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."



               "On her body":


                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "on-body", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"
                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "tavern"], soft=True)
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


             $ pic = girl.get_pic("mc", and_tags=["sex", "doggy", "public", "tavern"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "You hope nobody sees you while you grab her from behind and thrust your dick in her."


             "You keep looking around to see if anyone is watching."

             $ pic = girl.get_pic("mc", and_tags=["doggy", "public", "tavern"], soft=True)
             show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

             "A few more girls showed up, they must have finished their shift at the Hotel."

             "They're making so much noise and the loud music means no one can hear you."



             play sound s_moans


             you "You have to keep quiet, otherwise people will notice!"


             menu:

               "In her mouth":

                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "in-mouth", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She drinks it all with a happy look on her face."

                 you "Now that's what i call service."

                 girl.char "Thank you! Need to go back now!"

                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                 "She fixes her clothes and goes back to the bar."




               "On her face":

                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "on-face", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my face!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice!"

                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She moves fast and walks to the restrooms to clean up."



               "On her body":


                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "on-body", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



                 girl.char "Not on my clothes!"

                 you "Sorry, i couldn't hold it."

                 girl.char "I'll have to go wash up, before any of the other girls notice! This will probably leave a stain!"

                 "She moves fast and walks to the restrooms to clean up."





               "Inside":

                 $ pic = girl.get_pic("mc", and_tags=["public", "cumshot", "on-body", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "You came deep inside her, her legs are shaking and the cum started to drip out."


                 girl.char "Oh wow, that's a lot!"


                 $ pic = girl.get_pic("mc", and_tags=["aftersex", "embarassed", "sensitivity", "tavern"], soft=True)
                 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                 "She picks up her clothes and goes to the restroom."

                 "You go back to finish your drink and you leave after."





             $ MC.change_prestige(1)
             $ girl.change_stat("obedience", +6)
             $ girl.change_stat("fear", -7)
             $ girl.change_stat("love", +5)
             scene black with fade
             jump main

label office_girl_date:

 $ date_girl = girl

 "You take her back to your office, you passed by a few girls on the way who asked for help, but you told them you were busy today."




 girl.char "[MC.name], this office is amazing, i always loved the view."

 you "Glad you like it. I'm happy i bought this building."

 $ pic = girl.get_pic("profile", soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 "[girl.name], have you ever sat at my desk? Haha, why don't you give it a go and see how it feels?"

 "She goes around and sits on the chair."

 girl.char "Wow, i feel important! What else do you do here besides looking at missions and trying to help the region?"


 you "I'm glad you asked! How about you come closer and i'll show you?"

 play sound s_laugh

 girl.char "What would you want me to do?"

 $ pic = girl.get_pic("mc", and_tags=["kiss", "fondle", "grope"], not_tags=["public", "wet"], soft=True)
 show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

 play sound s_laugh
 girl.char "That feels amazing. Keep going."

 "You try to push her on her knees. She suddenly looks at you."

 girl.char "I see, is that what you want?"

 if girl.love < 20:

     girl.char "I would have to pass, came to see the office, but i'm not feeling great tonight, how about we postpone?"

     you "Ah, well some other time then..."

     "You were really hoping to get something out of her tonight, but it doesn't look like it will happen."

     girl.char "I'll go back to the hotel, see you in the morning!"

     $ MC.change_prestige(50)
     $ girl.change_fear(+7)
     $ girl.change_obediencer(-8)

     hide screen show_event

     scene black with fade
     jump main



 else:

     girl.char "All you had to do was ask. I've been waiting for this."

     you "You're the best, [girl.name]"

     play sound s_laugh

     "She takes out your cock and starts sucking it."


     $ pic = girl.get_pic("mc", and_tags=["service"], not_tags=["public"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     girl.char "You haven't seen anything yet!"

     "You keep watching her while she sucks your cock, she seems to be concentrating on pleasing you more than actually talking."


     $ pic = girl.get_pic("mc", and_tags=["oral"], not_tags=["public"], soft=True)
     show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

     you "That feels great, [girl.name]. Someone looking to get a promotion."

     girl.char "I think you could use a secretary, i would fit that job."


     if girl.love >= 50:

              "She stands up and pushes you on the desk."



              $ pic = girl.get_pic("mc", and_tags=["sex", "cowgirl"], not_tags=["public"], soft=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)


              girl.char "I think you would find me very helpful."

              "You keep fucking her for a while and tell her to bend over your desk."


              $ pic = girl.get_pic("mc", and_tags=["sex", "doggy"], not_tags=["cumshot", "public"], soft=True)
              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

              you "Just like that babe."

              girl.char "That feels great [MC.name]. You can have me any way you want!"

              play sound s_mmmh
              label office_girl2_date:



              "Choose position."


              menu:

                 "Doggy":
                  $ pic2 = girl.get_pic("mc", and_tags=["sex", "doggy"], not_tags=["public"], soft=True)
                  show screen show_event(pic2, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "You keep going for a bit more and you feel like you're going to cum soon."


                  jump office_girl2_date







                 "Cowgirl":

                  $ pic3 = girl.get_pic("mc", and_tags=["sex", "cowgirl"], not_tags=["public"], soft=True)
                  show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "She gets on top of you again and rides you hard while moaning."
                  jump office_girl2_date






                 "Spooning":

                  $ pic = girl.get_pic3("mc", and_tags=["sex", "spooning"], not_tags=["public"], soft=True)
                  show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "You keep fucking her harder."
                  jump office_girl2_date





                 "Piledriver":

                  $ pic = girl.get_pic3("mc", and_tags=["sex", "piledriver"], not_tags=["public"], soft=True)
                  show screen show_event(pic3, x=config.screen_width, y=int(config.screen_height*0.8), bg=None)

                  "You push her down and start fucking her again."
                  jump office_girl2_date


                 "Finish":


                     menu:
                         "In her mouth":
                            "You take it out and push it in her mouth."
                            $ pic = girl.get_pic("mc", and_tags=["cumshot", "in-mouth"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "Tastes so nice."

                            "You spray it in her mouth and she drinks it all with a smile."

                            $ pic = girl.get_pic("mc", and_tags=["cumshot", "in-mouth"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "That was great! Keep me in mind when you do offer a secretary position."

                            $ pic = girl.get_pic("mc", and_tags=["aftersex", "cumshot"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            if not pic:

                                $ pic = girl.get_pic("mc", and_tags=["aftersex"], not_tags=["public"], soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            play sound s_laugh

                            you "Will do, you would make an excellent employee, how about we go back to my room?"

                            girl.char "I could use some rest."
                            $ MC.change_prestige(+20)
                            $ girl.change_stat("obedience", +9)
                            $ girl.change_stat("fear", -4)
                            $ girl.change_stat("love", +4)


                            scene black with fade
                            jump main

                         "On her face":
                            "You stop fucking her and get your dick close to her face."

                            $ pic = girl.get_pic("mc", and_tags=["cumshot", "on-face"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "Yes, on my face!"

                            "You spray it on her face and she takes it all with a smile."

                            $ pic = girl.get_pic("mc", and_tags=["aftersex", "cumshot"], not_tags=["public"], soft=True)
                            show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            if not pic:

                                $ pic = girl.get_pic("mc", and_tags=["aftersex"], not_tags=["public"], soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                            girl.char "That was great! Keep me in mind when you do offer a secretary position."
                            $ MC.change_prestige(20)
                            $ girl.change_stat("obedience", +8)
                            $ girl.change_stat("fear", -4)
                            $ girl.change_stat("love", +2)



                            scene black with fade
                            jump main
                         "On her body":
                          $ pic = girl.get_pic("mc", and_tags=["cumshot", "on-body"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))
                          girl.char "Yes, i want it all, cum all over me!"
                          "You cum all over her. While she laughs."

                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "cumshot"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          if not pic:
                              $ pic = girl.get_pic("mc", and_tags=["aftersex"], not_tags=["public"], soft=True)
                              show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          $ MC.change_prestige(20)
                          $ girl.change_stat("obedience", +2)
                          $ girl.change_stat("fear", -1)
                          $ girl.change_stat("love", +4)



                          scene black with fade
                          jump main

                          girl.char "That was great! Keep me in mind when you do offer a secretary position."
                          you "I will, you can stick around and come sleep in my bedroom if you want?"
                          girl.char "Of course!"
                          $ MC.change_prestige(+20)
                          $ girl.change_stat("obedience", +2)
                          $ girl.change_stat("fear", -1)
                          $ girl.change_stat("love", +3)

                          scene black with fade
                          jump main



                         "Inside her":

                          "You start fucking her harder and faster."

                          $ pic = girl.get_pic("mc", and_tags=["cumshot", "inside"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))

                          girl.char "It's inside me, it feels so good!"

                          "You cum deep inside her and you take your cock out to admire your work!"

                          $ pic = girl.get_pic("mc", and_tags=["aftersex", "inside"], not_tags=["public"], soft=True)
                          show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                          if not pic:

                                $ pic = girl.get_pic("mc", and_tags=["aftersex"], not_tags=["public"], soft=True)
                                show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))


                          girl.char "That was great! Keep me in mind when you do offer a secretary position."


                          you "I will, you can stick around and come sleep in my bedroom if you want?"

                          girl.char "Of course!"
                          $ MC.change_prestige(+20)
                          $ girl.change_stat("obedience", +6)
                          $ girl.change_stat("fear", -5)
                          $ girl.change_stat("love", +6)

                          scene black with fade
                          jump main




     else:


         "She keeps going faster and you are about to cum. You try and focus on the work and let her deal with it under the desk."


         $ pic = girl.get_pic("mc", and_tags=["service", "cumshot"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Oh wow, [MC.name]! It's all over me, hahaha."


         you "That felt great, you're amazing!"

         you "You can stick around and come sleep in my bedroom if you want?"



         $ pic = girl.get_pic("mc", and_tags=["aftersex", "naked"], soft=True)
         show screen show_event(pic, x=config.screen_width, y=int(config.screen_height*0.8))



         girl.char "Thank you, i will!"





         play sound s_laugh

         $ MC.change_prestige(20)
         $ girl.change_stat("obedience", +3)
         $ girl.change_stat("fear", -7)
         $ girl.change_stat("love", +6)

         scene black with fade
         jump main
