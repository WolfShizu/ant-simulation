from map.map_stats import MapStats

def genereate_attributes(map_stats: MapStats, coord_x, coord_y, speed = 2, start_delay = 1):
    """
    Gera os atributos básicos da entidade
    Args:
        map_stats (MapStats): Objeto com as informações do mapa.
        coord_x (int): Coordenada do eixo X.
        coord_y (int): Coordenada do eixo Y.
        speed (int): Número de ticks entre ações.
        start_delay (int): Tick em que a entidade deve começar a agir
    Returns:
        dict:
            - "map_stats" (MapStats): Objeto com as informações do mapa
            - "coord_x" (int): Coordenada do eixo X
            - "coord_y" (int): Coordenada do eixo Y
            - "speed" (int): Número de ticks entre ações
            - "start_delay" (int): Tick em que a entidade deve começar a agir
    """
    return {
        "map_stats": map_stats,
        "coord_x": coord_x,
        "coord_y": coord_y,
        "speed": speed,
        "start_delay": start_delay
    }

class baseEntity:
    """
    Classe base para outras entidades com comandos básicos
    """
    def __init__(self, attributes):
        """
        Inicia a instância com as configurações básicas da entidade
        Args:
            attributes(dict): Contém os atributos básicos da entidade (gerados na função genereate_attributes)
        """
        self.attributes = attributes

    def get_attribute(self, key):
        """
        Retorna um atributo da entidade
        Args:
            key (string): Atributo a ser recuperado
        Returns:
            Valor do atributo
        """
        return self.attributes[key]

    def should_act(self):
        """
        Verifica se a entidade deve ou não se mover no tick atual com base no map_stats
        Returns:
            True: Caso a entidade possa se  mover
            False: Caso a entidade não possa se mover
        """
        speed = self.get_attribute("speed")
        start_delay = self.get_attribute("start_delay")
        map_stats = self.get_attribute("map_stats")
        current_tick = map_stats.current_tick
        
        if current_tick == start_delay or current_tick % speed == 0:
            return True
        return False

    def act(self):
        """
        Gera uma ação para a entidade
        """
        self.move()

    def move(self):
        """
        Move a entidade
        """
        print("moving...")