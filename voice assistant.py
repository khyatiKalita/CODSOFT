import os
import speech_recognition as sr
from dotenv import load_dotenv
from openai import OpenAI
from elevenlabs.client import ElevenLabs
from elevenlabs import play

# 🔑 Load environment variables from .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Initialize clients
gpt_client = OpenAI(api_key=OPENAI_API_KEY)
tts_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# 🎤 Convert speech to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio) #This part asks Google to listen to the recorded audio and change it into words (text).
        print("👤 You:", text)
        return text
    except Exception as e:
        print("❌ Speech recognition error:", e)
        return ""


def get_response(prompt):
    response = gpt_client.chat.completions.create(
        model="gpt-4o-mini",  # lightweight GPT model, change to gpt-4 if you prefer
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 🔊 Speak with ElevenLabs
def speak(text):
    audio = tts_client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel (default voice ID, change in dashboard if needed)
        model_id="eleven_multilingual_v2",
        text=text,
        output_format="mp3_22050_32"
    )
    play(audio)

# 🚦 Main loop
if _name_ == "_main_":
    print("🤖 Assistant ready! Say 'stop' to exit.")
    while True:
        user_input = listen()
        if not user_input:
            continue
        if user_input.lower() in ["stop", "exit", "quit"]:
            speak("Goodbye! Have a great day!")
            break

        answer = get_response(user_input)
        print("🤖 Assistant:", answer)
        speak(answer)
