# logic_memory/knowledge_loader.py

from general_memory import load_json_file, PEOPLE_FILE, FACTS_FILE # Usando import relativo

def _extract_principal_user(known_people_data):
    """
    Função auxiliar para extrair o usuário principal dos dados carregados de people.json.
    """
    if known_people_data and "principal_user" in known_people_data:
        principal_users_list = known_people_data.get("principal_user", [])
        if principal_users_list:  # Se a lista não estiver vazia
            return principal_users_list[0] # Pega o primeiro da lista
    return None

def load_all_knowledge():
    """
    Carrega todas as bases de conhecimento (memórias) da Aurora.
    Retorna um dicionário contendo 'known_people', 'learned_facts', 
    e 'principal_user_info'.
    """
    print("KnowledgeLoader: Iniciando carregamento de todas as bases de conhecimento...")

    # Carrega os dados de people.json (esperando um dicionário)
    known_people = load_json_file(PEOPLE_FILE, default_data_type=dict)
    
    # Carrega os dados de facts.json (esperando uma lista)
    learned_facts = load_json_file(FACTS_FILE, default_data_type=list)
    
    # Extrai informações do usuário principal dos dados carregados
    principal_user_info = _extract_principal_user(known_people)

    if principal_user_info:
        user_name = principal_user_info.get("main_name", "Usuário Principal Desconhecido")
        print(f"KnowledgeLoader: Usuário principal '{user_name}' encontrado e carregado.")
    else:
        print("KnowledgeLoader: Nenhum usuário principal encontrado nos dados carregados.")
        
    print("KnowledgeLoader: Carregamento de conhecimento concluído.")
    
    return {
        "known_people": known_people,
        "learned_facts": learned_facts,
        "principal_user_info": principal_user_info
    }

if __name__ == '__main__':
    # Pequeno teste para este módulo (opcional)
    # Para testar, certifique-se que você tem a pasta 'memories' com os arquivos JSON
    # no diretório correto em relação a este script se executado diretamente.
    # Geralmente, você testaria isso através do 'test_memory_system.py' ou do 'main.py'.
    print("Testando knowledge_loader.py diretamente...")
    memories = load_all_knowledge()
    print("\nPessoas Conhecidas Carregadas:")
    # Cuidado ao imprimir tudo se os arquivos forem grandes
    # print(json.dumps(memories["known_people"], indent=2, ensure_ascii=False)) 
    if memories["principal_user_info"]:
        print(f"Usuário Principal (teste direto): {memories['principal_user_info'].get('main_name')}")
    else:
        print("Usuário Principal não encontrado (teste direto).")
    # print("\nFatos Aprendidos Carregados:")
    # print(json.dumps(memories["learned_facts"], indent=2, ensure_ascii=False))