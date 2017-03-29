import os
import h5py
import numpy
from scipy.io.wavfile import read
from tqdm import tqdm
from calcChroma import calcChroma
from calcMFCC import calcMFCC


def saveChromaDataset(X, Y):
    file = h5py.File('../data/python_tutorial_RSCR/chromaData.h5', 'w')
    file.create_dataset("X", data=X)
    file.create_dataset("Y", data=Y)
    file.close()
    return 0


def saveMFCCDataset(X, Y):
    file = h5py.File('../data/python_tutorial_RSCR/mfccData.h5', 'w')
    file.create_dataset("X", data=X)
    file.create_dataset("Y", data=Y)
    file.close()
    return 0


def load_wav_data_to_extract_features(data_dir='../data/python_tutorial_RSCR/mono32000vad',inlude=''):
    chroma_dataset_X = []
    chroma_dataset_Y = []
    mfcc_dataset_X = []
    mfcc_dataset_Y = []
    for root, dir_name, files in os.walk(data_dir):
        for audio_file in tqdm(files):
            audio_path = os.path.join(root, audio_file)
            audio_owner = audio_path.split('-')[2].split('.')[0]
            if '.wav' in audio_path and inlude in audio_path:
                print 'processing %s' % audio_path
                # chroma
                chroma_feature = calcChroma(audio_path)
                chroma_feature = numpy.array(chroma_feature)
                for chroma_feature_frame in chroma_feature:
                    chroma_dataset_X.append(chroma_feature_frame)
                    chroma_dataset_Y.append(audio_owner)
                # mfcc
                fs, signal = read(audio_path)
                mfcc_feature = calcMFCC(signal, fs)
                for mfcc_feature_frame in mfcc_feature:
                    mfcc_dataset_X.append(mfcc_feature_frame)
                    mfcc_dataset_Y.append(audio_owner)
    saveChromaDataset(chroma_dataset_X, chroma_dataset_Y)
    saveMFCCDataset(mfcc_dataset_X, mfcc_dataset_Y)
    return 0


def main():
    load_wav_data_to_extract_features()
    return 0


if __name__ == '__main__':
    main()
