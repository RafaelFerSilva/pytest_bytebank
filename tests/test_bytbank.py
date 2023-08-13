from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given - Contexto
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When - Ação
        assert resultado == esperado  # Then - Desfecho

    def test_quando_sobrenome_recebe_Rafael_Silva_deve_retornar_Silva(self):
        entrada = ' Rafael Silva '
        esperado = 'Silva'

        funcionario_teste = Funcionario(entrada, '12/04/1989', 1111)
        resultado = funcionario_teste.sobrenome()
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_salario_100000_deve_retornar_90000(self):
        entrada = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2023', entrada)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        assert resultado == esperado


