# -----------------
# Count Palindromes
# -----------------
# Given a list of strings, count the number of palindromes that occur inside of the list (a palindrome is a word that is spelled the same backwards and forward).
# Example 1
# Input: solution(["level","noon", "putty"])
# Output: 2
# Example 2
# Input: solution(["Tommy", "Trini", "Zack"])
# Output: 0

def findPallin(lst):
    count = 0
    for word in lst:
        if word == word[::-1]:
            count += 1
    print(count) 

# findPallin(["Tommy", "Trini", "Zack","noon"])

# Break Camel Case
# ----------
# Complete the solution so that the function will break up camel casing, using a space between words.
# Example 1
# Input: solution('morphinGrid')
# Output: 'morphin Grid'
# Example 2
# Input: solution('fundamentals')
# Output: 'fundamentals'

def camelCase(word):
    stng = ""
    for letter in word:
        if letter.isupper():
            stng += " "
        stng += letter
    return stng.strip()
            
print(camelCase("morphinGrid"))