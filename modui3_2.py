# Задача "Рассылка писем":
def send_email(сообщение, получатель, отправитель="university.help@gmail.com"):  # Создайте функцию send_email,
    if отправитель not in ("@" or ".com" or ".ru" or ".net") and получатель not in ("@" or ".com" or ".ru" or ".net"):
        print("Невозможно отправить письмо с адреса", отправитель, "на адрес",
              получатель)  # Проверка на корректность e-mail отправителя и получателя
    elif получатель == отправитель:  # же sender и recipient совпадаю
        print('Нельзя отправить письмо самому себе!')  # то вывести
    elif отправитель == "university.help@gmail.com":  # отправитель по умолчанию
        print("Письмо успешно отправлено с адреса", отправитель, "на адрес", получатель)
    elif отправитель != "university.help@gmail.com":  # В противном случае
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", отправитель, "на адрес", получатель)
    #elif bool == False:


# print(f'Невозможно отправить письмо с адреса {отправитель} на адрес {получатель}')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', отправитель='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', отправитель='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', отправитель='urban.teacher@mail.ru')

