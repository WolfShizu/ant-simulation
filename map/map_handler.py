from map.map_stats import MapStats
map_stats = MapStats() # Cria o objeto que guarda os atributos do mapa

def get_map_stats():
    """
    Retorna a referência ao objeto dos atributos do mapa
    Returns:
        MapStats: Instância atual de MapStats
    """
    return map_stats