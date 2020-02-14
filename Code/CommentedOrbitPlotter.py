import numpy as np #Import Numpy
import matplotlib.pyplot as plt #Import Matplotlib
plt.rc('mathtext', fontset="cm") #Change matplotlib font to LaTeX euqation font
from scipy.integrate import odeint #Import scipy odient function
import random #Import Random
from matplotlib.collections import LineCollection #Import function for colour gradient lines

def LagrangeFlowPlot(initial, mu): #Define Orbit function
    #Data for plotting
    t=np.arange(0.0,20.0,0.001) #Define the number of time steps

    def motion(state ,t): #Define function with the equations of motion
        x, y, vx, vy = state #Define state vector
        xdot = vx #x velocity eqaution
        ydot = vy #y velocity equation
        vxdot = -((1-mu)*(x+mu)/((x+mu)**2 + y**2)**(3/2)) - (mu*(x+mu-1))/(((x+mu-1)**2 + y**2)**(3/2)) - x + 2*vy #x acceleration equation
        vydot = -((y*(1-mu)/(((x+mu)**2 + y**2)**(3/2)))) - ((y*mu)/(((x+mu-1)**2 + y**2)**(3/2))) - y - 2*vx #y acceleration equation
        return xdot, ydot, vxdot, vydot #Return equations

    fig, ax = plt.subplots() #Define new subplots
    ax.grid() #Add grid to axes

    #Plot Flow Lines:
    states=odeint(motion,initial,t) #Integrate the equations of motion with given initial conditions

    #Plot with velocity gradient:
    vel = np.sqrt(np.square(states[:,2]) + np.square(states[:,3])) #Calculate magnitude of velocity
    points = np.array([states[:,0], states[:,1]]).T.reshape(-1, 1, 2) #Reshape the array for equation of motion results
    segments = np.concatenate([points[:-1], points[1:]], axis=1) #Split the results into segments

    norm = plt.Normalize(vel.min(), vel.max()) #Normalise the velocity
    lc = LineCollection(segments, cmap='plasma', norm=norm) #Create line collection from the segements
    lc.set_array(vel) #Set line segment array to be the velocity values
    lc.set_linewidth(2) #Define the line width
    line = ax.add_collection(lc) #Set line as the set of line collections
    cbar = fig.colorbar(line, ax=ax) #Add colourbar to the figure
    cbar.ax.set_ylabel('Veclocity', rotation='vertical', fontsize=15) #Set the label for the colourbar

    #Can be used to plot if not using velcoity gradient:
    #flow=ax.plot(states[:,0],states[:,1])[0] #If we do not want a velocity plot, just plot the line


    #Plot Other Masses:
    ax.plot(-mu,0,'bo',markersize=10) #Add the position of one mass
    ax.plot(1 - mu,0,'bo',markersize=10) #Add position of other mass

    ax.set_title(r"Flow Diagram of the mass $m_3$",fontsize=16) #Set title
    ax.set_xlabel("$x$",fontsize=15) #Set x axis label
    ax.set_ylabel("$y$",fontsize=15) #Set y axis label

    textstr = '\n'.join((
        r'Initial Conditions',
        r'$x=%.2f$' % (initial[0],),
        r'$y=%.2f$' % (initial[1],),
        r'$v_x=%.2f$' % (initial[2],),
        r'$v_y=%.2f$' % (initial[3],),
        r'$\mu=%.2f$' % (mu,))) #Define text inside the text box

    props = dict(boxstyle='round', facecolor='white', alpha=0.5) #Deifne text box properties

    ax.text(0.05, 0.95, textstr, transform=ax.transAxes,
            verticalalignment='top', bbox=props) #Create text box

num = 10 #Define number of plots to be plotted
for plot in range(1,num + 1): #Loop through all the plots to be plotted

    randX = random.randint(-5, 5) #Generate random x initial condition
    randY = random.randint(-5, 5) #Generate random y initial condition
    randVX = random.randint(-5, 5) #Generate random v_x initial condition
    randVY = random.randint(-5, 5) #Generate random v_y initial condition
    randMu = round(random.random(),2) #Generate random mu initial condition

    LagrangeFlowPlot([randX, randY, randVX, randVY], randMu) #Call Orbit function

    #print("x: ",randX) #Print x value
    #print("y: ",randY) Print y value
    #print("vx: ",randVX) #Print v_x value
    #print("vy: ",randVY) #Print v_y value
    #print("mu: ",randMu) #Print mu value

    plt.savefig("Plots\\"+str(plot)+".png") #Save figure as png
    print("Plot",str(plot),"saved") #Print that figure has been saved
