from mpl_toolkits import mplot3d #Import 3D plotting tools
import numpy as np #Import Numpy
from scipy.integrate import odeint #Import scipy odeint funcitons for integrations
import random #Import random

import matplotlib.pyplot as plt #Import matplotlib
plt.rc('mathtext', fontset="cm") #Change maplotlib font to LaTeX equation font
from matplotlib.collections import LineCollection #Import maplotlib line collections

from tkinter import ttk #Import tkinter for GUI
from tkinter.filedialog import * #Import tkinter file dialogs for saving plots
import tkinter.messagebox #Import  tkinter message boxes for showing errors

cmaps = ['plasma', 'rainbow', 'gist_rainbow'] #Define different types of colour gradients for the velocity plots
cmapType = cmaps[0] #Assign the colour gradient that will be used
defailtTimeVal = 20 #Define the default time value for plotting
defailtTimeStepVal = 0.001 #Define the default timestep for plotting

class GUI: #Define GUI class
    def __init__(self, root): #Define initialisation variables
        self.content = Frame(root) #Create frame for content
        self.content.pack(side=TOP) #Pack frame

        self.titleFrame = Frame(self.content, bg=ColourConvert((240, 240, 240))) #Create title frame
        self.titleFrame.pack() #Pack title frame

        self.title = Label(self.titleFrame, text="Lagrange Plotter") #Define title
        self.title.grid(column=0, row=0) #Place title

        self.inputFrame = Frame(self.content, bg=ColourConvert((240, 240, 240))) #Create frame for input widgets
        self.inputFrame.pack() #Pakc widget frame

        self.initialLabel = Label(self.inputFrame, text="Initial Conditions:") #Define initial conditiosn label
        self.initialLabel.grid(column=0, row=1, columnspan=2, sticky=W) #Place label

        global saveFormat #Define global file format variable
        saveFormat = StringVar() #Assign file format variable as a string
        saveFormat.set("Select") #Set option for the dropdown menu
        self.saveFormat = ttk.OptionMenu(self.inputFrame, saveFormat, ".png", *[".png", ".svg"]) #Create dropdown menu for file formats
        self.saveFormat.grid(column=1, row=1, padx=(60,0)) #Place file format dropdown menu

        self.xLabel = Label(self.inputFrame, text="x:") #Create x position label
        self.xLabel.grid(column=0, row=2, padx=(0, 0), pady=(0,5)) #Position x position label

        global xVal #Define global x value variable
        xVal = StringVar() #Set x position value as a string
        self.xVal = ttk.Entry(self.inputFrame, width=10, textvariable=xVal) #Create input box for the x value
        self.xVal.grid(column=1, row=2, padx=(0, 0), sticky=W, pady=(0,5)) #Position the x position input box

        global xHold #Define variable to hold x value in random plots
        xHold = IntVar() #Set this variable as an integer
        self.xHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=xHold) #Add checkbox for the x hold
        self.xHold.grid(column=1, row=2, padx=(50, 0), pady=(0, 5)) #Position the x hold checkbox

        self.yLabel = Label(self.inputFrame, text="y:") #Create y position label
        self.yLabel.grid(column=0, row=3, padx=(0, 0), pady=(0,5)) #Position y position label

        global yVal #Define global y value variable
        yVal = StringVar() #Set y position value as a string
        self.yVal = ttk.Entry(self.inputFrame, width=10, textvariable=yVal) #Create input box for the y value
        self.yVal.grid(column=1, row=3, padx=(0, 0), sticky=W, pady=(0,5)) #Position the y position input box

        global yHold #Define variable to hold y value in random plots
        yHold = IntVar() #Set this variable as an integer
        self.yHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=yHold) #Add checkbox for the y hold
        self.yHold.grid(column=1, row=3, padx=(50, 0), pady=(0, 5)) #Position the y hold checkbox

        self.vxLabel = Label(self.inputFrame, text="vx:") #Create vx label
        self.vxLabel.grid(column=0, row=4, padx=(0, 0), pady=(0,5)) #Position vx label
        
        global vxVal #Define global vx value variable
        vxVal = StringVar() #Set vx value as a string
        self.vxVal = ttk.Entry(self.inputFrame, width=10, textvariable=vxVal) #Create input box for the vx value
        self.vxVal.grid(column=1, row=4, padx=(0, 0), sticky=W, pady=(0,5)) #Position the vx input box

        global vxHold #Define variable to hold vx value in random plots
        vxHold = IntVar() #Set this variable as an integer
        self.vxHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=vxHold) #Add checkbox for the vx hold
        self.vxHold.grid(column=1, row=4, padx=(50, 0), pady=(0, 5)) #Position the vx hold checkbox

        self.vyLabel = Label(self.inputFrame, text="vy:") #Create vy label
        self.vyLabel.grid(column=0, row=5, padx=(0, 0), pady=(0,5)) #Position v label

        global vyVal #Define global vy value variable
        vyVal = StringVar() #Set vy value as a string
        self.vyVal = ttk.Entry(self.inputFrame, width=10, textvariable=vyVal) #Create input box for the vy value
        self.vyVal.grid(column=1, row=5, padx=(0, 0), sticky=W, pady=(0,5)) #Position the vy input box
        
        global vyHold #Define variable to hold vy value in random plots
        vyHold = IntVar() #Set this variable as an integer
        self.vyHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=vyHold) #Add checkbox for the vy hold
        self.vyHold.grid(column=1, row=5, padx=(50, 0), pady=(0, 5)) #Position the vy hold checkbox

        self.muLabel = Label(self.inputFrame, text="μ:") #Create μ label
        self.muLabel.grid(column=0, row=6, padx=(0, 0), pady=(0, 5)) #Position μ label

        global muVal #Define global μ value variable
        muVal = StringVar() #Set μ value as a string
        self.muVal = ttk.Entry(self.inputFrame, width=10, textvariable=muVal) #Create input box for the μ value
        self.muVal.grid(column=1, row=6, padx=(0, 0), sticky=W, pady=(0, 5)) #Position the μ input box

        global muHold #Define variable to hold μ value in random plots
        muHold = IntVar() #Set this variable as an integer
        self.muHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=muHold) #Add checkbox for the μ hold
        self.muHold.grid(column=1, row=6, padx=(50, 0), pady=(0, 5)) #Position the μ hold checkbox

        self.timeLabel = Label(self.inputFrame, text="Time:") #Create time label
        self.timeLabel.grid(column=0, row=7, padx=(0, 0), pady=(0, 5)) #Position time label

        global timeVal #Define global time value variable
        timeVal = StringVar() #Set time value as a string
        self.timeVal = ttk.Entry(self.inputFrame, width=7, textvariable=timeVal) #Create input box for the time value
        self.timeVal.grid(column=1, row=7, padx=(0, 0), sticky=W, pady=(0, 5)) #Position the time input box
        timeVal.set(defailtTimeVal) #Set value of the time to the defualt time defined at the start

        self.timeStepLabel = Label(self.inputFrame, text="Step:") #Create time step label
        self.timeStepLabel.grid(column=1, row=7, padx=(0, 0), pady=(0, 5)) #Position time step label

        global timeStepVal #Define global time step value variable
        timeStepVal = StringVar() #Set time step value as a string
        self.timeStepVal = ttk.Entry(self.inputFrame, width=7, textvariable=timeStepVal) #Create input box for the time step value
        self.timeStepVal.grid(column=1, row=7, padx=(85, 0), sticky=W, pady=(0, 5)) #Position the time step input box
        timeStepVal.set(defailtTimeStepVal) #Set value of the time step to the defualt time step defined at the start

        self.PlotNumLabel = Label(self.inputFrame, text="Plots:") #Define the number of plots label to be plotted if plot random is selected
        self.PlotNumLabel.grid(column=0, row=8, padx=(0, 0), pady=(0, 5)) #Position the plot number label

        global plotNum #Define global plot number variable
        plotNum = StringVar() #Set plot value as a string
        self.plotNum = ttk.Entry(self.inputFrame, width=7, textvariable=plotNum) #Create input box for the plot value
        self.plotNum.grid(column=1, row=8, padx=(0, 0), sticky=W, pady=(0, 5)) #Position the plot input box

        global plotVel #Define variable for if veloity should be plotted
        plotVel = IntVar() #Set this variable as an integer
        self.plotVel = ttk.Checkbutton(self.inputFrame, text="Plot Velocity", variable=plotVel) #Create checkbox for plotting velocity
        self.plotVel.grid(column=1, row=8, padx=(50, 0), pady=(0, 5)) #Position velocity plotting checkbox

        self.plotFrame = Frame(self.content)# Create plot frame
        self.plotFrame.pack() #pack plot frame

        self.plotRandomButton = ttk.Button(self.plotFrame, text="Plot Random", command=self.PlotRandom) #Create button to plot random plots
        self.plotRandomButton.grid(column=1, row=9,  padx=(0,85), pady=(5, 0)) #Position random plots button

        self.plotValuesButton = ttk.Button(self.plotFrame, text="Plot Values", command=self.PlotValues) #Create button to plot with given values
        self.plotValuesButton.grid(column=1, row=9, padx=(85,0), pady=(5,0)) #Position plot values button

        self.plotPotentialButton = ttk.Button(self.plotFrame, text="Plot Potential", command=self.PlotPotential) #Add button for plotting the potentials
        self.plotPotentialButton.grid(column=1, row=10, padx=(0,85), pady=(1, 0)) #Position button for plotting potentials

        global topDown #Create global variable for potentail plots being plotted such that they are viewed from the top
        topDown = IntVar() #Set this variable as an integer
        self.topDown = ttk.Checkbutton(self.plotFrame, text="Top Down", variable=topDown) #Create checkbox for top down plotting
        self.topDown.grid(column=1, row=10, padx=(85, 0), pady=(1, 0)) #Position top down plotting textbox


    def PlotRandom(self): #Define function for plotting a series of random plots
        try:
            for plot in range(1, int(self.plotNum.get()) + 1): #Loop through the number of plots stated by the user
                if xHold.get() == 0: #Check if the hold checkbox is checked for the x values
                    x = random.randint(-5, 5) #If not, generate random x position between -5 and 5
                else:
                    x = float(self.xVal.get()) #If it is, use the given value

                if yHold.get() == 0: #Check if the hold checkbox is checked for the y values
                    y = random.randint(-5, 5) #If not, generate random y position between -5 and 5
                else:
                    y = float(self.yVal.get()) #If it is, use the given value

                if vxHold.get() == 0: #Check if the hold checkbox is checked for the vx values
                    vx = random.randint(-5, 5) #If not, generate random vx value between -5 and 5
                else:
                    vx = float(self.vxVal.get()) #If it is, use the given value

                if vyHold.get() == 0: #Check if the hold checkbox is checked for the vy values
                    vy = random.randint(-5, 5) #If not, generate random vy value between -5 and 5
                else:
                    vy = float(self.vyVal.get()) #If it is, use the given value

                if muHold.get() == 0: #Check if the hold checkbox is checked for the μ values
                    mu = round(np.random.uniform(low=0, high=1), 2) #If not, generate random μ value between 0 and 1 to 2dp
                else:
                    mu = float(self.muVal.get()) #If it is, use the given value

                Orbit([x, y, vx, vy], mu, plotVel.get()) #Call the Orbit function to calculate the orbit from the given initial conditions
                plt.savefig("Plots\\" + str(plot) + str(saveFormat.get())) #Save the figure using the format stated by the user
                print("Plot", str(plot), "saved") #Display that the figure n has been saved

        except ValueError: #Check for a valueError
            tkinter.messagebox.showerror("Value Error",
                                         "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")
            #If ValueError occurs, inform user that thet need to input values or correctly formatted values

    def PlotValues(self):
        try:
            x = float(self.xVal.get()) #Get the x position defined by the user
            y = float(self.yVal.get()) #Get the y position defined by the user
            vx = float(self.vxVal.get()) #Get the vx value defiend by the user
            vy = float(self.vyVal.get()) #Get the vy value defined by the user
            mu = float(self.muVal.get()) #Get the μ value defined by the user

            filePath = asksaveasfilename(title="Save Plot", filetypes=(
            (str(saveFormat.get())[1:].upper(), "*" + str(saveFormat.get())), ("All files", "*"))) #Get file path for where the plot should be saved
            if filePath != "": #Check if file path was entered
                Orbit([x, y, vx, vy], mu, plotVel.get()) #Call the Orbit function to calculate the orbit for the given initial conditions
                plt.savefig(str(filePath) + str(saveFormat.get())) #Save the figure using the format stated by the user
                print("Plot Saved") #Display that the figure has been saved
            else:
                tkinter.messagebox.showerror("Save Error",
                                             "There is no file name. Please provide a file name and try again.")
                #If there was no path entered, display error to user
        except ValueError: #Check for ValueError
            tkinter.messagebox.showerror("Value Error",
                                         "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")
            #If ValueError occurs, inform user that thet need to input values or correctly formatted values


    def PlotPotential(self):
        try:
            filePath = asksaveasfilename(title="Save Plot", filetypes=(
            (str(saveFormat.get())[1:].upper(), "*" + str(saveFormat.get())), ("All files", "*"))) #Get file path for where the plot should be saved
            if filePath != "": #Check if file path was entered
                Potential(float(self.muVal.get()), topDown.get()) #Call the Potential function to plot the gravitational potential for the given value of μ
                plt.savefig(str(filePath) + str(saveFormat.get())) #Save the figure using the format stated by the user
                print("Plot saved") #Display that the figure has been saved
            else:
                tkinter.messagebox.showerror("Save Error",
                                             "There is no file name. Please provide a file name and try again.")
                #If there was no path entered, display error to user
        except ValueError: #Check for ValueError
            tkinter.messagebox.showerror("Value Error",
                                         "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")
            #If ValueError occurs, inform user that thet need to input values or correctly formatted values


