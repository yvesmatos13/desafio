from cadastro import Cadastro
from metrica import Metrica
def main():

    clientes = Cadastro.clientes()
    maisAlto = Metrica.maisAlto(clientes)
    maisBaixo = Metrica.maisBaixo(clientes)
    maisGordo = Metrica.maisGordo(clientes)
    maisMagro = Metrica.maisMagro(clientes)
    print('\n######## Cliente Mais Alto #########')
    print('\ncodigo: ', maisAlto['codigo'],
              '\naltura: ', maisAlto['altura'],
              '\npeso: ', maisAlto['peso'])

    print('\n######## Cliente Mais Baixo #########')

    print('\ncodigo: ', maisBaixo['codigo'],
              '\naltura: ', maisBaixo['altura'],
              '\npeso: ', maisBaixo['peso'])

    print('\n######## Cliente Mais Gordo #########')

    print('\ncodigo: ', maisGordo['codigo'],
              '\naltura: ', maisGordo['altura'],
              '\npeso: ', maisGordo['peso'])

    print('\n######## Cliente Mais Magro #########')

    print('\ncodigo: ', maisMagro['codigo'],
              '\naltura: ', maisMagro['altura'],
              '\npeso: ', maisMagro['peso'])

    print('\n######## Clientes #########')
    for cliente in clientes:
        print('\n\n######## Cliente ', cliente['codigo'],' #########')
        print('\ncodigo: ', cliente['codigo'],
              '\naltura: ', cliente['altura'],
              '\npeso: ', cliente['peso'])

main()