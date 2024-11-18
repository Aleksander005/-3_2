# Задача "Рассылка писем":
def send_email(sms, recipient, senter="university.help@gmail.com"):  # Создайте функцию send_email,
    if (
            "@" not in recipient or # МОЖЕМ ЛИ НАПИСАТЬ сразу в эту же строку senter??????????
            (".com" not in recipient and ".ru" not in recipient and ".net" not in recipient) or
            "@" not in senter or
            (".com" not in senter and ".ru" not in senter and ".net" not in senter)
    ):
        print("Невозможно отправить письмо с адреса", senter, "на адрес", # В Вашей версии senter как {senter}, для чего в словаре ???????
              recipient)  # Проверка на корректность e-mail отправителя и получателя
    elif recipient == senter:  # же sender и recipient совпадаю
        print('Нельзя отправить письмо самому себе!')  # то вывести
    elif senter == "university.help@gmail.com":  # отправитель по умолчанию
        print("Письмо успешно отправлено с адреса", senter, "на адрес", recipient)
    elif senter != "university.help@gmail.com":  # В противном случае
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", senter, "на адрес", recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', senter='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', senter='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', senter='urban.teacher@mail.ru')
