#!/usr/bin/python3


import requests, bs4 , webbrowser ,
		smtplib, ssl



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

context = ssl.creat_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com" , port, context=context) as sever:
	server.logiin("mcbeeffserver@gmail.com" , password)

print("done")
