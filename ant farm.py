#ant farm base code!
#written by Dr. Mo, Jan 22

colony=[] #list to hold all the ants

#parent class---------------------------------------
class ant:
    def __init__(self):
        self.age = 0
        self.food = 10
    def eat(self):
        self.food+=10
    def __del__(self): #destructor
        print("ant killed.")
    def update(self):
        self.food-=1
        self.age+=1
        

#child class--------------------------
class worker(ant):
    def __init__(self):
        self.name = "worker"
        ant.__init__(self)
    
    def printInfo(self):
        print("I am a worker and I am ", self.age, " days old. My food level is ", self.food)
#child class--------------------------
class larva(ant):
    def __init__(self):
        self.name = "larva"
        ant.__init__(self)
    def printInfo(self):
        print("I am a larva and I am ", self.age, " days old. My food level is ", self.food)
    #def metamorphasis():
        
#child class--------------------------
class queen(ant):
    def __init__(self):
        self.name = "queen"
        ant.__init__(self)
        
    def printInfo(self):
        print("I am a queen and I am ", self.age, " days old. My food level is ", self.food)
        
    def egg(self):
        print("queen has laid an egg!")
        BabyLarva = larva()
        colony.append(BabyLarva)
        
#start of "main"########################################
q1 = queen()
colony.append(q1)
w1 = worker()
colony.append(w1)
w2 = worker()
colony.append(w2)
l1 = larva()
colony.append(l1)

#game loop

doExit = False
while doExit == False:


#print info for each ant in colony
    i = 0
    while i != len(colony):
        colony[i].printInfo()
        colony[i].update()
        if colony[i].name == "queen":
            colony[i].egg()
        if colony[i].age >5:
            print("A ", colony[i].name, " has died.")
            del colony[i]
            i-=1

        i += 1    
    
    
    
    print("------------")

    userInput = input("press any key to continue, q to quit")
    if userInput == "q":
        doExit = True
