# ROS/Arduino Serial Motor Demo

This is demonstration of a ROS 2 interface to an Arduino running differential-drive motor control code.

The corresponding Arduino code can be found [here](https://github.com/joshnewans/ros_arduino_bridge), which is itself a fork of [this repo](https://github.com/hbrobotics/ros_arduino_bridge), which also contains a similar implementation for the ROS/Python/Client side (ROS 1 though).

## Components

The `serial_motor_demo` package consists of two nodes, `driver.py` and `gui.py`. The idea is that the driver can be run on an onboard PC inside a robot (e.g. a Raspberry Pi), interfacing with the lower-level hardware. The driver exposes motor control through ROS topics (see below), which are to be published by the user's software.

The GUI provides a simple interface for development and testing of such a system. It publishes and subscribes to the appropriate topics.


## Driver configuration & usage

The driver has a few parameters:

- `encoder_cpr` - Encoder counts per revolution
- `serial_port` - Serial port to connect to (default `/dev/ttyACM0`)
- `baud_rate` - Serial baud rate (default `57600`)
- `serial_debug` - Enables debugging of serial commands (default `false`)

To run, e.g.
```bash
ros2 run serial_motor_demo driver --ros-args -p encoder_cpr:=442 -p serial_port:=/dev/ttyACM0 -p baud_rate:=57600 -p serial_debug:=True
```

It makes use of the following topics
- `motor_command` - Subscribes a `MotorCommand`, in rads/sec for each of the two motors
- `motor_vels` - Publishes a `MotorVels`, motor velocities in rads/sec
- `encoder_vals` - Publishes an `EncoderVals`, raw encoder counts for each motor



## GUI Usage

Has two modes, one for raw PWM input (-255 to 255) and one for closed-loop control (rpm). In this mode you must first set the limits for the sliders.

## Launch file usage

Update config file `./serial_motor_demo/config/driver.yaml`, then
```bash
ros2 launch serial_motor_demo driver_with_gui.launch.py
```


## Update

wty-yy changes:
1. Captiable commands with my [arduino_pid_controlled_motor](https://github.com/wty-yy/arduino_pid_controlled_motor/)
    - `p <pwm1> <pwm2>`: pwm control
    - `s <rpm1> <rpm2>`: rpm control
2. Add a three seconds sleep before driver controlling (for stability)
3. Change colsed-loop control from `encode_revolution/(s*loop_rate)` to `rpm (wheel revolution per minute)`



