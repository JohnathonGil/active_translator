from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from speech_to_text import SpeechToText
import gtts
from playsound import playsound

class TextTranslator:
    def __init__(self):
        # tokenizer = AutoTokenizer.from_pretrained("VanessaSchenkel/unicamp-finetuned-en-to-pt-dataset-ted")
        # model = AutoModelForSeq2SeqLM.from_pretrained("VanessaSchenkel/unicamp-finetuned-en-to-pt-dataset-ted")
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-es")
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-es")
        self.translation_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)
        self.speech_to_text = SpeechToText()

    def translate_speech(self):
        transcribed_text = self.speech_to_text.recognize_speech()
        if transcribed_text:
            results = self.translation_pipeline(transcribed_text)
            translated_text = str(results[0]['generated_text'])
            # translated_text = str(results[0]['translation_text'])
            return translated_text
        else:
            return None
        
# Create an instance of the TextTranslator class
# translator = TextTranslator()

# Translate speech
# while True:
#     translated_speech = translator.translate_speech()
#     converted_text = gtts.gTTS(translated_speech, lang="fr")
#     converted_text.save("translation.mp3")
#     playsound("translation.mp3")
    # print("Translated speech:", translated_speech)