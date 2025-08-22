
# i poured my heart and soul into this picture.

"""
/.                                                                              
,/,                                                                             
  /*                                                                            
   */.                                                                          
    ./*                  ,*(#%#(**..                 ..                         
      //.         .,//((/(%%%#((//*//***,,,****,*,,,,,*((#/.                    
       ,/*   .*//(##(((((%&%#(((/////******/(////*,,,,,,(%##/,,                 
        /((####(#%######(%%%((((((////******////**,,,,,.*(&%#*,//,              
       (##%%%%%%%%##%%%%#%%#((&&&&&&&%#((/**///###((/((*.*%%#***##((/*.         
       (#%%%%%%%%%%%%&&&%%%%#%%%%%&&&@&%#(/****/###%%&%##*(%/***/##((((/*       
       ,#%%%%%%%%%%&&&&&&%#(#####%%%%###((/***,.*/((((((/*##////*/#(((((//*     
        /%%%%%%%%%%%%&&&&%(((####%%##(((((//**,,,,,**/*,,,#/((((///((((((/.     
         (%%###%%%&&&&&&&%(((###((###((/((((/*/*,,,.,,,,..//(((((////((((*      
          *%#%%%%&&&&&&&&%%###(/((#(((//(%#%&%#%*.,...,,,*//#(((((////((/       
            (&%%&%%%&&%%&%%%%%#####((((##&@@@&&&@%, .,**((/((((((((///(/.       
              ,(&&%*&&&&&%%%%%#(/((((##%%&&&@&&@(*,..*/(((/(((((((((//*         
                 .//&&&&&&%#%%%#(((((##%%&&&&&%##*,.,(((##(#((((((((,           
                 /#%&&&&%%%##%#%#####%&&&@@&&&&%%(*,*((#%(.  ,***               
            ,///*/#%%%&%%%%#####%%%%#####(((#//*****//###/                      
        #//(//////%%&&&%%%%#####%%####%%(##(**////**/((((.                      
    #//((((/((((((#&&&&%%%###########%%#%%%(*/(/****/(*..                       
  ,(#((((((//((####%&&&&&%#((((((((##%%%%%#((//***/(//**,                       
#,(########//(####%&%&&&&&&&&@&%%%@@%##((/(/////////(///*.                       
######(###(//(##%%%%&&&&&&&&&@&&&&&&&&&&%%%%##(((((##(/**,        .              
#%%%##%%#((((###%%%%%&&&&&&%%&@&&&&@&%%##%(((/(//(((((((*/*.      .              
#%%%#%%#(((###%%%%%%%%&&&&&@&%%%##%&&%#####(##(///(/*,,(/***.     .              
#&%%#%#(((#%%%%%%%%%%%%%&&%%&&&&&&&&%%%%##((((((//****//****,                    
#&&%##((###%%%%%%%%%%%%%%%&%%%%&&%%%%%%#####(((((***********                     
#%&%((((#%#%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%%%#((//////*******,                     
#&&&(((#%%%%%%%%%%%%%%%%%%&%%%%%%%###%%%#(((//////((/***/**,,                    
#&&%((#%%%%&&%%%%%%%%%%%%%%%%%#########%#(((//(//((((///**,,*,                   
#&&###%%%%&&%%%&%%%%%%%%%%%%%##########(////(////(((/(/*******.      

doge 1493BC-2034AC
by paul 'the artiste'

"""

# jk i downloaded this from the internet

# time for sleep

import random
import time
import os

from colorama import Fore
# pyfiglet for title and oregon trail.
# man i made this game super unbalanced
health = 50
yourAtk = 4
equipment = ['farmers hat', 'overalls', 'boots']
weapons = []
damageW = []
# damageW is damage of weapons
# chainsaw = 0
stuff = []
pets = []
defenceVal = [1, 3, 2]
# defence of equipment # farmers hat = 0 overalls = 1 boots = 2
# petDamage is added to your damage
petHealth = [25, 10, 30]
petDamage = [5, 6, 7]
# cat = 0 index
# bird = 1 index
# dog = 2 index
swingAbles = ['pitchfork', 'fishing rod', 'chainsaw', 'scythe', 'sledgehammer']
friends = []
friHealth = []
# starting monster health
mHealth = 25
mDamage = 5
# the website i used for satan text
# lingojam.com/ZalgoText
# random hurt and heal values
r1 = random.randint(1, 50)
r2 = random.randint(-50, -10)
r3 = random.randint(1, 50)
r4 = random.randint(-50, -10)
r5 = random.randint(1, 50)
r6 = random.randint(-50, -10)
r7 = random.randint(1, 50)
r8 = random.randint(-50, -10)
r9 = random.randint(1, 50)
r10 = random.randint(-50, -10)
randHealList = [r1, r3, r5, r7, r9]
randChoiceFromHealList = random.choice(randHealList)
randHurtList = [r2, r4, r6, r8, r10]
randChoiceFromHurtList = random.choice(randHurtList)

goBack = ['go back', 'come back', 'back', 'return', 'return back']
listOfMonsters = []
# JAIL FOR PEOPLE WHO SAY BAD WORD

badWord = [
  'fuck', 'shit', 'bastard', 'motherfucker', 'bullshit', 'holy shit', 'cunt',
  'pussy', 'cocksucker', 'fucker', 'shiter', 'penis', 'cock', 'balls'
]
# please DO NOT ASK ME OKOKOKOK PLESE PLSEPELSEPLSE DONT OK?
listOfGirlNames = ['Sally','Sophia','Isabella','Mia','Evelyn','Emma','Olivia','Ava','Sofia','Amelia','Avery','Charlotte','Ava','Harper','Camila','Luna','Gianna','Elizabeth','Eleanor','Ella','Abigail','Scarlett','Aria','Penelope','Chloe','Madison','Ellie','Lily','Nova','Isla','Victoria','Willow','Emilia','Stella','Zoe','Grace','Violet','Aurora','Riley','Hazel','Nora','Zoey','Hannah','Addison','Mila','Layla']

# JAIL FOR PEOPLE WHO SAY BAD WORD!

listOfPhoneNum = ['cat', 'police', 'satan']
randPhoneNum = random.choice(listOfPhoneNum)
################################
# secret menu of Oregon Trail! #
################################
secretMenu = random.randint(1, 4)

# i love this
# hurt probably unused

def hurt():
  global health
  global defenceVal
  health = health + randChoiceFromHurtList+sum(defenceVal)
  print()
  print('> you lost '+str(randChoiceFromHurtList)+' health!')
  print()
  twoSecond()
