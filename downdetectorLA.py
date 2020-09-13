#!/usr/bin/python3


import requests, bs4 , webbrowser



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




print("done")
