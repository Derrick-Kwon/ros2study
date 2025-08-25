from my_first_package_msgs.srv import MultiSpawn
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn

import time
import numpy as np
import rclpy as rp
import rclpy.node
from rclpy.node import Node


class MultiSpawning(Node):
    def __init__(self):
        super().__init__('multi_spawning')
        self.server = self.create_service(MultiSpawn, 'multi_spawn', self.callback_service) #누가 호출할시 callback_service를 실행 
        self.teleport = self.create_client(TeleportAbsolute, 'turtle1/teleport_absolute')
        self.spawn = self.create_client(Spawn, '/spawn')
        
        self.req_teleport = TeleportAbsolute.Request() #텔레포트 absolute에서 request만 가져오는거ㅇㅇ
        self.req_spawn = Spawn.Request() #request하는 spawn
        self.center_x = 5.54
        self.center_y = 5.54
    
   
    def calc_position(self, n, r):
        gap_theta = 2 * np.pi / n
        theta = [i * gap_theta for i in range(n)]
        x =  [ r*np.cos(th) for th in theta]
        y =  [ r*np.sin(th) for th in theta]
        return x, y, theta
    
    
    def callback_service(self, request, response):
        x, y, theta = self.calc_position(request.num, 3)
        for n in range(len(theta)):
            self.req_spawn.x = x[n] + self.center_x
            self.req_spawn.y = y[n] + self.center_y
            self.req_spawn.theta = theta[n]
            self.spawn.call_async(self.req_spawn) #spawn 요청

            time.sleep(0.1) #spawn이 완료될 때까지 기다리기

            
        response.x = x
        response.y = y
        response.theta = theta
        
        return response
 


def main(args = None):
    rp.init(args = args)
    node = MultiSpawning()
    rp.spin(node)
    rp.shutdown()
    
    
if __name__ == '__main__':
    main()    