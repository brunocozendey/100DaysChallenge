import smtplib
import time
import imaplib
import email
from lxml import html
from bs4 import BeautifulSoup


file = open("/home/bruno/Desktop/senha.txt","r")

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "brechotech" + ORG_EMAIL
FROM_PWD    = file.read()
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')


        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[-2])
        #latest_email_id = int(id_list[-1])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )
            
            for response_part in data:
                soup = BeautifulSoup(response_part[1], 'html.parser')
                for td in soup.find_all('td'):
                    if ":" in td.get_text():
                        print(td.get_text())
                    #print(td.get_text())

                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'
                    print(msg)
                    print(type(msg))
                    #print(msg.xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td'))
                    #soup = BeautifulSoup(msg, 'html.parser')
                    soup = BeautifulSoup(msg, 'html.parser')
                    print(soup.get_text())

    except Exception, e:
        print str(e)

while True:
    print("--------------------------------------")
    print("Lendo emails")
    print("--------------------------------------")
    read_email_from_gmail()
    print("Termino leitura de emails!")
    break
    
