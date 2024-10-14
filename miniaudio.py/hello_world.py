import miniaudio

stream = miniaudio.stream_file("samples/music.mp3")
with miniaudio.PlaybackDevice() as device:
    device.start(stream)
    input("Audio file playing in the background. Enter to stop playback: ")
