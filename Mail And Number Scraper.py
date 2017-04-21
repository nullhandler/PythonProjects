# Made by Selva
# Made with ❤ in Selvasoft

import re
import pyperclip

#This function checks for number
def listnum(data):
    phonereg = re.compile(r'\+91\d\d\d\d\d\d\d\d\d\d') #Scraps only India phone number
    numlist = phonereg.findall(data)
    return numlist

#This function checks for mail ID
def listmail(data):
    mailreg = re.compile(r'\w+@\w+.com')
    maillist = mailreg.findall(data)
    return maillist

text_in_clipboard = str(pyperclip.paste()) #Copy the text in clipboard
numlist = listnum(text_in_clipboard)
maillist = listmail(text_in_clipboard)

print('The Mail IDs in the list are:')
for i in maillist:
    print('* ' + i) #Bullet points

print('The Numbers in the list are:')
for i in numlist:
    print('* ' + i) #Bullet points
