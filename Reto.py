#Treasure quest.
#Programa/Juego creado por Ángel Flores Bermúdez.
#Programa/Juego de Rol que planea mejorar la comprensión lectora.

import random
import shelve
import sys

hp=100
puntos=0


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Todas las preguntas con su respuesta correspondiente.
RelacionPreguntas={'''El barquito cabeceó, se ladeó, volvió a enderezarse en medio de traicioneros remolinos y
continuó su marcha por Witcham Street hacia el cruce de ésta y Jackson. El semáforo de la
esquina estaba a oscuras y también todas las casas, en aquella tarde de otoño de 1957. Llovía sin
cesar desde hacía una semana y dos días atrás habían llegado los vientos. Desde entonces, la
mayor parte de Derry había quedado sin corriente eléctrica y aún seguía así.

Teniendo en cuenta el texto anteror. ¿Cuál es el ambiente en Derry?''':'Lúgubre',
#2
'''George fue en busca de esas cosas. Oyó que su madre seguía tocando el piano, pero ya no
era Para Elisa, sino algo que no le gustaba tanto, algo que sonaba seco y alborotado; oyó la lluvia
azotando las ventanas de la cocina. Ese sonido era reconfortante, pero no así la idea de bajar al
sótano. No le gustaba el sótano ni le gustaba bajar por sus escaleras porque siempre imaginaba
que allí abajo, en la oscuridad, había algo. Era una tontería, por supuesto, lo decía su padre, lo
decía su madre, y, aún más importante, lo decía Bill, pero aun así...

Teniendo en cuenta el texto anterior. ¿Por qué George cree que hay algo en el sótano?''':'Superstición',
#3                  
'''No le gustaba siquiera abrir la puerta para encender la luz, porque temía (era algo tan
estúpido que no se atrevía a contárselo a nadie) que, mientras tanteaba en busca del interruptor,
una garra espantosa se posara sobre su muñeca... y lo arrebatara hacia esa oscuridad que olía a
suciedad, humedad y hortalizas podridas

Teniendo en cuenta el texto anterior. ¿Cómo se le llama a lo que siente ?''':'Pavor',
#4
'''Aquella mañana abrió la puerta para tantear interminablemente en busca del interruptor,
sujetando el marco de la puerta con la fuerza de siempre, los ojos apretados, la punta de la lengua
asomando por la comisura de los labios como una raicilla agonizante buscando agua en un sitio de
sequía. ¿Gracioso? ¡Claro! \"Mira a Georgie ¡Georgie le tiene miedo a la oscuridad! ¡Vaya tonto!\"
                   
Teniendo en cuenta el texto anterior. ¿Por qué la gente se burlaría de Georgie?''':'Degradar',
#5
'''George rió. El miedo había desaparecido, se había desprendido de él tan fácilmente como
una pesadilla se desprende del hombre que despierta con la piel fría y el aliento agitado
palpándose el cuerpo y mirando alrededor para asegurarse de que nada ha ocurrido en realidad:
olvida la mitad cuando sus pies tocan el suelo; las tres cuartas partes, cuando sale de la ducha y
comienza a secarse con la toalla; y la totalidad cuando termina el desayuno. Desaparecida por
completo... hasta la próxima vez, cuando en el puño de la pesadilla todos los miedos volverán a
recordarse
                   
Teniendo en cuenta el texto anterior. ¿Qué siente George después de ese proceso?''':'Alivio',
#6
'''El piano reinició Para Elisa. Bill el Tartaja no olvidaría jamás esa pieza, y aún muchos años
después no podría escucharla sin que se le pusiera carne de gallina, el corazón le daba un vuelco y
recordaba: \"Mi madre estaba tocando eso el día en que murió Georgie.\"


Teniendo en cuenta el texto anterior. ¿Qué siente Bill al escuchar \"Para Elisa\"?''':'Pánico',
#7
'''Forzó el paso y, por un momento, pareció que iba a alcanzarlo. Pero George resbaló y cayó
despatarrado con un grito de dolor. Desde su nueva perspectiva, a la altura del pavimento, vio que
el barco giraba en redondo dos veces, atrapado en otro remolino, antes de desaparecer.
 —¡Mierda y mierda! –volvió a chillar, golpeando el pavimento con el puño.
Eso también le dolió, y se echó a sollozar. ¡Qué manera tan estúpida de perder el barco!

Teniendo en cuenta el texto anterior. ¿Qué siente George después de perder el barco?''':'Tristesa',
#8
'''Se dirigió hacia la boca de tormenta y allí se dejó caer de rodillas, para mirar el interior. El
agua hacía un ruido hueco al caer en la oscuridad. Ese sonido le dio escalofríos. Hacía pensar en...
 —¡Eh! –exclamó de pronto, y retrocedió.
Allí adentro había unos ojos amarillos. Ese tipo de ojos que él siempre imaginaba, sin verlos
nunca, en la oscuridad del sótano. \"Es un animal –pensó–; eso es todo: un animal; a lo mejor un
gato que quedó atrapado...\"

Teniendo en cuenta el texto anterior. ¿Qué sintió George después de escuchar la exclamación?''':'Sorpresa',
#9
'''De todos modos, estaba por echar a correr a causa del espanto que le produjeron aquellos
ojos amarillos y brillantes. Sintió la áspera superficie del pavimento bajo los dedos y el agua fría
que corría alrededor. Se vio a sí mismo levantándose y retrocediendo. Y fue entonces cuando una
voz, una voz razonable y bastante simpática, le habló desde dentro de la boca de tormenta:
—Hola, George.                   
                   
Teniendo en cuenta el texto anterior. ¿Qué supone que alguien hable desde dentro de una \"Boca de tormenta\" (Drenaje)?''':'Peligro',
#10
'''El payaso sostenía en una mano un manojo de globos de colores, como tentadora fruta
madura. En la otra, el barquito de papel de George.
 —¿Quieres tu barquito, Georgie? –El payaso sonreía.
 George también sonrió, sin poder evitarlo.
 —Si, lo quiero.
 El payaso se echó a reír.
 —¡Así me gusta! ¿Y un globo? ¿Quieres un globo?
 —Bueno... sí, por supuesto. –Alargó la mano pero de inmediato la retiró–. No debo coger
nada que me ofrezca un desconocido. Lo dice mi papá.

Teniendo en cuenta el texto anterior. ¿Qué trataba de transmitirle el payaso a Georgie?''':'Seguridad',
#11
'''—Y tu papá tiene mucha razón –replicó el payaso sonriendo. George se preguntó cómo
podía haber creído que sus ojos eran amarillos, si eran de un azul brillante como los de su mamá y
de Bill–. Muchísima razón, ya lo creo. Por lo tanto, voy a presentarme. George, soy el señor Bob
Gray, también conocido como Pennywise el Payaso. Pennywise, te presento a George Denbrough.
George, te presento a Pennywise. Ahora ya nos conocemos. Yo no soy un desconocido y tú
tampoco. ¿Correcto?
 George soltó una risita
 
Teniendo en cuenta el texto anterior. ¿Qué siente George después de esa conversación?''':'Alegía',
#12
'''—Correcto. –Volvió a estirar la mano... y a retirarla–. ¿Cómo te has metido ahí adentro?
 –La tormenta me trajo volaaaando –dijo Pennywise el Payaso–. Se llevó todo el circo. ¿No
sientes olor a circo, George?
 George se inclinó hacia adelante. ¡De pronto olía a cacahuetes! ¡Cacahuetes tostados! ¡Y
vinagre blanco, del que se pone en las patatas fritas! Y olía a algodón de azúcar, a buñuelos, y
también a estiércol de animales salvajes. Olía el aroma regocijante del aserrín. Y sin embargo...
 Sin embargo, bajo todo eso olía a inundación, a hojas deshechas y a oscuras sombras en
bocas de tormenta. Era un olor húmedo y pútrido. El olor del sótano.

Teniendo en cuenta el texto anterior. ¿Qué significa que debajo de esos olores de gozo haya uno pútrido?''':'Engaño',
#13
'''Pero los otros olores eran más fuertes.
 —Sí, lo huelo –dijo.
 —¿Quieres tu barquito, George? Te lo pregunto otra vez porque no pareces desearlo mucho.
 Y se lo enseñó, sonriendo. Llevaba un traje de seda abolsado con grandes botones color
naranja. Una corbata brillante, de color azul eléctrico, le caía por la pechera. En las manos llevaba
grandes guantes blancos, como Mickey y Donald.
 —Sí, claro –dijo George, mirando el interior de la boca de tormenta.
 —¿Y un globo? Los tengo rojos, verdes, amarillos, azules...
 —¿Flotan?
 —¿Que si flotan? –La sonrisa del payaso se acentuó–. Oh, sí, claro que sí. ¡Flotan! También
tengo algodón de azúcar...
 George estiró la mano.
 
Teniendo en cuenta el texto anterior. ¿Qué quiere lograr el payaso al ofrecer objetos?''':'Aproximar',
#14
'''El payaso le sujetó el brazo.
 Y entonces George vio cómo la cara del payaso se convertía en algo tan horripilante que lo
peor que había imaginado sobre la cosa del sótano parecía un dulce sueño. Lo que vio destruyó su
cordura de un zarpazo.
 —Flotan –croó la cosa de la alcantarilla con una voz que reía como entre coágulos.
 
Teniendo en cuenta el texto anterior. 'Qué le causó a George observar aquella cosa?''':'Trauma',
#15
'''Sujetaba el brazo de George con su puño grueso y agusanado. Tiró de él hacia aquella
horrible oscuridad por donde el agua corría y rugía y aullaba llevando hacia el mar los desechos de
la tormenta. George intentó apartarse de esa negrura definitiva y empezó a gritar como un loco
hacia el gris cielo otoñal de aquel día de otoño de 1957. Sus gritos eran agudos y penetrantes y a
lo largo de toda la calle, la gente se asomó a las ventanas y salió a los porches.
 —Flotan –gruñó la cosa–, flotan, Georgie. Y cuando estés aquí abajo, conmigo, tú también
flotarás.

Teniendo en cuenta el texto anterior, ¿Qué significa para George todo lo sucedido?''':'Fatalidad',
#16
'''El hombro de George chocó contra el bordillo. Dave Gardener, que ese día no había ido a
trabajar al Shoeboat debido a la inundación, vio sólo a un niño de impermeable amarillo, un niño
que gritaba y se retorcía en el arroyo mientras el agua lodosa le corría sobre la cara haciendo que
sus alaridos sonaran burbujeantes.
 —Aquí abajo todo flota –susurró aquella voz nauseabunda, riendo, y de pronto sonó un
desgarro y hubo un destello de agonía y George Denbrough dejó de existir.
                   
Teniendo en cuenta el texto anterior, ¿Qué significan los últimos parrafos?''':'Muerte',
#17
'''Dave Gardener fue el primero en llegar. Aunque llegó sólo cuarenta y cinco segundos
después del primer grito, George Denbrough ya había muerto. Gardener lo agarró por el
impermeable, tiró de él hacia la calle... y al girar el cuerpo de George, también él empezó a gritar.
El lado izquierdo del impermeable del niño estaba de un rojo intenso. La sangre fluía hacia la
alcantarilla desde el agujero donde había estado el brazo izquierdo. Un trozo de hueso,
horriblemente brillante, asomaba por la tela rota.
 Los ojos del niño miraban fijamente el cielo y mientras Dave retrocedía a tropezones hacia
los otros que ya corrían por la calle, empezaron a llenarse de lluvia.

Teniendo en cuenta el texto anterior. ¿Qué sintió Dave Gardener al voltear a George?''':'Horror',
#18
'''Los habitantes de Derry consideraban que el Festival del Canal, que se desarrolló entre el 15
y el 21 de julio, había sido un gran éxito, algo bueno para la moral, la imagen de la ciudad... y el
bolsillo. Los festejos de esa semana celebraban el centenario de la inauguración del canal que
corría por el centro de la ciudad. Había sido ese canal el que abriera plenamente a Derry al
comercio de la madera, entre 1884 y 1910, dando origen a los años de bonanza de Derry.

Teniendo en cuenta el texto anterior. ¿Qué se esperaba de Derry al abrir el canal?''':'Prosperidad',
#19
'''En el parque había una carpa enorme de lona a rayas donde se vendían refrescos; todas las
noches, una banda daba un concierto. En el parque Bassey se instaló una feria con atracciones y
juegos administrados por los vecinos. Un tranvía especial recorría las zonas históricas de la
ciudad, de hora en hora, terminando el recorrido en la feria.

Teniendo en cuenta el texto anterior, ¿Cómo era el ambiente en el parque?''':'Jovial',
#20
'''Sus ojos recorrieron el vestíbulo, hasta el pie de la amplia escalera, y
Hallorann dejó escapar un grito ahogado. La alfombra estaba salpicada de
sangre. Sobre ella había un trozo de tela rosada. El rastro de sangre conducía a
la escalera. En el pasamanos también se veían manchas de sangre.
—Oh, Dios —murmuró Hallorann, y volvió a levantar la voz—: ¡Danny!
¡DANNY!
Parecía que el silencio del hotel se mofara de él con sus ecos, malignos,
retorcidos.
(¿Danny? ¿Quién es Danny? ¿Hay alguien aquí que conozca a Danny? Danny, Danny,
¿quién tiene el Danny? ¿Alguien quiere jugar a busquemos el Danny? ¿A ponerle la cola al
Danny? Vete de aquí, negro, que aquí nadie conoce a Danny desde Adán.) 
                   
Teniendo en cuenta el texto anterior. ¿Cómo describirías el estado mental de Hallorann?''':'Locura',
#21
'''Jesús, ¿acaso habría pasado por todo eso para en definitiva llegar
demasiado tarde? ¿Se había consumado ya todo?
Subió la escalera de dos en dos peldaños y se detuvo al llegar a la
primera planta. El rastro de sangre conducía al apartamento del vigilante. El
horror se le infiltró lentamente en las venas y en el cerebro, mientras empezaba
a andar por el corto pasillo. Los animales del seto habían sido algo tremendo,
pero esto era peor, íntimamente, sabía lo que iba a encontrar cuando llegara. 

Teniendo en cuenta el texto anterior. ¿Qué sentía mientras recorría el rastro?''':'Intranquilidad',
#22
'''Hallorann oyó el murmullo y empezó a darse la vuelta, al tiempo que se
agachaba, pero el mazo de roque bajó silbando. La capucha del chaquetón
amortiguó el golpe, pero no lo suficiente. Sintió como si en la cabeza le estallara
un cohete, deshaciéndose en un rastro de estrellas... y después, nada.
Tambaleante, retrocedió contra la pared empapelada, y Jack volvió a
golpearlo; esta vez, el mazo le acertó de costado y le hizo astillas el pómulo, al
mismo tiempo que le rompía la mayor parte de los dientes del lado izquierdo de
la mandíbula. Hallorann se desplomó, inerte.

Teniendo en cuenta el texto anterior. ¿Qué sentia el agresor de Hallorann para hacer todo eso?''':'Placer',
#23
'''Tres minutos más tarde, la puerta del ascensor se abría estrepitosamente
en la penumbra de la tercera planta. Sólo Jack Torrance estaba en él. La caja se
había detenido antes de llegar a la puerta, y Jack Torrance tuvo que izarse hasta
el nivel del pasillo, retorciéndose penosamente de dolor. Tras él arrastraba el
astillado mazo de roque. Afuera, en los aleros, el viento aullaba y rugía. Los ojos
de Jack giraban salvajemente en las órbitas. Tenía el pelo sucio de sangre y
confeti.

Teniendo en cuenta el texto anterior, ¿Qué es Jack?''':'Asesino',
#24
'''Allí arriba estaba su hijo, allí arriba en alguna parte. Jack lo percibía. Sin
nadie que lo controlara, sería capaz de cualquier cosa. De garrapatear con sus
pasteles de colores el carísimo empapelado sedoso, de estropear los muebles,
de romper las ventanas. Era un mentiroso, un falso, a quien había que castigar...
severamente.

Teniendo en cuenta el texto anterior. ¿Qué cree Jack que es su hijo?''':'Malicia',
#25
'''Oscuridad y pasillos. Danny andaba perdido por una oscuridad y unos
pasillos que eran como los que había dentro del hotel, pero de algún modo
diferentes. Las paredes, revestidas con su papel sedoso, se elevaban
interminablemente sin que Danny, por más que estirara el cuello, alcanzara a ver
el techo. Estaba perdido en la oscuridad. Todas las puertas tenían echada la
llave, y también ellas se perdían en la oscuridad. Debajo de las mirillas (que en
esas puertas gigantescas tenían el tamaño de miras de armas de fuego), en vez,
de leerse el número de la habitación, en cada puerta había una minúscula
calavera con las libias cruzadas.

Teniendo en cuenta el texto anterior. ¿Qué sentía Danny?''':'Confusion',
#26
'''Se detuvo, un niño que aún no hacía tres años había dejado los pañales,
y ahí estaba, solo para intentar decidir dónde se encontraba, dónde podía estar.
Le daba miedo, pero era un miedo que podía soportar. Ya hacía dos meses que
vivía todos los días con miedo, con un miedo que variaba desde una inquietud
sorda a un terror embrutecedor y directo. Eso se podía soportar. Pero quería
saber por que había venido Tony, por qué estaba pronunciando quedamente su
nombre en ese pasillo que no era parte de las cosas reales ni tampoco del país
de los sueños donde a veces Tony le mostraba cosas. Por qué, dónde...

Teniendo en cuenta el texto anterior. ¿Cómo se había sentido ultimamente el niño?''':'Angustiado',
#27
'''—Ya viene... —repitió Danny en un susurro aterrado, y le pareció que esa
resonancia de golpes sordos, irregulares, estaba más cerca, se oía con más
fuerza. El terror, que un momento antes era algo frío y distante, se convirtió en
una cosa inmediata. Ahora ya lograba entender las palabras, roncas, mezquinas,
articuladas en una burda imitación de la voz de su padre, pero eso no era papá.
Ahora Danny lo sabía. Sabia.

Teniendo en cuenta el texto anterior. ¿Qué comprendió Danny?''':'Usurpación',
#28
'''¿Qué era? Danny casi lo sabía. ¿Algo que podía salvarlos, a él y a su
madre? Pero Tony había dicho que tendría que hacerlo todo él solo. ¿Qué era?
Se apoyó contra la pared, tratando desesperadamente de pensar. Era tan
difícil... con el hotel que seguía intentando metérsele en la cabeza... con la
imagen de esa forma oscura, encorvada, que blandía el mazo a izquierda y
derecha, destrozando el empapelado... haciendo volar bocanadas de polvo de
yeso.

Teniendo en cuenta el texto anterior. ¿Qué le hace sentir a Danny aquello que puede salvarlos?''':'Esperanza',
#29
'''En algún punto del laberinto de corredores que el chico iba dejando tras
de sí, el ascensor se detuvo. Se oyó un ruido metálico al correrse la puerta. Y
después una voz, que ya no estaba en su cabeza, sino que era terriblemente
real: 
—¿Danny? Danny, ven aquí un minuto, ¿quieres? Te has portado mal y
quiero que vengas y te tomes tu medicina como un hombre. ¿Danny? ¡Danny!

Teniendo en cuenta el texto anterior. ¿A qué cosa se refiere como laberinto?''':'Hotel', 
#30
'''La obediencia estaba tan profundamente arraigada en él que llegó a dar
dos pasos, automáticamente, hacia donde lo llamaba la voz antes de detenerse.
Junto al cuerpo, los puños se le tensaron con violencia.
(¡No eres real! ¡Cara falsa! ¡Ya sé lo que eres! ¡Quítate la máscara!)
—¡Danny! —se reiteró el rugido—. ¡Ven aquí, cachorro! ¡Ven aquí y
tómatela como un hombre!
Un retumbar profundo y hueco, el del mazo al abatirse contra la pared.
Cuando la voz volvió a tronar su nombre, había cambiado de lugar: ahora estaba
más cerca. En el mundo de las cosas reales, la cacería comenzaba.

Teniendo en cuenta el texto anterior. ¿Cómo es realmente Danny?''':'Educado', 
#31
'''Danny escapó. Sin hacer ruido sobre la espesa alfombra, pasó corriendo
frente a las puertas cerradas, a lo largo del sedoso papel estampado, junto al
extintor de incendios asegurado a la esquina de la pared. Tras una breve
vacilación, echó a correr por el último pasillo. Al final no había nada más que una
puerta cerrada; ya no quedaba por dónde escapar.
Pero el palo seguía allí, todavía apoyado contra la pared, donde lo había
dejado papá.

Teniendo en cuenta el texto anterior. ¿Cómo se le llama a la situación en la que Danny se encuentra?''':'Acorralado',
#32
'''Danny lo atrapó, lo levantó, estiró el cuello para mirar la trampilla. En el
extremo del palo había un gancho que había que ensartar en una argolla fija en
la trampilla. Y entonces...
De la trampilla pendía un candado «Yale», flamante. Era el que Jack
Torrance había colocado en el cerrojo después de instalar las ratoneras para el
caso de que a su hijo se le ocurriera algún día la idea de hacer una exploración
por allí.

Teniendo en cuenta el texto anterior. ¿Cómo es realmente Jack?''':'Atento', 
#33
'''Un candado. El terror lo invadió.
Tras él, aquello venía, torpemente, tambaleándose, ya a la altura de la
suite presidencial, haciendo silbar malignamente en el aire el mazo de roque.
Danny retrocedió contra la última puerta, infranqueable, y lo esperó.

Teniendo en cuenta el texto anterio. ¿Qué está haciendo Jack?''':'Buscando',
#34
'''Wendy volvió en sí poco a poco; el agotamiento gris se disipó y fue
remplazándole el dolor: en la espalda, en la pierna, en el costado... no creyó que
sería capaz de moverse. Hasta los dedos le dolían, y en el primer momento no
sabía por qué.
(Por la hojita de afeitar, por eso.)

Teniendo en cuenta el texto anterior. ¿En qué estado se encuentra Wendy?''':'Miserable',
#35
'''El pelo rubio, ahora pegoteado y enredado, le caía sobre los ojos. Se lo
apartó con la mano y sintió que las costillas rotas se le clavaban por dentro,
haciéndola gemir. Empezó a ver el campo azul y blanco del colchón, manchado
de sangre. De ella, o tal vez de Jack. En todo caso, era sangre fresca. No había
estado mucho tiempo sin conocimiento, y eso era importante porque...
(¿Por qué?)

Teniendo en cuenta el texto anterior. ¿Qué sucedio con quien relata y con Jack?''':'Enfrentamiento',
#36
'''Porque...
Lo primero que recordó fue el zumbido, como de insecto, de un motor.
Durante un momento se quedó estúpidamente detenida en el recuerdo y
después, en una especie de picada vertiginosa y nauseabunda, su mente
retrocedió y le hizo ver todo en una sola mirada.
Hallorann. Debía de haber sido Hallorann. ¿Por qué, si no, podría
haberse ido Jack tan de improviso, sin haber terminado con... sin haber
terminado con ella?

Teniendo en cuenta el texto anterior. ¿Cómo se le llama al estado en el que estaba quien narra?''':'Trance',
#37
'''De alguna manera se las arregló para ponerse de pie, ir tambaleándose
por el dormitorio y, a través de las ruinas del cuarto de estar, hasta la destrozada
puerta del apartamento. La abrió de un empujón y salió al pasillo.
—¡Danny! —gritó, aunque el dolor en el pecho la hacía estremecer—.
¡Señor Hallorann! ¿Hay alguien ahí? ¿Hay alguien?

Teniendo en cuenta el texto anterior. ¿Qué era lo que estaba sintiendo quien narra?''':'Dolor', 
#38
'''El ascensor, que se había puesto otra vez en movimiento, se detuvo.
Wendy oyó el choque metálico de la puerta plegable al correrse, y después le
pareció oír una voz. Tal vez hubiera sido su imaginación. El ruido del viento era
demasiado fuerte para estar segura, en realidad.

Teniendo en cuenta el texto anterior. ¿Cuál es la razón de que escuchara una voz?''':'Imaginación', 
#39
'''Recostándose contra la pared, se dirigió lentamente hacia la intersección
con el pasillo corto. Cuando estaba a punto de llegar allí, la dejó helada el grito
que subió por el hueco del ascensor y por el de la escalera:
—¡Danny! ¡Ven aquí, cachorro! ¡Ven aquí y tómala como un hombre!
Jack. En la segunda o en la tercera planta. Buscando a Danny.
Al llegar a la esquina, Wendy tropezó y estuvo a punto de caerse. El
aliento se le heló en la garganta. Había algo
(¿alguien?)

Teniendo en cuenta el texto anterior. ¿Cómo se siente quien narra?''':'Desconcertado', 
#40
'''Era el señor Hallorann. Había venido, después de todo.
Cuidadosamente, Wendy se arrodilló junto a él, rogando en una
incoherente plegaria que no estuviera muerto. Le sangraba la nariz, y de la boca
le había salido un terrible coágulo de sangre. Un lado de la cara era un solo
magullón hinchado y purpúreo. Pero respiraba, a Dios gracias. Eran bocanadas
largas y difíciles que lo sacudían todo entero.

Teniendo en cuenta el texto anterior. ¿Cómo se sintío quien narra al ver que Hallorann sigue con vida?''' :'Consolado',
#41
'''No quedaba tiempo para pensarlo. Wendy sacudió a Hallorann, con la
cara contraída por el dolor de las costillas rotas, que sentía en el costado como
una masa ardiente, hinchada y magullada.
(¿Y si me desgarran el pulmón cada vez que me muevo?)
Tampoco eso había manera de evitarlo. Si Jack encontraba a Danny, lo
mataría, lo golpearía con el mazo hasta matarlo, como había intentado hacer
con ella.

Teniendo en cuenta el texto anterior. ¿Cómo se siente quien narra?''':'Preocupado', 
#42
'''Danny se quedó de espaldas contra la puerta, mirando hacia la
intersección donde los dos pasillos se cortaban en ángulo recto. El ruido
constante, irregular, retumbante del mazo contra las paredes se oía cada vez,
más. Aquello que lo perseguía aullaba, vociferaba y maldecía. Sueño y realidad
se habían unido sin fisura alguna.
Ahora apareció ante sus ojos.

Teniendo en cuenta el texto anterior. ¿Cómo es quien se acerca a Danny?''':'Irracional', 
#43
'''En cierto sentido, lo que sintió Danny fue alivio. Eso no era su padre. La
máscara del rostro y del cuerpo, desgarrada, hecha pedazos, era una triste
parodia. Eso no era su papá, ese horror de los programas de televisión
terroríficos del sábado por la noche, con los ojos en blanco, los hombros
encorvados, la camisa empapada de sangre. No era su papá.
—Ahora, por Dios —jadeó aquello y se enjugó los labios con una mano
temblorosa—. Ahora vas a ver quién es el que manda aquí. Ya verás. No es a ti
a quien quieren, es a mí. ¡A mí, a mí!

Teniendo en cuenta el texto anterior. ¿Qué empieza a surgir dentro de Danny?''':'Vigor', 
#44
'''—A ver si me sales con alguno de tus trucos ahora —farfulló—. No nací
ayer, ¿sabes? No acabo de caerme de la higuera, por Dios. Y voy a cumplir mis
deberes de padre contigo, muchachito.
—Tú no eres mi padre —declaró Danny.
Aquello se detuvo. Durante un momento pareció indeciso, como si en
realidad no estuviera seguro de quién —o qué— era. Después empezó a andar
de nuevo. El mazo descendió silbando y se estrelló contra una puerta, que
respondió con un ruido hueco.

Teniendo en cuenta el texto anterior. ¿Por qué dudó el \"padre\" de Danny?''':'Recuerdos',
#45
'''—Eres un mentiroso —respondió—. ¿Quién soy, si no? Tengo las dos
marcas de nacimiento, el ombligo hundido y la picha, muchachito. Pregúntale a
tu madre.
—Tú eres una máscara —insistió Danny—. Una cara falsa. La única
razón que tiene el hotel para usarte es que no estás tan muerto como los otros.
Pero cuando el hotel haya terminado contigo, no quedará nada de ti. A mí no me
asustas.

Teniendo en cuenta el texto anterior. ¿Qué es el hotel?''':'Titiretero', 
#46
'''—¡Pues ya te asustaré! —fue un aullido. El mazo silbó ferozmente al
descender y se estrelló sobre la alfombra, entre los pies de Danny. El chico no
retrocedió—. ¡Tú me mentiste! ¡Te conchabaste con ella! ¡Conspirasteis contra
mí! Además, ¡hiciste trampa! ¡Copiaste el examen final! —bajo las cejas
pobladas, los ojos lo miraban furiosamente con un resplandor de lunática
astucia—. Pero ya lo encontraré, también. Está por ahí en alguna parte, en el
sótano. Ya yo encontraré. Me prometieron que podía buscar todo lo que quisiera
—el mazo volvió a alzarse en el aire.

Teniendo en cuenta el texto anterior. Quien grita, ¿qué grita?''':'Conspiraciones', 
#47
'''Hallorann había empezado a reaccionar, pero de pronto Wendy dejó de
darle suaves golpes en la mejilla. Hacía un momento que por el hueco del
ascensor, casi inaudibles entre el rugido del viento, habían llegado unas
palabras:
—¡Hiciste trampa! ¡Copiaste el examen final!

Teniendo en cuenta el texto anterior. 'Qué le pasó a Hallorann?''':'Despertó',
#48
'''Venían desde algún lugar muy alejado del ala oeste. Wendy estaba casi
convencida de que estaban en la tercera planta, y de que Jack—o aquello que
había tomado posesión de Jack— había encontrado a Danny. Ni ella ni
Hallorann podían hacer nada ahora.
—Oh, doc —murmuró, y las lágrimas le velaron los ojos.
—El hijo de puta me rompió la mandíbula —masculló turbiamente
Hallorann—. Y la cabeza... —trabajosamente, se sentó.
Teniendo en cuenta el texto. ¿Cómo se tornó el ambiente?''':'Relajado', 
#49
'''—Mienten —repitió Danny. Con la rapidez relampagueante de un
meteoro, demasiado rápido para echarle mano y detenerlo, algo le había pasado
por la cabeza. No le quedaban más que algunas palabras de la idea.
(está por ahí en alguna parte en el sótano)
(tú recordarás lo que olvidó tu padre)

Teniendo en cuenta el texto anterior. ¿Cómo se siente Jack?''':'Eufórico', 
#50
'''—No... no deberías hablarle de esa forma a tu padre —la voz era ronca,
el mazo tembló y descendió lentamente—. Sólo haces empeorar las cosas para
ti. El... el castigo. Peor.
Tambaleándose como si estuviera ebrio, aquello lo miraba con una llorosa
conmiseración que empezaba a convertirse en odio. El mazo empezó a
levantarse nuevamente.

Teniendo en cuenta el texto anterior. ¿cómo es la actitud de Jack?''':'Desquiciada',                    
}
#Fabricar todo
def Pregunta ():
    for TodaslasPreguntas in range(10):                                                    #Se realizarán 10 archivos:
        Respuestas = open('respuestas%s.txt' % (TodaslasPreguntas + 1),'w+')               #Respuestas
        PreguntaconRespuesta = open('preguntacompleta%s.txt' % (TodaslasPreguntas +1),'w+')#La pregunta completa
                                                                                            
        RespuestasdePreguntas= list(RelacionPreguntas.keys())              #Aleatorizar las preguntas.
        random.shuffle(RespuestasdePreguntas)
        
        for TodaslasRespuestas in range(1):
            
            RespuestaCorrecta = RelacionPreguntas[RespuestasdePreguntas[TodaslasRespuestas]] #Indicar cuál es la respuesta correcta.
            RespuestaIncorrecta = list(RelacionPreguntas.values())                           #Mostrar otras respuestas incorrectas.
            del RespuestaIncorrecta[RespuestaIncorrecta.index(RespuestaCorrecta)]            #Eliminar de la lista de respuestas incorrectas la correcta
            RespuestaIncorrecta = random.sample(RespuestaIncorrecta, 3)                      #A respuesta incorrecta se le concatenan 3 valores al azar de la lista
            Opciones = RespuestaIncorrecta + [RespuestaCorrecta]                             #Las otras respuestas
            random.shuffle(Opciones)                                                         #Aleatorizar las otras respuestas
            
            PreguntaconRespuesta.write('%s. %s\n\n' % (TodaslasPreguntas + 1,RespuestasdePreguntas[TodaslasRespuestas])) #Escribir la pregunta en un archivo
            
            del RelacionPreguntas[RespuestasdePreguntas[TodaslasRespuestas]] #Evitar que se repitan las preguntas eliminandolas del diccionario
            
            for i in range(4):                                               #Escribir debajo de la pregunta las respuestas
                PreguntaconRespuesta.write(' %s. %s\n' % ('ABCD'[i], Opciones[i]))
                PreguntaconRespuesta.write('\n')
                        
            Respuestas.write('%s' % 'ABCD'[Opciones.index(RespuestaCorrecta)]) #Escribir en otro arhivo la respuesta de la pregunta
    
        PreguntaconRespuesta = open('preguntacompleta%s.txt' % (TodaslasPreguntas +1))    
    
        PreguntaFinal=PreguntaconRespuesta.read()
        
    Respuestas.close()
    PreguntaconRespuesta.close()      
    return(PreguntaFinal)                    #Enviar todo lo obtenido al programa main

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pregunta()   #Llamar a la función de arriba

