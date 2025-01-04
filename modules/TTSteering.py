import speech_recognition as sr
from pynput.keyboard import Controller

recognizer = sr.Recognizer()
keyboard = Controller()

word_to_key = {
    "vorne": "w",
    "hinten": "s",
    "links": "a",
    "rechts": "d",
}

def listen_and_execute():
    with sr.Microphone() as source:
        print("Hintergrundgeräusche werden erkannt und entfernt...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Aufnahme gestartet...")

        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio, language="de-DE").lower()

                if command in word_to_key:
                    print(f"Versuch: {command}")
                    keyboard.press(word_to_key[command])
                    keyboard.release(word_to_key[command])
                else:
                    print(f"'{command}' ist kein gültiger Befehl.")

            except sr.UnknownValueError:
                print("Konnte den Befehl nicht verstehen.")

            except sr.RequestError as e:
                print(f"RequestError; {e}")
                break

if __name__ == "__main__":
    listen_and_execute()