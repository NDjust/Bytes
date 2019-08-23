import utils

if __name__ == '__main__':
    utils.extract_audio_in_video('input/test.mp4', 'extract_audio/all_extract_audio.wav')
    print(utils.divide_audio('extract_audio/all_extract_audio.wav'))
    print('Complete!')