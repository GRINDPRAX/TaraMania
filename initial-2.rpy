init 900 python:

    initial_mod(
        "Taramania",
        "0.0.11d_test",
        "pon",
        "https://t.me/taramaniasg"
    )


    pers = 0 # temp переменная


    date_w_ghost = False # знаком с приведением?
    date_w_killer = False # знаком с киллером?
    date_w_tarakan = False  # тут False должно быть   ---- знаком с тараканом?

    tarakan_respect = 0    # респект от таракана
    npc_loc = 0     # локация нпс за которым следит таракан
    tarakan = 0    # для таракана, как предмет
    test = 0       # temp переменная


    think_about_ghost = False # знает о приведении?

    npc_name = "-"       # имя нпс за которым следит таракан


    tar_loc = "home" # локация таракана

    tarakan_can_diialog = 3   # заёбся таракан говоррить с тобой или нет  (заёбся, значит < 0)


    cr_facts = ["Ватикан — это самое маленькое государство в мире, но, тем не менее, там самый высокий уровень преступности.",
                "В 2005 году в Бразилии произошло самое комфортное ограбление. Грабители арендовали дом по соседству с банком и прорыли туннель до самого банковского хранилища. Для больших удобств, грабители провели в туннеле вентиляцию. Грабители перетащили в свой транспорт около 3 с половиной тонн денег, общей суммой в 69 миллионов долларов. Из 36 преступников, 10 так и не поймали. Нашли около трети украденной суммы.",
                "Организованная преступность – это третий, по величине дохода, бизнес в мире.",
                "Во Франции нельзя размещать снимки людей в наручниках, если их вина не доказана.",
                "В небольшом американском городе, в магазин по продаже магнитофонов, ворвались два грабителя. Один из них заорал “Никому не двигаться!”, и когда его напарник отправился к кассе… правильно, взял и застрелил его.",
                "великий учёный Исаак Ньютон работал тайным агентом и вывел на чистую воду 28 фальшивомонетчиков. По крайней мере, один из них был казнён за совершённое преступление.",
                "В штате Северная Каролина супружеское насилие не являлось преступлением вплоть до 1993 года. До сих пор в 33 штатах изнасилование мужем своей супруги рассматривается, как преступление средней тяжести.",
                "В Сиэтле, штат Вашингтон, есть свой настоящий супергерой, который законно борется с уличной преступностью."
                ]

    fil_citats = ["Не ищи счастье – оно всегда у тебя внутри.",
    "Лучше помолчать, чем  говорить без смысла.",
    "Тот, кто пьёт воду, должен помнить о тех, кто рыл колодец.",
    "Бедность приходит не из-за уменьшения богатства, а из-за умножения желаний",
    "Влияет ли имя человека на личность, которой он становится?",
    "Слишком много людей тратят деньги, которые они НЕ ЗАРАБОТАЛИ, чтобы покупать вещи, которые они НЕ ХОТЯТ, чтобы произвести впечатление на людей, которые им НЕ НРАВЯТЯ!",
    "Прослушивание подкастов перед сном - взрослая версия сказки на ночь.",
    "Когда вы стареете, то старый вы - технически новый вы, а  молодой вы - старый вы.",
    "Вы, вероятно, не найдете много негативных отзывов о парашютах в Интернете.",
    "Если у тебя получилось обмануть человека, это не значит, что он дурак, это значит, что тебе доверяли больше, чем ты этого заслуживаешь...",
    "Наш мозг одновременно ненавидит нас, любит нас, не заботится о нас и управляет каждым нашим движением.",
    "Где-то есть бабушка, чей внук действительно <<самый красивый мальчик>> в мире.",
    "Если когда-нибудь телепортация человека станет реальностью, люди все равно будут опаздывать на работу.",
    "В падающем самолёте нет атеистов.",
    "Дети следующего поколения, вероятно, будут ненавидеть нас за то, что мы взяли все хорошие имена пользователей...",
    "Если поставить солнечные батареи над парковками, наши машины не будут нагреваться, и у нас будет много чистой энергии.",
    "Когда вы покупаете ластик, вы буквально платите за свои ошибки.",
    "Прикусывание языка во время еды - прекрасный пример того, как вы все еще можете облажаться, даже имея многолетний опыт."]

    repl = ""    # TEMP переменная

    def_editor_in_hour1_hour("slezhka")
    def slezhka():
            global tar_loc
            global tarakan_can_diialog
            if tar_loc != 'home':
                tar_loc = 'home'
            tarakan_can_diialog += 1



        # знакомство с тараканом
    check_ivent(
        "location_gg == 'home' and date_w_tarakan == False and hour in [18, 19, 20, 21, 22, 23]",
        "new_neighborn"
    )

        # таракан рассказывает про призрака
    check_ivent(
        "location_gg == 'home' and tar_loc == 'home' and date_w_killer == True  ",
        "tarakan_speech_about_ghost"
    )

        # Знакомство с маньяком
    check_ivent(
        "location_gg == 'park' and date_w_killer == False and hour in [23, 0, 1, 2, 3, 4]",
        "killer_date"
    )

        # знакомство с призраком
    check_ivent(
        "location_gg == 'forest' and think_about_ghost == True and hour in [23, 0, 1, 2, 3, 4]",
        "date_ghost_label"
    )

    check_ivent(
        "location_gg == 'home' and date_w_ghost == True"
        "tarakan_speech_about_ghost"
    )




    add_button_in_activity_category(
        "Позвать таракана",
        "cringesuka456tarakan_dialog",
        ['home']
    )

    add_item(
        "Таракан",
        "tarakan",
        "tar_item_label",
        0.1,
        "Таракан",
        1,
        0)


