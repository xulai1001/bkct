## KING'S WAY 2.0
## created by MonkOne (v1.5)
## edited by Kite80 (v2.0), small edits by Darkmind (v2.01)
## compatible with Brothel King 0.2 beta

init -1 python:
    def cheat_max_en():
        for girl in MC.girls:
            girl.energy = girl.get_stat_minmax("energy")[1]
            girl.heal(99)
        for girl in farm.girls:
            girl.energy = girl.get_stat_minmax("energy")[1]
            girl.heal(99)
    def cheat_building_duration():
        for bd in all_furniture:
            bd.duration = 0
    def refresh_market():
        slavemarket.girls = [] # Empties slavemarket to get another chance at generating an original girl
        slavemarket.girls = get_girls(60)
    
    def KW_update_shop(context):
        if (context == "city_merchant"):
            # City merchants
            for merc in city_merchants:
                
                merc.items = []
                
                shop_mix = [
                ("F", dice(3)),
                ("junk", dice(6)),
                ("common", dice(6)+2),
                ("rare", dice(3)+1),
                ("exceptional", dice(3)-1)
                ]
                
                for quality, number in shop_mix:
                    for i in range(number):
                        it = get_rand_item(quality, item_types=merc.item_types)
                        if it:
                            merc.items.append(it)
                        elif quality != "junk": # Avoids incomplete inventory if all available items are junk
                            it = get_rand_item("junk", item_types=merc.item_types)
                            if it:
                                merc.items.append(it)
                    
                    merc.items.sort(key=lambda x: x.price)
                    
        elif (context == "minion_merchant"):
            # Minion merchants
                    
            #        for merc in (stallion_merchant, beast_merchant, monster_merchant, machine_merchant):
                    
            NPC_stella.items = get_rand_minion("stallion", nb=dice(5))
            NPC_goldie.items = get_rand_minion("beast", nb=dice(5))
            NPC_willow.items = get_rand_minion("monster", nb=dice(5))
            NPC_gina.items = get_rand_minion("machine", nb=dice(3))
            
            for i in xrange(dice(4)-1):
                NPC_stella.items.append(get_rand_item(rank="M"))
                NPC_goldie.items.append(get_rand_item(rank="M"))
                NPC_willow.items.append(get_rand_item(rank="M"))
                NPC_gina.items.append(get_rand_item(rank="M"))
            
            if NPC_gina.flags["extractor1 unlock"]:
                if dice(6) >= 4:
                    NPC_gina.items.append(extractor_items["extractor1"])
                    
            if NPC_gina.flags["extractor2 unlock"]:
                if dice(6) >= 5:
                    NPC_gina.items.append(extractor_items["extractor2"])
        else:
            # Item shop
            
            shop.items = []
            
            shop_mix = [
                ("F", dice(3)+1),
                ("junk", dice(3)+3),
                ("common", dice(6)),
                ("rare", dice(3)),
                ("exceptional", dice(3)-2)
                ]
            
            for quality, number in shop_mix:
                for i in xrange(number):
                    it = get_rand_item(quality)
                    shop.items.append(it)
        
        shop.items.sort(key=lambda x: x.price)
    def KW_update_shop_plus(): 
        # Item shop
        
        shop.items = []
        
        shop_mix = [
            ("F", KW_Shop_Flower),
            ("junk", KW_Shop_Junk),
            ("common", KW_Shop_Common),
            ("rare", KW_Shop_Rare),
            ("exceptional", KW_Shop_Exce)
            ]
        
        for quality, number in shop_mix:
            for i in xrange(number):
                it = get_rand_item(quality)
                shop.items.append(it)
#                shop.items.append(get_rand_item("F"))
         
        shop.items.sort(key=lambda x: x.price)

    def KW_update_slave():
        slavemarket.girls = []
        slavemarket.girls = get_girls(KW_Slave)
        return
        
    def KW_reset_free_girl():
        game.free_girls = []
        update_free_girls()
        cycle_free_girls()
        
    def KW_safe_remove_fix(slave_id,fix):
        slave_id.remove_fixation(fix)

    def KW_safe_add_pos_fix(slave_id,fix):
        slave_id.pos_fixations += [fix_dict[fix]]

    def KW_safe_add_neg_fix(slave_id,fix):
        slave_id.add_random_fixation(fixation=fix, type="neg")



    kingsway_template = Mod(
        
                ## Basic mod information (Important: Version is used to check for new versions of the mod. Failure to update the version number may lead to broken mods and saved games)
                name = "国王特权",
                folder = "King's Way",
                creator = "Monk One & Kite80",
                version = 2.02,
#                pic = "KWtitle.webm",
                description = """适用于青楼之王0.2版本的省肝的作弊工具""",
                
                ## Mod option menu (access through the Help (click on '?') menu)
                help_prompts = [("显示菜单按钮", "KW_showcheatbox"), ("隐藏菜单按钮", "KW_hidecheatbox")],
                
                ## Init label: This will run when the mod is activated, allowing you to set some variables and events if necessary
                init_label = "kingsway_init",
                
                ## Event dictionary (all mod events must be declared here)
                )
    
## This label runs when the mod is activated
label kingsway_init():
    
    style cheat_button:
        is default
