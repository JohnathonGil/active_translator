from gtts import gTTS
from translation import TextTranslator
from pydub import AudioSegment
import simpleaudio as sa
import os

class TextToSpeech:
    def __init__(self):
        self.tts_translated = TextTranslator()

    def convert_text_to_speech(self):
        try:
            translated_text = self.tts_translated.translate_speech()
            if translated_text:
                converted_text = gTTS(translated_text, lang='es')
                converted_text.save('translated_text.mp3')
                
                # Convert the MP3 to WAV format
                converted_text = AudioSegment.from_mp3('translated_text.mp3')
                converted_text.export('translated_text.wav', format='wav')
                print("Text successfully translated and converted to speech!")
            else:
                print("We couldn't translate your response!")
        except Exception as e:
            print("An error occurred:", e)

    def play_audio_file(self, filename):
        try:
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            play_obj.wait_done()
        except Exception as e:
            print("An error occurred while playing the audio file:", e)

# Create an instance of the TextToSpeech class
tts = TextToSpeech()

while True:
    # Convert text to speech and save as an audio file
    tts.convert_text_to_speech()
    # Play the audio file
    tts.play_audio_file('translated_text.wav')
    # Delete the audio files
    os.remove('translated_text.mp3')
    os.remove('translated_text.wav')