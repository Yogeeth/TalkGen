# Voice Assistant  

A simple voice assistant pipeline built with Python that records audio, transcribes it, generates AI responses, and plays them back as speech.  

---

## Tech Stack  

- **User Speech Input via Mic**  
  - Captures speech from the microphone  

- **sounddevice + soundfile**  
  - Records microphone input  
  - Saves audio as `.wav`  

- **FFmpeg**  
  - Converts formats (e.g., WAV → MP3)  
  - Ensures clean input for transcription  

- **Whisper**  
  - Transcribes audio (`.wav`) to text  

- **Gemini (1.5 Flash)**  
  - Processes transcribed text  
  - Generates a meaningful AI response  

- **gTTS (Google Text-to-Speech)**  
  - Converts AI response text → speech  
  - Saves audio as `.mp3`  

- **playsound**  
  - Plays the generated `.mp3` back to the user  

---

## Installation  

Clone the repo and install dependencies:  

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

  Speech Input 
      ↓
sounddevice + soundfile  →  WAV
      ↓
FFmpeg (format cleaning)
      ↓
Whisper → Transcribed Text
      ↓
Gemini → AI Response
      ↓
gTTS → MP3 Speech
      ↓
playsound → Audio Output 
