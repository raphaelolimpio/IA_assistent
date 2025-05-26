import datetime
import requests
import json

class ContextManager:
    def __init__(self, default_location: str = "Palmas, Tocantins"):
        self.default_location = default_location
        print(f"ContextManager inicializado com localização padrão: {self.default_location}")
        self._realtime_location: str | None = None
        self._last_location_update: datetime.datetime | None = None
        self._location_cache_duration_hours = 6

    def get_current_time(self) -> str:
        now = datetime.datetime.now()
        return now.strftime("%H horas e %M minutos")

    def get_default_location(self) -> str:
        now = datetime.datetime.now()
        
        if self._realtime_location is None or \
           (self._last_location_update is None) or \
           (now - self._last_location_update).total_seconds() > (self._location_cache_duration_hours * 3600):

            print("Tentando obter localização em tempo real via IP-API.com...")
            try:
                response = requests.get("http://ip-api.com/json/?fields=61439")
                response.raise_for_status()
                data = response.json()

                if data and data["status"] == "success":
                    city = data.get("city", "")
                    region = data.get("regionName", "")
                    country = data.get("country", "")

                    if city and region and country:
                        self._realtime_location = f"{city}, {region}, {country}"
                    elif city and country:
                        self._realtime_location = f"{city}, {country}"
                    else:
                        self._realtime_location = country if country else self.default_location

                    self._last_location_update = datetime.datetime.now()
                    print(f"Localização em tempo real obtida: {self._realtime_location}")
                    return self._realtime_location

                else:
                    print(f"Falha ao obter localização via IP-API: {data.get('message', 'Erro desconhecido')}. Usando padrão.")
                    return self.default_location
            except requests.exceptions.RequestException as e:
                print(f"Erro de conexão com IP-API: {e}. Usando localização padrão.")
                return self.default_location
            except Exception as e:
                print(f"Erro inesperado ao processar localização: {e}. Usando localização padrão.")
                return self.default_location
        else:
            print(f"Usando localização em tempo real do cache: {self._realtime_location}")
            return self._realtime_location