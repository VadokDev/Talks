# Artesanía de Software: Una mirada a su manifiesto desde la historia y la ingeniería

Sandro Mancuso es autor del libro The Software Craftsman: Professionalism, Pragmatism, Pride

## ¿Qué palabras describen qué es la Ingeniería de Software?

Wordcloud

## ¿Qué palabras describen qué es la Artesanía de Software?

Wordcloud

## ¿Qué es la Artesanía de Software?

Iniciemos por qué no es:
* Código hermoso
* TDD
* Grupo exclusivo de personas
* Tecnologías o metodologías específicas
* Certificaciones
* Religión

## Una pequeña historia

Sandro Mancuso llegó a una nueva empresa haciendo un nuevo trabajo, él era joven y consiente de sus habilidades, todo iba bien hasta que un día escuchó sobre el "equipo de arquitectura", responsable del núcleo del sistema y de desarrollar toda la infraestructura utilizada por el negocio. Éste equipo estaba compuesto por lo mejor de lo mejor, y liderado por Namur, quien además de todo el trabajo de gestión, era un excelente desarrollador. Todos hablaban del increíble código y trabajo que este equipo hacía, y ahí es donde Sandro quería estar, trabajando con los mejores, así que conversó con su manager para llevar a cabo el cambio, y con Namur para ver si es que era posible entrar en su equipo.

Luego de una entrevista, Namur le dio el pase a Sandro para trabajar en el equipo de arquitectura, y entonces le asignó su primera tarea a Sandro. Él, muy feliz, comenzó a dar lo mejor de sí para demostrar que merecía pertenecer a este equipo. Pese a que la idea era revisar el trabajo en 4 días, Sandro lo terminó en 1, sintiéndose como el dios del desarrollo al haber logrado semejante hazaña en un código ajeno y tan complejo.

Sandro corrió a la oficina de Namur y con mucha emoción dice "Lo logré!, está listo y funcionando", a lo que Namur calmadamente responde "Hacer las cosas funcionar es lo mínimo que se espera de alguien a quien se le paga por ello, el hecho de que esté finalizado, implica que funciona". Fue como un balde frío de agua, acto seguido, Namur abrió el único archivo .pas (Delphi) que contenía absolutamente todo el código, y le ofreció a Sandro sentarse a su lado para que revisaran el código juntos.

Fue una experiencia terrible, cada 5 líneas de código Namur decía: "Sabes qué pasa cuando asignas y liberas memoria?, puedes ver aquí ?, estás asignando memoria en un método y liberándola en otro, esto es un potencial memory leak, ¿sabes sobre acomplamiento temporal ?, puedes ver este bloque de código de aquí ?, si hubieses pensado un poco más, podrías reducir estas 8 líneas a 2, ¿sabes lo que pasa con un try/catch tan grande?, ¿qué me dices sobre el nombre de esta variable y método, qué significan?, ¿si quiera pensaste en tus colegas, cuando necesiten cambiar este código, no tendrán suficiente información o contexto como el que tienes tú ahora?, ¿cómo te sentirías si no supieras nada acerca de esta parte de código que tienes que mantener?, ¿y qué pasa con este bit hardcodeado aquí?, ¿si quieres has pensado que si queremos cambiar donde apunta, tendríamos que abrirlo, cambiarlo, recompilarlo y redesplegar la aplicación completa?, ¿por qué tienes esta pieza de código duplicada por todo el lugar? Wow!, este es un gran método, ¿sabes cuando tendríamos que almacenar en nuestras cabezas si todos los métodos fueran así de grandes?, ¿Qué tal si lo haces más pequeño y lo nombras de acuerdo a lo que hace?", y así seguía y seguía...

Luego de preguntar a Sandro si entendió todo y si cree que podría hacer este código mejor, Sandro asintió y Namur borró todo su código, indicándole que aún le quedaban 3 días. Antes de que Sandro saliera enojadísimo del lugar, Namur dijo: "El cómo se hace es tanto igual de importante que el sólo hacerlo".

- Quiero escuchar a alguien que me cuente cómo se sentiría de haber vivido esta experiencia

Y es que Namur pasó 1 hora con Sandro, explicándole, dándole ejemplos, sugerencias e ideas respecto de cómo hacer su código mejor, así Sandro luego de calmarse se dio cuenta que desde que escribió su primera línea de código, es la primera vez que alguien se sienta con él y le ayuda a que su código sea mucho mejor.

