from logic_memory.general_memory import FACTS_FILE, load_json_file, save_json_file


def add_learned_fact(fact_info):
    """
    Adiciona um fato aprendido ao arquivo learned_facts.json.
    fact_info deve ser um dicionário com os dados do fato, incluindo 'fact_id'.
    """
    if "fact_id" not in fact_info:
        print("Erro: fact_info deve conter um 'fact_id'.")
        return None

    facts_data = load_json_file(FACTS_FILE, default_data_type=list)

    # Verifica se o fato já existe para evitar duplicatas (opcional, baseado no conteúdo ou ID)
    # Esta verificação simples é pelo ID, mas pode ser mais complexa.
    fact_exists = any(f.get("fact_id") == fact_info["fact_id"] for f in facts_data)

    if not fact_exists:
        facts_data.append(fact_info)
        print(f"Fato '{fact_info.get('content', fact_info['fact_id'])}' adicionado.")
        save_json_file(FACTS_FILE, facts_data)
    else:
        print(f"Fato com ID {fact_info['fact_id']} já existe. Atualizando informações.")
        for i, f in enumerate(facts_data):
            if f.get("fact_id") == fact_info["fact_id"]:
                facts_data[i] = fact_info
                save_json_file(FACTS_FILE, facts_data)
                break
    return fact_info["fact_id"]
