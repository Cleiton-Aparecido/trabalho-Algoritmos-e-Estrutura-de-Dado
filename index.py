import heapq
from collections import defaultdict

class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerdo = None
        self.direito = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

def contagem_de_caracteres(frase):
    frequencias = defaultdict(int)
    for caractere in frase:
        frequencias[caractere] += 1
    return frequencias

def criar_arvore_de_huffman(frequencias):
    fila = [No(caractere, frequencia) for caractere, frequencia in frequencias.items()]
    heapq.heapify(fila)
    while len(fila) > 1:
        no1 = heapq.heappop(fila)
        no2 = heapq.heappop(fila)
        novo_no = No(None, no1.frequencia + no2.frequencia)
        novo_no.esquerdo = no1
        novo_no.direito = no2
        heapq.heappush(fila, novo_no)
    return fila[0]

def codificar_caracteres(raiz):
    codigo = {}
    def percorrer_arvore(no, caminho):
        if no.caractere is not None:
            codigo[no.caractere] = caminho
        else:
            percorrer_arvore(no.esquerdo, caminho + "0")
            percorrer_arvore(no.direito, caminho + "1")
    percorrer_arvore(raiz, "")
    return codigo

if __name__ == "__main__":
    frase = input("Digite a frase: ")
    frequencias = contagem_de_caracteres(frase)
    raiz = criar_arvore_de_huffman(frequencias)
    codigo = codificar_caracteres(raiz)


    print("Árvore de Huffman:", raiz.__dict__),
    print("Tabela de códigos:")
    print("Caracter | Codigo Binário")
    for caractere, codigo in codigo.items():
        print(f"   {caractere}     |    {codigo}")