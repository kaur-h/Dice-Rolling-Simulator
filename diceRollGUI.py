
import Tkinter
import random

numOfDice = 0
top = Tkinter.Tk()


message = Tkinter.StringVar()
welcome = Tkinter.Label(top, text = "Welcome to the Die Rolling Simulation")
space = Tkinter.Label(top, height = 3)

numDie = Tkinter.Label(top, text = "Number of Dice to roll")
numDie.pack(side = Tkinter.LEFT)

entry = Tkinter.Entry(top, bd = 3)
entry.pack(side = Tkinter.RIGHT)

def generate_roll():
    #print(entry.get())
    numOfDice = entry.get()
    diceAmount = []
    for i in range(int(numOfDice)):
        die = random.randrange(1, 7, 1)
        diceAmount.append(die)
        text = Tkinter.Label(top, text = 'Die #' + str(i+1) + ' rolled a value of ' + str(die))
        text.pack()
    space.pack()

button = Tkinter.Button(top, text = "Go", command = generate_roll)

new = Tkinter.Button(top, text = "Roll Again", command = generate_roll)

welcome.pack()
space.pack()
button.pack()
new.pack()
space.pack()
top.mainloop()