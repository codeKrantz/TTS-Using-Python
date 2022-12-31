import pyttsx3

# it says the import could not be resolved, but it still works when I hit run.

engine = pyttsx3.init()
engine.say("Hey guys, this is a text to speech in python!")
engine.runAndWait()
engine.stop()
