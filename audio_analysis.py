from __future__ import division, print_function

import sys

import numpy as np
import resampy
import soundfile as sf
import tensorflow as tf

import params as yamnet_params
import yamnet as yamnet_model


def analyse(raw_waveform, sr, number_of_inference_classes = 7):
    params = yamnet_params.Params()
    yamnet = yamnet_model.yamnet_frames_model(params)
    yamnet.load_weights('yamnet.h5')
    yamnet_classes = yamnet_model.class_names('yamnet_class_map.csv')

    waveform = np.asarray(raw_waveform).astype('float32')
    waveform = np.divide(waveform, 32768.0)
    print(waveform.shape)

    if len(waveform.shape) > 1:
      waveform = np.mean(waveform, axis=1)
    if sr != params.sample_rate:
      waveform = resampy.resample(waveform, sr, params.sample_rate)

    scores, embeddings, spectrogram = yamnet(waveform)
    prediction = np.mean(scores, axis=0)
    top10_i = np.argsort(prediction)[::-1][:number_of_inference_classes]
    return (
      [yamnet_classes[i] for i in top10_i],
      [prediction[i] for i in top10_i]
    )