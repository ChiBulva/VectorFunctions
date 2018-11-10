#By: Travis Gray 11/8/2018

#	Websites: 
#
#		ScyPi VectorCalc: https://docs.sympy.org/latest/modules/physics/vector/vectors.html#vector
#		

import math

print("This code executes before main.")

# UNIT_VECTOR = (0,0,0)
#x, y, x

UNIT_VECTOR = (0,0,1)

def SqRt(x):
	return(math.sqrt(int(x)))

def distance(Vector_1, Vector_2, Multiplayer, PrintToggle):
    Vector_1 = (1,43,5)
    Vector_2 = (1,234234,1000)
	
    Multiplayer = 1
    print(Vector_1)
    (x1,y1,z1) = Vector_1
    (x2,y2,z2) = Vector_2
	
    Distance = SqRt( math.pow(int(x2)-int(x1),2) + math.pow(int(y2)-int(y1),2) + math.pow(int(z2)-int(z1),2) )
    Distance = Distance * Multiplayer
    print(Distance)

def main():
    print("This code executes after main.")
    distance(1, 1, 1, 2)
##    Vector_1 = (Scalar, Unit_Vector)

#    AddVectors(Vector_1, Vector_2)

#Adds two vectors result will return
def AddVectors(Vector_1, Vector_2, PrintToggle):
    print("Function B")
    Result_Vector = Vector_1 + Vector_2 
    if(PrintToggle==True):
        print("Result_Vector: "+str(Result_Vector))

if __name__ == '__main__':
    main()

##############################################################################################################
#
#	Visul Examples	
#
##############################################################################################################	
#	
#   Basic Spacial Area	[1]
#			  [-1]		|
#                \		|
#                       |Y
#                  \    |
#                       |
#                    \  |
#                       |
#[-1]  _  _  _  _  _ (0,0,0)_________________X [1]
#                       \
#                       |\
#                         \
#                       |  \
#                           \
#                       |   Z\
#                     [-1]     \
#							   [1]
#
#     UNIT_VECTOR Area	|
#                \		|
#                       |Y
#                  \    |
#                       |
#                    \  |
#                       |           (1,0,0)
#   _  _  _  _  _  _  _ .@  @  @  @ <\/>_____X
#                       \
#                       |\
#                         \
#                       |  \
#                           \
#                       |   Z\
#                             \
#
#     (1,-1,0) Area	|
#                \		|
#                       |Y
#                  \    |
#                       |
#                    \  |
#                       |           (1,0,0)
#   _  _  _  _  _  _  _ .___________________ X   
#                       \@                  |
#                       |\   @
#                         \      @          |
#                       |  \         @
#                           \            @  |
#                       |_ _Z\_ _ _ _ _ _ _<\/> (1,-1,0)
#                             \
#
#     (1,0,1) Area	|
#                \		|
#                       |Y
#                  \    |
#                       |
#                    \  |
#                       |           (1,0,0)
#   _  _  _  _  _  _  _ .___________________ X
#                       \@                   \
#                       |\   @                \
#                         \       @            \
#                       |  \           @        \
#                           \               @    \
#                       |   Z\_ _ _ _ _ _ _ _ _ _<\/> (1,0,1)
#                             
#
##############################################################################################################
