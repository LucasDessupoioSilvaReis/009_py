def eh_string_valida(s):
    
    stack = []
    mapeamento = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapeamento.values():
            stack.append(char)
        elif char in mapeamento.keys():
            if not stack or mapeamento[char] != stack.pop():
                return False
        else:
            return False

    return not stack

string_teste1 = "(){}[]"
print("A string '{}' é válida?".format(string_teste1), eh_string_valida(string_teste1))

string_teste2 = "([{}])"
print("A string '{}' é válida?".format(string_teste2), eh_string_valida(string_teste2))

string_teste3 = "({[}])"
print("A string '{}' é válida?".format(string_teste3), eh_string_valida(string_teste3))
