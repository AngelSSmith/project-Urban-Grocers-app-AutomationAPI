import configuration
import data
import requests

def post_new_client_kit(kit_body):
    auth_token = post_new_user()
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body, headers=headers)
    return response

def post_new_user():
    user_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                                  json=data.user_body,
                                  headers=data.headers)

    if user_response.status_code == 201:
        return user_response.json().get('authToken')

    else:
        raise Exception(f"Error al crear el usuario: {user_response.json()}")
print(post_new_client_kit(data.kit_body))