############ HEADHUNTER VARIABLES ############
init -2:

    define headhunter = Character("Booty Hunter", color=c_firered, image = "headhunter", font ="CHOWFUN_0.TTF",  size=22, window_left_padding=160)

    $ game_image_dict["Characters"]["headhunter"] = [
                                            declare('headhunter', 'NPC/Headhunter/Headhunter.webp', 'f', x=0.7, y=0.7),
                                            declare('headhunter strip1', 'NPC/Headhunter/Headhunter2.webp', 'f', x=0.7, y=0.7),
                                            declare('headhunter strip2', 'NPC/Headhunter/Headhunter3.webp', 'f', x=0.7, y=0.7),
                                            declare('headhunter angry', 'NPC/Headhunter/Headhunter4.webp', 'f', x=0.7, y=0.7),
                                            declare('side headhunter', 'NPC/Headhunter/Headhunter_portrait.webp', 'p', x=152, y=152, gallery=False),
                                            declare('side headhunter strip1', 'NPC/Headhunter/Headhunter_portrait2.webp', 'p', x=152, y=152, gallery=False),
                                            declare('side headhunter strip2', 'NPC/Headhunter/Headhunter_portrait3.webp', 'p', x=152, y=152, gallery=False),
                                            declare('side headhunter angry', 'NPC/Headhunter/Headhunter_portrait4.webp', 'p', x=152, y=152, gallery=False),
                                            ]

    $ game_image_dict["Backgrounds"]["slavemarket"] += [declare("bg slave market21", "backgrounds/slave market21.webp", "p")]

    $ s_erm = "erm.mp3"
    $ s_hmmm = "uhm.ogg"
    $ s_hmm = "uhm.ogg"
    $ s_ahh_frustrated = "ahh_frustrated.ogg"
    $ s_giggle = "giggle.mp3"
    $ s_mm_mmh = "mm_mmh.ogg"
    
    
init -1 python:

    headhunter_mod_template = Mod(
        
                ## Basic mod information
                name = "Headhunter Mod",
                folder = "Headhunter",
                creator = "Jman",
                version = 0.3196,
                pic = "Headhunter_portrait2.webp",
                description = """Adds the Headhunter from my Bonanza mod to the game. \nShe hunts booty for you. \n
{b}Activation{/b}: go to the Help Menu (the "?"
in the upper right corner), click "Mods" and 
then "[[Headhunter Mod] Activate".""",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("Activate", "headhunter_mod_init"), ("Deactivate","headhunter_mod_revert")],
                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "headhunter_mod_init"
    )
    
    def headhunter_scaling():
        if game.headhunter_debug_enabled:
            return 25
        try:
            money_paid = game.headhunter_money_paid
        except:
            game.headhunter_money_paid = 0
            money_paid = game.headhunter_money_paid
        try:
            girls_bought = game.headhunter_girls_bought
        except:
            game.headhunter_girls_bought = 0
            girls_bought = game.headhunter_girls_bought
        money_scaling_list = [250, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7500, 9000, 11000, 13000, 15000, 17500, 20000, 23000, 26000, 30000, 35000, 40000, 45000, 50000]
        money_scale = 0
        for x in xrange(len(money_scaling_list)):
            if money_paid > sum(money_scaling_list[0:len(money_scaling_list)-x]):
                money_scale = len(money_scaling_list) - x
                break
        return min(money_scale, girls_bought)
        
    def headhunter_scaling_stats():
        hh_scale = headhunter_scaling()
        if hh_scale >= 22:
            return 8
        elif hh_scale >= 19:
            return 7
        elif hh_scale >= 16:
            return 6
        elif hh_scale >= 13:
            return 5
        elif hh_scale >= 10:
            return 4
        elif hh_scale >= 7:
            return 3
        elif hh_scale >= 4:
            return 2
        else:
            return 1

    def headhunter_scaling_pos_traits():
        hh_scale = headhunter_scaling()
        if hh_scale >= 24:
            return 5
        elif hh_scale >= 18:
            return 4
        elif hh_scale >= 12:
            return 3
        elif hh_scale >= 6:
            return 2
        elif hh_scale >= 1:
            return 1
        else:
            return 0

    def headhunter_scaling_neg_traits():
        hh_scale = headhunter_scaling()
        if hh_scale >= 14:
            return 3
        elif hh_scale >= 9:
            return 2
        elif hh_scale >= 0:
            return 1
        else:
            return 1

    def capitalize_allcaps(s):
        split_s = s.split()
        ans = ""
        for str in split_s:
            ans += " " + str.capitalize()
        return ans[1:]
        
    def string_to_list_version(string, string_list):
        if string in string_list:
            return string
        string_ununderscored = string.replace('_',' ')
        if string_ununderscored in string_list:
            return string_ununderscored
        string_capitalized = string.capitalize()
        if string_capitalized in string_list:
            return string_capitalized
        string_lowercase = string.lower()
        if string_lowercase in string_list:
            return string_lowercase
        string_title = string.title()
        if string_title in string_list:
            return string_title
        string_ununderscored_capitalized = string_ununderscored.capitalize()
        if string_ununderscored_capitalized in string_list:
            return string_ununderscored_capitalized
        string_ununderscored_title = string_ununderscored.title()
        if string_ununderscored_title in string_list:
            return string_ununderscored_title
        string_ununderscored_lowercase = string_ununderscored.lower()
        if string_ununderscored_lowercase in string_list:
            return string_ununderscored_lowercase
        for string2 in string_list:
            if string2.startswith(string) or string2.startswith(string_ununderscored) or string2.startswith(string_capitalized) or string2.startswith(string_lowercase) or string2.startswith(string_title)  or string2.startswith(string_ununderscored_capitalized) or string2.startswith(string_ununderscored_title) or string2.startswith(string_ununderscored_lowercase):
                return string2
        for string2 in string_list:
            if string.startswith(string2) or string_ununderscored.startswith(string2) or string_capitalized.startswith(string2) or string_lowercase.startswith(string2) or string_title.startswith(string2) or string_ununderscored_capitalized.startswith(string2) or string_ununderscored_title.startswith(string2) or string_ununderscored_lowercase.startswith(string2):
                return string2
        return ""

    def get_real_girlpath(path):
        if not isinstance(path, basestring):
            return ""
        ret_path = path
        if "/" in path:
            ret_path = path.split("/")[-1]
            if len(ret_path) < 1:
                ret_path = path.split("/")[-2]
        return GirlFilesDict.get_path_dict()[ret_path]

    def get_active_mix_paths():
        ret = []
        for mix in game.mixes:
            for girl in persistent.girl_mix[mix]:
                ret.append(get_real_girlpath(girl))
        return ret

    def get_active_mix_girls():
        ret = []
        for mix in game.mixes:
            for girl in persistent.girl_mix[mix]:
                ret.append(girl)
        return ret

    def compare_girl_paths(path1,path2):
        if path1 == path2 or "girls/" + path1 == path2 or path1 == "girls/" + path2:
            return True
        return False
        
    def get_girls_hh(nb, free=False, p_traits=None, n_trait=None, perks=None, level_range=None, prefer_original = None, init_dict = None, path = None, g_rank = -1): # This will return a list of new girls, if possible using different templates and checking for duplicates

        # If level_range is provided as a tuple of integers (min, max), girls will generate at a random level in range
        # Never set level range below 1 or above 25 to avoid problems

        # prefer_original prioritizes the creation of original girls. They will take the top spots in glist. The game will fall back to non-original if necessary

        if prefer_original is None:
            prefer_original=prefer_original_girls

        if g_rank < 0:
            g_rank = district.rank

        t1 = time.perf_counter()

        if p_traits == None: p_traits = []
        if perks == None: perks = []

        template_girls = [g for g in generate_girls() if can_generate(g, free)] # Must be separate from available_templates to avoid creating new girl objects with every loop

        if len(template_girls) < 1:
            template_girls = [g for g in generate_girls()]

        t2 = time.perf_counter()

        available_templates = []
        glist = []
        final_list = []
        
        while len(glist) < nb:
            if available_templates == []:
                available_templates = list(template_girls) # list() is necessary to make a true copy of template_girls
                random.shuffle(available_templates) # places girl templates in random order

            # Look at fixed path girls first

            if path:
                for girl in available_templates:
                    if girl not in glist and compare_girl_paths(get_real_girlpath(girl.path),get_real_girlpath(path)):
                        if not girl.init_dict["cloning options/unique"] or girl.count_occurences("all") == 0:
                            glist.append(girl)
                            available_templates.remove(girl)
                            break
            
            # First looks for girls that haven't been generated at all
            
            if nb == 1 and len(glist) == 1:
#                renpy.say("","Got just one girl in glist: " + glist[0].path)
                if (init_dict and not init_dict["cloning options/unique"]) or glist[0].count_occurences("all", original=True) == 0:
#                    renpy.say("","Proceeding with " + glist[0].path)
                    break
                else:
#                    renpy.say("","Too many originals: " + str(glist[0].count_occurences("all", original=True)))
                    glist.remove(glist[0])

#            renpy.say("","Finding more girls.")

            for girl in available_templates:
                if girl not in glist and girl.count_occurences("all") == 0:
                    glist.append(girl)
                    available_templates.remove(girl) # removing within the for loop is okay because of 'break'
                    if girl.init_dict["cloning options/unique"]: # Removes unique girls from the template pool if they are unique
                        template_girls.remove(girl)
                    break
            else: # 'for' loop failed
                # Next looks for girls that aren't owned by player and have less than 3 occurences elsewhere
                
                available_templates = [g for g in available_templates if not g.init_dict["cloning options/unique"]] # This clears unique girls from the list (shouldn't be needed)

                if init_dict and init_dict["cloning options/unique"]:
                    available_templates2 = [g for g in available_templates if g.count_occurences("all", original=True) == 0] # This clears existing originals
                    if available_templates2:
                        available_templates = list(available_templates2)
                    else:
                        init_dict["cloning options/unique"] = False

                if not available_templates:
                    raise AssertionError("Not enough girl templates available - Check your girlpack configuration (all set to 'unique'?)")

                for girl in available_templates:
                    if girl not in glist and girl.count_occurences("player") == 0 and girl.count_occurences("all") <= 3:
                        glist.append(girl)
                        available_templates.remove(girl) # removing within the for loop is okay because of 'break'
                        break
                
                # Finally, looks for girls with the least occurrences anywhere
                
                else:
                    if not available_templates:
                        raise AssertionError("Not enough girl templates available - Check your girlpack configuration")

                    found = False
                    i = 1
                    while not found:
                        i += 1
                        
                        if i > 250:
                            raise AssertionError("Error chasing duplicates - Possible infinite loop detected")
                        
                        for girl in available_templates:
                            if girl.count_occurences("all") < i:
                                glist.append(girl)
                                available_templates.remove(girl) # removing within the for loop is okay because of 'break'
                                found = True
                                break

        t3 = time.perf_counter()

        for template in glist:
            girl = copy.deepcopy(template)
            girl.id = game.girl_id_generated
            game.girl_id_generated += 1

            if level_range:
                lvl = random.randint(level_range[0], level_range[1])

            if nb==1 and init_dict:
                girl.init_dict = copy.deepcopy(init_dict)
                if not compare_girl_paths(get_real_girlpath(girl.init_dict["path"]),get_real_girlpath(girl.path)):
                    girl2 = copy.deepcopy(girl)
                    girl2.load_ini()
                    try:
                        girl.init_dict["background story/origin"] = girl2.init_dict["background story/origin"]
                    except:
                        girl.init_dict["background story/origin"] = None
                    try:
                        girl.init_dict["background story/origin_description"] = girl2.init_dict["background story/origin_description"]
                    except:
                        girl.init_dict["background story/origin_description"] = None
                    try:
                        girl.init_dict["background story/init_function"] = girl2.init_dict["background story/init_function"]
                    except:
                        girl.init_dict["background story/init_function"] = None
                    try:
                        girl.init_dict["background story/city_label"] = girl2.init_dict["background story/city_label"]
                    except:
                        girl.init_dict["background story/city_label"] = None
                    try:
                        girl.init_dict["background story/story_label"] = girl2.init_dict["background story/story_label"]
                    except:
                        girl.init_dict["background story/story_label"] = None
                    try:
                        girl.init_dict["background story/night_label"] = girl2.init_dict["background story/night_label"]
                    except:
                        girl.init_dict["background story/night_label"] = None
                    try:
                        girl.init_dict["background story/interact_prompt"] = girl2.init_dict["background story/interact_prompt"]
                    except:
                        girl.init_dict["background story/interact_prompt"] = None

                try:
                    globals()[girl.init_dict["background story/init_function"]]
                except:
                    girl.init_dict["background story/init_function"] = None
                lvl= random.randint(min(max(1,g_rank * 5-4),25),min(max(1,g_rank * 5),25))
            else: # Will pick a randomized level based on chapter
                lvl = randomize_girl_level()

            # <Chris12 - prefer_original>
            girl.randomize(free=free, p_traits=p_traits, n_trait=n_trait, perks=perks, level=lvl, force_original=(prefer_original and girl.count_occurences("all", original=True, add_list=final_list) == 0), temp_list=final_list) # final_list is checked to avoid multiple original generation
            # </Chris12 - prefer_original>