#        background None
        background "#1117"
        xpadding 0
        size res_font(10)
        idle_color "#559"
        hover_color "#ccf"
        selected_idle_color "#aa0"
        selected_hover_color "#ff9"
        insensitive_color "#2486" 



    ## Important! It is necessary to copy the mod template to a variable upon initializing it if you would like mod variables to save together with the player's saved game (ie. most cases)
    $ kingsway = kingsway_template
    
    default cheat_menu = "mainc"
    default slave_id = ""
    default trait_desc = ""
    default KW_Show = False
    default KWFreeGInt = False
    default KWInfInt = False
    default KWInfPow = False
    default KW_Widget_x = 99.0
    default KW_Widget_y = 3.0
    default KW_Shop_Flower = 2
    default KW_Shop_Junk = 3
    default KW_Shop_Common = 3
    default KW_Shop_Rare = 3
    default KW_Shop_Exce = 3
    default KW_Slave = 12

    default KW_paging = 0

    #$ config.overlay_screens.append('cheat_box')
    "国王特权模组已激活!"
    
    "要显示作弊控制按钮，请按照：右上角的帮助菜单——>模组——>显示作弊按钮的顺序依次点击。"
    
    "当本模组激活时，您可以按“展开”键打开作弊菜单。"
    
    return
    
label KW_showcheatbox():
    show screen cheat_box
    return

label KW_hidecheatbox():
    hide screen cheat_box
    return
    
screen cheat_box:
    key "K_KP_PLUS" action Show('cheat_main')
    zorder 100

    if KWInfPow:
        $ MC.interactions = MC.get_speed()

    hbox:
        xalign KW_Widget_x/100.0
        yalign KW_Widget_y/100.0
        if KW_Show:
            textbutton "隐藏" action SetVariable("KW_Show",False)  text_size 16
        else:
            textbutton "展开" action SetVariable("KW_Show",True)  text_size 16
        if KW_Show:
            textbutton "作弊菜单" action Show("cheat_main")  text_size 16
            textbutton "恢复互动次数" action SetField(MC,"interactions",MC.get_speed())  text_size 16
            textbutton "恢复魔力" action SetField(MC,"mana",MC.get_spirit() * MC.get_effect("boost", "mana") + MC.get_effect("change", "mana"))  text_size 16
            textbutton "恢复体力" action Function(cheat_max_en)  text_size 16
            textbutton "恢复女孩们的精力" action Function(cheat_max_en)  text_size 16
            if (renpy.get_screen("free_girl_interact")):
                #text "in free_girl_interact"
                if KWFreeGInt:
                    $ girl.MC_interact_counters = defaultdict(int)
            if (renpy.get_screen("girl_interact")):
                #text "in girl_interact"
                if KWInfInt:
                    $ girl.MC_interact_counters = defaultdict(int)
    if KW_Show:
        vbox:
            xalign 0.0
            yalign 1.0
            if (renpy.get_screen("item_tab")):
#                if (renpy.get_screen("item_tab").scope["context"] == "shop"):
                    #text "in shop"
                textbutton "刷新杂货铺" action Function(KW_update_shop,"shop") text_size 16
                textbutton "刷新杂货铺+" action Function(KW_update_shop_plus) text_size 16
#                if (renpy.get_screen("item_tab").scope["context"] == "minion_merchant"):
                    #text "in minion_merchant"
                textbutton "刷新仆从商店" action Function(KW_update_shop,"minion_merchant") text_size 16
#                if (renpy.get_screen("item_tab").scope["context"] == "city_merchant"):
                    #text "in city_merchant"
                textbutton "刷新城市商店" action Function(KW_update_shop,"city_merchant") text_size 16
            #text "in slave market"            
#            if (renpy.get_screen("girl_tab")):
#                if (renpy.get_screen("girl_tab").scope["context"] == "slavemarket"):   #two layer of If is required, other wise it'll crash when outside of slave market
            textbutton "刷新奴隶市场 全部" action [renpy.curried_invoke_in_new_context(refresh_market),SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "slavemarket"), Jump("teleport")] text_size 18
            textbutton "刷新奴隶市场 默认" action [renpy.curried_invoke_in_new_context(update_slaves),SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "slavemarket"), Jump("teleport")] text_size 18 ##teleport player to slavemarket again to make girl screen update
            textbutton "刷新奴隶市场 更多" action [renpy.curried_invoke_in_new_context(KW_update_slave),SetVariable("choice_menu_girl_interact", False), SetVariable("selected_destination", "slavemarket"), Jump("teleport")] text_size 18


screen cheat_main():
    modal True
    frame:
#        background '#aace'
        background '#333a'
        xfill True
        yfill True
        has vbox
        hbox:
            hbox:
                xalign 0.0
                textbutton '关闭' action Hide('cheat_main') text_size 16
                textbutton "主角设置" action SetVariable("cheat_menu", "mainc") text_size 16
                textbutton "女孩编辑器" action [SetVariable("cheat_menu", "slave"),SetVariable("slave_id", "")] text_size 16
                textbutton "模组设置" action SetVariable("cheat_menu", "option") text_size 16
            hbox:
                xcenter 2.0
                if cheat_menu == "slave":
                    $ KW_paging_page_length = 20
                    $ KW_paging_max = len(gold_traits+pos_traits+neg_traits+list(fix_dict.values()))//KW_paging_page_length
                    textbutton "上一页" action SetVariable("KW_paging", max(KW_paging-1,0)) xalign 0.9
                    textbutton "下一页" action SetVariable("KW_paging", min(KW_paging+1,KW_paging_max)) xalign 0.7
        if cheat_menu == "option":
            use KW_Options
        elif cheat_menu == "slave":
            if slave_id == "":
                use cheat_all_slave
            else:
                use cheat_slave_edit
        else :
            use MCCheat
                
screen cheat_all_slave:
    #text "cheat_all_slave"
    hbox:
        vbox:
            xsize 400
            text '青楼女孩'
            vpgrid:
                cols 1
                xfill True
                mousewheel True
                scrollbars "vertical"
                spacing 0
                for girl in MC.girls:
                    textbutton "{}".format(girl.get_name()) action SetVariable("slave_id",girl) xfill True
        vbox:
            xsize 400
            text '农场女孩'
            vpgrid:
                cols 1
                xfill True
                mousewheel True
                scrollbars "vertical"
                spacing 0
                for girl in farm.girls:
                    textbutton "{}".format(girl.get_name()) action SetVariable("slave_id",girl) xfill True
        vbox:
            xsize 400
            text '自由女孩'
            vpgrid:
                cols 1
                xfill True
                mousewheel True
                scrollbars "vertical"
                spacing 0
                for girl in game.free_girls:
                    textbutton "{}".format(girl.get_name()) action SetVariable("slave_id",girl) xfill True text_layout "nobreak" tooltip __("Love") + str_int(girl.love) + __("Fear") + str_int(girl.fear) + __("Energy") + str_int(girl.energy)

