from entities.basic_entity import basicEntity

class EntityHandler:
    """
    Classe responsável por gerenciar as entidades
    """
    def __init__(self):
        """
        Inicia a instância, gerando um dicionário das funções para criar as entidades
        """
        self.entities_type = { # Usando para saber qual entidade deve ser criada, usando a função correspondente
            "basic": self.create_basic_entity
        }

        self.entities_list = []

    def create_entity(self, entity_type: str, attributes: dict):
        """
        Cria uma entidade do tipo escolhido
        Args:
            entity_type(str): Tipo da entidade (ex: "basic", "tank")
            attributes(dict): Dicionário com os atributos da entidade
        """
        create_entity_function = self.entities_type.get(entity_type) # Pega a função da entidade escolhida

        if create_entity_function:
            entity = create_entity_function(attributes)
            self.entities_list.append(entity)
            return  entity
        else:
            pass
            # Adicionar tratamento de erro

    def create_basic_entity(self, attributes: dict):
        """
        Função para criar a entidade do tipo básico
        Args:
            attributes(dict): Atributos da entidade
        """
        return basicEntity(
            map_stats= attributes["map_stats"],
            coord_x= attributes["coord_x"],
            coord_y= attributes["coord_y"],
            speed= attributes["speed"],
            start_delay= attributes["start_delay"]
            )
