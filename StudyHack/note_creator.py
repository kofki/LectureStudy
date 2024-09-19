from StudyHack.file_slicer import split_audio_file, split_text_file, newline_process_text
#import transcript
import os
from openai import OpenAI
import markdown



'''
# path for audio test

path_audio_file = "StudyHack/audio_files_test/audio1.wav"
path_audio_segments ="StudyHack/audio_files_temp/"

# split audio files into smaller parts and make sure that it is only split when there is silence
split_audio_file(path_audio_file)

# Get the transcripts from the audio segments
notes = []
for file in os.listdir(path_audio_segments):
  if file.endswith(".wav"):
    notes.append(newline_process_text(transcript.get_transcript(
      path_audio_segments + file, api_key)))
'''
def testing_transcript():
    api_key = os.getenv("OPENAI_API_KEY")
    notes = []
    # Process text transcripts into smaller segments (test_file)
    if not notes:
        notes = split_text_file("StudyHack/transcript_files_test/CS50 Lecture 1 Transcript.txt")

    # Send an API call to OpenAI to generate a summary of the notes
    client = OpenAI(api_key=api_key)
    resulting_notes = []
    for note in notes[:3]:
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


def save_transcript(transcript_text, title):
    path = "saved_transcripts"
    open(f"{path}/{title}.txt", "a")
    with open(f"{path}/{title}.txt", "w", encoding="utf-8") as file:
        file.write(transcript_text)
        return f"{path}/{title}.txt"
