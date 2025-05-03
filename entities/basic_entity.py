from map.map_stats import MapStats

class basicEntity:
    """
    Classe da entidade básica
    """
    def __init__(self, id: int, map_stats: MapStats, coord_x: int, coord_y: int, speed: int, start_delay: int):
        """
        Inicia a instância com os atributos da entidade
        Args:
            id(int): ID da entidade
            map_stats(MapStats): Referência à instância dos stats do mapa
            coord_x(int): Coordenada X da entidade
            coord_y(int): Coordenada Y da entidade
            spped(int): Ticks entre cada ação da entidade
            start_delay(int): Tick em que a entidade começará a agir
        """
        self.id = id
        self.map_stats = map_stats
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.speed = speed
        self.start_delay = start_delay

    def should_act(self):
        """
        Verifica se a entidade deve ou não se mover no tick atual com base no map_stats
        Returns:
            True: Caso a entidade possa se  mover
            False: Caso a entidade não possa se mover
        """
        speed = self.attributes["speed"]
        start_delay = self.attributes["start_delay"]
        current_tick = self.attributes["map_stats"].current_tick
        
        if current_tick == start_delay or current_tick % speed == 0:
            return True
        return False

    def act(self): # teste
        """
        Gera uma ação para a entidade
        """
        self.move()

    def move(self): # teste
        """
        Move a entidade
        """
        print("moving...")
    
    def _generate_intentions(self):
        pass

    def get_intention(self):
        """
        Retorna os dados da intenção de ação da entidade (ex: mover, atacar)
        Returns:
            dict: Dicionário com os dados da ação
        """
        generated_intention = self._generate_intentions()

        extra_data = generated_intention["extra_data"] # Dados não obrigatórios (ex: dano, cura)

        intention = {
            "id": self.id,
            "source_x": self.coord_x,
            "source_y": self.coord_y,
            "action": generated_intention["action"],
            "target_x": generated_intention["target_x"],
            "target_y": generated_intention["target_y"]
        } 

        intention.update(extra_data)

        return intention