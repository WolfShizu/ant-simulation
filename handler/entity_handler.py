from entities.basic_entity import basicEntity

class EntityHandler:
    def create_attributes(self, map_stats, coord_x, coord_y, speed = 2, start_delay = 1):
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

    def __init__(self):
        self.entity_map = {
            "basic": self.create_basic_entity
        }

    def create_entity(self, entity_type, attributes):

        create_entity_function = self.entity_map.get(entity_type)

        if create_entity_function:
            return create_entity_function(attributes= attributes)
        else:
            pass
            # Adicionar tratamento de erro

    def create_basic_entity(self, attributes):
        return basicEntity(
            map_stats= attributes["map_stats"],
            coord_x= attributes["coord_x"],
            coord_y= attributes["coord_y"],
            speed= attributes["speed"],
            start_delay= attributes["start_delay"]
            )
