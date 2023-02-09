# Retos-Programacion-MoureDev
Retos de Programacion resueltos en Python.

<br>

<h1> Introduccion </h1>
Este repositorio contendrá un conjunto de scripts escritos en Python que resuelve una serie de problemas de lógica de programación.
Dentro de cada archivo se incluye el enunciado del ejercicio que se resuelve en el mismo.


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

<h2> Reto #3 --> Es un numero primo? </h2>
Este reto trata de crear una función que sea capaz de comprobar si un numero es primo o no. 

Ademas, debe devolver el resultado de comprobar que numeros son primeros y cuales no de una lista de numeros del 1 al 100.
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


<h2> Reto #10 --> Expresiones Equilibradas </h2>
Este reto consiste en crear una funcion que analice una determinada expresion que introduzca el usuario por teclado.
Tras analizarla, debe haber comprobado que los elementos '(',')' - '[',']' - '{','}' estan correctamente colocados, y retornar un resultado u otro en funcion de la comprobacion.
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


<h2> Reto #22 --> Conjuntos </h2>

Este reto consiste en crear una funcion que reciba tres parametros. Los dos primeros representan una lista cada uno que puede contener n valores con independecia de tipo. El tercer parametro debe ser un valor booleano que decidira el resultado que deberia tener el programa.

 - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
<br>
<br>
<br>
<br>

<h2> Reto #23 --> Minimo Comun Multiplo y Maximo Comun Divisor </h2>

Este reto consiste en crear dos funciones que reciban como parametros 2 numeros y devuelvan un resultado tras calcular el minimo comun multiplo (una funcion) y el maximo comun divisor (la otra funcion) de esos dos numeros.
<br>
<br>
<br>
<br>

<h2> Reto #24 --> Iteration Master </h2>
Este reto consiste en mostrar de cuantas formas diferentes se es capaz de imprimir por pantalla los numeros del 1 al 100.

<br>
<br>
<br>
<br>

<h2> Reto #25 --> Piedra, Papel o Tijera </h2>
Este reto consiste en crear un programa que, tras analizar una serie de jugadas de dos jugadores a piedra, papel o tijera, se determine cual de estos ha ganado, o si la partida ha resultado en empate.

Dentro del archivo del juego 'reto.py' hay mas informacion detallada sobre el modo de juego.

<br>
<br>
<br>
<br>


<h2> Reto #26 --> Cuadrado y Triangulo 2D </h2>
Este reto consiste en crear una funcion que imprima por pantalla un cuadrado o un triangulo, segun la eleccion del usuario.

Ambas figuras estan compuestas por el simbolo '*', y el usuario debe elegir la longitud de los lados o alturas de las figuras.

<br>
<br>
<br>
<br>


<h2> Reto #27 --> Vectores Ortogonales </h2>
Este reto consiste en crear una funcion que reciba dos listas como argumentos, representando dos vectores.

La funcion debe ser capaz de imprimir por pantalla si ambos vectores son ortogonales o no.

<br>
<br>
<br>
<br>

<h2> Reto #28 --> Maquina Expendedora </h2>
Este reto consiste en crear un programa que simule el comportamiento de una maquina expendedora.


La funcion tiene un argumento, y solicita al usuario introducir por teclado el numero del producto que desea comprar. En este caso, la funcion
tomara un camino u otro en funcion del argumento que haya pasado el usuario para el parametro, y el producto que haya seleccionado para comprar.

<br>
<br>
<br>
<br>

<h2> Reto #30 --> Marco de palabras </h2>
Este reto consiste en crear una funcion que, en base a un texto que esta reciba, imprima el texto por pantalla, pero en
el interior de un marco.

En mi funcion, no se le pasa un texto a la propia funcion al momento de invocarla, sino que, al ejecutarse, solicita un 
texto por teclado al usuario. El marco que se imprime al final contendra el texto que el usuario ha introducido por teclado.

<br>
<br>
<br>
<br>

<h2> Reto #31 --> Años bisiestos </h2>
Este reto consiste en crear una funcion que evalue cuando un año es bisiesto, y cuando no lo es.

