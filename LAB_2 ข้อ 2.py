import math

class Spherical:

    def __init__(self,r) :

        self.radius = r

    def changeR(self,Radius):

        self.radius = int(r2)
       
    def findVolume(self) :

        pass
        #print ( (4/3) * math.pi * ( self.radius * self.radius * self.radius ) )

    def findArea(self) :

        pass
        #print ( 4 * math.pi * ( self.radius * self.radius * self.radius ) )

    def __str__(self) :

        return 'Radius =' + str(self.radius) + ' Volumn = ' + str((4/3) * math.pi * ( self.radius * self.radius * self.radius )) + " Area = " + str(4 * math.pi * ( self.radius * self.radius ))

r1 , r2 = input("Enter R : ").split()

R1 = Spherical(int(r1))

print(type(R1))

print(dir(R1))

print(R1)

R1.changeR(int(r2))

print(R1)

