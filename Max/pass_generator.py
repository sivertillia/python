from random import randint as rnd
import pyperclip
import plyer


a = '1234567890`~!@#$%^&*()_+-=[]{};:\|,./<>?qwertyuiopasdfghjklzxcvgbhnmQWERTYUIOPASDFGHJKLZXCVBNM'
new_a = a
lenght_pass = rnd(8, 15)

asd = len(new_a) - 1
password = ''
while len(password) <= lenght_pass:
    randint = rnd(0, asd)
    password = password + new_a[randint]
    asd = len(new_a) - 1

plyer.notification.notify(message='Пароль помещен в буфер обмена', title='Пароль сгенерирован')

pyperclip.copy(password)
spam = pyperclip.paste()