import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from rudiment_library import precision
import librosa


root = Tk()
root.title("Rudiments Buddy")
root.geometry("500x500")

audio_file = "audio_samples/Metronome 120 BPM - QuickSounds.com.mp3"  # default

def browse_file():
    global audio_file
    filename = filedialog.askopenfilename(
        title="Select audio file",
        filetypes=[("Audio files", "*.mp3"), ("All files", "*.*")]
    )
    if filename:
        audio_file = filename
        file_label.config(text=f"File: {os.path.basename(filename)}")

def calculate_grade(precision_ms):
    if precision_ms < 20:
        return "A (Perfection)", "green"
    elif precision_ms < 40:
        return "B (Very good)", "lightgreen"
    elif precision_ms < 70:
        return "C (Good)", "yellow"
    elif precision_ms < 100:
        return "D (Practice more)", "orange"
    else:
        return "F (Restart)", "red"

def show():
    tempo = int(tempo_entry.get())
    y, sr = librosa.load(audio_file)
    detected_beats = librosa.onset.onset_detect(y=y, sr=sr, units='time')

    subdivision = cb.get()
    precision_calculator = precision.accuracy_deviation(tempo, y, sr, detected_beats, subdivision)
    precision_ms = precision_calculator * 1000
    grade, color = calculate_grade(precision_ms)

    result_text = f"""
    Precision: {precision_ms:.1f}ms
    Grade: {grade}
    Beats detected: {len(detected_beats)}
    Tempo: {tempo} BPM
    Subdivision: {subdivision}
        """
    lbl.config(text=result_text, fg=color, font=("Arial", 12))

a = ["crotchets", "quavers", "semiquavers"]
Button(root, text="Browse Audio File", command=browse_file).pack(pady=10)
file_label = Label(root, text="")
file_label.pack()
Label(root, text="Tempo (BPM):").pack()
tempo_entry = Entry(root)
tempo_entry.insert(0, "120")  # Default 120
tempo_entry.pack(pady=5)
cb = ttk.Combobox(root, values=a)
cb.set("Select subdivisions")
cb.pack()

Button(root, text="Next", command=show).pack()

lbl = Label(root, text="")
lbl.pack()

root.mainloop()
