from mpl_toolkits import mplot3d
import numpy as np
from scipy.integrate import odeint
import random

import matplotlib.pyplot as plt
plt.rc('mathtext', fontset="cm")
from matplotlib.collections import LineCollection
import matplotlib.colors as colours

from tkinter import ttk
from tkinter.filedialog import *
import tkinter.messagebox
from tkinter.colorchooser import *

style = False

#customCmap = {'cmap1':(255, 0, 0), 'cmap2':(0, 255, 0), 'cmap3':(0, 0, 255)}
lineThicknessDict = {'Thicc':[1,2], 'Thin':[0.75, 0.75]}
lineStylesDict = {"─":"-", "•":".", ".":",", "┄":"--"}
buttonColours = {"line":(0, 0, 0), "mass1":(0, 0, 0), "mass2":(0, 0, 0), 'cmap1':(255, 0, 0), 'cmap2':(0, 255, 0), 'cmap3':(0, 0, 255)}
cmapsDict = {'Plasma':'plasma', 'Rainbow 1':'rainbow', 'Rainbow 2':'gist_rainbow'}
infoBoxColourDict = {'Light':'white', 'Dark':'black'}


defailtTimeVal = 20
defailtTimeStepVal = 0.001

class GUI:
    def __init__(self, root):
        self.content = Frame(root)
        self.content.pack(side=TOP)

        self.titleFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.titleFrame.grid(column=0, row=0)

        self.title = Label(self.titleFrame, text="Lagrange Plotter")
        self.title.grid(column=0, row=0)

        self.inputFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.inputFrame.grid(column=0, row=1)

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

        self.plotFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
        self.plotFrame.grid(column=0, row=2, columnspan=3)

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

        self.styleButton = ttk.Button(self.plotFrame, text="Show Style Options", command=self.Style)
        self.styleButton.grid(column=1, row=11)

        #Define Style variables
        global plotTheme
        plotTheme = StringVar()
        plotTheme.set("Light")

        global axesState
        axesState = StringVar()
        axesState.set("On")

        global massState
        massState = StringVar()
        massState.set("On")

        global lineThickness
        lineThickness = StringVar()
        lineThickness.set("Thicc")

        global lineStyle
        lineStyle = StringVar()
        lineStyle.set("─")

        global velocityColour
        velocityColour = StringVar()
        velocityColour.set("Plasma")

        global lineThiccnessEntryVal
        lineThiccnessEntryVal = StringVar()#
        lineThiccnessEntryVal.set("Thicc")

    def Style(self):
        global style
        if not style:
            style = True
            root.geometry("382x329")
            root.wm_title("Lagrange Plotter")
            self.styleButton.config(text='Hide Style Options')

            #Create Dividing Line:
            self.titleFillFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
            self.titleFillFrame.grid(column=1, row=0)

            self.canvas = Canvas(self.content, width=1, height=200, bg=ColourConvert((0, 0, 0)))
            self.canvas.grid(column=1, row=1)

            self.styleTitleFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
            self.styleTitleFrame.grid(column=2, row=0)

            self.styleTitle = Label(self.styleTitleFrame, text="Plot Style")
            self.styleTitle.grid(column=0, row=0)

            self.styleFrame = Frame(self.content, bg=ColourConvert((240, 240, 240)))
            self.styleFrame.grid(column=2, row=1)

            self.themeLabel = Label(self.styleFrame, text="Plot Theme:")
            self.themeLabel.grid(column=0, row=0, pady=(0,5), sticky=W)

            self.plotTheme = ttk.OptionMenu(self.styleFrame, plotTheme, "Light", *["Light", "Dark"],
                                            command=self.updateAllColours)
            self.plotTheme.grid(column=1, row=0, padx=(20, 0), pady=(0,5))

            self.axesStateLabel = Label(self.styleFrame, text="Display Axes:")
            self.axesStateLabel.grid(column=0, row=1, pady=(0,5), sticky=W)

            self.axesState = ttk.OptionMenu(self.styleFrame, axesState, "On", *["On", "Off"])
            self.axesState.grid(column=1, row=1, padx=(20, 0), pady=(0,5))

            self.massStateLabel = Label(self.styleFrame, text="Display Masses:")
            self.massStateLabel.grid(column=0, row=2, pady=(0,5), sticky=W)

            self.massState = ttk.OptionMenu(self.styleFrame, massState, "On", *["On", "Off"])
            self.massState.grid(column=1, row=2, padx=(20, 0), pady=(0,5))

            self.lineThicknessLabel = Label(self.styleFrame, text="Line Thiccness:")
            self.lineThicknessLabel.grid(column=0, row=3, pady=(0,5), sticky=W)

            self.lineThickness = ttk.OptionMenu(self.styleFrame, lineThickness, "Thicc", *["Thicc", "Thin", "Custom"],
                                                command=self.customThiccness)
            self.lineThickness.grid(column=1, row=3, padx=(20, 0), pady=(0,5))

            self.lineColourLabel = Label(self.styleFrame, text="Line Colour:")
            self.lineColourLabel.grid(column=0, row=4, pady=(0,5), sticky=W)

            self.lineColourButton = Button(self.styleFrame, width=3, background=ColourConvert(buttonColours["line"]),
                                           borderwidth=1, activebackground=ColourConvert(buttonColours["line"]),
                                           relief="flat")
            self.lineColourButton.config(command=lambda: self.updateButtonColour(self.lineColourButton, "line"))
            self.lineColourButton.grid(column=1, row=4, columnspan=2, padx=(20, 0), pady=(0,5))

            self.lineStyleLabel = Label(self.styleFrame, text="Line Style:")
            self.lineStyleLabel.grid(column=0, row=5, pady=(0,5), sticky=W)

            self.lineStyle = ttk.OptionMenu(self.styleFrame, lineStyle, "─", *["─", "•", ".", "┄"])
            self.lineStyle.grid(column=1, row=5, padx=(20, 0), pady=(0,5))

            self.velocityColourLabel = Label(self.styleFrame, text="Velocity Colour:")
            self.velocityColourLabel.grid(column=0, row=6, pady=(0,5), sticky=W)

            self.velocityColour = ttk.OptionMenu(self.styleFrame, velocityColour, "Plasma", *["Plasma", "Rainbow 1", "Rainbow 2", "Custom"],
                                                 command=self.customCmap)
            self.velocityColour.grid(column=1, row=6, padx=(20, 0), pady=(0,5))

            self.massColoursLabel = Label(self.styleFrame, text="Mass Colours:")
            self.massColoursLabel.grid(column=0, row=7, pady=(0,5), sticky=W)

            self.mass1Label = Label(self.styleFrame, text="m1:")
            self.mass1Label.grid(column=1, row=7, pady=(0,5), sticky=W)

            self.mass1Button = Button(self.styleFrame, width=3, background=ColourConvert(buttonColours["mass1"]),
                                           borderwidth=1, activebackground=ColourConvert(buttonColours["mass1"]),
                                           relief="flat")
            self.mass1Button.config(command=lambda: self.updateButtonColour(self.mass1Button, "mass1"))
            self.mass1Button.grid(column=1, row=7, columnspan=2, padx=(25, 0), pady=(0,5), sticky=W)

            self.mass2Label = Label(self.styleFrame, text="m2:")
            self.mass2Label.grid(column=1, row=7, padx=(55, 0), pady=(0,5), sticky=W)

            self.mass2Button = Button(self.styleFrame, width=3, background=ColourConvert(buttonColours["mass2"]),
                                      borderwidth=1, activebackground=ColourConvert(buttonColours["mass2"]),
                                      relief="flat")
            self.mass2Button.config(command=lambda: self.updateButtonColour(self.mass2Button, "mass2"))
            self.mass2Button.grid(column=1, row=7, columnspan=2, padx=(80, 0), pady=(0,5), sticky=W)

        else:
            style = False
            root.geometry("180x308")
            root.wm_title("")
            self.styleTitleFrame.grid_forget()
            self.styleFrame.grid_forget()
            self.canvas.grid_forget()
            self.styleButton.config(text='Show Style Options')

    def updateAllColours(self, variable):
        if plotTheme.get() == 'Light':
            if buttonColours['line'] == (255, 255, 255):
                self.updateButtonColour(self.lineColourButton, 'line', newColour=(0, 0, 0))
            if buttonColours['mass1'] == (255, 255, 255):
                self.updateButtonColour(self.mass1Button, 'mass1', newColour=(0, 0, 0))
            if buttonColours['mass2'] == (255, 255, 255):
                self.updateButtonColour(self.mass2Button, 'mass2', newColour=(0, 0, 0))
        elif plotTheme.get() == 'Dark':
            if buttonColours['line'] == (0, 0, 0):
                self.updateButtonColour(self.lineColourButton, 'line', newColour=(255, 255, 255))
            if buttonColours['mass1'] == (0, 0, 0):
                self.updateButtonColour(self.mass1Button, 'mass1', newColour=(255, 255, 255))
            if buttonColours['mass2'] == (0, 0, 0):
                self.updateButtonColour(self.mass2Button, 'mass2', newColour=(255, 255, 255))

    def updateButtonColour(self, button, function, newColour=None):
        if not newColour:
            colour = buttonColours[function]
            prev = colour
            try:
                colour = GetColour()
                button.config(background=ColourConvert(colour),
                              activebackground=ColourConvert(colour))
                buttonColours[function] = colour
            except TypeError:
                colour = prev
                button.config(background=ColourConvert(colour),
                              activebackground=ColourConvert(colour))
        else:
            button.config(background=ColourConvert(newColour),
                          activebackground=ColourConvert(newColour))
            buttonColours[function] = newColour

    def customThiccness(self, variable):
        if lineThickness.get() == "Custom":
            self.lineThickness = ttk.Entry(self.styleFrame, width=10, textvariable=lineThiccnessEntryVal)
            self.lineThickness.grid(column=1, row=3, padx=(20, 0), pady=(0, 5))

    def customCmap(self, variable):
        if velocityColour.get() == "Custom":
            self.cmapButton1 = Button(self.styleFrame, width=3, background=ColourConvert(buttonColours["cmap1"]),
                                      borderwidth=1, activebackground=ColourConvert(buttonColours["cmap1"]),
                                      relief="flat")
            self.cmapButton1.config(command=lambda: self.updateButtonColour(self.cmapButton1, "cmap1"))
            self.cmapButton1.grid(column=1, row=6, columnspan=2, padx=(25, 0), pady=(0, 5), sticky=W)

            self.cmapButton2 = Button(self.styleFrame, width=3, background=ColourConvert(buttonColours["cmap2"]),
                                      borderwidth=1, activebackground=ColourConvert(buttonColours["cmap2"]),
                                      relief="flat")
            self.cmapButton2.config(command=lambda: self.updateButtonColour(self.cmapButton2, "cmap2"))
            self.cmapButton2.grid(column=1, row=6, columnspan=2, padx=(25, 0), pady=(0, 5))

            self.cmapButton3 = Button(self.styleFrame, width=3, background=ColourConvert(buttonColours["cmap3"]),
                                      borderwidth=1, activebackground=ColourConvert(buttonColours["cmap3"]),
                                      relief="flat")
            self.cmapButton3.config(command=lambda: self.updateButtonColour(self.cmapButton3, "cmap3"))
            self.cmapButton3.grid(column=1, row=6, columnspan=2, padx=(25, 0), pady=(0, 5), sticky=E)

    def PlotRandom(self):
        #empty = False
        #if self.muVal.get() == "":
        #    empty = True
        #    muVal.set(0)
        #if (float(self.muVal.get()) < 0 or float(self.muVal.get()) > 0.5) and muHold.get() == 1:
        #    tkinter.messagebox.showerror("Value Error",
        #                                     "μ must be between 0.01 and 0.49. Please provide a more appropriate value and try again.")
        #else:
            try:
                file = open("Plots\\InitialConditions.txt", "w")
                file.write('')
                file.close()
                file = open("Plots\\InitialConditions.txt", "a+")
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
                        #mu = round(np.random.uniform(low=0.01, high=0.49), 2)
                        mu = round(np.random.uniform(low=0, high=1), 2)
                    else:
                        mu = float(self.muVal.get())

                    Orbit([x, y, vx, vy], mu)
                    plt.savefig("Plots\\" + str(plot) + str(saveFormat.get()))
                    print("Plot", str(plot), "saved")
                    file.write("Plot "+str(plot)+":\n")
                    file.write("x = " + str(x) + "\n")
                    file.write("y = " + str(y) + "\n")
                    file.write("vx = " + str(vx) + "\n")
                    file.write("vy = " + str(vy) + "\n")
                    file.write("mu = " + str(mu) + "\n\n")
                    #if empty:
                    #    muVal.set("")
                file.close()

            except ValueError:
                tkinter.messagebox.showerror("Value Error",
                                             "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")

    def PlotValues(self):
        #if float(self.muVal.get()) < 0 or float(self.muVal.get()) > 0.5:
        #    tkinter.messagebox.showerror("Value Error",
        #                                 "μ must be between 0.01 and 0.49. Please provide a more appropriate value and try again.")
        #else:
            try:
                x = float(self.xVal.get())
                y = float(self.yVal.get())
                vx = float(self.vxVal.get())
                vy = float(self.vyVal.get())
                mu = float(self.muVal.get())

                filePath = asksaveasfilename(title="Save Plot", filetypes=(
                (str(saveFormat.get())[1:].upper(), "*" + str(saveFormat.get())), ("All files", "*")))
                if filePath != "":
                    Orbit([x, y, vx, vy], mu)
                    plt.savefig(str(filePath) + str(saveFormat.get()))
                    print("Plot Saved")
                else:
                    tkinter.messagebox.showerror("Save Error",
                                                 "There is no file name. Please provide a file name and try again.")
            except ValueError:
                tkinter.messagebox.showerror("Value Error",
                                             "A non-integer float value, or no value, has been entered. Please only use values that are integers or floats.")


    def PlotPotential(self):
        #if float(self.muVal.get()) < 0 or float(self.muVal.get()) > 0.5:
        #    tkinter.messagebox.showerror("Value Error",
        #                                 "μ must be between 0.01 and 0.49. Please provide a more appropriate value and try again.")
        #else:
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

