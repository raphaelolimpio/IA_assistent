# tools/weather_tool.py

import requests
import os
from dotenv import load_dotenv
import json

def get_weather_data(location: str) -> str:
    """
    Obtém os dados de clima atual para uma localidade específica usando WeatherAPI.com.

    Args:
        location (str): O nome da cidade ou código postal para o qual buscar o clima.

    Returns:
        str: Uma string formatada com os dados do clima ou uma mensagem de erro.
    """
    load_dotenv()
    # CERTIFIQUE-SE QUE ESTE É O NOME DA VARIÁVEL NO SEU ARQUIVO .env
    API_KEY = os.getenv("WEATHERAPI_API_KEY")

    if not API_KEY:
        return "Erro: Chave da WeatherAPI não configurada. Por favor, adicione WEATHERAPI_API_KEY ao seu arquivo .env."

    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": API_KEY,
        "q": location,
        "lang": "pt" # Para obter descrições em português
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Lança um erro para status de resposta HTTP ruins (4xx ou 5xx)
        data = response.json()

        if "error" in data:
            # Se a API retornar um erro (ex: cidade não encontrada)
            return f"Erro ao buscar clima para {location}: {data['error']['message']}"
        
        # Acessar dados da resposta
        city = data["location"]["name"]
        region = data["location"]["region"] # Adicionado para mais detalhes
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        feels_like_c = data["current"]["feelslike_c"]
        
        weather_report = (
            f"O clima atual em {city}, {region}, {country} é de {condition}. "
            f"A temperatura é de {temp_c}°C, com sensação térmica de {feels_like_c}°C. "
            f"A umidade é de {humidity}% e o vento está a {wind_kph} km/h."
        )
        return weather_report

    except requests.exceptions.RequestException as e:
        return f"Erro de conexão ao buscar o clima: {e}"
    except json.JSONDecodeError:
        return "Erro: A API do clima retornou uma resposta inválida."
    except KeyError as e:
        return f"Erro: Formato de dados inesperado da API do clima (chave ausente: {e})."
    except Exception as e:
        return f"Um erro inesperado ocorreu ao processar os dados do clima: {e}"

if __name__ == '__main__':
    print("Testando a ferramenta de clima...")
    print("\nClima em Palmas:")
    print(get_weather_data("Palmas"))
    
    print("\nClima em São Paulo:")
    print(get_weather_data("Sao Paulo"))
    
    print("\nClima em London:")
    print(get_weather_data("London"))
    
    print("\nClima em uma cidade inexistente:")
    print(get_weather_data("CidadeInexistenteXYZ"))