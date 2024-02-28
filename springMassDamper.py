import numpy as np
import matplotlib as plt

#Using: https://fastlabtutorials.blogspot.com/2015/04/everything-you-need-to-know-to-code.html
print('Spring Mass Damper Program')

#Initialize State Vector
state = np.asarray([1.0,-2.0])

#Create a Derivatives Function
# def Derivatives(state):
#     stateDot = np.asarray([0.0,0.0])
#     return stateDot

#Now, code in the math model for a spring damper. (Equations of Motion)
def Derivatives(state):
    m = 1.0
    c = 2.0
    k = 3.0
    ucontrol = 0.0
    A = np.asarray([[0.0,1.0],[-k/m,-c/m]])
    B = np.asarray([0.0,1.0/m])
    stateDot = np.dot(A,state) + B*ucontrol
    return stateDot

stateDot = Derivatives(state)

#simulate for 10 sec. We create a loop to compute the state derivatives over and over.
#make a massive time vector and then make a for loop that starts at 0 and ends at last time data point.

tfinal = 10.0
tinitial = 0.0
timestep = 0.01
time = np.arange(tinitial, tfinal+timestep,timestep)

#Create state Array

stateOut = np.zeros((2,len(time)))

for idx in range(0,len(time)):
    print('Simulation', time[idx]/tfinal*100, 'Percent Complete')
    stateOut[:,idx] = state
    stateDot = Derivatives(state)
    state += stateDot*timestep
#Now add Euler's Method to actually propogate the state forward. Could also use RK4 but gonna learn Euler's Method.

