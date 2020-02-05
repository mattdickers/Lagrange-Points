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
        self.xLabel.grid(column=0, row=2, padx=(0, 0))

        global xVal
        xVal = StringVar()
        self.xVal = ttk.Entry(self.inputFrame, width=15, textvariable=xVal)
        self.xVal.grid(column=1, row=2, padx=(0, 0), sticky=W)

        self.yLabel = Label(self.inputFrame, text="y:")
        self.yLabel.grid(column=0, row=3, padx=(0, 0))

        global yVal
        yVal = StringVar()
        self.yVal = ttk.Entry(self.inputFrame, width=15, textvariable=yVal)
        self.yVal.grid(column=1, row=3, padx=(0, 0), sticky=W, pady=(5,5))

        self.vxLabel = Label(self.inputFrame, text="vx:")
        self.vxLabel.grid(column=0, row=4, padx=(0, 0), pady=(0,5))

        global vxVal
        vxVal = StringVar()
        self.vxVal = ttk.Entry(self.inputFrame, width=15, textvariable=vxVal)
        self.vxVal.grid(column=1, row=4, padx=(0, 0), sticky=W, pady=(0,5))

        self.vyLabel = Label(self.inputFrame, text="vy:")
        self.vyLabel.grid(column=0, row=5, padx=(0, 0), pady=(0,5))

        global vyVal
        vyVal = StringVar()
        self.vyVal = ttk.Entry(self.inputFrame, width=15, textvariable=vyVal)
        self.vyVal.grid(column=1, row=5, padx=(0, 0), sticky=W, pady=(0,5))

        self.muLabel = Label(self.inputFrame, text="μ:")
        self.muLabel.grid(column=0, row=6, padx=(0, 0), pady=(0, 5))

        global muVal
        muVal = StringVar()
        self.muVal = ttk.Entry(self.inputFrame, width=15, textvariable=muVal)
        self.muVal.grid(column=1, row=6, padx=(0, 0), sticky=W, pady=(0, 5))

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


    def PlotValues(self):
        pass

    def PlotRandom(self):
        pass


def ColourConvert(rgb):
    return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

root = Tk()

GUI = GUI(root)

root.wm_title("")

root.geometry("180x257")

root.resizable(width=False, height=False)

root.pack_propagate(0)
root.grid_propagate(0)

root.mainloop()