# Speak script
# Modules
import pyttsx3


# Speak function
def speak(txt):
    # Initializing pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Setting the voice
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 170)
    print(f"VISDA: {txt}")
    engine.say(txt)
    engine.runAndWait()
