# python_tutorial_RSCR
pythonTutorial for tomorrow scientist @dou ze cheng 

# project title 

## (R)reading and (S)singing voice recognition and (C)cross (R)recognition


Step1. use preprocess.py function format_all_to_wav() to conver the raw recordings to 44100Hz and mono wav files.

Step2. only supprt 8k 16k 32k to vad. use vad.py function get_vad('../data/python_tutorial_RSCR/mono16000', 'mono16000')

Step3. extract features of mfcc and chroma use getXYdataset.py function load_wav_data_to_extract_features(). to save the features as h5 file.

Step4. in sklearnModel build DecisonTree model to classification .basic_model() to run classify and cross_val_score() for cross validation and grid_search() for parameters fine tune.


## main UI
![final UI](http://i1.piimg.com/567571/7c68c48c4aa5b130.png)