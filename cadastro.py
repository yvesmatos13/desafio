class Cadastro():
    def clientes():
        codigo = 1
        clientes = []
        while codigo != 0:
            codigo = int(input("código: "))
            if codigo == 0:
                break
            altura = float(input("altura: "))
            peso = float(input("peso: "))
            cliente = {'codigo':codigo, 'altura':peso, 'peso':altura}
            clientes.append(cliente)

        return clientes