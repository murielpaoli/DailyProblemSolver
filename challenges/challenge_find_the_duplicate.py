def check_valid_input(lst):
    # a entrada é uma lista e ela contém algum elemento?
    if not isinstance(lst, list) or not lst:
        return False

    # a lista contém apenas strings?
    if all(isinstance(item, str) for item in lst):
        return False

    # a lista contém apenas um elemento?
    if len(lst) == 1:
        return False

    # a lista contém apenas números negativos?
    if all(item < 0 for item in lst):
        return False

    return True


def find_duplicate(lst=None):
    if not check_valid_input(lst):
        return False

    # Encontrando a duplicata após as verificações
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return lst[i]

    # Se nenhum duplicado for encontrado, retorna False
    return False


print(find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))  # Saída esperada:10
print(find_duplicate(['a', 'b', 'a']))  # Saída esperada: False
print(find_duplicate([1]))  # Saída esperada: False
print(find_duplicate([1, 1, 2]))  # Saída esperada: False