#            # Trait King: Slavemarket & free girl additional traits
#            if dice(4) <= 1 and not free and len(girl.get_traits()) < 6 and not girl.fullname == "Sill Plain": # Trait King: Girls with hidden traits
#                girl.add_trait(hidden_trait2)
#            
            if free:
                trait_list = copy.copy(girl.traits)
                for trait in trait_list:
                    if trait.name == "Jaded":
                        girl.remove_trait(trait)
                        girl.add_trait(expensive_trait, forced=True, no_perks=True)
#                        girl.add_trait(weighted_choice([(trait_dict["Virgin"],10), (trait_dict["Housebroken"],5), (trait_dict["Teacher's pet"],0), (trait_dict["Farmgirl"],10), (trait_dict["Deflowered"],40), (trait_dict["Broken in"],10), (trait_dict["Experienced"],10), (trait_dict["Trauma"],10)]))
#                girl.add_effects([Effect("boost", "tip", 0.1, scales_with = "rank")], source = "freedom")
            else:
                trait_list = copy.copy(girl.traits)
                for trait in trait_list:
                    if trait.name in ("Recently kidnapped", "Slave Brand"):
                        girl.remove_trait(trait)

            final_list.append(girl)

            if girl.init_dict["background story/init_function"]:
#                renpy.say("", "Found " + girl.init_dict["background story/init_function"])
                try:
                    globals()[girl.init_dict["background story/init_function"]](girl)
                except:
                    raise AssertionError("Function " + girl.init_dict["background story/init_function"] + " in " + get_real_girlpath(girl.path) + "/_BK.ini doesn't exist or failed.")

            if len(final_list)>= nb:
                break

        t4 = time.perf_counter()

        try:
            game.func_time_log += "\nHH gen total time: %s" % (t4 - t1)
        except:
            pass

        return final_list

## This label runs when the mod is activated
label headhunter_mod_init():
    "The Headhunter is on the prowl!"

    transform centerhigh:
        xalign 0.5
        yalign 0.25

    transform centerhighleft:
        xalign 0.05
        yalign 0.25

    transform centerhighright:
        xalign 0.95
        yalign 0.25

    python:
    
        slavemarket_firstvisit2 = True
        slavemarket_firstvisit3 = True
        game.interacting_with_headhunter = 0
        game.headhunter_button_enabled = 1
        game.headhunter_time = 0
        game.headhunter_price = 0
        game.headhunter_girl = None
        game.headhunter_free = 0
        game.advertised_girl = None
        game.headhunter_discount = 50
        game.headhunter_discount_percent = 50
        game.headhunter_last_scaling = 0
        game.headhunter_money_paid = 0
        game.headhunter_girls_bought = 0
        game.headhunter_debug_enabled = False

    return

label headhunter_mod_revert:

    "Arrr! You meanie!"

    return
    
label headhunter_main:

    jump headhunter
    
    return

jump headhunter_end2

label headhunter():

    $ headhunted_name = "Nobody specific"
    $ headhunted_original = 0
    $ headhunted_free = game.headhunter_free
    $ headhunted_rank = district.rank
    $ headhunted_beauty = 0
    $ headhunted_body = 0
    $ headhunted_charm = 0
    $ headhunted_refinement = 0
    $ headhunted_libido = 0
    $ headhunted_obedience = 0
    $ headhunted_constitution = 0
    $ headhunted_sensitivity = 0
    $ headhunted_service = 0
    $ headhunted_sex = 0
    $ headhunted_anal = 0
    $ headhunted_fetish = 0
#    $ headhunted_virginity_trait = "Random"
    $ headhunted_pos_trait1 = None
    $ headhunted_pos_trait2 = None
    $ headhunted_pos_trait3 = None
    $ headhunted_pos_trait4 = None
    $ headhunted_pos_trait5 = None
    $ headhunted_pos_traits = []
    $ headhunted_neg_trait1 = None
    $ headhunted_neg_trait2 = None
    $ headhunted_neg_trait3 = None
    $ headhunted_neg_traits = []
    $ headhunted_personality = "random"
    $ headhunted_favorite_act1 = "None"
    $ headhunted_favorite_act2 = "None"
    $ headhunted_favorite_acts = []
    $ headhunted_disliked_act1 = "None"
    $ headhunted_disliked_act2 = "None"
    $ headhunted_disliked_acts = []
    $ headhunted_favorite_fixation1 = "None"
    $ headhunted_favorite_fixation2 = "None"
    $ headhunted_favorite_fixations = []
    $ headhunted_disliked_fixation1 = "None"
    $ headhunted_disliked_fixation2 = "None"
    $ headhunted_disliked_fixations = []
    $ headhunted_sexual_experience = 0
    $ headhunted_farm_weakness = "random"

    $ headhunter_specified_traits = 0
    $ headhunter_specified_pos_traits = 0
    $ headhunter_specified_neg_traits = 0
    $ headhunter_specified_stats = 0
    $ headhunter_gold_traits = 0
    $ express_default = "no express."

    $ headhunter_modifier = 1.0
    $ game.headhunter_button_enabled = 0
    $ game.interacting_with_headhunter = 1
    $ selected_girl = None
    $ slavemarket_bg = rand_choice(["bg slave market11", "bg slave market11", "bg slave market21"])

    hide screen girls
    show expression slavemarket_bg with fade

    show headhunter at centerhigh with dissolve

    $ hh_scale = headhunter_scaling()
    python:
        try:
            new_stuff = game.headhunter_last_scaling < hh_scale
        except:
            game.headhunter_last_scaling = 0
            new_stuff = game.headhunter_last_scaling < hh_scale

    if new_stuff:
        play sound s_scream

        headhunter "Ahoy there..."

        play sound s_hmmm

        extend " Hey, wait..."

        if hh_scale >= 25:

            play sound s_evil_laugh

            headhunter "Yer our v'ry best cust'mer now! That calls fer a toast!" 

            play sound s_aaha

            show headhunter strip1 at centerhigh with dissolve

            extend "\n\nLet's raise a glass an' strike a barg'n - from now on, ye get the pick o' the plunder." 

            play sound s_mm_mmh

            show headhunter strip2 at centerhigh with dissolve

            extend "\nJest tell me what booty yer heart desires an' I'll find it fer ye!" 

        elif hh_scale >= 20:

            play sound s_evil_laugh

            headhunter "Ye be one o' arrs best cust'mers!" 

            play sound s_aaha

            show headhunter strip1 at centerhigh with dissolve

            extend " What be the fine booty ye seek?" 

            play sound s_mm_mmh

            show headhunter strip2 at centerhigh with dissolve

            extend "\n\nJest say the word an' it be done." 

        elif hh_scale >= 15:

            play sound s_evil_laugh

            headhunter "[MC.name], ye be a real reg'lr custom'r now!" 

            play sound s_aaha

            show headhunter strip1 at centerhigh with dissolve

            extend " What rare plunder are ye aft'r this fine day?" 

            play sound s_mm_mmh

            show headhunter strip2 at centerhigh with dissolve

            extend "\n\nWe's do ours best for ye, arrr!" 

        elif hh_scale >= 10:

            play sound s_evil_laugh

            headhunter "Arrr, [MC.name], ye again!" 

            play sound s_aaha

            show headhunter strip1 at centerhigh with dissolve

            extend " What spec'l bounty are ye aft'r this day?" 

            play sound s_mm_mmh

            show headhunter strip2 at centerhigh with dissolve

            extend "\n\nJest lemme know yer needs an' we'll see what we can do." 

        elif hh_scale >= 6:

            play sound s_evil_laugh

            headhunter "Yer a regular cust'mer now, ain't ye?" 

            play sound s_aaha

            show headhunter strip1 at centerhigh with dissolve

            extend "\n\nWe be offerin' spec'l serv'ces to people such as yerself!" 

        elif hh_scale >= 3:

            play sound s_evil_laugh

            headhunter "Ye be lookin' to add to yer collection, eh?" 

            play sound s_aaha

            show headhunter strip1 at centerhigh with dissolve

            extend "\n\nWe's can cert'nly hook ye up with sum rare finds if ye keep comin' back and buyin' ours serv'ces." 

        elif hh_scale >= 1:

            play sound s_evil_laugh

            headhunter "I thunk I've seen yer face 'round these parts befarr!" 

            play sound s_hmm

            extend "\n\nYe look like th' kind who'd apprec'te sum rare an' val'ble goods. Keep buyin' and we'll work somethin' out." 

        while game.headhunter_last_scaling < hh_scale:
            $ game.headhunter_last_scaling += 1
            play sound s_spell
            if game.headhunter_last_scaling == 1:
                headhunter "{b}[[New choice o'booty{/b}: positive trait]" 
            elif game.headhunter_last_scaling == 2:
                headhunter "{b}[[New choice o'booty{/b}: phobia]" 
            elif game.headhunter_last_scaling == 3:
                headhunter "{b}[[New choice o'booty{/b}: fetish]" 
            elif game.headhunter_last_scaling == 4:
                headhunter "{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 5:
                headhunter "{b}[[New choice o'booty{/b}: free girls available to be scouted!]" 
            elif game.headhunter_last_scaling == 6:
                headhunter "{b}[[New choice o'booty{/b}: positive traits +1]" 
            elif game.headhunter_last_scaling == 7:
                headhunter "{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 8:
                headhunter "{b}[[New choice o'booty{/b}: express delivery!]" 
            elif game.headhunter_last_scaling == 9:
                headhunter "{b}[[New choice o'booty{/b}: negative traits +1]" 
            elif game.headhunter_last_scaling == 10:
                headhunter "{b}[[New choice o'booty{/b}: personality!]\n\n{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 11:
                headhunter "{b}[[New choice o'booty{/b}: previous sexual experience!]" 
            elif game.headhunter_last_scaling == 12:
                headhunter "{b}[[New choice o'booty{/b}: positive traits +1]" 
            elif game.headhunter_last_scaling == 13:
                headhunter "{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 14:
                headhunter "{b}[[New choice o'booty{/b}: negative traits +1]" 
            elif game.headhunter_last_scaling == 15:
                headhunter "{b}[[New choice o'booty{/b}: slave ranks!]" 
            elif game.headhunter_last_scaling == 16:
                headhunter "{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 17:
                headhunter "{b}[[New choice o'booty{/b}: fetish +1]" 
            elif game.headhunter_last_scaling == 18:
                headhunter "{b}[[New choice o'booty{/b}: positive traits +1]" 
            elif game.headhunter_last_scaling == 19:
                headhunter "{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 20:
                headhunter "{b}[[New choice o'booty{/b}: originals and gold traits!]\n\n{b}[[New choice o'booty{/b}: up to +1 rank above the market!]" 
            elif game.headhunter_last_scaling == 21:
                headhunter "{b}[[New choice o'booty{/b}: farm weakness!]" 
            elif game.headhunter_last_scaling == 22:
                headhunter "{b}[[New choice o'booty{/b}: stat choices +1]" 
            elif game.headhunter_last_scaling == 23:
                headhunter "{b}[[New choice o'booty{/b}: phobia +1]" 
            elif game.headhunter_last_scaling == 24:
                headhunter "{b}[[New choice o'booty{/b}: positive traits +1]" 
            elif game.headhunter_last_scaling == 25:
                headhunter "{b}[[New choice o'booty{/b}: up to two gold traits for originals!]" 


        if hh_scale >= 10:

            play sound s_mmmh

            headhunter "Now that was sum booty, eh!"

            show headhunter strip1 at centerhigh with dissolve

        if hh_scale >= 3:
            play sound s_erm

            headhunter "Arrr, back to bus'ness, Cap'n."

            show headhunter at centerhigh with dissolve

            play sound s_woman_scream

    else:
        play sound s_woman_scream

    menu:
        
        headhunter "Ahoy there, customerrr!"

        "Ahoy.":
                
            you "Ahoy yourself! I need a slavegirl."
        
            play sound s_erm
            headhunter "Arr, let me get a bit more comfy..." 
                
            jump headhunter_premenu

        "Bye.":

            you "Nevermind."
        
            play sound s_sigh
            headhunter "..."
            show headhunter strip1 at centerhigh with dissolve
            play sound s_aaha
            headhunter "You'll be back for more booty, matey!"
            hide headhunter strip1 with dissolve
            $ game.headhunter_button_enabled = 1
            jump headhunter_end
                   
