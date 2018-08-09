'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
This Damage class creates an object that has a certain amount of health points
that can be removed and added at random amounts using the different attack
mutators and information about the health can be obtained through the accessors
'''
import random

class Damage:

  # Constructor ---------------------------------------------------------------

  # creates an object with certain amount of Health Points (default is 100)
  # param initHP (int)
  def __init__(self, initHP = 100):
    self.__hp = initHP
    self.__totalHP = initHP

  # Accessors -----------------------------------------------------------------

  # return the current hp
  def getHealth(self):
    return self.__hp

  # returns what the total hp is
  def getTotalHP(self):
    return self.__totalHP

  # returns true if the hp is equal to zero
  def deathStatus(self):
    return self.__hp == 0

  # Mutators ------------------------------------------------------------------

  # removes a certain amount of hp
  # param damage  (int)
  def removeHP(self, damage):
    self.__hp = self.__hp - damage
    if self.__hp < 0:
      self.setHP(0)

  # sets the HP to the number set
  # param newHP (int)
  def setHP(self, newHP):
    self.__hp = newHP

  # removes a random amount of health
  # param other (Damage)
  def normalAttack(self, other):
    damage = random.randint(5, 11)
    other.removeHP(damage)

  # removes a random amount of health
  # param other (Damage)
  def mediumAttack(self, other):
    damage = random.randint(8, 21)
    other.removeHP(damage)

  # removes a random amount of health
  # param other (Damage)    
  def specialAttack(self, other):
    damage = random.randint(10, 35)
    other.removeHP(damage)

  # adds a set amount of health
  # param point (int)
  def healSpell(self, point=15):
    # checks to see if current hp is less than the total hp
    if self.__hp < self.__totalHP:
      tick = 0
      # adds a health point one at a time while checking if the max amount
      # of points have been added and if the hp is less than the total hp
      while (tick < point) and (self.__hp < self.__totalHP):
        self.__hp += 1
        tick += 1
    else:
      pass

  # randomizes which attack/skill the computer will user
  # param other (Damage)
  def enemyAI(self, other):
    number = random.randrange(1,51)
    if number >=1 and number <40:
      self.normalAttack(other)
    elif number >=40 and self.__hp < 100:
      self.healSpell()
    else:
      self.mediumAttack(other)

  # toString ------------------------------------------------------------------

  # returns the HP of the damage object as a formatted string
  def __str__(self):
    return ("HP: %d/%d" % (self.__hp, self.__totalHP))