screen KW_Options():
    vbox:
        text "按钮位置:" color "#33cccc"
        hbox:
            text "横坐标"
            bar:
                xsize 200
                value VariableValue("KW_Widget_x",100)
            text "{}".format(KW_Widget_x/100.0)
        hbox:
            text "纵坐标"
            bar:
                xsize 200
                value VariableValue("KW_Widget_y",100)
            text "{}".format(KW_Widget_y/100.0)

        text "————————————————————"

        text "💰修改奴隶市场奴隶数量" color "#33cccc"
        hbox:
            style_group "cheat"
            text "奴隶数量: {}".format(KW_Slave)
            textbutton " -5 " action SetVariable("KW_Slave",max(KW_Slave-5,6))
            textbutton " -1 " action SetVariable("KW_Slave",max(KW_Slave-1,6))
            textbutton " +1 " action SetVariable("KW_Slave",KW_Slave+1)
            textbutton " +5 " action SetVariable("KW_Slave",KW_Slave+5)

        text "————————————————————"

        text "🎁修改商店商品数量" color "#33cccc"
        hbox:
            style_group "cheat"
            text "次品数量: {}".format(KW_Shop_Junk)
            text "个 "
            textbutton " -5 " action SetVariable("KW_Shop_Junk",max(KW_Shop_Junk-5,0))
            textbutton " -1 " action SetVariable("KW_Shop_Junk",max(KW_Shop_Junk-1,0))
            textbutton " +1 " action SetVariable("KW_Shop_Junk",KW_Shop_Junk+1)
            textbutton " +5 " action SetVariable("KW_Shop_Junk",KW_Shop_Junk+5)
        hbox:
            style_group "cheat"
            text "凡品数量: {}".format(KW_Shop_Common)
            text "个 "
            textbutton " -5 " action SetVariable("KW_Shop_Common",max(KW_Shop_Common-5,0))
            textbutton " -1 " action SetVariable("KW_Shop_Common",max(KW_Shop_Common-1,0))
            textbutton " +1 " action SetVariable("KW_Shop_Common",KW_Shop_Common+1)
            textbutton " +5 " action SetVariable("KW_Shop_Common",KW_Shop_Common+5)
        hbox:
            style_group "cheat"
            text "珍品数量: {}".format(KW_Shop_Rare)
            text "个 "
            textbutton " -5 " action SetVariable("KW_Shop_Rare",max(KW_Shop_Rare-5,0))
            textbutton " -1 " action SetVariable("KW_Shop_Rare",max(KW_Shop_Rare-1,0))
            textbutton " +1 " action SetVariable("KW_Shop_Rare",KW_Shop_Rare+1)
            textbutton " +5 " action SetVariable("KW_Shop_Rare",KW_Shop_Rare+5)
        hbox:
            style_group "cheat"
            text "传说数量: {}".format(KW_Shop_Exce)
            text "个 "
            textbutton " -5 " action SetVariable("KW_Shop_Exce",max(KW_Shop_Exce-5,0))
            textbutton " -1 " action SetVariable("KW_Shop_Exce",max(KW_Shop_Exce-1,0))
            textbutton " +1 " action SetVariable("KW_Shop_Exce",KW_Shop_Exce+1)
            textbutton " +5 " action SetVariable("KW_Shop_Exce",KW_Shop_Exce+5)
