
class ball():
    a = 0
    v = 0

    # def __init__(self):
        # self.height = 0
        
    def __init__(self, ballheight=0):
        self.a = 0
        self.v = 0
        self.height = ballheight
        

def sim(ball, timestep):
    ball.a = acceleration()
    ball.v = velocity(ball.v, ball.a, timestep)
    ball.height = displacement(ball.height, ball.v, timestep)
    return ball

def acceleration():
    return -9.81
    
def velocity(startingVelocity, acceleration, timestep):
    return startingVelocity + acceleration*timestep
    
def displacement(startingDisplacement, velocity, timestep):
    return startingDisplacement + velocity*timestep

height = float(input("Drop height: "))
timestep = .001

ballArr = []
for i in range(0,100):
    ballArr.append(ball(height))
print(ballArr)
print(ballArr[0])
print(ballArr[0].height)
#exit()
v = 0
while ballA.height > 0:
    ballArr[0] = sim(ballArr[0], timestep)
    ballArr[1] = sim(ballArr[1], timestep)
    print("A: {},B: {}".format(ballArr[0].height, ballArr[1].height))