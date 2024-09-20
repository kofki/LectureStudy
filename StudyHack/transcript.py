from openai import OpenAI
import os

def get_transcript(audiofile_path, API_KEY_PATH):
  client = OpenAI(api_key=API_KEY_PATH)
  audiofile = open(audiofile_path, "rb")
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audiofile
  )
  return transcription.text