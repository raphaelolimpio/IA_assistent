# audio/speak.py

import speech_recognition as sr
from gtts import gTTS
import os
# Importa as novas bibliotecas para reprodução de áudio
from pydub import AudioSegment
from pydub.playback import play as pydub_play # Renomeado para evitar conflito com 'play'

def ouvir_microfone():
    """
    Ouve o microfone e tenta transcrever a fala em texto.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga alguma coisa...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

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
    """
    Converte o texto em fala e reproduz o áudio usando gTTS e pydub/simpleaudio.
    """
    if texto:
        print(f"Assistente falando: {texto}")
        try:
            # Cria o objeto gTTS com o texto e o idioma
            tts = gTTS(text=texto, lang='pt-br', slow=False)
            # Salva o áudio em um arquivo temporário
            audio_file = "temp_audio.mp3"
            tts.save(audio_file)

            # Carrega o áudio com pydub e reproduz
            audio = AudioSegment.from_mp3(audio_file)
            pydub_play(audio) # Usa a função 'play' do pydub

            # Remove o arquivo temporário
            os.remove(audio_file)
        except Exception as e:
            print(f"Erro ao gerar ou reproduzir áudio: {e}")
            print("Certifique-se de que o PyAudio esteja instalado corretamente.")
    else:
        print("Nenhum texto fornecido para falar.")