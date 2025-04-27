from handler.map_handler import MapHandler
from handler.entity_handler import EntityHandler

class SimulationHandler():
    """
    Classe responsável por gerenciar a simulação
    """
    def __init__(self):
        """
        Inicia a instância, gerando os handlers que serão usados
        """
        self.map_handler = MapHandler()
        self.entity_handler = EntityHandler()

    def start_map(self, size_x, size_y, sprite):
        """
        Inicia o mapa
        Args:
            size_x(int): Tamanho X do mapa
            size_y(int): Tamanho Y do mapa
            sprite(str): Sprite para cada célula do mapa
        """
        self.map_handler.start(size_x, size_y, sprite)

    def create_entity(self, entity_type, coord_x, coord_y, speed = 2, start_delay = 1):
        """
        Cria uma nova entidade
        Args:
            entity_type(str): Nome do tipo da entidade
            coord_x(int): Coordenada X da entidade
            coord_y(int): Coordenada Y da entidade
            speed(int): Número de ticks entre cada ação
            start_delay(int): Tick de início da entidade
        """
        
        attributes = self.entity_handler.create_attributes( # Gera um dicionário dos atributos
            map_stats= self.map_handler.get_map_stats(),
            coord_x= coord_x,
            coord_y= coord_y,
            speed= speed,
            start_delay= start_delay
        )
        return self.entity_handler.create_entity(entity_type, attributes)
