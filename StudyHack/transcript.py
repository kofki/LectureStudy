from openai import OpenAI
import os
print(os.getcwd())
# Transcribe the specified file and return the text of the JSON response
def get_transcript(audio_file_path, API_KEY_PATH):
  client = OpenAI(api_key=API_KEY_PATH)
  audio_file= open(audio_file_path, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
  )
  return transcription.text