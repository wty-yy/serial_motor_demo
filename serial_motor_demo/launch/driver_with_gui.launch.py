from launch import LaunchDescription
from launch.actions import TimerAction, RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_path

def generate_launch_description():

  pkg_name = "serial_motor_demo"

  path_driver_config = str(get_package_share_path(pkg_name) / "config/driver.yaml")

  driver = Node(
    package="serial_motor_demo",
    executable="driver",
    name="serial_arduino_driver",
    output="both",
    parameters=[path_driver_config]
  )

  gui = Node(
    package="serial_motor_demo",
    executable="gui",
    name="serial_arduino_gui",
    output="both"
  )

  delayed_gui = RegisterEventHandler(
    event_handler=OnProcessStart(
      target_action=driver,
      on_start=[
        TimerAction(period=3.0, actions=[gui])
      ]
    )
  )

  return LaunchDescription([
    driver, delayed_gui
  ])