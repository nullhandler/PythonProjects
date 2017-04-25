import requests
import bs4, webbrowser, sys

print('Search for:')
key = input()
print('Searching.....')
page = requests.get('https://www.google.co.in/search?q=%s' %key)
soup = bs4.BeautifulSoup(page.text)
element = soup.select('.r a')

for i in range(2):
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('https://google.com'+element[i].get('href'))
