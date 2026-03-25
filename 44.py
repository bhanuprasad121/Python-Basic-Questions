# Majority Element
# Problem Description
# Given an integer array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times in the array.

# You may assume that the majority element always exists in the array.

# Return the majority element.

def majority_element():
    num=list(map(int, input("Enter numbers separated by space: ").split()))
    n=len(num)
    for nums in num:
        if num.count(nums)>n//2:
            return nums
print(majority_element())        
        
    