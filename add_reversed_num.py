'''
* Question Description
You are given two lists containing integers in reverse order. You have to find the sum of the two integers
Example - Input - [4,7,1],[6,8,0,3]
         Output - [0,6,2,3]
         Since 174 + 3086 = 3260
'''

def add_two_num(l1,l2):
    # First I reversed both the input lists
    l1.reverse()
    l2.reverse()

    # Now I first converted both list items into string to join them together and get rid of the commas, then converted the output into integers to add
    num1 = int(''.join(str(x) for x in l1))
    num2 = int(''.join(str(x) for x in l2))

    # Converted the sum into string to iterate through the string
    sum = str(num1+num2)
    
    # Created an empty list to store the output
    myList = []
    
    # Appended all the digits of our solution in the list by iterating through the indices
    for digits in sum:
        myList.append(digits)

    # Again converted the strings into integer and reversed it    
    myList = list(map(int,myList))
    myList.reverse()
    return myList
