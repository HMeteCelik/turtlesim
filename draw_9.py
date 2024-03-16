#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

def upper_circle():

    circle_done = 0
    t0 = rospy.Time.now().to_sec()  
    while (circle_done < (circumference * 5 / 4)):     ## Drawing circle for upper part
        vel.linear.x = velocity
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = velocity / radius
        pub.publish(vel)
        rate.sleep()
        t1 = rospy.Time.now().to_sec()
        circle_done =  (t1 - t0) * velocity
    vel.linear.x = 0
    pub.publish(vel)
    rotate_turtle()
    
def rotate_turtle():
    
    vel.angular.z = math.pi    ## Rotating turtle
    pub.publish(vel) 
    rospy.sleep(1)
    downward_line()
    
    
def downward_line():

    line_done = 0
    t0 = rospy.Time.now().to_sec()    
    while (line_done < radius * 2):   ## Drawing downward line
        vel.linear.x = velocity  
        vel.linear.y = 0 
        vel.linear.z = 0  
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        pub.publish(vel)
        t1 = rospy.Time.now().to_sec()
        rate.sleep()
        line_done = (t1 - t0) * velocity
    vel.linear.y = 0  
    pub.publish(vel)
    down_arc_circle()

        
        
def down_arc_circle():
    
    circle_done = 0
    t0 = rospy.Time.now().to_sec()
    while (circle_done < (circumference * 1 / 3)):   ## Drawing down arc-circle
        vel.linear.x = velocity
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = -velocity / radius
        pub.publish(vel)
        t1 = rospy.Time.now().to_sec()
        rate.sleep()
        circle_done = abs((t1 - t0) * velocity)
    vel.linear.x = 0
    pub.publish(vel)
    

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim', anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(10)
        vel = Twist()
        radius = float(input("Enter input size (radius): "))
        velocity = float(input("Enter velocity: "))
        circumference = 2 * math.pi * radius
        upper_circle()
        rospy.loginfo("9 is drawn!")
    except rospy.ROSInterruptException:
        pass

