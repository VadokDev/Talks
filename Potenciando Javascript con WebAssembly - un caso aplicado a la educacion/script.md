## Presentación

* Walmart STA
* OCILabs
* Ayudante Coordinador de Programación


### OCILabs

Esta pasión me ha llevado a participar de diversas iniciativas, siendo OCILabs una de las que más orgulloso estoy. En ella, actualmente formo parte del equipo de coordinación en conjunto con María Paz Morales, Anastasiia Fedorova, Gabriel Carmona y Hugo Leyton, quienes trabajamos día a día para enseñarle a jóvenes de 7mo a 4to medio sobre programación en distintos niveles. 

Éstos niveles van desde el básico, donde se enseña el pensamiento computacional a través de Scratch, luego sigue el intermedio donde refuerzan estos contenidos de la mano del lenguaje de programación C++, y finalmente el avanzado, donde todo el conocimiento previo se lleva a otro nivel con estructuras de datos y algoritmos más complejos, de cara a participar de las Olimpiadas Chilenas de Informática.

Han participado un total de 3292, a lo largo de estos 4, lo cual ha sido posible gracias a los 87 tutores que nos han apoyado, y que además del conocimiento entregado, tenemos un total de 13 estudiantes que clasificaron a las finales de las Olimpiadas Chilenas de Informática. Además, hoy en día muchos con compañeros y compañeras de carrera tanto en la USM como en otras universidades, la verdad... es que no podríamos estar más orgullosos y motivados por seguir trabajando en esto.

### Programación IWI-131

Por otro lado, también me he dedicado a trabajar como profesor y coordinador durante muchos años. Actualmente tengo un excelente equipo de ayudantes para el ramo de Programación, en la UTFSM Campus San Joaquín, con quienes nos encargamos de apoyar la labor docente día a día. En la foto hay tanto ayudantes actuales como antiguos, me gustaría tener a todos en este collage, pero no tengo las fotos de cada uno.

En la Universidad Técnica Federico Santa María, se dicta este curso introductorio a lo largo de todos sus campus. Recibiendo de forma masiva a todos los estudiantes de primer año de ingeniería, y se dicta de igual forma independiente del campus o carrera del estudiante. El curso se divide en Unidades Virtuales de Aprendizaje (UVA), las cuales estructuran las actividades de cada semana, según el siguiente modelo formativo. Su diseño se basa en el alineamiento constructivista, el cual plantea la necesidad de que las evaluaciones del curso, reflejen los objetivos de aprendizaje del mismo, y a su vez definan las actividades y tareas a realizar. Esto brinda a las tareas un rol tanto formativo como sumativo a la hora de evaluar, y requiere por lo tanto, que estas cumplan ciertos estándares para justificar que cumplen con los objetivos de aprendizaje.
 
## Tareas

Todo esto suena muy lindo y bello pero y entonces... ¿Qué son las tareas?, ¿para qué sirven?, Hay una cita muy hermosa de Allison Boye, quién en su artículo "How do I Create Meaningful and effective assignments" dice que las tareas son parte importante del proceso de enseñanza y aprendizaje, y es que para el caso de los cursos introductorios de programación, éstas son el primer acercamiento que tienen los estudiantes a los conceptos fundamentales de la computación, y es que en el fondo, los principales aspectos para los que sirven una tarea son 

### ¿Para qué sirven?

- Brindarle al profesor una herramienta, con la cual puede medir cómo los estudiantes están adquiriendo los contenidos del curso a lo largo del semestre
- Instar al estudiante a aplicar los contenidos adquiridos a lo largo del curso
- Incentivar al estudiante a aprender más, y motivarse con el curso, a medida que éste toma los conocimientos adquiridos y los aplica en un caso real
- Y por último, retroalimentar al estudiante, permitiéndole aprender en base a sus errores y sus aciertos

### ¿Qué se debe cumplir?

- Las tareas deben tener alguna aplicación real, o bien, resolver un problema real que le dé sentido al tiempo que el estudiante invertirá en resolverla.
- Las tareas deben ser interesantes, un problema puede expresarse utilizando un contexto de la actualidad, de lo que los estudiantes en general considerarían interesante como lo son sus bandas, juegos, tendencias, etc.
- Las tareas deben tener un nivel de dificultad adecuado, ni muy difíciles como para frustrar al estudiante, ni muy fáciles como para no cumplir con los objetivos de aprendizaje de la misma.

### ¿Qué pasa cuando no se cumple?