print('Saludos, ingresa tu nombre')          #Introducción
name=str(input())                            #Usuario
if name.isalpha():
    name=name
else:
    while name.isalpha()==False:
        print('El nombre no puede llevar números ni caracteres especiales')
        print('Ingresa tu nombre')
        name=str(input())
print(name,''', un dia encaras un libro bastante extraño, su contenido cambia y hace preguntas. Parece que solo queda leerlo.

Presiona enter para comenzar.
Escribe "Help" y presiona enter para leer las instrucciones.''')
start=str(input())
if start != '' or start != 'help' or start != 'Help':           #Instrucciones si se escribe 'Help'
    if start == 'help' or start == 'Help':
        print('''El juego funciona de la siguiente manera:
-Deberás de leer con cuidado y antención los textos para responder correctamente.
-La respuesta que quieras dar deberá de ser escrita solo ingresando la letra de la misma, en mayuscula y después presionar enter.
-Si respondes erroneamente una pregunta, perderás vida.
-Si tu vida llega a 0, perderás y tendrás que empezar desde el principio.
-Los puntos que se obtienen son al azar.
-Perderás puntos su contestas mal a una respuesta (Puedes tener puntuación negativa).
-Obten la máxima puntuación.

Presiona enter para comenzar.
''')
        help1=str(input())                                      #Salir de instrucciones
        while help1 != '':
            print('Solo se acepta presionar la tecla \"enter\".')
            help1=str(input())