label headhunter_premenu:

            show headhunter strip1 at centerhigh with dissolve

            play sound s_aaha
            headhunter "Ayy, cap'n, tell me about them requirements!" 
        
label headhunter_menu:

            if len([g for g in generate_girls() if can_generate(g,headhunted_free) and g.count_occurences("all", original = True) == 0]) == 0:
                $ no_originals = True
            else:
                $ no_originals = False

            $ deforig = "No"
            $ freedom_default = "enslave."
            if headhunted_rank <= 5:
                if headhunted_rank != int(headhunted_rank):
                    $ rank_default = "try to find rank " + rank_name[int(headhunted_rank)] + "+ girls."
                else:
                    $ rank_default = "try to find rank " + rank_name[int(headhunted_rank)] + " girls."
            else:
                $ rank_default = "try to find rank X+ girls."

            $ menu_item_name = "Name: " + str(headhunted_name)
            $ menu_item_originality = "Originality: " + str(deforig)
            $ menu_item_personality = "Personality: " + str(headhunted_personality.lower())
            $ menu_item_freedom = "Freedom: " + str(freedom_default)
            $ menu_item_rank = "Rank: " + str(rank_default)
            $ menu_item_express = "Express: " + str(express_default)
            $ menu_item_charm = "Charm: " + str(headhunted_charm)
            $ menu_item_body = "Body: " + str(headhunted_body)
            $ menu_item_beauty = "Beauty: " + str(headhunted_beauty)
            $ menu_item_refinement = "Refinement: " + str(headhunted_refinement)
            $ menu_item_sensitivity = "Sensitivity: " + str(headhunted_sensitivity)
            $ menu_item_libido = "Libido: " + str(headhunted_libido)
            $ menu_item_constitution = "Constitution: " + str(headhunted_constitution)
            $ menu_item_obedience = "Obedience: " + str(headhunted_obedience)
#            $ menu_item_virginity_trait = "Virginity: " + str(headhunted_virginity_trait)
            $ menu_item_pos_trait1 = "Positive trait 1: " + str(headhunted_pos_trait1)
            $ menu_item_pos_trait2 = "Positive trait 2: " + str(headhunted_pos_trait2)
            $ menu_item_pos_trait3 = "Positive trait 3: " + str(headhunted_pos_trait3)
            $ menu_item_pos_trait4 = "Positive trait 4: " + str(headhunted_pos_trait4)
            $ menu_item_pos_trait5 = "Positive trait 5: " + str(headhunted_pos_trait5)
            $ menu_item_neg_trait1 = "Negative trait 1: " + str(headhunted_neg_trait1)
            $ menu_item_neg_trait2 = "Negative trait 2: " + str(headhunted_neg_trait2)
            $ menu_item_neg_trait3 = "Negative trait 3: " + str(headhunted_neg_trait3)
            $ menu_item_sex_experience = "Sexual experience: " + str(headhunted_sexual_experience)
            $ menu_item_farm_weakness = "Farm weakness: " + str(headhunted_farm_weakness.lower())
            $ menu_item_pos_fixation1 = "Fetish 1: " + str(headhunted_favorite_fixation1.lower())
            $ menu_item_pos_fixation2 = "Fetish 2: " + str(headhunted_favorite_fixation2.lower())
            $ menu_item_neg_fixation1 = "Phobia 1: " + str(headhunted_disliked_fixation1.lower())
            $ menu_item_neg_fixation2 = "Phobia 2: " + str(headhunted_disliked_fixation2.lower())
            $ menu_item_favourite_act1 = "Favourite act 1: " + str(headhunted_favorite_act1.lower())
            $ menu_item_favourite_act2 = "Favourite act 2: " + str(headhunted_favorite_act2.lower())
            $ menu_item_disliked_act1 = "Disliked act 1: " + str(headhunted_disliked_act1.lower())
            $ menu_item_disliked_act2 = "Disliked act 2: " + str(headhunted_disliked_act2.lower())

            menu:

                "Identity":
                    label headhunter_menu_identity:
                    if headhunted_original == 1:
                        $ deforig = "Yes"
                    else:
                        $ deforig = "No"
                    $ menu_item_originality = "Originality: " + str(deforig)
                    if headhunted_free == 1:
                        $ freedom_default = "leave free."
                    elif headhunted_free == 0:
                        $ freedom_default = "enslave."
                    else:
                        $ freedom_default = "buggy!"
                    if headhunted_rank <= 5:
                        if headhunted_rank != int(headhunted_rank):
                            $ rank_default = "try to find rank " + rank_name[int(headhunted_rank)] + "+ girls."
                        else:
                            $ rank_default = "try to find rank " + rank_name[int(headhunted_rank)] + " girls."
                    else:
                        $ rank_default = "try to find rank X+ girls."
                    $ menu_item_freedom = "Freedom: " + str(freedom_default)
                    $ menu_item_express = "Express: " + str(express_default)
                    if headhunted_rank <= 5:
                        if headhunted_rank != int(headhunted_rank):
                            $ menu_item_rank = "Rank: " + rank_name[int(headhunted_rank)] + "+"
                        else:
                            $ menu_item_rank = "Rank: " + rank_name[int(headhunted_rank)]
                    else:
                        $ menu_item_rank = "Rank: X+"
                    menu hh_menu:
                        "[menu_item_name]":
                            if headhunted_name == "Nobody specific":
                                $ headhunted_name = renpy.input("Do you need a specific girl?", default = "")
                            else:
                                $ headhunted_name = renpy.input("Do you need a specific girl?", default = headhunted_name)
                            $ all_the_real_girls = get_active_mix_girls()
                            $ headhunted_name = string_to_list_version(headhunted_name,all_the_real_girls)
                            if headhunted_name == "":
                                $ headhunted_name = "Nobody specific"
                            $ menu_item_name = "Name: " + str(headhunted_name)
                            jump headhunter_menu_identity
                        "{color=[c_lightgrey]}Originality: they are all gone!{/color}" if no_originals and headhunter_scaling() >= 20: 
                            jump hh_menu
                        "{color=[c_lightgrey]}[menu_item_originality]{/color}" if not no_originals and headhunter_scaling() >= 20 and headhunter_gold_traits >= 1:
                            $ headhunted_original = 1
                            $ deforig = "Yes"
                            jump hh_menu
                        "[menu_item_originality]" if not no_originals and headhunter_scaling() >= 20 and headhunter_gold_traits < 1:
                            if renpy.call_screen("yes_no", "Do you need an original girl? Current: " + deforig):
                                $ headhunted_original = 1
                                $ deforig = "Yes"
                            else:
                                $ headhunted_original = 0
                                $ deforig = "No"
                            $ menu_item_originality = "Originality: " + str(deforig)
                            jump headhunter_menu_identity
                        "[menu_item_personality]" if headhunter_scaling() >= 10:
                            $ pers_temp = "random"
                            if headhunted_personality:
                                $ pers_temp = headhunted_personality
                            if headhunted_personality == "random":
                                $ pers_temp = renpy.input("Choose: sweet, meek, nerd, superficial,\n rebel, cold, pervert, masochist or random. ", default = "").lower()
                            else:
                                $ pers_temp = renpy.input("Choose: sweet, meek, nerd, superficial,\n rebel, cold, pervert, masochist or random. ", default = "").lower()
                            if pers_temp in ("sweet", "swee", "swe", "sw", "swt", "st"):
                                $ pers_temp = "sweet"
                            elif pers_temp in ("meek", "mee", "me", "mk", "mek"):
                                $ pers_temp = "meek"
                            elif pers_temp in ("nerd", "ner", "ne", "n", "nrd", "nd", "ned", "nr"):
                                $ pers_temp = "nerd"
                            elif pers_temp in ("superficial", "superf", "super", "sficial", "sf", "superfic", "superficl", "supfic", "supficial", "supf", "sfic", "sf", "sup", "su"):
                                $ pers_temp = "superficial"
                            elif pers_temp in ("rebel", "rebe", "reb", "re", "r", "rb", "rl", "rbl"):
                                $ pers_temp = "rebel"
                            elif pers_temp in ("cold", "col", "cld", "cod", "cl", "cd", "co", "c"):
                                $ pers_temp = "cold"
                            elif pers_temp in ("pervert", "perver", "perve", "perv", "per", "pe", "p", "pervrt", "prvrt", "pervt", "prvt", "prv", "pvt", "pr", "pv", "pt"):
                                $ pers_temp = "pervert"
                            elif pers_temp in ("masochist", "masochis", "masochi", "masoch", "masoc", "maso", "mas", "ma", "ms", "mt", "mso", "msc", "msoc"):
                                $ pers_temp = "masochist"
                            elif pers_temp in ("random", "rando", "rand", "ran", "ra", "rn", "rd", "rm", "rdm", "rnd", "rndm", "randm"):
                                $ pers_temp = "random"
                            $ pers_temp = string_to_list_version(pers_temp,list(gpersonalities.keys()) + ["random"])
                            if pers_temp in list(gpersonalities.keys()) + ["random"]:
                                $ headhunted_personality = pers_temp
                            if pers_temp == "":
                                $ headhunted_personality = "random"
                            $ menu_item_personality = "Personality: " + str(headhunted_personality.lower())
                            jump headhunter_menu_identity
                        "[menu_item_freedom]" if headhunter_scaling() >= 5:
                            if renpy.call_screen("yes_no", "Do you want us to only find, not enslave her? Currently: " + freedom_default):
                                $ headhunted_free = 1
                                $ freedom_default = "leave free."
                            else:
                                $ headhunted_free = 0
                                $ freedom_default = "enslave."
                            $ menu_item_freedom = "Freedom: " + str(freedom_default)
                            jump headhunter_menu_identity
                        "[menu_item_rank]" if headhunter_scaling() >= 15:
                            $ rank_temp = renpy.input("Look for girls ranked as ", default = "")
                            $ done_already = False
                            python: 
                                try:
                                    rank_temp = int(rank_temp)
                                except ValueError: 
                                    if isinstance(rank_temp, basestring):
                                        if rank_temp in ("x", "X"):
                                            headhunted_rank = 5
                                        elif rank_temp in ("s+", "S+", "4+"):
                                            headhunted_rank = 4.5
                                        elif rank_temp in ("s", "S"):
                                            headhunted_rank = 4
                                        elif rank_temp in ("a+", "A+", "3+"):
                                            headhunted_rank = 3.5
                                        elif rank_temp in ("a", "A"):
                                            headhunted_rank = 3
                                        elif rank_temp in ("b+", "B+", "2+"):
                                            headhunted_rank = 2.5
                                        elif rank_temp in ("b", "B"):
                                            headhunted_rank = 2
                                        elif rank_temp in ("c+", "C+", "1+"):
                                            headhunted_rank = 1.5
                                        elif rank_temp in ("c", "C"):
                                            headhunted_rank = 1
                                        else:
                                            if headhunted_rank:
                                                if isinstance(headhunted_rank, int):
                                                    headhunted_rank = max(1,min(5, headhunted_rank))
                                                else:
                                                    headhunted_rank = district.rank
                                        done_already = True
                                    elif headhunted_rank:
                                        if isinstance(headhunted_rank, int):
                                            headhunted_rank = max(1,min(5, headhunted_rank))
                                        else:
                                            headhunted_rank = district.rank
                                        done_already = True
                                    else:
                                        headhunted_rank = district.rank
                                        done_already = True
                            if not done_already:
                                $ headhunted_rank = max(1,min(5, rank_temp))
                            if headhunted_rank <= 5:
                                if headhunted_rank != int(headhunted_rank):
                                    $ menu_item_rank = "Rank: " + rank_name[int(headhunted_rank)] + "+"
                                else:
                                    $ menu_item_rank = "Rank: " + rank_name[int(headhunted_rank)]
                            else:
                                $ menu_item_rank = "Rank: S+"
                            if headhunted_rank > district.rank + headhunter_scaling()//20:
                                $ headhunted_rank = district.rank + headhunter_scaling()//20
                            jump headhunter_menu_identity
                        "[menu_item_express]" if headhunter_scaling() >= 8:
                            if renpy.call_screen("yes_no", "Do you want to pay a premium to speed up the hunt (costs 50% extra, roughly twice as fast)? Currently: " + express_default):
                                $ express_default = "express."
                            else:
                                $ express_default = "no express."
                            $ menu_item_express = "Express: " + str(express_default)
                            jump headhunter_menu_identity
                        "Back":
                            jump headhunter_menu
                "Stats":
                    label headhunter_menu_stats:
                    $ headhunter_specified_stats = 0
                    if isinstance(headhunted_charm,int) and headhunted_charm > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_body,int) and headhunted_body > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_beauty,int) and headhunted_beauty > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_refinement,int) and headhunted_refinement > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_sensitivity,int) and headhunted_sensitivity > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_libido,int) and headhunted_libido > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_constitution,int) and headhunted_constitution > 0:
                        $ headhunter_specified_stats += 1
                    if isinstance(headhunted_obedience,int) and headhunted_obedience > 0:
                        $ headhunter_specified_stats += 1
                    
                    menu hh_menu_stats:
                        "{color=[c_lightgrey]}[menu_item_charm]{/color}" if headhunted_charm <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_charm]" if headhunted_charm > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Charm rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_charm:
                                        stat_temp = headhunted_charm
                                    else:
                                        stat_temp = 0
                            $ headhunted_charm = max(0,min(5, stat_temp))
                            $ menu_item_charm = "Charm: " + str(headhunted_charm)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_body]{/color}" if headhunted_body <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_body]" if headhunted_body > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Body rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_body:
                                        stat_temp = headhunted_body
                                    else:
                                        stat_temp = 0
                            $ headhunted_body = max(0,min(5, stat_temp))
                            $ menu_item_body = "Body: " + str(headhunted_body)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_beauty]{/color}" if headhunted_beauty <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_beauty]" if headhunted_beauty > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Beauty rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_beauty:
                                        stat_temp = headhunted_beauty
                                    else:
                                        stat_temp = 0
                            $ headhunted_beauty = max(0,min(5, stat_temp))
                            $ menu_item_beauty = "Beauty: " + str(headhunted_beauty)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_refinement]{/color}" if headhunted_refinement <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_refinement]" if headhunted_refinement > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Refinement rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_refinement:
                                        stat_temp = headhunted_refinement
                                    else:
                                        stat_temp = 0
                            $ headhunted_refinement = max(0,min(5, stat_temp))
                            $ menu_item_refinement = "Refinement: " + str(headhunted_refinement)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_sensitivity]{/color}" if headhunted_sensitivity <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_sensitivity]" if headhunted_sensitivity > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Sensitivity rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_sensitivity:
                                        stat_temp = headhunted_sensitivity
                                    else:
                                        stat_temp = 0
                            $ headhunted_sensitivity = max(0,min(5, stat_temp))
                            $ menu_item_sensitivity = "Sensitivity: " + str(headhunted_sensitivity)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_libido]{/color}" if headhunted_libido <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_libido]" if headhunted_libido > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Libido rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_libido:
                                        stat_temp = headhunted_libido
                                    else:
                                        stat_temp = 0
                            $ headhunted_libido = max(0,min(5, stat_temp))
                            $ menu_item_libido = "Libido: " + str(headhunted_libido)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_constitution]{/color}" if headhunted_constitution <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_constitution]" if headhunted_constitution > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Constitution rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_constitution:
                                        stat_temp = headhunted_constitution
                                    else:
                                        stat_temp = 0
                            $ headhunted_constitution = max(0,min(5, stat_temp))
                            $ menu_item_constitution = "Constitution: " + str(headhunted_constitution)
                            jump headhunter_menu_stats

                        "{color=[c_lightgrey]}[menu_item_obedience]{/color}" if headhunted_obedience <= 0 and headhunter_scaling_stats() <= headhunter_specified_stats:
                            jump hh_menu_stats
                        "[menu_item_obedience]" if headhunted_obedience > 0 or headhunter_scaling_stats() > headhunter_specified_stats:
                            $ stat_temp = renpy.input("Obedience rating 0 to 5\n 0 = random:", default = "")
                            python: 
                                try:
                                    stat_temp = int(stat_temp)
                                except ValueError: 
                                    if headhunted_obedience:
                                        stat_temp = headhunted_obedience
                                    else:
                                        stat_temp = 0
                            $ headhunted_obedience = max(0,min(5, stat_temp))
                            $ menu_item_obedience = "Obedience: " + str(headhunted_obedience)
                            jump headhunter_menu_stats

                            jump headhunter_menu_stats

                        "Back":
                            jump headhunter_menu
                "Traits":
                    label headhunter_menu_traits:
                    $ headhunter_gold_traits = 0
                    $ headhunter_specified_traits = 0
                    $ headhunter_specified_pos_traits = 0
                    $ headhunter_specified_neg_traits = 0
