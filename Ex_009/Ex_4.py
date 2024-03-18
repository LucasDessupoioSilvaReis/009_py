def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = 70  
altura = 1.75  

imc = calcular_imc(peso, altura)
print("O Índice de Massa Corporal (IMC) é:", imc)