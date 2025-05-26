import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Set the correct device index
device_index = 0  # Change from 1 to 0 (valid input device)
duration = 5  # seconds
sample_rate = 44100  # Hz

# Get device info
device_info = sd.query_devices(device_index)
max_input_channels = device_info["max_input_channels"]
channels = min(max_input_channels, 2)  # Use up to 2 channels

print(f"Using device: {device_info['name']} with {channels} channels.")

# Record audio
print("Recording...")
audio_data = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=channels,
    dtype=np.int16,
    device=device_index,
)
sd.wait()
print(audio_data)
print("Recording finished.")

# Save as WAV file
wav.write("output.wav", sample_rate, audio_data)
print("Saved as output.wav")
