import time
from datetime import datetime
import pywhatkit as kit
# read numbers from text file
with open ('numbers.txt','r')as r:
    w=r.read()
# Define a list of WhatsApp numbers
    x=w.split('\n')
    print(x)
# Get the current time hours , mins
count = 0
numbers = x
# Iterate through the list and send messages
for num in numbers:
    hours = datetime.now().hour
    minutes = datetime.now().minute
    # critical for the script to keep it running
    if (minutes < 59) :
        min = minutes + 1
    else :
        hours = hours +1
        min =1
    print(hours,min)
   # message to be sent

    message ="""
     type your text here
     .....................
     ................... 
      
"""

    # Sending the message to the current number
    kit.sendwhatmsg(num ,message,hours,min,20,20) #
    
    # Example: time.sleep(10)

    print(f"Message sent to {num}")
    # Delay between sending messages (to avoid spamming)
    # You can adjust this delay based on your needs
    time.sleep(10)    
    count+=1
    print(count)
print("All messages sent successfully!")

