'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
A screen that starts playing music and shows an image with the title of the
game and other information

Task (all names start with self.__):
  Create GUI with
    Views:
      splash (Canvas)
      gameSplash (Canvas-image)
    Organizational Widgets:
      splash (Canvas)
    Classes Used:
      winsound
  quit()
'''

from tkinter import *
import winsound

class SplashScreen:

  def __init__(self):
    self.__win = Tk()

    winsound.PlaySound('The Descent.wav',
                       winsound.SND_ASYNC|winsound.SND_LOOP)

    #-- Constants -------------------------------------------------------------
    self.__WIN_W = 800
    self.__WIN_H = 600

    # doesn't show the window frame
    self.__win.overrideredirect(True)
    # gets the dimensions of the monitor screen
    self.__w = self.__win.winfo_screenwidth()
    self.__h = self.__win.winfo_screenheight()
    # calculates where to put the window so that it would be centered    
    self.__wPos = self.__w/2 - self.__WIN_W/2
    self.__hPos = self.__h/2 - self.__WIN_H/2
    # sets the window with the height, width, and offset values    
    self.__win.geometry('%dx%d+%d+%d' % (self.__WIN_W, self.__WIN_H,
                                         self.__wPos, self.__hPos))

    # creates a canvas so that the opening image can be displayed
    self.__image_file = "splashScreenGif.gif"
    self.__image = PhotoImage(file=self.__image_file)
    self.__splash = Canvas(self.__win, height = self.__h*0.8,
                           width = self.__w*0.6, bg="black")
    self.__gameSplash = self.__splash.create_image(400, 300, image=self.__image)
    self.__splash.grid()

    # clicking the image or window closes the splashscreen window
    self.__win.bind("<Button-1>", self.quit)
    self.__win.mainloop()

  #-- Event Handler -----------------------------------------------------------

  # destroys the window
  def quit(self, event):
    self.__win.destroy()
