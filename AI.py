<<<<<<< HEAD
# -*- coding: utf-8 -*-
#Developed by Efrén Glez. @daerok_bot in telegram.
import json, numpy

from decimal import Decimal
from difflib import SequenceMatcher as comp


#compares two words to choose the best
def gen(i):
  answ=json.load(open("answ.json"))
  answ=answ[i]
  print(answ)
  text=[]
  ended=False
  while ended == False:
    listkey=[]
    probs=[]
    totalprob=0
    for i in answ:
      listkey.append(i)
      print(i)
      probs.append(int(answ[i][0]))
      print(probs)
    for i in probs:
      totalprob+=i
    for i in range (0,len(probs)):
      try:
        probs[i]=Decimal(probs[i])/totalprob
        print(probs)
      except:
        raise
        probs[i]=0
    print(probs)
    chosen=numpy.random.choice(listkey,p=probs)
    text.append(chosen)
    print(text)
    answ=answ[chosen][1]
    if answ=={}:
      ended=True
  return(" ".join(text))

def isall(list,type):
  for i in list:
    if not isinstance(i,type):
      return(False)
  return(True)
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

    if isall(list(p.values()), int ):
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
  while isall(list(p.values()), dict):
    p=p[numpy.random.choice(list(p.keys()))]
  for i in p.keys():
    if isinstance(p[i],int):
      intkey=i
  out=gen(i)
  print(out)
  return(out)


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
    lastmsg=json.load(open("lastmsg.json"))
    last=str(lastmsg[chat].decode("utf-8")).split(" ")
    print(last)
  try:
    last=args[0].split(" ")
  except:
    pass
    


  if last!=[""]:
    estatus="p"+str(estatus)
    #here we load the database
    database=json.load(open(estatus+".json"))
    db=database
    answ=json.load(open("answ.json"))
    for word in last:
      print(word)
      try:
        db=db[word]
      except:
        db[word]={}
        db=db[word]
    print(db)
    if db=={} or isall(list(db.values()),dict):
      print("mode1")
      db[str(len(list(answ.keys())))]=1
      answ[str(len(list(answ.keys())))]={}
      an=answ[str(len(list(answ.keys()))-1)]
      an[inp[0]]=[1,{}]
      an=an[inp[0]]
      for word in inp[1:]:
        print(an)
        an[1][word]=[1,{}]
        an=an[1][word]
        print(answ)
    else:
      #print(db)
      for entry in db.keys():
        try:
          an=answ[str(int(entry))]
          print(an)
          try:
            an=an[inp[0]]
            print(an)
          except:
            an[inp[0]]=[1,{}]
            an=an[inp[0]]
            print(an)
          if len(inp)>1:
            for word in inp[1:]:
              try:
                an[0]=an[0]+1
                an=an[1][word]
              except:
                an[1][word]=[1,{}]
                an=an[1][word]
          break
        except:
          pass
        
  lastmsg[chat]=inp
  with open("lastmsg.json","w") as f:
      json.dump(lastmsg, f, indent=4)
  with open("answ.json","w") as f:
      json.dump(answ, f, indent=4)
  with open(estatus+".json","w") as f:
      json.dump(database, f, indent=4)

if __name__ == '__main__':
  talk()
  learn()
=======
# -*- coding: utf-8 -*-
#Developed by Efrén Glez. @daerok_bot in telegram.
import json, numpy

from decimal import Decimal
from difflib import SequenceMatcher as comp


#compares two words to choose the best
def isall(list,type):
  for i in list:
    if not isinstance(i,type):
      
      return(False)
  return(True)
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

    if isall(list(p.values()), int ):
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
  intkeys=[]
  while isall(list(p.values()), dict):
    p=p[numpy.random.choice(list(p.keys()))]
  for i in p.keys():
    if isinstance(p[i],int):
      intkeys.append(i)
  out={}
  for i in intkeys:
    out[i]=p[i]
  print(out)
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
          break
    past=json.load(open(estatus+".json"))
    dic="["
    for i in last:
      print(i.encode("unicode_escape").decode("utf-8", "surrogateescape"))
      dic=dic+"'"+i.encode("unicode_escape").decode("utf-8", "surrogateescape")+"']["
    dic=dic+"'"+number+"']"
    print(dic)
    try:
      exec('''try:
  past{0}=past{0}
except:
  past{0}={}'''.format(dic.format("utf-8", "surrogateescape")))
    except:
      dic=u"["
      for i in last:
        dic=dic+"'"+i+"']"
        exec('''try:
    past{0} = past{0}
except:
  past{0}={1}'''.format(dic.encode("unicode_escape").decode("utf-8", "surrogateescape"),{}))
        dic=dic+"["
      dic=dic+"'"+number+"']"
      #print("asdasdasdaws")
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
>>>>>>> 1d3aeffb949790fc7578479b3b07cdd2252f5dd4
