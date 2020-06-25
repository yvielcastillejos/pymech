# In comments, generates a pcolormesh plot
#For now, generates the terbulence ratio (gamma) with vertical flux and horizontal flux
import exadata
import extract_data2D
import neksuite
import numpy as np
import matplotlib.pyplot as plt
import os


fifle = 'ddd0.f00001'
PATH = f"/Users/yvielcastillejos//Nek5000/run/try1/dataset"
files = sorted(os.listdir(PATH))
print(files)
Nus = []
times = []
turbratio = []
for file in files:
    data = neksuite.readnek(f"{PATH}/{file}")
    lr1 = data.lr1
    Uy = extract_data2D.reshapenek(data.elems.vel[1],lr1)
    temp =  extract_data2D.reshapenek(data.elems.temp[0],lr1)
    saln =extract_data2D.reshapenek(data.elems.scal[0],lr1)
    time = data.time 
    F_T = np.mean(np.multiply(temp,Uy))
    F_S =np.mean(np.multiply(saln,Uy)) 
    Nu = 1 - F_T
    turbratio.append(F_T/F_S)
    Nus.append(Nu)
    times.append(time)
    print(f"{file}" + " done")
    #print(times)
    #print(Nus)
#U = np.sqrt(np.square(Ux) + np.square(Uy))
#print(Ux.shape)
x = np.linspace(0, 300, 320)
y = np.linspace(0, 500, 320)
#print(Ux)


#calculate mean
tempmean = np.mean(temp,axis =1)

fig, ax = plt.subplots()
#cmap = ax.pcolormesh(x, y, Ux, vmin=-17.26, vmax=19.76)
#ax.set_aspect("equal")
#fig.colorbar(cmap)
plt.plot(times,turbratio)
#plt.title(f't ={time} (Nu = {Nu})')
plt.title('turbulent ratio over time(γ)')
plt.ylabel('γ')
plt.xlabel('time')
#ax.set_aspect("equal")
plt.show(fig)
