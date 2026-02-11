import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import librosa
import numpy as np
import matplotlib.pyplot as plt
from rudiment_library import precision

def load_audio(filepath):
    y, sr = librosa.load(filepath)
    return y,sr

def detect_beats(y, sr):
    """Detects beats in an audio file
    Args:
        y: audio-time series np.ndarray [shape=(…, n)]
        sr: sampling rate of y

    Returns:
        np.ndarray [shape=(n_onsets,) or onset_envelope.shape]
        estimated positions of detected onsets in time series"""
    onsets = librosa.onset.onset_detect(y=y,sr=sr, units = 'time')
    #beat_times = librosa.frames_to_time(onsets, sr=sr)
    return onsets


def plot_beats(y, sr):
    return librosa.display.waveshow(y, sr=sr)
if __name__ == "__main__":
    y, sr = load_audio("audio_samples/Metronome 120 BPM - QuickSounds.com.mp3")
    print(y,sr)
    detected_beats = detect_beats(y, sr)
    print(detected_beats)
    print(detected_beats.shape)
    print(librosa.get_duration(y=y, sr=sr))
    plot = plot_beats(y, sr)
    plt.savefig("beat_detector.png")


