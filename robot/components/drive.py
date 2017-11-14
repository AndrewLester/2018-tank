import wpilib

from networktables import NetworkTable
from networktables.util import ntproperty
import math

ENCODER_ROTATION = 1023
WHEEL_DIAMETER = 7.639
class Drive:
    """Encapsulates wpilib.RobotDrive"""
    dashboard = NetworkTable
    robot_drive = RobotDrive
    leftStick = Joystick
    rightStick = Joystick

    def __init__(self):
        self.angle_left = 0
        self.angle_right = 0

    def stop(self):
        self.move(angle_left=0, angle_right=0)

    def move(self, angle_left=None, angle_right=None):
        self.angle_left = angle_left
        self.angle_right = angle_right

    def stick_move(self, left_stick, right_stick):
        self.angle_left = left_stick.getY()
        self.angle_right = right_stick.getY()


    def execute(self):
        """Executes current speed and rotation values"""
        if self.angle_left is None and self.angle_right is None:
            return

        self.robot_drive.tankDrive(leftValue=self.leftStick, rightValue=self.rightStick)
        self.angle_left = None
        self.angle_right = None