#                    if headhunted_virginity_trait in list(trait_dict.keys()):
#                        if trait_dict[headhunted_virginity_trait] in gold_traits:
#                        $ headhunter_specified_traits += 1
#                        $ headhunter_specified_pos_traits = 1
#                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait1 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_pos_traits += 1
                        if trait_dict[headhunted_pos_trait1] in gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait2 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_pos_traits += 1
                        if trait_dict[headhunted_pos_trait2] in gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait3 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_pos_traits += 1
                        if trait_dict[headhunted_pos_trait3] in gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait4 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_pos_traits += 1
                        if trait_dict[headhunted_pos_trait4] in gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_pos_trait5 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_pos_traits += 1
                        if trait_dict[headhunted_pos_trait5] in gold_traits:
                            $ headhunter_gold_traits += 1
                    if headhunted_neg_trait1 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_neg_traits += 1
                    if headhunted_neg_trait2 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_neg_traits += 1
                    if headhunted_neg_trait3 in list(trait_dict.keys()):
                        $ headhunter_specified_traits += 1
                        $ headhunter_specified_neg_traits += 1
                    $ pos_trait_names = [tr.name for tr in pos_traits + gold_traits]
                    $ neg_trait_names = [tr.name for tr in neg_traits]
#                    $ virginity_trait_names = [tr.name for tr in pos_traits_virginity + neg_traits_virginity]
                    menu:
