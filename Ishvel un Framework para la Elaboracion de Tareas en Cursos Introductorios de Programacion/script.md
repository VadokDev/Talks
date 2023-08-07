# Ishvel, un Framework para la Elaboración de Tareas en Cursos Introductorios de Programación

## Introducción 

En la UTFSM se dicta el curso de Introducción a la Programación IWI-131 para todos los estudiantes de ingeniería en su primer año. Este suele ser para muchos, el primer acercamiento a la programación, y por consiguiente, la experiencia educativa que tengan en el semestre impactará directamente en su motivación para adentrarse más en este mundo.

Durante el semestre, los estudiantes experimentarán diversas formas de aprender y ser evaluados en base a la metodología de enseñanza impartida en el curso, la cual separa los contenidos de la asignatura en pequeñas Unidades Virtuales de Aprendizaje llamadas UVA. Cada UVA contempla distintas actividades tanto formativas como evaluativas, entre éstas, se encuentran las tareas.

### Tareas de Programación

Las tareas forman parte importante del proceso de aprendizaje y enseñanza, ya que permiten medir el nivel de aprendizaje del estudiante, y a su vez, entregarle retroalimentación sobre el mismo. Debido a esto, es que las tareas de programación deben elaborarse de la mejor manera posible, centrándose en evaluar los contenidos de modo tal que el estudiante se motive a aprender, y evitando a toda costa generar efectos adversos en el mismo como puede ser la frustración por el nivel de dificultad, la falta de ganas de aprender por verle nula utilidad al contenido, y en el peor de los casos, la deserción por los motivos antes expuestos y otros factores.

### Problemática

Cuando una tarea no está bien elaborada, el estudiante se ve enfrentado a:

* Pérdida del interés en aprender a programar, dejando de ver el ramo como una oportunidad de aprendizaje, y llevando una actitud donde sólo importa aprobar
* Frustración a lo largo del ramo, al punto en que el estudiante puede decidir desertar del ramo y de la programación en general
* Aumentar la probabilidades de realizar actos que falten a la honestidad académica para resolver la tarea
* Complicar la elaboración de la rúbrica con la que la tarea será evaluada, lo que conlleva a una retroalimentación menos valiosa para el estudiante.

Por lo mismo, se requiere de un marco de trabajo que facilite la elaboración de tareas, el cual brinde tanto una metodología como una herramienta para hacerlo y así apoyar a los profesores en esta labor.

### Objetivos

* Objetivo general: Desarrollar un framework para la elaboración de tareas en cursos introductorios de programación
* Objetivos específicos:
  * Identificar y definir criterios que puedan ser usados para evaluar una tarea
  * Definir una métrica que permita evaluar una tarea de acuerdo al cumplimiento de criterios
  * Definir una metodol.ogía para la elaboración de tareas utilizando el framework desarrollado

## Ishvel

En este contexto es que se desarrolla el framework Ishvel, el cual consta de una metodología de elaboración de tareas y una herramienta para llevarla a cabo, la cual cuenta con métricas para hacer un análisis oportuno de la dificultad de la tarea en base a su solución, y las soluciones de tareas anteriores.

### Métricas de una tarea de programación

Para poder comparar la dificultad de una tarea con otra, es necesario poder calcular ciertas métricas de software asociadas a las soluciones de estas, en particular, las métricas utilizadas en este trabajo son:

* Complejidad ciclomática: Es una métrica que mide la complejidad estructural de un programa. Cuanto mayor sea, más difícil es entender el código. Ayuda a identificar áreas problemáticas en el software.
* Volumen: Es una medida combinada de la longitud del programa y el tamaño del vocabulario utilizado. Cuanto mayor sea el volumen, mayor será la complejidad y el esfuerzo requerido para comprender y mantener el código.
* Dificultad según Halstead: es una métrica que estima la complejidad y la dificultad de comprensión de un código 
* Esfuerzo de Programación: es una métrica que estima la cantidad de trabajo mental requerido para desarrollar un programa
* Tiempo Estimado de Programación: Es el tiempo estimado en segundos requerido para realizar una implementación de código dada.

## Metodología

La metodología del framework Ishvel se divide en 3 partes:

* Determinar la diferencia de dificultad entre 2 tareas
* Elaborar una tarea utilizando el editor
* Análisis de tareas anteriores utilizando el editor

