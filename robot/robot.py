#!/usr/bin/env python3
import magicbot
import wpilib

from robotpy_ext.control.button_debouncer import ButtonDebouncer
from networktables.util import ntproperty
from components import drive

from robotpy_ext.common_drivers import navx

from networktables.networktable import NetworkTable

class Robot(MagicRobot):
    drive = drive.Drive

    def createObjects(self):
        self.dashboard = NetworkTable.getTable('SmartDashboard')
        self.drive_dashboard = self.dashboard
        self.drive_robot_drive = wpilib.RobotDrive

        self.navX = navx.AHRS.create_spi()
        self.robot_drive = wpilib.RobotDrive(self.lf_motor, self.lr_motor, self.rf_motor, self.rr_motor)

    def autonomous(self):
        """pass for now"""
        pass

    def disabledInit(self):
        self.drive.stop()

if __name__ == '__main__':
    wpilib.run(Robot)
