'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
Provides an interface for the user to create a character with the ablity for
them to input a name and choose a character class/image

Output:
  The name the user enters for the character (str)
  visual representation of which character class you have choosen (image)
Input:
  name of character in entry box (str)
Task (all names start with self.__):
  Create GUI with
    Model:
      player (CharCreate)
      fightScreen (GameGUI)
    Views:
      warriorChar (Canvas-item)
      mageChar (Canvas-item)
      healerChar (Canvas-item)
      userNameLabel (Label)
      nameVal (StringVar)
    Controllers:
      nameLabel (Label)
      charLabel (Label)
      nameEntry (Entry)
      okButt (Button)
      nextButt (Button)
    Organizational Widgets:
      parentFrame (Frame)
      charFrame (Frame)
      charCanvas (Canvas)
    Other instance objects:
      parent (GameParent)
    Classes Used:
      CharCreate
      GameGUI
  testName()
  classTest()
  getSavedName()
  getClass()
  getImage()
  saveName()
  saveNameE()
  selectCharHealer()
  selectCharMage()
  selectCharWarrior()
  nextScreen()
'''

from tkinter import *
import tkinter.messagebox
import character
import gameGUI

class CreateScreen:

  #-- Constructor -------------------------------------------------------------

  def __init__(self, parent):
    # allows this gui to be placed in the gui
    self.__parent = parent
    # gets the frame from the parent
    self.__parentFrame = self.__parent.getGameFrame()
    # sets the character name and fighting class to empty strings
    self.__nameStr = ''
    self.__gameClass = ''

    #-- Constants -------------------------------------------------------------
    self.__MAGE_CLASS = 'Mage'
    self.__WARRIOR_CLASS = 'Warrior'
    self.__HEALER_CLASS = 'Healer'

    # creates a frame where all the widgets will live within the parent frame
    self.__charFrame = Frame(self.__parentFrame) 
    self.__nameLabel = Label(self.__charFrame, text= 'Name?', font=('bold'))
    self.__nameEntry = Entry(self.__charFrame, width=20)
    self.__nameEntry.bind('<Return>', self.saveNameE)
    self.__okButt = Button(self.__charFrame, text='OK', command= self.saveName)
    self.__nextButt = Button(self.__charFrame, text='NEXT',
                             command= self.nextScreen)
    self.__charLabel = Label(self.__charFrame, text= 'CHOOSE A CHARACTER',
                             font=('TkDefaultFont',15,'bold'))

    # creates a string variable and label that will display the name the user
    # enters
    self.__nameVal = StringVar()
    self.__nameVal.set('')
    self.__userNameLabel = Label(self.__charFrame,
                                 textvariable=self.__nameVal, font=('bold'))
    
    # creates a canvas in which images can live and be displayed
    self.__charCanvas = Canvas(self.__charFrame, width=650, height=440)

    # the image files are sent to PhotoImage so that they will visible
    # in tkinter, one standard and one faded to be the active and selected
    # image
    self.__spriteW = "spriteWarrior.gif"
    self.__spriteWarrior = PhotoImage(file=self.__spriteW)
    self.__warrior_image = "WarriorStandard.gif"
    self.__warrior_fadedImage = "WarriorFaded.gif"
    self.__warrior = PhotoImage(file=self.__warrior_image)
    self.__warriorFaded = PhotoImage(file=self.__warrior_fadedImage)
    # creates an image at the coordinate position that changes to a differentt
    # images when you mouse over it
    self.__warriorChar = self.__charCanvas.create_image(132, 200,
                                                        image = self.__warrior,
                                                        activeimage=
                                                        self.__warriorFaded)

    # the image files are sent to PhotoImage so that they will visible
    # in tkinter, one standard and one faded to be the active and selected
    # image    
    self.__spriteM = "spriteGif.gif"
    self.__spriteMage = PhotoImage(file=self.__spriteM)
    self.__mage_image = "MageStandard.gif"
    self.__mage_fadedImage = "MageFaded.gif"
    self.__mage = PhotoImage(file=self.__mage_image)
    self.__mageFaded = PhotoImage(file=self.__mage_fadedImage)
    # creates an image at the coordinate position that changes to a differentt
    # images when you mouse over it
    self.__mageChar = self.__charCanvas.create_image(332, 200,
                                                   image = self.__mage,
                                                   activeimage = self.__mageFaded)

    # the image files are sent to PhotoImage so that they will visible
    # in tkinter, one standard and one faded to be the active and selected
    # image
    self.__spriteH = "spriteHealer.gif"
    self.__spriteHealer = PhotoImage(file=self.__spriteH)
    self.__healer_image = "HealerStandard.gif"
    self.__healer_fadedImage = "HealerFaded.gif"
    self.__healer = PhotoImage(file=self.__healer_image)
    self.__healerFaded = PhotoImage(file=self.__healer_fadedImage)
    # creates an image at the coordinate position that changes to a differentt
    # images when you mouse over it
    self.__healerChar = self.__charCanvas.create_image(532, 200,
                                                   image = self.__healer,
                                                   activeimage = self.__healerFaded)

    # binds an event (left mouse click) and event handler to each image
    self.__charCanvas.tag_bind(self.__warriorChar, '<Button-1>', self.selectCharWarrior)
    self.__charCanvas.tag_bind(self.__mageChar, '<Button-1>', self.selectCharMage)
    self.__charCanvas.tag_bind(self.__healerChar, '<Button-1>', self.selectCharHealer)
    
    # puts all the widgets in the window in a grid formatting
    self.__charFrame.grid(row=0,column=0)
    self.__nameLabel.grid(row=0,column=0)
    self.__nameEntry.grid(row=1, column=0, pady=3)
    self.__okButt.grid(row=2, column=0, pady=3, sticky=W+E)
    self.__charLabel.grid(row=0,column=1, rowspan=4,padx = 200)
    self.__charCanvas.grid(row=4, column=1)
    self.__nextButt.grid(row=5,column=1,sticky=E)

    self.__userNameLabel.grid(row=3, column=0)    
    
    mainloop()

  #-- Predicates --------------------------------------------------------------

  # returns true of false depending on if the length of the string is less
  # than 1
  def testName(self):
    return len(self.__nameStr)<3 or len(self.__nameStr)>12

  # returns true of false depending on if the length of the string is less
  # than 3
  def classTest(self):
    return len(self.__gameClass) < 3

  #-- Accessors ---------------------------------------------------------------

  # returns the nameStr (str)
  def getSavedName(self):
    return self.__nameStr

  # returns the gameClass, fighting class (str)
  def getClass(self):
    return self.__gameClass

  # returns the spriteImage (image)
  def getImage(self):
    return self.__spriteImage  

  #-- Event Handlers ----------------------------------------------------------

  # takes the character name tests if it has an appropriate length, shows
  # warning box if it doesn't saves and displays the name if it does
  def saveName(self):
    # gets input from Entry box
    self.__nameStr = self.__nameEntry.get()    
    if self.testName():
      tkinter.messagebox.showwarning('WARNING', 'Name must be between 3 and 12 \
characters long')
      # clears Entry box
      self.__nameEntry.delete(0,END)
      self.__nameVal.set('')
    else:
      # sets the variable value
      self.__nameVal.set(self.__nameStr)
      self.__nameEntry.delete(0,END)

  # same as above but attached to nameEntry (Entry box)
  def saveNameE(self, event):
    self.saveName()

  # sets spriteImage, and gameClass to objects associated with the Healer
  # fighting class, sets the Healer picture to the faded verison to indicate
  # that it's been clicked on, and sets the other two picture to the standard
  # version to indicate that it's been deselected
  def selectCharHealer(self, event):
    # the image that will be on the battle screen
    self.__spriteImage = self.__spriteHealer
    # the argument that will be sent to the CharCreate class
    self.__gameClass = self.__HEALER_CLASS
    # updates the canvas image items
    self.__charCanvas.itemconfig(self.__healerChar, image = self.__healerFaded)
    self.__charCanvas.itemconfig(self.__mageChar, image = self.__mage)
    self.__charCanvas.itemconfig(self.__warriorChar, image = self.__warrior)

  # sets spriteImage, and gameClass to objects associated with the Mage
  # fighting class, sets the Mage picture to the faded verison to indicate
  # that it's been clicked on, and sets the other two picture to the standard
  # version to indicate that it's been deselected
  def selectCharMage(self, event):
    # the image that will be on the battle screen
    self.__spriteImage = self.__spriteMage
    # the argument that will be sent to the CharCreate class
    self.__gameClass = self.__MAGE_CLASS
    # updates the canvas image items
    self.__charCanvas.itemconfig(self.__mageChar, image = self.__mageFaded)
    self.__charCanvas.itemconfig(self.__healerChar, image = self.__healer)
    self.__charCanvas.itemconfig(self.__warriorChar, image = self.__warrior)

  # sets spriteImage, and gameClass to objects associated with the Warrior
  # fighting class, sets the Warrior picture to the faded verison to indicate
  # that it's been clicked on, and sets the other two picture to the standard
  # version to indicate that it's been deselected
  def selectCharWarrior(self, event):
    # the image that will be one the battle screen
    self.__spriteImage = self.__spriteWarrior
    # the argument that will be sent to the CharCreate class
    self.__gameClass = self.__WARRIOR_CLASS
    # updates the canvas image items
    self.__charCanvas.itemconfig(self.__warriorChar, image = self.__warriorFaded)
    self.__charCanvas.itemconfig(self.__healerChar, image = self.__healer)
    self.__charCanvas.itemconfig(self.__mageChar, image = self.__mage)

  # tests whether a name with appropriate length was entered and displays a
  # messagebox if it was not, then tests if a class was selected otherwise
  # displaying a messagebox, if everything is done right, the player model
  # is created, the character creation screen is destroyed and the fightScreen
  # created
  def nextScreen(self):
    # tests the string length
    if self.testName():
      tkinter.messagebox.showwarning('WARNING', 'You need to input a name greater \
than 3 characters!')
    # tests the gameClass length if none was selected it would not be long
    # enough
    elif self.classTest():
      tkinter.messagebox.showwarning('WARNING', 'You need to select a class!')
    else:
      # creates character model
      self.__player = character.CharCreate(self.getSavedName(), self.getClass(),
                                           self.getImage())
      # destroyes charFrame
      self.__charFrame.destroy()
      # initializes battle screen model gui
      self.__fightScreen = gameGUI.GameGUI(self.__parent, self.__player)
