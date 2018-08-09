'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
Provides an interface for the user to control what skills their character
will use on the enemy, while showing the character name, enemy name, hp of the
enemy and character hp

Output:
  The current and total health points of the user character and enemy
Task (all names start with self.__):
  Create GUI with
    Model:
      userModel (CharCreate)
      playerOne (Damage)
      monster (Damage)
      normal (CounterWP)
      medium (CounterWP)
      special (CounterWP)
      heal (CounterWP)
    Views:
      playScreen (Canvas)
      spriteMonster (Canvas-image)
      indicateEnemy (Canvas-text)
      nameEnemy (Canvas-text)
      spritePlayer (Canvas-image)
      indicateUser (Canvas-text)
      namePlayer(Canvas-text)
    Controllers:
      specialButt (Button)
      medButt (Button)
      normButt (Button)
      healButt (Button)
    Organizational Widgets:
      parentFrame (Frame)
      playScreen (Canvas)
      topFrame (Frame)
      botFrame (Frame)
    Other instance objects:
      parent (GameParent)
    Classes Used:
      CharCreate
      Damage
      CreateScreen
      CounterWP
  dummyExit()
  quitExit()
  textUpdate()
  enemyAttack()
  endAttacks()
  noAttacksLeft()
  normalAttack()
  mediumAttack()
  specialAttack()
  healSpell()
  fightAgain()
  restartGame()
  quitGame()     
