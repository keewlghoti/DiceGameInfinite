###DICE GAME but, like, infinite and stuff.
###Mike Bell
###Creating an infinite number of dice games

#import random for random number gen
import random


class Gamespace(object): #creation of the gamespace
    dice1 = None #initialize class attributes
    dice2 = None
    i = None

    def __init__(self): #Gamespace creator
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)
        self.i = 0 #keeping track of fails

    def rolldice (self): #takes the current gamespace dice attrivutes and randomizes
        self.dice1 = random.randint(1,6)
        self.dice2 = random.randint(1,6)

class Userinteraction(object): #I create Userinteraction classes because its a tad more organized in my 'runtime/main' method

    def intro(): #intro isnt taking an object because i just need this called procedurally
        print('Welcome to the DiCeGaMe.'); print('\n')
        print('Shit\'s easy dog, just fucking roll until they match'); print('\n')
        print('Just stop being bad.'); print('\n')
        print('How many games did you want to play?')
        while True:
            try: #try-except block to check for interger value. currently just ejects the program on fail
                userget = int(input('Don\'t be an idoit, enter an interger: '))
                if userget == 0:
                    print('Okay then, we won\'t play')  
                else:
                    return userget #funky little way to get this procedure to execute and return an interger value. its called later.
            except ValueError:
                print('Yeah, you\'re a fucking idoit... Interger.')
               

    def gamemenu(self): #handles rules and printing to the user
        print('GAME SCREEN')
        print('Dice 1 = ' + str(self.dice1))
        print('Dice 2 = ' + str(self.dice2))
        if self.dice1 == self.dice2:
            print('Wow look at a randnumgen playing in your favor. You only failed ' + str(self.i) + ' times. Loser')
            return False #a False causes the script to move to the next object
        else:
            self.i = self.i + 1
            print('You\'ve failed ' + str(self.i) + ' times. Idiot')
            self.rolldice()
            return True #returns True causes this program to continue running against the object

class Infinite(object): # create the inifinite object
    pass
    userget = 0 #making these static attributes
    newgameList = []

    def __init__(self):
        self.userget = Userinteraction.intro() #calls intro sequence, intro() returns an int
        self.newgameList = [] #creates list
        for self.userget in range (0, int(self.userget)): #fills list form
            self.newgameList.append(Gamespace()) #fills list



class Runtime:
    pass
    newgame = True
    while newgame == True:
        newgame = Infinite() #starts the Infinite class object

        m = 0 #list interator
        for fart in newgame.newgameList:
            j = m + 1 #print interator, list position + 1. (list starts at 0, we like to start reading at 1)
            print('\n' + '****** NEXT GAME ******' + '\n')
            print('This is game number: ' + str(j))
            while Userinteraction.gamemenu(newgame.newgameList[m]) == True: #runs the method, if false, moves to next one
                print('\n')
            m += 1 #moves to next position on list

        print('\n' + '-------Here are your results--------' + '\n')
        n = 0 #list iterator
        for toot in newgame.newgameList:
            o = n + 1 #print interator, list position + 1. (list starts at 0, we like to start reading at 1)
            print('Game: ' + str(o) + ' - It took ' + str(newgame.newgameList[n].i) + ' tries to match') #prints the final fail (Gamespace.i) value of each gamespace object
            n += 1

    def vomit(): #this method just shits out w.e i need it too.
        print('Runtime.newgame.__dict__')
        print(Runtime.newgame.__dict__) #currently will tell me values of all attributes in my main gamespace


if __name__ == '__main__':
    Runtime()
