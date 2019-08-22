# dds-strategy-factory
Ejemplo de implementacion de un patron Strategy combinado con el patron creacional Factory Method

### Introduccion

En este ejemplo tenemos una app (hecha en python) a la cual le pasamos por parametro una lista de elementos y un criterio de ordenamiento y nos ordena la lista siguiendo ese mismo criterio.  
Los Criterios disponibles son: Orden ascendente, y orden descendente

Para eso vamos a implementar un patron Strategy donde cada criterio de ordenamiento lo vamos a transformar en una estrategia.  
Adicionalmente, para la creacion de cada una de las estrategias, vamos a implementar un patron Factory Method.

### Arquitectura y Organizacion

En el directorio `/app` esta la aplicacion.  
Todo comienza en main.py, particularmente en la funcion principal `main()`.  
El sistema recibe la informacion por parametro, la valida y delega la responsabilidad de la operacion a una capa de servicio. En este ejemplo a traves del `SortingService`
  
Dentro del directorio `/domain` esta el dominio de nuestra aplicacion, ahi estan definidas las estrategias, el factory que las crea y el servicio 

### Instalacion y Ejecución

La aplicacion esta Dockerizada. Para los que no saben que es Docker, pero les interesaria saber, dejo información abajo:

- [Que es Docker?](https://docs.docker.com/engine/docker-overview/)
- [Docker para Windows](https://docs.docker.com/docker-for-windows/)
- [Docker para Mac](https://docs.docker.com/docker-for-mac/)
- [Docker para Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

**Usando Docker, DockerCompose y Docker 4 Mac/Docker VM:**

Para facilitar la implementacion de la app, se encapsulo todo en un script llamado `entrypoint.sh`.  
Tanto instalación y la ejecución se realizan a través de una llamada a este script.  

Los comandos disponibles son: 

- `install`: Genera el **docker-compose.yml** a partir de un template de ejemplo (incluido en el directorio del proyecto) y realiza el buildeo de la imagen.  No toma parametros. 
- `run`: Realiza la ejecución de la aplicacion. Toma 2 parametros: una lista de valores numericos separados por `,` y el criterio de ordenamiento que puede ser **sorting-asc** o **sorting-desc**

Como ejecutar la aplicacion:

 1. Ejecutar `sh entrypoint.sh install`
 2. Ejecutar `sh entrypoint.sh run {elementos separados por coma} {estrategia: sorting-asc | sorting-desc}`

**Si no me interesa aprender Docker, como puedo correr la aplicación?:**

Para poder ejecutar la app en un entorno local "clasico" es necesario que tengan python Version 2.7.x o superior instalado

 1. Copiar todo lo que esta en el directorio /app a algun directorio de tu sistema local (como por ejemplo /Desacargas)
 2. Ejecutar `python main.py {elementos separados por coma} {estrategia: sorting-asc | sorting-desc}`



