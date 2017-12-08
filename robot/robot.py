#!/usr/bin/env python3
import magicbot
import wpilib

from robotpy_ext.control.button_debouncer import ButtonDebouncer
from networktables.util import ntproperty
from components import drive

from robotpy_ext.common_drivers import navx

from networktables.networktable import NetworkTable

class Robot(magicbot.MagicRobot):
    drive = drive.Drive

    def createObjects(self):
        self.dashboard = NetworkTable.getTable('SmartDashboard')
        self.drive_dashboard = self.dashboard
        self.navX = navx.AHRS.create_spi()

        self.drive_lf_motor = wpilib.Victor(0)
        self.drive_lr_motor = wpilib.Victor(1)
        self.drive_rf_motor = wpilib.Victor(2)
        self.drive_rr_motor = wpilib.Victor(3)

        self.robot_drive = wpilib.RobotDrive(self.drive_lf_motor, self.drive_lr_motor, self.drive_rf_motor, self.drive_rr_motor)

        self.left_stick = wpilib.joystick.Joystick(0)
        self.right_stick = wpilib.joystick.Joystick(1)

    def autonomous(self):
        """pass for now"""
        pass

    def teleopInit(self):
        """Do when teleoperated mode is started."""
        self.drive.stop()

    def disabledPeriodic(self):
        """Repeat periodically while robot is disabled. Usually emptied. Sometimes used to easily test sensors and other things."""

    def teleopPeriodic(self):
        """Do as fast as possible when teleoperated mode is on"""
        pass

    def disabledInit(self):
        self.drive.stop()

if __name__ == '__main__':
    wpilib.run(Robot)
