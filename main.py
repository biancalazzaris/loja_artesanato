
tamVetor=10

somaTotal=0
maiorQuantidade=0
posicaoMaiorQuantidade=0

preco = [0]*tamVetor
quantidade = [0]*tamVetor

print("\t*****BEM VINDO AO SISTEMA DE PEDIDO*****\n")

for x in range(tamVetor):
    print(" Digite a quantidade de produto nº",x+1,":")
    quantidade[x]=int(input())
    print(" Digite o preço do produto:")
    preco[x] = float(input());


print("\n""\t *****RELATÓRIO - ORÇAMENTO DO PEDIDO*****\n")
for i in range(tamVetor):
    print(" Produto",i+1, ": Preço:", preco[i],"Quantidade:", quantidade[i],"Soma:",(preco[i]*quantidade[i]))

for y in range(tamVetor):
    soma=preco[y]*quantidade[y]
    somaTotal= somaTotal + soma
print("\n Total da compra deu: R$", somaTotal, " - A sua comissão dessa venda foi de: R$", somaTotal*0.05 )

for n in range(tamVetor):
    if(quantidade[n] > maiorQuantidade):
        maiorQuantidade = quantidade[n]
        posicaoMaiorQuantidade = n
print("\t \n O produto com a maior quantidade vendida foi:", maiorQuantidade)
print(" E a sua posição no vetor é:", posicaoMaiorQuantidade)
        