#        hbox:
#            textbutton "X reset items X" action Function(init_items) text_size 6
        ###############
        text "————————————————————"

        text "🛏卧室上限:"
        hbox:
            hbox:
                xsize 110
                text "{size=25}主线章节{/size}"
            hbox:
                xsize 125 
                text "第一章"
            hbox:
                xsize 125
                text "第二章"
            hbox:
                xsize 125
                text "第三章"
            hbox:
                xsize 125
                text "第四章"
            hbox:
                xsize 125
                text "第五章"
            hbox:
                xsize 125
                text "第六章"
            hbox:
                xsize 125
                text "第七章"
        hbox:
            hbox:
                xsize 110
                text "{size=25}初始数量{/size}"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[1][0]) color c_white
                text "间"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[2][0]) color c_emerald
                text "间"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[3][0]) color c_crimson
                text "间"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[4][0]) color c_emerald
                text "间"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[5][0]) color c_crimson
                text "间"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[6][0]) color c_emerald
                text "间"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[7][0]) color c_crimson
                text "间"
        hbox:
            hbox:
                xsize 110
                text "{size=25}修改上限{/size}"
            hbox:
                xsize 125
                text "{}".format(bro_capacity[1][1]) color c_emerald
                textbutton "➖" action [SetDict(bro_capacity[1],1,max(bro_capacity[1][1]-1,bro_capacity[1][0])),SetDict(bro_capacity[2],0,max(bro_capacity[1][1]-1,bro_capacity[1][0]))] text_size 14 
                textbutton "➕" action [SetDict(bro_capacity[1],1,min(bro_capacity[1][1]+1,bro_capacity[2][1])),SetDict(bro_capacity[2],0,min(bro_capacity[1][1]+1,bro_capacity[2][1]))] text_size 14 
            hbox:
                xsize 125
                text "{}".format(bro_capacity[2][1]) color c_crimson
                textbutton "➖" action [SetDict(bro_capacity[2],1,max(bro_capacity[2][1]-1,bro_capacity[2][0])),SetDict(bro_capacity[3],0,max(bro_capacity[2][1]-1,bro_capacity[2][0]))] text_size 14 
                textbutton "➕" action [SetDict(bro_capacity[2],1,min(bro_capacity[2][1]+1,bro_capacity[3][1])),SetDict(bro_capacity[3],0,min(bro_capacity[2][1]+1,bro_capacity[3][1]))] text_size 14 
            hbox:
                xsize 125
                text "{}".format(bro_capacity[3][1]) color c_emerald
                textbutton "➖" action [SetDict(bro_capacity[3],1,max(bro_capacity[3][1]-1,bro_capacity[3][0])),SetDict(bro_capacity[4],0,max(bro_capacity[3][1]-1,bro_capacity[3][0]))] text_size 14 
                textbutton "➕" action [SetDict(bro_capacity[3],1,min(bro_capacity[3][1]+1,bro_capacity[4][1])),SetDict(bro_capacity[4],0,min(bro_capacity[3][1]+1,bro_capacity[4][1]))] text_size 14 
            hbox:
                xsize 125
                text "{}".format(bro_capacity[4][1]) color c_crimson
                textbutton "➖" action [SetDict(bro_capacity[4],1,max(bro_capacity[4][1]-1,bro_capacity[4][0])),SetDict(bro_capacity[5],0,max(bro_capacity[4][1]-1,bro_capacity[4][0]))] text_size 14 
                textbutton "➕" action [SetDict(bro_capacity[4],1,min(bro_capacity[4][1]+1,bro_capacity[5][1])),SetDict(bro_capacity[5],0,min(bro_capacity[4][1]+1,bro_capacity[5][1]))] text_size 14 
            hbox:
                xsize 125
                text "{}".format(bro_capacity[5][1]) color c_emerald
                textbutton "➖" action [SetDict(bro_capacity[5],1,max(bro_capacity[5][1]-1,bro_capacity[5][0])),SetDict(bro_capacity[6],0,max(bro_capacity[5][1]-1,bro_capacity[5][0]))] text_size 14 
                textbutton "➕" action [SetDict(bro_capacity[5],1,min(bro_capacity[5][1]+1,bro_capacity[6][1])),SetDict(bro_capacity[6],0,min(bro_capacity[5][1]+1,bro_capacity[6][1]))] text_size 14 
            hbox:
                xsize 125
                text "{}".format(bro_capacity[6][1]) color c_crimson
                textbutton "➖" action [SetDict(bro_capacity[6],1,max(bro_capacity[6][1]-1,bro_capacity[6][0])),SetDict(bro_capacity[7],0,max(bro_capacity[6][1]-1,bro_capacity[6][0]))] text_size 14 
                textbutton "➕" action [SetDict(bro_capacity[6],1,min(bro_capacity[6][1]+1,bro_capacity[7][1])),SetDict(bro_capacity[7],0,min(bro_capacity[6][1]+1,bro_capacity[7][1]))] text_size 14 
            hbox:
                xsize 125
                text "{}".format(bro_capacity[7][1]) color c_white
                textbutton "➖" action SetDict(bro_capacity[7],1,bro_capacity[7][1]-1) text_size 14 
                textbutton "➕" action SetDict(bro_capacity[7],1,bro_capacity[7][1]+1) text_size 14 
        
        text "————————————————————"
        
        textbutton "刷新女孩（删除城里的自由女孩，并创建新的自由女孩）" action renpy.curried_invoke_in_new_context(KW_reset_free_girl) text_size 22

                            
