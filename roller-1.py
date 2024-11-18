# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and GDie.

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import DieView 

def main():

    # create the application window
    win = GraphWin("Dice Roller", 300, 250)
    win.setBackground("lightblue")

    # Draw the interface widgets
    die1 = DieView(win, Point(100,60), 60)
    die2 = DieView(win, Point(200,60), 60)
    rollButton = Button(win, Point(150,140), 100, 30, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(150,220), 100, 30, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close 
    win.close()

            