init python hide:
    namemap = renpy.game.script.namemap
    namemap["new_neighborn"] = namemap["new_neighborn_mod"]




init:


    define tar_pers = Character(_("Роберт фон-Тараканиус"), color=Color("#00fa68"), who_font= 'gui/fonts/calibri_bold.ttf')

    define killer = Character(_("Маньяк"), color=Color("#f50505"), who_font= 'gui/fonts/calibri_bold.ttf')

    define ghost = Character(_("Призрак"), who_color="#f906d0ff", who_font='gui/fonts/calibri_bold.ttf')
    image ggrltest = "image/ggrltest.png"


    $ id_npc = 'npc1048'
    #$ generate_npc()
    $ npc_id = 'npc1048' 










    # призыв таракана
label cringesuka456tarakan_dialog:

    if date_w_tarakan == True and tar_loc == 'home':

        tar_pers "Я к вашим услугам, [player_name]"

        menu:
            "{color=#000000} Болтать\n{size=21}{i}+1 респект таракана{/i}{/size}{/color}":

                if tarakan_can_diialog >= 1:
                    $ tarakan_respect +=1

                elif tarakan_can_diialog <0:
                    tar_pers "Да ты заебал уже"
                    tar_pers "Ладно..."
                $ tarakan_can_diialog -= 1
                menu:
                    "{color=#000000} Поговорить о криминале{/color}":

                        $ repl = renpy.random.choice(cr_facts)
                        tar_pers "[repl]"



                    "{color=#000000} Поговорить о философии{/color}":

                        $ repl = renpy.random.choice(fil_citats)
                        tar_pers "[repl]"



                jump check_location

            "{color=#000000} Заглушка\n{size=21}{i}заглушка 2{/i}{/size}{/color}":
                    "in processing"


    elif date_w_tarakan == False:

        "О каком таракане идёт речь?"

        jump check_location



    elif tar_loc != 'home':

        glgg "Он же сейчас следит за [npc_name]"

        jump check_location




    # знакомство с тараканом
