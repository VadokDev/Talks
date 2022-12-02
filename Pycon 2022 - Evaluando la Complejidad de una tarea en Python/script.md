# Evaluando la complejidad de una tarea en Python, con Python

Hola!, qué tal ?, mi nombre es Gonzalo Fernández, actualmente me desempeño como desarrollador Full-stack en Walmart, pero además de desarrollador, tengo una pasión enorme por la docencia y por enseñar acerca del mundo de las ciencias de la computación.

## Presentación



### OCILabs

Esta pasión me ha llevado a participar de diversas iniciativas, siendo OCILabs una de las que más orgulloso estoy. En ella, actualmente formo parte del equipo de coordinación en conjunto con María Paz Morales, Anastasiia Fedorova, Gabriel Carmona y Hugo Leyton, quienes trabajamos día a día para enseñarle a jóvenes de 7mo a 4to medio sobre programación en distintos niveles. 

Éstos niveles van desde el básico, donde se enseña el pensamiento computacional a través de Scratch, luego sigue el intermedio donde refuerzan estos contenidos de la mano del lenguaje de programación C++, y finalmente el avanzado, donde todo el conocimiento previo se lleva a otro nivel con estructuras de datos y algoritmos más complejos, de cara a participar de las Olimpiadas Chilenas de Informática.

Han participado un total de [TOTAL ESTUDIANTES], a lo largo de estos [CANTIDAD DE AÑOS], lo cual ha sido posible gracias a los [TOTAL DE TUTORES] tutores que nos han apoyado, y que además del conocimiento entregado, tenemos un total de [TOTAL CLASIFICADORES OCI] estudiantes que clasificaron a las finales de las Olimpiadas Chilenas de Informática. Además, hoy en día muchos con compañeros y compañeras de carrera tanto en la USM como en otras universidades, la verdad... es que no podríamos estar más orgullosos y motivados por seguir trabajando en esto.

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

#### Hablar de Maurice Halstead.

#### Explicar cómo se mide la complejidad cognitiva de un código

## Aspectos Generales

* η1 = número de operadores distintos que aparecen en la implementación
* η2 = número de operandos distintos que aparecen en la implementación
* N1 = número total de usos de todos los operadores que aparecen en la implementación
* N2 = número total de usos de todos los operandos que aparecen en la implementación

Luego, podemos entender η = η1 + η2 como el vocabulario de la implementación, y N = N1 + N2 como su largo.

Veamos un ejemplo

```
def GCD(a, b):
    if(b == 0):
        return abs(a)
    else:
        return GCD(b, a % b)
```

Para este algoritmo del máximo común divisor entre 2 números, tenemos las siguientes métricas de N y η
```
η1: 2
η2: 3
N1: 2
N2: 4
vocabulario (η): 5
largo (N): 6
```

Revisemos estos valores:

1. η1 corresponde al operador de igualdad y al operador módulo
2. η2 corresponde a las variables a, b y al valor 0
3. N1 corresponde al único uso que se le da al operador de igualdad, y al operador módulo
4. N2 corresponde a los 2 usos que se les da al operando b, y al único uso que se le da tanto al operador a como al operador b
5. El vocabulario se calcula como η = η1 + η2
6. El largo se calcula como N = N1 + N2

Notar que los operandos sólo aplican para operaciones, es decir, los parámetros no cuentan como operandos en este cálculo. En el caso de las sentencias if, else y return, no se consideran operadores para darle generalidad al cálculo, aunque al final depende de la implementación que se realice. Éste ejemplo deriva del módulo radon, el cual veremos más adelante

### Volumen de un programa

Para cualquier algoritmo dado, podemos determinar su tamaño en base a la cantidad de código que tiene su implementación, sin embargo, sabemos que para 2 lenguajes de programación distintos, podemos implementar un mismo algoritmo utilizando más o menos código en uno que en el otro, pese a que ambos hacen prácticamente lo mismo. ¿Cómo podemos entonces, tener una medida de tamaño para un programa, que nos de información independiente del lenguaje?, aquí es donde Halstead propuso el Volumen de un programa.

Vamos a implementar un algoritmo con sólo 2 operadores y 2 operandos:

```
a = 1 + 2
b = 2 - 1
```

Luego, las métricas de este algoritmo son:

```
η1: 2
η2: 2
N1: 2
N2: 4
vocabulario (η): 4
largo (N): 6
```

Si se fijan bien, para este programa existen un total de 4 elementos únicos (2 operadores y 2 operandos), es decir, si quisiésemos representar representar todos los elementos posibles de éste código, sólo necesitaríamos 4 valores distintos, verdad?, por lo mismo, con sólo 2 bits, podemos representar únicamente cada elemento de este código:

```
00: +
01: -
10: 1
11: 2
```

