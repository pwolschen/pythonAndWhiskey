#benötigte Formeln:
    #a=9,81m/s² 
    #v=V0+a*t
    #x=x0+0,5*(Vn+Vn+1)*t

def V(Geschwindigkeit,inkrement):
    Geschwindigkeit=Geschwindigkeit + (float(inkrement)*Beschleunigung)
    return Geschwindigkeit
def X(Position,Veränderung):
    Position=Startposition+((Geschw*inkrement)+(0.5*Beschleunigung*inkrement**2))
    return Position
def A(Geschw,inkrement):
    Beschleunigung=((Geschw**2)/(2*inkrement))
    return Beschleunigung
    
#Try Cath
try: 
    #Falldauer
    Falldauer =float( input ("Wie lange dauerte der Fall an"))
    if (Falldauer < 0  ):
        print ("Realy Nigger???")
except: 
    print ("Bitte nur Zahlenwerte")
    exit ()
try: 
    #Starthöhe
    Starthöhe =float( input ("Starthöhe"))
    if (Starthöhe < 0  ):
        print ("Realy Nigger???")
except: 
    print ("Bitte nur Zahlenwerte")
    exit ()
    
try:
    #Schritte
    Schritte =float(input ("Inkrementweite"))
    if (Schritte < 0 ):
        print ("Realy Nigger")
except:
    print ("Bitte nur Zahlenwerte")
    exit()

#Inkrement Zähler
gesamtinkrement = Falldauer 
#Startwerte
Beschleunigung=float (9.81)
#print (gesamtinkrement)
Geschwindigkeit = float(0)
Startposition = float(0)
inkrement =float(0)
Position = float(0)
Veränderung = ((Geschwindigkeit*inkrement)*(0.5*Beschleunigung*inkrement**2))
#print (inkrement)
#Wiederholung
while (gesamtinkrement > inkrement) :
    # Geschwindigkeit
    Geschw = V(Geschwindigkeit,inkrement)
    #Position
    Pos = X(Position,Veränderung)
    #inkrementenzähler
    inkrement = inkrement + Schritte
    #Beschleunigung
    Besch = A(Geschw,inkrement)
    über0 = (Starthöhe - Pos)
    if (gesamtinkrement < inkrement) :
        print ("Geschwindigkeit")
    if (gesamtinkrement < inkrement) :
        print (Geschw)
    if (gesamtinkrement < inkrement) :
        print ("Position")
    if (gesamtinkrement < inkrement) :
        print (Pos)
    if (gesamtinkrement < inkrement) :
        print ("Höhe über Null")
    if (gesamtinkrement < inkrement) :
        print (über0)
    if (gesamtinkrement < inkrement) :
        print ("Beschleunigung")
    if (gesamtinkrement < inkrement) :
        print (Besch)
   # if (gesamtinkrement < inkrement) :
   #     print (inkrement)
   # if (gesamtinkrement < inkrement) :
   #     print (gesamtinkrement)