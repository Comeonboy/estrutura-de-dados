
def maxmin(seq):
    if len(seq)==0:
        return maior, menor
    if len(seq)==1:
        return seq[0], seq[0]
    maior, menor = maioremenor((len(seq)-1), seq)
    return maior, menor;

def maioremenor(tamanho, seq):
    if tamanho != 0:
        maior, menor = maioremenor(tamanho-1, seq)
    else:
        maior = seq[0]
        menor = seq[0]
        
    if seq[tamanho] > maior:
        maior = seq[tamanho]
    if seq[tamanho] < menor:
        menor = seq[tamanho]

    return maior, menor;

    
