import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from turtlesim.srv import TeleportAbsolute

import termios, sys, os, tty
from numpy import pi


# Condiciones inciales de la tortuga
i_position = (5.5, 5.5, 0)
i_orientation = 0
turtle_speed = 1



# Configuración de la tecla de salida del programa
def setup_terminal():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    return old_settings

# Restauración de la configuración original del terminal
def restore_terminal(old_settings):
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

# Función para publicar los comandos de movimiento
def publish_movement(msg):
    pub.publish(msg)

# Giro horario
def turn_clockwise():
    msg = Twist()
    msg.linear.x = 0
    msg.angular.z = -turtle_speed
    publish_movement(msg)

# Giro antihorario
def turn_counterclockwise():
    msg = Twist()
    msg.linear.x = 0
    msg.angular.z = turtle_speed
    publish_movement(msg)


# Mover hacia adelante
def move_forward():
    msg = Twist()
    msg.linear.x = turtle_speed
    msg.angular.z = 0
    publish_movement(msg)

# Mover hacia atrás
def move_backward():
    msg = Twist()
    msg.linear.x = -turtle_speed
    msg.angular.z = 0
    publish_movement(msg)

# Girar 180 grados
def turn_180():
    print("dentro de nuevo  ")
    msg = Twist()
    msg.linear.x = 0
    msg.angular.z = pi
    publish_movement(msg)    


# Volver a las condiciones iniciales
def return_to_center():
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleport_absolute = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        teleport_absolute(i_position[0], i_position[1], i_orientation)
    except rospy.ServiceException as e:
        print("Service call failed: ", e)





if __name__ == '__main__':
    # Inicializar el nodo ROS
    rospy.init_node('turtle_keyboard')

    # Crear un objeto publicador para enviar comandos de movimiento a la tortuga
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Configurar el terminal para recibir las teclas presionadas
    old_settings = setup_terminal()

    try:
        while not rospy.is_shutdown():
            key = ord(sys.stdin.read(1))
            print(key)
            #tecla 'w'
            if key == 119:
                move_forward()
            #tecla 's'
            elif key == 115:
                move_backward()
            #tecla 'd'
            elif key == 100:
                turn_clockwise()
            #tecla 'a'
            elif key == 97:
                turn_counterclockwise()
            #tecla 'r'
            elif key == 114:
                turn_180()
            #tecla 'space'
            elif key == 32:
                return_to_center()
    except: 
        print("Error")