label tarakan_speech_about_killer:
    $ date_w_tarakan = True


    tar_pers "А хотя стой! Теперь моя очередь говорить."
    "Мой новый знакомый перебежал ко мне на кровать и продолжил:"
    tar_pers "У вас в городе объявился маньяк. И его надо обязательно найти и поймать. Иначе..."
    glgg "Стой-стой-стой! Ты почему разговариваешь вообще?"
    tar_pers "Это сейчас не так важно. Тут дело мирового масштаба. У вас маньяк в городе! Людей убивает! А тебе интересно как таракан разговаривает..."
    tar_pers "Слушай меня, сударь! Именно ты должен узнать, кто маньяк и остановить его. Я буду тебе помогать... Если появятся подозрения на кого-то - говори мне, я прослежу за ним и узнаю, чем он занимается"
    tar_pers "Ты всегда сможешь найти меня у себя дома, если я, конечно, не занят слежкой"
    glgg "Ладно, но... Почему ты разговариваешь?"
    tar_pers "Сударь, Вы дурак? Ну автор так захотел, я что сделаю?"
    glgg "Автор?"
    tar_pers "Ну ты дебил? Автор - это значит авторитет."
    glgg "Ладно..."
    tar_pers "Ну всё, до встречи, сударь. Я пошёл, у меня свои тараканьи дела."

    jump home







    # знакомство с маньяком в парке ночью
label killer_date:

    $ date_w_killer = True

    "На мгновенье показалось, что за мной кто-то наблюдает, как вдруг я почувстовал острое лезвие у совего горла."
    killer "Пошевелишься - убью."
    "Я был не в самом лучшем положении сейчас, потому не стал предпринимать какие-то действия. На кону была моя жизнь."
    killer "Молодец, а теперь вытаскивай все, что у тебя есть. Медленно, без резких движений."
    menu:
        "{color=#000000} Выполнить условия неизвестного\n{size=21}{i}потеря всех денег и вещей{/i}{/size}{/color}":

            "Я понимал, что лишусь ценных мне вещей, но делать было нечего. Я достал все, что у меня с собой было."
            killer "Умница."
            killer "А теперь спать."
            "Я не сразу понял, что он имел ввиду, пока не почувствовал странный запах от платка, который мне прижали к носу."
            "Веки резко потяжелели, и я отрубился..."
            




        "{color=#000000} Оказать сопротивление{/color}":

            "Такие условия меня не устривали. Я понимал, что рискую жизнью, но лишаться кровно заработанных денег мне совсем не хотелось."
            "Локтем я ударил мерзавца в живот, из-за чего тот загнулся"
            killer "Сука..."
            "Я было принялся накинуться на него, но почувствовал резкую боль в районе живота."
            "Мерзавец резким движением воткнул в меня нож."
            killer "Не недооценивай меня, паршивец."
            "Я упал на землю, истекая кровью, а убийца поспешил удалиться. Из-за темноты мне так и не удалось разглядеть его лица."
            "Сознание резко помутнилось и я отключился."


    show black with fade
    
    label morning_in_hospital:

        $ location_gg = 'hospital'

        $ hour = 11
        
        scene black with fade
        scene image "backgrounds/location/hospital/ward_day.jpg" with fade 

        # прописать дальше больничку

        "больничный леёбл"

        jump hospital_location




        # таракан рассказывает про призрака
label tarakan_speech_about_ghost:

    tar_pers "Ну здравствуй, сударь."
    glgg "И тебе привет."
    tar_pers "Дело для тебя есть."
    glgg "Что? Какое ещё дело?"
    tar_pers "Этот маньяк слишком часто ходит в лес. Я конечно могу предположить, что он там людей прячет, но я не верю, что у него столько жертв за один день"
    glgg "Ммм... А я что должен сделать?"
    tar_pers "Как-будто ты и сам не понял. Вам, сударь, надо будет ночью сходить в лес и узнать, что он там делает."
    glgg "Ну зачем? Тебе какая разница, чем он в лесу занимается, главное, что он там не людей убивает."
    tar_pers "А может и убивает! Вот сходи и узнай."
    glgg "Окей... Но тогда... Почему ночью?"
    tar_pers "Ночью маньяк ходит по парку в поиске жертвы, поэтому это самое безопасное для тебя время."
    tar_pers "Всё. Я ушёл. Не подкачай."
    jump home

    $ think_about_ghost = True



    #знакомство с призраком в лесу 
