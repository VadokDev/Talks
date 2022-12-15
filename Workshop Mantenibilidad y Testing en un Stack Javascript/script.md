# Workshop Mantenibilidad y Testing en un Stack Javascript

Hola!, bienvenidos sean a este Workshop sobre mantenibilidad y testing sobre un stack de Javascript. El objetivo de esta charla es demostrar de forma práctica el cómo llevar a cabo un software mantenible, testeable y dentro de un entorno full stack de Javascript.

## Mantenibilidad

Pero antes de pasar a lo práctico, hablemos de mantenibilidad. La IEEE define la mantenibilidad de un software como:

```
"La facilidad con la que un software o componente puede ser modificado para corregir fallas, mejorar su desempeño u otros atributos, o adaptarse a un entorno cambiante."
```

"En software, añadir una pista de seis carriles a un puente ferroviario se considera mantenimiento, y sería especialmente bueno si se pudiera hacer sin interrumpir el tráfico"

Fuente: Paul Stachour and David Collier-Brown. 2009. You Don’t Know Jack About Software Maintenance: Long considered an afterthought, software maintenance is easiest and most effective when built into a system from the ground up. Queue 7, 9 (October 2009), 50–55. https://doi.org/10.1145/1626135.1640399

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

### Tipos de Testing

### Consejos para Testing

### Testear antes o testear después

## Práctica

* Definir el inicio de la aplicación
* Definir el repositorio
* Definir el cliente
* Definir el caso de uso de escritura
* Definir el controlador
* Definir el caso de uso de lectura
* Definir el bootstrap
* Realizar un test unitario
* Realizar un test de integración
* Realizar un test funcional
* Instalar materialUi
* Instalar Axios
* Crear un componente de escritura
* Crear un componente de lectura (tabla)
* Crear un botón de lectura
* Crear un componente Layout de App
* Realizar un test unitario
* Realizar un test de integración
* Realizar un test funcional