class basicEntity:
    """
    Classe base para outras entidades com comandos básicos
    """
    def __init__(self, map_stats, coord_x, coord_y, speed, start_delay):
        """
        Inicia a instância com as configurações básicas da entidade
        Args:
            attributes(dict): Contém os atributos básicos da entidade (gerados na função genereate_attributes)
        """
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