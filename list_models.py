# list_models.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configura a API Gemini usando a chave do .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("ERRO: A variável de ambiente GEMINI_API_KEY não está configurada.")
    print("Por favor, crie um arquivo .env na raiz do projeto com GEMINI_API_KEY=SUA_CHAVE_AQUI")
    exit()

genai.configure(api_key=GEMINI_API_KEY)

print("Listando modelos disponíveis no Google Gemini API...")
try:
    for m in genai.list_models():
        # Filtra apenas os modelos que suportam generateContent (texto a texto)
        if 'generateContent' in m.supported_generation_methods:
            print(f"Nome do Modelo: {m.name} | Métodos Suportados: {m.supported_generation_methods}")
except Exception as e:
    print(f"Erro ao listar modelos: {e}")

print("\nVerifique na lista acima qual modelo é o mais adequado para 'text-to-text', geralmente 'gemini-1.0-pro' ou 'gemini-1.5-flash' (ou suas versões mais recentes).")
print("Você deverá usar o nome completo, por exemplo, 'models/gemini-1.0-pro'.")