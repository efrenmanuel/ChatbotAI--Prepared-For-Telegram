# -*- coding: utf-8-*-


import telepot, time, re, os, json, numpy, decimal,AI
from decimal import Decimal, localcontext
import telepot.api
global last_msg

estatus=1

TOKEN = "TOKEN"
bot = telepot.Bot(TOKEN)

def talk(text, estatus):
    import AI
    rawdata=AI.talk(text,estatus)
    return(rawdata)

    

def listen(text,chat,estatus, *args):
    AI.learn(text,chat,estatus, *args)

def handle(msg):
    estatus=1
    content_type, chat_type, chat_id = telepot.glance(msg)
    idn=str(msg["from"]["id"])
    idg = str(chat_id)
    banned=0
    banned_words=["yiff","http",".com",".net",".org",".es",".co.uk","nuke","triggered"," puto"," puta"," soputa","penis","dick","cunt","fag","pene","vagina","gilipollas","cum","fucker"]
    if content_type=="text":
       
        for i in banned_words:
            if i in msg["text"]:
                banned=1
                break
    if content_type=="text" and not banned==1:
        reply=0
        try:
            if msg["reply_to_message"]["from"]["username"]==botname:
                reply=1
        except:
            reply=0
        text=msg["text"].replace("\n","%$space%$").replace("\"","%$quote%$").replace("\'","%$quot%$").replace("\{","%$dic1%$").replace("\}","%$dic2%$")

        if chat_type=="private" or botname.lower() in text.lower() or reply:
            bot.sendMessage(chat_id,talk(text.replace(botname,"").replace(botname.lower(),"").replace("$$$$$$&&","\\U").replace("$$&&$$&&","\\u").replace("%$space%$","\n").replace("%$quote%$","\"").replace("%$quot%$","\'").replace("%$dic1%$","\{").replace("%$dic2%$","\}"))
        else:
            try:
                listen(text,str(chat_id),estatus, msg["reply_to_message"]["text"])
            except:
                listen(text,str(chat_id),estatus)
            
bot.message_loop(handle)
while("true"):
    time.sleep(1)