print('''Comienzas a leerlo y al parecer si contestas correctamente a sus cuestionamientos te recompenzará.
Fragmentos de texto sacados de los siguientes libros:
-\"It\", de Stephen King.
-\"El resplandor\", de Stephen King. \n''') #Comienzo del juego

def abrirpregunta (a): #Abrir cada pregunta y mostrarla en pantalla, después cerrarlas para evitar arruinar todo.
    a1=open('preguntacompleta%s.txt' % (a),'r')
    print(a1.read())
    a1.close()
    
    a2=open('respuestas%s.txt' % (a),'r')
    return (a2)
    

for e in range(10):  #Juego en si
    a2=(abrirpregunta(e+1))   #Llamar a la función que mostrará las preguntas
    respuesta_real=str(input()) #Confirmar que la respuesta sea correcta
    
    while respuesta_real != 'A' and respuesta_real != 'B' and respuesta_real != 'C' and respuesta_real != 'D':
        print('Solo se aceptan los valores de las respuestas en mayusculas: A, B, C o D.')
        respuesta_real=str(input()) #Todo este segmento limita las respuestas.
        
    if (respuesta_real in a2)==True: #En caso de serlo:
        print('Excelente')
        hp=hp+5             #Sistema de vida que no logré hacer funcionar en una función
        print('''+5 hp
Tus puntos de vida son: ''',hp,'\n')
        azar=(random.randint(5,20)) #Sistema de puntos recibidos de forma al azar, minimo 5 y máximo 20
        puntosganados=azar
        puntos=puntos+puntosganados
        print('Has ganado, ',puntosganados,' puntos, tus puntos totales son: ',puntos)
        
    else:                             #En caso de no serlo:
        print('Respuesta incorrecta, asegurate de leer palabras clave y de comprender lo que estás leyendo.')
        hp=hp-20            #Sistema de vida que no logré hacer funcionar en una función
        print('''-20 hp
Tus puntos de vida son: ''',hp,'\n')
        azar=(random.randint(5,20)) #Sistema de puntos recibidos de forma al azar, minimo 5 y máximo 20
        puntosperdidos=azar
        puntos=puntos-puntosperdidos
        print('Has perdido, ',puntosperdidos,' puntos, tus puntos totales son: ',puntos)
        
    print('Presiona enter para continuar.')  #Pausa para leer información desplegada
    
    if hp <= 0:                #Game over si vida llega a 0
        print('Oh no!, tu vida ha llegado a su fin, concentrate más la próxima vez y asegurate de comprender lo que lees.')
        proseguirfinal=input()
        if proseguirfinal=='':
            print('Saliendo')
        else:
            while proseguirfinal != '':
                print('Solo se acepta la entrada \"Enter\"')
                print('Presiona enter para continuar.')
                proseguirfinal=input()
        break
    
    proseguir=input()        #Prosigue
    if proseguir=='':
        continue
    else:
        while proseguir != '':
            print('Solo se acepta la entrada \"Enter\"')
            print('Presiona enter para continuar.')
            proseguir=input()
            
    
if puntos>=150:              #Gamification
    print('''¡Felicidades!, tu conocimiento y el azar estuvieron de tu lado, no puedo recompensarte con nada mejor
que una felicitación pero lo has hecho muy bien, ¡vuelve y mejora aún más tu record!''')
else:
    if puntos <150 and puntos>100:
        print('¡Muy bien!, pero se puede obtener un mejor puntaje, ¡Vuelve a intentarlo!')
    else:
        if puntos<100 and puntos>=50:
            print('¿Eso no ha salido perfecto cierto?, ¡vuelve y mejora tu record!')
        else:
            if puntos<50 and puntos>0:
                print('Pudo haber sido peor, ¡esfuerzate más y lo lograrás!')
            else:
                if puntos<=0:
                    print('Tranquilo, la práctica hace al maestro, concentrate y lograrás mejorar ese puntaje.')







    
    