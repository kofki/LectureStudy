from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def split_audio_file(audio_file_path):
    audio_file = AudioSegment.from_file(audio_file_path)
    nonsilent_speech_segments = detect_nonsilent(audio_file)
    
    audio_segments = []
    for start, end in nonsilent_speech_segments:
        audio_segments.append(audio_file[start:end])

    for index, audio_segment in enumerate(audio_segments):
        audio_segment.export(f"audio_segment_{index}.mp3", format="mp3")