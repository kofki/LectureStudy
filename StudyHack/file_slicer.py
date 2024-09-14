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
    