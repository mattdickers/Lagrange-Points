from mpl_toolkits import mplot3d
import numpy as np
from scipy.integrate import odeint
import random
import zipfile

import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")
from matplotlib.collections import LineCollection

from tkinter import ttk
from tkinter.filedialog import *
import tkinter.messagebox

cmaps = ['plasma', 'rainbow', 'gist_rainbow']
cmapType = cmaps[0]
defailtTimeVal = 20
defailtTimeStepVal = 0.001

class GUI:
    def __init__(self, root):
        self.content = Frame(root)
        self.content.pack(side=TOP)

        self.titleFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.titleFrame.pack()

        self.title = Label(self.titleFrame, text="Lagrange Plotter")
        self.title.grid(column=0, row=0)

        self.inputFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.inputFrame.pack()

        self.initialLabel = Label(self.inputFrame, text="Initial Conditions:")
        self.initialLabel.grid(column=0, row=1, columnspan=2, sticky=W)

        global saveFormat
        saveFormat = StringVar()
        saveFormat.set("Select")
        self.saveFormat = ttk.OptionMenu(self.inputFrame, saveFormat, ".png", *[".png", ".svg"])
        self.saveFormat.grid(column=1, row=1, padx=(60,0))

        self.xLabel = Label(self.inputFrame, text="x:")
        self.xLabel.grid(column=0, row=2, padx=(0, 0), pady=(0,5))

        global xVal
        xVal = StringVar()
        self.xVal = ttk.Entry(self.inputFrame, width=10, textvariable=xVal)
        self.xVal.grid(column=1, row=2, padx=(0, 0), sticky=W, pady=(0,5))

        global xHold
        xHold = IntVar()
        self.xHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=xHold)
        self.xHold.grid(column=1, row=2, padx=(50, 0), pady=(0, 5))

        self.yLabel = Label(self.inputFrame, text="y:")
        self.yLabel.grid(column=0, row=3, padx=(0, 0), pady=(0,5))

        global yVal
        yVal = StringVar()
        self.yVal = ttk.Entry(self.inputFrame, width=10, textvariable=yVal)
        self.yVal.grid(column=1, row=3, padx=(0, 0), sticky=W, pady=(0,5))

        global yHold
        yHold = IntVar()
        self.yHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=yHold)
        self.yHold.grid(column=1, row=3, padx=(50, 0), pady=(0, 5))

        self.vxLabel = Label(self.inputFrame, text="vx:")
        self.vxLabel.grid(column=0, row=4, padx=(0, 0), pady=(0,5))

        global vxVal
        vxVal = StringVar()
        self.vxVal = ttk.Entry(self.inputFrame, width=10, textvariable=vxVal)
        self.vxVal.grid(column=1, row=4, padx=(0, 0), sticky=W, pady=(0,5))

        global vxHold
        vxHold = IntVar()
        self.vxHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=vxHold)
        self.vxHold.grid(column=1, row=4, padx=(50, 0), pady=(0, 5))

        self.vyLabel = Label(self.inputFrame, text="vy:")
        self.vyLabel.grid(column=0, row=5, padx=(0, 0), pady=(0,5))

        global vyVal
        vyVal = StringVar()
        self.vyVal = ttk.Entry(self.inputFrame, width=10, textvariable=vyVal)
        self.vyVal.grid(column=1, row=5, padx=(0, 0), sticky=W, pady=(0,5))

        global vyHold
        vyHold = IntVar()
        self.vyHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=vyHold)
        self.vyHold.grid(column=1, row=5, padx=(50, 0), pady=(0, 5))

        self.muLabel = Label(self.inputFrame, text="μ:")
        self.muLabel.grid(column=0, row=6, padx=(0, 0), pady=(0, 5))

        global muVal
        muVal = StringVar()
        self.muVal = ttk.Entry(self.inputFrame, width=10, textvariable=muVal)
        self.muVal.grid(column=1, row=6, padx=(0, 0), sticky=W, pady=(0, 5))

        global muHold
        muHold = IntVar()
        self.muHold = ttk.Checkbutton(self.inputFrame, text="Hold", variable=muHold)
        self.muHold.grid(column=1, row=6, padx=(50, 0), pady=(0, 5))

        self.timeLabel = Label(self.inputFrame, text="Time:")
        self.timeLabel.grid(column=0, row=7, padx=(0, 0), pady=(0, 5))

        global timeVal
        timeVal = StringVar()
        self.timeVal = ttk.Entry(self.inputFrame, width=7, textvariable=timeVal)
        self.timeVal.grid(column=1, row=7, padx=(0, 0), sticky=W, pady=(0, 5))
        timeVal.set(defailtTimeVal)

        self.timeStepLabel = Label(self.inputFrame, text="Step:")
        self.timeStepLabel.grid(column=1, row=7, padx=(0, 0), pady=(0, 5))

        global timeStepVal
        timeStepVal = StringVar()
        self.timeStepVal = ttk.Entry(self.inputFrame, width=7, textvariable=timeStepVal)
        self.timeStepVal.grid(column=1, row=7, padx=(85, 0), sticky=W, pady=(0, 5))
        timeStepVal.set(defailtTimeStepVal)

        self.PlotNumLabel = Label(self.inputFrame, text="Plots:")
        self.PlotNumLabel.grid(column=0, row=8, padx=(0, 0), pady=(0, 5))

        global plotNum
        plotNum = StringVar()
        self.plotNum = ttk.Entry(self.inputFrame, width=7, textvariable=plotNum)
        self.plotNum.grid(column=1, row=8, padx=(0, 0), sticky=W, pady=(0, 5))

        global plotVel
        plotVel = IntVar()
        self.plotVel = ttk.Checkbutton(self.inputFrame, text="Plot Velocity", variable=plotVel)
        self.plotVel.grid(column=1, row=8, padx=(50, 0), pady=(0, 5))

        self.plotFrame = Frame(self.content)
        self.plotFrame.pack()

        self.plotRandomButton = ttk.Button(self.plotFrame, text="Plot Random", command=self.PlotRandom)
        self.plotRandomButton.grid(column=1, row=9,  padx=(0,85), pady=(5, 0))

        self.plotValuesButton = ttk.Button(self.plotFrame, text="Plot Values", command=self.PlotValues)
        self.plotValuesButton.grid(column=1, row=9, padx=(85,0), pady=(5,0))

        self.plotPotentialButton = ttk.Button(self.plotFrame, text="Plot Potential", command=self.PlotPotential)
        self.plotPotentialButton.grid(column=1, row=10, padx=(0,85), pady=(1, 0))

        global topDown
        topDown = IntVar()
        self.topDown = ttk.Checkbutton(self.plotFrame, text="Top Down", variable=topDown)
        self.topDown.grid(column=1, row=10, padx=(85, 0), pady=(1, 0))


    def PlotRandom(self):
        empty = False
        if self.muVal.get() == "":
            empty = True
            muVal.set(0)
        if (float(self.muVal.get()) < 0 or float(self.muVal.get()) > 0.5) and muHold.get() == 1:
            tkinter.messagebox.showerror("Value Error",
                                             "μ must be between 0.01 and 0.49. Please provide a more appropriate value and try again.")
        else:
            try:
                for plot in range(1, int(self.plotNum.get()) + 1):
                    if xHold.get() == 0:
                        x = random.randint(-5, 5)
                    else:
                        x = float(self.xVal.get())

                    if yHold.get() == 0:
                        y = random.randint(-5, 5)
                    else:
                        y = float(self.yVal.get())

                    if vxHold.get() == 0:
                        vx = random.randint(-5, 5)
                    else:
                        vx = float(self.vxVal.get())

                    if vyHold.get() == 0:
                        vy = random.randint(-5, 5)
                    else:
                        vy = float(self.vyVal.get())

                    if muHold.get() == 0:
                        mu = round(np.random.uniform(low=0.01, high=0.49), 2)
                    else:
                        mu = float(self.muVal.get())

                    Orbit([x, y, vx, vy], mu, plotVel.get())
                    plt.savefig("Plots\\" + str(plot) + str(saveFormat.get()))
                    print("Plot", str(plot), "saved")
                    if empty:
                        muVal.set("")

            except ValueError:
                tkinter.messagebox.showerror("Value Error",
                                             "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")

    def PlotValues(self):
        if float(self.muVal.get()) < 0 or float(self.muVal.get()) > 0.5:
            tkinter.messagebox.showerror("Value Error",
                                         "μ must be between 0.01 and 0.49. Please provide a more appropriate value and try again.")
        else:
            try:
                x = float(self.xVal.get())
                y = float(self.yVal.get())
                vx = float(self.vxVal.get())
                vy = float(self.vyVal.get())
                mu = float(self.muVal.get())

                filePath = asksaveasfilename(title="Save Plot", filetypes=(
                (str(saveFormat.get())[1:].upper(), "*" + str(saveFormat.get())), ("All files", "*")))
                if filePath != "":
                    Orbit([x, y, vx, vy], mu, plotVel.get())
                    plt.savefig(str(filePath) + str(saveFormat.get()))
                    print("Plot Saved")
                else:
                    tkinter.messagebox.showerror("Save Error",
                                                 "There is no file name. Please provide a file name and try again.")
            except ValueError:
                tkinter.messagebox.showerror("Value Error",
                                             "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")


    def PlotPotential(self):
        if float(self.muVal.get()) < 0 or float(self.muVal.get()) > 0.5:
            tkinter.messagebox.showerror("Value Error",
                                         "μ must be between 0.01 and 0.49. Please provide a more appropriate value and try again.")
        else:
            try:
                filePath = asksaveasfilename(title="Save Plot", filetypes=(
                (str(saveFormat.get())[1:].upper(), "*" + str(saveFormat.get())), ("All files", "*")))
                if filePath != "":
                    Potential(float(self.muVal.get()), topDown.get())
                    plt.savefig(str(filePath) + str(saveFormat.get()))
                    print("Plot saved")
                else:
                    tkinter.messagebox.showerror("Save Error",
                                                 "There is no file name. Please provide a file name and try again.")
            except ValueError:
                tkinter.messagebox.showerror("Value Error",
                                             "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")



