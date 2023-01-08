# Retos-Programacion-MoureDev
Retos de Programacion resueltos en Python.

<br>

<h1> Introduccion </h1>
Este repositorio contendrá un conjunto de scripts escritos en Python que resuelve una serie de problemas de lógica de programación.

Todos los archivos de codigo contienen comentarios explicando el problema en cuestion, asi como comentarios que indican los pasos que yo he
seguidos para su resolucion.
<br>
<br>
<br>
<br>

<h2> Reto #0 --> El famoso 'fizzbuzz'. </h2>
Se trata de mostrar una serie de mensajes por pantalla en base a una secuencia de numeros.

En el caso de que el numero de la secuencia sea divisible entre 3, el programa mostrara el mensaje 'fizz'.

En el caso de que el numero de la secuencia sea divisible entre 5, el programa mostrara el mensaje 'buzz'.

Por su parte, si el numero de la secuencia es divisible entre 3 y 5 a la vez, el programa imprimira 'bizzbuzz' por pantalla.
<br>
<br>
<br>
<br>

<h2> Reto #1 --> ¿Es un anagrama? </h2>
Este reto trata de crear una función que retorne un valor booleano en funcion si dos strings pasados como argumentos al invocar la funcion
son anagramas o no.
<br>
<br>
<br>
<br>

<h2> Reto #2 --> La sucesion de Fibonacci. </h2>
Este reto trata de crear una función que calcule la sucesion de Fibonacci en base a los primeros 50 numeros.
<br>
<br>
<br>
<br>

<h2> Reto #4 --> Area de un poligono </h2>
Este reto trata de crear una función que reciba un poligono como argumento y devuelva el area del mismo.

La funcion que he creado recibe como argumento un input que representa el poligono en cuestion. En funcion de que poligono haya introducido
el usuario como poligono, el programa tomara una ruta u otra para devolver el area de los poligonos.

Esta funcion permite calcular el area de 3 poligonos:

  - Triangulo
  
  - Cuadrado
  
  - Rectangulo
<br>
<br>
<br>
<br>

<h2> Reto #6 --> Invirtiendo cadenas. </h2>
Este reto trata de crear una función que invierta una cadena pasada como argumento.

La funcion emplea un bucle for para introducire en una lista vacia cada elemento de la cadena desde el final en cada iteracion

e.g.:

    string = 'food'

 iteracion n1:
 
    listaCadena = ['d']

 iteracion n2:
 
    listaCadena = ['d','o']
    
    ...
    
    
Finalmente, hago uso del metodo .join() para crear la cadena resultante.
<br>
<br>
<br>
<br>



<h2> Reto #7 --> Contando palabras. </h2>
Este reto consiste en crear un programa al que, una vez introducido un texto, sea capaz de devolver cuantas repeticiones tiene cada palabra que
lo compone.
El programa utiliza como delimitador del texto un espacio (' '), lo cual esta documentado en el script (si se quiere cambiar el delimitador, deberia cambiarse en el metodo 'string'.strip('''delimitador aqui''')).
<br>
<br>
<br>
<br>


<h2> Reto #8 --> Decimal a binario </h2>
Este reto consiste en crear un programa que, dado un numero entero positivo cualquiera, sea capaz de devolver el mismo numero en codigo binario.
<br>
<br>
<br>
<br>


<h2> Reto #9 --> Código morse </h2>
Este reto consiste en crear un programa el cual pide al usuario introducir un texto.

El texto introducido por el usuario se comprobara mediante una funcion auxiliar para comprobar si esta escrito en lenguaje natural, o en codigo morse.

Una vez hecha la comprobacion, la funcion principal realiza la traduccion de acuerdo al tipo de texto original.
<br>
<br>
<br>
<br>

<h2> Reto #11 --> Eliminando caracteres </h2>
Este reto consiste en, a partir de dos cadenas pasadas como argumento a una funcion, conseguir que esta retorne otras dos nuevas cadenas (out1, out2) pero:

 - out1 solo puede contener aquellos valores del primer string que no esten en el segundo.
 - out2 solo puede contener aquellos valores del segundo string que no esten en el primero.
<br>
<br>
<br>
<br>

<h2> Reto #12 --> Es un palindromo? </h2>
Este reto consiste en crear una función que devuelva un valor booleano (True o False) en función si la cadena que recibe como argumento es o no un palindromo (Un palindromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.)
<br>
<br>
<br>
<br>

<h2> Reto #13 --> Factorial Recursivo </h2>
Este reto consiste en crear una funcion que calcule el factorial de un numero, la cual se llame a si misma durante la ejecucion de la funcion.
<br>
<br>
<br>
<br>

<h2> Reto #14 --> Es un numero de Armstrong? </h2>
Este reto consiste en crear una funcion que nos retorne un valor booleano (True o False) en funcion de si el numero que recibe como argumento es o no un numero de Armstrong o numero narcisista.

  - Un numero de Armstrong es un numero el cual la suma del resultado de elevar cada numero que lo compone a la cantidad total de numero que componen el argumento, es igual al propio argumento.
  
  e.g.:
  371 --> 3 elevado a 3 + 7 elevado a 3 + 1 elevado a 3 = 371
<br>
<br>
<br>
<br>

<h2> Reto #16 --> En mayuscula </h2>
El reto consiste en crear una funcion que reciba un string y que devuelva una copia del mismo con las letras iniciales de cada palabra en mayuscula. ESTA PROHIBIDO emplear funciones integradas que lo hagan de forma automatica.
<br>
<br>
<br>
<br>

<h2> Reto #17 --> La carrera de obstaculos </h2>
El reto consiste en crear una funcion con dos parametros.

- La función recibirá dos parámetros:

     - Un array que sólo puede contener String con las palabras
       "run" o "jump".
       
    - Un String que represente la pista y sólo puede contener "_" (suelo)
        o "|" (valla).
        
 - La función imprimirá cómo ha finalizado la carrera:
 
     - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
        será correcto y no variará el símbolo de esa parte de la pista.
        
      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
      
      - Si hace "run" en "|" (valla), se variará la pista por "/".
      
 - La función retornará un Boolean que indique si ha superado la carrera.
   Para ello tiene que realizar la opción correcta en cada tramo de la pista.
<br>
<br>
<br>
<br>

<h2> Reto #19 --> Conversor Tiempo </h2>

Este reto consiste en crear una funcion que reciba como argumentos unos datos de tiempo entrero que representen los dias, las horas, los minutos y los segundos, y retorne el numero de milisegundos totales.
<br>
<br>
<br>
<br>


<h2> Reto #20 --> Parando el tiempo </h2>

Este reto consiste en crear una funcion que reciba tres parametros. Dos de ellos representan dos enteros que la funcion tiene que sumar y retornar co o resultado. El tercer parametro representa el numero de segundos que deben pasar antes de que la funcion retorne su resultado.
<br>
<br>
<br>
<br>
