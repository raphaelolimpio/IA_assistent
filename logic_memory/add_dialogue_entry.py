from logic_memory.general_memory import DIALOGUES_FILE, load_json_file, save_json_file


def add_dialogue_entry(dialogue_info):
    """
    Adiciona uma entrada de diálogo ao arquivo dialogue.json.
    dialogue_info deve ser um dicionário com os dados do diálogo, incluindo 'dialogue_id'.
    """
    if "dialogue_id" not in dialogue_info:
        print("Erro: dialogue_info deve conter um 'dialogue_id'.")
        return None

    dialogues_data = load_json_file(DIALOGUES_FILE, default_data_type=list)

    # Verifica se o diálogo já existe (pelo ID)
    dialogue_exists = any(d.get("dialogue_id") == dialogue_info["dialogue_id"] for d in dialogues_data)

    if not dialogue_exists:
        dialogues_data.append(dialogue_info)
        print(f"Diálogo ID '{dialogue_info['dialogue_id']}' adicionado.")
        save_json_file(DIALOGUES_FILE, dialogues_data)
    else:
        print(f"Diálogo com ID '{dialogue_info['dialogue_id']}' já existe. Não foi adicionado.")
    return dialogue_info["dialogue_id"]

