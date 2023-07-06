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
hours = datetime.now().hour
minutes = datetime.now().minute



numbers = x

# Iterate through the list and send messages
for num in numbers:
   # message to be sent
    message ="""i whish this message find you well 
                my regards """
    # critical for the script to keep it running
    min = minutes+1

    # Sending the message to the current number
    kit.sendwhatmsg(f'+2'+num ,message,hours,min) # 10 represents hour, 30 represents minute

    # Delay between sending messages (to avoid spamming)
    # You can adjust this delay based on your needs
    # Example: time.sleep(10)

    print(f"Message sent to {num}")
    time.sleep(10)

print("All messages sent successfully!")
