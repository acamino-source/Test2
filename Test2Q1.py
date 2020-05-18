#AMS326 Test 2 Question 1 
#There's an accompanying graph in desmos: https://www.desmos.com/calculator/ofm79agcdp
from math import sqrt,pi as π
r1=13.333
r2=15.555
h=8.888
k=1.984

def r(y):
    #radius at height y
    return r2+(r1-r2)*(y/h)
def a(y):
    #surface area at height y
    return π*r(y)**2
def f(t,y):
    return -k*sqrt(abs(y))/a(y)# using abs(y) to prevent domain errors which crash the program. It's numerically insignificant.

#QUESTION 1: Euler Method (before flipping)
Δt=0.01#The timestep
y=h
t=0#Total time
while y>0:
    #Using the forward difference approximation of y'(t)
    y+=Δt*f(t,y)
    t+=Δt
print('Euler Method (before flipping) total time:',t)

#QUESTION 1: Heun's Method (before flipping)
Δt=0.01#The timestep
y=h
t=0#Total time
while y>0:
    #Using the forward difference approximation of y'(t)
    y_=y+Δt*f(t,y)#Forward-Euler
    y+=Δt/2*(f(t,y)+f(t+Δt,y_))#Heun
    t+=Δt
print('Heun Method (before flipping) total time:',t)

#Now, to flip the container we just swap r1 and r2
r1,r2=r2,r1

#QUESTION 1: Euler Method (after flipping)
Δt=0.01#The timestep
y=h
t=0#Total time
while y>0:
    #Using the forward difference approximation of y'(t)
    y+=Δt*f(t,y)
    t+=Δt
print('Euler Method (after flipping) total time:',t)

#QUESTION 1: Heun's Method (after flipping)
Δt=0.01#The timestep
y=h
t=0#Total time
while y>0:
    #Using the forward difference approximation of y'(t)
    y_=y+Δt*f(t,y)#Forward-Euler
    y+=Δt/2*(f(t,y)+f(t+Δt,y_))#Heun
    t+=Δt
print('Heun Method (after flipping) total time:',t)