label date_ghost_label:


    "Я долго ходил по лесу в поисках чего-то непонятного, пока не услышал чей-то голос."
    ghost "{size=60}{glitch=60}У-у-у-у{/glitch}{/size}"
    "Я резко обернулся и увидел там..."
    #glgg "{sc=2}ПРИЗРАК?!{/sc}"
    glgg "ПРИЗРАК?!"
    show ggrltest with dissolve
    "Передо мной парил в воздухе силуэт молодой девушки в белом платье. Ее черные, как ночь, глаза смотрели прямо мне в душу."
    ghost "{size=60}{glitch=60}Ты меня видишь?{/glitch}{/size}"
    glgg "ПРОШУ, НЕ УБИВАЙ!"
    ghost "{size=60}{glitch=60}...{/glitch}{/size}"
    ghost "{size=60}{glitch=60}Ты идиот?{/glitch}{/size}"
    "Не понял. Она что не убьет меня?"
    ghost "{size=60}{glitch=60}Я не могу никого убить, даже если очень сильно захочу, так что не бойся меня.{/glitch}{/size}"
    ghost "{size=60}{glitch=60}Я всего лишь девушка, что умерла пару лет назад{/glitch}{/size}"
    glgg "..."
    ghost "{size=60}{glitch=60}Так что ты забыл в лесу, так еще и в такое время?{/glitch}{/size}"
    glgg "Честно говоря, я и сам не знаю. В лесу мне нужно найти то, сам не знаю что."
    ghost "{size=60}{glitch=60}А по-подробнее?{/glitch}{/size}"
    glgg "В городе завелся маньяк, и один мой... друг? Сказал, что он частенько ходит в лес, поэтому я и подумал, что смогу найти здесь хоть что-то, что поможет мне избавиться от этого мерзавца."
    ghost "{size=60}{glitch=60}Так значит его еще не поймали...{/glitch}{/size}"
    glgg "Всмысле? Ты его знаешь?"
    ghost "{size=60}{glitch=60}Да...{/glitch}{/size}"
    ghost "{size=60}{glitch=60}Это он убил меня.{/glitch}{/size}"
    glgg "Да ну нахуй."
    ghost "{size=60}{glitch=60}...{/glitch}{/size}"
    glgg "Извини, просто удивился. Так получается ты можешь мне помочь избавиться от него?"
    ghost "{size=60}{glitch=60}Думаю, что да. Но только при одном условии.{/glitch}{/size}"
    "Девушка посмотрела на меня хитрым взглядом и ехидно усмехнулась."
    ghost "{size=60}{glitch=60}Ты должен выполнить мои желания.{/glitch}{/size}"
    menu:
        "{color=#000000}Маньяк убивает людей. Какие ещё, к черту, желания?{/color}":
            ghost "{size=60}{glitch=60}Ну, ну, не горячись. Ты тоже меня пойми, я уже 6 лет торчу в этом лесу в полном одиночестве.{/glitch}{/size}"
            ghost "{size=60}{glitch=60}Быть призраком не так уж и легко, знаешь ли.{/glitch}{/size}"
            ghost "{size=60}{glitch=60}Я вообще не понимаю, как ты меня видишь и слышишь, ведь до этого меня никто не замечал{/glitch}{/size}"
            "Лицо девушки на мгновенье помрачнело"
            ghost "{size=60}{glitch=60}Пойми, мне просто скучно. Я не могу уйти на покой. Сама не знаю почему.{/glitch}{/size}"
            glgg "Ладно. Я выполню твои желания"
            ghost "{size=60}{glitch=60}Урра! Спасибо тебе, [player_name]{/glitch}{/size}"

        "{color=#000000} Хорошо. Я согласен{/color}":
            ghost "{size=60}{glitch=60}Ого. Я думала ты сразу же откажешься. Спасибо тебе, [player_name]{/glitch}{/size}"
    
    glgg "Да не за что. Стоп. А откуда ты знаешь как меня зовут?"
    ghost "{size=60}{glitch=60}Я же призрак. Я много чего знаю и умею.{/glitch}{/size}"
    "Девушка снова улыбнулась мне."
    glgg "Ну раз ты знаешь мое имя, то может скажешь мне свое?"
    ghost "{size=60}{glitch=60}Меня зовут Юмико. Юмико Агава.{/glitch}{/size}"
    glgg "Что ж, приятно познакомиться, Юмико"
    ghost "{size=60}{glitch=60}Знал бы ты, как мне приятно. [player_name]{/glitch}{/size}"
    "Мы потянули друг другу руки для рукопожатия, но рука моей новой знакомой прошла сквозь мою, от чего стало немного холодно."
    ghost "{size=60}{glitch=60}Ты забыл? Я же призрак.{/glitch}{/size}"
    "Я посмотрел на нее, потом на руку, потом опять на нее, и мы оба начали смеяться с этой нелепой ситуации."
    glgg "Ну так что, какие у тебя пожелания?"
    ghost "{size=60}{glitch=60}Хмм, дай-ка подумать.{/glitch}{/size}"
    ghost "{size=60}{glitch=60}Я хочу, чтобы ты купил мне пару новых платьев.{/glitch}{/size}"
    glgg "Чего..."
    ghost "{size=60}{glitch=60}Я же девушка и люблю красивые платья, вот и принеси мне их.{/glitch}{/size}"
    ghost "{size=60}{glitch=60}Хоть с людьми я взаимодейстовать и не могу, но вот с некоторыми предметами у меня немного получается{/glitch}{/size}"
    glgg "Ну хорошо, как скажешь."
    glgg "Есть какие-то предпочтения?"
    ghost "{size=60}{glitch=60}Хммм...{/glitch}{/size}"
    ghost "{size=60}{glitch=60}Выбери то, которое мне по твоему мнению подойдет.{/glitch}{/size}"
    "Юмико снова мило вам улыбнулась."
    glgg "Как скажешь."
    ghost "{size=60}{glitch=60}Ну что ж, жду тебя завтра с платьями. Приходи ко мне ночью в 00 00.{/glitch}{/size}"
    glgg "Хорошо, до завтра"
    hide ggrltest with dissolve
    "Как только я попрощался с Юмико, она сразу же куда-то исчезла..."
    glgg "..."
    glgg "И что это было?"

    $ date_w_ghost = True
    



