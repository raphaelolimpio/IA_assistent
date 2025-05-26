import speech_recognition as sr
from gtts import gTTS
import os
import soundfile as sf
import sounddevice as sd
import time

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1.0)
        print("Processando...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
        except sr.WaitTimeoutError:
            return None
        except Exception as e:
            print(f"Erro ao capturar áudio inesperado: {e}")
            return None

    try:
        frase = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {frase}")
        return frase.lower()
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro na requisição ao serviço do Google Speech Recognition; {e}")
        return None

def falar(texto):
    if texto:
        print(f"Assistente falando: {texto}")
        audio_file = "temp_audio.mp3"
        try:
            tts = gTTS(text=texto, lang='pt-br', slow=False)
            tts.save(audio_file)

            data, samplerate = sf.read(audio_file)
            sd.play(data, samplerate)
            sd.wait() 

        except Exception as e:
            print(f"Erro ao gerar ou reproduzir áudio: {e}")
            print("Certifique-se de que o sounddevice e drivers de áudio estejam corretos.")
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)
    else:
        print("Nenhum texto fornecido para falar.")