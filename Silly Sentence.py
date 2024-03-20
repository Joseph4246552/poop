from random import randint
#NEW TEXT
Nou=["Women","Paulino Marsupial","Airplane","South Korea","HIV","Brazil"]
Ver=["Running","Driving","Bashing","Griddy-ing","Assaulting","Drinking"]
Adj=["Collywobbles","Gullible","Colossal","Stocky","Yummy","Smart"]
Con=["and","or","so","for","is","but"]
print(Nou[randint(0, len(Nou)-1)], Con[randint(0,len(Con)-1)], Ver[randint(0,len(Ver)-1)],
                                                                 Adj[randint(0,len(Adj)-1)])
