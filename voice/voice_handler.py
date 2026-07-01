import sounddevice as sd
import scipy.io.wavfile as wav
import requests
import edge_tts
import asyncio
from config import sarvam_api

SAMPLE_RATE = 16000
VOICE = "en-GB-RyanNeural"  # British male voice, JARVIS-style


def record_audio(filename="input.wav", duration=5):
    print(f"Bol lo boss... ({duration} seconds)")
    recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, SAMPLE_RATE, recording)
    print("Recording done")
    return filename


def speech_to_text(audio_file):
    url = "https://api.sarvam.ai/speech-to-text"
    headers = {"api-subscription-key": sarvam_api}
    
    with open(audio_file, "rb") as f:
        files = {"file": ("input.wav", f, "audio/wav")}
        data = {"model": "saarika:v2.5", "language_code": "en-IN"}
        response = requests.post(url, headers=headers, files=files, data=data)
    
    result = response.json()
    return result.get("transcript", "")


async def _generate_speech(text, output_file, voice=VOICE):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)


def text_to_speech(text, output_file="output.mp3"):
    asyncio.run(_generate_speech(text, output_file))
    return output_file


def play_audio(filename):
    import soundfile as sf
    data, samplerate = sf.read(filename)
    sd.play(data, samplerate)
    sd.wait()


if __name__ == "__main__":
    from core.agent import chat_With_friday
    
    audio_file = record_audio(duration=5)
    text = speech_to_text(audio_file)
    print(f"Tumne kaha: {text}")
    
    if text.strip():
        reply = chat_With_friday(text)
        print(f"FRIDAY: {reply}")
        
        output_file = text_to_speech(reply)
        play_audio(output_file)
    else:
        print("Kuch sunayi nahi diya, dobara try karo boss.")