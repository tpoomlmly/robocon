from sr.robot import *
import time
import smbus
import math

class DrivingMotor(): #manages a motor
    def __init__(self, motor, drivingWeight, steeringWeight, cap):
        self.motor = motor #refrence to the motor object
        self.drivingWeight = drivingWeight #this is how much this motor is affected by a forward input
        self.steeringWeight = steeringWeight #this is how much this motor is affected by a steering input
        self.cap = cap #maximum ammount of power to the motor
    def SetPower(self, speed):
        self.motor.power = speed * self.cap
        self.Cap()
    def Stop(self):
        self.motor.power = 0
    def Cap(self): #stops the motor power going too high
        if self.motor.power > self.cap:
            self.motor.power = self.cap
        if self.motor.power < -self.cap:
            self.motor.power = -self.cap

class Chassis (): #controling groups of motors on a vehicle
    def __init__(self, motors):
        self.motors = motors
        self.currentSpeed = 0 #the driving input
        self.currentSteering = 0 #the steering input
    def UpdateMotors(self):
        for x in range(0,len(self.motors)): #update all motors
            self.motors[x].SetPower((self.currentSpeed * self.motors[x].drivingWeight) + (self.currentSteering * self.motors[x].steeringWeight)) #apply steering + driving weights
    def SetSpeed(self,targetSpeed):
        self.currentSpeed = targetSpeed
        self.UpdateMotors()
    def SetSteering(self,targetSteering):
        self.currentSteering = targetSteering
        self.UpdateMotors()
    def StopTurning(self): #stops the robot from turning (keeps driving)
        self.currentSteering = 0
        self.UpdateMotors()
    def StopDriving(self): #stops the robot from driving (keeps turning)
        self.currentSpeed= 0
        self.UpdateMotors()
    def StopAll(self): #emergency stop/stops all movment
        self.currentSpeed = 0
        self.currentSteering = 0
        for x in range(0,len(self.motors)):
            self.motors[x].Stop()

def MoveToward ( target ):
    if target.centre.polar.rot_y > 0: #steer towards cube
        robotChassis.SetSteering(1)
    else:
        robotChassis.SetSteering(-1)
    time.sleep(abs(target.centre.polar.rot_y/turn))
    robotChassis.StopAll()
    time.sleep(0.2)
    if target.dist > 0.22: #steer towards cube
        robotChassis.SetSpeed(1)
    else:
        robotChassis.SetSpeed(-1)
    time.sleep(abs((target.dist - 0.2)/speed)) #drive to cube
    robotChassis.StopAll()
    time.sleep(0.2)

def Grab ():
    R.servos[0] = 100 #lower arm
    time.sleep(2.1)
    R.servos[0] = 0
    robotChassis.SetSpeed(0.5) #move forward
    time.sleep(0.8)
    robotChassis.StopAll()
    R.servos[1] = 30 #grab
    time.sleep(1)
    R.servos[0] = -100 #lift arm
    time.sleep(2.1)
    R.servos[0] = 0
    time.sleep(0.5)
    print "opening claw"
    R.servos[1] = -80 #release cube
    time.sleep(1)
    R.servos[1] = 0

def SentryMode ():
    robotChassis.SetSteering(1)
    time.sleep(0.2)
    robotChassis.StopAll()
    time.sleep(0.5)

def DumpAtBox():
    succses = False
    while succses == False:
        markers = R.see()
        buckets = []
        for marker in markers:
            if marker.info.marker_type == MARKER_BUCKET_SIDE:
                buckets.append(marker)
        if len(buckets) > 0: #checks if there are cubes
            target = buckets[0]#FindClosest(buckets)
            MoveToward(target)
            if .25 > target.dist and target.dist > .15:
                Dump()
                succses = True
        else:
            robotChassis.StopAll() #stops if nothing seen
            print "I SEE NOTHING"
            SentryMode()

def Dump ():
    robotChassis.SetSteering(1) #rotate 180
    time.sleep(1)
    robotChassis.StopAll() #stop
    time.sleep(0.5)
    robotChassis.SetSpeed(-0.5) #reverse
    time.sleep(1)
    robotChassis.StopAll() #stop
    time.sleep(0.5)
    
    R.servos[0] = 100 #lower arm
    R.servos[2] = 100 #dump bucket
    time.sleep(1.6)
    R.servos[0] = 0
    R.servos[2] = 0
    time.sleep(2)
    R.servos[0] = -100 #raise arm
    R.servos[2] = -100 #undump bucket
    time.sleep(1.6)
    R.servos[0] = 0
    R.servos[2] = 0
    
    robotChassis.SetSpeed(1) #forward
    time.sleep(0.5)
    robotChassis.StopAll() #stop

def Wiggle ():
    for i in range(3):
        robotChassis.SetSpeed(-1) #move forward
        time.sleep(0.2)
        robotChassis.SetSpeed(1) #move backward
        time.sleep(0.2)
    robotChassis.StopAll()
    
def Search (subject):
    markers = R.see()
    return markers

def FindClosest(markers):
    closest = None
    i = 0
    for marker in markers:
        if marker.info.marker_type == MARKER_TOKEN: #if a token
            if i == 0:
                closest = marker
                i += 1
            elif marker.dist < closest.dist: #This has to be this way because closest does not always have the attribute "dist"
                closest = marker
                i += 1
    if closest != None:
        return closest
    else:
        print "no markers seen"

#main       
R = Robot.setup()
R.init(smbus.SMBus(1))

#R.gpio.digital_write(1, True)# Power is allowed to flow into the servos
for i in range(3):
    R.servos[i] = 0
R.wait_start()

robotChassis = Chassis([DrivingMotor(R.motors[0].m0,1,-1,60),DrivingMotor(R.motors[0].m1,1,1,60)]) #setup motors + chassis

speed = 0.9
turn = 280
cubeCount = 0

while True:
    #--markers = Search()
    markers = R.see()
    cubes = []
    for marker in markers:
        if marker.info.marker_type == MARKER_TOKEN:
            cubes.append(marker)
    if len(cubes) > 0: #checks if there are cubes
        target = FindClosest(cubes)
        print "OHHH"
        MoveToward(target)
        if .25 > target.dist and target.dist > .2:
            holding = False
            while holding == False:
                Grab()
                time.sleep(1)
                if len(R.see()) == 0 or True:
                    holding = True
            Wiggle()
            cubeCount = cubeCount + 1
            print "holding " + str(cubeCount) + " cubes"
            if cubeCount >= 2:
                print "holding max cubes achieved, dumping"
                DumpAtBox()
                cubeCount = 0
    else:
        robotChassis.StopAll() #stops if nothing seen
        print "I SEE NOTHING"
        SentryMode()
