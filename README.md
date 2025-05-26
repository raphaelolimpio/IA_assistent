<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aurora: Documentação Completa do Projeto</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8F9FA;
            color: #212529;
            scroll-behavior: smooth;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 300px;
            max-height: 350px;
        }
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
                max-height: 400px;
            }
        }
        .section-card {
            background-color: #FFFFFF;
            border-radius: 0.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        .section-title {
            font-size: 2rem;
            font-weight: 700;
            color: #343A40;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #6C757D;
        }
        .subsection-title {
            font-size: 1.5rem;
            font-weight: 600;
            color: #495057;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }
        .content-text {
            font-size: 1rem;
            line-height: 1.6;
            color: #495057;
        }
        .hero-bg {
            background-color: #6C757D;
            color: #F8F9FA;
        }
        .hero-title {
            font-size: 2.5rem;
            font-weight: 700;
        }
        .hero-subtitle {
            font-size: 1.25rem;
            color: #E9ECEF;
        }
        .tree-view ul {
            list-style-type: none;
            padding-left: 1.5rem;
            position: relative;
        }
        .tree-view li {
            margin: 0.5rem 0;
            position: relative;
        }
        .tree-view li::before {
            content: '';
            position: absolute;
            top: -0.6em;
            left: -1rem;
            border-left: 1px solid #A0AEC0;
            height: 100%;
            width: 1px;
        }
        .tree-view li:last-child::before {
            height: 1.2em;
        }
        .tree-view li > span::before {
            content: '';
            position: absolute;
            top: 0.6em;
            left: -1rem;
            border-top: 1px solid #A0AEC0;
            width: 0.75rem;
            height: 0;
        }
        .tree-view .folder > span { font-weight: 600; color: #343A40; }
        .tree-view .file > span { color: #495057; }
        .tree-view .icon { margin-right: 0.5rem; color: #A0AEC0; }

        .accordion-button {
            background-color: #E9ECEF;
            color: #343A40;
            cursor: pointer;
            padding: 1rem;
            width: 100%;
            text-align: left;
            border: none;
            border-radius: 0.25rem;
            outline: none;
            transition: background-color 0.3s ease;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .accordion-button:hover {
            background-color: #CED4DA;
        }
        .accordion-content {
            padding: 0 1rem;
            background-color: white;
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out, padding 0.3s ease-out;
            border: 1px solid #E9ECEF;
            border-top: none;
            border-radius: 0 0 0.25rem 0.25rem;
        }
        .accordion-content.open {
            padding: 1rem;
        }
        .arrow-icon {
            transition: transform 0.3s ease;
        }
        .arrow-icon.open {
            transform: rotate(90deg);
        }
        .flow-step {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1rem;
            padding: 1rem;
            background-color: #E9ECEF;
            border-radius: 0.375rem;
        }
        .flow-step-number {
            font-size: 1.5rem;
            font-weight: 700;
            color: #6C757D;
            margin-right: 1rem;
            flex-shrink: 0;
            width: 2rem;
            text-align: center;
        }
        .flow-step-content {
            flex-grow: 1;
        }
        .flow-step-content strong { color: #343A40; }
        .code-block {
            background-color: #212529;
            color: #F8F9FA;
            padding: 1rem;
            border-radius: 0.25rem;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
            white-space: pre;
        }
        .chat-container {
            background-color: #F0F2F5;
            border-radius: 0.5rem;
            padding: 1rem;
            display: flex;
            flex-direction: column;
            height: 450px;
            overflow-y: auto;
            margin-bottom: 1rem;
        }
        .chat-message {
            margin-bottom: 0.75rem;
            padding: 0.5rem 0.75rem;
            border-radius: 0.5rem;
            max-width: 80%;
            word-wrap: break-word;
        }
        .chat-message.user {
            background-color: #E0F2F7;
            align-self: flex-end;
        }
        .chat-message.aurora {
            background-color: #D9EDF7;
            align-self: flex-start;
        }
        .chat-input-area {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        .chat-input-area textarea {
            flex-grow: 1;
            border: 1px solid #CED4DA;
            border-radius: 0.25rem;
            padding: 0.5rem;
            resize: vertical;
            min-height: 40px;
        }
        .chat-loading-indicator {
            text-align: center;
            margin-top: 0.5rem;
            font-style: italic;
            color: #6C757D;
        }
        .llm-button-group {
            display: flex;
            gap: 0.5rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }
        .llm-button-group button {
            flex-shrink: 0;
        }
    </style>
</head>
<body class="antialiased">

    <header class="hero-bg py-12 px-4 text-center">
        <div class="container mx-auto">
            <h1 class="hero-title mb-3">Aurora: Documentação Completa do Projeto</h1>
            <p class="hero-subtitle">Explore a arquitetura e o funcionamento do assistente virtual Aurora de forma clara e organizada.</p>
        </div>
    </header>

    <nav class="sticky top-0 bg-white shadow-md z-50">
        <div class="container mx-auto px-4">
            <div class="flex justify-center space-x-4 sm:space-x-8 py-3 overflow-x-auto whitespace-nowrap">
                <a href="#visao-geral" class="text-gray-600 hover:text-[#6C757D] font-medium">Visão Geral</a>
                <a href="#estrutura" class="text-gray-600 hover:text-[#6C757D] font-medium">Estrutura</a>
                <a href="#modulos" class="text-gray-600 hover:text-[#6C757D] font-medium">Módulos</a>
                <a href="#fluxo-operacional" class="text-gray-600 hover:text-[#6C757D] font-medium">Fluxo</a>
                <a href="#configuracao" class="text-gray-600 hover:text-[#6C757D] font-medium">Configuração</a>
                <a href="#padroes-design" class="text-gray-600 hover:text-[#6C757D] font-medium">Padrões</a>
                <a href="#consideracoes-finais" class="text-gray-600 hover:text-[#6C757D] font-medium">Finais</a>
                <a href="#perguntar-aurora" class="text-gray-600 hover:text-[#6C757D] font-medium">Perguntar à Aurora ✨</a>
            </div>
        </div>
    </nav>

    <main class="container mx-auto p-4 md:p-8">

        <section id="visao-geral" class="section-card">
            <h2 class="section-title">Visão Geral do Projeto</h2>
            <p class="content-text mb-4">
                O projeto <strong>Aurora</strong> é um assistente virtual interativo desenvolvido em Python, com foco em comunicação por voz (Speech-to-Text e Text-to-Speech) e na utilização de inteligência artificial (Large Language Model - Google Gemini) para processar requisições complexas e interagir com ferramentas externas, como APIs de clima e pesquisa web.
            </p>
            <h3 class="subsection-title">Objetivo</h3>
            <p class="content-text mb-4">
                Criar um assistente prestativo, com uma personalidade entusiasta e criativa, capaz de responder a perguntas, fornecer informações contextuais e realizar buscas dinâmicas, gerenciando eficientemente o uso de recursos de API.
            </p>
            <h3 class="subsection-title">Tecnologias Principais</h3>
            <ul class="list-disc list-inside content-text space-y-1">
                <li><span class="icon">🐍</span>Python: Linguagem de programação principal.</li>
                <li><span class="icon">✨</span>Google Gemini API: Para a inteligência do LLM e integração com ferramentas.</li>
                <li><span class="icon">🎤</span>Speech Recognition: Transcrição de fala para texto.</li>
                <li><span class="icon">🗣️</span>gTTS (Google Text-to-Speech): Conversão de texto para fala.</li>
                <li><span class="icon">🔊</span>Sounddevice & Soundfile: Para reprodução de áudio de baixa latência.</li>
                <li><span class="icon">🌦️</span>WeatherAPI.com: Para dados climáticos.</li>
                <li><span class="icon">🔍</span>Google Custom Search API: Para pesquisa web.</li>
                <li><span class="icon">🌐</span>Requests: Para requisições HTTP a APIs externas.</li>
                <li><span class="icon">⚙️</span>python-dotenv: Para gerenciamento seguro de variáveis de ambiente.</li>
            </ul>
        </section>

        <section id="estrutura" class="section-card">
            <h2 class="section-title">Estrutura do Projeto</h2>
            <p class="content-text mb-4">
                A arquitetura do Aurora é baseada em um design modular e desacoplado, facilitando a manutenção, escalabilidade e a adição de novas funcionalidades. Abaixo, a estrutura de pastas do projeto e uma visualização da distribuição de componentes.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                <div>
                    <h3 class="subsection-title">Estrutura de Pastas</h3>
                    <div class="tree-view bg-gray-50 p-4 rounded-md text-sm">
                        <ul>
                            <li class="folder"><span class="icon">📁</span>.
                                <ul>
                                    <li class="folder"><span class="icon">📁</span>audio/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>speak.py</li>
                                        </ul>
                                    </li>
                                    <li class="folder"><span class="icon">📁</span>conscience/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>__init__.py</li>
                                            <li class="file"><span class="icon">📄</span>context_manager.py</li>
                                            <li class="file"><span class="icon">📄</span>persona_manager.py</li>
                                            <li class="file"><span class="icon">📄</span>usage_tracker.py</li>
                                        </ul>
                                    </li>
                                    <li class="folder"><span class="icon">📁</span>core/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>__init__.py</li>
                                            <li class="file"><span class="icon">📄</span>assistant.py</li>
                                        </ul>
                                    </li>
                                    <li class="folder"><span class="icon">📁</span>llm/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>__init__.py</li>
                                            <li class="file"><span class="icon">📄</span>generator.py</li>
                                        </ul>
                                    </li>
                                    <li class="folder"><span class="icon">📁</span>memory/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>__init__.py</li>
                                            <li class="file"><span class="icon">📄</span>chat_history.py</li>
                                        </ul>
                                    </li>
                                    <li class="folder"><span class="icon">📁</span>nlp/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>__init__.py</li>
                                            <li class="file"><span class="icon">📄</span>processing.py</li>
                                        </ul>
                                    </li>
                                    <li class="folder"><span class="icon">📁</span>tools/
                                        <ul>
                                            <li class="file"><span class="icon">📄</span>__init__.py</li>
                                            <li class="file"><span class="icon">📄</span>weather_tool.py</li>
                                            <li class="file"><span class="icon">📄</span>web_search_tool.py</li>
                                        </ul>
                                    </li>
                                    <li class="file"><span class="icon">📄</span>main.py</li>
                                    <li class="file"><span class="icon">🔒</span>.env</li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
                <div>
                    <h3 class="subsection-title">Contagem de Componentes por Módulo</h3>
                    <div class="chart-container h-[300px] md:h-[380px]">
                        <canvas id="moduleComponentsChart"></canvas>
                    </div>
                    <p class="text-xs text-center mt-2 text-gray-500">Este gráfico de barras ilustra o número de arquivos Python principais (excluindo `__init__.py`) em cada diretório de módulo principal, oferecendo uma visão da distribuição de funcionalidade.</p>
                </div>
            </div>
        </section>

        <section id="modulos" class="section-card">
            <h2 class="section-title">Detalhamento dos Módulos e Racional de Escolha</h2>
            <p class="content-text mb-6">
                Cada módulo do projeto Aurora tem um propósito específico. Clique em cada um para expandir e ver mais detalhes sobre suas funções e dependências, e o racional por trás de sua escolha. Use o botão "Resumir Seção" para um resumo rápido via IA!
            </p>
            
            <div class="space-y-3">
                <div>
                    <button class="accordion-button">
                        <span><code>audio/speak.py</code> - Comunicação Vocal</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Habilitar a comunicação vocal bidirecional (usuário -> assistente e assistente -> usuário).</p>
                        <p class="content-text"><strong>Funções Principais:</strong> <code>ouvir_microfone()</code> (Speech-to-Text) e <code>falar()</code> (Text-to-Speech).</p>
                        <p class="content-text"><strong>Dependências:</strong> <code>speech_recognition</code>, <code>gTTS</code>, <code>soundfile</code>, <code>sounddevice</code>, <code>os</code>, <code>time</code>.</p>
                        <p class="content-text"><strong>Racional de Escolha:</strong></p>
                        <ul class="list-disc list-inside content-text pl-4">
                            <li><code>speech_recognition</code>: Biblioteca popular e flexível, com suporte a várias APIs de reconhecimento de fala, incluindo Google Speech Recognition, que oferece boa precisão para português. Inclui timeout e phrase_time_limit para controle do fluxo da escuta.</li>
                            <li><code>gTTS</code>: Simples e eficaz para gerar áudio a partir de texto usando a voz do Google, com suporte a várias línguas.</li>
                            <li><code>soundfile</code> e <code>sounddevice</code>: Escolhidos por sua robustez e capacidade de fornecer controle de baixo nível sobre a reprodução de áudio. Eles resolvem problemas de compatibilidade e de liberação de recursos de áudio que ocorriam com outras bibliotecas (playsound, pydub), garantindo uma reprodução fluida e a continuidade do loop do assistente. Uma pequena pausa (<code>time.sleep</code>) é adicionada após a reprodução para garantir a liberação do dispositivo de áudio.</li>
                        </ul>
                        <p class="content-text mt-2"><strong>Observações:</strong> A criação de um novo objeto <code>sr.Recognizer()</code> a cada chamada de <code>ouvir_microfone()</code> ajuda a reiniciar os recursos do microfone, mitigando problemas de escuta contínua em alguns sistemas.</p>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>

                <div>
                    <button class="accordion-button">
                        <span><code>conscience/</code> - Módulos de Consciência</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Prover ao assistente uma camada de "conhecimento" sobre si mesmo, o ambiente e suas capacidades, além de gerenciar recursos de forma persistente.</p>
                        <ul class="list-disc list-inside content-text mt-2 space-y-1 pl-4">
                            <li><strong><code>context_manager.py</code>:</strong>
                                <p><strong>Propósito:</strong> Obter e gerenciar informações contextuais em tempo real, como data, hora e localização geográfica.</p>
                                <p><strong>Funções Principais:</strong> <code>get_current_time()</code>, <code>get_default_location()</code>.</p>
                                <p><strong>Dependências:</strong> <code>datetime</code>, <code>requests</code>, <code>json</code>.</p>
                                <p><strong>Racional:</strong> Informações contextuais (hora, localização) tornam a interação mais natural e útil, permitindo respostas mais personalizadas sem que o usuário precise fornecer esses dados. Uso de <code>ip-api.com</code> para obter localização baseada em IP é uma abordagem simples, gratuita e eficaz. Implementa um mecanismo de cache para otimizar o uso da API.</p>
                            </li>
                            <li><strong><code>persona_manager.py</code>:</strong>
                                <p><strong>Propósito:</strong> Definir e injetar a personalidade do assistente nas respostas do LLM.</p>
                                <p><strong>Funções Principais:</strong> <code>get_persona_prompt()</code>.</p>
                                <p><strong>Dependências:</strong> Nenhuma externa direta, apenas strings.</p>
                                <p><strong>Racional:</strong> Garante que o assistente "Aurora" mantenha uma voz e estilo consistentes em todas as interações delegadas ao LLM, tornando a experiência do usuário mais agradável, engajadora e única. A injeção da persona via prompt é uma técnica padrão de Prompt Engineering.</p>
                            </li>
                            <li><strong><code>usage_tracker.py</code>:</strong>
                                <p><strong>Propósito:</strong> Monitorar, limitar e persistir o uso de APIs externas para evitar custos excessivos ou violações de limites de requisição.</p>
                                <p><strong>Funções Principais:</strong> <code>increment_usage()</code>, <code>is_within_limit()</code>, <code>get_remaining_uses()</code>.</p>
                                <p><strong>Dependências:</strong> <code>datetime</code>, <code>json</code>, <code>os</code>.</p>
                                <p><strong>Racional:</strong> Essencial para a sustentabilidade e viabilidade do projeto, especialmente com APIs que impõem limites diários de uso. O rastreamento em um arquivo JSON permite que o contador seja persistente entre as execuções do programa.</p>
                            </li>
                        </ul>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>
                
                <div>
                    <button class="accordion-button">
                        <span><code>core/assistant.py</code> - Lógica Central (Orquestrador)</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Agrupar os componentes principais que definem o comportamento e o fluxo do assistente. Atua como o maestro, coordenando a interação entre todos os outros módulos.</p>
                        <p class="content-text"><strong>Funções Principais:</strong> <code>__init__()</code>, <code>_adicionar_ao_historico()</code>, <code>_obter_resposta()</code>, <code>run()</code>.</p>
                        <p class="content-text"><strong>Dependências:</strong> Módulos internos (<code>audio</code>, <code>nlp</code>, <code>memory</code>, <code>conscience</code>, <code>llm</code>).</p>
                        <p class="content-text"><strong>Racional de Escolha:</strong> Implementa o loop principal de interação (<code>while True</code>). Delega tarefas especializadas para os módulos específicos. Implementa um roteamento de intenções híbrido:</p>
                        <ul class="list-disc list-inside content-text pl-4 mt-2">
                            <li><strong>Intenções Locais:</strong> Para <code>saudacao</code>, <code>pedir_horas</code>, <code>agradecimento</code>, <code>despedida</code>, as respostas são geradas localmente para maior velocidade e controle.</li>
                            <li><strong>Intenção <code>pesquisar_web</code> (Controlada):</strong> Antes de envolver o LLM, o Assistant verifica o limite de uso diário via <code>UsageTracker</code>. Se o limite for excedido, ele responde diretamente ao usuário. Caso contrário, delega a tarefa de pesquisa e resposta ao <code>LLMGenerator</code>.</li>
                            <li><strong>Outras Intenções (Delegadas ao LLM):</strong> Para <code>pedir_clima</code> e <code>intencao_desconhecida</code> (qualquer outra pergunta), a requisição é diretamente delegada ao <code>LLMGenerator</code>, que então utiliza o LLM e suas ferramentas para formular a resposta.</li>
                        </ul>
                        <p class="content-text mt-2">Promove o padrão de "controlador" que delega tarefas aos módulos especializados, mantendo o <code>assistant.py</code> focado no fluxo geral.</p>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>

                <div>
                    <button class="accordion-button">
                        <span><code>llm/generator.py</code> - Módulo do Large Language Model</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Encapsular toda a lógica de interação com o Google Gemini e gerenciar as ferramentas que o LLM pode utilizar.</p>
                        <p class="content-text"><strong>Funções Principais:</strong> <code>__init__()</code>, <code>generate_response()</code>.</p>
                        <p class="content-text"><strong>Dependências:</strong> <code>google.generativeai</code>, <code>os</code>, <code>dotenv</code>, <code>tools.weather_tool</code>, <code>tools.web_search_tool</code>, <code>conscience.persona_manager</code>, <code>conscience.usage_tracker</code>, <code>json</code>.</p>
                        <p class="content-text"><strong>Racional de Escolha:</strong></p>
                        <ul class="list-disc list-inside content-text pl-4">
                            <li><strong>Google Gemini (<code>models/gemini-1.5-flash-latest</code>):</strong> Escolhido por sua capacidade de processamento de linguagem natural, sua habilidade de seguir instruções e, crucialmente, seu suporte nativo a <strong>chamadas de função (Function Calling)</strong>. O modelo "flash" é otimizado para velocidade.</li>
                            <li><strong>Function Calling Centralizado:</strong> O modelo Gemini é configurado com a lista de <code>tools=[]</code> (passando as funções <code>get_weather_data</code> e <code>search_web</code>). Quando o LLM detecta que a intenção do usuário pode ser satisfeita por uma dessas ferramentas, ele gera uma <code>function_call</code>. O <code>LLMGenerator</code> intercepta essa chamada, executa a função Python real e, então, injeta o resultado da ferramenta de volta no LLM para que ele formule a resposta final ao usuário de forma natural.</li>
                            <li><strong>Controle de Uso de Busca na Web:</strong> O <code>UsageTracker</code> é usado aqui para incrementar o contador de uso da API de busca apenas quando o Gemini realmente decide e executa a <code>search_web</code>.</li>
                            <li><strong><code>persona_manager</code>:</strong> Integrado para que o <code>LLMGenerator</code> sempre infunda a personalidade definida nos prompts enviados ao Gemini.</li>
                        </ul>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>

                <div>
                    <button class="accordion-button">
                        <span><code>memory/chat_history.py</code> - Módulo de Memória</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Manter um registro das interações passadas para dar ao assistente um senso de contexto e coerência.</p>
                        <p class="content-text"><strong>Funções Principais:</strong> <code>add_message()</code>, <code>get_history()</code>, <code>clear_history()</code>.</p>
                        <p class="content-text"><strong>Dependências:</strong> Nenhuma.</p>
                        <p class="content-text"><strong>Racional de Escolha:</strong> A capacidade de um LLM de manter uma conversa coerente e relevante depende criticamente de um histórico de conversa. O limite de 20 mensagens (<code>self._history = self._history[-20:]</code>) é uma estratégia comum para gerenciar o tamanho do contexto do LLM, equilibrando coerência da conversa, custos de tokens e latência.</p>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>

                <div>
                    <button class="accordion-button">
                        <span><code>nlp/processing.py</code> - Processamento de Linguagem Natural</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Realizar a análise inicial do texto de entrada do usuário para identificar intenções básicas de forma eficiente.</p>
                        <p class="content-text"><strong>Funções Principais:</strong> <code>processar_texto()</code>.</p>
                        <p class="content-text"><strong>Dependências:</strong> Nenhuma.</p>
                        <p class="content-text"><strong>Racional de Escolha:</strong> Implementa uma estratégia híbrida de NLP: utiliza regras simples (<code>if/elif</code> com palavras-chave) para intenções de alta confiança e que podem ser tratadas rapidamente (saudação, hora, agradecimentos, despedidas, e o gatilho para "pesquisa na web"). Para intenções mais complexas ou ambíguas, a requisição é delegada ao <code>LLMGenerator</code> para análise semântica mais profunda e execução de tarefas via LLM.</p>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>

                <div>
                    <button class="accordion-button">
                        <span><code>tools/</code> - Módulos de Ferramentas</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> Encapsular a lógica para interagir com APIs e serviços externos, estendendo as capacidades do assistente para além do que o LLM pode fazer intrinsecamente.</p>
                        <ul class="list-disc list-inside content-text mt-2 space-y-1 pl-4">
                            <li><strong><code>weather_tool.py</code>:</strong>
                                <p><strong>Propósito:</strong> Interagir com a WeatherAPI.com para obter dados climáticos.</p>
                                <p><strong>Funções Principais:</strong> <code>get_weather_data()</code>.</p>
                                <p><strong>Dependências:</strong> <code>requests</code>, <code>os</code>, <code>dotenv</code>, <code>json</code>.</p>
                                <p><strong>Racional:</strong> <code>requests</code> é a biblioteca padrão para fazer requisições HTTP em Python, robusta e amplamente utilizada. A encapsulação da lógica de API em uma função dedicada permite que o LLM a "chame" de forma programática via Function Calling. Inclui tratamento de erros robusto para falhas na API.</p>
                            </li>
                            <li><strong><code>web_search_tool.py</code>:</strong>
                                <p><strong>Propósito:</strong> Interagir com a Google Custom Search API para realizar pesquisas web.</p>
                                <p><strong>Funções Principais:</strong> <code>search_web()</code>.</p>
                                <p><strong>Dependências:</strong> <code>requests</code>, <code>os</code>, <code>dotenv</code>.</p>
                                <p><strong>Racional:</strong> Permite ao assistente buscar informações na internet, estendendo significativamente seu "conhecimento" para além dos dados de treinamento do LLM (que podem estar desatualizados ou não cobrir tudo). Essencial para perguntas sobre eventos atuais, notícias ou informações muito específicas. Também encapsulada para ser chamada pelo LLM.</p>
                            </li>
                        </ul>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>

                <div>
                    <button class="accordion-button">
                        <span><code>main.py</code> - Ponto de Entrada</span>
                        <span class="arrow-icon">▶</span>
                    </button>
                    <div class="accordion-content">
                        <p class="content-text mt-2"><strong>Propósito:</strong> O ponto de entrada principal do aplicativo.</p>
                        <p class="content-text"><strong>Dependências:</strong> <code>core.assistant</code>.</p>
                        <p class="content-text"><strong>Racional:</strong> Segue a convenção Python para iniciar a execução de um programa, mantendo-o simples e focado apenas na inicialização do assistente.</p>
                        <div class="llm-button-group">
                            <button class="summarize-button px-4 py-2 bg-[#A0AEC0] text-white rounded-md hover:bg-[#6C757D] transition-colors duration-200">Resumir Seção ✨</button>
                        </div>
                        <div class="summary-output mt-2 text-sm text-gray-700"></div>
                        <div class="loading-indicator hidden mt-2 text-sm text-[#6C757D]">Gerando...</div>
                    </div>
                </div>
            </div>
        </section>

        <section id="fluxo-operacional" class="section-card">
            <h2 class="section-title">Fluxo de Execução Detalhado: "Aurora, pesquise para mim o que é computação quântica."</h2>
            <p class="content-text mb-6">
                Para ilustrar como o Aurora funciona de ponta a ponta, vamos seguir o fluxo de uma pergunta que envolve o uso de uma ferramenta externa, como a pesquisa na web.
            </p>
            <div class="space-y-4">
                <div class="flow-step">
                    <div class="flow-step-number">1.</div>
                    <div class="flow-step-content">
                        <strong><code>main.py</code> (Ponto de Entrada):</strong> O script <code>main.py</code> é executado, inicializando a classe <code>Assistant</code>.
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">2.</div>
                    <div class="flow-step-content">
                        <strong><code>core/assistant.py</code> (Inicialização e Contexto):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li>Instancia <code>ChatHistory</code>, <code>ContextManager</code> (que tenta obter a localização em tempo real), <code>PersonaManager</code> e <code>UsageTracker</code> (para controle de busca).</li>
                            <li>Instancia <code>LLMGenerator</code>, passando a ele a instância de <code>ChatHistory</code>. O <code>LLMGenerator</code> inicializa o Gemini e registra as ferramentas <code>get_weather_data</code> e <code>search_web</code>.</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">3.</div>
                    <div class="flow-step-content">
                        <strong><code>core/assistant.py</code> (<code>run()</code> - Loop Principal):</strong> O método <code>run()</code> entra em seu loop contínuo de interação. Uma mensagem como "Estou ouvindo... Diga algo:" é exibida.
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">4.</div>
                    <div class="flow-step-content">
                        <strong><code>audio/speak.py</code> (Ouvir Microfone):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li><code>ouvir_microfone()</code> ativa o microfone e captura a fala do usuário: "Aurora, pesquise para mim o que é computação quântica."</li>
                            <li>O áudio é enviado para o serviço Google Speech Recognition e transcrito.</li>
                            <li>Retorna a frase em texto: "aurora, pesquise para mim o que é computação quântica."</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">5.</div>
                    <div class="flow-step-content">
                        <strong><code>memory/chat_history.py</code> (Atualizar Histórico):</strong> A frase do usuário é adicionada ao histórico da conversa.
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">6.</div>
                    <div class="flow-step-content">
                        <strong><code>nlp/processing.py</code> (Processar Intenção):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li>A frase é passada para <code>processar_texto()</code>.</li>
                            <li>A função detecta "pesquise para mim" e retorna a intenção "pesquisar_web".</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">7.</div>
                    <div class="flow-step-content">
                        <strong><code>core/assistant.py</code> (Tomada de Decisão e Controle de Uso):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li>A intenção "pesquisar_web" é detectada.</li>
                            <li>O Assistant verifica <code>self.search_tracker.is_within_limit()</code>.</li>
                            <li><strong>Cenário A: Limite Excedido:</strong> Se o contador de busca já atingiu o limite, o Assistant formula uma resposta direta informando o limite, adiciona-a ao histórico, e a IA fala essa mensagem, sem chamar o <code>LLMGenerator</code> ou a API de busca. O loop continua.</li>
                            <li><strong>Cenário B: Dentro do Limite (Nosso Exemplo):</strong> Se o limite não foi excedido, a requisição é delegada ao <code>LLMGenerator</code>.</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">8.</div>
                    <div class="flow-step-content">
                        <strong><code>llm/generator.py</code> (Gerar Resposta com LLM e Ferramenta):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li><code>generate_response("aurora, pesquise para mim o que é computação quântica.")</code> é chamada.</li>
                            <li>O prompt da persona e o histórico do chat são usados para iniciar uma sessão com o Gemini.</li>
                            <li>O Gemini analisa a frase do usuário e, pré-configurado com as ferramentas, reconhece que a pergunta pode ser respondida pela ferramenta <code>search_web</code>.</li>
                            <li>O LLM retorna uma <code>function_call</code> para <code>search_web</code> com <code>query="computação quântica"</code>.</li>
                            <li>O <code>LLMGenerator</code> intercepta essa <code>function_call</code>.</li>
                            <li>Ele chama <code>self.search_tracker.increment_usage()</code> (incrementando o contador de uso da busca).</li>
                            <li>Ele executa a função Python <code>search_web(query="computação quântica")</code>.</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">9.</div>
                    <div class="flow-step-content">
                        <strong><code>tools/web_search_tool.py</code> (Execução da Ferramenta):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li><code>search_web("computação quântica")</code> faz uma requisição HTTP para a Google Custom Search API.</li>
                            <li>Recebe os resultados da pesquisa (títulos, links, snippets).</li>
                            <li>Retorna uma string formatada com esses resultados.</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">10.</div>
                    <div class="flow-step-content">
                        <strong><code>llm/generator.py</code> (Resposta Final do LLM):</strong>
                        <ul class="list-disc list-inside text-sm mt-1 pl-4">
                            <li>O <code>LLMGenerator</code> envia o resultado da ferramenta (a string com os resultados da pesquisa) de volta para a sessão do Gemini.</li>
                            <li>O Gemini, usando sua personalidade (Aurora), formula uma resposta amigável e entusiasmada baseada nos resultados da pesquisa. Ex: "Que pergunta fantástica! A computação quântica é um campo revolucionário que usa os princípios da mecânica quântica para resolver problemas complexos. É um universo de possibilidades, com computadores que operam de formas que nem imaginamos. Pronta para mais descobertas?"</li>
                            <li>Esta resposta final é retornada ao <code>assistant.py</code>.</li>
                        </ul>
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">11.</div>
                    <div class="flow-step-content">
                        <strong><code>memory/chat_history.py</code> (Atualizar Histórico):</strong> A resposta final da IA é adicionada ao histórico da conversa.
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">12.</div>
                    <div class="flow-step-content">
                        <strong><code>audio/speak.py</code> (Falar Resposta):</strong> A resposta final do Gemini é passada para <code>falar()</code>, que a converte em áudio e a reproduz.
                    </div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-number">13.</div>
                    <div class="flow-step-content">
                        <strong><code>core/assistant.py</code> (Continuar Loop):</strong> O assistente aguarda a próxima interação do usuário, exibindo "Estou ouvindo... Diga algo:".
                    </div>
                </div>
            </div>
        </section>

        <section id="configuracao" class="section-card">
            <h2 class="section-title">Configuração Essencial (`.env`)</h2>
            <p class="content-text mb-4">
                Para o correto funcionamento do Aurora, é crucial configurar as chaves de API em um arquivo <code>.env</code> na raiz do projeto. Este arquivo <strong>não deve</strong> ser enviado para repositórios de código (ex: Git), para evitar a exposição de credenciais sensíveis.
            </p>
            <div class="code-block">
# Google Gemini API Key
GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY_HERE"

# WeatherAPI.com Key
WEATHERAPI_API_KEY="YOUR_WEATHERAPI_KEY_HERE"

# Google Custom Search API Key and Custom Search Engine ID
Google Search_API_KEY="YOUR_Google Search_API_KEY_HERE"
Google Search_CX="YOUR_Google Search_CX_ID_HERE"
            </div>
            <p class="content-text mt-4">
                <strong>Como obter estas chaves:</strong>
            </p>
            <ul class="list-disc list-inside content-text space-y-1 pl-4">
                <li><strong><code>GEMINI_API_KEY</code>:</strong> Obtível no <a href="https://aistudio.google.com/app/apikey" target="_blank" class="text-[#6C757D] hover:underline">Google AI Studio</a> ou Google Cloud Console (habilitar Gemini API).</li>
                <li><strong><code>WEATHERAPI_API_KEY</code>:</strong> Registre-se em <a href="https://www.weatherapi.com/" target="_blank" class="text-[#6C757D] hover:underline">www.weatherapi.com</a> para obter sua chave de API gratuita.</li>
                <li><strong><code>Google Search_API_KEY</code> e <code>Google Search_CX</code>:</strong>
                    <ul class="list-circle list-inside pl-4">
                        <li><strong>API Key:</strong> No <a href="https://console.cloud.google.com/" target="_blank" class="text-[#6C757D] hover:underline">Google Cloud Console</a>, crie um projeto, navegue até "APIs & Services" -> "Credenciais", e crie uma chave de API. Recomenda-se restringi-la à "Custom Search API".</li>
                        <li><strong>CX ID:</strong> No <a href="https://programmablesearchengine.google.com/" target="_blank" class="text-[#6C757D] hover:underline">Google Programmable Search Engine</a>, crie um novo mecanismo de pesquisa (pode ser para <code>www.google.com</code> para toda a web), e você obterá um "Search engine ID" (CX).</li>
                    </ul>
                </li>
            </ul>
        </section>

        <section id="padroes-design" class="section-card">
            <h2 class="section-title">Padrões de Design e Metodologias</h2>
            <p class="content-text mb-4">
                O projeto Aurora emprega diversos padrões e metodologias para garantir uma arquitetura robusta, modular e de fácil manutenção. Esta seção detalha as abordagens de design adotadas.
            </p>
            <h3 class="subsection-title">Arquitetura Modular / Camadas</h3>
            <p class="content-text mb-2">
                O projeto é estruturado em módulos lógicos (<code>audio</code>, <code>conscience</code>, <code>core</code>, <code>llm</code>, <code>memory</code>, <code>nlp</code>, <code>tools</code>), cada um com responsabilidades bem definidas. Isso promove:
            </p>
            <ul class="list-disc list-inside content-text space-y-1 pl-4">
                <li><strong>Alta Coesão:</strong> Funções e classes relacionadas são agrupadas dentro de seus respectivos módulos.</li>
                <li><strong>Baixo Acoplamento:</strong> Módulos são independentes e se comunicam através de interfaces bem definidas (chamadas de função/método), minimizando dependências e facilitando a substituição ou atualização de componentes sem afetar outras partes do sistema.</li>
            </ul>

            <h3 class="subsection-title">Injeção de Dependência (via Construtor)</h3>
            <p class="content-text mb-2">
                Objetos de gerenciamento de estado e contexto (<code>ChatHistory</code>, <code>ContextManager</code>, <code>PersonaManager</code>, <code>UsageTracker</code>) e o <code>LLMGenerator</code> são instanciados e passados para outros módulos (principalmente para o <code>Assistant</code> e <code>LLMGenerator</code>) via construtor. Isso:
            </p>
            <ul class="list-disc list-inside content-text space-y-1 pl-4">
                <li>Promove o acoplamento fraco, pois os módulos não precisam criar suas próprias dependências, mas as recebem.</li>
                <li>Facilita testes unitários, permitindo a injeção de *mocks* (objetos simulados) em ambientes de teste.</li>
            </ul>

            <h3 class="subsection-title">Estratégia Híbrida de Processamento de Intenções (Regras + LLM com Ferramentas)</h3>
            <p class="content-text mb-2">
                O sistema emprega uma abordagem em camadas para processar as intenções do usuário:
            </p>
            <ul class="list-disc list-inside content-text space-y-1 pl-4">
                <li><strong><code>nlp/processing.py</code> (Camada de Regras):</strong> Utiliza uma estratégia baseada em regras (<code>if/elif</code> com palavras-chave) para detectar intenções simples e de alta confiança (saudações, horas, agradecimentos, despedidas) e a intenção de "pesquisar_web". Isso otimiza o desempenho e economiza chamadas ao LLM para tarefas triviais.</li>
                <li><strong><code>core/assistant.py</code> (Camada de Roteamento/Controle):</strong> Atua como um router para as intenções detectadas:
                    <ul class="list-circle list-inside pl-4">
                        <li><strong>Respostas Locais:</strong> Para intenções como <code>saudacao</code> ou <code>pedir_horas</code>, o Assistant gera e fornece a resposta diretamente, sem envolver o LLM.</li>
                        <li><strong>Controle de Ferramentas com Limite (<code>pesquisar_web</code>):</strong> Antes de delegar uma pesquisa na web, o Assistant verifica o limite de uso diário da API de busca via <code>UsageTracker</code>. Se o limite for excedido, ele responde diretamente ao usuário. Caso contrário, a requisição é passada para o <code>LLMGenerator</code>.</li>
                        <li><strong>Delegação ao LLM (<code>pedir_clima</code> e <code>intencao_desconhecida</code>):</strong> Para intenções que exigem compreensão complexa ou uso de ferramentas pelo LLM (como <code>pedir_clima</code> ou qualquer pergunta geral), a requisição é delegada ao <code>LLMGenerator</code>.</li>
                    </ul>
                </li>
                <li><strong><code>llm/generator.py</code> (Camada LLM e Ferramentas):</strong> Para intenções delegadas, o <code>LLMGenerator</code> utiliza o LLM (Gemini) para análise semântica mais profunda, geração de respostas criativas e, crucialmente, para orquestrar o uso de ferramentas externas.</li>
            </ul>

            <h3 class="subsection-title">Function Calling (Google Gemini)</h3>
            <p class="content-text mb-2">
                Um dos padrões mais críticos para a extensibilidade do assistente. O LLM (<code>models/gemini-1.5-flash-latest</code>) é configurado com a descrição das ferramentas externas disponíveis (<code>get_weather_data</code>, <code>search_web</code>). Quando o LLM (<code>generate_response()</code> no <code>llm/generator.py</code>) detecta que a intenção do usuário pode ser satisfeita por uma dessas ferramentas, ele gera uma <code>function_call</code> (uma chamada de função simulada com seus argumentos). O <code>LLMGenerator</code> intercepta essa chamada, executa a função Python correspondente (da pasta <code>tools/</code>) e, então, injeta o resultado da ferramenta de volta no LLM para que ele formule a resposta final ao usuário de forma natural, mantendo a personalidade. Isso permite ao LLM "agir" no mundo real e expandir seu conhecimento.
            </p>

            <h3 class="subsection-title">Gerenciamento de Estado de Conversa (Chat History)</h3>
            <p class="content-text mb-2">
                O <code>memory/chat_history.py</code> implementa um gerenciador de estado para a conversação. A manutenção de um histórico (<code>_history</code>) é vital para que o LLM compreenda o contexto e mantenha a coerência do diálogo, permitindo que a IA se lembre de referências anteriores. A estratégia de "janela deslizante" (manter apenas as últimas 20 mensagens) é um padrão comum para gerenciar o tamanho do contexto do LLM, equilibrando coerência, custos de tokens e latência.
            </p>

            <h3 class="subsection-title">Gerenciamento de Recursos Persistente (Usage Tracker)</h3>
            <p class="content-text mb-2">
                O <code>conscience/usage_tracker.py</code> implementa um padrão de contador e limite diário para APIs externas, persistindo os dados em um arquivo JSON (<code>Google Search_usage.json</code>). Isso é fundamental para gerenciar o consumo de APIs que impõem limites de requisição ou têm custos associados, garantindo a operabilidade contínua do assistente sem interrupções por exaustão de cota, e fornecendo feedback ao usuário sobre seu uso.
            </p>

            <h3 class="subsection-title">Configuração Externa (dotenv)</h3>
            <p class="content-text mb-2">
                O uso de <code>.env</code> para variáveis de ambiente (chaves de API) segue o princípio das "12 Fatores" (Twelve-Factor App), promovendo:
            </p>
            <ul class="list-disc list-inside content-text space-y-1 pl-4">
                <li><strong>Segurança:</strong> Chaves sensíveis não são commitadas para o controle de versão (ex: GitHub).</li>
                <li><strong>Portabilidade:</strong> O código pode ser implantado em diferentes ambientes (desenvolvimento, produção) sem modificações, apenas alterando o arquivo <code>.env</code>.</li>
            </ul>
        </section>

        <section id="consideracoes-finais" class="section-card">
            <h2 class="section-title">Considerações Finais</h2>
            <p class="content-text mb-4">
                A arquitetura proposta para o assistente Aurora demonstra uma abordagem robusta para o desenvolvimento de sistemas de conversação inteligentes e interativos. A modularidade, a integração inteligente de LLMs com *function calling*, e a atenção ao gerenciamento de recursos e estado (incluindo persistência para uso de API) são cruciais para a construção de assistentes virtuais eficientes, escaláveis e amigáveis ao usuário.
            </p>
            <p class="content-text">
                Futuras melhorias podem incluir a adição de mais ferramentas, um sistema de hotword para ativação do assistente, e uma interface de usuário mais sofisticada.
            </p>
        </section>

        <section id="perguntar-aurora" class="section-card">
            <h2 class="section-title">Perguntar à Aurora ✨</h2>
            <p class="content-text mb-4">
                Tem alguma dúvida específica sobre o projeto Aurora? Pergunte à nossa assistente de IA, e ela tentará responder com base nesta documentação!
            </p>
            <div id="chat-display" class="chat-container">
                <div class="chat-message aurora">Olá! Sou a Aurora, sua assistente de documentação. Como posso ajudar a explorar o projeto?</div>
            </div>
            <div class="chat-input-area">
                <textarea id="user-question" placeholder="Digite sua pergunta aqui..." rows="2"></textarea>
                <button id="ask-aurora-button" class="px-4 py-2 bg-[#6C757D] text-white rounded-md hover:bg-[#495057] transition-colors duration-200">Perguntar ✨</button>
            </div>
            <div id="chat-loading-indicator" class="chat-loading-indicator hidden">Aurora está pensando...</div>
            <div id="full-doc-text" class="hidden">
                <p>O projeto Aurora é um assistente virtual interativo desenvolvido em Python, com foco em comunicação por voz (Speech-to-Text e Text-to-Speech) e na utilização de inteligência artificial (Large Language Model - Google Gemini) para processar requisições complexas e interagir com ferramentas externas, como APIs de clima e pesquisa web.</p>
                <p>Objetivo: Criar um assistente prestativo, com uma personalidade entusiasta e criativa, capaz de responder a perguntas, fornecer informações contextuais e realizar buscas dinâmicas, gerenciando eficientemente o uso de recursos de API.</p>
                <p>Tecnologias Principais: Python, Google Gemini API, Speech Recognition, gTTS (Google Text-to-Speech), Sounddevice & Soundfile, WeatherAPI.com, Google Custom Search API, Requests, python-dotenv.</p>
                <p>Estrutura do Projeto: O projeto é organizado em módulos lógicos: audio/ (speak.py), conscience/ (context_manager.py, persona_manager.py, usage_tracker.py), core/ (assistant.py), llm/ (generator.py), memory/ (chat_history.py), nlp/ (processing.py), tools/ (weather_tool.py, web_search_tool.py), main.py e .env.</p>
                <p>Detalhes dos Módulos:</p>
                <p>audio/speak.py: Propósito: Comunicação vocal bidirecional (STT e TTS). Funções: ouvir_microfone(), falar(). Dependências: speech_recognition, gTTS, soundfile, sounddevice, os, time. Racional: Robustez na reprodução de áudio e reinício de recursos do microfone.</p>
                <p>conscience/: Propósito: Conhecimento sobre ambiente e recursos. context_manager.py: Gerencia hora e localização (ip-api.com, com cache). persona_manager.py: Define a personalidade "Aurora" para o LLM. usage_tracker.py: Monitora e persiste o uso de APIs externas (ex: Google Search) em JSON para evitar limites.</p>
                <p>core/assistant.py: Propósito: Orquestrador principal. Funções: run(). Dependências: Módulos internos. Racional: Controla o loop de interação, roteia intenções (locais, controladas com limite, delegadas ao LLM).</p>
                <p>llm/generator.py: Propósito: Integração com Google Gemini e gerenciamento de ferramentas. Funções: generate_response(). Dependências: google.generativeai, tools, conscience. Racional: Usa Gemini 1.5-flash-latest para NLP avançado e Function Calling, controlando o uso da busca web.</p>
                <p>memory/chat_history.py: Propósito: Manter histórico da conversa. Funções: add_message(), get_history(). Racional: Essencial para contexto do LLM, limita a 20 mensagens para otimização.</p>
                <p>nlp/processing.py: Propósito: Análise inicial de intenções. Funções: processar_texto(). Racional: Estratégia híbrida (regras para básico, LLM para complexo).</p>
                <p>tools/: Propósito: Encapsular APIs externas. weather_tool.py: Clima via WeatherAPI.com. web_search_tool.py: Pesquisa web via Google Custom Search API. Racional: Estende capacidades do assistente, encapsuladas para Function Calling.</p>
                <p>main.py: Propósito: Ponto de entrada do aplicativo. Dependências: core.assistant. Racional: Inicializa o assistente.</p>
                <p>Configuração Essencial (.env): Arquivo para chaves de API (GEMINI_API_KEY, WEATHERAPI_API_KEY, Google Search_API_KEY, Google Search_CX). Não deve ser versionado. Instruções detalhadas para obtenção de cada chave.</p>
                <p>Fluxo de Execução Detalhado: Exemplo de "Aurora, pesquise para mim o que é computação quântica." Mostra o passo a passo desde a entrada de voz, processamento de intenção, verificação de limite de API, chamada ao LLM, execução da ferramenta de busca, e formulação da resposta final pela IA.</p>
                <p>Padrões de Design e Metodologias: Arquitetura Modular/Camadas (alta coesão, baixo acoplamento), Injeção de Dependência (via Construtor), Estratégia Híbrida de Processamento de Intenções (Regras + LLM), Function Calling (Google Gemini), Gerenciamento de Estado de Conversa (Chat History), Gerenciamento de Recursos Persistente (Usage Tracker), Configuração Externa (dotenv).</p>
                <p>Considerações Finais: A arquitetura do Aurora é robusta e escalável. Futuras melhorias incluem mais ferramentas, hotword e UI sofisticada.</p>
            </div>
        </section>

    </main>

    <footer class="py-8 text-center border-t border-gray-200">
        <p class="text-sm text-gray-500">
            Documentação do Projeto Aurora &copy; 2025. Desenvolvido por <strong>Raphael Olimpio Aparecido Pereira Lima</strong> (Tec. Mecatrônica, Estudante de Eng. de Software) com a assistência de <strong>Gemini IA</strong>.
        </p>
    </footer>

    <script>
        // Fix: Access Chart components directly from the global Chart object
        const { LineController, CategoryScale, LinearScale, PointElement, LineElement, Filler, ArcElement, BarController, BarElement, RadialLinearScale, BubbleController } = Chart;
        Chart.register(
            LineController,
            CategoryScale,
            LinearScale,
            PointElement,
            LineElement,
            Filler,
            ArcElement,
            BarController,
            BarElement,
            RadialLinearScale,
            BubbleController
        );

        const accordionButtons = document.querySelectorAll('.accordion-button');
        accordionButtons.forEach(button => {
            button.addEventListener('click', () => {
                const content = button.nextElementSibling;
                const arrow = button.querySelector('.arrow-icon');
                
                button.setAttribute('aria-expanded', content.style.maxHeight ? 'false' : 'true');

                if (content.style.maxHeight) {
                    content.style.maxHeight = null;
                    content.classList.remove('open');
                    arrow.classList.remove('open');
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                    content.classList.add('open');
                    arrow.classList.add('open');
                }
            });
        });
        
        function processLabels(labels, maxLength = 16) {
            return labels.map(label => {
                if (typeof label === 'string' && label.length > maxLength) {
                    const words = label.split(' ');
                    const newLabel = [];
                    let currentLine = '';
                    words.forEach(word => {
                        if ((currentLine + word).length > maxLength) {
                            newLabel.push(currentLine.trim());
                            currentLine = word + ' ';
                        } else {
                            currentLine += word + ' ';
                        }
                    });
                    if (currentLine.trim()) newLabel.push(currentLine.trim());
                    return newLabel.length > 0 ? newLabel : [label];
                }
                return label;
            });
        }

        const tooltipTitleCallback = (tooltipItems) => {
            const item = tooltipItems[0];
            let label = item.chart.data.labels[item.dataIndex];
            if (Array.isArray(label)) {
                return label.join(' ');
            }
            return label;
        };
        
        const moduleCtx = document.getElementById('moduleComponentsChart').getContext('2d');
        const chartLabels = ['audio/', 'conscience/', 'core/', 'llm/', 'memory/', 'nlp/', 'tools/', 'main.py', '.env'];
        const processedChartLabels = processLabels(chartLabels);

        new Chart(moduleCtx, {
            type: 'bar',
            data: {
                labels: processedChartLabels,
                datasets: [{
                    label: 'Nº de Arquivos Python Principais',
                    data: [1, 3, 1, 1, 1, 1, 2, 1, 1],
                    backgroundColor: '#A0AEC0',
                    borderColor: '#6C757D',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                scales: {
                    x: {
                        beginAtZero: true,
                        ticks: {
                            color: '#495057',
                            stepSize: 1
                        },
                        grid: {
                            color: 'rgba(0,0,0,0.05)'
                        }
                    },
                    y: {
                        ticks: {
                            color: '#495057',
                            font: {
                                size: 11
                            }
                        },
                        grid: {
                            display: false
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            title: function(tooltipItems) {
                                const item = tooltipItems[0];
                                if (Array.isArray(item.label)) {
                                  return item.label.join(' ');
                                }
                                return item.label;
                            }
                        }
                    }
                }
            }
        });

        document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    const navHeight = document.querySelector('nav').offsetHeight;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - navHeight - 20;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: "smooth"
                    });
                }
            });
        });

        // Gemini API integration for Summarize Section
        const summarizeButtons = document.querySelectorAll('.summarize-button');
        summarizeButtons.forEach(button => {
            button.addEventListener('click', async () => {
                const accordionContent = button.closest('.accordion-content');
                const summaryOutput = accordionContent.querySelector('.summary-output');
                const loadingIndicator = accordionContent.querySelector('.loading-indicator');
                
                // Clear previous output and show loading
                summaryOutput.innerHTML = '';
                loadingIndicator.classList.remove('hidden');

                let contentToSummarize = '';
                accordionContent.childNodes.forEach(node => {
                    if (node.nodeType === Node.ELEMENT_NODE && !node.classList.contains('llm-button-group') && !node.classList.contains('summary-output') && !node.classList.contains('loading-indicator')) {
                        contentToSummarize += node.innerText + '\n';
                    } else if (node.nodeType === Node.TEXT_NODE) {
                        contentToSummarize += node.textContent + '\n';
                    }
                });

                const prompt = `Resuma o seguinte texto sobre um módulo ou arquivo do projeto Aurora em português, de forma concisa e clara: ${contentToSummarize.trim()}`;

                let chatHistory = [];
                chatHistory.push({ role: "user", parts: [{ text: prompt }] });
                const payload = { contents: chatHistory };
                const apiKey = "";
                const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

                try {
                    const response = await fetch(apiUrl, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(payload)
                    });
                    const result = await response.json();

                    if (result.candidates && result.candidates.length > 0 &&
                        result.candidates[0].content && result.candidates[0].content.parts &&
                        result.candidates[0].content.parts.length > 0) {
                        const text = result.candidates[0].content.parts[0].text;
                        summaryOutput.innerHTML = `<strong>Resumo da Aurora:</strong> ${text}`;
                    } else {
                        summaryOutput.innerHTML = 'Não foi possível gerar o resumo. Tente novamente.';
                    }
                } catch (error) {
                    console.error('Erro ao chamar a API Gemini para resumo:', error);
                    summaryOutput.innerHTML = 'Erro ao conectar com a IA para gerar o resumo.';
                } finally {
                    loadingIndicator.classList.add('hidden');
                }
            });
        });

        // Gemini API integration for Q&A about the project
        const userQuestionInput = document.getElementById('user-question');
        const askAuroraButton = document.getElementById('ask-aurora-button');
        const chatDisplay = document.getElementById('chat-display');
        const chatLoadingIndicator = document.getElementById('chat-loading-indicator');
        const fullDocText = document.getElementById('full-doc-text').innerText;

        let chatHistory = [{ role: "model", parts: [{ text: "Olá! Sou a Aurora, sua assistente de documentação. Como posso ajudar a explorar o projeto?" }] }];

        askAuroraButton.addEventListener('click', async () => {
            const userMessage = userQuestionInput.value.trim();
            if (!userMessage) return;

            userQuestionInput.value = '';
            displayChatMessage(userMessage, 'user');
            chatLoadingIndicator.classList.remove('hidden');
            chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom

            const prompt = `Você é um assistente de documentação chamado Aurora. Responda à pergunta do usuário APENAS com base no seguinte contexto do projeto Aurora. Se a informação não estiver explicitamente no contexto fornecido, diga educadamente que não pode responder a essa pergunta com base na documentação disponível.
            
            Contexto do Projeto Aurora:
            ${fullDocText}

            Pergunta do Usuário: ${userMessage}`;

            let currentChatHistory = [];
            currentChatHistory.push({ role: "user", parts: [{ text: prompt }] });

            const payload = { contents: currentChatHistory };
            const apiKey = "";
            const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

            try {
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const result = await response.json();

                if (result.candidates && result.candidates.length > 0 &&
                    result.candidates[0].content && result.candidates[0].content.parts &&
                    result.candidates[0].content.parts.length > 0) {
                    const auroraResponse = result.candidates[0].content.parts[0].text;
                    displayChatMessage(auroraResponse, 'aurora');
                } else {
                    displayChatMessage('Desculpe, não consegui processar sua pergunta no momento. Por favor, tente novamente.', 'aurora');
                }
            } catch (error) {
                console.error('Erro ao chamar a API Gemini para Q&A:', error);
                displayChatMessage('Ocorreu um erro ao conectar com a IA. Por favor, verifique sua conexão ou tente mais tarde.', 'aurora');
            } finally {
                chatLoadingIndicator.classList.add('hidden');
                chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom after response
            }
        });

        function displayChatMessage(message, sender) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('chat-message', sender);
            messageDiv.innerText = message;
            chatDisplay.appendChild(messageDiv);
            chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom
        }

    </script>
</body>
</html>