def menu():
  if (secretMenu == 1):
    print()
    print(
      '(=========================================================================)'
    )
    print()
    print()
    print(
      '(=========================================================================)'
    )
    print()
    print()
    twoSecond()
    print('you may:')
    oneSecond()
    print()
    print('  1. Travel the trail')
    oneSecond()
    print('  2. Learn about the trail')
    oneSecond()
    print('  3. See the Oregon top ten')
    oneSecond()
    print('  4. Turn sound off')
    oneSecond()
    print('  5. Choose management options')
    oneSecond()
    print('  6. End')
    print()
    twoSecond()
    print('What is your choice? _ ')
    print()
    print()
    fiveSecond()
    print('just kidding.')
    twoSecond()
    clearCons()
    print()
    print()
    print()
    oneSecond()
    print()
    print('By: Mr Paul')
    oneSecond()
  else:
    print()
    print()
    print()
    oneSecond()
    print('By: Mr Paul!')
    print()
    oneSecond()


def ifDead():
  if (health <= 0):
    print()
    print('> You died!')
    exit()

# when you start the program
def start():
  print()
  print('> Its a nice day in summer and you live a quiet life on a farm.')
  print()
  oneSecond()
  print('> You wake up and eat breakfast.')
  print()
  oneSecond()
  print('> You have a home altar.')
  oneSecond()
  print()
  print('> Do yo want to pray at the altar?')
  print()
  prayAtAltar = input('> [ yes or no ] : ')
  if (prayAtAltar == 'yes'):
    oneSecond()
    print()
    print('> You prayed at the altar and feel safer...')
    print()
    threeSecond()
  else:
    oneSecond()
    print()
    print('> You did not pray at the altar.')
    print()
    threeSecond()
  print('> You go outside.')
  oneSecond()





def ifInt():
  print('> *phone rings*')
  oneSecond()
  print()
  oneSecond()
  if (randPhoneNum == 'cat'):
    print('> The phone answers.')
    print()
    oneSecond()
    catLitter = random.choice(range(1, 10))
    for dpsa in range(catLitter):
      print('meow')
      print()
      oneSecond()
    print('> You hear banging on your door.')
    twoSecond()
    print()
    openCatDoor = input('> [ do you open it? ] : ')
    print()
    if (openCatDoor == 'yes'):
      print('> You open it.')
      print()
      oneSecond()
      print(
        '> Its a cat standing up on its two paws wearing a black trenchcoat!')
      print()
      twoSecond()
      print('> It pulls out a sawed off shotgun and blasts your head off.')
      print()
      twoSecond()
      print('> You died!')
      print()
      exit()
    elif (openCatDoor == 'no'):
      print('> You stay quiet and dont open the door')
    else:
      threeSecond()
      print('> BANG!')
      print()
      print('> The loud sound of a shot gun goes off!')
      print()
      twoSecond()
      print('')
  elif (randPhoneNum == 'police'):
    print('> The police come and arrest you.')
    print()
    oneSecond()
    print('> The say you are arrested for pooping on a kids birthday cake.')
    print()
    oneSecond()
    print('> You are escorted to the courthouse.')
    print()
    oneSecond()
    print('> You see the parents of the kid')
    print()
    oneSecond()
    finger = input(
      '> [ do you want to give the parrents the middle finger? ] : ')
    if (finger == 'yes'):
      oneSecond()
      print()
      print('> You wave the middle finger at the parrents!')
      print()
      twoSecond()
      print('> You feel no remorse.')
      print()
      oneSecond()
      print('> They are distraught.')
      print()
      print('> (+999999 happiness!)')
      print()
    elif (finger == 'no'):
      print()
      print("> [ Are you sure? ] : ")
      print()
      twoSecond()
      print(
        '> You start having an epileptic attack because you didnt flip them off.'
      )
      print()
      oneSecond()
      print('> Shame on you...')
      twoSecond()
      print('> You died!')
      exit()
    print('> The judge sentances you to death by firing squad!')
    twoSecond()
    print()
    print('> The juries and witnesses rip their civilian clothing off')
    print('  and pull out fully automatic rifles.')
    print()
    twoSecond()
    print('> FIRE!, the judge exclaims as he bangs the gavel.')
    print()
    oneSecond()
    print('> You died!')
    exit()
  elif (randPhoneNum == 'satan'):
    print('> The line picks up')
    print()
    print('> You feel a chill down your spine...')
    oneSecond()
    print()
    print('> The line picks up')
    print()
    print(
      '̴̩̄͑̌͘> { satan } :  b̵̰͓̩̹̺̌͛́̈̉͊̎o̴̜͉̬̗̱̱̻̞͆ñ̴̥͍̜̬͈̫̫͖͙̠̈͋͗̆͠j̷̒͊̈́̀̓̒̐̚̕͜͝͠ọ̷̘̦̥̻̺͍̩̯́̓̀ů̶̞̘̰̱̏̇̌̒̄͜͠͝r̵̛̳͎̩̭̭̹͙͙̦̻̾̃̐͒͛̿̾̌̏̂͐͜͜?'
    )
    print()
    print(
      '̷͚̂͗> { satan } : C̵̻̻̘̦̍̿̓͌͋͜ọ̵̢̆̄͒m̴̰̱̫̰͋͊̈m̴̭͉̐͊̒͛e̷̠̔n̷̢̡̬͎͐̍t̷̗̃́̔͝ ̶̢̗͈̣͑͆ç̶̟̺͈͚̓̋a̵͙͂́ ̴̭̭͕̖̉v̵̖͙̝͚̻̉̌ȁ̶͙͈͙̬̗̔̽̎͝?̴̤̠̩̎'
    )
    print()
    oneSecond()
    print()
    print('> A skelleton hand from the ground grabs you and pulls you down.')
    print()
    oneSecond()
    print('> You are dragged to the depths of hell and satan greets you.')
    print()
    twoSecond()
    print('> He speaks french...')
    print()
    dealWithTheDevil = input('̴̯̐> [ sell your soul?̶̝͂ ] : ')
    if (dealWithTheDevil == 'yes'):
      print()
      oneSecond()
      print('> merci baucoup')
      print()
      print('> satan says thank you in french.')
      print()
      twoSecond()
      print('> Your body rips into halves.')
      print()
      oneSecond()
      print('> You died! ')
      devilo = random.choice(range(1, 15))
      for prsdt in range(devilo):
        print('hail satan')
        print()
        oneSecond()
      print()
      exit()
    elif (dealWithTheDevil == 'no'):
      global st
      st = True
      fiveSecond()
      print()
      print('> { satan } : well fuck.')
      print()
      threeSecond()
      print('> satan spares you somehow?')
      threeSecond()
      clearCons()
      menu()
      start()
      inFrontOfHouse(health)
    elif (dealWithTheDevil.isdigit() == True):
      print()
      print('> You try to call someone but no one answers.')
      twoSecond()
      print()
      print('> Satan burns you alive.')
      print()
      threeSecond()
      print('> You died!')
      exit()


