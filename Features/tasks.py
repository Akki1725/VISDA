# Tasks file
# Importing modules
import os
import pyautogui
import datetime
import requests
from pymem import Pymem
import webbrowser
from Body.speak import speak
from Body.listen import recognize, refine
from Brain.AI import response
from Brain.AI import create
from Brain.AI import write, explain
from Features.hotword import clap
from Features.tpu import wishMe, tellTime
from Features.win_mgr import activate
from time import sleep
import wikipedia
import smtplib
import pywhatkit
import clipboard


# Extracting credentials
with open("Data\\credentials.txt") as f:

    credentials = f.read()
    credentials = dict(eval(credentials))

    username = credentials["username"]
    password = credentials["password"]


# Extracting emails
with open("Data\\emails.txt") as f:

    emails = f.read()


# Extracting languages
with open("Data\\languages.txt") as f:

    langs = f.read()

# Evaluation
emails = dict(eval(emails))
langs = dict(eval(langs))


# Sleep cycle
def sleepCycle(query):

    reply = response(query)
    speak(reply)

    print("Sleep mode...")
    sleep(2)
    print("Zzzzzzzz...")

    clap()

    reply = response("are u there visda?")
    speak(reply)


# Firmware off
def shutDown(query):

    reply = response(query)
    speak(reply)

    sleep(1)

    exit()


# Send email function
def sendEmail(to, content):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login(username, password)
    server.sendmail(username, to, content)

    server.close()


# Function to strip queries
def sprit(query):
        query = query.replace("visda ", "")
        query = query.replace("google ", "")
        query = query.replace("search ", "")
        query = query.replace(" in ", "")
        query = query.replace(" on ", "")
        query = query.replace("about ", "")
        query = query.replace("do ", "")
        query = query.replace("some ", "")
        query = query.replace("research ", "")
        query = query.replace(" google ", "")
        query = query.replace(" google", "")
        query = query.replace("google", "")
        query = query.replace(" for", "")
        query = query.replace(" on", "")
        query = query.replace(" search in google ", "")
        query = str(query)
        query = query.strip()
        return query


# Google search function
def googleSearch(query):
    pywhatkit.search(query)