screen MCCheat:
    vbox:
        hbox:
            style_group "cheat"
            text "{size=20}调整声望{/size} "
            textbutton "{size=16}-1000{/size}" action SetField(MC,"prestige",MC.prestige -1000)
            textbutton "{size=16} -100{/size}" action SetField(MC,"prestige",MC.prestige -100)
            textbutton "{size=16} -10{/size}" action SetField(MC,"prestige",MC.prestige -10)
            text "{size=20} [MC.prestige] {/size}"
            textbutton "{size=16}+10{/size}" action SetField(MC,"prestige",MC.prestige +10)
            textbutton "{size=16} +100{/size}" action SetField(MC,"prestige",MC.prestige +100)
            textbutton "{size=16} +1000{/size}" action SetField(MC,"prestige",MC.prestige +1000)
        hbox:
            style_group "cheat"
            text "{size=20}修改属性点{/size}"
            textbutton "{size=16}-10{/size}" action SetField(MC,"skill_points",MC.skill_points -10)
            textbutton "{size=16} -1{/size}" action SetField(MC,"skill_points",MC.skill_points -1)
            text "{size=20} [MC.skill_points] {/size}"
            textbutton "{size=16}+1{/size}" action SetField(MC,"skill_points",MC.skill_points +1)
            textbutton "{size=16} +10{/size}" action SetField(MC,"skill_points",MC.skill_points +10)
        hbox:
            style_group "cheat"
            text "{size=20}修改行动力{/size}"
            textbutton "{size=16}-10{/size}" action SetField(MC,"interactions",MC.interactions -10)
            textbutton "{size=16} -1{/size}" action SetField(MC,"interactions",MC.interactions -1)
            text "{size=20} [MC.interactions] {/size}"
            textbutton "{size=16}+1{/size}" action SetField(MC,"interactions",MC.interactions +1)
            textbutton "{size=16} +10{/size}" action SetField(MC,"interactions",MC.interactions +10)
        hbox:
            text "{size=20}修改金币{/size}"
            textbutton " -10000 " action SetField(MC,"gold",MC.gold -10000) text_size 16
            textbutton "  -100  " action SetField(MC,"gold",MC.gold -100) text_size 16
            text "{size=20} 现有：[MC.gold] {/size}" 
            textbutton "  +500  " action SetField(MC,"gold",MC.gold +500) text_size 16
            textbutton " +10000 " action SetField(MC,"gold",MC.gold +10000) text_size 16
            textbutton " +250000" action SetField(MC,"gold",MC.gold +250000) text_size 16
            textbutton "+1000000" action SetField(MC,"gold",MC.gold +1000000) text_size 16
        hbox:
            text "{size=20}调整速度上限{/size}" 
            textbutton "-1" action SetField(MC,"speed",MC.speed -1) text_size 16
            text "{size=20} 当前：[MC.speed] {/size}" 
            textbutton "+1" action SetField(MC,"speed",MC.speed +1) text_size 16
            textbutton "+5" action SetField(MC,"speed",MC.speed +5) text_size 16
        hbox:
            text "{size=20}调整魔力上限{/size}"
            textbutton "-10" action SetField(MC,"spirit",MC.spirit -10) text_size 16
            textbutton "-1" action SetField(MC,"spirit",MC.spirit -1) text_size 16
            text "{size=20} 当前：[MC.spirit] {/size}" 
            textbutton "+10" action SetField(MC,"spirit",MC.spirit +10) text_size 16
            textbutton "+50" action SetField(MC,"spirit",MC.spirit +50) text_size 16
        hbox:
            text "{size=20}调整力量上限{/size}" 
            textbutton "-10" action SetField(MC,"strength",MC.strength -10) text_size 16
            textbutton "-1" action SetField(MC,"strength",MC.strength -1) text_size 16
            text "{size=20} 当前：[MC.strength] {/size}"
            textbutton "+10" action SetField(MC,"strength",MC.strength +10) text_size 16
            textbutton "+50" action SetField(MC,"strength",MC.strength +50) text_size 16
        hbox:
            text "{size=20}青楼威胁等级设置{/size}" 
            textbutton " -1 " action SetField(brothel,"security",brothel.security -1) text_size 16
            text "{size=20} 现在：[brothel.security] {/size}" 
            textbutton " +10" action SetField(brothel,"security",brothel.security +10) text_size 16
            textbutton "+500" action SetField(brothel,"security",brothel.security +500) text_size 16
        text "{size=22}修改资源数量{/size}" color "#33cccc" 
        hbox:
            vbox:
                style_group "cheat"
                ysize 70
                for rs in build_resources:
                    text ("{} "+str(MC.resources[rs])).format(misc_name_dict[rs.capitalize()]) 
            vbox:
                style_group "cheat"
                ysize 50
                for rs in build_resources:
                    textbutton " +10  " action SetDict(MC.resources,rs,MC.resources[rs] + 10)
            vbox:
                style_group "cheat"
                ysize 50
                for rs in build_resources:
                    textbutton " +100 " action SetDict(MC.resources,rs,MC.resources[rs] + 100)
        textbutton "{size=18}快速建造（所有设施都可以立即完成）{/size}" action Function(cheat_building_duration)
        #textbutton "Refill Interaction" action SetField(MC,"interactions",MC.get_speed()) text_size 10
        if KWInfInt:
            textbutton "女孩互动次数有上限" action SetVariable("KWInfInt",False) text_size 18
        else:
            textbutton "女孩互动次数无上限" action SetVariable("KWInfInt",True) text_size 18
        if KWFreeGInt:
            textbutton "自由女孩互动次数有上限" action SetVariable("KWFreeGInt",False) text_size 18
        else:
            textbutton "自由女孩互动次数无上限" action SetVariable("KWFreeGInt",True) text_size 18
        if KWInfPow:
            #$ MC.interactions = MC.get_speed()
            textbutton "主角互动不消耗行动力" action SetVariable("KWInfPow",False) text_size 18
        else:
            textbutton "主角互动消耗行动力" action SetVariable("KWInfPow",True) text_size 18
        textbutton _("{size=18}{alpha=0.9}获取特定道具{/alpha}{/size}") action [ ui.callsinnewcontext("InvHacks") ]





