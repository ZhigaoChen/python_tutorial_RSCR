import os

from pydub import AudioSegment

from split2piece import split_into_words

SEP = os.sep

data_all_in = '../data/pythonTutorial5/'


def if_no_create_it(file_path):
    the_dir = os.path.dirname(file_path)
    if os.path.isdir(the_dir):
        pass
    else:
        os.makedirs(the_dir)


def init_data_dir():
    currentPath = os.getcwd()
    projectName = currentPath.split(SEP)[-1]
    if_no_create_it('../data/' + projectName + '/')
    return '../data/' + projectName + '/'


def format_all_to_wav(data_dir=data_all_in + 'raw_record_IUO_singing_reading_conversion', frame_rate_set=44100):
    for root, dir_name, files in os.walk(data_dir):
        for audio_file in files:
            audio_path = os.path.join(root, audio_file)
            if '.doc' not in audio_path:
                print audio_path
                audio_format = audio_path[-3:]
                print audio_format
                song = AudioSegment.from_file(audio_path, audio_format)
                song = song.set_channels(1)
                print 'frame_rate: ', song.frame_rate
                song = song.set_frame_rate(frame_rate_set)
                out_path = audio_path.replace('raw_record_IUO_singing_reading_conversion', 'mono' + str(frame_rate_set))
                out_path = out_path[:-3] + 'wav'
                if_no_create_it(out_path)
                song.export(out_path, 'wav')
                if '._' in audio_path:
                    os.remove(audio_path)

    return 0


data_dir = init_data_dir()


# format_all_to_wav(frame_rate_set=32000)


def split_into_five_piece(data_dir='mono16000'):
    for root, dir_name, files in os.walk(data_dir):
        for audio_file in files:
            pieces = 5
            audio_path = os.path.join(root, audio_file)
            if '.wav' in audio_path:
                print audio_path
                if 'reading5-m-ly' or '5-w-gw' in audio_path:
                    pieces = 6
                split_into_words(audio_path, pieces, 1e5)
    return 0


# get_vad('/Users/zhangxulong/Project/data/pythonTutorial5/mono32000/','mono32000')


def get_split_test_train(data_dir, dataset='mono16000vad', split_rate=0.8):
    for root, dir_name, files in os.walk(data_dir):
        for audio_file in files:
            audio_path = os.path.join(root, audio_file)
            if '.wav' in audio_path:
                song = AudioSegment.from_wav(audio_path)
                total_seconds = song.duration_seconds
                split_point = int(total_seconds * 1000 * split_rate)
                train = song[:split_point]
                test = song[split_point:]
                out_train = audio_path.replace(dataset, dataset + '_tt/train')
                out_test = audio_path.replace(dataset, dataset + '_tt/test')
                if_no_create_it(out_train)
                if_no_create_it(out_test)
                train.export(out_train, 'wav')
                test.export(out_test, 'wav')

    return 0


get_split_test_train('../data/pythonTutorial5/mono32000vad', 'mono32000vad', split_rate=0.8)