#                        "[menu_item_virginity_trait]":
#                            $ trait_name_temp = "Random"
#                            if headhunted_virginity_trait:
#                                $ trait_name_temp = headhunted_virginity_trait
#                            if trait_name_temp == "Random":
#                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
#                            else:
#                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
#                            if trait_name_temp in list(trait_dict.keys()):
#                                if trait_dict[trait_name_temp] in (pos_traits_virginity + neg_traits_virginity):
#                                    if trait_dict[trait_name_temp] in gold_traits and (headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25)):
#                                        $ headhunted_virginity_trait = "Too many gold traits!"
#                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
#                                        $ headhunted_virginity_trait = "Nice try! Catch her yourself!"
#                                    else:
#                                        $ headhunted_virginity_trait = trait_name_temp
#                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
#                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits_virginity + neg_traits_virginity):
#                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits and (headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25)):
#                                        $ headhunted_virginity_trait = "Too many gold traits!"
#                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
#                                        $ headhunted_virginity_trait = "Nice try! Catch her yourself!"
#                                    else:
#                                        $ headhunted_virginity_trait = trait_name_temp.capitalize()
#                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
#                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits_virginity + neg_traits_virginity):
#                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits and (headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25)):
#                                        $ headhunted_virginity_trait = "Too many gold traits!"
#                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
#                                        $ headhunted_virginity_trait = "Nice try! Catch her yourself!"
#                                    else:
#                                        $ headhunted_virginity_trait = capitalize_allcaps(trait_name_temp)
#                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified", "R", "Rn", "Rd", "Ran", "Rnd", "Rdm", "Rand", "Rndm", "Rando", "Random", "r", "rn", "rd", "ran", "rnd", "rdm", "rand", "rndm", "rando", "random"):
#                                $ headhunted_virginity_trait = "Random"
#                            elif trait_name_temp in ("D", "d", "De", "de", "Def", "def", "Deflo", "deflo", "Deflowered", "deflowered", "Defl", "defl"):
#                                $ headhunted_virginity_trait = "Deflowered"
#                            $ menu_item_virginity_trait = "Virginity: " + str(headhunted_virginity_trait)
#                            jump headhunter_menu_traits
                        "[menu_item_pos_trait1]" if headhunter_scaling_pos_traits() >= 1:
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait1:
                                $ trait_name_temp = headhunted_pos_trait1
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,pos_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait1 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait1 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait1 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait1 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait1 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait1 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait1 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait1 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait1 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait1 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits + gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait1 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait1 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait1 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait1 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait1 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_pos_trait2, headhunted_pos_trait3, headhunted_pos_trait4, headhunted_pos_trait5] if x]:
                                $ headhunted_pos_trait1 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait1 = "Not specified"
                            $ menu_item_pos_trait1 = "Positive trait 1: " + str(headhunted_pos_trait1)
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait2]" if headhunter_scaling_pos_traits() >= 2:
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait2:
                                $ trait_name_temp = headhunted_pos_trait2
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,pos_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait2 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait2 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait2 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait2 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait2 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait2 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait2 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait2 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait2 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait2 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits + gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait2 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait2 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait2 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait2 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait2 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_pos_trait1, headhunted_pos_trait3, headhunted_pos_trait4, headhunted_pos_trait5] if x]:
                                $ headhunted_pos_trait2 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait2 = "Not specified"
                            $ menu_item_pos_trait2 = "Positive trait 2: " + str(headhunted_pos_trait2)
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait3]" if headhunter_scaling_pos_traits() >= 3:
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait3:
                                $ trait_name_temp = headhunted_pos_trait3
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,pos_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait3 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait3 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait3 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait3 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait3 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait3 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait3 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait3 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait3 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait3 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits + gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait3 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait3 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait3 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait3 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait3 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_pos_trait1, headhunted_pos_trait2, headhunted_pos_trait4, headhunted_pos_trait5] if x]:
                                $ headhunted_pos_trait3 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait3 = "Not specified"
                            $ menu_item_pos_trait3 = "Positive trait 3: " + str(headhunted_pos_trait3)
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait4]" if headhunter_scaling_pos_traits() >= 4:
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait4:
                                $ trait_name_temp = headhunted_pos_trait4
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,pos_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait4 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait4 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait4 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait4 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait4 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait4 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait4 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait4 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait4 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait4 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits + gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait4 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait4 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait4 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait4 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait4 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_pos_trait1, headhunted_pos_trait2, headhunted_pos_trait3, headhunted_pos_trait5] if x]:
                                $ headhunted_pos_trait4 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait4 = "Not specified"
                            $ menu_item_pos_trait4 = "Positive trait 4: " + str(headhunted_pos_trait4)
                            jump headhunter_menu_traits
                        "[menu_item_pos_trait5]" if headhunter_scaling_pos_traits() >= 5:
                            $ trait_name_temp = "Not specified"
                            if headhunted_pos_trait5:
                                $ trait_name_temp = headhunted_pos_trait5
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,pos_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait5 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait5 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait5 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait5 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait5 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_dict[trait_name_temp.capitalize()] in (pos_traits + gold_traits):
                                    if trait_dict[trait_name_temp.capitalize()] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait5 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait5 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait5 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait5 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait5 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_dict[capitalize_allcaps(trait_name_temp)] in (pos_traits + gold_traits):
                                    if trait_dict[capitalize_allcaps(trait_name_temp)] in gold_traits:
                                        if headhunter_scaling() < 20 or headhunter_gold_traits >= 1 + min(1,headhunter_scaling()//25):
                                            $ headhunted_pos_trait5 = "Too many gold traits!"
                                        elif not headhunted_original:
                                            $ headhunted_pos_trait5 = "Not original girl!"
                                        else:
                                            $ headhunted_pos_trait5 = trait_name_temp
                                            $ headhunted_original = 1
                                            $ deforig = "Yes"
                                    elif trait_name_temp.lower() in ("recently kidnapped", ):
                                        $ headhunted_pos_trait5 = "Nice try! Catch her yourself!"
                                    else:
                                        $ headhunted_pos_trait5 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_pos_trait1, headhunted_pos_trait2, headhunted_pos_trait3, headhunted_pos_trait4] if x]:
                                $ headhunted_pos_trait5 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_pos_trait5 = "Not specified"
                            $ menu_item_pos_trait5 = "Positive trait 5: " + str(headhunted_pos_trait5)
                            jump headhunter_menu_traits
                        "[menu_item_neg_trait1]" if headhunter_scaling_neg_traits() >= 1:
                            $ trait_name_temp = "Not specified"
                            if headhunted_neg_trait1:
                                $ trait_name_temp = headhunted_neg_trait1
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,neg_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait1 = "Nice try! Catch her yourself!"
                                elif trait_dict[trait_name_temp] in neg_traits:
                                    $ headhunted_neg_trait1 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait1 = "Nice try! Catch her yourself!"
                                elif trait_dict[trait_name_temp.capitalize()] in neg_traits:
                                    $ headhunted_neg_trait1 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait1 = "Nice try! Catch her yourself!"
                                elif trait_dict[capitalize_allcaps(trait_name_temp)] in neg_traits:
                                    $ headhunted_neg_trait1 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_neg_trait2, headhunted_neg_trait3] if x]:
                                $ headhunted_neg_trait1 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_neg_trait1 = "Not specified"
                            $ menu_item_neg_trait1 = "Negative trait 1: " + str(headhunted_neg_trait1)
                            jump headhunter_menu_traits
                        "[menu_item_neg_trait2]" if headhunter_scaling_neg_traits() >= 2:
                            $ trait_name_temp = "Not specified"
                            if headhunted_neg_trait2:
                                $ trait_name_temp = headhunted_neg_trait2
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,neg_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait2 = "Nice try! Catch her yourself!"
                                elif trait_dict[trait_name_temp] in neg_traits:
                                    $ headhunted_neg_trait2 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait2 = "Nice try! Catch her yourself!"
                                elif trait_dict[trait_name_temp.capitalize()] in neg_traits:
                                    $ headhunted_neg_trait2 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait2 = "Nice try! Catch her yourself!"
                                elif trait_dict[capitalize_allcaps(trait_name_temp)] in neg_traits:
                                    $ headhunted_neg_trait2 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_neg_trait1, headhunted_neg_trait3] if x]:
                                $ headhunted_neg_trait2 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_neg_trait2 = "Not specified"
                            $ menu_item_neg_trait2 = "Negative trait 2: " + str(headhunted_neg_trait2)
                            jump headhunter_menu_traits
                        "[menu_item_neg_trait3]" if headhunter_scaling_neg_traits() >= 3:
                            $ trait_name_temp = "Not specified"
                            if headhunted_neg_trait3:
                                $ trait_name_temp = headhunted_neg_trait3
                            if trait_name_temp == "Not specified":
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            else:
                                $ trait_name_temp = renpy.input("Trait name: ", default = "")
                            $ trait_name_temp = string_to_list_version(trait_name_temp,neg_trait_names)
                            if trait_name_temp in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait3 = "Nice try! Catch her yourself!"
                                elif trait_dict[trait_name_temp] in neg_traits:
                                    $ headhunted_neg_trait3 = trait_name_temp
                            elif trait_name_temp.capitalize() in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait3 = "Nice try! Catch her yourself!"
                                elif trait_dict[trait_name_temp.capitalize()] in neg_traits:
                                    $ headhunted_neg_trait3 = trait_name_temp.capitalize()
                            elif capitalize_allcaps(trait_name_temp) in list(trait_dict.keys()):
                                if trait_name_temp.lower() in ("recently kidnapped", ):
                                    $ headhunted_neg_trait3 = "Nice try! Catch her yourself!"
                                elif trait_dict[capitalize_allcaps(trait_name_temp)] in neg_traits:
                                    $ headhunted_neg_trait3 = capitalize_allcaps(trait_name_temp)
                            if trait_name_temp.lower() in [x.lower() for x in [headhunted_neg_trait1, headhunted_neg_trait2] if x]:
                                $ headhunted_neg_trait3 = "Already asked for!"
                            if trait_name_temp in ("", "None", "Non", "No", "N", "Not", "NotS", "Not specified", "Not Specified", "none", "non", "no", "n", "nots", "Nots", "not specified"):
                                $ headhunted_neg_trait3 = "Not specified"
                            $ menu_item_neg_trait3 = "Negative trait 3: " + str(headhunted_neg_trait3)
                            jump headhunter_menu_traits
                        "Back":
                            jump headhunter_menu
                "Sexuality" if headhunter_scaling() >= 2:
                    label headhunter_menu_sexuality:
                    menu:
                        "[menu_item_sex_experience]" if headhunter_scaling() >= 11:
                            $ sex_name_temp = renpy.input("Sexual experience rating from 0 to 5,\n 0 = random: ", default = "")
                            python: 
                                try:
                                    sex_name_temp = int(sex_name_temp)
                                except ValueError: 
                                    if headhunted_sexual_experience:
                                        sex_name_temp = headhunted_sexual_experience
                                    else:
                                        sex_name_temp = 0
                            $ headhunted_sexual_experience = max(0,min(5, sex_name_temp))
                            $ menu_item_sex_experience = "Sexual experience: " + str(headhunted_sexual_experience)
                            jump headhunter_menu_sexuality

                        "[menu_item_farm_weakness]" if headhunter_scaling() >= 21:
                            $ sex_name_temp = "random"
                            if headhunted_farm_weakness:
                                $ sex_name_temp = headhunted_farm_weakness
                            if sex_name_temp == "random":
                                $ sex_name_temp = renpy.input("Choose: stallion, beast, monster,\n machine or random. ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Choose: stallion, beast, monster,\n machine or random. ", default = "").lower()
                            if sex_name_temp in ("stallion", "stallio", "stalli", "stall", "stal", "sta", "st", "s", "stallin", "stllion", "stalion", "stlion", "stalin", "staln", "stlio", "stln", "stlo", "stl", "sto", "sl", "sn"):
                                $ sex_name_temp = "stallion"
                            elif sex_name_temp in ("beast", "beas", "bea", "be", "b", "best", "bst", "bes", "bs", "bt"):
                                $ sex_name_temp = "beast"
                            elif sex_name_temp in ("monster", "monste", "monst", "mons", "mon", "mo", "monstr", "mnster", "mnstr", "mnst", "mstr", "mst", "mns", "mn", "mt"):
                                $ sex_name_temp = "monster"
                            elif sex_name_temp in ("machine", "machin", "machi", "mach", "mac", "ma", "machne", "mchine", "machne", "mchne", "mchn", "mch", "mas", "mc", "mh"):
                                $ sex_name_temp = "machine"
                            elif sex_name_temp in ("random", "rando", "rand", "ran", "ra", "rn", "rd", "rm", "rdm", "rnd", "rndm", "randm"):
                                $ sex_name_temp = "random"
                            if sex_name_temp == "":
                                $ sex_name_temp = "random"
                            if sex_name_temp in farm_type_list + ["random"]:
                                $ headhunted_farm_weakness = sex_name_temp
                            $ menu_item_farm_weakness = "Farm weakness: " + str(headhunted_farm_weakness.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_pos_fixation1]" if headhunter_scaling() >= 3:
                            $ sex_name_temp = "None"
                            if headhunted_favorite_fixation1:
                                $ sex_name_temp = headhunted_favorite_fixation1
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            $ sex_name_temp = string_to_list_version(sex_name_temp,list(fix_dict.keys()))
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_favorite_fixation1 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_favorite_fixation1 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_favorite_fixation1 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_favorite_fixation1 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_pos_fixation1 = "Fetish 1: " + str(headhunted_favorite_fixation1.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_pos_fixation2]" if headhunter_scaling() >= 17:
                            $ sex_name_temp = "None"
                            if headhunted_favorite_fixation2:
                                $ sex_name_temp = headhunted_favorite_fixation2
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            $ sex_name_temp = string_to_list_version(sex_name_temp,list(fix_dict.keys()))
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_favorite_fixation2 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_favorite_fixation2 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_favorite_fixation2 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_favorite_fixation2 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_pos_fixation2 = "Fetish 2: " + str(headhunted_favorite_fixation2.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_neg_fixation1]" if headhunter_scaling() >= 2:
                            $ sex_name_temp = "None"
                            if headhunted_disliked_fixation1:
                                $ sex_name_temp = headhunted_disliked_fixation1
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            $ sex_name_temp = string_to_list_version(sex_name_temp,list(fix_dict.keys()))
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_disliked_fixation1 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_disliked_fixation1 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_disliked_fixation1 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_disliked_fixation1 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_neg_fixation1 = "Phobia 1: " + str(headhunted_disliked_fixation1.lower())
                            jump headhunter_menu_sexuality
                        "[menu_item_neg_fixation2]" if headhunter_scaling() >= 23:
                            $ sex_name_temp = "None"
                            if headhunted_disliked_fixation2:
                                $ sex_name_temp = headhunted_disliked_fixation2
                            if sex_name_temp == "None":
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            else:
                                $ sex_name_temp = renpy.input("Fixation name: ", default = "").lower()
                            $ sex_name_temp = string_to_list_version(sex_name_temp,list(fix_dict.keys()))
                            if sex_name_temp == "":
                                $ sex_name_temp = "None"
                                $ headhunted_disliked_fixation2 = "None"
                            if sex_name_temp in fix_dict.keys():
                                $ headhunted_disliked_fixation2 = sex_name_temp
                            elif sex_name_temp.capitalize() in fix_dict.keys():
                                $ headhunted_disliked_fixation2 = sex_name_temp.capitalize()
                            elif capitalize_allcaps(sex_name_temp) in fix_dict.keys():
                                $ headhunted_disliked_fixation2 = capitalize_allcaps(sex_name_temp)
                            $ menu_item_neg_fixation2 = "Phobia 2: " + str(headhunted_disliked_fixation2.lower())
                            jump headhunter_menu_sexuality
                        "Back":
                            jump headhunter_menu
                "Ready":

                    you "Done. Start looking."
                    label headhunter_ready:

                    $ repeat_ready = False

                    $ headhunter_modifier = 1.0
                    $ headhunted_pos_traits = []
                    $ headhunted_neg_traits = []
                    $ headhunted_favorite_acts = []
                    $ headhunted_disliked_acts = []
                    $ headhunted_favorite_fixations = []
                    $ headhunted_disliked_fixations = []

