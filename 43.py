# Elements Greater Than a Value
# Given an array of numbers and a threshold value, return all elements that are greater than the specified number.
def greater_element():
    a=list(map(int, input("Enter numbers separated by space: ").split()))
    thresold=int(input('enter a threshold number:' ))
    result=[]
    for i in a:
        if i > thresold:
            result.append(i)
    return result
print(greater_element())        