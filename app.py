import librosa
import noisereduce as nr
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Load data
data, rate = librosa.load("test.wav")

# Remove noise
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("reduced_noise_file.wav", rate, reduced_noise)

# Plot graph
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(data)
ax.plot(reduced_noise)

plt.show()
