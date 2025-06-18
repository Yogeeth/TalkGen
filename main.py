import os
import time
import whisper
import sounddevice as sd
import soundfile as sf
import google.generativeai as genai
from gtts import gTTS
import playsound
import warnings

# Suppress FP16 warning from Whisper
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Configuration
SAMPLE_RATE = 16000
DURATION = 10
FILENAME = "request.wav"
OUTPUT_MP3 = "response.mp3"

def record_audio():
    print("🎙️ Please speak now...")
    try:
        recording = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()
        sf.write(FILENAME, recording, SAMPLE_RATE)
        print(f"✅ Audio saved as '{FILENAME}'")
    except Exception as e:
        print("❌ Error during audio recording:", e)
        exit()

def transcribe_audio():
    print("📝 Transcribing audio...")
    try:
        model = whisper.load_model("small")
        result = model.transcribe(FILENAME)
        return result["text"]
    except Exception as e:
        print("❌ Error during transcription:", e)
        exit()

def generate_response(prompt):
    print("🤖 Generating response from Gemini...")
    try:
        api_key = os.getenv("GENAI_API_KEY")
        if not api_key:
            raise ValueError("Missing GENAI_API_KEY environment variable.")
        genai.configure(api_key=api_key)
        gemini = genai.GenerativeModel("gemini-1.5-flash")
        response = gemini.generate_content(prompt)
        return response.text.replace("*", "")
    except Exception as e:
        print("❌ Error generating response:", e)
        exit()

def text_to_speech(text):
    print("🔊 Converting text to speech...")
    try:
        tts = gTTS(text=text)
        tts.save(OUTPUT_MP3)
        print(f"✅ Audio saved as '{OUTPUT_MP3}'")
    except Exception as e:
        print("❌ Error converting text to speech:", e)
        exit()

def play_audio():
    print("▶️ Playing audio...")
    try:
        playsound.playsound(OUTPUT_MP3)
    except Exception as e:
        print("❌ Error playing audio:", e)

def main():
    record_audio()
    transcript = transcribe_audio()
    print("🗒️ You said:", transcript)
    response_text = generate_response(transcript)
    print("🤖 Gemini says:", response_text)
    text_to_speech(response_text)
    play_audio()

if __name__ == "__main__":
    main()
