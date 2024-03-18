from collections import defaultdict

def agrupar_anagramas(lista_palavras):
    
    anagramas = defaultdict(list)
    
    for palavra in lista_palavras:
        anagramas[''.join(sorted(palavra))].append(palavra)
    
    lista_anagramas = list(anagramas.values())
    
    return lista_anagramas

lista_palavras = ["listen", "silent", "hello", "world", "elbow", "below", "car", "arc"]
anagramas_agrupados = agrupar_anagramas(lista_palavras)
print("Agrupamento de anagramas:", anagramas_agrupados)