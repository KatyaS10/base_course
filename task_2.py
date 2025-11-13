import numpy as np
import task_1  as cnst
h=100
a=np.radians(45)
b=np.radians(35)
v=np.sqrt((cnst.acceleration_of_gravity*h*np.tan(b)**2)/(2*np.cos(a)**2*(1-np.tan(a)*np.tan(b))))
print('Значение V равно: ',v,'м/с')
P=3.14
T=200
Q=300
d=2,71828