- Pérdida del interés en aprender a programar, de modo tal que el estudiante deje de ver el ramo como un curso de aprendizaje, y su actitud hacia él sea nétamente para aprobar.
- Frustración a lo largo del ramo, al punto en que el estudiante puede decidir desertar del curso y de la programación en general.
- Aumentar las probabilidades de que los estudiantes realicen actos que falten a la honestidad académica para resolverla.
- Complicar la elaboración de la rúbrica con la cual la tarea será evaluada, lo que puede conllevar a entregar un feedback menos valioso al estudiante

### Aspectos emocionales 

Diversas investigaciones acerca de las tareas, se han concentrado en el aspecto emocional que el estudiante experimenta durante la resolución de las mismas.

[DIAGRAMA]

Por todo esto y más, es que nace la importancia de hacer tareas de calidad, y que éstas logren cumplir un rol incentivador y pedagógico de cara al estudiante, quien está introduciéndose en este bello y enorme mundo de la computación.

## Complejidad de una tarea

La verdad es muy complicado llegar a una herramienta definitiva, que nos permita determinar de forma automatizada la calidad de una tarea dada, sin embargo, no estamos de manos vacías. Hoy en día las técnicas de inteligencia artificial nos permiten tener una aproximación de la complejidad textual de los enunciados, entre otros aspectos, sin embargo, yo soy un 0 a la izquierda cuando se trata de inteligencia artificial, así que decidí irme por otra rama de análisis: **El código que resuelve la tarea**.

#### Maurice Halstead

Para esto, tenemos que viajar 50 años en el pasado para toparnos con el trabajo de Maurice Halstead. 

Maurice fue Profesor de la Universidad de Purdue y creador de los conceptos de la ciencia del software, que condujo al desarrollo de las métricas del software.

En su libro, Elements of Software Science, él planteó el primer resumen sistemático de una rama de la ciencia experimental y teórica, que se ocupa del análisis y medición de la creación de programas computacionales.

### Métricas de Halstead

Entre las métricas que Halstead definió para un programa, se encuentran:

Vocabulario: Cantidad de operadores y operandos únicos utilizados en un programa
Largo: Cantidad de operadores y operandos utilizados en programa
Volumen: Tamaño en bits necesario para almacenar el programa, dependiente de la implementación de un algoritmo dado
Esfuerzo: Cantidad de operaciones mentales requeridas para desarrollar un programa
Tiempo requerido para progarmarse
Cantiad de bugs entregados: Estimación de cuantos errores puede tener la implementación

### Veamos un ejemplo

Vamos a ver a grandes rasgos cómo se calcula el esfuerzo de un programa, notar que todas estas métricas se calculan a partir de un código ya desarrollado.

Pensemos en la forma mínima en la que podemos expresar cualquier código, si nos abstraemos de los ifs, las clasaes, el polimorfismo, la subyacencia intercontractual (esa última la inventé). Podemos notar que todo programa se compone de un conjunto de operadores (funciones, sumas, restas, comparadores), y un conjunto de operandos (números, variables, palabras, etc), los cuales utilizamos las veces que sean necesarias para lograr nuestra implementación.

[Imagen de un programa mostrando qué operandos y operadores tiene]

Por lo mismo, podemos decir que la acción misma de programar, se reduce a elegir correctamente cada uno de estos operadores y operandos, y colocarlos en nuestro código.

De estas afirmaciones, podemos plantear el siguiente algoritmo, el cual llevará a cabo nuestro cerebro, para desarrollar cualquier código:

``` Javascript
while (el código no está listo) {
    if(necesito un operador)
        buscarOperador()
    
    if(necesito un operando)
        buscarOperando()
}

```

Ahora bien, concentrémonos en las 2 funciones que tenemos aquí, dado que buscarOperador y buscarOperando no hacen más que buscar, en su respectivo conjunto, el elemento que necesitamos poner en nuestro código.

[imagen de búsqueda de elementos]

Lo interesante de esto es que inmediatamente podemos notar que mientras más veces llamenos a estas funciones, más carga cognitiva le estamos dando a nuestro cerebro, pues debe realizar más búsquedas. Lo mismo pasa si el código es muy grande, o tiene muchos operadores y operandos distintos donde buscar.

[Ejemplos de código]

Halstead tomó muchos aspectos de la ciencia que estudia el funcionamiento de nuestras mentes, para llevar estas ideas a fórmulas, con las cuales poder medir cuantitativamente la cantidad de procesos cognitivos que debería llevar a cabo nuestro cerebro, para realizar un código específico.

