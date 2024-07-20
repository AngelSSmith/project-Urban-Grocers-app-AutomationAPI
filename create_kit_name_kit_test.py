import pytest
import data
import sender_stand_request
import configuration
import requests

@pytest.fixture
def post_new_user():
    user_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                                  json=data.user_body,
                                  headers=data.headers)

    if user_response.status_code == 201:
        return user_response.json().get('authtoken')

    else:
        raise Exception(f"Error al crear el usuario: {user_response.json()}")


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400


#Prueba n.1 el parametro name del kit_body cuenta con 1 caracter(es)

def test_create_new_user_kit_1_letter_in_kit_body():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

#Prueba n.2 el parametro name del kit_body cuenta con 511 caracter(es)
def test_create_new_user_kit_511_letters_in_kit_body():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

#Prueba n.3 el parametro name del kit_body cuenta con 0 caracter(es)
def test_create_new_user_kit_0_letters_in_kit_body():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

#Prueba n.4 el parametro name del kit_body cuenta con 512 caracter(es)
def test_create_new_user_kit_512_letters_in_kit_body():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

#Prueba n.5 el parametro name del kit_body cuenta con caracter(es) especial(es)
def test_create_new_user_kit_special_characters_in_kit_body():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

#Prueba n.6 el parametro name del kit_body cuenta con espacios entre caracter(es)
def test_create_new_user_kit_with_spaces_in_kit_body():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

#Prueba n.7 el parametro name del kit_body cuenta con numeros como caracter(es)
def test_create_new_user_kit_with_string_numbers_in_kit_body():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

#Prueba n.8 el parametro name del kit_body no cuenta con datos en el cuerpo
def test_create_new_user_kit_with_no_parameters_in_kit_body():
    kit_body = {}
    negative_assert_code_400(kit_body)

#Prueba n.9 el parametro name del kit_body cuenta con numeros como caracteres
def test_create_new_user_kit_with_numbers_in_kit_body():
    kit_body = get_kit_body(123)  # Enviamos un número en lugar de una cadena
    negative_assert_code_400(kit_body)