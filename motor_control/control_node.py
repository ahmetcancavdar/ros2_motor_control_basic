import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys, tty, termios

class KeyboardControl(Node):
    def __init__(self):
        super().__init__('keyboard_control_node')
        self.publisher_ = self.create_publisher(String, 'motor_commands', 10)
        self.get_logger().info("Kontrol Hazir: W=İleri, S=Geri, X=Dur")
        self.run_loop()

    def run_loop(self):
        msg = String()
        while rclpy.ok():
            key = self.get_key()
            if key in ['w', 's', 'x']:
                msg.data = key
                self.publisher_.publish(msg)
            elif key == '\x03': # CTRL+C
                break

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardControl()
    rclpy.shutdown()
