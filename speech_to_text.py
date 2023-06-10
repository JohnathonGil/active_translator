import speech_recognition as sr
import pyttsx3

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def recognize_speech(self):
        
        with sr.Microphone() as mic:
            print("Say something...")
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = self.recognizer.listen(mic)
        
        try:
            text = self.recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Text Recognized: {text}")
            return text

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            recognizer = sr.Recognizer()
        except sr.RequestError as e:
            print("Sorry, the service is currently unavailable. Error:", e)
        return None
