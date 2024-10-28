import os
import speech_recognition as sr
import pyttsx3
import time
import requests
from dotenv import load_dotenv

load_dotenv()

def log_interaction(text):
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(text + "\n")

def speak(text, engine):
    sentences = text.split('. ')
    for sentence in sentences:
        engine.say(sentence.strip())
        engine.runAndWait()
        time.sleep(0.5)

def recognize_and_repeat(engine):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Processing...")
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        log_interaction(text)

        if "joke" in text.lower():
            joke = "Why did the scarecrow win an award? Because he was outstanding in his field!"
            print("Joke: " + joke)
            speak(joke, engine)
        elif "weather" in text.lower():
            city = input("Which city do you want the weather for? ")
            weather_info = get_weather(city)
            print("Weather: " + weather_info)
            speak(weather_info, engine)
        else:
            time.sleep(0.5)
            speak(text, engine)

    except sr.UnknownValueError:
        handle_error("Sorry, I could not understand the audio.", engine)
    except sr.RequestError:
        handle_error("Could not request results from the speech recognition service.", engine)
    except Exception as e:
        handle_error(f"An error occurred: {e}", engine)

def handle_error(message, engine):
    print(message)
    speak(message, engine)

def choose_voice(engine):
    voices = engine.getProperty('voices')
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")
    choice = int(input("Select a voice by number: "))
    if 0 <= choice < len(voices):
        engine.setProperty('voice', voices[choice].id)

def set_speech_rate(engine):
    rate = int(input("Enter speech rate (default is 150): ") or 150)
    engine.setProperty('rate', rate)

def get_weather(city):
    api_key = os.getenv("API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        description = weather['description']
        return f"The current temperature in {city} is {temperature}°C with {description}."
    else:
        return "Sorry, I couldn't retrieve the weather information. Please check the city name."

def main():
    engine = pyttsx3.init()
    choose_voice(engine)
    set_speech_rate(engine)

    while True:
        recognize_and_repeat(engine)
        if input("Press Enter to speak again or type 'exit' to quit: ").strip().lower() == 'exit':
            break

if __name__ == "__main__":
    main()
