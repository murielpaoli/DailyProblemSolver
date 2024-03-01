def is_palindrome_iterative(word):
    # Se a palavra estiver vazia, retorna False
    if not word:
        return False

    # Inicializa os índices low_index e high_index
    low_index = 0
    high_index = len(word) - 1

    # Enquanto low_index for menor que high_index, verifica se os caracteres
    # nos índices low_index e high_index são iguais
    while low_index < high_index:
        # Se os caracteres não forem iguais, a palavra não é um palíndromo
        if word[low_index] != word[high_index]:
            return False

        # Atualiza os índices low_index e high_index
        low_index += 1
        high_index -= 1

    # Se o loop terminar, a palavra é um palíndromo
    return True