## Una mirada desde la Historia

Historia de la Artesanía de Software.

* En 1992 Jack W. Reeves sugiere que el desarrollo de software es más una artesanía que una práctica de ingeniería
* En 1992, Andy Hunt y Dave Thomas publican el libro "The Pragmatic Programmer: From Journeyman to Master", introduciendo la mayoría de ideas utilizadas en el que sería el movimiento de la Artesanía de Software
* En 2002, Ken Auer organizó un evento sobre aprendizaje de software de verano, invitando a distinguidos referentes del mundo del software como Pete McBreen, Ron Jeffries y Robert Martin (Uncle Bob). Este evento marcó un hito ya que se intentó formar una comunidad en torno al aprendizaje de software. 
* Esta comunidad no prosperó, pero sí generó impacto en la empresa de Robert Martin (Uncle Bob), donde comenzaron a contratar aprendices, no había mucha formalidad en el proceso, pero mucha gente entró como aprendiz a Object Mentor
* En el 2006, Micah Martin y Paul Pagel crearon 8th Light como la encarnación de los valores de la Artesanía de Software, ésta compañía llevó a cabo un programa para contratar a través de aprendices y cultivar su talento. 8th Light sólo empleaba artesanos de software, no desarrolladores.
* Del mismo modo, otras empresas como Obtiva comenzaron a ofrecer programas de aprendices, generando de a poco cada vez más impacto respecto de este movimiento.
* La agilidad comienza a meter ruido, llegando con muchas disciplinas, metodologías y técnicas que dieron un vuelco en la industria del desarrollo de software. Para ese entonces, no era necesaria una verdadera artesanía de software, ya que todo problema de la industria podía resolverse con metodologías ágiles.
* Agosto del 2008, Robert Martin (Uncle Bob) propuso en una conferencia de agilidad un quinto valor: "Artesanía por sobre basura", que más adelante propuso como "Artesanía por sobre ejecución". 
* Ese mismo año, Robert Martin publicó los libros "Clean Code: A Handbook of Agile Software Craftsmanship" y en 2011 "The Clean Coder: A Code of Conduct for Porfessional Programmers", los cuales han sido 2 de los más influyentes libros en el círculo de la artesanía de software.
* Seguimos en 2008, las cosas en el mundo de la agilidad no van como se esperaban, principalmente por la desviación que hubo de las metodologías ágiles técnicas como la Programación Extrema (Extreme Programming), y la comercialización de la misma.
* Ya en diciembre, Micah Martin y Paul Pagel organizan un nuevo evento sobre aprendizaje de software de verano, con el fin de ponerle una cara pública a la Artesanía de Software. Éste se llevó a cabo con una serie de grandes exponentes como Robert Martin, Brian Marick, Corey Haines, Dave Hoover, Doug Bradbure y David Chelimsky
* La discusión continúa en internet, hasta marzo del 2009 donde finalmente se presentan las conclusiones respecto de todo el debate, publicando así el primer Manifiesto de la Artesanía de Software.
* De a poco este movimiento empieza a cruzar fronteras, organizando seminarios y publicando libros sobre la artesanía de software alrededor de todo el mundo
  * Colocar aquí información sobre:
    * International Software Craftsmanship Conference en London 2009
    * Aspiring Software Craftman organizado por Adewale Oshineye
    * Enrique Comba publicó The Wandering Book, un libro que viabaja de artesano a artesano, permitiéndole escribir sus pensamientos con respecto al movimiento. Lamentablemente el libro se perdió, pero aún existe información sobre el mismo en algunos blogs.
    * Octubre 2009, Dave Hoover y Adewale Oshineye publican "Apprenticeship Patterns: Guidance for the Aspiring Software Craftsman", inspirando a cientos de profesionales a alcanzar la maestría de su profesión
    * Otras conferencias de Software Craftsmanship a lo largo de EEUU, Reino Unido, Alemania