def badWordie(health):
  print()
  print('> Somebody hears you and calls the police!')
  print()
  oneSecond()
  print('> The police come and arrest youse and you get put in jail')
  print()
  oneSecond()
  print(
    '> You have been arrested for saying bad word!, said the police officer.')
  print()
  oneSecond()
  print('> You walk into the courthouse...')
  print()
  twoSecond()
  print('> The judge sentances you to the death penalty by firing sqaud!')
  print()
  oneSecond()
  print('> You are lined up at a firing range')
  print()
  fiveSecond()
  print('> FIRE! ')
  oneSecond()
  print()
  print('> *BANG* BANG *BANG')
  print()
  oneSecond()
  print('> You died!')
  print()
  twoSecond()
  exit()


def pondDecisionz():
  print('> What do you want to do at the pond?')
  print()
  pondDecision = input('> [ sit, fish, swim, go back ] : ')
  if (pondDecision == 'sit'):
    oneSecond()
    print()
    print('you are boring')
    print()
    twoSecond()
    print('you are not gonna sit.')
    print()
    oneSecond()
    print('please do somthing else.')
    print()
    oneSecond()
    pondDecisionz()
  elif (pondDecision == 'fish'):
    if ('fishing rod' in weapons):
      oneSecond()
      print()
      print('You fished at the pond and got nothing.')
      print()
      oneSecond()
      pondDecisionz()
    else:
      oneSecond()
      print()
      print('You dont have any fishing rods.')
      print()
      oneSecond()
      pondDecisionz()
  elif (pondDecision == 'swim'):
    oneSecond()
    print()
    print('you dive into the shallow pond')
    print()
    twoSecond()
    print('blub blub blub')
    print()
    print('you started drowning.')
    print()
    threeSecond()
    print('...')
    print()
    oneSecond()
    print('You died!')
    print()
    exit()
  elif (pondDecision == 'masterbate' or pondDecision == 'jack off'
        or pondDecision == 'fap'):
    threeSecond()
    print()
    print('God sees you and smites you with a thunderbolt.')
    print()
    oneSecond()
    print('You died!')
    exit()
  
  elif (pondDecision.isdigit() == True):
    ifInt()
  elif (pondDecision in goBack):
    print()
    print('> you went back to the house.')
    oneSecond()
    inFrontOfHouse(health)
  else:
    oneSecond()
    print()
    print('You just stood there.')
    pondDecisionz()


def fieldDecisionz():
  stardewValley = ['harvest wheat', 'wheat', 'havest', 'farm', 'farm wheat']
  runningUpTheHill = [
    'run', 'run through field', 'go through field', 'field', 'go to field',
    'field', 'play', 'play in field'
  ]
  print('> What do you want to do at the wheat field?')
  oneSecond()
  print()
  fieldDecision = input('> [ harvest wheat, run through field, go back ] : ')
  if (fieldDecision in stardewValley):
    if ('scythe' in equipment):
      oneSecond()
      print()
      if ('wheat' not in stuff):
        print('> you harvested the wheat with your scythe')
        stuff.append('wheat')
        print()
        fieldDecisionz()
      else:
        oneSecond()
        print()
        print('> you cannot harvest more wheat.')
        print()
        fieldDecisionz()
    else:
      oneSecond()
      print()
      print('> you dont have a scythe to harvest the wheat')
      print()
      oneSecond()
      fieldDecisionz()
  elif (fieldDecision in runningUpTheHill):
    oneSecond()
    print()
    print('> you ran into the field and played in it.')
    print()
    oneSecond()
    print('> but you have to be more prodcutive.')
    print()
    oneSecond()
    fieldDecisionz()
  elif (fieldDecision in badWord):
    badWordie(health)
  elif (fieldDecision.isdigit() == True):
    ifInt()
  elif (fieldDecision in goBack):
    oneSecond()
    inFrontOfHouse(health)
  else:
    oneSecond()
    print('> you watched the wind blow over the wheat field')
    print()
    oneSecond()
    print('> but you have to more productive.')
    print()
    fieldDecisionz()


def petChoize():
  global petD
  print()
  print('> what pet do you want to choose?')
  print()
  oneSecond()
  petDecision = input('> [ cat, bird, dog ] : ')
  if (petDecision == 'cat'):
    pets.append('cat')
    petD = petDamage.pop(0)   
    petH = petHealth.pop(0)
    oneSecond()
    print()
    print('> you picked the cat!')
    print()
    oneSecond()
    print('> it has : '+str(petD)+' ATK and '+str(petH)+' HEALTH !')
    print()
    oneSecond()
    print('> good choice. meow.')
    print()
    twoSecond()
    barnDecisionz()
  elif (petDecision == 'bird'):
    pets.append('bird')
    petD = petDamage.pop(1)
    petH = petHealth.pop(1)
    oneSecond()
    print()
    print('> you picked the bird!')
    print()
    oneSecond()
    print('> the bird has : '+str(petD)+' ATK and '+str(petH)+' HEALTH ! ')
    print()
    twoSecond()
    print('> chirp chrip chirp chirp.')
    print()
    twoSecond()
    barnDecisionz()
  elif (petDecision == 'dog'):
    pets.append('dog')
    petD = petDamage.pop(2)
    petH = petHealth.pop(2)
    oneSecond()
    print()
    print('> you picked the dog!')
    print()
    oneSecond()
    print('> bark : '+str(petD)+' ATK bark bark woof '+str(petH)+' HEALTH woof woof.')
    threeSecond()
    print()
    barnDecisionz()
  else:
    oneSecond()
    print()
    print('> thats not a pet')
    print()
    petChoize()


def getToolie():
  global yourAtk
  print()
  print('> what tool do you want to get? (you can only get one.)')
  print()
  oneSecond()
  toolDecision = input(
    '> [ chainsaw, fishing rod, sledgehammer, pitchfork, scythe ] : ')
  if (toolDecision == 'chainsaw'):
    weapons.append('chainsaw')
    damageW.append(35)
    yourAtk = yourAtk + damageW[0]
    print()
    oneSecond()
    print('> you choose the chainsaw!')
    print()
    oneSecond()
    barnDecisionz()
  elif (toolDecision == 'fishing rod'):
    weapons.append('fishing rod')
    damageW.append(1)
    yourAtk = yourAtk + damageW[0]
    print()
    oneSecond()
    print('> you grabbed the fishing rod!')
    print()
    oneSecond()
    barnDecisionz()
  elif (toolDecision == 'sledgehammer'):
    weapons.append('sledghammer')
    damageW.append(40)
    yourAtk = yourAtk + damageW[0]
    print()
    oneSecond()
    print('> you grabbed the sledgehammer and feel powerful')
    print()
    oneSecond()
    barnDecisionz()
  elif (toolDecision == 'pitchfork'):
    weapons.append('pitchfork')
    damageW.append(10)
    yourAtk = yourAtk + damageW[0]
    print()
    oneSecond()
    print('> you gained the pitchfork!')
    print()
    oneSecond()
    barnDecisionz()
  elif (toolDecision == 'scythe'):
    weapons.append('scythe')
    damageW.append(23)
    yourAtk = yourAtk + damageW[0]
    print()
    oneSecond()
    print('> you acquired the scythe!')
    print()
    oneSecond()
    barnDecisionz()
  else:
    oneSecond()
    print()
    print('> just pick one.')
    oneSecond()
    getToolie()


