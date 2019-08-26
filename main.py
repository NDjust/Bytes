import utils
import threading
#from profane_recognizer import Recognizer
import profane_recognizer
import threading

input_video = 'input/test2.mp4'

if __name__ == '__main__':
    print('Reset all data files')
    utils.delete_data_files('extract_audio/entire_extract_audio.wav', 'wav')

    print('Convert video to audio')
    utils.extract_audio_in_video(input_video, 'extract_audio/entire_extract_audio.wav')

    print('divide audio file')
    audio_infor_0, audio_infor_1 = utils.divide_audio('extract_audio/entire_extract_audio.wav')

    print(audio_infor_0)
    print(audio_infor_1)

    print('Recognize word')
    result = []

    print('First Step')
    task0 = [None] * len(audio_infor_0)
    for i, val in enumerate(audio_infor_0):
        task0[i] = threading.Thread(target=profane_recognizer.get_profane_time, args=(0, i, val[0], val[1], val[2]))
        task0[i].start()

    for i, _ in enumerate(audio_infor_0):
        print(str(i + 1) + ' / ' + str(len(audio_infor_0)))
        task0[i].join()

    print('Second Step')
    # task1 = [None] * len(audio_infor_1)
    # for i, val in enumerate(audio_infor_1):
    #     task1[i] = threading.Thread(target=profane_recognizer.get_profane_time, args=(1, i, val[0], val[1], val[2]))
    #     task1[i].start()
    #
    # for i, _ in enumerate(audio_infor_1):
    #     print(str(i + 1) + ' / ' + str(len(audio_infor_1)))
    #     task1[i].join()

    #Get result from txt files in result_detector folder
    print('Load Result')
    result = utils.get_all_data()

    print('Generate sound')
    utils.generate_sound(result)

    print('Combine Video and Audio')
    utils.combine_audio_and_video(input_video)

    print('Complete!')