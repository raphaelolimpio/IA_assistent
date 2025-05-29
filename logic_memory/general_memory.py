import json
import os
import uuid

MEMORIES_DIR = "memories"
PEOPLE_FILE = os.path.join(MEMORIES_DIR, "people.json")
FACTS_FILE = os.path.join(MEMORIES_DIR, "facts.json")
DIALOGUES_FILE = os.path.join(MEMORIES_DIR, "dialogues.json")

os.makedirs(MEMORIES_DIR, exist_ok=True)

def generate_uuid():
    """
    Gera um UUID único.
    
    Returns:
        str: Um UUID no formato de string.
    """
    return str(uuid.uuid4())

def load_json_file(file_path, default_data_type=list):
    """
    Carrega o conteúdo de um arquivo JSON.
    
    Args:
        file_path (str): Caminho para o arquivo JSON.
        default_data_type (type): Tipo de dados padrão a ser retornado se o arquivo não existir.

    Returns:
        dict: Conteúdo do arquivo JSON ou um dicionário vazio se o arquivo não existir.
    """
    if not os.path.exists(file_path):
        if default_data_type == dict:
            return {}
        else: 
            return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content:
            return default_data_type()  # Verifica se o conteúdo está vazio/
        return json.loads(content)
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON no arquivo {file_path}. Retornando dados padrão.")
        return default_data_type()
    except Exception as e:
        print(f"Erro ao carregar o arquivo {file_path}: {e}")
        return default_data_type()
    
def save_json_file(file_path, data):
    """
    Salva dados em um arquivo JSON.
    
    Args:
        file_path (str): Caminho para o arquivo JSON.
        data (dict or list): Dados a serem salvos no arquivo JSON.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar o arquivo {file_path}: {e}")
    