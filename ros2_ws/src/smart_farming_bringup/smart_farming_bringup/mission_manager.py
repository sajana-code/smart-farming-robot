import rclpy
from rclpy.node import Node

class MissionManager(Node):
    def __init__(self):
        super().__init__('mission_manager')
        self.get_logger().info('=========================================')
        self.get_logger().info('SMART FARMING ROBOT')
        self.get_logger().info('Mission Manager Node has been started')
        self.get_logger().info('=========================================')

def main(args=None):
    rclpy.init(args=args)
    node = MissionManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

    if __name__ == '__main__':
        main()