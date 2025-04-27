from map.map_stats  import MapStats
from map.map_simulation import MapSimulation

class MapHandler:
    """
    Classe responsável por gerenciar o mapa
    """
    def start(self, size_x: int, size_y: int, sprite: str):
        """
        Gera um mapa com tamanho e sprite
        Args:
            size_x(int): Tamanho X do mapa
            size_y(int): Tamanho Y do mapa
            sprite(str): Sprite do mapa, que representará cada célula
        """
        self.map_stats = MapStats()
        self.map_simulation = MapSimulation(size_x= size_x, size_y= size_y, map_stats= self.map_stats)

        self.map_simulation.create_empty_map(key= sprite)

    def get_map_stats(self):
        """
        Retorna a referência ao objeto dos atributos do mapa
        Returns:
            MapStats: Instância atual de MapStats
        """
        return self.map_stats

    def get_map_string_view(self):
        return self.map_simulation.get_map_string()
    
    def add_entity(self, coord_X: int, coord_y: int, sprite: str):
        self.map_simulation.add_entity()


        