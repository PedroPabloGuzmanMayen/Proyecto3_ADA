# Proyecto 3: Análisis e implementación 


# Implementación de los algoritmos


## Modelo de costos

Para la implementación del modelo se uso este modelo de costos: 

- Encontrar el i-ésimo elemento de la lista tiene un costo de i
- Intercambiar e insertar elementos en la lista no tiene ningún costo

## MTF

Recibe dos parámetros: la lista de solicitudes y la lista de configuraciones. 

Este es el pseudocódigo del algoritmo:

- Definir la variable costo total, este variable almacena el costo total de toda la operación
- Recorrer la lista de solicitudes
- Buscar y encontrar la posición en la que se encuentra la iteración actual en la lista de configuraciones
- Definir la variable posición, esta guarda la posición en donde fue encontrado el elemento de la iteración actual
- Eliminar el valor encontrado en la posición de la lista de configuraciones
- Definir la variable valor, esta guarda el valor encontrado y solicitado
- Mover el valor encontrado a la posición de la lista
- Sumar el valor de la posición del elemento solicitado al valor del costo total


## IMTF

Recibe dos parámetros: la lista de solicitudes y la lista de configuraciones. 

Este es el pseudocódigo del algoritmo:

- Definir la variable costo total, este variable almacena el costo total de toda la operación
- Recorrer la lista de solicitudes
- Buscar y encontrar la posición en la que se encuentra la iteración actual en la lista de configuraciones
- Definir la variable posición, esta guarda la posición en donde fue encontrado el elemento de la iteración actual
- Eliminar el valor encontrado en la posición de la lista de configuraciones
- Definir la variable valor, esta guarda el valor encontrado y solicitado
- Mover el valor encontrado a la posición de la lista
- Sumar el valor de la posición del elemento solicitado al valor del costo total

# Video 

Puede encontrar un video con una explicación más detallada en este enlace: [Enlace al video][https://youtu.be/3h1XXIZhsuQ]

# Repositorio

El repositorio del código de este proytecto puede encontrarse en: [Link al Repositorio](https://github.com/PedroPabloGuzmanMayen/Proyecto3_ADA.git)

# Análisis y preguntas

- 1. Calcular el costo de acceso utilizando el algoritmo MTF para
  - (a) Lista de configuración: 0, 1, 2, 3, 4
  - (b) Secuencia de solicitudes: 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4

Para esta configuración y secuencia de solicitudes siguiendo el modelo de costos establecido al inicio, el costo total de la operación es de 90. 


![Imagen](https://raw.githubusercontent.com/PedroPabloGuzmanMayen/Proyecto3_ADA/f383242b5e91a47e7473fc17140678a0b9336730/P3%20P1.png)



- 2. Calcular el costo de acceso utilizando el algoritmo MTF para
  - (a) Lista de configuración: 0, 1, 2, 3, 4
  - (b) Secuencia de solicitudes: 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4

Para esta configuración y secuencia de solicitudes siguiendo el modelo de costos establecido al inicio, el costo total de la operación es de 67. 

![Imagen](P3_P2.png)

- 3. Para qué secuencia de 20 solicitudes se obtiene el mínimo costo total de acceso utilizando el algoritmo MTF para la configuración 0, 1, 2, 3, 4? ¿Cuál sería ese costo total de acceso?

La secuencia con la que se obtiene el costo mínimo es la secuencia que contiene 20 0's. Esto debido a que el 0 es el primer elemento en la lista de configuraciones y por lo tanto no tenemos que hacer ninguna búsqueda para encontrarlo y como 0 ya está al frente, tampoco se hace ningún intercambio y el orden original de la lista de configuraciones no se altera. Con el modelo de costo establaecido, el costo total de este caso es de 20 (1 operación por cada vez que solicitamos el 0). 

![Imagen](P3_P3.png)

- 4. ¿Para qué secuencia de 20 solicitudes se obtiene el peor de los casos utilizando el algoritmo MTF para la configuración 0, 1, 2, 3, 4? ¿Cuál sería ese costo total de acceso?

La secuencia de 20 solicitudes con el peor caso es la secuencia $$[4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0]$$ esto debido a que en esta secuencia cada una de las solcitudes el elemento a buscar está en la última posición de la lista de configuraciones y eso provoca que cada una de las solicitudes alcance su mayor costo posible. Por ejemplo, la primera solictud es 4 y se sabe que este número está en la última posición al inicio, 4 se mueve al frente pero la próxima solicitud es 3 y este número queda en la última posición debido al cambio realizado anteriormente. 
Con el modelo de costos establecido al inicio, el algoritmo alcanza un costo total de 100. 

![Imagen](P3_P4.png)

- 5. Calcular el costo de acceso utilizando el algoritmo MTF para
  (a) Lista de configuración: 0, 1, 2, 3, 4
  (b) Secuencia de solicitudes: 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
  (c) Secuencia de solicitudes: 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3
  (d) ¿Se observa algún patrón cuando hay una repetición de 20 elementos en la secuencia?


Con la secuencia de 20 números 2's, el costo total fue de 22 mientras que con la secuencia de números 3's el costo fue de 23. El patrón que se observa en estas solicitudes es que el costo final resulta siendo 20 + el costo total de la posición del elemento inicial en la solicitud. En este caso, cuando se solicito el número 2 al inicio se hizo una operación con un costo de 3 y se movió el 2 al frente, luego se hicieron 19 solictiudes en las cuáles el elemento solicitado estaba en la posición inicial lo cuál da un costo total de $$3+19 = 22$$ 

![Imagen](P3_P51.png)

![Imagen](P3_P52.png)

- 6. Mejor y peor caso del algoritmo IMTF

Al igual que en el algoritmo MTF, el algoritmo IMTF obtiene su mejor caso cuando se le provee una secuencia de solcitudes la cuál contiene solamente las solicitudes que solamente contienen al elemento en la primera posición de la lista de configuración original, usando el modelo de costos planteado al inicio y con una secuencia de 20 0's, se obtuvo que el costo total para el mejor caso es de 20. 

El peor caso también se produce con las solicitudes con la lista de solicutudes que contiene los elementos de la tabla de configuración original en orden inverso, esto debido a que el algoritmo jamás moverá al frente ningún elemento y deberá hacer siempre una búsqueda que sea igual a la posición del elemento que se busque . El costo total con una secuencia de 20 solcitudes usando el algoritmo fue de 60. 

Mejor caso: 
![Imagen](P3_61.png)


Peor caso:
![Imagen](P3_62.png)



