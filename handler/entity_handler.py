from entities.basic_entity import basicEntity

class EntityHandler:
    def __init__(self):
        self.entity_map = {
            "basic": self.create_basic_entity
        }

    def create_entity(self, entity_type: str, attributes: dict):

        create_entity_function = self.entity_map.get(entity_type)

        if create_entity_function:
            return create_entity_function(attributes)
        else:
            pass
            # Adicionar tratamento de erro

    def create_basic_entity(self, attributes: dict):
        return basicEntity(
            map_stats= attributes["map_stats"],
            coord_x= attributes["coord_x"],
            coord_y= attributes["coord_y"],
            speed= attributes["speed"],
            start_delay= attributes["start_delay"]
            )
