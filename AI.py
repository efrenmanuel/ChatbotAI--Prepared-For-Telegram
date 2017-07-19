# -*- coding: utf-8 -*-
#Developed by Efrén Glez. @daerok_bot in telegram.
import json, numpy

from decimal import Decimal
from difflib import SequenceMatcher as comp


#compares two words to choose the best

def compare(a,b):                                 
  return(comp(None,a,b).ratio())
#here it decides what to reply
def talk(inp, estatus):
  rawinp=inp
  
  #we transform our raw input into something more manejable
  
  inp=inp.lower().split(" ")
  estatus="p"+str(estatus)

  #here we load the database

  p=json.load(open(estatus+".json"))

  #we check for each word in the db

  for word in inp:

    #here it checks if the dic finished already

    if isinstance( list(p.values())[0], int ):
      break
    else:

      #here it tries to find that plain word
      
      try:
        p=p[word]
        
      #here it finds the most similar one
        
      except Exception as e:
#        print(e)
        probs=[]
        for key in list(p.keys()):
          probs.append(compare(word,key))
        big=0
        for i in range(0,len(probs)):
#          print(probs[i])
          if probs[i]>probs[big]:
            big=i
        p=p[list(p.keys())[big]]
        
  #checks if there is a plain response, otherwise, it uses random words to aproach an end

  while not isinstance( list(p.values())[0], int ):
    p=p[numpy.random.choice(list(p.keys()))]
  out=p
  #print(out)
  return (out)


def learn(inp, chat, estatus, *args):
  print(args)
  rawinp=inp
  inp=inp.lower().split(" ")
  try:
    lastmsg=eval(open("lastmsg.json").read())
    try:
      last=lastmsg[chat]
    except:
      lastmsg[chat]=[""]
      last=lastmsg[chat]
      with open("lastmsg.json","w") as f:
        json.dump(lastmsg, f, indent=4)
  except:
    dic={chat:[""]}
    with open("lastmsg.json","w") as f:
      json.dump(dic, f, indent=4)
    lastmsg=eval(open("lastmsg.json").read())
    last=str(lastmsg[chat].decode("utf-8"))
    print(last)
  try:
    last=args[0].split(" ")
  except:
    pass
    


  if last!=[""]:
    estatus="p"+str(estatus)
    
    #here we load the database
    answ=json.load(open("answ.json"))
    if rawinp not in list(answ.values()):
      number=str(len(answ)+1)
      answ[number]=rawinp
      json.dump(answ, open("answ.json","w"), indent=4)
    else:
      for i in answ:
        if answ[i]==rawinp:
          number=i
    past=json.load(open(estatus+".json"))
    dic="["
    for i in last:
      print(i.encode("unicode_escape").decode("utf-8", "surrogateescape"))
      dic=dic+"'"+i.encode("unicode_escape").decode("utf-8", "surrogateescape")+"']["
    dic=dic+"'"+number+"']"
    try:
      exec('''try:
  past{0} = past{0}+1
except:
  past{0}=1'''.format(dic.format("utf-8", "surrogateescape")))
    except:
      dic=u"["
      for i in last:
        dic=dic+"'"+i+"']"
        #print(dic)
        exec('''try:
  past{0} = past{0}+1
except:
  past{0} = {1}'''.format(dic.encode("unicode_escape").decode("utf-8", "surrogateescape"),{}))
        dic=dic+"["
      dic=dic+"'"+number+"']"
      #print(dic)
      exec('''try:
  past{0} = past{0}+1
except:
  past{0} = 1'''.format(dic.encode("unicode_escape").decode("utf-8", "surrogateescape")))
    with open(estatus+".json","w") as f:
        json.dump(past, f, indent=4)
    past=""

  last="[u'"+" ', u'".join(inp)+"']"
  last=eval(last)
  lastmsg[chat]=last
  with open("lastmsg.json","w") as f:
      json.dump(lastmsg, f, indent=4)

if __name__ == '__main__':
  talk()
  learn()
