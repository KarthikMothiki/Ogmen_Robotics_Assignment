import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
from math import pi

class LaserFilter(Node):
    def __init__(self):
        super().__init__('filter_node')
        
        # Subscriber to the /scan topic
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_cb,
            10
        )
        self.subscription
        
        
        # Publisher for the /filtered_scan topic
        self.publisher = self.create_publisher(LaserScan, '/filtered_scan', 10)
        
    def lidar_cb(self, msg):
        # https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/LaserScan.html
        # Filter the scan data, fs
        
        # Modifying only the min and max angles and leaving the others as it is
        self.get_logger().info('Subscribed to the /scan topic')
        fs = LaserScan()
        fs.header = Header()
        fs.header.stamp = self.get_clock().now().to_msg()
        fs.header.frame_id = msg.header.frame_id

        # float32 angle_min        # start angle of the scan [rad]
        # float32 angle_max        # end angle of the scan [rad]
        fs.angle_min = 0.0
        fs.angle_max = 120.0 * (pi/180.0)
        fs.angle_increment = msg.angle_increment
        fs.time_increment = msg.time_increment
        fs.scan_time = msg.scan_time
        fs.range_min = msg.range_min
        fs.range_max = msg.range_max

        # Publish filtered scan data
        self.get_logger().info(f'Publising the filtered scan topic with: \nminimum angle: {fs.angle_min} \nmaximum_angle: {fs.angle_max}\n')
        self.publisher.publish(fs)

def main(args=None):
    rclpy.init(args=args)
    node = LaserFilter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
