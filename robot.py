import wpilib
import wpilib.drive

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.joystick = wpilib.Joystick(0)
        self.motor_gauche = wpilib.VictorSP(0)
        self.motor_droit = wpilib.VictorSP(1)
        self.drive = wpilib.drive.DifferentialDrive(self.motor_gauche, self.motor_droit)
        self.encoder = wpilib.Encoder(0, 1)
        self.gyro = wpilib.AnalogGyro(1)

    def autonomousPeriodic(self):
        if self.gyro.getAngle() <= 89:
            self.drive.arcadeDrive(0, 1)
        else:
            self.drive.arcadeDrive(0, 0)

    def teleopPeriodic(self):
        self.drive.arcadeDrive(-1 * self.joystick.getY(), self.joystick.getX())



if __name__ == '__main__':
    wpilib.run(Robot)