def barnDecisionz():
  petChoicez = ['pick a pet', 'pet', 'pick pet', 'choose a pet', 'choose pet']
  feedAnimalz = [
    'feed the animals',
    'feed',
    'animals',
    'feed animals',
    'feed animal',
    'feed them',
  ]
  getToolz = ['get a tool', 'get tool', 'grab tool', 'choose tool']
  print('> what do you want to do at the barn?')
  print()
  oneSecond()
  barnDecision = input(
    '> [ pick a pet, feed the animals, get a tool, go back ] : ')
  oneSecond()
  if (barnDecision in petChoicez):
    if (len(pets) == 0):
      petChoize()
    else:
      oneSecond()
      print()
      print('> sadly, you cant have multiple pets :((((')
      print()
      oneSecond()
      barnDecisionz()
  elif (barnDecision in feedAnimalz):
    print()
    print('> you feed the animals.')
    print()
    oneSecond()
    barnDecisionz()
  elif (barnDecision in getToolz):
    if (len(weapons) == 0):
      getToolie()
    else:
      oneSecond()
      print()
      print('> you already have a weapon')
      print()
      oneSecond()
      barnDecisionz()
  elif (barnDecision in goBack):
    oneSecond()
    print()
    print('> you skip happily back to the house')
    print()
    oneSecond()
    inFrontOfHouse(health)
  else:
    print()
    print('> i dont have a clue what to do')
    print()
    oneSecond()
    barnDecisionz()


def oneSecond():
  time.sleep(1)


def threeSecond():
  time.sleep(3)


def twoSecond():
  time.sleep(2)


def fourSecond():
  time.sleep(4)


def fiveSecond():
  time.sleep(5)


def inFrontOfHouse(health):
  print()
  frontHouze = input(
    '> where do you want to go? [ pond , wheat field, barn, village ] : ')
  print()
  if (frontHouze == 'pond'):
    oneSecond()
    print('> You went to the pond.')
    print()
    pondDecisionz()
  elif (frontHouze == 'wheat farm' or frontHouze == 'field'
        or frontHouze == 'wheat field'):
    oneSecond()
    print('> you went to the wheat farm')
    print()
    fieldDecisionz()
  elif (frontHouze == 'barn'):
    oneSecond()
    print('> you walked to the barn')
    print()
    oneSecond()
    barnDecisionz()
  elif (frontHouze == 'village'):
    oneSecond()
    print('> you went to the nearby village.')
    print()
    oneSecond()
    print()
    print()
    print()
    villageDecisionz()
  
  elif (frontHouze.isdigit() == True):
    ifInt()
  elif (frontHouze in goBack):
    oneSecond()
    print('> please do something exciting')
    print()
    oneSecond()
    print('> please')
    inFrontOfHouse(health)
  else:
    print('> idk what you want me to do.')
    inFrontOfHouse(health)


def villageDecisionz():
  oneSecond()
  print()
  print('> what do you want to do in the village?')
  print()
  oneSecond()
  villageDecision = input(
    '> [ farmers market, bar, blacksmith, northern forest ] : ')
  if (villageDecision == 'farmers market'):
    oneSecond()
    print()
    print()
    print('> you walk towards the farmers market')
    print()
    farma()
  elif (villageDecision == 'bar'):
    oneSecond()
    print()
    print()
    print('> you walked into the bar')
    print()
    bart()
  elif (villageDecision == 'blacksmith'):
    oneSecond()
    print()
    print()
    print('> you travel towards the blacksmith.')
    print()
    oneSecond()
    print('> the blacksmith place is closed.')
    print()
    oneSecond()
    villageDecisionz()
  
  elif (villageDecision.isdigit() == True):
    ifInt()
  elif (villageDecision == 'north' or villageDecision == 'northern forest'):
    oneSecond()
    print()
    print()
    print()
    oneSecond()
    print('> Are you sure? [ you cant go back ] ')
    print()
    areYouseSures = input('> [ yes or no ] : ')
    print()
    oneSecond()
    if (areYouseSures == 'yes'):
      print()
      print('> you walk into the forest')
    else:
      print('> you rethink')
      oneSecond()
      villageDecisionz()
  elif (villageDecision in goBack):
    oneSecond()
    print()
    print()
    print('> you go back to your home')
    print()
    oneSecond()
    inFrontOfHouse(health)
  else:
    oneSecond()
    print()
    print()
    print('> if you dont know what to do ask the locals.')
    print()
    villageDecisionz()


def firstEncounter(health):
  twoSecond()
  clearCons()
  oneSecond()
  print()
  print('> { ??? } oh !')
  print()
  oneSecond()
  print('> { ??? } : what are you in the northern forest?')
  print()
  oneSecond()
  print('> choose one')
  print()
  forest1 = input('> [ trying to defeat the dragon, i just got lost ] : ')
  if (forest1 == 'i just got lost'):
    print()
    oneSecond()
    print('> you say that you got lost.')
    print()
    oneSecond()
    print('> { ??? } : oh, ok.')
    print()
    oneSecond()
    print('> Judas still joins your team!!!')
    print()
    oneSecond()
  else:
    print()
    oneSecond()
    print('> you say that you are trying to defeat the dragon')
    print()
    oneSecond()
    print('> { ??? } : me too! lets defeat the dragon together!')
    print()
    oneSecond()
    print('> you agree.')
    print()
    oneSecond()
    print('> [ someone has joined your team! ] yay!!!! ')
  friends.append('judas')
  print()
  print('> { Judas } : oh yeah my name is judas what is yours?')
  print()
  oneSecond()
  if (hasName == True):
    oneSecond()
    print('> you say that you name is '+yourName)
    print()
    twoSecond()
    print('> { Judas } : oh ok! '+yourName)
  else:
    print('> you say that you dont have a name.')
    print()
    oneSecond()
    print('> { Judas } : oh ok!')
    print()
    oneSecond()
    print()
    twoSecond()
    clearCons()
    oneSecond()
    print()
    print()
    print()
    print('> this is your health and other stuff')
    print()
    


