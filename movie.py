#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
import requests
url=""
r = requests.get(url)
files = r.json()
print(len(files))
f = open('events.txt')  
content_list = f.readlines()
f.close()
update_id = None

def present(id):
    if id+'\n' in content_list:
        return 1
    else:
        return 0   


def main():
    global update_id
    bot = telegram.Bot('')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    with open('events.txt','a+') as fd:
        content_list = fd.readlines()
        for i in range(len(files)):
            id=files[i]['videos_id']
            if not present(id):
                print(id+'\n')
                movieName = files[i]['title'].replace('#','\#')
                bot.send_photo("",files[i]['thumbnail_url'], caption=f"{movieName} added\. [Download here](/movie-info.html?id={files[i]['videos_id']})\. For more updates, join ", parse_mode='MarkdownV2')
                fd.write(files[i]['videos_id'])
                fd.write('\n')

if __name__ == '__main__':
    main()
