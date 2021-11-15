import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
from math import e

# Preparing the data for the plot
x = [0.3, 0.4, 0.5, 0.6, 0.7]
y = [1.11355, 1.281875, 1.438375, 1.569625, 1.6964]

def my_func(t,k,n):
    return k*(t**n)
# this is the function we want to fit. the first variable must be the
# x-data (time), the rest are the unknown constants we want to determine

init_guess=(2,0.5)
# your initial guess of (a,tau,T,phi)

popt, pcov = optimize.curve_fit(my_func, x, y, p0=init_guess)
# we have the best fit values in popt[], while pcov[] tells us the uncertainties

k=popt[0]
n=popt[1]
# best fit values are named nicely
u_k=pcov[0,0]**(0.5)
u_n=pcov[1,1]**(0.5)
# uncertainties of fit are named nicely

def fitfunction(t):  
    return k*(t**n)
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(x)
stop=max(x)    
xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata) 

# Resizing the figure
plt.figure(figsize=[7,5])

# Plotting the scatter plot
plt.scatter(x, y, c='g', alpha=0.6)
plt.title('loglog linear plot with y-axis log base 2', fontsize=15)
plt.xlabel('log(x) base 10', fontsize=13)
plt.ylabel('log(y) base 10', fontsize=13)

plt.plot(xs,curve)

# Changing to the log ticks at x and y axis using loglog
plt.loglog(basex=10, basey=10)

plt.show()