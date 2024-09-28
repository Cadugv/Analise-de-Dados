# neste codigo vamos conseguir ler um arquivo .txt 
# transformar para lista 
# execultar o calculo do faturamento total de uma empresa

with open("vendasloja.txt", "r") as arquivo:# aqui estamos importando o arquivo txt para lelo com "r"
    texto = arquivo.read()
lista_texto = texto.split("\n") # split e pra ordena apos o "\n" virando uma lista 

faturamento = 0 

lista_texto = lista_texto[1:]# excluindo  primeira linha onde não queromos pegar dados vulgo cabeçalho 

for linha in lista_texto:# aqui estou execultando o comando for para cada linha da minha lista 
    posicao_pv = linha.find(";") # ler apos o ";"
    valor = float(linha[posicao_pv + 1 : ])#começa a ler o proximo dado depois do ";"
    faturamento += valor #soma e armazena os valores das linha para dar o faturamento total

print(faturamento)
