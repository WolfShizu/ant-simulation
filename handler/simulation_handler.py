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

    def create_entity(
        self,
        entity_type: str,
        coord_x: int,
        coord_y: int,
        speed: int = 2,
        start_delay: int = 1,
        attack_damage: int | None = None
    ):
        """
        Cria uma nova entidade
        Args:
            entity_type(str): Nome do tipo da entidade
            coord_x(int): Coordenada X da entidade
            coord_y(int): Coordenada Y da entidade
            speed(int): Número de ticks entre cada ação
            start_delay(int): Tick de início da entidade
            attack_damage(int): Dano de ataque da entidade
        """
        
        attributes = {
            "entity_type": entity_type,
            "coord_x": coord_x,
            "coord_y": coord_y,
            "speed": speed,
            "start_delay": start_delay,
            "attack_damage": attack_damage
        }

        return self.entity_handler.create_entity(entity_type, attributes)
