import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose

from geometry_msgs.msg import Twist

from my_first_package_msgs.msg import CmdAndPoseVel


class CmdAndPose(Node):
    def __init__(self):
        super().__init__('turtle_cmd_pose')
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.callback_pose, 10
        )
        self.sub_cmdvel = self.create_subscription(
            Twist,
            'turtle1/cmd_vel',
            self.callback_cmd_vel, 10
        )
        self.publisher = self.create_publisher(CmdAndPoseVel, 'cmd_and_pose', 10) 
        self.timer_period = 1.0
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        
        self.cmd_pose = CmdAndPoseVel() 

    def callback_pose(self, msg):
        self.cmd_pose.pose_x = msg.x
        self.cmd_pose.pose_y = msg.y
        self.cmd_pose.linear_vel = msg.linear_velocity
        self.cmd_pose.angular_vel = msg.angular_velocity
        
    def callback_cmd_vel(self, msg):
        self.cmd_pose.cmd_vel_linear = msg.linear.x
        self.cmd_pose.cmd_vel_angular = msg.angular.z
    
    def timer_callback(self):
        self.publisher.publish(self.cmd_pose)   #나의 데이터 cmd_pose를 publish


def main():
    rp.init()
    node = CmdAndPose()
    rp.spin(node) #계속 돌리기
    
    node.destroy_node()
    rp.shutdown()
    
    print("Hi from my_first_package's subscriber.")
    
if __name__ == '__main__':
    main()
        
        
        
    
