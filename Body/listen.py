# Multilingual speech recognition
# Modules
import speech_recognition as sr
from googletrans import Translator

# Listen function
def listen():

    # Initializing the microphone
    r = sr.Recognizer()

    # Listening
    with sr.Microphone(device_index=2) as source:

        print("Listening...")

        # Properties
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi-in")

    except:
        return "None"

    query = str(query).lower()
    return query

# Translate function
def translate(txt):
    text = str(txt)
    translator = Translator()
    output = translator.translate(text)
    data = output.text
    return data

# Recognize function
def recognize():
    query = listen()
    data = translate(query)
    data = str(data).lower()
    return data

def refine(txt):
    txt = str(txt)
    data = txt.capitalize()
    data = (f"You: {data}.")
    print(data)
    return data
