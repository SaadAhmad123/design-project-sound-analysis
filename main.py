## Accuracy docs for YAMNET https://www.diva-portal.org/smash/get/diva2:1450868/FULLTEXT02
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import audio_analysis
import dog_inference as di
import utils

fs = 16000
channels = 1
sd.default.samplerate = fs
sd.default.channels = channels
duration = 5

recording = [None, None]
rec_idx = 0

print('Recording...')
recording[rec_idx] = sd.rec(int(duration * fs), dtype='int16')
rec_idx = (rec_idx + 1) % 2
sd.wait()

while True:
    print('Recording...')
    recording[rec_idx] = sd.rec(int(duration * fs), dtype='int16')
    rec_idx = (rec_idx + 1) % 2
    print('Infering...')
    a_rec = np.asarray(np.transpose(recording[rec_idx]).tolist()[0])
    infered_classes, scores = audio_analysis.analyse(a_rec, fs)
    infered_classes = [ic.lower() for ic in infered_classes]
    infered_classes_scores = dict(zip(infered_classes, scores))
    if di.isDogInfered(infered_classes_scores, 0):
        print("\033[1;37;42m--- Dog infered --- Y\033[1;30;47m")
        print(utils.print_inferences(infered_classes, scores))
        print(di.inferDogSound(infered_classes_scores))
    else:
        print("\033[1;37;41m--- No dog infered --- X\033[0;30;47m")
        
        print(utils.print_inferences(infered_classes, scores))
    sd.wait()
