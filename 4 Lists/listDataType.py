# A list is a value that contains multiple values in an ordered sequence.
# A list begins with an opening square bracket and ends with a closing square bracket.
# A list has an index we can access.
# The enumerate() function returns the index of the item in the list and the item in the list itself. You need both the item and the item's index in the loop's block.

# append() adds an argument to the end of the list, insert() adds a value at any index in the list.
# remove() removes a value from the list, del() removes a value if you know the index from the list.

# sort() method sorts a list (only numbers or only strings) in ASCIIbetical order.
# to order a list in lower case first, use sort(key=str.lower).
# sort(reverse=True) sorts the values in reverse order.
# reverse() reverses a list.


catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) +1) +' (Or enter nothing to stop.):')
    name = input()
    if name == ' ':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are: ')
for name in catNames:
    print (' ' + name)