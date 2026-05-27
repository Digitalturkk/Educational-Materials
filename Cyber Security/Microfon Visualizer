import sounddevice as sd
import numpy as np

def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("Громкость:", int(volume_norm))

with sd.InputStream(callback=audio_callback):
    print("Слушаю микрофон...")
    input()
