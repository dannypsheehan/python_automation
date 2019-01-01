import requests, sys, webbrowser, bs4

res = requests.get('https://github.com/ehmatthes/pcc/blob/master/chapter_18/README.md)'

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

print(res.text)