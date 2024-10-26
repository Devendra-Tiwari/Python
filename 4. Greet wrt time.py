'''
Create a python program capable of greeting you with Good Morning,
Good Afternoon and Good Evening. 
Your program should use time module to get the current hour
'''

import time
timestamp = time.strftime('%H%M%S')
if int(timestamp) >= 40000 and int(timestamp) <= 115959:
    print("Good Morning")

elif int(timestamp) >= 120000 and int(timestamp) <= 170000:     
    print("Good Afternoon")

elif int(timestamp) >= 170001 and int(timestamp) <= 210000:    
    print("Good Night")

else:
    print("Good Night")    