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
