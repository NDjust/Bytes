import os
from pydub import AudioSegment

def extract_audio_in_video(video_path, output_audio_path):
    return os.system('ffmpeg -y -i ' + video_path + ' -vn -ar 44.1k -ac 1 -ab 256k ' + output_audio_path)

def divide_audio(audio_path):
    audio = AudioSegment.from_wav(audio_path)

    audio_len = len(audio) * 0.001
    segment_count = 0
    segment_len = audio_len
    for i in range(2, 100):
        if audio_len / i < 30.0:
            segment_len /= i
            segment_count = i
            break

    for i in range(segment_count):
        audio_divided = audio[i * segment_len * 1000:i * segment_len * 1000 + segment_len * 1000]
        audio_divided.export('extract_audio/output' + str(i) + '.wav', format='wav')

    return audio_len, segment_len, segment_count