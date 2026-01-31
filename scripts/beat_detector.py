import librosa
import numpy as np
import matplotlib.pyplot as plt
def load_audio(filepath):
    y, sr = librosa.load(filepath)

    return y,sr

def detect_beats(y, sr):
    onsets = librosa.onset.onset_detect(y, sr=sr)
    beat_times = librosa.frames_to_time(onsets, sr=sr)
    return beat_times

def plot_beats(y, sr, beat_times):
    return librosa.display.specshow()