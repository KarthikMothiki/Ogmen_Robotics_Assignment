#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import radians, sqrt, atan2, pi

class square(Node):

    def __init__(self):
        super().__init__('diff_drive_robot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.odom_subscriber_ = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)
        self.timer = self.create_timer(0.1, self.move_robot)
        self.waypoints = [
            [0.0, 0.0, 0.0],
            [5.0, 0.0, radians(45)],
            [5.0, 5.0, radians(90)],
            [0.0, 5.0, radians(0)],
            [0.0, 0.0, radians(135)]
        ]
        self.current_waypoint = 0
        self.current_pose = [0.0, 0.0, 0.0]
        self.reached_waypoint = False
        self.max_linear_velocity = 0.3
        self.max_angular_velocity = 1.0

    def odom_callback(self, msg):
        self.current_pose[0] = msg.pose.pose.position.x
        self.current_pose[1] = msg.pose.pose.position.y
        orientation_q = msg.pose.pose.orientation
        self.current_pose[2] = self.quaternion_to_euler(orientation_q)

    def quaternion_to_euler(self, q):
        t3 = +2.0 * (q.w * q.z + q.x * q.y)
        t4 = +1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        yaw = atan2(t3, t4)
        return yaw

    def move_robot(self):
        if self.current_waypoint < len(self.waypoints):
            target_x, target_y, target_theta = self.waypoints[self.current_waypoint]
            distance = sqrt((target_x - self.current_pose[0]) ** 2 + (target_y - self.current_pose[1]) ** 2)
            angle_to_target = atan2(target_y - self.current_pose[1], target_x - self.current_pose[0])
            angle_difference = angle_to_target - self.current_pose[2]
            angle_difference = self.normalize_angle(angle_difference)
            
            print(f"Going to waypoint:\n{self.waypoints[self.current_waypoint]}")

            cmd = Twist()

            if distance > 0.1:  
                linear_velocity = 0.5 * distance
                angular_velocity = 1.0 * angle_difference
                cmd.linear.x = min(self.max_linear_velocity, linear_velocity)
                cmd.angular.z = min(self.max_angular_velocity, angular_velocity)
            elif abs(target_theta - self.current_pose[2]) > 0.1:
                cmd.angular.z = 1.0 * self.normalize_angle(target_theta - self.current_pose[2])
                cmd.angular.z = min(self.max_angular_velocity, cmd.angular.z)
            else:
                self.current_waypoint += 1
                self.reached_waypoint = True
                
            self.publisher_.publish(cmd)

    def normalize_angle(self, angle):
        while angle > pi:
            angle -= 2 * pi
        while angle < -pi:
            angle += 2 * pi
        return angle

def main(args=None):
    rclpy.init(args=args)
    robot = square()

    try:
        rclpy.spin(robot)
    except KeyboardInterrupt:
        pass

    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