def bart():
  bartenderLines = [
    'what do you want?', 'are you looking for a drink?',
    'what is the meaning of life?', 'god i need to poop very badly'
  ]
  randomBartenderLine = random.choice(bartenderLines)
  oneSecond()
  print('> { bartender } : ' + randomBartenderLine)
  print()
  oneSecond()
  print('> ask the bartender something. or go back.')
  print()
  oneSecond()
  askBart = input(
    '> [ get a drink, ask about life, how to beat the video game ] : ')
  if (askBart == 'get a drink'):
    oneSecond()
    print()
    print('> you order a drink')
    print()
    oneSecond()
    print('> *glug* *glug* *glug*')
    print()
    print('burp')
    print()
    oneSecond()
    print()
    bart()
  elif (askBart == 'ask about life'):
    oneSecond()
    print()
    print('> { bartender } : how did we get here? ?')
    print()
    oneSecond()
    bart()
  elif (askBart == 'how to beat the video game'):
    oneSecond()
    print()
    print('> { bartender } : i dont know what your saying you must be crazy!')
    print()
    oneSecond()
    bart()
  elif (askBart.isdigit() == True):
    ifInt()
  elif (askBart in badWord):
    badWordie(health)
  elif (askBart in goBack):
    oneSecond()
    print()
    print('> you walk out of the bar')
    print()
    oneSecond()
    villageDecisionz()
  else:
    oneSecond()
    print()
    print('> you stare at the bartender for 44 seconds.')
    print()
    oneSecond()
    print('> you win the staring contest!!!')
    print()
    oneSecond()
    bart()


def farma():
  oneSecond()
  print('> ask the farmer something. or go back.')
  print()
  oneSecond()
  askFarmer = input(
    '> [ buy an apple, how to beat the video game, do you know my name, go back ] : '
  )
  if (askFarmer == 'buy an apple'):
    oneSecond()
    print()
    print('> you ask to buy an apple')
    print()
    oneSecond()
    print('> { farmer } : dont buy them')
    print()
    oneSecond()
    print('> { famer } : just trust me.')
    print()
    oneSecond()
    print()
    oneSecond()
    farma()
  elif (askFarmer == 'how to beat the video game'):
    oneSecond()
    print()
    print('> you ask how to beat the game')
    print()
    oneSecond()
    print('> { farmer } : you will have to defeat the dragon to win the game!')
    print()
    oneSecond()
    print('> you ask how to get to the dragon')
    print()
    oneSecond()
    print(
      '> { farmer } : you will have to climb the holy tower and fight it at the tower peak.'
    )
    print()
    oneSecond()
    print(
      '> { farmer } : the holy tower is north of this village and you will need good equipment to defeat the dragon.'
    )
    print()
    oneSecond()
    print('> { farmer } : good luck.')
    print()
    farma()
  elif (askFarmer == 'do you know my name'):
    global yourName
    global hasName
    hasName = True
    oneSecond()
    print()
    print('> { farmer } : no i dont')
    print()
    oneSecond()
    print('> { farmer } : just pick your name.')
    print()
    oneSecond()
    print('> please pick your name')
    print()
    oneSecond()
    yourName = input('[ your name! ] : ')
    if (yourName == 'satan'):
      print()
      print()
      oneSecond()
      clearCons()
      for iopeqw in range(20):
        print()
        oneSecond()
        print(
          '> ḧ̴̢̲͍́̈́͜͠ë̸̡̲̮͒̊͌̎̃͂͜ļ̶̘̯̲̝̦̬̋̌́̿̕͝ŏ̷̡̺̽h̷̛̦̫́e̶͓͊l̷̜̺͉̲̀͊͆̏͝͝ǫ̵̩̪̍̊̃h̴̺̟̻͚̆̑͘͝ë̸̹ļ̷̹͎̘̪̄̾͒̊͝ò̶͈̜̳̻̜͕̇̽̃̅ḧ̷̳̺͖̹́̈̉͒́̔͘͜ë̴̢͍̪l̸̟̫̀͗̏̇͆̑o̷̧͎̖̺̻̯̱͐̎̋̓͘͝h̸̼͙̯̜͎̃̓̃̿͝ẽ̵̬͔̙͍̊̓͂̈́͝͝l̴̠͙͙̪̓̾̀̎̕͜ơ̵̮͑͒̈̈̽'
        )
        oneSecond()
        exit()
    elif (yourName == 'name' or yourName == 'farmer'):
      print()
      print(
        '> ( WARNING ) : every monster will instantly kill you if name yourself this.'
      )
      print()
      oneSecond()
      print(
        '> Are you sure? ( talk to the people in the village before doing this ) '
      )
      print()
      oneSecond()
      choiceNam = input('> [ yes or no ] : ')
      if (choiceNam == 'yes'):
        global mHealth
        global mDamage
        oneSecond()
        mDamage = mDamage+999999999
        print()
        print('ok')
        print()
        farma()
      else:
        oneSecond()
        print()
        print('ok choose another namer')
        print()
        farma()
    elif (yourName == 'paul'or yourName =='Paul'):
      print()
      print('> hehehe')
      print()
      oneSecond()
      farma()
    else:
      print()
      print('> { farmer } : alright ' + yourName + '!')
      print()
      oneSecond()
      farma()
  elif (askFarmer in goBack):
    oneSecond()
    print()
    print('> you walk back to the village center.')
    print()
    oneSecond()
    villageDecisionz()
  else:
    print('??????')
    print()
    farma()

def stats():
  global health
  global yourAtk
  fiveFLine = 42 - len(str(yourAtk)) - len(str(health))
  if (hasName == True):
    nameSlot = 59 - len(yourName)
    firstFLine = 62 - nameSlot
    twoFLine = firstFLine - len(yourName) - 2
    print('0' + firstFLine * '=' + '0')
    print('| ' + yourName + ':' + twoFLine * ' ' + '|' + firstFLine * ' ')
  else:
    print('0================0')
    print('|  protagonist:  |')
  print('0=============================================================0')
  if (len(pets) == 0):
    print('|  atk   |   health   |  pet : none                           |')
  else:
    print('|  atk   |   health   |  pet : ' + pets[0] +
          '                           |')
  print('|   ' + str(yourAtk) + '    |     ' + str(health) + '     |' +
        fiveFLine * ' ' + '|')
  print('0=============================================================0')
  print()


def firstEncounter2():
  oneSecond()
  print('> it also shows your atk and total health')
  print()
  oneSecond()
  print('> type stats during combat to show stats')
  print()
  oneSecond()
  print('> { Judas } : i conveniently have a compass ')
  print()
  oneSecond()
  print('> you move north ')
  print()