[Desglose matemático]

Y es que esta forma de ver el software es increíble, porque con datos como estos, si sabemos que (según estudios de ese entonces) el cerebro realiza 18 discriminaciones por segundo, entonces también podemos estimar el tiempo que tardaríamos en realizar un código dado con tan sólo dividir el esfuerzo por 18.

[Fórmula tiempo]

Estas y muchas otras métricas más, pueden encontrarlas en el libro Elements of Software Science, ahora bien, cual es la utilidad de todo esto ?

## Aplicación de estas métricas

Maurice Halstead planteó varias métricas de este estilo, pues su objetivo era definir el software como una ciencia, en base a fórmulas fundamentales, las cuales nos permitirían entender y predecir el comportamiento de cualquier programa, así como con la física podemos entender y precedir aspectos de la naturaleza misma.

Para aplicar estas métricas, la idea es pensar en que cuando un docente termine de redactar el enunciado de una tarea, la resuelva. En el momento en que resuelve la tarea, se debe pasar el programa resultante por las métricas de Halstead, para determinar el esfuerzo que podría tomarle a un estudiante el desarrollar un programa así, entre otros aspectos.

[Diagrama de aplicación]

## Ishvel

Es por esto que nace Ishvel, un framework para la elaboración de tareas de cursos introductorios de programación. En esta plataforma los profesores pueden redactar su tarea, luego escribir el código que la resuelve, e inmediatamente obtener feedback respecto a las métricas de Halstead, y una comparación con las tareas del semestre pasado.

[Foto de Ishvel]

Sin embargo, el desarrollo de esta plataforma no estuvo excemto de complicaciones, principalmente porque:

1. La biblioteca que ya implementa el cálculo de métricas de Halstead para Python, está pues... escrita en Python
2. Es difícil mantener un proyecto universitario en línea cuando nadie le da soporte, por lo tanto había que encontrar una forma de hacer distribuir la aplicación dependiendo lo menos posible de servidores externos.

Entonces... cómo resolvemos esto?

## Solución Técnica

Aquí es donde entran en juego los héroes de mi tesis

### WebAssembly

WebAssembly es un formato de instrucciones binarias creado con el fin de ser ejecutado en una máquina virtual, es decir, podemos ejecutarlo en cualquier dispositivo capaz de correr esta máquina virtual, lo que nos permite ejecutar código de muy bajo nivel en nuestros navegadores.

Sin embargo, el objetivo final de WebAssembly no es que comencemos a desarrollar en un lenguaje como ensamblador nuestras aplicaciones, si no más bien, brindarnos la posibilidad de utilizar otros lenguajes de programación en ellas, gracias a su capacidad de ejecutar código de muy bajo nivel, veamos esto a grandes rasgos.

Originalmente, si quisiéramos ejecutar un programa de C++ en nuestros computadores, lo primero que debemos hacer es escribir el código 

[Hola mundo en C++]

Y luego, lo compilamos y obtenemos nuestro ejecutable, este ejecutable en realidad no es más que un conjunto de instrucciones en binario las cuales puede ejecutar nuestro computador, las cuales son determinadas por el compilador a medida que lee nuestro código.

Pero... qué tal si hacemos un compilador a nuestra pinta?, y en vez de utilizar el formato de instrucciones que tiene el compilador de C++, utilizamos el formato de WebAssembly?

Aquí es donde podemos ver una de las mayores gracias de WebAseembly, y que gracias a su capacidad de ejecutar código de bajo nivel, podemos utilizar un compilador que lleve nuestro código de C++ (o de cualquier otro lenguaje!) a un set de instrucciones que WebAssembly pueda ejecutar, como lo es por ejemplo, emscripten. Aquí podemos ver un ejemplo directo del sitio web de Mozilla Developers Network

[Ejemplo gráfico]
https://developer.mozilla.org/en-US/docs/WebAssembly/C_to_wasm

### Pyodide

Pero esto no se detiene aquí, volviendo al primer problema, la librería multimetric sólo puede ejecutarse en Python, aquí es donde retomamos la idea de que WebAssembly busca complementar nuestras aplicaciones con programas en otros lenguajes, y encuentro Pyodide.

* Implementación

## Conclusiones

* Ventajas y desventajas de hacer una aplicación autocontenida
* Descubrimientos interesantes 
* Mantención
 