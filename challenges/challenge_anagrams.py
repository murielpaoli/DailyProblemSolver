def merge_sort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left = merge_sort(s[:mid])
    right = merge_sort(s[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def is_anagram(first_string, second_string):
    # Se alguma das strings estiver vazia, retorna False
    if not first_string or not second_string:
        return (''.join(merge_sort(list(first_string.lower()))),
                ''.join(merge_sort(list(second_string.lower()))),
                False)

    # Converte as strings para minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Ordena as strings
    ordered_first_string = ''.join(merge_sort(list(first_string)))
    ordered_second_string = ''.join(merge_sort(list(second_string)))

    # Verifica se as strings ordenadas são iguais
    are_anagrams = ordered_first_string == ordered_second_string

    return (ordered_first_string, ordered_second_string, are_anagrams)