# Function to execute tasks
def execute(query):

    query = str(query)

    # If nothing is spoken then dismiss
    if query == "none":
        pass

    # Opening querys or webs based on the query
    elif "open whatsapp" in query or "launch whatsapp" in query or "visit whatsapp" in query:

        link = "https://web.whatsapp.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} whatsapp..."
        speak(reply)

        return True


    elif "open " in query and ("openai" in query or "open ai" in query) and "website" in query:

        link = "https://openai.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} openai..."
        speak(reply)

        return True


    elif "launch youtube" in query or "open youtube" in query or "visit youtube" in query or "i want to watch youtube" in query or "i want to watch something on youtube" in query:

        link = "https://www.youtube.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} youtube..."
        speak(reply)

        return True


    elif "open facebook" in query or "visit facebook" in query or "launch facebook" in query or "show facebook" in query:

        link = "https://www.facebook.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} facebook..."
        speak(reply)

        return True


    elif "launch google" in query or "open google" in query or "visit google" in query or "i want to search something on google" in query or "i want to search google" in query or "i have to do some google search" in query:

        link = "https://www.google.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} google..."
        speak(reply)
        
        return True


    elif "launch microsoft" in query or "open microsoft" in query or "visit microsoft" in query:

        link = "https://www.microsoft.com/en-in/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} microsoft website..."
        speak(reply)
        
        return True




    elif "launch classroom" in query or "open classroom" in query or "visit classroom" in query or  "launch the classroom" in query or "open the classroom" in query or "visit the classroom" in query:

        link = "https://classroom.google.com/u/2/h"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} classroom..."
        speak(reply)
        
        return True


    elif (("launch " in query or "open " in query or "visit " in query) and ("mail" in query)) or "show my important mail" in query:
        link = "https://www.gmail.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} gmail..."
        speak(reply)
        

    elif (("launch " in query or "open " in query or "visit " in query) and ("translate" in query)):
        link = "https://translate.google.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} google translate..."
        speak(reply)
        
        return True


    elif (("launch " in query or "open " in query or "visit " in query or "show" in query) and ("maps" in query)) or "show " in query and "location" in query:
        link = "https://maps.google.com"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"
            reply = f"{reply} google maps..."
            speak(reply)

        elif "launch" in query:
            reply = "Launching"
            reply = f"{reply} google maps..."
            speak(reply)

        elif "visit" in query:
            reply = "Visting"
            reply = f"{reply} google maps..."
            speak(reply)

        elif "show " in query and "location" in query:
            speak("Showing your current location on google maps...")
            sleep(4)
            pyautogui.moveTo(1332, 592, 0.5)
            sleep(0.5)
            pyautogui.click()

        else:
            reply = "Opening"
            reply = f"{reply} google maps..."
            speak(reply)

        
        return True



    elif "launch instagram" in query or "open instagram" in query or "visit instagram" in query or "show my followers in instagram" in query or "show my followers on instagram" in query or "open insta" in query or "visit insta" in query or "launch insta" in query:
        
        link = "https://www.instagram.com/"
        webbrowser.open(link)
        
        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"
            
        reply = f"{reply} instagram..."
        speak(reply)

        return True


    elif "launch twitter" in query or "open twitter" in query or "visit twitter" in query or "show tweets" in query or "what is the status of my tweets" in query:
        
        link = "https://www.twitter.com/"
        webbrowser.open(link)
        
        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} twitter..."
        speak(reply)

        return True


    elif "launch linkedin" in query or "open linkedin" in query or "visit linkedin" in query:

        link = "https://www.linkedin.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} linkedin..."
        speak(reply)

        return True


    elif "launch github" in query or "open github" in query or "visit github"in query or "show my github"in query or "show source code in github"in query or "open projects in github"in query or "open project in github" in query or "show commits in github" in query:
        
        link = "https://www.github.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} github..."
        speak(reply)

        return True


    elif "launch stackoverflow" in query or "open stackoverflow" in query or "visit stackoverflow" in query or "i have some doubt on my code" in query or "i want to find some solutions for my code" in query:
        
        link = "https://www.stackoverflow.com/"
        webbrowser.open(link)
        
        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} stackoverflow..."
        speak(reply)

        return True


    elif "launch quora" in query or "open quora" in query or "visit quora" in query or "i have some query in quora" in query or "i have some query on quora" in query:
        
        link = "https://www.quora.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} quora..."
        speak(reply)

        return True


    elif "launch amazon" in query or "open amazon" in query or "visit amazon" in query or "shop amazon" in query or "shop on amazon" in query or "shop in amazon" in query or "shopping on amazon" in query or "shopping in amazon" in query or "shop something on amazon" in query or "shop something in amazon" in query:

        link = "https://www.amazon.com/"
        webbrowser.open(link)
        
        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} amazon..."
        speak(reply)
        
        return True


    elif "launch flipkart" in query or "open flipkart" in query or "visit flipkart" in query or "shop flipkart" in query or "shop on flipkart" in query or "shop in flipkart" in query or "shopping on flipkart" in query or "shopping in flipkart" in query or "shop something on flipkart" in query or "shop something in flipkart" in query or "i want to do some shopping" in query or "i want to shop" in query or "order" in query and "flipkart" in query:

        link = "https://www.flipkart.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} flipkart..."
        speak(reply)
        
        return True


    elif "launch myntra" in query or "open myntra" in query or "visit myntra" in query or "shop myntra" in query or "shop clothes on myntra" in query or "i want to shop clothes" in query:
       
        link = "https://www.myntra.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} myntra..."
        speak(reply)

        return True


    elif "launch paytm" in query or "open paytm" in query or "visit paytm" in query or "i want to do payment" in query or "i want to do some payment" in query or "i want to do payments" in query or "i want to do some payments" in query or "do paytm" in query:
        
        link = "https://www.paytm.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} paytm..."
        speak(reply)

        return True


    elif "launch freecharge" in query or "open freecharge" in query or "visit freecharge" in query or "i want to recharge mobile" in query:

        link = "https://www.freecharge.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} freecharge..."
        speak(reply)

        return True

    elif "what is your version" in query:
        version = "beta version 0.5"
        speak(f"My current version is {version}.")

    elif "launch mobikwik" in query or "open mobikwik" in query or "visit mobikwik" in query:

        link = "https://www.mobikwik.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} mobikwik..."
        speak(reply)

        return True


    elif "launch ola" in query or "open ola" in query or "visit ola" in query or "book cabs" in query or "book cab" in query or "book ola" in query or "book a cab" in query:

        link = "https://www.olacabs.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        elif "book" in query:
            reply = "Booking"

        else:
            reply = "Opening"

        reply = f"{reply} ola..."
        speak(reply)

        return True


    elif "launch uber" in query or "open uber" in query or "visit uber" in query or "book uber" in query:

        link = "https://www.uber.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} uber..."
        speak(reply)

        return True

    # Swiggy open
    elif "launch swiggy" in query or "open swiggy" in query or "visit swiggy" in query or "book food in swiggy" in query or "book food on swiggy" in query or "book swiggy" in query or "order food in swiggy" in query or "order food on swiggy" in query or "order swiggy" in query:
        
        link = "https://www.swiggy.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} swiggy..."
        speak(reply)

        return True


    elif "launch zomato" in query or "open zomato" in query or "visit zomato on web" in query or "book food in zomato" in query or "book food on zomato" in query or "book zomato" in query or "order food in zomato" in query or "order food on zomato" in query or "order zomato" in query or "i want to order food" in query or "i want to book food" in query or "order food" in query:
        
        link = "https://www.zomato.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} zomato..."
        speak(reply)

        return True

    elif "launch foodpanda" in query or "open foodpanda" in query or "visit foodpanda" in query:

        link = "https://www.foodpanda.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} foodpanda..."
        speak(reply)

        return True


    elif "launch grofers" in query or "open grofers" in query or "visit grofers" in query or "order groceries" in query:

        link = "https://www.grofers.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} grofers..."
        speak(reply)

        return True


    elif "launch bigbasket" in query or "open bigbasket" in query or "visit bigbasket" in query or "order bigbasket" in query:

        link = "https://www.bigbasket.com/"
        webbrowser.open(link)

        if "open" in query:
            reply = "Opening"

        elif "launch" in query:
            reply = "Launching"

        elif "visit" in query:
            reply = "Visting"

        else:
            reply = "Opening"

        reply = f"{reply} bigbasket..."
        speak(reply)

        return True


    # Wikipedia search
    elif "wikipedia" in query or "search wikipedia" in query or "search wiki" in query or "search in wikipedia" in query or "search in wiki" in query or "search on wikipedia" in query or "search  on wiki" in query:

        query = query.replace("wikipedia", "")
        query = query.replace("wiki", "")
        query = query.replace("in", "")
        query = query.replace("on ", "")
        query = query.strip()

        speak("Searching wikipedia...")
        results = wikipedia.summary(query, sentences=2)

        speak("According to wikipedia: ")
        speak(results)


    # Wish me
    elif "wish " in query and "me" in query:
        wishMe()

    # Cache clearing
    elif ("clear" in query or "clean" in query) and ("cache" in query or "caches" in query or "memory" in query):
        
        cmd = ('find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf')
        os.startfile("C:\\Windows\\System32\\cmd.exe")
        speak("Clearing caches...")
        sleep(0.2)
        activate("cmd.exe")
        pyautogui.typewrite(cmd, 0.000005)
        pyautogui.press('enter')
        sleep(0.2)
        pyautogui.hotkey('alt', 'f4')

        speak("Done...")

        return True


    # Send emails
    elif "send email to" in query or "send mail to" in query or "send gmail to" in query or "send gmail" in query or "i want to send an email" in query or "i want to send a mail" in query or "i want you to send a mail" in query or "i want to send a gmail" in query or "i want you to send an email" in query or "i want you to send a gmail" in query or "mail" in query and "send" in query:
        
        speak("Processing request...")
        speak("To whom should I send the message?")

        try:

            person = recognize()
            refine(person)

            if person == "exit":
                pass

            else:

                for name in emails.keys():

                    if name in person:
                        to = emails[name]

                        try:

                            speak("What should I say?")

                            content = recognize()
                            refine(content)


                            content = content.replace("say that", "")
                            content = content.replace("say", "")
                            content = content.replace("send", "")
                            content = content.strip()
                            content = content.capitalize()
                            content = f"{content}."

                            speak("Ok...")

                            sendEmail(to, content)
                            speak("The email has been sent!")

                        except Exception as e:
                            speak("An error occurred.")
                            print(e)
                            speak("Sorry, I am unable to send the email.")
                    
        except:

            person = "None"
            speak("Sorry, the name is invalid...")

        return True


    # Create image
    elif "make an image" in query or "make" in query and "photo" in query or "create an image" in query or "render an image" in query or "i want you to create an image" in query or "i want to create an image" in query or "image" in query and "create" in query or "image" in query and "make" in query:
        
        speak("Processing request...")
        speak("Which image would you like to make?")
        
        query = recognize()
        query = refine(query)
        
        speak("Creating image...")
        image = create(query)
        speak("Rendering done...")

        link = image
        webbrowser.open(link)
        
        return True


    # Write code
    elif (("write" in query and "code" in query) or ("write" in query and "program" in query) or "i want you to write code" in query) or (("make" in query and "code" in query) or ("make" in query and "program" in query) or "i want you to make code" in query):
        
        speak("Ok...")
        speak("Processing...")

        query = f"{query} "
        if "here " in query:

            code = write(query)
            pyautogui.typewrite(code, 0.00005)
        
        else:
            code_prompt = query

            for language in langs.keys():
                if language in query:
                    extension = langs[language]
                    break
                else:
                    extension = "txt"

            name = datetime.datetime.now().strftime(f"file-%Y-%m-%d-%I-%M-%S")
            file_name = f"{name}.{extension}"

            os.system("code E:\Docs\Projects\VisdaPrograms")
            activate("Visual Studio Code")

            sleep(3)

            pyautogui.hotkey('ctrl', 'shift', 'alt', 'n')

            pyautogui.typewrite(file_name)
            pyautogui.press('enter')
            sleep(0.5)

            code = write(code_prompt)
            pyautogui.typewrite(code, 0.00005)
            pyautogui.hotkey('ctrl', 's')

        speak("Done...")

    # # Explain code
    # elif "explain" in query and "code" in query:
    #     prompt = query
    #     code = 1

    #     reply = explain(prompt, code)

    # Automation
    elif "open new tab" in query:
        is_open = False

        try:
            Pymem("chrome.exe")
            is_open = True
        except:
            is_open = False

        if is_open == True:
            activate("Google Chrome")
            sleep(0.1)
            pyautogui.hotkey('ctrl', 't')

        elif is_open == False:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            sleep(1)
        speak("Ok...")

    elif "close" in query and "tab" in query:
        
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'w')
        speak("Ok...")

    elif "close" in query and "window" in query:
        
        pyautogui.hotkey('alt', 'f4')
        speak("Ok...")

    elif "maximize" in query and "window" in query:
        
        pyautogui.hotkey('win', 'up')
        speak("Ok...")

    elif "minimize" in query and "down" in query:
        
        pyautogui.hotkey('win', 'down')
        speak("Ok...")

    elif "show" in query and "desktop" in query:
        
        pyautogui.hotkey('win', 'd')
        speak("Ok...")

    elif "change" in query and "window" in query:
        pyautogui.hotkey('alt', 'tab')
        speak("Ok...")

    elif "change" in query and "tab" in query:
        pyautogui.hotkey('ctrl', 'tab')

    elif "new" in query and "desktop" in query:
        
        pyautogui.hotkey('win', 'ctrl', 'd')
        speak("Ok...")

    elif "change" in query and "desktop" in query:
        
        pyautogui.hotkey('win', 'ctrl', 'f4')
        speak("Ok...")

    elif "reopen tab" in query or "re open tab" in query or "reopen" in query and "tab" in query:
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'shift', 't')
        speak("Ok...")

    elif "reload tab" in query or "re load tab" in query or "reload " in query and "tab" in query:
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'r')
        speak("Ok...")

    elif "next" in query and "tab" in query:
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'tab')
        speak("Ok...")

    elif "previous" in query and "tab" in query:
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'tab')
        speak("Ok...")

    elif ("pause" in query and "video" in query) or ("stop" in query and "video" in query) or ("play" in query and "video" in query) or ("keep" in query and "video" in query):
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.keyDown("space")

    elif (("big" in query and "video" in query) or ("maximize" in query and "video" in query) or ("full screen" in query and "video" in query) or ("enlarge" in query and "video" in query)) or (("small" in query and "video" in query) or ("minimize" in query and "video" in query) or ("full screen" in query and "video" in query) or ("ensmall" in query and "video" in query)):
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.keyDown("f")

    elif ("cinema" in query and "mode" in query) or ("default" in query and "mode" in query) or ("default" in query and "view" in query):
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.keyDown("t")

    elif "open " in query and ("download" in query or "downloads" in query):
        os.startfile("C:\\Users\AK\\Downloads")
    
        speak("Ok...")

    elif "open games folder" in query or "open the games folder" in query:
        os.startfile("E:\\Docs\\Games")
        speak("Ok...")

    elif "open " in query and ("documents" in query or "doc" in query or "document" in query or "docs" in query):
        os.startfile("E:\\Docs")
        speak("Ok...")

    elif "open " in query and "project " in query and ("files" in query or "file" in query or "folder" in query):
        os.startfile("E:\\Docs\\Projects")
        speak("Ok...")

    elif "open history" in query:
        activate("Google Chrome")
        sleep(0.1)
        pyautogui.hotkey('ctrl', 'h')
        speak("Ok...")


    # Launch webs
    elif ("launch" in query or "visit" in query or "open" in query) and "website" in query:
        query = query.replace("launch ", "")
        query = query.replace(" launch", "")
        query = query.replace("open ", "")
        query = query.replace(" open", "")
        query = query.replace("visit ", "")
        query = query.replace(" visit", "")
        query = query.replace("website ", "")
        query = query.replace(" website", "")
        query = query.replace("the ", "")
        query = query.replace(" the ", "")
        query = query.replace(" the", "")

        link = f"https://www.{query}.com"
        webbrowser.open(link)
        speak(f"Opening {query}...")


    # Launch apps
    elif "launch" in query or "open" in query:

        query_raw = query
        query = query.replace("launch ", "")
        query = query.replace("open ", "")

        if "launch" in query_raw:
            reply = f"Launching {query}..."

        elif "open" in query_raw:
            reply = f"Opening {query}..."

        speak(reply)
        pyautogui.press("win")

        sleep(0.5)

        pyautogui.typewrite(query)

        sleep(0.5)

        pyautogui.press("enter")

        return True


    # Read selected text
    elif "read" in query and "text" in query:
        pyautogui.hotkey('ctrl', 'c')
        text = clipboard.paste()
        speak(text)


    # Google search
    elif "google search" in query or "search in google" in query or "google" in query and "search" in query:
        
        query = sprit(query)
        googleSearch(query)
        speak("Searching google...")


    # Search in youtube
    elif "search" in query and "youtube" in query:

        query = query.replace("search ", "")
        query = query.replace(" youtube ", "")
        query = query.replace("youtube", "")
        query = query.replace(" in ", "")
        query = query.replace(" on ", "")
        query = query.replace("for ", "")
        query = query.replace(" for", "")
        query = query.replace(" on", "")
        query = query.replace("visda", "")
        query = query.strip()

        speak("Searching youtube...")

        link = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(link)

        return True


    # FLipkart search
    elif "flipkart" in query and "search" in query:
        
        query = query.replace("search ", "")
        query = query.replace(" flipkart ", "")
        query = query.replace(" on ", "")
        query = query.replace("for ", "")
        query = query.replace("flipkart ", "")
        query = query.replace(" flipkart", "")
        query = query.replace("flipkart", "")
        query = query.strip()
        
        link = (f"https://www.flipkart.com/search?q={query}")
        speak("Searching flipkart...")

        webbrowser.open(link)

        return True
    

    # Amazon search
    elif "amazon" in query and "search" in query:
        
        query = query.replace("search ", "")
        query = query.replace(" amazon ", "")
        query = query.replace(" on ", "")
        query = query.replace("for ", "")
        query = query.replace("amazon ", "")
        query = query.replace(" amazon", "")
        query = query.replace("amazon", "")
        query = query.replace(".pay", "")
        query = query.strip()
        
        link = (f"https://www.amazon.in/s?k={query}")
        speak("Searching amazon...")

        webbrowser.open(link)

        return True


    # Play on youtube
    elif "youtube" in query and "play" in query or "youtube" in query and "put" in query:

        query = query.replace("play ", "")
        query = query.replace("put ", "")
        query = query.replace(" youtube ", "")
        query = query.replace("youtube", "")
        query = query.replace(" in ", "")
        query = query.replace(" on ", "")
        query = query.replace("for", "")
        query = query.replace("on", "")
        query = query.strip()

        speak(f"Playing {query} on youtube.")
        pywhatkit.playonyt(query)

        return True

    # Tell weather
    elif ("weather" in query or "temperature" in query) and ("tell" in query or "speak" in query or "show" in query):
        url = f'https://wttr.in/Ranchi'
        # Getting the Weather Data of the City
        res = requests.get(url)
        
        speak("Sure, heres the weather report!")
        
        print(res.text)

    # Tell time
    elif "current time" in query or "what is the time" in query or "tell me the time" in query or "what time is it now" in query or "time now" in query or "time" in query and "tell" in query:
        
        strTime = tellTime()
        speak(f"The current time is: {strTime}")

        return True


    # Trigger sleep cycle
    elif "go to sleep" in query or "leave me alone" in query or "sleep" in query or "take rest" in query or "go to rest" in query or "relax for sometime" in query or "standby" in query:

        sleepCycle(query)

        return True


    # Shut down VISDA
    elif "exit" in query or "shut off" in query or "shut down" in query or "turn off" in query or "bye bye" in query or "goodbye" in query:

        shutDown(query)


    # Conversational talk
    else:
        # Send to brain
        reply = response(query)
        # Speak thoughts
        speak(reply)
