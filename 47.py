# Contains Duplicate
# Given an list of integers called input, return True if any value appears at least twice in the array. Return False if every element in the input list is distinct.
def countains_duplicates():
    nums=eval(input('Enter a number e.g:[2,5,9,2,6]: '))
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print('This number list countains duplicates:',countains_duplicates())    
