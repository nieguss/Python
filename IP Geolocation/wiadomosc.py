"""
    This code allows you to geo locate your IP address and send it to your mail using gmail account.
"""


import smtplib
import urllib.request as ureq
import json

url = "https://extreme-ip-lookup.com/json"
gmail_user = 'XXX'              # change XXX with your gmail addres for sending mail
gmail_pass = 'xxx'          # change xxx with your gmail pass for sending mail
ip_inf = json.load(ureq.urlopen(url))
new_body = []

for param, val in ip_inf.items():
    to_append = f"{param.upper()}{' ' * (15 - len(param))}: {val if len(val) != 0 else 'NA'}"
print(to_append)
new_body.append(to_append)

sent_from = gmail_user
to = ['XYZ']                    # change XYZ to your receiving mail account
subject = 'Geo-location'
body = json.dumps(ip_inf)

email_text = """
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_pass)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Succes!')
except:
    print('Something went wrong with connection!')
