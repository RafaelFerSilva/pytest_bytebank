from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Rafael', '12/04/1989', 15000)
    print(f'Rafael = {funcionario_teste.idade()}')


teste_idade()