def RGBtoFloat(rgb):
    return (int(rgb[0])/255, int(rgb[1])/255, int(rgb[2])/255)

def GetColour():
    colour = askcolor()
    return colour[0]

def Orbit(initial, mu):
    if plotTheme.get() == 'Dark':
        plt.style.use('dark_background')
    elif plotTheme.get() =='Light':
        plt.style.use('grayscale')

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

    if plotVel.get() == 1:
        if velocityColour.get() == "Custom":
            cmap = colours.LinearSegmentedColormap.from_list("", [RGBtoFloat(buttonColours['cmap1']),
                                                                  RGBtoFloat(buttonColours['cmap2']),
                                                                  RGBtoFloat(buttonColours['cmap3'])])
        else:
            cmap = cmapsDict[velocityColour.get()]

        #Plot general line to obtain correct axes
        if plotTheme.get() == 'Light':
            lineColour = (255, 255, 255)
        elif plotTheme.get() == 'Dark':
            lineColour = (0, 0, 0)
        flow=ax.plot(states[:, 0], states[:, 1], color=RGBtoFloat(lineColour), linewidth=0)[0]

        #Plot with velocity gradient:
        vel = np.sqrt(np.square(states[:,2]) + np.square(states[:,3]))
        points = np.array([states[:,0], states[:,1]]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        norm = plt.Normalize(vel.min(), vel.max())
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(vel)
        if lineThickness.get() == "Custom":
            lc.set_linewidth(lineThiccnessEntryVal.get().lower().count('c'))
        else:
            lc.set_linewidth(lineThicknessDict[lineThickness.get()][1])
        line = ax.add_collection(lc)
        if axesState.get() == 'On':
            cbar = fig.colorbar(line, ax=ax)
            cbar.ax.set_ylabel('Magnitude of Veclocity', rotation='vertical', fontsize=15)

    else:
        #Can be used to plot if not using velcoity gradient:
        if lineThickness.get() == "Custom":
            flow = ax.plot(states[:, 0], states[:, 1], lineStylesDict[lineStyle.get()],
                           color=RGBtoFloat(buttonColours["line"]),
                           linewidth=lineThiccnessEntryVal.get().lower().count('c'))[0]
        else:
            flow=ax.plot(states[:,0],states[:,1], lineStylesDict[lineStyle.get()],
                         color=RGBtoFloat(buttonColours["line"]),
                        linewidth=lineThicknessDict[lineThickness.get()][0])[0]


    #Plot Other Masses:
    if massState.get() == 'On':
        size = 10
        ax.plot(-mu,0,'o', color=RGBtoFloat(buttonColours["mass1"]), markersize=((1 - mu)*size))
        ax.plot(1 - mu,0,'o', color=RGBtoFloat(buttonColours["mass2"]), markersize=(mu * size))

    if axesState.get() == 'On':
        ax.set_title(r"Plot of the Orbit of a mass $m_3$", fontsize=16)
        ax.set_xlabel("$x$", fontsize=15)
        ax.set_ylabel("$y$", fontsize=15)

        textstr = '\n'.join((
            r'Initial Conditions',
            r'$x=%.2f$' % (initial[0],),
            r'$y=%.2f$' % (initial[1],),
            r'$v_x=%.2f$' % (initial[2],),
            r'$v_y=%.2f$' % (initial[3],),
            r'$\mu=%.2f$' % (mu,)))

        props = dict(boxstyle='round', facecolor=infoBoxColourDict[plotTheme.get()], alpha=0.5)

        ax.text(0.05, 0.95, textstr, transform=ax.transAxes,
                verticalalignment='top', bbox=props)
    else:
        plt.axis('off')

def Potential(mu, top):
    if plotTheme.get() == 'Dark':
        plt.style.use('dark_background')
    elif plotTheme.get() =='Light':
        plt.style.use('grayscale')

    if velocityColour.get() == "Custom":
        cmap = colours.LinearSegmentedColormap.from_list("", [RGBtoFloat(buttonColours['cmap1']),
                                                              RGBtoFloat(buttonColours['cmap2']),
                                                              RGBtoFloat(buttonColours['cmap3'])])
    else:
        cmap = cmapsDict[velocityColour.get()]

    def potential(x, y, mu):
        return (0.5 * (x ** 2 + y ** 2)) + ((1 - mu) / np.sqrt((x + mu) ** 2 + y ** 2)) + (
                    mu / np.sqrt((x + mu - 1) ** 2 + y ** 2))

    x = np.linspace(-2, 2, 30)
    y = np.linspace(-2, 2, 30)

    x, y = np.meshgrid(x, y)
    z = potential(x, y, mu)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.contour3D(x, y, z, 50, cmap=cmapsDict[velocityColour.get()])
    ax.invert_xaxis()

    if axesState.get() == 'On':
        ax.set_xlabel(r'$x$', fontsize=15)
        ax.set_ylabel(r'$y$', fontsize=15)
        ax.set_title('Plot of the Gravitational Potential for $\mu=%.2f$' % (mu,), fontsize=16)
        if top != 1:
            ax.set_zlabel(r'$z$', fontsize=15)
    else:
        plt.axis('off')

    if top == 1:
        ax.view_init(elev=90., azim=90)
        ax.w_zaxis.line.set_lw(0.)
        ax.set_zticks([])
        ax.dist = 7


root = Tk()

GUI = GUI(root)

root.wm_title("")

root.geometry("180x308")

root.resizable(width=False, height=False)

root.pack_propagate(0)
root.grid_propagate(0)

root.mainloop()