### Intervalos de Comparación de Dificultad para determinar la Diferencia de Dificultad entre 2 Tareas

Para poder comparar la dificultad entre 2 tareas, necesitamos una base desde la cual partir, que nos permita decir que una tarea es más difícil que otra, para así luego, inferir cómo es que se llega a esta diferencia de dificultad en base a la diferencia entre las métricas de sus soluciones.

Para esto se deben determinar los Intervalos de Comparación de Dificultad de cada métrica, exceptuando la métrica de tiempo estimado dado que ésta es múltiplo de la métrica de esfuerzo y su diferencia porcentual no nos aporta más información. Los Intervalos de Comparación de Dificultad permiten categorizar la diferencia de dificultad entre 2 tareas en base a la diferencia porcentual de sus métricas, de esta manera, al promediar la categoría en la que cae la diferencia porcentual de cada una de las métricas entre ambas tareas, se puede obtener la diferencia de dificultad final entre estas.

Por ejemplo, sean los intervalos de comparación de difucultad:

[Ver tabla en presentación de Canva]

Y las diferencias porcentuales

[Ver tabla en presentación de Canva]

Se puede determinar a qué intervalo pertenece la diferencia porcentual de cada una de las métricas obteniendo los siguientes valores

* Complejidad Ciclomática: 3
* Dificultad H: 4
* Esfuerzo: 2
* Volumen: 1

Por lo que según los Intervalos de Comparación de Dificultad del ejemplo, ambas tareas tendrían una dificultad similar, ahora bien, ¿Cómo se determinan los Intervalos de Comparación de Dificultad?

## Determinar los Intervalos de Dificultad

Para determinar los intervalos de dificultad, se requiere:

* Un conjunto de expertos en programación, ya sea docentes, ayudantes docentes o personas con experiencia en el área, y al menos 
* Todas las tareas de al menos 2 semestres distintos del ramo

Teniendo esto, se debe llevar a cabo una encuesta al equipo de expertos, en la cual se les pide comparar las tareas que corresponden a un mismo contenido lectivo, y determinar en base a su opinión, qué tan difícil es la tarea del semestre posterior en comparación a la otra tarea. La encuesta se ve de la siguiente manera:
  
* La segunda tarea es mucho más fácil que la primera tarea
* La segunda tarea es más fácil que la primera tarea
* La segunda tarea tiene una dificultad similar a la primera tarea
* La segunda tarea es más difícil que la primera tarea
* La segunda tarea es mucho más difícil que la primera tarea

Una vez obtenidos los resultados, se determina la diferencia de dificultad entre las tareas utilizando el promedio de las respuestas para cada contenido según el ejemplo:

[Ver tabla en presentación de Canva]

Luego se deben calcular las métricas de las tareas evaluadas por el equipo de expertos, y luego calcular la diferencia porcentual entre las métricas de las tareas del mismo contenido.

[Ver tabla en presentación de Canva]

Finalmente, se agrupan los resultados y se obtiene la siguiente tabla

Teniendo estos resultados, se deben determinar 5 intervalos de diferencias porcentuales por cada métrica, denotados como Límites Inferiores y Límites Superiores i y j, donde i corresponde al intervalo de comparación de dificultad, y j corresponde a la métrica evaluada.

Para completar la tabla, se utiliza una heurística definida para este fin, la cual consta de los siguientes pasos:

1. El límite inferior del primer intervalo de comparación de dificultad es -inf%
2. El límite superior del último intervalo de comparación de dificultad es inf%
3. A partir del primer intervalo "mucho más fácil", se calcula el límite superior restante como el mínimo entre la máxima diferencia porcentual de esa dificultad comparativa, y la mínima diferencia porcentual de la dificultad comparativa siguiente, para el caso del ejemplo, es -37.50%

[Ver Tabla en Canva]

4. El siguiente intervalo se calcula como el límite superior + 0.01%, resultando -37.49%
5. Se repiten los pasos 3 y 4 para el resto de intervalos, obteniendo la siguiente tabla:

[Ver Tabla en Canva]

Una vez que se cuenta con los intervalos de comparación de dificultad definidos, podemos utilizarlos para comparar 2 tareas en base a sus métricas según el ejemplo mostrado anteriormente. Esta información debe cargarse en el editor de Ishvel así como las métricas de las tareas calculadas editando los archivos de métricas del mismo.

