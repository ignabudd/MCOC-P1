# MCOC2020-P1

## Entrega 1 - Integración Ecuaciones Diferenciales

  ![Trayectoria para distintos vientos](https://user-images.githubusercontent.com/69213519/91117774-748d8480-e65d-11ea-8e32-74457769c927.png)

## Entrega 2 - Primeras predicciones con la EDM básica del satélite

+ En el siguiente gráfico se observan las distintas posiciones en (x,y,z), para dos orbitas completas. Se puede apreciar que para que esto se cumpla debe pasar un lapso de 3 horas y media, en donde en el eje x oscila entre 5000 y -5000 km, al igual que en el eje y, mientras que en el eje z, se mantiene constante en 0, pues la órbita se mantiene en el plano xy.

![Hitsorias de tiempo](https://user-images.githubusercontent.com/69213519/91517638-2f1ac280-e8bc-11ea-9473-9be9e4ed42f7.png)

+ En el gráfico de abajo se puede apreciar la distancia r(t) versus el tiempo, en donde se logró obtener una velocidad inicial v=24600 km/h, para que el satelite no cayera de vuelta a la atmosfera, este resultado se obtuvo al "ojo".

![Trayectoria Satelite Vista 1](https://user-images.githubusercontent.com/69213519/91517639-304bef80-e8bc-11ea-92d3-9e5011f18836.png)

+ Por último, en eset gráfico se puede notar la tierra en verde y el satélite orbitandoa su al rededor en el plano xy. Se pueden ver las dos orbitas. 

![Trayectoria Satelite Vista 2](https://user-images.githubusercontent.com/69213519/91517640-304bef80-e8bc-11ea-95fd-333097f535f7.png)

## Entrega 4 - Estudio de Convergencia método de Euler

  + En el gáfico a continuación se pueden apreciar como se comportan las diferentes soluciones para el estudio de una ecuación diferencial armónica, entre ellas, se obtuvo la solución real, esta calculada previamente, la solución odeint de la libreria scipy y el método Euler.
  +  Se puede observar que las soluciones de Euler con N=10 y N=100, al igual que la solución odeint, son las que más se acercan a la solución real, sin embargo no llegan a ser iguales los resultados. Por otra parte, la solución euler con N=1, se aleja de la solución real, de manera que es la menos precisa.

![ Entrega 4](https://user-images.githubusercontent.com/69213519/91795284-4246ce80-ebeb-11ea-84cd-84f077f5e68e.png)

## Entrega 5 - Mejoras al modelo y estudio de convergencia
  + 1. Grafíque, como arriba, la posición (x,y,z) en el tiempo del vector de estado de Sentinel 1A/B que le tocó. Para esto, descargue y utilice la función leer_eof.
  
![P1 - Posicion XYZ](https://user-images.githubusercontent.com/69213519/92385385-30cc5d80-f0e8-11ea-9c3d-8d51ac8a5252.png)

  + 2. Usando la condición inicial (primer OSV) de su archivo, compare la solución entre odeint y eulerint. Use Nsubdiviciones=1. Grafíque la deriva en el tiempo como arriba       ¿Cuánto deriva eulerint de odeint en este caso al final del tiempo? (Esta pregunta solo compara algoritmos, no se usa más que la condición inicial del archivo EOF). ¿Cuanto se   demora odeint y eulerint respectivamente en producir los resultados?
  
![P2 - Distancia pos  euler y odeint (N=1)](https://user-images.githubusercontent.com/69213519/92385387-31fd8a80-f0e8-11ea-9ee7-6c655904d73d.png)

  + 3. ¿Cuantas subdivisiones hay que usar para que la predicción con eulerint al final del tiempo esté en menos de un 1% de error? Grafique la deriva en el tiempo. Comente con    respecto del tiempo de ejecución de eulerint ahora.
  
![P3 - Distancia pos  euler y odeint (N=240)](https://user-images.githubusercontent.com/69213519/92385389-32962100-f0e8-11ea-9275-c5d8e76880e7.png)

  + 4. Implemente las correcciones J2 y J3. Repita los gráficos de arriba para su caso particular. ¿Cuánta deriva incurre al agregar las correcciones J2 y J3? ¿Cuanto se demora     su código en correr?

![P4 - Posicion XYZ (j2)](https://user-images.githubusercontent.com/69213519/92385393-332eb780-f0e8-11ea-8d3c-56f5e935aca7.png)
![P4 - Distancia pos  real y predicha con j2](https://user-images.githubusercontent.com/69213519/92385511-696c3700-f0e8-11ea-8193-058e7c99f1d7.png)

![P4 - Posicion XYZ (j2j3) ](https://user-images.githubusercontent.com/69213519/92385394-33c74e00-f0e8-11ea-8f3f-b00739912dea.png)
![P4 - Distancia pos  real y predicha con j2j3](https://user-images.githubusercontent.com/69213519/92385521-6e30eb00-f0e8-11ea-876f-27bfe9419d7c.png)


