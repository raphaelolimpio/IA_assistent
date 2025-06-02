# llm/generator.py

import google.generativeai as genai
import os
from dotenv import load_dotenv
from tools.weather_tool import get_weather_data
from tools.web_search_tool import search_web
from conscience.persona_manager import PersonaManager
from conscience.usage_tracker import UsageTracker
import json

class LLMGenerator:
    def __init__(self, chat_history_instance):
        load_dotenv()
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        if not GEMINI_API_KEY:
            print("ERRO: A variável de ambiente GEMINI_API_KEY não está configurada para o LLM.")
            exit()

        genai.configure(api_key=GEMINI_API_KEY)
        
        try:
            self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
            print(f"LLMGenerator: Modelo '{self.model.model_name}' carregado com sucesso.")
        except Exception as e:
            print(f"LLMGenerator: Erro ao carregar modelo Gemini: {e}")
            exit()

        self.search_tracker = UsageTracker(api_name="Google Search", limit=100, file_path="Google Search_usage.json")

        self.registered_tools_model = genai.GenerativeModel(
            model_name='models/gemini-1.5-flash-latest',
            tools=[get_weather_data, search_web]
        )
        print("LLMGenerator: Ferramentas registradas com o modelo (Clima e Pesquisa Web).")
        print(f"LLMGenerator: Contador de Busca Web: {self.search_tracker.get_current_usage()} de {self.search_tracker.limit} usos hoje.")


        self.chat_history_instance = chat_history_instance
        self.persona_manager = PersonaManager()


    def generate_response(self, user_text: str) -> str:
        print(f"LLMGenerator: Gerando resposta para '{user_text}' com LLM...")
        try:
            persona_prompt = self.persona_manager.get_persona_prompt()
            
            chat_session = self.registered_tools_model.start_chat(
                history=self.chat_history_instance.get_history()
            )
            
            # Constrói o prompt completo incluindo a personalidade e a pergunta do usuário
            full_prompt = f"{persona_prompt}\n\nUsuário: {user_text}"

            response = chat_session.send_message(full_prompt)

            # --- LÓGICA DE EXECUÇÃO DE FERRAMENTAS ---
            if response.candidates and response.candidates[0].content.parts[0].function_call:
                tool_call = response.candidates[0].content.parts[0].function_call
                tool_name = tool_call.name
                tool_args = {k: v for k, v in tool_call.args.items()}
                
                print(f"✨ LLMGenerator: IA sugeriu chamar a ferramenta: {tool_name} com argumentos: {tool_args} ✨")

                tool_result = "Erro: Ferramenta desconhecida solicitada." # Valor padrão de erro

                if tool_name == "get_weather_data":
                    if "location" not in tool_args:
                        tool_result = "Erro: A ferramenta 'get_weather_data' requer um argumento 'location'."
                    else:
                        tool_result = get_weather_data(location=tool_args["location"])
                elif tool_name == "search_web": 
                    
                    self.search_tracker.increment_usage() 
                    
                    if "query" not in tool_args:
                        tool_result = "Erro: A ferramenta 'search_web' requer um argumento 'query'."
                    else:
                        num_results = tool_args.get("num_results", 3)
                        tool_result = search_web(query=tool_args["query"], num_results=num_results)
                else: 
                    tool_result = f"Erro: Ferramenta desconhecida solicitada: {tool_name}"
                    
                print(f"LLMGenerator: Resultado da ferramenta: {tool_result}")

                final_response_from_tool = chat_session.send_message(
                    genai.protos.Part(function_response=genai.protos.FunctionResponse(
                        name=tool_name,
                        response={"result": tool_result}
                    ))
                )
                if final_response_from_tool.candidates and final_response_from_tool.candidates[0].content.parts:
                    return final_response_from_tool.candidates[0].content.parts[0].text
                else:
                    return "LLMGenerator: A ferramenta foi executada, mas não consegui formular uma resposta final."


            elif response.candidates and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text
            else:
                return "LLMGenerator: Não consegui gerar uma resposta significativa com o Gemini."

        except Exception as e:
            print(f"LLMGenerator: Erro ao chamar a API Gemini ou processar resposta: {e}")
            self.chat_history_instance.clear_history()
            return "LLMGenerator: Desculpe, tive um problema ao tentar te responder."