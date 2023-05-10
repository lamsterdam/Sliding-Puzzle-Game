"""
    CS5001
    Fall 2022
    Project
    Leigh-Riane Amsterdam

    This a program that functions as a puzzle game
"""


import turtle

from game_board_class import GameBoard
from tile_placement_class import TilePlacement


def main():
    tile_placement = TilePlacement(300, 300, 98, 98)
    tile_placement.splash_screen()
    turtle.clearscreen()
    game_board = GameBoard()
    tile_placement.dialog_box()
    game_board.start_screen()
    game_board.draw_bottom_rectangle()
    game_board.draw_left_rectangle()
    game_board.draw_right_rectangle()
    game_board.get_image()

    tile_placement.create_dictionary()
    tile_placement.get_click_x()
    tile_placement.get_click_y()
    game_board.wn.onscreenclick(tile_placement.click_decision)
    turtle.done()


if __name__ == "__main__":
    main()