* Incluso, en abril del 2009, 8th Light y Obtiva llevaron a cabo un intercambio de artesanos, para así aprender mútuamente sobre las prácticas de ambas empresas, una experiencia que según quienes participaron fue simplemente fenomenal para aprender y enseñar.
* Nacen comunidades sobre la Artesanía de Software
  * Colocar aquí información sobre:
    * Agosto del 2010 David Green y Sandro Mancuso (autor del libro The Software Craftmanship) fundan la Comunidad de Artesanía de Software de London (LSCC).
    * 2011, Se funda SoCraTes en Alemania, la Conferencia de Artesanía y Testing de Software, así como también 6 comunidades de artesanía de software, que al día de hoy ya son 15
    * Octubre del 2011, Comunidad de Artesanía de Software de Paris
    * La LSCC es la más grande del mundo con más de 2000 desarrolladores, siendo un modelo a seguir para distintas comunidades.

## Manifiesto 

¿Por qué un manifiesto?, Corey Haines responde: "Al convertirnos en una comunidad que se hace oír, publicar un manifiesto y empezar a trabajar en el establecimiento de principios y escuelas de pensamiento concretas, estamos creando una luz que los nuevos desarrolladores pueden ver. Aquellos que estén realmente interesados podrán encontrarnos fácilmente, hablar con nosotros sobre aprendizajes, conocer empresas que participan activamente en actividades de artesanía de software. En algunos casos, esto les introducirá antes en estas ideas, con la esperanza de ahorrar a algunos las frustraciones a las que pueden enfrentarse en una situación diferente

