def send_email(message, recipient, *, sender='university.help@gmail.com'):
    necessarily = ('.com', '.ru', '.net')

    def valid_email(email):
        return '@' in email and email.endswith(necessarily)

    if not valid_email(sender) or not valid_email(recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Привет!', 'example@gmail.com')
send_email('Привет!', 'example@gmail.com', sender='support@company.com')
send_email('Привет!', 'example@gmail.com', sender='invalid-email')
send_email('Привет!', 'university.help@gmail.com', sender='university.help@gmail.com')
