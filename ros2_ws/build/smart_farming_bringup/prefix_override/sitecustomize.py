import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/parallels/smart-farming-robot/ros2_ws/install/smart_farming_bringup'
