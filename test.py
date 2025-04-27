from handler.simulation_handler import SimulationHandler

simulation_handler = SimulationHandler()

simulation_handler.start_map(size_x= 10, size_y= 10, sprite= "X")

print(simulation_handler.map_handler.get_map_string_view()) # remover depois porque ta puxando do map_handler, num pode

basic_entity_1 = simulation_handler.create_entity(entity_type= "basic", coord_x= 0, coord_y= 0, speed= 2, start_delay= 2)

basic_entity_1.move()