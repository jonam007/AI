def towerofhanai(n,a,b,c):
    if n==1:
        print('move 1st disk from',a,'to',c)
        return 
    towerofhanai(n-1,a,c,b)
    print('move', n ,'disk from',a,'to',c)
    towerofhanai(n-1,b,a,c)


towerofhanai(2,'s','h','d')