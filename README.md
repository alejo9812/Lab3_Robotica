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

Abriendo el programa Matlab *Matlab.mlx* se ejecuta el siguiente script.

```
Matlab.mlx
```


![Graph](Graph_mlx)


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
