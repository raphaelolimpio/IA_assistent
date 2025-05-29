import sys
import os

# Caminho para o diretório raiz do projeto (minha_ia_assistente)
# O script está em .../minha_ia_assistente/logic_memory/test/
# Então, precisamos subir dois níveis ('..', '..') para chegar em 'minha_ia_assistente'
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Adiciona o diretório raiz ao sys.path para que 'logic_memory' seja encontrado
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Agora os imports devem funcionar
from logic_memory.consolidate_memory import consolidate_memory


if __name__ == "__main__":
    print("Testando o sistema de memória...")

    # Certifique-se que a pasta 'memories' está vazia ou não existe antes do primeiro teste,
    # ou que os arquivos JSON estão com a estrutura inicial correta ({})

    consolidate_memory(
        user_input_name="Raphael",
        current_dialogue_summary="Usuário se apresentou como Raphael. Trocamos saudações.",
        facts_from_dialogue=[
            {"content": "O usuário principal se chama Raphael.", "theme": "informacao_pessoal_usuario"}
        ]
    )

    # Você pode adicionar mais chamadas para testar outros cenários:
    # - Segunda interação com Raphael
    # - Introdução de uma nova pessoa
    # - Aprendizado de novos fatos
    print("\nTeste concluído. Verifique a pasta 'memories/' e os arquivos JSON.")