label tarakan_speech_about_ghost:

    "Придя домой, я посешил"
    glgg "Эй, тараканище"











    # модифицированный лэйбл для знакомства с тараканом
label new_neighborn_mod:

    scene image room_path()[0]:
        size(1920, 1080)
    if items_in_room == 5:
        show image room_path()[2][0]
        show image room_path()[2][1]
        show image room_path()[2][2]
        show image room_path()[2][3]
        show image room_path()[2][4]
    elif items_in_room == 4:
        show image room_path()[2][0]
        show image room_path()[2][1]
        show image room_path()[2][2]
        show image room_path()[2][3]
    elif items_in_room == 3:
        show image room_path()[2][0]
        show image room_path()[2][1]
        show image room_path()[2][2]
    elif items_in_room == 2:
        show image room_path()[2][0]
        show image room_path()[2][1]
    elif items_in_room == 1:
        show image room_path()[2][0]
    if room_path()[0] == "backgrounds/location/ph/room_n_with_light.png" and window_room == True:
        show image 'backgrounds/location/room/room_n_with_light_window.png'
    if window_room == True and room_gg == 0:
        show image 'backgrounds/location/room/'+str(room_path()[3])+'/window.png'
    if room_path()[4] == 3:

        if not room_path()[0] == "backgrounds/location/ph/room_n_with_light.png":

            show image 'backgrounds/location/room/'+str(room_path()[3])+'/trash1.png':
                size(1920, 1080)
            show image 'backgrounds/location/room/'+str(room_path()[3])+'/trash2.png':
                size(1920, 1080)
            show image 'backgrounds/location/room/'+str(room_path()[3])+'/trash3.png':
                size(1920, 1080)

        else:

            if room_path()[0].find('backgrounds/location/ph/') <= -1:
                show image 'backgrounds/location/room/trash1.png':
                    size(1920, 1080)
                show image 'backgrounds/location/room/trash2.png':
                    size(1920, 1080)
                show image 'backgrounds/location/room/trash3.png':
                    size(1920, 1080)
            else:
                show image 'backgrounds/location/ph/'+str(room_path()[3])+'/trash1.png':
                    size(1920, 1080)
                show image 'backgrounds/location/ph/'+str(room_path()[3])+'/trash2.png':
                    size(1920, 1080)
                show image 'backgrounds/location/ph/'+str(room_path()[3])+'/trash3.png':
                    size(1920, 1080)

    elif room_path()[4] == 2:

        if not room_path()[0] == "backgrounds/location/ph/room_n_with_light.png":

            show image 'backgrounds/location/room/'+str(room_path()[3])+'/trash1.png':
                size(1920, 1080)
            show image 'backgrounds/location/room/'+str(room_path()[3])+'/trash2.png':
                size(1920, 1080)

        else:

            if room_path()[0].find('backgrounds/location/ph/') <= -1:
                show image 'backgrounds/location/room/trash1.png':
                    size(1920, 1080)
                show image 'backgrounds/location/room/trash2.png':
                    size(1920, 1080)
            else:
                show image 'backgrounds/location/ph/'+str(room_path()[3])+'/trash1.png':
                    size(1920, 1080)
                show image 'backgrounds/location/ph/'+str(room_path()[3])+'/trash2.png':
                    size(1920, 1080)
 
    elif room_path()[4] == 1:

        if not room_path()[0] == "backgrounds/location/ph/room_n_with_light.png":
            show image 'backgrounds/location/room/'+str(room_path()[3])+'/trash1.png':
                size(1920, 1080)
        else:
            if room_path()[0].find('backgrounds/location/ph/') <= -1:
                show image 'backgrounds/location/room/trash1.png':
                    size(1920, 1080)
            else:
                show image 'backgrounds/location/ph/'+str(room_path()[3])+'/trash1.png':
                    size(1920, 1080)

    $ new_neighborn_event = True
    'Спокойно отдыхая на своей кровати, ваш глаз заметил странное движение на краю поля зрения.'
    'Переключив своё внимание, вы вдруг поняли, что по стене ползёт таракан. Весьма крупное и усатое насекомое словно догадалось, что вы его заметили, и замерло на месте, видимо решив, что это ему поможет.'
    'В любом случае, его действия дали вам возможность подумать о том, что делать с этим новообретённым соседом.'

    menu:

        "{color=000000}Поговорить?..\n{size=21}2 энергии\nВозможность завести нового друга":

            $ energy -= 2
            'Посмотрев на таракана, вас вдруг наполнило непреодолимое желание побеседовать с ним.'
            'Первоначально разговор был не особо заурядными, однако, по ходу общения он приобретал более разнообразные темы: от обсуждения школьной политики до влияния цены продуктов на экономику.'
            'Насекомое тем временем даже не пошевелилось. Складывалось впечатление, словно он действительно слушает вас и размышляет на разные темы вместе с вами. Впрочем, уже спустя 30 минут вас это утомило.'
            'Похоже, что пришло время решать судьбу вашего недавнего собеседника.'
  
            menu:

                "{color=000000}Отпустить.\n{size=21}0 энергии":

                    glgg 'Хороший ты собеседник, однако. Иди себе с миром.'
                    robert_von_cockroach 'Благодарю вас, сударь.'
                    'Сказав это, насекомое поспешило удалиться, а вы стали думать какого хрена сейчас только произошло...'
                    $ robert_von_cockroach_friend = True

            $ minute += renpy.random.randint(30, 40)

    $ energy_minus(renpy.random.randint(1, 2))
    $ satiety_minus(renpy.random.randint(1, 2))
    $ minute += renpy.random.randint(5, 10)

    jump tarakan_speech_about_killer
