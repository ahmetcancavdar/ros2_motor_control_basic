import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class MotorDriver(Node):
    def __init__(self):
        super().__init__('motor_driver_node')
        self.subscription = self.create_subscription(String, 'motor_commands', self.listener_callback, 10)
        # Port ismini ve hızı kontrol et
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
            self.get_logger().info('Arduino baglantisi basarili!')
        except Exception as e:
            self.get_logger().error(f'Baglanti hatasi: {e}')

    def listener_callback(self, msg):
        self.get_logger().info(f'Gelen Komut: {msg.data}')
        self.ser.write(msg.data.encode())

def main(args=None):
    rclpy.init(args=args)
    node = MotorDriver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
