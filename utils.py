import os
from pydub import AudioSegment

def delete_data_files(entire_audio_file_path, filename_extension):
    '''
    :param entire_audio_file_path: 전체 오디오 파일의 이름과 확장자를 포함한 오디오 경로입니다.
    :param filename_extension: 오디오 파일들의 기본 파일형식 입니다. 예)wav, mp3
    '''
    if os.path.isfile('/extract_audio/' + entire_audio_file_path):
        os.remove('/extract_audio/'+entire_audio_file_path)

    if os.path.isfile('profane_detector_result.txt'):
        os.remove('profane_detector_result.txt')

    file_list_0 = os.listdir('extract_audio/output0')
    file_list_1 = os.listdir('extract_audio/output1')
    file_list_2 = os.listdir('result_detector/')

    file_list_0 = [name for name in file_list_0 if name.endswith(filename_extension)]
    file_list_1 = [name for name in file_list_1 if name.endswith(filename_extension)]
    file_list_2 = [name for name in file_list_2 if name.endswith(filename_extension)]

    for val in file_list_0:
        os.remove('extract_audio/output0/' + val)

    for val in file_list_1:
        os.remove('extract_audio/output1/' + val)

    for val in file_list_2:
        os.remove('result_detector/' + val)

def extract_audio_in_video(video_path, output_audio_path):
    '''
    입력된 비디오에서 오디오 파일을 추출합니다.
    :param video_path: 비디오의 이름과 확장자를 포함한 비디오 경로입니다.
    :param output_audio_path: 출력될 오디오의 이름과 확장자를 포함한 오디오 경로입니다.
    :return: 터미널 내용을 return 합니다.
    '''
    return os.system('ffmpeg -y -i ' + video_path + ' -vn -ar 44.1k -ac 1 -ab 256k ' + output_audio_path)

def divide_audio(audio_path):
    '''
    입력된 오디오 파일을 특정 길이를 가진 여러개의 오디오 파일로 자릅니다.
    :param audio_path: 오디오의 이름과 확장자를 보함한 오디오 경로입니다.
    :return: 잘라진 모든 오디오의 이름, 시작점과 끝 점을 return 합니다.
    '''
    audio = AudioSegment.from_wav(audio_path)

    audio_len = len(audio) * 0.001
    segment_count = 0
    segment_len = audio_len
    for i in range(2, 100):
        if audio_len / i <= 30.0: #자를 오디오의 길이
            segment_len /= i
            segment_count = i
            break

    path_and_startend_0, path_and_startend_1 = [], []

    #첫번 째 작업
    for i in range(segment_count):
        audio_divided = audio[i * segment_len * 1000:i * segment_len * 1000 + segment_len * 1000]
        path_and_startend_0 += [['extract_audio/output0/output0_' + str(i) + '.wav', i * segment_len, i * segment_len + segment_len]]
        audio_divided.export('extract_audio/output0/output0_' + str(i) + '.wav', format='wav')

    #두번 째 작업
    for i in range(segment_count):
        audio_divided = audio[i * segment_len * 1000 + 5000:i * segment_len * 1000 + segment_len * 1000 + 5000]
        path_and_startend_1 += [['extract_audio/output1/output1_' + str(i) + '.wav', i * segment_len + 5, i * segment_len + segment_len + 5]]
        audio_divided.export('extract_audio/output1/output1_' + str(i) + '.wav', format='wav')

    return path_and_startend_0, path_and_startend_1

def generate_sound(start_and_end_time):
    '''
    :param start_and_end_time: 욕을 말한 시작점과 끝점입니다.
    '''
    beep_sound = AudioSegment.from_wav('beep.wav')
    result_sound = AudioSegment.from_wav('extract_audio/entire_extract_audio.wav')

    print(start_and_end_time)

    for start, end in start_and_end_time:
        result_sound = result_sound[:start * 1000] + beep_sound[:(end - start) * 1000] + result_sound[end * 1000:]

    result_sound.export('result/audio_result.wav', format='wav')

def combine_audio_and_video(video_path):
    '''
    :param video_path: 합칠 비디오의 이름을 포함한 경로입니다.
    :return:
    '''
    return os.system('ffmpeg -y -i ' + video_path + ' -i result/audio_result.wav -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 result/result.mp4')

def get_all_data():
    file_list_0 = os.listdir('result_detector/')

    file_list_0 = [name for name in file_list_0 if name.endswith('txt')]

    all_result = []
    for path in file_list_0:
        f = open('result_detector/' + path, 'r')
        result = f.read().split()

        for i, val in enumerate(result):
            result[i] = val.split(',')
            result[i][0] = float(result[i][0])
            result[i][1] = float(result[i][1])

        all_result += result

    return all_result
