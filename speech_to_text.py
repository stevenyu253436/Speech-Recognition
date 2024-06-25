import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        audio = recognizer.listen(source)
    try:
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        response = "API unavailable"
    except sr.UnknownValueError:
        response = "Unable to recognize speech"
    return response

recognizer = sr.Recognizer()
mic = sr.Microphone()
print("Please say 'Apple'")
text = recognize_speech_from_mic(recognizer, mic)
print("Recognized text:", text)