screen cheat_slave_edit:
    #text "cheat_slave_edit"
    hbox:
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            xfill True
            yfill True
            xsize 0.6
            spacing 1
            has vbox
            hbox:
                text "{size=30}女 孩：[slave_id.fullname]{/size}"
            if slave_id in game.free_girls:
                hbox:
                    $ slave_id.location_cn = tl_cn(slave_id.location, location_name_dict)
                    text "{size=30}位 置: [slave_id.location_cn]{/size}"
            hbox:
                text "{size=30}等 级{/size}"
                textbutton "-1级" action SetField(slave_id,"level",slave_id.level -1) text_size 20
                text "[slave_id.level]"
                textbutton "+1级" action SetField(slave_id,"level",slave_id.level +1) text_size 20
                textbutton "提升等级" action Function(slave_id.level_up, forced = True) text_size 20
            hbox:
                text "{size=30}人 气{/size}"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "rep", slave_id.get_rep_cap())
                text "[slave_id.rep]"
                textbutton "最大值" action SetField(slave_id,"rep",slave_id.get_rep_cap()) text_size 20
            hbox:
                text "{size=30}经 验{/size}"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "xp", slave_id.get_xp_cap())
                text "[slave_id.xp]"
                textbutton "最大值" action SetField(slave_id,"xp",slave_id.get_xp_cap()) text_size 20
            hbox:
                text "{size=32}天赋点{/size}" layout "nobreak"
                textbutton "-1" action SetField(slave_id,"perk_points",slave_id.perk_points -1) text_size 20
                textbutton "[slave_id.perk_points]" action SetField(slave_id,"perk_points",0) text_size 20
                textbutton "+1" action SetField(slave_id,"perk_points",slave_id.perk_points +1) text_size 20
                textbutton "+10" action SetField(slave_id,"perk_points",slave_id.perk_points +10) text_size 20

            text "————————————————————"
            text ' 🧬主要属性' layout "nobreak" color "#33cccc"
            hbox:
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        $ stat.name_cn = tl_cn(stat.name, girl_related_dict)
                        text "{size=26}[stat.name_cn]{/size}"
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        bar:
                            xsize 200
                            value FieldValue(stat, "value", slave_id.get_stat_minmax(stat.name)[1])
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        text "{size=26}[stat.value]{/size}"
                vbox:
                    ysize 300
                    for stat in slave_id.stats:
                        textbutton "最大" action SetField(stat,"value",slave_id.get_stat_minmax(stat.name)[1]) text_size 12
            hbox:
                text "{size=26}精力{/size}" layout "nobreak" 
                bar:
                    xsize 200
                    value FieldValue(slave_id, "energy", slave_id.get_stat_minmax("energy")[1])
                text "{size=26}[slave_id.energy]{/size}" layout "nobreak"
                textbutton "最大" action SetField(slave_id,"energy",slave_id.get_stat_minmax("energy")[1]) text_size 12
            text ' 💝性技熟练度' layout "nobreak" color "#33cccc"
            
            hbox:
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        $ stat.name_cn = tl_cn(stat.name, girl_related_dict)
                        text "{size=26}[stat.name_cn]{/size}"
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        bar:
                            xsize 200
                            value FieldValue(stat, "value", slave_id.get_stat_minmax(stat.name)[1])
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        text "{size=26}[stat.value]{/size}"
                vbox:
                    ysize 120
                    for stat in slave_id.sex_stats:
                        textbutton "最大值" action SetField(stat,"value",slave_id.get_stat_minmax(stat.name)[1]) text_size 10

            text "————————————————————"   
            text ' 😀情 绪' layout "nobreak" color "#33cccc"
            hbox:
                text "{size=26}好感度{/size}"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "love", 250, offset=-125)
                text "[slave_id.love]"
                textbutton "最大值" action SetField(slave_id,"love",125) text_size 16
            hbox:
                text "{size=26}恐惧值{/size}"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "fear", 200, offset=-100)
                text "[slave_id.fear]"
                textbutton "最大值" action SetField(slave_id,"fear",100) text_size 16
            hbox:
                text "{size=26}心 情{/size}"
                bar:
                    xsize 200
                    value FieldValue(slave_id, "mood", 200, offset=-100)
                text "[slave_id.mood]"
                textbutton "最大值" action SetField(slave_id,"mood",100) text_size 16
            if slave_id.personality_unlock["origin"]:
                textbutton '{}'.format(slave_id.origin.capitalize()) action ToggleDict(slave_id.personality_unlock, "origin") text_layout "nobreak"
            else:
                textbutton '揭露背景故事' action ToggleDict(slave_id.personality_unlock, "origin") text_layout "nobreak"
            text ' 🔍揭露品味' layout "nobreak" color "#33cccc"
            if slave_id.personality_unlock["fav_color"]:
                textbutton '{}'.format(slave_id.likes["color"].capitalize()) action ToggleDict(slave_id.personality_unlock, "fav_color") text_layout "nobreak"
            else:
                textbutton '揭露最喜欢的颜色' action ToggleDict(slave_id.personality_unlock, "fav_color") text_layout "nobreak"
            if slave_id.personality_unlock["fav_food"]:
                textbutton '{}'.format(slave_id.likes["food"].capitalize()) action ToggleDict(slave_id.personality_unlock, "fav_food") text_layout "nobreak"
            else:
                textbutton '揭露最喜欢的食物' action ToggleDict(slave_id.personality_unlock, "fav_food") text_layout "nobreak"
            if slave_id.personality_unlock["fav_drink"]:
                textbutton '{}'.format(slave_id.likes["drink"].capitalize()) action ToggleDict(slave_id.personality_unlock, "fav_drink") text_layout "nobreak"
            else:
                textbutton '揭露最喜欢的饮料' action ToggleDict(slave_id.personality_unlock, "fav_drink") text_layout "nobreak"
            if slave_id.personality_unlock["hobby_" + slave_id.hobbies[0]]:
                textbutton '{}'.format(slave_id.hobbies[0].capitalize()) action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[0]) text_layout "nobreak"
            else:
                textbutton '揭露兴趣爱好1' action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[0]) text_layout "nobreak"
            if slave_id.personality_unlock["hobby_" + slave_id.hobbies[1]]:
                textbutton '{}'.format(slave_id.hobbies[1].capitalize()) action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[1]) text_layout "nobreak"
            else:
                textbutton '揭露兴趣爱好2' action ToggleDict(slave_id.personality_unlock, "hobby_" + slave_id.hobbies[1]) text_layout "nobreak"
            if slave_id.personality_unlock["dis_color"]:
                textbutton '{}'.format(slave_id.dislikes["color"].capitalize()) action ToggleDict(slave_id.personality_unlock, "dis_color") text_layout "nobreak"
            else:
                textbutton '揭露最讨厌的颜色' action ToggleDict(slave_id.personality_unlock, "dis_color") text_layout "nobreak"
            if slave_id.personality_unlock["dis_food"]:
                textbutton '{}'.format(slave_id.dislikes["food"].capitalize()) action ToggleDict(slave_id.personality_unlock, "dis_food") text_layout "nobreak"
            else:
                textbutton '揭露最讨厌的食物' action ToggleDict(slave_id.personality_unlock, "dis_food") text_layout "nobreak"
            if slave_id.personality_unlock["dis_drink"]:
                textbutton '{}'.format(slave_id.dislikes["drink"].capitalize()) action ToggleDict(slave_id.personality_unlock, "dis_drink") text_layout "nobreak"
            else:
                textbutton '揭露最讨厌的饮料' action ToggleDict(slave_id.personality_unlock, "dis_drink") text_layout "nobreak"
