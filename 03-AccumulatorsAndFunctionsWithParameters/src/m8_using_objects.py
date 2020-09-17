"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Neha Bhasin.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    lines()
    circle_and_rectangle()
def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #     -- ANY two rg.Circle objects that meet the criteria are fine.
    #     -- File  COLORS.txt  lists all legal color-names.
    #   Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    circle = rg.Circle(rg.Point(100,150),10)
    circle.fill_color = "gold"
    circle.attach_to(window)

    circle2 = rg.Circle(rg.Point(250, 150), 100)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines, for the thicker Line):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #    -- ANY lines that meet the criteria are fine.
    #  Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the name of the relevant method
    #    and instance variables.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    line = rg.Line(rg.Point(200, 100), rg.Point(221, 200))
    line.attach_to(window)

    thick_line = rg.Line(rg.Point(100, 100), rg.Point(121, 200))
    thick_line.thickness = 10
    thick_line.attach_to(window)
    print(thick_line.get_midpoint())
    x = (thick_line.start.x + thick_line.end.x)/2
    y = (thick_line.start.y + thick_line.end.y)/2
    print(x)
    print(y)

    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle (using its INSTANCE VARIABLES):
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.  (Hint: For this, you'll need to use
         a METHOD that begins with "get".)
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function, per its green doc-string above.
    #    -- ANY objects that meet the criteria are fine.
    #  Put a statement in   main   to test this function
    #    (by calling this function).
    #   HINT: Module  m2r_using_rosegraphics  has helpful examples for this.
    #  ___
    #  IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()

    x = 180
    y = 115
    circle = rg.Circle(rg.Point(x, y), 50)
    circle.fill_color = "blue"
    circle.outline_thickness = 1
    circle.attach_to(window)
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(x)
    print(y)


    rect = rg.Rectangle(rg.Point(50, 200), rg.Point(100, 100))
    rect.outline_thickness = 1
    rect.attach_to(window)
    rex = (rect.corner_1.x + rect.corner_2.x) / 2
    rey = (rect.corner_1.y + rect.corner_2.y) / 2
    print(rect.outline_thickness)
    print(rect.fill_color)
    print(rect.get_center())
    print(rex)
    print(rey)

    window.render()
    window.close_on_mouse_click()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
