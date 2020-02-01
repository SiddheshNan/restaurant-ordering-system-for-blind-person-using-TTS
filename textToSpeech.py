import pyttsx3

class TextToSpeech:
    def speak(self, text):
        engine = pyttsx3.init()
        self.eng = engine
        engine.setProperty('rate', 165)
        engine.setProperty('volume',1.0)
        #voices = engine.getProperty('voices')
        #engine.setProperty('voice', voices[10].id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    def stop(self):
        self.eng.stop()

