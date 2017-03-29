# coding=utf-8
import os

import h5py
import joblib
from scipy.io.wavfile import read
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from calcMFCC import calcMFCC


def load_saved_dataset(path_to_dataset='../data/python_tutorial_RSCR/feature_mono32000/mix56mfccData.h5'):
    h5file = h5py.File(path_to_dataset, 'r')
    X = h5file['X'][:]
    Y = h5file['Y'][:]
    h5file.close()
    return X, Y


def split_dataset_to_tain_test(X, Y, test_size=0.2):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=42)
    return x_train, x_test, y_train, y_test


def grid_search(x_train, y_train):
    print 'grid search...'
    # 用信息增益启发式算法建立决策树
    pipeline = Pipeline([('clf', SGDClassifier())])
    print pipeline.get_params().keys()
    parameters = {
        'clf__max_depth': [10, 30, 50, 80, 100],  # to be modify

    }
    # f1查全率和查准率的调和平均
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1,
                               verbose=2, scoring='f1')
    grid_search.fit(x_train, y_train)
    print '最佳效果：%0.3f' % grid_search.best_score_
    print '最优参数'
    best_parameters = grid_search.best_estimator_.get_params()
    print best_parameters
    return best_parameters


def basic_model(x_train, x_test, y_train, y_test):
    if not os.path.isfile('sgd.model'):
        clf = SGDClassifier(random_state=1007, n_iter=100, shuffle=True, verbose=1, warm_start=True, n_jobs=1)
    else:
        clf = joblib.load('sgd.model')
    print 'start fit model...'
    clf = clf.fit(x_train, y_train)
    print 'predict on test data...'
    predictions = clf.predict(x_test)
    right = 0
    print 'calc acc...'
    for pre, tru in zip(predictions, y_test):
        if pre == tru:
            right += 1
    acc = right / 1.0 / len(y_test)
    print 'acc is: %f.' % acc
    return acc, clf


def predict_user_choose_audio_file(wav_path, model_path='sgd.model'):
    mfcc_data_list = []
    model = joblib.load(model_path)
    fs, signal = read(wav_path)
    mfcc_feature = calcMFCC(signal, fs)
    for mfcc_feature_frame in mfcc_feature:
        mfcc_data_list.append(mfcc_feature_frame)
    print 'load model...'
    predict_owner = model.predict(mfcc_data_list)
    predict_owner = list(predict_owner)
    owner = max(predict_owner, key=predict_owner.count)

    return owner


def main():
    print "start load dataset..."
    X, Y = load_saved_dataset()
    print 'build model...'
    x_train, x_test, y_train, y_test = split_dataset_to_tain_test(X, Y, test_size=0.2)
    # grid_search(x_train, y_train)
    acc, model = basic_model(x_train, x_test, y_train, y_test)
    joblib.dump(model, 'sgd.model')
    print "save model..."
    print predict_user_choose_audio_file('reading5-m-yxx.wav')

    # print cross_val_score(model, X, Y, cv=10)
    return 0


if __name__ == '__main__':
    main()
    # mfcc mix56 acc=0.27 @32k
