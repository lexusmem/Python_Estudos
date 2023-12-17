import unittest
from unittest import TestCase
from alura_testes_excecoes import LanceInvalido
from alura_testes import Usuarios, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):

        self.alex = Usuarios('Alex', 500.00)
        self.laura = Usuarios('Laura', 500.00)

        self.lance_alex = Lance(self.alex, 100.00)
        self.lance_laura = Lance(self.laura, 150.00)

        self.leilao = Leilao('Celular')

    def test_nao_deve_permitir_propor_lance_em_ordem_decrecente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_laura)
            self.leilao.propoe(self.lance_alex)

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
        pamela = Usuarios('Pamela', 500.00)

        lance_pamela = Lance(pamela, 250.00)

        self.leilao.propoe(self.lance_alex)
        self.leilao.propoe(self.lance_laura)
        self.leilao.propoe(lance_pamela)

        maior_valor_esperado = 250.00
        menor_valor_esperado = 100.00

        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

    # Se não tiver lance deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_leilao_nao_possuir_lance(self):
        self.leilao.propoe(self.lance_alex)

        qtd_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, qtd_lances_recebidos)

    # Se o último usuário for diferente deve permitir propor lance
    def test_se_ultimo_usuario_for_diferente_permitir_propor_lance_(self):
        camila = Usuarios('Camila', 500.00)
        lance_camila = Lance(camila, 1500.00)

        self.leilao.propoe(self.lance_alex)
        self.leilao.propoe(lance_camila)

        qtd_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, qtd_lances_recebidos)

    # Se o último usuário for o mesmo, não deve permitir propor lance.
    def test_se_ultimo_usuario_for_o_mesmo_não_permitir_propor_lance(self):
        lance_alex_2 = Lance(self.alex, 2345.00)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_alex)
            self.leilao.propoe(lance_alex_2)


if __name__ == '__main__':
    unittest.main()
