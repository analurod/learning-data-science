'''
Exercício - Aula 3.2

Neste nosso script a ideia é fazer a etapa de soma dos preços dos ingredientes. Lendo preços do terminal
'''

# Função aque recebe a referencia de quais ingrdientes temos disponiveis no mercado para compra  retorna o valor final da compra com base nos preçõs dos ingredientes
def soma_ingredientes(tem_cenoura, tem_ovo, tem_oleo, tem_leite, tem_fermento, tem_farinha, tem_acucar):
    total_compra = 0

    if tem_cenoura:
        total_compra += precoCenoura
    if tem_ovo:
        total_compra += precoOvo
    if tem_oleo:
        total_compra += precoOleo
    if tem_leite:
        total_compra += precoLeite
    if tem_farinha:
        total_compra += precoFarinha
    if tem_fermento:
        total_compra += precoFermento
    if tem_acucar:
        total_compra += precoAcucar
    return total_compra


# Preço dos Ingredientes
precoCenoura = float(input("Cenoura: "))
precoOvo = float(input("Ovo: "))
precoOleo = float(input("Oleo: "))
precoLeite = float(input("Leite: "))
precoFermento = float(input("Fermento: "))
precoFarinha = float(input("Farinha: "))
precoAcucar = float(input("Açucar: "))

    
# Verificando total dessa situação
print(f'O total da compra é R$ {soma_ingredientes(True, False, True, True, True, True, True)}')