#                if slave_id.personality_unlock["loves"]:
#                    textbutton '{}'.format(gift_description[slave_id.personality_unlock["loves"]]) action ToggleDict(slave_id.personality_unlock, "loves") text_layout "nobreak"
#                else:
#                    textbutton 'Unlock loves' action ToggleDict(slave_id.personality_unlock, "loves") text_layout "nobreak"
#                if slave_id.personality_unlock["hates"]:
#                    textbutton '{}'.format(gift_description[slave_id.personality_unlock["hates"]]) action ToggleDict(slave_id.personality_unlock, "hates") text_layout "nobreak"
#                else:
#                    textbutton 'Unlock hates' action ToggleDict(slave_id.personality_unlock, "hates") text_layout "nobreak"
#                if slave_id.personality_unlock["likes"]:
#                    textbutton 'Lock likes' action ToggleDict(slave_id.personality_unlock, "likes") text_layout "nobreak"
#                else:
#                    textbutton 'Unlock likes' action ToggleDict(slave_id.personality_unlock, "likes") text_layout "nobreak"
            text "————————————————————"   
            text " 😃个 性" layout "nobreak" color "#33cccc"
            for pt in gpersonalities:
                hbox:
                    text "    -" layout "nobreak"
                    textbutton "{}".format(gpersonalities[pt].name):
                        if (gpersonalities[pt].name == slave_id.personality.name):
                            action NullAction()
                            text_color c_emerald
                        else:
                            action SetField(slave_id,"personality",gpersonalities[pt])
                            text_color c_crimson
                        text_layout "nobreak"
            hbox:
                text "社交" layout "nobreak"
                if (slave_id.personality_unlock["EI"]<100) :
                    textbutton "🔓解 锁" action SetDict(slave_id.personality_unlock,"EI",100) text_size 12
                else:
                    textbutton "🔒锁 定" action SetDict(slave_id.personality_unlock,"EI",0) text_size 12

            hbox:
                text "关心" layout "nobreak"
                if (slave_id.personality_unlock["MI"]<100) :
                    textbutton "🔓解 锁" action SetDict(slave_id.personality_unlock,"MI",100) text_size 12
                else:
                    textbutton "🔒锁 定" action SetDict(slave_id.personality_unlock,"MI",0) text_size 12

            hbox:
                text "支配" layout "nobreak"
                if (slave_id.personality_unlock["DS"]<100) :
                    textbutton "🔓解 锁" action SetDict(slave_id.personality_unlock,"DS",100) text_size 12
                else:
                    textbutton "🔒锁 定" action SetDict(slave_id.personality_unlock,"DS",0) text_size 12
            hbox:
                text "道德" layout "nobreak"
                if (slave_id.personality_unlock["LR"]<100) :
                    textbutton "🔓解 锁" action SetDict(slave_id.personality_unlock,"LR",100) text_size 12
                else:
                    textbutton "🔒锁 定" action SetDict(slave_id.personality_unlock,"LR",0) text_size 12

            text "————————————————————"   
            text ' 性癖设置' layout "nobreak" color "#33cccc"
            text ' 弱 点' layout "nobreak" color c_emerald
            for act in {"naked", "service", "sex", "anal", "fetish", "bisexual", "group"}:
                if act in slave_id.pos_acts:
                    $ act_cn = tl_cn(act, girl_related_dict)
                    textbutton "移除[act_cn]" action RemoveFromSet(slave_id.pos_acts,act) text_layout "nobreak" text_size 20
                else:
                    $ act_cn = tl_cn(act, girl_related_dict)
                    textbutton "添加[act_cn]" action AddToSet(slave_id.pos_acts,act) text_layout "nobreak" text_size 20
            text ' 抗 拒' layout "nobreak" color c_crimson
            for act in {"naked", "service", "sex", "anal", "fetish", "bisexual", "group"}:
                if act in slave_id.neg_acts:
                    $ act_cn = tl_cn(act, girl_related_dict)
                    textbutton "移除[act_cn]" action RemoveFromSet(slave_id.neg_acts,act) text_layout "nobreak" text_size 20
                else:
                    $ act_cn = tl_cn(act, girl_related_dict)
                    textbutton "添加[act_cn]" action AddToSet(slave_id.neg_acts,act) text_layout "nobreak" text_size 20
            text "————————————————————"           
            text ' 性 癖' layout "nobreak" color "#33cccc"
            for act in extended_sex_acts:
                hbox:
                    text girl_related_dict[act.capitalize()]
                    textbutton "最小" action SetDict(slave_id.preferences,act,base_reluctance[act]) text_size 16
                    textbutton "-50" action SetDict(slave_id.preferences,act,slave_id.preferences[act] - 50) text_size 16
                    textbutton "-10" action SetDict(slave_id.preferences,act,slave_id.preferences[act] - 10) text_size 16
                    text preference_color[slave_id.get_preference(act)] % girl_related_dict[slave_id.get_preference(act).capitalize()] layout "nobreak"
                    textbutton "+10" action SetDict(slave_id.preferences,act,slave_id.preferences[act] + 10) text_size 16
                    textbutton "+50" action SetDict(slave_id.preferences,act,slave_id.preferences[act] + 50) text_size 16
                    textbutton "最大" action SetDict(slave_id.preferences,act,-1 * base_reluctance[act]) text_size 16
            text " 正面性癖" color c_emerald
            for kwfix in slave_id.pos_fixations:
                hbox:
                    text "{}:".format(girl_related_dict[kwfix.name.capitalize()])
                    if slave_id.personality_unlock[kwfix.name]:
                        text "解锁的" color c_emerald
                        textbutton "🔒锁 定" text_color c_crimson action SetDict(slave_id.personality_unlock,kwfix.name,0) text_size 16
                    else:
                        text "锁定的" color c_crimson
                        textbutton "🔓解 锁" text_color c_crimson action SetDict(slave_id.personality_unlock,kwfix.name,1) text_size 16
                    textbutton "移除" action Function(KW_safe_remove_fix,slave_id,kwfix.name) text_size 16
            text " 负面性癖" color c_crimson
            for kwfix in slave_id.neg_fixations:
                hbox:
                    text "{}:".format(girl_related_dict[kwfix.name.capitalize()])
                    if slave_id.personality_unlock[kwfix.name]:
                        text "解锁的" color c_emerald
                        textbutton "🔒锁 定" text_color c_crimson action SetDict(slave_id.personality_unlock,kwfix.name,0) text_size 16
                    else:
                        text "锁定的" color c_crimson
                        textbutton "🔓解 锁" text_color c_crimson action SetDict(slave_id.personality_unlock,kwfix.name,100) text_size 16
                    textbutton "移除" action Function(KW_safe_remove_fix,slave_id,kwfix.name) text_size 16
            text "————————————————————"        
            text " 职 业" color "#33cccc"
            hbox:
                vbox:
                    ysize 120
                    for job in all_jobs:
                        text job.capitalize() layout "nobreak"  size 25
                vbox:
                    ysize 120
                    for job in all_jobs:
                        bar:
                            xsize 200
                            value DictValue(slave_id.jp, job, slave_id.get_jp_cap(job))
                vbox:
                    ysize 120
                    for job in all_jobs:
                        text "{}".format(slave_id.jp[job]) layout "nobreak"  size 25
                vbox:
                    ysize 120
                    for job in all_jobs:
                        textbutton "最大值" action SetDict(slave_id.jp,job,slave_id.get_jp_cap(job)) text_size 10
            hbox:
                vbox:
                    ysize 120
                    #for job in ("service", "sex", "anal", "fetish"):
                    for job in ("service", "sex", "anal", "fetish"):
                        text girl_related_dict[job.capitalize()] layout "nobreak"  size 25
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        bar:
                            xsize 200
                            value DictValue(slave_id.jp, job, slave_id.get_jp_cap(job))
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        text "{}".format(slave_id.jp[job]) layout "nobreak"   size 25
                vbox:
                    ysize 120
                    for job in ("service", "sex", "anal", "fetish"):
                        textbutton "最大值" action SetDict(slave_id.jp,job,slave_id.get_jp_cap(job)) text_size 10

            text "————————————————————"             
            text "互动计数器" layout "nobreak" color "#33cccc"
            for act in slave_id.MC_interact_counters:
                if act not in ("present", "money", "offer", None):
                    hbox:
                        text "{}: {}".format(act.capitalize(), slave_id.MC_interact_counters[act]) layout "nobreak"
                        textbutton "" action SetDict(slave_id.MC_interact_counters,act,0)
            
        vbox:
            xfill True
            text ' 修改特质'
            viewport:
                mousewheel True
                draggable True
                scrollbars "vertical"
                xfill True
                yfill True
                ysize 0.975
                spacing 2
                has vbox
                for trait in (gold_traits + pos_traits + neg_traits + list(fix_dict.values()))[KW_paging*KW_paging_page_length:(KW_paging+1)*KW_paging_page_length]:

                    if trait in gold_traits:
                        if trait in slave_id.traits:
                            $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                            textbutton "移除特质 [trait.name_cn]":
                                action Function(slave_id.remove_trait,trait)
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                                text_layout "nobreak" 
                        else:
                            $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                            textbutton "添加特质 [trait.name_cn]":
                                action Function(slave_id.add_trait,trait)
                                text_color c_orange 
                                text_layout "nobreak" 
                                hovered SetVariable("trait_desc",trait.get_description("girls")) 
                                unhovered SetVariable("trait_desc"," ")
                    elif trait in pos_traits:
                        if trait in slave_id.traits:
                            $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                            textbutton "移除特质 [trait.name_cn]":
                                action Function(slave_id.remove_trait,trait)
                                text_layout "nobreak" 
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                        else:
                            $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                            textbutton "添加特质 [trait.name_cn]":
                                action Function(slave_id.add_trait,trait)
                                text_color c_emerald 
                                text_layout "nobreak" 
                                hovered SetVariable("trait_desc",trait.get_description("girls")) 
                                unhovered SetVariable("trait_desc"," ")
                    elif trait in neg_traits:
                        if trait in slave_id.traits:
                            $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                            textbutton "移除特质 [trait.name_cn]":
                                action Function(slave_id.remove_trait,trait)
                                text_layout "nobreak" 
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")
                        else:
                            $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                            textbutton "添加特质 [trait.name_cn]":
                                action Function(slave_id.add_trait,trait)
                                text_color c_crimson 
                                text_layout "nobreak" 
                                hovered SetVariable("trait_desc",trait.get_description("girls"))
                                unhovered SetVariable("trait_desc"," ")

#                    text 'Sexual Fixations'

                    elif trait in fix_dict.values():
                        $ trait.name_cn = tl_cn(trait.name, trait_name_dict)
                        textbutton "作为正面特质添加 [trait.name_cn]":
                            action Function(KW_safe_add_pos_fix,slave_id,trait.name)
                            text_color c_green 
                            text_layout "nobreak" 
                            hovered SetVariable("trait_desc",fix_description[trait.name + " description"])
                            unhovered SetVariable("trait_desc"," ")
                        textbutton "作为负面特质添加 [trait.name_cn]":
                            action Function(KW_safe_add_neg_fix,slave_id,trait.name)
                            text_color c_crimson 
                            text_layout "nobreak" 
                            hovered SetVariable("trait_desc",fix_description[trait.name + " description"])
                            unhovered SetVariable("trait_desc"," ")
                text "[trait_desc]"