def twoPathz():
  oneSecond()
  print('> there are two paths both leading north')
  print()
  oneSecond()
  leftOrRight = input('> [ left or right ] : ')
  if (leftOrRight == 'left'):
    oneSecond()
    print()
    print('> you went left')
    print()
    oneSecond()
    if ('machine gun' not in weapons):
      global yourAtk
      if (len(weapons) == 0):
        weapons.append('machine gun')
        damageW.append(9999)
        yourAtk = yourAtk + damageW[0]
        print('> the left path leads to a dead end')
        print()
        oneSecond()
        print('> there seems to be a random chest at the end of the path')
        print()
        oneSecond()
        print('> you open it to find a machine gun ! ')
        print()
        oneSecond()
        print('whoever coded this must be dumb')
        print()
        oneSecond()
        print('> this will be useful for defeating the dragon.')
        print()
        print('> you go back.')
        print()
        oneSecond()
        twoPathz()
      else:
        oneSecond()
        print('> you already have a weapon !!')
        print()
        oneSecond()
        print()
        print('> you went right')
        print()
        oneSecond()
        print('> you come across a waterfall pouring into a winding river.')
        print()
        oneSecond()
        print('> you kept on going forward across the path')
        print()
        oneSecond()

    else:
      print(
        '> you go back hoping for the loot to respawn but it doesnt. :((((')
      print()
      oneSecond()
      twoPathz()
  elif (leftOrRight == 'right'):
    oneSecond()
    print()
    print('> you went right')
    print()
    oneSecond()
    print('> you come across a waterfall pouring into a winding river.')
    print()
    oneSecond()
    print('> you kept on going forward across the path')
    print()
    oneSecond()
  else:
    oneSecond()
    print()
    print('> you scream from the  top of your lungs')
    print()
    oneSecond()
    print('> but nobody hears you.')
    print()
    twoPathz()


def clearCons():
  os.system('clear')
  
encountersCounter = 0

def encounter():
  global health
  global yourAtk
  global encountersCounter
  encountersCounter = encountersCounter+1
  anEnemyApears = ['a monster comes out of a bush!','a monster falls out of a tree!','a monster burrows up from underneth!','a monster apears out of thin air','a monster jumps out of the lake!','a monster bellyflops into existence!',' a ufo crashes and a monster comes out of the ufo!','a monster comes out of its cocoon!','a monster wants to have an arm wrestling match with you!']
  rAnEnemyApears = random.choice(anEnemyApears)
  stats()
  twoSecond()
  print()
  print('> (' +rAnEnemyApears+' ) ')
  print()
  oneSecond()
  print('> ATK : ' + str(mDamage) + ' HEALTH : ' + str(mHealth))
  print()
  oneSecond()
  battle()


def battle():
  global health
  global yourAtk
  global mHealth
  global mDamage
  global defenceVal
  print('> what will you do ? ')
  print()
  oneSecond()
  battleChoice = input('> [ atk, block, flee ] : ')
  if (battleChoice == 'atk'):
    oneSecond()
    print()
    if (weapons in swingAbles):
      print('> you swing at the monster!')
      print()
      oneSecond()
    elif ('machine gun' in weapons):
      rBulet = random.randint(50,1000)
      print('> you shot '+str(rBulet)+' bullets through the monsters chest.')
      print()
      oneSecond()
    else:
      print('> you hit the monster.')
      print()
      oneSecond()
    print()
    oneSecond()
    mHealth = mHealth - yourAtk
    if(len(pets)!=0):
      mHealth = mHealth - petD
      listATK = [' pulls out a glock and starts shooting!',' detonates a nuke and destroys the monter!',' pulls out a HIV infected syringe stabs the monster!',' calls the batmobile and runs over the monster!',' calls in the Death Star and annihilates the monster!',' calls in a fighter jet to carpet bomb',' summons a portal to hell and releases demons',' pulls out a fucking flamethrower and burns the monster alive!']
      rListOfPetATK = random.choice(listATK)
      print('> and your pet '+pets[0]+rListOfPetATK)
      print()
      twoSecond()
      print('> the '+pets[0]+' did '+str(petD)+' damage! ')
      print()
      oneSecond()
    else:
      print('> it did ' + str(yourAtk) + ' damage!')
      print()
      twoSecond()
    if (mHealth <= 0):
      mHealth = 25
      mHealth = mHealth+random.randint(1,5)*encountersCounter
      mDamage = mDamage+random.randint(1,5)*encountersCounter
      randHeal = random.randint(1,5)
      randDamage = random.randint(3,8)
      health = health+randHeal
      yourAtk = yourAtk+randDamage
      print('> you have slain the beast! ')
      print()
      oneSecond()
      print('> you healed '+str(randHeal)+' and gained '+str(randDamage)+' ATK !')
      print()
      twoSecond()
      print('> yay!')
      print()
      oneSecond()
      print('> but the monsters get stronger.')
      print()
      twoSecond()
    else:
      print('> the monster is still alive.')
      print()
      oneSecond()
      print('> ATK : ' + str(mDamage) + ' HEALTH : ' + str(mHealth))
      oneSecond()
      print()
      print('> it hits u back!')
      print()
      oneSecond()
      print('ouch!')
      defence()
      ifDead()
      battle()
  elif (battleChoice == 'block'or battleChoice=='meatshield'):
    twoSecond()
    print()
    print('> you crossed your arms together.')
    print()
    oneSecond()
    print('> you blocked all incoming damage!')
    print()
    oneSecond()
    battle()
  elif (battleChoice == 'flee'):
    mHealth = mHealth+5
    mDamage = mDamage+5
    print()
    print('> you flee but the monsters get stronger.')
    print()
    oneSecond()
    print('> coward')
    print()
    oneSecond()
  else:
    print('> you say PAUSE and you need to take a pee break.')
    print()
    twoSecond()
    battle()
def defence():
  global defenceVal
  global health
  global mDamage
  trueDefence = sum(defenceVal)
  if(trueDefence>=mDamage):
    twoSecond()
    print()
    print('> your armour has blocked all the damage!')
    print()
  else:
    health = health - mDamage + trueDefence
def fakeDeath():
  oneSecond()
  print()
  oneSecond()
  print()
  print('> You died!')
  oneSecond()
  print()
  print(Fore.RED + 'repl process died unexpectedly:')
  print()
  fourSecond()
def moveForward():
  oneSecond()
  print()
  print('> you move forward along the dirt path')
  print()
  oneSecond()
def caveOrMountain():
  oneSecond()
  clearCons()
  print()
  print('> you walk across the dirt road')
  print()
  threeSecond()
  print('> the path goes two different ways :')
  print()
  twoSecond()
  print('> there is a montain path and a promising cave entrance.')
  print()
  twoSecond()
  print('> both ways lead north.')
  print()
  twoSecond()
  cavesAndCliffs = input('> [ mountain , cave ] : ')
  if(cavesAndCliffs=='mountain'):
    oneSecond()
    mountain()
  elif(cavesAndCliffs=='cave'):
    oneSecond()
    cave()
