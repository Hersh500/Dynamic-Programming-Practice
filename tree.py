import turtle
from random import *
#penSize goes down as tree becomes thinner
def tree(branchLen,t, penSize):
	if branchLen > 5:
		t.pensize(penSize)
		turn = int(random() * 100) % 45 + 15		

		t.forward(branchLen)
		t.right(turn)
		tree(branchLen-15,t, penSize-2)
		t.left(turn * 2)
		tree(branchLen-15,t, penSize-2)
		t.right(turn)
		t.backward(branchLen)

def main():
	t = turtle.Turtle()
	myWin = turtle.Screen()
	t.left(90)
	t.up()
	t.backward(100)
	t.down()
	t.color("green")
	tree(75,t, 10)
	myWin.exitonclick()

main()


