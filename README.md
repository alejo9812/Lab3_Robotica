# Lab3_Robotica
Hector Alejandro Montes Lobaton  
Bryan Steven Pinilla Castro  

## Introducción

En este laboratorio se utilizó ROS en el que se hizo uso de la herramienta turtlesim para comprender los conceptos básicos de la programcación de robots en este ambiente de programación.  


## MATLAB
Se realizaron dos ejercicios, uno en Matlab y otro en Python, 

## PYTHON

Como primer paso se incializa ROS en una terminal.

```
roscore
```
Y de manera paralela se incia el nodo *turtlesim* en otra terminal.

```
rosrun turtlesim turtlesim_node
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



Se implementan las siguientes operaciones:

- W: Mover hacia adelante 
- S: Mover hacia atrás
- D: girar en sentido horario
- A: girar en sentido antihorari
- R: Retornar a su posición y orientación iniciales
- SPACE: Giro de 180°


## Resultado del código en python

https://drive.google.com/file/d/10vb24eUO3-6WHGjRxMKwllmTiXIngnt-/view?usp=sharing
