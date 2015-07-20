from Tkinter import *
import webbrowser
import time
import sys
import random
 
print('Welcome to the Life Simulator!')
time.sleep(1)
print("Today you'll be able to live the life of some nerds!")

class Simulator:
    YOU_CANT="You can't %s! You took too many pills!"

    def __init__(self):
        pass #idk

    def die(self, reason):
        print('You died! Reason: %s' % reason)
        time.sleep(3)
        sys.exit(1)

    def win(self):
        print('Congrats, you survived as a ginger!')
        time.sleep(3)
        sys.exit(1)

class chandlerSimulator(Simulator):
 
    MAX_PILLS = 3
 
    def __init__(self):
        Simulator.__init__(self)
        self.pillsTaken = 0
 
    def takePills(self):
        self.pillsTaken += 1
 
        webbrowser.open_new('http://prntscr.com/7u3wh9')
 
        if self.pillsTaken > self.MAX_PILLS:
                self.die('You took too many pills!')
 
        if self.pillsTaken < self.MAX_PILLS:
                print('You just took some pills!')
 
    def leave(self):
        self.die("You couldn't survive as a ginger!")
        sys.exit(1)
 
    def makeTuts(self):
        webbrowser.open_new('https://www.youtube.com/user/Giggletwist')
        print('Time to code and upload tutorials!!!')
				
    def getCrispy(self):
        print("You're getting crispy at avasquad!!!")
				
    def fakeSuicide(self):
        print("Just told all of avasquad you're gonna kill yourself! They believe it! Hahahahaha!")

    def makeChecklist(self):
        print('Just made a checklist on what to do for girls!!!')

    def stalkMatt(self):
        print("Stalking all of Matt's personal info even tho he tells you not to!")

    def bitchtoMatt(self):

        webbrowser.open_new('http://pastebin.com/4Nc6vhYS')
        print('Bitching to Matthew!')

    def subMormon(self):

        webbrowser.open_new('https://www.youtube.com/user/MormonMessages')
        print('Subscribing to the Mormons!!!')

    def workOut(self):

        webbrowser.open_new('http://prntscr.com/7u2un5')
        print('Working out and flexing dude!')

    def payKeana(self):

        webbrowser.open_new('http://prntscr.com/7u3o98')
        print("Just paid keana $1 for a kiss and a picture!")

    def suckatSmash(self):
        print('Getting your ass beat by everyone in smash!')

    def pegboardNerds(self):

        webbrowser.open_new('https://www.youtube.com/watch?v=ggqI-HH8yXc')
        print('Jamming out to Pegboard Nerds!!!')

def chandlerGUI():
    #gui
    root = Tk()
    root.title('Chandler Billman Simulator')
    root.geometry('600x400')
    root.resizable(0,0)

    #pic of the sexy beast
    #photo = PhotoImage(file='')
 
    #label = Label(image=photo)
    #label.image = photo #referencelol
    #label.pack()
 
    #take more pills button
    takePillsButton = Button(text="Take More Pills", fg="white", bg="red", width=15, command=chandlerSimulator().takePills)
    takePillsButton.pack(side='bottom', pady=15)

    #leave button
    leaveButton = Button(text="Leave", fg="white", bg="grey", width=5, command=chandlerSimulator().leave)
    leaveButton.place(x=540, y=360)
 
    #make some tuts!!! https://www.youtube.com/user/Giggletwist
    makeTutsButton = Button(text="Make Panda3d Tuts!!!", fg="white", bg="blue", width=20, command=chandlerSimulator().makeTuts)
    makeTutsButton.pack(fill=X)

    #get crispy boy
    getCrispyButton = Button(text="Get Crispy", fg="white", bg="green", width=15, command=chandlerSimulator().getCrispy)
    getCrispyButton.pack(fill=X)

    #fake suicide
    fakeSuicideButton = Button(text="Fake your Suicide!", fg="white", bg="purple", width=15, command=chandlerSimulator().fakeSuicide)
    fakeSuicideButton.pack(fill=X)

    #make check list
    makeChecklistButton = Button(text="Make a Checklist!", fg="white", bg="orange", width=15, command=chandlerSimulator().makeChecklist)
    makeChecklistButton.pack(fill=X)

    #stalks matt
    stalkMattButton = Button(text="Stalk Matt", fg="white", bg="pink", width=15, command=chandlerSimulator().stalkMatt)
    stalkMattButton.pack(fill=X)

    #bitch to matt about this LOL
    bitchtoMattButton = Button(text="Bitch to Matt about this", fg="white", bg="maroon", width=15, command=chandlerSimulator().bitchtoMatt)
    bitchtoMattButton.pack(fill=X)

    #sub to the mormon channel
    subMormonButton = Button(text="Subscribe to the Mormon Channel", fg="white", bg="dark green", width=15, command=chandlerSimulator().subMormon)
    subMormonButton.pack(fill=X)

    #work out and flex
    workOutButton = Button(text="Work out and flex!!", fg="white", bg="navy", width=15, command=chandlerSimulator().workOut)
    workOutButton.pack(fill=X)

    #pay keana for a kiss :*
    payKeanaButton = Button(text="Pay Keana for a kiss", fg="white", bg="hot pink", width=15, command=chandlerSimulator().payKeana)
    payKeanaButton.pack(fill=X)

    #suck at smash
    suckatSmashButton = Button(text="Suck at Smash", fg="white", bg="brown", width=15, command=chandlerSimulator().suckatSmash)
    suckatSmashButton.pack(fill=X)

    #listen to pegboard nerds https://www.youtube.com/watch?v=ggqI-HH8yXc
    pegboardNerdsButton = Button(text="Listen to Pegboard Nerds", fg="black", bg="yellow", width=15, command=chandlerSimulator().pegboardNerds)
    pegboardNerdsButton.pack(fill=X)

    #start the gui
    root.mainloop()

