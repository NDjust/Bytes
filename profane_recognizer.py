import google_cloud_api as gc_api

def get_profane_time(index1, index2, file_path_and_name, start_time, end_time):
    word_and_startend_time = gc_api.transcribe_file_with_word_time_offsets(file_path_and_name)

    defined_profane_word = []
    f = open('profane_word.txt', 'r')
    defined_profane_word = f.read().split()

    profane_startend_time = []

    for word, start, end in word_and_startend_time:
        for profane_word in defined_profane_word:
            if word.find(profane_word) != -1:
                profane_startend_time += [[start_time + start, start_time + end]]

    f = open('result_detector/result' + str(index1) + '_' + str(index2) + '.txt', 'w')
    for start, end in profane_startend_time:
        f.write(str(start)+','+str(end)+'\n')
'''
class Recognizer:
    def __init__(self, path_and_startend_time):
        self.file_path_and_name = path_and_startend_time[0]
        self.start_time = path_and_startend_time[1]
        self.end_time = path_and_startend_time[2]

    def get_profane_time(self):
        :return: 욕을 시작한 부분의 시작과 끝점을 return 합니다.
        word_and_startend_time = gc_api.transcribe_file_with_word_time_offsets(self.file_path_and_name)

        defined_profane_word = []
        f = open('profane_word.txt', 'r')
        defined_profane_word = f.read().split()

        profane_startend_time = []

        for word, start, end in word_and_startend_time:
            for profane_word in defined_profane_word:
                if word.find(profane_word) != -1:
                    profane_startend_time += [[self.start_time + start, self.start_time + end]]


        return profane_startend_time
'''