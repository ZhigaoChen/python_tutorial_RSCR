# python_tutorial_RSCR
pythonTutorial for tomorrow scientist @dou ze cheng 

# project title 

## (R)reading and (S)singing voice recognition and (C)cross (R)recognition


Step1. use preprocess.py function format_all_to_wav() to conver the raw recordings to 44100Hz and mono wav files.

Step2. only supprt 8k 16k 32k to vad. use vad.py function get_vad('../data/python_tutorial_RSCR/mono16000', 'mono16000')

Step3. extract features of mfcc and chroma use getXYdataset.py function load_wav_data_to_extract_features(). to save the features as h5 file.

Step4. in sklearnModel build DecisonTree model to classification .basic_model() to run classify and cross_val_score() for cross validation and grid_search() for parameters fine tune.


## main UI
![final UI](http://i4.buimg.com/567571/512d99b5a2197374.png)




# 读唱识别及交叉识别

## 摘要

本项目针对读唱识别以及其交叉识别进行了研究，采用MFCC、LPCC以及Chroma音频特征，以及联合多种机器学习模型组建的的模型库来进行识别分类。在28人的读唱数据集上单纯读识别和唱识别均达到100%准确率，在使用歌声进行训练，读声进行测试时达到64%的准确率，另外使用读声训练使用歌声测试达到68%准确率。

## 研究目的

本项目研究的主要目的是结合声纹识别这个大背景，以及目前大数据和网络环境下，音频数据中大量标注信息缺失。面对海量的音乐数据，通过人工进行逐个识别并标注歌手等音乐内容信息显得以及不可能。如果能够通过机器学习让机器自动的去识别音频内容就能够实现自动化的标注，从而降低人力消耗。但是考虑到歌手所唱歌曲不容易获取和收集，如某些歌手可能参加各种节目演唱或者翻唱其他歌曲，也就是同一首歌曲的演唱人可能不唯一，同一歌手的演唱歌曲也会因为版权信息等造成收集成本较高。因此，如果能够通过歌手参加访谈类节目或其他宣传活动等的语音数据来辨识其歌曲的属主，将大大降低海量数据下歌手识别系统的开发成本。因此，本项目主要围绕读唱识别以及交叉识别中的音频特征选取以及模型库的建立。

## 主要内容

主要包含以下几个方面: 
(1)语音预处理  
处理原始录音数据，主要目的是将原始录音语音信号与歌唱声音进行格式统一，包括采样率以及单声道等。另外，利用VAD检测过滤静音片段。   
（2）特征参数的选取及优化   
根据说话人语音中所包含的物理特性，在特征提取时选取了MFCC以及PLCC和Chroma特征。  
（3）模型库建立   
结合机器学习模型，我们构造了语音识别模型库，包括多个机器模型，如···。   

## 实验

* 读识别
* 唱识别
* 读训练唱识别
* 唱训练读识别
* 混合识别