Es decir, podemos calcular la cantidad de elementos diferentes de un algoritmo, sin preocuparnos del lenguaje de programación en que está desarrollado. Para calcular cuantos bits necesitamos para representar los η elementos distintos, basta con aplicarle logaritmo en base 2. Luego, para obtener el volumen V de la implementación de un algoritmo, sólo nos falta determinar cuantas veces se utilizan estos elementos, y para ésto sabemos que N es la cantidad de usos de cada uno. Finalmente, podemos calcular el volumen de un programa como N log2(η)

V = N log2(η)

Ésta interpretación de volumen nos permite calcular el tamaño de un programa basándonos sólo en la cantidad de elementos que contiene, y no en el largo de sus operadores. Si utilizáramos un lenguaje de programación donde la suma se realizara con el operador +++++, y la resta con el operador -----, el código resultante sería:

```
a = 1 +++++ 2
b = 2 ----- 1
```

Sin embargo, si aplicamos el cálculo anterior, notamos que tanto en este lenguaje de programación, como en el lenguaje del código anterior, ambas implementaciones tienen exactamente el mismo volumen:

```                
a = 1 +++++ 2                                 a = 1 + 2
b = 2 ----- 1                                 b = 2 - 1
          
00: +++++                                     00: +
01: -----                                     01: -
10: 1                                         10: 1
11: 2                                         11: 2
          
η1: 2                                         η1: 2                       
η2: 2                                         η2: 2                       
N1: 2                                         N1: 2                       
N2: 4                                         N2: 4                       
vocabulario (η): 4                            vocabulario (η): 4                                 
largo (N): 6                                  largo (N): 6

V = N log2(η) = 12                          V = N log2(η) = 12
```           

### Volumen Potencial

Existen lenguajes de programación que ya implementan de base ciertos algoritmos en sus librerías, como resultado, la mínima forma en la que podemos expresar un algoritmo, es llamando a la función correspondiente que lo ejecute, considerando tanto sus resultados como sus parámetros.

```
resultado = superAlgoritmo(valor1, valor2)
```

En este caso, el nombre de la función sería un operador, y el operador de asignación para utilizar su resultado sería otro, lo que nos da que para toda forma mínima de expresar un algoritmo, η1* siempre será 2, donde * significa "potencial". Además, cómo no necesitamos repetir ni los operadores ni los operandos, también tenemos que N1* = η1* y N2* = η2*, entonces, retomando la operación de volumen, podemos calcular el volumen potencial como:

V* = N* log2(η*) = (η1* + η2*) log2 (2 η1 + η2) = (2 + η2) log2 (2 + η2)

Es decir, el volumen potencial nos ayuda a representar el caso en que utilicemos la mínima forma posible de llamar un algoritmo, la cual es, teniendo el algoritmo implementado. No ahondaremos mucho más en este cálculo, sin embargo es importante ser consiente del mismo para lo que viene ahora.

### Resumiendo

Para recapitular, tenemos hasta ahora un conjunto de métricas generales, y una manera de estimar el volumen de la implementación de un algoritmo, independiente del largo de los operadores del lenguaje de programación en que está desarrollado.

1. η1 = número de operadores distintos que aparecen en la implementación
2. η2 = número de operandos distintos que aparecen en la implementación
3. N1 = número total de usos de todos los operadores que aparecen en la implementación
4. N2 = número total de usos de todos los operandos que aparecen en la implementación
5. El vocabulario se calcula como η = η1 + η2
6. El volumen se calcula como N log2(η)
7. El volumen potencial se calcula como (2 + η2) log2 (2 + η2)

### Esfuerzo de realizar un programa

Ahora que sabemos todo ésto, por fin estamos listos para entender cómo calcular el esfuerzo que toma realizar cierto programa, para ello, acompáñenme a derivar la ecuación.

* Sabemos de base que cualquier implementación de un algoritmo, va a consistir en realizar N selecciones de un vocabulario de η elementos. Es decir, dado un lenguaje de programación, nuestro código resultante será el haber elegido correctamente N veces un elemento del mismo.

* Para la fecha en que Halstead publicó su trabajo, la forma de búsqueda más eficiente en un conjunto ordenado es la búsqueda binaria. Vamos a asumir que nuestros cerebros son eficientes para seleccionar elementos, y por lo tanto, que la acción de realizar N selecciones de un vocabulario de η elementos, en realidad se traduce a realizar N búsquedas binarias en un conjunto ordenado de η elementos, y por ende, cada selección realiza log2(η) comparaciones.

* Para este punto, podemos notar que escribir un código equivale a realizar N log2(η) procesos cognitivos, ¿y qué era N log2(η)?, el volumen!, vale decir, el Volumen de un programa es equivalente a la cantidad de comparaciones mentales requeridas para generar un programa.

* Por otro lado, y en este punto, tendrán que creerme, el número promedio de discriminaciones que realizaríamos cognitivamente (es decir, la cantidad de elementos equivocados que encontraremos durante nuestra búsqueda binaria cognitiva), se expresa como la razón entre el volumen de un programa y el volumen potencial V* / V

