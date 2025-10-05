from kittentts import KittenTTS
m = KittenTTS("KittenML/kitten-tts-nano-0.1")

audio = m.generate("Let's test this little model thoroughly to see what it can do. I'm very excited to put my hands on it. Today is 5th of August 20 25")

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)

