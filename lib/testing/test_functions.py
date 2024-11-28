# In your test file (test_functions.py)
from lib.functions import greet_programmer, greet, greet_with_default, add, halve

def test_greet_programmer():
    # This function should print "Hello, programmer!"
    greet_programmer()

def test_greet():
    # Test greeting with a name
    greet("Alice")

def test_greet_with_default():
    # Test default and non-default greetings
    greet_with_default()  # Should print "Hello, programmer!"
    greet_with_default("Bob")  # Should print "Hello, Bob!"

def test_add():
    # Test adding two numbers
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_halve():
    # Test halving a number
    assert halve(10) == 5.0
    assert halve(7) == 3.5