#                    if headhunted_virginity_trait:
#                        if headhunted_virginity_trait in ["Random"]:
#                            $ headhunted_virginity_trait2 = weighted_choice([(trait_dict["Virgin"],10), (trait_dict["Housebroken"],5), (trait_dict["Teacher's pet"],0), (trait_dict["Farmgirl"],10), (trait_dict["Deflowered"],40), (trait_dict["Broken in"],10), (trait_dict["Experienced"],10), (trait_dict["Jaded"],5), (trait_dict["Trauma"],10)])
#                        elif headhunted_virginity_trait in list(trait_dict.keys()):
#                            if trait_dict[headhunted_virginity_trait] in (pos_traits_virginity + neg_traits_virginity):
#                                $ headhunted_virginity_trait2 = trait_dict[headhunted_virginity_trait]
#                            else:
#                                $ headhunted_virginity_trait2 = weighted_choice([(trait_dict["Virgin"],10), (trait_dict["Housebroken"],5), (trait_dict["Teacher's pet"],0), (trait_dict["Farmgirl"],10), (trait_dict["Deflowered"],40), (trait_dict["Broken in"],10), (trait_dict["Experienced"],10), (trait_dict["Jaded"],5), (trait_dict["Trauma"],10)])

                    if headhunted_pos_trait1: 
                        if headhunted_pos_trait1 in list(trait_dict.keys()):
                            if trait_dict[headhunted_pos_trait1] in (pos_traits + gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait1]
                    if headhunted_pos_trait2: 
                        if headhunted_pos_trait2 in list(trait_dict.keys()):
                            if trait_dict[headhunted_pos_trait2] in (pos_traits + gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait2]
                    if headhunted_pos_trait3: 
                        if headhunted_pos_trait3 in list(trait_dict.keys()):
                            if trait_dict[headhunted_pos_trait3] in (pos_traits + gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait3]
                    if headhunted_pos_trait4: 
                        if headhunted_pos_trait4 in list(trait_dict.keys()):
                            if trait_dict[headhunted_pos_trait4] in (pos_traits + gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait4]
                    if headhunted_pos_trait5: 
                        if headhunted_pos_trait5 in list(trait_dict.keys()):
                            if trait_dict[headhunted_pos_trait5] in (pos_traits + gold_traits):
                                $ headhunted_pos_traits = headhunted_pos_traits + [headhunted_pos_trait5]
                    if headhunted_neg_trait1: 
                        if headhunted_neg_trait1 in list(trait_dict.keys()):
                            if trait_dict[headhunted_neg_trait1] in neg_traits:
                                $ headhunted_neg_traits = headhunted_neg_traits + [headhunted_neg_trait1]
                    if headhunted_neg_trait2: 
                        if headhunted_neg_trait2 in list(trait_dict.keys()):
                            if trait_dict[headhunted_neg_trait2] in neg_traits:
                                $ headhunted_neg_traits = headhunted_neg_traits + [headhunted_neg_trait2]
                    if headhunted_neg_trait3: 
                        if headhunted_neg_trait3 in list(trait_dict.keys()):
                            if trait_dict[headhunted_neg_trait3] in neg_traits:
                                $ headhunted_neg_traits = headhunted_neg_traits + [headhunted_neg_trait3]

                    if headhunted_favorite_act1 in extended_sex_acts:
                        $ headhunted_favorite_acts = headhunted_favorite_acts + [headhunted_favorite_act1]
                    if headhunted_favorite_act2 in extended_sex_acts:
                        $ headhunted_favorite_acts = headhunted_favorite_acts + [headhunted_favorite_act2]
                    if headhunted_disliked_act1 in extended_sex_acts:
                        $ headhunted_disliked_acts = headhunted_disliked_acts + [headhunted_disliked_act1]
                    if headhunted_disliked_act2 in extended_sex_acts:
                        $ headhunted_disliked_acts = headhunted_disliked_acts + [headhunted_disliked_act2]

                    if headhunted_favorite_fixation1 in fix_dict.keys():
                        $ headhunted_favorite_fixations = headhunted_favorite_fixations + [headhunted_favorite_fixation1]
                    if headhunted_favorite_fixation2 in fix_dict.keys():
                        $ headhunted_favorite_fixations = headhunted_favorite_fixations + [headhunted_favorite_fixation2]
                    if headhunted_disliked_fixation1 in fix_dict.keys():
                        $ headhunted_disliked_fixations = headhunted_disliked_fixations + [headhunted_disliked_fixation1]
                    if headhunted_disliked_fixation2 in fix_dict.keys():
                        $ headhunted_disliked_fixations = headhunted_disliked_fixations + [headhunted_disliked_fixation2]

                    if headhunted_sexual_experience > 0:
                            $ headhunter_modifier += headhunted_sexual_experience / 5.0
                    $ sex_exp_list = [ "random", "very inexperienced", "inexperienced", "average", "experienced", "very experienced"]

                    if headhunted_personality in gpersonalities.keys():
                        $ headhunted_personality2 = [headhunted_personality]
                    elif headhunted_personality in ["random"]:
                        $ headhunted_personality2 = []
                    else:
                        $ headhunted_personality2 = []

                    python:
                        try:
                            input_dict = defaultdict(list)
                            input_dict = read_init_file(get_real_girlpath(headhunted_name) + "/_BK.ini")
                        except:
                            input_dict = defaultdict(list)

                    $ input_dict["path"] = get_real_girlpath(headhunted_name)
                    $ game.headhunter_free = headhunted_free

                    if headhunted_rank != district.rank:
                        $ diff_rank = abs(headhunted_rank - district.rank)
                        if diff_rank >= 6:
                            $ headhunter_modifier += 2.0
                        elif diff_rank >= 5.5:
                            $ headhunter_modifier += 1.75
                        elif diff_rank >= 5:
                            $ headhunter_modifier += 1.5
                        elif diff_rank >= 4.5:
                            $ headhunter_modifier += 1.25
                        elif diff_rank >= 4:
                            $ headhunter_modifier += 1.0
                        elif diff_rank >= 3.5:
                            $ headhunter_modifier += 0.75
                        elif diff_rank >= 3:
                            $ headhunter_modifier += 0.5
                        elif diff_rank >= 2.5:
                            $ headhunter_modifier += 0.35
                        elif diff_rank >= 2:
                            $ headhunter_modifier += 0.25
                        elif diff_rank >= 1.5:
                            $ headhunter_modifier += 0.15
                        elif diff_rank >= 1:
                            $ headhunter_modifier += 0.1
                        elif diff_rank >= 0.5:
                            $ headhunter_modifier += 0.1

                    if headhunted_name != "Nobody specific":
                        $ headhunter_modifier += 0.0 # 0.5
                    if headhunted_original:
                        $ headhunter_modifier += 1.0
                    if headhunted_beauty:
                        $ headhunter_modifier += headhunted_beauty / 10.0
                    if headhunted_body:
                        $ headhunter_modifier += headhunted_body / 10.0
                    if headhunted_charm:
                        $ headhunter_modifier += headhunted_charm / 10.0
                    if headhunted_refinement:
                        $ headhunter_modifier += headhunted_refinement / 10.0
                    if headhunted_libido:
                        $ headhunter_modifier += headhunted_libido / 10.0
                    if headhunted_obedience:
                        $ headhunter_modifier += headhunted_obedience / 10.0
                    if headhunted_constitution:
                        $ headhunter_modifier += headhunted_constitution / 10.0
                    if headhunted_sensitivity:
                        $ headhunter_modifier += headhunted_sensitivity / 10.0
#                    if headhunted_virginity_trait in list(trait_dict.keys()):
#                        if headhunted_virginity_trait in ["Deflowered", "Random"]:
#                            $ headhunter_modifier += 0.0
#                        elif trait_dict[headhunted_virginity_trait] in pos_traits_virginity:
#                            $ headhunter_modifier += 0.75
#                        elif headhunted_virginity_trait in ["Trauma"]:
#                            $ headhunter_modifier += 0.25
#                        elif trait_dict[headhunted_virginity_trait] in neg_traits_virginity:
#                            $ headhunter_modifier += 0.50
#                        else:
#                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait1 in list(trait_dict.keys()):
                        if trait_dict[headhunted_pos_trait1] in gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait2 in list(trait_dict.keys()):
                        if trait_dict[headhunted_pos_trait2] in gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait3 in list(trait_dict.keys()):
                        if trait_dict[headhunted_pos_trait3] in gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait4 in list(trait_dict.keys()):
                        if trait_dict[headhunted_pos_trait4] in gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_pos_trait5 in list(trait_dict.keys()):
                        if trait_dict[headhunted_pos_trait5] in gold_traits:
                            $ headhunter_modifier += 0.75
                        else:
                            $ headhunter_modifier += 0.25
                    if len(headhunted_pos_traits) > 2:
                        $ headhunter_modifier += 0.5 * (len(headhunted_pos_traits) - 2)
                    if headhunted_neg_trait1 in list(trait_dict.keys()):
                        if len(headhunted_pos_traits) > 2:
                            $ headhunter_modifier += 0.1
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_neg_trait2 in list(trait_dict.keys()):
                        if len(headhunted_pos_traits) > 2:
                            $ headhunter_modifier += 0.1
                        else:
                            $ headhunter_modifier += 0.25
                    if headhunted_neg_trait3 in list(trait_dict.keys()):
                        if len(headhunted_pos_traits) > 2:
                            $ headhunter_modifier += 0.1
                        else:
                            $ headhunter_modifier += 0.25
                    if len(headhunted_neg_traits) > 1:
                        $ headhunter_modifier -= 0.3 * len(headhunted_neg_traits)
                    if headhunted_personality in gpersonalities.keys():
                        $ headhunter_modifier += 0.25
                    if headhunted_favorite_act1 in extended_sex_acts:
                        $ headhunter_modifier += 0.25
                    if headhunted_favorite_act2 in extended_sex_acts:
                        $ headhunter_modifier += 0.25
                    if headhunted_disliked_act1 in extended_sex_acts:
                        $ headhunter_modifier += 0.1
                    if headhunted_disliked_act2 in extended_sex_acts:
                        $ headhunter_modifier += 0.1
                    if headhunted_favorite_fixation1 in fix_dict.keys():
                        $ headhunter_modifier += 0.25
                    if headhunted_favorite_fixation2 in fix_dict.keys():
                        $ headhunter_modifier += 0.25
                    if headhunted_disliked_fixation1 in fix_dict.keys():
                        $ headhunter_modifier += 0.1
                    if headhunted_disliked_fixation2 in fix_dict.keys():
                        $ headhunter_modifier += 0.1
                    if headhunted_farm_weakness in farm_type_list:
                        $ headhunter_modifier += 0.25

                    call headhunter_make_input_dict(making_name = headhunted_name)

                    call make_hhgirl(making_name = headhunted_name)

                    if hhgirl.original and not headhunted_original:
                        if hhgirl.original == "unique" and headhunter_scaling() >= 20 and compare_girl_paths(get_real_girlpath(input_dict["path"]),get_real_girlpath(hhgirl.path)):
                            $ headhunted_original = True
                            $ headhunter_modifier += 1.0
                        else:
                            if hhgirl.original == "unique":
                                $ attempts_original = 0
                                while (hhgirl.original == "unique" or compare_girl_paths(get_real_girlpath(input_dict["path"]),get_real_girlpath(hhgirl.path))) and attempts_original < 100:
                                    $ attempts_original += 1
                                    $ hhgirl = get_girls(1)[0]
                                if hhgirl.original == "unique" or compare_girl_paths(get_real_girlpath(input_dict["path"]),get_real_girlpath(hhgirl.path)):
                                    $ hhgirl = None
                            else:
                                $ attempts_original = 0
                                while hhgirl.original and attempts_original < 100:
                                    $ attempts_original += 1
                                    call make_hhgirl(making_name = headhunted_name)
                                if hhgirl.original:
                                    $ hhgirl = None

                    if input_dict["path"] and not compare_girl_paths(get_real_girlpath(input_dict["path"]),get_real_girlpath(hhgirl.path)):

#                        $ renpy.say("","Wrong girl, making new one! (" + get_real_girlpath(hhgirl.path) + " vs " + get_real_girlpath(input_dict["path"]) + ")" )

                        if hhgirl.original and not headhunted_original:
                            $ attempts_match = 0
                            while hhgirl.original and attempts_match < 100:
                                $ attempts_match += 1
                                $ hhgirl = get_girls(1)[0]
                            if hhgirl.original:
                                $ hhgirl = None

#                        $ renpy.say("","She is " + hhgirl.path)

                        $ new_path = get_real_girlpath(hhgirl.path)
                            
                        call headhunter_make_input_dict(making_name = new_path)

                        call make_hhgirl(making_name = new_path)

                        if hhgirl.original and not headhunted_original:
                            $ attempts_match_original = 0
                            while hhgirl.original and attempts_match_original < 100:
                                $ attempts_match_original += 1
                                call make_hhgirl(making_name = new_path)
                            if hhgirl.original:
                                $ hhgirl = None

                    if hhgirl:

                        $ hhgirl.traits = [x for x in hhgirl.traits if not trait_dict[x.name] in gold_traits + pos_traits + neg_traits] + [x for x in hhgirl.traits if trait_dict[x.name] in gold_traits] + [x for x in hhgirl.traits if trait_dict[x.name] in pos_traits] + [x for x in hhgirl.traits if trait_dict[x.name] in neg_traits]

