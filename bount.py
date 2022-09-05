# ветвление игры бессмысленные факты
# Игра угадай слово из четверостишья 
# С пасхалкой на слова член, хуй и хер при запросе готов ли игрок начать игру
# Усть и пасхалки на слова пизда, в пизду, пиздуй при запросе готов ли игрок начать игру
import random
name = input("\aВведите свое имя ")
print("\aПриветствую тебя " + name)
print("\aТы попал/a в одну из ветвей программы 'Бессмысленные факты', похоже ответил/а неправило на контрольный вопрос")
print("Игра называется 'Угадай слово'")
print("Тебе будет предложено несколько стихотворений на английском языке,\nтвоя задача, выбрать и написать название стихотворения.")
print("Я загадаю случайное слово из предложенного отрывка, без каких либо знаков, прям то же самое слово что и отрывке. Регистр имеет знечение")
branching = input("\aГотов/а начать игру? " + name + " ")

yes = "Да"
no = "Нет"

kipling = "If"
Wordsworth = "Daffodils"

dick = "Член"
dick1 = "Хуй"
dick2 = "Хер"

pussy = "Пизда"
pussy1 = "В пизду"
pussy2 = "Пиздуй"

random_word_tyger = random.choice(list(["\aTyger" "Tyger" "burning" "bright" 
"In" "the" "forests" "of" "the" "night"
"What" "immortal" "hand" "or" "eye"
"Could" "frame" "thy" "fearful" "symmetry"]))

random_word_if = random.choice(list(["If" "you" "can" "dream"  "and" "not" "make" 
"dreams" "your" "master"" think" "thoughts" "your" "aim"
 "meet" "with" "Triumph" "Disaster" "And" "treat" "those" "two" "impostors" "just" "the" "same"]))

# вспомогательная переменная для цикла while
counter = 0


if branching == yes:
    print( name + " я загадываю случайное слово из следующего отрывка стихотворения 'The tyger' Вильяма Блэйка")
    print("\aTyger! Tyger! burning bright\nIn the forests of the night,\nWhat immortal hand or eye\nCould frame thy fearful symmetry?")

    for counter in range(4):
        user_input = input("\aВводи свой вариант, у тебя 4 попыток ")
        print( "Твой ответ " + user_input )
        input("\n\aНажми Enter чтобы продолжить")
        if user_input != random_word_tyger:
            print( name + " неверно")
        else:
            print(name + " поздравляю! Это был совершенно верный ответ!")
            break
    else:
        print("Ты проиграл/а ((")
elif branching == dick or dick1 or dick2:
    print("Ты нашла или нашел пасхалку, поздравляю!")
    print("Несколько фактов про мужской половой орган. В качестве сюрприза попробую угадать размер твоего члена, если он у тебя есть.\n Или, если ты девушка, представим какой был бы у тебя член))")
    input("\n\aНажми Enter чтобы продолжить, пошлый друг или подруга))")
    print("Основываясь на отчёте UNAIDS и WHO (Всемирная Организация Здравоохранения) 2007 года, 30% мужчин старше 15 лет обрезаны. Некоторые исследования доказали, что обрезание снижает риск заражения ВИЧ-инфекцией у гетеросексуалов. Дабы привести ещё один аргумент в пользу обрезания, напомним, что Американская Академия Педиатрии (ААП) в 2012 году заявила: 'Оценка текущих данных показывает, что польза обрезания для здоровья новорожденного перевешивает риски, а выгода процедуры оправдывает её доступность'.")
    input("\n\aНажми Enter чтобы продолжить, пошлый друг или подруга))")
    print("Долгое время титул обладателя самого огромного члена принадлежал 43-летнему Йохану Фэлкону из Нью-Йорка, 'меч' которого достигал 33 см. Но в этом году нашёлся новый экземпляр, по сравнению с которым 'меч' Мистера Фэлкона выглядит как небольшой штопор. Роберто Эскувэль Карбреа обладает впечатлительными 48 см. Вот это да!")
    input("\n\aНажми Enter чтобы продолжить, пошлый друг или подруга))")
    print('Часто говорят: "Вы знаете, что означает большой размер ноги...". Фраза подразумевает, что мужчины с большими ногами обладают большим членом, но на самом деле это говорит только о том, что они носят большие ботинки. Не существует научного исследования, которое бы показало отношение размера ноги к размеру пениса.\nПрошу прощения, если это читает цирковой клоун, но, во имя науки, этот миф нужно было разрушить.')

elif branching == kipling:
    print("\aТы выбрал/а стихотвопение If R. Kipling\nЯ выбрал следующий отрывок")
    print("\aIf you can dream - and not make dreams your master;\nIf you can think - and not make thoughts your aim,\nIf you can meet with Triumph and Disaster\nAnd treat those two impostors just the same:")
    input("\n\aНажми Enter чтобы продолжить")
    for counter in range(4):
        user_input = input("\aВводи свой вариант, у тебя 4 попыток ")
        print( "Твой ответ " + user_input )
        input("\n\aНажми Enter чтобы продолжить")
        if user_input != random_word_tyger:
            print( name + " неверно")
        else:
            print(name + " поздравляю! Это был совершенно верный ответ!")
            break
    else:
        print("Ты проиграл/а ((")
elif branching == Wordsworth:
    print("Ты выбрал/а стих Нарциссы.Daffodils. Уильям Вордсворт. " + name)
    input("\n\aНажми Enter чтобы продолжить")
    print("Я выбрал следующий отрывок этого стихотворения")
    print("I wandered lonely as a cloud\nThat floats on high o'er vales and hills,\nWhen all at once I saw a crowd,\nA host, of golden daffodils;\nBeside the lake, beneath the trees,\nFluttering and dancing in the breeze.")
    input("\n\aНажми Enter чтобы продолжить")
    for counter in range(4):
        user_input = input("\aВводи свой вариант, у тебя 4 попыток ")
        print( "Твой ответ " + user_input )
        input("\n\aНажми Enter чтобы продолжить")
        if user_input != random_word_tyger:
            print( name + " неверно")
        else:
            print(name + " поздравляю! Это был совершенно верный ответ!")
            break
    else:
        print("Ты проиграл/а ((")