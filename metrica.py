class Metrica():
    
    def maisAlto(clientes):
        retorno = {'codigo': 0, 'altura': 0, 'peso': 0}
        for cliente in clientes:
            if cliente['altura'] > retorno['altura']:
                retorno = cliente
        return retorno

    def maisBaixo(clientes):
        retorno = clientes[0]
        for cliente in clientes:
            if cliente['altura'] < retorno['altura']:
                retorno = cliente
        return retorno

    def maisMagro(clientes):
        retorno = clientes[0]
        for cliente in clientes:
            if cliente['peso'] < retorno['peso']:
                retorno = cliente
        return retorno

    def maisGordo(clientes):
        retorno = {'codigo': 0, 'altura': 0, 'peso': 0}
        for cliente in clientes:
            if cliente['peso'] > retorno['peso']:
                retorno = cliente
        return retorno
