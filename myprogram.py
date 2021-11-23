#myprogram.py
### EXAMPLE PYTHON MODULE
# Define some variables:
numberone = 1
age = 78
# define some functions
def printhello():
print "hello"
def timesfour(input):
print input * 4
# define a class
class house:
def __init__(self):
self.type = raw_input("What type of house? ")
self.height = raw_input("What height (in feet)? ")
self.price = raw_input("How much did it cost? ")
self.age = raw_input("How old is it (in years)? ")
def print_details(self):
print "This house is a/an " + self.height + " foot",
print self.type, "house, " + self.age, "years old and costing\
" + self.price + " dollars."