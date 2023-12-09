import unittest
from unittest import TestCase
from alura_testes import Avaliador, Lance, Leilao, Usuarios


class TestAvaliador(TestCase):

    def setUp(self):

        self.alex = Usuarios('Alex')
        self.laura = Usuarios('Laura')

        self.lance_alex = Lance(self.alex, 100.00)
        self.lance_laura = Lance(self.laura, 150.00)

        self.leilao = Leilao('Celular')

    def test_maior_e_menor_valor_de_lance_quando_adicionados_em_ordem_crescente(self):

        self.leilao.lances.append(self.lance_laura)
        self.leilao.lances.append(self.lance_alex)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_maior_e_menor_valor_de_lance_quando_adicionados_em_ordem_decrescente(self):

        self.leilao.lances.append(self.lance_alex)
        self.leilao.lances.append(self.lance_laura)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        maior_valor_esperado = 150.00
        menor_valor_esperado = 100.00

        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)

    def test_deve_retornar_o_mesmo_valor_para_menor_e_maior_lance_quando_existir_um_unico_lance(self):

        self.leilao.lances.append(self.lance_laura)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150, avaliador.menor_lance)
        self.assertEqual(150, avaliador.maior_lance)

    def test_maior_e_menor_valor_de_mais_dois_lance(self):
        pamela = Usuarios('Pamela')

        lance_pamela = Lance(pamela, 250.00)

        self.leilao.lances.append(self.lance_alex)
        self.leilao.lances.append(self.lance_laura)
        self.leilao.lances.append(lance_pamela)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        maior_valor_esperado = 250.00
        menor_valor_esperado = 100.00

        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)


if __name__ == '__main__':
    unittest.main()
