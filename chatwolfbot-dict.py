#encoding=utf8
#qpy:2
#qpy:console

import telepot, time, re, os, thread, random, math, datetime
from decimal import Decimal, localcontext
import telepot.api
global last_msg
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

last_msg={}
TOKEN = "255425760:AAEMpfezE0tU8Iom9jef9g-d1wnVUVwwVrw"
bot = telepot.Bot(TOKEN)
def in_nest(search,list):
    for i in list:
        if search in i:
            return True
            break
    return False
def handle(msg):
    global last_msg
    content_type, chat_type, chat_id = telepot.glance(msg)
    idn=str(msg["from"]["id"])
    idg = str(chat_id)
    z = 0
    banned=0
    banned_words=["yiff","http",".com",".net",".org",".es",".co.uk","nuke","triggered"," puto"," puta"," soputa","penis","dick","cunt","fag","pene","vagina","gilipollas","cum","fucker"]
    if content_type=="text":
        for i in banned_words:
            if i in msg["text"]:
                banned=1
                
    if content_type=="text" and not banned==1:
        text=msg["text"].replace("\n","%$space%$")
        
        try:
            f=open("storage/emulated/0/qpython/scripts/brain.txt","r")
            f.close()
        except:
            f=open("storage/emulated/0/qpython/scripts/brain.txt","w")
            f.write("hi%%@$Hello%%@$Heya!\nhow are you?%%@$Fine!")
            f.close()
        learned={}
        with open("storage/emulated/0/qpython/scripts/brain.txt") as f:
            for line in f:
                if len(line)>4:
                    print line
                    (key,value)=line.split("%%@$",1)
                    value=value.replace("\n","").split("%%@$")
                    learned[key]=value
        
            
        if msg["chat"]["type"]=="private" or "chatwolf" in text.lower():
            priv=text.lower()
            priv=priv.replace(" ,chatwolf ","")
            priv=priv.replace(" chatwolf,",",")
            priv=priv.replace(", chatwolf","")
            priv=priv.replace("chatwolf, ","")
            priv=priv.replace(" chatwolf "," ")
            priv=priv.replace(" chatwolf","")
            priv=priv.replace("chatwolf ","")
            priv=priv.replace("chatwolf","")
            print priv
            sent=0
            if priv in learned.keys():
                if not msg["chat"]["id"]=="91692492":
                    bot.sendMessage(chat_id, learned[priv][random.randrange(0,len(learned[priv]))].replace("%$space%$","\n"))
                    sent=1
            if priv=="":
                bot.sendMessage(chat_id,"What do you want?")
            elif sent==0:
                bot.sendMessage(chat_id,"I dont know a reply yet")
        else:
            if not chat_id in last_msg:
                last_msg[chat_id]=text.lower()
            elif last_msg[chat_id]!="":
                try:
                    if not last_msg[chat_id] in learned:
                        learned[last_msg[chat_id]]=[text]
                    else:
                        learned[last_msg[chat_id]].append(text)
                except Exception as E:
                    print E
            
                if text not in learned[last_msg[chat_id]]: 
            	      learned[last_msg[chat_id]].append(text)
            
            last_msg[chat_id]=text.lower()
            wrt=""
            with open("storage/emulated/0/qpython/scripts/brain.txt","w")as f:
                f.close()
           
            f=open("storage/emulated/0/qpython/scripts/brain.txt","w")
            for i in learned.keys():
                f.write(i+"%%@$"+"%%@$".join(learned[i])+"\n")
            f.close
            print learned
      
            #print last_msg
        #print learned
            #print wrt
        print text.encode("utf-8")
bot.message_loop(handle)
while("true"):
    time.sleep(1)