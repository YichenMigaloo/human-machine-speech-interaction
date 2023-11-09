import pyaudio
import threading
import start
from pydub import AudioSegment

class Recorder:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.frames = []
        self.is_recording = False
        #self.init_stream()
        self.recording_thread = None

    def init_stream(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

    def start_recording(self):
        self.init_stream()
        if self.is_recording:
            print("Recording is already in progress.")
            return

        self.is_recording = True
        self.frames = []

        # Starting a new thread for recording
        self.recording_thread = threading.Thread(target=self._record)
        self.recording_thread.start()
        print("Recording started...")

    def _record(self):
        while self.is_recording:
            
            data = self.stream.read(self.CHUNK, exception_on_overflow = False)
            self.frames.append(data)
            

    def stop_recording(self):
        if not self.is_recording:
            print("No recording in progress to stop.")
            return

        print("Stopping recording...")
        self.is_recording = False

        audio_segment = AudioSegment(
            data=b''.join(self.frames),
            sample_width=self.p.get_sample_size(self.FORMAT),
            frame_rate=self.RATE,
            channels=self.CHANNELS
        )

        if self.recording_thread is not None:
            self.recording_thread.join()  # Wait for recording thread to finish

        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.stream = None

        if self.p is not None:
            self.p.terminate()
            self.p = None

        # Assemble the frames and create an AudioSegment
        

        # Define the output filename with the mp3 extension
        wave_output_filename = "prompt.mp3"

        # Export the audio segment to an MP3 file
        audio_segment.export(wave_output_filename, format="mp3")
        print(f"File saved: {wave_output_filename}")
        start.get_prompt()
        

