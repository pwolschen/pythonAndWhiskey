

def acceleration():
    return -9.81
    
def velocity(startingVelocity, acceleration, timestep):
    return startingVelocity + acceleration*timestep
    
def displacement(startingDisplacement, velocity, timestep):
    return startingDisplacement + velocity*timestep

height = float(input("Drop height: "))
timestep = .001


v = 0
while height > 0:
    a = acceleration()
    v = velocity(v, a, timestep)
    height = displacement(height, v, timestep)
    print("{},{},{}".format(a,v,height))