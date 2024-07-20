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
