import sys
import math

### TEST FUNCTION
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

### TEST SUITE
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    #2
    print()
    print("fruit")
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    test("strawberries" in new_inventory)
    test(new_inventory["strawberries"] == 10)
    add_fruit(new_inventory, "strawberries", 25)
    test(new_inventory["strawberries"] == 35)



#1
def alphabetBreakdown(input):
    count = 0
    lower = input.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in alphabet:
        count = 0
        if str.find(lower, i):
            count = lower.count(i)
            #print(i + "\t" + str(count)) ##added if below so that values with 0 count are excluded from return list
            if count == 0:
                continue
            else:
                print(i + "\t" + str(count))

alphabetBreakdown("ThiS is String with Upper and lower case Letters")

#2
#>>> d = {"apples": 15, "bananas": 35, "grapes": 12}
#>>> d["bananas"]
#35

#>>> d["oranges"] = 20
#>>> len(d)
#4

#>>> "grapes" in d
#True

#>>> d["pears"]
#KeyError: 'pears'

#>>> d.get("pears", 0)
#0

#>>> fruits = list(d.keys())
#>>> fruits.sort()
#>>> print(fruits)
#['apples', 'bananas', 'grapes', 'oranges']

#>>> del d["apples"]
#>>> "apples" in d
#False

def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] = inventory[fruit] + quantity
    else:
        inventory[fruit] = quantity
    return True


test_suite()