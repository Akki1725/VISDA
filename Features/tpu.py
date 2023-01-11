# Time Processing Unit
# Importing modules
import time
import datetime
from Body.speak import speak

# Wish me function
def wishMe():
    # Extracting current time
    hour = int(datetime.datetime.now().hour)
    # Morning time
    if hour >= 0 and hour < 12:
        speak("Good Morning sir...")

    # Afternoon time
    elif hour >= 12 and hour > 17:
        speak("Good afternoon sir...")

    #Evening time
    else:
        speak("Good evening sir...")

# Current time function
def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M")
    return strTime