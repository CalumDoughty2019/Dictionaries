import sys

eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print(eng2sp)
#sys.exit(0)

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
print(eng2sp)
#sys.exit(0)

print("\n", eng2sp["two"])
#sys.exit(0)

inventory = {'apples':430, 'bananas':312, 'oranges':525, 'pears':217}
print("\n", inventory)
#sys.exit(0)

#delete
del inventory['pears'] ##delete the key
print("\n", inventory)
#sys.exit(0)

#add - no position or index, just a key
inventory['pears'] = 0
print("\n", inventory)
#sys.exit(0)

dict_length = len(inventory)
print("\nLength = ", dict_length)
#sys.exit(0)

print(inventory.keys())
print(inventory.values())
#sys.exit(0)

valid_key = "apples" in inventory.keys()
print("valid key = ", valid_key)

if "five" in inventory.keys():
    print("Key is valid")
else:
    print("Key is invalid")
#sys.exit(0)

if 525 in inventory.values():
    print("Value is valid")
else:
    print("Value is invalid")