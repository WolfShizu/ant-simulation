from map.map_handler import get_map_stats
from entities.base_entity import genereate_attributes, baseEntity

entity1 = baseEntity(genereate_attributes(
    map_stats= get_map_stats(),
    coord_x= 0,
    coord_y= 0,
    speed= 2,
    start_delay= 0 
))

entity1.move()

entity_map_stat = entity1.attributes["map_stats"] # Acessa a classe da entidade

print(entity_map_stat.current_tick) # acessa a classe do map_stats

entity_map_stat.current_tick = 2

print(entity_map_stat.current_tick)