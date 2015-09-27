import requests
import time
import random
import re
import string as String

EMAIL = "leavethemails@gmail.com"   # Gmail address
REFERRAL_CODE = "PXDP3Y"               #5-6character reservation ID


# Randomly place dot with following criteria:
# - Not at start or end
# - Atleast two characters inbetween the dot (Seems like only one character seperation is usually rejected)

## THIS EXPLOIT HAS BEEN PATCHED ALREADY ##


def random_dotify(address, separator=2):
    split = address.split('@')
    while True:
        account = split[0]
        index = 1
        while index < len(account)-1:
            if random.random() < 0.5:
                account = account[:index] + "." + account[index:]
                index += separator
            index += 1
        yield account + '@' + split[1]

for email in random_dotify(EMAIL):
    requestURL = "https://invites.oneplus.net/index.php?r=share/signup&success_jsonpCallback=success_jsonpCallback&email={0}&koid={1}&_=1438677876942".format(email.replace("@", "%40"), REFERRAL_CODE)
    print("Sending invite to " + email)
    res = requests.get(requestURL)
    while res.status_code != 200:
        print("Request failed. "+str(res.status_code))
        time.sleep(5)
        res = requests.get(requestURL)
    print("Successfully retrieved response")
