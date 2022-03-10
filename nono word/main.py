from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import nltk
import os
nltk.download('omw-1.4')


recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty("rate", 150)


def shutdown_pc():
    global recognizer

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                print(note)

                if note == "f***" or note == "piss" or note == "c***" or note == "b****" or note =="niga" : #fuck, piss, cunt, bitch, nugett you can add more but you get the point
                    print("don't swear")
                    os.system('shutdown -s -t 0')



        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("i didnt understand")


mapping = {"greetings": shutdown_pc}

assistant = GenericAssistant("intents.json", intent_methods = mapping)
assistant.train_model()


while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
