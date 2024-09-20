from StudyHack.file_slicer import split_audio_file, split_text_file, newline_process_text
from StudyHack.transcript import get_transcript
import os
from openai import OpenAI
import copy

api_key = os.getenv("OPENAI_API_KEY")



def transcript_audio(audio_file_name):
    path_uploaded = "uploaded_files"

    # split audio files into smaller parts and make sure that it is only split when there is silence
    audio_length = split_audio_file(f"{path_uploaded}/{audio_file_name}")
    temp_file_path = "StudyHack/audio_files_temp/"

    # Get the transcripts from the audio segments
    notes = []
    for i, item in enumerate(os.listdir(temp_file_path)):
        if i < audio_length:
            file_path = os.path.join(temp_file_path, item)
            notes.append(newline_process_text(get_transcript(file_path, api_key)))

    return create_transcript(notes)


def create_transcript(notes, limit=-1):
 # Send an API call to OpenAI to generate a summary of the notes
    client = OpenAI(api_key=api_key)
    resulting_notes = []
    if limit != -1:
        notes = copy.deepcopy(notes[:limit])
    for note in notes:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # Testing messages
            {"role": "system", "content": "You will assist in summarizing large lecture transcripts for note-taking purposes." 
            "Your task is to condense the information efficiently, ensuring all key points and relevant details are preserved,"
            " while excluding unnecessary or repetitive information. Keep the notes clear and organized, leaving space for "
            "additional future notes but without adding any filler content. Only condense when necessary, maintaining "
            "essential context and meaning. Whenever possible, group related information and emphasize core concepts. Avoid "
            "restating unimportant or redundant points. Do not include any closing statements or prompts for future input."
            },
            {"role": "user", "content": note}
        ]
        )
        resulting_notes.append(response.choices[0].message.content)
    final_text = ""
    # Print the resulting notes
    for note in resulting_notes:
        final_text += note + "\n"
    
    return final_text

    

def testing_transcript():
    notes = []
    # Process text transcripts into smaller segments (test_file)
    if not notes:
        notes = split_text_file("StudyHack/transcript_files_test/CS50 Lecture 1 Transcript.txt")
    return create_transcript(notes, 2)
   

def save_transcript(transcript_text, title):
    path = "saved_transcripts"
    open(f"{path}/{title}.txt", "a")
    with open(f"{path}/{title}.txt", "w", encoding="utf-8") as file:
        file.write(transcript_text)
        return f"{path}/{title}.txt"