class sirSimulator(Simulator):
    MAX_ROASTS = random.randint(3, 10)

    def __init__(self):
        Simulator.__init__(self)
        self.pillsTaken = 0

    def takePills(self):
        self.pillsTaken += 1

        webbrowser.open_new('http://prntscr.com/7u3wh9')

        if self.pillsTaken > self.MAX_PILLS:
                self.die('You took too many pills!')

        if self.pillsTaken < self.MAX_PILLS:
                print('You just took some pills!')

    def leave(self):
        self.die("You couldn't survive as a ginger!")
        sys.exit(1)

    def makeTuts(self):
        webbrowser.open_new('https://www.youtube.com/user/Giggletwist')
        print('Time to code and upload tutorials!!!')

    def getCrispy(self):
        print("You're getting crispy at avasquad!!!")

    def fakeSuicide(self):
        print("Just told all of avasquad you're gonna kill yourself! They believe it! Hahahahaha!")

    def makeChecklist(self):
        print('Just made a checklist on what to do for girls!!!')

    def stalkMatt(self):
        print("Stalking all of Matt's personal info even tho he tells you not to!")

    def bitchtoMatt(self):

        webbrowser.open_new('http://pastebin.com/4Nc6vhYS')
        print('Bitching to Matthew!')

    def subMormon(self):

        webbrowser.open_new('https://www.youtube.com/user/MormonMessages')
        print('Subscribing to the Mormons!!!')

    def workOut(self):

        webbrowser.open_new('http://prntscr.com/7u2un5')
        print('Working out and flexing dude!')

    def payKeana(self):

        webbrowser.open_new('http://prntscr.com/7u3o98')
        print("Just paid keana $1 for a kiss and a picture!")

    def suckatSmash(self):
        print('Getting your ass beat by everyone in smash!')

    def pegboardNerds(self):

        webbrowser.open_new('https://www.youtube.com/watch?v=ggqI-HH8yXc')
        print('Jamming out to Pegboard Nerds!!!')

def chandlerGUI():
    #gui
    root = Tk()
    root.title('Chandler Billman Simulator')
    root.geometry('600x400')
    root.resizable(0,0)

    #pic of the sexy beast
    #photo = PhotoImage(file='')

    #label = Label(image=photo)
    #label.image = photo #referencelol
    #label.pack()

    #take more pills button
    takePillsButton = Button(text="Take More Pills", fg="white", bg="red", width=15, command=chandlerSimulator().takePills)
    takePillsButton.pack(side='bottom', pady=15)

    #leave button
    leaveButton = Button(text="Leave", fg="white", bg="grey", width=5, command=chandlerSimulator().leave)
    leaveButton.place(x=540, y=360)

    #make some tuts!!! https://www.youtube.com/user/Giggletwist
    makeTutsButton = Button(text="Make Panda3d Tuts!!!", fg="white", bg="blue", width=20, command=chandlerSimulator().makeTuts)
    makeTutsButton.pack(fill=X)

    #get crispy boy
    getCrispyButton = Button(text="Get Crispy", fg="white", bg="green", width=15, command=chandlerSimulator().getCrispy)
    getCrispyButton.pack(fill=X)

    #fake suicide
    fakeSuicideButton = Button(text="Fake your Suicide!", fg="white", bg="purple", width=15, command=chandlerSimulator().fakeSuicide)
    fakeSuicideButton.pack(fill=X)

    #make check list
    makeChecklistButton = Button(text="Make a Checklist!", fg="white", bg="orange", width=15, command=chandlerSimulator().makeChecklist)
    makeChecklistButton.pack(fill=X)

    #stalks matt
    stalkMattButton = Button(text="Stalk Matt", fg="white", bg="pink", width=15, command=chandlerSimulator().stalkMatt)
    stalkMattButton.pack(fill=X)

    #bitch to matt about this LOL
    bitchtoMattButton = Button(text="Bitch to Matt about this", fg="white", bg="maroon", width=15, command=chandlerSimulator().bitchtoMatt)
    bitchtoMattButton.pack(fill=X)

    #sub to the mormon channel
    subMormonButton = Button(text="Subscribe to the Mormon Channel", fg="white", bg="dark green", width=15, command=chandlerSimulator().subMormon)
    subMormonButton.pack(fill=X)

    #work out and flex
    workOutButton = Button(text="Work out and flex!!", fg="white", bg="navy", width=15, command=chandlerSimulator().workOut)
    workOutButton.pack(fill=X)

    #pay keana for a kiss :*
    payKeanaButton = Button(text="Pay Keana for a kiss", fg="white", bg="hot pink", width=15, command=chandlerSimulator().payKeana)
    payKeanaButton.pack(fill=X)

    #suck at smash
    suckatSmashButton = Button(text="Suck at Smash", fg="white", bg="brown", width=15, command=chandlerSimulator().suckatSmash)
    suckatSmashButton.pack(fill=X)

    #listen to pegboard nerds https://www.youtube.com/watch?v=ggqI-HH8yXc
    pegboardNerdsButton = Button(text="Listen to Pegboard Nerds", fg="black", bg="yellow", width=15, command=chandlerSimulator().pegboardNerds)
    pegboardNerdsButton.pack(fill=X)

    #start the gui
    root.mainloop()

def pickSimulator():
    simulator = raw_input('What simulator do you want to play? [ Chandler | Sir ]: ').lower().rstrip()
    if simulator == 'chandler':
        chandlerGUI()
        chandlerSimulator()
    elif simulator == 'sir':
        sirSimulator()
    else:
        print("I don't know how to simulate %s!' % simulator")
        pickSimulator()

pickSimulator()
