# checkboard

n=6
for i in range(n):
    for j in range(n):
        print('▫️'if(i+j)%2!=0 else '▪️',end=' ')    
    print()    

    