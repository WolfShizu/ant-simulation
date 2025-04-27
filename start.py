from map.map_handler import get_map_stats, SimulationMap
from entities.base_entity import genereate_attributes, baseEntity

entity1 = baseEntity(genereate_attributes(
    map_stats= get_map_stats(),
    coord_x= 2,
    coord_y= 2,
    speed= 2,
    start_delay= 0 
))

entity1.move()

entity_map_stat = entity1.attributes["map_stats"] # Acessa a instância da entidade

print(entity_map_stat.current_tick) # acessa a classe do map_stats

simulation_map = SimulationMap(size_x= 10, size_y= 10) # instancia o mapa

simulation_map.create_empty_map() # Cria o mapa dentro do objeto

print(simulation_map.map_array) 

print(simulation_map.get_map_string()) # Mostra o mapa formatado fora da lista

print("==============")

simulation_map.add_entity(entity1)

print(simulation_map.get_map_string())