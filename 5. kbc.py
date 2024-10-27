'''
Create a program capable of displaying questions to the user like KBC. 
Use List data type to store the questions and their correct answers. 
Display the final amount the person is taking home after playing the game.
'''

amt = 0
ques1 = ["1.What is 2+2? \nA.0\nB.4\nC.22\nD.None"]
for i in ques1:
    print(ques1[0])
    print("")
    ch = input("Enter Your Choice: ")
    if ch.upper() == "B":
        amt+=1000
        print("\nCorrect! You won",amt,"INR\n")
    else:
        print("You Lost! Total amount won is",amt,"INR\nThanks for playing!\n")
        exit

ques2 = ["2.What is 11+11? \nA.10\nB.14\nC.22\nD.1111"]
for i in ques2:
    print(ques2[0])
    print("")
    ch = input("Enter Your Choice: ")
    if ch.upper() == "C":
        amt+=1000
        print("\nCorrect! You won",amt,"INR\nThanks for playing!\n")
    else:
        print("You Lost! Total amount won is",amt,"INR\nThanks for playing!\n")   
        exit

#Add more questions        