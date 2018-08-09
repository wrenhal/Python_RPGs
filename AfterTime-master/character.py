'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
This CharCreate (Character Create) class creates an object that has name,
a fighting class and an image for the object.  Depending on the fighting class
there are different names for each fighting skill, you can also retrive the
name, fighting class and image for the object
'''
class CharCreate:

  #-- Constructor -------------------------------------------------------------

  # creates object with name, fighting class and image
  # param name (str)
  # param fClass (str)
  # param sprite (image)
  def __init__(self, name, fClass, sprite):
    self.__charName = name
    self.__charSprite = sprite
    self.__fightClass = fClass

  #-- Constants ---------------------------------------------------------------

    self.__MAGE_CLASS = 'Mage'
    self.__WARRIOR_CLASS = 'Warrior'
    self.__HEALER_CLASS = 'Healer'

  #-- Accessors ---------------------------------------------------------------

  # returns the character name (str)
  def getName(self):
    return self.__charName

  # returns the character sprite image (image)
  def getSprite(self):
    return self.__charSprite

  # returns the fighting class name (str)
  def getfightClass(self):
    return self.__fightClass

  # returns the name for the normal skill attack (str)
  def nameNormalAttack(self):
    if self.__fightClass == self.__MAGE_CLASS:
      self.__nameNormal = "Magic Ball"
    elif self.__fightClass == self.__WARRIOR_CLASS:
      self.__nameNormal = "Slam"
    elif self.__fightClass == self.__HEALER_CLASS:
      self.__nameNormal = "Parry"
    else:
      self.__nameNormal = "This class doesn't exist"
    return self.__nameNormal

  # returns the name for the medium skill attack (str)
  def nameMediumAttack(self):
    if self.__fightClass == self.__MAGE_CLASS:
      self.__nameMedium = "Arcane Blast"
    elif self.__fightClass == self.__WARRIOR_CLASS:
      self.__nameMedium = "Charge"
    elif self.__fightClass == self.__HEALER_CLASS:
      self.__nameMedium = "Strike"
    else:
      self.__nameMedium = "This class doesn't exist"
    return self.__nameMedium

  # returns the name for the special skill attack (str)
  def nameSpecialAttack(self):
    if self.__fightClass == self.__MAGE_CLASS:
      self.__nameSpecial = "Flamestrike"
    elif self.__fightClass == self.__WARRIOR_CLASS:
      self.__nameSpecial = "Colossus Smash"
    elif self.__fightClass == self.__HEALER_CLASS:
      self.__nameSpecial = "Starfall"
    else:
      self.__nameSpecial = "This class doesn't exist"
    return self.__nameSpecial 

  # returns the name for the heal skill (str)
  def nameHealSpell(self):
    if self.__fightClass == self.__MAGE_CLASS:
      self.__nameHeal = "Rejuvenation"
    elif self.__fightClass == self.__WARRIOR_CLASS:
      self.__nameHeal = "Renew"
    elif self.__fightClass == self.__HEALER_CLASS:
      self.__nameHeal = "Lifebloom"
    else:
      self.__nameHeal = "This class doesn't exist"
    return self.__nameHeal

  #-- toString ----------------------------------------------------------------

  # returns the name of the character as formatted string 
  def __str__(self):
    return ("%s (%s)" % (self.__charName, self.__fightClass))
