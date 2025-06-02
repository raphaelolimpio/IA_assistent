

def processar_texto(texto):
    if texto is None:
        return "nenhuma_intencao"

    texto_limpo = texto.lower()

    if "olá" in texto_limpo or "oi" in texto_limpo or "bom dia" in texto_limpo:
        return "saudacao"
    elif "horas" in texto_limpo or "que horas são" in texto_limpo:
        return "pedir_horas"
    elif "clima" in texto_limpo or "previsão do tempo" in texto_limpo or \
         "temperatura" in texto_limpo or "tempo em" in texto_limpo:
        return "pedir_clima"
    elif "obrigado" in texto_limpo or "valeu" in texto_limpo:
        return "agradecimento"
    elif "tchau" in texto_limpo or "adeus" in texto_limpo:
        return "despedida"

    elif "pesquise para mim" in texto_limpo or "pesquisar sobre" in texto_limpo or \
         "busque na web" in texto_limpo or "procure por" in texto_limpo:
        return "pesquisar_web"
    else:
        return "intencao_desconhecida"