# Workshop Mantenibilidad Stack Javascript

Hola!, bienvenidos sean a este Workshop sobre mantenibilidad sobre un stack de Javascript. El objetivo de esta charla es demostrar de forma práctica el cómo llevar a cabo un software mantenible, testeable y dentro de un entorno full stack de Javascript.

## Mantenibilidad

```
"En software, añadir una pista de seis carriles a un puente ferroviario se considera mantenimiento, y sería especialmente bueno si se pudiera hacer sin interrumpir el tráfico"
```

Fuente: Paul Stachour and David Collier-Brown. 2009. You Don’t Know Jack About Software Maintenance: Long considered an afterthought, software maintenance is easiest and most effective when built into a system from the ground up. Queue 7, 9 (October 2009), 50–55. [https://doi.org/10.1145/1626135.1640399](https://doi.org/10.1145/1626135.1640399)

La IEEE define la mantenibilidad de un software como:

```
"La facilidad con la que un software o componente puede ser modificado para corregir fallas, mejorar su desempeño u otros atributos, o adaptarse a un entorno cambiante."
```

Esta mantenibilidad depende de muchos factores; en general, el software debe ser fácil de entender (esto es: cómo funciona, qué hace y por qué lo hace de esa manera y no de otra), fácil de encontrar qué se necesita cambiar, y fácil de ser modificable y de validar que esos cambios no añaden bugs.

La mantenibilidad nos ayuda a ahorrar tiempo y dinero a futuro, pues a medida que van rotando quienes se encargan de desarrollar el software, el hecho de que sea mantenible será lo que permita a las nuevas personas seguir desarrollando funcionalidades. Además, a la ahora de encontrar bugs, la mantenibilidad del software también garantizará un corto periodo de análisis para encontrar el error, corregirlo, y evitar que vuelva a ocurrir en el futuro. 

Un software que no está pensado en ser mantenible siempre será más fácil y rápido de desarrollar, pero trae consigo sus costos asociados: todo este ahorro obtenido se transformará en una deuda técnica acumulada, la cual se pagará cuatriplicando los tiempos de soporte en cada bug, o el esfuerzo en seguir manteniéndolo o añadiéndole funcionalidades.

¡Más vale prevenir que curar!, hoy en día contamos con herramientas como , linters, incluso en nuestros propios editores de código, que nos ayudan a hacer un código mantenible. Además, claro, de añadir testing siempre que podamos para así tener más seguridad a la hora de continuar añadiendo cambios, Veamos un ejemplo:

## Mantenibilidad en Javascript

Todas las definiciones a continuación, se basan en la ISO/IEC 25010, la cual pueden consultar con más detalle en Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models, International Organization for Standardization, 2011.

### Analizabilidad (Analyzability)

Grado de efectividad y eficiente con la cual es posible determinar el impacto que un cambio tiene en una o más partes de un sistema, diagnosticar fallos, e identificar partes a modificar durante la modificación del mismo.

Al inicio hacemos software sin todas las funcionalidades, y a medida que éste evoluciona, puede haber una rotación de las personas que lo mantienen, lo que implica que si el código no cuenta con un buen grado de analizabilidad, será complicado para un integrante nuevo del equipo modificarlo sin considerar el impacto negativo de sus cambios, dado la dificultad de entender el código en el que trabaja.

Javascript es un lenguaje extremadamente permisivo, lo cual es un factor de suma importancia a la hora de pensar en mantenibilidad. 

Qué herramientas tenemos para mejorarlo?, principalmente forzar un estilo de programación. 

* Typescript (tipado), 
* Prettier y Linters
* Comentarios
* Documentación

Un dato curioso, es que existe evidencia empírica de que los lenguajes tipados benefician la mantenibilidad del software que los utiliza, facilitan el entendimiento de código no documentado y el arreglo de errores de tipos, sin embargo, cuando se trata de errores semánticos, se vuelve más complicado méramente porque en el desarrollo en lenguajes de tipado débil, quienes desarrollan se acostumbran a mirar diferentes archivos del sistema constantemente. No obstante, hoy en día existen distintas herramientas de análisis de código que permiten validar estos errores semánticos de manera automática, justamente gracias a que el lenguaje en que está el sistema es tipado

Fuente: Hanenberg, S., Kleinschmager, S., Robbes, R. et al. An empirical study on the impact of static typing on software maintainability. Empir Software Eng 19, 1335–1382 (2014). https://doi.org/10.1007/s10664-013-9289-1

Una de las méjores métricas que tenemos para analizar la analizabilidad es la Complejidad Ciclomática.

### Modificalidad (Modifiability)

Grado con el cual se puede efectivamente modificar un sistema sin introducir defectos o degradar su calidad.

A medida que el software crece, vamos comprometiendo su modificabilidad y testeabilidad a cambio de integrar nuevas funcionalidades, dejando deuda técnica y avanzando con la entrega de valor a los stakeholders. En ocasiones podemos vernos en la necesidad de realizar enormes refactorizaciones de código, sin que éstas generen algún valor notable a nuestros stakeholders

Qué herramientas tenemos para mejorarlo?

* Linters
* Tests
* Typescript
* Documentación
* Comentarios

### Modularidad (Modularity)

Grado con que un sistema está compuesto de componentes independientes, tal que un cambio en uno de ellos tiene un impacto mínimo en los demás.

Un alto grado de modularidad nos facilita la tarea de testear individualmente cada componente, lo que aumenta su modificabilidad y testeabilidad. Javascript cuenta con un soporte nativo parcial para la inmutabilidad de sus datos, lo que significa que si bien podemos definir variables constantes, las propiedades de sus objetos siempre podrán ser manipuladas, lo que nos puede llegar a tener partes de la aplicación donde un objeto es modificado a medida que es transferido desde una parte de la aplicación a otra, y en el caso de nuestros módulos, aumentar el impacto que tiene en el resto de la aplicación realizar una modificación en ellos.

* Typescript
* Forzar inmutabilidad con linters
* Inyección de dependencias

### Reusabilidad

Grado con que una parte del sistema puede ser utilizado en otros sistemas, o bien, o en construir otras partes del mismo

La reusabilidad es algo que en el ecosistema de javascript es difícil de lograr, principalmente porque una aplicación puede requerir una cantidad denorme de dependencias, especialmente aplicaciones grandes, más aún, no se puede garantizar que cada una de estas dependencias (ni las dependencias de las dependencias), mantengan información útil como documentación de calidad, comentarios o uso del tipado correspondiente para Typescript. 

Una parte del sistema puede ser reutilizada si su interfaz es definida correctamente y usada a lo largo del mismo (o de otros sistemas), por lo mismo, dado que las interfaces de javascript son sólo azúcar sintáctica, hoy en día los esfuerzos están concentrados en crear los archivos de tipado necesarios para las dependencias del ecosistema de javascript, de modo tal de poder ser utilizados en un sistema con Typescript.

Por otro lado, la mejor forma de lograr un alto grado de reusabilidad, es tratar de minimizar lo más posible la cantidad de dependencias utilizadas en el proyecto, algo que nuevamente, es difícil de lograr en el ecosistema de javascript por su propia naturaleza.

## Testeabilidad

Grado de efectividad con la que podemos establecer criterios de prueba para un sistema, y de las pruebas que pueden realizarse para determinar si esos criterios se cumplen.

La testeabilidad tiene 2 aspectos claves, qué tan fácil es definir lo que vamos a probar, y la capacidad que tenemos como equipo para crear y ejecutar aquellas pruebas. Podemos resolver el primer aspecto mediante un buen trabajo con los roles correspondientes, para llegar a una definición concreta de los casos de uso a validar, mientras que para el segundo aspecto, en Javascript contamos con diversas herramientas que facilitan la automatización de pruebas. Para el caso de este workshop, nuestra herramienta designada será Jest, y lo que vamos a validar es la creación de testing unitario y testing funcional en base al caso de uso de nuestra aplicación

Mientras más partes de nuestro código cubramos con sus respectivas pruebas, podremos implementar cambios y mejoras con mucha más confianza ya que ante cualquier problema que generemos, los tests serán nuestra primera herramienta para detectarlos.

### Complejidad Ciclomática

La complejidad ciclomática es una métrica que define el número de posibles caminos de ejecución dentro de un bloque de código, mientras más alto es este valor, mayor cantidad de ramificaciones tendrá nuestro código, y por lo tanto, será mucho más complejo de analizar.

Para calcular la complejidad ciclomática de nuestro código, necesitamos visualizar el grafo de ejecución. Cada línea de código es un nodo del grafo, y de cada nodo saldrá una arista al nodo inmediatamente siguiente según la línea de ejecución, es decir, si un nodo es una condición, entonces podría salir una arista desde ese nodo hacia la primera línea de código dentro de la condición en caso de que se cumpla, o bien, hacia la primera línea de código fuera de la condición en caso contrario. El valor de la complejidad ciclomática será el número de aristas menos el número de nodos más el doble de la cantidad de componentes conexas. 

E = Aristas
N = nodos
P = número de componentes conexas

CC = E - N + 2P

Ejemplos de complejidad ciclomática:

[ejemplos]

## Resumen

Fuente: Tupeli, Pauli (2020). Ensuring maintainability of JavaScript web applications. https://trepo.tuni.fi/handle/10024/123717

## Puesta en Práctica

Para este Workshop, trabajaremos con una aplicación muy básica con 2 casos de uso: 

* Publicar mensajes desde una interfaz
* Recibir mensajes desde una interfaz

## Stack de Trabajo

Backend:
* Mini API en Python

Frontend:
* Create React App - Scaffold
* Axios - Cliente HTTP

Testing:
* Jest

Herramientas de Mantenibilidad:

* Eslint
* Prettier
* SonarQube

## Mostrar la aplicación funcionando, cargar mensajes y leerlos

## Pasos para el workshop

* Mostrar la versión básica del proyecto
* Analizar algunas de las fallas y métricas
* Experimento 1: Añadir más botones, mostrar que la complejidad ciclomática sube, y que el código se vuelve menos manipulable
* Discusión: En teoría, cada botón tiene una función distinta... verdad ?, cada una de estas añade componentes al cálculo de la complejidad ciclomática.
* Realizar un test, mostrar lo que falta por validar.
* Discusión: se considera realmente unitario validar todo este componente?
* Discusión: ¿Es este componente modularizable?, ¿Puede reutilizarse?
* Discusión: ¿Qué pasaría si ahora tuviésemos que añadir autentificación a las llamadas de nuestra API?
* Separemos la capa de persistencia y lectura de la capa de presentación
* Crear un repositorio, mover al repositorio las funciones
* Discusión: Cada parte de la aplicación deberia tener su propia instancia del repositorio?

## Explicación parte no práctica

Vamos a continuar mejorando la mantenibilidad de esta aplicación, sin embargo, en honor al tiempo utilizaremos la presentación en vez de programación en vivo.

Una de las cosas que podemos haxcer para mejorar la mantenibilidad de esta aplicación, es aplicar algún sistema con el cual poder separar los componentes del mismo. Para este caso, voy a tomar inspiración de lo que sería el Diseño Atómico, no lo vamos a aplicar al pie de la letra, pero sí vamos a repasar un poco como funciona, y las ventajas que podemos obtener tanto de aplicarlo, como de aplicar otros sistemas para separar los componentes de nuestra aplicación.

## Diseño Atómico

El diseño atómico es un sistema de diseño que nos permite organizar nuestros nuestros componentes. Estos se separan en:

* Átomos: La unidad de construcción básica de componentes, pueden ser inputs, textos, colores, etc.
* Moléculas: Cuando combinamos átomos, generamos componentes más grandes los cuales son llamados moléculas. Éstas agrupan átomos para volverse unidades funcionales, es decir, se vuelven mucho más tangibles y funcionales de cara a nuestra interfaz. Por ejemplo, una imagen con texto y fondo generan una caja de información, mucho más útil que los 3 por separados.
* Organismos: Teniendo moléculas, ya podemos construir secciones más complejas de nuestra interfaz, como lo sería una lista de contactos. Un organismo es entonces un grupo de moléculas unidas para formar un componente más complejo.
* Plantillas: Las plantillas agrupan organismos al mismo tiempo que les dan contexto dentro de nuestra interfaz, nos permiten posicionar todo para que tenga un sentido, y darnos el paso final para generar el componente más grande de este sistema. Una plantilla será le organización final con la cual presentar al cliente la idea de diseño.
* Paginas: Una pagina es una instancia de una plantilla, es decir, dejamos de hablar de cómo posicionaríamos los elementos, y generamos vistas concretas con la información e imágenes correspondientes que suponíamos colocar a medida que generábamos plantillas. Nuestra pagina será finalmente lo que el usuario de nuestra aplicación verá.

Veamos cómo resultaría aplicarlo en nuestra aplicación. Para ello, observemos el siguiente diagrama: Como podrán notar, tenemos moléculas de mensajes, que vendrían siendo los botones que presionamos cuando queremos publicar algo. Estrictamente hablando, un botón podría ser méramente un átomo, pero para no entrar en complicaciones, lo veo como molécula porque a futuro podría componerse de más cosas, como dije antes, vamos a inspirarnos en diseño atómico, pero no a seguirlo al pié de la letra.

Ésta molécula, si la colocamos por cada mensaje de los que tenemos disponibles para publicar, generamos un organismo el cual llamaremos Publish Organism. Éste entonces será una mitad de nuestra interfaz, y se encargará méramente de agrupar nuestras moléculas de mensajes a publicar.

Por el otro lado, tenemos nuestra molécula Read Button, la cual es el botón con el cual llamamos a la API de manera manual, y obtenemos los mensajes. Ésta formará parte del organismo Read Organism, el cual a su vez, tendrá también moléculas de los mensajes que estemos leyendo, es decir, se compondrá de las moléculas Read Button y Message Molecule, ya que en este caso, éstas moléculas las vamos a reutilizar de modo tal de que en el organismo de Publicación, llamen a la API, y en el organismo de lectura, no hagan nada.

## Message Molecule

Lo primero que vamos a crear es una molécula de mensaje, estrictamente hablando, un botón podría ser méramente un átomo, pero para no entrar en complicaciones, lo veo como molécula porque a futuro podría componerse de más cosas, como dije antes, vamos a inspirarnos en diseño atómico, pero no a seguirlo al pié de la letra.

Este componente recibirá 2 propiedades, recordar que si bien estamos utilizando React, esta forma de asignar propiedades a un componente no es estrictamente de React, si no que pueden verla como una asignación genérica de atributos a sus componentes, independiente de si están utilizando algún framework para gestionar su renderizado.

### Propiedad Content

La propiedad content de este componente nos permite indicar qué texto mostrará el botón

### Propiedad onClickHandler

La propiedad onClickHandler nos permite indicar qué hará éste botón cuando es presionado, notar que si la omitimos, el botón no hará nada en cuanto se le haga clic, y por lo tanto, podemos reutilizar este componente tanto para los mensajes a publicar, como los mensajes recibidos.

## Publish Organism

Ahora que tenemos nuestra molécula de mensaje, vamos a generar nuestro primer organismo, éste será el Publish organism que vimos anteriormente en el diagrama. Vamos a utilizar el Stack de Material UI, para apilar nuestras moléculas de mensajes hacia abajo. Entendiendo esto, desmenucemos las propiedades de este componente.

### Propiedad messages

La propiedad mensajes contiene un arreglo con los mensajes que se van a renderizar para publicar, éstos contienen sólamente la propiedad contenido, pero a futuro podrían tener más cosas. 

### Propiedad sendMessageHandler

El organismo va a recibir por propiedades la función encargada de enviar los mensajes a la API, de modo tal de no acoplar esta lógica al organismo, si no dejarlo en un componente de más alto nivel.

Para renderizar los mensajes, se iterará sobre esta lista y se mostrará una molécula de mensaje por cada uno de ellos, entregando sus propiedades correspondientes, en el onClickHandler será una función que ejecutará el sendMessageHandler y el contenido a mostrar, será el contenido del mensaje en el que se está iterando.

### 

## Conclusiones

Existen muchas maneras de hacer software mantenible, la que se expresa en este workshop es una de ellas y como siempre, todo tiene sus pros y contras, hay cosas que les van a generar ruido, y seguramente habrán partes que les hará más sentido hacer las de una forma por sobre otra, por lo mismo, es importante que más allá de encontrar la Bala de Plata, nos preocupemos de integrar la mantenibilidad en nuestro día a día, e implementemos formas de medirla, en nuestros pipelines de despliegue, en nuestra metodología de desarrollo, en todo. Para así, ser siempre consientes de que estamos creando un producto que a futuro será manejado por otras personas y que seguirá creciendo. Ahora es cuando tenemos que tomar una manera de trabajar que a futuro no nos haga arrepentirnos de la forma en la que decidimos maniobrar la mantenibilidad de nuestro software.