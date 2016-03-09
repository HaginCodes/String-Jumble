"""
stringjumble.py
Author: Hagin 
Credit: None

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
Input = input("Enter a sentence, a word or a paragraph, the more the better ;): ")

print('You entered "'+Input+'". Now jumble it: ')
print(Input[:: -1])

x = Input.split()

Print = 1 

while Print< len(x):
    print(x[-Print],end=" ")
    Print +=