from sr.robot import *
import time
import smbus
#from math import sin, cos, radians

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

def MoveToward ( target, distance ):
    if target.centre.polar.rot_y > 0: #steer towards cube
        robotChassis.SetSteering(1)
        lastCubeRight = True
        print "RIIIIGHT"
    else:
        robotChassis.SetSteering(-1)
        lastCubeRight = False
        print "LEEEEFT"
    time.sleep(abs(target.centre.polar.rot_y/turn))
    robotChassis.StopAll()
    time.sleep(0.2)
    if target.dist > distance: #steer towards cube
        robotChassis.SetSpeed(1)
    else:
        robotChassis.SetSpeed(-1)
    time.sleep(abs((target.dist - distance)/speed)) #drive to cube
    robotChassis.StopAll()
    time.sleep(0.2)

def Grab ():
    print "ATTACKING THE CUBE"
    R.servos[0] = 100 #lower arm
    time.sleep(2.3)
    R.servos[0] = 0
    robotChassis.SetSpeed(1) #move forward
    time.sleep(0.8)
    robotChassis.StopAll()
    R.servos[1] = 30 #grab
    time.sleep(1)
    R.servos[0] = -100 #lift arm
    time.sleep(2.3)
    R.servos[0] = 0
    time.sleep(0.3)
    print "opening claw"
    R.servos[1] = -80 #release cube
    time.sleep(1)
    R.servos[1] = 0

def Setup ():
    R.servos[0] = 100 #lower arm
    time.sleep(0.5)
    R.servos[0] = 0

def SentryMode ():
    if lastCubeRight == True:
        robotChassis.SetSteering(1)
        print "target last seen to the right"
    else:
        robotChassis.SetSteering(-1)
        print "target last seen to the left"
    time.sleep(0.5)
    robotChassis.StopAll()

def GoToZone():
    giveUp = 0
    unsuccses = True
    while ((unsuccses)):#and (giveUp < 7)):
        print "giving up:", giveUp
        time.sleep(0.5)
        markers = R.see(res=(1296, 736))
        buckets = []

        for marker in markers:
            isHome = False
            for i in range(5):
                if marker.info.code == i + (R.zone * 6):
                    isHome = True
            if marker.info.marker_type == MARKER_ARENA and isHome:
                buckets.append(marker)
        if len(buckets) > 0: #checks if there are cubes'
            print "going home"
            target = buckets[0]#FindClosest(buckets)
            MoveToward(target, 1)
            if 0.5 > target.dist  and target.centre.polar.rot_y > -20:
                GoToBox()
                unsuccses = False
        else:
            robotChassis.StopAll() #stops if nothing seen
            print "IM LOST"
            SentryMode()
            giveUp += 1
    giveUp = 0
    print "gave up"

def ZoneDump ():
    robotChassis.SetSteering(-1) #rotate 180
    time.sleep(2)
    robotChassis.StopAll() #stop
    time.sleep(0.1)
    robotChassis.SetSpeed(-0.7) #reverse
    time.sleep(4)
    robotChassis.StopAll() #stop
    time.sleep(0.1)

    robotChassis.SetSpeed(1) #forward
    time.sleep(0.5)
    robotChassis.StopAll() #stop
    time.sleep(0.1)
    
    R.servos[0] = 100 #lower arm
    R.servos[2] = 100 #dump bucket
    time.sleep(1.6)
    R.servos[0] = 0
    R.servos[2] = 0
    time.sleep(1.8)
    R.servos[0] = -100 #raise arm
    R.servos[2] = -100 #undump bucket
    time.sleep(1.6)
    R.servos[0] = 0
    R.servos[2] = 0
    robotChassis.SetSteering(-1) #rotate left a bit
    time.sleep(0.5)
    robotChassis.StopAll()

    robotChassis.SetSpeed(1) #forward
    time.sleep(3)
    robotChassis.StopAll() #stop

