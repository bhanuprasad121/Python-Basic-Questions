# Pascal's triangle

from math import comb

n=6
for i in range(n):
    print(' '*(n-i),end=' ')
    for j in range(i+1):
        print(comb(i,j),end=' ')    
    print()


#        1 
#       1 1 
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#   1 5 10 10 5 1