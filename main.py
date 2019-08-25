import utils
import threading
from profane_recognizer import Recognizer

if __name__ == '__main__':
    print('Reset all data files')
    utils.delete_data_files('extract_audio/entire_extract_audio.wav', 'wav')

    print('Convert video to audio')
    utils.extract_audio_in_video('input/test.mp4', 'extract_audio/entire_extract_audio.wav')

    print('divide audio file')
    audio_infor_0, audio_infor_1 = utils.divide_audio('extract_audio/entire_extract_audio.wav')

    print(audio_infor_0)
    print(audio_infor_1)

    print('Recognize word')
    result = []
    for i, val in enumerate(audio_infor_0):
        print(i + 1, '/', len(audio_infor_0))
        recognizer = Recognizer(val)
        result += recognizer.get_profane_time()

    #정확도 향상을 위해 두번 하려고 했지만, 한 번 한것도 결과가 괜찮게 나와서 일단 생략하였습니다.
    # for i, val in enumerate(audio_infor_1):
    #     print(i + 1, '/', len(audio_infor_1))
    #     recognizer = Recognizer(val)
    #     result += [recognizer.get_profane_time()]

    print('Generate sound')
    utils.generate_sound(result)

    print('Combine Video and Audio')
    utils.combine_audio_and_video('input/test.mp4')

    print('Complete!')