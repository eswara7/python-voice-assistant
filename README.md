# 🎙️ Python Voice Assistant

This is a voice-controlled assistant built using **Python** that allows users to interact with the system using voice commands. The voice assistant can perform various tasks like answering questions, playing music, providing information, telling the time, and more.

## 🛠️ Project Overview

The Python Voice Assistant project is designed to recognize user commands through speech and provide appropriate responses. It utilizes **speech recognition** to listen to and interpret the user’s voice and **pyttsx3** for text-to-speech synthesis to communicate back with the user. The assistant can:

- Search the web
- Play songs on YouTube
- Tell the current time
- Provide information from Wikipedia
- Tell jokes
- And more...

## 🔧 Tools and Libraries Used

- **speech_recognition**: For recognizing and interpreting voice commands.
- **pyttsx3**: For text-to-speech conversion.
- **pywhatkit**: For performing actions like playing songs on YouTube and web searches.
- **datetime**: To fetch the current time.
- **wikipedia**: For answering queries about people, places, or things.
- **pyjokes**: To tell jokes.

## 🎬 How It Works

1. **Voice Command**: The assistant listens to your command via the microphone using **speech_recognition**.
2. **Command Interpretation**: The recognized speech is processed and mapped to specific actions like playing a song, telling the time, or searching Wikipedia.
3. **Text-to-Speech**: Once the command is recognized, the assistant responds using **pyttsx3**, generating a human-like voice.
4. **Continuous Interaction**: The assistant keeps running in a loop, listening for commands and performing the appropriate actions.

## 📝 Features

- **Play Music**: Command the assistant to play songs on YouTube.
- **Search the Web**: Ask the assistant to search for things on Google.
- **Tell Time**: Get the current time when asked.
- **Wikipedia Search**: Ask questions like "Who is [name]?" or "What is [thing]?"
- **Tell Jokes**: Ask for a joke, and the assistant will provide one.
- **Simple Interaction**: Commands like "Who are you?" or "Are you single?" are responded with fun answers.
- **Exit Command**: Type or say "Bye" to exit the assistant.