## Elaborar una Tarea

### Configuración del editor

Primero se abre el editor de Ishvel y se configuran las opciones para poder elaborar una tarea. La primera opción indica cual es el contenido correspondiente a la tarea que se va a elaborar, como lo son listas, programas secuenciales, ciclos, etc. La segunda es el semestre a comparar, la cual determina con las tareas de qué semestre se va a comparar la solución de la tarea a elaborar. Por último, la tercera opción permite seleccionar si la comparación se realizará con las soluciones entregadas por los profesores, o con el promedio de las soluciones entregadas por los estudiantes.

### Redacción de la tarea

Una vez configurado el editor, se inicia con la redacción de la tarea, siguiendo el siguiente formato previamente estructurado por el editor

Contexto: Contextualización corta respecto al problema que se está enfrentando, buscando que sea real, concisa e interesante. En caso de necesitar ideas para contextualizar el problema, se puede ver la sugerencia por defecto que el framework ofrece, la cual invita al docente a abrir Google Trends ™ y ver situaciones de actualidad que pueden ser interesantes para el contexto de un problema

Instrucciones: Sección con la lista de instrucciones de lo que el estudiante debe realizar, concentrándose en que éste pueda relacionar lo que el texto dice con lo que él debe escribir en su programa. La idea de separar la sección de instrucciones de la sección de contextualización, es poder tener un espacio centrado netamente en cómo el estudiante traducirá instrucciones en lenguaje humano a lenguaje máquina, sin tener distractores o tener que pasar por algún proceso cognitivo previo del cual desprender lo que se debe hacer, como lo sería por ejemplo mezclando el contexto con las instrucciones en un sólo texto.

Ejemplos: Sección con ejemplos de la salida completa del programa. De esta manera, el estudiante tiene una guía visual de cómo debería ser su programa, y no tiene que imaginar por completo los detalles visuales de la salida del programa, para así concentrarse en programar

Recomendaciones: Sección extra con las recomendaciones que se pueden dar al estudiante para que realice un mejor trabajo, así como también, restricciones al mismo con las cuales el estudiante evite utilizar herramientas o bibliotecas que no están consideradas como parte de lo que se busca evaluar en la tarea.

### Resolución de la tarea

Luego de haber redactado la tarea, se debe resolver la misma en cualquier editor de código, hecho ésto, se debe copiar el código de la solución y pegarlo en el campo "Resolver Tarea", para que el editor calcule las métricas de software de éste.

### Sugerencias

Entonces se debe iterar sobre el enunciado leyendo las sugerencias que el editor entregue en base a las métricas calculadas y las métricas de las soluciones configuradas previamente.

### Descargar la Tarea

Finalmente, para descargar la tarea en formato PDF, se debe presionar el botón Descargar Tarea
Estos son los pasos para la elaboración de una tarea según el framework Ishvel

## Análisis de Tareas anteriores utilizando el Framework Ishvel

El editor de Ishvel también tiene una sección para revisar las métricas anteriores, ésta permite, utilizando las configuraciones de la sección derecha del editor, revisar cómo han variado las métricas de las tareas a lo largo de los semestres según la información cargada en el editor.

[Ver Métricas en Canva]

## Experimentos

Con el fin de validar el framework elaborado, se llevó a cabo la siguiente experimentación utilizando las tareas del ramo IWI-131 del primer y segundo semestre del 2022

### Cálculo de Métricas

Utilizando la herramienta *metrics-research* del framework, se calculó el promedio de las métricas de las soluciones de los estudiantes, así como también, las métricas de las soluciones de los profesores, para las tareas de ambos semestres del 2022

### Cálculo de los Intervalos de Comparación de Dificultad

Utilizando Google Forms, se consultó a un conjunto de expertos para que comparase la dificultad de las tareas del segundo semestre con las tareas del primero, obteniendo los siguientes resultados, donde 

* La tarea del segundo semestre es mucho más fácil que la tarea del primer semestre
* La tarea del segundo semestre es más fácil que la tarea del primer semestre
* La tarea del segundo semestre tiene una dificultad similar a la tarea del primer semestre
* La tarea del segundo semestre es más difícil que la tarea del primer semestre
* La tarea del segundo semestre es mucho más difícil que la tarea del primer semestre

