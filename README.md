# Practica III/ Sara Echeverri Gómez 

# Estructura del código: 
Mi proyecto implementa en Python un analizador sintáctico para recrear expresiones aritméticas, para el desarrollo de este analizador se utilizaron la biblioteca NLTK y una interfaz visual con PyQt. El proyecto implementa la gramática de contexto libre (CFG) para instaurar las normas sintácticas y a su vez para saber como se utiliza el parser ChartParser para evaluar la expresión generada por el usuario. La interfaz de el analizador propone la elección de porque lado se va a evaluar la derivación sea por derecha o por izquierda; luego muestra gráficamente el árbol de derivación en una ventana resultante al darle al botón siguiente, mostrando de manera visual la estructura sintáctica de la expresión dada por el usuario. 

 # 1.	Definición de la gramática:
Mi proyecto emplea para la definición de la gramática, una CFG (gramática de contexto libre) que establece las normas para expresiones aritméticas que involucran operaciones de adición (+), sustracción (-), multiplicación (*) y división (/); además admite variables de la A la Z y cifras del 0 al 9. 

# 2.	Expresión objetivo:
La expresión brindada por el usuario se manifiesta en forma de una cadena de caracteres o de texto, debido a esto esta cadena se debe tokenizar que es dividir un texto en unidades más pequeñas, es decir, dividir la cadena en componentes divididos por espacios. Un ejemplo es la expresión 5+(z * k)-g para poder que el programa la analice se debe tokenizar quedando como resultado los siguientes caracteres 5 + ( z * k ) – g .

# 3.	Creación del Analizador: 
El componente ChartParser de NLTK toma la gramática definida para analizar la expresión y verificar si cumple las reglas sintácticas.

# 4.	Interfaz Gráfica:
La interfaz gráfica permite al usuario ingresar la expresión y seleccionar el tipo de derivación (izquierda o derecha) que desea, para que posteriormente pueda ver el árbol de derivación en una ventana gráfica nueva.

# 5.	Generación del Árbol de Derivación:
Dependiendo de la selección del usuario, el programa genera el árbol de derivación, el cual se muestra mediante una ventana gráfica de PyQt.

# Requisitos para ejecutar el código: 
-	Tener Python instalado 
-	Instalar NLTK  (pip install nltk)
-	 Instalar PYQT5 (pip install pyqt5)

# Uso 
En la terminal de tu computador en mi caso powershell debes colocar este comando python main.py, para que el programa ejecute la interfaz que te va a permitir ingresar la expresión, posteriormente debes darle en si derivación por izquierda o derivación por derecha,  para luego darle al botón siguiente que es que te va a mostrar en una nueva ventana tu árbol sintáctico 

