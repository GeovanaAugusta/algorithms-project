from pytest import raises

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 7)

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Message", "key not integer")

    assert encrypt_message('Message', -1) == "egasseM"

    assert encrypt_message('Message', 3) == "seM_egas"

    assert encrypt_message('Message', 5) == "asseM_eg"
