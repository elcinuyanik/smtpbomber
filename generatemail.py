import random
import string
import nameslist

"Names"
"From nameslist.py"



email_providers = ["yahoo","gmail","hotmail","outlook"]
tlds = [".com",".co.uk",".net",".au",".org"]

for i in range (20):
    random_numbers = random.randint(1,10)
    random_server_sel = "@"+random.choice(email_providers)+random.choice(tlds)
    randnames = random.choice(nameslist.Names)
    random_2lettercomb = ''.join(random.choice(string.ascii_letters) for l in range (1))
    print(randnames+random_2lettercomb+str(random_numbers)+random_server_sel)

