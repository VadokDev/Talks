# Workshop Mantenibilidad y Testing en un Stack Javascript

Hola!, bienvenidos sean a este Workshop sobre mantenibilidad y testing sobre un stack de Javascript. El objetivo de esta charla es demostrar de forma práctica el cómo llevar a cabo un software mantenible, testeable y dentro de un entorno full stack de Javascript.

Para este Workshop, trabajaremos con una aplicación muy básica con 2 casos de uso: 

* Publicar mensajes desde una interfaz
* Recibir mensajes desde una interfaz

## Stack de Trabajo

Backend:
* NodeJS - Entorno de ejecución
* Express - Framework HTTP
* KafkaJS - Cliente Kafka

Frontend:
* Create React App - Scaffold
* Axios - Cliente HTTP

Testing:
* Jest

## Mantenibilidad

Pero antes de pasar a lo práctico, hablemos de mantenibilidad. La IEEE define la mantenibilidad de un software como:

```
"La facilidad con la que un software o componente puede ser modificado para corregir fallas, mejorar su desempeño u otros atributos, o adaptarse a un entorno cambiante."
```

Esta mantenibilidad depende de muchos factores; en general, el software debe ser fácil de entender (esto es: cómo funciona, qué hace y por qué lo hace de esa manera y no de otra), fácil de encontrar qué se necesita cambiar, y fácil de ser modificable y de validar que esos cambios no añaden bugs.

La mantenibilidad nos ayuda a ahorrar tiempo y dinero a futuro, pues a medida que van rotando quienes se encargan de desarrollar el software, el hecho de que sea mantenible será lo que permita a las nuevas personas seguir desarrollando funcionalidades. Además, a la ahora de encontrar bugs, la mantenibilidad del software también garantizará un corto periodo de análisis para encontrar el error, corregirlo, y evitar que vuelva a ocurrir en el futuro. 

Un software que no está pensado en ser mantenible siempre será más fácil y rápido de desarrollar, pero trae consigo sus costos asociados: todo este ahorro obtenido se transformará en una deuda técnica acumulada, la cual se pagará cuatriplicando los tiempos de soporte en cada bug, o el esfuerzo en seguir manteniéndolo o añadiéndole funcionalidades.

¡Más vale prevenir que curar!, hoy en día contamos con herramientas como Sonarqube, linters, incluso en nuestros propios editores de código, que nos ayudan a hacer un código mantenible. Además, claro, de añadir testing siempre que podamos para así tener más seguridad a la hora de continuar añadiendo cambios, Veamos un ejemplo:

## Testing

### Tipos de Testing

### Consejos para Testing

### Testear antes o testear después

## Práctica

* Levantar un docker-compose con kafka
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