class ChatHistory:
    def __init__(self):
        self._history = []

    def add_message(self, role, text):
        self._history.append({'role': role, 'parts': [text]})
        self._history = self._history[-20:] # Limitar histórico se necessário

    def get_history(self):
        return self._history

    def clear_history(self):
        self._history = []
        print("Histórico da conversa limpo.")

    def print_history(self):
        print("\n--- Histórico da Conversa ---")
        for message in self._history:
            print(f"{message['role'].capitalize()}: {message['parts'][0]}")
        print("----------------------------")