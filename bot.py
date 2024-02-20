import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6569891735:AAGmrfy-CF3_scVWMPV8OSwwvWImbCAPihM")

API_ID = int(os.environ.get("API_ID", "14084834"))

API_HASH = os.environ.get("API_HASH", "3370f5b5ed3ac5ad6931724413f529f6")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