def ColourConvert(rgb): #Function to convert an RGB colour list to a string format that matplotlib and tkinter like
    return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2])) #Conver list of RBG values to string

def Orbit(initial, mu, velocity):#Define Orbit function
    #Data for plotting
    t=np.arange(0.0,float(timeVal.get()),float(timeStepVal.get())) #Define the number of time steps

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

    if velocity == 1: #Check if plottig with velocity is turned on
        #Plot with velocity gradient:
        vel = np.sqrt(np.square(states[:,2]) + np.square(states[:,3])) #Calculate magnitude of velocity
        points = np.array([states[:,0], states[:,1]]).T.reshape(-1, 1, 2) #Reshape the array for equation of motion results
        segments = np.concatenate([points[:-1], points[1:]], axis=1) #Split the results into segments

        norm = plt.Normalize(vel.min(), vel.max()) #Normalise the velocity
        lc = LineCollection(segments, cmap=cmapType, norm=norm) #Create line collection from the segements
        lc.set_array(vel) #Set line segment array to be the velocity values
        lc.set_linewidth(2) #Define the line width
        line = ax.add_collection(lc) #Set line as the set of line collections
        cbar = fig.colorbar(line, ax=ax) #Add colourbar to the figure
        cbar.ax.set_ylabel('Magnitude of Veclocity', rotation='vertical', fontsize=15) #Set the label for the colourbar

    else:
        #Plot without velocity:
        flow=ax.plot(states[:,0],states[:,1],'k')[0] #Plot lines


    #Plot Other Masses:
    size = 10 #Define maximum size of the masses
    ax.plot(-mu,0,'ko' ,markersize=((1 - mu)*size)) #Add the position of one mass
    ax.plot(1 - mu,0,'ko', markersize=(mu * size)) #Add position of other mass

    ax.set_title(r"Plot of the Orbit of a mass $m_3$", fontsize=16) #Set title
    ax.set_xlabel("$x$", fontsize=15) #Set x axis label
    ax.set_ylabel("$y$", fontsize=15) #Set y axis label

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

