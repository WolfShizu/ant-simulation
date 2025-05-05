# 🧠 Sistema de Simulação de Entidades
A proposta deste projeto é desenvolver um simulador de entidades complexas, capazes de executar tarefas variadas, como coletar recursos, explorar o mapa e atacar outras entidades. Haverá diferentes tipos de entidades e, futuramente, pretende-se implementar entidades do tipo "rainhas", como em colônias de formigas.
As decisões das entidades serão geradas por algoritmos de Machine Learning.

# 🛠️ Funcionalidades
- Criação de entidades com atributos personalizados
- Estrutura para implementação de ações com verificação de validade
- Sistema de simulação por ciclos (ticks)
- Estrutura modular com múltiplos _handlers_:
    - ``simulation_handler``: controle geral da simulação
    - ``entity_handler``: gerenciamento de entidades
    - ``map_handler``: cotrole do ambiente
- Estrutura inicial para implementação de Machine Learning

# 🗺️ RoadMap de Funcionalidades
- Sistema de combate
- Sistema de coleta de recursos
- Comportamento baseado em Machine Learning
- Logs e métricas de comportamento das entidades
- Sistema de construção
- Tipos distintos de entidades com novos comportamentos (explorador, coletor, construtor)

# 📂 Estrutura do projeto
```
📦ant-simulation
 ┣ 📂entities # Tipos de entidades
 ┃ ┗ 📜basic_entity.py 
 ┣ 📂handler
 ┃ ┣ 📜entity_handler.py # Controla as entidades
 ┃ ┣ 📜map_handler.py # Controla o mapa
 ┃ ┗📜simulation_handler.py # Controla a simulação
 ┣ 📂map 
 ┃ ┣ 📜map_simulation.py # Gera o mapa com as entidades no terminal
 ┃ ┗ 📜map_stats.py # Dados do mapa 
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┣ 📜start.py 
 ┗ 📜test.py 
 ```