import wpilib
import wpilib.drive

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.joystick = wpilib.Joystick(0)
        self.motor_gauche = wpilib.VictorSP(0)
        self.motor_droit = wpilib.VictorSP(1)
        self.drive = wpilib.drive.DifferentialDrive(self.motor_gauche, self.motor_droit)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(-1 * self.joystick.getY(), self.joystick.getX())



if __name__ == '__main__':
    wpilib.run(Robot)
