def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = 10
print(num, "é par?", eh_par(num))

num = 7
print(num, "é par?", eh_par(num))