def Potential(mu, top): #Define function for plotting potentials
    def potential(x, y, mu): #Define the function for calculating potential
        return (0.5 * (x ** 2 + y ** 2)) + ((1 - mu) / np.sqrt((x + mu) ** 2 + y ** 2)) + (
                    mu / np.sqrt((x + mu - 1) ** 2 + y ** 2))

    x = np.linspace(-2, 2, 30) #Define series of evenly spaced number for x
    y = np.linspace(-2, 2, 30)  #Define series of evenly spaced number for y

    x, y = np.meshgrid(x, y) #Create mesh grid from x and y
    z = potential(x, y, mu) #Call potential function to calculate the potential at each x and y point

    fig = plt.figure() #Create figure
    ax = plt.axes(projection='3d') #Set the axes to be 3D
    ax.contour3D(x, y, z, 50, cmap=cmapType) #Plot a 3D contour with the values x, y and z, using the colourmap defined at the start
    ax.invert_xaxis() #Invert the x axis
    ax.set_xlabel(r'$x$', fontsize=15) #x axis label
    ax.set_ylabel(r'$y$', fontsize=15) #y axis label
    if top == 1: #Check if top down view checkbox is checked
        ax.view_init(elev=90., azim=90) #Change the oreitnation of the plot to be looking down from the top
        ax.w_zaxis.line.set_lw(0.) #Disable the z axis lines
        ax.set_zticks([]) #Disable the z axis ticks
        ax.dist = 7 #Set the plot distance from the camera to 7
    else:
        ax.set_zlabel(r'$z$', fontsize=15) #If not plotting top down, add z axis label
    ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16) #Set title


root = Tk() #Define root

GUI = GUI(root) #Call GUI class

root.wm_title("") #Set window title

root.geometry("180x285") #Set the size of the window

root.resizable(width=False, height=False) #Disable window resizing

root.pack_propagate(0) #Ensure that changin widget size will not move other widgets that are packed
root.grid_propagate(0) #Ensure that changin widget size will not move other widgets that are arranged on the grid

root.mainloop() #Loop for GUI
