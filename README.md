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

![Posicion](https://user-images.githubusercontent.com/69213519/92318138-376eae00-efde-11ea-9da8-c0433d544bb2.png)

![Distancia pos  real y predicha(N=1)](https://user-images.githubusercontent.com/69213519/92318136-363d8100-efde-11ea-9e8a-f844bb9a7d67.png)

![Distancia pos  real y predicha(N=240)](https://user-images.githubusercontent.com/69213519/92318137-36d61780-efde-11ea-8c66-b347bc93a103.png)



