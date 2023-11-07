import pyaudio 
import wave
in_path = "prompt.mp3" 

def get_audio():
    
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1                # 声道数
    RATE = 11025                # 采样率
    RECORD_SECONDS = 10        # 录音时间
    WAVE_OUTPUT_FILENAME = in_path
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("*"*5, "I'm listening", "*"*5)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("*"*5, "Loading\n","*"*5)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()




