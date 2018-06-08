import matplotlib.pyplot as plt
import mplleaflet
import site
site.getsitepackages()

xs = [24.30,25.30]
ys = [60.5,60.1]
plt.scatter(xs,ys) #points
xs = [24.20,25.40]
ys = [60.5,60.1]
plt.plot(xs,ys,'r') #points
mplleaflet.show()