La funcion tiene que ser probada imprimiendo que años son bisiestos y cuales no en los proximos 30 años.

<br>
<br>
<br>
<br>


<h2> Reto #32 --> EL SEGUNDO </h2>
Este reto consiste en crear una funcion reciba una secuencia como argumento y retorne el segundo numero mas grande de la misma.

La funcion esta pensada para que la secuencia pasada como argumento solo contenga numeros, pero en la caso de que algun elemento de la misma sea una cadena de texto, se la evaluara como la suma de todos los puntos de codigo de las letras que la componen.

<br>
<br>
<br>
<br>

<h2> Reto #34 --> Los numeros perdidos </h2>
Este reto consiste en crear una funcion que evalue una lista pasada como argumento, y retorne todos los numeros comprendidos entre el primer elemento del argumento (argumento[0]), y el ultimo elemento (argumento[-1]) QUE NO ESTEN CONTENIDOS en el propio argumento.

<br>
<br>
<br>
<br>

<h2> Reto #35 --> Batalla Pokémon </h2>
Este reto consiste en crear un programa que retorne un resultado numerico tras evaluar los argumentos pasados a la funcion principal del programa en su invocacion.

Mi funcion retorna por pantalla un string que detalla al usuario cuando daño ha inflingido un Pokémon a otro.
<br>
<br>
<br>
<br>

<h2> Reto #36 --> Los anillos de poder</h2>
Este reto consiste en crear un programa que sumile una batalla entre dos bandos de personajes.

El programa debe permitir elegir al usuario la cantidad de personajes que debe haber en cada bando.
<br>
<br>
<br>
<br>

<h2> Reto #37 --> Los lanzamientos de "The Legend of Zelda” </h2>
Este reto consiste en crear un programa que solicite al usuario dos juegos de la franquicia de Nintendo "The Legend of Zelda”, y devuelva por pantalla el tiempo transcurrido en años y días entre el lanzamiento al mercado de ambos juegos.

<br>
<br>
<br>
<br>

<h2> Reto #38 --> Binario a decimal </h2>
Este reto consiste en crear una funcion que reciba un numero en codigo binario y retorne su equivalente a numero decimal.

<br>
<br>
<br>
<br>

<h2> Reto #41 --> La ley de Ohm </h2>
Este reto consiste en crear una funcion con tres parametros que reciba argumentos para dos de ellos durante la invocacion, y devuelva por pantalla  el valor del tercero de ser posible.

<br>
<br>
<br>
<br>

<h2> Reto #42 --> Conversor de temperatura </h2>
Este reto consiste en crear una funcion que, en base a la informacion de temperatura recibida por teclado, devuelta un string por pantalla con la temperatura en una unidad diferente.

<br>
<br>
<br>
<br>

<h2> Reto #43 --> Truco o trato </h2>
Este reto consiste en crear un programa que reciba una serie de parametros y retorne un string final con el resultado. Las instrucciones y demas infromacion estan en el archivo reto.py del reto.

<br>
<br>
<br>
<br>

<h2> Reto #44 --> Boomeranes </h2>
Este reto consiste en crear una funcion que reciba un array y, tras evaluarlo, devuelva por pantalla los boomeranes que se encuentran dentro del propio array.

En el enunciado del ejercicio (dentro del archivo reto.py) se encuentran las instrucciones de que es un boomeran y como debe actuar la funcion.
<br>
<br>
<br>
<br>

<h2> Reto #47 --> La vocal más común </h2>
Este reto consiste en crear una funcion que evalue un texto o string, y retorne por pantalla la vocal mas repetida.
<br>
<br>
<br>
<br>

<h2> Reto #48 --> El calendario de aDEViento 2022 </h2>
Este reto consiste en crear una funcion que imprima por pantalla el regalo correspondiente al dia del calendario de aDEViento 2022 pasado como argumento o, en su defecto, el tiempo que queda para que empiece el calendario, o tiempo que ha pasado desde que ha terminado.
<br>
<br>
<br>
<br>







