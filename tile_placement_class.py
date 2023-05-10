"""
    CS5001
    Fall 2022
    Project
    Leigh-Riane Amsterdam

    This a program that creates tiles for puzzle game and does game logic
"""
import time
import turtle
import math
import random


class TilePlacement:
    """
    TilePlacement sets creates the tiles,handles mouse clicks and swaps to determine win/loss
    """
    def __init__(self, x, y, width, height):
        """
        Function: init
        This is the constructor method of the TilePlacement class.
        Self is the tiles.
        :param x: x coordinate of the mouse click
        :param y: y coordinate of the mouse click
        :param width: width of the puzzle tiles
        :param height: height of the puzzle tiles
        """
        self.wn = turtle.Screen()
        self.turtlelist = []
        self.copy_turtlelist = []
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dictionary = {}
        self.tiles = []
        # self.visible = visible
        self.blank_index = -1  # random value to start until game starts
        self.moves = 0
        self.name = ""
        self.chances = 0
        self.puzzle_decision = "mario.puz"  # default puzzle when game starts
        self.my_otherturtle = turtle.Turtle()
        self.counter = 0

    def leader_file(self):
        """
        Function: leader_file
        This opens the leaderboard file for reading. It will be empty to start
        and later written to when a player win
        """
        self.leader = []
        with open("Leaderboard.txt", mode="r", encoding="utf8") as in_file:
            for each_leader in in_file:
                self.leader.append(each_leader.split())
                return self.leader

    def dialog_box(self):
        """
        Function: dialog_box
        This function pops up windows for user to enter name and maximum moves
        """
        self.name = turtle.textinput("CS5001 Puzzle Slide", "Your Name")
        self.chances = turtle.numinput("CS5001 Puzzle Slide Moves",
                                       "Enter the number of moves (chances) you want"
                                       "(5-200)", None, 5, 200)

    def splash_screen(self):
        """
        Function: splash_screen
        This adds the splash screen to be shown at the beginning of the game
        """
        load_image5 = turtle.Turtle()
        self.wn.addshape("Resources/splash_screen.gif")
        load_image5.shape("Resources/splash_screen.gif")
        load_image5.penup()
        load_image5.goto(60, 90)
        time.sleep(3)

    def get_data(self):
        """
        Function: get_data
        This loads in the puz file for the puzzle to be solved
        """
        self.tiles = []
        with open("mario.puz", mode="r", encoding="utf8") as in_file:
            for each_tile in in_file:
                self.tiles.append(each_tile.split())
                return self.tiles

    def create_dictionary(self):
        """
        Function: create_dictionary
        This creates a dictionary using numbers from puz file as keys and images as values.
        It also finds the blank in the dictionary and updates the index in the turtlelist
        """

        self.dictionary = {}
        # self.tiles is the puz file read into lists of lists for each line
        self.tiles = []

        with open(self.puzzle_decision, mode="r", encoding="utf8") as in_file:
            for each_tile in in_file:
                self.tiles.append(each_tile.split())

            # from the 4th nested list create a dictionary with numbers and images
            for i in range(4, len(self.tiles)):
                key = self.tiles[i][0].strip(":")
                value = self.tiles[i][1]
                self.dictionary[key] = value

            # add a check for number malformed puzzle
            if int(self.tiles[1][1]) == 16 or int(self.tiles[1][1]) == 9 or \
                    int(self.tiles[1][1]) == 4:
                try:
                    # using range in self.tiles[1][1] position get images from dictionary values
                    # create a turtlelist made up of the images from the dictionary keys
                    for i in range(int(self.tiles[1][1])):
                        self.wn.addshape(self.dictionary[str(i + 1)])
                        image = turtle.Turtle()
                        image.shape(self.dictionary[str(i + 1)])
                        image.penup()
                        # image.goto(-260 + (i % math.sqrt(int(self.tiles[1][1])) * int(self.tiles[2][1])),
                        # 245 - (int(i / math.sqrt(int(self.tiles[1][1]))) * int(self.tiles[2][1])))
                        self.turtlelist.append(image)

                        # check for the blank in the dictionary and grab the index
                        if "blank" in self.dictionary[str(i + 1)]:
                            self.blank_index = i
                            print(f" The current blank index is: {self.blank_index}")

                    self.shuffle()
                except IOError:
                    print("Error has occurred. Malformed file.")
                    with open("5001_puzzle_error.txt", mode="w", encoding="utf8") as out_file:
                        out_file.write("Error has occurred. Malformed file.")
                    load_image8 = turtle.Turtle()
                    self.wn.addshape("Resources/file_error.gif")
                    load_image8.shape("Resources/file_error.gif")
                    load_image8.penup()
                    load_image8.goto(100, 100)
                    time.sleep(3)

    def shuffle(self):
        """
        Function: shuffle
        This function creates a list of numbers for the tiles, shuffles the numbers
        and sets the image to correspond to a random number. Images then show up shuffled.
        """
        numbers = [i for i in range(0, int(self.tiles[1][1]))]
        random.shuffle(numbers)
        for i in range(len(numbers)):
            image = self.turtlelist[numbers[i]]
            image.goto(-260 + (i % math.sqrt(int(self.tiles[1][1])) * int(self.tiles[2][1])),
                       245 - (int(i / math.sqrt(int(self.tiles[1][1]))) * int(self.tiles[2][1])))

    def reset(self):
        """
        Function: reset
        This resets the turtles to their original position using ordered turtlelist of images
        """
        for i in range(int(self.tiles[1][1])):
            image = self.turtlelist[i]
            image.goto(-260 + (i % math.sqrt(int(self.tiles[1][1])) * int(self.tiles[2][1])),
                       245 - (int(i / math.sqrt(int(self.tiles[1][1]))) * int(self.tiles[2][1])))

    def quit(self):
        """
        Function: quit
        This loads in the quit button and ends the turtle window after 3 seconds
        """
        load_image4 = turtle.Turtle()
        self.wn.addshape("Resources/quitmsg.gif")
        load_image4.shape("Resources/quitmsg.gif")
        load_image4.penup()
        load_image4.goto(100, 100)
        time.sleep(3)
        turtle.bye()

    def click_button(self, x, y):
        """
        Function: click_button
        This function checks if the mouse click is within area for reset, quit, or
        load button. If within range it calls the helper functions which carry out
        those tasks
        :param x:  x coordinate of the mouse click
        :param y:  y coordinate of the mouse click
        """
        if abs(x - 75) < 40 and abs(y - (-200)) < 40:
            self.reset()
        if abs(x - 250) < 40 and abs(y -(-200)) < 27:
            self.quit()
        if abs(x - 163) < 40 and abs(y -(-200)) < 38:
            self.load_puzzle()

    def get_click_x(self):
        """
        Function: get_click_x
        This is a basic getter function for the x coordinate of mouse click
        """
        return self.x

    def get_click_y(self):
        """
        Function: get_click_y
        This is a basic getter function for the y coordinates of mouse click
        """
        return self.y

    def is_clicked(self, x, y):
        """
        Function: is_clicked
        This function determines which tile was clicked and if the blank is adjacent.
        If adjacent it makes a swap and updates moves taken, and carries out a task if
        player won or lost
        :param x: x coordinate of the mouse click
        :param y: y coordinate of the mouse click
        """

        print(f"the coordinates are {x}, {y}")
        # gets the width and height of tiles to be used in calculations
        self.width = int(self.tiles[2][1])
        self.height = int(self.tiles[2][1])

        # if the click is within this area it is a valid click for that tile
        for i in range(len(self.turtlelist)):
            # checking if clicked on a specific tile
            if abs(x - self.turtlelist[i].xcor()) < self.width / 2 and \
                    abs(y - self.turtlelist[i].ycor()) < self.height / 2:
                # checking if the blank is adjacent to left or right
                if abs(self.turtlelist[i].xcor() - self.turtlelist[self.blank_index].xcor())\
                        == int(self.tiles[2][1]):

                    # if both True, have the clicked tile go to blank position and blank to
                    # clicked tile position
                    x, y = self.turtlelist[i].xcor(), self.turtlelist[i].ycor()
                    blank_x, blank_y = self.turtlelist[self.blank_index].xcor(),\
                                       self.turtlelist[self.blank_index].ycor()
                    self.turtlelist[self.blank_index].goto(x, y)
                    self.turtlelist[i].goto(blank_x, blank_y)

                    # update self.blank_index = i
                    temp = self.turtlelist[self.blank_index]
                    self.turtlelist[self.blank_index] = self.turtlelist[i]
                    self.turtlelist[i] = temp
                    self.blank_index = i

                    # after a swap increase moves by 1
                    self.moves += 1
                    print(f"The total moves are: {self.moves}")
                    print(f" The current blank index is: {self.blank_index}")

                    self.player_moves()
                    break

                # checking if the blank is adjacent above or below
                elif abs(self.turtlelist[i].ycor() - self.turtlelist[self.blank_index].ycor())\
                        == int(self.tiles[2][1]):

                    # if both True, have the clicked tile go to blank position and blank to
                    # clicked tile position
                    x, y = self.turtlelist[i].xcor(), self.turtlelist[i].ycor()
                    blank_x, blank_y = self.turtlelist[self.blank_index].xcor(),\
                                       self.turtlelist[self.blank_index].ycor()
                    self.turtlelist[self.blank_index].goto(x, y)
                    self.turtlelist[i].goto(blank_x, blank_y)

                    # update self.blank_index = i
                    temp = self.turtlelist[self.blank_index]
                    self.turtlelist[self.blank_index] = self.turtlelist[i]
                    self.turtlelist[i] = temp
                    self.blank_index = i

                    # after a swap increase moves by 1
                    self.moves += 1
                    print(f"The total moves are: {self.moves}")
                    print(f" The current blank index is: {self.blank_index}")
                    self.player_moves()
                    break

        # if player won then write player to text file, show winner gif and end game
        if self.is_win() is True:
            with open("Leaderboard.txt", mode="w", encoding="utf8") as out_file:
                out_file.write(self.name + "," + str(self.chances))
                load_image6 = turtle.Turtle()
                self.wn.addshape("Resources/winner.gif")
                load_image6.shape("Resources/winner.gif")
                load_image6.penup()
                load_image6.goto(100, 100)
                self.leaders()
                time.sleep(6)
                turtle.bye()

        # if player lost, show lose gif and end game
        else:
            if self.moves >= self.chances:
                load_image7 = turtle.Turtle()
                self.wn.addshape("Resources/Lose.gif")
                load_image7.shape("Resources/Lose.gif")
                load_image7.penup()
                load_image7.goto(100, 100)
                time.sleep(3)
                turtle.bye()

    def is_win(self):
        """
        Function: is_win
        This function checks if the player won by using an ordered list of numbers, and the
        turtlelist of images. If the images at each index corresponding to list of numbers
        are in the correct x and y position then it returns True
        """
        numbers_ordered = [i for i in range(0, int(self.tiles[1][1]))]
        for i in range(len(numbers_ordered)):
            image = self.turtlelist[numbers_ordered[i]]
            correct_x = -260 + (i % math.sqrt(int(self.tiles[1][1])) * int(self.tiles[2][1]))
            correct_y = 245 - (int(i / math.sqrt(int(self.tiles[1][1]))) * int(self.tiles[2][1]))
            if image.pos() == (correct_x, correct_y):
                self.counter += 1
                print(f"The current count is:  {self.counter}")
        if self.counter == int(self.tiles[1][1]):
            return True

    def click_decision(self, x, y):
        """
        Function: click_decision
        This function is passed to onscreen click. It first determines if
        the mouse click occured in the puzzle or button area. After deciding
        the area, it calls the functions that handle buttons or puzzles and
        passes that helper function back to onscreenclick to capture the click
        :param x: x coordinate of the mouse click
        :param y: y coordinate of the mouse click
        """
        # check if clicked in the bottom rectangle which holds the buttons and call click button
        if x > -350 and x < 350 and y > -250 and y < -150:
            self.click_button(x, y)
        else:
            # else call is clicked which handles the puzzles
            self.is_clicked(x, y)

    def leaders(self):
        """
        Function: leaders
        This function gets the name of the winner and displays it in the leaderboard box
        """
        my_leader = str(self.name)
        turtle.clear()
        turtle.penup()
        turtle.goto(200, 200)
        turtle.write("Leaders" + my_leader, move=True, align="center", font=("Arial", 16, "normal"))

    def player_moves(self):
        """
        Function: player_moves
        This grabs the updated number of moves after each move is done in the game
        and writes it on the turtle screen in the bottom rectangle area
        """
        turtle.clear()
        turtle.penup()
        turtle.goto(-200,-200)
        my_text = str(self.moves)
        turtle.write("Player moves" + my_text, move= True, align= "center", font=("Arial", 16, "normal"))

    def load_puzzle(self):
        """
        Function: load_puzzle
        This function pops up the load puzzle box for the user to load a puzzle.
        After the puzzle is entered it updates the puzzle from the default mario,
        clears the screen and the tiles and creates a new dictionary of puzzle images.
        If file entered doesn't exist it displays the file error gif
        """
        self.puzzle_decision = turtle.textinput("Load Puzzle", "Enter the name of the puzzle you wish"
                                                               "to load. Choices are: \n"
                                                               "luigi.puz \n"
                                                               "smiley.puz \n"
                                                               "yoshi.puz \n"
                                                               "fifteen.puz \n"
                                                               "mario.puz \n")

        # Try to load in a new puzzle if it exists and erase old one
        # "Erased" the old puzzle by drawing a white box over it
        try:
            self.turtlelist.clear()
            self.tiles.clear()
            self.my_otherturtle.penup()
            self.my_otherturtle.fillcolor("white")
            self.my_otherturtle.begin_fill()
            self.my_otherturtle.goto(-320, -104)
            self.my_otherturtle.pendown()
            self.my_otherturtle.forward(410)
            self.my_otherturtle.left(90)
            self.my_otherturtle.forward(400)
            self.my_otherturtle.left(90)
            self.my_otherturtle.forward(410)
            self.my_otherturtle.left(90)
            self.my_otherturtle.forward(400)
            self.my_otherturtle.end_fill()

            # open the new puzzle file and create a dictionary for the images
            with open(self.puzzle_decision, mode="r", encoding="utf8") as in_file:
                for each_tile in in_file:
                    self.tiles.append(each_tile.split())
                self.create_dictionary()

        # if file does not exit, enter the except block and display the error gif
        except IOError:
            print("Error has occurred. File not found.")
            load_image8 = turtle.Turtle()
            self.wn.addshape("Resources/file_error.gif")
            load_image8.shape("Resources/file_error.gif")
            load_image8.penup()
            load_image8.goto(100, 100)
            time.sleep(3)
            load_image8.clear()


