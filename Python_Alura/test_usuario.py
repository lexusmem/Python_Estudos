from alura_testes_excecoes import LanceInvalido
from alura_testes import Leilao, Usuarios
import pytest


@pytest.fixture
def alex():
    return Usuarios('Alex', 100.00)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propor_lance(alex, leilao):

    alex.propoe_lance(leilao, 50.00)

    assert alex.carteira == 50.00


def test_permitir_propor_lance_quando_valor_menor_que_o_valor_da_carteira(alex, leilao):

    alex.propoe_lance(leilao, 1.00)

    assert alex.carteira == 99


def test_permitir_propor_lance_quando_valor_igual_ao_valor_da_carteira(alex, leilao):

    alex.propoe_lance(leilao, 100.00)

    assert alex.carteira == 0.00


def test_nao_permitir_propor_lance_quando_valor_maior_ao_valor_da_carteira(alex, leilao):

    with pytest.raises(LanceInvalido):
        alex.propoe_lance(leilao, 200.00)
