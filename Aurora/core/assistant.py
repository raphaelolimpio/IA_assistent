# core/assistant.py

from audio.speak import ouvir_microfone, falar
from nlp.processing import processar_texto
from memory.chat_history import ChatHistory
from conscience.context_manager import ContextManager
from conscience.persona_manager import PersonaManager
from llm.generator import LLMGenerator
from conscience.usage_tracker import UsageTracker
import random
import os
from dotenv import load_dotenv

class Assistant:
    def __init__(self):
        print("Assistente inicializado e pronto para ouvir!")

        load_dotenv()

        self.chat_history = ChatHistory()
        self.current_dialogue_transcript = []
        self.context_manager = ContextManager()
        self.persona_manager = PersonaManager()
        self.llm_generator = LLMGenerator(self.chat_history) 
        self.search_tracker = UsageTracker(api_name="Google Search", limit=100, file_path="Google Search_usage.json")

        print("Assistente: Solicita ")


        self.respostas = {
            "saudacao": ["Olá!", "Oi, como posso ajudar?", "Bom dia!"],
            "pedir_horas": "Agora são {horas_atuais}.",
            "agradecimento": ["De nada!", "Por nada!", "Disponha!"],
            "despedida": ["Até a próxima!", "Tchau!", "Foi um prazer ajudar!"],
        }

    def _adicionar_ao_historico(self, role, texto):
        self.chat_history.add_message(role, texto)
        self.current_dialogue_transcript.append({
            "role": role,
            "parts": [texto]
        })

    def _obter_resposta(self, intencao, texto_original):

        if intencao == "saudacao":
            response = random.choice(self.respostas["saudacao"])
            self._adicionar_ao_historico("model", response)
            return response
        elif intencao == "pedir_horas":
            horas_atuais = self.context_manager.get_current_time()
            response = self.respostas["pedir_horas"].format(horas_atuais=horas_atuais)
            self._adicionar_ao_historico("model", response)
            return response
        elif intencao == "agradecimento":
            response = random.choice(self.respostas["agradecimento"])
            self._adicionar_ao_historico("model", response)
            return response
        elif intencao == "despedida":
            response = random.choice(self.respostas["despedida"])
            self._adicionar_ao_historico("model", response)
            return response

        elif intencao == "pesquisar_web":
            if not self.search_tracker.is_within_limit():
                remaining = self.search_tracker.get_remaining_uses()
                limited_message = (f"Ops! Sinto muito, mas meu limite de pesquisas na web para hoje chegou ao fim. "
                                   f"Já usei {self.search_tracker.get_current_usage()} de {self.search_tracker.limit} buscas. "
                                   f"Faltam {remaining} usos. Que tal me perguntar outra coisa que eu já saiba? 😉")
                self._adicionar_ao_historico("model", limited_message)
                return limited_message
            else:

                return self.llm_generator.generate_response(user_text=texto_original)

        else: 
            return self.llm_generator.generate_response(user_text=texto_original)


    def run(self):
        self.current_dialogue_transcript = []
        while True:
            print("\nEstou ouvindo... Diga algo:")
            fala_do_usuario = ouvir_microfone()

            intencao = "nenhuma_intencao"
            if fala_do_usuario:
                self._adicionar_ao_historico("user", fala_do_usuario)
                
                print(f"Analisando a fala: '{fala_do_usuario}'")
                intencao = processar_texto(fala_do_usuario)
                print(f"Intenção detectada: {intencao}")

                resposta_texto = self._obter_resposta(intencao, fala_do_usuario)

                
                falar(resposta_texto)
            else:
                resposta_texto_erro = "Não entendi o que você disse. Poderia tentar novamente?"
                falar(resposta_texto_erro)


            if intencao == "despedida":
                self._process_and_commit_memory_from_last_dialogue(self.current_dialogue_transcript)
                self.current_dialogue_transcript = []
                print("Assistente desligado. Até a próxima!")
                break
    
    def _process_and_commit_memory_from_last_dialogue(self, full_dialogue_history):
        print("Iniciando processamento pós-diálogo para consolidação da memória...")
        if not full_dialogue_history:
            print("Nenhuma conversa para processar.")
            return
