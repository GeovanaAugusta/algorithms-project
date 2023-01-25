from pytest import raises

from challenges.challenge_encrypt_message import encrypt_message

# message = string
# key = int


def test_encrypt_message():

    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 7)

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Message", "key not integer")

    assert encrypt_message('Message', -1) == "egasseM"

    assert encrypt_message('Message', 3) == "seM_egas"

    assert encrypt_message('Message', 5) == "asseM_eg"

# SOURCE
# 2
# https://github.com/pytest-dev/pytest/issues/7489
# https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/290e715d-73e3-4b2d-a3c7-4fe113474070/section/b436f9e0-dfde-4a16-9bad-82f0c559dd45/day/c37f7952-fcf3-49cc-8b4a-4ccb8e06e2ad/lesson/0456b0bb-e9df-4a8b-8b03-1689bb2b6bac/solution

# import pytest

# def test_function():
#     with pytest.raises(TypeError, match="tipo inválido para message"):
#         function_under_test(4)
