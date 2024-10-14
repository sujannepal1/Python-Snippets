import sounddevice as sd
from scipy.io.wavfile import write

import wavio as wv


FREQUENCY = 44100
DURATION = 2


# TODO try in different computers make generic way to find the sound device
# see all the sound device available
print(sd.query_devices())
sd.default.device = 5  # setting my laptops:  HD-Audio Generic: ALC257 Analog (hw:1,0), ALSA (2 in, 2 out)


# sudo apt-get install libportaudio2 if not found in linux
recording = sd.rec(int(DURATION * FREQUENCY), samplerate=FREQUENCY, channels=2)
sd.wait()

write("recording0.wav", FREQUENCY, recording)

wv.write("recording1.wav", recording, FREQUENCY, sampwidth=2)
