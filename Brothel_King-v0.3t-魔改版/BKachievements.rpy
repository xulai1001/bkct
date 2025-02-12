#### BK Achievements ####

## How to add an achievement easily:
## Simple binary unlock (use level_cap to limit the max unlock level, optional):
# $ unlock_achievement(target, level_cap)

## Increment a counter:
## 1/ Declare the target in 'tracked_achievements' below
## 2/ Insert this in the relevant part of code:
# $ game.track(target, value)

init python:
    def count_achievements(locked=False):
        if locked:
            return sum(a.level_nb*a.multi for a in achievement_list)
        else:
            return sum(a.level*a.multi for a in achievement_list)



    achievement_list = [
                        Achievement(_("磨刀不误砍柴功"), __("观看新手教程。"), pic="portrait.webp", pic_path="NPC/Sill/", target="intro"),

                        Achievement(_("新培训师：玛雅"), __("你解锁了玛雅。她可以提高女孩的自卫能力。"), pic="portrait.webp", pic_path="NPC/Maya/", target="trainer maya", multi=3),
                        Achievement(_("新培训师：伦萨"), __("你解锁了伦萨。她可以把你的女孩训练成小偷。"), pic="portrait.webp", pic_path="NPC/Renza/", target="trainer renza", multi=3),
                        Achievement(_("新培训师：萨特拉"), __("你解锁了萨特拉。她将使你的女孩们感到恐惧。"), pic="portrait.webp", pic_path="NPC/Satella/", target="trainer satella", multi=3),
                        Achievement(_("新培训师：法拉"), __("你解锁了法拉。她训练的是比较刺激的性行为。"), pic="portrait.webp", pic_path="NPC/Captain/", target="trainer farah", multi=3),
                        Achievement(_("新培训师：莉迪"), __("你解锁了莉迪。她可以让你的女孩们更听话。"), pic="portrait.webp", pic_path="NPC/Lieutenant/", target="trainer lydie", multi=3),
                        Achievement(_("新培训师：史黛拉"), __("你解锁了史黛拉。她可以提高你的农场训练效果。"), pic="portrait.webp", pic_path="NPC/Stella/", target="trainer stella", multi=3),
                        Achievement(_("新培训师：巴斯特"), __("你解锁了巴斯特。她可以帮助你收集资源。"), pic="portrait.webp", pic_path="NPC/Bast/", target="trainer bast", multi=3),
                        Achievement(_("新培训师：戈尔迪"), __("你解锁了戈尔迪。她可以对你的女孩进行温和的技术培训。"), pic="portrait.webp", pic_path="NPC/Goldie/", target="trainer goldie", multi=3),
                        Achievement(_("新培训师：公会职员"), __("你解锁了公会职员。她可以保护你的部分收入免于纳税。"), pic="portrait.webp", pic_path="NPC/Taxgirl/", target="trainer taxgirl", multi=3),

                        Achievement(_("解锁商户：戈尔迪"), __("你解锁了牧场，戈尔迪在这里出售野兽和相关物品。"), pic="portrait.webp", pic_path="NPC/Goldie/", target="merchant goldie", multi=2),
                        Achievement(_("解锁商户：史黛拉"), __("史黛拉出售种马和相关物品，如果你敢接近她。"), pic="portrait.webp", pic_path="NPC/Stella/", target="merchant stella", multi=2),
                        Achievement(_("解锁商户：薇儿"), __("薇洛出售她为生计而捕获的怪物，以及相关物品。"), pic="portrait.webp", pic_path="NPC/Willow/", target="merchant willow", multi=2),
                        Achievement(_("解锁商户：吉娜"), __("科学家吉娜销售机械小玩意，并研究如何飞行。"), pic="portrait.webp", pic_path="NPC/Gina/", target="merchant gina", multi=2),
                        Achievement(_("解锁商户：瑞秋"), __("瑞秋出售她在植物园里采摘的鲜花。"), pic="portrait.webp", pic_path="NPC/Riche/", target="merchant riche", multi=4),
                        Achievement(_("解锁商户：卡特林"), __("卡特林卖小饰品，脾气很暴躁。"), pic="portrait.webp", pic_path="NPC/Katryn/", target="merchant katryn", multi=4),
                        Achievement(_("解锁商户：古里古拉"), __("古里古拉卖玩具、食品和用品，当她不分心的时候。"), pic="portrait.webp", pic_path="NPC/Gurigura/", target="merchant gurigura", multi=4),
                        Achievement(_("解锁商户：拉米娅"), __("拉米娅贩卖武器，她不受傻瓜和讨价还价的影响。"), pic="portrait.webp", pic_path="NPC/Ramias/", target="merchant ramias", multi=4),
                        Achievement(_("解锁商户：礼品店"), __("礼品店女孩卖的是....礼物。废话。"), pic="portrait.webp", pic_path="NPC/Gift girl/", target="merchant giftgirl", multi=4),
                        Achievement(_("解锁商户：双胞胎"), __("双胞胎，我的天！是双胞胎！"), pic="body.webp", pic_path="NPC/Twins/", target="merchant twins", multi=4),

                        Achievement(_("第一章：狼狈为奸"), __("你帮助一群混混在下水道里强暴了一个无助的女人。"), pic="portrait naked.webp", pic_path="NPC/Sewer girl/", target="c1 gang", multi=2),
                        Achievement(_("第一章：正义联盟"), __("你已经完成了第一章的剧情，并且站在了玛雅那一边。"), pic="portrait.webp", pic_path="NPC/Maya/", target="c1 good", multi=10),
                        Achievement(_("第一章：盗亦有道"), __("你已经完成了第一章的剧情，并且站在了伦萨那一边。"), pic="portrait.webp", pic_path="NPC/Renza/", target="c1 neutral", multi=10),
                        Achievement(_("第一章：趋炎附势"), __("你已经完成了第一章的剧情，并且站在了上尉那一边。"), pic="portrait.webp", pic_path="NPC/Captain/", target="c1 evil", multi=10),

                        Achievement(_("第二章：狩猎忍者"), __("你第一次抓到了女忍者。"), pic="kunoichi portrait.webp", pic_path="NPC/kunoichi/", target="c2 kunoichi", multi=4),
                        Achievement(_("第二章：悲伤往事"), __("你了解了春香悲伤的过去。"), pic="portrait.webp", pic_path="NPC/kunoichi/haruka/", target="c2 haruka", multi=4),
                        Achievement(_("第二章：温泉幽灵"), __("你在温泉中与美月发生了奇怪的、令人激动的邂逅。"), pic="portrait.webp", pic_path="NPC/kunoichi/mizuki/", target="c2 mizuki", multi=4),
                        Achievement(_("第二章：不良少女"), __("你偷看了鸣香的自慰秀。"), pic="portrait.webp", pic_path="NPC/kunoichi/narika/", target="c2 narika", multi=4),

                        Achievement(_("猎艳：金发女郎"), __("你和那个金发碧眼的女郎做了爱。"), pic="amber ring.webp", pic_path="items/ring/", target="h treasure blonde", multi=10),
                        Achievement(_("猎艳：粉红女郎"), __("你和那个粉红头发的女孩做了爱。"), pic="amber ring.webp", pic_path="items/ring/", target="h treasure pink", multi=10),
                        Achievement(_("猎艳：希露"), __("你与你的奴隶希露激烈地做爱。"), pic="portrait2.webp", pic_path="NPC/Sill/", target="h sill1", multi=5),
                        Achievement(_("猎艳：女仆"), __("你与乔的女仆上了床。"), pic="portrait blush.webp", pic_path="NPC/Maid/", target="h maid", multi=5),
                        Achievement(_("猎艳：银行家"), __("你与银行家做了爱。"), pic="portrait.webp", pic_path="NPC/Banker/", target="h banker", multi=10),
                        Achievement(_("猎艳：上尉"), __("你与法拉做了爱。"), pic="portrait.webp", pic_path="NPC/Captain/", target="h farah", multi=5),
                        Achievement(_("猎艳：中尉"), __("你与莉迪做了爱。"), pic="portrait.webp", pic_path="NPC/Lieutenant/", target="h lydie", multi=5),
                        Achievement(_("猎艳：中士"), __("你与卡希夫做了爱。"), pic="portrait.webp", pic_path="NPC/Sergeant/", target="h kashiv", multi=5),
                        Achievement(_("猎艳：守卫"), __("你与玛雅做了爱。"), pic="portrait.webp", pic_path="NPC/Maya/", target="h maya", multi=5),
                        Achievement(_("猎艳：盗贼领袖"), __("你与伦萨做了爱。"), pic="portrait.webp", pic_path="NPC/Renza/", target="h renza", multi=10),
                        Achievement(_("猎艳：农场少女"), __("你与戈尔迪做了爱。"), pic="portrait.webp", pic_path="NPC/Goldie/", target="h goldie", multi=5),
                        Achievement(_("猎艳：官员"), __("你与史黛拉做了爱。"), pic="portrait.webp", pic_path="NPC/Stella/", target="h stella", multi=5),
                        Achievement(_("猎艳：将军"), __("你与卡将军做了爱。"), pic="ka portrait.webp", pic_path="NPC/Stella/", target="h ka", multi=10),
                        Achievement(_("猎艳：上将"), __("你与泽伊做了爱。"), pic="zee portrait.webp", pic_path="NPC/Stella/", target="h zee", multi=10),
                        Achievement(_("猎艳：怪物猎人"), __("你与薇儿做了爱。"), pic="portrait.webp", pic_path="NPC/Willow/", target="h willow", multi=5),
                        Achievement(_("猎艳：表妹"), __("你与薇洛的表亲做了爱。"), pic="portrait.webp", pic_path="NPC/Willow/", target="h relative", multi=10),
                        Achievement(_("癞蛤蟆想吃天鹅肉"), __("你变成蟾蜍后发生了性关系，你最好永远保守这个秘密。"), pic="milkmaid.webp", pic_path="NPC/Misc/", target="h toad", multi=10),
                        Achievement(_("猎艳：老板娘"), __("你与老板娘做了爱。"), pic="silky nighties.webp", pic_path="items/gift/", target="h shop", multi=10),
                        Achievement(_("猎艳：夜之使徒"), __("你与萨特拉做了爱。"), pic="portrait.webp", pic_path="NPC/Satella/", target="h satella", multi=10),
                        Achievement(_("猎艳：月之女神"), __("你与女神莎莉娅做了爱。"), pic="portrait.webp", pic_path="NPC/Shalia/", target="h shalia", multi=25),
                        Achievement(_("猎艳：下水道"), __("你与从下水道里救出的女人做了爱。"), pic="portrait.webp", pic_path="NPC/Sewer girl/", target="h sewer", multi=10),
                        Achievement(_("猎艳：工匠"), __("你与贝斯特做了爱。"), pic="portrait.webp", pic_path="NPC/Bast/", target="h bast", multi=10),
                        Achievement(_("猎艳：性感沙滩"), __("你与阿妮卡做了爱。"), pic="anika portrait.webp", pic_path="NPC/Jobgirl/beach/", target="h anika", multi=10),
#                         Achievement("Bedded: The Adventurer", "You had sex with Scarlet.", pic="portrait.webp", pic_path="NPC/Jobgirl/", target="h jobgirl"), # Event not ready yet?
                        Achievement(_("猎艳：女税务官"), __("你与奴隶公会的女职员发生了性关系。"), pic="portrait.webp", pic_path="NPC/taxgirl/", target="h taxgirl", multi=10),
                        Achievement(_("猎艳：风之忍者"), __("你与云雀发生了（多次）关系。"), pic="portrait.webp", pic_path="NPC/suzume/", target="h suzume", multi=10),
                        Achievement(_("猎艳：贵族千金"), __("你与汉索-焰做了爱。"), pic="portrait.webp", pic_path="NPC/homura/", target="h homura", multi=10),


                        Achievement(_("露水姻缘：冒险家"), __("你与%s位女冒险家做了爱。"), pic="impress0.webp", pic_path="NPC/encounters/", target="h impress", level_nb=4, multi=2),
                        Achievement(_("露水姻缘：奴隶"), __("你帮助训练了一个女奴隶。"), pic="slave2.webp", pic_path="NPC/misc/", target="h slavegirl", multi=2),
                        Achievement(_("露水姻缘：训奴师"), __("你与奴隶市场的女人做了爱。"), pic="slave1.webp", pic_path="NPC/misc/", target="h slavemarket", multi=4),
                        Achievement(_("露水姻缘：猫娘"), __("你与%s位猫娘做了爱。"), pic="cat found.webp", pic_path="NPC/encounters/", target="h catgirl", level_nb=2, multi=2),
                        Achievement(_("露水姻缘：占卜师"), __("你与一个吉普赛女占卜师做了爱。"), pic="gypsy1_1.webp", pic_path="NPC/encounters/", target="h gypsy", multi=2),
                        Achievement(_("露水姻缘：蟊贼"), __("你与一个被打败的女蟊贼做了爱。"), pic="rob5_1.webp", pic_path="NPC/encounters/", target="h robber", multi=2),
                        Achievement(_("露水姻缘：赌徒"), __("你与一个女赌徒做了爱。"), pic="gambler4_1.webp", pic_path="NPC/encounters/", target="h gambler", multi=2),
                        Achievement(_("圣诞快乐"), __("你与一位神秘的冬季访客做了爱。"), pic="portrait.webp", pic_path="NPC/Hmas/", target="hmas", multi=10),


                        Achievement(_("崭露头角"), __("拥有%s位奴隶（除去希露）。"), pic="slave1.webp", pic_path="NPC/Misc/", level_nb=5, target="slaves", requirements={1 : 4, 2 : 8, 3 : 16, 4 : 24, 5 : 32}, multi=5),
                        Achievement(_("初试锋芒"), __("拥有%s位B阶或以上的奴隶。"), pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank B", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=2),
                        Achievement(_("群英荟萃"), __("拥有%s位A阶或以上的奴隶。"), pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank A", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=3),
                        Achievement(_("艳名远扬"), __("拥有%s位S阶或以上的奴隶。"), pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank S", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=5),
                        Achievement(_("佳丽三千"), __("拥有%s位X阶或以上的奴隶。"), pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="rank X", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=10),
                        Achievement(_("苦中作乐"), __("拥有%s位受虐狂奴隶。"), pic="slave2.webp", pic_path="NPC/Misc/", level_nb=5, target="masochist", requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, multi=3),
                        Achievement(_("饱经风霜"), __("一局游戏中，你的女孩们在农场的训练时间累积有 %s 天。"), pic="beast2.webp", pic_path="NPC/Minions/", level_nb=5, target="farm_days", requirements={1 : 10, 2 : 30, 3 : 90, 4 : 180, 5 : 365}, multi=2),
                        Achievement(_("玩物丧志"), __("让你的女孩们在一局游戏中使用性爱玩具的次数达到 %s 。"), pic="black dildo.webp", pic_path="Items/Toy/", level_nb=5, target="used toy", requirements={1 : 1, 2 : 10, 3 : 100, 4 : 500, 5 : 2500}, multi=3),
                        Achievement(_("正当防卫"), __("给%s位女孩配备武器。"), pic="knife.webp", pic_path="Items/Weapon/", level_nb=5, target="hands", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement(_("人靠衣装"), __("给%s位女孩换上衣服。"), pic="frilly dress.webp", pic_path="Items/dress/", level_nb=5, target="body", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement(_("宠物项圈"), __("给%s位女孩戴上项链。"), pic="dog collar.webp", pic_path="Items/necklace/", level_nb=5, target="neck", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement(_("情比金坚"), __("给%s位女孩戴上戒指。"), pic="brass ring.webp", pic_path="Items/ring/", level_nb=5, target="finger", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement(_("点睛之笔"), __("给%s位女孩装备饰品。"), pic="lace panties.webp", pic_path="Items/accessory/", level_nb=5, target="accessory", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}),
                        Achievement(_("性感沙滩"), __("有%s位女孩同时处于裸体状态。"), pic="naked2.webp", pic_path="UI/status/", level_nb=5, target="naked", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=3),
                        Achievement(_("花开并蒂"), __("有%s位女孩喜欢双飞。"), pic="naked2.webp", pic_path="UI/status/", level_nb=5, target="bisexual", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=5),
                        Achievement(_("百花齐放"), __("有%s位女孩喜欢群交。"), pic="naked2.webp", pic_path="UI/status/", level_nb=5, target="group", requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=10),


                        Achievement(_("勇冠三军"), __("战士职业的等级达到%s级。"), pic="warrior.webp", pic_path="UI/", level_nb=5, target="战士", requirements={1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25}, multi=5),
                        Achievement(_("法力风暴"), __("法师职业的等级达到%s级。"), pic="wizard.webp", pic_path="UI/", level_nb=5, target="法师", requirements={1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25}, multi=5),
                        Achievement(_("唯利是图"), __("商人职业的等级达到%s级。"), pic="trader.webp", pic_path="UI/", level_nb=5, target="商人", requirements={1 : 5, 2 : 10, 3 : 15, 4 : 20, 5 : 25}, multi=5),
                        Achievement(_("与人为善"), __("成为正义的光辉榜样。同时做好一个青楼老板。为什么不可能呢? "), pic="al_good.webp", pic_path="UI/", target="good", multi=10),
                        Achievement(_("保持中立"), __("你不偏袒任何一方，你只想闷声发大财。"), pic="al_neutral.webp", pic_path="UI/", target="neutral", multi=10),
                        Achievement(_("恶贯满盈"), __("你真坏到流脓。获得超过%s点邪恶点数。"), pic="al_evil.webp", pic_path="UI/", level_nb=3, target="evil", requirements={1 : 10, 2 : 100, 3 : 1000}, custom_titles={1 : "Mother-In-Law", 2 : "Dr. Evil", 3 : "Palpatine"}, multi=5),
                        Achievement(_("和平主义"), __("在这个游戏过程中，没有任何超自然的动物受到伤害. {b}{i}果真如此吗?{/i}{/b}"), pic="pet1.webp", pic_path="NPC/Misc/Pets/", target="pet armageddon", multi=25),
                        Achievement(_("力大无穷"), __("主角的力量达到10。"), pic="warrior.webp", pic_path="UI/", target="mc strength", multi=10),
                        Achievement(_("百折不挠"), __("主角的精神达到10。"), pic="wizard.webp", pic_path="UI/", target="mc spirit", multi=10),
                        Achievement(_("貌若潘安"), __("主角的魅力达到10。"), pic="trader.webp", pic_path="UI/", target="mc charisma", multi=10),
                        Achievement(_("风驰电掣"), __("主角的速度达到10。"), pic="Leather boots.webp", pic_path="items/accessory/", target="mc speed", multi=10),

                        Achievement(_("长夜漫漫"), __("一局游戏中，累积游玩了%s个月。"), pic="calendar.webp", pic_path="UI/", level_nb=5, target="months", requirements={1 : 1, 2 : 3, 3 : 6, 4 : 12, 5 : 24}, multi=5),
                        Achievement(_("衣冠禽兽"), __("成功完成%s份合约。"), pic=license_dict[1][1], pic_path="UI/", level_nb=5, target="completed contracts", requirements={1 : 1, 2 : 3, 3 : 6, 4 : 12, 5 : 24}, multi=10),
                        Achievement(_("改弦更张"), __("在完美完成合约之后转卖掉一个女孩。"), pic="maid.webp", pic_path="NPC/Misc/", target="contract sale", multi=25),
                        Achievement(_("任务达人"), __("完成%s份委托。"), pic="portrait.webp", pic_path="NPC/Jobgirl/", level_nb=5, target="completed quest", requirements={1 : 5, 2 : 25, 3 : 50, 4 : 100, 5 : 250}, multi=5),
                        Achievement(_("变态高校"), __("完成%s次培训。"), pic="portrait.webp", pic_path="NPC/Jobgirl/", level_nb=5, target="completed class", requirements={1 : 5, 2 : 25, 3 : 50, 4 : 100, 5 : 250}, multi=5),
                        Achievement(_("求知若渴"), __("在一个培训班里塞满你的女孩。"), pic="portrait.webp", pic_path="NPC/Sewer girl/", target="filled class", multi=10),
                        Achievement(_("动物牧场"), __("获得%s位仆从。"), pic="beast1.webp", pic_path="NPC/Minions/", level_nb=5, target="minions", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 12, 5 : 20}, multi=5),
                        Achievement(_("生财有道"), __("一局游戏中赚取%s金币。"), pic="gold bag.webp", pic_path="items/misc/", level_nb=6, target="total_gold", requirements={1 : 1000, 2 : 10000, 3 : 100000, 4 : 1000000, 5 : 10000000, 6 : 100000000}, multi=10),
                        Achievement(_("夜进斗金"), __("一夜之间赚取%s金币。"), pic="coin.webp", pic_path="UI/", level_nb=5, target="income", requirements={1 : 100, 2 : 1000, 3 : 10000, 4 : 100000, 5 : 250000}, multi=10),
                        Achievement(_("血本无归"), __("一夜之间损失了%s金币。"), pic="portrait.webp", pic_path="NPC/Kosmo/", level_nb=5, target="losses", requirements={1 : 100, 2 : 1000, 3 : 5000, 4 : 10000, 5 : 25000}, multi=10),
                        Achievement(_("富甲一方"), __("拥有%s金币的现金。"), pic="jewel bag.webp", pic_path="items/misc/", level_nb=5, target="gold", requirements={1 : 1000, 2 : 10000, 3 : 100000, 4 : 1000000, 5 : 10000000}, multi=10),
                        Achievement(_("和和睦睦"), __("你的女孩中有%s个有好朋友。"), pic="heart.webp", pic_path="UI/", level_nb=5, target="friends", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=5),
                        Achievement(_("勾心斗角"), __("你的女孩中有%s个和别人结仇。"), pic="broken heart.webp", pic_path="UI/", level_nb=5, target="rivals", requirements={1 : 2, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=5),
                        Achievement(_("久经沙场"), __("安全度过%s个突发事件。"), pic="shield.webp", pic_path="UI/", level_nb=5, target="security events", requirements={1 : 10, 2 : 25, 3 : 50, 4 : 125, 5 : 250}, multi=5),
                        Achievement(_("擒贼先擒王"), __("捕获一名敌方首领。"), pic="portrait.webp", pic_path="NPC/Kenshin", target="general captured", multi=25),
                        Achievement(_("解救人质"), __("拯救一个被绑架的女孩。"), pic="knight portrait.webp", pic_path="NPC/Misc/", target="rescued from kidnapping", multi=25),
                        Achievement(_("蠢蠢欲动"), __("在你的女孩身上发现 %s 个正面性癖。"), pic="droplet.webp", pic_path="UI/", target="pos fixations", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 125, 5 : 250}, multi=5),
                        Achievement(_("人无完人"), __("发现你的女孩有%s个负面癖好。"), pic="skull.webp", pic_path="UI/", target="neg fixations", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 125, 5 : 250}, multi=5),
                        Achievement(_("迎难而上"), __("让你的女孩消除%s个负面癖好。"), pic="droplet.webp", pic_path="UI/", target="neg fixation removed", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=5),
                        Achievement(_("弄巧成拙"), __("过于用力结果锁定了女孩的负面癖好。"), pic="skull.webp", pic_path="UI/", target="neg fixation locked", multi=5),
                        Achievement(_("催眠大师"), __("成功催眠女孩%s次。"), pic="droplet.webp", pic_path="UI/", target="hypnotize success", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 50, 4 : 100, 5 : 250}, multi=5),
                        Achievement(_("笨手笨脚"), __("催眠女孩失败%s次。"), pic="droplet.webp", pic_path="UI/", target="hypnotize failure", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 50, 5 : 100}, multi=3),

                        Achievement(_("妇女之友"), __("有%s个女孩的好感度达到%s 或更多。"), level_nb=5, pic="heart.webp", pic_path="UI/", target="love", requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 25, 2 : 50, 3 : 75, 4 : 100, 5 : 125}, multi=3),
                        Achievement(_("惊弓之鸟"), __("有%s个女孩的恐惧值达到%s 或更多。"), level_nb=5, pic="skull.webp", pic_path="UI/", target="fear", requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 25, 2 : 50, 3 : 75, 4 : 100, 5 : 125}, multi=3),
                        Achievement(_("女子天团"), __("有%s个女孩的美貌超过%s 。"), pic="portrait.webp", pic_path="NPC/Katryn/", target="Beauty", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("魔鬼身材"), __("有%s个女孩的身材超过%s 。"), pic="portrait.webp", pic_path="NPC/Ramias/", target="Body", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("风华绝代"), __("有%s个女孩的魅力超过%s 。"), pic="portrait.webp", pic_path="NPC/Gurigura/", target="Charm", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("知书达理"), __("有%s个女孩的优雅超过%s 。"), pic="portrait.webp", pic_path="NPC/Riche/", target="Refinement", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("淫娃荡妇"), __("有%s个女孩的性欲超过%s 。"), pic="portrait.webp", pic_path="NPC/Captain/", target="Libido", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("唯命是从"), __("有%s个女孩的服从超过%s 。"), pic="portrait.webp", pic_path="NPC/Maid/", target="Obedience", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("身强体壮"), __("有%s个女孩的体格超过%s 。"), pic="portrait.webp", pic_path="NPC/Jobgirl/", target="Constitution", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("敏感体质"), __("有%s个女孩的敏感超过%s 。"), pic="portrait.webp", pic_path="NPC/Satella/", target="Sensitivity", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=2),
                        Achievement(_("侍奉精通"), __("有%s个女孩的性服侍熟练度超过 %s 。"), pic="portrait.webp", pic_path="NPC/Willow/", target="Service", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=4),
                        Achievement(_("性交精通"), __("有%s个女孩的性交熟练度超过 %s 。"), pic="portrait.webp", pic_path="NPC/Goldie/", target="Sex", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=4),
                        Achievement(_("肛交精通"), __("有%s个女孩的肛交熟练度超过 %s 。"), pic="portrait.webp", pic_path="NPC/Kosmo/", target="Anal", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=4),
                        Achievement(_("调教精通"), __("有%s个女孩的调教熟练度超过 %s 。"), pic="portrait.webp", pic_path="NPC/Stella/", target="Fetish", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=4),
                        Achievement(_("登峰造极"), __("有%s个女孩的所有技能熟练度都超过 %s 。"), pic="portrait.webp", pic_path="NPC/Sill/", target="ultimate", level_nb=5, requirements={1 : 1, 2 : 2, 3 : 4, 4 : 8, 5 : 16}, requirements2={1 : 50, 2 : 100, 3 : 150, 4 : 200, 5 : 250}, multi=5),
                        Achievement(_("K K园区"), __("一局游戏中，出售女孩累积赚取 %s 金币。"), pic="slave1.webp", pic_path="NPC/Misc/", target="sell girl gold", level_nb=5, requirements={1 : 500, 2 : 2500, 3 : 10000, 4 : 25000, 5 : 100000}, multi=5),
                        Achievement(_("铁石心肠"), __("出售一个爱你的女孩。"), pic="spirit portrait.webp", pic_path="NPC/Misc/", target="sell girl love", multi=20),
                        Achievement(_("有一种爱叫做放手"), __("让女孩重新获得自由。"), pic="broken heart.webp", pic_path="UI/", target="release free girl", multi=10),
                        Achievement(_("索求无度"), __("强奸你的女孩%s次。"), pic="spirit portrait.webp", pic_path="NPC/Misc/", target="raped", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 10, 4 : 25, 5 : 100}, multi=3),
                        Achievement(_("家庭暴力"), __("体罚你的女孩%s次。"), pic="spirit portrait.webp", pic_path="NPC/Misc/", target="beaten", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 10, 4 : 25, 5 : 100}, multi=3),
                        Achievement(_("小惩大诫"), __("惩罚你的女孩%s次。"), pic="skull.webp", pic_path="UI/", target="punished", level_nb=5, requirements={1 : 5, 2 : 25, 3 : 100, 4 : 250, 5 : 500}, multi=2),
                        Achievement(_("寓教于乐"), __("奖励你的女孩%s次。"), pic="droplet.webp", pic_path="UI/", target="rewarded", level_nb=5, requirements={1 : 5, 2 : 25, 3 : 100, 4 : 250, 5 : 500}, multi=2),
                        Achievement(_("养尊处优"), __("你对女孩奖励太多，导致她被宠坏了。"), pic="bun.webp", pic_path="items/food/", target="spoiled", multi=2),
                        Achievement(_("高压管理"), __("你对女孩的惩罚太多，导致她很害怕。"), pic="monster juice.webp", pic_path="items/misc/", target="terrified", multi=2),
                        Achievement(_("垦辟荒野"), __("你解锁了奴隶农场。"), pic="beast2.webp", pic_path="NPC/Minions/", target="farm", multi=2),
                        Achievement(_("再接再厉"), __("你解锁了木匠的马车。"), pic="portrait.webp", pic_path="NPC/Carpenter/", target="wagon", multi=2),
                        Achievement(_("下水道骑士"), __("你在下水道里解救了被绑架的女孩。"), pic="portrait naked.webp", pic_path="NPC/Sewer girl/", target="sewer defender", multi=2),
                        Achievement(_("没完没了"), __("科斯莫骚扰了你%s次。"), pic="portrait.webp", pic_path="NPC/Kosmo/", target="kosmo", level_nb=4, requirements={1 : 1, 2 : 5, 3 : 10, 4 : 20}, multi=2),

                        Achievement(_("风流浪子"), __("与女孩上床%s次。"), pic="heart.webp", pic_path="UI/", level_nb=5, target="had sex", requirements={1 : 5, 2 : 25, 3 : 100, 4 : 250, 5 : 1000}, multi=5),
                        Achievement(_("人才投资"), __("在奴隶市场上花费%s金币。"), pic="slave2.webp", pic_path="NPC/Misc/", target="gold spent slavemarket", level_nb=4, requirements={1 : 500, 2 : 2500, 3 : 10000, 4 : 25000, 5 : 100000}, multi=2),
                        Achievement(_("挥金如土"), __("在商店里花费%s金币。"), pic="portrait.webp", pic_path="NPC/Gift girl/", target="gold spent shops", level_nb=4, requirements={1 : 500, 2 : 2500, 3 : 10000, 4 : 25000, 5 : 100000}, multi=2),
                        Achievement(_("知根知底"), __("一局游戏中倾听%s位女孩的背景故事。"), pic="empty heart.webp", pic_path="UI/", target="origin stories", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 24}, multi=2),
                        Achievement(_("逼良为娼"), __("说服%s位自由女孩在你的青楼工作。"), pic="empty heart.webp", pic_path="UI/", target="free girl acquired", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=5),
                        Achievement(_("十艘跳"), __("同时拥有十个女朋友。"), pic="heart.webp", pic_path="UI/", target="girlfriends", requirements={1 : 10}, multi=25),
                        Achievement(_("原班人马"), __("在你的青楼里有%s位原始女孩。"), pic="license2.webp", pic_path="UI/", target="originals", level_nb=5, requirements={1 : 1, 2 : 4, 3 : 8, 4 : 16, 5 : 32}, multi=2),

                        Achievement(_("一掷千金：混混"), __("让一名混混在青楼里花光所有的钱。"), pic="beggar.webp", pic_path="UI/customers/", target="broke beggars"),
                        Achievement(_("一掷千金：冒险者"), __("让一名冒险者在青楼里花光所有的钱。"), pic="thug.webp", pic_path="UI/customers/", target="broke thugs", multi=2),
                        Achievement(_("一掷千金：工人"), __("让一名工人在青楼里花光所有的钱。"), pic="Laborer.webp", pic_path="UI/customers/", target="broke laborers", multi=2),
                        Achievement(_("一掷千金：水手"), __("让一名水手在青楼里花光所有的钱。"), pic="Sailor.webp", pic_path="UI/customers/", target="broke sailors", multi=2),
                        Achievement(_("一掷千金：社畜"), __("让一名社畜在青楼里花光所有的钱。"), pic="Commoner.webp", pic_path="UI/customers/", target="broke commoners", multi=3),
                        Achievement(_("一掷千金：工匠"), __("让一名工匠在青楼里花光所有的钱。"), pic="Craftsman.webp", pic_path="UI/customers/", target="broke craftsmen", multi=3),
                        Achievement(_("一掷千金：公务员"), __("让一名公务员在青楼里花光所有的钱。"), pic="Bourgeois.webp", pic_path="UI/customers/", target="broke bourgeois", multi=3),
                        Achievement(_("一掷千金：生意人"), __("让一名生意人在青楼里花光所有的钱。"), pic="Guild Member.webp", pic_path="UI/customers/", target="broke guild members", multi=4),
                        Achievement(_("一掷千金：骑士"), __("让一名骑士在青楼里花光所有的钱。"), pic="Patrician.webp", pic_path="UI/customers/", target="broke patricians", multi=4),
                        Achievement(_("一掷千金：法师"), __("让一名法师在青楼里花光所有的钱。"), pic="aristocrat.webp", pic_path="UI/customers/", target="broke aristocrats", multi=4),
                        Achievement(_("一掷千金：贵族子弟"), __("让一名贵族子弟在青楼里花光所有的钱。"), pic="Noble.webp", pic_path="UI/customers/", target="broke nobles", multi=5),
                        Achievement(_("一掷千金：皇室成员"), __("让一名皇室成员在青楼里花光所有的钱。"), pic="Royal.webp", pic_path="UI/customers/", target="broke royals", multi=10),
                        Achievement(_("五星好评：混混"), __("让一名混混在青楼里完全满足。"), pic="beggar.webp", pic_path="UI/customers/", target="happy beggars"),
                        Achievement(_("五星好评：冒险者"), __("让一名冒险者在青楼里完全满足。"), pic="thug.webp", pic_path="UI/customers/", target="happy thugs", multi=2),
                        Achievement(_("五星好评：工人"), __("让一名工人在青楼里完全满足。"), pic="Laborer.webp", pic_path="UI/customers/", target="happy laborers", multi=2),
                        Achievement(_("五星好评：水手"), __("让一名水手在青楼里完全满足。"), pic="Sailor.webp", pic_path="UI/customers/", target="happy sailors", multi=2),
                        Achievement(_("五星好评：社畜"), __("让一名社畜在青楼里完全满足。"), pic="Commoner.webp", pic_path="UI/customers/", target="happy commoners", multi=3),
                        Achievement(_("五星好评：工匠"), __("让一名工匠在青楼里完全满足。"), pic="Craftsman.webp", pic_path="UI/customers/", target="happy craftsmen", multi=3),
                        Achievement(_("五星好评：公务员"), __("让一名公务员在青楼里完全满足。"), pic="Bourgeois.webp", pic_path="UI/customers/", target="happy bourgeois", multi=3),
                        Achievement(_("五星好评：生意人"), __("让一名生意人在青楼里完全满足。"), pic="Guild Member.webp", pic_path="UI/customers/", target="happy guild members", multi=4),
                        Achievement(_("五星好评：骑士"), __("让一名骑士在青楼里完全满足。"), pic="Patrician.webp", pic_path="UI/customers/", target="happy patricians", multi=4),
                        Achievement(_("五星好评：法师"), __("让一名法师在青楼里完全满足。"), pic="aristocrat.webp", pic_path="UI/customers/", target="happy aristocrats", multi=4),
                        Achievement(_("五星好评：贵族子弟"), __("让一名贵族子弟在青楼里完全满足。"), pic="Noble.webp", pic_path="UI/customers/", target="happy nobles", multi=5),
                        Achievement(_("五星好评：皇室成员"), __("让一名皇室成员在青楼里完全满足。"), pic="Royal.webp", pic_path="UI/customers/", target="happy royals", multi=10),

                        Achievement(_("登峰造极：女仆"), __("让一名女孩上解锁女仆天赋树上的所有的天赋分支。"), pic="The Maid portrait.webp", pic_path="perks/", target="The Maid", multi=5),
                        Achievement(_("登峰造极：优伶"), __("让一名女孩上解锁优伶天赋树上的所有的天赋分支。"), pic="The Player portrait.webp", pic_path="perks/", target="The Player", multi=5),
                        Achievement(_("登峰造极：模特"), __("让一名女孩上解锁模特天赋树上的所有的天赋分支。"), pic="The Model portrait.webp", pic_path="perks/", target="The Model", multi=5),
                        Achievement(_("登峰造极：花魁"), __("让一名女孩上解锁花魁天赋树上的所有的天赋分支。"), pic="The Courtesan portrait.webp", pic_path="perks/", target="The Courtesan", multi=5),
                        Achievement(_("登峰造极：伴游"), __("让一名女孩上解锁伴游天赋树上的所有的天赋分支。"), pic="The Escort portrait.webp", pic_path="perks/", target="The Escort", multi=5),
                        Achievement(_("登峰造极：狐娘"), __("让一名女孩上解锁狐娘天赋树上的所有的天赋分支。"), pic="The Fox portrait.webp", pic_path="perks/", target="The Fox", multi=5),
                        Achievement(_("登峰造极：荡妇"), __("让一名女孩上解锁荡妇天赋树上的所有的天赋分支。"), pic="The Slut portrait.webp", pic_path="perks/", target="The Slut", multi=5),
                        Achievement(_("登峰造极：新娘"), __("让一名女孩上解锁新娘天赋树上的所有的天赋分支。"), pic="The Bride portrait.webp", pic_path="perks/", target="The Bride", multi=5),

                        Achievement(_("私人定制"), __("让女孩提供侍奉服务%s次。"), pic="egg vibrator.webp", pic_path="items/toy/", target="perform service", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}, multi=5),
                        Achievement(_("万人斩"), __("让女孩提供性交服务%s次。"), pic="lace panties.webp", pic_path="items/accessory/", target="perform sex", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}, multi=5),
                        Achievement(_("后庭花开"), __("让女孩提供肛交服务%s次。"), pic="butt plug.webp", pic_path="items/toy/", target="perform anal", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}, multi=5),
                        Achievement(_("女王大人"), __("让女孩进行SM调教%s次。"), pic="ropes.webp", pic_path="items/toy/", target="perform fetish", level_nb=5, requirements={1 : 1, 2 : 10, 3 : 100, 4 : 1000, 5 : 10000}, multi=5),
                        Achievement(_("莺歌燕舞"), __("让女孩提供双飞服务%s次。"), pic="black dildo.webp", pic_path="items/toy/", target="perform bisexual", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 100, 5 : 250}, multi=5),
                        Achievement(_("派对之星"), __("让女孩提供群交服务%s次。"), pic="beer keg.webp", pic_path="items/furniture/", target="perform group", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 100, 5 : 250}, multi=5),
                        Achievement(_("明日之星"), __("达到%s声望。"), pic="star.webp", pic_path="UI/", target="rep", level_nb=5, requirements={1 : 100, 2 : 1000, 3 : 5000, 4 : 10000, 5 : 30000}, multi=5),
                        Achievement(_("面面俱到"), __("在第%s章建造所有的设施。"), pic="steam jacuzzi.webp", pic_path="items/furniture/", target="furniture", level_nb=6, requirements={1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7}, multi=2),
                        Achievement(_("完美主义"), __("在第%s章完成所有的设施升级。"), pic="chapel.webp", pic_path="items/furniture/", target="upgrades", level_nb=7, requirements={1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7}, multi=2),
                        Achievement(_("强迫症"), __("在清洁青楼上花费%s金币。"), pic="broom.webp", pic_path="items/furniture/", target="gold clean", level_nb=5, requirements={1 : 250, 2 : 1000, 3 : 5000, 4 : 25000, 5 : 100000}, multi=2),
                        Achievement(_("最后期限"), __("成功偿还银行的贷款。"), pic="portrait.webp", pic_path="NPC/Banker/", target="first loan", multi=3),
                        Achievement(_("越挫越勇"), __("输掉一次游戏。"), pic="zap traps.webp", pic_path="items/furniture/", target="game over", multi=3),
                        Achievement(_("逃之夭夭"), __("一个女孩从你身边逃走了。"), pic="skull.webp", pic_path="UI/", target="runaway", multi=3),
                        Achievement(_("天罗地网"), __("你派遣雇佣兵抓到了逃跑的女孩。"), pic="guard portrait.webp", pic_path="NPC/Misc/", target="caught NPC", multi=3),
                        Achievement(_("插翅难飞"), __("你亲自出马抓住了一个逃跑的女孩。"), target="caught MC", multi=5),
                        Achievement(_("青楼大亨"), __("在普通难度下解锁无尽模式。"), pic="bronze statue.webp", pic_path="items/furniture/", target="win normal", multi=25),
                        Achievement(_("青楼之王"), __("在困难难度下解锁无尽模式。"), pic="silver statue.webp", pic_path="items/furniture/", target="win hard", multi=50),
                        Achievement(_("青楼之神"), __("在最高难度下解锁无尽模式。"), pic="gold statue.webp", pic_path="items/furniture/", target="win insane", multi=100),

                        Achievement(_("十恶不赦"), __("施展%s种邪恶力量。"), pic="evil deck.webp", pic_path="UI/powers/", target="powers", level_nb=5, requirements={1 : 1, 2 : 5, 3 : 25, 4 : 50, 5 : 100}, multi=3),
                        Achievement(_("紫色心情"), __("积累%s单位的紫色咒力"), pic="purple mojo.webp", pic_path="UI/powers/", target="purple mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}, multi=2),
                        Achievement(_("植树造林"), __("积累%s单位的绿色咒力。"), pic="orb_green.webp", pic_path="UI/powers/", target="green mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}, multi=2),
                        Achievement(_("忧郁蓝调"), __("积累%s单位的蓝色咒力。"), pic="orb_blue.webp", pic_path="UI/powers/", target="blue mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}, multi=2),
                        Achievement(_("红色警戒"), __("积累%s单位的红色咒力。"), pic="orb_red.webp", pic_path="UI/powers/", target="red mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}, multi=2),
                        Achievement(_("黄色狂热"), __("积累%s单位的黄色咒力。"), pic="orb_yellow.webp", pic_path="UI/powers/", target="yellow mojo", level_nb=5, requirements={1 : 10, 2 : 25, 3 : 50, 4 : 100, 5 : 500}, multi=2),
                        Achievement(_("吃干抹净"), __("让%s个女孩的心智崩溃。"), pic="whip.webp", pic_path="Items/weapon/", target="broken", level_nb=5, requirements={1 : 1, 2 : 3, 3 : 10, 4 : 25, 5 : 50}, multi=2),
                        Achievement(_("兔死狗烹"), __("把一个崩溃的女孩丢到街上自生自灭。"), pic="navThe Slums_idle.webp", pic_path="UI/", target="broken girl auction", multi=5),
                        Achievement(_("飞越疯人院"), __("把一个崩溃的女孩送去精神病院。"), pic="navThe Cathedra_idle.webp", pic_path="UI/", target="broken girl asylum", multi=5),
                        Achievement(_("命悬一线"), __("成功地治疗一个崩溃的女孩。"), pic="Tonic.webp", pic_path="items/misc/", target="broken girl healed", multi=5),
                        Achievement(_("人才妓妓"), __("拥有%s个站街妓女。"), pic="brothelnavbutton_idle.webp", pic_path="UI/", target="broken girl street", level_nb=4, requirements={1 : 1, 2 : 3, 3 : 10, 4 : 20}, multi=3),
                        Achievement(_("混乱无序"), __("解锁会说话的混沌魔剑。"), pic="portrait.webp", pic_path="NPC/Chaos/", target="chaos", multi=25),

                        Achievement(_("新周目"), __("通关游戏并解锁了新周目。"), pic="pet1.webp", pic_path="NPC/misc/Pets/", target="newgame+", multi=5),
                        Achievement(_("自由之翼"), __("在激活自由女孩挑战的情况下通关游戏。"), pic="girl.webp", pic_path="spells/", target="free girl challenge", multi=100),
                        Achievement(_("百炼成钢"), __("在激活训练挑战的情况下通关游戏。"), pic="militia.webp", pic_path="spells/", target="training challenge", multi=200),
                        ]

    achievement_dict = {}

    for achv in achievement_list:
        achievement_dict[achv.target] = achv

    # List of achievement targets that are tested with a game.track() update
    tracked_achievements = ["used toy", "farm_days", "had sex", "completed quest", "completed class", "completed contracts", "total_gold", "security events", "neg fixation removed", "hypnotize success", "hypnotize failure", "sell girl gold", "raped", "beaten", "punished", "rewarded", "free girl acquired", "origin stories", "gold spent slavemarket", "gold spent shops", "gold clean", "kosmo", "powers", "purple mojo", "green mojo", "blue mojo", "red mojo", "yellow mojo", "broken", "broken girl street", "perform service", "perform sex", "perform anal", "perform fetish"]

    def unlock_achievement(target, level_cap=99):
        if achievement_dict[target].unlock(level_cap):
            renpy.show_screen("achievement_notification", [achievement_dict[target]])
            memorize_achievement(target)

    def reset_achievements():
        global selected_achievement

        for achv in achievement_list:
            achv.level = 0
        persistent.achievements = {}
        selected_achievement = None
        latest_achievements = []

    def test_achievements(target_list):
        r = []
        for target in target_list:
            if achievement_dict[target].test():
                r.append(achievement_dict[target])
                memorize_achievement(target)

        renpy.show_screen("achievement_notification", r)

    def test_achievement(target):
        test_achievements([target])

    def memorize_achievement(target):
        global latest_achievements

        # Rotates the last 3 achievements
        if len(latest_achievements) >=3:
            latest_achievements = [[achievement_dict[target], achievement_dict[target].level]] + latest_achievements[0:2]
        else:
            latest_achievements = [[achievement_dict[target], achievement_dict[target].level]] + latest_achievements

#### END OF BK ACHIEVEMENTS FILE ####
