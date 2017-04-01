import os

import joblib
from scipy.io.wavfile import read

from calcMFCC import calcMFCC


def vote_all_model_with_acc(models_dir='model', tobe_predict='test.wav'):
    vote_box = []
    print 'calc mfcc...'
    mfcc_data_list = []
    fs, signal = read(tobe_predict)
    mfcc_feature = calcMFCC(signal, fs)
    for mfcc_feature_frame in mfcc_feature:
        mfcc_data_list.append(mfcc_feature_frame)
    print 'load models...'
    for root, dir_name, files in os.walk(models_dir):
        for model_file in files:
            model_path = os.path.join(root, model_file)
            if '.model' in model_path:
                count_times = int(model_path.split('.')[1])
                model = joblib.load(model_path)
                predict_owner = model.predict(mfcc_data_list)
                predict_owner = list(predict_owner)
                owner = max(predict_owner, key=predict_owner.count)

                vote_box.extend([owner] * count_times)

    final_owner = max(vote_box, key=vote_box.count)

    return final_owner


def validate_on_all(data_dir=''):
    right = 0
    total = 0
    for root, dir_name, files in os.walk(data_dir):
        for wav_file in files:
            wav_path = os.path.join(root, wav_file)
            if '.wav' in wav_path and 'singing' in wav_path:
                final_owner = vote_all_model_with_acc('model28readOnsing',tobe_predict=wav_path)
                print final_owner, ' is the predict by our models'
                true_answer = wav_path.split('-')[2].split('.')[0]
                print true_answer, ' is the ground truth'
                total += 1
                if final_owner == true_answer:
                    right += 1
    acc=right/1.0/total
    print acc
    return acc


def main():
    owner = vote_all_model_with_acc('model', 'reading5-m-yxx.wav')
    print owner
    return 0


if __name__ == '__main__':
    validate_on_all('../data/python_tutorial_RSCR/mono32000vad/')
    # main()
