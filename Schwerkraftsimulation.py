
class ball():
    a = 0
    v = 0

    def __init__(self):
        self.height = 0
        
    def __init__(self, height):
        self.a = 0
        self.v = 0
        self.height = height
        
    


def acceleration():
    return -9.81
    
def velocity(startingVelocity, acceleration, timestep):
    return startingVelocity + acceleration*timestep
    
def displacement(startingDisplacement, velocity, timestep):
    return startingDisplacement + velocity*timestep

height = float(input("Drop height: "))
timestep = .001

ballA = ball(height)
v = 0
while ballA.height > 0:
    ballA.a = acceleration()
    ballA.v = velocity(ballA.v, ballA.a, timestep)
    ballA.height = displacement(ballA.height, ballA.v, timestep)
    print("{},{},{}".format(a,v,height))