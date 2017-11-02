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

    def __init__(self):
        self.yaw = self.

    def stop(self):
        self.move(angle_deg=0, power=0)

    def move(self, angle_deg: int=0, angle_rad: float=0, power=0):
        pass

    def execute(self):
        """Executes current speed and rotation values"""
        if(self.isTheRobotBackwards):
            self.robot_drive.arcadeDrive(-self.y, -self.rotation / 2, self.squaredInputs)
        else:
            self.robot_drive.arcadeDrive(self.y, -self.rotation * self.halfRotation, self.squaredInputs)


        # by default, the robot shouldn't move
        self.y = 0
        self.rotation = 0
