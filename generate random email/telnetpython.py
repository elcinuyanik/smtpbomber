import os.path
import random
import string
import nameslist
from SimpleTelnetMail import TelnetMail


def get_email_list(totalrcpt):
    dummy_list = []
    email_providers = ["yahoo", "gmail", "hotmail", "outlook"]
    tlds = [".com", ".co.uk", ".net", ".au", ".org"]
    for i in range(random.randint(totalrcpt, totalrcpt)):
        random_numbers = random.randint(0, 9)
        random_server_sel = "@" + random.choice(email_providers) + random.choice(tlds)
        dummy = random.choice(nameslist.Names)
        random_2lettercomb = ''.join(random.choice(string.ascii_letters) for x in range(2))
        dummy_list.append(dummy + random_2lettercomb + str(random_numbers) + random_server_sel)
    print("Gönderilecek Dummy Mail Adresleri: " + str(dummy_list))
    return dummy_list


totalrcpt = int(input("Gönderilecek Mail Adedi Girin: "))
emlfile = random.choice(os.listdir("/home/elcin/PycharmProjects/generate/emlfiles"))
print("Gönderilecek eml Dosyası: " + emlfile)

try:
    """EXAMPLES:
    SimpleTelnetMail - -host = "smtp.server.com" - -
    from="my.address@domain.com" - -to = "receiver@domain.com" - -message = "my email message""""
    client = TelnetMail("host", port="port", from_="mailfrom", to=get_email_list(), message="emlfile")
    client.send_mail()
except Exception as e:
    print('Failed to send mail.')
    print(str(e))
else:
    print('Succeeded to send mail.')