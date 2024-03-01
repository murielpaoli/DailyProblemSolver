def is_palindrome_recursive(word, low_index, high_index):
    # Se a palavra estiver vazia, retorna False
    if not word:
        return False

    # Se low_index for maior ou igual a high_index, a palavra é um palíndromo
    if low_index >= high_index:
        return True

    # Se o caractere no low_index não for igual ao caractere no high_index,
    # a palavra não é um palíndromo
    if word[low_index] != word[high_index]:
        return False

    # Chama a função recursivamente para os próximos índices
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# Testa a função com a palavra "arara"
print(is_palindrome_recursive("arara", 0, 4))  # Saída esperada: True
