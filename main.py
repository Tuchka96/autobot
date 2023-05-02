from analizer_lib.analyser import detect_subject, \
    detect_topic, avtomat, preparation, timetable, \
    place, contacts

print("""              
                        Вас приветствует АВТОБОТ. 
            Моя задача помочь вам спастить от СЕССИИ путем АВТОМАТА
    Вы можете узнать, что необходимо ПРИНЕСТИ В ЖЕРТВУ, чтобы получить АВТОМАТ
        Напишите мне интересующую вас дисциплину или преподавателя, 
               чтобы получить заветную секретную информацию
                Чтобы закончить общение со мной введите exit""")
message = 0
while message != "exit":
    message = input("Введите интересующую вас ДИСЦИПЛИНУ: ")
    if message == "exit":
        break
    subject = detect_subject(message)
    if subject == False:
        print("Все фигня, давай по новой")
        continue
    zapros = input("С предметом мы разобрались. Что же вы хотите узнать?")
    if zapros == "exit":
        break
    topic = detect_topic(zapros)
    if topic == False:
        print("Все фигня, давай по новой")
        continue

    if topic == "auto":
        avtomat(subject)
    elif topic == "education":
        preparation(subject)
    elif topic == "timetable":
        timetable(subject)
    elif topic == "place":
        place(subject)
    elif topic == "contacts":
        contacts(subject)
### есть 3 предмета: математика, питон и литература
### и 5 тем вопросов 1) автомат, 2) место проведения