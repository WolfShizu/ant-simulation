import numpy as np

class MapSimulation:
    """
    Classe do mapa da simulação
    """
    def __init__(self,  size_x, size_y, map_stats):    
        """
        Inicia a instância com as configurações básicas do mapa
        Args:
            size_x(int): Quantidade de linhas do mapa
            size_y(int): Quantidade de colunas do mapa
        """
        self.stats = map_stats
        self.size_x = size_x
        self.size_y = size_y
        self.map_array = None

    def create_empty_map(self, key = "X"):
        """
        Cria um mapa vazio e guarda no map_array
        Args:
            key(str): Define o que será cada espaço do mapa
        """
        new_map = np.full(shape= (self.size_x, self.size_y), fill_value= key)
        self.map_array = new_map

    def get_map_string(self):
        """
        Retorna o mapa em formato de string
        Returns:
            str: Mapa em string
        """
        lines_list = [] # Segunda lista com as linhas em string

        for line in self.map_array:
            string_line = " ".join(line) # Transforma cada lista dentro da lista do mapa em uma string
            lines_list.append(string_line) # Adiciona essa string à segunda lista

        map_string = "\n".join(lines_list) # Passando a segunda lista para a string final

        return map_string
    
    def add_entity(self, entity):
        self.map_array[entity.attributes["coord_x"], entity.attributes["coord_y"]] = "O"
