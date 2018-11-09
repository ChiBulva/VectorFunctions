#	Websites: 
#
#		ScyPi VectorCalc: https://docs.sympy.org/latest/modules/physics/vector/vectors.html#vector
#		

print("This code executes before main.")

# UNIT_VECTOR = (0,0,0)
x, y, x

UNIT_VECTOR = (0,0,1)

def main():
    print("This code executes after main.")

    Vector_1 = (Scalar, Unit_Vector)

    AddVectors(Vector_1, Vector_2)

#Adds two vectors result will return
def AddVectors(Vector_1, Vector_2, PrintToggle):
    print("Function B")
    Result_Vector = Vector_1 + Vector_2
    if(PrintToggle==True):
        print("Result_Vector: "+str(Result_Vector))

if __name__ == '__main__':
    main()
    functionB()

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
#                             \
#
##############################################################################################################