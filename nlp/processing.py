# nlp/processing.py

def processar_texto(texto):
    """
    Processa o texto para identificar a intenção do usuário.
    """
    if texto is None:
        return "nenhuma_intencao"

    texto_limpo = texto.lower()

    if "olá" in texto_limpo or "oi" in texto_limpo or "bom dia" in texto_limpo:
        return "saudacao"
    elif "horas" in texto_limpo or "que horas são" in texto_limpo:
        return "pedir_horas"
    elif "clima" in texto_limpo or "previsão do tempo" in texto_limpo:
        return "pedir_clima"
    elif "obrigado" in texto_limpo or "valeu" in texto_limpo:
        return "agradecimento"
    elif "tchau" in texto_limpo or "adeus" in texto_limpo:
        return "despedida"
    else:
        return "intencao_desconhecida"