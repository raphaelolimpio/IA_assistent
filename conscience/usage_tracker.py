# conscience/usage_tracker.py

import datetime
import json
import os

class UsageTracker:
    def __init__(self, api_name: str, limit: int, file_path: str = "usage_data.json"):
        """
        Inicializa o rastreador de uso para uma API.
        Args:
            api_name (str): O nome da API que está sendo rastreada (ex: "Google Search").
            limit (int): O limite de uso diário para esta API.
            file_path (str): O caminho do arquivo para salvar/carregar os dados de uso.
        """
        self.api_name = api_name
        self.limit = limit
        self.file_path = file_path
        self._data = self._load_data()
        self._check_and_reset_daily()

    def _load_data(self) -> dict:
        """Carrega os dados de uso do arquivo."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        return data
                    else:
                        print(f"Aviso: Conteúdo inválido no {self.file_path}. Criando novo.")
                        return {}
            except json.JSONDecodeError:
                print(f"Aviso: Erro ao decodificar JSON em {self.file_path}. Criando novo.")
                return {}
        return {}

    def _save_data(self):
        """Salva os dados de uso no arquivo."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4)

    def _check_and_reset_daily(self):
        """Verifica se o dia mudou e reseta o contador se necessário."""
        today = datetime.date.today().isoformat() # Formato 'YYYY-MM-DD'

        if self.api_name not in self._data:
            self._data[self.api_name] = {"last_reset_date": today, "count": 0}
            self._save_data()
            print(f"UsageTracker: Dados iniciais para '{self.api_name}' criados.")
            return

        last_reset_date = self._data[self.api_name].get("last_reset_date")

        if last_reset_date != today:
            self._data[self.api_name]["last_reset_date"] = today
            self._data[self.api_name]["count"] = 0
            self._save_data()
            print(f"UsageTracker: Contador diário para '{self.api_name}' resetado para 0.")
        else:
            print(f"UsageTracker: Contador diário para '{self.api_name}' (Dia {today}): {self._data[self.api_name]['count']} de {self.limit} usos.")

    def increment_usage(self):
        """Incrementa o contador de uso."""
        self._data[self.api_name]["count"] += 1
        self._save_data()
        print(f"UsageTracker: Uso de '{self.api_name}' incrementado para {self._data[self.api_name]['count']}.")

    def get_current_usage(self) -> int:
        """Retorna o uso atual do dia."""
        return self._data[self.api_name]["count"]

    def is_within_limit(self) -> bool:
        """Verifica se o uso atual está dentro do limite diário."""
        return self.get_current_usage() < self.limit

    def get_remaining_uses(self) -> int:
        """Retorna o número de usos restantes para o dia."""
        return self.limit - self.get_current_usage()

if __name__ == "__main__":
    # Exemplo de uso para testar o rastreador
    tracker = UsageTracker(api_name="Google Search", limit=100, file_path="Google Search_usage.json")
    print(f"Está dentro do limite? {tracker.is_within_limit()}")

    if tracker.is_within_limit():
        tracker.increment_usage()
        print(f"Usos restantes: {tracker.get_remaining_uses()}")

    # Testar reset diário (mude a data no arquivo Google Search_usage.json para testar)
    print("\nSimulando novo dia...")
    tracker_new_day = UsageTracker(api_name="Google Search", limit=100, file_path="Google Search_usage.json")
    # Para testar o reset, altere manualmente a data em Google Search_usage.json para um dia anterior
    # e execute o script novamente.
    print(f"Usos após 'novo dia': {tracker_new_day.get_current_usage()}")