#                        $ hhgirl.add_trait(headhunted_virginity_trait2)

                        ################ Discount for missing traits due to trait limits and whatnot ############

                        $ headhunter_modifier = round(headhunter_modifier,2)
                        $ headhunter_modifier_start = headhunter_modifier + 0

                        $ headhunter_start_gold_traits = len([x for x in headhunted_pos_traits if trait_dict[x] in gold_traits])
                        $ headhunter_start_pos_traits = len(headhunted_pos_traits) - headhunter_start_gold_traits
                        $ headhunter_start_neg_traits = len(headhunted_neg_traits)

                        $ headhunter_final_pos_traits = len([x for x in hhgirl.traits if trait_dict[x.name] in pos_traits])
                        $ headhunter_final_gold_traits = len([x for x in hhgirl.traits if trait_dict[x.name] in gold_traits])
                        $ headhunter_final_neg_traits = len([x for x in hhgirl.traits if trait_dict[x.name] in neg_traits])

                        if headhunter_final_pos_traits < headhunter_start_pos_traits:
                            $ headhunter_modifier -= 0.25 * (headhunter_start_pos_traits - headhunter_final_pos_traits)

                            $ headhunter_modifier -= 0.1 * (headhunter_start_pos_traits - headhunter_final_pos_traits)

                        if headhunter_final_gold_traits < headhunter_start_gold_traits:
                            $ headhunter_modifier -= 0.75 * (headhunter_start_gold_traits - headhunter_final_gold_traits)

                            $ headhunter_modifier -= 0.25 * (headhunter_start_gold_traits - headhunter_final_gold_traits)

                        if headhunter_final_neg_traits < headhunter_start_neg_traits:
                            if headhunter_start_gold_traits + headhunter_start_pos_traits > 2:
                                $ headhunter_modifier -= 0.1 * (headhunter_start_neg_traits - headhunter_final_neg_traits)

                                $ headhunter_modifier -= 0.05 * (headhunter_start_neg_traits - headhunter_final_neg_traits)
                            else:
                                $ headhunter_modifier -= 0.25 * (headhunter_start_neg_traits - headhunter_final_neg_traits)

                                $ headhunter_modifier -= 0.1 * (headhunter_start_neg_traits - headhunter_final_neg_traits)

                            if headhunter_start_neg_traits > 1:
                                $ headhunter_modifier += 0.3 * (headhunter_start_neg_traits - headhunter_final_neg_traits)

                        if headhunter_final_pos_traits + headhunter_final_gold_traits < headhunter_start_gold_traits + headhunter_start_pos_traits:
                            if headhunter_start_gold_traits + headhunter_start_pos_traits > 2: 
                                $ headhunter_modifier -= 0.5 * min((headhunter_start_gold_traits + headhunter_start_pos_traits - (headhunter_final_pos_traits + headhunter_final_gold_traits)), (headhunter_start_gold_traits + headhunter_start_pos_traits - 2))

                        $ headhunter_modifier = round(headhunter_modifier,2)
                        $ headhunter_modifier_final = headhunter_modifier + 0

                        $ game.headhunter_price = hhgirl.get_price("buy") * headhunter_modifier
                        if express_default == "express.":
                            $ game.headhunter_price = round_int(game.headhunter_price*1.5)
                        $ headhunter_advance = max(250, round_int((game.headhunter_price - hhgirl.get_price("buy")) / 500.0) * 250)
                        $ headhunter_advance_str = str(headhunter_advance) + " gold"
                        $ payment = max(10,headhunter_advance - game.headhunter_discount//2*100)
                        $ payment_str = str(payment) + " gold"
#                        $ payment_str += "\n Modifier difference: " + str(headhunter_modifier_final) + " / " + str(headhunter_modifier_start)

                        play sound s_hmm
                        if game.headhunter_free:
                            headhunter "This'll be [headhunter_advance_str] to find the booty, cap'n!"
                        else:
                            headhunter "This'll be [headhunter_advance_str] to find the booty first, cap'n. We'll talk about the real price later."

                        if repeat_ready:
                            hide screen girl_stats
                            hide screen girl_profile

                        show screen girl_stats(hhgirl, context="slavemarket")
                        show screen girl_profile(hhgirl, context="slavemarket")

                        if not repeat_ready:
                            show headhunter at centerhighright with move

                        if game.headhunter_discount > 0:
                            play sound s_giggle
                            $ discount_str = str(headhunter_advance - payment) + " gold"
                            headhunter "And matey, you get a [discount_str] discount, 'cus it's yer first time! *wink*"
                        
                        if renpy.call_screen("yes_no", "Price: [payment_str]\nHaggle about it?"):
#                        if renpy.call_screen("yes_no", "Haggle about the price?"):
                            show headhunter angry at centerhighright with dissolve
                            play sound s_ahh_frustrated
                            headhunter angry "Arr! Hold yer horses..."
                            $ del hhgirl
                            $ renpy.free_memory()
                            $ repeat_ready = True
                            show headhunter at centerhighright with dissolve
                            jump headhunter_ready

                        python:
                            try:
                                game.headhunter_debug_enabled
                            except:
                                game.headhunter_debug_enabled = False

                        if game.headhunter_debug_enabled and renpy.call_screen("yes_no", "Get a debug discount?"):                        #False: 
                            show headhunter strip2 at centerhighright with dissolve
                            play sound s_aaha
                            headhunter "You meanie!"
                            $ game.headhunter_time = 0
                            $ game.headhunter_price = 0
                            $ game.headhunter_girl = hhgirl
                            show headhunter strip1 at centerhighright with dissolve
                            play sound s_ahh_frustrated
                            headhunter "Hmmph!"
                            hide headhunter strip1 with dissolve
                            $ game.headhunter_button_enabled = 0
                            jump headhunter_end
                        elif MC.gold >= payment:
                            if renpy.call_screen("yes_no", "Pay the advance of [payment_str]?"):
                                $ MC.gold -= payment
                                python:
                                    try:
                                        game.headhunter_money_paid += payment
                                    except:
                                        game.headhunter_money_paid = payment
                                play sound s_giggle
                                play sound s_gold
                                $ game.headhunter_time = round_int(3 * headhunter_modifier)
                                if express_default == "express.":
                                    $ game.headhunter_time = max(1,round_int((0.333+(random.random()/3)) * game.headhunter_time))
                                $ game.headhunter_girl = hhgirl
                                headhunter "Pleasure doin' business with ya, cap'n!"
                                show headhunter at centerhighright with dissolve
                                play sound s_evil_laugh
                                headhunter "We'll be back in [game.headhunter_time] days!"
                                hide headhunter with dissolve
                                $ game.headhunter_button_enabled = 0
                                jump headhunter_end
                            else:
                                show headhunter at centerhighright with dissolve
                                play sound s_hmm
                                headhunter "Window shopping, eh, cap'n?"
                                show headhunter angry at centerhighright with dissolve
                                play sound s_woman_scream
                                headhunter "I'm of a mind put some lead into yer balls! Be glad that I'm in a good mood today!"
                                hide headhunter angry with dissolve
                                $ game.headhunter_button_enabled = 1
                                jump headhunter_end
                        else:
                            show headhunter at centerhighright with dissolve
                            play sound s_evil_laugh
                            headhunter "Yer hoard be empty, cap'n! Come back when you've raided some booty for yerself!"
                            hide headhunter with dissolve
                            $ game.headhunter_button_enabled = 1
                            jump headhunter_end
                    else:
                        show headhunter at centerhighright with dissolve
                        play sound s_aaha
                        headhunter "No can do, cap'n. It be impossible!"
                        hide headhunter with dissolve
                        $ game.headhunter_button_enabled = 1
                        jump headhunter_end

                "Nevermind":

                    you "Nevermind."
                    play sound s_sigh
                    headhunter "..."
                    show headhunter strip1 at centerhigh with dissolve
                    play sound s_aaha
                    headhunter "You'll be back for more booty, matey!"
                    hide headhunter strip1 with dissolve
                    $ game.headhunter_button_enabled = 1
                    jump headhunter_end
                        


label headhunter_delivers:

        $ game.interacting_with_headhunter = 1
        show headhunter at truecenter with dissolve
        $ girl_name = game.headhunter_girl.fullname
        if game.headhunter_free:
            play sound s_hmm
            show screen girl_profile(game.headhunter_girl, context="slavemarket")
            show headhunter at centerhighleft with move
            headhunter "Thar' she blows, cap'n: [girl_name]!"
            hide screen girl_profile
            show headhunter at truecenter with move
            play sound s_giggle
            headhunter "You'll have to catch her yerself!"
            $ passes = 0
            $ temp_position = dice(len(game.free_girls))-1
            $ talkdate = calendar.time
            $ found = False
            $ temp_loc = None
            python: 
                for i in xrange(0, len(game.free_girls) - 1):
                    if game.free_girls[i].location and not game.free_girls[i].original:
                        if not game.free_girls[i].talked_to_date:
                            temp_position = i
                            found = True
                            break
                        elif game.free_girls[temp_position].talked_to_date < talkdate:
                            temp_position = i
                            talkdate = game.free_girls[temp_position].talked_to_date
                            found = True
                if not found: # all originals
                    talkdate = calendar.time
                    for i in xrange(0, len(game.free_girls) - 1):
                        if game.free_girls[i].location:
                            if not game.free_girls[i].talked_to_date:
                                temp_position = i
                                found = True
                                break
                            elif game.free_girls[temp_position].talked_to_date < talkdate:
                                temp_position = i
                                talkdate = game.free_girls[temp_position].talked_to_date
                                found = True
                if not found:
                    temp_position = len(game.free_girls)
                    ddist = [x for x in district_dict.values() if x.rank <= district.rank]
                    random.shuffle(ddist)
                    breaking = False
                    for dist in ddist:
                        if breaking:
                            break
                        ddist_loc = [x for x in location_dict[dist.name]]
                        random.shuffle(ddist_loc)
                        for loc in ddist_loc:
                            temp_loc = loc
                            if len(loc.girls) < 3:
                                breaking = True
                                break
            $ game.headhunter_girl.free = True
            $ game.headhunter_girl.tips = 50
#            if not temp_loc:
#                $ temp_loc = game.free_girls[temp_position].location
#                $ game.free_girls[temp_position] = game.headhunter_girl
#                $ game.free_girls[temp_position].location = temp_loc
#                $ temp_loc.girls.append(game.free_girls[temp_position])
#            else:
            $ game.free_girls.append(game.headhunter_girl)
            $ game.free_girls[-1].location = temp_loc
#            $ temp_loc.girls.append(game.headhunter_girl)
            
            $ cycle_free_girls()
#            $ game.free_girls.append(game.headhunter_girl)
            $ game.headhunter_girl = None
            $ game.headhunter_price = 0
            $ game.headhunter_time = 0
            $ game.headhunter_free = 0
            $ game.headhunter_discount = 0
            show headhunter strip1 at truecenter with dissolve
            play sound s_evil_laugh
            headhunter "Pleasure doin' business with ya!"
            hide headhunter strip1 with dissolve
            $ game.headhunter_button_enabled = 1
            jump headhunter_end2
        else:
            $ headhunter_price_final = int(max(game.headhunter_girl.get_price("buy"), game.headhunter_price - max(250, round_int((game.headhunter_price - hhgirl.get_price("buy")) / 500.0) * 250)))
            $ headhunter_price_final_str = str(headhunter_price_final) + " gold"
            $ finders_fee = max(0, headhunter_price_final - game.headhunter_girl.get_price("buy"))
            $ finders_fee_str = str(finders_fee) + " gold"
            $ payment = max(game.headhunter_girl.get_price("buy"),headhunter_price_final - game.headhunter_discount//2*100)
            $ finder_payment = max(0,finders_fee - game.headhunter_discount//2*100)
            play sound s_hmm
            show screen girl_profile(game.headhunter_girl, context="slavemarket")
            show headhunter at centerhighleft with move
            headhunter "Here's yer booty, cap'n: [girl_name]!"
            hide screen girl_profile
            show headhunter at truecenter with move
            play sound s_scream
            headhunter "That'll be [headhunter_price_final_str]!"
            if game.headhunter_discount > 0:
                play sound s_giggle
                $ discount_str = str(finders_fee - finder_payment) + " gold"
                headhunter "Oh, and yer first-timer discount is [discount_str]! *wink*"
            $ slavery_default = 1
            if slavery_default == 0:
                $ slavery_default_string = "Slave Market."
            else:
                $ slavery_default_string = "buy her."
            $ payment_str = str(payment) + " gold"
            $ finder_payment_str = str(finder_payment) + " gold"
            if renpy.call_screen("yes_no", "Do you want to buy her now for [payment_str]? Otherwise you will pay the finder's fee of [finder_payment_str] and she is sent to the Slave Market?"): # Currently: " + slavery_default_string):
                $ slavery_default = 1
            else:
                $ slavery_default = 0

            if slavery_default == 0 and MC.gold >= finder_payment:
                label headhunter_release:
                if finder_payment > 0:
                    play sound s_gold
                $ MC.gold -= finder_payment
                python:
                    try:
                        game.headhunter_money_paid += finder_payment
                    except:
                        game.headhunter_money_paid = finder_payment
                $ game.headhunter_discount = 0
                $ slavemarket.girls.append(game.headhunter_girl)
                $ game.headhunter_girl = None
                $ game.headhunter_price = 0
                $ game.headhunter_time = 0
                $ game.headhunter_free = 0
                python:
                    try:
                        game.headhunter_girls_bought += 1
                    except:
                        game.headhunter_girls_bought = 1
                show headhunter strip1 at truecenter with dissolve
                play sound s_evil_laugh
                headhunter "Thankee for yer custom, cap'n! Don't forget to go pick her up later!"
                hide headhunter strip1 with dissolve
                $ game.headhunter_button_enabled = 1
                jump headhunter_end2
            elif slavery_default == 1 and MC.gold >= payment:
                label headhunter_buy:
                if len(MC.girls) < brothel.bedrooms:
                    if payment > 0:
                        play sound s_gold
                    python:
                        try:
                            game.headhunter_money_paid += finder_payment
                        except:
                            game.headhunter_money_paid = finder_payment
                        try:
                            game.headhunter_girls_bought += 1
                        except:
                            game.headhunter_girls_bought = 1
                    $ girl = game.headhunter_girl
                    $ game.headhunter_discount = 0
                    $ game.headhunter_girl = None
                    $ game.headhunter_price = 0
                    $ game.headhunter_time = 0
                    $ game.headhunter_free = 0
                    $ MC.buy(None, girl, payment)
#                    $ girl.initial_mood_change_acquired()
                    show headhunter strip1 at truecenter with dissolve
                    play sound s_evil_laugh
                    headhunter "Thankee for yer custom, cap'n! Come visit us again!"
                    hide headhunter strip1 with dissolve
                    $ game.headhunter_button_enabled = 1
                    if girl.personality.name in ("rebel") or girl.get_stat("obedience") < 0.4 * girl.rank * 50:
                        play sound s_ahh_frustrated
                        $ renpy.say(girl.char, "*sullen glare*")
                    elif girl.personality.name in ("pervert") or girl.get_stat("libido") >= 0.6 * girl.rank * 50:
                        play sound s_sexy_sigh
                        $ renpy.say(girl.char, "A brothel owner...? Hmm...")
                    elif girl.personality.name in ("sweet","superficial") or girl.get_stat("sensitivity") >= 0.6 * girl.rank * 50:
                        play sound s_aaha
                        $ renpy.say(girl.char, "Please be kind to me, Master.")
                    elif girl.is_("introvert"):
                        play sound s_sigh
                        $ renpy.say(girl.char, "...")
                    else:
                        play sound s_sigh
                        $ renpy.say(girl.char, "Ah, Master...")

                    jump headhunter_end2
                elif farm.active and farm.has_room():
                    menu:
                        sill "But Master, we don't have enough room..."

                        "Send her to the farm":
                            $ farmed = True
                        "Nevermind":
                            $ farmed = False

                    if not farmed:
                        jump headhunter_no_room

                    if payment > 0:
                        play sound s_gold
                    $ girl = game.headhunter_girl
                    python:
                        try:
                            game.headhunter_money_paid += finder_payment
                        except:
                            game.headhunter_money_paid = finder_payment
                    $ game.headhunter_discount = 0
                    $ game.headhunter_girl = None
                    $ game.headhunter_price = 0
                    $ game.headhunter_time = 0
                    $ game.headhunter_free = 0
                    $ MC.buy(None, girl, payment)
                    python:
                        try:
                            game.headhunter_girls_bought += 1
                        except:
                            game.headhunter_girls_bought = 1
#                    $ girl.initial_mood_change_acquired()
                    show headhunter strip1 at truecenter with dissolve
                    play sound s_evil_laugh
                    headhunter "Thankee for yer custom, cap'n! Come visit us again!"
                    hide headhunter strip1 with dissolve
                    $ game.headhunter_button_enabled = 1
                    if girl.personality.name in ("rebel") or girl.get_stat("obedience") < 0.4 * girl.rank * 50:
                        play sound s_ahh_frustrated
                        $ renpy.say(girl.char, "*sullen glare*")
                    elif girl.personality.name in ("pervert") or girl.get_stat("libido") >= 0.6 * girl.rank * 50:
                        play sound s_sexy_sigh
                        $ renpy.say(girl.char, "A brothel owner...? Hmm...")
                    elif girl.personality.name in ("sweet","superficial") or girl.get_stat("sensitivity") >= 0.6 * girl.rank * 50:
                        play sound s_aaha
                        $ renpy.say(girl.char, "Please be kind to me, Master.")
                    elif girl.is_("introvert"):
                        play sound s_sigh
                        $ renpy.say(girl.char, "...")
                    else:
                        play sound s_sigh
                        $ renpy.say(girl.char, "Ah, Master...")

                    call send_to_farm(girl, can_beg=False, context = "slavemarket")

                    jump headhunter_end2
                else:
                    play sound s_aaha
                    sill sad "But Master, we don't have enough room..." 
                    $ enough_beds = False
                    $ farmed = False
                    if brothel.bedrooms < brothel.get_maxbedrooms():
                        $ price1 = brothel.get_room_price()
                        $ price1_str = str(price1) + " gold"
                        $ price2 = farm.get_pen_cost()
                        $ price2_str = str(price2) + " gold"
                    
                        menu:
                            sill "But Master, we don't have enough room..."
                        
                            "Add a new room to your brothel ([price1_str])" if brothel.bedrooms < brothel.get_maxbedrooms():
                                if brothel.add_room():
                                    $ enough_beds = True

                            "Add a new pen to your farm ([price2_str])" if farm.active and farm.pens < farm.get_pen_limit() and not farm.has_room():
                                $ res, text1 = farm.add_pen()
                                
                                if res:
                                    $ farmed = True
                                
                                if text1:
                                    play sound s_hmm
                                    gizel normal "[text1]"

                            "Nevermind":
                                $ enough_beds = False
                                $ farmed = False

                    if enough_beds or farmed:
                        jump headhunter_buy
                    label headhunter_no_room:
                        play sound s_woman_scream
                        show headhunter angry at truecenter with dissolve
                        headhunter "Arr, you can't hold the the booty!" 
                        $ slavery_default_string = "leave her."
                        if renpy.call_screen("yes_no", "Do you want to leave the girl with the hunter? She won't be happy about it, but otherwise you will pay the finder's fee of [finder_payment_str] and she is sent to the Slave Market? Currently: " + slavery_default_string):
                            $ slavery_default = 1
                        else:
                            $ slavery_default = 0
                        if slavery_default:
                            jump headhunter_charges
                        else:
                            jump headhunter_release
            else:
                play sound s_woman_scream
                show headhunter angry at truecenter with dissolve
                headhunter "Are you tryin' to cheat me, cap'n?"
                label headhunter_charges:
                $ game.headhunter_price = min(1.05 * game.headhunter_price, game.headhunter_girl.get_price("buy") * 100)
                $ game.headhunter_time = 1
                play sound s_evil_laugh
                show headhunter at truecenter with dissolve
                headhunter "I'll be back t'morrow, and charge for her room and board!"
                hide headhunter with dissolve
                $ game.headhunter_button_enabled = 0
                jump headhunter_end2


label headhunter_end:

    $ game.interacting_with_headhunter = 0

    $ selected_girl = None
    hide screen girl_stats
    hide screen girl_profile

    jump slavemarket

label headhunter_end2:

    $ game.interacting_with_headhunter = 0

    $ selected_girl = None
    hide screen girl_stats
    hide screen girl_profile

    jump main


label headhunter_make_input_dict(making_name):

    $ new_path = get_real_girlpath(making_name)

#    $ renpy.say("", "Making dict for " + making_name)

    python:
        try:
            input_dict = defaultdict(list)
            input_dict = read_init_file(new_path + "/_BK.ini")
        except:
            input_dict = defaultdict(list)

    $ input_dict["path"] = new_path

    if making_name == "Nobody specific":
        $ input_dict["identity/first_name"] = None
        $ input_dict["identity/last_name"] = None
#    else:
#        $ namelist = making_name.split()
#        if len(namelist) >= 1:
#            $ input_dict["identity/first_name"] = namelist[0]
#        if len(namelist) >= 2:
#            $ input_dict["identity/last_name"] = ''.join(namelist[1:])

    $ input_dict["cloning options/keep_skills"] = True
    $ input_dict["cloning options/keep_traits"] = True
    $ input_dict["cloning options/keep_personality"] = True
    $ input_dict["cloning options/keep_sex"] = True

    if not input_dict["cloning options/unique"]:
        $ input_dict["cloning options/unique"] = headhunted_original
    if not input_dict["base skills/Beauty"]:
        $ input_dict["base skills/Beauty"] = headhunted_beauty
    elif isinstance(input_dict["base skills/Beauty"], int):
        $ input_dict["base skills/Beauty"] = max(input_dict["base skills/Beauty"], headhunted_beauty)
    if not input_dict["base skills/Body"]:
        $ input_dict["base skills/Body"] = headhunted_body
    elif isinstance(input_dict["base skills/Body"], int):
        $ input_dict["base skills/Body"] = max(input_dict["base skills/Body"], headhunted_body)
    if not input_dict["base skills/Charm"]:
        $ input_dict["base skills/Charm"] = headhunted_charm
    elif isinstance(input_dict["base skills/Charm"], int):
        $ input_dict["base skills/Charm"] = max(input_dict["base skills/Charm"], headhunted_charm)
    if not input_dict["base skills/Refinement"]:
        $ input_dict["base skills/Refinement"] = headhunted_refinement
    elif isinstance(input_dict["base skills/Refinement"], int):
        $ input_dict["base skills/Refinement"] = max(input_dict["base skills/Refinement"], headhunted_refinement)
    if not input_dict["base skills/Sensitivity"]:
        $ input_dict["base skills/Sensitivity"] = headhunted_sensitivity
    elif isinstance(input_dict["base skills/Sensitivity"], int):
        $ input_dict["base skills/Sensitivity"] = max(input_dict["base skills/Sensitivity"], headhunted_sensitivity)
    if not input_dict["base skills/Libido"]:
        $ input_dict["base skills/Libido"] = headhunted_libido
    elif isinstance(input_dict["base skills/Libido"], int):
        $ input_dict["base skills/Libido"] = max(input_dict["base skills/Libido"], headhunted_libido)
    if not input_dict["base skills/Constitution"]:
        $ input_dict["base skills/Constitution"] = headhunted_constitution
    elif isinstance(input_dict["base skills/Constitution"], int):
        $ input_dict["base skills/Constitution"] = max(input_dict["base skills/Constitution"], headhunted_constitution)
    if not input_dict["base skills/Obedience"]:
        $ input_dict["base skills/Obedience"] = headhunted_obedience
    elif isinstance(input_dict["base skills/Obedience"], int):
        $ input_dict["base skills/Obedience"] = max(input_dict["base skills/Obedience"], headhunted_obedience)                    
    if not input_dict["base positive traits/always"]:
        $ input_dict["base positive traits/always"] = headhunted_pos_traits
    else:
        $ input_dict["base positive traits/always"] += headhunted_pos_traits
    if not input_dict["base negative traits/always"]:
        $ input_dict["base negative traits/always"] = headhunted_neg_traits
    else:
        $ input_dict["base negative traits/always"] += headhunted_neg_traits
    if not input_dict["base personality/always"]:
        $ input_dict["base personality/always"] = headhunted_personality2
    if not input_dict["sexual preferences/favorite_acts"]:
        $ input_dict["sexual preferences/favorite_acts"] = headhunted_favorite_acts
    else:
        $ input_dict["sexual preferences/favorite_acts"] += headhunted_favorite_acts
    if not input_dict["sexual preferences/disliked_acts"]:
        $ input_dict["sexual preferences/disliked_acts"] = headhunted_disliked_acts
    else:
        $ input_dict["sexual preferences/disliked_acts"] += headhunted_disliked_acts
    if not input_dict["sexual preferences/always_fixations"]:
        $ input_dict["sexual preferences/always_fixations"] = headhunted_favorite_fixations
    else:
        $ input_dict["sexual preferences/always_fixations"] += headhunted_favorite_fixations
    if not input_dict["sexual preferences/favorite_fixations"]:
        $ input_dict["sexual preferences/favorite_fixations"] = headhunted_favorite_fixations
    else:
        $ input_dict["sexual preferences/favorite_fixations"] += headhunted_favorite_fixations
    if not input_dict["sexual preferences/disliked_fixations"]:
        $ input_dict["sexual preferences/disliked_fixations"] = headhunted_disliked_fixations
    else:
        $ input_dict["sexual preferences/disliked_fixations"] += headhunted_disliked_fixations
    if not input_dict["sexual preferences/sexual_experience"]:
        $ input_dict["sexual preferences/sexual_experience"] = sex_exp_list[headhunted_sexual_experience]
    if not input_dict["sexual preferences/farm_weakness"]:
        $ input_dict["sexual preferences/farm_weakness"] = headhunted_farm_weakness

    return

label make_hhgirl(making_name):

    $ new_path = get_real_girlpath(making_name)

    if headhunted_rank != int(headhunted_rank):
#        $ renpy.say("", "Making " + making_name + ", path dict " + input_dict["path"] + ", path " + new_path)
        $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = new_path, g_rank = int(headhunted_rank))
        $ attempts_make_hhgirl = 0
        while len(g_list) < 1 and attempts_make_hhgirl < 100:
            $ attempts_make_hhgirl += 1
#            $ renpy.say("", "Making " + making_name + ", path dict " + input_dict["path"] + ", path " + new_path)
            $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = new_path, g_rank = int(headhunted_rank))
        if len(g_list) >= 1:
            $ hhgirl = g_list[0]
        else:
            $ hhgirl = None
    else:
#        $ renpy.say("", "Making " + making_name + ", path dict " + input_dict["path"] + ", path " + new_path)
        $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = new_path, g_rank = int(headhunted_rank))
        $ attempts_make_hhgirl = 0
        while len(g_list) < 1 and attempts_make_hhgirl < 100:
            $ attempts_make_hhgirl += 1
#            $ renpy.say("", "Making " + making_name + ", path dict " + input_dict["path"] + ", path " + new_path)
            $ g_list = get_girls_hh(1, free = game.headhunter_free, init_dict = input_dict, path = new_path, g_rank = int(headhunted_rank))
        if len(g_list) >= 1:
            $ hhgirl = g_list[0]
        else:
            $ hhgirl = None

    if hhgirl:
#        $ name_pair = get_name(hhgirl.path)
#        $ hhgirl.init_dict["identity/first_name"] = name_pair[0]
#        $ hhgirl.init_dict["identity/last_name"] = name_pair[1]
        $ hhgirl.set_name()
        $ hhgirl.traits = [x for x in hhgirl.traits if not trait_dict[x.name] in gold_traits + pos_traits + neg_traits] + [x for x in hhgirl.traits if trait_dict[x.name] in gold_traits] + [x for x in hhgirl.traits if trait_dict[x.name] in pos_traits] + [x for x in hhgirl.traits if trait_dict[x.name] in neg_traits]

    return