[Ver tabla en Canva]

Luego se calcula la diferencia porcentual entre las métricas de cada una de las tareas, obteniendo los siguientes resultados:

[Ver Tabla en canva]

De estos resultados, se determinaron los intervalos de dificultad aplicando la heurística antes planteada.

### Diferencia de Dificultad entre las Tareas del 1er y 2do semestre del 2022

Luego de obtener la tabla de intervalos de dificultad comparativa, es aplican estos intervalos a las diferencias porcentuales antes calculadas, obteniendo los siguientes resultados por métrica para cada tarea:

[Ver tabla en canva]

Al comparar los resultados obtenidos por la metodología del framework con los resultados de la encuesta, se determina que la heurística aplicada coincide con la opinión de expertos en 3 pares de tareas, mientras que para el resto, los resultados no se alejan demasiado de los obtenidos por la encuesta.

### Elaboración de una Tarea con el Editor de Ishvel

Siguiendo la metodología y la plantilla ya indicada en el editor de Ishvel, se procedió a configurar el editor y redactar una tarea, indicando imágenes, fórmulas y completando el contexto, instrucciones, ejemplos y recomendaciones de la tarea, así como cualquier otro aspecto relevante para el estudiante

[Ver imagen en Canva]

Luego se desarrolla el código que resuelve la tarea y se evalúa en base a la tarea de strings del 2022-2, observando las sugerencias y la dificultad comparativa. El editor indica que la tarea elaborada es mucho más fácil que la tarea de strings del 2022-2, y entrega sugerencias para poder abordar este resultado.

Finalmente, se itera el enunciado y la solución con las sugerencias entregadas por el framework, y se lleva a los siguientes resultados, lo que nos da una tarea que mantiene la dificultad de la tarea de strings del 2022-2

[Ver Imagen en canva]

### Análisis Tareas de Listas del 2022

Con esto, es posible hacer ciertos análisis respecto de las tareas involucradas, como por ejemplo, para el caso de la tarea de Listas de IWI-131 del 2022, primer y segundo semestre

Se puede apreciar que las soluciones de las tareas de los estudiantes se acercaron bastante a las soluciones propuestas por los profesores, ésto denota que la dificultad de las tareas era la adecuada y los estudiantes comprendieron a cabalidad lo que necesitaban hacer, incluso acercándose a resolverlo casi como lo hicieron los profesores.

Algunos aspectos relevantes de este caso son:

* La tarea del primer semestre era en 2 partes, la primera constaba de resolver un cuestionario en aula y la segunda sobre el código. Ésto contextualizó adecuadamente a los estudiantes sobre lo que había que resolver, además de ser una tarea centrada en un problema real e interesante.
* El formato de la tarea del primer semestre es muy similar al propuesto en la metodología de este framework, permitiendo a los estudiantes tener mucha claridad respecto de lo que se tenía que hacer.
* Los contenidos evaluados se limitaban a lo enseñado en la UVA, y al tener los contenidos de Listas separados en 2 semanas, los estudiantes trabajaron con los contenidos frescos en su memoria.
* El tiempo estimado de desarrollo según la solución de los profesores se encontraba por debajo de 1 hora, lo que apoya enormemente a los estudiantes en la gestión de sus horarios académicos y se respeta la exigencia horaria del ramo.

Por otro lado, para el caso de la tarea de listas del segundo semestre, las métricas de las soluciones de los estudiantes difieren de las de los profesores, esto debido a que

* El tiempo estimado de solución de la tarea es de 5 horas, lo que de antemano indica que fue difícil para los estudiantes organizarse para resolverla
* La complejidad ciclomática de las soluciones de los estudiantes está por sobre la de los profesores, debido a que el formato del enunciado no se acerca para nada a los propuestos por la metodología, no quedó suficientemente claro qué es lo que se debía evaluar en el código, llevando a los estudiantes a evaluar más casos bordes de los que el enunciado realmente solicitaba.
* Según el análisis de dificultad, la tarea del segundo semestre era mucho más difícil que la del primer semestre, lo que complicó a los estudiantes en su resolución

### Análisis Tareas de Archivos del 2022

Otro caso interesante de analizar son las tareas de Archivos del 2022, particularmente, en el primer semestre.

