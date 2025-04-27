from handler.map_handler import MapHandler
from handler.entity_handler import EntityHandler

class SimulationHandler():
    def __init__(self):
        self.map_handler = MapHandler()
        self.entity_handler = EntityHandler()

    def start_map(self, size_x, size_y, sprite):
        self.map_handler.start(size_x, size_y, sprite)

    def create_entity(self, entity_type, coord_x, coord_y, speed = 2, start_delay = 1):
        
        attributes = self.entity_handler.create_attributes(
            map_stats= self.map_handler.get_map_stats(),
            coord_x= coord_x,
            coord_y= coord_y,
            speed= speed,
            start_delay= start_delay
        )
        return self.entity_handler.create_entity(entity_type, attributes)
