# core/assistant.py

from audio.speak import ouvir_microfone, falar # Importa a nova função falar
from nlp.processing import processar_texto
import datetime # Para obter a hora atual

class Assistant:
    def __init__(self):
        print("Assistente inicializado e pronto para ouvir!")
        # Mapeamento de intenções para respostas
        self.respostas = {
            "saudacao": ["Olá!", "Oi, como posso ajudar?", "Bom dia!"],
            "pedir_horas": "Agora são {horas_atuais}.",
            "pedir_clima": "Desculpe, ainda não consigo verificar o clima.", # Futuramente, aqui chamaremos uma API
            "agradecimento": ["De nada!", "Por nada!", "Disponha!"],
            "despedida": ["Até a próxima!", "Tchau!", "Foi um prazer ajudar!"],
            "intencao_desconhecida": ["Desculpe, não entendi.", "Poderia repetir?", "Não sei como responder a isso."]
        }

    def _obter_resposta(self, intencao):
        """
        Retorna uma resposta com base na intenção.
        """
        resposta = self.respostas.get(intencao, self.respostas["intencao_desconhecida"])

        # Lógica para respostas dinâmicas
        if intencao == "pedir_horas":
            agora = datetime.datetime.now()
            # Formata a hora para um formato mais amigável
            horas_minutos = agora.strftime("%H horas e %M minutos")
            return resposta.format(horas_atuais=horas_minutos)
        elif isinstance(resposta, list): # Se a resposta for uma lista, escolhe uma aleatoriamente
            import random
            return random.choice(resposta)
        else:
            return resposta

    def run(self):
        """
        Executa o ciclo principal do assistente: ouvir, processar, responder.
        """
        while True:
            fala_do_usuario = ouvir_microfone()

            if fala_do_usuario:
                print(f"Analisando a fala: '{fala_do_usuario}'")
                intencao = processar_texto(fala_do_usuario)
                print(f"Intenção detectada: {intencao}")

                resposta_texto = self._obter_resposta(intencao)
                falar(resposta_texto) # A IA fala a resposta!

            else:
                print("Nenhuma fala detectada ou compreendida. Tentando novamente...")
                falar("Desculpe, não entendi. Poderia repetir?")

            if intencao == "despedida":
                print("Assistente desligado.")
                break