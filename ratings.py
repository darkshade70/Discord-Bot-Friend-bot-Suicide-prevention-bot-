ratingFile = open("ratings.txt", "r")  # Opens the rating text file
ratingInfo = ratingFile.readlines()  # Reading the lines of text file
ratingFile.close()  # Closes file
list = []


def ratingSort():
    for i in ratingInfo:  # Gets rid of the \n in textfile
        i = i[0:-1]
        i = int(i)
        list.append(i)

    list.sort()  # .sort() in python


ratingSort()
print(list)


def insertionSort(list):
    """
    Sort the value in the list from smallest value to largest value

    Attributes
    ----------
    list: str
      The list of values/numbers from the rating file
    return:
      None
    """


for i in range(1, len(list)):
    startValue = list[i]
    position = i
    while position > 0 and list[position - 1] > startValue:
        list[position] = list[position - 1]
        position = position - 1
    list[position] = startValue
insertionSort(list)


# print(averageRating)   #This will print the average rating from the list of ratings in the console


def bubbleSort(list):
    """
      uses bubble sorting to organizes the numbers from smallest value to largest value

      Attributes
      ----------
    list: str
        The list of values/numbers from the rating file
    return:
        None
    """


for j in range(len(list) - 1, 0, -1):
    for i in range(j):
        if list[i] > list[i + 1]:
            switch = list[i]
            list[i] = list[i + 1]
            list[i + 1] = switch

bubbleSort(list)
print(list)


def linearSearch(list, num):
    """
      uses linear searching to find if value/number is in the list

      Attributes
      ----------
    list: str
        The list of values/numbers from the rating file
    num: Int
        The number the user is looking to find
    """
    found = False
    for x in list:
        if x == int(num):
            found = True
            break
    if found:
        print('match found')
    if not found:
        print('no match found')


list1 = list
inp = input('Enter number to search:')
linearSearch(list1, inp)


def binarySearch(list, value):
    '''
      uses binary searches to find if selected value is apparent in the list

      Attributes
      ----------
    list: str
        The list of values/numbers from the rating file
    value: Int
        The number the user is looking to find
    '''
    firstValue = 0
    lastValue = len(list) - 1
    found = False

    while firstValue <= lastValue and not found:
        midpoint = (firstValue + lastValue) // 2
        if list[midpoint] == value:
            found = True
        else:
            if value < list[midpoint]:
                lastValue = midpoint - 1
            else:
                firstValue = midpoint + 1

    if found:
        print("Item found")
    else:
        print("Item not found")
    return found


numInput = int(input("What number do you want to find?"))
binarySearch(list, numInput)

"""
bubble sort: 
insertion sort: 0.6 seconds
python default sort: 0.6 seconds
"""
"""The default .sort() function in python is quite fast and compared tot he two sorting algorithms, insertion and
the .sort() has sort the ist the quickest. It took bout 0.6 seconds or less to sort a list of about 10000 numbers. 
In comparison it took about 12.90 seconds for bubble sort to sort through the list. This means insertion and .sort() 
was roughly 23 times faster. It's important to note my data set was not in any way, very large. It was only a list
of 10000 items in it. If the list is mostly already sorted or small insertion sorting would be a viable option.
This is a good demonstration of how effective different sorting algorithms are and
if the data was much larger, how using the type of sorting algorithm matters greatly"""

"""
The linear search goes through the list one by one in a linear fashion unlike binary search which starts
in the middle of the list. Since binary is recursive and divides the list into half, it is more efficient and sorts 
larger data quicker. If the data is already pre sorted and relatively small, than linear will be much more effective 
than binary. The binary search algorithm is faster. 
"""