def ColourConvert(rgb):
    return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

def Orbit(initial, mu, velocity):
    #Data for plotting
    t=np.arange(0.0,float(timeVal.get()),float(timeStepVal.get()))  # time steps

    def motion(state ,t):
        x, y, vx, vy = state  # unpack state vector
        xdot = vx
        ydot = vy
        vxdot = -((1-mu)*(x+mu)/((x+mu)**2 + y**2)**(3/2)) - (mu*(x+mu-1))/(((x+mu-1)**2 + y**2)**(3/2)) - x + 2*vy
        vydot = -((y*(1-mu)/(((x+mu)**2 + y**2)**(3/2)))) - ((y*mu)/(((x+mu-1)**2 + y**2)**(3/2))) - y - 2*vx
        return xdot, ydot, vxdot, vydot

    fig, ax = plt.subplots()
    ax.grid()

    #Plot Flow Lines:
    states=odeint(motion,initial,t)

    if velocity == 1:
        #Plot with velocity gradient:
        vel = np.sqrt(np.square(states[:,2]) + np.square(states[:,3]))
        points = np.array([states[:,0], states[:,1]]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        norm = plt.Normalize(vel.min(), vel.max())
        lc = LineCollection(segments, cmap=cmapType, norm=norm)
        lc.set_array(vel)
        lc.set_linewidth(2)
        line = ax.add_collection(lc)
        cbar = fig.colorbar(line, ax=ax)
        cbar.ax.set_ylabel('Veclocity', rotation='vertical', fontsize=15)

    else:
        #Can be used to plot if not using velcoity gradient:
        flow=ax.plot(states[:,0],states[:,1])[0]


    #Plot Other Masses:
    ax.plot(-mu,0,'bo' ,markersize=10)
    ax.plot(1 - mu,0,'bo', markersize=10)

    ax.set_title(r"Flow Diagram of the mass $m_3$", fontsize=16)
    ax.set_xlabel("$x$", fontsize=15)
    ax.set_ylabel("$y$", fontsize=15)

    textstr = '\n'.join((
        r'Initial Conditions',
        r'$x=%.2f$' % (initial[0],),
        r'$y=%.2f$' % (initial[1],),
        r'$v_x=%.2f$' % (initial[2],),
        r'$v_y=%.2f$' % (initial[3],),
        r'$\mu=%.2f$' % (mu,)))

    props = dict(boxstyle='round', facecolor='white', alpha=0.5)

    ax.text(0.05, 0.95, textstr, transform=ax.transAxes,
            verticalalignment='top', bbox=props)

def Potential(mu, top):
    def potential(x, y, mu):
        return (0.5 * (x ** 2 + y ** 2)) + ((1 - mu) / np.sqrt((x + mu) ** 2 + y ** 2)) + (
                    mu / np.sqrt((x + mu - 1) ** 2 + y ** 2))

    x = np.linspace(-2, 2, 30)
    y = np.linspace(-2, 2, 30)

    x, y = np.meshgrid(x, y)
    z = potential(x, y, mu)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(x, y, z, 50, cmap=cmapType)
    ax.set_xlabel(r'$x$', fontsize=15)
    ax.set_ylabel(r'$y$', fontsize=15)
    if top == 1:
        ax.view_init(elev=90., azim=90)
        ax.w_zaxis.line.set_lw(0.)
        ax.set_zticks([])
        ax.dist = 7
    else:
        ax.set_zlabel(r'$z$', fontsize=15)
    ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16)


root = Tk()

GUI = GUI(root)

root.wm_title("")

root.geometry("180x285")

root.resizable(width=False, height=False)

root.pack_propagate(0)
root.grid_propagate(0)

root.mainloop()
