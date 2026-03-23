# Count Vowels in a String
# A vowel is any of the letters a, e, i, o, u (both lowercase and uppercase). The task is to count the number of vowels in a given string.
def count_vowel():
    word=input('enter a word: ')
    vowels='aeiouAEIOU'
    count=0
    for chr in word:
        if chr in vowels:
            count+=1
    return count

print('Number of vowels in word are:',count_vowel())