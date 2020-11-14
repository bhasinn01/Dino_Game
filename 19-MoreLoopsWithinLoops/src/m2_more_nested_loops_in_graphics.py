"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, Mark Hays, their colleagues, and
         Neha Bhasin.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, "Upside-down wall, Tests 1 and 2")

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------
    new_rect = rectangle.clone()
    corner1 = new_rect.get_lower_left_corner()
    corner2 = new_rect.get_upper_right_corner()
    width = new_rect.get_width()
    height = new_rect.get_height()
    for k in range(n):
        for j in range(k + 1):
            new_rect = rg.Rectangle(corner1, corner2)
            new_rect.attach_to(window)
            window.render()
            corner1.x = corner1.x + width
            corner2.x = corner2.x + width
        corner1 = rectangle.get_lower_left_corner()
        corner2 = rectangle.get_upper_right_corner()
        corner1.x = corner1.x - width * 0.5 * (k + 1)
        corner2.x = corner2.x - width * 0.5 * (k + 1)
        corner1.y = corner1.y - height * (k + 1)
        corner2.y = corner2.y - height * (k + 1)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
