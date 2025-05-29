import datetime

from logic_memory.general_memory import (
    load_json_file,
    save_json_file,
    generate_uuid,
    PEOPLE_FILE,      
    FACTS_FILE,      
  
)
# Imports das funções de adição específicas
from logic_memory.add_person import add_person
from logic_memory.add_learned_fact import add_learned_fact
from logic_memory.add_dialogue_entry import add_dialogue_entry

def consolidate_memory(user_input_name, current_dialogue_summary, facts_from_dialogue=None, people_mentioned=None):
    """
    Processa as informações de um diálogo e as salva nos arquivos de memória.
    Esta é uma versão inicial e simplificada.
    """
    print("\nIniciando consolidação da memória...")
    now_utc_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # --- Gerenciar Pessoas ---
    # Supondo que 'user_input_name' é o nome do usuário principal na primeira vez.
    # Em interações futuras, você precisará de uma lógica para identificar pessoas.
    
    # Para o principal_user (exemplo simplificado para a primeira vez)
    # Em um sistema real, você carregaria people_data e verificaria se já existe.
    people_data = load_json_file(PEOPLE_FILE, default_data_type=dict)
    principal_user_id = None

    # Procura pelo principal_user. Se não existir, cria.
    # Esta lógica de busca pode ser aprimorada.
    found_principal = False
    if "principal_user" in people_data:
        for person in people_data["principal_user"]:
            if person.get("main_name", "").lower() == user_input_name.lower(): # Simples verificação pelo nome
                principal_user_id = person["person_id"]
                # Atualizar last_interaction_utc
                person["last_interaction_utc"] = now_utc_iso
                add_person(person, category="principal_user") # Para salvar a atualização
                found_principal = True
                break
    
    if not found_principal:
        principal_user_id = generate_uuid()
        principal_user_data = {
            "person_id": principal_user_id,
            "main_name": user_input_name,
            "aliases": [],
            "first_contact_utc": now_utc_iso,
            "last_interaction_utc": now_utc_iso,
            "relevant_facts_ids": []
        }
        add_person(principal_user_data, category="principal_user")
        print(f"Usuário principal '{user_input_name}' adicionado com ID: {principal_user_id}")
    else:
        print(f"Usuário principal '{user_input_name}' já existe com ID: {principal_user_id}")

    # Lógica para 'people_mentioned' (amigos, etc.) viria aqui.

    # --- Gerenciar Fatos Aprendidos ---
    generated_facts_ids_for_dialogue = []
    if facts_from_dialogue: # Supondo que facts_from_dialogue é uma lista de dicts com info dos fatos
        for fact_detail in facts_from_dialogue:
            fact_id = generate_uuid()
            fact_to_save = {
                "fact_id": fact_id,
                "content": fact_detail.get("content"),
                "theme": fact_detail.get("theme", "geral"),
                "source_dialogue_id": None, # Será preenchido pelo ID do diálogo atual
                "timestamp_learned_utc": now_utc_iso,
                "associated_people_ids": [principal_user_id] if principal_user_id else [] # Exemplo
            }
            # Adicionar mais detalhes se vierem de fact_detail
            if add_learned_fact(fact_to_save):
                 generated_facts_ids_for_dialogue.append(fact_id)


    # --- Gerenciar Diálogo ---
    dialogue_id = generate_uuid()
    dialogue_entry_data = {
        "dialogue_id": dialogue_id,
        "timestamp_start_utc": now_utc_iso, # Simplificado, idealmente você teria o início real
        "timestamp_end_utc": now_utc_iso,
        "participants_ids": [principal_user_id] if principal_user_id else [],
        "main_type": "desconhecido", # Você precisaria determinar o tipo de diálogo
        "llm_summary": current_dialogue_summary,
        "user_input_transcript": "...", # Opcional: transcrição da fala do usuário
        "aurora_response_transcript": "...", # Opcional: transcrição da resposta da Aurora
        "generated_facts_ids": generated_facts_ids_for_dialogue
    }
    add_dialogue_entry(dialogue_entry_data)

    # Atualizar source_dialogue_id nos fatos recém-adicionados
    if generated_facts_ids_for_dialogue:
        all_facts = load_json_file(FACTS_FILE, default_data_type=list)
        for fact in all_facts:
            if fact["fact_id"] in generated_facts_ids_for_dialogue:
                fact["source_dialogue_id"] = dialogue_id
        save_json_file(FACTS_FILE, all_facts)

    print(f"Consolidação da memória concluída para o diálogo ID: {dialogue_id}")


# Exemplo de como você poderia chamar isso (após uma interação):
# Suponha que no primeiro diálogo, Aurora aprende o nome do usuário.
# E o LLM gerou um resumo.
# consolidate_memory(
#     user_input_name="Raphael",
#     current_dialogue_summary="Usuário se apresentou como Raphael. Trocamos saudações.",
#     facts_from_dialogue=[
#         {"content": "O usuário principal se chama Raphael.", "theme": "informacao_pessoal_usuario"}
#     ]
# )