Podemos notar que la tarea del primser semestre, las solucionse de los estudiantes se acercaron mucho a las soluciones propuestas por los profesores, excepto en la complejidad ciclomática, donde la complejidad ciclomática del código de los profesores es mucho más grande que la de los estudiantes.

* Ésto se debe a que en la solución de los profesores, se hicieron uso de funciones utilitarias, las cuales al ser bloques independientes de código, aumentan la complejidad ciclomática del mismo. Los estudiantes en cambio no hicieron uso de este tipo de funciones dado que no fueron solicitadas explícitamente, lo que da cómo resultado un código que no hace uso de reutilización de funciones y por ende entrga programas más grandes el de los profesores, como se puede apreciar en la diferencia de volumen de ambas implementaciones.

* Esta tarea al ser la última del semestre, hay un menor incentivo a ser entregada, por lo mismo es que casi la mitad de los estudiantes no hicieron entrega de esta. La falta de incentivo al estar cerrando el semestre con muchas otras responsabilidades, lleva a los estudiantes a enviar programas incompletos o que no funcionan, lo que explica por qué la dificultad de sus implementaciones es ligeramente menor a la de los profesores.

* Por último, el enunciado de esta tarea sigue un formato parecido al planteado por la metodología del framework, lo que permite a los estudiantes tener un entendimiento claro de lo que se solicita, y que llevó a que éstos generaran programas con métricas similares al desarrollado por los profesores.

Por otro lado, con respecto a la tarea del segundo semestre, se puede apreciar que pese a que la solución de los profesores mantiene métricas similares a la solución de la tarea del semestre anterior, las métricas de las soluciones de los estudiantes difieren demasiado de éstas. 

* Obviando la situación de que es la última tarea del semestre, el enunciado de la tarea requiere inferir ciertas condiciones que no están explícitamente descritas, lo que añade una carga cognitiva a los estudiantes de tener que descifrar cómo llevar a cabo esto, y que los lleva además a añadir muchas condiciones en su código que podrían no ser realmente requeridas para resolver el problema.
* Las exigencias de la tarea comprenden no sólo el manejo de archivos, si no también la elaboración de diccionarios con una estructura no trivial. La mezcla de estos 2 contenidos como exigencia para la resolución de la tarea lleva a los estudiantes a elaborar programas con un mayor volumen de código, lo que aumenta la dificultad y el esfuerzo de éstos. Si bien el aprendizaje de las UVAs es incremental y por lo tanto se pueden hacer usos de UVAs anteriores, es notorio que la complicación del código se concentró en la función que debe tanto leer archvos como generar diccionarios. De haber sido una función con la única tarea de leer archivos, la métrica de volumen de código serí0a mejor, y por consiguiente, la de dificultad y esfuerzo.
* El tiempo de solución esperado es mayor a una hora, lo que conlleva a los estudiantes a tener complicaciones con el manejo de sus horarios al tener que dedicarle tanto tiempo al ramo.

## Conclusiones

El curso de Programación de la UTFSM está muy bien estructurado, sin embargo, hay muchas mejoras que se pueden llevar a cabo en sus tareas. Las recomendaciones entregadas por el framework Ishvel a la hora de elaborar una tarea, pueden ser de mucha utilidad para combatir la frustración que una tarea puede generar en los estudiantes.

Por otro lado, la aplicación de métricas de software como herramienta de medición para la dificultad de una tarea, y para el estudio de la experiencia que tienen los estudiantes a la hora de desarrollar una tarae, fue de gran ayuda para entender ciertos aspectos en los que hay que prestar atención a la hora de elaborar una tarea, y cómo la solución de la misma entrega información importante a tener en cuenta durante este proceso.

Este estudio muestra el potencial que tienen las métricas de software para conocer la dificultad de una tarea antes de publicarla a sus estudiantes, esta retroalimentación inmediata es súmamente útil para el profesor que está redactando una tarea. Sin embargo, se requiere una mayor cantidad de datos respecto a más semestres de tareas y el análisis de sus métricas, para poder extraer así mejores conclusiones. Además de las métricas de Halstead, la métrica de complejidad ciclomática entra una interesante aproximación sobre cómo se traduce el enunciado a una tarea a la cantidad de condiciones que el estudiante tendrá que desarrollar, y cómo éstas complicarán el proceso de desarrollo de su solución, impactando en otras métricas.

