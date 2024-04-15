# Lab3_Robotica
Hector Alejandro Montes Lobaton  
Bryan Steven Pinilla Castro  

## Introducción

En este laboratorio se utilizó ROS en el que se hizo uso de la herramienta turtlesim para comprender los conceptos básicos de la programcación de robots en este ambiente de programación.  



## MATLAB : Conexion ROS a Matlab.
En una terminal inicializar ROS.

```
roscore
```
En otra se incia el nodo *turtlesim*.

```
rosrun turtlesim turtlesim_node
```

Abriendo en Matlab  se ejecuta el siguiente script *Matlab.mlx*.

```
Matlab.mlx
```


![Graph](Graph_mlx)



```
% Apagar cualquier instancia de ROS en ejecución
rosshutdown;

% Inicializar ROS
rosinit;

% Crear un publicador para enviar comandos de velocidad a la tortuga
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist');

% Crear un mensaje vacío de velocidad
velMsg = rosmessage(velPub);

% Configurar la velocidad lineal en el mensaje
velMsg.Linear.X = 1;

% Enviar el mensaje de velocidad a la tortuga
send(velPub, velMsg);

% Esperar durante 1 segundo para permitir que la tortuga se mueva
pause(1);

% Crear un suscriptor para el tópico de velocidad de la tortuga
cameraSub = rossubscriber('/turtle1/cmd_vel', 'geometry_msgs/Twist');

% Obtener el último mensaje de velocidad recibido por la tortuga
cameraMsg = cameraSub.LatestMessage;

% Extraer los componentes lineales y angulares del mensaje de velocidad
Lin = cameraMsg.Linear;
Ang = cameraMsg.Angular;
```

## PYTHON :  Direccion de turtlesim por teclado.

En una terminal inicializar ROS.

```
roscore
```
En otra se incia el nodo *turtlesim*.

```
rosrun turtlesim turtlesim_node
```

En una tercera de ejecuta el archivo *myTeleopKey.py* agregando la ruta. Tomando como ejemplo.

```
/bin/python3/home/"suusuario"/catkin_ws/src/myTeleopKey.py
```

Librerias utilizadas en python

```
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from turtlesim.srv import TeleportAbsolute

import termios, sys, os, tty
from numpy import pi
```


![Graph](Graph_py)


![Turtle](Turtle)

Se implementan las siguientes operaciones:

- W: Mover hacia adelante 
- S: Mover hacia atrás
- D: girar en sentido horario
- A: girar en sentido antihorari
- R: Retornar a su posición y orientación iniciales
- SPACE: Giro de 180°


## Resultado del código en python

https://drive.google.com/file/d/10vb24eUO3-6WHGjRxMKwllmTiXIngnt-/view?usp=sharing
