import whois
import datetime
import requests
from urllib.parse import urlencode


current_date = datetime.date.today()

domains = ['exampledomain1.com', 'exampledomain2.com']


# SEND SMS FUNCTION
def send_sms():
    phone = 'phone number'
    recipient = 'country code' + phone.lstrip('0')
    body = "Your domain {} expires in {} days.".format(i, days_to_expire)

    url = "https://api.hubtel.com/v1/messages"

    payload_dict = {
          "Content" : body,
          "From" : 'SenderID',
          'To': recipient,
          'Direction': 'out',
        }

    payload = urlencode(payload_dict)

    headers = {

        'authorization': "Authorisation code",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

# END SEND SMS FUNCTION

for i in domains:
    x = whois.whois(i)
    exp_date = x.expiration_date.date()
    days_to_expire = (exp_date - current_date).days

    if days_to_expire < 10: #days to set to 10 days.
        send_sms()
