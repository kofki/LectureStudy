from pydub import AudioSegment
from pydub.silence import split_on_silence
import io

def split_audio_file(audio_file_path):
    audio_file = AudioSegment.from_file(file=audio_file_path, format='wave')

    audio_segments = split_on_silence(
        audio_file,
        # split on silences longer than 1000ms (1 sec)
        min_silence_len=1000,

        # anything under -16 dBFS is considered silence
        silence_thresh=-40, 

        # keep 200 ms of leading/trailing silence
        keep_silence=200
    )
    for i, segment in enumerate(audio_segments):
        segment.export(f"StudyHack/audio_files_temp/segment{i}.wav", format="wav")
    return len(audio_segments)
    

def split_text_file(text_file_path):
    with open(text_file_path, "r") as file:
        text = file.read()
    text_segments = text.split("\n")
    index_of_segment = 0
    while index_of_segment < len(text_segments) - 1:
        if len(text_segments[index_of_segment]) > 7000: # at least 7000 characters in string (aprox 1000-1750 words)
            index_of_segment += 1
        elif index_of_segment < len(text_segments) - 1:
            text_segments[index_of_segment] += "\n" + text_segments.pop(index_of_segment + 1)

    return text_segments

def newline_process_text(text):
    text += "\n"
    return text