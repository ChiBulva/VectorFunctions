'''
=================
Plotting of Input Vectors
=================

'''

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt, mpld3


def Plot_Input_Vectors(Plot_List):
    count = 0
    for Vector in Plot_List:
        print(Plot_List[count])
        X, Y, Z = Plot_List[count]

        ax.plot(X,Y,Z, 'b->')
        ax.plot([X[0]],[Y[0]],[Z[0]], 'bo')
        count = count + 1

    return ax

def Input_Points_To_Matplotlib(Input_Points):
    print("Length: "+str(len(Input_Points)))
    Plot_List = Input_Points
    Number_Of_Vectors = len(Input_Points)
    Loop_Count = Number_Of_Vectors*2

    Plot_List = []
    for Vector_Number in range(Number_Of_Vectors):
        X = []
        Y = []
        Z = []
        X.append(Input_Points[Vector_Number][0][0])
        X.append(Input_Points[Vector_Number][1][0])
        Y.append(Input_Points[Vector_Number][0][1])
        Y.append(Input_Points[Vector_Number][1][1])
        Z.append(Input_Points[Vector_Number][0][2])
        Z.append(Input_Points[Vector_Number][1][2])

        Plot_List.append([X,Y,Z])

        '''
        for Position in range(2):
            for Axis_Position in range(3):
                print("Printing -> Array[",
                        str(Vector_Number)+"][",
                        str(Position)+"][",
                        str(Axis_Position)+"]: ",
                        str(Input_Points[Vector_Number][Position][Axis_Position]))
        '''

    return Plot_List

def Get_Int(Axis, Vector_Number, Position):
    return int(input(Position+" -> Enter axis "+Axis+" on Vector #"+str(Vector_Number)+": "))

def Get_PlotPoint3D(Vector_Number, Position):
    PlotPoint3D = [ Get_Int('X', Vector_Number, Position), \
                    Get_Int('Y', Vector_Number, Position), \
                    Get_Int('Z', Vector_Number, Position)]

    return PlotPoint3D # [0,0,0]

def Input_To_Vector(Input_Points):
    Vector = Input_Points
    return Vector

def Input_Mode():
    InputMode = input("Would you like to enter the Input Manually (1) or with a file (2)?: ")
    if(InputMode=='1'):
        return Get_Input()
    elif(InputMode=='2'):
        return Get_File()

def Get_File():

    temp = open("text.txt",'r').read().split('\n')
    Vector_Array = []

    for vector in temp:
        appendlist = []
        words = vector.split("|")
        X,Y,Z = words[0].split(",")
        X2,Y2,Z2 = words[1].split(",")
        vec1 = [int(X),int(Y),int(Z)]
        vec2 = [int(X2),int(Y2),int(Z2)]
        appendlist.append(vec1)
        appendlist.append(vec2)
        #print(appendlist)
        Vector_Array.append(appendlist)

    return Vector_Array		
	
def Get_Input():
    #Add file upload functionality later
    Number_Of_Vectors = input("How Many Vectors do you want to input?: ")

    #print("\n**Defaul Value added!!!!**\n")

    Vector_Array = []

    #IMPORTANT!!! Uncomment for user input
    for Vector_Number in range(int(Number_Of_Vectors)):
        print(1)
        Vector_Array.append(
            [Get_PlotPoint3D(Vector_Number+1, 'Start'),
            Get_PlotPoint3D(Vector_Number+1, 'Finish')])

    return Vector_Array

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
#X, Y, Z = axes3d.get_test_data(0.05)
#Z = np.array([[0],[0]])

#

X,Y,Z = [1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]

#Gets user Input
Input_Points = Input_Mode()
print(Input_Points)

#Changes the inputs to somehting the progam can read
Plot_List = Input_Points_To_Matplotlib(Input_Points)
print(Plot_List)
 
ax = Plot_Input_Vectors(Plot_List)

ax.view_init(40, 35)

plt.show()


#_________________________________________
#Old things:

#X,Y,Z = [0,1],[0,1],[0,1]
#X2,Y2,Z2 = [2,3],[2,3],[2,3]

#X = [[-30  -29.5 -29  :  28.5  29   29.5]]

#Y = [[-30  -30  -30  : -30  -30  -30 ]]

#Z = [[-0.00982064 -0.0113957  -0.01319036 : -0.01522953 -0.01319036 -0.0113957]]

# Plot a basic wireframe.
#ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3)
