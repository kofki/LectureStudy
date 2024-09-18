from StudyHack.file_slicer import split_audio_file, split_text_file, newline_process_text
#import transcript
import os
from openai import OpenAI
import re


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
    for note in notes[:2]:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # Testing messages
            {"role": "system", "content": "You will assist in summarizing large lecture transcripts for note-taking purposes." 
            "Your task is to condense the information efficiently, ensuring all key points and relevant details are preserved,"
            " while excluding unnecessary or repetitive information. Keep the notes clear and organized, leaving space for "
            "additional future notes but without adding any filler content. Only condense when necessary, maintaining "
            "essential context and meaning. Whenever possible, group related information and emphasize core concepts. Avoid "
            "restating unimportant or redundant points. Do not include any closing statements or prompts for future input."},
            {"role": "user", "content": note}
        ]
        )
        resulting_notes.append(response.choices[0].message.content)
    final_text = ""
    # Print the resulting notes
    for note in resulting_notes:
        final_text += note + "\n"
    
    return final_text

def parse_to_html(gpt_response):
    # Convert newlines to <br>
    gpt_response = gpt_response.replace('\n', '<br>')

    # Convert Markdown-style headings (## and ###) to <h2> and <h3>
    gpt_response = gpt_response.replace('### ', '<h6>').replace('## ', '<h7>')

    # Convert bullet points to <ul><li>
    lines = gpt_response.split('<br>')
    in_list = False
    html_output = ''
    for line in lines:
        if line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html_output += '<ul>'
                in_list = True
            html_output += f'<li>{line[2:]}</li>'
        else:
            if in_list:
                html_output += '</ul>'
                in_list = False
            html_output += line

    # Wrap code snippets (```...```) in <pre><code> tags
    gpt_response = gpt_response.replace('```', '<pre><code>').replace('``', '</code></pre>')

    # Handle bold (**) and italic (*) formatting
    # Convert **text** to <strong>text</strong>
    gpt_response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', gpt_response)
    # Convert *text* to <em>text</em>
    gpt_response = re.sub(r'\*(.*?)\*', r'<em>\1</em>', gpt_response)

    return gpt_response
    


def test():
    string = testing_transcript()
    return parse_to_html(string)