El editor de Ishvel es una gran herramienta para aplicar la metodología del framework, entrega de antemano una tarea de ejemplo para acelerar el proceso de elaboración. Sin embargo, la información respecto a la dificultad que éste entrega, está limitado por la eficacia de la heurística utilizada para determinar los intervalos de dificultad comparativa, dado que ésta no ha sido afinada aún, se requiere de mayor trabajo en ella para lograr una mayor eficacia

Del mismo modo, el uso de tecnologías web que permiten ejecutar Ishvel en cualquier navegador sin necesidad de un servidor externo, facilita la distribución del framework a gran escala, pues todo está alojado en Github Pages. Por lo mismo, el framework fue publicado como código abierto, para que cualquier profesor pueda utilizarlo y añadir las métricas de sus propias tareas, lo que hace del framework una herramienta mucho más versátil y aplicable a otros cursos.

Por lo demás, en base a la validación y experimentación, es posible determinar que fue posible cumplir el objetivo general de esta memoria, creando un framework capaz de apoyar a los profesores en la elaboración de tareas de programación, utilizando una metodología y la definición de métricas que ayudan a entender la dificultad de una tarea en base a su solución. 

## Trabajo a Futuro

Como trabajo a futuro, es necesario determinar una mejor heurística para determinar los intervalos de dificultad comparativa, ya que la actual no está lo suficientemente afinada y requiere de mayor información. Del mismo modo, se deben analizar más tareas con las cuales obtener más métricas, y realizar la encuesta a grupos más grandes de expertos para ir afinando poco a poco las sugerencias del framework y los intervalos de dificultad comparativa. Con mayor información, es posible afinar mucho más la metodología del framework para el análisis de la dificultad de las tareas.

También se puede llevar a cabo un análisis sobre la experiencia del usuario con respecto al editor, para así probar en un laboratorio y obtener datos sobre la experiencia de un profesor elaborando una tarea en él, de modo tal de corregir aspectos de la interfaz, ver qué otras opciones añadir, y hacer mejoras en la metodología. 

También a futuro se puede disminuir la carga cognitiva entregada por las métricas del framework en la interfaz, reduciendo todo a una única métrica que resulte de la ponderación de las métricas ya analizadas en este trabajo, y  que entregue un valor final con el cual categorizar la tarea en cuestión. 

Queda como trabajo a futuro también la experimentación de cómo distintos valores en las métricas de las soluciones impactan en la experiencia de los estudiantes a la hora de desarrollar sus tareas, mediante encuestas que permitan agrupar los valores de las métricas, ponderarlos y finalmente extraer una única métrica de evaluación para las tareas.

## Anexos

### Heurística en caso de que falte información

Si es que no hay información suficiente para aplicar los pasos 3 y 4, se debe aplicar el siguiente algoritmo según la dificultad comparativa en la que falte:

* Si falta información para la dificultad comparativa 1:
  * Se utiliza LI2m - 0.01% como LS, si LI2m no está definido, se considera la menor diferencia porcentual de la dificultad comparativa 2 - 0.01% como límite superior
* Si falta información para la dificultad comparativa 2:
  * Se calcula LI2m como LS1m + 0.01% y LS2m como LS1m + 0.01% + abs(LI4m - LS4m)
* Si falta información para la dificultad comparativa 3:
  * Se calcula LI3m como LS2m + 0.01%
  * Se calcula LS3m como LI4m - 0.01%
* Si falta información para la dificultad comparativa 4:
  * Se calcula LI4m como LS3m + 0.01% y LS4m como LS3m + 0.01% + abs(LI2m - LS2m)
* Si falta información para la dificultad comparativa 5:
  * LI = LS4m + 0.01%, si LS4m no está definido, se considera la mayor diferencia porcentual + 0.01% como líomite inferior
  * Si ya se definió el límite inferior de la dificultad comparatida *d*, pero no hay información para el límite superior, se define LSdm = LIdm + 20, dado que 20 sería el tamaño del intervalo si todos fuesen iguales
  * Si no hay información suficiente para definir los límites de *d*, se debe seguir aplicando la heurística con el resto de dificultades comparativas hasta que hayan suficientes límites definidos.

### Cálculo de Métricas según Halstead

