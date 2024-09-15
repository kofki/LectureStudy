from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def split_audio_file(audio_file_path):
    audio_file = AudioSegment.from_mp3(audio_file_path)
    nonsilent_speech_segments = detect_nonsilent(audio_file)
    audio_segments = []
    if not nonsilent_speech_segments:
        audio_segments.append(audio_file)
    else:
        for start, end in nonsilent_speech_segments:
            audio_segments.append(audio_file[start:end])

    for index, audio_segment in enumerate(audio_segments):
        audio_segment.export(f"StudyHack/audio_files_temp/audio_segment_{index}.wav", format="wav")
    

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