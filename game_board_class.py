"""
    CS5001
    Fall 2022
    Project
    Leigh-Riane Amsterdam

    This a program that builds a gameboard for puzzles
"""

import turtle


class GameBoard:
    """
    Gameboard creates the gameboard layout of the puzzle game
    """
    def __init__(self):
        """
        Function: init
        This is the constructor method of the GameBoard class.
        Self is the game board.
        """

        # initializing the screen and the turtle
        self.wn = turtle.Screen()
        self.myturtle = turtle.Turtle()
        self.myturtle.speed(9)

    def start_screen(self):
        """
        Function: start_screen
        This function builds the turtle screen and features of the screen
        """
        # initializing/building the features of the screen
        self.wn.setup(width=970, height=635)

    def draw_bottom_rectangle(self):
        """
        Function: draw_bottom_rectangle
        This uses turtle to draw the bottom rectangle which will house the game buttons
        """
        self.myturtle.width(4)
        self.myturtle.penup()
        self.myturtle.sety(-250)
        self.myturtle.setx(-350)
        self.myturtle.pendown()
        self.myturtle.forward(700)
        self.myturtle.left(90)
        self.myturtle.forward(100)
        self.myturtle.left(90)
        self.myturtle.forward(700)
        self.myturtle.left(90)
        self.myturtle.forward(100)

    def draw_left_rectangle(self):
        """
        Function: draw_left_rectangle
        This uses turtle to draw the left rectangle which will house the puzzle tiles
        """
        self.myturtle.width(4)
        self.myturtle.penup()
        self.myturtle.sety(300)
        self.myturtle.setx(-350)
        self.myturtle.pendown()
        self.myturtle.forward(410)
        self.myturtle.left(90)
        self.myturtle.forward(460)
        self.myturtle.left(90)
        self.myturtle.forward(410)
        self.myturtle.left(90)
        self.myturtle.forward(460)

    def draw_right_rectangle(self):
        """
        Function: draw_right_rectangle
        This uses turtle to draw the right rectangle which will house the leaders
        """
        self.myturtle.width(4)
        self.myturtle.pencolor("blue")
        self.myturtle.penup()
        self.myturtle.sety(300)
        self.myturtle.setx(340)
        self.myturtle.pendown()
        self.myturtle.forward(210)
        self.myturtle.left(90)
        self.myturtle.forward(410)
        self.myturtle.left(90)
        self.myturtle.forward(210)
        self.myturtle.left(90)
        self.myturtle.forward(410)

    def get_image(self):
        """
        Function: get_image
        This function adds the reset, load and quit button to the gameboard
        """
        # get the reset button
        load_image = turtle.Turtle()
        self.wn.addshape("Resources/resetbutton.gif")
        load_image.shape("Resources/resetbutton.gif")
        load_image.penup()
        load_image.goto(75, -200)

        # get the load button
        load_image2 = turtle.Turtle()
        self.wn.addshape("Resources/loadbutton.gif")
        load_image2.shape("Resources/loadbutton.gif")
        load_image2.penup()
        load_image2.goto(163, -200)

        # get the quit button
        load_image3 = turtle.Turtle()
        self.wn.addshape("Resources/quitbutton.gif")
        load_image3.shape("Resources/quitbutton.gif")
        load_image3.penup()
        load_image3.goto(250, -200)

