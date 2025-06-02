from logic_memory.general_memory import PEOPLE_FILE, load_json_file, save_json_file


def add_person(person_info, category="others"):
    if "person_id" not in person_info:
        print("Erro: 'person_id' é obrigatório.")
        return None
    people_data = load_json_file(PEOPLE_FILE, default_data_type=dict)
    
    if category not in people_data:
        people_data[category] = []
    person_exists = False
    for i, p in enumerate(people_data[category]):
        if p.get("person_id") == person_info["person_id"]:
            people_data[category][i] = person_info
            print(f"Pessoa com ID {person_info['person_id']} atualizada na categoria '{category}'.")
            person_exists = True
            break
    if not person_exists:
        people_data[category].append(person_info)
        print(f"Pessoa com ID {person_info['person_id']} adicionada na categoria '{category}'.")
    save_json_file(PEOPLE_FILE, people_data)
    return person_info["person_id"]
