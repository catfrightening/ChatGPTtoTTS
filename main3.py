import openai
import gtts
import os
from playsound import playsound
from tkinter import Tk, Label

# Set your OpenAI API key
openai.api_key = "YOUR-API-KEY"

# Prompt the user to enter some text
text = input("ChatGPT: ")

# Use the OpenAI API to generate a response from ChatGPT
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text,
    max_tokens=1024,
    temperature=0.5,
)

# Get the response text from the API response
response_text = response["choices"][0]["text"]

print(response_text)

# Use the TTS engine to generate audio from the response text
tts = gtts.gTTS(response_text)

# Save the audio to a file
tts.save("/home/USERNAME/.config/response.mp3")

# Play the audio file
playsound("/home/USERNAME/.config/response.mp3")

# Remove the audio file
os.remove("/home/USERNAME/.config/response.mp3")