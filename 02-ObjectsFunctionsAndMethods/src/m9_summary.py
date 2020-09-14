"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Neha Bhasin.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   Define a complete program that:
#     a.  Imports  rosegraphics
#     b.  Defines a   main   function that:
#          - Constructs a TurtleWindow.
#          - Calls the function that YOU define (see next bullet, below) TWICE
#              (with different arguments each time) to TEST your function.
#          - Asks the TurtleWindow to wait for a mouse click, then close.
#     c.  Defines another function that takes three parameters:
#             a SimpleTurtle, a string that represents a color,
#             and an integer for the distance to move (in pixels),
#         and causes the SimpleTurtle to:
#           - Move backward the given distance.
#           - Change its Pen's color to the given color.
#           - Turn left 90 degrees.
#           - Move forward twice the given distance.
#     d.  Calls main.
###############################################################################
import rosegraphics as rg
def main():
    window = rg.TurtleWindow()
    creating_turtle("turtle", "blue", 100)
    creating_turtle("square", "red", 50)
    window.close_on_mouse_click()

def creating_turtle(turtle, color, distance):
    created = rg.SimpleTurtle(turtle)
    created.backward(distance)
    created.pen = rg.Pen(color, 5)
    created.left(90)
    created.forward(distance * 2)

main()