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

class GUI:
    def __init__(self, root):
        self.content = Frame(root)
        self.content.pack(side=TOP)

        self.titleFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.titleFrame.pack()

        self.title = Label(self.titleFrame, text="Orbit Plotter")
        self.title.grid(column=0, row=0)

        self.inputFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.inputFrame.pack()

        self.initialLabel = Label(self.inputFrame, text="Initial Conditions:")
        self.initialLabel.grid(column=0, row=1, columnspan=2, sticky=W)

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

        self.PlotNumLabel = Label(self.inputFrame, text="Plots:")
        self.PlotNumLabel.grid(column=0, row=7, padx=(0, 0), pady=(0, 5))

        global plotNum
        plotNum = StringVar()
        self.plotNum = ttk.Entry(self.inputFrame, width=7, textvariable=plotNum)
        self.plotNum.grid(column=1, row=7, padx=(0, 0), sticky=W, pady=(0, 5))

        global plotVel
        plotVel = IntVar()
        self.plotVel = ttk.Checkbutton(self.inputFrame, text="Plot Velocity", variable=plotVel)
        self.plotVel.grid(column=1, row=7, padx=(50, 0), pady=(0, 5))

        self.plotFrame = Frame(self.content)
        self.plotFrame.pack()

        self.plotRandomButton = ttk.Button(self.plotFrame, text="Plot Random", command=self.PlotRandom)
        self.plotRandomButton.grid(column=1, row=8, pady=(5, 0))

        self.plotValuesButton = ttk.Button(self.plotFrame, text="Plot Values", command=self.PlotValues)
        self.plotValuesButton.grid(column=1, row=9, pady=(1,0))


    def PlotRandom(self):
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
                    mu = round(random.random(), 2)
                else:
                    mu = float(self.muVal.get())

                LagrangeFlowPlot([x, y, vx, vy], mu, plotVel.get())
                plt.savefig("Plots\\" + str(plot) + ".png")
                print("Plot", str(plot), "saved")

        except ValueError:
            tkinter.messagebox.showerror("Value Error",
                                         "An non-integer or float value as entered . Please only use values that are integers or floats.")

    def PlotValues(self):
        try:
            x = float(self.xVal.get())
            y = float(self.yVal.get())
            vx = float(self.vxVal.get())
            vy = float(self.vyVal.get())
            mu = float(self.muVal.get())

            filePath = asksaveasfilename(title="Save Plot", filetypes=(("PNG", "*.png"), ("All files", "*")))
            LagrangeFlowPlot([x, y, vx, vy], mu, plotVel.get())
            plt.savefig(str(filePath) + ".png")
            print("Plot saved")

        except ValueError:
            tkinter.messagebox.showerror("Value Error",
                                         "An non-integer or float value as entered . Please only use values that are integers or floats.")

def ColourConvert(rgb):
    return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

def LagrangeFlowPlot(initial, mu, velocity):
    #Data for plotting
    t=np.arange(0.0,20.0,0.001)  # time steps

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
        lc = LineCollection(segments, cmap='plasma', norm=norm)
        lc.set_array(vel)
        lc.set_linewidth(2)
        line = ax.add_collection(lc)
        cbar = fig.colorbar(line, ax=ax)
        cbar.ax.set_ylabel('Veclocity', rotation='vertical', fontsize=15)

    else:
        #Can be used to plot if not using velcoity gradient:
        flow=ax.plot(states[:,0],states[:,1])[0]


    #Plot Other Masses:
    ax.plot(-mu,0,'bo',markersize=10)
    ax.plot(1 - mu,0,'bo',markersize=10)

    ax.set_title(r"Flow Diagram of the mass $m_3$",fontsize=16)
    ax.set_xlabel("$x$",fontsize=15)
    ax.set_ylabel("$y$",fontsize=15)

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

root = Tk()

GUI = GUI(root)

root.wm_title("")

root.geometry("180x257")

root.resizable(width=False, height=False)

root.pack_propagate(0)
root.grid_propagate(0)

root.mainloop()
