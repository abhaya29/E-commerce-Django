# # 1. Indexing and Slicing
# #    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]
# s = "PythonPractice"
# print(s[1])
# print(s[-3:])
# print(s[2:7])

# # 2. Reverse a String
# #    Write a one-liner to reverse the string "developer" using slicing.
# a = "developer"
# print(a[::-1])

# # 3. Count Vowels
# #    Write a function that counts the number of vowels in a given string.
# def vowel(word):
#     vowel = 'aeiouAEIUO'
#     count = 0
#     for char in word:
#         if char in vowel:
#          count += 1
#     return count

# print(vowel("hello world"))

# # 4. Check for Palindrome
# #    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
# def is_palindrome(word):
#     cleaned = word.replace(" ", "").lower()
#     return cleaned == cleaned[::-1]

# print(is_palindrome('Madam'))
# print(is_palindrome('Race Car'))
# print(is_palindrome('pokhara'))

# # 5. Clean and Format String
# #    Given text = "   hello world! welcome to Python.   ", write code to:
# #    - Remove leading/trailing spaces
# #    - Capitalize each word
# #    - Replace the word "Python" with "Programming"
# text = "  hello world! welcome to Python.  "
# print(text.replace("  ","").capitalize().replace("Python", "Programming"))

# # 6. Find Longest Word
# #    Write a function that takes a sentence and returns the longest word in it.
# def longest_word(sentence):
#     words = sentence.split()  # Split sentence into words
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# print(longest_word("Find the longest word in this sentence")) 

# # 7. String Operators
# #    Given s1 = "Py" and s2 = "thon", what are the results of:
# #    - s1 + s2
# #    - s1 * 3
# #    - "y" in s1
# s1 = "Py"
# s2 = "thon"
# print(s1 + s2)
# print(s1 * 3)
# print("y" in s1)

# # 8. Remove Duplicate Characters
# #    Write a function that removes all duplicate characters from a string but keeps the first occurrence.
# def remove_duplicates(s):
#     result = ""    
#     for char in s:   
#         if char not in result:  
#             result += char
#     return result

# s = input('Enter the word: ').lower()
# print(remove_duplicates(s))

# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.
# def are_anagrams(str1, str2):
    
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
#     return sorted(str1) == sorted(str2)

# print(are_anagrams("listen", "silent"))  
# print(are_anagrams("hello", "world"))    
# print(are_anagrams("Dormitory", "Dirty room")) 

