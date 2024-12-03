def palind(r):
    e=len(r) - 1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r=('a','b','c','b','a')
if(palind(r)):
    print("THE TURTLE IS FLIPFLOP")
else:
    print("THE TURTLE IS NOT FLIPFLOP")