def GoToBox():
    giveUp = 0
    unsuccses = True
    while ((unsuccses) and (giveUp < 7)):
        print "giving up:", giveUp
        time.sleep(0.5)
        markers = R.see(res=(1920, 1440))
        buckets = []
        for marker in markers:
            if marker.info.marker_type == MARKER_BUCKET_SIDE and (R.zone == marker.info.code - 72 or R.zone == marker.info.code - 76):
                buckets.append(marker)
        if len(buckets) > 0: #checks if there are cubes'
            print "going home"
            target = buckets[0]#FindClosest(buckets)
            MoveToward(target, 0.2)
            if .25 > target.dist and target.dist > .15 and 20 > target.centre.polar.rot_y and target.centre.polar.rot_y > -20:
                Dump()
                unsuccses = False
        else:
            robotChassis.StopAll() #stops if nothing seen
            print "IM LOST"
            SentryMode()
            giveUp = giveUp + 1
    giveUp = 0
    print "gave up"

def Dump ():
    robotChassis.SetSteering(-1) #rotate 180
    time.sleep(2)
    robotChassis.StopAll() #stop
    time.sleep(0.5)
    robotChassis.SetSpeed(-0.7) #reverse
    time.sleep(1)
    robotChassis.StopAll() #stop
    time.sleep(0.5)
    
    R.servos[0] = 100 #lower arm
    R.servos[2] = 100 #dump bucket
    time.sleep(1.6)
    R.servos[0] = 0
    R.servos[2] = 0
    time.sleep(1)
    R.servos[0] = -100 #raise arm
    R.servos[2] = -100 #undump bucket
    time.sleep(1.6)
    R.servos[0] = 0
    R.servos[2] = 0
    
    robotChassis.SetSpeed(1) #forward
    time.sleep(3)
    robotChassis.StopAll() #stop

def Wiggle ():
    print "WIGGLE"
    for i in range(3):
        robotChassis.SetSpeed(-1) #move backward
        time.sleep(0.2)
        robotChassis.SetSpeed(1) #move forward
        time.sleep(0.2)
    robotChassis.StopAll() #stop
    
def Search (subject):
    markers = R.see()
    return markers

def FindClosest(markers):
    closest = None
    i = 0
    for marker in markers:
        if marker.info.marker_type == MARKER_TOKEN: #if a token
            if i == 0 or marker.dist < closest.dist: #This has to be this way because closest does not always have the attribute "dist"
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

speed = 0.5
#speed = 0.6
turn = 200
cubeCount = 0
lastMarker = -1
lastCubeRight = True
giveUp = 0
safe = []
holding = []

Setup()

while True:
    #--markers = Search()
    time.sleep(0.5)
    markers = R.see(res=(640 ,480))
    cubes = []
    for marker in markers:
        if marker.info.marker_type == MARKER_TOKEN and not(marker.info.code in safe):
            cubes.append(marker)
    if len(cubes) > 0: #checks if there are cubes
        target = FindClosest(cubes)
        if target.info.code == lastMarker:
            lastMarker = -1
        print "OHHH"
        MoveToward(target, 0.25)
        if .3 > target.dist and target.dist > .2 and 20 > target.centre.polar.rot_y and target.centre.polar.rot_y > -20:
            lastMarker = target.info.code
            Grab()
            markers = R.see(res=(640, 480)) #checking to see if picked up
            cubes = []
            for marker in markers:
                if marker.info.marker_type == MARKER_TOKEN:
                    cubes.append(marker)
            if len(cubes) > 0: #checks if there are cubes
                target = FindClosest(cubes)
                if target.info.code != lastMarker: #end of pick up check
                    print "picked up the cube"
                    cubeCount = cubeCount + 1
                    holding.append(lastMarker)
                    if cubeCount != 2:
                        Wiggle()
                else:
                    print "failed to pick up cube"
            else:
                print "picked up the cube"
                cubeCount = cubeCount + 1
                holding.append(lastMarker)
                if cubeCount != 2:
                    Wiggle()
            print "holding", str(cubeCount), " cubes"
    else:
        robotChassis.StopAll() #stops if nothing seen
        print "I SEE NOTHING"
        SentryMode()
    if cubeCount >= 2:
        print "holding max cubes achieved, dumping"
        # GoToBox()
        GoToZone()
        for cube in holding:
            safe.append(cube)
        holding = []
        print safe
        cubeCount = 0
