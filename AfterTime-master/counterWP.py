'''
Omowumi L. Ademola, Rachael Wang
oademol1@binghamton.edu, rwang32@binghamton.edu
Final Project
A52 & A51
Kyle Miller
'''
'''
The Counter class models a simple up/down counter that maintains a single value
It can be imported and used in text-base OR GUI programs
In a GUI, an instance of this class can serve as the Model (MVC Meta-Pattern)
'''
class CounterWP:
  
  #-- Constructor -------------------------------------------------------------

  # param initValue (int)
  def __init__(self, initValue=0):
    self.__value = initValue

  #-- Predicates --------------------------------------------------------------

  # returns true or false if the counter is below zero
  def isNegative(self):
    return self.__value < 0

  # returns true of false is the counter is equal to zero
  def isZero(self):
    return self.__value == 0

  #-- Accessors ---------------------------------------------------------------

  # returns value (int)
  def getValue(self):
    return self.__value
  
  #-- Mutators ----------------------------------------------------------------

  # adds one to the counter value
  def increment(self):
    self.__value += 1

  # Does NOT stop at 0
  # subtracts one from the counter value
  def decrement(self):
    self.__value -= 1

  # sets counter value to 0
  def reset(self):
    self.__value = 0

  # param value (int)
  # sets counter value to the inputted value
  def set(self, value):
    self.__value = value

  #-- toString ----------------------------------------------------------------

  # returns a formatted representation of the counter value (str)
  def __str__(self):
    return "%s" % self.__value
  
    
