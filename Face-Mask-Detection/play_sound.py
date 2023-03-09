import wave
from playsound import playsound
import numpy as np



f = open('emolist.txt', 'r')
emodata = f.read().splitlines()
f.close()
data_len = len(emodata)
emo = emodata[data_len-1][2:5]