def cave():
  oneSecond()
  print()
  print('> you walk into the cave.')
  print()
  oneSecond()
  print('> there is rays of light through holes from above ')
  print()
  twoSecond()
  print('> that light up the cave.')
  print()
  twoSecond()
  print('> but then suddenly')
  print()
  oneSecond()
  print(' HELP! HELP! ')
  print()
  oneSecond()
  print('> someone is getting jumped by a monster worm !')
  print()
  bossWorm()
def bossWorm():
  global health
  global yourAtk
  global mHealth
  global mDamage
  global defenceVal
  wormD = 10+mDamage
  wormH = 20+mHealth
  oneSecond()
  print('> ( you and judas both attack the worm creature! ) ')
  print()
  oneSecond()
  stats()
  twoSecond()
  print()
  print('> its a giant worm! ')
  print()
  oneSecond()
  print('> their ATK is : ' +str(wormD)  + ' and HEALTH is : ' + str(wormH))
  print()
  oneSecond()
  print('> what will you do ? ')
  print()
  oneSecond()
  battleChoice = input('> [ atk, block, flee ] : ')
  if (battleChoice == 'atk'):
    oneSecond()
    print()
    if (weapons in swingAbles):
      print('> you swing at the worm!')
      print()
      oneSecond()
    elif ('machine gun' in weapons):
      rBulet = random.randint(50,1000)
      print('> you shot '+str(rBulet)+' bullets but 90% missed because its a worm.')
      print()
      oneSecond()
    else:
      print('> you hit the monster.')
      print()
      oneSecond()
    print()
    oneSecond()
    wormH = wormH - yourAtk
    if(len(pets)!=0):
      wormH = wormH - petD
      listATK = [' pulls out a glock and starts shooting!',' detonates a nuke and destroys the monter!',' pulls out a HIV infected syringe stabs the monster!',' calls the batmobile and runs over the monster!',' calls in the Death Star and annihilates the monster!',' calls in a fighter jet to carpet bomb',' summons a portal to hell and releases demons',' pulls out a flamethrower and burns the monster alive!']
      rListOfPetATK = random.choice(listATK)
      print('> and your pet '+pets[0]+rListOfPetATK)
      print()
      twoSecond()
      print('> the '+pets[0]+' did '+str(petD)+' damage! ')
      print()
      oneSecond()
    else:
      print('> it did ' + str(yourAtk) + ' damage!')
      print()
      twoSecond()
    if (mHealth <= 0):
      mHealth = 25
      mHealth = mHealth+random.randint(1,5)*encountersCounter
      mDamage = mDamage+random.randint(1,5)*encountersCounter
      randHeal = random.randint(1,5)
      randDamage = random.randint(3,8)
      health = health+randHeal
      print('> the worm bleeds white liquid and dies! ')
      print()
      oneSecond()
      print('> you healed '+str(randHeal)+' and gained '+str(randDamage)+' ATK!')
      print()
      twoSecond()
      print('> yay!')
      print()
      oneSecond()
      print('> { ??? } : bro i thought that i was dead !.')
      print()
      oneSecond()
      print('> { ??? } : thank youse for saving me !')
      print()
      oneSecond()
      print('> { ??? } : im guessing that youse also wanting to defeat the dragon!')
      print()
      noName = listOfGirlNames.pop(random.randrange(len(listOfGirlNames)))
      friends.append(noName)
      print('> { ??? } ill join you!')
      print()
      twoSecond()
      print('> { '+noName+' } : also my name is '+noName)
      print()
      oneSecond()
      print('> '+noName+' has joined your party!')
      print()
      twoSecond()
      print('> you walked and walked north to find an exit. ')
      print()
      
      oneSecond()
      cave2()
    else:
      print('> the worm still flops around.')
      print()
      oneSecond()
      print('> ATK : ' + str(wormD) + ' HEALTH : ' + str(wormH))
      oneSecond()
      print()
      print('> it hits u back!')
      print()
      oneSecond()
      print('ouch!')
      health = health-wormD+sum(defenceVal)
      ifDead()
      bossWorm()
  elif (battleChoice == 'block'or battleChoice=='meatshield'):
    twoSecond()
    print()
    print('> you crossed your arms together.')
    print()
    oneSecond()
    print('> but the worm tickles you!')
    print()
    oneSecond()
    print('> and it slaps judas !')
    print()
    oneSecond()
    print()
    oneSecond()
    encounter()
    oneSecond()
    print()
    print()
    bossWorm()
  elif (battleChoice == 'flee'):
    print('> you flee')
    print()
    oneSecond()
    print('> but the worm chokes you and slams you on the ground!')
    print()
    oneSecond()
    health = health-wormD+sum(defenceVal)
    print('> it did '+str(wormD)+' damage!')
    print()
    oneSecond()
    ifDead()
    bossWorm()
def cave2():
  twoSecond()
  clearCons()
  print()
  print()
  print()
  oneSecond()
  stats()
  oneSecond()
  print()
  print('> you keep walking ')
  print()
  oneSecond()
  print('> you see a light at the end of the tunnel!')
  print()
  oneSecond()
  print('> AAAAHHH')
  print()
  oneSecond()
  print('> the bright light dazes you.')
  print()
  oneSecond()
  print('> you walk out of the cave!')
  print()
  oneSecond()
  print('> and onto a dirt path that leads to the tower')
  print()
  oneSecond()
  
