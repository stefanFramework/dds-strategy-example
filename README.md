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

**Usando Docker, DockerCompose y Docker 4 Mac o Docker VM:**
 1. Ejecutar `sh entrypoint.sh install`
 2. Ejecutar `sh entrypoint.sh run {elementos separados por coma} {estrategia: sorting-asc | sorting-desc}`

**Sin Docker porque no se lo que es, y ademas estoy en Windows:**
 1. Copiar todo lo que esta en el directorio /app a algun directorio de tu sistema local (como por ejemplo /Desacargas)
 2. Ejecutar `python main.py {elementos separados por coma} {estrategia: sorting-asc | sorting-desc}`



