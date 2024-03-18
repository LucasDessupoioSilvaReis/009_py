def contar_letra(string, letra):

    contador = 0
    for char in string:
        if char == letra:
            contador += 1
    return contador

texto = "Esta é uma string de exemplo."
letra = "a"

ocorrencias = contar_letra(texto, letra)
print(f"A letra '{letra}' aparece {ocorrencias} vezes na string.")