# reversed alphapet triangle

n=5
for i in range(1,n+1):
    space=n-i
    print(' '*space,end='')
    for j in range(64+n,64+n-i,-1):
        print(chr(j),end=' ')
    print()    


#     E 
#    E D 
#   E D C 
#  E D C B 
# E D C B A 
