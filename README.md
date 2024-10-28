# PyAssistant

PyAssistant is a Python-based Text-to-Speech (TTS) and Speech Recognition CLI tool. It allows users to interact with the system using voice commands, and it can respond with spoken text. This CLI tool can tell jokes, provide weather information, and repeat what the user says.

## Features

- **Voice Interaction**: Recognizes and processes voice commands.
- **Text-to-Speech**: Converts text to speech using different voices and adjustable speech rates.
- **Jokes**: Tells a predefined joke when prompted.
- **Weather Information**: Fetches and speaks the current weather for a specified city.
- **Logging**: Logs all interactions to a file.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- `requests` library
- `python-dotenv` library
- Microphone for voice input
- Internet connection for weather information

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Falkern/py-assistant.git
   cd py-assistant
   ```

2. Install the required libraries:

   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your OpenWeatherMap API key:
   ```
   API_KEY=your_openweathermap_api_key
   ```

## Usage

1. Run the application:

   ```sh
   python tts.py
   ```

2. Follow the prompts to select a voice and set the speech rate.

3. Speak into the microphone when prompted. The application will recognize your speech and respond accordingly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [OpenWeatherMap](https://openweathermap.org/)
