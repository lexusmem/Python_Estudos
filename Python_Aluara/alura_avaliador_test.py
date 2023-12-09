import unittest
from unittest import TestCase
from alura_testes import Lance, Leilao, Usuarios


class TestAvaliador(TestCase):

    def setUp(self):

        self.alex = Usuarios('Alex')
        self.laura = Usuarios('Laura')

        self.lance_alex = Lance(self.alex, 100.00)
        self.lance_laura = Lance(self.laura, 150.00)

        self.leilao = Leilao('Celular')

    def test_maior_e_menor_valor_de_lance_quando_adicionados_em_ordem_crescente(self):

        self.leilao.propoe(self.lance_laura)
        self.leilao.propoe(self.lance_alex)

        menor_valor_esperado = 100.00
        maior_valor_esperado = 150.00

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_maior_e_menor_valor_de_lance_quando_adicionados_em_ordem_decrescente(self):

        self.leilao.propoe(self.lance_alex)
        self.leilao.propoe(self.lance_laura)

        maior_valor_esperado = 150.00
        menor_valor_esperado = 100.00

        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

    def test_deve_retornar_o_mesmo_valor_para_menor_e_maior_lance_quando_existir_um_unico_lance(self):

        self.leilao.propoe(self.lance_laura)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_maior_e_menor_valor_de_mais_dois_lance(self):
        pamela = Usuarios('Pamela')

        lance_pamela = Lance(pamela, 250.00)

        self.leilao.propoe(self.lance_alex)
        self.leilao.propoe(self.lance_laura)
        self.leilao.propoe(lance_pamela)

        maior_valor_esperado = 250.00
        menor_valor_esperado = 100.00

        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)


if __name__ == '__main__':
    unittest.main()
