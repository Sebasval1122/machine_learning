Juan Pablo Tafur – Sebastián Valencia 


README - Calculadora de Hipoteca Inversa

¿Qué es y para qué es?

La Calculadora de Hipoteca Inversa es una herramienta diseñada para estimar el monto que un propietario puede recibir a través de una hipoteca inversa. Utiliza datos como la edad del propietario, el valor de su vivienda y otros factores financieros para calcular los pagos mensuales y la deuda acumulada.


Entradas
Las entradas son los datos proporcionados por el usuario para el cálculo de la hipoteca inversa. Estas incluyen:

1.	Edad: Es la edad actual del propietario que solicita la hipoteca inversa.

2.	Expectativa de vida: Es el número de años que, en promedio, se espera que viva el propietario a partir de su edad actual. Se basa en tablas actuariales y estadísticas de longevidad.

3.	Años renta: Es la cantidad de años durante los cuales el propietario recibirá pagos mensuales de la hipoteca inversa.

4.	Total de cuotas: Es el número total de pagos mensuales que el propietario recibirá.

5.	Precio de la vivienda: Es el valor de mercado actual de la vivienda que se usará como garantía en la hipoteca inversa.

6.	Porcentaje del precio real: Es el porcentaje del valor total de la vivienda que el banco está dispuesto a prestar.

7.	Valor de la hipoteca: Es la cantidad total de dinero que el propietario recibirá a lo largo de la hipoteca inversa.

8.	Ingreso mensual: Es el monto que el propietario recibirá cada mes mientras dure la hipoteca inversa.

9.	Tasa de interés mensual: Es la tasa de interés aplicada mensualmente sobre la hipoteca inversa.




El cálculo de la hipoteca inversa sigue los siguientes pasos:

1.	Ingreso de datos: Se registran los valores de la Edad del propietario, expectativa de vida, Años renta, Precio de la vivienda, Porcentaje del precio real, Tasa de interés anual, Determinación del monto elegible:

o	Se aplican regulaciones y límites según la ubicación.
o	Se estima el monto basado en la edad y el valor de la vivienda.
o	Se descuenta cualquier saldo de hipoteca previa.

2.	Cálculo del interés acumulado: Se estima cómo crecerá la deuda con el tiempo.

3.	Generación del resultado: Se obtiene el monto disponible y las opciones de pago.


Salidas: 

El resultado del cálculo incluye:

•	Ingreso Mensual
•	Deuda Total
•	Errores de ingreso de datos

¿Cómo lo hago funcionar?

Prerrequisitos

Antes de ejecutar el proyecto, asegúrese de contar con:

•	Python instalado (versión 3.8 o superior).
•	Un entorno virtual configurado (opcional, pero recomendado).
•	Acceso a Git para clonar el repositorio.

Instalación y configuración

1.	Abra la terminal o el símbolo del sistema (cmd en Windows).
2.	Cambie al directorio donde desea clonar el proyecto:

cd ruta/deseada

3.	Clone el repositorio con el siguiente comando:

git clone https://github.com/JuanTafur10/HipotecaInversa.git

4.	Ingrese al directorio del proyecto:

cd HipotecaInversa

5.	Instale las dependencias necesarias:

pip install -r requirements.txt


Ejecución

Para ejecutar la interfaz de consola:

1.	Desde la carpeta raíz del proyecto, cambie a la carpeta src/view:

cd src/view

2.	Ejecute el siguiente comando para iniciar la aplicación:

python Hipoteca_Inversa_consola.py


Para ejecutar las pruebas unitarias:
1.	Regrese a la carpeta raíz del proyecto:

cd ../../

2.	Ejecute las pruebas unitarias:

python -m unittest discover -s tests

3.	Si las pruebas no se ejecutan correctamente, asegúrese de que la ruta de búsqueda de módulos incluya src. Para ello, agregue lo siguiente al inicio del archivo de pruebas:

import sys
sys.path.append("src")

¿Cómo está hecho?
El proyecto sigue una arquitectura modular con separación de responsabilidades. Se organiza en las siguientes carpetas:

•	src/: Contiene el código fuente de la aplicación.
  o	model/: Contiene la lógica del cálculo de la hipoteca inversa (hipoteca_inversa.py).
  o	view/: Contiene la interfaz de consola con la que interactúa el usuario (Hipoteca_Inversa_consola.py).

•	tests/: Contiene las pruebas unitarias del proyecto.
  o	test_hipoteca_inversa.py: Implementa casos de prueba para verificar el funcionamiento del código.

•	.vscode/: Contiene configuraciones de VS Code para el entorno de pruebas.

•	.gitignore: Define archivos y carpetas que no deben incluirse en el repositorio.

Cada carpeta de código fuente contiene un archivo __init__.py para que Python la reconozca como un módulo importable.
