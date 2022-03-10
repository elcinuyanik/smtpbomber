import sys
import os.path
import smtplib
import random
import string
import nameslist
from getpass import getpass


def get_email_list():
    email_list = []
    email_providers = ["yahoo", "gmail", "hotmail", "outlook"]
    tlds = [".com", ".co.uk", ".net", ".au", ".org"]
    for i in range(10):
        random_numbers = random.randint(1, 10)
        random_server_sel = "@" + random.choice(email_providers) + random.choice(tlds)
        randnames = random.choice(nameslist.Names)
        random_2lettercomb = ''.join(random.choice(string.ascii_letters) for x in range(5))
        email_list.append(randnames + random_2lettercomb + str(random_numbers) + random_server_sel)
    print("Mail listesi oluşturuldu.")
    return email_list


server = input("Mail Server Giriniz:")
port = int(input("Port Giriniz:"))
mailfrom = input("Gönderici Adresi Giriniz:")
password = getpass(mailfrom + " Adresinin Şifresini Girin: ")
message = ''

if len(sys.argv) >= 1:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('File "' + filename + '" not found.')
        sys.exit(0)
    with open(filename) as f:
        message = f.read()

smtp = None

try:
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(mailfrom, password)
    rcpt = get_email_list()
    smtp.sendmail(mailfrom, rcpt, message)
except Exception as e:
    print('Failed to send mail.')
    print(str(e))
else:
    print('Succeeded to send mail.')
