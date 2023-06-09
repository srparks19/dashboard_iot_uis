# dashboard_iot_uis
Interfaz grafica para la presentación y análisis de resultados de la plataforma IoT Smart Campus.

Se decidió desarrollar una página web como medio de visualización de los datos recopilados por un prototipo IoT. Esta página web ofrece a los usuarios diversas formas de presentación y lectura de la información, lo que facilita su comprensión y clasificación.

<h1>Arquitectura del aplicativo</h1>

En el diseño del prototipo se construyó una arquitectura de software capaz de alcanzar los objetivos planteados en secciones anteriores, este proceso se fue modificando y complementando a medida que la construcción del aplicativo avanzaba obteniendo la versión del prototipo actual que cubre las necesidades planteadas. La arquitectura cuenta de dos componentes principales.

- El Hardware: El cual se puede encontrar explicado en el siquiente enlace: <a href="https://github.com/srparks19/prototipo_IoT_Uis">Aqui</a>
- El software: Donde se almacenará, recopilará y visualizará la información. 

![Imagen ilustrativa de la arquitectura del prototipo](https://github.com/srparks19/dashboard_iot_uis/assets/66749108/950a8227-75e2-4a18-ae36-2bb617805ee6)


Desarrollado para el estudio y transformación de datos se divide en dos componentes principales. El primero es responsable del renderizado y la comunicación con la base de datos MongoDB, mientras que el segundo se encarga de la parte visual del sistema. Para lograr un funcionamiento adecuado, se utiliza la distribución de trabajo proporcionada por el Framework Flask. Esto permite una adecuada organización y estructura del software, facilitando su mantenimiento y escalabilidad.

Para la comunicación con la base de datos y el renderizado del componente visual, se implementó Flask, un framework de Python, que proporciona un entorno virtual para la gestión de la página web. Esto permite crear puntos de comunicación que obtienen los datos almacenados en la base de datos MongoDB y manipulan las diferentes rutas del aplicativo para facilitar la navegación del usuario entre páginas.

<h2>Vista del aplicativo</h2>

El aplicativo se compone de varias vistas que permitirían al usuario interactuar con los datos obtenidos en el proceso.

<h3>Dashboard</h3>

La pantalla inicial del aplicativo muestra una vista de todas las estaciones disponibles. Desde esta pantalla, se puede seleccionar la estación deseada y acceder a una vista que muestra los dispositivos asociados a dicha estación.

![Dashboard](https://github.com/srparks19/dashboard_iot_uis/assets/66749108/8f5bfefd-d869-4d54-aa6d-025adcd3e1d9)

<h3>Estaciones y dispositivos</h3>

Al desglosar cada estación, se muestran los dispositivos asociados a ella. Al seleccionar uno de estos dispositivos, se accede a una vista que presenta información relevante obtenida por el sensor. Esta información incluye datos de interés relacionados con la toma de muestras del sensor, como valores de temperatura, humedad, presión o cualquier otro parámetro medido por el dispositivo.

![Estaciones y dispositivos](https://github.com/srparks19/dashboard_iot_uis/assets/66749108/ee896b25-509b-47e7-914b-6db50289604f)

<h3>Visualización geosatelital</h3>

Cada uno de los dispositivos cuenta con una lectura geolocalizada de los datos, el momento en el cual fueron captados por el sensor y plasmados en un mapa de densidad, el cual permite obtener un detalle cualitativo de cada lectura.

![Visualización geosatelital](https://github.com/srparks19/dashboard_iot_uis/assets/66749108/5c685ccc-59d2-4454-8b35-464e6ac6a0b1)

<h3>Tabulación de datos</h3>

En este apartado el usuario podrá obtener la información de cada una de las lecturas obtenidas por la estación donde se otorga la libertad de obtener una lectura de ellos y descarga del banco de datos en formato CSV.

![Tabulación de datos](https://github.com/srparks19/dashboard_iot_uis/assets/66749108/8e3224de-f004-4864-ab75-01190b0d9117)

<h2>Despliegue del aplicativo</h2>

Luego de haber clonado y descargado el repositorio se deben tener en consideración tener las siguientes herramientas instaladas:

- Python 3+
- Flask
- Mongo DB
- Mongo Express

<h2>Comandos importantes</h2>

Antes de iniciar con la explicación de los comandos implementados para el correcto funcionamiento del aplicativo es necesario descargar el proyecto de Samrt Campus ya que el presente proyecto es una extensión de este: <a href="https://github.com/UIS-IoT-Smart-Campus/smart_campus_production">Smart Campus UIS</a>

Para el despliegue del aplicativo se implementó un entorno virtual de python, este con el fin de crear un espacio de trabajo que permita la creación y renderización de las vistas del usuario. Como se comentó el entorno virtual ya se encuentra dentro del aplicativo, para su ejecución se debe (en la raiz del proyecto) ejecutar el siguiente comando:

- env\Scripts\activate

Este comando permitirá activar el entorno virtual permitiendo a los interesados, interactuar con el aplicativo. Para subir el entorno para su visualización tan solo se debe ejecutar el siguiente comando:

- python3 app.py

De lo contrario, si el anterior comando no funciona, se debe ejecutar el comando alternativo:

- flask run

Luego que el aplicativo se encuentre arriba, se podrá visualizar por la puerta de enlace predeterminada:

- http://localhost:5000
