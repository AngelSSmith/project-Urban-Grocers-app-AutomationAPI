# Proyecto Urban Grocers 
# El presente proyecto cuenta con una serie de funciones que permiten realizar pruebas automatizadas en una API para comprobar el parametro "name" al crear un kit dentro de un usuario.

# En el archivo "configuation.py" se agregaron todas las direcciones URL que conectan con el servidor.
# En el archivo "data.py" se encuentran el formato en el cual se espera la respuesta de la creacion del usuario junto con la informacion que sera requerida para la creacion del usuario y del kit.
# En el archivo "sender_stand_request.py" contiene las siguientes funciones: Una que permite crear un usuario y almacenar un autoToken de respuesta necesario para crear un kit dentro de este usuario y la funcion que crea el kit dentro del usuario.
# En el archivo "create_kit_name_kit_test.py" Se pueden encontrar funciones que: copian datos de kit body del archivo "data.py" y lo modifican sin alterar el archivo original, dos funciones que permiten crear kits dentro de los usuarios y confirmen si la plataforma los creo o no segun la documentacion de la API y contiene 9 funciones que prueban todos los casos de prueba de interes para el parametro "name".

# La funcion "post_new_user" crea un usuario en la base de datos y almacena como respuesta un auth_token necesario para la creacion de un kit dentro del usuario como especifica la documentacion de la APi.
# La funcion "post_new_client_kit" crea un kit de productos en la direccion "KITS_PATH" utilizando el auth_token generado por la funcion "post_new_user"
# La funcion "get_kit_body" copia el contenido de la variable "kit_body" y prepara el parametro "name" para modificarlo.
# La funcion "positive_assert" llama la variable "kit_body" y a la funcion "post_new_client_kit" para crear un kit con un usuario y confirma que al crearse el kit con las condiciones dadas confirme que se creo con exito.
# La funcion "negative_assert_code_400" llama la variable "kit_body" y a la funcion "post_new_client_kit" para crear un kit con un usuario y confirma que al correr la funcion el kit con las condiciones dadas confirme que el proceso fallo.

# La funcion "possitive_assert" comprueba que el status de la prueba arroje el codigo 201, simultaneamente comprueba que el campo "name" coincida con el valor utilizado en la prueba.
# La funcion "negative_assert_code_400" comprueba que el codigo de la prueba arroje error 400 al ingresar los datos.

# El flujo de trabajo es el siguiente:
# a) Para una prueba positiva en donde el nombre del kit es "a" (como en la primer prueba realizada) la funcion "post_new_user" del archivo "sender_stand_request.py" crea un usuario y permite almacenar en la variable response el "authToken" requerido para crear un kit (segun la documentacion),
# la funcion "post_new_client_kit" del archivo "sender_stand_request.py" crea un kit dentro del usuario con el "authToken" recibido como respuesta de la funcion "post_new_user", ambas funciones recopilan informacion del archivo "data.py" y las direcciones URL del archivo "configuration.py" del presente proyecto.
# La funcion "get_kit_body" del archivo "create_kit_name_kit_test.py" permite copiar la informacion del "kit_body" presente en el archivo "data.py" sin modificar la informacion original de ese archivo y posteriormente modificar el parametro "name".
# La funcion "positive_assert" del archivo "create_kit_name_kit_test.py" recicla la funcion "post_new_client_kit" del archivo "sender_stand_request.py" y confirma que el codigo al crear el nuevo kit dentro del usuario arroje el status de respuesta 201, simultaneamente comprueba que el campo "name" coincida con el valor utilizado en la prueba para este ejemplo "a".
# La funcion "test_create_new_user_kit_1_letter_in_kit_body" del archivo "create_kit_name_kit_test.py" llama a la funcion "positive_assert" y a la funcion "get_kit_body" con el valor "a" en el parametro "name".

# b) Para una prueba negativa en donde el nombre del kit es "" (como en la tercer prueba realizada) la funcion "post_new_user" del archivo "sender_stand_request.py" crea un usuario y permite almacenar en la variable response el "authToken" requerido para crear un kit (segun la documentacion),
# la funcion "post_new_client_kit" del archivo "sender_stand_request.py" crea un kit dentro del usuario con el "authToken" recibido como respuesta de la funcion "post_new_user", ambas funciones recopilan informacion del archivo "data.py" y las direcciones URL del archivo "configuration.py" del presente proyecto.
# La funcion "get_kit_body" del archivo "create_kit_name_kit_test.py" permite copiar la informacion del "kit_body" presente en el archivo "data.py" sin modificar la informacion original de ese archivo y posteriormente modificar el parametro "name".
# La funcion "negative_assert_code_400" del archivo "create_kit_name_kit_test.py" recicla la funcion "post_new_client_kit" del archivo "sender_stand_request.py" y confirma que el codigo al crear el nuevo kit dentro del usuario arroje el status de respuesta 400, confirmando un error al ingresar el parametro "name".
# La funcion "test_create_new_user_kit_0_letters_in_kit_body" del archivo "create_kit_name_kit_test.py" llama a la funcion "negative_assert_code_400" y a la funcion "get_kit_body" con el valor "" en el parametro "name".