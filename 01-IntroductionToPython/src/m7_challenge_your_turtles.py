"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Neha Bhasin.
"""
###############################################################################
# DONE: 1.
#   On Line 6 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#  _
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2  rg.SimpleTurtle  objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#  _
#   In this CHALLENGE problem, be creative!
#   Strive for way-cool pictures!  Abstract pictures rule!
#  _
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#  _
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

cass = rg.SimpleTurtle("circle")
cass.pen = rg.Pen("purple", 5)
cass.speed = 20
size = 300
for k in range(6):
    cass.draw_circle(100)
    cass.pen_up()
    cass.right(45)
    cass.forward(10)
    cass.left(45)
    cass.pen_down()
    size = size - 10

window.tracer(20)

sierra = rg.SimpleTurtle("square")
sierra.pen = rg.Pen("blue", 3)
sierra.backward(50)

for k in range(200):
    sierra.draw_square(100)
    sierra.left(91)
    sierra.forward(k)

window.close_on_mouse_click()