'''

from tkinter import *
import character
import damage
import createscreen
import counterWP

class GameGUI:

  #-- Constructor -------------------------------------------------------------

  def __init__(self,parent,char):
    # allows gui to be placed in the parent gui
    self.__parent = parent
    # gets the frame from the parent
    self.__parentFrame = self.__parent.getGameFrame()
    # gets the window from the parent
    self.__parentWin = self.__parent.getParentWin()    

    #-- Constants -------------------------------------------------------------
    self.__HEAL_AMNT = 2
    self.__NORM_AMNT = 9
    self.__MED_AMNT = 4
    self.__SPECIAL_AMNT = 1
    self.__MENU_WIN_W = 310
    self.__MENU_WIN_H = 55
    self.__CANVAS_W = 793
    self.__CANVAS_H = 300
    self.__BUTT_W = 40
    self.__BUTT_H = 5

    #-- Models ----------------------------------------------------------------
    # import the character class model from the character select screen
    self.__userModel = char
    self.__playerOne = damage.Damage()
    self.__monster = damage.Damage()
    self.__normal = counterWP.CounterWP(self.__NORM_AMNT)
    self.__medium = counterWP.CounterWP(self.__MED_AMNT)
    self.__special = counterWP.CounterWP(self.__SPECIAL_AMNT)
    self.__heal = counterWP.CounterWP(self.__HEAL_AMNT)

    # puts the frames in the parent frame
    self.__topFrame = Frame(self.__parentFrame)
    self.__botFrame = Frame(self.__parentFrame)

    # creates background image for where the fighting is going to take place
    self.__image_file = "GameFightBackground.gif"
    self.__image = PhotoImage(file=self.__image_file)
    self.__playScreen = Canvas(self.__topFrame, width=self.__CANVAS_W,
                               height=self.__CANVAS_H,
                               bd=2, relief=SUNKEN)
    self.__fightBG = self.__playScreen.create_image(404, 170, image=self.__image)

    # creates the sprite image, name and health indicator for the monster and
    # player as Canvas items
    self.__monsterImage = "dragon.gif"
    self.__dragon = PhotoImage(file=self.__monsterImage)
    self.__spriteMonster = self.__playScreen.create_image(700, 190,
                                                          image = self.__dragon)
    self.__indicateEnemy = self.__playScreen.create_text(780,260,
                                                         text=self.__monster,
                                                         fill='red',
                                                         font=('Time',30, 'bold'),
                                                         anchor=NE)
    self.__nameEnemy = self.__playScreen.create_text(780, 25, text='Thales the Dragon',
                                                     fill='white',
                                                     font=('Time',30,'bold'), anchor=NE)
    self.__spritePlayer = self.__playScreen.create_image(100, 215,
                                                         image=self.__userModel.getSprite())
    self.__indicateUser = self.__playScreen.create_text(20,260,
                                                        text=self.__playerOne,
                                                        fill='red',
                                                        font=('Time',30, 'bold'),
                                                        anchor=NW)
    self.__namePlayer = self.__playScreen.create_text(20, 25, text=self.__userModel.getName(),
                                                      fill='white',
                                                      font=('Time',30,'bold'), anchor=NW)
    
    # create the buttons for the user's attacks with names based on the
    # fighting class that was selected
    self.__specialButt = Button(self.__botFrame,text=('%s\n%s/%s' %
                                (self.__userModel.nameSpecialAttack(),
                                 self.__special, self.__SPECIAL_AMNT)),
                                width = self.__BUTT_W,height=self.__BUTT_H,
                                command=self.specialAttack)
    self.__medButt = Button(self.__botFrame,text=('%s\n%s/%s' %
                            (self.__userModel.nameMediumAttack(),
                             self.__medium, self.__MED_AMNT)),
                            width=self.__BUTT_W,height=self.__BUTT_H,
                            command=self.mediumAttack)
    self.__normButt = Button(self.__botFrame,text=('%s\n%s/%s' %
                             (self.__userModel.nameNormalAttack(),
                              self.__normal, self.__NORM_AMNT)),
                             width=self.__BUTT_W,height=self.__BUTT_H,
                             command = self.normalAttack)
    self.__healButt = Button(self.__botFrame,text=('%s\n%s/%s' %
                             (self.__userModel.nameHealSpell(),
                              self.__heal, self.__HEAL_AMNT)),
                             width=self.__BUTT_W,height=self.__BUTT_H,
                             command=self.healSpell)
   

    # places all of the widgets in the window using a grid configuration
    self.__topFrame.grid(column=0, row=0)
    self.__botFrame.grid(column=0, row=1)
    self.__playScreen.grid(column=0, row=0, columnspan=4)
    self.__healButt.grid(row=1, column=0, padx=10, pady=10)
    self.__normButt.grid(row=1, column=1, padx=10, pady=10)
    self.__medButt.grid(row=2, column=0, padx=10, pady=20)
    self.__specialButt.grid(row=2, column=1, padx=10, pady=20)


    mainloop()

  #-- Mutators ----------------------------------------------------------------

  # Makes a button do nothing
  # used to disable the title bar close button
  def dummyExit(self):
    pass

  # closes/destroys the parent windown
  def quitExit(self):
    self.__parentWin.destroy()

  # changes the canvas text to show the updated hp value string
  def textUpdate(self):
    self.__playScreen.itemconfig(self.__indicateEnemy, text=self.__monster)
    self.__playScreen.itemconfig(self.__indicateUser, text=self.__playerOne)

  # as long as the enemy is not dead it will use some random skill and then
  # update the hp indicator text
  def enemyAttack(self):
    if self.__monster.getHealth() > 0:
      self.__monster.enemyAI(self.__playerOne)
      self.textUpdate()

  # when either the user or monster's health is 0 the deathStatus will be true
  # and it will show the game over window
  def endAttacks(self):
    if (self.__monster.deathStatus() or self.__playerOne.deathStatus()):
      # all of the attack buttons get disabled
      self.__healButt.config(state=DISABLED)
      self.__normButt.config(state=DISABLED)
      self.__medButt.config(state=DISABLED)
      self.__specialButt.config(state=DISABLED)

      # the menu window gets created
      self.__menu = Tk()
      # names the window
      self.__menu.title("GAME OVER")
      # gets the dimensions of the monitors
      self.__w = self.__menu.winfo_screenwidth()
      self.__h = self.__menu.winfo_screenheight()
      # calculates where to put the window so that it would be centered
      self.__wPos = self.__w/2 - self.__MENU_WIN_W/2
      self.__hPos = self.__h/2 - self.__MENU_WIN_H/2
      # sets the window with the height, width, and offset values
      self.__menu.geometry('%dx%d+%d+%d' % (self.__MENU_WIN_W,
                                            self.__MENU_WIN_H, self.__wPos,
                                            self.__hPos))
      # makes this window stay on top
      self.__menu.wm_attributes('-topmost',1)
      # disables other windows within the program
      self.__menu.grab_set()
      # disables both the menu and parent windows close buttons
      self.__menu.protocol("WM_DELETE_WINDOW", self.dummyExit)
      self.__parentWin.protocol("WM_DELETE_WINDOW", self.dummyExit)

      # Creates frame, label and buttons
      self.__menuFrame = Frame(self.__menu)
      self.__messageLabel = Label(self.__menuFrame,
                                  text=(('CONGRATS %s! You beat the monster!' %
                                         self.__userModel.getName()) if
                                        self.__monster.deathStatus()else
                                        ('OH NO %s! You died!' %
                                         self.__userModel.getName())))
      self.__fightAgainButt = Button(self.__menuFrame, text='CONTINUE FIGHTING',
                                     command=self.fightAgain)
      self.__restartButt = Button(self.__menuFrame, text='RESTART GAME',
                                  command=self.restartGame)
      self.__quitButt = Button(self.__menuFrame, text='EXIT GAME',
                               command=self.quitGame)

      # places buttons using a grid configuration
      self.__menuFrame.grid(row=0,column=0)
      self.__messageLabel.grid(row=0,column=0,columnspan=3)
      self.__fightAgainButt.grid(row=1, column=0, padx=3)
      self.__restartButt.grid(row=1, column=1, padx=3)
      self.__quitButt.grid(row=1, column=2, padx=3)

  # when counter for all of the attacks are zero then it will show the game
  # over window
  def noAttacksLeft(self):
    if (self.__normal.isZero() and self.__medium.isZero()
        and self.__special.isZero() and self.__heal.isZero()):
      # the menu window gets created
      self.__menu = Tk()
      self.__menu.title("GAME OVER")
      # gets the dimensions of the computer screen      
      self.__w = self.__menu.winfo_screenwidth()
      self.__h = self.__menu.winfo_screenheight()
      self.__wPos = self.__w/2 - self.__MENU_WIN_W/2
      self.__hPos = self.__h/2 - self.__MENU_WIN_H/2      
      self.__menu.geometry('%dx%d+%d+%d' % (self.__MENU_WIN_W,
                                            self.__MENU_WIN_H, self.__wPos,
                                            self.__hPos))
      self.__menu.wm_attributes('-topmost',1)      
      self.__menu.grab_set()
      self.__menu.protocol("WM_DELETE_WINDOW", self.dummyExit)
      self.__parentWin.protocol("WM_DELETE_WINDOW", self.dummyExit)      

      # Creates frame, label and buttons
      self.__menuFrame = Frame(self.__menu)
      self.__messageLabel = Label(self.__menuFrame,
                                  text='You have no more attacks left')
      self.__fightAgainButt = Button(self.__menuFrame, text='CONTINUE FIGHTING',
                                     command=self.fightAgain)
      self.__restartButt = Button(self.__menuFrame, text='RESTART GAME',
                                  command=self.restartGame)
      self.__quitButt = Button(self.__menuFrame, text='EXIT GAME',
                               command=self.quitGame)

      # places buttons using a grid configuration
      self.__menuFrame.grid(row=0,column=0)
      self.__messageLabel.grid(row=0,column=0,columnspan=3)
      self.__fightAgainButt.grid(row=1, column=0, padx=3)
      self.__restartButt.grid(row=1, column=1, padx=3)
      self.__quitButt.grid(row=1, column=2, padx=3)     
    


  #-- Event Handlers --------------------------------------------------------

  # the users damage model attacks the monster damage model and vice versa
  # the text updates the counter decreases, the button text updates, and when
  # the counter equals zero the button is disabled and checks whether all the
  # other moves had been all used
  def normalAttack(self):
    # user model attacks monster model
    self.__playerOne.normalAttack(self.__monster)
    # text is updated
    self.textUpdate()
    # the enemy attacks
    self.enemyAttack()
    # calls method to test whether or not either on of the model's hp was
    # at zero
    self.endAttacks()
    # decreases the counter
    self.__normal.decrement()
    # updates the button to show the number of moves left
    self.__normButt.config(text=('%s\n%s/%s' %
                                 (self.__userModel.nameNormalAttack(),
                                  self.__normal, self.__NORM_AMNT)))
    # if the counter is equal to zero then the button is disabled and calls
    # the noAttacksLeft method to test whether all the counters are equal to
    # zero
    if self.__normal.isZero():
      self.__normButt.config(state=DISABLED)
      self.noAttacksLeft()      

  # the users damage model attacks the monster damage model and vice versa
  # the text updates the counter decreases, the button text updates, and when
  # the counter equals zero the button is disabled and checks whether all the
  # other moves had been all used
  def mediumAttack(self):
    self.__playerOne.mediumAttack(self.__monster)
    self.textUpdate()
    self.enemyAttack()
    self.endAttacks()
    self.__medium.decrement()
    self.__medButt.config(text=('%s\n%s/%s' %
                                 (self.__userModel.nameMediumAttack(),
                                  self.__medium, self.__MED_AMNT)))
    if self.__medium.isZero():
      self.__medButt.config(state=DISABLED)
      self.noAttacksLeft()

  # the users damage model attacks the monster damage model and vice versa
  # the text updates the counter decreases, the button text updates, and when
  # the counter equals zero the button is disabled and checks whether all the
  # other moves had been all used
  def specialAttack(self):
    self.__playerOne.specialAttack(self.__monster)
    self.textUpdate()
    self.enemyAttack()
    self.endAttacks()
    self.__special.decrement()
    self.__specialButt.config(text=('%s\n%s/%s' %
                                (self.__userModel.nameSpecialAttack(),
                                 self.__special, self.__SPECIAL_AMNT)))    
    if self.__special.isZero():
      self.__specialButt.config(state=DISABLED)
      self.noAttacksLeft()       

  # the users damage model heals itself, the text updates the counter
  # decreases, the button text updates, and when the counter equals
  # zero the button is disabled and checks whether all the
  # other moves had been all used
  def healSpell(self):
    self.__playerOne.healSpell()
    self.textUpdate()
    self.enemyAttack()
    self.endAttacks()
    self.__heal.decrement()
    self.__healButt.config(text=('%s\n%s/%s' %
                                (self.__userModel.nameHealSpell(),
                                 self.__heal, self.__HEAL_AMNT)))    
    if self.__heal.isZero():
      self.__healButt.config(state=DISABLED)
      self.noAttacksLeft()       

  # allows the user to just keep on fighting
  # allow the parent window to be closed using the default close buttton,
  # resets the hp indicator text, enables the attack buttons, sets the counters
  # back to their numberr of moves and updates the button text to show the
  # new value the counters, destroys the menu window
  def fightAgain(self):
    # allows window close button to close window
    self.__parentWin.protocol("WM_DELETE_WINDOW", self.quitExit)
    # sets the player and monsgter hp value to 100
    self.__playerOne.setHP(100)
    self.__monster.setHP(100)
    self.textUpdate()
    # enables the buttons
    self.__healButt.config(state=NORMAL)
    self.__normButt.config(state=NORMAL)
    self.__medButt.config(state=NORMAL)
    self.__specialButt.config(state=NORMAL)
    # the counters are set
    self.__normal.set(self.__NORM_AMNT)
    self.__medium.set(self.__MED_AMNT)
    self.__special.set(self.__SPECIAL_AMNT)
    self.__heal.set(self.__HEAL_AMNT)
    # the button text is updated
    self.__normButt.config(text=('%s\n%s/%s' %
                                 (self.__userModel.nameNormalAttack(),
                                  self.__normal, self.__NORM_AMNT)))
    self.__medButt.config(text=('%s\n%s/%s' %
                                 (self.__userModel.nameMediumAttack(),
                                  self.__medium, self.__MED_AMNT)))
    self.__specialButt.config(text=('%s\n%s/%s' %
                                (self.__userModel.nameSpecialAttack(),
                                 self.__special, self.__SPECIAL_AMNT)))
    self.__healButt.config(text=('%s\n%s/%s' %
                                (self.__userModel.nameHealSpell(),
                                 self.__heal, self.__HEAL_AMNT)))
    # the menu window is destroyed
    self.__menu.destroy()

  # allow the user to create a new character
  # the parent window in reactivated and the battle screen is removed
  # the counters are set and the button text is updated, the menu is destroyed
  # and the character creation screen is put back
  def restartGame(self):
    self.__parentWin.protocol("WM_DELETE_WINDOW", self.quitExit)
    # removes the frames and all the widgets within them from the screen
    self.__topFrame.grid_remove()
    self.__botFrame.grid_remove()
    self.__normal.set(self.__NORM_AMNT)
    self.__medium.set(self.__MED_AMNT)
    self.__special.set(self.__SPECIAL_AMNT)
    self.__heal.set(self.__HEAL_AMNT)
    self.__normButt.config(text=('%s\n%s/%s' %
                                 (self.__userModel.nameNormalAttack(),
                                  self.__normal, self.__NORM_AMNT)))
    self.__medButt.config(text=('%s\n%s/%s' %
                                 (self.__userModel.nameMediumAttack(),
                                  self.__medium, self.__MED_AMNT)))
    self.__specialButt.config(text=('%s\n%s/%s' %
                                (self.__userModel.nameSpecialAttack(),
                                 self.__special, self.__SPECIAL_AMNT)))
    self.__healButt.config(text=('%s\n%s/%s' %
                                (self.__userModel.nameHealSpell(),
                                 self.__heal, self.__HEAL_AMNT)))      
    self.__menu.destroy()
    # puts the character creation screen back into the window
    self.__charScreen = createscreen.CreateScreen(self.__parent)

  # the game is exited
  def quitGame(self):
    # the menu is destroyed
    self.__menu.destroy()
    # and the parent window is destroyed
    self.quitExit()
