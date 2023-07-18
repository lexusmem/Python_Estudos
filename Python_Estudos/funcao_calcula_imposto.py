# Função de calcular imposto
def calcular_imposto_1(preco, taxa):
    imposto = preco * taxa
    return imposto


"""
Condicional para ser executado o teste da função apenas neste arquivo
foi criado a condição
"""
if __name__ == "__main__":
    print(calcular_imposto_1(1500, 0.2))
    print("Alex - Impressão do Teste")
