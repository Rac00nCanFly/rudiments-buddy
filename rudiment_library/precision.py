import librosa
import numpy as np

def accuracy_deviation(tempo, y,sr,onsets, subdivision):
    subdivision = text_to_number(subdivision)
    ideal_beat = 60.0 / tempo / subdivision
    precision = []
    for x in range(1, len(onsets)):
        beat = onsets[x - 1] + ideal_beat
        diff = abs(onsets[x] - beat)
        precision.append(diff)
    mean_precision = np.mean(precision)
    return mean_precision

def text_to_number(text):
    if isinstance(text, (int, float)):
        return text

    mapping = {
        "crotchets": 1,
        "quavers": 2,
        "semiquavers": 4
    }

    if text in mapping:
        return mapping[text]
    else:
        raise ValueError(f"Unknown subdivision: {text}")