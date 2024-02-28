import numpy as np
import matplotlib.pyplot as plt

#Using: https://fastlabtutorials.blogspot.com/2015/04/everything-you-need-to-know-to-code.html
print('Spring Mass Damper Program')

#Initialize State Vector
state = np.asarray([1.0,-2.0])

#Create a Derivatives Function
#Now, code in the math model for a spring damper. (Equations of Motion)
def Derivatives(state):
    m = 1.0
    c = 2.0
    k = 3.0
    A = np.asarray([[0.0,1.0],[-k/m,-c/m]])
    B = np.asarray([0.0,1.0/m])
    stateDot = np.dot(A,state) + B*ucontrol
    return stateDot


#simulate for 10 sec. We create a loop to compute the state derivatives over and over.
#make a massive time vector and then make a for loop that starts at 0 and ends at last time data point.

tfinal = 10.0
tinitial = 0.0
timestep = 0.01
time = np.arange(tinitial, tfinal+timestep,timestep)

#Create state Array

stateOut = np.zeros((2,len(time)))

def Control(state,t):
    kp = 30.0
    kd = 10.0
    xcommand = 1.0
    xdotcommand = 0.0
    ucontrol = 0.0
    if t>5:
        ucontrol = -kp*(state[0]-xcommand) - kd*(state[1]-xdotcommand)
    return ucontrol


#Now add Euler's Method to actually propogate the state forward. Could also use RK4 but gonna learn Euler's Method.
# xn+1 = xn + dx * deltaTime
for idx in range(0,len(time)):
    print('Simulation', time[idx]/tfinal*100, 'Percent Complete')
    stateOut[:,idx] = state
    ucontrol = Control(state,time[idx])
    stateDot = Derivatives(state)
    state += stateDot*timestep


#Plotting
position = stateOut[0,:]
velocity = stateOut[1,:]
plt.figure()
plt.subplot(121)
plt.plot(time,position)
plt.xlabel('Time (sec)')
plt.ylabel('Position (m)')
plt.grid()
plt.subplot(122)
plt.plot(time,velocity)
plt.xlabel('Time (sec)')
plt.grid()
plt.show()


#Adding Control for 5 Secs
#this function creates another method that takes the state as an argument and the current time.
#The if statement checks to see if the time is greater than 5 seconds. If true, ucontrol is a simple PD controller.
    #the main loop must then be updated to include Control Call. 
    




