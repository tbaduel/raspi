import pyaudio
import wave
 
BUFF = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
 
p = pyaudio.PyAudio()
 
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=BUFF)

while(1): 
	print("recording ...")
 
	frames = []
 
	for i in range(0, int(RATE / BUFF * RECORD_SECONDS)):
	   	 data = stream.read(BUFF)
   		 frames.append(data)
 
	print(" done recording")
 
	stream.stop_stream()
	#stream.close()
	#p.terminate()
 
 
	wavefile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wavefile.setnchannels(CHANNELS)
	wavefile.setsampwidth(p.get_sample_size(FORMAT))
	wavefile.setframerate(RATE)
	wavefile.writeframes(b''.join(frames))
	wavefile.close()
stream.close()
p.terminate()
