texh stack used
User Speech Input via Mic
         |
        
sounddevice and soundfile
-Captures microphone audio
-Saves it as WAV file

        |
        
whisper
-Transcribes recorded audio to text

       |
        
Gemini (Model - 1.5 flash)
-Takes transcribed text
-Generates a meaningful AI response

       |
        
gTTS
-Converts AI response text to speech
- Saves it as MP3 audio

        |
      
playsound
-Plays the MP3 response back to the user


+++
FFmpeg
-Can convert formats (e.g., WAV to MP3)  
-To Ensures Whisper gets clean input


pip install -r requirements.txt
