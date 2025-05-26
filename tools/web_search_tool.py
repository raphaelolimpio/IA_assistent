import requests
import os
from dotenv import load_dotenv

def search_web(query: str, num_results: int = 3) -> str:
    """
    Realiza uma pesquisa na web usando a Google Custom Search API.

    Args:
        query (str): A string de pesquisa.
        num_results (int): O número máximo de resultados a retornar (padrão: 3).

    Returns:
        str: Uma string formatada com os títulos e links dos resultados da pesquisa,
             ou uma mensagem de erro.
    """
    load_dotenv()
    API_KEY = os.getenv("Google Search_API_KEY")
    CX = os.getenv("Google Search_CX") 

    if not API_KEY or not CX:
 
        return "Erro: Credenciais da Google Search API não configuradas. Verifique Google Search_API_KEY e Google Search_CX no seu arquivo .env."

    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": query,
        "num": str(num_results)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if "items" not in data:
            return "Não encontrei resultados para sua pesquisa."

        results = []
        for item in data["items"]:
            title = item.get("title", "Sem título")
            link = item.get("link", "#")
            snippet = item.get("snippet", "Sem descrição").replace('\n', ' ')
            results.append(f"Título: {title}\nLink: {link}\nDescrição: {snippet}\n---")

        return "Resultados da pesquisa:\n" + "\n".join(results)

    except requests.exceptions.RequestException as e:
        return f"Erro de conexão ao realizar a pesquisa: {e}"
    except Exception as e:
        return f"Um erro inesperado ocorreu ao processar os resultados da pesquisa: {e}"

if __name__ == '__main__':
    print("Testando a ferramenta de pesquisa web...")
    print(search_web("capital do Brasil"))
    print("\n" + "="*50 + "\n")
    print(search_web("receita bolo de chocolate simples"))
    print("\n" + "="*50 + "\n")
    print(search_web("notícias de hoje"))