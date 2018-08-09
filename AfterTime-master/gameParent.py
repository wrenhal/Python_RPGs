'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
Provides the screen where all the other guis for the game will be shown,
character creation and the battle scenes will take place in this window

Task (all names start with self.__):
  Create GUI with
    Model:
      charScreen (CharCreate)
    Views:
      storyScreen (Canvas)
      storyLine (Canvas-image)
    Controller:
      storyLine (Canvas-image) - clicking the image gets to the next window
    Organizational Widgets:
      gameFrame (Frame)
      canvasFrame (Frame)
      storyScreen (Canvas)
    Classes Used:
      SplashScreen
      GameGUI
      CreateScreen
  getGameFrame()
  getParentWin()
  nextDelete()
'''

import tkinter
import splashScreen
import gameGUI
import createscreen


class GameParent:

  #-- Constructor -------------------------------------------------------------
  def __init__(self):
    # creates window with the title AFTER TIME
    self.__win = tkinter.Tk()
    self.__win.title("AFTER TIME")

    #-- Constants -------------------------------------------------------------
    self.__WIN_W = 800
    self.__WIN_H = 600
    self.__IMAGE_X = 398
    self.__IMAGE_Y = 298

    # get the dimension of the monitor screen
    self.__w = self.__win.winfo_screenwidth()
    self.__h = self.__win.winfo_screenheight()
    # calculates where to put the window so that it would be centered
    self.__wPos = self.__w/2 - self.__WIN_W/2
    self.__hPos = self.__h/2 - self.__WIN_H/2
    # sets the window with the height, width, and offset values
    self.__win.geometry('%dx%d+%d+%d' % (self.__WIN_W, self.__WIN_H,
                                         self.__wPos, self.__hPos))

    # creates the frames for the image and all the other guis
    self.__gameFrame = tkinter.Frame(self.__win)
    self.__canvasFrame = tkinter.Frame(self.__win)

    # creates the canvas to that the storyline image can be displayed
    self.__storyScreen = tkinter.Canvas(self.__canvasFrame, width=self.__WIN_W,
                                height=self.__WIN_H)
    self.__image = "GameStoryLine1.gif"
    self.__storyPhoto = tkinter.PhotoImage(file=self.__image)
    self.__storyLine = self.__storyScreen.create_image(self.__IMAGE_X,
                                                       self.__IMAGE_Y,
                                                       image=self.__storyPhoto)

    # clicking the image allows the event to take place which is to got to the
    # next gui screen
    self.__storyScreen.tag_bind(self.__storyLine, '<Button-1>', self.nextDelete)

    # places the widgets in the window using the grid configuration
    self.__canvasFrame.grid(row=0,column=0)
    self.__storyScreen.grid(row=0,column=0)

    tkinter.mainloop()

  #-- Accessor ----------------------------------------------------------------

  # returns the parent gameFrame (Frame)
  def getGameFrame(self):
    return self.__gameFrame

  # returns the parent window (Tk)
  def getParentWin(self):
    return self.__win

  #-- Event Handlers ----------------------------------------------------------

  # removes the canvas and image and allows the character selection screen
  # to appear
  def nextDelete(self, event):
    self.__storyScreen.delete(self.__storyLine)
    self.__storyScreen.grid_remove()
    self.__canvasFrame.grid_remove()
    self.__gameFrame.grid(row=0,column=0)
    self.__charScreen = createscreen.CreateScreen(self)


#-- Main ----------------------------------------------------------------------

def main():
  splashScreen.SplashScreen()
  GameParent()
main()
