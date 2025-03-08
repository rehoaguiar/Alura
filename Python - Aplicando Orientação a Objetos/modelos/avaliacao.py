class Avaliacao:
    def __init__(self, cliente, nota):
        ''' 
        Inicializa  uma instância de Avaliação
        
        Parâmetros;
        - cliente (str): O nome do cliente do restaurante
        - nota (str): A nota dada ao restaurante pelo cliente
        '''
        
        self._cliente = cliente
        self._nota = nota