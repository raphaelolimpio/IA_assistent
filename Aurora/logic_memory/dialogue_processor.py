import json
from consolidate_memory import consolidate_memory

def _format_transcript_for_llm(full_dialogue_history):
    """
    Formata o histórico de diálogo completo para ser usado como entrada para o LLM.
    
    Args:
        full_dialogue_history (list): Lista de dicionários representando o histórico de diálogo.
        
    Returns:
        str: String formatada do histórico de diálogo.
    """
    transcript_lines = []
    for message in full_dialogue_history:
        role = message.get('role', 'desconhecido').capitalize()
        text = message.get('parts', [''])[0] if message.get('parts') else ""
        transcript_lines.append(f"{role}: {text}")
    return "\n".join(transcript_lines)

def analyse_and_extract_from_dialogue(full_dialogue_history, llm_generator, principal_user_info):
    if not full_dialogue_history:
        print("DialogueProcessor: Nenhum histórico de diálogo fornecido para análise.")
        return 
    print("DialogueProcessor: Iniciando análise do histórico de diálogo...")
    transcript_text = _format_transcript_for_llm(full_dialogue_history)
    
    summary_prompt = (
        f"Você é um assistente de sumarização. Resuma o seguinte diálogo de forma concisa em uma ou duas frases. "
        f"Concentre-se nos principais tópicos discutidos ou nas principais ações realizadas.\n\n"
        f"DIÁLOGO:\n{transcript_text}\n\n"
        f"RESUMO CONCISO:"
    )
    
    try: 
        llm_summary = llm_generator.generate_response(user_text=summary_prompt, use_chat_history=False)
        print(f"DialogueProcessor: Sumarização gerada: {llm_summary}")
    except Exception as e:
        print(f"DialogueProcessor: Erro ao gerar a sumarização do diálogo: {e}")
        llm_summary = "Erro ao gerar a sumarização do diálogo."
    
    facts_prompt = (
        f"Você é um assistente de extração de informações. Analise o seguinte diálogo e extraia até 3 fatos importantes "
        f"que a assistente virtual deveria memorizar para referência futura. "
        f"Para cada fato, forneça o 'content' (o fato em si) e sugira um 'theme' (ex: informacao_pessoal, tarefa, preferencia, curiosidade_geral, etc.). "
        f"Responda APENAS com uma lista de objetos JSON. Cada objeto deve ter as chaves 'content' e 'theme'. "
        f"Se nenhum fato importante for encontrado, responda com uma lista JSON vazia [].\n\n"
        f"DIÁLOGO:\n{transcript_text}\n\n"
        f"FATOS EXTRAÍDOS (lista JSON):"
    )
    facts_from_dialogue_extracted = []
    try:
        extracted_facts_str = llm_generator.generate_response(user_text=facts_prompt, use_chat_history=False)
        try:
            prased_json = json.loads(extracted_facts_str)
            if isinstance(prased_json, list):
                facts_from_dialogue_extracted = [
                    f for f in parsed_json
                    if isinstance(f, dict) and 'content' in f and 'theme' in f
                ]
            else:
                print("DialogueProcessor: Resposta do LLM não é uma lista JSON válida. Usando lista vazia.")
        except json.JSONDecodeError:
            print("DialogueProcessor: Resposta do LLM não é uma lista JSON válida. Usando lista vazia.")
        print(f"DialogueProcessor: Fatos extraídos: {facts_from_dialogue_extracted}")
    except Exception as e:
        print(f"DialogueProcessor: Erro ao gerar os fatos extraídos: {e}")
    user_name_for_consolidation =  "usuario Principal Padrão"
    if principal_user_info_known:
        user_name_for_consolidation = principal_user_info_known.get("main_name", user_name_for_consolidation)
    else:
        first_user_message_text =  full_dialogue_history[0].get('parts', [''])[0] if full_dialogue_history and full_dialogue_history[0].get('parts') else ""
        if "meu nome é" in first_user_message_text.lower():
            try:
                user_name_for_consolidation = first_user_message_text.lower().split("meu nome é")[-1].strip("")[0].capitalize()
            except:
                pass
    other_people_mentioned_data = None
    print(f"DialogueProcessor: Consolidando memória com o nome do usuário ...")
    consolidate_memory(
        user_input_name=user_name_for_consolidation,
        current_dialogue_summary= llm_summary,
        facts_from_dialogue=facts_from_dialogue_extracted,
        people_mentioned= other_people_mentioned_data,
    )
    print("DialogueProcessor: Processamento pós-diálogo concluído. Memória atualizada com sucesso.")