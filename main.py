import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import os

r = sr.Recognizer()

mic = sr.Microphone(device_index = 0)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

res_lan=r.recognize_google(audio)
Languages = {
'en'    : 'English',
'it'    : 'Italian',
'sv'    : 'Swedish',
'ar'    : 'Arabic',
'ur'    : 'Urdu',
'es'    : 'Spanish',
'ru'    : 'Russian',
'pt'    : 'Portuguese',
'la'    : 'Latin',
'gu'    : 'Gujarati',
'ta'    : 'Tamil',
'fr'    : 'French',
'bn'    : 'Bengali',
'hi'    : 'Hindi',
'ja'    : 'Japanese',
'te'    : 'Telugu',
'zh-TW' : 'Chinese Traditional',
'ko'    : 'Korean',
'kn'    : 'Kannada',
'zh-CN' : 'Chinese Simplified',
'de'    : 'German',
}

for Language in Languages :
    if Languages[Language] == res_lan :
        result=Language
        break

print(result)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

with open('./my_file.txt', mode='w',encoding="utf-8") as my_file:
    my_file.write(r.recognize_google(audio))

translator = Translator(to_lang = result)

with open('./my_file.txt', mode='r') as my_file:
    text = my_file.read()
    translation = translator.translate(text)
    with open('./my_file2.txt', mode='w',encoding="utf-8") as my_file2:
        my_file2.write(translation)

with open('./my_file2.txt', mode='r' ,encoding = "utf-8") as myfile:
    mytext = myfile.read()

language = result

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system(" welcome.mp3")
