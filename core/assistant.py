from audio.speak import ouvir_microfone, falar
from nlp.processing import processar_texto
from memory.chat_history import ChatHistory
import datetime
import random
import os
from dotenv import load_dotenv
import google.generativeai as genai

class Assistant:
    def __init__(self):
        print("Assistente inicializado e pronto para ouvir!")

        load_dotenv()
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        if not GEMINI_API_KEY:
            print("ERRO: A variável de ambiente GEMINI_API_KEY não está configurada.")
            print("Por favor, crie um arquivo .env na raiz do projeto com GEMINI_API_KEY=SUA_CHAVE_AQUI")
            exit()

        genai.configure(api_key=GEMINI_API_KEY)
        # Modelo agora configurado para gemini-1.5-flash-latest, que você confirmou funcionar
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        print(f"Modelo '{self.model.model_name}' carregado com sucesso.")

        self.chat_history = ChatHistory()

        self.respostas = {
            "saudacao": ["Olá!", "Oi, como posso ajudar?", "Bom dia!"],
            "pedir_horas": "Agora são {horas_atuais}.",
            "pedir_clima": "Desculpe, ainda não consigo verificar o clima, mas posso pesquisar outras coisas!",
            "agradecimento": ["De nada!", "Por nada!", "Disponha!"],
            "despedida": ["Até a próxima!", "Tchau!", "Foi um prazer ajudar!"],
        }

    def _adicionar_ao_historico(self, role, texto):
        self.chat_history.add_message(role, texto)

    def _obter_resposta(self, intencao, texto_original):
        if intencao == "saudacao":
            return random.choice(self.respostas["saudacao"])
        elif intencao == "pedir_horas":
            agora = datetime.datetime.now()
            horas_minutos = agora.strftime("%H horas e %M minutos")
            return self.respostas["pedir_horas"].format(horas_atuais=horas_minutos)
        elif intencao == "agradecimento":
            return random.choice(self.respostas["agradecimento"])
        elif intencao == "despedida":
            return random.choice(self.respostas["despedida"])
        else:
            print(f"Enviando para o Gemini com contexto: '{texto_original}'")
            try:
                # NOVO PROMPT DE PERSONALIDADE:
                prompt_para_gemini = (
                    f"Você é 'Aurora', uma assistente virtual com uma personalidade **entusiasmada, criativa e um pouco brincalhona**. "
                    f"Sua missão é ser prestativa, mas sempre com um toque de alegria e originalidade. "
                    f"Responda de forma convidativa e, se possível, adicione um toque de surpresa ou um pequeno desafio criativo. "
                    f"Mantenha a conversa fluida e evite respostas secas. "
                    f"Aqui está a pergunta do usuário: {texto_original}"
                )

                chat = self.model.start_chat(history=self.chat_history.get_history())
                response = chat.send_message(prompt_para_gemini)

                if response.candidates and response.candidates[0].content.parts:
                    return response.candidates[0].content.parts[0].text
                else:
                    return "Não consegui gerar uma resposta significativa com o Gemini."
            except Exception as e:
                print(f"Erro ao chamar a API Gemini: {e}")
                self.chat_history.clear_history()
                return "Desculpe, não consegui me conectar com a inteligência. Tente novamente mais tarde."

    def run(self):
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

                self._adicionar_ao_historico("model", resposta_texto)

                falar(resposta_texto)
            else:
                resposta_texto_erro = "Não entendi o que você disse. Poderia tentar novamente?"
                falar(resposta_texto_erro)


            if intencao == "despedida":
                print("Assistente desligado. Até a próxima!")
                break