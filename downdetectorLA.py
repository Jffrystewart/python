#!/usr/bin/python3


import requests, bs4 , webbrowser , smtplib, ssl


sender_email = "mcbeeffserver@gmail.com"
receiver_email = "jffrystwrt@gmail.com"
smtp_server = "smtp.gmail.com"

spectrumurl = 'https://downdetector.com/status/spectrum/los-angeles/'
webbrowser.open(spectrumurl)
res = requests.get(spectrumurl)


elems = bs4.BeautifulSoup(res.text, 'html.parser')
type(elems)

img = elems.find('div', {'class': "charjs-size-monitor-shrink"})

if img == []:
	print("no idea what this is")
else:
	print("Got it!")


port = 465
password = input("Please enter a password")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server , port , context=context) as server:
	server.login(sender_email , password)
	server.sendmail(sender_email , receiver_email , img )



print("done")
