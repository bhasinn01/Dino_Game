"""
Permits exploration of EXPRESSIONS, e.g. 3 + (5 * 2) and "hello" + "goodbye",
and NAMES and ASSIGNMENT, e.g.    n = n + 1

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
         Neha Bhasin.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random
import math

###############################################################################
# DONE: 2.
#   Do this module while you watch the Session 2 Preparation video for
#       m1_expressions
#   Do the exercises in this module when the video says to do so.
#  _
#   After you have read and understood the above instructions,
#   mark this _TODO_ as DONE and continue to the next _TODO_.
###############################################################################

###############################################################################
# Part 1: Numbers, Arithmetic, and Precedence.
###############################################################################

###############################################################################
# DONE: 3.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program, paying close attention
#   to what gets printed.  (The video shows you how to "uncomment" statements.)
#  _
#   Then type an example of your own for each of:
#        -- subtraction
#        -- division
#   and run the program, checking that what gets printed is what you expect.
###############################################################################

print()
print("_TODO 3:")
print("4 + 8 evaluates to:   ", 4 + 8)
print("7 * 10 evaluates to:  ", 7 * 10)
print("1.53 + 8 evaluates to:", 1.53 + 8)
print("8 - 4 evaluates to:  ", 8 - 4)
print("70 / 10 evaluates to:  ", 70 / 10)

###############################################################################
# DONE: 4.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
###############################################################################

print()
print("_TODO 4:")
print("(4 + 2) * 3 evaluates to:", (4 + 2) * 3)
print("4 + (2 * 3) evaluates to:", 4 + (2 * 3))
print("4 + 2 * 3   evaluates to:", 4 + 2 * 3)
print("(4 - 2) + 3 evaluates to:", (4 - 2) + 3)
print("4 - (2 + 3) evaluates to:", 4 - (2 + 3))
print("4 - 2 + 3   evaluates to:", 4 - 2 + 3)

###############################################################################
# DONE: 5.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
###############################################################################

print()
print("_TODO 5:")
print("2 ** 10  evaluates to:", 2 ** 10)
print("10 ** 2  evaluates to:", 10 ** 2)
print("2 ** 0.5  evaluates to:", 2 ** 0.5)
print("10 ** -2  evaluates to:", 10 ** -2)
print("10 ** -0.5  evaluates to:", 10 ** -0.5, "(do you see why?")

###############################################################################
# DONE: 6.  [Do this when the video says to do so.]
#   Type some expressions of your own choosing that use combinations of:
#     -- addition, subtraction
#     -- multiplication, division
#     -- exponentiation
#   using parentheses to make clear the order of operations.
#   Then run the program, checking that what gets printed is what you expect.
#  _
#  After you feel that you understand how to do arithmetic in Python,
#  do Part 1 of the Moodle quiz (on Numbers, Arithmetic, and Precedence).
###############################################################################

print()
print("_TODO 6:")
print((55 + 2 * 3) ** 2)
print((8-2)/2)
print(2 ** (2+5))

###############################################################################
# Part 2: Exceptions: Syntax and Run-Time Errors.
###############################################################################

###############################################################################
# DONE: 7.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the syntax error.
#  _
#   Now type some other statement that causes a syntax error,
#   for example a statement that is missing a required parenthesis.
#   Run again to see the error-message from your syntax error,
#   and finally comment-out your statement to continue to the next _TODO.
###############################################################################

print()
print("_TODO 7:")
# This is crazy!  Python will make no sense of it!
# print (This is a syntax error).

###############################################################################
# DONE: 8.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed, especially the last red line.
#   Note that the error-output (in red) may (or may not) appear BEFORE the
#   ordinary output from previously executed PRINT statements.
#  _
#   Then comment-out the line that causes the run-time error.
###############################################################################

print()
print("_TODO 8:")
print("3 + 2 evaluations to:", 3 + 2)
# print("3 / 0 evaluations to:", 3 / 0)

###############################################################################
# DONE: 9.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed, especially the last red line.
#   Again note that the error-output (in red) may PRECEDE ordinary output.
#  _
#   Then comment-out the first line that causes the run-time error
#   and run the program again to see the result of running the line below it.
###############################################################################

print()
print("_TODO 9:")
# print("3 / 'hello' evaluations to:", 3 / 'hello')

###############################################################################
# DONE : 10.  [Do this when the video says to do so.]
#   Type some expressions of your own choosing that cause error messages.
#   Then run the program, paying close attention to the last line
#   of each error message (in red).
#  _
#  After you feel that you understand the basics of syntax and run-time errors,
#  do Part 2 of the Moodle quiz (on Exceptions: Syntax and Run-Time Errors).
###############################################################################

print()
print("_TODO 10:")
#PRINT("ERROR")
#print(0/0 "Do 0/0 because I have no cookies and no friends. Reference to Siri 0/0")
#print ("stuff"/ "me")

###############################################################################
# Part 3: Objects, Types, and Values.
###############################################################################

###############################################################################
# DONE: 11.  [Do this when the video says to do so.]
#   READ the following statements and PREDICT what they will produce as output.
#   Then, uncomment them and run the program, checking your predictions
#   and learning from any predictions that you got wrong
###############################################################################

print()
print("_TODO 11:")

print("The type of   482      is:", type(482))
#Guess: int
print("The type of   48.203   is:", type(48.203))
#Guess: float
print('The type of   "blah blah blah"      is:', type("blah blah blah"))
#Guess: str
print("The type of   'blah blah blah'      is:", type('blah blah blah'))
#Guess: str
print("The type of   [4, 2, 9]      is:", type([4, 2, 9]))
#Guess: list
print("The type of   (4, 2, 9)      is:", type((4, 2, 9)))
#Guess: list
print("The type of   min     is:", type(min))
#Guess: module
print("The type of   'min'   is:", type('min'))
#Guess: str
print("The type of   min(4, 6, 2, 12, 10)    is:", type(min(4, 6, 2, 12, 10)))
#Guess: float
print("The type of   min(4, 6, 2.0, 12, 10)  is:", type(min(4, 6, 2.0, 12, 10)))
#Guess: float


###############################################################################
# DONE: 12.  [Do this when the video says to do so.]
#   Type an expression that involves addition, subtraction and multiplication
#   (but NOT division, yet), using whole numbers (which are of type int).
#   Then run the program, checking that what gets printed is what you expect.
#  _
#   Next, repeat the above, but making just a single one of the numbers in
#   your expression a float, by appending a decimal point to it, like this:
#       instead of 2 (which is an int), write 2.0 (which is a float).
#  _
#  Finally, try division by uncommenting the following and then run the program,
#  paying close attention to what gets printed.  What do you notice about the
#  type that results from division, even if both arguments are  int  objects?
###############################################################################

print()
print("_TODO 12:")
print(type (2 + (5 * 6) - 7))
print(type (2 + (5.0 * 6) - 7))
print("4.2 / 2.0 evaluations to:", 4.2 / 2.0)
print("4.2 / 2   evaluations to:", 4.2 / 2)
print("4 / 2     evaluations to:", 4 / 2)
print("3 / 2     evaluations to:", 3 / 2)

###############################################################################
# DONE: 13.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#  Then try more expressions involving the   //   and   %   operators
#  until you understand what those operators do.
###############################################################################

print()
print("_TODO 13:")
print("17 // 5   evaluations to:", 17 // 5)
print("17 % 5    evaluations to:", 17 % 5)
print(15 % 3)
print (81 // 2)
print (0 // 1)
print(13 % 5)

###############################################################################
# DONE: 14.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#  Then try more expressions involving string arithmetic as needed, until you
#  understand what the  +   and   *   operators do when applied to strings.
###############################################################################

print()
print("_TODO 14:")

print("hello" + "goodbye girl")
print("big" * 20)
print(("hello " + "goodbye ") * 4)

###############################################################################
# DONE: 15.  [Do this when the video says to do so.]
#   Type a statement that prints:
#     I'm not a bug, that's right!
#   and then run the program, checking that it printed the above sentence
#   (including the punctuation exactly as written above).
#  _
#   Then repeat the above for the sentence:
#     What does "yarborough" mean?
#  _
#   Then repeat the above for the sentence:
#     I'm on "pins and needles" about '"'".
#   Hint: consider using the   +   operator as part of your solution.
#  _
#   After you feel that you understand the basics of the preceding _TODOs,
#   do Part 3 of the Moodle quiz (on Objects, Types, and Values).
###############################################################################

print()
print("_TODO 15:")
print("I'm not a bug, that's right!")
print('What does "yarborough" mean?')
print("I'm on " + '"pins and needles" about ' + "'" + '"' +"'" + '".')

###############################################################################
# Part 4: Names, Variables, and Assignment.
###############################################################################

###############################################################################
# DONE: 16.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the run-time error,
#   PREDICT what the subsequent lines will print,
#   and run again to check your predictions.
#  _
#   Finally, practice assignment as suggested by the examples below, that is:
#   choose your own names, given them values by using the assignment (=)
#   operator, and define new names by using expressions that include names
#   that you defined previously.
###############################################################################

print()
print("_TODO 16:")
first_program = "Hello, world!"
print(first_program)
#print(greeting)

greeting = "Hello, earthlings"
print(greeting)
print(first_program + (greeting * 2))

n = 3
print(first_program * n)
n = 2 * first_program
print(n + greeting)

###############################################################################
# DONE: 17.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Throughout this program, remember that error-output may (or may not)
#   PRECEDE ordinary output from previous PRINT statements.  Be sure to scroll
#   up to see if any error message (in red) appears higher up in the Console.
#  _
#   Then repeatedly:
#     -- comment-out the line that causes a run-time error
#     -- run again to see the output from the statements that follow it.
#   until you see the output from the last statement below,
#   noting its perhaps-surprising output.
#  _
#   Finally, try out your own assignment statements that yield run-time errors.
###############################################################################

print()
print("_TODO 17:")
r = 0
s = -9
#t = s / r
#y = "oops" + s
#u = math.sqrt(-2)
v = (-2) ** 0.5
print(v)
x = 0
stuff = 5
oh = -4
#print(x/0)
#print(math.sqrt(oh))
#print("wrong" - stuff )
###############################################################################
# DONE: 18.  [Do this when the video says to do so.]
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the run-time error,
#   PREDICT what the subsequent lines will print,
#   and run again to check your predictions.
###############################################################################

print()
print("_TODO 18:")
a = 45
#45 = a
b = 10
c = b + 20
b = c
print(a, b, c)

###############################################################################
# DONE: 19.  [Do this when the video says to do so.]
#   Uncomment the following and PREDICT what will get printed.
#   Then run the program, checking to see whether your prediction is correct.
###############################################################################

print()
print("_TODO 19:")
x = 5
x = x + 1
print(x)
# prediction: 6
x = x + 1
print(x)
# prediction: 7
x = x + 1
print(x)
# prediction: 8
###############################################################################
# DONE: 20.  [Do this when the video says to do so.]
#   Uncomment the following and PREDICT what will get printed.
#   (Hint: what gets printed is  NOT  75 10.)
#   Then run the program, checking to see whether your prediction is correct.
###############################################################################

print()
print("_TODO 20:")
x = 10
y = 75
x = y
y = x
print(x, y)
# prediction: 75, 75

###############################################################################
# DONE: 21.  [Do this when the video says to do so.]
#  The statements below make x and y refer to random integers between 1 and 99,
#  then prints the values of x and y.
#  _
#  Challenge: can you write statements below the following that causes the
#    values of x and y to SWAP?  For example, if the values of x and y are set
#    randomly to 40 and 33, so that the given print statement prints:  40 33
#    then your code should print:  33 40
#  _
#  Spend up to 1 minute on this challenge, typing your code and running the
#  program to try out your solution.  Then watch the solution per the video.
#  _
#  Finally, if you have not already done so, do Part 4 of the Moodle quiz
#  (on Names, Variables, and Assignment).
###############################################################################

print()
print("_TODO 22:")
x = random.randint(1, 99)
y = random.randint(1, 99)
print(x, y)
z = x
x = y
y = z
print(x, y)