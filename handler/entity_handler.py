from entities.basic_entity import basicEntity

class EntityHandler:
    """
    Classe responsável por gerenciar as entidades
    """
    def __init__(self):
        """
        Inicia a instância, gerando um dicionário das funções para criar as entidades
        """

        self.id_counter = 0

        self.entities_type = { # Usando para saber qual entidade deve ser criada, usando a função correspondente
            "basic": self.create_basic_entity
        }

        self.entities_map = {}

    def _new_id(self):
        """
        Gera um novo ID único
        """
        self.id_counter += 1
        return self.id_counter

    def _register_entity(self, entity):
        """
        Adiciona a entidade ao mapa de entidades, junto de seu ID
        Args:
            entity(basic_entity): Qualquer entidade que herde do basic_entity
        """
        self.entities_map[entity.id] = entity

    def get_intentions(self):
        """
        Gera uma lista com as intenções das entidades
        """
        pass
    
    def recalculate_intentions(self, intentions):
        """
        Recalcula a intenção das entidades
        """
        pass

    def create_entity(self, entity_type: str, attributes: dict):
        """
        Cria uma entidade do tipo escolhido
        Args:
            entity_type(str): Tipo da entidade (ex: "basic", "tank")
            attributes(dict): Dicionário com os atributos da entidade
        """
        create_entity_function = self.entities_type.get(entity_type) # Pega a função da entidade escolhida

        if create_entity_function:
            entity = create_entity_function(self._new_id, attributes)
            self._register_entity(entity)
            return entity
        else:
            pass
            # Adicionar tratamento de erro

    def create_basic_entity(self, id: int, attributes: dict):
        """
        Função para criar a entidade do tipo básico
        Args:
        id(int): ID da entidade
            attributes(dict): Atributos da entidade
        """
        entity = basicEntity(
            id= id,
            map_stats= attributes["map_stats"],
            coord_x= attributes["coord_x"],
            coord_y= attributes["coord_y"],
            speed= attributes["speed"],
            start_delay= attributes["start_delay"]
            )

        return entity
