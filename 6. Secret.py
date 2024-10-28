'''
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language:

#Coding:
If:  the word contains atleast 3 characters, remove the first letter and append it at the end
now append three random characters at the starting and the end
else: Simply reverse the string

#Decoding:
If: the word contains less than 3 characters, reverse it
else: Remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode.
'''
import random
str = "abcdefghijklmnopqrstuvwxyz"

while True:
    ch = input("Enter \"C\" to code and \"D\" to decode: ")
    if ch.upper() == "C":
        word = input("You've chosen to code...\nEnter the word: ")
        if len(word) > 3:
            code = (random.choice(str)+word+random.choice(str))
            print("The code is: ",code,"\n")

        else:
            code = word[::-1]    
            print("The code is: ",code,"\n")

    elif ch.upper() == "D":
        code = input("You've chosen to decode...\nEnter the code: ")
        if len(code) > 3:
            print(code[1:-1])
        else:
            word = code[::-1]    
            print("The code is: ",word,"\n")
            