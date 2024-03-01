import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Testa se uma exceção quando os tipos de entrada são inválidos
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 2)

    # Testa se a função divide a mensagem no índice da chave,
    # inverte os caracteres de cada parte e retorna a união das partes
    # com "_" entre elas quando a chave é ímpar
    assert encrypt_message('message', 3) == 'sem_egas'

    # Testa se a função divide a mensagem no índice da chave,
    # inverte os caracteres de cada parte e retorna a união das partes
    # com "_" entre elas quando a chave é par
    assert encrypt_message('message', 2) == 'egass_em'

    # Testa se retorna a mensagem invertida quando a chave é um índice inválido
    assert encrypt_message('eldenring', 10) == 'gnirnedle'