[Manifiesto](http://manifesto.softwarecraftsmanship.org/)

Como aspirantes a Artesanos del Software estamos elevando el listón de desarrollo de software profesional practicando y ayudando a otros a aprender el oficio. A través de este trabajo hemos llegado a valorar:

* No sólo software que funciona,
  * sino también software bien diseñado
* No sólo responder al cambio,
  * sino también agregar valor constantemente
* No sólo individuos e interacciones,
  * sino también una comunidad de profesionales
* No sólo colaboración de clientes,
  * sino también asociaciones productivas

Es decir, en la búsqueda de los elementos de la izquierda, hemos encontrado indispensables los elementos de la derecha.

"Elevando la barra de desarrollo" es una excelente forma de resumir la esencia de la Artesanía de Software. El manifiesto resume los valores, frustraciones y aspiraciones de desarrolladores muy experimentados y talentosos. Para ello,s los proyectos deben dejar de fallar por un mal manejo, procesos mal definidos, y definitivamente, por código mal escrito.

Los desarrolladores están tomando en sus manos el asunto y están intentando cambiar como es que la industria ve el desarrollo de software. 

## No sólo software que funciona, sino también software bien diseñado

Imaginen una aplicación de hace 5 años sin documentación, tests, miles de clases y ningún desarrollador veterano en ella. ¿Qué les provocaría ser responsables de hacerle algún cambio? pues miedo..., miedo de saber las implicaciones que pueden tener causar un error, y es que si lo miramos desde cierta perspectiva, es software que funciona, pero és esto suficiente?

El código debe ser mantenible y predecible, de manera de no tener miedo a la hora de hacerle cambios, y como desarrolladores, debemos hacerle el quite al miedo de cambiar una aplicación en pos de hacerla mejor. El desarrollo guiado por tests, un diseño simple y expresar el lenguaje de negocio en código son las mejores formas de mantener un código sano y bien elaborado.

## No sólo responder al cambio, sino también agregar valor constantemente

Los proyectos de software son carísimos, y la única razón por la que una empresa invertiría tanto en ellos, es para ganar dinero, con esto en mente, nuestro trabajo es ayudarles a lograrlo. Cuando se habla de añadir valor constantemente, se refiere a hacer que mientras más grande el software se haga, más beneficios le entregue a la empresa, manteniéndolo extensible, limpio, testeable y mantenible, logrando así que a medida que este envejezca, se haga cada vez más valioso, y no un dolor de cabeza.

Como regla de oro, siempre hay que dejar el código más limpio que como lo encontramos, el software de alta calidad debe ser la primera prioridad. De otro modo, una aplicación que debe ser reescrita cada cierta cantidad de años, sólo se vuelve un pésimo retorno en la inversión de la empresa. La mayoría de veces, la decisión de reescribir una aplicación, nace del hecho de lo prohibitivos que son los costos de mantenerla.

## No sólo individuos e interacciones, sino también una comunidad de profesionales

Compartir y mentorear son el corazón de la artesanía de software, pues somos responsables de preparar a las nuevas generaciones de artesanos. Un desarrollador no puede ser un artesano de software si considera que la artesanía es sobre elitismo, pues enseñar y aprender de los demás, es por lejos la mejor forma de mejorar para uno mismo. Escribir blogs, dictar charlas, contribuír al código abierto, hacer código público, participar de comunidades locales y, de lo más importante, hacer pairing con otros desarrolladores para contribuír a nuestro ecosistema.

Buenos desarrolladores buscan trabajar con buenos desarrolladores y en buenas empresas, pero un buen artesano de software busca trabajar con personas que puedan ayudarle a llegar más lejos.

## No sólo colaboración de clientes, sino también asociaciones productivas



## Qué piensa la ingeniería al respecto? 

La ingeniería de software prometía un conjunto de prácticas profesionales para el desarrollo de software como las vistas en otras disciplinas, como por ejemplo el manejo de proyectos, diseño y planificación, control de procesos, etc. Todo esto de la mano de ver el software como un producto de manufactura, lo cual tiene sentido en otras disciplinas ya que el diseño y trabajo previo de cara a resolver algo, tiene un fuerte respaldo en base a los fundamentos de la disciplina, en cambio, en el software ésto no suele funcionar así, más aún, pese a que quienes programan son quienes hacen efectivamente el software, éstos terminand devaluados por la ingeniería de software dado que no están considerados como parte del diseño a lo grande de un software antes de empezar a desarrollarlo.

La artesanía de software es una reacción directa a esta situación, concentrándose en la creación del software como tal, llegando incluso a cuestionar si realmente hace sentido ver el software como una "ingeniería". Más aún, si pensamos que el objetivo final del código es que funcione, tiene sentido pensar en crear código de calidad desde un inicio, lo que respalda la idea de verlo como una artesanía. El código puede construirse en base a la experiencia de expertos, quienes guíen a la comunidad a crear código cada vez mejor, a su vez, podemos complementar este procreso de la mano de la agilidad para crear software de alta calidad utilizando un enfoque centrado en la creación del software, negando este ímpetu de la ingeniería respecto a poner las actividades de diseño a gran escala en primer lugar.

Si tomamos la ingeniería de construcción como ejemplo, podemos notar que una verdadera disciplina de ingeniería combina la artesanía ancestral de estructuras con los fundamentos teóricos de las investigaciones más recientes, de esta manera, es posible enfrentar de manera metodológica aquellos problemas de esta disciplina, incluso cuando se encuentran fuera de la experiencia de los ingenieros. Y en base a esto, es que la ingeniería de software no sería entonces una ingeniería después de todo.

## ¿Entonces... qué nos falta?

Nace la necesidad de una nueva ingeniería de software construída sobre la experiencia de la artesanía de software, tomando todo su entendimiento como un fundamento que puede ser utilizado para educar y apoyar a las nuevas generaciones de profesionales. ¿Pero cómo logramos eso?

De aquí es donde nace la iniciativa SEMAT (Software Engineering Method and Theory), la cual concentra un esfuerzo internacional de cara a construir una ingeniería de software que haga conversar la artesanía (métodos) con la construcción de fundamentos (teoría), buscando así completar este nuevo paradigma de ingeniería de software.

## Conclusión 

Y ya para terminar, hemos ahondado en el manifiesto de la artesanía de software, dándole una mirada tanto desde su historia como desde su impacto en la ingeniería, gracias a todos estos sucesos, hoy en día podemos encontrarnos una enorme comunidad de profesionales, quienes día a día contribuyen a esta labor con su experiencia y son parte de esta nueva "refundación" de la ingeniería de software, o tal véz, como dijo Ivar Jacobson y Ed Seidewitz, su verdadera primera fundación.

## Bibliografía

* Ivar Jacobson and Ed Seidewitz. 2014. A New Software Engineering: What happened to the promise of rigorous, disciplined, professional practices for software development? Queue 12, 10 (October 2014), 30–38. https://doi.org/10.1145/2685690.2693160
* Mancuso, S. (2014). Software Craftsman: Professionalism, Pragmatism, Pride (Robert C. Martin Series) (1st ed.). Prentice Hall.