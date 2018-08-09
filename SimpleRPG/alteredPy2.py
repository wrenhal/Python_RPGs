import random
from random import randint

class Character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
  def do_damage(self, enemy):
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0:
      print "%s evades the %s's attack.\n -%dhp" % (enemy.name, self.name, damage)
    else: print "%s hurts the%s!\n -%dhp" % (self.name, enemy.name, damage)
    return enemy.health <= 0

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    enemy_name1 = randint(0, 7)
    ex = randint (3, player.health_max)
    if enemy_name1 == 0:
      en = " super mutant"
      eh = ex +3
    elif enemy_name1 == 1:
      en = " raider"
      eh = ex 
    elif enemy_name1 == 2:
      en = " mole rat"
      eh = ex -1
    elif enemy_name1 == 3:
      en = " Brotherhood paladin"
      eh = ex +2
    elif enemy_name1 == 4:
      en = " Enclave solider"
      eh = ex +3
    elif enemy_name1 == 5:
      en = " feral goul"
      eh = ex +1
    elif enemy_name1 == 6:
      en = " deathclaw"
      eh = ex +4
    elif enemy_name1 == 7:
      en = " mirelurk"
      eh = ex +1
    self.name = "%s"%(en)
    self.health = eh

class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.merchstate = 'normal'
    self.health = 10
    self.health_max = 10
    self.loot = 10
    self.stim = 2
    self.ammo = 10
  def quit(self):
    print "%s can't find the way back home, and dies of starvation.\nR.I.P." % self.name
    self.health = 0
  def help(self): print Commands.keys()
  def status(self): print "%s's health: %d/%d\n caps:%d stim:%d e.cells:%d" % (self.name, self.health, self.health_max, self.loot, self.stim, self.ammo)
  def oofammo(self):
    if self.ammo <= 0:
      print"Might as well be dead, without ammo,\nin the wastes."
      self.health = 0   
  def item1(self):
    if self.merchstate == 'buy' :
      if self.merchstim > 0:
        if self.loot >=20:
          self.stim = self.stim +1
          self.loot = self.loot - 20
          self.merchstim = self.merchstim -1
          print"%s bought 1 Stimpack." % self.name
        else: print "Not enough caps."
      else: print "Merchant has no Stimpacks."
    else:
      print "No merchant."
      self.merchstate = 'normal'
  def item2(self):
    if self.merchstate == 'buy' :
      if self.merchammo > 0:
        if self.loot >= 10:
          self.ammo = self.ammo + 5
          self.loot = self.loot - 10
          self.merchammo = self.merchammo - 5
          print"%s bought 5 E.Cells." % self.name 
        else: print"Not enough caps."
      else: print"Merchant has no E.Cells."
    else:
      print "No merchant."
      self.merchstate = 'normal'
  def sell(self):
    if self.merchstate == 'buy' :
      if self.stim > 0:
          self.stim = self.stim -1
          self.loot = self.loot + 10
          self.merchstim = self.merchstim +1
          print"%s sold 1 Stimpack." % self.name
      else: print "%s has no Stimpacks." % self.name
    else:
      print "No merchant."
      self.merchstate = 'normal'
  def stim(self):
    if self.stim > 0:
      if self.health < self.health_max:
        self.health = self.health + 2
        self.stim = self.stim -1
        print "used stimpack.\n +2hp."
        if self.health > self.health_max:
          self.health = self.health_max
      else: print "full health."
    else: print "no stimpacks."
  def merch(self):
    self.merchstate = 'buy'
    self.merchammo = 0
    self.merchstim = 0
    self.merchstim = self.merchstim + randint(0,10)
    self.merchammo = self.merchammo + randint(0, 50)
    print "%s encounters a merchant!" % self.name
    print "Merchants items:\n Stimpacks:%d\n E.Cells:%d" % (self.merchstim, self.merchammo)
  def tired(self):
    print "%s feels tired." % self.name
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print "%s can't rest now!" % self.name; self.enemy_attacks()
    else:
      print "%s rests." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s is rudely awakened by a %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print "%s slept too much." % self.name; self.health = self.health - 1
  def areas(area1, n=1):
      a1 = area1.split('\n')
      random.shuffle(a1)
      area = []
      for a in range(n):
          try:
              s = a1[a]
              s = s.capitalize() + '.'
              area.append(s)
          except IndexError:
              break
      return area
  area1 = """\
  the waste-land
  the super-duper-mart
  the vault"""
  area = areas(area1, 1)
  for item in area:
     item
  def explore(self):
    self.oofammo()
    self.merchstate = 'normal'
    if self.state != 'normal':
      print "%s is too busy right now!" % self.name
      self.enemy_attacks()
    elif self.ammo > 0:
      print "%s explores%s" % (self.name, Player.item)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s encounters a%s!\n Enemy hp: %d." % (self.name, self.enemy.name, self.enemy.health)
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
        if randint(0, 1): self.merch()
  def flee(self):
    if self.state != 'fight': print "%s runs in circles for a while." % self.name; self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print "%s flees from the%s." % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
      else: print "%s couldn't escape from the%s!" % (self.name, self.enemy.name); self.enemy_attacks()
  def attack(self):
    self.oofammo()
    self.ammo = self.ammo - 1
    if self.state != 'fight': 
      if self.ammo > 0: print "%s shoots into the air, without notable results." % self.name; self.tired()
    else:
      if self.do_damage(self.enemy):
        print "%s executes %s!" % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
        eloot = randint(0, 25)
        self.loot = eloot + self.loot
        print "you recovered %d caps from the corpse." %(eloot)
        eammo = randint (0, 5)
        self.ammo = eammo + self.ammo
        print "you recovered %d energy cells from the corpse." %(eammo)
        stimp = randint(0, 4)
        if stimp == 0:
          self.stim = self.stim +1
          print "you recoverd a stimpack!"
        if randint(0, self.health_max) == 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print "%s feels stronger!" % self.name
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print "%s was slaughtered by %s!!!\nR.I.P.\n" %(self.name, self.enemy.name)
Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'stat': Player.status,
  'rest': Player.rest,
  'e': Player.explore,
  'run': Player.flee,
  'a': Player.attack,
  'stim': Player.stim,
  '1': Player.item1,
  '2': Player.item2,
  'sell': Player.sell
  }

p = Player()
p.name = raw_input("What is your character's name? ")
print "(type help to get a list of actions)\n"
print "%s ventures the wastes, searching for adventure." % p.name

while(p.health > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print "%s doesn't understand the suggestion." % p.name

"""
Code by Maxwell Phelps 2013

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.
"""