def mountain():
  oneSecond()
  print()
  print('> you walk up the mountain path')
  print()
  oneSecond()
  encounter()
  oneSecond()
  print('> you kept on moving')
  print()
  oneSecond()
  encounter()
  oneSecond()
  print()
  print('> you kept on moving')
  print()
  oneSecond() 
  encounter()
  print()
  print('> god there are so many monsters')  
  print()
  oneSecond() 
  encounter()
  oneSecond()
  print()
  print('> stop')
  print()
  oneSecond()
  encounter()
  oneSecond()
  print()
  print('> { mountain goat } : hi im the mountain goat and i need to ask you a question because your in an adventure game!')
  print()
  oneSecond()
  print('> { mountain goat } : ok, at which hospital did the first heart transplant take place?')
  mountGoat = input('> [ Cleveland Clinic , Mayo Clinic , Groote Schuur Hospital ] : ')
  if(mountGoat!='Groote Schuur Hospital'):
    oneSecond()
    print()
    print('> { trivia goat } : WRONG')
    print()
    twoSecond()
    print('> the goat bites your head off')
    print()
    twoSecond()
    print('> You died!')
    print()
    oneSecond()
    exit()
  else:
    oneSecond()
    print()
    print('> { triva goat } : but its not over!')
    print()
    twoSecond()
    print('> { triva goat } : WHO invented walking??>?')
    print()
    twoSecond()
    paulWalker = input('> [ Paul Walker , Luke Skywalker , Usain Bolt , ')
    if(paulWalker!='Paul Walker'):
      oneSecond()
      print()
      print("> It's been a long day without you, my friend")
      print()
      oneSecond()
      print('> And Ill tell you all about it when I see you again')
      print()
      oneSecond()
      print('> We come a long way from where we began')
      print()
      oneSecond()
      print('> Oh, Ill tell you all about it when I see you again')
      print()
      oneSecond()
      print('> When I see you again')
      print()
      twoSecond()
      print('> You died!')
      print()
      fourSecond()
      exit()
    else:
      oneSecond()
      print()
      print('> { goat } : right!!!!11!1!')
      print()
      oneSecond()
      print('> { micel jordan } : one last question...')
      print()
      twoSecond()
      print('> { Paul Walker } : who invented the whip and nae nae ???/')
      print()
      oneSecond()
      whipNaeNae = input('> [ Solder Boy , Cardi B , Nicki Minaj , Rihanna ] :')
      if(whipNaeNae!='Solder Boy'):
        oneSecond()
        print()
        print('> Out in public, make a scene')
        print()
        oneSecond()
        print('> I dont cook, I dont clean')
        print()
        oneSecond()
        print('> But let me tell you, I got this ring.')
        print()
        oneSecond()
        print('> You died!')
        print()
        twoSecond()
        exit()
      else:
        oneSecond()
        print()
        print('> youse gots it rightSSss1!')
        print()
        oneSecond()
        print('> you are finally done with the questions.')
        print()
        oneSecond()
        print('> you walk down from the hill and onto a dirt path.')
        print()
        oneSecond()
        
def final1():
  clearCons()
  oneSecond()
  print()
  print('> you can see the tower from here!.')
  print()
  oneSecond()
  print('> you move across the dirt path')
  print()
  oneSecond()
  encounter()
  print('> you are getting closer')
  print()
  encounter()
  print()
  print("> you are getting closer")
  print()
  encounter()
  print()
  print("> you are getting closer")
  print()
  encounter()
  print()
  print("> you are getting closer")
  print()
  encounter()
  print()
  print("> you are getting closer")
  print()
  encounter()
  print()
  print("> you are getting closer")
  print()
  oneSecond()
  print('> ok you are here.')
  print()
  oneSecond()
  print('> you climb the tower without resistance')
  print()
  twoSecond()
  print('> you are at the top of the tower')
  print()
  oneSecond()
  print('> { dragon } : ')

def bossDragon():
  global health
  global yourAtk
  global mHealth
  global mDamage
  global defenceVal
  dragonD = 50+mDamage
  dragonH = 225+mHealth
  oneSecond()
  print('> ( you have been waiting for this moment! ) ')
  print()
  oneSecond()
  stats()
  twoSecond()
  print()
  print('> its a giant dragon! ')
  print()
  oneSecond()
  print('> their ATK is : ' +str(dragonD)  + ' and HEALTH is : ' + str(dragonH))
  print()
  oneSecond()
  print('> what will you do ? ')
  print()
  oneSecond()
  battleChoice = input('> [ atk, block, flee ] : ')
  if (battleChoice == 'atk'):
    oneSecond()
    print()
    if (weapons in swingAbles):
      print('> you swing at the worm!')
      print()
      oneSecond()
    elif ('machine gun' in weapons):
      rBulet = random.randint(50,1000)
      print('> you shot '+str(rBulet)+' bullets but 90% missed because its a worm.')
      print()
      oneSecond()
    else:
      print('> you hit the monster.')
      print()
      oneSecond()
    print()
    oneSecond()
    dragonH = dragonH - yourAtk
    if(len(pets)!=0):
      dragonH = dragonH - petD
      listATK = [' pulls out a glock and starts shooting!',' detonates a nuke and destroys the monter!',' pulls out a HIV infected syringe stabs the monster!',' calls the batmobile and runs over the monster!',' calls in the Death Star and annihilates the monster!',' calls in a fighter jet to carpet bomb',' summons a portal to hell and releases demons',' pulls out a fucking flamethrower and burns the monster alive!']
      rListOfPetATK = random.choice(listATK)
      print('> and your pet '+pets[0]+rListOfPetATK)
      print()
      twoSecond()
      print('> the '+pets[0]+' did '+str(petD)+' damage! ')
      print()
      oneSecond()
    else:
      print('> it did ' + str(yourAtk) + ' damage!')
      print()
      twoSecond()
    if (mHealth <= 0):
      mHealth = 25
      mHealth = mHealth+random.randint(1,5)*encountersCounter
      mDamage = mDamage+random.randint(1,5)*encountersCounter
      randHeal = random.randint(1,5)
      randDamage = random.randint(3,8)
      health = health+randHeal
      print('> the worm bleeds white liquid and dies! ')
      print()
      oneSecond()
      print('> you healed '+str(randHeal)+' and gained '+str(randDamage)+' ATK!')
      print()
      twoSecond()
      final2()
    else:
      print('> the dragon take exotic poses.')
      print()
      oneSecond()
      print('> ATK : ' + str(dragonD) + ' HEALTH : ' + str(dragonH))
      oneSecond()
      print()
      print('> le dragon belly flops on you!')
      print()
      oneSecond()
      print('ouch!')
      health = health-dragonD+sum(defenceVal)
      ifDead()
      bossDragon()
  elif (battleChoice == 'block'or battleChoice=='meatshield'):
    twoSecond()
    print()
    print('> you crossed your arms together.')
    print()
    oneSecond()
    print('> the dragon blows you so hard that you die!')
    print()
    oneSecond()
    print('> You died !')
    print()
    twoSecond()
    exit()
  elif (battleChoice == 'flee'):
    print('> you flee')
    print()
    oneSecond()
    print('> you fall off of the tower!')
    print()
    oneSecond()
    print('> you died!')
    threeSecond()
    exit()




hasName = False



menu()

start()

inFrontOfHouse(health)

firstEncounter(health)

stats()

firstEncounter2()

twoPathz()
# left or right
encounter()
moveForward()
encounter()
moveForward()
encounter()
caveOrMountain()
final1()
# decide to go to through the cave or montain

def final2():
  threeSecond()
  print()
  print('> the beast falls over limp')
  print()
  oneSecond()
  print('> what now?')
  print()
  oneSecond()
  print('you look around and god lets you into heaven for some reason....')
  print()
  threeSecond()
  print('wait...')
  threeSecond()
  print()
  print('<THE END>')



# randBsannsit 
