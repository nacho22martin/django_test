django_test
===========

DESCRIPCIÓN APP
===========


Este repositorio contiene los archivos necesarios para la realizacion del test sobre django.

Una vez realizada la clonacion del repositorio y habiendo instalado django, se podrán correr los commandos para iniciar la aplicacion:

1. python manage.py syncdb

Esto creará la base de datos en etapa de development (sqlite3) y le solicitará la creacion de un usuario administrador.

2. python manage.py runserver

Esto arranca el servidor para responder peticiones en el puerto 8000 es decir desde la estacion donde corre se podra acceder al servidor de la siguienter forma:

Interfaz Admin:
http://localhost:8000/admin

Interfaz Publica:
http://localhost:8000/vehiculo

Debemos cargar un vehiculo como minimo para poder verlo en el catalogo y poder ver la forma en la que se muestra el modal al hacer clic en el vehiculo seleccionado.

TAREA A REALIZAR
===========

Se busca desarrollar una caracteristica nueva al sitio. Cuando el uisuario ingresa a ver un modelo de auto se agregará un pequeño widget que permita calcular el financiamiento que se puede hacer al auto.

La parte estetica y de diseño no será evaluada en esta instancia. Simplemente el funcionamiento logico del sistema.

A continuacion se detalla los detalles numericos y se muestra con un ejemplo.

Cuotas		Coheficientes Cuota promedio X cada $1000
12			  108.67
24			  67.57
36		  	54.81

Porcentaje a Financiar de acuerdo al modelo:
Antigüedad hasta 3 años: 70% 
Antigüedad entre 4 y 5 años: 60% 
Antigüedad entre 6 y 8 años: 50%

Ejemplo:
Calculo para auto Fiesta Kinetic 2008 - precio de lista $98000

Por modelo 2008 vemos que el maximo a financiar es el 60% por lo tanto:

Entrega = Monto total - Monto Fianciado

Entrega = $98000 - $58800
Entrega = $39200

Calculo de cuota:

Para 12 meses:

Cuota Promedio = (Monto Financiado * Cuota promedio) / 1000

Cuota Promedio = $6389.796


El sistema debería
===========
Lado Publico:
1. No permitir que se introduzcas un valor superior al maximo a financiar segun el modelo 
2. Permitir la seleccion de cuotas (12, 24 y 36)
3. Luego de presionar "Calcular" debería Mostrar el valor de la cuota promedio.
Lado Adminitracion:
1. Ingresar los coheficientes que varian mensualmente.


