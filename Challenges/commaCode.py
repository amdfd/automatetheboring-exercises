# This code separates items in a list by a comma and adds "and" before the last item.

commaList = ['apples', 'bananas', 'tofu', 'cats']
colorsList = ['red', 'green', 'blue', 'yellow', ['magenta', 'cyan', 'orange']] # Just playing around with lists within lists


def commaFunction(anyList): # Create a function that reads the list and adds "and" before the last item.
    result = ''
    for i in anyList:
        if i == anyList[-1]:
             result += 'and ' + i
        else:
            result += i + ', '
    
    print(result)

commaFunction(colorsList[-1])
