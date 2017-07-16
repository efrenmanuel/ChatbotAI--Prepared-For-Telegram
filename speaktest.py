import json, numpy, decimal
est=1
'''if est==1:
    est=2
  else:
    est=1'''

while 1:
  #try:
    import AI
    rawdata=AI.talk(str(input("You: ")),est)
    answsheet=json.load(open("answ.json"))
    probs=list(rawdata.values())
    totalprob=0
    for i in probs:
      totalprob=totalprob+i
    for i in range (0,len(probs)):
      probs[i]=decimal.Decimal(probs[i])/totalprob
      print(probs)
    print(answsheet[numpy.random.choice(list(rawdata.keys()),p=probs)])
  #except Exception as E:
   # print(E)
