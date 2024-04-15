rosshutdown;
rosinit; 

velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist')
velMsg = rosmessage(velPub)

velMsg.Linear.X = 1
send(velPub,velMsg)
pause(1)

cameraSub = rossubscriber('/turtle1/cmd_vel',"geometry_msgs/Twist");
cameraMsg = cameraSub.LatestMessage

Lin = cameraMsg.Linear
Ang = cameraMsg.Angular
