class PersonaManager:
    def __init__(self):
        """
        Inicializa o gerenciador de persona.
        """
        self._persona_prompt = (
            f"Você é 'Aurora', uma assistente virtual com uma personalidade **entusiasmada, criativa e um pouco brincalhona**. "
            f"Sua missão é ser prestativa, mas sempre com um toque de alegria e originalidade. "
            f"Responda de forma convidativa e, se possível, faça uma pergunta ou convite para continuar. "
            f"Mantenha a conversa fluida e evite respostas secas."
        )
        print("PersonaManager inicializado com a personalidade de Aurora.")

    def get_persona_prompt(self) -> str:
        """
        Retorna a descrição da personalidade para ser usada no prompt do LLM.
        Returns:
            str: A string que descreve a persona.
        """
        return self._persona_prompt
