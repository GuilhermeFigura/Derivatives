"""Um pecuarista possui 100 cabeças de gado magro no pasto, e estima-se que deverá levar seis meses para engordar e vender os bois para o
frigorífico pesando, em média, 25 arrobas cada um deles. Hoje, o valor da arroba de boi à vista está em R$ 240.
Preocupado com o preço da carne no mercado interno, o criador poderia fazer a venda a termo de 2.500 arrobas de boi a um preço de R$ 249 por arroba
ao frigorífico, para o prazo de seis meses. Dessa maneira, o criador poderia garantir o seu lucro e preocupar-se apenas com os problemas relacionados
à criação do gado. Ao final de seis meses, no vencimento da operação a termo, considere dois cenários: no primeiro, a arroba de boi gordo à vista
está cotada a R$ 234 e no segundo R$ 255.
Compare os cenários, qual deverá ser o ganho do pecuarista na operação a termo, isoladamente? Qual a receita e o fluxo de caixa do pecuarista?
O que a operação a termo lhe proporcionou? """

print(f'O programa abaixo irá simular uma NDF na posição vendida, mostrando o ajuste da posição, fluxo de caixa e a receita. '
      f'\nFavor inserir as informações solicitadas.')
#Solicitações de informações
cabeças = int(input(f'Quantas cabeça de gado o agricultor deseja fazer o HEDGE? '))
arroba = int(input(f'Qual a média da arroba dos gados? '))
avista = float(input(f'Qual o valor em R$ da arroba do boi à vista? '))
futuro = float(input(f'Qual o valor em R$ da arroba do boi a termo? '))
cenário = float(input(f'Qual o valor em R$ da arroba no vencimento do termo? '))

#Cálculo da NDF
quantidade = cabeças * arroba
ajuste = (futuro - cenário) * quantidade
receita = (cabeças * cenário)

#Resultado da operação
if ajuste >= 0:
      print(f'O produtor terá um ajuste de R$ {ajuste:.2f} à RECEBER, '
            f'gerando um fluxo de caixa da operação total de R$ {(quantidade * cenário) + ajuste:.2f}')
else:
      print(f'O produtor terá um ajuste de R$ {ajuste:.2f} à PAGAR, '
            f'gerando um fluxo de caixa da operação total de R$ {(quantidade * cenário) + ajuste:.2f}')
