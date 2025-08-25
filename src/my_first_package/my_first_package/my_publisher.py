import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class turtlesimPublisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        self.publisher.publish(msg) #publish를 msg로 보냄
    
        # self.subscription  # prevent unused variable warning

def main():
    rp.init()
    node = turtlesimPublisher()
    rp.spin(node) #계속 돌리기
    
    node.destroy_node()
    rp.shutdown()
    
    print("Hi from my_first_package's subscriber.")
    
if __name__ == '__main__':
    main()
        
        
        
    