* Teniendo entonces la cantidad de comparaciones y discriminaciones cognitivas, podemos calcular el esfuerzo mental de desarrollar un programa como la multiplicación entre la cantidad de comparaciones, y la cantidad de discriminaciones, es decir, E = V (V / V*) = V^2 / V*

## Aplicación de estas métricas 

Maurice Halstead planteó varias métricas de este estilo, pues su objetivo era definir el software como una ciencia, en base a fórmulas fundamentales, las cuales nos permitirían entender y predecir el comportamiento de cualquier programa, así como con la física podemos entender y precedir aspectos de la naturaleza misma.

Para aplicar estas métricas, la idea es pensar en que cuando un docente termine de redactar el enunciado de una tarea, la resuelva. En el momento en que resuelve la tarea, se debe pasar el programa resultante por las métricas de Halstead, para determinar el esfuerzo que podría tomarle a un estudiante el desarrollar un programa así, entre otros aspectos.

### Experimento

A continuación, se presenta el siguiente experimento, donde para cada tarea de este semestre de programación, se tomó 1 entrega cuya nota sea 100, y se calcularon sus métricas de Halstead utilizando radon

Radon es una biblioteca de Python que ya trae implementado el cálculo de métricas para un código dado, no sólo de Halstead si no también métricas puras como la cantidad de líneas de código, métricas de complejidad ciclomática como la cantidad de ramificaciones (cuantas decisiones debe realizar un código durante su ejecución), y métricas sobre mantenibilidad para calcular qué tan fácil de mantener es este software en el tiempo.

Radon se puede utilizar tanto pragmáticamente (es decir, siendo importado en nuestro código), como mediante su consola de comandos [foto de la CLI]


#### Mostrar ejemplos de las métricas de halstead sobre las tareas del semestre junto con las notas

Lamentablemente, el promedio de notas se ve afectado por diversos motivos, en este caso es que a medida que el semestre avanzaba, menos gente comenzaba a entregar sus tareas. Sin embargo, es posible notar que para cada tarea, tanto el volumen, esfuerzo y tiempo estimado de programar se mantienen proporcionales para una misma tarea, mientras que en términos de notas, para la tarea 4 donde está la tarea más difícil según las métricas de Halstead, aún estábamos en una etapa mediada del semestre, y las entregas aún no disminuían tanto. Se puede suponer una desmotivación o frustración en base a enfrentarse a esa tarea, que conlleva a no seguir esforzándose dado que ya se tenían muy buenas notas al inicio, o derechamente ya se llegó a un punto de mínimo esfuerzo para avanzar en el ramo.

Lamentablemente no es del todo conclusivo el impacto que pueden tener estas métricas y su relación con las notas, sin embargo, éste es un trabajo inicial, y aún queda para futuro poder evaluar el resto de potencial que se puede sacar de aquí. Más adelante se complementarán estos estudios con encuestas a los estudiantes, y se relacionará tanto su experiencia emocional como su percepción misma de la tarea en conjunto con las métricas de Halstead, para encontrar relaciones que van más allá de sólo la nota obtenida y la cantidad de personas que entregan las tareas.


#### Cerrar explicando que en realidad, ninguna de estas cosas tiene una alpicación práctica tanto en la naturaleza como en la ingeniería

Vale la pena mencionar aún así, que 5 años después de que se presentara el trabajo de Halstead, Elements of Software Science, se publicaron trabajos donde se planteaba que ninguna de estas ideas tiene una aplicación práctica, ni en la naturaleza ni en la ingeniería. Pero 50 años después, llega un jovencito que aún tiene fe en que si combinamos todo esto, podemos aportar con nuestro granito de arena a hacer de la educación sobre programación, un lugar mucho mejor. [FOTO DEL PAPER]

#### Hablar de Ishvel

Bueno gente, éste ha sido el resultado del trabajo teórico actual acerca de cómo calcular la complejidad de una tarea de Python, en Python. Sin embargo, ésto no termina aquí, toda esta investigación culmina en el trabajo de mi memoria llamado Ishvel: un framework para la elaboración de tareas para cursos introductorios de programación. Éste framework vendría siendo un grammarly de las tareas, ayudando a docentes a preparar sus tareas y permitirles tener un acercamiento inmediato a la dificultad estimada de sus tareas, en base tanto a las métricas de Halstead, como la implementación de otras métricas y análisis.

#### Invitarles a la charla "Potenciando Javascript con WebAssembly: Un caso aplicado a la educación" en la JSConf 2023, para ver la implementación final

Les extiendo cordialmente la invitación a verme en la charla "Potenciando Javascript con WebAssembly: Un caso aplicado a la educación", de la Javascript Conf Chile 2023, donde veremos la culminación de todo este trabajo, y cómo implementar el cálculo de estas métricas desde un navegador que ejecuta Javascript

Gracias por su tiempo!